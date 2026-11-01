# fleet02/B08 independent fixed-multiplicity audit

Run: `20260924T123814Z-fleet02-B08-fixedmult-audit-r1`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript source SHA-256 (package/owner pin): `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Pinned manuscript git blob independently observed on fresh `master`: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Fresh package-head used for the full source read: `e3baf218091e01cc7d41542f934ce269951b47e7`; a later refresh at `b5e04c2f5c0c856ed72190e7554a93650a1a22f3` still had the same manuscript blob.

## Verdict

**PASS for the complete mathematical 17-eigenvalue candidate, with one nonfatal wording clarification and one repository-package GAP.** I read the full 790-line `manuscript.tex` independently and checked every displayed equation, definition, lemma/proposition/theorem invocation and proof chain. I found no fatal mathematical defect in

\[
 s_{17}(A)\ge s>0\quad\Longrightarrow\quad
 \|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary real symmetric `A`, arbitrary affine `b,c`, and independent real coordinate densities bounded by `K`.

This is one independent review, not a self-awarded validation certificate. The unrestricted three-large-eigenvalue QFORM conjecture remains open. No multiplicity reduction below 17 is certified here.

## End-to-end source ledger

Every manuscript line is covered by one row below; the ranges are source-line ranges in the pinned 790-line manuscript.

| Source lines / statement | Status | Independent reasoning | Impact / next obligation |
|---|---|---|---|
| 1–83: conventions, main theorem, 33-corollary, parameters, architecture | PASS | Singular values/eigenvalue moduli are consistently defined; the theorem keeps arbitrary dimension/signature/remaining spectrum, affine terms and rough product laws. `Y=KX` later has cap-one densities and gives exactly the advertised `K^2/s` rescaling. | Main quantifiers and target are coherent. |
| 84–151: Fourier convention, Gaussian inversion, power envelope, Riesz half potential | PASS | Plancherel and inversion use the correct `2π` normalization. The gamma identity gives `|z|^{-1/2}=Γ(1/4)^{-1}∫v^{-3/4}e^{-vz^2}dv`; after Gaussian inversion the inner `v` integral is `√2 Γ(1/4)|t|^{-1/2}`, yielding `(2π)^{-1/2}`. The weighted `3/4` envelope integral is exactly `12√u`. | All later Fourier and half-potential constants are normalized correctly. |
| 152–220: nonsymmetric singular-value perturbation, Schur count, diagonal dominance | PASS | Approximation numbers give both perturbation inequalities for arbitrary real matrices. For invertible `A`, `S^{-1}` is the complementary principal compression of `A^{-1}`; positive and negative interlacing separately imply `N_S(t)≥N_A(t)-k`. The `A+εI` argument covers singular `A`. Strict row diagonal dominance needs no symmetry. | Exact hypotheses needed later are satisfied even for nonsymmetric auxiliaries. |
| 221–255: geometric rank-one Brascamp–Lieb heat flow | PASS | The frame makes the column operator with columns `√c_i u_i` a contraction, so `Σc_i v_i^2-|Σc_i u_iv_i|^2≥0`. Compact-support heat convolutions justify differentiation/integration by parts; the large-time Gaussian limit uses `Σc_i=d` and the frame identity, and monotone approximation handles general nonnegative integrable inputs. | Self-contained analytic input is sound. |
| 256–287: product projections | **PASS with wording clarification** | After dropping factors with `b_i=0`, the proof obtains `log p≤(1/2)Σ_{b_i>0}[-b_i log b_i]`. Extending `-b log b` by `0` at `b=0`, one may sum over all `i` and use `-b log b≤1-b`; equivalently insert an explicit `≤` before `Σ_i(1-b_i)=d`. Thus the stated `e^{d/2}` bound is correct. | No theorem change. Editorial repair: write the positive-`b_i` sum explicitly, then `≤Σ_i(1-b_i)=d`. |
| 288–300: integrated scalar Fourier powers | PASS | With `m=floor(p/2)`, `|fhat|≤1` gives `∫|fhat|^p≤∫|fhat|^{2m}`. The latter is the characteristic function of a sum of `m` independent differences; it is integrable because it is bounded by the `L^2` power. Projection density of the `2m` signed original variables gives the zero-density bound and hence `2π√(2e)/√p`. | Correct scalar input for graph BL. |
| 301–328: two-copy and fourth-power decoupling | PASS | Cauchy–Schwarz is taken in the original `X_I` law, an independent `X'_J` is introduced, and integration over original independent `X_i` produces the product of scalar Fourier transforms. Jensen gives the fourth-power form. Difference coordinates remain independent and cap one. | No post-rotation independence or hidden moments. |
| 329–400: regularized crossing determinant and crossing volumes | PASS | For `H=αI+a^2M^TM`, the vectors `√αH^{-1/2}e_j` and `aH^{-1/2}m_i` form the exact geometric frame. The `c_j,d_i` scale factors and `L^{1/c_j}`, `L^{1/d_i}` norms are correct. `α=(2πe)^2` cancels the entropy multiplier. Fourth roots give determinant exponent `-1/8`. Cauchy–Binet gives the `Z_k` polynomial; retaining one positive coefficient gives exponent `k/4`. `k=5` is integrable; `k=3` is used only with the Riesz weight. | Determinant/volume receiver is sound at the stated exponents. |
| 401–500: scalar square, definite pair, hyperbolic pair | PASS | Scalar inverse branches give the exact square-root profile and interval preimage length. Definite quadratic polar coordinates have Jacobian `1/(2√|det B|)`. In the indefinite case, the hyperbolic parameterization has the same absolute Jacobian; each tail is controlled by one original coordinate density using monotonicity and mass one, and the middle interval length gives the logarithm. | Pair/scalar pivots retain original-coordinate product provenance. |
| 501–535: quarter-power concentration and log potential | PASS | If no diagonal has size `L/2`, a random sign cut of `offdiag(S)` has cross-block norm at least `L/4`. One determinant singular factor gives `|t|^{-1/4}`; Gaussian smoothing yields the stated `ρ^{1/4}` small-ball bound with a coefficient safely below 16. Layer cake gives `4+4 log16`. | One surviving spectral direction controls logarithmic singularities. |
| 536–600: `V_r`, no-pivot entry bound, sampled interpolation, completion | PASS; B08 primary lens | The bordered determinant identity is exact; sorting signs disappear after squaring. Singular seeds only reduce the extension count, so `(r+1)^2 V_{r+1}/V_r` is an upper bound as claimed. For `P=A[:,T]B^{-1}A[S,:]`, `P[S,:]=A[S,:]` and `P[:,T]=A[:,T]` exactly. With the manuscript's `D,E,R`, `R[L,L]=P[L,L]`; `R-P` vanishes on rows `S`, columns `T`, and all of `L×L`, hence is supported in rows `T` or columns `S`. Splitting those two supports gives `rank(R-P)≤2r`; with `rank P≤r`, `rank R≤3r`, while `rank R[L,L]≤r`. `D` vanishes on the seed and `diag E=0`. | Sensitive nonsymmetric support propagation and both rank bounds are correct. See sharpness counterexample below. |
| 601–630: no-pivot spectral-to-volume proposition | PASS | A bad telescoping ratio gives `||E||≤(r+1)/80≤1/16`. With `m=4k-3` and `r≤k-1`, `m≥4r+1`; after the global rank-`3r` loss, at least `r+1` diagonal entries of `D` are `≥1-ε` in modulus, all in `L`. On their set `H`, `|R_ii|≥371/400`; every off-diagonal is `<1/7+1/16`, so for `r≤4` the row sum is `<23/28`. The exact strict-dominance slack is `297/2800>0`, contradicting `rank R[L,L]≤r`. The `r=0` Frobenius branch is also valid. | This is the exact algebraic source of the `4k-3` count. |
| 631–660: random cut, order-3 and order-5 consequences | PASS | Each ordered disjoint `k`-minor survives a fair cut with probability `4^{-k}`. With `κ=1/80^2`, `Z_k^{-1/(2k)}≤160`. Hence `12√(80e)=176.959336...<200` and `800e=2174.625463...<2400`. | Gives the nine-direction full half potential and seventeen-direction no-pivot density. |
| 661–730: truncated half potential, kernel estimates, pivot-H | PASS | The `J(d)` split gives the stated near-region constant and logarithmic far tail; the translated log kernel is maximized at zero by interval-overlap rearrangement. Scalar pivot averages the exact square profile against a one-direction logarithmic potential; definite and indefinite pair bounds are uniform after conditioning on original coordinates. The manuscript keeps truncated and full half potentials separate; adding at most one outside distance one gives 601. | Pivot branch closes without exceptional-slice or conditional-cap assumptions. |
| 731–790: nine-direction proposition, main theorem, scaling, limitations/bibliography | PASS for proof; attribution-only bibliography not used as a black box | No pivot gives `<2400`. A scalar pivot under `s_17≥1` leaves at least 16 Schur directions, so the proved nine-direction full half potential applies and gives `6010`. A definite pair gives `<40`; an indefinite pair leaves at least 15 directions and only one is needed for the log potential, giving `<251`. Scaling `Y=KX` gives `Q=(s/K^2)\widetilde Q` and therefore `10^4K^2/s`. The final remarks accurately avoid a continuity claim in pivot branches and avoid claiming the three-eigenvalue theorem. | Complete candidate closes as stated. |

No manuscript source line is left mathematically UNCHECKED in this review.

## B08 counterexample audit: nonsymmetry and both rank bounds are genuinely necessary

The following exact family is a counterexample to two tempting *strengthenings* of the interpolation lemma, not to the theorem.

Let
\[
 C=\begin{pmatrix}0&1&1\\1&0&1\\1&1&1\end{pmatrix},\qquad
 A_r=\delta\,(I_r\otimes C),\qquad 0<\delta<10^{-2},
\]
and in each 3-coordinate block choose the first coordinate for `S`, the second for `T`, and the third for `L`. Then
\[
 B=A_{S,T}=\delta I_r,
\]
and the manuscript interpolation is block diagonal with one-block piece
\[
 P_0=\delta\begin{pmatrix}0&1&1\\0&0&0\\0&1&1\end{pmatrix}.
\]
Therefore `rank P=r`, `A[L,L]=P[L,L]=δI_r`, so `F=0`, `E=0`, `D=0`, and the manuscript completion has `R=A_r`. Since `det C=1`,
\[
 \boxed{\operatorname{rank}R=3r},\qquad
 \boxed{\operatorname{rank}R[L,L]=r}.
\]
Thus **both rank bounds are sharp simultaneously**. In particular a universal replacement `rank R≤2r` is false even for symmetric `A` and even in the no-pivot regime: for `δ=10^{-3}`, every diagonal entry is `<η=10^{-2}` and every principal two-coordinate determinant has modulus at most `δ^2=10^{-6}<η`.

The same family shows why symmetrizing the interpolant is invalid. For one block,
\[
 \frac{P_0+P_0^T}{2}
 =\delta\begin{pmatrix}0&1/2&1/2\\1/2&0&1/2\\1/2&1/2&1\end{pmatrix},
\]
whose `S` row is `(0,δ/2,δ/2)`, not the required `(0,δ,δ)` row of `A`. Hence symmetrization destroys exact row/column interpolation and the support statement for `R-P`.

This counterexample was checked exactly for `r=1,2,3,4`: `rank R=3r`, `rank R[L,L]=r`, `F=0`, `D=0`, exact row-`S`/column-`T` interpolation holds for the nonsymmetric `P`, and fails after symmetrization.

### Consequence for threshold reduction

At the terminal `k=5`, `r=4` chamber, the existing proof needs `m-3r≥r+1`, i.e.
\[
 m\ge 3r+(r+1)=4r+1=17.
\]
At `m=16`, the global rank loss can guarantee only four large diagonal entries, which is compatible with the restricted rank bound four. The exact family above rules out lowering the global `3r` coefficient by a purely algebraic improvement of this completion, and it also shows the restricted `r` bound itself is sharp. Therefore **17 cannot be reduced by merely tightening either rank estimate in Lemma `completion`**. A lower theorem requires a genuinely new terminal mechanism (for example an endpoint analytic receiver or additional quantitative structure), not a numerical retuning of `η,κ` or a symmetrization of `P`.

I do not claim this proves 17 optimal; it only blocks the natural B08 rank-improvement route. No complete replacement proof below 17 was obtained in this run, so no lower threshold is claimed.

## Package audit

| Package item | Status | Evidence / impact |
|---|---|---|
| `README.md` | PASS for theorem/source description; **FALSE** for its claim that all listed supplementary files are present | Fresh source reads agree with the theorem/blob pins, but direct fetches of the advertised supplementary files below returned `404`. |
| `AUDIT.md` | PASS as a self-audit description; finite-test claims **UNCHECKED** | Its mathematical summary is consistent with the manuscript. The numerical-check claims cannot be reproduced from this root because the scripts/results are absent. |
| `SOURCE_MANIFEST.json` | **UNCHECKED / absent** | Direct fetch returned `404`; source SHA-256 is therefore a package/owner pin, while byte identity was independently checked through the git blob. |
| `proof_map.csv` | **UNCHECKED / absent** | Direct fetch returned `404`. This review supplies its own complete line-range ledger above. |
| `verify.py` | **UNCHECKED / absent** | Direct fetch returned `404`; no checker was fabricated. |
| `checks.json` | **UNCHECKED / absent** | Direct fetch returned `404`; recorded finite-test claims remain unrerun here. |

The missing supplementary files are a reproducibility/release-package GAP, not a mathematical dependency gap: every specialized mathematical input actually used by the theorem is proved in `manuscript.tex` and was checked independently above.

## Exact arithmetic rechecks

- `371/400-23/28 = 297/2800 > 0`.
- `12√(80e) = 176.959336187... < 200`.
- `800e = 2174.625462767... < 2400`.
- scalar-pivot truncated-half-potential bound `10(20+12 log16)=532.710646669...<600`.
- indefinite-pair truncated-half-potential bound `10(32+4 log16)+4/e=432.375066654...<600`.
- final scalar branch `6010<10000`; final indefinite-pair branch `10(10+5 log16)+1/e=238.997315553...<251`.

These arithmetic diagnostics support but do not replace the symbolic proof.

## Final status

- Mathematical 17-eigenvalue candidate: **PASS in this independent B08 review**.
- Fatal mathematical gap found: **none**.
- Local manuscript repair suggested: clarify the zero-`b_i` summation in the projection lemma; no constant or conclusion changes.
- Repository package: **GAP** because four advertised supplementary files are absent.
- Multiplicity below 17: **not proved**.
- B08 rank-improvement attempt: **FALSE as a route**; the `3r` global and `r` restricted bounds are simultaneously sharp by the explicit no-pivot block family above.
- Unrestricted three-eigenvalue QFORM: **OPEN; not claimed solved**.
- Native learned-memory ingestion: `WITHOUT_VERIFIED_BRAIN`; authenticated repository transport/readback is not native receiver use.
