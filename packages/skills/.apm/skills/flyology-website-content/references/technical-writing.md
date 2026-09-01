# Technical writing

Apply this style to authored technical pages such as guides, architecture, and
support content. Confirm the consumer's page taxonomy before assuming scope.
Do not mechanically apply it to a home page, report, generated API reference,
or other content class with a different established register.

Use the useful parts of ASD-STE100 as a house style. Do not claim compliance
with ASD-STE100.

- Use one project term for one concept. Do not add synonyms only for variety.
- Define an unfamiliar term before its first use. Keep project identifiers,
  Ada terms, protocol terms, OS interfaces, and compiler terms exact.
- Put one main idea or instruction in each sentence. Use a list when parallel
  facts would otherwise obscure the structure.
- Keep closely related cause, contrast, sequence, and consequence in the same
  paragraph. Do not split connected reasoning into abrupt statements merely to
  shorten sentences.
- Prefer sentences of 25 words or fewer and instructions of 20 words or fewer.
  Treat these lengths as review signals, not mechanical acceptance gates.
- Use active voice when the actor matters. Replace unclear pronouns with the
  responsible actor.
- Preserve modal meaning: `must` states a requirement, `can` a capability, and
  `may` a possibility.
- Use present tense for current behavior and the imperative for instructions.
- Put a prerequisite or safety condition before the action it controls.
- Use direct, sentence-case headings that state the subject or action.
- Prefer concrete verbs. Avoid promotional language, rhetorical questions,
  idioms, metaphors, personification, filler, nominalizations, and stacked
  modifiers.
- Keep limits beside the capabilities they qualify. Do not remove a condition,
  ownership rule, exception, timing fact, compatibility boundary, or
  experimental qualification to make prose shorter.
- Keep paragraphs focused, but do not split connected technical reasoning into
  unnatural fragments.

Examples and walkthroughs may use a more conversational cadence when that
helps explain why one step follows another. Commands, contracts, warnings, and
limits retain the tighter technical style. Do not add fictional scenarios,
decorative stories, or personality that does not improve understanding.

Review examples as paragraphs, not only as sentence-level scores. Combine
repeated short statements when the relationship becomes clearer, while
retaining short warnings, results, and important boundaries.

## Code examples

Inspect the site build and example-verification scripts before editing a code
sample. When the consumer verifies named regions from maintained sources, edit
the source example and retain the exact marker and byte-for-byte extraction
contract. Keep the owning example project and runner executable.

Do not write illustrative pseudocode that resembles a supported public call
when the page presents it as executable. Keep profiles, capacities, deadlines,
identities, and other policy values explicit. State when a value belongs only
to the example and is not a library default or recommendation.

Before finishing, check terminology, sentence length, HTML syntax, local links,
code examples, metadata, navigation labels, callouts, captions, SVG
accessibility text, code comments, and redirects.
