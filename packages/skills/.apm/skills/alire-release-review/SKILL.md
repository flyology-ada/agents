---
name: alire-release-review
description: Review an Ada crate for an Alire and Git release or development snapshot. Use for version changes, dependency constraints, manifests, immutable tags, rolling -dev origins, release checks, or publication readiness. Do not publish a stable version or create a tag without explicit authorization.
license: Apache-2.0
metadata:
  version: "0.2.0"
---

# Review an Alire release

Read the repository's release instructions, `alire.toml`, maintained release
scripts, recent tags, and default branch. Establish the intended crate name,
version, tag namespace, supported toolchain, and publication target from the
repository and user direction.

Classify the version before reviewing publication:

- Stable versions and every Git tag are immutable. Never replace, move, or
  reuse them.
- A semantic version ending in `-dev` may move in the Flyology Alire index to
  a newly reviewed exact source origin under the same version without
  per-move authorization. The exact source commit must already be pushed to
  GitHub, and the corresponding stable version must not have been published.
- When a new origin meets those conditions and all snapshot gates pass, move
  the `-dev` index entry to it instead of leaving the index on the superseded
  development snapshot.
- Once the corresponding stable version is published, do not create or move
  its `-dev` index entry.
- Development snapshots do not require Git tags. Do not extend this exception
  to stable versions or to any Git tag.

Check:

- manifest name and version consistency;
- development versus stable dependency constraints;
- path and Git pins that cannot be published as intended;
- build profiles, platform availability, licenses, maintainers, and source
  archive contents;
- generated files and nested test crates;
- changelog or release-note evidence;
- clean builds, tests, proofs, documentation, and repository-specific checks;
- whether the proposed tag already exists locally or remotely.

Treat every `-dev` origin move as a new development snapshot. For each
snapshot, re-run the complete applicable CI matrix, candidate release
reproduction, Alire index validation, indexed release reproduction, and a
fresh downstream resolution with no Git or path pins. Do not reuse evidence
from an earlier source origin under the same version.

Identify a development snapshot by the exact source origin commit recorded by
the index, not by a tag. Record both that exact source commit and the exact
Alire-index commit in the release record.

Separate readiness review from publication. Do not create, move, delete, or
push a tag, or publish a stable version, unless the user explicitly authorizes
that action and exact version. A qualifying `-dev` origin may roll without
per-move authorization after all snapshot gates pass; submit that index move
as part of the development-snapshot workflow.

Report blocking findings, warnings, commands and revisions checked, the exact
source and Alire-index commits, any proposed immutable tag, and the remaining
publication steps.
