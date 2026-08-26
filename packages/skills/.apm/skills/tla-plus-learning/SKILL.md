---
name: tla-plus-learning
description: Refresh or deepen an agent's TLA+ knowledge for state-machine modeling, temporal logic, safety and liveness, fairness, TLC model checking and trace projection, or TLAPM/TLAPS proofs. Use when the user asks to learn or explain TLA+, or when the `tla-plus` workflow is blocked by uncertainty about the language or tools. Do not use for a routine run of an already-maintained TLA+ gate.
license: Apache-2.0
metadata:
  version: "0.1.0"
  upstream_agent_skills: "https://github.com/tlaplus/AgentSkills"
---

# TLA+ learning pack

Load only the reference needed for the current gap, then apply the repository's
`tla-plus` workflow for production work.

- For abstraction, `Init`/`Next`, stuttering, refinement, and property choice,
  read [modeling.md](references/modeling.md).
- For finite configurations, safety/liveness checks, fairness, coverage,
  negative probes, simulation, and trace projection, read
  [model-checking.md](references/model-checking.md).
- For inductive invariants, hierarchical proofs, proof kernels, and honest
  proof boundaries, read [proofs.md](references/proofs.md).
- For the primary learning corpus and existing official agent skills, read
  [resources.md](references/resources.md).

Prefer small, executable examples. State the abstraction and assumptions in
plain language before writing temporal formulas. When a concept remains
uncertain, consult the primary source linked by the relevant reference instead
of guessing from syntax.
