---
name: flyology-website-content
description: Write, revise, review, or build Flyology websites, including guides, architecture and support pages, journals, executable examples, generated API links, and shared website-kit integration. Use for authored website content and site builds, but not for unrelated repository documentation.
license: Apache-2.0
metadata:
  version: "0.2.0"
---

# Work on Flyology website content

Establish the consumer's local contract before editing. Read the root agent
instructions, `.gitmodules`, the maintained site build and verification
scripts, and representative nearby pages. For factual content, also read the
relevant implementation, architecture, contracts, tests, and qualification
evidence. Determine which page classes, generated API roots, link-authoring
mechanism, example verifier, and site checks actually apply. Do not infer these
from another Flyology repository.

If `.gitmodules` declares `vendor/website-kit` and its checkout is
uninitialized, materialize only its pinned revision:

```sh
git submodule update --init --recursive vendor/website-kit
```

Do not use `--remote` or change the website-kit gitlink unless the user
explicitly requests a dependency revision change.

Load only the guidance needed for the task:

- For authored technical pages and code examples, read
  [references/technical-writing.md](references/technical-writing.md).
- When the page mentions project-owned public APIs, read
  [references/api-links.md](references/api-links.md).
- For journal content, also read [references/journal.md](references/journal.md).
- For site builds, dependency materialization, or shared presentation behavior,
  read [references/integration.md](references/integration.md).
- For a factual change or broad rewrite, read
  [references/review.md](references/review.md).

Ground every technical claim in the repository's maintained code, scripts,
contracts, tests, or qualification evidence. Preserve project vocabulary,
conditions, ownership, exceptions, timing, limits, compatibility boundaries,
and experimental qualifications. Repository-local instructions remain the
authority for product semantics; this skill does not replace or generalize
them.

Keep consumer-authored content and configuration in the consumer. Change shared
templates, generators, assets, or behavior in website-kit and update a consumer
gitlink only as a separately reviewable dependency change.

Run the site build and content, example, generated-API, and link checks selected
by the repository's maintained scripts or CI. Do not substitute a generic
command for a stronger repository gate.

Report the pinned website-kit revision when present, commands run, generated
page or link evidence, and any claims that remain unverified.
