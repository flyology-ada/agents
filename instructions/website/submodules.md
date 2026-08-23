# Website dependencies

- Before website work, inspect `.gitmodules` and the relevant build script.
- If `vendor/website-kit` is uninitialized, run
  `git submodule update --init --recursive vendor/website-kit` to materialize
  the repository's pinned revision.
- Do not use `git submodule update --remote`, change a gitlink, or select a new
  website-kit revision without explicit user authorization.
- Read the pinned website-kit instructions and scripts before writing or
  changing generated site infrastructure.
- Change project-authored content in the project. Change shared templates,
  generators, or behavior in website-kit and update the consumer gitlink only
  through a separately reviewable dependency change.
