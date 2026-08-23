# Flyology agent packages

This repository publishes reusable Flyology instructions and Ada development
skills as [Agent Package Manager](https://microsoft.github.io/apm/) packages.
Consumers select a profile in `apm.yml`; APM resolves its instruction and skill
dependencies, records exact commits and content hashes in `apm.lock.yaml`, and
materializes the native Codex and Claude layouts.

## Consumer setup

Declare the required profile at an exact tag or commit:

```yaml
name: flyology-http-agent-context
version: 0.1.0
targets: [codex, claude]
dependencies:
  apm:
    - git: https://github.com/flyology-ada/agents.git
      path: packages/profiles/ada-library
      ref: <tag-or-commit>
```

Resolve once and commit the resulting lockfile:

```sh
apm install
apm compile
git add apm.yml apm.lock.yaml AGENTS.md .apm
```

After cloning or creating a worktree, provision the locked resources before
starting either client:

```sh
apm install --frozen
apm compile
```

Start a fresh Codex or Claude session after installation so its skill catalog
includes the deployed packages.

## Packages

- `packages/instructions/` contains independently installable instruction
  modules.
- `packages/skills/` contains the canonical portable skill bundles used by
  both clients.
- `packages/profiles/ada-library` composes the common Ada library rules and
  skills.
- `packages/profiles/flyology-website` composes website rules and skills.
- `packages/profiles/agents-repository` composes the rules for this repository.

Profiles use APM's `git: parent` dependencies so every module resolves from the
same repository commit. Direct subpackage installs and exact Git refs keep
publishing distributed; a registry is not required.

## Development

APM 0.28.0 is the validated CLI version for this revision. From the repository
root, run:

```sh
apm install
apm compile --validate
apm compile --target codex,claude --clean
apm audit --ci
```

The root manifest is also a consumer of the agents-repository profile's
components. Its compilation excludes package source directories so only the
declared dependency closure enters the generated root context.

Commit `apm.lock.yaml` and generated `AGENTS.md` files. Claude consumes the
generated `.claude/rules/` tree; both clients consume generated skill trees.
Do not commit `apm_modules/` or deployed client skill/rule trees: reproduce
them with the frozen install when creating a clone or worktree.

## Adapted skills

The `alire`, `gnatdoc`, `gnatprove`, and `gnattest` skills are adapted from
`AdaCore/skills` at revision
`ab0360b0adcb0c0831bc2836aaa4d4bcfdc9cf74`. GNATfuzz content is intentionally
not included because that tool is not available in the target environments.
See `NOTICE` and the source metadata in each adapted `SKILL.md`.
