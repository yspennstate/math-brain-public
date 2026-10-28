SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-23T07:31:01Z.
attacking: a weighted joint negative-moment receiver for the shared-coefficient double-null fiber, and the collinear endpoint forced by the third large direction.

# account02/B06 — shared-coefficient curved-fiber receiver and a collinear target stress family

**Run:** `b06-20260923T073101Z-auto11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration / complementary constructions and source-valid counterexamples  
**Classification:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED`; full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository transport occurred, but no verified native learned-memory retrieval plus receiver use was established.  
**Continuity:** not claimed; the positive conclusions are essential-density bounds.

## 0. Control, exact target, and dependencies actually used


The exact target is unchanged. For arbitrary independent real original-coordinate inputs with probability densities bounded by one and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential density bound for `X^T A X`, or give a valid target counterexample. No moment, support, log-concavity, identical-law, diagonal-basis, Gaussian, or post-rotation-independence assumption is used. Continuity is separate.

The live correction boundary was retained: law-uniform pointwise quadratic-phase decay is unavailable; arbitrary-joint rank-three coarea is false; positive moments of worst conditional projection-density caps are false; unrestricted fiber suprema lose dimension; spectral rotation does not preserve independence; aggregate determinant mass need not yield one uniformly good physical minor; and a small nonzero tail cannot simply be deleted.

The source-valid inputs actually used below are:

1. **Designated partner account03/B06 r28**, canonical mathematics `yspennstate/math-open-problems@36cc5730f42c76c15fdc330dc4b47beec060b8fd`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T061939Z-account03-B06-qform-r28/REPORT.md`. For a cross block

   `B=[[b,r^T],[c,D]]`,

   it proves the exact anchored currency

   `Z_(i,a)=||bD-cr^T||_F^2`,

   hence at `b=0`, `Z_(i,a)=||c||^2||r||^2`. In its live two-hub chamber it obtains

   `Z_(i,a)>127 G^4/800`.

2. **Own weighted affine-fiber Brascamp--Lieb theorem**, canonical source `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`. If `R` has orthonormal columns and `Z` has independent cap-one coordinates, then `R^T Z` has density at most `e^(k/2)` in dimension `k`. After an invertible linear map, a one-dimensional linear form `a.Z` has density at most `sqrt(e)/||a||`, while a two-dimensional pair `(a.Z,b.Z)` has density at most

   `e/sqrt(||a||^2||b||^2-(a.b)^2)`.

3. **Required newest-Claude package**, pinned at `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` were read. The completed coordinate-hyperbola peel from `FOURIER_ROUTE_REPORT.md` is applied in Section 5 to a genuine target family, not merely cited.

4. Immediate own predecessor `b06-20260923T065430Z-3f494f528ca7`, which paid the disjoint-coefficient double-null branch by factorising two one-dimensional negative moments, but left shared coefficient forms unpaid. The present theorem removes that disjoint-support hypothesis whenever the two shared coefficient rows are transverse.

The early mathematical checkpoint was committed first in this run as `EARLY_CHECKPOINT.md` at math-open-problems commit `dc2401f70c4c1f175829b8e0ca542d8d1e940a39`.

## 1. A two-dimensional weighted negative-moment lemma

The first unpaid implication from the preceding run contains a conditional fiber density proportional to `|UV|^(-1/2)`, where `U,V` are two possibly dependent linear coefficient forms of the same product background. Taking a fiber supremum is impossible, and factorising the two negative moments is invalid once the coefficient forms share background coordinates. The correct replacement is a joint rectangular small-ball integral.

### Theorem 1 — `QFORM-JOINT-RECIPROCAL-RECTANGLE-v1`

Let `(U,V)` be a real random pair with joint density bounded by `K`, and one-dimensional marginal densities bounded by `L_U,L_V`. Assume

`kappa:=K/(L_U L_V)>=1`.

Then

`boxed:
 E |UV|^(-1/2)
 <= sqrt(L_U L_V) [8+2 log kappa].
`                                                                    (1.1)

The statement is translation-invariant: the same bound applies to `(U-u0,V-v0)` with the same caps.

### Proof

For `x>0`,

`x^(-1/2)=(1/2) integral_x^infinity s^(-3/2) ds`.                    (1.2)

Tonelli therefore gives

`E|UV|^(-1/2)
 = (1/4) integral_0^infinity integral_0^infinity
     P(|U|<=s, |V|<=t) s^(-3/2)t^(-3/2) ds dt`.                    (1.3)

The actual law supplies four simultaneous rectangular bounds:

`P(|U|<=s,|V|<=t)
 <= min(1, 2L_U s, 2L_V t, 4Kst)`.                                 (1.4)

Set

`x=2L_U s`, `y=2L_V t`.

Then (1.3)-(1.4) become

`E|UV|^(-1/2)
 <= (1/2)sqrt(L_U L_V) J(kappa)`,                                  (1.5)

where

`J(kappa)=integral_0^infinity integral_0^infinity
 min(1,x,y,kappa xy)x^(-3/2)y^(-3/2) dxdy`.                         (1.6)

For fixed `x`, put

`a=min(1,x)`, `c=min(1,kappa x)`.

Since `min(1,x,y,kappa xy)=min(a,cy)`, direct integration gives

`integral_0^infinity min(a,cy)y^(-3/2)dy=4 sqrt(ac)`.               (1.7)

When `kappa>=1`, the remaining `x`-integral splits at `1/kappa` and `1`:

`J(kappa)
 = integral_0^(1/kappa) 4 sqrt(kappa)x * x^(-3/2) dx
 + integral_(1/kappa)^1 4 sqrt(x) * x^(-3/2) dx
 + integral_1^infinity 4 x^(-3/2) dx
 = 8 + 4 log kappa + 8
 = 16+4 log kappa`.                                                 (1.8)

Insert (1.8) in (1.5). This proves (1.1). QED.

### Check at the product endpoint

If `U,V` are independent uniform variables on `[-1/2,1/2]`, then `K=L_U=L_V=1`, so (1.1) gives `8`. In fact

`E|UV|^(-1/2)=[E|U|^(-1/2)]^2=(2sqrt2)^2=8`.

Thus the rectangular calculation has the correct endpoint constant and is not merely a crude integrability argument.

## 2. Shared affine coefficient forms from one product background

The preceding abstract lemma becomes useful because the original product law gives both marginal and joint density caps before the reciprocal singularity is paid.

### Corollary 2 — `QFORM-SHARED-LINEAR-COEFFICIENT-NEGATIVE-MOMENT-v1`

Let `Z=(Z_1,...,Z_m)` have independent cap-one coordinates. Let

`U=a.Z+u0`, `V=b.Z+v0`,

where `a,b` are nonzero and linearly independent. Put

`A=||a||`, `B=||b||`,
`Delta=sqrt(A^2 B^2-(a.b)^2)>0`.                                    (2.1)

Then

`boxed:
 E|UV|^(-1/2)
 <= [2sqrt(e)/sqrt(AB)] [4+log(AB/Delta)].
`                                                                    (2.2)

### Proof

The one-dimensional form of the weighted affine-fiber theorem gives

`L_U<=sqrt(e)/A`, `L_V<=sqrt(e)/B`.                                 (2.3)

For the joint pair, let `C` be the `2 x m` matrix with rows `a^T,b^T`. Write

`S=(CC^T)^(1/2)`, `R=C^T S^(-1)`.

Then `R` has orthonormal columns and

`CZ=S R^T Z`.

The two-dimensional weighted affine-fiber theorem gives `R^T Z` density at most `e`; the linear image therefore has joint density cap

`K<=e/det(S)=e/Delta`.                                               (2.4)

Use these explicit caps in Theorem 1. Their ratio is

`kappa=(e/Delta)/(e/(AB))=AB/Delta>=1`.                             (2.5)

Equation (1.1) yields (2.2). QED.

This is the requested weighted product-structure replacement: a two-dimensional product-derived density cap is combined with both one-dimensional marginal caps before the curved reciprocal singularity is integrated. No independence between `U` and `V` is asserted or needed.

## 3. Double-null curved-fiber receiver with shared coefficients

Now retain the original physical anchor variables instead of rotating them away.

### Theorem 3 — `QFORM-DOUBLE-NULL-SHARED-COEFFICIENT-v1`

Let `X,Y` be independent cap-one real variables, independent of the product background `Z`. Let

`U=a.Z+u0`, `V=b.Z+v0`

with `a,b` as in Corollary 2, and let `R=R(Z)` be arbitrary measurable. Then

`T=2XU+2YV+R(Z)`                                                     (3.1)

has an essentially bounded density satisfying

`boxed:
 ||p_T||_infinity
 <= [sqrt(e)/sqrt(AB)] [4+log(AB/Delta)].
`                                                                    (3.2)

Arbitrary quadratic and affine curvature inside `R(Z)` is retained. In particular `R` may be strongly dependent on `(U,V)`.

### Proof

Condition on the full original-coordinate background `Z`. Then `U=u`, `V=v`, and `R` is only a translation. The density of `2uX` has

`||p_(2uX)||_2 <= (2|u|)^(-1/2)`                                    (3.3)

because `int f_X^2<=int f_X=1`; similarly

`||p_(2vY)||_2 <= (2|v|)^(-1/2)`.                                   (3.4)

The two anchor variables remain genuinely independent under this conditioning. Young/Cauchy--Schwarz gives

`||p_(T|Z)||_infinity <= 1/[2 sqrt(|UV|)]`.                          (3.5)

Average the **actual** conditional bound rather than taking its infinite supremum. Corollary 2 gives

`||p_T||_infinity
 <= (1/2)E|UV|^(-1/2)
 <= [sqrt(e)/sqrt(AB)] [4+log(AB/Delta)]`.                           (3.6)

QED.

The singular conditional fiber at `U=0` or `V=0` is real. The proof succeeds only because the original product background supplies enough two-dimensional weighted mass near their simultaneous zero set.

## 4. Quantitative splice into designated partner r28

Consider the partner's zero-cross-anchor branch and additionally the double-null physical subbranch

`A_ii=A_aa=A_ia=0`.                                                  (4.1)

Let the full two coefficient rows into all remaining original coordinates be `a_full,b_full`. In the partner's row/column split their cross-bank components contain `r,c`, respectively. Put

`A0=||a_full||`, `B0=||b_full||`,
`Delta0=sqrt(A0^2 B0^2-(a_full.b_full)^2)`.                          (4.2)

The partner identity at cross anchor `b=0` is

`Z_(i,a)=||c||^2||r||^2`,                                           (4.3)

and its live two-hub chamber gives

`||c||||r|| > sqrt(127/800) G^2`.                                  (4.4)

Therefore

`A0 B0 >= ||r||||c|| > sqrt(127/800)G^2`.                            (4.5)

Suppose only that the **full shared coefficient rows** have angle bounded away from collinearity:

`Delta0 >= eta A0 B0`, `0<eta<=1`.                                  (4.6)

Theorem 3 now applies without requiring disjoint coefficient supports. Equations (3.2), (4.5), and (4.6) give the real partner-spliced inequality

`boxed:
 ||p_Q||_infinity
 < [sqrt(e)/(127/800)^(1/8)] [4+log(1/eta)] G^(-1)
 = 2.0751907562... [4+log(1/eta)] G^(-1).
`                                                                    (4.7)

At the orthogonal/disjoint endpoint `eta=1`,

`||p_Q||_infinity < 8.300763025/G`.                                 (4.8)

This strictly improves the preceding B06 disjoint-bank constant `10.448/G` and, more importantly, removes the disjoint-support assumption: the two coefficient forms may share every background coordinate, provided their deterministic coefficient rows are quantitatively transverse.

No individual physical edge or minor is selected. The entire partner currency is used to lower-bound the product of the two row norms before the reciprocal exponent is paid.

## 5. Candidate refuted: partner double-star currency does not force transversality

The new theorem leaves `Delta0/(A0B0)` as the only geometric loss. It would be tempting to infer a universal lower bound on that angle from the partner's anchored currency. That implication is false even inside the exact QFORM target and even when every local physical cross edge tends to zero.

### Construction — `QFORM-DOUBLESTAR-CURRENCY-NO-ANGLE-v1`

Let `N,M>=1`. Let

`u=(N^(-1/2),...,N^(-1/2)) in R^N`,
`v=(M^(-1/2),...,M^(-1/2)) in R^M`,

so `||u||=||v||=1`. Take independent cap-one original variables

`X,Y,U_1,...,U_N,V_1,...,V_M,Z`.

Define

`L=u.U+v.V`,
`Q_(N,M)=2(X+Y)L+Z^2`.                                               (5.1)

Use the partner split

`I={X,U_1,...,U_N}`, `J={Y,V_1,...,V_M}`.

The physical cross block is exactly

`B=[[0,v^T],[u,0]]`.                                                 (5.2)

Thus at the anchor `(X,Y)`,

`b=0`, `D=0`, `c=u`, `r=v`,

and the partner currency is

`Z_(X,Y)=||c||^2||r||^2=1`.                                         (5.3)

Every individual star edge has magnitude at most `max(N^(-1/2),M^(-1/2))`, tending to zero as both banks diffuse.

However, the **full** coefficient row of `X` into the leaves is `(u,v)`, and the full coefficient row of `Y` is the same vector `(u,v)`. Hence

`A0=B0=sqrt2`, `Delta0=0`.                                          (5.4)

So no positive universal `eta` follows from the anchored double-star currency.

This is a counterexample only to that intermediate structural implication, not to QFORM. In fact the symmetric matrix of the star term has nonzero spectrum `{2,-2}`: if

`S=(X+Y)/sqrt2`, `T=L/sqrt2`,

then `2(X+Y)L=4ST`, whose `2 x 2` matrix has eigenvalues `+2,-2`. The independent square `Z^2` adds eigenvalue `+1`. Therefore the full matrix in (5.1) has exactly

`boxed: nonzero spectrum {2,-2,1},`                                 (5.5)

and is a genuine target matrix.

The exact family therefore proves that the near-collinear endpoint is not an artefact of a loose estimate. The third large direction really has to enter the payment.

## 6. Required newest-Claude theorem applied to the collinear target family

The family (5.1) is exactly where the new transverse receiver diverges, but it is uniformly controlled once the third direction is used before taking the absolute hyperbolic singularity.

First, `S0=X+Y` is independent of all leaves and `Z`. Since it is a convolution of two cap-one probability densities,

`||p_(S0)||_infinity<=1`.                                           (6.1)

Second, `L=u.U+v.V` is a one-dimensional linear projection with coefficient norm

`sqrt(||u||^2+||v||^2)=sqrt2`.

The weighted affine-fiber theorem gives

`||p_L||_infinity <= sqrt(e/2)=:K_L`.                               (6.2)

Set

`W=K_L L`.

Then `W` has density at most one, is independent of `S0` and `Z`, and

`Q_(N,M)=2 mu S0 W+Z^2`, `mu=1/K_L`.                                (6.3)

Now apply the completed newest-Claude **coordinate-hyperbola peel**, `FOURIER_ROUTE_REPORT.md`, Lemma 4.3(b): for two independent cap-one variables in a zero-diagonal physical pair,

`D(2mu S0 W+R)
 <= 2^(3/4) kappa_h |mu|^(-3/4) H_(1/4)(R)`,                         (6.4)

where

`kappa_h=sup_(y>0) log(1+y)/sqrt(y)=0.8047423425...`.

The same completed package, Lemma 4.2, gives for the independent cap-one square

`H_(1/4)(Z^2)<=4`.                                                   (6.5)

Combining (6.2)-(6.5),

`boxed:
 ||p_(Q_(N,M))||_infinity
 <= 4*2^(3/4)*kappa_h*(sqrt(e/2))^(3/4)
 = 6.073842461... .
`                                                                    (6.6)

This bound is uniform in `N,M` and in all independent cap-one input laws. It covers **all output levels**, not only the one-sheet side of the ruled theorem used in the preceding B06 run.

Thus the exact collinear obstruction is not a QFORM counterexample. It is paid by first grouping the two anchor variables and the diffuse coefficient bank into a genuine independent hyperbolic pair, then using the third square through its quarter-Riesz potential. This is a direct application of a completed newest-Claude result to a real target inequality.

## 7. What changed and the first unpaid implication

This run advances the double-null branch in three ways.

1. It proves an exact two-dimensional reciprocal-product estimate from joint and marginal density caps. The logarithmic angular factor is derived by an explicit rectangle integral, not by a worst-fiber supremum.
2. It converts that estimate into a product-preserving curved-fiber theorem for two shared affine coefficient forms. The coefficients may be arbitrarily dependent because they are functions of the same product background.
3. It splices the theorem into the designated partner r28 currency. Every quantitatively transverse shared-coefficient double-null survivor is now paid with the explicit bound (4.7); the earlier disjoint-support branch is subsumed and improved.
4. It gives a target-valid diffuse family proving that the partner currency alone cannot force transversality, and then applies the required newest-Claude coordinate-hyperbola theorem plus quarter-Riesz square estimate to pay that exact collinear endpoint by `6.074`.

The first unpaid implication is now

`QFORM-NEAR-COLLINEAR-SHARED-COEFFICIENT-THIRD-DIRECTION-v1`:

> In the partner r28 double-null zero-cross-anchor state, after the transverse receiver (4.7) is removed, the two full coefficient rows can be arbitrarily close to collinear. Retain every same-bank quadratic term and every complementary spectral component. Show that the third large spectral direction supplies a product-preserving quarter-Riesz / grouped-hyperbola payment before the logarithmic factor `log(A0B0/Delta0)` diverges, or route the state into an already-paid physical-pair, aggregate-volume, ridge, or grouped-bank exit. No post-rotation independence, worst conditional-density cap, deletion of a small nonzero tail, or single-minor selector is permitted.

The family (5.1) proves that this implication cannot be replaced by a deterministic angle lower bound. Its successful payment (6.6) gives the model endpoint: exact collinearity is harmless when the third direction survives as an independent square, so the missing theorem is a robust product-preserving interpolation between (4.7) and that quarter-Riesz endpoint.

## 8. Deterministic verification

`CHECK.py` evaluates a representative `N=9,M=16` matrix from (5.1), the partner currency, the coefficient-row area, and the constants. It returned

`nonzero_eigenvalues [-2.0, 1.0, 2.0]`,
`cross_anchor_currency 1.0`,
`shared_row_area 0.0`,
`linear_form_cap 1.165821990799`,
`claude_collinear_bound 6.073842460959`,
`eta_1_bound_constant 8.300763024759`.

Executed checker source SHA-256: `803080fc75f4253c6522c3794496f931bededbf5aa21595c0363a3f69181eee7`.  
Checker output SHA-256: `51ecf8f3775262a5d5aa020f291c0de27a61032728d1f636a651b22daec0f9b1`.

The computation is only a consistency check for the exact algebra and constants; the proofs above are analytic.
