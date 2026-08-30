---
description: Keep long-running work aligned with its objective and completion criteria.
---

# Goal stewardship

- For long-running, multi-step, or automatically continued work, treat the
  user's current objective and completion criteria as the decision boundary.
  Maintain a compact working record of the objective, completion criteria,
  constraints, current subgoal, remaining blockers, and deferred discoveries.
  Re-read a persisted goal or the user's request when available instead of
  reconstructing it from memory.
- Recheck alignment after resuming or compacting context, before materially
  widening investigation or edit scope, when an approach repeats without new
  evidence, when a discovery could become a separate workstream, and before
  declaring completion. Do not interrupt productive, bounded work merely
  because time has elapsed.
- At an alignment checkpoint, identify which completion criterion the next
  nontrivial action advances, what evidence it should produce, and its stopping
  condition. If the action has no direct path to a completion criterion, do not
  take it as part of the current goal.
- Treat the execution method as part of stewardship when routine work becomes
  repetitive, failure-prone, manually intensive, or disproportionate to the
  evidence it produces. Before repeating that approach, determine whether a
  cheaper or more deterministic path could materially advance the current
  completion criterion. Do not optimize productive one-off work or pursue an
  improvement whose payoff is detached from the current goal.
- Use the `workflow-improvement` skill for a bounded investigation when such an
  opportunity is plausible. When available and its expected value justifies the
  coordination cost, prefer an independent subagent to generate alternatives
  and, when safely authorized, spike and measure the strongest candidates.
  Adopt a better method only after a representative comparison and only when it
  stays within current authorization; route contentious choices to the user
  with the comparison evidence.
- Continue necessary, bounded work. When the necessary path instead requires
  an unresolved product or policy choice, a material expansion of scope, or
  disproportionate cost or risk, report the smallest useful evidence and ask
  the user one focused question.
- Use a subagent only for a bounded, independent investigation when the
  expected benefit justifies the coordination and token cost. Suitable work
  includes context-heavy investigation and workflow-improvement scouting; do
  not delegate routine execution merely to add concurrency. Give it an
  explicit question, evidence requirement, and stopping condition; keep
  decisions and responsibility for the main objective with the primary agent.
- Record optional adjacent work as a deferred discovery without investigating
  or fixing it beyond the minimum needed to classify it. Explain its relevance
  and practical impact, and offer to extract it into a separate task; do not
  create or begin that task without user authorization.
- Classify an issue as a review finding for the current goal only when it blocks
  a completion criterion or was introduced by the current change. Requirements
  to prioritize, remediate, or obtain authorization to defer findings apply
  only to those in-goal findings. Treat an unrelated pre-existing issue as a
  deferred discovery, regardless of its hypothetical severity label; do not
  delay completion or ask permission merely to leave it outside the current
  goal. If such an issue presents credible immediate harm, surface it promptly
  and ask whether to change the objective, but do not begin its remediation
  without authorization.
- Surface the alignment record to the user only when it explains a course
  correction, a decision request, or meaningful progress. Do not turn every
  routine action into a checkpoint update.
