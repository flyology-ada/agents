---
description: Detect task-relevant APM updates without mutating the pinned agent context.
---

# APM update awareness

- Treat the committed `apm.lock.yaml` and the instructions loaded from it as
  the authority for the current session. An available upstream update does not
  supersede that context, and checking for one does not authorize advancing a
  dependency pin.
- For substantial multi-step work in a repository whose `apm.yml` declares a
  moving remote update channel, run `apm update --dry-run` once before material
  implementation, or once after resuming if the pinned state may have changed.
  Skip the check when it already ran for the same lockfile state, the repository
  has no moving remote dependency, or the necessary network access is
  unavailable. An unavailable freshness check does not by itself block work
  under the committed context.
- When the dry run finds a candidate update, inspect only the candidate agent
  resource changes needed to judge their relevance to the active objective.
  A change is material when it would alter authorization or safety boundaries,
  required workflow or verification, task-relevant skill guidance, the current
  approach, or the completion criteria.
- If a candidate change is material, pause before the next action that depends
  on the affected guidance. Tell the user the current and candidate revisions,
  the relevant change, its practical effect on the work, and whether updating
  is recommended, then ask whether to update and restart with the new context
  or continue under the committed pin.
- Do not interrupt active work for an unchanged or immaterial update check.
  Mention an immaterial available update only at a natural handoff when it is
  useful to the requested outcome.
- Do not run the actual update, modify the lockfile or deployed resources,
  adopt the candidate guidance as current authority, or restart the task unless
  the user chooses to update. After an authorized update, use the repository's
  normal review, compile, and validation workflow and start a fresh agent
  session before relying on the new context.
