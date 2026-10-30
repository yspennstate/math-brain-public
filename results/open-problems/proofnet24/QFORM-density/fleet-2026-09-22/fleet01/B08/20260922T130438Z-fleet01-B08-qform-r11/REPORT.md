# fleet01/B08 — dependent-pair hyperbolic-square smoothing and a heavy/diffuse bridge

Run: `20260922T130438Z-fleet01-B08-qform-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: `Diffuse eigenvector case`  
Outcome: `ESSENTIAL_STEP_APPLIED / TARGET_SUPPORTING_THEOREM / FULL_CONJECTURE_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact target, source state, and corrections

The full target remains open: for arbitrary dimension, arbitrary independent real inputs with one-dimensional densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a single finite universal bound for the density of `X^T A X` (and separately decide continuity).

Fresh control was read on `yspennstate/math-research-brain` main. The source snapshot used for the derivation was `aa49b2cdc46db4546cc5966137e0a64a89bc5e95`; before publication main had advanced to `11e3bf8d2af6472a8a18f2b9e5ea91557f663bf5` with the same owner revision. The live correction inbox at that later source includes, in particular, the failures of law-uniform pointwise Fresnel decay, naive fiber-sup integration, cross-minor-only extraction, conditional conjugate-variable caps, single-pivot Schur rank-two extraction, and the new `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` counterexample. The theorem below does not contradict the last correction: it preserves genuine independence of one scalar aggregate from the entire dependent projected pair.

Completed dependencies actually used:

1. Partner `fleet02/B08`, `QFORM-WHITENED-PHYSICAL-BLOCK-v1`, canonical report `yspennstate/math-open-problems@84657e690f8411d99602ddc772b622686c3874ed`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T124007Z-r11/REPORT.md`.
2. `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`, `yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`, path `proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`.
3. `fleet02/B10`, `QFORM-HYPERBOLIC-SQUARE-v1`, creation commit `1eba911614ef9f6683f8eacb5d6608a0f9a4b833`, canonical path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T1147Z-qform-rank3-coupled-B10-r1/REPORT.md`.
4. `fleet04/B20`, `QFORM-AGGREGATE-HYPERBOLIC-SQUARE-v1`, `yspennstate/math-open-problems@1f85677029fc5ae27fc69b278620ae89d789efd2`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260922T132134Z-fleet04-B20-QFORM-r1/REPORT.md`.
5. The two-dimensional product-projection density bound `<=2` (the `k=2` case of the Livshyts--Paouris--Pivovarov product-marginal theorem), already used in the team's cross-block proof.

The new theorem strictly extends the just-completed aggregate hyperbolic-square mechanism in one direction: the two variables feeding the square channel need not be independent; they may be an arbitrary dependent pair with a bounded joint density. Independence of the hyperbolic scalar from that whole pair remains essential.

## 2. Compact conditional end-to-end argument

For a rank-three saddle normal form one would like to expose

`T = 2 a X Y + H(Y) + b (Z+theta(Y))^2`

without paying small individual coordinate minors. If `X` is an aggregate of one original-coordinate block while `(Y,Z)` is a two-dimensional projection of a disjoint block, then original-coordinate independence gives `X independent of (Y,Z)`, while the product-projection theorem gives a dimension-free joint-density cap for `(Y,Z)`. The missing implication was whether this weaker dependence structure still smooths the hyperbolic-square singularity.

The answer is yes, with an explicit bound. This closes a new high-cardinality heavy/diffuse saddle family. It does not extract such a normal form from an arbitrary target matrix, so it is supporting progress rather than a full solution.

## 3. Main theorem: one independent scalar plus a dependent projected pair

### Theorem `QFORM-DEPENDENT-PAIR-HYPERBOLIC-SQUARE-v1`

Let `X` be a real random variable with probability density `f` satisfying

`||f||_infinity <= M < infinity`.

Let `(Y,Z)` be a real random pair, independent of `X`, with joint probability density `rho` satisfying

`||rho||_infinity <= K < infinity`.

Let `a,b` be nonzero real numbers and let `H,theta` be arbitrary measurable real functions (finite almost surely). Define

`T = 2 a X Y + H(Y) + b (Z+theta(Y))^2`.

Then `T` is absolutely continuous and

`||p_T||_infinity <= 6 K^(2/3) M^(2/3) |a|^(-2/3) |b|^(-1/3)`.

The statement is sign-uniform in `a,b`. No moment, support, regularity, log-concavity, or independence between `Y` and `Z` is assumed. This argument proves essential boundedness / absolute continuity; it does **not** prove that the density has a continuous representative.

### Proof

For almost every `y`, put

`rho_y(z)=rho(y,z)`,  `m(y)=integral rho_y(z) dz`.

Thus `m` is the marginal density of `Y` and `integral m(y)dy=1`.

Push the unnormalized measure `rho_y(z)dz` through

`v=b(z+theta(y))^2`.

Its density `g_y` satisfies, for `v` of the appropriate sign,

`g_y(v) = [rho(y,-theta(y)+sqrt(|v/b|)) + rho(y,-theta(y)-sqrt(|v/b|))] / [2 sqrt(|b v|)]`,

with the obvious reflection when `b<0`. Hence

`0 <= g_y(v) <= K / (sqrt(|b|) sqrt(|v|))`,

and `integral g_y(v)dv=m(y)`.

For `y != 0`, let `h_y` be the (unnormalized) density contribution of

`2 a y X + b(Z+theta(y))^2 + H(y)`

at fixed `Y=y`. It is the convolution of the density of `2ayX` with `g_y`. Two different estimates are available.

First, the affine image `2ayX` has density bounded by `M/(2|ay|)`, so

`h_y(t) <= M m(y)/(2|a y|)`.                                      (3.1)

Second, using the inverse-square-root bound for `g_y`,

`h_y(t) <= [K/sqrt(|b|)] integral f(x) |t-H(y)-2ayx|^(-1/2) dx`.

For any probability density `f<=M`, any `d!=0`, and any `c`, decreasing rearrangement of the kernel gives

`integral f(x)|c-dx|^(-1/2)dx <= 2 sqrt(2M)/sqrt(|d|)`.

Indeed the maximizing admissible density is bounded by `M` and can be packed on an interval of length `1/M` around the singularity; direct integration gives the displayed constant. Taking `d=2ay` yields

`h_y(t) <= 2 K sqrt(M) / sqrt(|ab| |y|)`.                         (3.2)

The exceptional value `y=0` has zero `Y`-probability because `Y` has a density. Therefore

`p_T(t)=integral h_y(t)dy`

for almost every `t`. For arbitrary `R>0`, use (3.2) on `|y|<=R` and (3.1) on `|y|>R`:

`p_T(t)
 <= [2K sqrt(M)/sqrt(|ab|)] integral_{|y|<=R}|y|^(-1/2)dy
    + [M/(2|a|R)] integral m(y)dy
 = 8K sqrt(M) sqrt(R)/sqrt(|ab|) + M/(2|a|R)`.

Minimizing `A sqrt(R)+B/R` at `R=(2B/A)^(2/3)` gives

`min = 6 K^(2/3) M^(2/3) |a|^(-2/3)|b|^(-1/3)`.

The bound is uniform in `t`, proving absolute continuity and the stated essential-supremum estimate. QED.

### Why the new correction does not refute this theorem

`QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` constructs a correlated triple `(S,Y,Z)` with bounded joint/conditional densities but with `2SY+Z^2` logarithmically singular. Here `X` is genuinely independent of the **whole pair** `(Y,Z)`. The proof uses that independence at the convolution step before any density cap is spent. Thus the correction precisely marks the boundary of the theorem rather than invalidating it.

## 4. Product-projection corollary: dependent aggregate square pair

Let `J` be a block of original independent coordinates and let `r,s in R^J` be linearly independent coefficient vectors. Put

`Y=r dot X_J`,  `Z=s dot X_J`,

and let

`G = [[||r||^2, r dot s],[r dot s, ||s||^2]]`.

The normalized map has orthonormal columns after whitening by `G^(-1/2)`. The two-dimensional product-marginal theorem therefore gives

`||p_(Y,Z)||_infinity <= 2 / sqrt(det G)`.

If an independent scalar aggregate `X` has density cap `M`, Theorem 3 gives

`||p_T||_infinity <= 6 * 2^(2/3) * M^(2/3)
                      * |a|^(-2/3)|b|^(-1/3) * (det G)^(-1/3)`.

If `r,s` are orthonormal, `det G=1`. If the scalar aggregate is a normalized one-dimensional projection of another disjoint product block, its density cap is at most `sqrt(2)`, and hence

`||p_T||_infinity <= 12 |a|^(-2/3)|b|^(-1/3)`.

If the scalar is one physical coordinate, retain `M<=1`, obtaining

`||p_T||_infinity <= 6*2^(2/3)|a|^(-2/3)|b|^(-1/3)`.

Unlike `QFORM-AGGREGATE-HYPERBOLIC-SQUARE-v1`, this corollary permits `Y` and `Z` to be dependent overlapping projections of the **same** original-coordinate block. A generic bounded pair density alone is not being used for an indefinite quadratic pushforward; the separate independent scalar is retained throughout the convolution proof.

## 5. Target-matching heavy/diffuse family and explicit partner application

This section applies the named partner `fleet02/B08` theorem to an actual inequality and stitches it to the new result.

Fix `0<c<1`. Split original coordinates into three disjoint pieces: one physical coordinate `h`, a block `G0`, and a block `J`. Choose unit vectors `w` on `G0` and orthonormal vectors `r,s` on `J`. Define three orthonormal physical vectors

`v1 = sqrt(c) e_h + sqrt(1-c) w`,
`v2 = r`,
`v3 = s`,

and put `U=[v1,v2,v3]` and

`Lambda = [[0,1,0],[1,0,0],[0,0,1]]`.

Then `A=U Lambda U^T` has exactly three nonzero eigenvalues `{1,-1,1}`, so it matches the target threshold exactly. Moreover

`Q = 2 S Y + Z^2`,

where

`S=sqrt(c)X_h + sqrt(1-c)(w dot X_G0)`,
`Y=r dot X_J`, `Z=s dot X_J`.

The scalar `S` is independent of the pair `(Y,Z)`. Because convolution cannot increase the density supremum and the coefficient of `X_h` is `sqrt(c)`,

`||p_S||_infinity <= c^(-1/2)`.

The pair `(Y,Z)` is a two-dimensional orthogonal projection of the product law on `J`, so

`||p_(Y,Z)||_infinity <=2`.

The new theorem therefore gives the dimension-free estimate

`||p_Q||_infinity <= 6*2^(2/3)c^(-1/3)`.                         (5.1)

This already closes the family even when `Y,Z` are highly dependent non-Gaussian projections with overlapping coordinate support.

Now assume additionally

`max_i w_i^2 <=1/2`,  `max_j (r_j^2+s_j^2)<=1/2`.

The physical row `h` has leverage `c`. Conditioning on `h`, the partner theorem has

`M=I-u_hu_h^T=diag(1-c,1,1)`,  `det M=1-c`.

After whitening, the residual row leverages are exactly `w_i^2` on `G0` and `r_j^2+s_j^2` on `J`, hence are all at most `1/2`. Since `|det Lambda|=1`, `fleet02/B08` gives

`||p_Q||_infinity <= 3e(1-c)^(-1/3)`.                            (5.2)

For `c<=1/2`, the unconditioned diffuse theorem gives `||p_Q||_infinity<=3e`. For `c>1/2`, combine (5.1) and (5.2):

`||p_Q||_infinity <= min{3e(1-c)^(-1/3), 6*2^(2/3)c^(-1/3)}`.

The two terms cross when

`c = 32/(32+e^3)`.

Consequently the **entire** heavy/diffuse interpolation family satisfies the uniform parameter-free bound

`||p_Q||_infinity <= 3(32+e^3)^(1/3) < 11.25`.

This is a genuine partner application: the partner's determinant-volume estimate is strongest before the heavy direction becomes too concentrated, while the new dependent-pair aggregate estimate removes its `(1-c)^(-1/3)` blow-up as `c` approaches one.

Continuity is available on the partner-covered diffuse subbranch from its integrable characteristic-function proof. The new dependent-pair theorem only establishes an essentially bounded density, so continuity is not claimed for the full stitched family by this report.

## 6. First remaining implication

The full conjecture remains open. The first diffuse/heavy structural debt is now

`QFORM-PRODUCT-PROJECTION-HYPERBOLIC-OVERLAP-v1`:

For a genuine rank-three minority-sign saddle with a leverage-heavy physical row, after an isotropic row is rotated to the canonical form one encounters

`Q = 2(sqrt(c)X_h + S_L)Y_L + Z_L^2`,

where `(S_L,Y_L,Z_L)` is a three-dimensional linear projection of the **same** residual product block. The theorem above handles this if `S_L` lives on a block disjoint from `(Y_L,Z_L)`; the partner diffuse theorem handles it when the whitened residual leverage is at most `1/2`. The unresolved overlap regime is to exploit the actual three-dimensional product-projection provenance strongly enough to control the extra `2S_LY_L` term without replacing true independence by a mere conditional-density cap (which the new fleet02/B10 correction proves false).

A solution of this overlap implication would substantially tighten the rank-three indefinite branch. Arbitrary additional spectral directions remain a further debt even after rank-three closure.

## 7. Status

Outcome: `ESSENTIAL_STEP_APPLIED / TARGET_SUPPORTING_THEOREM / FULL_CONJECTURE_OPEN`.

No full-solution claim is made. All signs `a,b!=0` are covered in the theorem. Degenerate cases `a=0` or `b=0` are outside this theorem and cannot be used to satisfy the target without another mechanism. No pointwise Fresnel claim, post-rotation independence, moment assumption, compact-support assumption, or simulation-based inference is used.
