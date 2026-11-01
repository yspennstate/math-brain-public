# fleet01/B05 — diffuse rank-two half-Riesz coarea and Schur hybrid

**Run:** `20260922T125608Z-qform-coarea-B05-a01`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval was used, but repository transport is not native learned-memory ingestion).

## 1. Exact target and compact conditional route

The full target remains: for every dimension, every independent real inputs with densities at most one, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove a dimension- and law-independent bound on the essential supremum of the density of `X^T A X`, or give a valid counterexample. Continuity is a separate requested regularity conclusion.

This run attacks the coarea/small-interval interface. The current conditional route for the rank-exactly-three core is:

1. if the rank-three spectral projector has all coordinate leverage norms at most `1/2`, fleet03/B05's Fresnel--Brascamp--Lieb theorem already gives a universal continuous density bound;
2. otherwise choose a physical heavy coordinate and complete the square there;
3. if the resulting rank-two Schur residual is diffuse in the remaining original coordinates, prove a *half-Riesz* bound for that residual and insert it into fleet02/B05's scalar-square inequality;
4. the remaining branch is therefore structurally localized or nearly isotropic at every usable heavy pivot. It must be closed by a product-preserving aggregate/hyperbolic mechanism, not by assuming one strong fixed minor.

The first new implication below closes step 3 exactly.

Corrections respected: no law-uniform pointwise one-dimensional Fresnel decay is used; no independence is asserted after rotation; no unrestricted fiber supremum is taken; no single cross minor or single Schur rank-two extraction is asserted to follow from the spectral hypothesis.

## 2. Named partner actually applied

The designated partner fleet02/B05 proved at

`yspennstate/math-open-problems@e06922bfa31bbd225cdce6ee6aea563254e62563`

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260922T122133Z-b05-qform-5c41e5bb/REPORT.md`

the scalar-Schur inequality. If a physical pivot coefficient `a!=0` is completed in the original independent coordinate,

`Q = a (X+m(Z))^2 + R(Z)`,

then

`p_Q(t) <= |a|^(-1/2) E |t-R(Z)|^(-1/2)`.                 (2.1)

Its binary gradient-box theorem also proves a complete fixed nonsingular physical-triple interface. The present run applies (2.1) to an aggregated diffuse rank-two Schur residual rather than paying a single reciprocal physical minor.

The Fourier input is the completed fleet03/B05 theorem

`yspennstate/math-open-problems@c828d2ee2f8acef5eb96892bc8a9a25594db0f51`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260922T113800Z-fleet03-B05-qform-r11/REPORT.md`.

Its proof gives, for an `r`-dimensional orthogonal projection of a product law with spectral-projector leverage norm at most `1/2`, an `L^1` Fourier bound `||psi||_1<=B^r` with an absolute constant `B`. The associated Fresnel estimate is valid already for `r=2`; only the final unweighted time integral in their density theorem requires `r>2`.

## 3. New theorem: diffuse rank-two half-Riesz bound

### Theorem 3.1 — `QFORM-RANK2-DIFFUSE-HALF-RIESZ-v1`

Let `Z=(Z_1,...,Z_m)` have independent real coordinates with densities bounded by one. Let `S` be a real symmetric rank-two matrix with nonzero eigenvalues `mu_1,mu_2`, and let `P` be the orthogonal projector onto `range(S)`. Assume

`max_j ||P e_j||_2 <= 1/2`.                                                (3.1)

Then, with the same absolute Fourier--Brascamp--Lieb base `B` as above,

`sup_s E |s-Z^T S Z|^(-1/2)`
` <= (2 sqrt(2) B/pi) |mu_1 mu_2|^(-1/4)`.                              (3.2)

No sign restriction on `mu_1,mu_2` is imposed. In particular, (3.2) is compatible with the logarithmic density singularity of an opposite-sign rank-two quadratic form: the rank-two density itself need not be bounded.

### Proof

Choose a `2 x m` matrix `R` with orthonormal rows spanning `range(S)`, so

`S=R^T diag(mu_1,mu_2) R`.

Let `Y=RZ` and `psi(xi)=E exp(i<xi,Y>)`. The small-leverage Fourier--Brascamp--Lieb estimate gives

`||psi||_1 <= B^2`.                                                       (3.3)

Let

`W=Y^T diag(mu_1,mu_2)Y`, `phi(t)=E exp(i t W)`.

Repeating the Gaussian-regularized Fresnel pairing from fleet03/B05 in dimension two gives, for `t!=0`,

`|phi(t)| <= B^2/(4 pi |t| sqrt(|mu_1 mu_2|))`.                          (3.4)

Together with `|phi(t)|<=1`, write

`|phi(t)| <= min(1,c/|t|)`,
`c=B^2/(4 pi sqrt(|mu_1 mu_2|))`.                                        (3.5)

Under the Fourier convention used in the cited proof,

`widehat{|x|^(-1/2)}(t)=sqrt(2 pi)|t|^(-1/2)`

in the tempered-distribution sense. Regularize the kernel at zero and infinity and pass to the limit by monotone/dominated convergence; (3.5) supplies the integrable majorant. Hence

`E|s-W|^(-1/2)`
` <= 1/sqrt(2 pi) int_R |phi(t)| |t|^(-1/2) dt`.                         (3.6)

The last integral is explicit:

`int_R min(1,c/|t|)|t|^(-1/2)dt`
` = 2 int_0^c t^(-1/2)dt + 2c int_c^infinity t^(-3/2)dt`
` = 8 sqrt(c)`.                                                          (3.7)

Substituting `c` yields exactly (3.2). QED.

## 4. Exact rank-three Schur identities

Let now `A` have rank exactly three, with nonzero spectral representation

`A=U Lambda U^T`, `U^T U=I_3`,

where `Lambda` is invertible symmetric. Write `u_i in R^3` for the `i`th row of `U`,

`ell_i=||u_i||^2`, `a_i=u_i^T Lambda u_i=A_ii`.

Fix `i` with `a_i!=0`. Completing the physical coordinate `X_i` gives the Schur residual

`S_i=A_{-i,-i}-A_{-i,i}A_{i,-i}/a_i`
`   =U_- K_i U_-^T`,

where

`K_i=Lambda-(Lambda u_i)(Lambda u_i)^T/a_i`.                             (4.1)

Three exact identities are useful.

First, `K_i u_i=0`, so `K_i` has rank two. Second,

`U_-^T U_-=I-u_i u_i^T`,

and therefore `U_-` is an isometry on `u_i^perp`. Thus the two nonzero eigenvalues `mu_1,mu_2` of `S_i` are exactly the two nonzero eigenvalues of `K_i`.

Third,

`adj(K_i)=(det Lambda/a_i) u_i u_i^T`.                                  (4.2)

Indeed, for `K(s)=Lambda-s(Lambda u_i)(Lambda u_i)^T/a_i`, the matrix determinant lemma gives `det K(s)=det(Lambda)(1-s)`. Differentiating at `s=1` and using that a symmetric rank-two `3x3` matrix with kernel `span(u_i)` has adjugate proportional to `u_i u_i^T` proves (4.2). Comparing (4.2) with

`adj(K_i)=(mu_1 mu_2/ell_i) u_i u_i^T`

gives the exact product identity

`mu_1 mu_2=(det Lambda) ell_i/a_i`.                                     (4.3)

Finally, if `P_i^res` is the rank-two spectral projector of `S_i`, then for every `j!=i`,

`||(P_i^res)e_j||_2^2 = ||Proj_{u_i^perp} u_j||_2^2`.                    (4.4)

Thus diffuseness of the Schur residual is an explicit geometric statement about the original rank-three frame, not a rotated-coordinate independence assumption.

## 5. New hybrid branch obtained by applying the partner inequality

### Corollary 5.1 — `QFORM-RANK3-HEAVY-DIFFUSE-SCHUR-v1`

Under the rank-three setup above, assume `a_i!=0` and

`max_{j!=i} ||Proj_{u_i^perp}u_j|| <= 1/2`.                              (5.1)

Then `Q=X^TAX` has an essentially bounded density satisfying

`||p_Q||_infinity`
` <= (2 sqrt(2) B/pi) (|a_i| |det Lambda| ell_i)^(-1/4)`.                (5.2)

### Proof

The remaining physical coordinates are still independent with density caps one. Apply Theorem 3.1 to their rank-two Schur residual and then apply the partner's scalar-square inequality (2.1):

`p_Q(t)`
` <= |a_i|^(-1/2) E|t-X_{-i}^T S_i X_{-i}|^(-1/2)`
` <= (2 sqrt(2)B/pi)|a_i|^(-1/2)|mu_1mu_2|^(-1/4)`.

Substitute (4.3) to obtain (5.2). QED.

A useful constant-form specialization is this. Put `rho_i=a_i/ell_i` (the Rayleigh quotient of `Lambda` along the normalized heavy row). If

`ell_i>=1/4`, `|rho_i|>=eta>0`, `|det Lambda|>=1`,

then

`||p_Q||_infinity <= (4 sqrt(2) B/pi) eta^(-1/4)`.                       (5.3)

Thus a heavy coordinate is harmless whenever it is not too close to the null cone of the indefinite spectral form and its two-dimensional Schur residual is diffuse.

The proof establishes absolute continuity and an essential density bound. It does **not** establish a continuous representative in this branch.

## 6. Precise remaining factor

Combine fleet03/B05 with Corollary 5.1. For rank exactly three:

- if every spectral row has leverage norm at most `1/2`, the existing diffuse theorem closes the form;
- if a heavy row `u_i` exists and it has a non-negligible Rayleigh quotient, the only way Corollary 5.1 can fail is that its Schur residual is localized: some `j` has

`||Proj_{u_i^perp}u_j||>1/2`;

- geometrically this implies the squared Euclidean area of the physical spectral rows satisfies

`||u_i wedge u_j||^2 = ell_i ||Proj_{u_i^perp}u_j||^2 > ell_i/4`;

but an indefinite `Lambda` can still make the corresponding quadratic `2x2` restriction tangent or degenerate. A large Euclidean row area is therefore not yet a definite-pair certificate;
- if every heavy row instead has small `|rho_i|`, the obstruction is a genuine **near-isotropic heavy-pivot** regime. The fleet01/B19 hard saddle family has exactly this flavor and is known to require high-cardinality aggregation.

This is the first unpaid implication after the present run:

`QFORM-HEAVY-ISOTROPIC-OR-LOCALIZED-RESIDUAL-AGGREGATE-v1`.

One must convert the near-isotropic/localized residual geometry into a product-preserving hyperbolic/aggregate channel (such as fleet02/B10's hyperbolic-square theorem), or find a valid target counterexample. The live correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` rules out simply declaring that one such heavy pivot must expose a strong fixed disjoint rank-two block.

Arbitrary extra small nonzero eigenvalues remain a separate spectral-truncation debt after rank-exact-three closure; this report does not discard them.

## 7. Integrity

No simulation is used as evidence. The only numerical check performed during derivation was a private algebra sanity check of identity (4.3); the proof above is exact and does not depend on that check. The full conjecture remains open. No universal constant for the full target is claimed, and continuity remains unproved for the new branch.
