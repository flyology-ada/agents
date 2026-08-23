#!/usr/bin/env python3
"""Expose selected shared skills to Codex and Claude without duplication."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


def ensure_link(link: Path, target: Path, check: bool) -> None:
    relative_target = Path(os.path.relpath(target, start=link.parent))
    if link.is_symlink():
        if Path(os.readlink(link)) != relative_target:
            raise RuntimeError(
                f"{link} points to {os.readlink(link)}, expected {relative_target}"
            )
        return
    if link.exists():
        raise RuntimeError(f"refusing to replace existing path: {link}")
    if check:
        raise RuntimeError(f"missing skill link: {link}")
    link.symlink_to(relative_target, target_is_directory=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("repository", type=Path)
    parser.add_argument("skills", nargs="+")
    parser.add_argument("--agents-submodule", default="vendor/agents", type=Path)
    parser.add_argument("--check", action="store_true")
    return parser.parse_args()


def main() -> int:
    arguments = parse_args()
    repository = arguments.repository.resolve()
    shared = repository.joinpath(arguments.agents_submodule, "skills")
    codex = repository.joinpath(".agents", "skills")
    claude = repository.joinpath(".claude", "skills")

    try:
        for skill in arguments.skills:
            target = shared.joinpath(skill)
            if not target.joinpath("SKILL.md").is_file():
                raise RuntimeError(f"shared skill does not exist: {skill}")
        if not arguments.check:
            codex.mkdir(parents=True, exist_ok=True)
            claude.parent.mkdir(parents=True, exist_ok=True)
        for skill in arguments.skills:
            ensure_link(codex.joinpath(skill), shared.joinpath(skill), arguments.check)
        ensure_link(claude, codex, arguments.check)
    except (OSError, RuntimeError) as error:
        print(f"link-skills: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
