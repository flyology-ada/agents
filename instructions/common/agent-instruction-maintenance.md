# Agent instruction maintenance

- Keep reusable instructions in focused files under `instructions/`.
- Use a profile only to compose modules with standalone `@path` lines.
- Keep project-specific implementation invariants with the repository and code
  they govern unless several repositories share the same contract.
- Put always-applicable constraints in instruction modules. Put specialized,
  multi-step workflows and deep review procedures in skills.
- Keep portable skill frontmatter to `name`, `description`, `license`,
  `compatibility`, `metadata`, and `allowed-tools`.
- Do not duplicate a skill for Codex and Claude. Consumers expose one canonical
  directory through their respective discovery paths.
- Regenerate `AGENTS.md` after changing a referenced instruction or profile.
- Validate both explicit and implicit skill activation in fresh Codex and
  Claude sessions before proposing a consumer pull request.
