---
description: Maintain reusable agent resources as reproducible APM packages.
---

# Agent instruction maintenance

- Keep reusable instructions in focused APM instruction packages.
- Compose larger profiles as dependency-only packages.
- Keep project-specific implementation invariants with the repository and code
  they govern unless several repositories share the same contract.
- Put always-applicable constraints in instruction modules. Put specialized,
  multi-step workflows and deep review procedures in skills.
- Keep portable skill frontmatter to `name`, `description`, `license`,
  `compatibility`, `metadata`, and `allowed-tools`.
- Do not maintain separate skill source copies for Codex and Claude. Let APM
  deploy the same package to each selected target.
- Pin consumer targets in `apm.yml`, commit `apm.lock.yaml`, and use
  `apm install --frozen` for reproducible installation.
- Run `apm compile` to regenerate Codex and Claude root instruction files.
- Validate both explicit and implicit skill activation in fresh Codex and
  Claude sessions before proposing a consumer pull request.
