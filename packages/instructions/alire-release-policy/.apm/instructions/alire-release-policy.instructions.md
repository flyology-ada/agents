---
description: Preserve stable Alire release identity while permitting reviewed development snapshots to roll.
---

# Alire release identity

- A stable version is immutable once published, and every Git tag is immutable
  once created. Do not replace, move, or reuse either identity.
- A semantic version that ends in `-dev` may move in the Flyology Alire index
  to a newly reviewed exact source origin under the same version without
  per-move authorization, provided that exact source commit has been pushed to
  GitHub and the corresponding stable version has not been published.
- When a new source origin meets those conditions and all snapshot gates pass,
  move the `-dev` index entry to it; do not leave the index on the superseded
  development snapshot.
- Once the corresponding version without `-dev` has been published, do not
  create or move that version's `-dev` index entry.
- Treat every `-dev` origin move as a new development snapshot. Re-run the
  complete applicable CI matrix, candidate release reproduction, Alire index
  validation, indexed release reproduction, and a fresh downstream resolution
  with no Git or path pins.
- The exact source origin commit recorded by the index, not a Git tag, is the
  identity of a development snapshot. Release records must name both that
  exact source commit and the exact Alire-index commit.
- Development snapshots do not require Git tags. This permission applies only
  to qualifying `-dev` index entries and does not weaken stable-version or Git
  tag immutability.
