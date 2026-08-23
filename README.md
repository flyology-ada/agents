# Flyology agent resources

This repository contains reusable agent instructions and Ada development
skills for repositories in the `flyology-ada` organization.

Instruction modules are composed with Claude Code-compatible `@path` imports.
Codex does not expand those imports, so `scripts/render_agents.py` produces a
checked-in `AGENTS.md` from the same source manifest.

Skills use the open Agent Skills layout. A consuming repository selects skills
by symlinking their directories into `.agents/skills/`, then exposes the same
selection to Claude Code with:

```sh
ln -s ../.agents/skills .claude/skills
```

Code-coupled skills that apply to only one consumer may live directly under
that consumer's `.agents/skills/`. The `.claude/skills` directory still links
to the complete selection. Shared workflows remain symlinks to this repository
instead of being copied into consumers.

The shared repository is normally included as `vendor/agents`:

```sh
git submodule add https://github.com/flyology-ada/agents.git vendor/agents
```

After cloning a consumer or creating a worktree, initialize the pinned agents
submodule before starting Codex or Claude:

```sh
git submodule update --init --recursive vendor/agents
```

Skill discovery happens when a client session starts. If the client was
already running while the skill symlinks were broken, start a fresh session
after initialization.

Create `AGENTS.sources.md` in the consumer with the required `@` imports, put
`@AGENTS.sources.md` in `CLAUDE.md`, and render the Codex file:

```sh
python3 vendor/agents/scripts/render_agents.py AGENTS.sources.md AGENTS.md
```

Run `python3 scripts/validate.py` in this repository before publishing an
agents revision. Consumer repositories should run:

```sh
python3 vendor/agents/scripts/validate_consumer.py .
```

This checks every consumer `AGENTS.sources.md` against its generated
`AGENTS.md`, each Claude entry point, and both clients' symlinked skill
selection.

## Adapted skills

The `alire`, `gnatdoc`, `gnatprove`, and `gnattest` skills are adapted from
`AdaCore/skills` at revision
`ab0360b0adcb0c0831bc2836aaa4d4bcfdc9cf74`. GNATfuzz content is intentionally
not included because that tool is not available in the target environments.
See `NOTICE` and the source metadata in each adapted `SKILL.md`.
