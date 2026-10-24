SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T04:33:44Z.
attacking: rigorous rough-input one-sheet intervals, then the uncovered indefinite two-sheet curved integral without unrestricted fiber suprema.

# account02/B05 r22 — exact-coloop mixed-transverse closure on the two-sheet route

**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM / FULL_QFORM_OPEN / WITHOUT_VERIFIED_BRAIN`.

This run does not claim the full arbitrary-dimensional conjecture. It first recorded the requested rough-input one-sheet interval theorem and exact reciprocal-shear two-sheet obstruction in `CHECKPOINT.md`. A fresh read then recovered the immediately preceding B05 r21 final mathematics report, which had already proved those two items plus the near-null scalar/dependent-pair interpolation theorem. To avoid repeating an unchanged attempt, this report advances the r21 first unpaid implication and closes its exact-coloop mixed-transverse branch.

## 1. Source pins actually used

Fresh brain control at run start: `yspennstate/math-research-brain@242a09dd205070fbf820b4d950daeb89f1af4b8a`, OWNER revision `2026-09-22.15`. A later fresh-main comparison through `8839f2409b12a2e9183e0e4a30b0599adadfbffd` showed only worker-run/status additions and no owner/control/correction change affecting B05.

Required newest Claude/math package:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Its Theorem C is applied at measure level in `CHECKPOINT.md`: for exact rank-three signature `(+,+,-)` and every interval `J subset [0,infinity)`, the ruled coordinates give

`P(Q in J) <= C_+(lambda1,lambda2,mu)|J| <= pi sqrt(2)|J|`

without a continuity assumption. The same checkpoint writes the exact negative-side reciprocal-shear/null-segment identity and applies the designated partner's transverse small-ball lemma to show that coarse transverse concentration is not the missing factor.

Immediately preceding B05 mathematics, recovered before the new proof:

`yspennstate/math-open-problems@c661893c05a7fd40d7f1e9b0a0a81a6f08f242a6`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T035943Z-account02-B05-QFORM-r21/REPORT.md`.

The dependency used below from that report is `QFORM-NEARNULL-SCALAR-DEPENDENT-PAIR-v1`: if `X` is a cap-one scalar independent of a dependent pair `(C,D)` having joint density cap `M`, and

`B=[[a,beta,0],[beta,alpha,delta],[0,delta,gamma]]`

is invertible with `beta gamma !=0`, then

`||p_Q||_infinity <=31 M^(2/3)|beta^2 gamma det B|^(-1/6)`,

with the exact-null `a=0` endpoint supplied by the source-pinned B16 theorem.

Rank-two fractional receiver:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`, Theorem 6.1. In the zero-affine case it gives

`sup_t E |(U^T Z)^T S(U^T Z)-t|^(-1/2) <=16 sqrt(30)|det S|^(-1/4)`

for every two-dimensional orthogonal projection `U^T Z` of a cap-one product law and every invertible symmetric `S`.

Designated partner account03/B05 r20:

`yspennstate/math-open-problems@929322485c85c8a08367589be2b8e2e73839c65f`, theorem `QFORM-HS-LINEAR-SMALLBALL-v1` and `QFORM-THREE-ARM-FROBENIUS-COAREA-v1`. The checkpoint applies the first theorem to the two null-transverse coordinates. The three-arm theorem remains the complementary receiver for the non-coloop/same-side-curvature branch after the exact-coloop theorem below.

All live corrections remain in force: no post-rotation independence, no arbitrary-joint three-dimensional coarea bound, no X-ray-only two-sheet replacement, and no conditional-cap-to-independence substitution.

## 2. Exact-coloop setup

Consider an **exact rank-three** form

`A=R B R^T`,  `R^T R=I_3`,

whose three nonzero eigenvalues all have magnitude at least one. Suppose some original coordinate is a leverage-one row of `R`.

An orthogonal change only inside the three-dimensional spectral space sends that row to `e1`. Because the row already exhausts one unit of the Parseval identity, every other row has first component zero. Therefore the active random vector has the form

`(X,C,D)`,

where `X` is one original cap-one coordinate and is independent of the pair `(C,D)`, while `(C,D)=U^T Z` is a two-dimensional orthogonal projection of the remaining cap-one product coordinates. No independence between `C` and `D` is asserted. Their joint density is bounded by `2` by the sharp two-dimensional product-projection bound used in the required newest source.

Rotate only inside this already-dependent pair so that the cross vector from `X` points along `C`. The coefficient matrix becomes

`B = [[a,beta,0],
      [beta,alpha,delta],
      [0,delta,gamma]]`.                                             (2.1)

Since every eigenvalue of `B` has magnitude at least one,

`||B^(-1)||_op <=1`, `|det B|>=1`.                                  (2.2)

Also

`a^2+beta^2=||B e1||^2>=1`.                                         (2.3)

The scalar `X` remains an original independent coordinate throughout; only the dependent pair was rotated.

## 3. New inverse certificate for the mixed-transverse branch

The r21 debt was the state `|a|` small and `|gamma|` small, where its new theorem does not directly give a uniform constant because of the factor `|gamma|^(-1/6)`. The large mixed coefficient `delta` forced by spectral nondegeneracy actually pays the old scalar-pivot loss.

### Lemma 3.1 — `QFORM-COLOOP-MIXED-INVERSE-CERTIFICATE-v1`

Assume (2.1)--(2.3), `a!=0`, `|a|<=1/16`, and `|gamma|<1/2`. Then

`|a det B| > beta^2/2 >=255/512`.                                   (3.1)

#### Proof

Let `x=B^(-1)e3`. From (2.2), `||x||_2<=1`. The first and third rows of `Bx=e3` are

`a x1+beta x2=0`,
`delta x2+gamma x3=1`.

Hence

`|x2| <= |a|/|beta|`

and therefore

`1 <= |delta||x2|+|gamma||x3|
   <= |a delta|/|beta| + |gamma|`.

Thus

`|a delta|/|beta| >=1-|gamma| >1/2`.                                (3.2)

On the other hand direct inversion gives

`(B^(-1))_31 = beta delta/det B`.

Again using (2.2),

`|det B| >= |beta delta|`.                                           (3.3)

Multiplying (3.3) by `|a|` and inserting (3.2),

`|a det B| >= |a beta delta|
             = beta^2 |a delta|/|beta|
             > beta^2/2`.

Finally (2.3) and `|a|<=1/16` give `beta^2>=1-a^2>=255/256`. This proves (3.1). QED.

This certificate uses the full inverse constraint, not merely a column norm. In particular it explains why the r21 estimate `|delta|>sqrt(3)/2` was not the final currency: in the small-`gamma` branch the correct invariant is the product `|a det B|`, and it stays bounded away from zero even as `a` tends to zero through nonzero values.

## 4. Pay the branch by a scalar square plus rank-two half-Riesz

For `a!=0`, complete the square only in the genuine original scalar:

`Q = a (X+(beta/a)C)^2 + R(C,D)`,                                   (4.1)

where

`R(C,D)=[C,D] S [C,D]^T`,

`S = [[alpha-beta^2/a, delta],
      [delta,             gamma]]`.                                  (4.2)

The determinant identity for a scalar Schur complement is exact:

`det S = det B/a`.                                                    (4.3)

Condition on the entire dependent pair. Since the conditional shift in (4.1) is only a translation of the independent scalar `X`, the density of the square term is bounded by the usual square kernel. Consequently, for a.e. `t`,

`p_Q(t) <= |a|^(-1/2) E |t-R(C,D)|^(-1/2)`.                         (4.4)

Now apply the source-pinned rank-two half-Riesz theorem to the two-dimensional orthogonal projection `(C,D)`. Because there is no affine term in `R`, the sharper source constant applies:

`sup_t E |t-R|^(-1/2)
 <=16 sqrt(30)|det S|^(-1/4)`.                                      (4.5)

Combining (4.3)--(4.5),

`||p_Q||_infinity
 <=16 sqrt(30)|a det B|^(-1/4)`.                                    (4.6)

Lemma 3.1 therefore gives, throughout the previously unpaid `|gamma|<1/2` branch,

`boxed: ||p_Q||_infinity
 <16 sqrt(30)(512/255)^(1/4)
 <104.319.`                                                          (4.7)

No moment, support, continuity, pair independence, or post-rotation independence is used.

## 5. Full exact-coloop closure

### Theorem 5.1 — `QFORM-EXACT-COLOOP-CLOSURE-v1`

Under the exact-rank-three setup of Section 2, if the active Parseval frame contains a leverage-one original coordinate, then

`boxed: ||p_Q||_infinity <=256.`                                    (5.1)

#### Proof

Use the aligned form (2.1).

**Case A: `|a|>1/16`.** The source-pinned exact-rank-three scalar-pivot theorem gives

`||p_Q||_infinity <=128(|a||det B|)^(-1/4) <=256`.                  (5.2)

**Case B: `a=0`.** Invertibility forces `beta gamma !=0`, and

`det B=-beta^2 gamma`.

The r21 near-null scalar/dependent-pair theorem includes its source-pinned exact-null endpoint, so with the joint pair density cap `M<=2`,

`||p_Q||_infinity
 <=31 2^(2/3)|beta^2 gamma det B|^(-1/6)
 =31 2^(2/3)|det B|^(-1/3)
 <=31 2^(2/3)
 <49.210`.                                                           (5.3)

**Case C: `0<|a|<=1/16` and `|gamma|>=1/2`.** By (2.3), `beta^2>=255/256`; by (2.2), `|det B|>=1`. Apply the same r21 theorem:

`||p_Q||_infinity
 <=31 2^(2/3)(512/255)^(1/6)
 <55.272`.                                                           (5.4)

**Case D: `0<|a|<=1/16` and `|gamma|<1/2`.** This is exactly (4.7), hence `<104.319`.

The worst displayed branch is therefore Case A, giving (5.1). QED.

This closes the exact-coloop version of the convex/two-sheet heavy-leverage obstruction. It also shows that the mixed-transverse coefficient `delta` is not itself a new pathology: when direct transverse curvature `gamma` is small, the inverse matrix forces enough `a*delta`, and the cofactor identity forces enough determinant, to restore the scalar-square/rank-two fractional receiver.

## 6. Relation to the rough two-sheet geometry and the designated partner

The rough negative-side reciprocal-shear identity in `CHECKPOINT.md` remains the correct geometric description for a general exact-rank-three projection. Theorem 5.1 does **not** bound that curved transform for an arbitrary projected density. Instead it proves that when one spectral degree of freedom is carried by an actual original coordinate, the product provenance can be retained through a genuine scalar square or the r21 scalar selector. That is precisely the kind of product-sensitive replacement demanded by the `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction.

The designated partner r20 remains complementary rather than redundant. Its three-arm Frobenius theorem closes states where three disjoint original-coordinate coefficient resources can be exposed with an affine smoothing side. This run's theorem closes the opposite extreme where one original coordinate is a full coloop and the remaining two spectral coordinates are an arbitrarily dependent projection pair. The open region is between those extremes: a heavy but non-coloop row leaves residual same-side quadratic curvature on more than two spectral degrees of freedom, exactly where the partner reports its obstruction.

The partner's `QFORM-HS-LINEAR-SMALLBALL-v1` was applied in the run checkpoint to the null-transverse pair `(B,W)`: their `2 x n` projection matrix has Hilbert--Schmidt norm `sqrt(2)`, so

`sup_z P(||(B,W)-z||<=rho) <= min(1,C_HS rho/sqrt(2))`.

The required newest source already gives the stronger `2 pi rho^2` small-radius consequence from the two-dimensional density cap. Thus the remaining general two-sheet problem is not missing coarse transverse concentration; it is retaining longitudinal/product structure through the reciprocal-shear segment.

## 7. First unpaid implication

`QFORM-TWOSHEET-NEARCOLOOP-RESIDUAL-CURVATURE-v1`:

Let an exact-rank-three active frame have a heavy original row of leverage `c in (1/2,1)` but no leverage-one coloop. After the diffuse-leverage branch and the non-small scalar-pivot branch are removed, the row is near-null and carries a strong cross arm, but deleting it leaves a **three-dimensional** projected residual rather than the two-dimensional pair of Theorem 5.1.

Prove one of the following without rotating product independence away:

1. quantitatively extract a true/approximate coloop plus an error whose same-side curvature can be absorbed into the r21 scalar-selector argument;
2. route the strong arm and the residual curvature into account03/B05 r20's three-resource Frobenius packet while allowing its currently unpaid same-side quadratic smoothing curvature; or
3. prove a direct product-sensitive Carleson estimate for the reciprocal-shear null segments from `CHECKPOINT.md`.

The exact-coloop mixed-transverse branch is no longer an unpaid endpoint. The missing factor is now **non-coloop residual curvature / longitudinal reciprocal-shear localization**, not the small direct transverse coefficient by itself.

## 8. Status

- Full arbitrary-dimensional QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Rough one-sheet interval theorem: source-applied and recorded in this run checkpoint; already fully proved in recovered r21.
- Exact two-sheet reciprocal-shear identity: recorded; already fully proved in recovered r21.
- Near-null scalar/dependent-pair theorem: recovered r21 dependency.
- New inverse certificate `|a det B|>=255/512` in the small-`a`, small-`gamma` exact-coloop branch: **proved here**.
- Exact rank-three leverage-one coloop state: **closed here with universal density bound 256**.
- Heavy non-coloop / same-side residual-curvature two-sheet state: **OPEN**.
- Independent review of the new theorem: **PENDING**.
