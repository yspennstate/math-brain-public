# fleet02/B20 — proof closure synthesis: heavy-isotropic residual-diffuse closure

**Run:** `20260922T125832Z-fleet02-B20-qform-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Assignment:** Proof closure and keeper, pathway SYNTHESIS  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source state

The owner target is: for every dimension `n`, every independent real coordinate family `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a density whose essential supremum is bounded by one universal finite constant, or produce a valid counterexample.

No Gaussianity, log-concavity, moment, compact-support, connected-support, diagonal-basis, or post-rotation independence assumption is made. The current corrections are enforced: law-uniform pointwise Fresnel decay is false; naive spectral-fiber supremum can lose dimension; rotated coordinates are not independent; a generic 3D X-ray cap alone does not control the indefinite two-sheet trace; conditioning on conjugate projected coordinates does not preserve a uniform conditional density cap; and the three-large-eigenvalue hypothesis does not force a single physical pivot with a useful rank-two Schur cross block.

The exact named partner `fleet03/B20` had no completed current-QFORM handoff at the fresh startup and subsequent source checks; its newest observed completed B20 run was from the superseded FEI programme. No partner result is fabricated. The present derivation instead consumes two compatible completed QFORM results:

1. fleet03/B10, canonical report `yspennstate/math-open-problems@c1af196adade03e07456c8f6e783f952b0fa0e8d`, proves the exact heavy-isotropic normal form and the boundary case `c=1`, together with the determinant identity `B^2|tau|=|det Lambda|`;
2. fleet01/B08, canonical report `yspennstate/math-open-problems@cdd32fd16a694a5f8acc7ba758e0db6596a3e4a1`, proves the product-space Fourier--Brascamp--Lieb estimate for a diffuse orthonormal frame and arbitrary coordinate-separable phases. Its proof, without the normalization `|lambda_j|>=1`, gives the determinant-scale rank-three bound `3e |det Gamma|^(-1/3)` for every invertible `3 x 3` spectral matrix `Gamma`.

A later compatible source, fleet02/B19, gives singular-spectrum multi-pivot and dependent hyperbolic-square aggregation but explicitly leaves mixed-leverage extraction open. The theorem below supplies a product-preserving reduction inside the exact heavy-isotropic leakage wall rather than invoking a vanishing coordinate minor.

## 2. Strongest conditional end-to-end argument currently supported

A complete proof would follow if the following two source-preserving bridges were closed.

First, an arbitrary target matrix must be reduced to strong spectral blocks without treating the orthogonal spectral complement as independent noise. The diffuse theorem already closes `A=D+U Lambda U^T` when `D` is diagonal/separable and `U` is diffuse, but an arbitrary nonseparable complement `C`, `CU=0`, is still unpaid.

Second, the exact-rank-three localized branch must be closed. Existing results pay: diffuse rank three; diffuse rank-two Schur remainders for a nonzero physical pivot; the leverage-one isotropic boundary; several pure-cross/two-zero-diagonal and aggregate hyperbolic-square configurations. The remaining heavy isotropic branch has the exact fleet03/B10 form below. The new theorem closes its residual-diffuse subbranch and proves that failure of this closure forces a finite, at-most-three-coordinate residual localization certificate.

Thus the full owner target remains open, but the one-heavy isotropic leakage wall is reduced to a strictly smaller localized collar rather than an unrestricted dependence problem.

## 3. Exact heavy-isotropic setup

Assume for this section that `A` has rank exactly three,

`A=U Lambda U^T`, `U^TU=I_3`, `|lambda_k(Lambda)|>=1`.

Let physical row `u_i` have leverage

`c=||u_i||_2^2 in (1/2,1)`

and put `e=u_i/sqrt(c)`. Assume the heavy row is isotropic:

`alpha=e^T Lambda e=0`.

Let

`beta=P_(e^perp) Lambda e`, `B=||beta||_2>0`, `f=beta/B`,

and choose a unit `g` so `(e,f,g)` is an orthonormal spectral basis. In this basis

`Lambda = [[0,B,0],[B,r,kappa],[0,kappa,tau]]`,

hence

`det Lambda=-B^2 tau`, so `B^2|tau|=|det Lambda|>=1`.          (3.1)

For `j!=i`, decompose

`u_j=sigma_j e+w_j`, `w_j in e^perp`.

Parseval gives

`sum sigma_j^2=1-c`, `sum sigma_j w_j=0`, `sum w_jw_j^T=I_(e^perp)`.    (3.2)

Write

`y_j=<w_j,f>`, `z_j=<w_j,g>`, `d=1-c>0`, `t_j=sigma_j/sqrt(d)`.

Then the three residual coefficient vectors `t=(t_j)`, `y=(y_j)`, `z=(z_j)` are orthonormal in the original residual-coordinate space. Equivalently the matrix `V` with rows

`v_j=(t_j,y_j,z_j)`, `j!=i`,

satisfies

`V^T V=I_3`.                                                     (3.3)

Define the residual projected coordinates

`W=sum t_j X_j`, `Y=sum y_jX_j`, `Z=sum z_jX_j`.

The exact quadratic form is

`Q=2B(sqrt(c)X_i+sqrt(d)W)Y+rY^2+2kappa YZ+tau Z^2`.             (3.4)

This identity records the leakage without declaring `W,Y,Z` independent.

## 4. New theorem: residual-diffuse closure

### Theorem 4.1 — `QFORM-HEAVY-ISOTROPIC-RESIDUAL-DIFFUSE-v1`

Under the hypotheses of Section 3, suppose

`max_(j!=i) ||v_j||_2^2 <=1/2`.                                  (4.1)

Then for arbitrary independent input coordinates with densities bounded by one, `Q` has a bounded continuous density and

`||p_Q||_infinity <= 3e [(1-c)|det Lambda|]^(-1/3)`

and therefore

`||p_Q||_infinity <= 3e(1-c)^(-1/3)`.                            (4.2)

#### Proof

Condition only on the original physical coordinate `X_i=x`. The remaining variables are still independent with the same density caps. Equation (3.4) becomes

`Q_x = 2B sqrt(c) x Y + (W,Y,Z)^T Gamma (W,Y,Z)`,                 (4.3)

where

`Gamma=[[0,B sqrt(d),0],[B sqrt(d),r,kappa],[0,kappa,tau]]`.      (4.4)

Its determinant is exact:

`det Gamma=-d B^2 tau=d det Lambda`, so

`|det Gamma|=(1-c)|det Lambda|`.                                 (4.5)

The first term in (4.3) is coordinate-separable in the original residual variables:

`2B sqrt(c)xY=sum_(j!=i) [2B sqrt(c)x y_j] X_j`.                  (4.6)

Thus the fleet01/B08 product Fourier--Brascamp--Lieb proof applies verbatim to the residual orthonormal frame `V`; it does not require the projected variables to be independent. For completeness, the determinant-scale `k=3` version of that proof gives

`|phi_(Q_x)(s)| <= min(1,(pi e/|s|)^(3/2)|det Gamma|^(-1/2))`.   (4.7)

Set `s_0=pi e |det Gamma|^(-1/3)`. Integrating the envelope,

`int_R |phi_(Q_x)(s)| ds <= 6 pi e |det Gamma|^(-1/3)`.          (4.8)

Fourier inversion yields

`||p_(Q_x)||_infinity <=3e |det Gamma|^(-1/3)`.                  (4.9)

The bound is uniform in `x`. Averaging the conditional laws over `X_i` proves (4.2). The same uniform integrable characteristic-function envelope gives continuity of the unconditional density. No post-rotation independence or conditional projected-density cap is used. QED.

### Immediate quantitative collar

If `c<=7/8`, then `1-c>=1/8`, so the direct diffuse branch satisfies

`||p_Q||_infinity <=6e`.                                         (4.10)

At `c=1`, the completed fleet03/B10 dependent-pair hyperbolic-square theorem gives the separate universal boundary bound `<7.560`. The genuinely unpaid near-boundary issue is therefore not the existence of the leakage decomposition, but controlling a localized residual frame uniformly as `c` approaches one from below.

## 5. New theorem: three-deletion localization collar

The direct row-leverage assumption (4.1) can be replaced by a finite dichotomy.

### Theorem 5.1 — `QFORM-HEAVY-ISOTROPIC-THREE-DELETION-COLLAR-v1`

In the setup of Section 3, run the following source-preserving greedy procedure on the residual frame `V`.

Start with retained set `R_0={j:j!=i}`, deleted set `D_0=empty`, Gram matrix

`G_0=sum_(j in R_0) v_jv_j^T=I_3`, `q_0=det G_0=1`.

At a stage with positive-definite `G=sum_(j in R)v_jv_j^T`, whiten the retained frame and define

`ell_j=v_j^T G^(-1)v_j`.

If every `ell_j<=1/2`, stop diffusely. Otherwise delete one row with `ell_j>1/2`. Then one of the following occurs after at most three such deletions:

**(A) Diffuse stop before localization.** `q=det G>=1/8`, all retained whitened leverages are at most `1/2`, and after conditioning on `X_i` and the at-most-two deleted original coordinates,

`||p_Q||_infinity <= 3e [q(1-c)|det Lambda|]^(-1/3)
 <= 6e[(1-c)|det Lambda|]^(-1/3)`.                               (5.1)

**(B) Finite localization.** For a deleted set `D` with `|D|<=3`,

`det G_R<1/8`,

and there is a unit `a in R^3` such that

`sum_(j in D) <v_j,a>^2 >1/2`.                                  (5.2)

Thus one residual spectral direction is more than half localized on at most three original physical residual coordinates.

#### Proof

For a deletion of row `v_j`, the matrix determinant lemma gives

`det(G-v_jv_j^T)=det G (1-v_j^T G^(-1)v_j)=q(1-ell_j)`.           (5.3)

A deleted heavy row has `ell_j>1/2`, so every such deletion multiplies `q` by a factor strictly smaller than `1/2`. Hence either the procedure stops with `q>=1/8` after at most two heavy deletions, or by the third deletion `q<1/8` (including the singular case).

In the diffuse stop, put `W_R=V_R G^(-1/2)`, so `W_R^TW_R=I_3`. After conditioning the deleted original coordinates, their contribution to `(W,Y,Z)` is a fixed vector and therefore produces only coordinate-separable linear terms in the retained independent coordinates. The retained quadratic spectral matrix is

`Gamma_R=G^(1/2) Gamma G^(1/2)`,

with

`|det Gamma_R|=q |det Gamma|=q(1-c)|det Lambda|`.                (5.4)

Applying the determinant-scale diffuse theorem proves (5.1).

For the localization branch, relative to the original residual orthonormal frame,

`G_R=I_3-sum_(j in D)v_jv_j^T`,

so `0<=G_R<=I_3`. If every eigenvalue of `G_R` were at least `1/2`, its determinant would be at least `1/8`; therefore `det G_R<1/8` gives a unit vector `a` with

`a^T G_R a<1/2`.

Using `sum_all v_jv_j^T=I_3`,

`sum_(j in D)<v_j,a>^2=1-a^T G_Ra>1/2`,

which is (5.2). QED.

### Fixed numerical corollary

If `c<=7/8`, branch (A) gives the universal numerical cap

`||p_Q||_infinity <=12e`                                        (5.5)

because both `q` and `1-c` are at least `1/8` and `|det Lambda|>=1`.

Consequently, in the exact heavy-isotropic rank-three branch with `c in (1/2,7/8]`, failure of a `12e` density bound through this mechanism forces the explicit finite localization certificate (5.2). This replaces an unrestricted dependent-leakage wall by an at-most-three-coordinate obstruction.

## 6. Connection to the full target and first unpaid implication

The new theorems do **not** prove the owner target and do **not** prove all exact rank-three cases. They advance the exact heavy-isotropic branch in a source-valid way.

The first sharpened local implication is now:

`QFORM-NEAR-LEVERAGE1-ISOTROPIC-LOCALIZED-CLOSURE-v1`:

> In exact rank three, under the Section 3 hypotheses, assume either `c>7/8` or the three-deletion collar produces a set `D` of at most three residual original coordinates carrying more than half of one normalized residual spectral direction. Prove a universal density bound by combining the zero physical pivot, the exact aggregate identity `||b||_2^2 |z^T A[-i,-i]z|=c|det Lambda|`, and one source-preserving multi-pivot / pure-cross / hyperbolic-square mechanism; or produce a genuine independent-coordinate counterexample.

The global first implication remains separate:

`QFORM-SPECTRAL-COMPLEMENT-SOURCE-PRESERVING-REDUCTION-v1`:

> Given arbitrary symmetric `A` with at least three `|lambda|>=1`, control the nonseparable spectral complement without declaring rotated coordinates independent and without a fiber supremum, or reduce it to one of the already-paid product-coordinate mechanisms with a universal quantitative loss.

No current source closes that global bridge. The latest fleet02/B19 handoff explicitly records an extra-spectral-direction debt after exact rank three.

## 7. Corrections and mechanism audit

This derivation never uses:

- law-uniform pointwise Fresnel decay;
- a spectral-fiber `L^infinity` supremum;
- independence of `W,Y,Z` or of any rotated coordinates;
- a bounded conditional density after conditioning on a conjugate projection;
- a single vanishing coordinate minor or a forced single Schur rank-two cross block;
- a generic 3D X-ray cap as a substitute for product provenance.

The only conditioning is on original independent physical coordinates. The Fourier--Brascamp--Lieb step is run on the retained original-coordinate product law, with conditioned contributions appearing solely as coordinate-separable linear phases.

## 8. Status

- Full QFORM target: **OPEN**.
- Exact named partner fleet03/B20 current-QFORM result: **not available at source checks; no adoption inferred**.
- `QFORM-HEAVY-ISOTROPIC-RESIDUAL-DIFFUSE-v1`: **PROVED**.
- `QFORM-HEAVY-ISOTROPIC-THREE-DELETION-COLLAR-v1`: **PROVED**.
- Target-level movement: none; mechanism-level movement: exact heavy-isotropic leakage reduced to a uniform diffuse branch or an at-most-three-coordinate localization certificate.
- Next method if unchanged on later runs: attack the localized collar via the exact zero-pivot aggregate certificate plus singular-spectrum multi-pivot aggregation, rather than repeating a diffuse-frame argument.
