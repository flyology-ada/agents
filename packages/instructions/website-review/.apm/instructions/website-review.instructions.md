---
description: Review broad documentation changes through separate editorial and technical lenses.
---

# Documentation review

For a broad rewrite, perform separate editorial, technical, and
controlled-language reviews on a stable draft. When independent reviewers are
authorized and available, give each role its own read-only reviewer. Reviewers
report findings and do not edit the same checkout concurrently.

Run a technical review whenever prose changes a capability, limit, ownership
rule, timing fact, lifecycle boundary, compatibility statement, or
experimental qualification, even for a small edit.

Each finding identifies its severity, exact location, relevant wording,
violated rule, and proposed correction. A technical finding also names its
supporting implementation, script, contract, or invariant.

The editorial review checks headings, paragraph order, cadence, transitions,
cognitive load, mechanical sentence splitting, repeated openings, and list
structure. It also checks that examples explain why one step follows another.

The technical review compares prose with earlier text, maintained code, and
scripts. It checks API links, conditions, ownership, exceptions, timing,
lifecycle, concurrency, modal verbs, and the strength of claims. Executable
code and maintained scripts are stronger evidence than earlier prose.

The controlled-language review checks one term per concept, clear actors,
condition-before-action order, concrete verbs, sentence structure, and
excessive splitting without forcing unnatural prose.

Resolve technical findings first. Re-run a targeted technical review for any
factual passage changed while reconciling style findings.

The editing agent addresses each finding or records why the retained wording
is more accurate. Review metadata, navigation labels, callouts, captions, SVG
accessibility text, code comments, redirects, and body text. If independent
reviewers are unavailable, perform and label the three reviews in sequence
instead of collapsing them into one generic pass.
