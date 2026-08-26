# Ada conformance runners and reporting

Use the reusable runner surface rather than giving each consumer its own trace
limits, output grammar, evidence identity, or exit-status policy.

## Command-line surface

Build a runner with `Flyology_TLA.Command_Line.Parse`, `Load`, `Report`,
`Set_Exit_Status`, `Put_Help`, and `Fail`. The stable grammar is:

```text
PROGRAM [--format terse|verbose|json] [--result-json PATH]
  [--max-file-bytes N] [--max-steps N] [--max-json-depth N]
  [--max-object-names N] [--max-name-bytes N]
  [--max-string-bytes N] [--max-value-bytes N] [--help] TRACE
```

The consuming application supplies every default field of
`Flyology_TLA.Traces.Load_Limits`; explicit limit options override individual
fields. The library publishes no universal resource defaults. Output defaults
to terse.

`Command_Line.Load` hashes the exact bytes it parses. `Command_Line.Report`
uses that retained identity for JSON stdout and any sidecar, so changing the
trace after loading cannot relabel the result. A requested sidecar is written
before stdout and must not resolve to `TRACE`; a sidecar failure must not look
like success. Call `Set_Exit_Status` after reporting. Only `Conformant` receives
a successful exit status.

## Reporting contract

Use `Flyology_TLA.Reporting.Image` and `Put` for terse or verbose diagnostics.
Their deterministic human wording is not versioned and must not be parsed as a
protocol.

Use `JSON_Image`, `Put_JSON`, or `Write_JSON` for the versioned
`flyology.tla.result/1` machine contract. JSON stdout and sidecar output must
use the same encoder and exact loaded-trace identity.

## Consumer flags

Register consumer-owned boolean switches with
`Flyology_TLA.Command_Line.Flag`, pass the array to `Parse`, and query it with
`Is_Set`. Names are strict lowercase `--long-option` flags, take no value,
must not collide with built-ins, and are rejected when repeated. Keep domain
flags such as an example's injected `--buggy` option in the consumer; do not
promote them into the reusable crate.

## Validated example shape

From `flyology-ada/tla/examples/counter/ada`, these forms exercise normal,
verbose, JSON, sidecar, and deliberately divergent reporting:

```sh
alr -n build
./bin/counter-conformance ../traces/counter.trace.json
./bin/counter-conformance --format verbose ../traces/counter.trace.json
./bin/counter-conformance --format json ../traces/counter.trace.json
./bin/counter-conformance --result-json /path/to/result.json \
  ../traces/counter.trace.json
./bin/counter-conformance --buggy --format verbose \
  ../traces/counter.trace.json
```

The divergent example must exit unsuccessfully and retain the stable first
failure identity `state:Counter!Increment`. Treat that fingerprint as example
evidence, not as a universal consumer property.
