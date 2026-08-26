---
description: Require TLA+ assurance for Flyology algorithms whose correctness depends on temporal behavior.
---

# TLA+ assurance

- Use the `tla-plus` skill when an algorithm or protocol must establish
  nontrivial safety, reachability, liveness, fairness, starvation freedom,
  deadlock freedom, termination, recovery, idempotency, fencing, ordering, or
  refinement/equivalence properties across multiple steps or interleavings.
- Start the model before implementation when it will select externally visible
  semantics. Do not let a finite model's constants, bounds, scheduler, failure
  geometry, or fairness assumptions silently become product policy.
- For a TLA+-worthy algorithm, use both TLC bounded state exploration and
  TLAPM/TLAPS proof. One is not evidence for the other. If TLAPS cannot express
  or discharge a required property, state that boundary and do not turn a
  successful TLC run into an unbounded proof claim.
- When the model corresponds to an Ada implementation, generate stable traces
  from TLC and replay them through the shared `flyology-ada/tla` Ada harness,
  comparing modeled and observed post-transition outcomes. Treat replay as
  conformance evidence, not a refinement proof.
- TLA+ is usually unnecessary for a local wrapper, presentation change, simple
  data conversion, or straight-line computation whose full contract is more
  directly established by Ada/SPARK contracts and tests.
