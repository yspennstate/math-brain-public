Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 run 10 — entropy-stabilized rescue pays the full inner `(Q,B,E)` reoptimization

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN**.

**SOURCE-METRIC NO MOVEMENT.**  For the exact owner-frozen iid proper-clause model, the directly verified published explicit-decimal bracket remains

\[
[\alpha_L,\alpha_U]=[3.52,4.4898],
\qquad W=0.9698\longrightarrow0.9698.
\]

This run makes the required method change rather than building another local rescue motif.  The main result is a theorem that charges any attempt to move the three rescue aggregates `Q` (safe `ps` mass), `B` (canonical blocker mass), or `E` (eligible `j=1` leaf mass) away from their Gibbs values by an explicit relative-entropy penalty.  Combined with an exact fractional-knapsack envelope for the weighted center mass, this pays **all inner `(Q,B,E)` reoptimization at each fixed copy macrostate `(u,v,w)`**.  The remaining source obstruction is now the outer three-dimensional copy-mass optimization, not aggregate collapse.

The three materially different approaches tried were:

1. **deterministic clause-capacity floors** — succeeds for `Q` and gives an exact lower bound, but a positive global feasibility floor for `B` is false;
2. **KL/Pinsker entropy stabilization plus a fractional-knapsack rescue envelope** — succeeds and is the main theorem of the run;
3. **a pure copy-conservation floor for `E`** — fails because the resulting lower bound can be zero in the relevant parameter region, so `E` also has to be stabilized entropically.

No finite SAT/UNSAT instance, simulation, or physics decimal is used as source progress.

## 1. Continuity, ownership, and evidence consumed

I continued only the scoped **cluster-aware weighted-counting / overlap-variational** claim in

- `operations/claims/PROB10-04.md`, blob `1095e6bfb106b53e810af56f2605521abb7143b4`.

I did not override the historical `F0097` parent claim, did not take over NM13-13's interpolation route, and did not duplicate NM13-06's constructive route.

Consumed repository state included:

- `operations/PROB10_2026-09-20.md` on current `master`;
- current root `POSTED.md` exclusion registry;
- the canonical scoped claim above;
- the preserved pre-refocus HARD7-06 handoff
  `runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md`, which retains the actual F0095/binary-cascade 3-colourability history rather than relabeling it as 3-SAT work;
- own immediately preceding report
  `runs/prob10_2026-09-20/PROB10-04/2026-09-20T08-10-00Z__six_scalar_conditional_rescue_dual.md`
  @ `69322d0a6f5943a1b9ed2176e3c32fbb96f25caa`;
- the latest upper-bound neighbor at the time of this run,
  NM13-13 commit `33899732d86721418e88ec0ba92cdbdb042ad3c1`, which reports **CANDIDATE_FULL pending independent review** at `4.38900`; this track does not audit or promote it to the external metric;
- the latest constructive neighbor at the time of this run,
  NM13-06 commit `2775266b099bf53f5a36cbe962d9ca4a2222e12f`, which develops the distinct hidden-split/adjoint lower-bound compiler and remains OPEN/PARTIAL.

The new mathematical idea was frozen **before code** in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T08-45-00Z__entropy_stabilized_rescue_idea_before_code.md`

at creation commit `a3e0659697552ce8131bd355cd75dd209ec2a3e3`.

The complete theorem/proof is frozen separately in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T09-15-00Z__entropy_stabilized_rescue_theorem.md`

at creation commit `24b5f72076922417d95602b0d410b713572a0681`.

## 2. Current source status, freshly checked

The exact target remains the owner's standard model: `m=floor(alpha n)` independent clauses, each clause choosing three distinct variables uniformly and then three independent fair signs.

The bounded fresh source check supports the same conservative baseline:

- Hajiaghayi--Sorkin, <https://arxiv.org/abs/math/0310193>, prove satisfiability with high probability below `3.52` in the standard independent proper-clause model.
- Díaz--Kirousis--Mitsche--Pérez-Giménez, <https://arxiv.org/abs/0807.3600> and DOI `10.4230/LIPIcs.FSTTCS.2008.1750`, prove asymptotic unsatisfiability at `4.4898`.
- Gaia Carenini, ECCC TR26-145, publication date 16 August 2026, <https://eccc.weizmann.ac.il/report/2026/145/>, proves an `O(n/log n)` scaling window for every fixed `k>=3`; this does not identify or prove convergence to a limiting `alpha_3`.
- Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, published online 27 March 2026 in *Combinatorics, Probability and Computing*, still states that for `3<=k<k_0` even existence of a uniform satisfiability threshold remains open.  Ding--Sly--Sun is therefore not specialized to `k=3`.
- ESA 2025 studies a different `k`-wise-independent clause model and is not substituted for the classical iid-clause target.

The search did not find a newer published explicit-decimal theorem replacing either `3.52` or `4.4898`.  This is a bounded current-status check, not a worldwide novelty certificate.

## 3. Exact obstruction inherited from run 9

Run 9 proved a correct conditional rescue dual after fixing

\[
(u,v,w,q,\beta,e)
=(\ell_{ps},\ell_{ns1},\ell_{ns2},Q/u,B/N,E/v),
\qquad N=\lambda_n-v-w.
\]

The inherited iid-priority one-rescue factor is

\[
R(x)=\prod_{i=1}^{M}
\left(1-\frac12\frac BN\left(\frac Qu\right)^i\frac Ev\right)^{t_{i,1}}.
\tag{3.1}
\]

The simple outer relaxation allowed `q=0`, `beta=0`, or `e=0`, making (3.1) equal to one.  Trying to fix this only by feasibility is impossible.  In particular, the clause-type polytope admits configurations with positive blocker mass `v` but `B=0`: every negative-singleton blocker can place both unsatisfied literals in `pu` slots.  Hence no globally positive deterministic floor for `B` exists.

The correct way to stop this escape is therefore **variational rather than combinatorial**: moving `B`, `Q`, or `E` far from their natural Gibbs values must lose entropy.

## 4. Attack 1 — deterministic clause geometry: useful but insufficient

Let `gamma_b=sum_k hat_gamma_k` be the core clause density.  The number of singleton positive-satisfied clauses is exactly `u-Q`; the number of singleton negative-satisfied clauses is `v`.  The remaining

\[
R=\gamma_b-(u-Q)-v
\]

clauses have two or three satisfied literals, and their satisfied-copy count is `Q+w`.  Therefore

\[
Q+w\le3R,
\]

so every feasible type obeys

\[
\boxed{
Q\ge\frac{[3u+3v+w-3\gamma_b]_+}{2}.
}
\tag{4.1}
\]

At the rounded source copy macrostate this is

\[
Q\ge3.4560642027\ldots,
\qquad Q/u\ge0.5901075801\ldots.
\]

This is a genuine exact structural constraint and will help the eventual outer interval calculation.  But it does not solve the run-9 obstruction because `B` can still be zero.

## 5. Attack 2 — main theorem: exact KL remainders stabilize `Q,B,E`

Fix a copy macrostate `(u,v,w)` and arbitrary positive Díaz multipliers `nu,mu`.  Let `D_0(u,v,w;nu,mu)` be the ordinary **unrescued** conditional Díaz dual.  Because the copy masses are fixed, the convex copy-count term is constant, so the wrong-curvature obstruction from run 9 disappears.

For the `j=1` variable blocks put

\[
\delta_i=\widehat\delta_{i,1},\qquad
D_1=\sum_i\delta_i,
\]

and let the unrescued Gibbs false probability be

\[
p_i^*=\frac{\nu_{ns1}}{\nu_{ps}^i+\nu_{ns1}},
\qquad
E_*=\sum_i\delta_i p_i^*.
\tag{5.1}
\]

For clause type `alpha=(ps,ns,pu,nu)` define

\[
b(\alpha)=\mathbf1\{ps=0,ns=1,nu\ge1\},
\qquad
q(\alpha)=ps\,\mathbf1\{ps+ns\ge2\}.
\tag{5.2}
\]

Let `B_*` and `Q_*` be their expectations under the unrescued clause Gibbs law induced by `mu` within each fixed syntactic class.  Exact enumeration of the 16 admissible extended 3-clause types gives the within-class range vectors

\[
\operatorname{range}_k b=(1,1,0,0),
\qquad
\operatorname{range}_k q=(0,1,2,3).
\tag{5.3}
\]

Therefore define

\[
G_B=\widehat\gamma_0+\widehat\gamma_1,
\qquad
G_Q=\widehat\gamma_1+4\widehat\gamma_2+9\widehat\gamma_3.
\tag{5.4}
\]

The source log-sum inequalities have exact KL remainders.  Pinsker plus Cauchy gives

\[
K_{var}\ge\boxed{\frac{2(E-E_*)^2}{D_1}},
\tag{5.5}
\]

and, by splitting the clause KL remainder into two halves,

\[
K_{clause}\ge
\boxed{
\frac{(B-B_*)^2}{G_B}
+\frac{(Q-Q_*)^2}{G_Q}}.
\tag{5.6}
\]

These are theorem inequalities, not numerical fits.

### 5.1 Exact fractional-knapsack center envelope

For `0<=s<=1` and `0<=E<=D_1`, define

\[
A_{min}(s,E)=
\min\left\{\sum_i(\delta_i-f_i)s^i:
0\le f_i\le\delta_i,\ \sum_i f_i=E\right\}.
\tag{5.7}
\]

Since `s^i` decreases with `i`, minimizing the true-center weight is equivalent to maximizing the removed false-center weight, and the exact greedy optimum fills `f_1,f_2,...` in increasing degree order.  If `r` is determined by

\[
\sum_{i<r}\delta_i\le E\le\sum_{i\le r}\delta_i,
\]

then

\[
\boxed{
A_{min}(s,E)=
\sum_{i>r}\delta_i s^i
+\left(\delta_r-E+\sum_{i<r}\delta_i\right)s^r.
}
\tag{5.8}
\]

This is nondecreasing in `s` and nonincreasing in `E`.

### 5.2 Entropy-stabilized rescue theorem

Using `log(1-x)<=-x` in (3.1) and (5.7),

\[
\log R(x)
\le-\frac{BE}{2Nv}
A_{min}\!\left(\frac Qu,E\right).
\tag{5.9}
\]

Combining (5.5), (5.6), and (5.9) with the exact KL-remainder form of the source dual yields the new theorem

\[
\boxed{
\log F_R(x)
\le D_0(u,v,w;\nu,\mu)-\mathcal P(Q,B,E),
}
\tag{5.10}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal P(Q,B,E)=\;&
\frac{2(E-E_*)^2}{D_1}
+\frac{(B-B_*)^2}{G_B}
+\frac{(Q-Q_*)^2}{G_Q}\\
&+\frac{BE}{2Nv}
A_{min}\!\left(\frac Qu,E\right).
\end{aligned}}
\tag{5.11}
\]

The complete proof, including boundary conventions and the exact range enumeration argument, is in the theorem artifact cited in section 1.

This is stronger than run 9's simple six-scalar relaxation in the precise sense needed here: if `B_*,Q_*>0` and `0<E_*<D_1`, then on the compact feasible `(B,Q,E)` box

\[
\boxed{\inf_{Q,B,E}\mathcal P(Q,B,E)>0.}
\tag{5.12}
\]

The three quadratic terms vanish simultaneously only at the Gibbs point `(B_*,Q_*,E_*)`, where the rescue term is strictly positive.  Thus aggregate collapse has a nonzero entropy price.

### 5.3 A directly certifiable four-case bound

Choose radii `r_B,r_Q,r_E`.  If one aggregate leaves its relative neighborhood of the Gibbs value, a quadratic term pays.  If all remain inside, monotonicity of `A_min` pays the rescue term.  Explicitly,

\[
\inf\mathcal P\ge
\min\left\{
\frac{r_B^2B_*^2}{G_B},
\frac{r_Q^2Q_*^2}{G_Q},
\frac{2r_E^2E_*^2}{D_1},
L_R
\right\},
\tag{5.13}
\]

with

\[
L_R=
\frac{(1-r_B)B_*(1-r_E)E_*}{2Nv}
A_{min}\!\left(\frac{(1-r_Q)Q_*}{u},(1+r_E)E_*\right).
\tag{5.14}
\]

This is the form intended for a future outward-interval proof over the remaining three copy variables.

## 6. Attack 3 — forcing `E` by conservation alone fails

A coarse conservation bound can only say

\[
E\ge
\left[v-h_{ns}-\sum_{i,j\ge2}j\widehat\delta_{i,j}\right]_+,
\tag{6.1}
\]

because all `ns1` mass not in `j=1` false leaves may be absorbed by heavy negative copies and `j>=2` false-variable classes.  The right side can be zero in the relevant region.  More elaborate positive-copy budget relaxations have the same issue unless they retain essentially the full degree split.

Thus the variable KL charge (5.5), not another deterministic floor, is the clean mechanism that keeps `E` near its natural value.

## 7. Actual executed diagnostic — inner reoptimization at the rounded source macrostate

Only after proving the theorem did I run one diagnostic at the rounded source saddle.  The matching script is

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T09-08-00Z__entropy_stabilized_rescue_diagnostic.py`

creation commit `50f91a65545dcf6070b9aa9da3ecbababa33e904`, with archived stdout

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T09-08-30Z__entropy_stabilized_rescue_diagnostic.out`

creation commit `a9ed0db1284bef1c55372c76a3cfe8b7e996eaf6`.

The 16-clause-type range vectors in (5.3) are checked by exact integer enumeration.  The remaining values are high-precision evaluations from the rounded source multipliers and are explicitly **not** outward intervals.

For

\[
r_B=0.0016,\qquad r_Q=0.0006,\qquad r_E=0.05,
\]

the four terms in (5.13) evaluate to

\[
3.51250669925\times10^{-7},\quad
3.82723938403\times10^{-7},\quad
3.85766616189\times10^{-7},\quad
2.94688866148\times10^{-7}.
\]

Hence the rounded surrogate has the uniform inner defect

\[
\boxed{\inf_{Q,B,E}\mathcal P\ge2.94688866148\times10^{-7}.}
\tag{7.1}
\]

This is about `84.20` times the Díaz paper's printed rounded final log margin and about `83.89%` of run 8's fixed-outer scalarized rescue correction.  Unlike the old fixed-saddle evaluation, (7.1) has paid **arbitrary inner reallocation of all three rescue aggregates** at that fixed copy macrostate.

Again, (7.1) is a rounded-multiplier diagnostic, not a new asymptotic threshold endpoint.  The output ends

`ROUNDED_DIAGNOSTIC_CHECKS_PASS = True`.

## 8. Before/after metrics

Source metric:

\[
W_{source}:0.9698\longrightarrow0.9698
\quad\text{(no movement).}
\]

Separate mechanism metric:

- before: run 9 reduced the raw `M=23` count to six adversarial outer scalars `(u,v,w,q,beta,e)` but the simple relaxation allowed zero-cost rescue collapse;
- after: the present theorem gives a strictly positive explicit defect after **fully optimizing `(Q,B,E)` at fixed `(u,v,w)`**, leaving only the three copy masses as genuine outer variables for the next certificate.

At the rounded source macrostate, the certified-formula diagnostic defect is `2.94688866148e-7`; this number is auxiliary and not part of `W_source`.

## 9. Unresolved full-scope gap and next method

The remaining source obligation is now precise:

\[
\boxed{
\sup_{(u,v,w)\in\mathcal C}
\inf_{\nu,\mu}
\left[D_0(u,v,w;\nu,\mu)-\inf_{Q,B,E}\mathcal P(Q,B,E)\right]
< -\log B_{source}-\log(1+10^{-7})
}
\]

at some density `alpha<4.4898`, with the source heavy/light truncation and simple-formula transfer retained.  Here `mathcal C` is the source three-dimensional copy-count polytope.

This run does **not** claim that inequality.  What it proves is that the feared inner aggregate escape is no longer the obstruction.  A next bounded run should change from inner combinatorics to a genuine **outer interval branch-and-bound in `(u,v,w)`**, using boxwise multiplier choices, (4.1), and the explicit defect (5.13).  If that outer optimization cannot beat `4.4898`, the report should isolate which copy direction absorbs the `~10^-7` rescue gain rather than returning to another local motif.

Status remains **PARTIAL / source OPEN**.