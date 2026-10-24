SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-24T12:29:30Z.
attacking: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924 — full end-to-end audit with B05 emphasis on product-projection densities, rough conditional slices, measurability, and source-valid counterexamples to forbidden slice shortcuts.

# account02/B05 independent audit — fixed-multiplicity candidate

Run: `20260924T122930Z-account02-B05-fixedmult-audit-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Repository: `yspennstate/math-open-problems`, branch `master`  
Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned `manuscript.tex` git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Owner/package-recorded source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Fresh master observed during this audit retained exactly that manuscript git blob.

## Verdict

**PASS for the mathematical 17-eigenvalue theorem in this independent B05 textual audit.** I found no FALSE statement and no theorem-breaking GAP in the 790-line pinned manuscript. This is one worker audit, not a release certificate or formal verification. The unrestricted three-eigenvalue QFORM conjecture is **OPEN** and is not claimed here.

**Repository-package GAP / UNCHECKED:** current master contains `README.md`, `AUDIT.md`, `manuscript.tex`, `audits/`, and `improvements/`, but the README-advertised `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` returned Not Found when requested directly. Therefore the mathematical proof is auditable because it is self-contained in `manuscript.tex`, but the advertised finite checker, proof map, and manifest cannot be independently rerun/read from the current repository package in this audit.

No multiplicity below 17 is claimed. I did not obtain a complete replacement proof with constants and a closed dependency map, so threshold reduction is **UNCHECKED / NOT PROVED** in this run.

## B05 lens: product-projection density reconstructed

### Lines 231–283, geometric BL and `lem:projection`: PASS

Let `U in R^{n x d}` have orthonormal columns and let the original independent coordinate densities satisfy `0<=f_i<=1`. Complete `U` to an orthogonal matrix `(U,W)`. For fixed projected value `y`, the marginal density is

`p(y)=int prod_i f_i((Uy)_i+w_i dot z) dz`.

This is a Fubini marginal of the original product density; no independence of the rotated coordinates is asserted. Put `b_i=|w_i|^2=1-|U^T e_i|^2`. Rows with `b_i=0` contribute factors at most one and may be dropped. For `b_i>0`, `v_i=w_i/sqrt(b_i)` gives `sum_i b_i v_i v_i^T=I_{n-d}`. Apply the proved geometric Brascamp--Lieb inequality with `h_i(t)=f_i((Uy)_i+sqrt(b_i)t)^{1/b_i}`. Since `f_i<=1`, `int h_i<=b_i^{-1/2}`. Therefore

`p(y)<=prod_{b_i>0} b_i^{-b_i/2}`.

Using `-b log b<=1-b` and restoring zero rows only on the harmless right-hand sum,

`log p(y) <= (1/2) sum_{b_i>0}(1-b_i) <= (1/2) sum_i(1-b_i)=d/2`.

Thus `||p_{U^T X}||_infty<=e^{d/2}`. The manuscript's final equality is correct when the sum is read over all original rows; if read only over retained rows it becomes `<=d`, still sufficient. This is PASS, with at most a wording clarification. Scaling gives the scalar cap `sqrt(e)/|a|`.

### Lines 284–302, integrated scalar Fourier powers: PASS

For `p>=2`, `m=floor(p/2)>=p/4`; because `|hat f|<=1`, `int|hat f|^p<=int|hat f|^{2m}`. The latter is the characteristic function of a sum of `m` independent differences and is integrable. The product-projection scalar estimate on the `2m` signed original coordinates, whose coefficient vector has norm `sqrt(2m)`, gives density at zero at most `sqrt(e)/sqrt(2m)`. Hence `int|hat f|^p<=2pi sqrt(2e)/sqrt(p)`. No conditional cap or rotated independence is used.

### Lines 303–374, provenance through decoupling/determinant: PASS

The decoupling uses disjoint original coordinate sets and an independent copy only of one original subvector. Difference coordinates remain independent with density cap one. The graph BL step is a deterministic integral inequality for linear functionals, not a probabilistic independence assertion. Every product-projection input therefore has valid original-source provenance.

## B05 lens: exceptional slices and rough-law uniformity

### Lines 415–438, scalar square: PASS

The conditional profile `p(z)<=|a|^{-1/2}|z-R|^{-1/2}` is promoted through nonnegative output test functions and Tonelli, not by selecting pointwise conditional density versions. The singularity is integrated rather than maximized.

### Lines 439–486, hyperbolic pair: PASS

The branch Jacobian is `1/(2sqrt(D))`. Each tail is paid using one original coordinate, only its density cap and mass. The critical output level may have an infinite density; this creates no exceptional-slice gap because the statement is used through nonnegative test functions. A singleton is output-Lebesgue-null for each conditioning parameter, and Tonelli handles the graph of critical values.

In `prop:pivot-H` the logarithmic envelope is integrated against the truncated `|z-a|^{-1/2}` kernel before outside averaging; the proved log-kernel integral is uniformly finite even when the critical value equals `a`. In the main indefinite-pair branch, the random critical value is a nonconstant Schur-complement quadratic polynomial; quarter-power concentration removes atoms and uniformly controls `E log_+(1/|R-z|)`. No exceptional conditional slice is promoted to a bounded conditional density.

### Lines 487–529, quarter-power concentration: PASS

Both routes preserve original-coordinate conditioning/provenance. The conclusion is a small-ball estimate and log-potential bound, not a hidden density cap.

## Source-valid counterexamples to invalid strengthenings

1. **Conditional rotated slice caps are false.** Let `X_1,X_2` be independent uniforms on `[-1/2,1/2]`, `Y=(X_1+X_2)/sqrt(2)`, `Z=(X_1-X_2)/sqrt(2)`. The joint density of `(Y,Z)` is one on `|Y|+|Z|<=1/sqrt(2)`, so `p_Y(y)=sqrt(2)-2|y|` and `||p_Y||_infty=sqrt(2)<sqrt(e)`. But `Z|Y=y` is uniform on a slice of length `sqrt(2)-2|y|`, so its conditional density diverges as `|y|->1/sqrt(2)`. Thus bounded projected marginal density does not imply uniform conditional rotated-slice caps. The manuscript correctly avoids this shortcut.

2. **Indefinite pair fiber supremum is false.** For independent `W_1,W_2~Unif[-1/2,1/2]` and `q=2W_1W_2`, direct integration gives `p_q(z)=log(1/(2|z|))` for `0<|z|<1/2`. The density is genuinely logarithmically unbounded at the critical level. The manuscript's logarithmic envelope is qualitatively sharp.

3. **Scalar square density cap is false.** For `Y~Unif[-1/2,1/2]`, `T=Y^2` has `p_T(t)=t^{-1/2}` on `0<t<1/4`. The half-potential receiver is necessary; a uniform conditional-density replacement would fail.

## End-to-end source ledger

| Source range / label | Status | Reason / impact |
|---|---|---|
| 1–60 theorem definitions/quantifiers | PASS | Full arbitrary-law, affine, sign, dimension scope retained. |
| 61–80 architecture/parameters | PASS | `9=4*3-3`, `17=4*5-3`; no hidden regularity. |
| 81–120 Fourier identities | PASS | Normalizations and approximate-identity argument consistent. |
| 121–160 envelope/Riesz | PASS | Constants and weighted integral rederived. |
| 161–181 rank perturbation | PASS | Valid for nonsymmetric auxiliaries. |
| 182–218 Schur count | PASS | Inverse compression plus singular approximation correct. |
| 219–230 diagonal dominance | PASS | No symmetry needed. |
| 231–264 geometric BL | PASS | Heat-flow sign, limits, rough approximation valid. |
| 265–283 product projection | PASS | Fully reconstructed above; no rotated independence. |
| 284–302 scalar Fourier powers | PASS | Product-projection input valid and inversion justified. |
| 303–330 decoupling | PASS | Original-coordinate independence only. |
| 331–374 determinant theorem | PASS | Frame scales, entropy cancellation, regularizer and fourth root correct. |
| 375–414 crossing volumes | PASS | Cauchy--Binet and exponents correct. |
| 415–438 scalar/definite pivot | PASS | Measure domination and deterministic 2D change of variables valid. |
| 439–486 hyperbolic pair | PASS | Jacobian/tails/logarithmic exceptional slice handling valid. |
| 487–529 quarter-power | PASS | Original-coordinate crossing, small-ball and log potential valid. |
| 530–545 definitions/no-pivot entries | PASS | Ordered disjoint convention and entry bound correct. |
| 546–572 sampling | PASS | Bordered determinant and multiplicity inequality correct. |
| 573–629 completion/volume | PASS | Global rank `<=3r`, restricted rank `<=r`, diagonal-dominance contradiction correct. |
| 630–666 random cut/no-pivot | PASS | `4^{-k}` and constants correct. |
| 667–720 kernels/pivot H | PASS | Full versus truncated potentials kept distinct; Tonelli-safe. |
| 721–790 nine-direction/main/scaling | PASS | All branches close below `10^4`; scaling exact; no continuity overclaim. |
| `SOURCE_MANIFEST.json` | GAP / UNCHECKED | Not Found on fresh master; proof does not depend on it. |
| `proof_map.csv` | GAP / UNCHECKED | Not Found; ranges reconstructed directly. |
| `verify.py`, `checks.json` | GAP / UNCHECKED | Not Found; finite diagnostics not reproduced. |

## Threshold accounting

The present audit secures the 17-eigenvalue baseline but does **not** lower it. The no-pivot density branch uses order-five crossing because the determinant envelope is `|t|^{-5/4}`, integrable; order four is the borderline `|t|^{-1}` and is insufficient by absolute inversion alone. Algebraically, the terminal `r=4` completion count uses 17 directions to force five large diagonal entries against restricted rank four. A lower multiplicity needs a new endpoint receiver or stronger structure; the three counterexamples above rule out doing this via conditional projected caps or unrestricted square/hyperbolic fiber suprema.

Next B05 obligation: attack the order-four/high-leverage endpoint by integrating true curved product fibers before maximalization, with an explicit uniform exceptional-slice argument and complete constants/dependency map.
