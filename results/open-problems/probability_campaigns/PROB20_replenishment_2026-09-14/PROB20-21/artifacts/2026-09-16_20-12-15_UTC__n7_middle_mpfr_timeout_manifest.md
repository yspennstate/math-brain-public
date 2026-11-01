# PROB20-21 n=7 middle-interval MPFR attempt — NO COVERAGE CREDIT

Purpose: rigorous adaptive Bernstein/de Casteljau verification of the Courtade–Kumar defect for the source-compressed n=7 family over the then-uncovered middle interval, using exact GMP rationals for posterior Bernstein coefficients and MPFR directed rounding for entropy logarithms.

Executed source: `2026-09-16_20-12-15_UTC__n7_middle_mpfr_timeout.cpp`.

Input convention: the checker read `/tmp/s7_reps.txt`, a locally reconstructed list of the 22,225 representatives of the exact involution `D(A)={x: complement(x) notin A}` inside the 44,315 source pair-compressed S7 family. The underlying S7 list matched the frozen SHA-256 `9caace4fb804076a20a55c2e0b9fb3e1f860a7a7629f788a9e42fe1c1e77a50d`. The representative list is deterministically reconstructible from the prior archived n=7 symmetry checker; this temporary file is not treated as a durable certificate by itself.

Observed diagnostics before the full attempt: a 20-function benchmark completed in about 1.17 s; a 100-function benchmark beginning at representative index 130 completed in about 24.2 s. Those timings are diagnostics, not mathematical coverage.

A partitioned five-process attempt to cover the complete representative list did not finish within the execution limit. The tool returned the timeout status `Command failed because it timed out.` after the long execution window. No aggregate PASS record was produced.

**Coverage credited by this artifact: NONE.** A timeout is not a proof, and the frozen dimension metric is unchanged. The checker is archived because it was executed and because its cost profile identifies direct per-node MPFR logarithms as the bottleneck. The next exact implementation should replace repeated transcendental evaluations by precomputed rigorous entropy envelopes or use analytic screens before direct subdivision.
