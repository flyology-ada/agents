# Documentation review

Run a technical review whenever prose changes a capability, limit, ownership
rule, timing fact, lifecycle boundary, compatibility statement, performance
claim, or experimental qualification, even for a small edit.

Treat a rewrite of three or more pages as broad unless the repository defines a
stricter trigger. For a broad rewrite, perform separate editorial, technical,
and controlled-language reviews on a stable draft. Use independent read-only
reviewers only when they are authorized and available. Reviewers report
findings and do not edit the same checkout concurrently. If separate reviewers
are unavailable, perform and label the three reviews in sequence.

Each finding identifies its severity, exact location, relevant wording,
violated rule, and proposed correction. A technical finding also names its
supporting implementation, script, contract, test, qualification artifact, or
invariant.

## Editorial review

Check headings, paragraph order, cadence, transitions, cognitive load,
mechanical sentence splitting, repeated openings, and list structure. Check
that examples explain why one step follows another. For a journal, preserve a
candid, personable voice without adding a persona or decorative story.

## Technical review

Compare prose with earlier text, maintained code, scripts, contracts, tests,
and qualification evidence. Check API links, conditions, ownership,
exceptions, timing, lifecycle, concurrency, modal verbs, compatibility, and
the strength of claims. Executable code and maintained scripts are stronger
evidence than earlier prose.

## Controlled-language review

Check one term per concept, clear actors and references,
condition-before-action order, direct headings, concrete verbs, sentence
structure, and excessive splitting without forcing unnatural prose.
Distinguish instructions and warnings from explanatory examples; apply the
tighter length signals to the former, not mechanically to the latter.

Resolve technical findings first. Re-run a targeted technical review for any
factual passage changed while reconciling style findings. Address each finding
or record why retained wording is more accurate. Review metadata, navigation
labels, callouts, captions, SVG accessibility text, code comments, redirects,
and body text.
