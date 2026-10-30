SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-23T15:50:17Z.
attacking: non-null scalar/dependent-pair interpolation — expose the exact rank-one Schur normal left by an invertible physical pair, average the curved pair singularity against its genuine product-derived square law, and avoid every fiber supremum.

# fleet01/B06 r35 — exact rank-three Schur normal and weighted quarter-Riesz compiler

## Status

`ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_AND_ANALYTIC_THEOREMS_PROVED / NEAR-RANKONE-DETERMINANT-SINGULARITY_REDUCED / FULL_TARGET_OPEN`.

The unrestricted QFORM conjecture is **not** proved or disproved. This run treats an exact-rank-three chamber with an invertible indefinite original-coordinate physical pair. It proves an exact Schur/Pluecker identity, spends the true third direction before taking any supremum, and reduces the pair-determinant loss from the predecessor's `D^(-3/8)` to `D^(-1/8)`. It also gives a determinant-free exit whenever the exact Schur normal has one quantitatively heavy original coordinate. The remaining near-rank-one diffuse-Schur-normal chamber is stated explicitly below.

Global continuity is **not** claimed. The conclusions below are essential-density bounds. Repository transport was used; native learned-memory ingestion was not verified, so execution remains `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh controls and source-valid inputs


Corrections explicitly retained:

- no law-uniform pointwise quadratic-phase decay from a density cap;
- no independence after spectral or pair rotations;
- no unrestricted fiber supremum whose integral can grow with dimension;
- a bounded projection density alone does not control an arbitrary indefinite quadratic pushforward;
- no deletion of a small nonzero quadratic tail;
- finite half-Riesz credit for only two effective directions does not by itself imply an `L^infinity` density bound;
- a scalar square-root slice estimate without the third determinant/curvature resource is insufficient.

Two completed own/partner inputs are used at equation level.

1. **fleet01/B06 r33 quarter-Riesz pair receiver**: `yspennstate/math-open-problems@ababe93762d210413fe9f19389e3b45f5dd150ba`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260923T130129Z-fleet01-B06-QFORM/REPORT.md`. For an invertible indefinite original-coordinate physical pair `B`, `D=|det B|`, arbitrary affine terms and critical value `t0`, the pair output has the translation-uniform envelope

   `p_pair(t) <= 2 sqrt(3) D^(-3/8) |t-t0|^(-1/4)`.

2. **designated partner fleet02/B06 product-projection theorem** `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`: `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`. A unit scalar projection of an original cap-one product bank has density cap `sqrt(e)`. It is applied below to the exact Schur-normal projection `H=h^T Z` at the concrete inequality

   `||p_H||_infinity <= sqrt(e)`.

The newest fleet02/B06 r39 null-bank receiver was also read (`math-open-problems@6cd2c039236dd0ef98cd972d35be5d0752bd4c95`): its exact-null theorem and its counterexample to naive nonzero-curvature perturbation are consistent with the present mechanism. This report does **not** infer a perturbative extension from that theorem.

## 2. Exact rank-three Schur-normal identity

### Theorem 2.1 — `QFORM-EXACTR3-SCHUR-NORMAL-PLUCKER-v1`

Let

`A = R Lambda R^T`,  `R^T R = I_3`,

where `Lambda` is an invertible real diagonal `3 x 3` matrix. Fix an **original-coordinate** pair `I={i,j}` and write `J=I^c`. Put

`P=R_I` (a `2 x 3` row matrix),
`B=A_[I,I]=P Lambda P^T`,
`C=A_[I,J]`,
`D0=A_[J,J]`.

Assume `B` is invertible. Let the two rows of `P` be `p_i,p_j`, define

`c = p_i x p_j`,  `tau=||c||^2`,  `n=c/sqrt(tau)`.

Then `tau>0`, `P n=0`. Define the Schur complement

`S = D0 - C^T B^(-1) C`.

Then there is a **unit original-background coefficient vector**

`h = R_J n`,  `||h||=1`,

such that

`boxed: S = lambda h h^T`,

with the exact scalar

`boxed: lambda = det(Lambda) tau / det(B).`                 (2.1)

Equivalently,

`boxed: det(B) lambda = det(Lambda) tau.`                   (2.2)

Moreover, for every physical background coordinate `k in J`,

`boxed: det A_[I union {k}, I union {k}]
       = det(Lambda) tau h_k^2.`                            (2.3)

Consequently all these principal-triple determinants have the same sign (apart from zeros) and

`boxed: sum_(k in J) |det A_[I union {k}]|
       = |det Lambda| tau.`                                 (2.4)

#### Proof

First use the generalized Lagrange identity for two vectors in `R^3`:

`det(P Lambda P^T)
 = (p_i x p_j)^T adj(Lambda) (p_i x p_j)
 = det(Lambda) c^T Lambda^(-1)c.`                           (2.5)

Since `c=sqrt(tau)n`,

`det B = det(Lambda) tau (n^T Lambda^(-1)n).`               (2.6)

Now set

`K = Lambda - Lambda P^T B^(-1) P Lambda.`                  (2.7)

Then `P K=0`; because `K` is symmetric and `ker P=span{n}`, its range is contained in `span{n}`, hence `K=kappa n n^T` for some scalar `kappa`. Also

`K Lambda^(-1)n
 = n - Lambda P^T B^(-1) P n
 = n`,                                                        (2.8)

so

`kappa = 1/(n^T Lambda^(-1)n)
       = det(Lambda) tau/det B`                              (2.9)

by (2.6).

Because `C=P Lambda R_J^T` and `D0=R_J Lambda R_J^T`,

`S=R_J K R_J^T=kappa (R_Jn)(R_Jn)^T`.                       (2.10)

Furthermore `R^T R=P^T P+R_J^T R_J=I_3` and `Pn=0`, so

`||R_Jn||^2=n^T(I-P^TP)n=1`.                                (2.11)

This proves (2.1)-(2.2). Finally the scalar Schur determinant formula gives, for each `k in J`,

`det A_[I union {k}]
 = det B * S_kk
 = det B * lambda h_k^2
 = det(Lambda) tau h_k^2`,                                  (2.12)

which proves (2.3); summing and using `||h||=1` gives (2.4). `QED`

### Interpretation

Equation (2.4) is an aggregate-before-selection identity. The entire third-compound packet extending the fixed physical pair is exactly `|det Lambda| tau`; it cannot disappear by spreading over many physical coordinates. When it does spread, the unit vector `h` records that spread and can be treated as a genuine product-derived scalar projection rather than by summing reciprocal individual minors.

## 3. Translation-uniform quarter-potential of a square

### Lemma 3.1 — `QFORM-SQUARE-QUARTER-POTENTIAL-v1`

Let `H` have a probability density bounded by `L`. Then

`boxed: sup_(a in R) E |H^2-a|^(-1/4) <= 2 sqrt(2L).`        (3.1)

#### Proof

For any center `z`, the bathtub principle for the decreasing kernel gives

`E |H-z|^(-1/2)
 <= L int_(-1/(2L))^(1/(2L)) |x|^(-1/2) dx
 = 2 sqrt(2L).`                                             (3.2)

If `a<0`, then `|H^2-a|^(-1/4) <= |H|^(-1/2)` and (3.2) applies. If `a=r^2>=0`, then

`|H^2-r^2|^(-1/4)
 = |H-r|^(-1/4)|H+r|^(-1/4)`.

Cauchy-Schwarz and (3.2) at the two centers give

`E |H^2-r^2|^(-1/4)
 <= [E|H-r|^(-1/2) E|H+r|^(-1/2)]^(1/2)
 <= 2 sqrt(2L).`                                            (3.3)

`QED`

For the unit Schur-normal projection `H=h^T X_J`, the designated fleet02/B06 theorem gives the actual inequality

`boxed: ||p_H||_infinity <= sqrt(e).`                        (3.4)

Thus

`boxed: sup_a E|H^2-a|^(-1/4)
       <= 2 sqrt(2) e^(1/4).`                               (3.5)

No conditional density of `H` is asserted and no rotation of the random coordinates is used.

## 4. Weighted Schur-square compiler for an indefinite pair

### Theorem 4.1 — `QFORM-SCHUR-SQUARE-QUARTER-COMPILER-v1`

In Theorem 2.1 additionally assume the physical pair compression `B` is indefinite. Let

`D=|det B|`, `Lambda_det=|det Lambda|`.

Let the original coordinates be independent with densities at most one. Then the exact-rank-three quadratic form `Q=X^TAX` has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= 4 sqrt(6) e^(1/4)
    D^(-1/8) (Lambda_det tau)^(-1/4).`                       (4.1)

Numerically

`4 sqrt(6) e^(1/4) = 12.5808283506...`.

If the nonzero singular values of `A` are `s1>=s2>=s3=s>0`, then `Lambda_det=s1 s2 s3>=s^3`, hence

`boxed:
 ||p_Q||_infinity
 <= 12.581 / [ s tau^(1/4) (D/s^2)^(1/8) ].`                (4.2)

#### Proof

Partition the original random vector as `(X_I,Z)`. Since `B` is invertible,

`Q
 = (X_I+B^(-1)CZ)^T B (X_I+B^(-1)CZ)
   + Z^T S Z.`                                               (4.3)

Theorem 2.1 gives `Z^TSZ=lambda(h^TZ)^2=lambda H^2`, with

`|lambda|=Lambda_det tau/D`.                                 (4.4)

Condition on the **original** background vector `Z`. The two physical coordinates in `I` remain independent cap-one variables; the shift `B^(-1)CZ` is deterministic. The r33 indefinite-pair theorem therefore gives, uniformly in `Z` and the target level `t`,

`p_(Q|Z)(t)
 <= 2 sqrt(3) D^(-3/8)
    |t-lambda H^2|^(-1/4).`                                 (4.5)

Average (4.5) with respect to the actual background product law. By (3.5), after scaling by `|lambda|`,

`E|t-lambda H^2|^(-1/4)
 <= 2 sqrt(2)e^(1/4)|lambda|^(-1/4).`                        (4.6)

Therefore

`||p_Q||_infinity
 <=4 sqrt(6)e^(1/4)D^(-3/8)|lambda|^(-1/4)
 =4 sqrt(6)e^(1/4)D^(-1/8)(Lambda_det tau)^(-1/4),`           (4.7)

which is (4.1). `QED`

### What was gained

The r33 conditional pair envelope by itself carries `D^(-3/8)`. Spending the **exact third Schur direction** against its genuine product-projection weight cancels a factor `D^(1/4)`, leaving only `D^(-1/8)`. This is a source-level weighted replacement for a curved-fiber maximum. It does not invoke the newly refuted implication that two-direction half-Riesz control alone yields `L^infinity`: the third rank-one Schur direction is used explicitly in (4.6).

## 5. Heavy Schur-normal coordinate gives a determinant-free exit

Let

`eta = max_(k in J) h_k^2.`                                        (5.1)

From (2.3) there is an actual original coordinate `k_*` such that

`|det A_[I union {k_*}]|
 = Lambda_det tau eta.`                                            (5.2)

Apply r33 `QFORM-PHYSICAL-TRIPLE-DET-ONLY-v1` to that original-coordinate principal triple. Its constant is

`C3 = 16 * 2^(1/4) * sqrt(30)
    = 104.216889989...`.

Thus

`boxed:
 ||p_Q||_infinity
 <= C3 (Lambda_det tau eta)^(-1/3)
 <= 104.217/[s (tau eta)^(1/3)].`                          (5.3)

This branch is independent of `D`: a near-singular physical pair is harmless if the exact Schur normal has a quantitatively heavy original coordinate.

Combining (4.2) and (5.3), every invertible indefinite physical pair in an exact-rank-three target has the certified bound

`boxed:
 ||p_Q||_infinity <= (1/s) min{
  12.581 tau^(-1/4)(D/s^2)^(-1/8),
  104.217 (tau eta)^(-1/3)
 }.`                                                           (5.4)

At the exact rank-one endpoint `D=0`, predecessor r34 supplies the separate parabolic receiver whenever the null-star is nonzero. Thus the remaining discontinuity is now confined to a simultaneous **near-rank-one + diffuse-Schur-normal** chamber, not the entire determinant-degenerate region.

## 6. First unpaid implication

`QFORM-DIFFUSE-SCHUR-NORMAL-NEARRANKONE-v1`:

In an exact-rank-three target, suppose an original physical pair is invertible indefinite, has useful spectral row area `tau`, but its normalized determinant `D/s^2` is very small and its exact Schur normal is diffuse (`eta=max h_k^2` small). Prove a determinant-free bound by aggregating the original product source behind the two shear projections together with `H=h^TZ` **before** any pair-fiber supremum. The exact identities above show the third resource is not missing: its total principal-triple packet is `Lambda_det tau`; it is merely distributed through `h`.

A valid next receiver must retain the dependence among the two shear projections and `H`. A bounded marginal projection theorem alone is insufficient, and a small nonzero second pair eigenvalue may not be deleted as a perturbation. Candidate mechanism: a three-form product-projection/Fresnel integral in which the `D^(-1/8)` from (4.1) is canceled by the increasing Schur scale `|lambda|=Lambda_det tau/D` without compressing the source to an arbitrary joint density.

The full arbitrary-dimensional theorem has an additional extension debt: arbitrary higher-rank/small spectral tails must be retained, not convolved away as independent noise.

## 7. Checks and scope

A deterministic numerical identity check on random exact-rank-three matrices verifies (2.1)-(2.4) to machine precision; details are in `CHECKS.md`. This is only an algebra/scaling check, not independent proof review.

No counterexample to QFORM was found. Independent end-to-end review of the new r35 identities/compiler is pending. The full arbitrary-dimensional QFORM conjecture remains **OPEN**, and the requested global continuous-density conclusion remains **OPEN**.
