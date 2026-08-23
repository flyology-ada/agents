#!/usr/bin/env python3
"""Validate portable skills and generated agent instructions."""

from __future__ import annotations

import re
import os
import subprocess
import sys
from pathlib import Path

from render_agents import RenderError, generated_text, render


ROOT = Path(__file__).resolve().parent.parent
PORTABLE_FIELDS = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK = re.compile(r"\[[^]]*\]\(([^)]+\.md)(?:#[^)]+)?\)")


def frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValueError("unterminated YAML frontmatter") from error

    values: dict[str, str] = {}
    keys: list[str] = []
    for line in lines[1:end]:
        if not line or line[0].isspace():
            continue
        if ":" not in line:
            raise ValueError(f"invalid top-level frontmatter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        keys.append(key)
        values[key] = value.strip().strip('"\'')
    return values, keys


def validate_skill(skill: Path) -> list[str]:
    errors: list[str] = []
    entrypoint = skill.joinpath("SKILL.md")
    try:
        values, keys = frontmatter(entrypoint)
    except (OSError, UnicodeError, ValueError) as error:
        return [f"{entrypoint.relative_to(ROOT)}: {error}"]

    unexpected = set(keys) - PORTABLE_FIELDS
    if unexpected:
        errors.append(
            f"{entrypoint.relative_to(ROOT)}: non-portable frontmatter: "
            + ", ".join(sorted(unexpected))
        )
    if values.get("name") != skill.name:
        errors.append(
            f"{entrypoint.relative_to(ROOT)}: name must match directory {skill.name}"
        )
    if not NAME.fullmatch(skill.name):
        errors.append(f"{entrypoint.relative_to(ROOT)}: invalid skill name")
    if not values.get("description"):
        errors.append(f"{entrypoint.relative_to(ROOT)}: missing description")

    for markdown in skill.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        if "gnatfuzz" in text.casefold():
            errors.append(
                f"{markdown.relative_to(ROOT)}: GNATfuzz content is not available"
            )
        for raw_target in LINK.findall(text):
            if "://" in raw_target:
                continue
            target = markdown.parent.joinpath(raw_target)
            if not target.is_file():
                errors.append(
                    f"{markdown.relative_to(ROOT)}: missing Markdown target {raw_target}"
                )
    return errors


def main() -> int:
    errors: list[str] = []
    for skill in sorted(ROOT.joinpath("skills").iterdir()):
        if skill.is_dir():
            errors.extend(validate_skill(skill))

    try:
        expected, _ = generated_text(ROOT.joinpath("AGENTS.sources.md"), ROOT)
        actual = ROOT.joinpath("AGENTS.md").read_text(encoding="utf-8")
        if actual != expected:
            errors.append("AGENTS.md is stale; run scripts/render_agents.py")
        for profile in sorted(ROOT.joinpath("profiles").glob("*.md")):
            render(profile, ROOT)
    except (OSError, UnicodeError, RenderError) as error:
        errors.append(str(error))

    if ROOT.joinpath("CLAUDE.md").read_text(encoding="utf-8") != "@AGENTS.sources.md\n":
        errors.append("CLAUDE.md must contain only @AGENTS.sources.md")

    for discovery_path in (ROOT / ".agents" / "skills", ROOT / ".claude" / "skills"):
        if not discovery_path.is_symlink():
            errors.append(f"{discovery_path.relative_to(ROOT)} must be a symlink")
        elif Path(os.readlink(discovery_path)) != Path("../skills"):
            errors.append(
                f"{discovery_path.relative_to(ROOT)} must point to ../skills"
            )

    tests = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(ROOT / "tests")],
        cwd=ROOT,
        check=False,
    )
    if tests.returncode:
        errors.append("renderer tests failed")

    for error in errors:
        print(f"validate: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
