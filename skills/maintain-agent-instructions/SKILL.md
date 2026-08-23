---
name: maintain-agent-instructions
description: Create, extract, compose, render, validate, or migrate shared AGENTS.md and CLAUDE.md instructions and repository skills. Use for flyology-ada/agents changes, consumer submodule adoption, @ import profiles, or cross-agent discovery testing.
license: Apache-2.0
metadata:
  version: "0.1.0"
---

# Maintain shared agent resources

Separate always-on constraints from specialized workflows. Keep reusable rules
in focused instruction modules, project composition in `@` manifests, and
task-specific procedures in skills.

Use one canonical skill directory. Expose selected skills through
`.agents/skills/` for Codex and link `.claude/skills` to that selection for
Claude Code. Keep shared skill frontmatter portable across both clients.

Render `AGENTS.md` from `AGENTS.sources.md` because Codex does not expand
`@path` imports. Let Claude load the same source manifest through `CLAUDE.md`.
Do not hand-edit the generated file.

Before a consumer pull request:

- initialize the pinned agents submodule;
- validate imports, skill links, and generated output;
- start fresh Codex and Claude sessions in the consumer fork;
- test a realistic instruction-dependent task;
- test explicit and implicit activation for selected skills;
- run an unrelated negative-control prompt;
- record client versions, prompts, revisions, observed behavior, and failures;
- fix discovery or adherence failures before opening the pull request.

Keep code-coupled invariants with the repository unless several repositories
share the exact contract. Do not centralize a rule merely because its wording
looks similar.
