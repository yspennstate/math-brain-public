# fleet02/B05 — two-sheet hybrid obstruction, aggregate-bank repair, and the full-eigenbank peel

**Run:** `20260923T032012Z-fleet02-B05-QFORM-29fa25e8`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Quadratic coarea bound / complementary constructions and source-valid counterexamples  
**Status:** `ESSENTIAL_STEP_APPLIED / CANDIDATE_REFUTED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not claimed below; only essential boundedness / interval-density consequences are used.

## 0. First unpaid implication

The previous B05 checkpoint already made the newest ruled one-sheet calculation rigorous for arbitrary measurable cap-one product laws by smooth approximation and Portmanteau at the interval level. The current differentiated B05 assignment therefore begins on the opposite, convex/two-sheet side.

The first unpaid implication attacked here is

`QFORM-TWOSHEET-NONEIGEN-NEARISOTROPIC-v1`:

> after aggregate-bank extraction in an exact-rank-three indefinite state, control the regime in which the scalar-bank compression is singular or nearly isotropic **and** no rank-one bank carries an entire true spectral eigenline. A proof may not fall back to a reciprocal physical pivot, an unrestricted fibre supremum, or a conditional density cap.

This report proves that three tempting physical-coordinate certificates are not exhaustive even in exact rank three, applies the designated fleet03/B05 aggregate theorem to the resulting family, and then removes the apparent near-isotropic loss whenever one scalar bank is in fact a complete eigenbank.

## 1. Fresh sources actually applied

Required newest-Claude source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

from `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

I use its proved ruled one-sheet theorem from `COUNTEREXAMPLE_SEARCH.md`: for exact rank three with signature `(+,+,-)` and all three eigenvalue magnitudes at least one,

`ess sup_(t>=0) p_Q(t) <= pi sqrt(2)`.

This is used only on the one-sheet side; the construction below targets `t<0`.

The designated completed partner is fleet03/B05 `QFORM-ONE-RANK2-TWO-RANK1-BANK-COAREA-v1`, run `20260922T223741Z-fleet03-B05-QFORM-r19`, pinned at

`yspennstate/math-open-problems@70f181cf738aa51ee6fb7043a329ac9e8b22c4ec`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260922T223741Z-fleet03-B05-QFORM-r19/REPORT.md`.

For one spectral-rank-two original product bank and two spectral-rank-one original product banks, with indefinite invertible scalar-bank compression `B`, `kappa=sigma_min(B)`, and aggregate principal-determinant mass `mu`, it proves

`||p_Q||_infinity <= 8*2^(3/4)*sqrt(5)*(kappa*mu)^(-1/4)`.      (1.1)

The newer partner checkpoint `20260923T024819Z-fleet03-B05-QFORM-auto11`, commit `fcec29b7bb07e62686f004d85d77e1c73c89f9c7`, proves the physical-pair `L^p` receiver

`||p_Q||_infinity
 <=2^(11/4)(D*kappa)^(-1/4)
   ||p_R||_p^[p/(4(p-1))],  p>=2`,                            (1.2)

with pair translations allowed to depend arbitrarily on the residual environment. I use (1.2) below to show that better residual smoothing does not cure the physical-pair loss in the stress family.

Finally, the complete orientation-free rank-two fractional theorem at

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

proves, when the affine term lies in the rank-two range (in particular when it is zero),

`sup_t E |R-t|^(-1/2)
 <=16 sqrt(30) |det Lambda_2|^(-1/4)`.                       (1.3)

This is the receiver for the new eigenbank peel in Section 5.

No result below uses independence after spectral rotation, arbitrary-joint coarea, pointwise law-uniform oscillatory decay, a worst conditional projection-density supremum, or a uniformly good physical minor.

## 2. A non-coloop exact target family

Fix

`1/2<c<1`, `0<beta<1`, and an integer `m>=1`.

Let `R` be an `(1+4m) x 3` matrix whose rows are the following original-coordinate spectral rows.

**The positive `e_1` bank `G_2`:**

one heavy row

`h=sqrt(c) e_1`,

and `m` tail rows

`a_j=sqrt((1-c)/m) e_1`, `j=1,...,m`.

Thus this bank has total Gram mass exactly `e_1e_1^T`, but no row is a coloop because `c<1`.

**The rank-two mixed bank `G_1`:** for each `k=1,...,m`, two rows

`u_(k,+)=(0,1/sqrt(2m), +sqrt((1-beta)/(2m)))`,

`u_(k,-)=(0,1/sqrt(2m), -sqrt((1-beta)/(2m)))`.

Their total Gram matrix is

`diag(0,1,1-beta)`.

**The diffuse minority bank `G_3`:** `m` rows

`v_k=sqrt(beta/m) e_3`,

whose total Gram matrix is `beta e_3e_3^T`.

Hence, exactly,

`R^T R=I_3`.                                                   (2.1)

Take

`Lambda=diag(1,1,-1)`, `A=R Lambda R^T`.                      (2.2)

Because `R` is an isometry from the spectral three-space, the nonzero eigenvalues of `A` are exactly

`{1,1,-1}`                                                     (2.3)

for every `m,c,beta`. Thus (2.2) is a genuine target family in arbitrarily large dimension.

Its physical diagonals are

`A_hh=c`,

`A_(a_j,a_j)=(1-c)/m`,

`A_(u,u)=beta/(2m)` for every mixed row,

`A_(v_k,v_k)=-beta/m`.                                        (2.4)

In particular, **every minority-sign physical diagonal tends to zero like `1/m`**, while the largest row leverage is the fixed value `c>1/2`.

## 3. Why the obvious physical two-sheet exits are not exhaustive

### 3.1 Full-frame low leverage fails

The newest-source Fresnel/Brascamp-Lieb rank-three exit requires every full-frame leverage to be at most `1/2`. The heavy row has leverage `c>1/2`, so that theorem is deliberately outside its hypothesis.

### 3.2 Every minority physical pivot is near-null

The only negative physical diagonals are the `v_k`, each of magnitude `beta/m`. Any single-minority-pivot cone compiler therefore pays a factor at least of order

`(m/beta)^2`.                                                  (3.1)

More strongly, take the obvious indefinite physical pair consisting of the heavy row `h` and one `v_k`. Its pair matrix is diagonal:

`B_phys=diag(c,-beta/m)`.                                      (3.2)

For `m` large enough that `beta/m<=c`,

`D=|det B_phys|=c beta/m`,

`kappa=sigma_min(B_phys)=beta/m`,

so the current partner `L^p` receiver (1.2), even if the completed residual has an arbitrarily strong dimension-free `L^p` bound, carries the unavoidable physical-pair factor

`(D*kappa)^(-1/4)
 =c^(-1/4) beta^(-1/2) sqrt(m)`.                              (3.3)

Thus better smoothing of the residual does not remove the selected-pair tax.

### 3.3 The valid aggregate physical cone cover still costs `sqrt(m)`

Use the completed curvature-weighted physical-fibre cone theorem `QFORM-CURVATURE-WEIGHTED-PHYSICAL-FIBER-COVER-v1` from fleet01/B06. Here `Lambda^2=I`, so every transverse determinant factor equals one, and every product-fibre factor `M_i` is at least one.

For the two-sheet cone, the strict minority-axis vector `z=e_3` is admissible. Any cone-cover weights `a_i>=0` must therefore satisfy

`sum_i a_i r_(i3)^2 >=1`.                                     (3.4)

The exact cost is at least `sum_i a_i q_i`, where `q_i=||r_i||`. For rows seeing `e_3`,

minority-bank rows have

`q_i/r_(i3)^2 = sqrt(m/beta)`,                                (3.5)

while mixed rows have

`q_i/r_(i3)^2
 =sqrt(2m(2-beta))/(1-beta)`.                                 (3.6)

Therefore the optimal cone-cover currency satisfies the rigorous lower bound

`Gamma_-(R,Lambda)
 >=sqrt(m) * min{ beta^(-1/2), sqrt(2(2-beta))/(1-beta) }`.    (3.7)

For every fixed `beta in (0,1)`, this diverges like `sqrt(m)`.

So the natural shortcut

`low full-frame leverage OR one non-null minority pivot OR bounded physical cone-cover cost`

is **not exhaustive**, even for exact rank three with spectrum `{1,1,-1}`.

This is a mechanism counterexample, not a counterexample to QFORM.

## 4. The designated partner theorem pays the same family before physical inversion

Use the three banks from Section 2.

`G_1` has genuine spectral rank two, spanning `e_2,e_3`.

`G_2` is a rank-one `e_1` bank with total coefficient-square mass one, despite containing a heavy physical row.

`G_3` is a diffuse rank-one `e_3` bank with total coefficient-square mass `beta`.

In the partner notation,

`t_2=e_1`, `t_3=sqrt(beta)e_3`,

and the scalar-bank quadratic compression is

`B=diag(1,-beta)`.                                           (4.1)

Hence

`D=beta`, `kappa=beta`.                                      (4.2)

The aggregate determinant mass is also exact. By the rank-three principal-minor identity,

`|det A_{ {i,j,k},{i,j,k} }|
 =|det Lambda| det(r_i,r_j,r_k)^2`.

Summing over `i in G_1`, `j in G_2`, `k in G_3` factors the squared determinant mass into the total `e_2`, `e_1`, and `e_3` bank masses, namely

`mu=1*1*beta=beta`.                                          (4.3)

Applying the completed fleet03/B05 theorem (1.1) gives

`||p_Q||_infinity
 <=8*2^(3/4)*sqrt(5) beta^(-1/2)`,                           (4.4)

**independent of `m` and of the heavy-row parameter `c`**.

At `beta=1/2`,

`||p_Q||_infinity
 <=8*2^(5/4)*sqrt(5)
 =42.5463671755...`.                                         (4.5)

The required newest-source ruled theorem simultaneously gives the sharper one-sheet estimate

`ess sup_(t>=0) p_Q(t) <=pi sqrt(2)=4.4428829381...`.         (4.6)

Thus the two-sheet family that defeats all three physical-coordinate currencies in Section 3 is uniformly controlled once the diffuse minority bank is aggregated **before** local pair inversion or cone-cover payment.

## 5. New supporting theorem: a complete eigenbank removes the near-isotropic loss

The factor `beta^(-1/2)` in (4.4) blows up as the scalar-bank compression becomes singular. In the family above this blow-up is not genuine, because `G_2` carries an entire true eigenline. The following simple but useful theorem records the exact repair.

### Theorem — `QFORM-FULL-EIGENBANK-PEEL-v1`

Let

`A=R diag(lambda_1,lambda_2,lambda_3) R^T`, `R^TR=I_3`,

with all `|lambda_j|>=s>0`. Suppose there is an original-coordinate bank `G` such that

`r_i=c_i e_1` for every `i in G`,

and

`sum_(i in G)c_i^2=1`.                                      (5.1)

Then for arbitrary independent original-coordinate densities bounded by one,

`boxed:
 ||p_(X^TAX)||_infinity
 <=16 sqrt(60)
   |lambda_1|^(-1/2)|lambda_2 lambda_3|^(-1/4)
 <=16 sqrt(60)/s.
`                                                               (5.2)

No moment, support, centering, connectedness, smoothness, or post-rotation independence is assumed.

#### Proof

Because the spectral columns of `R` are orthonormal and the bank in (5.1) already carries the full unit `e_1` Gram mass, every row outside `G` has zero first spectral component. Therefore the quadratic form splits exactly into independent original-coordinate banks:

`Q=lambda_1 U^2 + R_2`,                                      (5.3)

where

`U=sum_(i in G)c_i X_i`,                                     (5.4)

and `R_2` is a rank-two quadratic form on the complementary original coordinates with orthonormal spectral frame and eigenvalues `lambda_2,lambda_3`.

The Rogozin--Ball scalar projection theorem gives

`||p_U||_infinity <=sqrt(2)`                                 (5.5)

because the coefficient vector `(c_i)` has Euclidean norm one. Put `V=sqrt(2)U`; then `V` has density cap one and

`Q=(lambda_1/2)V^2+R_2`.                                     (5.6)

The completed rank-two theorem (1.3), with zero affine term, gives

`sup_t E|R_2-t|^(-1/2)
 <=16 sqrt(30)|lambda_2 lambda_3|^(-1/4)`.                   (5.7)

For a cap-one scalar `V`, the translated square kernel satisfies

`p_((lambda_1/2)V^2)(w)
 <=sqrt(2/|lambda_1|)|w|^(-1/2)`                             (5.8)

on the appropriate half-line. Convolving (5.8) against the law of the independent residual `R_2` and applying (5.7) proves

`||p_Q||_infinity
 <=sqrt(2/|lambda_1|)*16 sqrt(30)
   |lambda_2 lambda_3|^(-1/4)`,

which is (5.2). QED.

### Application to the stress family

The complete `e_1` bank `G_2` in Section 2 satisfies (5.1), even though its heaviest single row has leverage `c>1/2` and no physical coordinate is a coloop. Hence for **every** `0<beta<1`, every `m`, and every `1/2<c<1`,

`||p_Q||_infinity <=16 sqrt(60)=123.9354670786...`.           (5.9)

Consequently the `beta->0` near-isotropic endpoint of this entire family is already paid by rerouting through the complete eigenbank, rather than by trying to keep `kappa` bounded below.

This sharpens the genuine remaining near-isotropic debt: small `kappa` is only intrinsically unpaid when no scalar product bank can be recognized as a complete true eigenbank (or another already-paid peel).

## 6. What changed in the proof map

This run establishes two concrete facts.

First, **physical-coordinate exhaustiveness is false** on the two-sheet side. A fixed heavy majority row, vanishing minority diagonals, and a cone-cover cost growing like `sqrt(m)` can coexist in an exact target family, while an aggregate determinant packet stays constant and the designated partner theorem controls the law uniformly.

Second, **near-isotropic aggregate compression is not itself the final obstruction**. If one scalar bank carries a complete eigenline, `QFORM-FULL-EIGENBANK-PEEL-v1` removes the small-`kappa` loss uniformly using the rank-two half-Riesz receiver.

The first genuinely unpaid implication is therefore narrower:

`QFORM-TWOSHEET-NONEIGEN-NEARISOTROPIC-v1`:

> in an exact-rank-three indefinite survivor with no diffuse-volume exit and no complete eigenbank peel, show that aggregate bank geometry supplies a uniformly nondegenerate scalar compression, or directly spend the rank-two bank's embedded third curvature when every available scalar compression is singular/near-isotropic.

The newer partner `L^p` bridge proves that residual roughness alone is not this missing factor: once a physical pair has stable `D*kappa`, even an `L^p` residual is enough; conversely, equation (3.3) shows that no amount of residual `L^p` smoothing repairs a pair whose geometric currency decays like `m^-2`.

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`.

## 7. Exact checks

Two deterministic regression scripts are saved with this report.

`check_twosheet_hybrid.py` checks the simpler coloop stress family from the early checkpoint.

`check_noncoloop_hybrid.py` checks the stronger non-coloop family at `c=3/4`, `beta=1/2` for `m=1,2,3,10,100`: `R^TR=I`, nonzero spectrum `{-1,1,1}`, maximum leverage `3/4`, minimum physical diagonal `-1/(2m)`, and the exact cone-cost lower bound `sqrt(2m)`. Its executed output is in `noncoloop_check.txt` and ends `PASS`.

The checks are regression evidence only. Equations (2.1)--(5.9) are analytic and do not depend on finite computation.
