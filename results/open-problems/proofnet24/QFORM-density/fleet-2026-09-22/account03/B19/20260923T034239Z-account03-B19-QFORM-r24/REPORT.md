SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T03:42:39Z.
attacking: QFORM-SQRT-COLLAR-TO-LINEAR-SMOOTHING-v1 via a two-physical-gradient 2/3-small-ball receiver and independent singularity transducers.

# account03/B19 r24 — two-gradient 2/3 receiver and linear-density splices

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** universal proof assembly  
**Owner control at start:** `yspennstate/math-research-brain@8a24ac3b3b610693138602ff0294f093838b4eb2`, OWNER CONTROL revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING ANALYTIC THEOREM / FULL TARGET OPEN`.

The unrestricted QFORM theorem is not claimed. The global continuous-density conclusion is also still open. This report uses only original-coordinate independence. It does not rotate independent inputs, does not invoke law-uniform pointwise van der Corput, does not replace a product source by an arbitrary joint density in a quadratic trace, and does not select one local minor from aggregate volume.

## 1. Inputs used

### 1.1 Two-dimensional product-projection density

The completed product-projection input used in account01/B16 (`QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v1`, canonical source `yspennstate/math-open-problems@80f95e245b7f3418e8da36173ac4eb9d81fb58a7:proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260923T003846Z/REPORT.md`) includes the sharp dimension-two projection fact:

if `Y=(Y_j)` has independent marginal densities bounded by one and `M` is a real `2 x m` matrix of row rank two, then

`||p_(MY)||_infinity <= 2 / sqrt(det(M M^T)).`                 (1.1)

Indeed normalize `M` by `G=M M^T`: `R=M^T G^(-1/2)` has orthonormal columns; the orthogonal two-dimensional product projection has density cap two, and the determinant change of variables gives (1.1).

### 1.2 Existing B19 indefinite-pair transducer

The preceding account03/B19 r23 bundle, canonical `yspennstate/math-open-problems@80403bc0adff2c5e8278848674c81448e9782e44`, records the completed implication:

if an invertible **indefinite original-coordinate physical pair** has `D=|det B|`, `kappa=sigma_min(B)`, and its exact Schur residual `R` obeys

`sup_z P(|R-z|<=rho) <= H rho^(1/4)`,                            (1.2)

then

`||p_Q||_infinity <= 3*2^(4/3) H^(2/3) D^(-1/3) kappa^(-1/6).`   (1.3)

Only the stated scope is used below.

## 2. Main lemma: two physical gradients give a 2/3 small-ball exponent

Let `X_1,X_2` be two original coordinates and let `Y` be a disjoint bank of original coordinates. Assume all coordinates are independent and all marginal densities are at most one. Let `B` be an arbitrary real symmetric `2 x 2` matrix, `beta in R^2`, `M` a real `2 x m` matrix of row rank two, and `S(Y)` an arbitrary measurable real function. Put

`X=(X_1,X_2)^T`,

`R = X^T B X + X^T(2 M Y + beta) + S(Y)`.                       (2.1)

Define the two-row area currency

`Delta_2 := sqrt(det(M M^T)) > 0`.                               (2.2)

No assumption is imposed on the signs or degeneracy of `B`, and `S` may contain arbitrary quadratic, affine, or more general measurable dependence on the residual bank.

### Theorem 2.1 — `QFORM-TWO-PHYSICAL-GRADIENT-2OVER3-SMALLBALL-v1`

For every `z in R` and `eps>0`,

`P(|R-z|<=eps)
 <= 12 (2 Delta_2)^(-1/3) eps^(2/3).`                            (2.3)

#### Proof

Write

`C(Y)=2 M Y+beta`.

By (1.1), scaling a two-dimensional vector by the factor two in both coordinates gives

`||p_C||_infinity <= M_2 := 1/(2 Delta_2).`                      (2.4)

For fixed `Y=y`, let

`q_y(x)=x^T Bx + C(y)^T x + S(y)-z`.

Fix `eta>0` and split according to the two **physical** derivatives.

### Far-gradient region

On the event `|partial_1 q_Y(X)|>=eta`, condition on `(X_2,Y)`. As a function of the original scalar `X_1`, `q_y` is a quadratic polynomial and has at most two monotonicity branches. On each branch where the derivative has modulus at least `eta`, the inverse image of the output interval `[-eps,eps]` has Lebesgue length at most `2 eps/eta`. Since the density of `X_1` is at most one, the total contribution is at most

`4 eps/eta`.                                                     (2.5)

On the remaining part of the far-gradient region we have `|partial_1 q|<eta` and `|partial_2 q|>=eta`. Conditioning instead on `(X_1,Y)` gives another `4 eps/eta`. Thus

`P(|R-z|<=eps, max_j |partial_j q_Y(X)|>=eta)
 <= 8 eps/eta`.                                                   (2.6)

No support-length factor appears: each one-dimensional conditional law has total mass one and density cap one.

### Near-gradient region

For fixed `X=x`,

`grad_x q_Y(x) = 2 Bx + C(Y)`.                                   (2.7)

If both physical derivatives have modulus below `eta`, then `C(Y)` lies in an axis-parallel square of side length `2 eta`, hence area `4 eta^2`. Because `X` is independent of the residual original-product bank and (2.4) is an **unconditional product-projection density bound**,

`P(max_j |partial_j q_Y(X)|<eta | X=x)
 <= 4 M_2 eta^2`.                                                (2.8)

Averaging in `x` gives the same bound. Therefore

`P(|R-z|<=eps)
 <= 8 eps/eta + 4 M_2 eta^2`.                                   (2.9)

Choose `eta=(eps/M_2)^(1/3)`. Both terms then have the same scale and

`P(|R-z|<=eps)
 <= 12 M_2^(1/3) eps^(2/3)
 <= 12(2 Delta_2)^(-1/3) eps^(2/3)`.                            (2.10)

This proves (2.3). QED.

### Scope check

The proof never conditions on a rotated projection. The only conditioning is on original coordinates. The two-dimensional density cap is used only after conditioning on the genuinely independent original pair `X_1,X_2`, exactly where it remains valid. In particular this does not contradict the live conditional-cap corrections.

## 3. Fractional consequence: a half-Riesz potential is now finite

Let

`H = 12(2 Delta_2)^(-1/3)`.                                      (3.1)

Then (2.3) and probability normalization give

`P(|R-z|<=r) <= min(1,H r^(2/3)).`                               (3.2)

Using layer cake,

`E|R-z|^(-1/2)
 = integral_0^infinity P(|R-z|<s^(-2)) ds`.                      (3.3)

The crossover is `s_0=H^(3/4)`. Therefore

`E|R-z|^(-1/2)
 <= s_0 + H integral_(s_0)^infinity s^(-4/3) ds
 = 4 H^(3/4).`                                                    (3.4)

Hence

`boxed:
 sup_z E|R-z|^(-1/2)
 <= 4*12^(3/4)*(2 Delta_2)^(-1/4)
 < 21.687 Delta_2^(-1/4).`                                      (3.5)

This is the key upgrade over the one-hub r23 estimate: exponent `2/3>1/2` crosses the exact threshold needed to integrate a square-root singularity.

## 4. First linear-density splice: one disjoint scalar square

Let `Z` be one more original coordinate, disjoint from `(X_1,X_2,Y)`, with density at most one. Suppose a quadratic form has a nonzero original scalar pivot `d` in `Z`. Complete the square **only in this original coordinate**:

`Q = d (Z+h(X,Y))^2 + R(X,Y)`,                                   (4.1)

where `R` is the exact Schur remainder. Assume its two chosen original coordinates and residual bank satisfy Theorem 2.1 with area currency `Delta_2`.

Conditioned on `(X,Y)`, translation by `h` preserves the density cap of `Z`. The density of `d(Z+h)^2` is bounded pointwise by

`|d|^(-1/2) |u|^(-1/2)`                                         (4.2)

on its allowed half-line. Therefore, by (3.5),

### Corollary 4.1 — `QFORM-SCALAR-PLUS-TWOGRADIENT-DENSITY-v1`

`boxed:
 ||p_Q||_infinity
 <= 4*12^(3/4)*2^(-1/4)
    |d|^(-1/2) Delta_2^(-1/4)
 < 21.687 |d|^(-1/2) Delta_2^(-1/4).`                            (4.3)

This branch allows arbitrary signs, arbitrary self-curvature in the two active coordinates, and arbitrary measurable residual curvature `S(Y)` after the exact Schur completion.

For the concrete scale-comparable thresholds

`|d|>=1/64`, `Delta_2>=1/64`,                                   (4.4)

the bound is `<491`.

Continuity is not asserted by this argument; it proves an essentially bounded density.

## 5. Second linear-density splice: an outer indefinite physical pair

The `2/3` estimate also implies a quarter-Hoelder estimate without losing product provenance. For every `r>0`,

`min(1,H r^(2/3)) <= H^(3/8) r^(1/4)`.                           (5.1)

Apply the completed B19 transducer (1.3) to an **outer disjoint original-coordinate indefinite pair** whose exact Schur residual has the form of Theorem 2.1. We obtain

### Corollary 5.1 — `QFORM-INDEFINITE-PAIR-PLUS-TWOGRADIENT-v1`

`boxed:
 ||p_Q||_infinity
 <= C_2 D^(-1/3) kappa^(-1/6) Delta_2^(-1/12),`                  (5.2)

where

`C_2 = 3*2^(4/3)*12^(1/4)*2^(-1/12)
     = 13.2801830364...`.                                        (5.3)

Thus

`D>=1/64`, `kappa>=1/64`, `Delta_2>=1/64`                        (5.4)

imply

`boxed: ||p_Q||_infinity <151.`                                  (5.5)

The dependence on the two-row area is only `Delta_2^(-1/12)`, which is substantially softer than paying a reciprocal local determinant directly. This is a genuine arbitrary-extra-spectrum branch: all coordinates not in the outer physical pair are retained in the exact Schur residual, and `S(Y)` in Theorem 2.1 is unrestricted.

## 6. Application to the current proof tree

The preceding r23 one-hub theorem paid the arbitrary hub diagonal analytically but left only a square-root small-ball estimate in the exact-rank-three small-Pluecker collar. The present theorem identifies the **next exact currency that upgrades square-root smoothing**: a second original physical gradient whose two cross rows have nonzero aggregate area `Delta_2`.

Consequently, in any current branch carrying a scale-comparable scalar pivot or a scale-comparable outer indefinite pair, the first unpaid state can now be restricted to configurations in which every candidate two-row Schur cross bank is nearly rank one. This is precisely compatible with the fleet's bank/ridge structural program: one should now attack the remaining `rank-one cross-row alignment` state rather than seek a single large physical minor.

This does **not** by itself close the B10/B19 exact-rank-three collar, because the collar currently guarantees one aggregate star row, not a uniform lower bound for a second-row area. The exact next implication is therefore:

`QFORM-COLLAR-SECOND-GRADIENT-OR-RANKONE-ALIGNMENT-v1`:
from the exact-rank-three small-Pluecker collar, either extract a quantitatively nonzero two-row cross area in original coordinates and route it through the present receiver, or prove that the failure of every such area forces the source into the already-paid exact-coloop/rank-one-bank geometry.

This is a strictly narrower structural question than r23's former generic `sqrt -> linear` request.

## 7. Designated partner account04/B19 applied at an actual inequality

The completed designated-partner theorem `QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1`, canonical source

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a:proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`,

proves in its residual-diffuse exact-null-coloop scope

`||p_Q||_infinity < 34 sqrt(log(e/D_res))`, `0<D_res<=1`.         (7.1)

On the actual quantitative interval `e^(-8)<=D_res<=1`,

`log(e/D_res)<=9`, hence

`boxed: ||p_Q||_infinity <102.`                                  (7.2)

The partner source separately pays `D_res=0` and `D_res>=1`. No near-coloop or non-diffuse scope is silently added.

## 8. Status

The full target remains **OPEN / NOT PROVED / NOT DISPROVED**. The full continuous-density conclusion remains open. The new results are exact analytic supporting theorems and two target-level paid branches. Their proof uses arbitrary bounded-density input laws and no moment, support, log-concavity, Gaussian, or diagonal-basis assumptions.

The first essential missing implication after this run is `QFORM-COLLAR-SECOND-GRADIENT-OR-RANKONE-ALIGNMENT-v1`, followed separately by the still-open global assembly from exact/near rank three to arbitrary extra spectrum outside the now-paid pair-plus-two-gradient branch.
