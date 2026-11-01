# fleet02/B08 fixed-multiplicity audit — r2

Run: `20260924T134341Z-fleet02-B08-fixedmult-audit-r2`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Fresh package head at the start of this run: `8c893780233ba299a0fa3954b07409f462d744fe`; fresh head immediately before START write: `c44630d8ef37149a7c6c3600277ee7b7e58860b7`. The manuscript blob remained the pinned blob after the START write.

## Verdict

**PASS for the complete mathematical 17-eigenvalue candidate.** I performed a fresh end-to-end read of all 790 source lines and the full package. I found no mathematical gap or false statement in the candidate

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s
\]

for arbitrary real symmetric `A`, arbitrary affine `b,c`, and arbitrary independent real coordinate densities bounded by `K`.

This is an audit report, not formal verification and not a self-awarded release certificate. The unrestricted three-large-eigenvalue QFORM problem is **not** solved here. I obtained no complete replacement proof below multiplicity 17, so I do not lower the theorem threshold in this run.

The package gap recorded by this slot in the earlier r1 audit is now **RESOLVED**: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are present on current `master` and were read in this run.

## Complete source ledger

Every source line is included in one of the following ranges. `PASS` means I independently checked the displayed formulas, hypotheses, proof step, and downstream invocation in this run.

| Lines / statement | Status | Reasoning / hypothesis check | Impact / next obligation |
|---|---|---|---|
| 1–83: definitions, theorem, corollary, parameters, architecture | PASS | Singular values are consistently used for nonsymmetric auxiliaries and eigenvalue moduli for symmetric `A`. The theorem retains arbitrary dimension, signs, remaining spectrum, affine terms and rough product laws. The later scaling is exactly homogeneous of degree two. | Target and quantifiers close correctly. |
| 84–151: Fourier convention, Gaussian regularization/inversion, power envelope, Riesz half potential | PASS | Plancherel/inversion use the stated `2π` convention. The gamma representation and the `v`-integral give the coefficient `(2π)^(-1/2)` in the half-potential inequality. The `3/4` envelope gives weighted integral exactly `12 sqrt(u)`. | Fourier constants feeding every later branch are consistent. |
| 152–220: singular-value perturbation, Schur count, strict diagonal dominance | PASS | Approximation numbers prove both singular-value statements without symmetry. The Schur proof correctly uses the complementary compression of `A^{-1}` and treats positive/negative eigenvalues separately; `A+εI` handles singular `A`. Row diagonal dominance does not require symmetry. | Valid for the nonsymmetric matrices created later. |
| 221–255: geometric rank-one Brascamp–Lieb | PASS | The frame operator is a contraction, yielding the heat-flow differential inequality. Compactly supported heat convolutions justify differentiation and integration by parts, the large-time Gaussian limit uses `sum c_i=d`, and monotone approximation handles rough inputs. | Specialized BL input is self-contained at the used constant. |
| 256–287: product projections | PASS | Zero-`b_i` factors are dropped; after extending `-b log b` by zero at `b=0`, the entropy sum is bounded by `sum_i(1-b_i)=d`. The `d=n` endpoint is handled separately. | The earlier wording subtlety is already harmless as written; no proof change needed. |
| 288–300: integrated scalar Fourier powers | PASS | `m=floor(p/2)` and `|fhat|<=1` reduce to the integrable even power. Fourier inversion of the independent-difference sum and the product-projection lemma yield `2π sqrt(2e)/sqrt(p)`. | Correct input to the graph determinant. |
| 301–328: decoupling | PASS | Cauchy–Schwarz is in the original coordinate law, then an independent copy of `X_J` is introduced. Integration over original independent `X_i` produces the scalar Fourier factors; Jensen gives the fourth-power form. Difference coordinates are independent and cap one. | No rotated-coordinate independence or moment assumption is introduced. |
| 329–400: regularized crossing determinant and volume envelopes | PASS | `H=αI+a^2M^TM` gives an exact rank-one frame. The one-dimensional scale factors in BL are correct. Scalar Fourier powers cancel the `d_i` factors; `α=(2πe)^2` cancels the entropy multiplier. Fourth roots give determinant exponent `-1/8`. Cauchy–Binet gives `Z_k`; `k=5` is directly integrable and `k=3` is used only with the Riesz weight. | Fourier receiver is correct at the claimed exponents. |
| 401–500: scalar square, definite pair, hyperbolic pair | PASS | Square inverse branches and interval preimages are correct. Definite polar coordinates have Jacobian `1/(2 sqrt(|det B|))`. Hyperbolic coordinates have the same absolute Jacobian; each tail is controlled by one original-coordinate density and total mass one, while the bounded middle interval gives the logarithm. | Pivot estimates retain product provenance. |
| 501–535: quarter-power concentration and logarithmic potential | PASS | If no diagonal is large, the random sign cut of `offdiag S` has a cross block with norm at least `L/4`. One singular factor in the determinant estimate gives `|t|^{-1/4}`; Gaussian smoothing gives the stated `rho^(1/4)` concentration. Layer cake gives `4+4 log 16`. | One surviving spectral direction suffices for the logarithmic terms. |
| 536–564: `V_r`, no-pivot entry bound, sampled interpolation | PASS | Absence of a principal two-coordinate pivot implies `|a_ij|<1/7`. The bordered determinant identity is exact. Sorting contributes only a sign, removed by squaring. Singular seeds can have nonsingular extensions, so the sampling count is correctly an inequality. `P=A[:,T]B^{-1}A[S,:]` interpolates rows `S` and columns `T` exactly. | Sensitive nonsymmetric interpolation step is correct. |
| 566–580: completion and two rank bounds | PASS | With `E` only on off-diagonal `L×L` and `D_ii=A_ii-P_ii` on `L`, one has `R[L,L]=P[L,L]`. `R-P` vanishes on rows `S`, columns `T`, and `L×L`, hence every remaining entry is in a row `T` or column `S`. Splitting those supports yields `rank(R-P)<=2r`, so `rank R<=3r`; restriction gives `rank R[L,L]<=r`. `D` vanishes on the seed and `diag E=0`. | Both rank bounds and support propagation are valid. See the sharpness family below. |
| 582–619: no-pivot spectral-to-volume proposition | PASS | A bad telescoping ratio yields `||E||<=1/16`. With `m=4k-3` and `r<=k-1`, global rank `3r` leaves at least `r+1` large entries of diagonal `D`; seed vanishing puts all of them in `L`. On an `(r+1)`-set, `|R_ii|>=371/400` and each off-diagonal is `<1/7+1/16`; for `r<=4` the row sum is `<23/28`. Strict diagonal dominance contradicts `rank R[L,L]<=r`. The `r=0` branch follows from the Frobenius norm. | This is the exact source of the count `4k-3`. |
| 621–645: random cut and no-pivot order-3/order-5 consequences | PASS | Each ordered disjoint minor survives the fair cut with probability `4^{-k}`. With `kappa=1/80^2`, one gets `Z_k^{-1/(2k)}<=160`; hence `12 sqrt(80e)<200` and `800e<2400`. | Nine directions give a full half potential; seventeen give density in the no-pivot branch. |
| 654–714: singular kernels and pivot control of truncated half potentials | PASS | The split for `J(d)` and the interval-overlap argument for the log kernel are valid. Scalar pivot uses the exact conditional square profile and a surviving Schur eigenvalue; definite and indefinite pair estimates are uniform under conditioning on original coordinates. Truncated and full half potentials are kept distinct. | Pivot branch closes without exceptional-slice or conditional-cap shortcuts. |
| 716–724: nine-eigenvalue half-potential proposition | PASS | Pivot gives truncated `H<=600`; no pivot gives the stronger full `<200`. Outside unit distance the half-kernel is at most one, hence full potential `<=601`. | Correct dependency for the scalar pivot in the main theorem. |
| 726–790: main theorem, scaling, accounting and limitations | PASS | No pivot gives `<2400`. A scalar pivot under `s_17>=1` leaves at least 16 Schur directions, so the nine-direction bound applies and gives 6010. A definite pair gives `<40`; an indefinite pair leaves at least 15 Schur directions and only one is needed for the log potential, giving `<251`. For general `K,s`, `Y=KX` has cap-one coordinates and `Q=(s/K^2) Qtilde`, yielding exactly `10^4K^2/s`. Final limitations correctly avoid continuity and three-eigenvalue claims. | Candidate closes as stated. |

**UNCHECKED mathematical source lines: none.** Classical references are attribution only; all specialized estimates used by the proof are reproved in the manuscript.

## B08 counterexample audit: every rank contribution is sharp

The previous B08 sharpness family can be strengthened to show that not only the final `3r` and restricted `r` bounds, but also the two support legs in `R-P`, are simultaneously saturated.

Let
\[
C=\begin{pmatrix}0&1&1\\1&0&1\\1&1&1\end{pmatrix},\qquad
A_r=\delta(I_r\otimes C),\qquad 0<\delta<10^{-2}.
\]
In every 3-coordinate block put the first coordinate in `S`, the second in `T`, and the third in `L`. Then
\[
B=A_{S,T}=\delta I_r,
\]
and on one block
\[
P_0=\delta\begin{pmatrix}0&1&1\\0&0&0\\0&1&1\end{pmatrix},
\qquad
(R-P)_0=\delta\begin{pmatrix}0&0&0\\1&0&1\\1&0&0\end{pmatrix}.
\]
Here `A[L,L]=P[L,L]=δI_r`, hence `F=E=D=0` and `R=A_r`. Since `det C=1`, block additivity gives
\[
\boxed{\operatorname{rank}P=r},\qquad
\boxed{\operatorname{rank}(R-P)=2r},\qquad
\boxed{\operatorname{rank}R=3r},\qquad
\boxed{\operatorname{rank}R[L,L]=r}.
\]
More precisely, the rows-`T` part of `R-P` has rank exactly `r`, and after removing those rows the remaining columns-`S` part also has rank exactly `r`. Thus the proof's support splitting itself is sharp. Moreover `R=A_r` is symmetric, so merely exploiting symmetry of the final corrected matrix cannot improve the global `3r` bound.

For `delta=10^{-3}`, every diagonal entry is `<eta=10^{-2}` and every principal two-coordinate determinant has modulus at most `10^{-6}<eta`, so the family lies in the manuscript's no-pivot regime. It is therefore a genuine obstruction to the tempting universal strengthenings `rank R<=2r`, `rank(R-P)<2r`, or either support leg `<r`.

Symmetrizing the interpolant also fails. On one block,
\[
\frac{P_0+P_0^T}{2}
=\delta\begin{pmatrix}0&1/2&1/2\\1/2&0&1/2\\1/2&1/2&1\end{pmatrix},
\]
whose `S` row is not the required row of `A`; exact row/column interpolation and therefore the support proof are destroyed. This directly validates the manuscript's insistence that `P` may be nonsymmetric.

**Status:** these are counterexamples to stronger interpolation/rank claims, not counterexamples to the density theorem.

## Threshold 16: exact terminal obstruction and a narrower next obligation

The existing proof cannot simply replace 17 by 16. In the order-five terminal case the only new equality chamber is `r=4`: global rank `rank R<=12` and `s_16(A-E)>=1-epsilon` force only four large diagonal entries of `D`, exactly matching the restricted `rank R[L,L]<=4`. The preceding sharpness family rules out obtaining the missing fifth entry by lowering either rank coefficient as a general algebraic statement.

There is, however, a useful quantitative refinement of this equality chamber. If `H subset L` consists of the four forced large diagonal entries, then only three off-diagonal terms occur in each row of `R[H,H]`. With the manuscript constants,
\[
|R_{ii}|\ge 371/400,
\qquad
|R_{ij}|<1/7+1/16=23/112,
\]
so
\[
|R_{ii}|-\sum_{j\in H\setminus\{i\}}|R_{ij}|
>\frac{371}{400}-3\frac{23}{112}
=\boxed{\frac{109}{350}}.
\]
Thus `R[H,H]` is not merely invertible; it is quantitatively well conditioned in the row-dominance sense. Since `rank R[L,L]<=4`, the survivor must actually have `rank R[L,L]=4`, and every `L×L` entry is algebraically generated through this four-coordinate core. Also symmetry of `A,D` gives the deterministic near-symmetry relation
\[
R-R^T=E^T-E,
\qquad \|R-R^T\|\le2\|E\|\le1/8.
\]

This sharply identifies the first unpaid implication for a true multiplicity-16 theorem:

> **Equality-chamber obligation.** Prove, or refute by an explicit no-pivot symmetric counterexample, that a decomposition `A=D+R+E` with `rank R<=12`, `rank R[L,L]=4`, a four-coordinate core with row-dominance margin `109/350`, `||E||<=1/16`, and `||R-R^T||<=1/8` cannot have `s_16(A)>=1` while the order-five disjoint-minor volume remains below `kappa^5`.

I do **not** have a complete proof of this implication. It is recorded as the next obligation, not as a threshold reduction. A trial exact block construction saturating the rank bounds leaves small seed-difference modes and therefore does not furnish an `s_16>=1` counterexample; conversely that failure alone is not a proof that the equality chamber is impossible.

Accordingly the rigorously certified threshold remains **17**.

## Package and reproducibility audit

| Package item | Status | This-run check |
|---|---|---|
| `README.md` | PASS | Correctly states the `s_17` candidate, support-file inventory, and non-claim for unrestricted three-eigenvalue QFORM. |
| `DELIVERY_STATUS.md` | PASS as delivery metadata | Correctly distinguishes source/PDF delivery, native assignment evidence, new finite checker, and proof validation. |
| `SOURCE_MANIFEST.json` | PASS | Pins baseline commit `7c0d...`, blob `183ccd...`, SHA-256 `9f3b...`, 47,883 bytes / 790 lines and explicitly marks support/check limitations. |
| `manuscript.tex` | PASS | Entire 790-line source read. Current master and pinned baseline expose the same git blob. |
| historical `AUDIT.md` | PASS as historical self-report; not proof | Its status and old finite-test counts are explicitly labeled historical and are not conflated with the new reproducibility suite. |
| `proof_map.csv` | PASS | Statement/proof line ranges agree with the source locations checked in this run. |
| `verify.py` | PASS for scoped checker logic | Source hash guard, exact interpolation/rank assertions, sampling inequality, diagonal-dominance arithmetic, Schur diagnostics and graph-weight identities match the manuscript claims they purport to test. |
| `checks.json` | PASS as an execution record, not a proof certificate | Reports PASS on the pinned source with 534 exact interpolation seeds, 18 volume cases, 9 strict sampling cases, 240 floating Schur threshold cases and 30 graph-weight cases. Independent recomputation of the deterministic loop/count logic and identities in this run reproduced those counts and assertions. |

The support files are therefore **present** and the earlier package reproducibility GAP is closed. The finite suite remains finite diagnostics only and does not change the mathematical PASS reasoning above.

## Exact arithmetic rechecks

- `371/400 - 23/28 = 297/2800 > 0` (the five-coordinate terminal dominance used by the paper).
- `371/400 - 3*(23/112) = 109/350 > 0` (the new four-coordinate equality-chamber margin above).
- `12 sqrt(80e) = 176.959336187... < 200`.
- `800e = 2174.625462767... < 2400`.
- scalar-pivot truncated-half-potential bound `10(20+12 log16)=532.710646669... <600`.
- indefinite-pair truncated-half-potential bound `10(32+4log16)+4/e=432.375066654... <600`.
- final scalar branch `6010<10000`.
- final indefinite-pair branch `10(10+5log16)+1/e=238.997315553... <251`.

## Final status

- Mathematical candidate at multiplicity 17: **PASS in this B08 audit**.
- Fatal manuscript gaps: **none found**.
- Package support-file gap from B08 r1: **resolved**.
- B08 interpolation/rank lens: **PASS**, with an explicit family saturating `rank P=r`, both rank-`r` support legs, `rank(R-P)=2r`, global `rank R=3r`, and restricted `rank R[L,L]=r` simultaneously.
- Certified lower threshold: **none**; 17 remains the baseline.
- First next obligation: settle the quantitatively constrained `m=16,r=4` equality chamber above with a complete proof or a genuine counterexample, while preserving all theorem quantifiers.
- Unrestricted three-large-eigenvalue QFORM: **not claimed solved**.
