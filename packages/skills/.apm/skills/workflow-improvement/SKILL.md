---
name: workflow-improvement
description: Find and validate a cheaper, more deterministic path through a current goal when execution has become repetitive, manual, failure-prone, or disproportionately costly. Use when routine work is fumbling or stalled and a tool, script, batching strategy, existing workflow, or reframing could unlock a completion criterion. Do not use for productive one-off work or speculative optimization detached from the active goal.
license: Apache-2.0
metadata:
  version: "0.1.0"
---

# Improve the path to the goal

Improve how the current goal is reached without expanding what the user asked
to accomplish. The primary agent owns the decision and remains responsible for
the goal.

## Qualify the opportunity

Name the blocked completion criterion, the current method, and concrete
evidence of waste such as repeated attempts, manual transformations, avoidable
serial work, nondeterministic failures, or weak evidence relative to cost. Set
a small investigation budget and stopping condition. Continue the current
method when it is already bounded and an improvement is unlikely to repay its
investigation and adoption cost within the active goal.

## Scout independently

When subagents are available and the expected savings exceed their coordination
cost, delegate one bounded scouting task. Give the scout the bottleneck,
relevant artifacts, constraints, evidence required, and stopping condition,
but do not prescribe a favored solution. Ask it to:

- inspect maintained scripts, documentation, tools, and existing automation;
- generate a small ranked set of alternatives, including keeping the current
  method;
- identify the smallest representative spike for the strongest candidates;
- estimate setup cost, recurring cost, reliability, scope, and tradeoffs;
- when the spike authority gate below is satisfied, run the smallest safe
  baseline and candidate comparison and report its artifacts and results.

The primary agent may continue nonconflicting goal work while scouting runs.
Do not delegate the adoption decision or allow the scout to mutate shared or
external state merely to test an idea.

## Spike and compare

Before any primary agent or subagent runs a spike, confirm that the spike itself
stays within existing authorization. It must not add a dependency, persist a
shared workflow change, mutate external state, incur material external cost,
widen scope, select externally visible behavior, or trade away quality or
assurance. If useful measurement requires any of those, use existing evidence,
a read-only simulation, or ask the user before running it.

Test only the smallest viable candidates on the same representative slice as
the current method, using disposable artifacts and read-only probes where
possible. First verify that each candidate preserves correctness, required
output, and required assurance; these are gates rather than optimization
dimensions. Then compare the baseline and candidate using dimensions that
matter to the goal, such as commands or manual decisions required, elapsed
time, retries, determinism, coverage, and quality of evidence. Prefer stable
work-unit counts over noisy timing when elapsed time is not a credible
comparison.

Reject a candidate when its setup, validation, or ongoing complexity consumes
the expected gain, when it changes the required output or assurance, or when
the spike cannot distinguish it from the baseline. Stop after one bounded
round unless new evidence makes another round likely to change the decision.

## Adopt or ask

Change course only when the comparison shows a material net benefit within the
current goal. Adopt the candidate directly when the change is reversible,
stays within existing authorization, preserves required output and evidence,
and introduces no new dependency, persistent shared workflow, external
mutation, or meaningful quality, compatibility, cost, or resource tradeoff.
Re-run the representative step and its relevant downstream check after
adoption.

When a candidate has demonstrated a material net benefit but adoption would add
a dependency, persist new repository or team automation, affect external state,
widen scope, select externally visible behavior, or trade assurance or quality
for speed or cost, present the evidence and ask the user one focused question.
Describe the current method, measured candidate, practical benefit, adoption
cost, and what remains unchanged.

If no candidate demonstrates a material net benefit, resume the best current
path and record the result briefly so the same unsupported optimization is not
repeated. Remove disposable spike artifacts unless they are needed as evidence.
