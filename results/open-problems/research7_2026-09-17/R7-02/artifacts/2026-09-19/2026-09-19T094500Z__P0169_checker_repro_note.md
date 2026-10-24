Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0169 boundary-checker reproducibility note

During exact-SHA delivery readback, I noticed a presentation mismatch: the first archived output file recorded the diagnostic field `triangular_prefixes_checked 223104`, while the first committed checker computed the same exhaustive loops but did not print that counter. This does not affect the mathematical verdict, but the output was not byte-reproducible from that exact checker source as committed.

To preserve immutability rather than overwrite either file, I added an instrumented checker with the same exact enumeration and explicit prefix counter:

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_degree5_12var_boundary_impossibility_repro.py`

and its executed output:

`research7_2026-09-17/R7-02/artifacts/2026-09-19/p0169_degree5_12var_boundary_impossibility_repro.out`.

The instrumented checker asserts exactly `223104` prefixes for each target mean and zero surviving necessary profiles for both `+3/16` and `-3/16`, then ends `ASSERTIONS_PASS`. All arithmetic remains integer/Fraction with no floating point. The theorem and the immutable run report are unchanged; this note only repairs the audit trail for exact source/output reproducibility.
