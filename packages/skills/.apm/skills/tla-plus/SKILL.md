---
name: tla-plus
description: Model and assure Flyology algorithms with TLA+, TLC, and TLAPM/TLAPS, including safety, liveness, fairness, termination, recovery, refinement, counterexample traces, and Ada trace-replay conformance. Use when designing or changing a multi-step, concurrent, distributed, failure-sensitive, or otherwise stateful algorithm whose required outcomes must be established beyond ordinary tests. Do not use for routine local code with no temporal or interleaving behavior.
license: Apache-2.0
metadata:
  version: "0.1.0"
---

# TLA+ assurance workflow

Use TLA+ to make the algorithm and its claims precise. Keep the model,
bounded exploration, unbounded proof kernel, executable implementation, and
trace replay connected without claiming that one artifact proves another.

If TLA+ semantics, syntax, fairness, TLC configuration, or TLAPS proof
construction is unfamiliar, first read the sibling
[`tla-plus-learning`](../tla-plus-learning/SKILL.md) skill. Return here for the
project workflow.

For a matching focused edit, also use the imported official
`tlaplus-from-source`, `tlaplus-add-variable`, or `tlaplus-split-action` skill.
Those skills perform the transformation; this workflow still governs the
assurance campaign, evidence boundaries, and Ada conformance lane.

## Adopt the shared harness

Install the CLI from a `flyology-ada/tla` checkout into a dedicated absolute
prefix:

```sh
cd /path/to/flyology-ada/tla
alr -n install --prefix /absolute/path/to/flyology-tla-install
/absolute/path/to/flyology-tla-install/bin/flyology-tla --help
```

Use the installed command rather than copying its scripts into a consumer.
Add the replay library to an Alire consumer by pointing `--use` at the same
checkout, then build the consumer:

```sh
cd /path/to/consumer
alr -n with flyology_tla --use ../relative/path/to/flyology-ada/tla
alr -n build
```

Use only the toolchain provisioning commands documented and tested by that
repository's current revision; do not reproduce download URLs, hashes, Java
selection, TLAPS platform policy, or an unvalidated provisioning command in
the consumer.

After TLC has written its JSON trace, normalize and validate it through the
installed command. Supply campaign-specific resource limits explicitly:

```sh
/absolute/path/to/flyology-tla-install/bin/flyology-tla trace normalize \
  /path/to/raw.json /path/to/trace.json Module Module.cfg SOURCE_SHA256 \
  TOOLCHAIN_ID MAX_STEPS MAX_JSON_DEPTH
/absolute/path/to/flyology-tla-install/bin/flyology-tla trace validate \
  /path/to/trace.json MAX_STEPS MAX_JSON_DEPTH
```

For Ada replay, extend `Flyology_TLA.Replay.Adapter`, implement `Reset` and
`Apply`, load the trace with explicit `Flyology_TLA.Traces.Load_Limits`, and
call `Flyology_TLA.Replay.Run`. The default comparison is structural JSON
equality: whitespace, object member order, and equivalent string escape
spellings are ignored; array order is significant; number token spelling is
exact. The same caller limits govern JSON returned by the adapter. Override
comparison only for a justified domain projection or relation.

When building a consumer conformance executable, read
[runner-and-reporting.md](references/runner-and-reporting.md) for the reusable
command-line API, stable option grammar, result identity, reporting order, and
machine-contract boundary.

Keep any JSON implementation behind the foundation's private boundary.
Counterweave and Flyology.DB may consume this layer; the foundation must not
depend on either.

## Establish the assurance boundary

Before writing the model, record:

- the algorithmic question and the externally required outcomes;
- state and action boundaries, including failures, cancellation, crash, retry,
  recovery, and environmental interference;
- safety invariants and forbidden states;
- progress properties: reachability, deadlock/livelock freedom, starvation
  freedom, termination, and any required fairness assumptions;
- the abstraction map between modeled state/actions and Ada operations/state;
- what TLC, TLAPS, SPARK, executable tests, and trace replay will each establish
  and omit.

Ask the user before selecting a product policy, public default, compatibility
promise, resource bound, or fairness/environment assumption that the existing
contract does not determine. Model constants are qualification geometry unless
the product contract independently authorizes them.

## Build two related artifacts

Use a finite executable model for TLC and a smaller unbounded proof kernel for
TLAPS when the rich finite model is not a tractable proof object.

The TLC model should expose `Init`, named actions, `Next`, the complete variable
tuple, a type invariant, the required safety invariants, and temporal properties.
Keep action names stable and meaningful because they become trace and replay
identities. Add comments or metadata that map actions to Ada operations or
source boundaries.

The TLAPS kernel should quantify over arbitrary relevant domains rather than
reusing TLC's small bounds. Prove initialization and action-by-action
preservation of an inductive invariant. Strengthen the invariant when TLAPS
finds reachable-state assumptions that were only implicit; do not add an
unjustified axiom or finite cap merely to make a proof pass.

For termination or liveness, state the ranking/progress argument and fairness
assumptions explicitly. Prove the portion supported by the maintained TLAPS
toolchain. A bounded TLC liveness check does not establish unbounded liveness.

## Run TLC as a bounded search, not a proof

Use the repository's maintained runner and pinned `tla2tools.jar` when present.
Otherwise use the provisioning and command surface published by
`flyology-ada/tla`; do not add a second downloader or version policy to the
consumer.

For each model:

- parse it and exhaust the intended finite state graph;
- check type, safety, deadlock, and declared temporal properties;
- make fairness assumptions visible in the specification/configuration;
- require useful action coverage so an invariant cannot pass vacuously;
- add a deliberately invalid action or probe for important invariants and
  require TLC to reject it for the intended reason;
- use simulation only as supplemental exploration, never instead of exhaustive
  checking for the declared bounded model;
- retain exact tool versions, model/configuration, bounds, seed/fingerprint
  settings when relevant, state/depth results, warnings, and counterexamples.

Do not suppress TLC warnings in a qualification gate. Treat a changed state
count, depth, uncovered action, or unexpected counterexample as review input,
not as a snapshot to update mechanically.

## Run TLAPM/TLAPS as proof

Invoke the repository's maintained TLAPM wrapper against the exact reviewed
tree. Require every intended obligation to be proved and retain the tool
version plus obligation summary. Review what the theorem actually states:
proof of an abstract safety kernel does not cover byte formats, provider
behavior, resource ownership, liveness, or Ada refinement unless those appear
in the proved statement.

After the shared harness has provisioned and verified TLAPM, use its exported
binary path. A validated strict SMT invocation has this shape:

```sh
"$FLYOLOGY_TLAPM" --cache-dir /path/to/proof-cache --cleanfp --nofp \
  --strict --method smt /path/to/Proof.tla
```

Use the proof's maintained method and require a successful summary covering
every expected obligation. Do not copy a desktop-sandbox process-probe shim
into consumer setup; host-specific test compatibility is not part of the
installed toolchain contract.

Keep expensive formal tools serialized when their maintained scripts or shared
output directories require exclusive ownership. Do not rerun a completed proof
only to recover output that was already retained.

## Generate and replay implementation traces

For a model with an Ada counterpart, use `flyology-ada/tla` as the independent
lower trace-generation and replay layer. Flyology.DB and Counterweave are
downstream consumers, not dependencies of this foundation.

The conformance lane must:

- project a TLC trace through a stable `ALIAS` representation and dump JSON;
- validate a versioned artifact fail-closed before replay;
- preserve stable property, failure, action, and source identities;
- materialize deterministic replay inputs rather than reparsing human logs;
- apply each action through the Ada adapter and compare modeled versus observed
  post-transition state/outcome at every step;
- report the first divergence while retaining the complete trace;
- retain enough model/configuration/tool/seed identity to reproduce a failure;
- shrink only through model-valid choices, preserving the same property and
  stable failure identity.

Do not label a generated witness as implementation evidence until the Ada
adapter has actually replayed it. Passing replay establishes agreement for the
replayed traces; it is not a general refinement theorem.

## Close the campaign

Review the specification and implementation separately, then review their
mapping. Report a compact claim/evidence/omission table. Include exact TLC
state/depth/coverage evidence, expected negative-probe failures, TLAPS
obligations, replay trace counts and divergence status, and any fairness,
boundedness, abstraction, or implementation gaps. Never claim more than the
maintained artifacts establish.
