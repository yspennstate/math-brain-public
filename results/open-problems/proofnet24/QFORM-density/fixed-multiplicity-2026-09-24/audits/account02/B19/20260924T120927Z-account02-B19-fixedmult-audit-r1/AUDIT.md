# account02/B19 independent end-to-end audit — fixed multiplicity 17

Run: `20260924T120927Z-account02-B19-fixedmult-audit-r1`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer lens: B19 independent proof reconstruction and guarded integration; account02 counterexample emphasis.

## Source pin and package state

Baseline theorem source is pinned to `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, file `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`. The package advertises SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`; this connector-only audit pins that advertised SHA and the independently observed git blob, but does not claim a separate raw-byte SHA-256 recomputation. Fresh master snapshot `742ce5bda88b0ffa0680e6bd1ba7feace222d135` still contained the identical manuscript blob.

**Mathematical verdict: PASS for the complete written 17-eigenvalue candidate.** I read all 790 source lines and reconstructed the proof before consulting peer audit verdicts. I found no fatal mathematical gap in

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary signs and remaining spectrum, and arbitrary affine `b,c`.

This file is one worker review. It does not self-award release/peer-review status and does not claim the unrestricted three-eigenvalue QFORM theorem.

**Repository-package verdict: GAP / supplementary material UNCHECKED.** At fresh master snapshot `742ce5...`, the package root contained `README.md`, `AUDIT.md`, `manuscript.tex`, and the audit/improvement directories. Direct fetches of `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` returned 404. Both root `README.md` and root `AUDIT.md` describe those files/checks as package material. Therefore the finite-check/reproducibility claims that depend on those absent files are **UNCHECKED in this run**. This does not break the theorem proof because every specialized mathematical dependency used by the candidate is written in `manuscript.tex` itself.

## End-to-end line audit

| Source lines | Status | Independent reasoning / hypothesis check | Impact / next obligation |
|---|---|---|---|
| 1–45, preamble and abstract | PASS | The abstract states exactly the fixed-multiplicity theorem later proved; no hidden support, moment, sign, or regularity hypothesis is inserted. Macros do not change mathematical scope. | None mathematically. Compilation was not re-run in this connector-only audit. |
| 46–83, theorem, quantifiers, normalization architecture | PASS | `s_j` are singular values; for symmetric `A` these are absolute eigenvalues. The theorem retains arbitrary `n`, laws, signature, remaining spectrum, `b,c`. `eta=1/100`, `kappa=1/80^2`. The architecture distinguishes order 3 half-potential from order 5 density. | Main scope is preserved. |
| 84–160, Fourier/Gaussian identities, power envelope, Riesz half-potential | PASS | With `hat f(t)=int e^{itx}f(x)dx`, Gaussian regularization gives the stated Plancherel and inversion constants. The gamma representation plus Gaussian inversion yields coefficient `1/sqrt(2*pi)` in the half-potential bound. For the `3/4` envelope, the weighted integral is exactly `12 sqrt(u)`. Tonelli is used only on nonnegative majorants. | Supplies rough-law inversion and the order-3 receiver. |
| 161–220, singular values, Schur count, diagonal dominance | PASS | The perturbation/rank statements are approximation-number inequalities valid without symmetry. For invertible `A`, `S^{-1}` is a principal compression of `A^{-1}`; positive and negative interlacing separately imply `N_S(t)>=N_A(t)-k`. The `A+eps I` limit handles singular `A`. Strict row diagonal dominance is valid for nonsymmetric matrices. | Every later Schur invocation meets the invertible-pivot hypothesis. |
| 221–300, geometric BL, product projections, scalar Fourier powers | PASS | Heat flow gives `partial_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0` from the Parseval frame. Large-time normalization uses `sum c_i=d`. The projection proof integrates the original product density over deterministic orthogonal fibers and never asserts rotated independence. For scalar Fourier powers, `|hat f|^{2m}` is already integrable by Plancherel and inversion at zero is therefore noncircular. | Uniform product-projection and scalar Fourier inputs are valid at the constants used. |
| 301–400, cross-block decoupling, regularized determinant, volume envelopes | PASS | Cauchy–Schwarz in one physical bank and one independent copy of the other gives the power-2 inequality; Jensen gives power 4. Difference coordinates remain independent and cap one. In the graph BL calculation, the `d_i` scale powers cancel against the scalar Fourier bound; `prod c_j^{-c_j/2}<=e^{theta/2}` and `alpha=(2*pi*e)^2` cancel the remaining scalar multiplier. Taking fourth roots gives determinant exponent `-1/8`. Cauchy–Binet then gives order-5 exponent `5/4` and order-3 exponent `3/4`. | This is the only direct `L^1` Fourier receiver in the baseline; order 4 is endpoint only. |
| 401–428, scalar square and definite pair | PASS | Square change of variables gives the two-branch `|z-v|^{-1/2}` profile and interval-preimage bound. The conditional profile is a measure domination statement, not independence. The definite pair is diagonalized only inside a deterministic 2-D integral; the Jacobian gives `pi M/sqrt(|det B|)`. | Pivot branches are valid for arbitrary rough laws. |
| 429–484, hyperbolic pair | PASS | The `(delta,t)` Jacobian is `1/(2 sqrt D)`. On each branch `u e^t+w e^{-t}`, one original coordinate has a growing coefficient at least `sqrt(delta Lambda)/(2 sqrt2)`; after the stated cutoff it is one-sign monotone and `|y'|>=|y|/3`. Cap one plus mass one bounds each tail by `3 log 2`; the middle interval gives the logarithmic term. `Lambda>=2/sqrt D` yields the displayed envelope. Exceptional critical levels are handled through test functions/Tonelli. | The logarithmic singularity is genuine; it must be averaged against a surviving Schur direction. |
| 485–530, quarter-power concentration | PASS | If no diagonal is large, random signs isolate a physical cross block with norm at least `||S||/4`; keeping one singular factor in the determinant theorem gives the `|t|^{-1/4}` envelope. Gaussian smoothing with `v=1/8` gives a coefficient below 16. Layer cake gives `L0=4+4 log 16`. | Supplies the one-surviving-eigenvalue logarithmic receiver. |
| 531–584, disjoint volumes, sampled interpolation, completion | PASS | The bordered determinant is exact for nonsingular seeds. Singular deleted seeds can have nonsingular extensions, so the sampling statement is correctly an inequality. `P=A[:,T]B^{-1}A[S,:]` may be nonsymmetric but agrees on rows `S` and columns `T`. `R-P` is supported in rows `T` or columns `S`, hence `rank R<=3r`; on the seed complement `R[L,L]=P[L,L]`, so `rank<=r`. `D` is diagonal and vanishes on `S union T`; `E` has zero diagonal. | The two distinct rank bounds are both essential to the 17 threshold. |
| 585–652, spectral-to-volume, random cut, no-pivot consequences | PASS | A bad ratio gives `||E||_F<=(r+1)/80<=1/16`. Singular-value perturbation plus `rank R<=3r` forces at least `r+1` large entries of diagonal `D`, all in `L`. There `|R_ii|>=371/400`; each off-diagonal is `<1/7+1/16`; for `r<=4` the row sum is `<23/28`. Exact dominance slack is `297/2800>0`, contradicting `rank R[L,L]<=r`. A fair cut retains every ordered disjoint pair with probability `4^{-k}`. The resulting constants are `12 sqrt(80e)=176.959336...<200` and `800e=2174.625462...<2400`. | Closes no-pivot `s_9` half-potential and no-pivot `s_17` density branches. |
| 653–726, singular kernels, pivot half-potential, nine-direction receiver | PASS | The `J(d)` near/far split has the stated fixed integral and logarithmic tail. The log kernel is maximized by centered interval overlap. Scalar pivot + surviving Schur direction gives truncated half-potential `<600`; definite and indefinite pair alternatives are uniformly bounded. Full versus truncated potentials are explicitly separated: outside distance one the kernel is at most one, hence `<=601`. | Supplies exactly the receiver required by the scalar pivot of the main theorem. |
| 727–774, main theorem, scaling, dependency accounting | PASS | Case split is exhaustive: no pivot; scalar pivot; definite pair; indefinite pair. Scalar pivot from `s_17>=1` leaves at least 16 Schur directions, more than the 9 required. A pair leaves at least 15 and the indefinite branch needs only one. Largest normalized branch is `6010`. With `Y=KX`, `tilde Q=(K^2/s)Q`; density scaling returns `10000 K^2/s`. | Candidate theorem closes as stated. |
| 775–790, limitations/acknowledgment/bibliography | PASS for scope; UNCHECKED for attribution | The manuscript correctly says it does not prove the `s_3` theorem and does not assert continuity in domination-only branches. I did not independently re-run a primary-source priority/attribution audit of BCCT or Rudelson–Vershynin in this B19 run. Their specialized inequalities are reproved in the manuscript, so no proof edge depends on that attribution. | No mathematical downstream effect; literature attribution remains outside this review. |

## Equation and invocation audit

Every labeled proof equation was checked in the line pass above. In particular the following dependency-critical labels are **PASS** with their exact hypotheses preserved: `eq:plancherel`, `eq:inversion`, `eq:gaussian-inversion`, `eq:envelope`, `eq:riesz`, `eq:riesz-power`, `eq:rank-perturb`, `eq:frame`, `eq:bl`, `eq:projection`, `eq:scalar-fourier`, `eq:decouple2`, `eq:decouple4`, `eq:determinant`, `eq:graph-bl`, `eq:Zk`, `eq:det-expand`, `eq:vol-envelope`, `eq:five-volume`, `eq:three-volume`, `eq:profile`, `eq:hyperbola`, `eq:quarter`, `eq:log-bound`, `eq:Vr`, `eq:small-entry`, `eq:P`, `eq:sampling`, `eq:completion`, `eq:completion-bounds`, `eq:volume-lower`, `eq:cut`, `eq:no-pivot-nine`, `eq:no-pivot-seventeen`, `eq:H`, `eq:J`, `eq:log-kernel`, `eq:pivot-H`, `eq:scalar-max`, `eq:nine-H`, and `eq:final-scalar`.

The most sensitive invocation checks are:

1. **Schur counts:** every use conditions on an actually invertible scalar/pair pivot. The main scalar branch removes one direction (`17 -> >=16`), the pair branch removes two (`17 -> >=15`), and the auxiliary pivot-half-potential proposition assumes two input directions before removing one.
2. **Nonsymmetric interpolation:** only singular values/ranks are applied to `R,E,A-E`; no eigenvalue statement is made about a nonsymmetric auxiliary.
3. **Seed support:** `D=0` on `S union T` is what puts the forced large diagonal entries inside `L`, where the sharper `rank R[L,L]<=r` applies.
4. **Rough laws:** all conditioning remains on original coordinates; exceptional coarea slices are avoided by nonnegative-test-function formulations; no conditional density cap is inferred from an unconditional rotated marginal.
5. **Full/truncated half potentials:** the manuscript never substitutes the truncated `H` for the full half-potential without adding the outside contribution `<=1`.

## Account02 adversarial counterexample: the rank bounds cannot be improved from local no-pivot information alone

Status: **PASS / exact proof-mechanism obstruction**, not a counterexample to the 17-eigenvalue theorem.

Let

\[
A_0=\begin{pmatrix}
-3&1&-3&-3\\
1&-3&-3&-3\\
-3&-3&10&9\\
-3&-3&9&9
\end{pmatrix},
\qquad S=\{1\},\quad T=\{2\},\quad L=\{3,4\}.
\]

Then `B=A0[S,T]=[1]`. The sampled-interpolation formula gives `F=0`,

\[
D=\operatorname{diag}(0,0,1,0),
\]

and `R=A0-D`. Exact elimination gives

\[
\det A_0=144,\quad \operatorname{rank}A_0=4,
\quad \operatorname{rank}R=3,
\quad \operatorname{rank}R[L,L]=1,
\quad \operatorname{rank}D=1.
\]

Thus for `r=1` the two completion bounds are simultaneously saturated: global rank `3r`, restricted rank `r`, while `D+R` can have rank `4r`. Direct sums give the corresponding algebraic saturation for arbitrary `r`.

Moreover this rank saturation persists inside the manuscript's **no-pivot small-entry class**. For `alpha=1/20000`, put `A=alpha A0`. The largest diagonal magnitude is `10 alpha=0.0005<eta`; the largest absolute principal pair determinant is `39 alpha^2=9.75e-8<eta`. Hence there is no `eta`-pivot, while ranks are unchanged and `E=0`. This does not meet the unit spectral hypothesis after scaling, so it is not a lower-threshold theorem counterexample. It does prove that one cannot replace `rank R<=3r` or `rank R[L,L]<=r` by a smaller universal rank bound merely by invoking the local no-pivot inequalities.

**Downstream consequence.** A `17 -> 16` or `17 -> 13` proof cannot be obtained by bookkeeping that simply decrements the existing completion ranks. At the worst sampled ratio `r=4`, the present contradiction needs `r+1=5` large diagonal residuals; `4r` spectral directions can saturate the rank count with only `r` such residuals.

## Guarded integration after baseline reconstruction

Only after completing the independent audit above did I compare current peer artifacts. Two source-backed barriers are compatible with this reconstruction and sharpen the next obligation without changing the baseline manuscript:

- account03/B07 gives an exact deletion-multiplicity identity and an independent rank-saturation example, confirming that the universal `(r+1)^2` sampling multiplicity and the `(3r,r)` rank pair cannot be improved by counting/rank bookkeeping alone;
- account01/B03 proves that, within the same leverage-free independent-copy + geometric-BL + uniform scalar-Fourier-power family, the baseline fourth-power choice is analytically optimal: order-four crossing volume remains at the nonintegrable `|t|^{-1}` endpoint, while attempting a lower copy power would require a false uniform scalar `L^p` Fourier bound for `p<2`.

These are **method obstructions, not lower-bound theorems for multiplicity**. I found no complete replacement argument lowering 17 while preserving arbitrary rough product laws, arbitrary affine terms, arbitrary signature and remaining spectrum. Therefore this run makes **no multiplicity-reduction claim**.

The first honest improvement obligation is to add genuinely new information at one of two places: either convert the same-index bordered minors represented by the large diagonal residuals into quantitative disjoint crossing volume, or develop an order-four endpoint receiver that does not rely on absolute `L^1` inversion and the leverage-free scalar `L^p` input. Any claimed `17 -> m` reduction must then be written as a complete replacement proof with constants and a closed dependency map.

## Final status matrix

- 790-line mathematical manuscript: **PASS**.
- Theorem quantifiers/scaling/affine terms: **PASS**.
- Nonsymmetric interpolation support and ranks: **PASS**.
- Spectral-to-volume conversion: **PASS**.
- Fourier normalization/decoupling/determinant exponents: **PASS**.
- Heat-flow and rough-law limiting steps: **PASS**.
- Schur counts, including singular limit: **PASS**.
- Full versus truncated half potentials: **PASS**.
- Repository claims that `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json` are present: **GAP** at the audited master snapshot.
- Finite-check claims depending on those absent artifacts: **UNCHECKED** in this run.
- External classical attribution/priority: **UNCHECKED** here; no proof dependency.
- Complete lower-than-17 replacement theorem: **UNCHECKED / not established**.
- Unrestricted three-eigenvalue QFORM: **OPEN; not claimed solved**.

No baseline source patch is justified by this audit. The only concrete repository repair indicated is to restore the four advertised supplementary files or correct the package metadata; that repair has no downstream mathematical effect on the self-contained manuscript proof.
