SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-23T09:21:38Z.
attacking: the fully coupled nonzero scalar/dependent-pair branch: keep the original scalar independent, retain dependence inside the product-projection pair, and pay the curved discriminant by the completed rank-two half-Riesz theorem.

# fleet03/B06 r31 — a fully coupled nonzero-pivot scalar/dependent-pair transducer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration / current differentiated B06 task: extend the genuine scalar/dependent-pair kernel to a relevant non-null or coupled regime while retaining source independence hypotheses.  
**Status:** NEW SUPPORTING THEOREM + TARGET-VALID COUPLED FAMILY / FULL QFORM OPEN.  
**Continuity:** not proved by the new general theorem; only essential boundedness is asserted there.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction boundary

The owner target remains: for every `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a density whose essential supremum is bounded by one universal finite constant, or give a valid counterexample. The additional continuous-density conclusion is tracked separately.

This report uses only independence among explicitly disjoint ORIGINAL source objects. It does not assume independence after spectral rotation; no arbitrary-joint coarea bound; no law-uniform pointwise Fresnel decay; no worst conditional projection-density cap/moment; no single uniformly good physical minor; no small-random-error consequence from a small matrix error; and no unrestricted fiber supremum. The input supports may be fragmented and unbounded.

The new theorem is deliberately nonzero-pivot. Its constant diverges as the scalar quadratic pivot tends to zero. Section 7 identifies why that divergence is a real limitation of this proof mechanism rather than evidence against QFORM.

## 2. Source-valid inputs actually used

### 2.1 Current B06 continuation and volume-stability gate

The current eighty-worker continuation requires B06 to extend the genuine scalar/dependent-pair kernel to a relevant non-null or coupled regime while retaining all independence hypotheses. It also supplies the new volume-stability exit: if an ORIGINAL-coordinate cross block satisfies `M=M0+E`, `s3(M0)>=a`, `max diag(P_range(M0))<=1/2`, and `||E||op<=a/16`, then the full ambient form has a continuous density `<23/a`. At the concrete normalized scale `a=1/64`, this already pays any such branch by `<1472`. Thus the coupled mechanism below is needed only after at least one of those volume-stability gates fails; I do not duplicate that paid branch.

Source package: `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/`.

### 2.2 Exact-null scalar/dependent-pair kernel

Fleet02/B16 proved `QFORM-NULL-SCALAR-DEPENDENT-PAIR-v1` at

`yspennstate/math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260922T232932Z-fleet02-B16-QFORM-auto11/REPORT.md`.

If `X` has density cap one, is independent of a possibly dependent pair `(C,D)` whose joint density cap is `M`, then

`2 beta X C + alpha C^2 + 2 eta C D + gamma D^2`

has density cap

`3(2M)^(2/3)|beta^2 gamma|^(-1/3)`.

The proof retains the genuine scalar independence and pays a weak-`L^(3/2)` root-selector kernel. It does not license replacing that scalar by a dependent conditional variable.

### 2.3 Rank-two affine half-Riesz theorem

The completed theorem

`QFORM-RANK2-AFFINE-HALF-RIESZ-v1`

is at

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For an orthonormal two-dimensional product projection `P^T Z`, invertible symmetric `2x2` matrix `Lambda`, and arbitrary original-coordinate affine term `b.Z`,

`sup_s E |(P^T Z)^T Lambda(P^T Z)+b.Z-s|^(-1/2)
 <=128 |det Lambda|^(-1/4).`                                      (2.1)

If `b` lies in the projection range, including `b=0`, the constant improves to

`16 sqrt(30)`.                                                     (2.2)

This is exactly the fractional curved-fiber payment needed below.

### 2.4 Completed fleet04 dependence-safe square theorem

No completed canonical current-QFORM artifact exists in the designated `fleet04/B06` directory at this run's source refresh. I therefore do not invent a designated-partner result. I apply the compatible completed fleet04/B18 theorem instead:

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

Its `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` says that if a base variable `R` has density cap `M` and, conditionally on `R`, a translated square coordinate has density cap one, then

`||p_{R+aV_R^2}||_infinity <=2 sqrt(M/|a|)`,                       (2.3)

without requiring independence between `R` and the translated square. If the conditional scalar cap is `L`, rescaling gives the immediate variant

`||p_{R+aV_R^2}||_infinity <=2 L sqrt(M/|a|)`.                     (2.4)

### 2.5 Current ruled-side theorem actually applied

The newest Claude package contains the corrected source-valid ruled estimate in

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

For a rank-three signature `(+, +, -)` form with spectral moduli at least one, the one-sheet side has

`p(s)<=pi sqrt(2)`,                                                 (2.5)

using line integrals that are two-dimensional marginals of the ORIGINAL product law. This does not declare the spectral coordinates independent and is applied to an explicit family in Section 6.

## 3. Main theorem: fully coupled nonzero scalar/dependent-pair transducer

### Theorem 3.1 — `QFORM-COUPLED-NONZERO-PIVOT-DISCRIMINANT-HALFRIESZ-v1`

Let `X` be a real random variable with density cap

`||p_X||_infinity <= L_X`.

Let `Z=(Z_1,...,Z_m)` be a vector of independent real variables, each with density cap one. Let `W` be an auxiliary source. Assume `X`, `Z`, and `W` are mutually independent source objects.

Choose linearly independent `u,v in R^m` and define

`U=u.Z`, `V=v.Z`,

`G=||u||^2 ||v||^2-(u.v)^2 >0`.                                   (3.1)

Let `H=H(Z,W)` be arbitrary measurable, let `R=R(W)` be arbitrary measurable, and let `ell in R^m`. For nonzero real `gamma,k,delta,beta`, set

`Y=gamma X+H`,

`Q=delta Y^2+2k UY+beta V^2+ell.Z+R`.                              (3.2)

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <=128 (L_X/|gamma|)
       [ k^2 |delta beta| G ]^(-1/4).`                              (3.3)

If `ell` lies in `span{u,v}`—in particular if `ell=0`—then

`boxed:
 ||p_Q||_infinity
 <=16 sqrt(30) (L_X/|gamma|)
       [ k^2 |delta beta| G ]^(-1/4).`                              (3.4)

The same-bank quantities `H`, `U`, and `V` may be arbitrarily dependent through the product vector `Z`. No density cap for `U|H`, `V|H`, or `(U,V)|H` is assumed.

### Proof

Fix `t`, and condition on `(Z,W)=(z,w)`. Write

`u_0=u.z`, `v_0=v.z`, `h=H(z,w)`.

Because `X` is genuinely independent of `(Z,W)`, the conditional variable

`Y=gamma X+h`

has a translated density bounded by

`L_Y=L_X/|gamma|`.                                                  (3.5)

For fixed `(z,w)`, the equation `Q=t` is the scalar quadratic equation

`delta y^2+2k u_0 y+
 [beta v_0^2+ell.z+R(w)-t]=0`.                                    (3.6)

Its discriminant divided by four is

`D(z,w;t)
 =k^2 u_0^2
   +delta[t-beta v_0^2-ell.z-R(w)].`                               (3.7)

When `D<=0`, there is no contribution apart from a null double-root set. When `D>0`, the two roots have derivative magnitude

`|2 delta y+2ku_0|=2 sqrt(D)`.                                    (3.8)

Therefore the sum of the two root-density contributions is bounded by

`p_{Q|Z,W}(t|z,w)
 <= L_Y D(z,w;t)^(-1/2).`                                         (3.9)

Averaging gives

`p_Q(t)
 <=(L_X/|gamma|)
   E | k^2 U^2-delta beta V^2-delta ell.Z-s_W |^(-1/2),`           (3.10)

where

`s_W=delta(R(W)-t)`.                                               (3.11)

The key point is that `H` has disappeared from the discriminant. This is the product-preserving curved-fiber replacement: the arbitrary shared-bank translation is removed algebraically before any fiber supremum or conditional projection-density payment.

For each fixed `W=w`, choose an orthonormal matrix `P` whose columns span `span{u,v}`. Put

`a=P^T u`, `b=P^T v`.

Then the quadratic part in (3.10) is

`(P^T Z)^T Lambda(P^T Z)`,

with

`Lambda=k^2 aa^T-delta beta bb^T`.                                (3.12)

In dimension two,

`det Lambda
 =-k^2 delta beta [det(a,b)]^2`.                                 (3.13)

Because `P` is orthonormal on the span of `u,v`,

`[det(a,b)]^2
 =det Gram(u,v)
 =G`.                                                             (3.14)

Thus

`|det Lambda|=k^2 |delta beta| G`.                                 (3.15)

The remaining term `-delta ell.Z` is an arbitrary original-coordinate affine term. Apply (2.1), uniformly in the scalar shift `s_W`, to (3.10). This proves (3.3). If `ell in span{u,v}`, the affine term lies in the projection range, so (2.2) gives (3.4). Averaging over `W` does not change the bound. QED.

### Why this is genuinely coupled

The theorem does not require `V` to come from an independent source bank. Both `U` and `V`, and even the translation `H`, may depend on the same product coordinates `Z`. The only isolated source is the original scalar `X`, whose translation-uniform density cap is retained until after the scalar quadratic root calculation. The remaining curved singularity is then paid by the full rank-two product-projection fractional theorem, not by an unrestricted spectral-fiber maximum.

## 4. Opposite-sign sharpening using the completed fleet04 theorem

When the scalar pivot and the final square have opposite signs, the curved pair left after square completion is definite and the fleet04 theorem yields a much smaller constant.

### Theorem 4.1 — `QFORM-COUPLED-DEFINITE-SCHUR-SQUARE-v1`

Assume the hypotheses of Theorem 3.1, take `ell=0`, and suppose

`delta beta<0`.                                                     (4.1)

Then

`boxed:
 ||p_Q||_infinity
 <=2 sqrt(2pi) (L_X/|gamma|)
      [ k^2 |delta beta| G ]^(-1/4).`                               (4.2)

### Proof

Reflect `Q` if necessary, so `delta>0` and `beta<0`. Complete the scalar square:

`Q
 =delta (Y+kU/delta)^2
   + beta V^2-(k^2/delta)U^2+R`.                                   (4.3)

For the moment condition on `W=w`; `R(w)` is a harmless scalar translation. The pair `(U,V)` is a linear image of the two-dimensional orthogonal projection `P^T Z`. The standard product-projection density bound gives

`||p_{(U,V)}||_infinity <=2/sqrt(G)`.                               (4.4)

The base quadratic

`B(U,V)=beta V^2-(k^2/delta)U^2`                                  (4.5)

is definite. The elementary two-dimensional definite quadratic density bound therefore gives

`||p_B||_infinity
 <= pi [2/sqrt(G)] /
       sqrt( (k^2/delta)|beta| )
 = 2pi sqrt(delta)/(|k| sqrt(|beta|G)).`                            (4.6)

Disintegrate over the value of `B`. Given that base value, the translated-square coordinate

`Y+kU/delta
 =gamma X+[H+kU/delta]`                                           (4.7)

is a mixture of translations of `gamma X`, because the genuinely independent original scalar `X` is still untouched. Hence its conditional density cap is at most

`L_X/|gamma|`.                                                      (4.8)

Apply the scaled fleet04/B18 dependence-safe square theorem (2.4) at the actual identity (4.3):

`||p_Q||_infinity
 <=2(L_X/|gamma|)
    sqrt( [2pi sqrt(delta)/(|k|sqrt(|beta|G))]/delta )`

`=2sqrt(2pi)(L_X/|gamma|)
  [k^2 |delta beta|G]^(-1/4).`                                     (4.9)

This proves (4.2). No independence between the base quadratic and the translated square is assumed. QED.

This is an actual application of a completed fleet04 theorem to a displayed inequality, as required. The exact designated partner `fleet04/B06` still has no completed canonical QFORM artifact visible and is not credited with a nonexistent result.

## 5. Explicit target-valid fully coupled families

The next families show that Theorem 3.1 genuinely extends beyond the semi-aligned fleet02/B16 theorem in which the final square variable must come from an independent source bank.

Let `m>=3`. Take arbitrary independent cap-one variables

`X_0,Z_1,...,Z_m`.

Choose three orthonormal coefficient vectors `t,u,v in R^m` and define

`T=t.Z`, `U=u.Z`, `V=v.Z`.                                         (5.1)

For `c in (0,1)` write `a=1-c` and

`Y=sqrt(c)X_0+sqrt(a)T`.                                            (5.2)

The three physical frame columns

`r_1=(sqrt(c),sqrt(a)t)`,
`r_2=(0,u)`,
`r_3=(0,v)`                                                        (5.3)

are orthonormal in the original coordinate space. Thus the spectral variables `Y,U,V` are generally dependent, because all three contain the same `Z` bank, but the deterministic frame is exact.

For `delta>0` put

`k_delta=sqrt(1+delta)`.                                            (5.4)

### 5.1 Signature `(+, +, -)` family

Define

`Q^+_{c,delta}
 =delta Y^2+2 k_delta UY+V^2`.                                    (5.5)

Its spectral matrix in the frame `(r_1,r_2,r_3)` is

`B_+(delta)=
 [[delta,k_delta,0],
  [k_delta,0,0],
  [0,0,1]].`                                                       (5.6)

The `2x2` upper block has eigenvalues `1+delta` and `-1`, so

`spec B_+(delta)={1+delta,-1,1}`.                                  (5.7)

Hence every `delta>0` is an exact three-large-eigenvalue instance of the owner's target. The final `V^2` does NOT come from an independent source bank: `T,U,V` all use `Z`.

Apply (3.4) with `gamma=sqrt(c)`, `k=k_delta`, `beta=1`, and `G=1`:

`boxed:
 ||p_{Q^+_{c,delta}}||_infinity
 <=16sqrt(30)c^(-1/2)
      [delta(1+delta)]^(-1/4).`                                    (5.8)

### 5.2 Signature `(+, -, -)` family

Define

`Q^-_{c,delta}
 =delta Y^2+2 k_delta UY-V^2`.                                    (5.9)

Now

`spec B_-(delta)={1+delta,-1,-1}`.                                 (5.10)

The opposite-sign sharpening (4.2) gives

`boxed:
 ||p_{Q^-_{c,delta}}||_infinity
 <=2sqrt(2pi)c^(-1/2)
      [delta(1+delta)]^(-1/4).`                                    (5.11)

This family is likewise genuinely coupled through the single `Z` bank.

### 5.3 Numerical collar constants

In the live near-coloop chamber `c>63/64`, the all-level constants are, for `delta=1,1/4,1/16,1/64,1/256`:

- `(+, +, -)` via (5.8): `74.2751`, `118.138`, `174.000`, `248.864`, `352.970`;
- `(+, -, -)` via (5.11): `4.24896`, `6.75814`, `9.95377`, `14.2365`, `20.1919`.

These checks only illustrate the quantitative collar; the symbolic estimates above are the proofs.

## 6. Actual newest-Claude ruled-side application

The source-valid ruled theorem (2.5) can be applied directly to the exact target families above.

For `Q^+_{c,delta}`, the spectral signature is

`(1+delta,1,-1)`.                                                   (6.1)

Therefore the one-sheet side obeys the stronger dimension-free estimate

`boxed: p_{Q^+_{c,delta}}(s)<=pi sqrt(2),  s>=0.}`                  (6.2)

Consequently the new transducer (5.8) is only needed on the opposite, two-sheet side `s<0` for this family.

For `Q^-_{c,delta}`, reflect the output. The reflected spectral signature is

`(1,1,-(1+delta))`.                                                 (6.3)

Thus

`boxed: p_{Q^-_{c,delta}}(s)<=pi sqrt(2),  s<=0.}`                  (6.4)

and the new fleet04-assisted estimate (5.11) pays the complementary side. This is an actual use of the current Claude result at a concrete inequality, not a bibliography-only citation.

## 7. Exact-null boundary: what the proof does not do

The new constants behave like `|delta|^(-1/4)` as `delta->0`. This is not a claim that the target density must blow up. It is a limitation of the present root-density/half-Riesz mechanism.

Indeed, if one simply sets `delta=0` in the scalar root calculation, the derivative of

`2k UY`

with respect to the independent scalar `Y` is `2kU`, and the crude absolute root-density majorant requires a factor comparable to

`E |U|^(-1)`.                                                       (7.1)

For an admissible `U` whose density is positive near zero—for example a centered uniform variable—(7.1) diverges logarithmically. Therefore the exact-null endpoint cannot be recovered by taking `delta=0` inside the same absolute root bound.

This does **not** refute QFORM. The exact-null fleet02/B16 theorem avoids precisely this loss by using the probability-normalized root selector together with a second curved coordinate. The current fully coupled obstruction is that in the family (5.5) at `delta=0`, the translation `H`, the bilinear coefficient `U`, and the final square coordinate `V` all come from the same product bank. The semi-aligned theorem that assumes an independent final square does not apply.

The next precise B06 debt is therefore

`QFORM-FULLY-COUPLED-EXACT-NULL-ROOT-SELECTOR-v1`:

> retain the genuine original scalar `X`, but before taking an absolute `1/|U|` root Jacobian, aggregate the pair `(U,V)` together with the shared translation `H` using the original product law; prove a weak-`L^(3/2)` or equivalent weighted curved-fiber bound that remains finite at `delta=0`, without any conditional density cap for `(U,V)|H` and without declaring the spectral variables independent.

A source-valid alternative is to force the exact-null survivor into one of the already-paid volume/ridge/physical-grouped branches. Either route must retain the full ambient spectrum and arbitrary same-bank curvature.

## 8. Finite checks

The companion `CHECKS.md` records:

1. the exact determinant identity

`det(k^2 aa^T-d bb^T)=-k^2 d det Gram(u,v)`

checked on 5,000 random pairs, maximum normalized floating discrepancy `8.25e-14`;
2. the target-family spectra checked across 200 logarithmically spaced `delta` values, maximum absolute discrepancy `4.55e-13`;
3. the explicit constants in the live `c>63/64` collar;
4. the logarithmic exact-null `E|U|^-1` warning.

These are sanity checks, not proof certificates.

## 9. Status and proof map

Proved in this report:

- `QFORM-COUPLED-NONZERO-PIVOT-DISCRIMINANT-HALFRIESZ-v1`, (3.3)-(3.4);
- `QFORM-COUPLED-DEFINITE-SCHUR-SQUARE-v1`, (4.2), using fleet04/B18 at the actual completed-square identity;
- two exact target-valid fully coupled families, (5.5) and (5.9), with all-level bounds;
- an actual splice with the newest ruled-side theorem, (6.2) and (6.4).

Not proved:

- the exact-null fully coupled endpoint;
- an exhaustive reduction of every surviving N3 matrix to the hypotheses of these theorems;
- the full QFORM conjecture;
- a universal continuous representative. The new general theorems establish essential boundedness only.

No source-matching published theorem was found here that closes the same unrestricted scope, and no novelty claim is made. The designated `fleet04/B06` result remains unavailable; the compatible completed `fleet04/B18` theorem was the actual fleet04 result used.
