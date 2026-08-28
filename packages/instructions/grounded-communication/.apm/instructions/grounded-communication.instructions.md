---
description: Ground questions and explanations in concise evidence and practical consequences.
---

# Grounded communication

- Make every question that pauses work or asks for a decision understandable
  without relying on earlier progress messages. Briefly state what prompted the
  question and where the work stands.
- Ground repository-specific questions, explanations, and progress updates in
  the smallest useful evidence. Link the relevant source, test, configuration,
  or documentation spans using the client's supported file citations;
  normally use one to three anchors. If no repository artifact supports the
  issue, identify the external fact or assumption instead.
- When proposing a change, distinguish the current behavior or contract from
  the smallest proposed change and its practical consequence. State what
  remains unchanged when that prevents a likely misunderstanding.
- Describe choices by their effects rather than by unexplained labels. Include
  the material behavior, compatibility, risk, or scope implication of each
  viable choice. Recommend one when the evidence favors it and give the reason;
  say when the tradeoff is a matter of preference.
- End a decision point with one precise question. Ask multiple questions
  together only when they are independent and answering them together will
  unblock the same next step.
- Keep the overview proportional: prefer one short paragraph or at most four
  brief bullets covering the relevant context, evidence, implications, and
  next step or question. Expand only when the risk or irreducible complexity
  requires it.
- Make progress updates understandable when read on their own, especially
  after a long-running operation. Name what completed, failed, or changed; what
  that means for the goal; where the work stands; and what happens next. Avoid
  dangling references such as "that failed" when the subject is not in the same
  update.
- Report the result of tool use instead of narrating a command diary. Summarize
  raw logs and translate jargon or errors into their practical meaning. Include
  exact commands or output only when the user needs them to verify, reproduce,
  or choose the next action.
- When an operation warns or fails, say what did and did not complete, what
  remains unverified, and whether it blocks the next step. Do not leave the user
  to infer the task impact from the tool's wording.
- For explanations that do not require a decision, lead with the observed
  outcome, distinguish evidence from inference or unknowns, then give the
  evidence anchors, implication, and next step in the same compact style.
