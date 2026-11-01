# fleet01/B04 r12 — complete fixed-multiplicity source audit

Run: `20260924T141332Z-fleet01-B04-fixedmult-audit-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Owner-pinned baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Source observed on fresh master at start: `3a901aa5c1eda9b8291041cfc548fe4686685101`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Execution classification: `WITHOUT_VERIFIED_BRAIN`.

## Verdict

**PASS** for the mathematical theorem actually written in the 790-line baseline manuscript. I read all of `manuscript.tex`, `README.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` in this invocation. I found no fatal mathematical defect in the claim

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}\le 10^4 K^2/s
\]

for arbitrary dimension, arbitrary real symmetric signature and remaining spectrum, arbitrary deterministic affine terms, and arbitrary independent scalar densities bounded by `K`.

This is an independent worker audit, not owner-level validation or a release certificate. The unrestricted three-eigenvalue conjecture is not proved by the manuscript.

The current fleet has subsequently produced a complete nine-direction replacement proof and separate reviews; I reviewed that proof after completing the baseline audit. Section 4 below records the current threshold status. A new constant sharpening is written separately under this run's `improvements/` directory.

## 1. Complete manuscript line ledger

Every source line 1--790 is covered below. `PASS` means I checked the statement and the proof logic at the indicated source range. Nothing in the manuscript remains mathematically `UNCHECKED` except external bibliographic facts explicitly used as named standard results and the separately described build/checker execution metadata.

| Source range | Item | Status | Audit reasoning |
|---|---|---|---|
| 1--46 | title, abstract, setup, normalization and notation | PASS | Quantifiers match cap-`K` product laws, arbitrary symmetric `A`, affine `b,c`; the theorem is explicitly a fixed-multiplicity result, not the three-eigenvalue conjecture. |
| 47--57 | main 17-direction theorem | PASS | Scale `K^2/s` is consistent with `Y=KX`, `A/s`; final proof at 726--749 closes every pivot/no-pivot branch. |
| 59--90 | corollary, proof plan and conventions | PASS | Essential boundedness is correctly distinguished from the `C_0` conclusion proved only on Fourier-`L^1` branches in the baseline. |
| 91--120 | Fourier convention, Gaussian regularization, inversion | PASS | With `\hat f(t)=\int e^{itx}f(x)dx`, the Gaussian multiplier is `e^{-\epsilon t^2}`, Plancherel contributes `2\pi`, and inversion contributes `(2\pi)^{-1}`. Dominated/Fatou passage is legitimate. |
| 122--130 | power-envelope integration | PASS | Direct integration of `min(1,(u/|t|)^p)` gives the printed factor for `p>1`. |
| 132--160 | half-Riesz representation and envelope | PASS | The inner Gaussian integral gives the stated `\Gamma(1/4)` normalization; the final coefficient reduces to `(2\pi)^{-1/2}`. For `min(1,(u/|t|)^p)` at the used exponent, the weighted integral and constants check. |
| 162--181 | rank/singular-value perturbation | PASS | Weyl/Mirsky-type singular-value perturbation and rank-shift inequalities are used with the correct index loss. |
| 183--207 | Schur spectral count | PASS | For invertible `A`, `(A/B)^{-1}` is the complementary principal block of `A^{-1}`; positive and negative eigenvalue counts are handled separately. Kernel perturbation plus `t-|\epsilon|` passes to singular `A`. |
| 209--220 | strict diagonal dominance and transition | PASS | Standard row-dominance contradiction is applied only to a square principal block whose restricted rank bound is already established. |
| 221--255 | geometric Brascamp--Lieb heat-flow theorem | PASS | Independently re-derived in detail in Section 2 below: derivative sign, frame contraction, integration by parts, Gaussian domination, `t\to\infty` limit and rough-factor approximation all check. |
| 256--283 | product-projection density lemma | PASS | The BL frame is physical-coordinate based. If rows with `b_i=0` are dropped, the displayed `\sum_i(1-b_i)=d` is read over all original indices; equivalently the retained-index sum is `\le d`. This is a harmless indexing clarification, not a gap. No projected coordinates are declared independent. |
| 284--301 | scalar Fourier-power lemma | PASS | `|\hat f|^{2m}` is the Fourier transform of an `m`-fold difference convolution; integrability follows from `|\hat f|^{2m}\le|\hat f|^2`. The scalar projection bound gives the stated `m^{-1/2}` scale and interpolation to all `p\ge2` is valid. |
| 302--324 | two-copy decoupling | PASS | Cauchy--Schwarz/Weyl differencing cancels same-bank phases exactly; the difference coordinates remain independent with densities bounded by one. Affine terms are harmless phases. |
| 326--373 | determinant/BL crossing estimate | PASS | For `H=\alpha I+a^2M^TM`, the coordinate and row weights form an exact frame. `\theta=\sum d_i=\sum(1-c_j)`. Fourier-power factors, row Jacobians and coordinate entropy cancel against `\alpha=(2\pi e)^2`; fourth-rooting gives exponent `-1/8` and the printed determinant scale. |
| 374--400 | Cauchy--Binet volume corollaries | PASS | `\det(I+zM^TM)` expansion yields the order-5 density and order-3 half-potential constants. The order-3 branch is used through Riesz, not incorrectly through an `L^1` Fourier claim. |
| 401--414 | scalar-square measure domination | PASS | The two inverse branches and Jacobian give the displayed square kernel; the statement is measure domination and does not require pointwise density representatives on exceptional fibers. |
| 415--434 | definite two-coordinate pivot | PASS | Elliptic area/Jacobian calculation gives `\pi/\sqrt{\det B}` after conditioning on all outside original coordinates. |
| 435--482 | indefinite hyperbolic pair | PASS | Branch parametrization and Jacobian `1/(2\sqrt D)` check. The tail monotonicity cutoff and middle-length logarithm yield the stated `6+\log_+(16\sqrt D/|\delta|)` envelope. |
| 483--525 | quarter-power concentration | PASS | In the diagonal case the square-root interval estimate is correct. In the off-diagonal case the random-sign cut gives a physical crossing with the required norm; the determinant envelope plus Gaussian smoothing gives `2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8)<16` as used. Layer cake gives the logarithmic potential. |
| 526--544 | pivot/no-pivot definitions and entry consequences | PASS | Absence of a scalar/pair pivot implies the printed entry bounds; in particular `|a_{ij}|^2<\eta^2+\eta<1/49`. |
| 545--564 | determinant-squared seed sampling | PASS | Bordered determinant identity is exact. Summing extensions incurs at most `(r+1)^2`; singular seeds may have nonsingular extensions, so the inequality direction is correct. |
| 566--580 | completion/interpolation decomposition | PASS | `E` is the off-diagonal residual on `L\times L`, `D` is diagonal and vanishes on the seed, `R-P` is supported only on seed rows/columns, giving `rank R\le3r`, while `R[L,L]=P[L,L]` gives the sharper restricted rank `\le r`. |
| 582--619 | spectral-to-disjoint-volume proposition | PASS | If the volume ratios all fail, the sampled completion has small `E`. For `r=0`, diagonal plus off-diagonal norms contradict `\|A\|\ge1`. For `r\ge1`, `m\ge4r+1` yields enough large diagonal entries of `D`; the exact row-dominance margin is `371/400-23/28=297/2800>0`, contradicting `rank R[L,L]\le r`. |
| 621--630 | random physical cut | PASS | An ordered disjoint pair of `k`-sets crosses a fair cut with probability exactly `4^{-k}`. |
| 632--645 | no-pivot density/half-potential corollaries | PASS | `Z_k^{-1/(2k)}\le2\kappa^{-1/2}=160`; the printed `<200` and `<2400` arithmetic is valid. |
| 646--674 | singular kernels and convolution estimates | PASS | Layer-cake/Tonelli manipulations are nonnegative and valid for rough laws; truncated versus full potentials are kept separate. |
| 676--714 | pivot half-potential proposition | PASS | Scalar pivot combines square domination with the quarter/log estimate; definite pair and indefinite pair constants check. Tail `|Q-a|>1` is added only when passing to the full half-potential. |
| 716--724 | nine-direction half-potential proposition inside baseline | PASS | This is an auxiliary half-potential result, not a nine-direction density theorem by itself; the case split and constants are correct. |
| 726--749 | proof of the 17-direction theorem | PASS | No pivot `<2400`; scalar pivot `6010`; definite pair `<40`; indefinite pair `<251`. Schur count leaves the required number of directions in each branch. Scaling restores `K^2/s`. |
| 750--790 | remarks, limitations, references | PASS | The manuscript does not claim the full three-eigenvalue theorem or universal continuity. References are used in scopes consistent with the proof. |

## 2. Heat-flow lens: independent reconstruction of lines 221--255

Let `f_i(t,\cdot)=g_t*h_i`, `v_i=\partial_s\log f_i`, and

\[
F(t,x)=\prod_i f_i(t,u_i\cdot x)^{c_i},\qquad
\sum_i c_i u_i u_i^T=I_d.
\]

Because `\partial_t f_i=\partial_s^2 f_i`, one has

\[
\partial_t\log f_i=v_i'+v_i^2,
\qquad
\nabla\log F=\sum_i c_i u_i v_i,
\qquad
\Delta\log F=\sum_i c_i v_i'.
\]

Therefore

\[
\frac{(\partial_t-\Delta)F}{F}
 =\sum_i c_i v_i^2-
   \left|\sum_i c_i u_i v_i\right|^2.
\]

If `W` has columns `\sqrt{c_i}u_i`, then `WW^T=I_d`, so `\|W\|_{op}=1`; applying this contraction to the vector with coordinates `\sqrt{c_i}v_i` proves the right side is nonnegative. Thus the heat-flow integral is nondecreasing. **Derivative sign: PASS.**

For bounded compactly supported factors and `t` in a compact positive interval, Gaussian convolution gives Gaussian tails for `f_i` and polynomial-times-Gaussian control for the derivatives appearing above. Products are dominated by an integrable Gaussian because the frame identity gives `\sum_i c_i(u_i\cdot x)^2=|x|^2`. Hence differentiation under the integral and `\int\Delta F=0` by integration by parts are justified. **Integration by parts / domination: PASS.**

Taking traces in the frame identity gives `\sum_i c_i=d`. With `x=\sqrt t\,z`,

\[
\sqrt t\,f_i(t,\sqrt t\,u_i\cdot z)
\to (4\pi)^{-1/2}\Bigl(\int h_i\Bigr)e^{-(u_i\cdot z)^2/4}.
\]

The same Gaussian domination allows passage under the integral, and the frame identity collapses the limiting product Gaussian to the standard `d`-dimensional integral. This yields exactly `\prod_i(\int h_i)^{c_i}`. **Large-time limit: PASS.**

At `t\downarrow0`, Lebesgue differentiation holds simultaneously for the finitely many one-dimensional factors off a null union of inverse-image hyperplanes; Fatou gives the inequality for bounded compactly supported factors. Finally `h_{i,m}=\min(h_i,m)1_{[-m,m]}` increases to `h_i`, so monotone convergence proves the full nonnegative integrable statement. **Approximation limit: PASS.**

## 3. Repository support files

- `README.md`: **PASS** as a description of the current package; the files it lists are now present.
- `SOURCE_MANIFEST.json`: **PASS** for the source metadata. It records 790 lines, 47883 bytes, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, and SHA-256 `9f3b...5e69`, matching the source read in this run.
- `proof_map.csv`: **PASS**; every theorem/proof range agrees with the manuscript and is covered in Section 1.
- `verify.py`: **PASS as source-code audit**. Its assertions match the manuscript hash, the exact diagonal slack `297/2800`, the interpolation identities/rank tests, volume sampling, Schur numerical tests and graph-weight tests. **UNCHECKED as an execution event in this run**: I did not claim that I reran this repository script.
- `checks.json`: **PASS as a source-pinned recorded receipt**, reporting 534 interpolation seeds, 18 volume comparisons, 9 strict sampling cases, 240 Schur threshold cases and 30 graph-weight cases. **UNCHECKED as independent recomputation in this run**; finite checks do not replace the analytic proof.
- historical `AUDIT.md`: **PASS as historical self-audit metadata**. Its older finite-check counts are explicitly historical and were not independently reproduced here; those historical execution counts are **UNCHECKED**, without mathematical impact.
- compiled PDF/render claims in the manifest: **UNCHECKED** here because the binary is not part of the source package I read through the repository connector. This is a packaging/build-status item, not a mathematical gap.

## 4. Current threshold after the baseline audit

After finishing the baseline audit, I read the complete replacement proof `QFORM-FIXED-MULTIPLICITY-9-v1` from fleet03/B04 (blob `054facef834d29927713c5d42a1f09a541c5644b`). I independently checked its grouped product-Fourier compiler, the light-bank `L^2` difference argument, weighted-subset entropy inequality, Gram--Schmidt heavy-row promotions, marginal-free `E_3` density receiver, marginal-free `E_2` half-potential receiver, and the final pivot/no-pivot case split. **Verdict on that replacement proof: PASS.**

The nine-direction mechanism preserves arbitrary dimension, arbitrary signs and remaining spectrum, affine terms, and arbitrary rough product densities. Its no-pivot branch uses the audited `4k-3` structural proposition with `k=3`; pivot branches use the original physical-coordinate Schur machinery. No subclass substitution or post-rotation independence occurs.

Two genuinely separate pre-existing reviews are visible in the repository: fleet01/B16 commit `54ec2a651d854563f8db0d92c4c3426f76551786` independently reconstructed the nine-direction proof and reported PASS, and fleet03/B14 independently audited it and sharpened the constant. This B04 audit is an additional independent read. I do not self-assign owner-level validation/release status.

The current eight-direction work is not a completed uniform theorem. In the unresolved no-pivot collar, the repository proves quantitative overlap-one/two-sided currency and a universal half-potential, but not the required dimension-free linear interval estimate. Qualitative `C_0\cap L^\infty` regularity is known for each fixed rank-at-least-three matrix with a matrix-dependent height; that does not supply a universal eight-direction constant.

## 5. Classification

- Baseline 17-eigenvalue manuscript: **PASS**.
- Fatal defects found: **none**.
- Mathematical baseline lines marked `GAP` or `FALSE`: **none**.
- Execution/build metadata not independently rerun: explicitly **UNCHECKED** above.
- Nine-eigenvalue replacement proof: **PASS in this B04 review**, with existing separate reviews; owner-level status remains separate.
- Eight-eigenvalue universal-height theorem: **OPEN**.
- Full three-eigenvalue conjecture: **OPEN**.
