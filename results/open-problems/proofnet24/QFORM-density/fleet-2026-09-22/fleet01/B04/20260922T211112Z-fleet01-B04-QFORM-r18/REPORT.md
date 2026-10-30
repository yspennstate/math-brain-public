SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-22T21:11:12Z.
attacking: translation-uniform near-null physical-pair half-Riesz smoothing, then splice it through the exact scalar-square Schur route while retaining arbitrary outside curvature.

# fleet01/B04 r18 — near-null pair half-Riesz collar

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T211112Z-fleet01-B04-QFORM-r18`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Fresh owner control before publication:** revision `2026-09-22.15`; QFORM remains the sole research target.

## 1. Exact target and correction discipline

The full target remains open: for every finite `n`, independent real physical coordinates with one-dimensional densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite essential bound for the density of `X^T A X`, or give a valid target counterexample. Continuity is tracked separately.

No Gaussian, moment, compact-support, connected-support, log-concavity, post-rotation independence, arbitrary-joint rank-three coarea, positive conditional projection-density moment, worst-fiber scalar density cap, one-good-local-minor principle, or law-uniform pointwise quadratic-phase decay is used here.

This run first checked the apparent scalar-square plus rank-two-cross route and found that it is already completed in fleet01/B03 (`QFORM-COPY-RECTANGULAR-CROSS-v1` and its rank-two half-Riesz corollary). I therefore did not duplicate it. The new step below attacks the genuinely different near-null physical-pair collar: both physical diagonal coefficients may be nonzero, so the exact-zero Schur-row theorem does not apply, while the pair remains strongly hyperbolic.

## 2. Completed inputs actually consumed

### 2.1 Near-null product density envelope

Source pinned at

`yspennstate/math-open-problems@287235f6ed9d0e0b876f0301f10a7b636db87ec1`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T172625Z-fleet02-B13-productset-r13/REPORT.md`.

Its theorem `QFORM-NEAR-NULL-ASINH-v1` implies the following convenient scaled form. Let `U,V` be independent cap-one inputs and

`q(u,v)=alpha u^2+2buv+beta v^2 + (arbitrary affine term)`,

where `b!=0` and

`|alpha|<=|b|/2`, `|beta|<=|b|/2`.                                (2.1)

Then, after a critical-value translation `tau`, the density obeys

`p_q(s) <= (2 sqrt(3)/|b|) Psi((s-tau)/(2|b|))`,                    (2.2)

where

`Psi(x)=1+log(1/|x|)` for `0<|x|<=1`,
`Psi(x)=|x|^(-1/4)` for `|x|>=1`.                                  (2.3)

The function `Psi` is even and decreasing on `(0,infinity)`. The estimate is uniform over arbitrary fragmented cap-one laws and arbitrary affine terms.

### 2.2 Designated partner fleet02/B04

Latest completed designated-partner source used here:

`yspennstate/math-open-problems@6155d85896070c87f6523a30646c38ac10be43a9`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260922T201618Z-fleet02-B04-qform-r13/REPORT.md`.

Its theorem `QFORM-SQUARE-WEIGHTED-DETERMINANT-HALFRIESZ-v1` says that for a genuine original-coordinate square completion

`Q=a(Z+d(Y))^2+R(Y)`, `a!=0`,                                    (2.4)

and a residual original-coordinate cross block `B`, one has

`||p_Q||_infinity <= |a|^(-1/2) J_q(B)`,                         (2.5)

under the theorem's stated range-leverage condition when `1<=q<2`, with no leverage condition at `q=2`. If `B` has at least `r` singular values at least `sigma` and `r>q`, then

`||p_Q||_infinity <= C_(r,q)/sqrt(|a| sigma)`,                    (2.6)

and at `q=2,r=3`,

`C_(3,2)=9.499315272418066...`.                                  (2.7)

This theorem retains arbitrary self-quadratic leakage on both sides of the residual cut. It is applied quantitatively in Section 5.

## 3. New theorem: a near-null pair has a uniform half-Riesz potential

Let `W` be an arbitrary collection of original coordinates, independent of original coordinates `U,V`. All coordinates have densities bounded by one. Let `L_1(W),L_2(W),G(W)` be arbitrary measurable functions for which the displayed random variable is finite, and put

`R = alpha U^2 + 2bUV + beta V^2
    + U L_1(W) + V L_2(W) + G(W)`.                               (3.1)

Assume (2.1).

### Theorem 3.1 — `QFORM-NEAR-NULL-PAIR-HALFRIESZ-v1`

The translation-uniform half-Riesz potential satisfies

`boxed(
 H_(1/2)(R):=sup_t E|R-t|^(-1/2)
 <= C_NN |b|^(-1/2),
)`                                                                  (3.2)

with the explicit constant

`boxed(
 C_NN = [8 sqrt(6)/13] [3+log(169)] + 13/sqrt(2)
      = 21.44722108592986... .
)`                                                                  (3.3)

No condition is imposed on `G(W)`; in particular, arbitrary same-bank quadratic curvature, extra spectrum, and couplings among the outside coordinates are retained.

### Proof

Condition on `W=w`. The coefficients of `U,V` outside their fixed quadratic pair become deterministic affine terms, so (2.2) applies. Thus for some `tau_w`, the conditional density `g_w` of `R` satisfies

`g_w(s) <= (2 sqrt(3)/|b|) Psi((s-tau_w)/(2|b|)).`                 (3.4)

Fix a target `t` and set

`rho = 2|b|/169`.                                                   (3.5)

Split the negative half moment into the local interval and its complement:

`E[|R-t|^(-1/2)|W=w]
 <= integral_(|s-t|<rho) g_w(s)|s-t|^(-1/2)ds + rho^(-1/2).`      (3.6)

The second term uses only total conditional mass one.

For the first term, both

`x -> Psi(x/(2|b|))`

and

`x -> |x|^(-1/2) 1_(|x|<rho)`

are nonnegative symmetric decreasing functions. The elementary one-dimensional rearrangement inequality (equivalently: the convolution of two symmetric decreasing functions is maximized at zero) therefore shows that the local integral is largest when the envelope center `tau_w` equals the kernel center `t`. Hence, with `r=rho/(2|b|)=1/169`,

`local
 <= (2 sqrt(3)/|b|) sqrt(2|b|)
    integral_(|x|<r) Psi(x)|x|^(-1/2) dx.`                       (3.7)

Since `r<1`, only the logarithmic part of `Psi` enters. Direct integration gives

`integral_(|x|<r) Psi(x)|x|^(-1/2) dx
 =4 sqrt(r) [3+log(1/r)].`                                      (3.8)

Indeed on the positive half-line,

`int_0^r x^(-1/2)dx=2sqrt(r)`,
`int_0^r x^(-1/2)log(1/x)dx=4sqrt(r)+2sqrt(r)log(1/r)`,

and then one doubles. Substituting `r=1/169` into (3.7) gives

`local <= [8 sqrt(6)/13][3+log(169)] |b|^(-1/2).`               (3.9)

The tail term from (3.6) is

`rho^(-1/2)=13/sqrt(2) |b|^(-1/2).`                              (3.10)

Equations (3.6)-(3.10) prove (3.2)-(3.3), uniformly in `w` and `t`. Averaging over `W` completes the proof. QED.

### Why this is genuinely different from the exact-zero endpoint

The exact-zero Schur-row theorem applies when one physical diagonal is exactly zero and uses a linear-in-one-coordinate representation. Theorem 3.1 allows both diagonals to be nonzero, up to half the cross coefficient in modulus. It therefore pays a robust hyperbolic collar without any coefficient-perturbation argument on remote supports: the proof uses the actual near-null density envelope and then a translation-uniform fractional potential.

## 4. Square splice: a full ambient density theorem

Let `Z` be a further original coordinate, independent of all coordinates inside `W`, and suppose after a genuine physical square completion the full form is

`Q = a (Z+d(W))^2 + R(W)`, `a!=0`,                                (4.1)

where the residual `R` contains a physical pair satisfying Theorem 3.1. The shift `d(W)` may reuse every residual variable.

For a fixed residual state, the translated square has the standard one-sided density envelope

`p_(a(Z+d)^2)(u) <= |a|^(-1/2)|u|^(-1/2)`.                       (4.2)

Therefore

`p_Q(t) <= |a|^(-1/2) E|R-t|^(-1/2)`.                           (4.3)

### Corollary 4.1 — `QFORM-OUTER-SQUARE-NEAR-NULL-PAIR-v1`

Under (4.1) and (2.1), the full quadratic form has an essentially bounded density and

`boxed(
 ||p_Q||_infinity <= C_NN / sqrt(|a b|)
                  < 21.448 / sqrt(|a b|).
)`                                                                  (4.4)

All other physical coefficients are arbitrary.

**Continuity:** not claimed by this argument. The conclusion is absolute continuity plus an essential `L^infinity` bound.

This is directly relevant to the live scalar-Schur S0 route: once an outer physical pivot has been formed, any surviving anchored residual pair in the near-null collar is analytically paid, even though both selected residual coordinates can have nonzero self curvature and even though the rest of the Schur residual is completely arbitrary.

## 5. Actual designated-partner application and a hybrid inequality

The fleet02/B04 theorem from Section 2.2 and Corollary 4.1 apply to the same parent square whenever the residual simultaneously contains a near-null physical pair and a partner-valid determinant cross bank. Hence

`boxed(
 ||p_Q||_infinity
 <= |a|^(-1/2)
    min{ C_NN |b|^(-1/2), J_q(B) }.
)`                                                                  (5.1)

If the partner block has at least `r` singular values at least `sigma` with `r>q`, then

`boxed(
 ||p_Q||_infinity
 <= |a|^(-1/2)
    min{ C_NN |b|^(-1/2), C_(r,q) sigma^(-1/2) }.
)`                                                                  (5.2)

In particular at the unconditional partner endpoint `q=2,r=3`,

`boxed(
 ||p_Q||_infinity
 <= |a|^(-1/2)
    min{21.447221086 |b|^(-1/2),
         9.499315273 sigma^(-1/2)}.
)`                                                                  (5.3)

This is an equation-level use of the completed designated-partner theorem, not a decorative citation.

For the partner's own dense seven-dimensional example, its completed square has `a=1`, the residual cross block has all three singular values `sigma=2`, and choosing a physical cross pair with coefficient `|b|=4/3` gives residual diagonals `3/10` and `-2/5`, which obey the near-null condition because both have modulus at most `2/3`. Thus the new branch gives

`21.447221086/sqrt(4/3)=18.573838301...`,

while the partner determinant branch gives

`9.499315272/sqrt(2)=6.717030246...`.

The hybrid inequality (5.3) therefore certifies

`||p_Q||_infinity <= 6.717030246...`                              (5.4)

on that fully coupled example, while Theorem 3.1 remains available when the residual determinant bank collapses to only one strong near-null pair.

## 6. A genuinely rotated indefinite three-dimensional target instance

Let

`H=[[2/5, 6/5],[6/5,-3/10]]`,
`v=(1/20,-1/25)^T`,

and define the physical matrix

`A = [[3, v^T], [v, H+vv^T/3]]`

that is,

`A = [[3,       1/20,       -1/25],
      [1/20,    481/1200,    1799/1500],
      [-1/25,   1799/1500,  -1123/3750]].`                         (6.1)

Every off-diagonal entry is nonzero. Completing the first physical square gives the exact product-coordinate identity

`X^TAX
 =3 (X_0 + (v^T(X_1,X_2))/3)^2
  +(X_1,X_2) H (X_1,X_2)^T.`                                     (6.2)

The residual pair is near-null because

`|2/5|<=|6/5|/2`, `|3/10|<=|6/5|/2`.                              (6.3)

The eigenvalues of `H` are exactly `13/10` and `-6/5`. Hence `diag(3,H)` has smallest singular value `6/5`. The perturbation from `diag(3,H)` to `A` has operator norm at most

`||v|| + ||v||^2/3
 = sqrt(41)/100 + 41/30000
 <0.065398.`                                                       (6.4)

Weyl's singular-value inequality therefore gives

`s_3(A)
 >=6/5 - sqrt(41)/100 - 41/30000
 >1.13460>1.`                                                       (6.5)

Thus this is an exact target-valid genuinely non-diagonal indefinite matrix with all three eigenvalues of modulus greater than one. Corollary 4.1 gives, for every admissible independent cap-one input law,

`boxed(
 ||p_(X^TAX)||_infinity
 <= C_NN/sqrt(3*(6/5))
 =11.3036780188... .
)`                                                                  (6.6)

Only essential boundedness is asserted; continuity is not proved by this branch.

## 7. Relation to the current high-leverage S0 frontier

The current fleet03/B07 high-leverage S0 analysis starts from a Schur residual cross block with `E_2(B)>=1/48`. At calibrated effective rank two, its diffuse collar is already paid; if both ridge sides are near-coloops, it produces physical anchors `i,j` carrying more than half of the second-compound mass and the exact edge/two-star dichotomy

`b^2 ||C||_F^2 > E_2(B)/8`

or

`||r||_2^2 ||c||_2^2 > E_2(B)/8`.

Theorem 3.1 now pays the entire arbitrary-curvature anchored branch whenever the corresponding physical pair

`[[S_ii,S_ij],[S_ij,S_jj]]`

satisfies

`|S_ii|,|S_jj| <= |S_ij|/2`, `S_ij!=0`.                            (7.1)

No zero-self hypothesis and no clean-side hypothesis remains in this subbranch.

The first unpaid implication is therefore sharpened to

`QFORM-ANCHORED-NONNEARNULL-OR-TINY-CROSS-ROUTING-v1`:

> In the two-sided ridge-near-coloop S0 state, if the anchored pair fails (7.1) or its cross coefficient is quantitatively tiny, use the large anchored edge-times-bank / two-star reserve to force a second physical pivot, a rank-two banked Schur packet, a zero-self/Frobenius endpoint, or another completed ridge/grouped branch, without selecting one tiny coordinate minor.

The new theorem removes the robust strongly-hyperbolic collar from that debt. Full QFORM remains open.

## 8. Status and provenance

- Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.
- New proved supporting theorem: `QFORM-NEAR-NULL-PAIR-HALFRIESZ-v1`.
- New ambient corollary: `QFORM-OUTER-SQUARE-NEAR-NULL-PAIR-v1`.
- Continuity in the new branch: **not proved**; essentially bounded density is proved after the outer square.
- Designated partner fleet02/B04 was applied in the actual hybrid inequalities (5.1)-(5.4).
- Pointwise Fresnel decay, post-rotation independence, arbitrary-joint coarea, normalized conditional density moments, and one-good-minor selection are not used.
- Repository transport occurred; no authenticated native brain retrieval/receiver ingestion was verified, so the execution status remains `WITHOUT_VERIFIED_BRAIN`.
