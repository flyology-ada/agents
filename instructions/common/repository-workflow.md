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
