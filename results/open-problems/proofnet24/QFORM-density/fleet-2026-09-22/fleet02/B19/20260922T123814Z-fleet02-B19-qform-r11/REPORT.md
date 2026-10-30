# fleet02/B19 — universal proof assembly: singular-spectrum aggregation and dependent aggregate hyperbolic smoothing

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T123814Z-fleet02-B19-qform-r11`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET_SUPPORTING_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Exact target, corrections, and source-valid assembly

The target is the full arbitrary-law statement: for every dimension, every independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential-supremum bound for the density of `Q=X^TAX`, or produce a valid counterexample.

This report respects the live corrections: law-uniform pointwise Fresnel decay is false; a fixed coordinate cross minor alone is insufficient; unrestricted fiber suprema and generic X-ray data lose essential product provenance; diagonalization of `A` does not preserve input independence; and `C=pi` is not a universal target constant.

Completed source-valid pieces actually used are:

1. **fleet03/B19**, package commit `f600d39b2e88b14acf5af050076e1062cc33f1f6`, proves the critical diffuse rank-two `L^3` theorem and the localized rank-three diffuse-residual bound
   `||p_Q||_infinity <= 4 sqrt(3e) (|a| c |det Lambda|)^(-1/4)`.
   Its remaining exact-rank-three debt is two-level mixed-leverage / near-isotropic aggregation.
2. **fleet01/B19**, commit `072cf685a12893b44d555f14e4e610bcf2154037`, proves the full-matrix near-diagonal basin
   `||A-diag(A)||op<1/2 => ||p_Q||infinity <= pi/sqrt(1-2 delta)`
   and exhibits a rank-three target family on which every fixed physical triple degenerates while aggregate hyperbolic-square smoothing succeeds.
3. **fleet02/B09**, commit `fa592b592c61bd1597aa8cf3270c3c9f58f410bf`, proves direct multi-pivot linearization when an original-coordinate pivot block vanishes, but its determinant formulation can lose dimension on spread rank-two cross packets.
4. **fleet02/B10**, commit `1eba911614ef9f6683f8eacb5d6608a0f9a4b833`, proves hyperbolic-square smoothing for three independent scalar channels.
5. **QFORM-DIFFUSE-SEPARABLE-PHASE-v1**, interactive report commit `773b7fb6f0e6a8142066f0bac08d228dfc164fdb`, proves the diffuse-rank theorem survives arbitrary coordinate-separable perturbations and arbitrary outside couplings once a suitable physical principal block is present.

Thus a compact conditional end-to-end proof is now: close the near-diagonal basin by fleet01/B19; in the hard basin preserve original-coordinate product structure until one obtains either a diffuse separable rank-three block, a paid localized Schur branch as in fleet03/B19, a multi-channel linear pivot packet, or a hyperbolic-square aggregate packet; then condition outside and apply the corresponding source-valid smoother. The first unpaid implication is the universal **product-preserving extraction/aggregation step** from the three-large-eigenvalue hypothesis. Fixed-minor selection is already refuted as a universal bridge.

This run proves two aggregate smoothers that remove two unnecessary restrictions from that extraction problem.

## 2. Theorem A: rectangular singular-spectrum multi-pivot smoothing

### `QFORM-RECTANGULAR-MULTIPIVOT-SINGULAR-v1`

Let `I,J` be disjoint original-coordinate sets. Condition on all coordinates outside `I union J`. Assume

- `A[I,I]=0`;
- the rectangular cross block `B=A[I,J]` has second singular value `s_2(B)>0`.

Then for arbitrary independent input densities bounded by one,

`||p_{X^TAX}||_infinity <= 2 sqrt(pi) / sqrt(s_1(B) s_2(B)).`   (2.1)

The block may be rectangular and arbitrarily large. No coordinate minor or determinant of a square subblock is selected.

### Proof

After conditioning outside `I union J`, write `x=X_I`, `y=X_J`. Because `A[I,I]=0`,

`Q = 2 x^T(By+d) + H(y)`

for a deterministic vector `d` and arbitrary measurable quadratic-affine `H` under the conditioning.

Fix `y` and set `c=By+d`. For a product law with one-dimensional densities at most one, the sharp one-dimensional product-projection estimate gives

`||p_{c^T x}||_infinity <= sqrt(2)/||c||_2`.

Hence

`||p_{2 c^T x}||_infinity <= 1/(sqrt(2)||c||_2)`.

It remains to average `||By+d||_2^{-1}`.

Let `s_1>=s_2>0` be the two largest singular values of `B`, with corresponding left/right singular vectors `u_1,u_2` and `v_1,v_2`. Put

`Z=(v_1^T y,v_2^T y)`.

The two-dimensional orthogonal product-marginal theorem gives a density bound

`||p_Z||_infinity <= 2`.

Also

`||By+d||_2 >= [ (s_1 Z_1+d_1)^2 + (s_2 Z_2+d_2)^2 ]^(1/2)`

for suitable constants `d_1,d_2`. Thus the two-vector

`W=(s_1 Z_1+d_1,s_2 Z_2+d_2)`

has density at most

`M=2/(s_1 s_2)`.

For any probability density `h` on `R^2` with `h<=M`, layer cake gives the sharp elementary estimate

`E |W|^{-1}
 = integral_0^infinity P(|W|<t^{-1}) dt
 <= integral_0^infinity min(1, pi M t^{-2}) dt
 = 2 sqrt(pi M)`.

Therefore

`E ||By+d||_2^{-1}
 <= 2 sqrt(2 pi/(s_1 s_2)).`

Averaging the conditional linear-form density bound yields

`||p_Q||_infinity
 <= (1/sqrt(2)) 2 sqrt(2 pi/(s_1s_2))
 = 2 sqrt(pi)/(s_1s_2)^(1/2).`

The bound is uniform in the conditioned outside variables, so the same inequality holds unconditionally. QED.

### Why this is a genuine aggregation advance

The B09 determinant theorem pays `|det B_0|^{-1/2}` after selecting an invertible coordinate `2x2` minor `B_0`. Theorem (2.1) instead pays only the **top two singular values of the entire packet**. It therefore remains constant when determinant mass is spread over many tiny coordinate minors.

## 3. Exact target family separating singular-spectrum aggregation from minor selection

Let `m` be even. In `R^m` define

`u_1=m^(-1/2)(1,...,1)`,
`u_2=m^(-1/2)(1,...,1,-1,...,-1)`

with `m/2` plus signs and `m/2` minus signs, and put

`B_m=u_1u_1^T+u_2u_2^T`.

Then `B_m` has singular values exactly `1,1,0,...,0`. Its entries are `2/m` within the two sign classes and zero across them. Consequently every coordinate `2x2` minor has determinant of absolute value at most `4/m^2`, and this value is attained.

Now set

`A_m = [[0,B_m],[B_m^T,0]]`

on two disjoint `m`-coordinate blocks. The nonzero eigenvalues of `A_m` are exactly `1,1,-1,-1`, so every `A_m` is in the owner's target class.

Theorem A gives the dimension-free bound

`||p_{X^T A_m X}||_infinity <= 2 sqrt(pi)`

for every admissible product input law.

By contrast, applying the square-minor theorem to any coordinate `2x2` minor gives no better than

`2/sqrt(4/m^2)=m`,

and every larger square cross minor is singular because `rank B_m=2`.

Hence this is an exact arbitrary-dimensional target family on which **all coordinate-minor reciprocal costs diverge while the full rectangular packet has a constant smoothing parameter**. This directly strengthens the existing Walsh/Pluecker no-go: the right object can be a singular-spectrum aggregate rather than any individual minor.

## 4. Theorem B: hyperbolic-square smoothing with dependent aggregate channels

The independent-scalar hypothesis on the two aggregate channels in fleet02/B10 is also stronger than necessary.

### `QFORM-DEPENDENT-AGGREGATE-HYPERBOLIC-SQUARE-v1`

Let `X` be independent of a pair `(Y,Z)`. Assume

- `X` has density at most one;
- `(Y,Z)` has a joint density `g` with `||g||_infinity <= M`;
- `alpha,beta` are nonzero reals;
- `H,theta` are arbitrary measurable functions.

Then

`T = 2 alpha X Y + H(Y) + beta (Z+theta(Y))^2`

has an essentially bounded density satisfying

`||p_T||_infinity
 <= 6 M^(2/3) |alpha|^(-2/3) |beta|^(-1/3).`   (4.1)

No independence between `Y` and `Z` is assumed.

### Proof

For fixed `y`, let `m(y)=integral g(y,z)dz`. The shifted-square submeasure

`beta(Z+theta(y))^2`

has total mass `m(y)` and a density `k_y` satisfying, on the appropriate half-line,

`k_y(v) <= M/(sqrt(|beta|) sqrt(|v|)).`   (4.2)

The independent linear variable `2 alpha y X` has a probability density `h_y` with

`||h_y||_infinity <= L_y:=1/(2|alpha y|)`.

For any `R>0`, using (4.2) near the square singularity and total mass one of `h_y` away from it,

`||(k_y*h_y)||_infinity
 <= 2 M L_y sqrt(R)/sqrt(|beta|)
    + M/(sqrt(|beta|)sqrt(R)).`

The optimizing choice is `R=(2L_y)^(-1)`, which gives

`||(k_y*h_y)||_infinity
 <= 2M / sqrt(|alpha beta y|).`   (4.3)

The trivial convolution bound also gives

`||(k_y*h_y)||_infinity <= m(y)/(2|alpha y|).`   (4.4)

Since `H(y)` only translates the output, integrating the better of (4.3) and (4.4) yields, for any `R>0`,

`||p_T||_infinity
 <= 8 M sqrt(R)/sqrt(|alpha beta|)
    + 1/(2|alpha|R).`

Optimizing in `R` gives exactly

`6 M^(2/3)|alpha|^(-2/3)|beta|^(-1/3)`.

QED.

### Orthogonal-product corollary

If `(Y,Z)` is any two-dimensional orthogonal projection of an original-coordinate product law with one-dimensional density caps one, then `M<=2`. Therefore

`||p_T||_infinity
 <= 6*2^(2/3)|alpha|^(-2/3)|beta|^(-1/3).`   (4.5)

This applies even when the two aggregate directions overlap all of the same physical coordinates and are highly dependent.

For example, let `u,v` be any orthonormal vectors in `R^m` and let `X_0,X_1,...,X_m` be independent admissible coordinates. With

`Y=u^T(X_1,...,X_m)`, `Z=v^T(X_1,...,X_m)`,
`Q=2 alpha X_0 Y + beta Z^2`,

its nonzero eigenvalues are `|alpha|,-|alpha|,beta`. Thus `|alpha|,|beta|>=1` gives a genuine rank-three target family, and (4.5) proves a universal density bound although `Y,Z` need not be independent. This strictly enlarges the aggregate hyperbolic-square family closed by B10.

## 5. Application to the named partner and sharpened first unpaid implication

The newest named partner fleet03/B19 replaces the old local majority-sign obstruction by

`QFORM-TWOLEVEL-MIXED-LEVERAGE-AGGREGATION-v1`.

For a localized pivot `v` it has the exact resource

`sum_{j!=i} A_ij^2 = |Lambda v|^2-a^2 >= c-a^2`,

and it already closes the case where the whitened rank-two Schur residual is diffuse through a critical `L^3` bridge and dependence-safe square smoothing.

Theorems A and B identify two dimension-free ways to spend the remaining distributed coupling **before** selecting a small coordinate minor:

1. if a product-preserving two-pivot linear packet has top two cross singular values bounded below, Theorem A pays the whole packet at cost `(s_1s_2)^(-1/2)`;
2. if second-level localization collapses to one bilinear aggregate channel plus one quadratic aggregate channel, Theorem B pays it even when the two aggregate projections are dependent, requiring only the universal two-dimensional projection-density cap.

Thus the first unpaid implication can be stated more sharply:

> **`QFORM-MIXED-LEVERAGE-AGGREGATE-EXTRACTION-v2` (OPEN).** In the rank-exactly-three indefinite hard branch left by fleet03/B19, prove from the spectral/frame identities that second-level localization forces, with universal quantitative parameters, either (i) a diffuse Schur residual already paid by fleet03/B19, (ii) a rectangular two-channel linear packet to which Theorem A applies, or (iii) an aggregate hyperbolic-square packet to which Theorem B applies. The extraction must stay in the original product coordinates and may not select a single vanishing minor.

Even after this rank-three implication is closed, arbitrary additional spectral directions remain a separate debt except in already covered near-diagonal or separable-perturbation principal-block basins.

## 6. Status

**Proved in this run**

- `QFORM-RECTANGULAR-MULTIPIVOT-SINGULAR-v1` with explicit constant `2 sqrt(pi)/(s_1s_2)^(1/2)`;
- the exact rank-two flat cross family showing coordinate-minor reciprocal loss `~m` while the singular-spectrum bound stays `2 sqrt(pi)`;
- `QFORM-DEPENDENT-AGGREGATE-HYPERBOLIC-SQUARE-v1` with explicit constant `6 M^(2/3)|alpha|^(-2/3)|beta|^(-1/3)`;
- a genuine target-level overlapping-aggregate rank-three family closed by the dependent theorem.

**Not proved**

- the mixed-leverage aggregate extraction implication above;
- arbitrary extra-spectrum interaction outside already supported basins;
- the full conjecture;
- a continuous density representative in the direct small-ball branches.

No full-proof claim is made and no numerical census is used as closure evidence.

## 7. Source pins

- Fresh owner control initially read at `yspennstate/math-research-brain@6140a0528a06cc52e4b8bb8f75bb09160aafb464`, revision `2026-09-22.5`; prepublication main later observed at `f6d2e0022dfeb2760d307a8df432e6ee8b99bf46` with unchanged correction inbox.
- Named partner fleet03/B19 latest handoff blob `7937c8fdd82462a845cae1964524269c1e7c58ff`; canonical package commit `f600d39b2e88b14acf5af050076e1062cc33f1f6`.
- fleet01/B19 canonical report commit `072cf685a12893b44d555f14e4e610bcf2154037`, report blob `2530c90971b43a49cf9da35be03919868719abb9`.
- fleet02/B09 canonical report commit `fa592b592c61bd1597aa8cf3270c3c9f58f410bf`, report blob `a2e19e4b00617ac931a3a73036d2e3f2ea28d949`.
- fleet02/B10 handoff blob `32f901773eb6ae16172010d6a88b16a657d4c231`, canonical report commit `1eba911614ef9f6683f8eacb5d6608a0f9a4b833`.
- diffuse separable-phase canonical report commit `773b7fb6f0e6a8142066f0bac08d228dfc164fdb`, blob `d08d2488c072386e2b8ad818e30b1a6dec79e63a`.
- live correction inbox blob at prepublication refresh: `1681679e291cfd73917b46a25dc5bc8584d40bec`.
