---
name: ada-hardcoded-constants
description: Audit Ada specifications and bodies for constants, defaults, bounds, and literals that encode unapproved policy. Use when reviewing `.ads` or `.adb` values, questioning hard-coded choices, or deciding how a value should be represented. Report decisions and alternatives before editing; do not mechanically replace literals.
license: Apache-2.0
metadata:
  version: "0.1.0"
---

# Audit Ada values

Find values that encode design choices the user did not authorize. Begin with
specifications: an accidental value in an `.ads` file can become public API,
representation, or a reusable default.

## Scope

Inspect both explicit constant declarations and values expressed through:

- subtype, array, modular, and discriminant constraints;
- parameter, discriminant, and generic formal defaults;
- representation aspects and clauses;
- capacities, timeouts, retries, pool sizes, buffer sizes, and resource bounds;
- configuration packages, build-generated specifications, and platform units;
- magic values, versions, sentinels, protocol fields, and ABI declarations;
- body literals that control externally visible behavior.

Classify visible declarations, private-part declarations, and body-only values
separately. Exclude generated files from proposed hand edits and locate their
generator.

## Establish authority

For each consequential value, look for authority in maintained requirements,
protocol or ABI documentation, persisted-format definitions, tests, existing
configuration, type derivation, or explicit user direction. Usage alone can
show impact but does not prove the chosen value was intended.

Feature authorization does not authorize a new value or its visibility. Do not
introduce a visible constant in an `.ads` file until the user approves its
meaning, value, name, type, and public visibility.

## Evaluate alternatives

Consider whether the value should instead be:

- a private implementation detail;
- derived from an existing type, object, or external contract;
- supplied by the caller;
- a generic formal or discriminant;
- selected through build-time or runtime configuration;
- represented by an enumeration or stronger domain type;
- deliberately exposed as a public constant;
- retained as a clear mathematical, test-fixture, protocol, or ABI literal.

Do not assume a named constant is better than a literal. A name can hide an
unapproved policy choice while making it appear intentional.

## Report before changing

Present a decision table with the location, current value, visibility,
classification, evidence of authority, behavioral or compatibility impact,
alternatives, recommendation, and user decision required.

Separate findings that need decisions from harmless literals and externally
fixed values. Do not edit consequential values until the user resolves the
open decisions. After approval, implement only the selected representation and
run focused tests for the affected contract.
