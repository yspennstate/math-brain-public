# HARD8-03 — 2026-09-16T07:13:09Z checkpoint receipts

This is an append-only receipt companion to

`hard8_2026-09-16/HARD8-03/runs/2026-09-16/2026-09-16T07-13-09Z__report.md`.

## GitHub receipts

- Primary mathematical report commit: `3d586649f72a30a995b8e51b63472c58dba810e9`.
- Primary report read back successfully at exactly that commit: **VERIFIED**.
- Verifier path: `hard8_2026-09-16/HARD8-03/artifacts/2026-09-16T07-13-09Z__local_cancellation_width_verifier.py`.
- Verifier commit: `3c7e3a3cfb3e3ba093df71665413eeee1e8df8a1`.
- Verifier read back successfully at exactly that commit: **VERIFIED**.
- Approval/security denial: **NOT EXPOSED**.

## Actual bounded checks completed in-session

The exact-integer/rational implementation underlying the archived verifier completed the following checks before delivery:

1. Pair-sum obstruction family `M_p`, for `p=1,...,6`:
   - exact real rank `r=p+2` in every case;
   - exact enumeration of all maximal HLS-dissociated subsets;
   - counts respectively `4,12,32,80,192,448`, matching `(p+1)2^p`;
   - every maximal set has exactly one complete equal-sum pair and one member of every other pair.
2. Rank-4 six-vector obstruction `A={3,5,6,7,11,12}`:
   - exhaustive search over all maximal dissociated subsets and all `{-1,0,1}` representations gives optimum local negative width exactly `2`;
   - one optimal basis is `{3,5,6,7,11}`, with `12=-3+5+6-7+11`.
3. Local-cancellation-width partition constructor:
   - deterministic pseudorandom seed `20260916`;
   - 30,000 generated signed rectangle systems on `4 x 5` grids;
   - 3,024 systems happened to evaluate exactly to Boolean matrices;
   - for all 3,024 accepted cases, the constructive partition covered every 1-cell exactly once, every 0-cell zero times, and respected the theorem's explicit rectangle-count bound.

These checks validate the implementation and finite instances only. The infinite-family obstruction and Theorem 3.1 are established in the primary report by proofs, not by finite computation.
