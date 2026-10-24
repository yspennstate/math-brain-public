# Post-refresh addendum — later skeleton correction consumed

Run: `account02-B13-20260923T1811Z`. Programme: `QFORM-DENSITY-3EIG-20260922`.

After the main report was written, I refreshed the current checked projected-crossing source at

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its 2026-09-23T17:05:55Z addendum corrects the old structure/REPORT.md Theorem 3.1: the volume-sampled skeleton relation is in general an **upper bound**, not an equality, because a singular `r`-minor can have a nonsingular `(r+1)`-extension and therefore contributes on the right without being sampled as a seed.

The same addendum explicitly proves that the robust consequence used in this B13 run survives unchanged:

`V_{r+1} <= kappa V_r`

still implies a physical decomposition

`A=D+R+E`, `rank(R)<=4r`, `E` zero-diagonal,

`||E||_F <= 3(r+1) sqrt(kappa)`.

The proof chooses a nonsingular seed whose residual Frobenius norm is at most `(r+1)sqrt(V_{r+1}/V_r)`, symmetrizes its rank-r light block, takes a best rank-r symmetric approximation, and retains the `2r` skeleton coordinates. This is exactly the corollary used in Theorem 4.1 of the main report. Therefore the new theorem

`QFORM-UNCONDITIONAL-D5-RANK16-FROB-SKELETON-v1`

is unaffected by the correction.

The same refresh also makes the review chronology of the designated-partner receiver newer than account03/B13 r30's own snapshot. The main report's phrase "pending projected-crossing receiver" should be read as **the status recorded inside r30 at its publication time**, not as a claim about the final-release review state. The present rank-sixteen theorem does not use that receiver at all, so its validity is independent of this chronology.

No other formula in the main report changes. In particular the exact Bernoulli-cut identity

`E_cut e_5(A[I,J]^T A[I,J]) = 4^-5 V_5(A)`

is a direct Cauchy--Binet counting identity and is unrelated to the corrected skeleton-seed equality.

Changed-file privacy check: manual allowlist review; pure mathematics and public source pins only.
