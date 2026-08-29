---
description: Apply shared source and documentation conventions to Ada changes.
---

# Ada source style

- Prefer Ada for implementation. Use a native bridge only for ABI facts or
  mechanisms that direct Ada imports cannot express reliably.
- Keep policy, validation, retry behavior, ownership, and cleanup decisions in
  Ada when Ada can express them.
- Preserve the owning project's formatting and warning configuration.
- Treat formatting as bounded hygiene, not an independent assurance campaign.
  After editing handwritten Ada, run the repository's maintained formatter at
  most once before the required tests, and run at most one maintained format
  check, only when the formatter is already provisioned. Do not install,
  upgrade, debug, or independently test byte-for-byte formatter idempotence
  unless formatter behavior or reproducible output is explicitly in scope.
  Report an unavailable or failing formatter; treat it as blocking only when an
  established CI or release gate requires it.
- Change a generator instead of formatting generated Ada independently.
- Do not hand-edit generated sources. Identify their generator and regenerate
  them through the maintained workflow.
- Preserve parameter modes, ownership, exceptions, bounds, and representation
  semantics when refactoring an interface.
