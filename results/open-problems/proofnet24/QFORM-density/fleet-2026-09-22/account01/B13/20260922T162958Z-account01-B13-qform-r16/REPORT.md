# account01/B13 — affine-uniform two-variable half-Riesz bridge

**Run:** `20260922T162958Z-account01-B13-qform-r16`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control at publication:** revision `2026-09-22.7`  
**Assignment:** extremal product laws  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full conjecture remains **OPEN**. This run closes a previously explicit near-pure-saddle loss in the three-original-coordinate Schur route: every nonsingular physical principal triple with at least one nonzero diagonal pivot now gives a translation-uniform density certificate. The still unpaid geometry is the genuinely zero-pivot/isotropic grouped-coordinate branch, followed by robustness to arbitrary additional spectral directions.

## 1. Exact dependencies used

1. `account02/B13`, `QFORM-PRODUCT-BANGBANG-REDUCTION-v1`, canonical commit `yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`: for any nonnegative measurable kernel, optimization over one-dimensional cap-one probability densities can be purified coordinatewise to measure-one indicator sets. In the proof below I apply its one-coordinate bathtub identity to a singular kernel majorant rather than merely cite the product reduction.
2. Latest compatible assigned-partner addendum `account02/B13`, `QFORM-RANGE-AFFINE-GAUGE-v1`, canonical commit `yspennstate/math-open-problems@0a857bd45e25ebe3ced60b019558d6dfbf4f380f`: affine terms in `Range(A)` are exactly removable by coordinate translations at the level of the universal density/slab functional. For an invertible two-variable Hessian, every affine term lies in the range. This is applied below to make the half-Riesz bound exactly translation-uniform.
3. `account01/B03`, Schur half-Riesz handoff, canonical proof `yspennstate/math-open-problems@6ab17ba5d3198aa7ca7838e68d110db9c22f8306`: the earlier two-variable argument paid the balanced Schur region and the exact pure-saddle endpoint but retained a loss for `0<max(|S_11|,|S_22|)<<sqrt(|det S|)`. The theorem below removes that residual.
4. The live corrections forbidding post-rotation independence, raw same-support perturbation, conditional cap substitution, fixed fragment count, and pointwise quadratic oscillatory decay are all respected. No such premise enters the proof.

## 2. A uniform weak-L1 quadratic-root lemma

For `sigma in {+1,-1}` and `s in R`, define

`k_{sigma,s}(y)=|sigma y^2+s|^{-1/2}`,

with the value `+infinity` at zeros.

### Lemma 2.1

For every `lambda>0`,

`|{y in R: k_{sigma,s}(y)>lambda}| <= 2 sqrt(2) / lambda`.        (2.1)

Consequently the decreasing rearrangement obeys

`k^*(u) <= 2 sqrt(2)/u`, `u>0`.                                  (2.2)

#### Proof

Put `rho=lambda^{-2}`. The superlevel condition is

`|sigma y^2+s|<rho`.

After changing the sign/renaming the center this asks that `y^2` lie in an interval of length at most `2rho`, truncated at zero. If that interval is `(a,b)` with `0<=a<b` and `b-a<=2rho`, its two-sided square-root preimage has measure

`2(sqrt(b)-sqrt(a))`.

For fixed width this is maximized at the boundary `a=0`, and the worst possible upper endpoint is `2rho`. Hence the measure is at most `2sqrt(2rho)=2sqrt(2)/lambda`. This proves (2.1), hence (2.2). QED.

## 3. A one-dimensional quadratic-strip estimate

### Lemma 3.1

For `H in R`, `delta>0`,

`|{u: |u^2-H|<=delta}| <= 2 sqrt(2) delta / sqrt(|H|)`             (3.1)

whenever `H!=0`. At `H=0` the left side is `2sqrt(delta)`.

#### Proof

If `H>0` and `delta<H`, the left side is

`2[sqrt(H+delta)-sqrt(H-delta)]
 =4delta/[sqrt(H+delta)+sqrt(H-delta)]
 <=2sqrt(2)delta/sqrt(H)`.

If `H>0` and `delta>=H`, it is `2sqrt(H+delta)`, and with `r=delta/H>=1`, `sqrt(1+r)<=sqrt(2)r` gives (3.1). If `H<0`, the set is empty unless `delta>=|H|`; then its measure is `2sqrt(delta-|H|)`, again bounded by `2sqrt(2)delta/sqrt(|H|)`. QED.

## 4. Main theorem: affine-uniform two-variable half-Riesz

### Theorem 4.1 — `QFORM-2VAR-AFFINE-UNIFORM-HALF-RIESZ-v1`

Let `Y,Z` be independent real random variables with probability densities bounded by one. Let

`S=[[a,b],[b,c]]`

be a real symmetric invertible `2 x 2` matrix, and set

`Delta=|det S|>0`.

For arbitrary `ell in R^2`, `kappa in R`, define

`R=(Y,Z)^T S (Y,Z)+ell^T(Y,Z)+kappa`.

Then for every `t in R` and `epsilon>0`, with

`tau=8 epsilon/sqrt(Delta)`,                                      (4.1)

one has

`P(|R-t|<=epsilon) <= 1`                                         (4.2)

and, whenever `tau<=1`, the sharper logarithmic bound

`P(|R-t|<=epsilon) <= tau [1+log(1/tau)]`.                       (4.3)

Moreover

`sup_t E |R-t|^{-1/2} <= 8 sqrt(2) Delta^{-1/4}`.                (4.4)

All constants are uniform in the affine term, translations of the input laws, signs of the eigenvalues of `S`, and the locations/shapes of the one-dimensional supports.

#### Proof: affine terms are a free gauge

Because `S` is invertible, choose `h=(1/2)S^{-1}ell`. Then

`x^T S x+ell^T x+kappa=(x+h)^T S(x+h)+kappa-h^T S h`.

Coordinatewise translation by the two fixed components of `h` preserves independence and the one-dimensional density caps. This is exactly the invertible two-variable specialization of the assigned partner's `QFORM-RANGE-AFFINE-GAUGE-v1`. A scalar translation is absorbed into `t`. Hence it suffices to prove the theorem for

`R=aY^2+2bYZ+cZ^2`.                                               (4.5)

#### Proof: the case `c!=0`

Condition on `Y=y`, set

`u=cz+by`,
`H(y)=ct-(ac-b^2)y^2`.

The exact identity

`c(R-t)=u^2-H(y)`                                                 (4.6)

holds. Put `delta=|c|epsilon`. Since the density of `Z` is at most one and `dz=du/|c|`, Lemma 3.1 gives, for `H(y)!=0`,

`P(|R-t|<=epsilon | Y=y)
 <= min{1, 2sqrt(2) epsilon / sqrt(|H(y)|)}`.                    (4.7)

The same inequality holds with the right side interpreted as one when `H(y)=0`.

Write `d=det S=ac-b^2`, `Delta=|d|`. Then

`|H(y)|=Delta |sigma y^2+s|`                                    (4.8)

for some `sigma in {+1,-1}` and some real `s` depending on `c,t,d`. Thus

`P(|R-t|<=epsilon | Y=y)
 <= min{1, beta k_{sigma,s}(y)}`,
`beta=2sqrt(2) epsilon/sqrt(Delta)`.                             (4.9)

By Lemma 2.1, the decreasing rearrangement of the majorant in (4.9) is bounded by

`min{1, 8 epsilon/(sqrt(Delta) u)}`.                              (4.10)

Now apply the one-coordinate bathtub identity from the assigned partner `account02/B13`: for any density `f_Y` with `0<=f_Y<=1`, `int f_Y=1`, the integral against a nonnegative majorant is at most the integral of its decreasing rearrangement over a set of measure one. Therefore

`P(|R-t|<=epsilon)
 <= int_0^1 min{1,tau/u} du`.                                    (4.11)

If `tau<=1`, the last integral equals

`tau+tau log(1/tau)`,                                            (4.12)

which is (4.3).

#### Proof: the case `c=0`

Invertibility forces `b!=0` and `Delta=b^2`. Conditioning on `Y=y`, the expression in `Z` is linear with slope `2by`, hence

`P(|R-t|<=epsilon |Y=y)
 <= min{1, epsilon/(|b y|)}`.                                    (4.13)

The weak-L1 constant of `|y|^{-1}` is two, so the same bathtub argument gives (4.3) with a smaller numerical constant. Thus (4.3) is valid for every invertible `S`.

#### Proof of the half-Riesz estimate

Layer cake gives

`E|R-t|^{-1/2}=int_0^infinity P(|R-t|<u^{-2}) du`.               (4.14)

Set

`u0=2sqrt(2) Delta^{-1/4}`.                                      (4.15)

For `u<=u0`, use probability at most one. For `u>=u0`, (4.3) has `tau=(u0/u)^2`. Therefore

`E|R-t|^{-1/2}
 <= u0 + u0 int_1^infinity v^{-2}(1+2log v) dv
 =u0+3u0
 =8sqrt(2) Delta^{-1/4}`.                                       (4.16)

This proves (4.4). QED.

## 5. Three-original-coordinate Schur corollary

### Corollary 5.1 — `QFORM-3COORD-NONZERO-PIVOT-AFFINE-CERT-v1`

Let a full quadratic form in independent cap-one variables be given. Condition on all but three **original physical coordinates** `X,Y,Z`. Let the fixed symmetric principal Hessian on these coordinates be an invertible matrix `T`, and suppose one diagonal pivot, say

`d=T_11`,

is nonzero. Arbitrary outside coordinates and arbitrary couplings to them are allowed. Then the conditional density of the full quadratic, uniformly in all conditioned outside values, satisfies

`||p_{Q|outside}||_infinity
 <= 8sqrt(2) |d det T|^{-1/4}`.                                  (5.1)

Hence the unconditional density obeys the same bound.

#### Proof

Write

`T=[[d,u^T],[u,C]]`.

After conditioning outside coordinates, only affine terms are added to the selected three-variable polynomial. Complete the square in the original independent coordinate `X`. Conditional on `(Y,Z)` and the outside variables, the shifted `X` still has a density bounded by one, and the square pushforward satisfies

`p_Q(q |Y,Z,outside)
 <= |d|^{-1/2}|q-R_out(Y,Z)|^{-1/2}`,                            (5.2)

where the residual two-variable Hessian is the Schur complement

`S=C-u u^T/d`                                                    (5.3)

and `R_out` may contain arbitrary affine terms. Since

`det S=det T/d`,                                                 (5.4)

Theorem 4.1 gives

`p_Q(q|outside)
 <= |d|^{-1/2} 8sqrt(2) |det S|^{-1/4}
 =8sqrt(2)|d det T|^{-1/4}`.                                    (5.5)

Average over the outside variables. QED.

### What this closes

The earlier `account01/B03` Schur theorem left the near-pure-saddle range

`0<max(|S_11|,|S_22|)<<sqrt(|det S|)`

as its first unpaid endpoint. Corollary 5.1 removes that loss entirely: no balance assumption on the two-variable Schur complement remains. The only local obstruction is now a genuinely zero diagonal pivot (or absence of a quantitatively usable nonsingular original-coordinate triple), not a near-saddle interpolation problem.

## 6. Applying the latest account02/B13 collar obstruction

The latest compatible assigned-partner run constructs a tetrahedral exact-rank-three frame with

`Lambda=diag(1,1,-1)`,

adds a zero fifth coordinate, and rotates by an angle `theta` mixing the tetrahedral direction `w=(e1+e2)/sqrt(2)` with the fifth coordinate. It proves

`||A_theta-A_0||_op <= 2 theta`                                  (6.1)

while allowing product supports translated by order `1/sin(theta)`, thereby refuting any raw same-support slab-continuity modulus. Its subsequent `QFORM-RANGE-AFFINE-GAUGE-v1` addendum explains that the induced order-one affine term is a free range translation, not a density obstruction.

Apply Corollary 5.1 to the fixed physical triple `I={1,2,3}`. At `theta=0`, its principal matrix is

`T_0=(1/4) [[1,1,1],[1,1,-3],[1,-3,1]]`.                        (6.2)

It has

`det T_0=-1/4`,

and eigenvalues

`1`, `(-1-sqrt(17))/8`, `(sqrt(17)-1)/8`.                       (6.3)

In particular

`d_0=1/4`,
`sigma_min(T_0)=(sqrt(17)-1)/8`.                                (6.4)

For `theta<=1/16`, (6.1) and principal-submatrix contraction give

`|d_theta|>=1/8`,                                                (6.5)

and Weyl gives

`sigma_min(T_theta)
 >= (sqrt(17)-2)/8=:s_* >0`.                                    (6.6)

Therefore

`|det T_theta|>=s_*^3`,                                         (6.7)

and Corollary 5.1 yields the explicit uniform bound

`||p_{Q_theta}||_infinity
 <=8sqrt(2)[(1/8)s_*^3]^{-1/4}
 <51.46`.                                                        (6.8)

This holds for **every** cap-one product law, including the partner's translated fifth-coordinate supports. Thus the new affine-uniform half-Riesz mechanism passes the exact support-translation obstruction that kills raw operator-norm slab continuity.

At the exact endpoint `theta=0`, the same certificate gives

`||p_{Q_0}||_infinity <=16sqrt(2)<22.63`.                        (6.9)

The point is not the numerical constant but the uniformity: arbitrarily remote supports create no loss once the affine gauge is handled before estimating the Schur trace.

## 7. Exact status and next implication

**Old missing implication:** close the near-pure-saddle two-variable Schur residual while retaining original-coordinate product provenance and arbitrary affine leakage.

**New status:** paid by Theorem 4.1 and Corollary 5.1.

**First unpaid implication:**

`QFORM-ZERO-PIVOT-GROUPED-COLLAR-v1` — obtain a product-preserving bound in the remaining geometry where every quantitatively useful nonsingular original-coordinate triple has zero or vanishing diagonal pivot, especially the approximate four-bank nested-heavy rank-three limit identified in the preceding B13 run. The proof must aggregate original independent banks before conditioning; bounded projected density or same-support coefficient continuity is insufficient. After exact rank three, arbitrary additional spectral components remain a separate full-target debt.

This report does **not** claim the full conjecture, does not claim continuity of the output density, and does not infer a universal good physical triple from the three-large-eigenvalue hypothesis.
