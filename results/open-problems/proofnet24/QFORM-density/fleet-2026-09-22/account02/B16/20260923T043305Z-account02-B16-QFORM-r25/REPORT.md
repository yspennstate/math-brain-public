# QFORM account02/B16 r25 — near-null square-peel logarithmic barrier

Status: **PROVED INTERMEDIATE-MECHANISM OBSTRUCTION + SOURCE-VALID PAID CONTROL; FULL QFORM OPEN.**

Programme: `QFORM-DENSITY-3EIG-20260922`.  Role: projection-product interaction / complementary source-valid constructions.  Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication attacked

The latest completed designated-partner result available at the start of this derivation is account03/B16 r23, `QFORM-MIXED-PLUECKER-DOMINANT-STAR-v1`, canonical source

`yspennstate/math-open-problems@7e5413dce1b8aeab65d5a7663a3ede11a8e70f82:proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T025235Z-account03-B16-QFORM-r23/REPORT.md`.

Its unpaid exact-rank-three chamber contains a dominant original-coordinate star with leverage

`c_i > 643/7936`,

normalized Rayleigh coefficient

`|alpha_i| < 31/10288`,

cross-plane coupling `||beta_i|| > 0.999995`, a mixed Pluecker packet `>643/7936`, and every residual transverse leverage at most `1/2`.  The partner explicitly identifies the missing operation as an `L^infinity` transducer stable for small nonzero `alpha_i`, without replacing product provenance by a conditional density cap.

This report tests the most natural continuation: complete the small scalar pivot and then pay the exact one-sided square kernel / rank-two half-Riesz remainder.  The conclusion is negative in a target-valid family lying inside the partner geometry: **the exact cap-only square-envelope certificate itself diverges logarithmically as the pivot tends to zero, although the true density stays uniformly below 7.56 by the completed mixed-Fresnel theorem.**  Thus the loss is not merely the earlier crude `|alpha|^{-1/4}` determinant estimate.

## 2. Target-valid same-bank family

Fix any even `m >= 128` (one may take `m` arbitrarily large).  Let

`X_0,X_1,...,X_m`

be independent `Uniform[-1/2,1/2]` variables.  Choose balanced signs `eps_j in {+1,-1}` with exactly `m/2` of each sign, and set

`Y = m^{-1/2} sum_{j=1}^m X_j`,

`Z = m^{-1/2} sum_{j=1}^m eps_j X_j`.

The coefficient vectors of `Y` and `Z` are orthonormal, but **Y and Z are not asserted independent**: they are projections of the same original leaf product law.

For `delta>0` put

`c_delta = sqrt(1+delta)`

and

`Q_delta = delta X_0^2 + 2 c_delta X_0 Y + Z^2`.                         (2.1)

On the orthonormal three-dimensional range coordinates `(X_0,Y,Z)`, the quadratic matrix is

`B_delta = [[delta,c_delta,0],[c_delta,0,0],[0,0,1]]`.

The top-left two eigenvalues solve

`lambda^2-delta lambda-(1+delta)=0`,

hence are `1+delta` and `-1`.  Therefore

`spec_nonzero(Q_delta) = {1+delta,-1,1}`.                                (2.2)

Every `Q_delta` is an exact-rank-three instance of the full target, for every `delta>0`.

The physical hub coordinate has range leverage one.  Relative to the hub direction, every leaf has transverse leverage

`h_j = (1/sqrt(m))^2 + (eps_j/sqrt(m))^2 = 2/m <= 1/64`.                 (2.3)

Every nonzero rank-three Pluecker basis consists of the hub and two leaves, so the disjoint-basis mass is zero and the HLL packet of the hub has mass one.  The normalized hub Rayleigh coefficient is exactly `alpha_0=delta`, while the cross-plane coupling has norm `c_delta>1`.  Thus for sufficiently small `delta` this family satisfies the quantitative dominant-near-null-star / transverse-diffuse conditions isolated by account03/B16 r23 (indeed with stronger packet and leverage values).

## 3. The projected pair is dependent, with explicit product provenance

Let

`A_+ = m^{-1/2} sum_{eps_j=+1} X_j`,

`A_- = m^{-1/2} sum_{eps_j=-1} X_j`.

The two variables `A_+,A_-` are genuinely independent because they use disjoint original-coordinate banks, and

`Y=A_++A_-`,  `Z=A_+-A_-`.                                               (3.1)

Let `p_m` denote their common one-dimensional density.  It is a compactly supported continuous convolution density, strictly positive in the interior of its support.  The change of variables in (3.1) gives the exact joint density

`rho_m(y,z) = (1/2) p_m((y+z)/2) p_m((y-z)/2)`.                           (3.2)

Its support is a diamond rather than the Cartesian product of the marginal supports, so `(Y,Z)` is not independent.  Equation (3.2), rather than any post-rotation independence claim, is what will be used below.

Choose constants `eta_m in (0,1/2]` and `kappa_m>0` such that

`p_m(a) >= kappa_m` for `|a|<=eta_m`.

Such constants exist by continuity and positivity at zero.  Hence

`rho_m(y,z) >= kappa_m^2/2` whenever `|y|,|z|<=eta_m`.                    (3.3)

Separately, the standard two-dimensional product-projection theorem applies to the orthonormal pair `(Y,Z)` and gives `||rho_m||_infinity<=2`; this bounded joint projected density is compatible with, but does not remove, the logarithmic obstruction below.

## 4. Completed Claude mixed-Fresnel theorem pays the family uniformly

Use the required pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, Theorem MF.

Take the heavy set `H={0}` and the leaves `L={1,...,m}`.  The leaf quadratic block is exactly the one spread square `Z^2`, so `r=1`, `lambda=1`, and the augmented leaf rows in Theorem MF are

`w_j = (c_delta/sqrt(m), eps_j/sqrt(m))`.

Their Gram matrix is

`Gamma = sum_j w_j w_j^T = diag(c_delta^2,1)`,                            (4.1)

because the signs are balanced.  Every normalized augmented leverage equals

`w_j^T Gamma^{-1} w_j = 1/m + 1/m = 2/m <= 1/2`.                         (4.2)

Therefore Theorem MF gives

`|phi_delta(t)| <= (4 pi)^{3/2}/(2 c_delta) * |t|^{-3/2}`.                (4.3)

Combining (4.3) with `|phi_delta|<=1` and integrating the exact envelope,

`int_R min(1,B|t|^{-3/2}) dt = 6 B^{2/3}`,

shows that `Q_delta` has a continuous density satisfying

`||p_{Q_delta}||_infinity`
` <= 3*2^{4/3} c_delta^{-2/3}`
` = 3*2^{4/3}(1+delta)^{-1/3}`
` <= 3*2^{4/3}`
` = 7.559526299369239...`.                                               (4.4)

This is a direct equation-level application of a completed required-source theorem to a member of the designated partner's near-null geometry.  The proof uses the original leaf factors; it never treats `Y` and `Z` as independent.

## 5. Scalar completion loses a logarithm even with the exact one-sided square kernel

For every `delta>0`, completing the physical hub square gives the exact identity

`Q_delta = delta (X_0 + (c_delta/delta)Y)^2 + R_delta`,

`R_delta = Z^2 - L_delta Y^2`,

`L_delta = c_delta^2/delta = (1+delta)/delta`.                            (5.1)

The usual cap-one square peel conditions on all leaves and bounds the translated `X_0` density only by one.  Its exact one-sided envelope at output level `s` is

`K_delta(s) := delta^{-1/2} E[(s-R_delta)^{-1/2} 1_{R_delta<s}]`.          (5.2)

In particular `||p_{Q_delta}||_infinity <= sup_s K_delta(s)`, and the usual half-Riesz certificate `delta^{-1/2} H_{1/2}(R_delta)` is still larger.

I now show that even the sharper quantity `K_delta(0)` diverges logarithmically.  Assume `L_delta^{-1/2}<eta_m`; this holds for all sufficiently small `delta`.  In the rectangle

`E_delta = { L_delta^{-1/2} <= y <= eta_m, |z|<=eta_m }`,                 (5.3)

we have from (3.3) `rho_m(y,z)>=kappa_m^2/2`.  Since `eta_m<=1/2`,

`L_delta y^2 >= 1 > eta_m^2 >= z^2`,

so `R_delta=z^2-L_delta y^2<0` and

`(-R_delta)^{-1/2}`
` = (L_delta y^2-z^2)^{-1/2}`
` >= (sqrt(L_delta) y)^{-1}`.                                            (5.4)

Consequently

`K_delta(0)`
` >= delta^{-1/2} * (kappa_m^2/2) * (2 eta_m) * L_delta^{-1/2}`
`      * int_{L_delta^{-1/2}}^{eta_m} dy/y`
` = (kappa_m^2 eta_m/c_delta) log(eta_m sqrt(L_delta))`
` = (kappa_m^2 eta_m/c_delta) log(eta_m c_delta/sqrt(delta)).`            (5.5)

Thus

`K_delta(0) -> infinity` as `delta downarrow 0`.                          (5.6)

In particular the exact full half-Riesz certificate obeys the same lower bound:

`delta^{-1/2} H_{1/2}(R_delta) >= K_delta(0) -> infinity`.                (5.7)

This is stronger than observing that the generic determinant bound gives a power loss.  The translation-uniform scalar-square envelope itself throws away enough source information to create a genuine logarithmic loss, even for an orthonormal two-dimensional projection of an independent product source with a uniformly bounded joint density.

There is no contradiction with (4.4).  The peel replaces the actual translated density

`f_0( -c_delta Y/delta +/- sqrt((s-R_delta)/delta) )`

by its height cap one.  On most of the large rectangle responsible for the logarithm, the translation is of order `Y/delta`; the source support/weight therefore matters.  The mixed-Fresnel proof keeps that original-coordinate factor and pays the cross coupling jointly with the transverse curvature before scalar completion.

## 6. New obstruction and proof-map consequence

**QFORM-NEAR-NULL-SQUARE-PEEL-LOG-BARRIER-v1.** There exists a target-valid exact-rank-three family with arbitrary-small nonzero physical hub pivot, a leverage-one dominant star, diffuse transverse leaves (`h_j=2/m<=1/2`), and a genuinely dependent same-bank two-dimensional projection such that:

1. the completed source-valid mixed-Fresnel theorem gives the uniform continuous-density bound (4.4), while
2. the exact translation-uniform one-sided scalar-square envelope `sup_s K_delta(s)` and hence the usual scalar-square/half-Riesz certificate diverge at least as `c_m log(1/delta)`.

Therefore the account03/B16 r23 near-null residual cannot be closed uniformly by the mechanism

`small nonzero scalar pivot -> complete the pivot -> discard the translated source density except for f<=1 -> bound the Schur remainder by a half-Riesz potential`,

even if the rank-two remainder law is the genuine bounded-density product projection and even if one optimizes the half-Riesz estimate beyond determinant scaling.

The next viable interface must retain the translating original-coordinate factor through the curved integral (as Theorem MF does here), or use an equivalent modulation-stable unnormalised product object.  This is an obstruction to a proof mechanism, **not** a counterexample to QFORM.  The unrestricted theorem, arbitrary extra spectrum, and global continuity remain open.

## 7. Source discipline

No arbitrary-joint coarea lemma, post-rotation independence, normalized conditional-density supremum/moment, law-uniform pointwise quadratic-phase decay, or small-matrix-as-small-random-error step is used.  The construction uses independent original coordinates throughout, and dependence of the projected pair is retained explicitly through (3.2).
