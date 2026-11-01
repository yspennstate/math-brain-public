# fleet02/B16 independent end-to-end audit — fixed multiplicity 17

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T122844Z-fleet02-B16-FIXMULT-auto11-r1`  
Lens: independent full proof reconstruction before relying on peer verdicts; fleet02 counterexample emphasis.

## Source pin and package state

Mathematical source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, file `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.

- Git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- Advertised source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69b89591a4107e785340f65e69` is **NOT** used; the actual advertised SHA-256 read from the owner objective/README is `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- Fresh master snapshot pinned for this audit: `763cd52f2b764cfd974ddd63eb61db4871df85e4`.
- `compare_commits(7c0d6e...,763cd52...)` showed only added audit/improvement/package files and no modification of `manuscript.tex`; the audited master snapshot therefore contains the same manuscript blob as the initial source commit.

Repository package status: **GAP / supplementary finite-check material UNCHECKED.** At the pinned snapshot the root contains `README.md`, `AUDIT.md`, `manuscript.tex`, `audits/`, and `improvements/`. Direct fetches of `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` returned 404 although `README.md` and `AUDIT.md` describe them as canonical/reproducible package members. This is a reproducibility/documentation gap, not a mathematical dependency gap, because every specialized argument used by the theorem is written in `manuscript.tex`.

The SHA-256 string above is the repository-advertised value; this connector-only review independently observed the git blob but did not recompute raw-file SHA-256 bytes.

## Overall verdict

**PASS for the complete written 17-eigenvalue candidate.** I independently read all 790 source lines, reconstructed the proof graph, checked every lemma invocation against its hypotheses, and found no fatal mathematical gap in

\[
s_{17}(A)\ge s>0 \Longrightarrow
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s
\]

for arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary signature and remaining spectrum, and arbitrary affine `b,c`.

This is one worker review only. It does not self-award independent-validation/release status and does not claim the unrestricted three-eigenvalue QFORM conjecture is solved.

## Exhaustive source-line audit

| Source lines | Status | Independent check | Downstream impact / next obligation |
|---|---|---|---|
| 1–45 | PASS | Preamble/macros are harmless; abstract matches the later theorem and does not insert support, moment, sign, regularity, log-concavity, or diagonal-basis assumptions. | None. |
| 46–83 | PASS | Singular-value convention, essential-supremum convention, theorem quantifiers, affine terms, and normalization architecture are correct. `eta=1/100`, `kappa=1/80^2`. The distinction between order-3 half potential and order-5 density is explicit. | Main scope preserved. |
| 84–160 | PASS | Fourier convention gives the stated Plancherel/inversion constants. Gaussian regularization and weak convergence are sufficient for rough laws. The gamma representation plus Gaussian inversion gives coefficient `1/sqrt(2*pi)` in the Riesz half-potential bound; the `3/4` envelope yields exactly `12 sqrt(u)`. All Tonelli steps are on nonnegative majorants. | Supplies inversion and the order-3 receiver. |
| 161–220 | PASS | Approximation-number perturbation/rank inequalities are valid for nonsymmetric matrices. For an invertible principal pivot, `S^{-1}` is the complementary principal block of `A^{-1}`; positive and negative interlacing separately give `N_S(t)>=N_A(t)-k`. The `A+epsilon I` limit repairs singular `A`. Strict row diagonal dominance is valid without symmetry. | Every later Schur use meets the invertible-pivot hypothesis. |
| 221–300 | PASS | Heat flow gives `d_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0` from the Parseval frame; large-time normalization uses `sum c_i=d`, and compact support supplies a Gaussian dominating function. Product projections integrate the original product density over deterministic orthogonal fibers and never infer rotated independence. In the scalar Fourier-power lemma, `|hat f|^{2m}` is integrable already by Plancherel, so inversion at zero is noncircular. | Uniform product-projection and scalar Fourier inputs are valid at the constants used. |
| 301–400 | PASS | Cauchy–Schwarz in one physical bank gives the power-2 decoupling; Jensen gives power 4; difference coordinates remain independent and cap one. In the graph BL calculation, ridge weights form a Parseval frame, the `d_i` scale powers cancel against the scalar Fourier bound, `prod c_j^{-c_j/2}<=e^{theta/2}`, and `alpha=(2*pi*e)^2` cancels the remaining scalar factor. Fourth roots give determinant exponent `-1/8`. Cauchy–Binet gives order-5 exponent `5/4` and order-3 exponent `3/4`. | Only order 5 is directly `L^1`; order 3 is used with the half-potential weight. |
| 401–428 | PASS | Scalar square inverse branches give the stated `|z-v|^{-1/2}` profile and interval-preimage bound. Conditional use is a domination-of-measures statement, not independence. The definite-pair Jacobian is `1/(2 sqrt(det B))`; integrating angle gives `pi M/sqrt(|det B|)` without rotated independence. | Pivot branches valid for rough product laws. |
| 429–484 | PASS | Hyperbolic parametrization has Jacobian `1/(2 sqrt D)`. On each `u e^t+w e^{-t}` branch, one original coordinate has coefficient at least `sqrt(delta Lambda)/(2 sqrt2)`; beyond the stated cutoff it is one-sign monotone with `|y'|>=|y|/3`. Density cap plus total mass bounds each tail by `3 log 2`; the middle interval contributes at most `(15/2)log2<6`. `Lambda>=2/sqrt D` yields the displayed logarithmic envelope. Exceptional critical levels are handled through nonnegative test functions/Tonelli. | Correct logarithmic pair receiver. |
| 485–530 | PASS | If no diagonal is at least `||S||/2`, random signs isolate a physical cross block with norm at least `||S||/4`; retaining one singular factor in the determinant theorem gives `|t|^{-1/4}`. Gaussian smoothing with `v=1/8` gives coefficient `3.9952593616<16`; layer cake gives `L0=4+4 log16`. | Supplies one-surviving-eigenvalue logarithmic control. |
| 531–584 | PASS | Ordered disjoint minors and the bordered determinant identity are correct. Singular deleted seeds may have nonsingular extensions, so sampling is correctly an inequality, not an equality. `P=A[:,T]B^{-1}A[S,:]` may be nonsymmetric but exactly interpolates rows `S` and columns `T`. Completion gives `D=0` on `S union T`, `E_ii=0`, `rank R<=3r`, and `R[L,L]=P[L,L]` with restricted rank `<=r`. | Both rank bounds and seed support are genuine, not inherited assertions. |
| 585–652 | PASS | A bad volume ratio gives `||E||_F<=(r+1)/80<=1/16`. Singular-value perturbation plus global rank `3r` forces at least `r+1` diagonal entries of `D` of size `>=1-epsilon`, all inside `L`. On the resulting `(r+1)`-set, `|R_ii|>=371/400` while each off-diagonal is `<1/7+1/16`; for `r<=4`, row sum `<23/28`. Slack is `371/400-23/28=0.10607142857>0`, contradicting restricted rank `<=r`. Fair cuts retain each ordered disjoint pair with probability `4^{-k}`. Constants check to `12 sqrt(80e)=176.959336187<200` and `800e=2174.625462767<2400`. | Closes no-pivot `s_9` half potential and no-pivot `s_17` density. |
| 653–726 | PASS | The two singular-kernel estimates have correct near/far and centered-overlap bounds. Scalar pivot plus one Schur direction yields truncated half potential `<600`; definite and indefinite pair alternatives are uniformly controlled. The full/truncated distinction is explicit: outside distance one, `|Q-a|^{-1/2}<=1`, giving `<=601`. | Supplies exactly the nine-direction receiver required by the main scalar pivot. |
| 727–774 | PASS | Case split is exhaustive: no pivot; scalar pivot; definite pair; indefinite pair. Scalar pivot from `s_17>=1` leaves at least 16 Schur directions, hence the nine-direction input. A pair leaves at least 15; the indefinite branch only needs one surviving direction for the logarithmic potential. Largest normalized branch is `6010`; the other key maxima are `<2400`, `<40`, and `238.9974<251`. Scaling with `Y=KX` and `Q=(s/K^2) tilde Q` returns `10000 K^2/s`. | Candidate theorem closes exactly as stated. |
| 775–790 | PASS for mathematical scope; UNCHECKED for external attribution | Limitations correctly state that the `s_3` theorem is not proved and that domination-only branches do not claim continuity. BCCT/RV are attribution only because the specialized inequalities used are reproved in the manuscript. I did not perform a primary-source priority audit in this B16 run. | No theorem edge depends on the unchecked attribution. |

All 790 source lines are covered by the contiguous ranges above; no mathematical range is left UNCHECKED.

## Equation and definition audit

The following labeled definitions/equations were independently checked against the surrounding derivation and are **PASS**: `eq:main`, `eq:parameters`, `eq:plancherel`, `eq:inversion`, `eq:gaussian-inversion`, `eq:envelope`, `eq:riesz`, `eq:riesz-power`, `eq:rank-perturb`, `eq:frame`, `eq:bl`, `eq:projection`, `eq:scalar-fourier`, `eq:cross-form`, `eq:decouple2`, `eq:decouple4`, `eq:determinant`, `eq:graph-bl`, `eq:Zk`, `eq:det-expand`, `eq:vol-envelope`, `eq:five-volume`, `eq:three-volume`, `eq:profile`, `eq:hyperbola`, `eq:hyper-coarea`, `eq:quarter`, `eq:log-bound`, `eq:Vr`, `eq:small-entry`, `eq:P`, `eq:sampling`, `eq:completion`, `eq:completion-bounds`, `eq:volume-lower`, `eq:cut`, `eq:no-pivot-nine`, `eq:no-pivot-seventeen`, `eq:H`, `eq:J`, `eq:log-kernel`, `eq:pivot-H`, `eq:scalar-max`, `eq:nine-H`, and `eq:final-scalar`. Definition `def:pivot-volume` and every theorem/lemma/proposition invocation were checked with the hypotheses listed below.

## Hypothesis ledger and proof graph

| Node | Exact hypothesis checked | Receiver / dependency actually checked |
|---|---|---|
| `lem:fourier` | `f in L1 cap L2`; or `phi_Z in L1`; arbitrary law for Gaussian identity | Gaussian approximate identity, Fubini, weak convergence. |
| `thm:bl` | unit vectors, positive weights, Parseval-frame identity, nonnegative integrable one-dimensional inputs | Heat-flow proof reconstructed; no external BL theorem needed. |
| `lem:projection` | independent original coordinates, cap one, `U^T U=I` | Deterministic orthogonal fiber integration + `thm:bl`; no projected independence. |
| `lem:scalar-fourier` | one probability density `<=1`, `p>=2` | Plancherel + scalar projection density of independent signed copies. |
| `lem:decoupling` | disjoint original-coordinate banks, arbitrary finite measurable self phases | Cauchy–Schwarz, independent copy, Jensen; difference coordinates retain product structure. |
| `thm:determinant` | exactly the decoupled cross-form; no rank/sign/leverage assumption | Graph Parseval frame + BL + scalar Fourier powers; determinant exponent `-1/8`. |
| `lem:schur` | real symmetric original matrix and invertible principal pivot | Inverse-compression interlacing, then singular limit. |
| `lem:hyperbola` | two **independent original** scalar coordinates with caps one; indefinite invertible `2x2` block | Original-coordinate tail integration; rotation only parametrizes the deterministic conic. |
| `lem:sampling` | `V_r(A)>0`, disjoint nonsingular seed | Bordered determinants and volume-weighted averaging. |
| `lem:completion` | sampled seed from previous lemma | `D` seed vanishing; nonsymmetric `R,E`; global/restricted ranks checked separately. |
| `prop:volume` | symmetric `A`, no `eta`-pivot, `s_{4k-3}(A)>=1`, `1<=k<=5` | Sampling/completion + nonsymmetric singular-value perturbation + diagonal dominance. |
| `cor:no-pivot` | no pivot plus `s_9` or `s_17` | Random physical cut + volume envelope. |
| `prop:pivot-H` | at least two large eigenvalues plus an `eta`-pivot | Scalar, definite-pair, indefinite-pair alternatives exhaust pivots. |
| `prop:nine` | `s_9(A)>=1` | Pivot branch uses truncated `H<=600`; no-pivot branch supplies full half potential; outside contribution adds at most one. |
| `thm:main` | arbitrary product laws `<=1` after normalization, symmetric `A`, `s_17>=1`, arbitrary affine terms | Exhaustive pivot/no-pivot split; only original-coordinate conditioning. |
| scaling | original caps `<=K`, `s_17(A)>=s>0` | `Y=KX`, `tilde Q=(K^2/s)Q`, scalar density scaling. |

No proof edge is inherited solely from the author self-audit. The only UNCHECKED items are external attribution/priority and the absent supplementary checker files.

## Counterexample stress tests and structural obstructions

### 1. Target-valid no-pivot witness

For any integers `q>=1`, `m>=101`, let

\[
A_{q,m}=I_q\otimes (J_m/m),
\]

where `J_m` is the all-ones `m x m` matrix. Each block `J_m/m` has spectrum `{1,0,...,0}`, so `A_{q,m}` has exactly `q` singular values equal to one. For `q=17`, `s_17(A_{17,m})=1`.

Every physical diagonal entry is `1/m<1/100`. A physical principal two-coordinate determinant is either zero (two coordinates in the same block) or `1/m^2<1/100` (coordinates in different blocks, where the off-diagonal is zero). Thus `A_{17,m}` has **no `eta`-pivot despite satisfying the full 17-direction spectral hypothesis**.

Status: **PASS / valid counterexample to the shortcut “many unit spectral directions force a physical scalar or pair pivot.”** It is not a counterexample to the theorem; it confirms that the no-pivot Fourier-volume branch is indispensable.

### 2. Completion-rank saturation

Take

\[
A_0=\begin{pmatrix}
-3&1&-3&-3\\
1&-3&-3&-3\\
-3&-3&10&9\\
-3&-3&9&9
\end{pmatrix},\quad S=\{1\},\ T=\{2\},\ L=\{3,4\}.
\]

For the manuscript interpolation `B=[1]`, `P=A_0[:,T]B^{-1}A_0[S,:]`, one gets

\[
A_0[L,L]-P[L,L]=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\]

hence `E=0`, `D=diag(0,0,1,0)`, and `R=A_0-D`. Exact algebra gives

\[
\det A_0=144,\quad \operatorname{rank}A_0=4,\quad
\operatorname{rank}R=3,\quad \operatorname{rank}R[L,L]=1.
\]

Scaling by `1/20000` puts this witness strictly inside the local no-pivot entry inequalities while preserving the rank pair. Therefore the completion bounds `(3r,r)` are simultaneously sharp already at `r=1` from local no-pivot information alone.

Status: **PASS / proof-mechanism obstruction.** The scaled example does not retain unit spectral size, so it is not a counterexample to a lower-multiplicity density theorem. It does rule out lowering the `4r+1` bookkeeping threshold merely by decrementing either existing rank estimate.

## Threshold-reduction audit

No complete replacement proof lowering 17 was obtained in this run, so **no lower multiplicity is claimed**. Within the audited pipeline, order four gives characteristic-function exponent exactly `4/4=1`, i.e. only a `|t|^{-1}` endpoint, which is not absolutely integrable; order five is the first direct `L^1` receiver. The algebraic conversion simultaneously needs `4r+1` spectral directions in the worst sampled ratio. The rank-saturation witness above blocks a bookkeeping-only reduction.

A legitimate `17 -> m` improvement must therefore add new information beyond the present local no-pivot/rank argument, for example a source-valid endpoint receiver at order four or a quantitative mechanism converting the same-index bordered information into extra disjoint crossing volume. Any such claim must be supplied as a full replacement proof with constants and a closed dependency map before changing the theorem statement.

## Final status matrix

| Item | Status |
|---|---|
| 790-line mathematical manuscript | PASS |
| Theorem quantifiers/scaling/affine terms | PASS |
| Fourier normalization and rough-law limits | PASS |
| Geometric BL heat-flow proof | PASS |
| Product-projection and scalar Fourier powers | PASS |
| Decoupling/determinant exponents | PASS |
| Schur counts, including singular matrices | PASS |
| Hyperbolic/definite/scalar pivot receivers | PASS |
| Nonsymmetric interpolation support and both rank bounds | PASS |
| Spectral-to-volume conversion and constants | PASS |
| Full versus truncated half potentials | PASS |
| Current theorem `s_17 -> 10^4 K^2/s` | PASS as a written candidate under this one independent review |
| `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json` at pinned package snapshot | GAP / UNCHECKED because absent |
| Primary-source attribution/priority | UNCHECKED in this B16 run; no mathematical dependency |
| Any theorem below 17 | UNCHECKED / NOT CLAIMED |
| Unrestricted three-eigenvalue QFORM theorem | OPEN / NOT CLAIMED SOLVED |
