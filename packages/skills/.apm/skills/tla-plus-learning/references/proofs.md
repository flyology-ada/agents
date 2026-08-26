# TLAPM and TLAPS proofs

## Prove an inductive invariant

For a safety theorem, find an inductive invariant `Inv` strong enough to imply
the desired property:

1. `Init => Inv`.
2. For every action, `Inv /\ Action => Inv'`.
3. `Inv => Safety`.

An invariant that holds in every TLC-reachable state may still be too weak for
induction because the preservation proof considers every state satisfying the
invariant. Strengthen it with the missing type, phase, ownership, or authority
relationship. Do not add an assumption that is not established by `Init` and
preserved by every action.

Use a smaller proof kernel when the executable model contains finite arithmetic,
format detail, or failure geometry irrelevant to the general theorem. Quantify
over arbitrary nonempty domains and arbitrary cycle counts where those are the
claim. Keep a written map from the finite model to the kernel and list every
omission.

## Structure proofs for review

TLAPS checks hierarchical claims and their leaf obligations. Prefer named
lemmas and explicit facts over one large backend-sensitive obligation. When a
backend cannot prove an apparently simple leaf, decompose the reasoning or make
the necessary definitions/facts usable; avoid tailoring the specification to a
particular backend tactic.

Run TLAPM through the repository's pinned wrapper and retain its exact version
and obligation count. Inspect whether there are omitted, assumed, or unchecked
claims before reporting success.

## Progress and termination

TLAPS is most mature for safety proofs. For termination, a well-founded ranking
argument may turn progress into state reasoning. Temporal liveness proofs need
fairness and proof-system support that must be checked against the maintained
toolchain. If the toolchain does not prove the temporal theorem, report the
bounded TLC result and the unproved general liveness claim separately.

## Proof boundaries

An abstract proof covers exactly its theorem. It does not automatically prove:

- the richer TLC model refines the proof kernel;
- the Ada code refines either TLA+ artifact;
- serialization, arithmetic overflow, memory ownership, or provider behavior;
- liveness, if only inductive safety was proved;
- a public resource limit represented only by finite model geometry.

Use SPARK, executable tests, provider conformance, and TLA+/Ada trace replay for
their respective boundaries. State the gaps instead of merging evidence into a
single “formally verified” label.

## Primary sources

- TLA+ Proof System, [Tutorial](https://proofs.tlapl.us/doc/web/content/Documentation/Tutorial/The_example.html)
- TLA+ Proof System, [Practical hints](https://proofs.tlapl.us/doc/web/content/Documentation/Tutorial/Practical_hints.html)
- TLA+ Proof System, [Tactics and maintainable obligations](https://proofs.tlapl.us/doc/web/content/Documentation/Tutorial/Tactics.html)
- TLA+ project, [TLAPM](https://github.com/tlaplus/tlapm)
