# QFORM-RANK3-BILINEAR-SCHUR-BANK-v1

Run: `20260922T183809Z-account02-B09-QFORM-r7`  
Worker: account02/B09 — Bilinear block mechanism  
Status: **ESSENTIAL_STEP_APPLIED / FULL_QFORM_OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## First unpaid implication

`QFORM-PAIRAGGREGATE-OR-CURVED-SCHUR-ROUTING-v1`: starting only from the three-large-eigenvalue hypothesis, route the remaining matrices either to (i) a bilinear physical pair whose entire rank-one Schur bank has a universal aggregate payment as below, (ii) an already completed diffuse/ridge/definite branch, or (iii) a genuinely higher-rank curved Schur residual and control that residual without taking a conditional spectral supremum. The newest scalar-fiber corrections forbid replacing (iii) by a mixed conditional-`L^infinity` moment.

The point of this run is to remove the *one physical third coordinate* from the exact-rank-three bilinear payment. The full rank-one Schur remainder is aggregated before reciprocal minor inversion.

## Sources actually used


Named partner result actually applied: account03/B09 `QFORM-INDEFINITE-PAIR-SCHUR-SMOOTHING-v1`, canonical source `yspennstate/math-open-problems@f510cd96f4505202fa369a8ac74b9d016b72ae14`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/account03-B09-20260922T171558Z-qform13/REPORT.md`. I use its translation-uniform indefinite-pair density envelope and the source-pinned weak-`L^2` logarithmic-square estimate.

Also consumed: account03/B09 correction `QFORM-CONDITIONAL-THREEPROJ-2OVER3-MOMENT-FALSE-v1`, canonical source `yspennstate/math-open-problems@60b3f717b1a0e336406bc2acdfc1eaf951906fca`; account01/B05 correction `QFORM-WEIGHTED-SCALAR-FIBER-SUP-FALSE-v1`, canonical source `yspennstate/math-open-problems@058acb5c8f9186ef199bbaf136b57f4dd9ea3800`. Neither refuted interface is used here.

The one-dimensional linear-projection cap `||p_{u^T X}||_infinity<=sqrt(2)` for `||u||_2=1` is the same LPP input already used in this worker's previous theorem `QFORM-ZEROINTERNAL-BANK-WEDGE-v1`, canonical source `yspennstate/math-open-problems@de2e592f5ba2ee9ed9ff152afa6a8856f3e29e1f`.

## Theorem 1 — rank-one Schur bank aggregation

Let `X=(X_1,...,X_n)` have independent real densities bounded by one, and let `A` be real symmetric of **rank exactly three**. Select two original coordinates `i,j` and write, after reordering,

`A = [[H, C^T],[C,D]]`,

where `H` is the physical `2x2` principal block. Assume `H` is invertible and indefinite. Put

`S = D-C H^{-1} C^T`.

Block Gaussian elimination is a congruence, so

`rank(A)=rank(H)+rank(S)`.

Hence `rank(S)=1`. Write

`S = sigma w w^T`, `||w||_2=1`, `sigma!=0`,

and set `W=w^T X_K` on the complementary original-coordinate bank `K`. By the one-dimensional LPP projection estimate,

`||p_W||_infinity <= sqrt(2)`.

Let `Psi(u)=1+log(1/|u|)` for `0<|u|<=1` and `Psi(u)=|u|^{-1/4}` for `|u|>=1`.

Condition on the entire complementary bank `X_K=z`. Completing the two physical pair variables translates their two one-dimensional densities separately, hence preserves both cap-one bounds. The partner theorem therefore applies **pointwise in z**. Crucially, its envelope is translation-uniform, so after the pair variables are integrated out the only remaining `z` dependence is through

`z^T S z = sigma (w^T z)^2`.

Thus the full complementary bank enters only through the single *unconditioned* marginal `W`; no conditional projection density is taken.

### (a) Pair with a nonzero diagonal

Write

`H=[[r,s],[s,t]]`, `Delta=|det H|`,

and suppose `r!=0`. The partner envelope gives

`p_{pair|z}(u) <= 8 Delta^{-1/2} Psi(r u/Delta)`.

The partner's weak-`L^2` square estimate says for a cap-one scalar density `g`, uniformly in translations,

`int g(y) Psi(a+delta y^2)dy <= 2 sqrt(15) delta^{-1/4}`.

If the scalar density cap is `L`, scaling `Y'=LY` changes `delta` to `delta/L^2`, so the right side becomes

`2 sqrt(15) L^{1/2} delta^{-1/4}`.

Using `L<=sqrt(2)` and `delta=|r sigma|/Delta` yields

`||p_{X^TAX}||_infinity <= 16*2^(1/4)*sqrt(15) [Delta |r sigma|]^(-1/4)`.

The symmetric statement with `t` holds when `t!=0`.

### (b) Pure bilinear physical pair

If

`H=[[0,s],[s,0]]`, `s!=0`,

the partner product envelope gives

`p_{pair|z}(u) <= |s|^{-1} Psi(u/(2s))`.

Now `delta=|sigma|/(2|s|)`. The same scalar projection and weak-`L^2` estimate give

`boxed:  ||p_{X^TAX}||_infinity <= 2^(3/2) sqrt(15) (|s|^3 |sigma|)^(-1/4).`

Every interval `L` therefore satisfies the same coefficient times `|L|`. No resampling or square-root small-ball conversion appears.

## Corollary 2 — zero-diagonal exact-rank-three pair aggregate

Assume in addition `A_kk=0` for every physical coordinate and `rank(A)=3`. Fix any nonzero edge `s=A_ij`. Then the pair block is pure bilinear, and the Schur remainder above is rank one.

For each `k` outside the pair, the `3x3` principal determinant factors through the same Schur complement:

`det A[{i,j,k}] = det(H) S_kk = -s^2 sigma w_k^2`.

But zero diagonal also gives exactly

`det A[{i,j,k}] = 2 A_ij A_ik A_jk`.

All the first expressions have the same sign. Summing absolute values over `k` and using `sum w_k^2=1` gives the exact aggregate identity

`|s|^2 |sigma| = 2 |s| sum_{k!=i,j} |A_ik A_jk|`,

hence

`|sigma| = (2/|s|) sum_{k!=i,j}|A_ik A_jk|`.

Substituting into Theorem 1(b) yields

`boxed:  ||p_{X^TAX}||_infinity <= 2^(5/4) sqrt(15) [ |A_ij|^2 sum_{k!=i,j}|A_ik A_jk| ]^(-1/4).`

This is an **aggregate third-coordinate payment**. The partner's local theorem pays one quantity `|A_ik A_jk|`; the new bound pays their sum before inversion.

## Target-valid clone-bank family closed uniformly

Let

`B=[[0,1,1],[1,0,-1],[1,-1,0]]`.

Its nonzero spectrum is `{1,1,-2}`. For `m>=1`, split the third physical coordinate into `m` clones by the isometry

`S_m=[e_1,e_2,m^{-1/2} 1_m]`,

and set

`A_m=S_m B S_m^T`.

Then `A_m` has the same nonzero spectrum `{1,1,-2}` and zero diagonal. In physical coordinates,

`A_12=1`, `A_1k=m^{-1/2}`, `A_2k=-m^{-1/2}` for every clone `k`, and the clone-clone block is zero.

For the fixed pair `(1,2)`,

`sum_k |A_1k A_2k| = m*(1/m)=1`.

Therefore the new aggregate theorem gives the dimension-free target bound

`boxed: ||p_{X^T A_m X}||_infinity <= 2^(5/4) sqrt(15) < 9.212.`

By contrast, applying the named partner theorem to any single physical triple gives

`||p||_infinity <= 2 sqrt(15) m^(1/4)`,

because every such triple has determinant magnitude `2/m`. The previous B09 `QFORM-ZEROINTERNAL-BANK-WEDGE-v1` also does not pay this family through its flat clone bank: the clone-to-`{1,2}` cross block has rank one, whereas that theorem requires two nonzero cross singular values. Thus the present Schur-bank aggregation closes a genuinely different diffuse-local-minor obstruction.

## Scope and remaining debt

This report does **not** prove the full conjecture. It proves a new exact-rank-three bilinear aggregation theorem and closes the clone-bank target family above. A universal pair with

`|A_ij|^2 sum_k |A_ik A_jk| >= c`

is not forced by the spectral hypothesis; diffuse light-cone families can make every such pair payment small and must be routed to the existing diffuse/ridge mechanisms. For higher-rank matrices the Schur residual need not be rank one, and the new scalar-fiber corrections prohibit paying it by moving a conditional supremum outside its translated mixture.

No numerical computation is used as mathematical evidence in this report; the displayed decimal is only the evaluation of the exact constant `2^(5/4)sqrt(15)`.
