#!/usr/bin/env python3
"""Validate a consumer repository's shared instructions and skill links."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from render_agents import generated_text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("repository", nargs="?", default=".", type=Path)
    parser.add_argument(
        "--agents-submodule", default="vendor/agents", type=Path
    )
    return parser.parse_args()


def validate(repository: Path, submodule: Path) -> list[str]:
    errors: list[str] = []
    repository = repository.resolve()
    shared = repository.joinpath(submodule).resolve()
    if not shared.joinpath("scripts", "render_agents.py").is_file():
        errors.append(f"agents submodule is not initialized: {submodule}")
        return errors

    manifests = [
        path
        for path in repository.rglob("AGENTS.sources.md")
        if not path.resolve().is_relative_to(shared)
        and ".git" not in path.relative_to(repository).parts
    ]
    if not manifests:
        errors.append("no AGENTS.sources.md manifests found")

    for source in sorted(manifests):
        output = source.with_name("AGENTS.md")
        claude = source.with_name("CLAUDE.md")
        try:
            expected, _ = generated_text(source, repository)
        except (OSError, UnicodeError, RuntimeError) as error:
            errors.append(f"cannot render {source.relative_to(repository)}: {error}")
            continue
        try:
            actual = output.read_text(encoding="utf-8")
        except FileNotFoundError:
            errors.append(f"missing generated file: {output.relative_to(repository)}")
        else:
            if actual != expected:
                errors.append(f"stale generated file: {output.relative_to(repository)}")
        try:
            claude_text = claude.read_text(encoding="utf-8")
        except FileNotFoundError:
            errors.append(f"missing Claude entry point: {claude.relative_to(repository)}")
        else:
            if claude_text != "@AGENTS.sources.md\n":
                errors.append(
                    f"unexpected Claude entry point: {claude.relative_to(repository)}"
                )

    codex_skills = repository.joinpath(".agents", "skills")
    claude_skills = repository.joinpath(".claude", "skills")
    if not codex_skills.is_dir():
        errors.append("missing Codex skill directory: .agents/skills")
    else:
        entries = sorted(codex_skills.iterdir())
        if not entries:
            errors.append("no shared skills selected in .agents/skills")
        for entry in entries:
            if not entry.is_symlink():
                if entry.is_dir() and entry.joinpath("SKILL.md").is_file():
                    continue
                errors.append(
                    "local skill is not a directory with SKILL.md: "
                    f"{entry.relative_to(repository)}"
                )
                continue
            target = entry.resolve()
            try:
                target.relative_to(shared.joinpath("skills"))
            except ValueError:
                errors.append(f"skill points outside shared skills: {entry.relative_to(repository)}")
                continue
            if not target.joinpath("SKILL.md").is_file():
                errors.append(f"skill has no SKILL.md: {entry.relative_to(repository)}")

    expected_claude_target = Path(os.path.relpath(codex_skills, claude_skills.parent))
    if not claude_skills.is_symlink():
        errors.append(".claude/skills is not a symlink")
    elif Path(os.readlink(claude_skills)) != expected_claude_target:
        errors.append(
            f".claude/skills points to {os.readlink(claude_skills)}, "
            f"expected {expected_claude_target}"
        )
    return errors


def main() -> int:
    arguments = parse_args()
    errors = validate(arguments.repository, arguments.agents_submodule)
    for error in errors:
        print(f"validate-consumer: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
