<!-- Generated from AGENTS.sources.md by scripts/render_agents.py. Do not edit AGENTS.md directly. -->

# Repository workflow

- Run `git status --short --branch` before changing anything.
- Preserve unrelated user changes. Do not rewrite, discard, or reformat them.
- Read the relevant implementation and maintained scripts before relying on
  README prose.
- Use `rg` or `rg --files` for discovery and `apply_patch` for hand edits.
- Keep changes focused on the requested problem.
- Run the repository's documented checks and `git diff --check` before
  presenting a change.
- Do not claim behavior, portability, proof, test coverage, or performance
  beyond evidence from maintained code, scripts, proof runs, tests, or
  benchmarks.
- Use `gh` outside a sandbox when GitHub access is required.

# Decision authority

- Authorization to implement a feature does not authorize the agent to invent
  externally visible policy, limits, defaults, compatibility promises, or
  resource budgets.
- Derive a choice from an existing contract when the repository clearly
  establishes it. Otherwise present the viable choices and ask the user.
- Ask before adding a dependency or changing a submodule revision unless the
  user already authorized that exact dependency change.
- Distinguish materializing a pinned dependency from selecting a new revision.
- Record the authority for externally mandated protocol, ABI, file-format, or
  mathematical values near their declaration or validation.

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

# Commits

Keep each commit focused on one problem. Use this message structure:

```text
Problem: <one-line problem statement in the present tense>

<Who is affected, what goes wrong, where it happens, and the impact.>

Solution: <one-line solution statement>

<What changed and why.>
```

State the problem independently of its solution. Give a future maintainer
enough repository context to understand the change without the originating
conversation.
