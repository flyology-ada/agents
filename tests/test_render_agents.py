from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from render_agents import RenderError, render


class RenderAgentsTests(unittest.TestCase):
    def workspace(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temporary = tempfile.TemporaryDirectory()
        return temporary, Path(temporary.name)

    def test_nested_relative_imports(self) -> None:
        temporary, root = self.workspace()
        with temporary:
            (root / "parts").mkdir()
            (root / "AGENTS.sources.md").write_text(
                "@parts/profile.md\n", encoding="utf-8"
            )
            (root / "parts/profile.md").write_text("@rule.md\n", encoding="utf-8")
            (root / "parts/rule.md").write_text("# Rule\n\nKeep it.\n", encoding="utf-8")
            text, sources = render(root / "AGENTS.sources.md", root)
            self.assertEqual(text, "# Rule\n\nKeep it.\n")
            self.assertEqual(len(sources), 3)

    def test_import_inside_fence_is_literal(self) -> None:
        temporary, root = self.workspace()
        with temporary:
            (root / "AGENTS.sources.md").write_text(
                "```text\n@missing.md\n```\n", encoding="utf-8"
            )
            text, _ = render(root / "AGENTS.sources.md", root)
            self.assertIn("@missing.md", text)

    def test_cycle_fails(self) -> None:
        temporary, root = self.workspace()
        with temporary:
            (root / "a.md").write_text("@b.md\n", encoding="utf-8")
            (root / "b.md").write_text("@a.md\n", encoding="utf-8")
            with self.assertRaisesRegex(RenderError, "cycle"):
                render(root / "a.md", root)

    def test_escape_fails(self) -> None:
        temporary, root = self.workspace()
        with temporary:
            outside = root.parent / f"{root.name}-outside.md"
            outside.write_text("outside\n", encoding="utf-8")
            self.addCleanup(outside.unlink, missing_ok=True)
            (root / "a.md").write_text(f"@../{outside.name}\n", encoding="utf-8")
            with self.assertRaisesRegex(RenderError, "escapes"):
                render(root / "a.md", root)


if __name__ == "__main__":
    unittest.main()
