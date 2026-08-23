# Documentation review

For a broad rewrite, perform separate editorial, technical, and
controlled-language reviews on a stable draft. Reviewers report findings and
do not edit the same checkout concurrently.

Run a technical review whenever prose changes a capability, limit, ownership
rule, timing fact, lifecycle boundary, compatibility statement, or
experimental qualification, even for a small edit.

Each finding identifies its severity, location, relevant wording, violated
rule, proposed correction, and supporting implementation, script, contract,
or invariant.

The editorial review checks headings, paragraph order, cadence, transitions,
cognitive load, mechanical sentence splitting, and list structure.

The technical review compares prose with maintained code and scripts. It
checks API links, conditions, ownership, exceptions, timing, lifecycle,
concurrency, modal verbs, and the strength of claims.

The controlled-language review checks one term per concept, clear actors,
condition-before-action order, concrete verbs, sentence structure, and
excessive splitting without forcing unnatural prose.

Resolve technical findings first. Re-run a targeted technical review for any
factual passage changed while reconciling style findings.
