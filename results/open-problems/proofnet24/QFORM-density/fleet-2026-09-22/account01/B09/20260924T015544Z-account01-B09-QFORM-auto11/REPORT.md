SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-24T01:55:44Z.
attacking: the exact singular-pair/rank-one-cross branch with arbitrary same-leaf curvature, using a literal physical-pivot completion and conditional square-plus-linear anti-concentration.

# account01/B09 — rank-one pair with arbitrary same-leaf curvature

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Bilinear block mechanism / GEOMETRY  
Run: `20260924T015544Z-account01-B09-QFORM-auto11`  
Status: **ESSENTIAL STEP APPLIED / NEW SUPPORTING THEOREM / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN / not proved / not disproved. Full-target continuity remains OPEN. This report closes the *analytic* arbitrary-leaf-curvature obstruction at an exact rank-one physical pair and exact rank-one pair-to-leaf cross block, at a quantitative price depending only on the physical pair eigenvalue and the physical kernel-star scale. It then uses the three-large-eigenvalue hypothesis to make that price universal whenever the leaf-block operator norm is bounded away from one.

No random coordinate rotation is made, no moment/support/log-concavity hypothesis is used, and no leaf quadratic term is discarded as a small random error.

## 1. Source-pinned premises and corrections


Corrections respected here include: no law-uniform pointwise quadratic-phase decay; no independence after spectral rotation; no dimension-free conclusion from naive fiber suprema; no inference of a uniformly large physical minor from aggregate Frobenius mass; and no deletion of a small matrix coefficient as a small random quadratic perturbation.

Two mathematical dependencies are used.

1. Previous account01/B09 exact singular-pair ledger, source
   `yspennstate/math-open-problems@b6ecc365cd6c0b38adc73872dec204ab5d4e3059`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260924T005202Z-account01-B09-QFORM-auto11/REPORT.md`.
   For an exact rank-one physical pair and rank-one pair-to-leaf cross, it proves the anchored compound identity and the exact relation `P_H+Omega_(2,H)=tau^2 s^4` in the notation below.

2. Designated partner account02/B09 r15, source
   `yspennstate/math-open-problems@57b57dc6fa114b1c782a91599bdfbe94a358b2cb`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T224553Z-account02-B09-QFORM-r15/REPORT.md`.
   Besides its square-hyperbola theorem, it uses the reviewed one-dimensional product-projection estimate
   `||p_(r^T X)||_infinity <= sqrt(2)/||r||_2`
   for independent cap-one coordinates, and proves the zero-active-leaf collinear-star bound `<=6` in its exact rank-one-pair scope.

## 2. Setup

Let `H={h1,h2}` be two literal original coordinates and `L=H^c`. Assume

`B=A[H,H]=tau ell ell^T`,  `tau != 0`,  `||ell||_2=1`,

and assume the physical pair-to-leaf cross block has rank one,

`A[H,L]=g r^T`,  `r != 0`.

Let `k` be a unit vector perpendicular to `ell` and assume the kernel-star is nonzero,

`k^T g != 0`.

The leaf block

`D=A[L,L]`

is completely arbitrary symmetric. We also permit an arbitrary affine term; this is useful after conditioning other disjoint original coordinates in a larger argument.

Define the physical kernel-star scale

`s = ||A[L,H] k||_2 = |k^T g| ||r||_2 >0`.                 (2.1)

## 3. Literal physical-pivot completion

Relabel the two physical hub coordinates, if necessary, so that

`|ell_1| >= |ell_2|`, hence `|ell_1| >= 1/sqrt(2)`.            (3.1)

This is only a permutation of original independent coordinates. Write

`ell=(ell_1,ell_2)`, `g=(g_1,g_2)`,
`a=tau ell_1^2`, `b=tau ell_1 ell_2`, `c=tau ell_2^2=b^2/a`,
`W=r^T X_L`.

For clarity first omit affine terms. The hub and cross part is

`a X_1^2 + 2b X_1 X_2 + c X_2^2 + 2g_1 X_1 W + 2g_2 X_2 W`.

Complete the square in the **literal physical coordinate** `X_1`:

`= a [X_1+(b/a)X_2+(g_1/a)W]^2
   + 2 beta W X_2 - (g_1^2/a)W^2`,                         (3.2)

where

`beta = g_2-(b/a)g_1
      = (ell_1 g_2-ell_2 g_1)/ell_1
      = (k^T g)/ell_1`                                     (3.3)

for the orientation `k=(-ell_2,ell_1)`.

All of the arbitrary leaf curvature is retained inside

`R(X_L)=X_L^T D X_L-(g_1^2/a)W^2`.

With arbitrary affine terms, the same completion has the form

`Q = a U^2 + (2 beta W+eta) X_2 + R_1(X_L)`,                (3.4)

where

`U=X_1+(b/a)X_2+(g_1/a)W+constant`,

`eta` is a constant (or a fixed value after conditioning a disjoint bank), and `R_1` is an arbitrary measurable function of the leaf variables for purposes of the next estimate. Thus the proof in fact needs no quadratic structure from `R_1`.

Crucially, the change `X_1 -> U` is a unit-Jacobian shear **inside the two physical hub variables**. It does not assert independence of rotated variables.

## 4. Conditional square-plus-linear anti-concentration

Fix the entire leaf vector `X_L=z`; write `w=r^T z` and

`K=2 beta w+eta`.

For fixed `z`, the joint density of `(U,X_2)` is

`f_1(U-(b/a)X_2-(g_1/a)w-constant) f_2(X_2)`,

so it is bounded by `f_2(X_2)` pointwise.

For a target `t`, resolve the equation

`a U^2 = t-R_1(z)-K X_2`.

At a fixed `X_2=v`, summing the two possible roots in `U` and using `f_1<=1` gives the density contribution

`<= |a|^(-1/2) f_2(v)
    1_{correct half-line} |t-R_1(z)-Kv|^(-1/2)`.             (4.1)

The following one-sided bathtub bound is exact enough for our purpose. If `f` is a probability density with `0<=f<=1` and `K!=0`, then

`sup_c int f(v) 1_{correct side} |c-Kv|^(-1/2) dv
 <= 2 |K|^(-1/2)`.                                          (4.2)

Indeed, after the change `y=Kv`, the pushed-forward density has cap `1/|K|` and mass one; a decreasing one-sided kernel `y_+^(-1/2)` is maximized by filling the interval adjacent to zero, giving

`(1/|K|) int_0^{|K|} y^(-1/2)dy =2|K|^(-1/2)`.

Therefore, for every fixed leaf vector with `K!=0`,

`boxed:
 ||p_(Q | X_L=z)||_infinity
 <= 2 |a|^(-1/2) |2 beta w+eta|^(-1/2).`                    (4.3)

No leaf-curvature quantity appears.

## 5. Average the physical kernel-star before paying a reciprocal scale

The product-projection estimate from the reviewed partner dependency gives

`||p_W||_infinity <= S := sqrt(2)/||r||_2`.                  (5.1)

Hence `Y=2 beta W+eta` has density cap

`D_Y <= S/(2|beta|)`.                                       (5.2)

For every one-dimensional probability density bounded by `D`, the symmetric bathtub estimate gives

`E |Y|^(-1/2) <= 2 sqrt(2D)`.                               (5.3)

Applying (5.3) to (5.2),

`E |2 beta W+eta|^(-1/2)
 <= 2 sqrt(S/|beta|)`.                                      (5.4)

The exceptional event `2 beta W+eta=0` has probability zero because `W` has a density. Averaging (4.3) and using (5.4) yields

`||p_Q||_infinity
 <=4 |a|^(-1/2) sqrt(S/|beta|)
 =2^(9/4) |a beta|^(-1/2) ||r||_2^(-1/2).`                  (5.5)

By (3.3),

`|a beta|=|tau| |ell_1| |k^T g|`.

Using (3.1) and (2.1), we obtain the main theorem.

### Theorem `QFORM-RANKONEPAIR-ARBITRARY-LEAFCURVATURE-v1`

Under the setup of section 2, for arbitrary symmetric leaf block `D` and arbitrary affine terms,

`boxed:
 ||p_Q||_infinity
 <= 2^(5/2) (|tau| s)^(-1/2).`                               (5.6)

Equivalently, every interval `I` satisfies

`boxed:
 P{Q in I}
 <= 2^(5/2) (|tau|s)^(-1/2) |I|.`                           (5.7)

This proves an essentially bounded density. **Continuity is not claimed** by this argument.

The theorem directly removes the previous B09 analytic obstruction that arbitrary same-active-leaf curvature might destroy the collinear singular-pair receiver. It does not by itself make `|tau|s` universal under the full target.

## 6. Target-level corollary when the leaf curvature is below the spectral scale

Let

`A_0 = [[B, g r^T], [r g^T, 0]]`,

so `A=A_0+diag(0_H,D)`. Put

`d=||D||_op`.

Assume the owner's target `s_3(A)>=1` and `d<1`. Weyl stability of singular values gives

`s_3(A_0) >= 1-d >0`.                                       (6.1)

Thus `A_0` has rank exactly three on the invariant physical subspace `H + span{r}`.

Two literal test vectors bound its smallest nonzero singular value from above:

1. Extend the unit hub-kernel vector `k` by zero on `L`. Then
   `||A_0 k||=s`, hence `s_3(A_0)<=s`.
2. Choose a unit vector `h in H` perpendicular to `g`. Then the leaf component of `A_0h` vanishes and `||A_0h||=||Bh||<=|tau|`, hence `s_3(A_0)<=|tau|`.

Combining with (6.1),

`s>=1-d`, `|tau|>=1-d`, and therefore `|tau|s >=(1-d)^2`.     (6.2)

Substitution into (5.6) gives:

### Corollary `QFORM-RANKONEPAIR-SMALL-LEAFBLOCK-v1`

If, in addition, `s_3(A)>=1` and `||D||_op=d<1`, then

`boxed:
 ||p_Q||_infinity <= 2^(5/2)/(1-d),`                         (6.3)

and

`boxed:
 P{Q in I} <= [2^(5/2)/(1-d)] |I|.`                         (6.4)

In particular, if `||D||_op<=1/2`,

`boxed: ||p_Q||_infinity <=2^(7/2)=11.313708499... .`        (6.5)

Again continuity is not claimed.

This is a genuine target-level branch: the only extra condition is a quantitative property of the physical leaf block used to define the branch, not an input-law assumption.

## 7. Macroscopic overlap-two consequence: the remaining chamber is forced to have large leaf curvature

From the preceding B09 exact anchored-compound identity, at this exact rank-one pair/rank-one cross geometry,

`P_H+Omega_(2,H)=tau^2 s^4`.                                 (7.1)

Therefore

`Omega_(2,H) <= tau^2 s^4`.                                  (7.2)

Suppose the anchored overlap-two mass is already macroscopic,

`Omega_(2,H)>=1/4`.

Then

`|tau|s^2>=1/2`.                                              (7.3)

There are now two alternatives.

- If `|tau|s>=1/4`, Theorem (5.6) gives

  `boxed: ||p_Q||_infinity <=2^(7/2)<11.314.`                 (7.4)

- If `|tau|s<1/4`, divide (7.3) by this inequality to get

  `s>2`, and then `|tau|<1/8`.                               (7.5)

  Since `s_3(A_0)<=|tau|<1/8` while `s_3(A)>=1`, Weyl forces

  `boxed: ||D||_op > 7/8.`                                   (7.6)

Thus at macroscopic overlap-two scale, the exact singular-pair/rank-one-cross endpoint is now reduced to a sharply defined chamber:

`boxed:
 either ||p_Q||_infinity<11.314,
 or |tau|<1/8, s>2, and ||D||_op>7/8.`                        (7.7)

The second branch contains a genuinely large same-leaf quadratic direction; the next proof step should spend that curvature through a disjoint crossing, one-shared overlap, mixed-hub receiver, or a new direct large-leaf-curvature theorem. The arbitrary leaf block is no longer an analytic obstacle by itself.

## 8. Required account02/B09 result applied to an actual target inequality

Use the stress family from the previous B09 run. For any `m>=2`, let

`B=diag(1,0)`, `g=e_2`,
`r=m^(-1/2)(1,...,1)`,
`D=t vv^T`,

where `v` is any unit vector perpendicular to `r` and `t` is arbitrary real. The exact nonzero spectrum is

`{1,+1,-1,t}`

(with the `t=0` zero omitted), so the owner target holds for **every real `t`**.

At `t=0`, the completed designated partner theorem `QFORM-RANKONE-PAIR-COLLINEAR-STAR-v1` applies with `tau=1` and `s=1` and gives the actual target inequality

`boxed: ||p_(Q_0)||_infinity <=6`,
`boxed: P{Q_0 in I}<=6|I|.`                                  (8.1)

The new theorem keeps the entire leaf curvature `t vv^T` and gives, uniformly for every real `t`,

`||p_(Q_t)||_infinity <=2^(5/2)=5.656854250... .`             (8.2)

Because this example has `|ell_1|=1`, retaining the sharper physical-pivot constant in (5.5) improves (8.2) to

`boxed:
 ||p_(Q_t)||_infinity <=2^(9/4)
 =4.756828460...,
 P{Q_t in I}<=2^(9/4)|I|`                                    (8.3)

for every real `t`.

Thus the arbitrary dense leaf-curvature stress family that was explicitly left unpaid in the previous B09 report is now fully paid, uniformly through all `t`. The result is stronger than the partner's `t=0` bound on this family while genuinely using the partner theorem at (8.1) as the required completed-result application.

## 9. Scope, continuity, and next implication

This run does **not** prove the unrestricted conjecture. The new theorem is exact for the singular rank-one physical-pair / rank-one pair-to-leaf-cross geometry; a near-rank-one pair remains a quantitative passage. The theorem gives an essentially bounded density and a linear interval estimate, but continuity is not established by this real-variable mixture argument.

The first unpaid B09 implication is now

`QFORM-SINGULARPAIR-LARGE-LEAFCURVATURE-EXIT-v1`:

> In the exact singular-pair/rank-one-cross branch, after the new receiver, a macroscopic overlap-two packet can remain unpaid only when the pair eigenvalue is small, the kernel-star is large, and the same-leaf block has genuinely large operator norm (`|tau|<1/8`, `s>2`, `||D||_op>7/8` at the normalization above). Spend that large leaf curvature through a literal disjoint crossing / one-shared packet / mixed-hub theorem, or prove a direct three-resource inequality. Do not infer a uniformly large single physical minor from Frobenius mass, and do not delete a small coefficient matrix as a random perturbation.

No valid full-target counterexample was found in this run.
