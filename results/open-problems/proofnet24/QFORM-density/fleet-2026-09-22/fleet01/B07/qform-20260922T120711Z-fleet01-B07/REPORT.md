# fleet01/B07 — quantitative diffuse-or-finite-core flag decomposition for exact rank three

**Run:** `qform-20260922T120711Z-fleet01-B07`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Coordinate minor selection  
**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Current scope and source pins

The later owner control supersedes the incoming FEI assignment. The live target is: for independent real coordinates with densities bounded by one and real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a dimension-free density bound for `X^T A X` or give a valid counterexample.

This report treats the exact-rank-three geometry and produces a quantitative dichotomy that removes the fully diffuse branch and compresses every remaining obstruction into a bounded physical-coordinate core carrying a spectral flag. It is not a proof of the full conjecture because extra spectral components and the localized indefinite hybrid remain unpaid.

Dependencies actually applied:

1. **Assigned partner fleet02/B07**, current handoff `20260922T120042Z-b07-65e12dbc`, canonical mathematics `yspennstate/math-open-problems@f232e0365995ab3a5fcb6e5906b3f887b7a58a9d`. It proves a Pluecker flag decomposition and gives the mandatory stress family with one exact heavy direction and two determinant-delocalized directions. I use that family below to test the new constants and to avoid the already-refuted bounded-triple-det-mass shortcut.
2. **fleet03/B05**, canonical report `yspennstate/math-open-problems@c828d2ee2f8acef5eb96892bc8a9a25594db0f51`. Its diffuse Fresnel–Brascamp–Lieb theorem says: for exact rank `r>=3`, `A=R Lambda R^T`, `R^T R=I_r`, if every projection leverage satisfies `||P e_i||_2<=1/2`, then with `D=(prod |lambda_j|)^(1/r)` the output density is bounded by `[B^2/(4 pi^2 D)] r/(r-2)` for an absolute constant `B`.
3. **fleet01/B09**, canonical report `yspennstate/math-open-problems@6dc9ff8894e196a28a48c3eb6ce917103722f0ec`. Its rank-three volume-cut theorem aggregates disjoint Pluecker mass before paying reciprocal-minor costs. The present result is complementary: it identifies what must happen when a diffuse whitening criterion fails.

Fresh corrections consumed before publication: `QFORM-CROSSMINOR-ALONE-FALSE` and `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`. No law-uniform pointwise Fresnel decay, post-rotation independence, or fiber-supremum estimate is used.

## 2. Setup

Let

`A = R Lambda R^T`

have exact rank three, where `R` is `n x 3`, `R^T R=I_3`, and the three eigenvalues of the real symmetric invertible `Lambda` obey

`min_j |lambda_j| >= 1`.

Write the `i`-th row of `R` as `r_i` and its leverage as

`ell_i = ||r_i||_2^2`.

Then

`sum_i ell_i = tr(R^T R)=3`.

Fix a parameter `c in (0,1)`. Define the heavy set

`H_c = {i : ell_i >= c/4}`,

its complement `L_c`, and the light Gram matrix

`G_c = R_{L_c}^T R_{L_c} = I_3 - R_{H_c}^T R_{H_c}`.

Immediately

`|H_c| <= 12/c`.

The useful concrete choice is `c=1/2`, giving at most 24 heavy coordinates.

## 3. Affine extension of the diffuse theorem

The fleet03/B05 proof is unchanged if, after conditioning outside a coordinate set, a linear term remains in the three spectral variables. Indeed, for invertible symmetric `M`,

`y^T M y + 2 d^T y = (y+M^{-1}d)^T M (y+M^{-1}d) - d^T M^{-1}d`.

Translation of the projected density multiplies its Fourier transform only by a unit-modulus character, so the Wiener `L^1` norm used in the B05 Fresnel argument is unchanged. Therefore the same density constant is uniform over arbitrary affine terms produced by conditioning physical coordinates.

This observation is essential below because conditioning heavy coordinates leaves a light quadratic block plus a heavy-value-dependent linear term.

## 4. Main theorem: diffuse-or-finite-core spectral flag

### Theorem `QFORM-FINITECORE-DIFFUSE-FLAG-v1`

With the setup above and any `c in (0,1)`, exactly one of the following conclusions is available.

### (A) Diffuse light branch

If

`G_c >= c I_3`,

then, after conditioning all heavy coordinates `X_{H_c}`, the conditional law of `Q=X^TAX` has a density bounded uniformly by

`3 B^2 / (4 pi^2 c)`.

Consequently the unconditional law has the same bound.

### (B) Localized spectral-flag branch

Let `q` be the number of eigenvalues of `G_c` strictly below `c`; thus `q in {1,2,3}` when branch (A) fails. Let `E` be the corresponding `q`-dimensional spectral subspace. Then there exists a `q`-tuple `I subset H_c` for which the squared projected `q`-volume satisfies

`det( (R_I V)(R_I V)^T ) >= (1-c)^q / binom(|H_c|,q)`,

where the columns of `V` form any orthonormal basis of `E`. In particular, using `|H_c|<=12/c`,

`max_{I subset H_c, |I|=q} det(R_I V)^2 >= (1-c)^q / binom(floor(12/c),q)`

(with the obvious harmless ceiling/floor adjustment when `12/c` is not integral).

For the concrete choice `c=1/2`, `|H|<=24` and one obtains the explicit witnesses

- `q=1`: squared one-direction loading at least `1/48`;
- `q=2`: squared projected area at least `1/1104`;
- `q=3`: squared projected volume at least `1/16192`.

When `q=3`, `E=R^3`, hence some physical heavy triple `I` obeys

`|det A[I,I]| = |det Lambda| det(R_I)^2 >= 1/16192`.

### Proof of branch (A)

Put `G=G_c` and assume `G>=cI`. Define the whitened light frame

`Rtilde = R_L G^{-1/2}`.

Then `Rtilde^T Rtilde=I_3`. For every light row,

`elltilde_i = r_i G^{-1} r_i^T <= c^{-1} ell_i < 1/4`,

because `i in L` means `ell_i<c/4`. Thus the leverage criterion in the B05 theorem holds:

`||Ptilde e_i||_2 = sqrt(elltilde_i) < 1/2`.

The light-light quadratic block factors exactly as

`A_LL = R_L Lambda R_L^T = Rtilde M Rtilde^T`,

where

`M = G^{1/2} Lambda G^{1/2}`.

Since `sigma_min(Lambda)>=1` and `G>=cI`,

`sigma_min(M) >= sigma_min(G^{1/2})^2 sigma_min(Lambda) >= c`.

As `M` is symmetric, all three of its eigenvalues have absolute value at least `c`, so

`D_M = |det M|^(1/3) >= c`.

Condition on `X_H`. The remaining variables are still independent with the same one-dimensional density caps. The conditional quadratic is the light block plus an arbitrary linear term and constant. By Section 3 and the B05 theorem with `r=3`,

`||p_{Q | X_H}||_infinity <= 3 B^2/(4 pi^2 D_M) <= 3 B^2/(4 pi^2 c)`.

The bound is uniform in the conditioned heavy values, and averaging conditional densities preserves it. This proves (A).

### Proof of branch (B)

Let

`T = R_H^T R_H = I-G`.

If `E` is the span of the `q` eigenvectors of `G` with eigenvalues below `c`, then on `E`

`T|_E > (1-c) I_E`.

Let `V` be a `3 x q` orthonormal basis matrix for `E` and set

`W = R_H V`.

Then

`W^T W = V^T T V > (1-c) I_q`,

so

`det(W^T W) > (1-c)^q`.

Cauchy--Binet gives the exact determinant accounting

`det(W^T W) = sum_{I subset H, |I|=q} det(W_I)^2`.

There are `binom(|H|,q)` summands, hence at least one is at least their average, proving the claimed lower bound. For `c=1/2`, direct substitution yields

`(1/2)/24 = 1/48`,

`(1/4)/binom(24,2) = 1/1104`,

`(1/8)/binom(24,3) = 1/16192`.

For `q=3`, `V` is an orthogonal `3 x 3` matrix, so `det(R_I V)^2=det(R_I)^2`; the rank-three principal-minor identity

`det A[I,I] = det(Lambda) det(R_I)^2`

gives the final assertion. QED.

## 5. Application to the assigned partner stress families

This theorem directly sharpens and classifies the fleet02/B07 mechanisms.

### Walsh rank-three projection

In the partner's Walsh projection, every leverage is `3/n`. For `n>=32`, every coordinate is light at `c=1/2`, hence `H` is empty and `G=I`. The construction is therefore automatically in branch (A), even though every bounded-size physical principal block tends to zero. This is exactly the phenomenon B07 is supposed to preserve: determinant information must first be aggregated/whitened rather than paid through one physical minor.

The partner independently closed this family by four-class high-cardinality aggregation; the present theorem supplies a second, frame-geometric closure from the diffuse Wiener/Fresnel mechanism.

### One-heavy-direction / two-delocalized-directions family

For the partner's exact counterexample to bounded-coordinate determinant-mass capture (one row `e_1`, many copies of `e_2/sqrt(m)` and `e_3/sqrt(m)`), the choice `c=1/2` puts the `e_1` coordinate in `H`, while

`G = diag(0,1,1)`.

Thus `q=1`, the localized spectral line is exactly `span(e_1)`, and the heavy witness has squared loading `1`, far above the guaranteed `1/48`. The determinant mass in the other two directions may still be spread over arbitrarily many tiny triples; the theorem does not incorrectly demand otherwise. This is why the flag conclusion is the correct replacement for the refuted bounded-triple-mass shortcut.

## 6. What this pays and what remains unpaid

The exact-rank-three problem now has a clean quantitative split:

1. If deleting at most 24 high-leverage coordinates leaves spectral Gram at least `I/2`, the density is bounded by the diffuse theorem, uniformly in the conditioned heavy values.
2. Otherwise a `q=1,2,3` spectral flag has a quantitative witness on at most 24 physical coordinates, with explicit one-/two-/three-volume lower bounds above.
3. In the fully localized `q=3` endpoint, one gets a physical principal `3 x 3` determinant of magnitude at least `1/16192`; this is a true constant-scale coordinate minor, not a dimension-dependent selection.

The first unpaid implication is therefore narrower than generic determinant aggregation:

`QFORM-FINITECORE-FLAG-HYBRID-v1`: close the `q=1` and `q=2` localized-plus-diffuse branches (and the indefinite `q=3` physical-triple branch) by a product-preserving smoothing inequality, and then make the reduction stable under arbitrary additional spectral components of the full matrix.

The fleet01/B09 rank-three bilinear-cut theorem handles a complementary branch whenever two disjoint spectral bases carry enough Pluecker mass; fleet03/B11 handles one special physical saddle-plus-square geometry. The missing theorem must combine the finite-core flag with the diffuse complement without projecting away the original product structure or using the refuted rank-two-cross-minor shortcut.

## 7. Status

`ESSENTIAL_STEP_APPLIED` for the exact-rank-three structural reduction and diffuse closure.  
`FULL_TARGET_OPEN`: arbitrary extra eigencomponents and the localized indefinite flag hybrid are not solved here.  
No full-proof promotion, novelty claim, or brain-ingestion claim is made.
