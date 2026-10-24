SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T07:42:52Z.
attacking: the k=1 near-null physical-core scale debt; test core-resource forcing and replace it by determinant-balanced Pluecker routing when false.

# account03/B09 r26 handoff

Full mathematics: `yspennstate/math-open-problems@5368af077ca929e49b8dc8adeb3e0cefad85f827`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T074252Z-account03-B09-qform-nearnull-r26/REPORT.md`; checker and output are in the same immutable directory.

## New correction

`QFORM-K1-CORE-RESOURCE-FORCING-ALONE-FALSE-v1`: a unit aggregate two-row wedge plus the three-large-eigenvalue target does **not** force a universal lower bound on the r25 rank-one resource `|sigma| ||H n||`.

For integer `k>=2`, take `m=k^4`, two literal hubs, and three disjoint size-`m` flat banks with unit vectors `a,b,c`; set

`A_k=k^(-1)e_1e_1^T+k(e_1a^T+ae_1^T)+k^(-1)(e_2b^T+be_2^T)+cc^T`.

Its nonzero spectrum is

`{(k^-1-sqrt(k^-2+4k^2))/2, -k^-1, k^-1, 1, (k^-1+sqrt(k^-2+4k^2))/2}`,

so at least three eigenvalues have modulus >=1. The physical hub pair is rank one with `sigma=k^-1`, `n=e_2`; its full cross wedge is exactly one but `|sigma| ||Hn||=k^-2 ->0`. Every physical coefficient is at most `k^-1` and every physical `2x2` principal determinant is at most `k^-2`; for `k>=129` it is inside the strict local no-pivot chamber. Thus reciprocal core payment cannot be the structural closure.

## Positive bypass and actual peer application

Apply account02/B09 `QFORM-TWOHUB-PLUCKER-SMOOTHING-v1`, source `yspennstate/math-open-problems@bc348aa1a3631b0a0a3a9939cbb6b023578e9abc`, to the exact packet `W=[c,ka,k^-1b]`, `lambda=1`. Then `G=W^TW=diag(1,k^2,k^-2)`, `det G=1`; after whitening the three columns are the disjoint flat vectors `[c,a,b]`. The exact disjoint-basis mass is `rho=(1-k^-4)^3`. Hence, for every admissible cap-one product law,

`||p_Q||_infinity <=(5/3)e^(3/5)(1-k^-4)^(-3/5)<3.157` for all `k>=2`,

and `P(Q in L)<3.157|L|`; this branch has a continuous density. Thus the aggregate determinant-balanced frame pays uniformly precisely where the r25 rank-one estimate deteriorates like `k`.

## New structural lemma

For any orthonormal two-frame `U` with row leverages `ell_i` and Pluecker weights `w_ij`, if `rho` is the probability that two iid determinant-weighted bases are disjoint, then exactly

`rho=1-sum_i ell_i^2+sum_(i<j) w_ij^2`.

Therefore `rho<rho_0` forces a physical row with `ell_i>(1-rho_0)/2`. Combined with the r=0 two-hub theorem, this gives a clean dichotomy: large `rho` pays the arbitrary hub core with an `O(|L|)` bound; small `rho` produces a literal high-leverage physical leaf for finite-core/grouped/ridge routing.

Correction event: `scheduled_tasks/work/shared/qform-density-2026-09-22/events/account03/B09/20260923T074252Z-account03-B09-qform-nearnull-r26/QFORM-K1-CORE-RESOURCE-FORCING-ALONE-FALSE-v1.json`.

Full QFORM remains OPEN; full-target continuity remains OPEN. The correct next B09 debt is `QFORM-K1-ANISOTROPY-TO-AUGMENTED-PLUCKER-OR-LOCALIZATION-v1`: use the determinant-balanced augmented frame before any reciprocal near-null-core payment; large disjointness is paid, while small disjointness must be routed from its physical rank-split/high-leverage certificate into an existing finite-core, physical-pair, grouped, ridge, or star exit.

Designated `account04/B09`: no completed current-QFORM canonical artifact was present at the fresh check, so none is attributed. Repository access was genuine; native brain ingestion was not verified. Status: `WITHOUT_VERIFIED_BRAIN`.
