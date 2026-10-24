# account01/B05 — qform principal-block handoff

Outcome: `ESSENTIAL_STEP_APPLIED`; full target `OPEN_NOT_PROVED`; execution `WITHOUT_VERIFIED_BRAIN`.

Scientific report: `yspennstate/math-open-problems`, commit `e3e8754ab0cd1ae93bbe74f9fdbf0df8947fc6c8`, path `qform/fleet-2026-09-22/account01/B05/20260922T1136Z-qform-principal2d-B05-r1/REPORT.md`.

Consumed OTHER-account result: account03/B17 handoff at brain commit `5a060b9340b64e27474a5d95d7b4782cfb894382`. Its law-uniform one-dimensional Fresnel-decay falsifier is accepted; its diagonal same-sign-pair `pi` theorem is extended below.

## New theorem
If some original-coordinate 2x2 principal block `B=A[{i,j},{i,j}]` is positive or negative definite, then conditioning every other coordinate gives a planar quadratic with joint amplitude `f_i f_j<=1`. Elliptic-shell area therefore yields for every interval `I`

`P(X^TAX in I) <= pi |I| / sqrt(|det B|)`.

Hence `||p_Q||_infty <= pi/sqrt(|det B|)`. In particular `|det B|>=1` gives constant `pi`. This allows an arbitrary cross term `A_ij`, not just B17's diagonal pair.

## Two decisive bridge failures
1. Three large eigenvalues do not yield a uniformly nondegenerate coordinate pair. For `n=2^m`, the rank-three Walsh projection `A=sum_{r=1}^3 u_r u_r^T` has eigenvalues `1,1,1,0,...`, but every 2x2 coordinate principal determinant is at most `9/n^2` (nonzero values are `8/n^2`).
2. Crude fiber-supremum averaging over a two-dimensional spectral subspace is dimension-losing. For cube density and a flat Walsh 2-plane `E`, `int_{E^perp} sup_{y in E} 1_[0,1]^n(y+z) dz` equals the projection volume `n/2`.

## First unpaid implication
Prove a genuinely averaged nonlinear Brascamp-Lieb/coarea bound for the same-sign two-eigenvector subspace that keeps the product amplitude inside the elliptic level-set integral. It must survive the flat rank-three Walsh projection family; one cannot select a single good coordinate pair or take a fiberwise amplitude supremum first.
