Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 run 11 — outer covariance compensation and exact support oracles

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN**.

**SOURCE-METRIC NO MOVEMENT.**  For the owner-frozen classical iid proper-clause model, the externally verified explicit-decimal bracket remains

\[
[\alpha_L,\alpha_U]=[3.52,4.4898],
\qquad W=0.9698\longrightarrow0.9698.
\]

This run obeys the required method change after repeated endpoint nonmovement.  It does **not** tune another local rescue motif.  The main analytic result is an exact covariance/Legendre formula for the Hessian of the remaining three-dimensional Díaz copy-mass optimization, together with exact projected support oracles for the variable and clause feasibility polytopes.  A post-proof numerical solve of the six source stationarity equations gives a strongly negative local Hessian at the `4.4898` saddle, with least-magnitude eigenvalue about `-0.0744743`; this is diagnostic, not interval-certified endpoint progress.

The three materially different approaches tried were:

1. **global one-side KL domination of copy curvature** — **refuted as a universal shortcut** by a high-degree two-state block: state KL is paid once while induced copy Bregman curvature scales with degree;
2. **Legendre/covariance compensation of the two incidence sides** — **succeeds analytically** and gives the exact outer Hessian `H_copy-Sigma_V^{-1}-Sigma_C^{-1}`;
3. **project the outer feasible set by support functions instead of a blind grid** — **succeeds analytically**, giving closed-form variable and finite clause separation oracles; `34,224` exact integer block checks of the variable oracle passed.

No finite SAT/UNSAT sample, annealed fit, physics threshold, or neighboring unaudited project candidate is counted as source-metric movement.

## 1. Continuity, ownership, and consumed evidence

I continued only the scoped **cluster-aware weighted-counting / overlap-variational** claim in

- `operations/claims/PROB10-04.md`, blob `1095e6bfb106b53e810af56f2605521abb7143b4`.

I did not overwrite the historical `F0097` parent claim, did not take over NM13-06's constructive lower-bound route, and did not treat NM13-13's interpolation candidate as an independently validated external endpoint.

Consumed repository state included:

- current `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md` exclusion registry;
- the canonical scoped claim above;
- the preserved pre-refocus HARD7-06 handoff `runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md`, which retains the actual F0095/binary-cascade 3-colourability work instead of relabeling it as 3-SAT work;
- own preceding report `runs/prob10_2026-09-20/PROB10-04/2026-09-20T09-28-00Z__entropy_stabilized_inner_rescue.md`, which reduced the remaining obstruction to the outer copy masses `(u,v,w)` after paying arbitrary inner `(Q,B,E)` drift;
- neighboring upper-bound report `proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T09-07-39Z__t04_three_node_gaussian_tail_438890.md`, blob `7f16e752b0aaaaf07bb66097bdeca53598c82a02`, status `OPEN / PARTIAL; CANDIDATE_FULL ... pending later independent review`, with project candidate `4.38890`;
- neighboring constructive report `proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T11-28-00__t04_hidden_split_adjoint_compiler.md`, blob `378698a2afa312d3cc04b416aa77aed0293fa47e`, status `OPEN / PARTIAL`.

The new mathematical route and exact missing lemma were frozen **before code** in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T09-45-00Z__outer_covariance_compensation_idea_before_code.md`

at creation commit `313902293b2052a9b2f111ce1ea796a420081182`.

The complete analytic derivation is frozen in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T09-57-00Z__outer_covariance_compensation_theorem.md`

at creation commit `dda036e19c011856bb99a590cd67ec4de2fa680e`.

The diagnostic code/output are

- `artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T09-50-00Z__outer_covariance_hessian_diagnostic.py`, creation commit `2f984fda0c9f0241b755379bfaabf1787200fe58`;
- `artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T09-50-00Z__outer_covariance_hessian_diagnostic.out`, creation commit `e3c934c0d6adb1f06e199669210e76427ed5a9b0`.

## 2. Fresh source/model check

The exact target is unchanged: `m=floor(alpha n)` independent clauses; each clause chooses three distinct variables uniformly and then independent fair signs.

A bounded fresh source check on 20 September 2026 found no externally published replacement for the explicit `[3.52,4.4898]` bracket used by this track:

- Hajiaghayi--Sorkin, <https://arxiv.org/abs/math/0310193>, prove satisfiability with high probability below `3.52` in the classical independent model.
- Díaz--Kirousis--Mitsche--Pérez-Giménez, <https://doi.org/10.4230/LIPIcs.FSTTCS.2008.1750>, prove the `4.4898` asymptotic unsatisfiability upper bound.
- Carenini, ECCC TR26-145, publication 16 August 2026, <https://eccc.weizmann.ac.il/report/2026/145/>, proves an `O(n/log n)` scaling window for every fixed `k>=3`; that is a sharp-window result, not identification or convergence of an exact `alpha_3`.
- Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, published online in 2026 in *Combinatorics, Probability and Computing*, still describes the exact satisfiability threshold as known for `k=2` and sufficiently large `k`, not for `k=3`.
- Ding--Sly--Sun, <https://arxiv.org/abs/1411.0650>, is explicitly a sufficiently-large-`k` theorem and is not specialized here to `k=3`.
- ESA 2025, <https://doi.org/10.4230/LIPIcs.ESA.2025.103>, explicitly changes the independent-clause assumption to `k`-wise independent clause distributions, so its results are not substituted for the present model.

This is a bounded status check, not a claim of exhaustive worldwide priority.

## 3. Inherited obstruction from run 10

Run 10 proved, for each fixed copy macrostate

\[
y=(u,v,w)=(\ell_{ps},\ell_{ns1},\ell_{ns2}),
\]

that arbitrary rescue-aggregate drift `(Q,B,E)` can be charged by exact KL/Pinsker terms plus a fractional-knapsack rescue envelope.  Thus the rescue aggregates can no longer collapse for free.  What remained was the source's wrong-curvature copy block in `y`.

Let `V(y)` and `C(y)` be the maximum variable-side and clause-side entropy terms at fixed `y`, and let

\[
\Phi(y)=K(y)+V(y)+C(y)+\mathrm{const},
\]

where

\[
K=u\log u+(\lambda_p-u)\log(\lambda_p-u)
+v\log v+w\log w+(\lambda_n-v-w)\log(\lambda_n-v-w).
\]

The copy term is convex.  The question is whether the two optimized entropy sides supply enough negative curvature to compensate it.

## 4. Attack 1 — a global KL shortcut is too strong

I first tried to eliminate the outer problem globally by proving that the variable-side KL remainder dominates the copy Bregman divergence.  A simple high-degree block shows why this cannot be a universal coefficient-one argument.

Take a block of mass `d_0` with two states `0` and `D e_1`, Gibbs true probability `p`, and perturb `p` to `p+epsilon`.  Its state relative entropy is

\[
d_0D_{KL}(\operatorname{Ber}(p+\epsilon)\|\operatorname{Ber}(p))
=\frac{d_0\epsilon^2}{2p(1-p)}+O(\epsilon^3).
\]

The induced positive-copy mass changes by `D d_0 epsilon`; even the `u log u` part of the copy Bregman cost is

\[
\frac{D d_0\epsilon^2}{2p}+O(\epsilon^3).
\]

The ratio tends to `D(1-p)`, which can be greater than one.  Thus a coherent high-degree state can move many copies while paying state KL only once.  This refutes the naive **one-side** global data-processing shortcut.  It does not rule out a more sophisticated joint variable-plus-clause inequality.

The failure suggests using both incidence sides through their covariance matrices rather than another scalar KL floor.

## 5. Attack 2 — exact covariance-compensation Hessian

For variable natural parameters

\[
\theta=(\log\nu_{ps},\log\nu_{ns1},\log\nu_{ns2}),
\]

define the log-partition

\[
A_V(\theta)=h_{ps}\theta_{ps}
+h_{ns}\log(e^{\theta_{ns1}}+e^{\theta_{ns2}})
+\sum_{(i,j)\in L}\widehat\delta_{ij}\log\Psi_{ij}(e^\theta),
\]

with

\[
\Psi_{ij}=\nu_{ps}^i+(\nu_{ns1}+\nu_{ns2})^j-\nu_{ns2}^j.
\]

Its gradient is the Gibbs mean copy vector and its Hessian is the weighted covariance matrix `Sigma_V` of `(ps,ns1,ns2)`.  Similarly, summing the four clause log-partitions gives `A_C(phi)` with Hessian `Sigma_C`.

The conditional maximum-entropy values are Legendre transforms

\[
V(y)=A_V(\theta)-\theta\cdot y+\mathrm{const},
\qquad
C(y)=A_C(\phi)-\phi\cdot y+\mathrm{const},
\]

at `nabla A_V=y=nabla A_C`.  Differentiation gives the exact theorem

\[
\boxed{
\nabla^2V(y)=-\Sigma_V(y)^{-1},
\qquad
\nabla^2C(y)=-\Sigma_C(y)^{-1}.}
\]

Therefore

\[
\boxed{
\nabla^2\Phi(y)=
H_{copy}(y)-\Sigma_V(y)^{-1}-\Sigma_C(y)^{-1},}
\tag{5.1}
\]

where

\[
H_{copy}=\begin{pmatrix}
 u^{-1}+(\lambda_p-u)^{-1}&0&0\\
 0&v^{-1}+(\lambda_n-v-w)^{-1}&(\lambda_n-v-w)^{-1}\\
 0&(\lambda_n-v-w)^{-1}&w^{-1}+(\lambda_n-v-w)^{-1}
\end{pmatrix}.
\tag{5.2}
\]

The complete proof, including the finite Gibbs state spaces and nonsingularity hypothesis, is in the theorem artifact.

### Consequence for the rescue route

If at the true interior saddle `y_*`

\[
\Sigma_V^{-1}+\Sigma_C^{-1}-H_{copy}\succeq\kappa I
\]

for some `kappa>0`, continuity gives a neighborhood on which the unrescued exponent falls quadratically from `y_*`.  Run 10's minimized rescue penalty is also continuous and strictly positive at an interior Gibbs point.  Hence an interval certificate for this matrix inequality would settle the **local** outer problem completely: the rescued exponent would be uniformly below the original saddle value throughout a whole neighborhood.  Only a global annulus/boundary certificate would remain.

This is the main mathematical reduction of the run.

## 6. Attack 3 — exact support functions for the global annulus

The same source constraints give a clean projected-polytope description.

For a light degree `(i,j)`, its outer copy state lies in

\[
\operatorname{conv}\bigl(\{(i,0,0)\}\cup\{(0,k,j-k):1\le k\le j\}\bigr).
\]

Thus the variable projection is a Minkowski sum of these small polytopes, plus the heavy-positive point and heavy-negative segment.  For a direction `xi=(a,b,c)`, its exact support function is

\[
\boxed{
h_V(\xi)=a h_{ps}+h_{ns}\max\{b,c\}
+\sum_{ij}\widehat\delta_{ij}\max\{ai,m_j(b,c)\},}
\tag{6.1}
\]

with the closed-form false-state support

\[
\boxed{
m_j(b,c)=
\begin{cases}
bj,&b\ge c,\\
b+(j-1)c,&b<c.
\end{cases}}
\tag{6.2}
\]

because `bk+c(j-k)` is affine in `k`.

On the clause side,

\[
\boxed{
h_C(\xi)=\sum_{r=0}^3\widehat\gamma_r
\max_{\alpha:p(\alpha)=r}
\{a\,ps(\alpha)+b\,ns1(\alpha)+c\,ns2(\alpha)\}.}
\tag{6.3}
\]

There are only sixteen admissible extended clause types.  Every feasible outer point must satisfy all support inequalities from both projected polytopes.  These formulas give exact separation oracles for a future branch-and-bound/interval proof and eliminate the need to solve a generic inner LP at every outer box.

## 7. Actual executed diagnostic, clearly separated from theorem claims

Only after freezing the idea and proving the identities did I execute the matching checker.

At `alpha=4.4898`, `M=23`, it solved the six source stationarity equations in log multipliers, starting from the decimals printed by Díaz et al.  The result was

\[
\nu\approx(1.278201778245619,
0.3327728049379551,
0.9533692701180739),
\]

\[
\mu\approx(1.997279589033755,
0.4502935808272316,
0.3379403003525446),
\]

with floating residual infinity norm `1.77635683940025e-15`.  The corresponding copy point is

\[
y\approx(5.856667999143172,
0.5364470108663389,
1.153411776660164).
\]

The numerical matrix (5.1) has eigenvalues

\[
\boxed{-9.121055045516814,
-1.770536639601354,
-0.0744742571776404.}
\]

The leading principal minors of `-H_out` are

\[
1.432599417995044,
\quad3.351897666914776,
\quad1.202696855155688.
\]

So the computed stationary point is strongly locally concave with diagnostic margin about

\[
\boxed{0.07447425718}.
\]

This number is **not interval certified** and does not change `alpha_U`.

The exact finite part of the checker compared (6.2) against explicit enumeration for every light block `1<=j<=i<=23` and all `124` nonzero directions in `{-2,-1,0,1,2}^3`.  All

\[
124\times276=34,224
\]

integer comparisons passed.  The program also enumerated the sixteen admissible extended clause types.  Output ends with

`EXACT_SUPPORT_BLOCK_CHECKS_PASS = True`

and

`NUMERICAL_NEGATIVE_DEFINITE_AT_SOLVED_SADDLE = True`.

The latter is intentionally labelled numerical.

## 8. Before / after ledger

**Source metric:**

\[
W_{source}:0.9698\longrightarrow0.9698
\qquad\text{(no movement).}
\]

**Mechanism progress, kept separate:**

- before: the remaining `(u,v,w)` outer problem had no analytic curvature certificate and inherited the source's projected grid search;
- after: exact Hessian identity (5.1), exact variable/clause support oracles (6.1)--(6.3), and a solved-saddle diagnostic with local curvature margin `0.07447425718`;
- exact support-block validations: `0 -> 34,224` passed comparisons, but this is validation of the oracle formula, not a threshold improvement.

The neighboring `4.38890` interpolation endpoint remains **CANDIDATE_FULL pending independent review** and is not promoted into this track's external source metric.

## 9. Full-scope gap and next nonduplicating attack

The exact missing source-level lemma is now:

\[
\boxed{
\text{certify a neighborhood }N\text{ with }
\Sigma_V^{-1}+\Sigma_C^{-1}-H_{copy}\succeq\kappa I,
\text{ and certify }\sup_{y\in\mathcal P\setminus N}\Phi(y)
\le\Phi(y_*)-\eta
}
\]

for explicit `kappa,eta>0`, where `mathcal P` is the intersection of the two projected feasibility polytopes.  The first part should use interval Newton plus interval covariance bounds around the six solved multipliers.  The second should use the new support-function separators and rigorous Taylor/Bernstein upper bounds on outer boxes rather than another blind `100^3` mesh.  Only after both pieces are certified should this route lower `alpha` below `4.4898` and recompute the full first-moment/rescue calculation.

The exact current blockers are therefore **interval localization** and **global annulus separation**.  The rescue aggregate collapse and the absence of an outer feasibility oracle are no longer blockers.

No scheduler state, email, Drive, public repository, permissions, or other track files were modified.