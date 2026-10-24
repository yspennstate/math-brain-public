# account01/B11 complete audit — fixed multiplicity 17

Run: `20260924T121239Z-account01-B11-fixed-multiplicity-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Starting lens: sign-independent Schur-complement spectral counts, inverse compression, strict/non-strict thresholds, singular-matrix approximation.  
Pinned mathematical source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Pinned source SHA-256 reported by the objective/package: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Fresh master immediately before publication was observed at `9516b965846f9cf55364f37ffecd0794c435d8ba`; the manuscript blob was unchanged.

## Verdict

**Mathematical verdict: PASS on the complete 790-line written 17-eigenvalue proof.** I read and independently checked every mathematical definition, displayed identity, lemma, proposition, branch of the proof, scaling step, and stated limitation in `manuscript.tex`. I found no FALSE statement and no theorem-breaking mathematical GAP.

This is one worker's complete audit. It is not a self-awarded independent-validation certificate, and it is not a solution of the unrestricted three-eigenvalue conjecture.

**Repository/package verdict: GAP, non-mathematical.** Fresh root listings and direct path reads show that `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are absent even though `README.md` advertises them. The proof itself is self-contained in `manuscript.tex`, so this does not affect the theorem. The finite-check claims in `AUDIT.md` are therefore **UNCHECKED in this run**: I did not treat missing checker files as mathematical evidence.

**Presentation verdict: GAP-PRESENTATION, repaired without changing the theorem.** The hypothesis gives marginal density caps only almost everywhere, while a few later inverse-branch/coarea formulas evaluate chosen density versions pointwise. At the beginning of the proof one may choose, for every coordinate, a Borel density representative equal a.e. to the original one and replace it pointwise by `min(K,max(0,f_i))`. This leaves the law unchanged and makes the pointwise cap globally valid. The projection lemma already makes this choice locally; stating it once globally removes the representative ambiguity.

## Fatal-defect check

No fatal defect was found. The most sensitive chain—singular Schur count, nonsymmetric interpolation support, global rank `<=3r` versus restricted rank `<=r`, the fact that `D` vanishes on the seed, the spectral-to-volume conversion, Fourier normalization, and full versus truncated half potentials—survives the checks below.

## B11 reconstruction: Schur spectral count, including singular A

For

\[
A=\begin{pmatrix}B&C\\ C^T&D\end{pmatrix},\qquad \det B\ne0,\qquad
S=D-C^TB^{-1}C,
\]
with `A` real symmetric and `B` of size `k`, the manuscript claims

\[
N_S(t)\ge N_A(t)-k,\qquad N_T(t)=\#\{j:|\lambda_j(T)|\ge t\},\quad t>0.
\]

**PASS.** If `A` is invertible, `S^{-1}` is exactly the complementary principal block of `A^{-1}`. Cauchy interlacing/min-max applied separately to `A^{-1}` and `-A^{-1}` gives

\[
\#\{|\lambda(S^{-1})|>t^{-1}\}
\le \#\{|\lambda(A^{-1})|>t^{-1}\}.
\]

Because strict inverse threshold `>t^{-1}` corresponds exactly to original modulus `<t`, the two sides are `(n-k)-N_S(t)` and `n-N_A(t)`. This preserves the manuscript's non-strict original threshold `>=t` exactly and yields the stated inequality.

For singular `A`, choose real `\varepsilon_m\to0` avoiding the finitely many roots for which `A+\varepsilon_m I` or `B+\varepsilon_m I_k` is singular, with `|\varepsilon_m|<t`. Its Schur complement

\[
S_m=D+\varepsilon_m I-C^T(B+\varepsilon_m I)^{-1}C
\]
converges to `S`, while Weyl gives

\[
N_{A+\varepsilon_mI}(t-|\varepsilon_m|)\ge N_A(t).
\]

The invertible case at threshold `t-|\varepsilon_m|` yields

\[
N_{S_m}(t-|\varepsilon_m|)\ge q:=N_A(t)-k.
\]

If `q>0`, the `q`-th ordered modulus of an eigenvalue of `S_m` is at least `t-|\varepsilon_m|`; continuity of ordered eigenvalue moduli gives the `q`-th ordered modulus of `S` at least `t`. Thus `N_S(t)>=q`. If `q<=0`, the claim is trivial. This supplies the explicit strict/non-strict limiting step only compressed in the manuscript's prose.

Equivalently,

\[
\boxed{s_j(S)\ge s_{j+k}(A),\qquad 1\le j\le n-k,}
\]

where for symmetric matrices `s_j` are ordered absolute eigenvalues. The loss of exactly `k` directions is sharp for diagonal block examples, so lowering the global multiplicity cannot come from a better universal Schur count alone.

## End-to-end line audit

| Source lines / object | Status | Reasoning and impact |
|---|---|---|
| 1–80: definitions, theorem, corollary, normalization architecture | PASS | Quantifiers retain arbitrary dimension/sign/remaining spectrum/affine terms/rough product laws. The stated normalized targets `9` and `17` agree with later dependencies. |
| 81–160: Fourier convention, Gaussian inversion, Plancherel, power envelope, Riesz half potential | PASS | Constants match `hat f(t)=int e^{itx}f(x)dx`. Gaussian approximation does not presuppose a density for the output law. The weighted `3/4` envelope integral is exactly `12 sqrt(u)`. |
| 161–220: singular-value perturbation, `lem:schur`, strict diagonal dominance | PASS | Rank perturbation direction is correct for nonsymmetric matrices. Schur count is independently reconstructed above, including singular ambient matrices and threshold equality. Row diagonal dominance works without symmetry. |
| 221–282: geometric rank-one Brascamp–Lieb and product projections | PASS | Heat-flow derivative has the correct nonnegative sign from the frame contraction. Large-time Gaussian normalization uses `sum c_i=d`; small-time limit uses Lebesgue points/Fatou. Projection proof rotates deterministic integration variables only, not probabilistic independence. |
| 283–320: integrated scalar Fourier powers and start of decoupling | PASS | `m=floor(p/2)>=p/4` and `|hat f|<=1` justify reduction to an even power. The density at zero is bounded by the genuine product-projection theorem with coefficient norm `sqrt(2m)`. |
| 321–400: decoupling, regularized determinant, crossing volumes | PASS | Independent copies and conditioning preserve original product structure. In the graph BL calculation, the `d_i` powers cancel and `alpha=(2 pi e)^2` cancels the entropy factor; fourth roots give determinant exponent `-1/8`. Cauchy–Binet volume identities are exact. |
| 401–460: volume envelopes, scalar square profile, definite pair, hyperbolic setup | PASS | Order five gives an integrable `|t|^{-5/4}` envelope; order three is only used with the Riesz weight. Square and definite-pair Jacobians have the stated constants. No independence after rotation is used. |
| 461–526: hyperbolic tails and quarter-power concentration | PASS | Hyperbolic `(delta,t)` Jacobian is `1/(2 sqrt(D))`; an original coordinate pays each tail. Random-sign splitting produces a genuine cross block of norm at least `||S||/4`, and Gaussian smoothing gives the stated `1/4` small-ball exponent. Layer cake gives `L0=4+4 log 16`. |
| 527–584: disjoint volume, sampling, nonsymmetric interpolation, completion | PASS | Bordered determinant identity is exact. Singular deleted seeds justify an inequality rather than equality. `P=A[:,T]B^{-1}A[S,:]` interpolates rows `S` and columns `T`; `R[L,L]=P[L,L]`, `rank R[L,L]<=r`, while seed-supported corrections give `rank R<=3r`. `D` is exactly zero on `S union T`. |
| 585–651: no-pivot spectral-to-volume, cut, analytic consequences | PASS | Bad-ratio `r=0` is excluded by operator norm. For `1<=r<=4`, `epsilon<=(r+1)/80<=1/16`; with `m=4k-3`, global rank loss forces `r+1` large entries of `D` in `L`. On their block, `371/400 > 23/28` gives strict diagonal dominance, contradicting restricted rank `<=r`. Random cut contributes exactly `4^{-k}`. |
| 652–720: singular kernels, pivot half-potential, nine-direction bound | PASS | Kernel estimates are Tonelli/rearrangement arguments. Scalar pivot uses Schur remainder plus the quarter-power logarithmic potential; pair branches use conditional domination. `H(Q)<=600` is truncated, while adding at most one outside `|Q-a|<=1` correctly gives the full half potential `<=601`. |
| 721–760: main theorem branches and general scaling | PASS | No-pivot `<2400`; scalar pivot `<=6010`; definite pair `<40`; indefinite pair `<251`. The Schur counts lose exactly the pivot dimension. General scaling gives the required `K^2/s`. |
| 761–790: threshold accounting, limitations, regularity scope | PASS | Manuscript correctly distinguishes `k=5` direct density from `k=3` half-potential use, does not claim `s_3` suffices, and claims continuity only in the integrable-Fourier no-pivot branch. |
| README/AUDIT references to missing supplementary files | GAP (package) | `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json` were absent on fresh master; finite-check claims are UNCHECKED here. No mathematical dependency. |

No mathematical source range is left `UNCHECKED`; the only `UNCHECKED` items are the advertised finite diagnostics whose files are absent.

## Exact branch constants and same-proof sharpening

The manuscript's scalar-pivot truncated half-potential estimate is actually

\[
H_* = 10(8+3L_0)=10(20+12\log16)=200+120\log16.
\]

This dominates the other nine-direction truncated-half-potential branches: the no-pivot value is `<200`, the definite-pair value is `<40 pi`, and the indefinite-pair calculation is smaller than `200+120 log16`. Therefore

\[
\sup_a E|Q-a|^{-1/2}\le 201+120\log16
\]

for every nine-direction remainder. The main scalar-pivot branch is consequently

\[
\|p_Q\|_\infty\le 10(201+120\log16)
=2010+1200\log16
=5337.106466687737\ldots .
\]

All other normalized branches are below this (`800e≈2174.63`, definite pair `<40`, indefinite pair `<251`). Thus the **same 17-eigenvalue proof** rigorously strengthens the advertised constant to

\[
\boxed{\|p_Q\|_\infty\le(2010+1200\log16)\,K^2/s<5610\,K^2/s.}
\]

This sharpens the numerical constant but does not lower the eigenvalue multiplicity.

## Threshold-lowering audit: why the present mechanism stops at 17

For the density branch `k=5`, a bad telescoping ratio can occur at terminal `r=4`. Under `s_17(A)>=1`, the global rank bound `rank R<=12` leaves five large entries of `D`, and a `5x5` strictly diagonally dominant block contradicts `rank R[L,L]<=4`.

With only `s_16(A)>=1`, the same argument forces only four large entries. An invertible `4x4` block is compatible with `rank R[L,L]<=4`. Therefore changing `17` to `16` in the current proof is invalid.

I pushed the Schur mechanism further and obtained an exact saturation description rather than a contradiction. Let `tau=1-epsilon`, assume the terminal `r=4` chamber, and suppose exactly four entries of `D` have modulus at least `tau`; call their set `H`. Put `M=A-E=D+R` and `N=M-D_H`. Then `rank D_H<=4` and `s_16(M)>=tau`, hence

\[
s_{12}(N)\ge tau.
\]

On `H`, `N[H,H]=R[H,H]=P[H,H]`, which is invertible by the same diagonal-dominance estimate. A nonsymmetric singular-value Schur-count lemma (proved in the companion improvement note) then gives at least eight singular values `>=tau` in the Schur complement of this pivot.

Write `R=P+U+V`, where `U` is supported on the four seed rows `T` and `V` on the four seed columns `S`. Because `P` has rank four and `P[H,H]` is invertible, the Schur complement of `P` across `H` vanishes exactly. Expanding the Schur complement of `N` leaves

\[
D_K+W_T+W_S,
\]

where `W_T` remains supported on rows `T` and has rank at most four, and `W_S` remains supported on columns `S` and has rank at most four. If no fifth `D` entry reaches `tau`, then `||D_K||<tau`; rank perturbation shows this Schur complement has **at most eight** singular values `>=tau`. Hence the attempted 16-direction Schur route lands at an exact `8 versus 8` saturation, not a contradiction.

This identifies the terminal obstruction more sharply: any strict rank slack in either seed-supported correction, any ninth Schur singular direction, or any fifth diagonal entry would close the chamber, but none follows from the present hypotheses alone.

A fresh source match also found account02/B14's independently posted terminal growth lemma: in this same `r=4` chamber, a sampled-good seed forces two neighboring disjoint four-minors larger by the factor `(109/100)^4>1`. That is compatible with the saturation description above but still does not prove the 16-eigenvalue theorem because the heavier neighboring seeds need not inherit the good residual bound. I do not count that peer theorem as my result.

## Final audit status

- Written 17-eigenvalue theorem: **PASS** in this complete account01/B11 audit.
- Advertised constant `10000`: **PASS**, and same proof improves it to `2010+1200 log 16 <5610`.
- Full 16-eigenvalue theorem: **GAP / not proved**. The first unpaid implication is the terminal `r=4` good-seed/heavier-neighbor transfer or another mechanism that breaks the exact `8 versus 8` Schur saturation.
- Missing `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json`: **GAP (packaging/reproducibility only)**; finite-check claims are **UNCHECKED** in this run.
- Pointwise density representative convention: **GAP-PRESENTATION**, repaired as stated above.
- Unrestricted three-eigenvalue QFORM: **OPEN**.
