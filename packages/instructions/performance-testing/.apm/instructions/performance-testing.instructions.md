---
description: Keep local performance measurements meaningful across host power states.
---

# Performance testing

- Before local performance testing on macOS or Linux, use the
  `performance-testing` skill's read-only power-profile detector when it is
  available. Otherwise use available read-only system indicators to check
  whether the host is detectably using a low-power, power-saving, or otherwise
  reduced-performance profile. Treat an unavailable or unclassifiable profile
  as unknown rather than assuming normal performance.
- When such a profile is detected, defer performance testing by default. If it
  is unclear whether performance testing is part of the current activity, ask
  the user. If it is part of the activity, tell the user about the detected
  profile and ask whether to proceed now or defer, unless the user has already
  explicitly directed you to run the performance testing under the current
  conditions.
- Record the detectable power profile with performance results. Take every
  baseline and its comparative measurements under the same power profile; if
  matching profiles cannot be established, do not present the measurements as
  a valid comparison.
