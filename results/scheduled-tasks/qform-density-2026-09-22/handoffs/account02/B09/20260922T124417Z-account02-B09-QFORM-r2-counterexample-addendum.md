# account02/B09 addendum — universal single-pivot extraction refuted

Run `20260922T124417Z-account02-B09-QFORM-r2`; classification addendum `CANDIDATE_REFUTED`. Canonical proof: `yspennstate/math-open-problems@17dec75dc10459933f8bfde30daa86d1c6d90a6a:proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260922T124417Z-account02-B09-QFORM-r2/SCHUR_PIVOT_EXTRACTION_FALSIFIER.md`.

Apply account01/B19's exact target family `A_m` (canonical source `072cf685a12893b44d555f14e4e610bcf2154037`): one coordinate `0`, groups `Y,Z` of size `m`, edges `A_{0y}=m^-1/2`, and `ZxZ=J_m/m`. Its nonzero spectrum is exactly `{1,-1,1}`.

Only `Z` coordinates have nonzero diagonal, each `d=1/m`. Pivot any `z in Z`. Its Schur correction cancels the entire residual `ZxZ` block exactly, leaving only the `0-Y` star. Every disjoint cross block of a star has rank at most one. Coordinates `0` and `Y` have diagonal zero, so they are unavailable as scalar pivots. Therefore this genuine three-large-eigenvalue family has **no** pivot satisfying the new rank-two Schur-cross theorem.

This is not a QFORM counterexample. The same family aggregates exactly to `2 X0 Y_m + Z_m^2` and account01/B19, applying account02/B10, gives a universal density bound `<19.1`.

Correction registered as `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`. The correct residual is `QFORM-SCHUR-CROSS-OR-DIFFUSE-AGGREGATION-v2`: either use a quantitative rank-two Schur pivot, or recognize low-cross-rank/star geometry and aggregate product coordinates before paying local reciprocal costs.
