---
description: Maintain reusable agent resources as reproducible APM packages.
---

# Agent instruction maintenance

- Keep reusable instructions in focused APM instruction packages.
- Compose larger profiles as dependency-only packages.
- Keep project-specific implementation invariants with the repository and code
  they govern as local packages under `agent-packages/`, unless several
  repositories share the same contract.
- Put always-applicable constraints in instruction modules. Put specialized,
  multi-step workflows and deep review procedures in skills.
- Keep portable skill frontmatter to `name`, `description`, `license`,
  `compatibility`, `metadata`, and `allowed-tools`.
- Do not maintain separate skill source copies for Codex and Claude. Let APM
  deploy the same package to each selected target.
- Declare the intended consumer update channel in `apm.yml`, commit
  `apm.lock.yaml` as the exact revision and content pin, and use
  `apm install --frozen` for reproducible installation. Advance shared
  packages only with an explicit `apm update` and review the lockfile and
  generated output.
- Run `apm install` to deploy Claude rules and both clients' skill trees. Run
  `apm compile --target codex` to regenerate Codex `AGENTS.md` files without
  removing the installed Claude rules.
- Validate both explicit and implicit skill activation in fresh Codex and
  Claude sessions before proposing a consumer pull request.
