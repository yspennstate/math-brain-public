# account02/B11 fixed-multiplicity end-to-end audit r16

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T125059Z-account02-B11-FIXEDMULT-r16`  
Role lens: Schur-complement spectral counts, singular/near-singular cases, counterexamples to overcount.  
Canonical manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Canonical manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Owner-stated source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Audit snapshot first pinned at master `0af0baa36daa54149d3f40fda559f185ede8affa`; control refresh later found master `94a3001b0042aff40d4ffcfe704607b9d19fa510`, with the manuscript blob still exactly `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Verdict

**Mathematical baseline manuscript: PASS in this independent worker review.** I read the complete 790-line `manuscript.tex` and rederived every specialized step below. I found no fatal mathematical gap in the stated 17-eigenvalue theorem. This is one worker review, not a self-awarded release certificate and not a proof of the unrestricted three-eigenvalue conjecture.

**Package/reproducibility: GAP.** At both the pinned audit snapshot and the refreshed master directory, `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are absent, although README/AUDIT describe them as canonical package contents. Direct fetches return 404. Thus the manuscript proof can be audited because it is self-contained, but the claimed finite-check bundle and its exact recorded results are **UNCHECKED in this run** and the package inventory claim is **FALSE as delivered at these snapshots**. This does not invalidate a line of the mathematical proof; it does prevent independent reproduction of the advertised checker from the current package.

## Full-source line coverage

Every source line is covered by the contiguous passes below. Line ranges are source ranges in the 790-line canonical blob.

| Source range / statement | Status | Audit reasoning, impact, next obligation |
|---|---|---|
| 1-91: metadata, abstract, definitions, main theorem/corollary, normalization and architecture | PASS | Quantifiers match the owner objective: independent coordinate densities `<=K`, arbitrary symmetric `A`, arbitrary affine `b,c`, `s_17(A)>=s>0`, essential density bound `10000 K^2/s`. No support/moment/sign assumptions are inserted. The 33-eigenvalue statement is only a corollary. Scaling is checked again at the final proof. |
| 92-181: Fourier conventions, Gaussian inversion, power envelope, Riesz half-potential, singular-value perturbation | PASS | Fourier constants and Gaussian factors are consistent with `hat f(t)=int e^{itx}f(x)dx`. The Riesz representation plus Gaussian inversion gives the stated `1/sqrt(2pi)` coefficient; the `3/4` envelope integrates to `12 sqrt(u)`. Eckart-Young gives both perturbation inequalities for nonsymmetric matrices. |
| 183-222: `lem:schur`, including singular ambient matrices | PASS | Full independent derivation below. The invertibility of the pivot `B` is essential and is respected at every invocation. Singular ambient `A` is handled by `A+epsilon I`; the threshold is reduced to `t-|epsilon|` before taking the limit, so equality-at-threshold eigenvalues are not lost. |
| 223-244: strict diagonal dominance | PASS | Standard maximum-coordinate argument applies to nonsymmetric matrices exactly as used later. |
| 245-303: geometric rank-one BL heat-flow proof | PASS | Direct differentiation gives `d_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0` because the frame matrix has operator norm one. Large-time Gaussian limit, small-time Lebesgue-point/Fatou step, truncation and monotone convergence cover rough nonnegative integrable inputs. |
| 304-354: product projection and scalar Fourier powers | PASS | The orthogonal complement rows furnish the exact frame. `f_i<=1` gives `f_i^{1/b_i}<=f_i`; zero `b_i` factors may be dropped. The scalar Fourier-power proof uses a genuine sum of independent differences and evaluates the continuous inversion density at zero. No rotated independence is asserted. |
| 355-432: decoupling and regularized crossing determinant | PASS | Cauchy-Schwarz is taken in the original product law, expansion uses independent copies, and Jensen gives the fourth-power version. In the determinant proof, the graph frame weights satisfy `theta=sum d_i=sum(1-c_j)`. The `d_i` powers cancel against the scalar Fourier bound and `alpha=(2pi e)^2` cancels the remaining graph entropy factor. Fourth root gives determinant exponent `-1/8` and scale `t^2/(pi^2 e^2)`. |
| 433-464: crossing volumes and order-3/order-5 envelopes | PASS | Cauchy-Binet coefficient identity is correct. Retaining the order-`k` term gives exponent `k/4`; `k=5` is integrable and yields `5e Z_5^{-1/10}`, while `k=3` is used only with the half-Riesz weight, yielding `12 sqrt((e/2) Z_3^{-1/6})`. No direct bounded-density claim is made from `k=3`. |
| 465-532: scalar square, definite pair, indefinite hyperbolic pair | PASS | Square inverse branches and interval lengths are correct. The definite-pair Jacobian is `1/(2 sqrt(det B))`, hence `pi M/sqrt(det B)`. For the hyperbolic pair, the two-branch coarea Jacobian is `1/(2 sqrt D)`; the original-coordinate tail monotonicity is valid after the stated cutoff, and the mass-one/density-one tail bound gives the logarithmic envelope. No post-rotation independence is used. |
| 533-579: quarter-power concentration and logarithmic potential | PASS | If no large diagonal exists, the randomized sign cut produces a true original-coordinate cross block with norm at least `L/4`. The determinant bound then gives the `|t|^{-1/4}` envelope. Gaussian smoothing produces the stated `rho^{1/4}` concentration; layer cake gives `4+4 log 16`. This excludes atoms before the later kernel invocation. |
| 580-638: pivot-volume definition, no-pivot entry bounds, sampled interpolation, completion | PASS | Ordered disjoint minors are used consistently. The bordered determinant sampling is an inequality because singular seeds may have nonsingular extensions. `P` may be nonsymmetric. `R-P` is supported only in rows `T` or columns `S`, giving global `rank R<=3r`, while exactly `R[L,L]=P[L,L]` gives the crucial restricted `rank<=r`; `D=0` on the seed and `E` has zero diagonal. |
| 639-688: spectral-to-volume proposition, random cut, no-pivot analytic consequences | PASS | From `V_k<kappa^k`, a ratio `<kappa` exists even if a first volume vanishes. For `r>=1`, `epsilon<=(r+1)/80<=1/16`; rank perturbation yields at least `r+1` large diagonal entries because `m=4k-3>=4r+1`. They lie in `L`. The exact diagonal-dominance comparison `23/28 < 371/400` contradicts restricted rank `<=r`. This use of singular values remains valid for nonsymmetric `A-E`. The random-cut factor `4^{-k}` is exact. Constants `160`, `<200`, and `800e<2400` follow. |
| 689-726: singular kernels and pivot truncated half-potential | PASS | The near-singularity kernel is uniformly bounded on the rescaled near region; on the far region `|x-d|>=|x|/2`. The logarithmic kernel is maximized by centered interval overlaps. Scalar-pivot, definite-pair and indefinite-pair alternatives exhaust the pivot definition and all are applied through measure domination/Tonelli, so rough exceptional slices do not create a hidden conditional-density assumption. |
| 727-756: nine-eigenvalue half-potential and main normalized proof | PASS | Pivot branch uses only `s_2>=1` for the truncated bound; no-pivot branch uses `s_9>=1`. Full half potential is at most truncated `H+1`. In the main theorem a scalar pivot loses at most one large spectral direction, leaving 16 and hence the needed 9; a pair loses at most two, leaving 15. Definite pair is direct; indefinite pair needs only one surviving Schur direction for the logarithmic-potential lemma. |
| 757-774: general `K,s` scaling and interval/density equivalence | PASS | With `Y=KX`, coordinate density caps become one and `tilde Q=(K^2/s)Q`; density rescaling gives `10000 K^2/s`. Affine coefficients are transformed correctly. Interval domination and essential-density equivalence are standard. |
| 775-790: threshold accounting, limitations, bibliography | PASS | The text correctly identifies 17 as coming from the no-pivot order-five volume mechanism, not Schur loss. It explicitly does not claim a three-eigenvalue theorem or continuity in all branches. Classical citations are attribution only because specialized claims are reproved. |

## B11 Schur-complement audit

For

\[
A=\begin{pmatrix}B&C\\C^T&D\end{pmatrix}=A^T,\qquad \det B\ne0,\qquad S=D-C^TB^{-1}C,
\]

with `B` of order `k`, the manuscript claims

\[
N_S(t)\ge N_A(t)-k,\qquad t>0.
\]

### Invertible ambient matrix: PASS

Block Gaussian elimination is a congruence to `B\oplus S`, and the complementary principal block of `A^{-1}` is `S^{-1}`. Principal-compression interlacing applied separately to `A^{-1}` and `-A^{-1}` gives

\[
\#\{ |\lambda(S^{-1})|>t^{-1}\}
\le \#\{|\lambda(A^{-1})|>t^{-1}\}.
\]

For invertible matrices these counts are `(n-k)-N_S(t)` and `n-N_A(t)` because `|1/lambda|>1/t` iff `0<|lambda|<t`. Rearrangement gives the claim. The strict `>` in the inverse count is exactly compatible with the original `>=t` count.

### Singular ambient matrix: PASS

Choose `epsilon_m ->0` avoiding the finite bad values for both `A+epsilon I` and `B+epsilon I`. Since the original `B` is invertible, `B+epsilon I` is invertible for all sufficiently small `epsilon`, and

\[
S_\epsilon=D+\epsilon I-C^T(B+\epsilon I)^{-1}C\to S.
\]

Every eigenvalue of `A` with modulus at least `t` produces an eigenvalue of `A+epsilon I` with modulus at least `t-|epsilon|`; hence
`N_{A+epsilon I}(t-|epsilon|)>=N_A(t)`. Applying the invertible case at that lowered threshold and taking ordered-eigenvalue limits proves the result. No rank is silently lost at zero and no continuity claim for the count at a fixed discontinuity is needed.

### Exact counterexample 1: singular pivot extension is FALSE

The invertibility hypothesis on `B` cannot be removed by replacing `B^{-1}` with a Moore-Penrose pseudoinverse. Take

\[
A=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad B=(0),\qquad D=(0).
\]

The pseudoinverse Schur expression is `S=0`, while at `t=1`, `N_A(1)=2` and `N_S(1)=0`. Even the naive order-one loss would demand `0>=1`, false. **Impact:** any singular-pivot generalization is invalid. **Repair:** retain exactly the manuscript hypothesis `det B !=0`; all actual pivot branches satisfy it because `|a_ii|>=eta` or `|det B|>=eta`.

### Exact counterexample 2: a tiny nonzero scalar pivot can consume one full large direction

For `0<epsilon<1`, let

\[
A_\epsilon=\begin{pmatrix}\epsilon&\sqrt\epsilon\\\sqrt\epsilon&1\end{pmatrix},\qquad B=(\epsilon).
\]

Then `S=1-epsilon/epsilon=0`, while

\[
\operatorname{spec}(A_\epsilon)=\{1+\epsilon,0\}.
\]

At `t=1`, `N_A=1`, `N_S=0`, but the pivot itself has no eigenvalue of magnitude one (`N_B(1)=0`). Thus one cannot improve the Schur loss to “lose only the large eigenvalues already visible in the pivot”. The order-`k` loss is geometric, not threshold-local in `B`.

### Exact counterexample 3: near-singular indefinite pair can consume two full large directions

For `0<epsilon<1`, set

\[
B_\epsilon=\operatorname{diag}(\epsilon,-\epsilon),\quad
C=\sqrt\epsilon I_2,\quad
D=\operatorname{diag}(1,-1).
\]

Then

\[
S=D-C^TB_\epsilon^{-1}C=0,
\]

and, after a permutation, `A_epsilon` is the direct sum of
`[[epsilon,sqrt(epsilon)],[sqrt(epsilon),1]]` and
`[[-epsilon,sqrt(epsilon)],[sqrt(epsilon),-1]]`. Hence

\[
\operatorname{spec}(A_\epsilon)=\{1+\epsilon,-(1+\epsilon),0,0\}.
\]

At `t=1`, `N_A=2`, `N_S=0`, while `N_{B_epsilon}(1)=0`. The full order-two Schur loss is therefore sharp even for an arbitrarily near-singular **indefinite** pivot and a singular ambient matrix. Sign-resolved, one positive and one negative large direction are each consumed. **Impact:** no threshold reduction is available by arguing that a small or indefinite pivot should cost fewer spectral directions.

## Invocation audit of Schur hypotheses

- `prop:pivot-H`, scalar pivot: `|a_ii|>=eta` makes the 1x1 pivot invertible. Ambient hypothesis `s_2>=1`; Schur lemma leaves at least one direction. **PASS.**
- Main proof, scalar pivot: `s_17>=1`; order-one loss leaves at least 16, so the nine-direction half-potential lemma is applicable. **PASS, with slack.** A scalar-pivot-only branch would need only 10 ambient large directions.
- Main proof, definite pair: determinant magnitude `>=eta` makes the pair invertible. The density estimate is direct; no surviving Schur spectrum is needed. **PASS.**
- Main proof, indefinite pair: determinant magnitude `>=eta` makes the pair invertible. Order-two loss leaves at least 15, more than enough for the one-direction logarithmic-potential lemma. **PASS, with large slack.** This branch alone would need only 3 ambient large directions.
- No other invocation forms a Schur complement with a singular principal block. **PASS.**

## Package-file audit

| File | Status at pinned/refreshed master | Impact / next obligation |
|---|---|---|
| `README.md` | PASS content, but package inventory claim partly FALSE | Correct theorem/status text. It says four supplementary files are canonical, but they are absent from the directory. |
| `manuscript.tex` | PASS | Blob matches canonical `183ccd...`; complete mathematical proof is present. |
| `AUDIT.md` | PASS as self-audit description; finite-check claims UNCHECKED here | It explicitly labels itself a self-audit and does not claim independent validation. |
| `SOURCE_MANIFEST.json` | GAP / missing (404) | Restore if reproducibility metadata is intended to be part of the package. |
| `proof_map.csv` | GAP / missing (404) | Restore if line-map reproducibility is intended. This review reconstructed its own full-line coverage. |
| `verify.py` | GAP / missing (404) | The advertised finite diagnostics cannot be rerun from current master. |
| `checks.json` | GAP / missing (404) | Recorded numerical checker results cannot be independently inspected from current master. |

## Threshold conclusion

I do **not** lower 17 in this run. The Schur branch is already much cheaper than 17, and the counterexamples above show that its order-`k` spectral loss cannot be improved merely from pivot smallness, near-singularity, or the pivot's own threshold count. The current threshold is forced by the no-pivot order-five crossing-volume argument (`4k-3` with `k=5`). Lowering 17 requires a complete replacement of that no-pivot mechanism (or a stronger analytic consequence of a lower-order crossing volume) with explicit constants and a closed dependency map. No such complete replacement proof is supplied here.

## Final status

- `PASS`: canonical 17-eigenvalue manuscript, all 790 source lines, all theorem/lemma hypotheses and invocations checked in this run.
- `GAP`: four README-advertised supplementary package files are absent from current master; finite-check reproducibility is therefore incomplete.
- `FALSE`: any extension of `lem:schur` to a singular pivot by Moore-Penrose substitution; any attempt to charge only threshold-large eigenvalues of a near-singular pivot for the Schur spectral loss.
- `UNCHECKED`: the advertised `verify.py` / `checks.json` finite tests, because those files are not present.
- Unrestricted three-eigenvalue QFORM: **not claimed solved**.
