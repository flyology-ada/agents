---
name: performance-testing
description: Run or assess local performance tests on macOS or Linux while detecting power-saving profiles and keeping baseline and comparative measurements under matching power conditions.
license: Apache-2.0
metadata:
  version: "0.1.0"
---

# Test performance under comparable power profiles

Before running a local performance test, run the read-only detector from this
skill directory:

```sh
./scripts/check-power-profile.sh
```

Capture its output with the measurements. Interpret its exit status as:

- `0`: a profile was detected and is not classified as reduced-performance;
- `10`: a low-power or other reduced-performance profile was detected;
- `2`: the operating system or active profile could not be classified.

When the detector returns `10`, follow the repository's performance-testing
rule: defer by default and ask the user before proceeding when performance work
is in scope. Treat status `2` as unknown rather than assuming a normal profile.
Do not change the host's profile without separate user authorization.

Run the detector immediately before each baseline and comparative measurement.
Require matching `os`, `detector`, and `profile` values and, when
`power_source` is known, a matching source. Unknown profiles do not establish
comparability.
