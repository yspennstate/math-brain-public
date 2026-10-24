SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B11, 2026-09-23T22:00:48Z.
attacking: the r43 unique-heavy-row/two-diffuse-star survivor; determine whether splitting one hub's leaf mass supplies a third smoothing direction, and isolate the exact source-preserving resource that does.

# account02/B11 — r43 same-hub two-star obstruction and source-disjoint square splice

Programme: `QFORM-DENSITY-3EIG-20260922`, OWNER CONTROL revision `2026-09-22.15`.
Status: **ESSENTIAL_STEP_APPLIED / proof-interface obstruction + target-valid normalization closure / full unrestricted QFORM OPEN**.
Regularity: essential boundedness only in the positive scoped family below; no full-target continuity claim.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh inherited chamber

The latest designated partner result consumed here is account03/B11 r43,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T221215Z-account03-B11-QFORM-r43/REPORT.md`.

In its exact-rank-three indefinite survivor, after the pair-area, scalar-pivot, and strong-single-edge exits are paid, there is one heavy physical hub `i` and two **disjoint original-coordinate** leaf banks `B_1,B_2` such that

`q_i>3/4`, `|A_ii|<beta_0 s/16`, `|A_ij|<theta_0 s` for every leaf,

and

`sum_{j in B_r} A_ij^2 > theta_0^2 s^2`,  `r=1,2`,

where `beta_0=289/15984` and `theta_0=(sqrt(191)/32) beta_0 = 0.00780870609624...`.  The partner also retains a quantitatively nonzero internal-curvature coefficient.  Its first unpaid implication is to use that curvature jointly with the same-hub star without destroying original product provenance.

The mandatory rank-two control remains logarithmic; this report shows that the **mere existence of two disjoint leaf banks does not improve it at all** when the hub is shared.

## 2. Same-hub two-bank splitting is still rank two

Let `U,X_1,...,X_{2m}` be independent cap-one inputs and put

`c_j=(2m)^(-1/2)`,  `S_m=sum_j c_j X_j`,

with `B_1={1,...,m}` and `B_2={m+1,...,2m}`.  Define the same-hub two-bank core

`R_m = 2 b U S_m`,  `b != 0`.

Its physical matrix is

`[[0, b c^T],[b c, 0]]`,

so its only nonzero eigenvalues are `+|b|,-|b|`, regardless of the number of leaf banks.  In particular

`sum_{j in B_1} (b c_j)^2 = sum_{j in B_2} (b c_j)^2 = b^2/2`,

while `max_j |b c_j|=|b|/sqrt(2m) -> 0`.

Thus fixed star energy in two source-disjoint leaf banks plus arbitrarily small individual star edges does **not** manufacture a third quadratic direction.

This is also the exact endpoint predicted by the completed pinned Fresnel hub theorem in

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`:
with one hub and no additional spread square, Theorem H supplies only the borderline `|t|^{-1}` Fourier power.  The phrase “two disjoint stars” in that theorem means two independent hub directions; partitioning the leaves of **one** hub cannot be counted twice.

### Explicit logarithmic density

Take all `U,X_j` centered unit uniforms.  The law of `S_m` has a continuous density `g_m` with `g_m(0)>0`.  For `t != 0`, product change of variables gives

`p_{R_m}(t) = integral_{-1/2}^{1/2} g_m(t/(2 b u)) [2|b u|]^(-1) du`.

Choose `delta_m>0` so that `g_m(v)>=g_m(0)/2` for `|v|<=delta_m`.  For sufficiently small `|t|`, restrict to

`|u| in [ |t|/(2|b| delta_m), 1/2 ]`.

Then

`p_{R_m}(t) >= [g_m(0)/(2|b|)] log( |b| delta_m/|t| ) -> infinity`.

(The displayed constant is not optimized; only the logarithmic divergence matters.)  Hence the r43 two-bank star decomposition, taken without its separate curvature resource, still has the genuine opposite-sign rank-two logarithmic singularity.  This is a source-valid product example, not an arbitrary dependent-pair construction.

**Proof-interface consequence.**  Any proof of the r43 survivor that replaces the two star banks by two abstract bounded one-dimensional marginals and then claims “two stars give integrability” is invalid.  The nonzero r43 internal curvature must be used before such a collapse, or one must extract a genuinely source-disjoint third smoothing direction.

## 3. Exact target-valid normalization: a diffuse independent square removes the logarithm

Now add an entirely disjoint original-coordinate bank `Y_1,...,Y_k`, with

`w_l=k^(-1/2)`,  `W_k=sum_l w_l Y_l`,

and define

`Q_{m,k}= a W_k^2 + 2 b U S_m`,  `|a|>=1`, `|b|>=1`.

The two unit coefficient vectors `c,w` live on disjoint original-coordinate banks.  Therefore the physical coefficient matrix has exact nonzero spectrum

`{a, +|b|, -|b|}`.

So `Q_{m,k}` is a genuine exact-rank-three target family: signature `(2,1)` when `a>0`, and `(1,2)` when `a<0`, with all three nonzero eigenvalue magnitudes at least one.

For the flat choice and `m,k>=2`, the spectral projector has a unique heavy row at the hub `U`: its leverage is one, while every star leaf has leverage `1/(2m)` and every square-bank coordinate has leverage `1/k`.  If `m>=8200`, every physical star edge is below the r43 threshold `theta_0` while each of the two star banks still carries energy `b^2/2`.  Thus this is a normalization test for the collective-star geometry, with the third direction deliberately made source-disjoint.

### 3.1 Full-line half-Riesz bound

Let

`T_m = 2 b U S_m`.

The two columns consisting of the physical hub vector and the normalized star vector `c` are orthonormal in the original coordinate space.  Hence the completed orientation-free rank-two half-Riesz theorem

`math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`

gives, in its homogeneous refined form,

`sup_t E |T_m-t|^(-1/2) <= 16 sqrt(30) |b|^(-1/2)`.

This does **not** say that `T_m` has bounded density; Section 2 shows it need not.

By the Rogozin--Ball scalar projection theorem, the independent linear form `W_k` has density at most `sqrt(2)`.  Therefore the density of `a W_k^2` is bounded by

`sqrt(2) |a|^(-1/2) y^(-1/2) 1_{sign(a)y>0}`

after the obvious reflection when `a<0`.  Since the `Y` bank is genuinely independent of `(U,X)`, convolution with the preceding half-potential yields the real inequality

`||p_{Q_{m,k}}||_infinity <= 16 sqrt(60) (|a b|)^(-1/2) <= 16 sqrt(60)`.

Numerically, `16 sqrt(60)=123.9354670786...`.  No moment, support, log-concavity, diagonal-basis, or post-rotation independence assumption occurs.

This identifies the third-direction mechanism exactly: the rank-two star density remains logarithmically unbounded, while the independent square asks only for its finite half-order Riesz potential.

### 3.2 Sign-specific ruled estimate on the one-sheet side

Apply the completed ruled theorem (Theorem C) from the required pinned

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

For `a>0`, `Q_{m,k}` has signature `(2,1)`, so on the one-sheet side

`p_{Q_{m,k}}(t) <= pi sqrt(2)`,  `t>=0`.

For `a<0`, reflection gives the corresponding estimate on `t<=0`.  I do **not** extend this X-ray/ruling estimate to the opposite two-sheet side; the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction forbids that inference.  The half-Riesz convolution above pays the opposite side for this source-disjoint-square subclass.

## 4. What this changes in the r43 proof map

Partner r43 has now reduced the hard exact-rank-three finite-heavy-row chamber to one hub with two diffuse star banks and a separate quantitative internal-curvature resource.  Sections 2--3 show a sharp dichotomy about what can and cannot be inferred from that geometry:

1. **Not enough:** two source-disjoint leaf banks sharing one hub are still one rank-two hyperbolic form and retain the logarithmic singularity, even when every individual edge tends to zero.
2. **Enough:** if the third curvature can be realized on a genuinely source-disjoint normalized linear-form square, then product provenance gives a uniform full-line bound `16 sqrt(60)`; the pinned ruled theorem simultaneously gives `pi sqrt(2)` on the one-sheet side.
3. Therefore the first unpaid r43 implication is not “find two star banks” any more.  It is to convert the partner's nonzero internal curvature into an **overlap-safe half-Riesz resource** while it still shares original coordinates with the star, or to force a source-disjoint square/pair/volume exit.

I record the sharpened unpaid implication as

`QFORM-R43-SAMEHUB-CURVATURE-HALFRIESZ-v1`:

> In the unique-heavy-row r43 survivor, combine the quantitative internal curvature with the two same-hub diffuse star banks before conditioning/absolute values so that the rank-two logarithmic receiver gains a finite half-order potential uniformly.  Either prove the required opposite-two-sheet bound with all same-bank and cross-bank quadratic terms retained, or force a genuine source-disjoint third resource.  Do not count a partition of one star as two hubs, condition on a dependent projected coordinate, or discard a small nonzero shear perturbatively.

Closing this exact-rank-three implication would still leave the separate arbitrary-additional-nonseparable-spectrum bridge in the full owner target.

## 5. Source and correction discipline

Fresh brain controls were read through main `b8450d7f190783eea0b0375d55710844b6800a2a`, OWNER CONTROL revision `2026-09-22.15`; the live correction inbox blob remained `47b2ff15d8ca6acfe35d9fd3de3b6281a86439f3` immediately before publication.  Relevant prohibitions retained: no post-rotation independence, no arbitrary-joint coarea shortcut, no conditional-density-cap substitution, no X-ray-only two-sheet conclusion, and no replacement of a small matrix coefficient by a small random perturbation.

The earlier `EARLY_CALC.md` in this same run remains a correct r42-era localized-heavy-triple calculation, but r43 is the later designated-partner reduction and supersedes it as the active first-unpaid interface.  No full-QFORM solution or counterexample is claimed.