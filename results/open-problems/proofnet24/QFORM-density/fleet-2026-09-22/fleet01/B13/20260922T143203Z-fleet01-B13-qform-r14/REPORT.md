# fleet01/B13 — disjoint-Pluecker stability, a three-coordinate collar, and the exact zero-mass boundary

**Run:** `20260922T143203Z-fleet01-B13-qform-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Assignment:** Extremal product laws  
**Classification:** `ESSENTIAL_STEP_APPLIED / RANK-THREE STRUCTURAL REDUCTION / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full conjecture remains **OPEN / NOT PROVED**. Everything below concerns the rank-exactly-three spectral core. Arbitrary additional spectral directions remain a separate full-target interaction problem except in already completed scoped branches.

## 1. Fresh source state and corrections

Initial coherent control was read at `yspennstate/math-research-brain@c767fb2477f733e6d828bd37431e2fb420620eea`; immediately before publication the control was refreshed through `94161ed90fc36af81e2c403a7a45490f08b64e79`. The owner programme remained `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`, and the full target remained OPEN.

The live correction set was re-read. In particular this report does **not** use law-uniform pointwise quadratic oscillatory decay, post-rotation independence, a fiber-supremum trace bound, one cross minor, one Schur rank-two extraction, conditional density caps as a substitute for independence, or an absolute phase-Wiener integral.

## 2. Completed assigned-partner results actually applied

The assigned partner `fleet02/B13` supplied two exact ingredients.

### 2.1 Exact bang-bang product-law reduction

Canonical source:

`yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T115714Z-fleet02-B13-qform-480ba28b/REPORT.md`.

For every measurable `K:R^n->[0,1]`, if

`D={f: 0<=f<=1, int f=1}`,

then

`sup_{f_i in D} int K(x) prod_i f_i(x_i) dx`
` = sup_{|E_i|=1} int_{prod E_i} K(x) dx`.                 (2.1)

For `K=1_{Q in J}`, the worst small-ball probability over all admissible independent laws is therefore **exactly** the worst slab volume over product sets of one-dimensional measure one. The supremum is unchanged if each `E_i` is a bounded finite union of intervals. No single-interval or centered-uniform reduction is valid.

### 2.2 Finite-projective-direction rank-three theorem

Canonical strengthened source:

`yspennstate/math-open-problems@8a21bd3d25ce1622121616ce789589e1e073f68d`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T125435Z-fleet02-B13-80c2a32d/FINITE_DIRECTION_ADDENDUM.md`.

Let `A=R Lambda R^T` have rank exactly three, `R^T R=I_3`, and all three nonzero eigenvalues have modulus at least one. If the nonzero rows of `R` lie in at most `m` projective directions, then

`||p_Q||_infinity <= 2 C_3 binom(m,3)`,                  (2.2)

where

`C_3=2 pi+3 sqrt(3)=11.4793377298...`.

Thus `m=3` gives `<23`, `m=4` gives `<92`, and `m=5` gives

`||p_Q||_infinity <= 20 C_3 = 40 pi+60 sqrt(3) <230`.    (2.3)

Both partner results are used below on the actual geometric residual produced by the previous B13 theorem.

## 3. Previous B13 theorem: aggregate disjoint exterior mass

The preceding run proved at

`yspennstate/math-open-problems@0b5cf04790e5927df0efed8811a2a1295006e141`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260922T135910Z-fleet01-B13-qform-r13/REPORT.md`

the following. Write the rank-three Parseval frame rows as `r_i in R^3`, so

`sum_i r_i r_i^T=I_3`.

For every triple `I`, define

`w_I=det(R_I)^2`,                                         (3.1)

where `R_I` is the `3 x 3` row submatrix. Cauchy--Binet gives

`sum_{|I|=3} w_I=1`.                                      (3.2)

Define the ordered disjoint Pluecker mass

`D_0=sum_{I cap J=empty} w_I w_J`.                        (3.3)

Then

`||p_Q||_infinity <= 12 |det Lambda|^(-1/3) D_0^(-1/6)` (3.4)

whenever `D_0>0`. Under `|lambda_j|>=1`,

`||p_Q||_infinity <= 12 D_0^(-1/6)`.                     (3.5)

The old residual was the overlap-heavy regime `D_0` small. The point of this run is to identify its geometry quantitatively rather than selecting a single minor.

## 4. Exact complement identity for a basis triple

For a fixed triple `I`, let

`S_I=R_I^T R_I`.

Since `R^T R=I_3`,

`R_{I^c}^T R_{I^c}=I_3-S_I`.                             (4.1)

Applying Cauchy--Binet to the complement matrix gives the exact identity

`sum_{J subset I^c, |J|=3} w_J`
` = det(R_{I^c}^T R_{I^c})`
` = det(I_3-S_I)`.                                       (4.2)

Therefore

`boxed(D_0 = sum_I w_I det(I_3-S_I))`.                   (4.3)

This is the projection-DPP avoidance identity here, but (4.2) is a direct Cauchy--Binet proof and needs no probabilistic machinery.

Because the weights `w_I` sum to one, (4.3) says that `D_0` is the `w_I`-average of the complement determinant of a random spectral basis triple.

## 5. Quantitative stability: small disjoint mass forces a three-coordinate collar

### Theorem `QFORM-RANK3-D0-STABILITY-v1`

Let `0<delta<1`. If

`D_0 < delta`,                                            (5.1)

then there is a basis triple `I={i_1,i_2,i_3}` and a unit spectral vector `v in R^3` such that

`sum_{i in I} <v,r_i>^2 > 1-delta^(1/3)`,                (5.2)

or equivalently

`sum_{i notin I} <v,r_i>^2 < delta^(1/3)`.               (5.3)

Thus an overlap-heavy rank-three frame has a spectral direction whose mass is concentrated on **three original physical coordinates**.

### Proof

By (4.3), some basis triple `I` with `w_I>0` satisfies

`det(I_3-S_I) <= D_0 < delta`.                            (5.4)

The matrix `S_I` is positive definite and `S_I<=I_3`, because

`I_3-S_I=sum_{i notin I} r_i r_i^T >=0`.

Let its eigenvalues be `mu_1,mu_2,mu_3 in (0,1]`. Then

`prod_k (1-mu_k) < delta`.                                (5.5)

Hence one factor is `<delta^(1/3)`, so

`max_k mu_k > 1-delta^(1/3)`.                            (5.6)

Take a unit eigenvector `v` for that eigenvalue. Then

`v^T S_I v=sum_{i in I}<v,r_i>^2>1-delta^(1/3)`,

and subtracting from `v^T I_3 v=1` proves (5.3). QED.

### Concrete universal dichotomy

Take `delta=1/64`. Combining (3.5) and Theorem 5 gives:

`boxed(`
`either ||p_Q||_infinity <=24,`
`or some spectral direction has >3/4 of its squared mass on three physical coordinates.`
`)`                                                           (5.7)

Indeed, if `D_0>=1/64`, (3.5) gives `12*(64)^(1/6)=24`; otherwise (5.2) gives mass `>1-1/4=3/4` on a triple.

This is a dimension-free structural reduction of the previous overlap-heavy debt. It uses aggregate exterior mass before any reciprocal local-minor payment.

### A useful leverage corollary

If every physical row has leverage

`ell_i=||r_i||^2 <= alpha <1/3`,                          (5.8)

then for every triple `I`,

`lambda_max(S_I) <= tr(S_I) <=3alpha`.

Therefore

`det(I_3-S_I) >=(1-3alpha)^3`,

and averaging with (4.3) yields

`D_0 >=(1-3alpha)^3`.                                    (5.9)

Consequently the previous two-bank theorem gives

`||p_Q||_infinity <= 12(1-3alpha)^(-1/2)`.               (5.10)

The point is not a new global diffuse threshold; it is an exact quantitative bridge from frame leverage to the aggregate disjoint channel.

## 6. Actual geometric slab implication via the assigned partner

Let `J` be any interval and let `E_i subset R` be arbitrary measurable sets with `|E_i|=1`. Give `X_i` the density `1_{E_i}`. In the branch `D_0>=1/64`, (5.7) gives

`|{x in prod_i E_i : x^T A x in J}| <=24 |J|`.           (6.1)

By the partner's exact bang-bang identity (2.1), (6.1) is equivalently the worst-law small-ball bound on this matrix branch:

`sup_{0<=f_i<=1, int f_i=1} P(X^TAX in J) <=24 |J|`.     (6.2)

Thus the assigned product-indicator reduction is not merely cited: it converts the new exterior-mass dichotomy into the exact geometric sublevel-set inequality requested by this slot.

In the complementary `D_0<1/64` branch, the geometric problem is now localized to a three-coordinate collar (5.2)--(5.3), not to arbitrary overlap-heavy frames.

## 7. Exact endpoint `D_0=0`: finite directions or a leverage-one coordinate

The stability theorem has an exact combinatorial endpoint.

Let `M` be the rank-three vector matroid of the nonzero rows `r_i`. A triple `I` is a matroid basis exactly when `w_I>0`. Because every term in (3.3) is nonnegative,

`D_0=0` iff `M` has no two disjoint bases.                (7.1)

Use Edmonds' base-packing criterion in the special case of two rank-three bases: two disjoint bases exist iff for every subset `X` of the ground set,

`|E\X| >= 2(3-rank(X))`.                                 (7.2)

If there are no two disjoint bases, some `X` violates (7.2). Since all quantities are integral:

- `rank(X)=0` implies `|E\X|<=5`; hence there are at most five nonzero rows and at most five projective directions.
- `rank(X)=1` implies `|E\X|<=3`; hence all but at most three rows lie on one line, giving at most four projective directions.
- `rank(X)=2` implies `|E\X|<=1`. Full rank forces exactly one row `r_j` outside the plane `span(X)`.

In the last case choose a unit normal `v` to that plane. Parseval gives

`1=sum_i <v,r_i>^2=<v,r_j>^2`.                           (7.3)

Also `||r_j||<=1`, because `I_3-r_jr_j^T>=0`. Therefore equality in (7.3) forces

`r_j=+/-v`, `||r_j||^2=1`.                               (7.4)

So `j` is a physical coordinate of **leverage exactly one**. Conversely, if `||r_j||=1`, then every other row is orthogonal to `r_j`; every spectral basis must contain `j`, so two disjoint bases are impossible and `D_0=0`.

We have proved:

### Theorem `QFORM-RANK3-D0-ENDPOINT-v1`

If `D_0=0`, then either

1. the nonzero spectral-frame rows lie in at most five projective directions, or
2. there is a physical coordinate with leverage exactly one.

Consequently, if `D_0=0` and no leverage-one coordinate exists, the assigned partner's finite-direction theorem (2.2) gives the **universal** bound

`boxed(||p_Q||_infinity <= 40 pi+60 sqrt(3) <230)`.       (7.5)

By (2.1), the equivalent finite-fragment geometric statement is

`|{x in prod E_i: x^T A x in J}|`
` <= (40 pi+60 sqrt(3)) |J|`                             (7.6)

for arbitrary measure-one product sets in this entire endpoint branch.

## 8. The leverage-one endpoint has an exact canonical normal form

Suppose now `D_0=0` and the endpoint is a leverage-one coordinate `j`. Rotate only the **three-dimensional spectral representation** so that

`r_j=e_1`;                                                (8.1)

this does not rotate the physical input vector. Every other frame row lies in `e_1^perp`. Hence the first spectral coordinate is exactly the original independent variable `X_j`, while the remaining spectral pair `(Y,Z)` is a two-dimensional orthogonal projection of the remaining independent coordinates.

Write in this spectral basis

`Lambda = [[a,b^T],[b,C]]`,                               (8.2)

where `C` is symmetric `2x2`.

If `a!=0`, the completed universal rank-two half-Riesz/Schur theorem of fleet01/B05 gives

`||p_Q||_infinity <= C_2 (|a| |det Lambda|)^(-1/4)`,      (8.3)

so only the near-isotropic limit `a->0` is uniformly unresolved by that scalar-pivot route.

If `a=0`, invertibility forces `b!=0`. Rotate inside the residual spectral plane (again not in physical coordinate space) so that `b=(B,0)`, `B>0`. Then

`Lambda = [[0,B,0],[B,r,kappa],[0,kappa,tau]]`,           (8.4)

and the determinant identity is exact:

`det Lambda = -B^2 tau`.                                 (8.5)

Thus the quadratic form is

`Q = 2B X_j Y + rY^2 +2kappa YZ + tau Z^2`,              (8.6)

with

`B^2 |tau|=|det Lambda|>=1`.                             (8.7)

This is precisely the product-provenance hyperbolic/projection boundary that the current heavy-isotropic programme has isolated, but here it arises as the **exact endpoint** of vanishing disjoint Pluecker mass.

There is one further exact simplification. If every residual physical coordinate `k!=j` has zero diagonal pivot, then with residual row `s_k in R^2`,

`s_k^T C s_k=0` for every k.                              (8.8)

The matrix `C` cannot be zero, since otherwise (8.4) would have rank at most two. The real zero cone of a nonzero binary quadratic form is contained in at most two projective lines. Hence all residual rows lie in at most two projective directions; together with `r_j`, the whole frame has at most three directions. The partner theorem therefore gives

`||p_Q||_infinity <=4 pi+6 sqrt(3)<23`.                  (8.9)

So an unresolved leverage-one / zero-pivot endpoint must have at least one residual physical coordinate with nonzero pivot, even though that pivot may be arbitrarily small.

## 9. What changed and the exact unpaid implication

**Old missing implication:** control arbitrary rank-three overlap-heavy frames when the disjoint Pluecker mass `D_0` is small.

**New proved structural condition:** small `D_0` forces a spectral direction into a three-original-coordinate collar; at the exact endpoint `D_0=0`, every non-leverage-one frame is automatically a <=5-projective-direction frame already covered by the assigned partner theorem. The leverage-one endpoint itself has the exact canonical form (8.6), and its all-zero-residual-pivot subcase is also finite-direction and closed.

The first rank-three unpaid implication is now:

> **`QFORM-RANK3-THREE-COORDINATE-COLLAR-CLOSURE-v1` (OPEN).** Starting from a rank-three Parseval frame in which some spectral direction has at least `3/4` of its mass on three original coordinates, prove a universal small-ball/density bound while retaining the product provenance of the residual two-dimensional projection; in the limiting leverage-one case this includes the canonical form (8.6). Equivalently, construct a valid cap-one product-law counterexample.

This is materially narrower than the previous unrestricted overlap-heavy problem. It is also consistent with the correction that one local principal/cross minor need not be well conditioned: the collar may need aggregate hyperbolic-square or half-Riesz payment rather than inverse-minor selection.

A second, separate debt remains after rank three: arbitrary additional spectral directions must be retained or conditioned by a source-valid theorem; the rank-three argument alone does not justify deleting them.

## 10. Status

- Full QFORM: **OPEN / NOT PROVED**.
- New results: exact Cauchy--Binet complement identity, quantitative `D_0` stability, `24`-or-three-coordinate-collar dichotomy, exact `D_0=0` matroid endpoint classification, and the leverage-one canonical hyperbolic form.
- Assigned partner `fleet02/B13` was applied to actual slab inequalities and to the endpoint finite-direction closure.
- No continuity claim is made outside scopes where an imported theorem already supplies it.
- No new counterexample to the owner conjecture was found.
