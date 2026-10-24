# account01/B16 early checkpoint — crossing/Fresnel dimension trade

Status: supporting calculation in progress; full QFORM remains OPEN.

Run: `20260923T194021Z-account01-B16-QFORM-auto11`.

Source pins consumed before this calculation:

- designated partner account02/B16 r35: `math-open-problems@44d1b6391e145d4323077bbca0b16f68476df42f`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T182948Z-account02-B16-QFORM-r35/REPORT.md`;
- projected-crossing/product projection checkpoint: `math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`;
- live corrections in the brain: no independence after rotation; bounded joint projection density alone does not control an arbitrary indefinite curved trace; conditional projection-height shortcuts are invalid.

## Candidate generalization

Let original independent source coordinates be split as `I disjoint_union J disjoint_union K` and condition on `X_K`. Suppose the conditioned phase can be written

`Q = F(X_I) + 2 X_I^T M X_J + X_J^T D X_J + (W^T X_J)^T Gamma (W^T X_J) + b^T X_J + const`,

where `F` is arbitrary measurable real, `D` is diagonal in the ORIGINAL `J` coordinates, `M=U Sigma V^T` has rank `k`, `Gamma` is invertible symmetric `ell x ell`, and `W` is `|J| x ell`. Put `Sigma=diag(s_1,...,s_k)`. For each `j in J`, define the augmented source row

`a_j=(s_1 V_{j1},...,s_k V_{jk},W_{j1},...,W_{j ell}) in R^(k+ell)`,

`G=sum_j a_j a_j^T`, and normalized row leverage `c_j=a_j^T G^{-1}a_j` whenever `G>0`.

If `G>0` and every nonzero row satisfies `c_j<=1/2`, then the partner r35 proof extends verbatim from `(k,ell)=(2,1)` to arbitrary `k,ell`. If `M_I=||p_{U^T X_I}||_infinity`, the expected pointwise bound is

`|phi_Q(t)| <= B |t|^(-alpha)`,

where

`alpha=k+ell/2`,

`B=M_I 2^(k+ell) pi^alpha |det Gamma|^(-1/2) det(G)^(-1/2)`.

Indeed: push the complex `I`-side phase to `z=U^T X_I`, so its complex density has modulus at most `p_z`; Fresnel-linearize only the rank-`ell` same-side quadratic on the still-factorized ORIGINAL `J` bank; scale `y=2tz`; then apply geometric Brascamp--Lieb to the augmented rows and the pinned twisted scalar Fourier estimate `int |hat g|^p <=4pi/sqrt(p)`, `p>=2`. The row condition `c_j<=1/2` is exactly what ensures `p_j=1/c_j>=2`.

For `alpha>1`, integrating `min(1,B|t|^-alpha)` should give

`||p_Q||_infinity <= [alpha/(alpha-1)] [M_I 2^(k+ell)]^(1/alpha) [|det Gamma| det G]^(-1/(2alpha))`,

with a continuous `C_0` density.

Checks:

- `(k,ell)=(2,1)`, `M_I<=2`, gives exactly the designated partner constant `(5/3)2^(8/5)[|det Gamma|det G]^-1/5` and reproduces r35.
- `(k,ell)=(1,2)`, `M_I<=sqrt(2)`, gives the new complementary rank-one-cross/rank-two-curvature estimate
  `||p_Q||_infinity <=2^(11/4)[|det Gamma|det G]^-1/4 <6.728[|det Gamma|det G]^-1/4`.

The main report will verify constants and give a target-valid Walsh family for the new `(1,2)` branch. This is a source-preserving Fourier/Fresnel calculation, not a use of a bare projected-density cap in a curved coarea integral.
