# Website integration

Inspect `.gitmodules` and the maintained site build before making a website
change. Follow the pinned dependency materialization boundary in `SKILL.md`.
The absence of a `vendor/website-kit` declaration is not permission to add one.

Read the pinned website-kit instructions and the consumer's build scripts
before changing generated-site infrastructure. Keep consumer names, prose,
navigation, metadata, styling overrides, and project policy in the consumer.
Change shared templates, generators, assets, or behavior in website-kit and
update the consumer gitlink only through a separately reviewable dependency
change.

Derive build and verification commands from maintained scripts and CI. Check
for consumer-specific API-link resolution, executable-example extraction,
GNATdoc normalization or filtering, public-unit checks, asset installation,
cache busting, generated search indexes, and final site-link validation. Run
the gates affected by the change and the repository's required aggregate site
check before completion.
