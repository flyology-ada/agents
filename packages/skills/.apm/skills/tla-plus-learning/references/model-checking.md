# TLC model checking

## Configure a finite question

Give TLC finite constant assignments and the exact specification and properties
to check. Start with a type invariant, required safety invariants, and deadlock
checking. Add temporal properties with their justified fairness assumptions.
Use the smallest domain that contains the interaction shape under review, then
expand it until the assurance goal and available resources are balanced.

Exhaustive checking explores the complete reachable graph for that finite
configuration. It can find a bounded counterexample; it does not prove the
property for unbounded domains. Simulation samples behaviors and is useful for
large or exploratory models, but it is weaker than exhaustive checking.

## Make the gate non-vacuous

Require action coverage for important branches. Add focused witness models to
obtain useful behaviors and negative probes that introduce a forbidden action
or mutation. A negative probe should violate the intended invariant for the
intended reason. This tests the property and runner, not just the happy model.

Treat warnings, unexpected uncovered actions, and unexplained state/depth
changes as findings. Avoid `-nowarning` in maintained qualification. Preserve
the configuration, tool version, bounds, relevant seed/fingerprint choices,
and exact result with the artifact.

## Generate stable traces

TLC supports `-dumpTrace json FILE` for an error trace. An `ALIAS` expression
can project a pair of states into a stable record, hiding model-internal detail
and exposing action names, parameters, expected observations, and source
identity for a replay consumer.

The reusable Flyology lane should validate that projection against a versioned
schema, fail closed on unknown fields/versions where the contract requires it,
and materialize deterministic replay input. Do not scrape human-formatted TLC
logs. Retain the complete original counterexample even when the report focuses
on the first divergence.

Use stable action names. Worker scheduling, set enumeration, and model changes
can affect which counterexample TLC finds, so retain all reproduction inputs
and avoid treating the incidental first trace as the only allowed behavior.

## Liveness review

For a progress property, check which actions are enabled and whether weak or
strong fairness is required. TLC can produce a lasso-shaped counterexample for
liveness. Distinguish:

- deadlock: no next action;
- livelock: actions continue without reaching the goal;
- starvation: the system progresses while one participant does not;
- termination failure: no terminating state is eventually reached.

If success depends on an environment step, state whether the environment is
assumed continuously or repeatedly willing to take it. A bounded green run is
evidence about the finite model only.

## Primary sources

- TLA+ project, [Current Tools: TLC command-line options](https://github.com/tlaplus/tlaplus/blob/master/general/docs/current-tools.md)
- TLA+ project, [Examples corpus](https://github.com/tlaplus/Examples)
- Leslie Lamport, [PlusCal Tutorial: Liveness](https://lamport.azurewebsites.net/tla/tutorial/session9.html)
