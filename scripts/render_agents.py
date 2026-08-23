#!/usr/bin/env python3
"""Expand Claude-compatible standalone @ imports into a Codex AGENTS.md."""

from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
from pathlib import Path


# Claude Code permits four import hops. CLAUDE.md consumes one hop by importing
# AGENTS.sources.md, leaving three recursive hops inside the source manifest.
CLAUDE_IMPORT_HOPS = 4
SOURCE_IMPORT_HOPS = CLAUDE_IMPORT_HOPS - 1
IMPORT_LINE = re.compile(r"^\s*@([^\s`]+)\s*$")
FENCE_LINE = re.compile(r"^\s*(```|~~~)")


class RenderError(RuntimeError):
    """The instruction graph cannot be rendered safely."""


def _inside_root(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def render(source: Path, root: Path) -> tuple[str, list[Path]]:
    """Render source and return its text plus ordered contributing files."""

    root = root.resolve()
    source = source.resolve()
    if not _inside_root(source, root):
        raise RenderError(f"source is outside repository root: {source}")

    ordered: list[Path] = []
    seen: set[Path] = set()

    def expand(path: Path, depth: int, stack: tuple[Path, ...]) -> str:
        path = path.resolve()
        if depth > SOURCE_IMPORT_HOPS:
            chain = " -> ".join(str(item) for item in (*stack, path))
            raise RenderError(
                f"instruction imports exceed Claude's {CLAUDE_IMPORT_HOPS}-hop "
                f"limit after CLAUDE.md: {chain}"
            )
        if path in stack:
            chain = " -> ".join(str(item) for item in (*stack, path))
            raise RenderError(f"instruction import cycle: {chain}")
        if not _inside_root(path, root):
            raise RenderError(f"import escapes repository root: {path}")
        if not path.is_file():
            raise RenderError(f"missing instruction import: {path}")
        if path not in seen:
            ordered.append(path)
            seen.add(path)

        lines = path.read_text(encoding="utf-8").splitlines()
        chunks: list[str] = []
        in_fence = False
        fence_marker = ""
        literal: list[str] = []

        def flush_literal() -> None:
            if literal:
                chunks.append("\n".join(literal).rstrip())
                literal.clear()

        for line in lines:
            fence = FENCE_LINE.match(line)
            if fence:
                marker = fence.group(1)
                if not in_fence:
                    in_fence = True
                    fence_marker = marker
                elif marker == fence_marker:
                    in_fence = False
                    fence_marker = ""
                literal.append(line)
                continue

            match = None if in_fence else IMPORT_LINE.match(line)
            if match:
                flush_literal()
                raw_import = match.group(1)
                if raw_import.startswith(("/", "~")):
                    raise RenderError(
                        f"only repository-relative imports are allowed: {raw_import}"
                    )
                imported = path.parent.joinpath(raw_import)
                chunks.append(expand(imported, depth + 1, (*stack, path)).rstrip())
            else:
                literal.append(line)
        flush_literal()
        return "\n\n".join(chunk for chunk in chunks if chunk).rstrip() + "\n"

    return expand(source, 0, ()), ordered


def generated_text(source: Path, root: Path) -> tuple[str, list[Path]]:
    body, ordered = render(source, root)
    relative_source = source.resolve().relative_to(root.resolve())
    header = (
        "<!-- Generated from "
        f"{relative_source.as_posix()} by scripts/render_agents.py. "
        "Do not edit AGENTS.md directly. -->\n\n"
    )
    return header + body, ordered


def write_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", dir=path.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as output:
            output.write(text)
        temporary.replace(path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--root",
        type=Path,
        help="repository root; defaults to the source file's parent",
    )
    parser.add_argument(
        "--check", action="store_true", help="fail if output is missing or stale"
    )
    parser.add_argument(
        "--list-sources", action="store_true", help="print contributing files"
    )
    return parser.parse_args()


def main() -> int:
    arguments = parse_args()
    source = arguments.source.resolve()
    root = (arguments.root or source.parent).resolve()
    output = arguments.output.resolve()
    try:
        text, sources = generated_text(source, root)
    except (OSError, UnicodeError, RenderError) as error:
        print(f"render-agents: {error}", file=sys.stderr)
        return 2

    if arguments.list_sources:
        for item in sources:
            print(item.relative_to(root).as_posix())

    if arguments.check:
        try:
            existing = output.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"render-agents: missing generated file: {output}", file=sys.stderr)
            return 1
        if existing != text:
            print(f"render-agents: stale generated file: {output}", file=sys.stderr)
            return 1
        return 0


    write_atomic(output, text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
