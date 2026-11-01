# fleet02/B19 independent end-to-end audit — fixed multiplicity

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T134752Z-fleet02-B19-fixedmult-audit`  
Lens: independent full proof reconstruction, counterexample stress, guarded integration only after baseline reconstruction.

## Source pins

Fresh `math-open-problems/master` observed before delivery: `6f66b0489379ff8a5f183465eaf465571c427a66`. The mathematical baseline itself is unchanged and is pinned byte-for-byte by the package as:

- initial source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`;
- manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`;
- SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`;
- 47,883 bytes, 790 lines.

I read the package `README.md`, `SOURCE_MANIFEST.json`, all 790 source lines of `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json` before consulting threshold-improvement verdicts. The package members that were missing in an earlier B19 run are now present. `checks.json` records PASS for the new finite suite (534 exact interpolation seeds, 18 exact volume comparisons, 240 floating Schur cases, 30 graph-weight cases); I read the checker and its stored output but did not independently execute that finite suite in this run, so **B19 re-execution of the checker is UNCHECKED**. This does not affect the symbolic proof audit.

## Baseline theorem verdict

**PASS after one local wording repair; no fatal mathematical gap found.** The audited theorem is

\[
s_{17}(A)\ge s>0
\Longrightarrow
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary independent real coordinate laws with densities at most `K`, arbitrary real symmetric `A`, arbitrary signs and remaining spectrum, and arbitrary affine terms. The argument establishes essential boundedness globally; it does not claim global continuity.

### Audit ledger

| Source lines / label | Status | Independent check, impact, next obligation |
| --- | --- | --- |
| 47–74, `thm:main`, architecture | **PASS** | Quantifiers, singular-value convention, affine terms, normalization target, and the distinct roles of order 3 and order 5 are consistent. No moment/support/log-concavity/rotated-independence premise is inserted. |
| 91–160, `lem:fourier`, `lem:envelope`, `lem:riesz` | **PASS** | Fourier normalization is consistent with `2π`; Gaussian regularization proves Plancherel/inversion at the constants used. Tonelli plus the Gaussian half-potential representation gives the factor `1/sqrt(2π)`. The `3/4` envelope is used only with the `|t|^{-1/2}` Riesz weight. |
| 169–217, `lem:rank`, `lem:schur`, `lem:dd` | **PASS** | Nonsymmetric singular-value perturbation is correctly used. For invertible `A`, the complementary block of `A^{-1}` is `S^{-1}`; positive/negative compression gives `N_S(t)>=N_A(t)-k`. The singular `A+εI` limit with threshold `t-|ε|` preserves eigenvalues exactly at `t`. Strict row diagonal dominance is standard and valid without symmetry. |
| 221–255, `thm:bl` | **PASS** | Heat-flow derivative has the correct nonnegative sign from the frame contraction; Gaussian tails justify integration by parts; the large-time Gaussian limit uses `sum c_i=d`; Fatou and monotone truncation handle rough nonnegative integrable inputs. |
| 258–282, `lem:projection` | **GAP (wording only), theorem PASS after repair** | After dropping rows with `b_i=0`, the text writes the entropy sum as if `sum_{b_i>0}(1-b_i)=d`. In general only `sum_{b_i>0}(1-b_i)<=sum_i(1-b_i)=d`. Replacing equality by this inequality proves the same `exp(d/2)` bound with no downstream constant change. No rotated-coordinate independence is asserted. |
| 284–400, scalar Fourier powers, decoupling, determinant, volume envelopes | **PASS** | `m=floor(p/2)>=p/4`, the difference density remains cap one, and inversion at zero is applied to an integrable Fourier transform. Two-copy decoupling keeps product provenance. The graph frame, `α=(2πe)^2`, scalar powers, entropy factor, and fourth-root step give determinant exponent `-1/8`. Cauchy–Binet yields `Z_k`; `k=5` is integrable and `k=3` supplies the weighted half-potential, not a density bound. |
| 404–525, scalar/definite/hyperbolic/quarter-power pivots | **PASS** | Square inverse branches and definite-pair Jacobian are correct. The hyperbolic change of variables has Jacobian `1/(2sqrt D)`; its tail estimates spend only original coordinate caps and total mass. The quarter-power sign cut gives a physical cross block of norm at least `||S||/4`; determinant smoothing yields the claimed `ρ^{1/4}` anti-concentration and finite logarithmic potential. Exceptional levels are handled as measure domination, not pointwise conditional-density assertions. |
| 528–580, `def:pivot-volume`, `lem:sampling`, `lem:completion` | **PASS** | Ordered disjoint minors and bordered determinants are correct. Singular seeds can have nonsingular extensions, so the sampling comparison is correctly an inequality. The nonsymmetric interpolant `P=A[:,T]B^{-1}A[S,:]` has rank `<=r`, matches rows `S` and columns `T`; in `A=D+R+E`, `D` vanishes on the seed, `E` has zero diagonal, `rank R<=3r`, while `R[L,L]=P[L,L]` has rank `<=r`. |
| 582–645, `prop:volume`, `lem:cut`, `cor:no-pivot` | **PASS** | If a ratio first falls below `κ`, rank subtraction from `s_{4k-3}` forces at least `r+1` large diagonal entries outside the seed. On that set, row diagonal dominance has exact slack `371/400-23/28=297/2800>0`, contradicting restricted rank `r`. The `r=0` case is separately controlled by `||diag A||+||off A||_F<1`. A fair physical cut retains each ordered disjoint minor with probability `4^{-k}`. Constants are `12sqrt(80e)<200` and `800e<2400`. |
| 654–724, kernels, pivot half-potential, nine-direction half-potential | **PASS** | The two singular kernels are integrable with the stated coarse constants. A scalar pivot plus one surviving Schur direction controls the logarithmic singularity; definite and indefinite pair branches are uniform in induced affine terms. Under `s_9>=1`, pivot and no-pivot alternatives yield truncated half-potential `<=600` and full half-potential `<=601`. |
| 726–790, main proof, scaling, limitations | **PASS** | Under `s_17>=1`: no-pivot `<2400`; scalar pivot leaves at least 16 Schur directions and uses the nine-direction half-potential to give `6010`; definite pair `<40`; indefinite pair leaves at least one direction and gives `<251`. For `Y=KX`, coordinate caps become one and `Q=(s/K^2)Qtilde`, giving `10^4K^2/s`. The manuscript correctly does not claim the unrestricted three-eigenvalue theorem. |

No source line outside these ranges carries a specialized mathematical assertion needing a different verdict; preamble/bibliography/presentation metadata are **PASS/NOT MATHEMATICAL**.

## Counterexample stress: why the baseline rank bookkeeping cannot simply be tightened

The `r=1` completion can saturate all three global rank directions. For

\[
A=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix},\qquad S=\{1\},\ T=\{2\},
\]

the manuscript construction has `E=0`, and the resulting correction `R` has determinant one, hence `rank R=3=3r`. Scaling preserves the rank statement. Thus a formal replacement `rank R<=2r` is false for this interpolation. This is a counterexample to a proof shortcut, not to the density theorem.

A second endpoint obstruction matters below multiplicity nine: a single rank-two indefinite quadratic does not itself have bounded density. If `U,V` are independent uniform variables, the density of `U^2-V^2` has a logarithmic singularity at zero because the convolution integrand contains `∫_0^1 ds/(4s)=∞`. Therefore an eight-direction proof cannot close merely by extracting one order-two crossing-volume packet.

## Baseline impact

- Fatal defect: **none found**.
- Local repair: projection lemma wording `=` -> `<=` after zero-`b_i` rows are omitted; no theorem or constant changes.
- Package reproducibility: supplementary files are present in the observed master snapshot; stored checker result is PASS, but B19 did not rerun it.
- Baseline 17 theorem: **PASS in this independent B19 reconstruction**.
- Unrestricted three-eigenvalue QFORM: **OPEN and not claimed here**.

The guarded threshold-nine integration and the first eight-direction obstruction are recorded separately under this run's improvement artifact.
