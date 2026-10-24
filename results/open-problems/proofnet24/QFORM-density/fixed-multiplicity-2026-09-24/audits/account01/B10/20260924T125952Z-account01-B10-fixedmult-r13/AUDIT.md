# account01/B10 fixed-multiplicity audit — r13

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Actual run sign-in: `2026-09-24T12:59:52Z`  
Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob read from current `master`: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Owner/source SHA-256 pin: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Fresh `math-open-problems/master` observed before the audit: `b9a766ebe4c465f200e0052b45d0fc1653f12a55`.

## Verdict first

**Mathematical candidate at multiplicity 17: PASS in this fresh B10 end-to-end review.** I found no FALSE statement and no fatal mathematical GAP in the 790-line manuscript proving

\[
 s_{17}(A)\ge s>0\Longrightarrow
 \|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s.
\]

This run is another review by the same account/slot and is **not** a second independent peer review and does not self-award validation. The unrestricted three-eigenvalue conjecture remains open.

**Repository-package GAP:** `README.md` advertises `proof_map.csv`, `SOURCE_MANIFEST.json`, root `verify.py`, and root `checks.json`; fresh direct reads on current `master` returned 404 for all four, and `proof_map.csv` was also absent at the pinned baseline commit. Therefore the advertised root finite-check package is not currently reproducible from that directory. This is not a proof dependency because every specialized mathematical ingredient used by the theorem is written in `manuscript.tex`.

No manuscript source line is mathematically UNCHECKED in this review. The missing root supplementary artifacts and the finite-check claims depending on them remain UNCHECKED as package/reproducibility claims.

## Complete source ledger

The ranges below partition the full source and record my own checks rather than importing another worker's verdict.

| source range | status | B10 check and reason |
|---|---|---|
| 1–83 | PASS | Definitions and quantifiers are coherent. Singular values of symmetric `A` are absolute eigenvalues. The theorem keeps arbitrary dimension, signature, remaining spectrum, affine `b,c`, and arbitrary independent real densities capped by `K`. The later normalization `Y=KX`, `A/s` gives exactly the `K^2/s` scale. |
| 84–151 | PASS | Fourier convention is consistent with `2π` Plancherel/inversion. Gaussian regularization has transform `e^{-εt^2}`. The Riesz computation gives the exact factor `(2π)^(-1/2)` and the weighted `3/4` envelope integral is `12 sqrt(u)`. Tonelli is used only on nonnegative majorants. |
| 152–220 | PASS | Approximation-number proof gives the two singular-value perturbation/rank inequalities for nonsymmetric matrices. For the Schur lemma, when `A` is invertible, `S^{-1}` is the complementary principal compression of `A^{-1}`; positive and negative interlacing separately imply the absolute-value count. The `A+εI` limit handles singular `A`. Strict diagonal dominance needs no symmetry. |
| 221–255 | PASS | In the heat-flow BL proof, `WW^T=I` makes the relevant column operator a contraction and gives `∂_tF-ΔF≥0`. Compact-support heat tails justify differentiation/integration by parts, the large-time Gaussian limit uses `Σc_i=d`, and monotone approximation closes general nonnegative inputs. |
| 256–287 | PASS | Product-projection proof correctly drops only factors with `b_i=0`, then applies BL to the remaining frame. `f_i^{1/b_i}≤f_i` because `0≤f_i≤1`; `-b log b≤1-b`; extending the left contribution by zero at `b=0` yields the stated `e^{d/2}` cap. Scalar scaling gives `sqrt(e)/|a|`. |
| 288–300 | PASS | With `m=floor(p/2)`, `2m≤p` and `|fhat|≤1` imply `|fhat|^p≤|fhat|^{2m}`. The latter is integrable because it is bounded by the Plancherel `L^2` power. It is the characteristic function of a sum of `m` independent differences; projection density at zero gives `2π sqrt(2e)/sqrt(p)`. |
| 301–328 | PASS | Decoupling conditions on original coordinate blocks only. One Cauchy–Schwarz introduces an independent `X'_J`; integrating original independent `X_i` gives the product of Fourier transforms. Jensen yields the fourth-power version. Difference coordinates are independent and have densities capped by one. |
| 329–400 | PASS | For `H=αI+a^2M^TM`, the normalized `e_j` and row vectors form the exact rank-one frame. The `c_j,d_i` Jacobian powers are correct. Scalar Fourier powers cancel the `d_i` factors; `-c log c≤1-c` produces the entropy term; `α=(2πe)^2` cancels it. Fourth roots give determinant exponent `-1/8`. Cauchy–Binet gives `Z_k`; retaining the order-`k` term gives exponent `k/4`. The `k=5` inversion and `k=3` half-Riesz constants are correct. |
| 401–500 | PASS | Square inverse branches produce the displayed `|z-v|^{-1/2}` profile and interval-preimage length. Definite-pair polar coordinates have Jacobian `1/(2 sqrt(|det B|))`. The hyperbolic parametrization has the same absolute Jacobian. On each tail, one original coordinate is monotone with derivative at least one third of its magnitude, and cap-one/mass-one controls the `1/|y|` integral. The middle length and AGM step give the displayed logarithmic envelope. |
| 501–535 | PASS | If no diagonal carries half the operator norm, the random-sign cut of the off-diagonal matrix has a cross block of norm at least `L/4`. One determinant singular factor gives the `|t|^{-1/4}` envelope. Gaussian smoothing has the displayed coefficient; the manuscript's `<16` is safe. Layer cake gives `4+4 log 16`. This run also proves a substantially better exact coefficient bound; see the improvement report. |
| 536–600 | PASS | `V_r` uses ordered disjoint pairs. The no-pivot entry estimate is valid: `|a_ij|^2<η^2+η<2η`, hence `|a_ij|<1/7`. The bordered-determinant identity in sampling is exact. Singular seeds can have nonsingular extensions, so the counting step is correctly an inequality, not equality; an exact diagnostic is supplied in `verify_b10.py`. The nonsymmetric interpolation satisfies exact row-`S`/column-`T` interpolation. In completion, `R-P` is supported in rows `T` or columns `S`, giving global rank `≤3r`, while `R[L,L]=P[L,L]` gives restricted rank `≤r`; `diag E=0` and `D=0` on the seed are exact. |
| 601–630 | PASS | If `V_k<κ^k`, telescoping supplies `r≤k-1` with `V_{r+1}<κV_r`. The `r=0` Frobenius branch contradicts `s_m(A)≥1`. For `r≥1`, `||E||≤(r+1)/80≤1/16`; with `m=4k-3`, the global rank loss leaves `m-3r≥r+1` large diagonal entries, all in `L`. The exact worst-case row-dominance slack for `r=4` is `371/400-23/28=297/2800>0`, contradicting restricted rank `≤r`. |
| 631–660 | PASS | Each ordered disjoint `k`-minor survives the fair coordinate cut with probability `4^{-k}`. With `κ=1/80^2`, the selected cross block has `Z_k^{-1/(2k)}≤160`. Substitution into the analytic receivers gives `12 sqrt(80e)<200` for `k=3` and `800e<2400` for `k=5`. |
| 661–730 | PASS | `H` is explicitly truncated. The `J(d)` near/far split and translated logarithmic-kernel rearrangement are valid. Scalar pivot uses the Schur complement and one-direction log control; definite and indefinite pair cases condition only on original coordinates and are uniform in induced affine terms. Full versus truncated half potential is not conflated. |
| 731–790 | PASS | Nine-direction proposition correctly takes the maximum of pivot and no-pivot branches and adds at most one outside the truncation window. In the main theorem, a scalar pivot leaves at least 16 Schur directions, hence at least nine; a pair leaves at least 15, while the indefinite branch needs only one. All normalized branches are below `10^4`. The general `K,s` scaling is exact. The limitations correctly avoid a three-eigenvalue or full continuity claim. |

## B10 exact arithmetic and adversarial diagnostics

The companion `verify_b10.py` and `checks_b10.json` are **diagnostics, not proof certificates**. They reproduce the following exact facts with rational arithmetic only.

1. Baseline `r=4` diagonal-dominance slack:
\[
\frac{371}{400}-4\frac{23}{112}=\frac{297}{2800}>0.
\]

2. Terminal sixteen-direction `4\times4` slack:
\[
\frac{371}{400}-3\frac{23}{112}=\frac{109}{350}>0.
\]

3. A singular sampled order-one seed can have a nonsingular disjoint order-two extension. In the symmetric four-coordinate diagnostic with only `a_{14}=a_{41}=a_{23}=a_{32}=1`, the seed `A[{1},{2}]` has determinant zero while the extension `A[{1,3},{2,4}]` has determinant `-1`. Thus the manuscript is correct to use `≤` rather than equality in the global extension count.

4. The block
\[
C=\begin{pmatrix}0&1&1\\1&0&1\\1&1&1\end{pmatrix},\qquad \det C=1,
\]
block-diagonalized `r=1,2,3,4` times, has exact ranks `3,6,9,12`. With the manuscript's seed choice (first coordinate in `S`, second in `T`, third in `L`) this is a finite adversarial check that the **particular manuscript completion** can attain global rank `3r` while the restricted block attains rank `r`. It is not a counterexample to a different completion or to the theorem.

## Package/reproducibility ledger

| item | status | reason |
|---|---|---|
| `README.md` | PASS for theorem/source description; GAP for advertised package contents | Current text accurately states the mathematical target but says the four supplementary files below are stored at root; direct reads disagree. |
| root `AUDIT.md` | PASS as self-audit summary; its finite-run claims UNCHECKED here | It is consistent with the source proof, but the advertised root checker/results are absent. |
| `proof_map.csv` | UNCHECKED / absent | 404 on current `master` and on baseline commit. This report supplies its own 1–790 range ledger. |
| `SOURCE_MANIFEST.json` | UNCHECKED / absent | 404 on current `master`; the git blob identity itself was directly read. |
| root `verify.py` | UNCHECKED / absent | 404; no claim of rerunning that missing checker. |
| root `checks.json` | UNCHECKED / absent | 404; root numerical claims remain unreproduced from the package. |

## Downstream status

- Candidate multiplicity 17: **PASS in this B10 review**, but not self-certified as independently validated.
- Improved constant: complete proof in the sibling improvement artifact; **not independently validated**.
- Multiplicity 16: still OPEN. The only unclosed no-pivot branch of the present mechanism is terminal sampled order `r=4`; the improvement report records a stronger exact structural normal form for that survivor.
- Full three-eigenvalue QFORM: OPEN.
