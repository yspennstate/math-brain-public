SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-24T10:09:17Z.
attacking: exact rank-one/P2-flat and near-flat hub transition via product-preserving near-null coordinate deletion and an affine inductive compiler.

# fleet01/B06 r53 — rank-one hub transverse-or-delete compiler

Programme: `QFORM-DENSITY-3EIG-20260922`. Owner control read on fresh `main`: revision `2026-09-22.15`. Full unrestricted QFORM remains **OPEN**; global continuity remains **OPEN**. Execution remains `WITHOUT_VERIFIED_BRAIN` because repository retrieval/writeback is not verified native learned-memory receiver use.

## 1. Inputs actually consumed

1. Immediate predecessor fleet01/B06 r52, canonical bundle head `6c9adce6b8378fa430fc731b4969ae9e2f2f0659`, report introduced at `84bf6f24ab7baeec288164f8b8d36c10b878b286`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260924T093818Z-fleet01-B06-QFORM-r52/REPORT.md`.
   Its theorem `QFORM-RANKONE-HUB-TRANSVERSE-P2-WEIGHTED-v1` states, in the exact rank-one three-hub setup below, that if the transverse two-dimensional tail map has singular-value product `Delta_perp>0`, then
   
   `||p_Q||_infinity < 12 |lambda|^(-1/2) Delta_perp^(-1/4)`.

2. Designated partner fleet02/B06 latest completed report `QFORM-SPARSE-KERNEL-PRODUCT-DELETION-v1`, commit `006892a091e8f58edf21e071244a2c7e2a340ec0`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260924T092809Z-auto11-a9c3/REPORT.md`.
   For a kernel subspace supported on at most three literal coordinates it conditions on literal original coordinates, preserves product density caps by deterministic translation, and retains `s_3` with loss at most a factor three.

3. Pinned three-dimensional affine base theorem at `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`: for a literal three-coordinate symmetric matrix whose three eigenvalue magnitudes are at least `sigma`, arbitrary independent cap-one inputs and arbitrary linear terms give density at most `6 sqrt(pi)/sigma`.

4. Live correction `QFORM-DENSITY-PRESERVING-SHEAR-FACTORISATION-GAP-v1` was explicitly checked before this argument. The invalid interface there removes a translated density factor inside a leaf Fourier transform after a random-variable shear. The argument below does **not** do that. It conditions first on one literal original coordinate; only then are the remaining variables deterministically translated, so their product provenance is exact.

## 2. Scale-normalized affine target functional

It is useful to record the exact recursive object rather than silently assuming that linear terms disappear. For `m>=3`, define `C_m^aff` to be the least constant (possibly `+infinity`) such that for every `tau>0`, every real symmetric `m x m` matrix `C` with

` s_3(C) >= tau, `

every vector `b`, every scalar `c`, and every independent real input vector with one-dimensional densities bounded by one, the scalar

` X^T C X + 2 b^T X + c `

has density bounded by

` C_m^aff / tau. `

The original target is contained in this affine formulation by taking `b=0`. The three-dimensional pinned theorem gives

` C_3^aff <= 6 sqrt(pi). `

Nothing below claims that `sup_m C_m^aff` is already known finite.

## 3. Exact rank-one hub setup

Let `n>=4`. Select three **literal original coordinates** `H` and write

` A = [[K,M],[M^T,C_0]], `

where `K` is `3 x 3`, the columns of `M` correspond to the tail bank, and `C_0` is arbitrary. Assume

` K = lambda u u^T,   ||u||_2=1,   |lambda| >= kappa sigma, `

for some `kappa>0`, while the full matrix satisfies

` s_3(A) >= sigma > 0. `

Let

` P_perp = I_3-u u^T `

and define `nu` to be the smaller singular value of the tail map into the plane `u^perp`, equivalently

` nu = min_{w in u^perp, ||w||=1} ||M^T w||_2. `

If the transverse rank is at most one then `nu=0`. Let `beta_1>=nu` be the two singular values on `u^perp`; r52's currency is

` Delta_perp = beta_1 nu. `

## 4. Main theorem — `QFORM-RANKONE-HUB-TRANSVERSE-OR-AFFINE-DELETE-v1`

Under the setup above, exactly one of the following two quantitative routes is available.

### Route A: transverse curvature is not small

If

` nu > sigma/(2 sqrt(3)), `

then r52 applies and

` Delta_perp = beta_1 nu >= nu^2. `

Therefore

` ||p_Q||_infinity < 12 |lambda|^(-1/2) nu^(-1/2) `

and hence

` boxed( ||p_Q||_infinity < [12 sqrt(2 sqrt(3)/kappa)] / sigma ). `

The front constant is

` 12 sqrt(2 sqrt(3)) = 22.3345166184... `

before the factor `kappa^(-1/2)`.

This branch is a direct density payment. It retains the full tail quadratic form and never takes a curved-fiber maximum.

### Route B: a near-null literal coordinate can be deleted product-preservingly

If

` nu <= sigma/(2 sqrt(3)), `

then there exist a unit `w in u^perp` and a literal hub coordinate `k in H` such that

` ||M^T w||_2 = nu,   |w_k|^2 >= 1/3. `

Let `R` be all coordinates except `k`, put

` C = A_RR, `

and extend `w` by zeros on the tail. After ordering coordinate `k` first, write

` T = w_R / w_k, `

` P = [-T  I_R], `

and

` q = (A w)_R / w_k. `

Because `w in u^perp`,

` K w = 0. `

Hence `Aw` vanishes on all three hub coordinates and equals `M^T w` on the tail. Consequently `q` is tail-supported while `T` is supported only on the other two hub coordinates, so

` q^T T = 0 `

and

` ||q||_2 = nu/|w_k| <= sqrt(3) nu <= sigma/2. `

The block equations `Aw=(0_H,M^T w)` now give the **exact matrix identity**

` boxed( A = P^T C P + [[0,q^T],[q,0]] ). `

Also

` ||P||_op^2 = 1+||T||_2^2 = 1/|w_k|^2 <= 3. `

Since the off-diagonal error matrix has operator norm `||q||_2`, Weyl's singular-value inequality and the product singular-value inequality give

` s_3(P^T C P) >= s_3(A)-||q||_2 `

and

` s_3(P^T C P) <= ||P||_op^2 s_3(C). `

Therefore

` boxed( s_3(C) >= |w_k|^2 (sigma-||q||_2) >= sigma/6 ). `

This is a deterministic spectral statement only; it does **not** treat the small matrix error as a small random quadratic perturbation.

## 5. Product-preserving conditional identity

Let the parent scalar include an arbitrary affine term,

` Q(X)=X^T A X + 2 g^T X + c. `

Condition on the **literal original coordinate** `X_k=t`. Define

` Z = X_R - T t. `

For every fixed `t`, the coordinates of `Z` are independent deterministic translations of the original coordinates in `R`; all one-dimensional density caps remain at most one.

Using `q^T T=0`, the exact matrix identity from Route B becomes

` Q | (X_k=t) = Z^T C Z + 2 (g_R+t q)^T Z + c_t `

for a scalar `c_t`. No Fourier factor is removed and no rotated coordinate is declared independent.

Since `s_3(C)>=sigma/6`, the definition of `C_{n-1}^aff` gives the uniform conditional bound

` ||p_{Q | X_k=t}||_infinity <= 6 C_{n-1}^aff / sigma. `

Averaging the actual conditional densities therefore yields

` boxed( ||p_Q||_infinity <= 6 C_{n-1}^aff / sigma ). `

Combining the two routes gives the concise recursive certificate

` boxed( sigma ||p_Q||_infinity <= max{ 12 sqrt(2 sqrt(3)/kappa), 6 C_{n-1}^aff } ). `

This is a complete end-to-end implication for every exact rank-one three-coordinate hub satisfying `|lambda|>=kappa sigma`.

## 6. Actual application of the designated fleet02/B06 result

If `nu=0`, choose `w in u^perp` with `M^T w=0`. Then the extended vector `(w,0_tail)` is an **actual global kernel vector supported on the three literal hub coordinates**:

` A (w,0)^T = 0. `

Apply fleet02/B06 `QFORM-SPARSE-KERNEL-PRODUCT-DELETION-v1` with `d=1`, `m=3`. It supplies a literal coordinate `k` for which

` |w_k|^2 >= 1/3, `

and, for `C=A_RR`, the sharper exact-endpoint inequality

` boxed( s_3(C) >= sigma/3 ). `

Conditioning on `X_k=t` leaves independent translated cap-one variables, so the affine child bound gives the actual inequality

` boxed( ||p_Q||_infinity <= 3 C_{n-1}^aff / sigma ) `

at the exact P2-flat endpoint.

In dimension four this partner theorem plus the pinned three-dimensional affine base theorem gives the fully numeric target payment

` ||p_Q||_infinity <= 18 sqrt(pi)/sigma = 31.904169.../sigma. `

Thus r52's exact P2-flat survivor is not a new probabilistic pathology: it is a product-preserving lower-dimensional target instance.

## 7. Relation to r52's aggregate P2 packet

r52 proved the exact identity

` P_2 = lambda^2 Delta_perp^2. `

The present theorem identifies what happens when the second transverse singular value, rather than merely the product, collapses. A small `nu` creates a physical near-null direction `w`; a large `nu` makes the entire transverse product packet large enough for r52's curved receiver. The threshold is paid **before** any individual tail minor is selected.

At `nu=0`, r52's structural form

` M = u alpha^T + v beta^T `

with `v in u^perp` makes the sparse null vector explicit: any unit `w` perpendicular to both `u` and `v` satisfies `Kw=0` and `M^T w=0`.

## 8. Why the live shear correction does not invalidate this argument

The current correction `QFORM-DENSITY-PRESERVING-SHEAR-FACTORISATION-GAP-v1` forbids dropping a translated density mask inside a Fourier transform after a leaf-dependent shear. Here the order is different and exact:

1. choose a **deterministic matrix direction** `w` from `A`;
2. choose one **literal original coordinate** `k`;
3. condition on the scalar original variable `X_k=t`;
4. only then translate each remaining original coordinate by the deterministic number `T_j t`;
5. invoke the affine target theorem on that genuine conditional product law.

There is no masked/unmasked Fourier comparison. Therefore the correction is consumed rather than bypassed.

## 9. Finite checks

A deterministic random checker in this run verifies, for ambient dimensions `4,5,8,12`, the identities

` A = P^T C P + E, `

` ||P||^2 = 1/|w_k|^2, `

` ||q|| = nu/|w_k|, `

and the spectral inequality

` s_3(C) >= |w_k|^2 (s_3(A)-||q||). `

The worst reconstruction discrepancy was below `6e-10`; the norm and singular-value identities were at machine precision, and every tested spectral margin was nonnegative. These are sanity checks only; Sections 4--5 are exact proofs.

## 10. Status and next debt

**New result:** proved supporting direct-or-delete compiler for the exact rank-one three-coordinate hub, including the entire P2-flat endpoint and a quantitative near-flat transition.  
**Essential boundedness:** direct in Route A; conditional on the lower-dimensional affine target constant in Route B.  
**Continuity:** not proved in Route A. In Route B, continuity would pass from a uniformly bounded continuous child density by dominated convergence, but the full-target continuity claim remains open.  
**Full QFORM:** OPEN.  
**Counterexample:** none found.

The first unpaid local implication is now

`QFORM-NEARRANKONE-HUB-STABLE-TRANSVERSE-OR-DELETE-v1`:

extend this exact-rank-one dichotomy to `0 < sigma_2(K) << sigma_1(K)` while retaining the small nonzero hub curvature exactly. One may not delete that curvature as a small random perturbation on unbounded inputs. The right object should combine the current near-null coordinate deletion with the existing two-hub gradient-volume / pair-log receivers, so that a large transverse packet is paid directly and a genuinely small combined hub-plus-tail residual routes to a lower-dimensional affine child without accumulating an uncontrolled reciprocal physical minor.

A separate global assembly issue remains: repeated lower-dimensional deletions can multiply the spectral-scale loss. This report does not claim that the recursion has already been globally closed.

## 11. Source pins

- Owner source message: `https://github.com/yspennstate/math-research-brain/blob/0dc369ddf8b860648dd780d8f92c62994dc53ecf/scheduled_tasks/README.md`.
- Prepublication refresh read: `yspennstate/math-research-brain@b0b17be8ce16b8baaccfeec0230015dd1e66ec46`.
- Predecessor r52: `yspennstate/math-open-problems@6c9adce6b8378fa430fc731b4969ae9e2f2f0659:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260924T093818Z-fleet01-B06-QFORM-r52/REPORT.md`.
- Designated partner result actually applied: `yspennstate/math-open-problems@006892a091e8f58edf21e071244a2c7e2a340ec0:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260924T092809Z-auto11-a9c3/REPORT.md`, theorem `QFORM-SPARSE-KERNEL-PRODUCT-DELETION-v1`.
- Three-dimensional affine base theorem: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `COUNTEREXAMPLE_SEARCH.md`, Theorem A.
- Live shear-interface correction consumed: `yspennstate/math-research-brain@b944bf36baa222e9f7e778a91a3ef8a06ae70a64`, event `QFORM-DENSITY-PRESERVING-SHEAR-FACTORISATION-GAP-v1`.
