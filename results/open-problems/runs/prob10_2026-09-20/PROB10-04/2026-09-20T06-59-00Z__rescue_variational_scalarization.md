Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 run 8 — scalarizing the rescue correction and reducing the ranked correction to one-dimensional Bellman states

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN**.

**SOURCE-METRIC NO MOVEMENT.** For the exact owner-frozen model, the externally published explicit-decimal bracket remains

\[
[\alpha_L,\alpha_U]=[3.52,4.4898],\qquad W=0.9698\to0.9698.
\]

This run changes method rather than adding another local rescue motif.  The main new result is an exact variational reduction: the already-proved iid-priority one-rescue correction no longer requires optimizing the full `M=23` vector of `j=1` degree splits.  Conditional on the outer Díaz macrostate, its corrected degree-split optimization reduces to **one scalar false-leaf mass `e` plus one monotone scalar multiplier `z(e)`**.  The stronger class-ranked correction also admits an exact **one-dimensional tail-state Bellman recursion**.  These are mechanism advances, not a threshold endpoint.

At the rounded Díaz outer saddle, exact high-precision evaluation of the scalar reduction gives

\[
\Delta_{\rm inner}=3.5129045422595363\times10^{-7},
\]

retaining `0.9998839968368874` of the unreoptimized iid-priority penalty and about `100.3684` times the source's printed rounded log margin.  This is deliberately labeled **fixed-outer diagnostic only**: the outer clause/slot macrostate has not yet been interval-reoptimized, so `4.4898` is not changed here.

## 1. Continuity, ownership, and evidence consumed

This run continues only the scoped cluster-aware weighted-counting / overlap-variational route in

- `operations/claims/PROB10-04.md`, blob `1095e6bfb106b53e810af56f2605521abb7143b4`.

It does not take over the NM13-13 interpolation route or NM13-06 constructive route.

Consumed repository state:

- `operations/PROB10_2026-09-20.md` on current `master`;
- current root `POSTED.md` exclusion registry;
- root `RESULTS.md` current compact ledger, while recovering newer target-specific reports rather than substituting its older retained values;
- actual pre-refocus HARD7-06 handoff `runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md`, blob `e59380417dc476970e22b72b66c59ffbffa4af3a`, preserving the real F0095 / binary-cascade 3-colourability target and its `W_3<=0.6565076260769` progress as a separate history;
- own preceding substantive report `runs/prob10_2026-09-20/PROB10-04/2026-09-20T05-55-00Z__priority_weighted_rescue_compiler.md` @ commit `ca48292f8b51332b63068172b7ca7b1f422a7259`;
- newest interpolation-neighbor report `proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T06-23-41Z__t04_logconvex_moment_tail_43906.md` @ claim commit `951d31a5a028f53568ed04cdae3fd6539394be48`; it records a **CANDIDATE_FULL, pending independent review** endpoint `4.3906`.  I do not promote that project candidate into this worker's externally verified source metric;
- newest constructive-neighbor report `proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T09-28-00__t04_closed_four_spectrum_drift_and_barrier_policy.md`, which closes a four-spectrum unit-cascade drift calculation but explicitly leaves the external bracket unchanged.  That lower-bound route is not duplicated here.

The mathematical idea for this run was written before code at

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T06-51-00Z__iid_priority_scalarization_idea_before_code.md`

creation commit `a2d24ac1779e1b6eb27094af14b8fdb252f8635e`.

## 2. Source model and bounded current-status recheck

The owner-frozen model is `m=floor(alpha n)` iid clauses; each clause chooses three distinct variables uniformly and then three independent fair signs.

The externally published explicit endpoints remain supported by:

1. Hajiaghayi--Sorkin, *The Satisfiability Threshold of Random 3-SAT Is at Least 3.52*, <https://arxiv.org/abs/math/0310193>.  Their standard model is iid proper clauses with replacement and they prove w.h.p. satisfiability below `3.52`.
2. Díaz--Kirousis--Mitsche--Pérez-Giménez, *A new upper bound for 3-SAT*, <https://arxiv.org/abs/0807.3600>, prove a.a.s. unsatisfiability at `4.4898` in the simple proper-clause model used by their count.
3. Carenini, *The Scaling Window of Random k-SAT*, ECCC TR26-145, posted 16 August 2026, <https://eccc.weizmann.ac.il/report/2026/145/>, proves an `O(n/log n)` scaling-window upper bound for every fixed `k>=3`.  This sharpens window width but does **not** prove convergence of the threshold centers or identify `alpha_3`.
4. Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, published online 27 March 2026, <https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/random-textitksat-gibbs-uniqueness-threshold-revisited/6EF42EB37F15370DB593F0F02E3538E9>, still treats fixed small `k` as outside the exactly identified satisfiability-threshold regime.  Physics/1RSB numerical values are not substituted for a certified endpoint.
5. Ding--Sly--Sun <https://arxiv.org/abs/1411.0650> is a sufficiently-large-`k` theorem, not automatically a `k=3` theorem.  The ESA 2025 `k`-wise-independent model is also different from the present iid-clause target.

A small model-transfer point is worth making explicit.  Let

\[
N_n=8\binom n3
\]

be the number of proper signed 3-clauses and `m=floor(alpha n)`.  In the iid-with-replacement model,

\[
\Pr(\hbox{some repeated clause})
\le {m\choose2}/N_n=O(n^{-1}).
\]

Conditioned on no repetition, the ordered clause list is uniform over ordered distinct clauses, hence induces the simple model.  Therefore an a.a.s. UNSAT theorem for the simple model transfers to the owner-frozen iid model with only `o(1)` loss.  Thus using `4.4898` as the external upper endpoint is source-valid.

The bounded search in this run did not find a newer published theorem replacing either explicit decimal endpoint.  This is not a worldwide novelty certificate.

## 3. Exact obstruction inherited from run 7

Run 7 proved the class-ranked one-rescue survival factor.  In asymptotic density notation, for `j=1` true centers of positive degree `i`, let

- `t_i=t_{i,1}`;
- `f_i=f_{i,1,1}` be false degree-`(i,1)` leaves;
- `E=\sum_i f_i`;
- `P=ell_ps`, `L=ell_ns1`, `U=ell_nu` be the corresponding slot densities;
- `Q` be the multiply-satisfied safe `ps` density;
- `B_can` be the canonical blocker `nu` density;
- `q=Q/P`, `beta=B_can/U`.

The strongest ranked correction uses

\[
h_i={\sum_{k>i}f_k+f_i/2\over L}
\]

and contributes

\[
\prod_i(1-\beta q^i h_i)^{t_i n+o(n)}.
\]

Its local rounded-saddle penalty is strongest, but `h_i` couples all 23 degree classes.  The missing step was no longer another rescue lemma; it was a global reoptimization that could absorb that coupling without losing rigor.

## 4. Three materially different attacks tried

### Attack A — keep the full ranked correction, change variables to cumulative tails

Instead of optimizing the 23-vector directly, put

\[
S_i=\sum_{k\ge i}f_k,\qquad S_{M+1}=0.
\]

Then `f_i=S_i-S_{i+1}` and

\[
h_i={S_i+S_{i+1}\over2L}.
\]

This makes the objective nearest-neighbor in the tail states `(S_i,S_{i+1})`.  Section 7 proves an exact Bellman recursion.  **Outcome: succeeds analytically.**  It retains the full ranked correction but still needs a rigorous continuous-state interval dynamic program inside each outer Díaz box.

### Attack B — iid priorities to scalarize the degree split

Use the weaker iid continuous-priority representative from run 7.  Each vertex-disjoint completed one-rescue pair beats the chosen representative with probability exactly `1/2`; the leaf pool is therefore center-class independent.  The correction becomes

\[
1-c_iE,\qquad c_i={\beta q^i\over2L}.
\]

Because all `f_i` enter this factor only through their sum `E`, conditioning on `E` restores a separable entropy maximization.  Section 6 proves that the entire 23-class split reduces exactly to one scalar `E` and one monotone scalar `z(E)`.

**Outcome: succeeds and is presently the cleanest full-certification route.**  At the rounded source outer saddle it retains `99.9884%` of the unreoptimized iid penalty after exact inner reoptimization.

### Attack C — linearize / rearrange the ranked kernel

Using `-log(1-x)>=x`, the ranked penalty has the rigorous linear lower bound

\[
{\beta\over L}\left(
\sum_{i<k}u_i f_k+{1\over2}\sum_i u_i f_i
\right),\qquad u_i=t_iq^i.
\]

Subtracting the iid half-pair value gives the exact identity

\[
\sum_{i<k}u_if_k+{1\over2}\sum_i u_if_i
-{1\over2}\Big(\sum_i u_i\Big)\Big(\sum_k f_k\Big)
={1\over2}\sum_{i<k}(u_if_k-u_kf_i).
\tag{4.1}
\]

Hence the ranked linear penalty dominates the iid linear penalty whenever `f_i/u_i` is nondecreasing.  At the unrescued source stationary split,

\[
{f_i\over t_iq^i}={\nu_{ns1}\over(\nu_{ps}q)^i},
\]

so a sufficient condition is `nu_ps q<=1`.  The rounded source saddle has

\[
\nu_{ps}q=0.956078232396056\ldots<1.
\]

For the reoptimized iid scalar diagnostic, the stronger adjacent-ratio test remains below `0.956103`.  **Outcome: useful conditional dominance criterion, but not yet a global theorem**, because `nu_ps q<=1` has not been interval-certified over every outer box relevant to the full Díaz maximum.  I therefore do not use (4.1) to claim a threshold gain.

## 5. Finite-to-asymptotic iid-priority penalty

The preceding finite theorem gives, for one exact integer coarse type,

\[
S_n\le\prod_{i=1}^M
\left(1-a_{i,n}\,\beta_n\,{E_n\over2L_n}\right)^{C_{i,n}},
\tag{5.1}
\]

where

\[
a_{i,n}={(Q_n)_i\over(P_n)_i},\quad
\beta_n={B_n\over U_n},
\]

`E_n` is the number of eligible `f_{k,1,1}` leaf copies, `L_n` the `ns1` pool, and `C_{i,n}` the `t_{i,1}` center count.

### Lemma 5.1 — exponential fixed-type limit

Fix `M`.  Along any interior coarse-type sequence with

\[
P_n/n\to P>0,\quad Q_n/n\to Q,\quad
U_n/n\to U>0,\quad B_n/n\to B_{can},\quad
L_n/n\to L>0,
\]

and

\[
E_n/n\to E,\qquad C_{i,n}/n\to t_i,
\]

(5.1) implies

\[
\limsup_{n\to\infty}{1\over n}\log S_n
\le
\sum_{i=1}^M t_i\log(1-c_iE),
\qquad
c_i={\beta q^i\over2L},
\tag{5.2}
\]

where `q=Q/P`, `beta=B_can/U`.

#### Proof

For fixed `i`,

\[
{(Q_n)_i\over(P_n)_i}
=\left({Q_n\over P_n}\right)^i
\prod_{r=0}^{i-1}
{1-r/Q_n\over1-r/P_n}
=q^i+o(1).
\]

Because `M` is fixed, the convergence is uniform over `1<=i<=M` on every compact interior box.  Also `beta_n->beta` and `E_n/L_n->E/L`.

Since eligible leaves form a subset of `ns1` copies, `0<=E_n/L_n<=1`; also `0<=beta_n,a_{i,n}<=1`.  Thus every factor in (5.1) lies in `[1/2,1]`, so `log` is uniformly Lipschitz on the relevant interval.  Divide the logarithm of (5.1) by `n`, pass to the limits, and sum over the fixed finite set `i<=M`.  This gives (5.2). QED.

This is the finite-to-continuum payment that was missing from a mere rounded finite sampling argument.

## 6. Main theorem — exact scalar reduction of the iid-priority corrected degree split

Fix an interior outer Díaz macrostate, so `q,beta,L` and the degree masses

\[
\delta_i=\widehat\delta_{i,1},\qquad 1\le i\le M,
\]

are fixed.  In the source `j=1` split write

\[
f_i=f_{i,1,1},\qquad t_i=\delta_i-f_i,\qquad E=\sum_i f_i.
\]

For fixed source multipliers define

\[
A_i=\nu_{ps}^i,\qquad B=\nu_{ns1},\qquad
c_i={\beta q^i\over2L},\qquad s_i(E)=1-c_iE.
\]

Because `E<=L` and `beta,q<=1`, one always has `s_i(E)>=1/2`.

Up to terms independent of the `j=1` true/false split, the source entropy plus the iid-priority correction is

\[
\mathcal G(f)=\sum_i\Big[
\delta_i\log\delta_i-t_i\log t_i-f_i\log f_i
+t_i\log A_i+f_i\log B+t_i\log s_i(E)
\Big].
\tag{6.1}
\]

### Theorem 6.1 — conditional one-scalar reduction

For a fixed value `0<E<sum_i delta_i`, let `z(E)>0` be the unique solution of

\[
E=\sum_i\delta_i\,{zB\over A_is_i(E)+zB}.
\tag{6.2}
\]

Then

\[
\boxed{
\max_{\substack{0\le f_i\le\delta_i\\\sum f_i=E}}
\mathcal G(f)
=
\Phi(E)
:=\sum_i\delta_i\log(A_is_i(E)+z(E)B)-E\log z(E).
}
\tag{6.3}
\]

The maximizing split is unique and equals

\[
\boxed{
f_i=\delta_i{zB\over A_is_i+zB},\qquad
 t_i=\delta_i{A_is_i\over A_is_i+zB}.}
\tag{6.4}
\]

Consequently the full corrected `M`-class degree-split maximum is exactly

\[
\max_{0\le E\le\sum_i\delta_i}\Phi(E),
\tag{6.5}
\]

not an `M`-dimensional optimization.

If the maximizer is interior, it also satisfies the two-scalar system

\[
E=\sum_i\delta_i{zB\over A_i(1-c_iE)+zB},
\tag{6.6}
\]

\[
\boxed{
\log z+\sum_i\delta_i{A_ic_i\over A_i(1-c_iE)+zB}=0.}
\tag{6.7}
\]

#### Proof

Fix `E`, so all `s_i(E)` are constants.  For arbitrary `z>0`, the log-sum inequality applied to the two weights `A_is_i` and `zB` gives

\[
\delta_i\log(A_is_i+zB)
\ge
\delta_i\log\delta_i-t_i\log t_i-f_i\log f_i
+t_i\log(A_is_i)+f_i\log(zB),
\]

with equality exactly when the normalized pair `(t_i,f_i)/delta_i` is proportional to `(A_is_i,zB)`.  Sum over `i` and use `sum f_i=E`.  Moving the term `E log z` to the other side yields

\[
\mathcal G(f)
\le
\sum_i\delta_i\log(A_is_i+zB)-E\log z.
\tag{6.8}
\]

For fixed `E`, the right-hand false mass in (6.2) is continuous and strictly increasing from `0` to `sum delta_i` as `z` runs from `0` to `infinity`; hence there is a unique `z(E)`.  Choosing it makes the equality conditions in every log-sum inequality compatible with `sum f_i=E`, proving (6.3)--(6.4).  Maximizing over `E` proves (6.5).

For an interior `E`, differentiate the envelope (6.3).  The `z'(E)` terms cancel because (6.2) is precisely the first-order condition in `z`.  Since `s_i'(E)=-c_i`,

\[
\Phi'(E)
=-\log z-\sum_i\delta_i{A_ic_i\over A_is_i+zB}.
\]

Setting this to zero gives (6.7). QED.

### Why this matters

The naive statement in the pre-code note that one merely replaces `Psi_{i,1}` by `A_i(1-c_iE)+B` was **too optimistic** because `E` itself is endogenous.  The theorem above pays the missing derivative correctly: the false-state weight acquires the single multiplier `z`.  Thus the corrected partition is

\[
\Psi^{\rm iid}_{i,1}=A_i(1-c_iE)+zB,
\]

with the two scalar equations (6.6)--(6.7).  No 23-class derivative system remains.

## 7. Stronger route — exact Bellman reduction for the full ranked correction

The class-ranked correction from run 7 is stronger than iid priorities.  It can also be reduced structurally.

Let

\[
S_i=\sum_{k\ge i}f_k,\qquad S_{M+1}=0,
\]

so `f_i=S_i-S_{i+1}` and

\[
h_i={S_i+S_{i+1}\over2L}.
\]

For `s>=r` with `0<=s-r<=delta_i`, put

\[
\begin{aligned}
g_i(s,r)=&\;\delta_i\log\delta_i
-(\delta_i-s+r)\log(\delta_i-s+r)
-(s-r)\log(s-r)\\
&+(\delta_i-s+r)\log A_i+(s-r)\log B\\
&+(\delta_i-s+r)
\log\left(1-\beta q^i{s+r\over2L}\right),
\end{aligned}
\tag{7.1}
\]

with the usual `0 log 0=0` convention.

Define backward value functions by `V_{M+1}(0)=0` and

\[
V_i(s)=
\max_{r:\;0\le s-r\le\delta_i}
\{g_i(s,r)+V_{i+1}(r)\},
\tag{7.2}
\]

where infeasible tail masses for classes `>i` are assigned `-infinity`.

### Proposition 7.1 — ranked Bellman identity

The maximum of the entire ranked-corrected `j=1` degree-split objective is exactly

\[
\boxed{\max_s V_1(s).}
\tag{7.3}
\]

#### Proof

The map `f_1,...,f_M <-> S_1,...,S_M` is bijective under `S_{M+1}=0`, with `f_i=S_i-S_{i+1}`.  The source entropy term for class `i` depends only on `f_i`, while the ranked rescue term for class `i` depends on `f_i` and the higher-degree tail only through

\[
h_i=(S_i+S_{i+1})/(2L).
\]

Therefore the total objective is exactly `sum_i g_i(S_i,S_{i+1})`.  The principle of optimality applied backward over the chain gives (7.2), and maximizing the initial tail mass gives (7.3). QED.

This keeps the full ranked correction and replaces a generic 23-dimensional search by 23 sequential one-dimensional state transitions.  It is not yet an interval certificate: the next step must control continuous-state interpolation/branching error and then embed the Bellman result into the outer Díaz macrostate search.

## 8. Rounded fixed-outer diagnostic for the scalar theorem

After proving the reduction, I ran only one numerical diagnostic, using the source's rounded outer saddle inherited from the preceding report.  The script is

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T06-54-00Z__iid_priority_scalarization_diagnostic.py`

creation commit `5ce9a7e613d99c38406c0d312c50021f82f5cb97`.

Actual archived output is

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T06-54-30Z__iid_priority_scalarization_diagnostic.out`

creation commit `b7d096de588aba34db1cd1342a4f06c738b773bf`.

The decisive values are

\[
E_{source}=0.0011163237549413102105\ldots,
\]

\[
J_{iid}=3.5133120975758567242\times10^{-7},
\]

and after solving the **exact scalar reoptimization at the same frozen outer macrostate**,

\[
E_*=0.0011160365662448580929\ldots,
\]

\[
z_*=0.99968531447301236648\ldots,
\]

\[
\Delta_{inner}=3.5129045422595363160\times10^{-7}.
\]

Thus reoptimizing the degree split erodes only

\[
4.07555316320408\times10^{-11}
\]

from the direct iid penalty, retaining

\[
0.9998839968368874440\ldots.
\]

The stationarity residual in 80-digit Decimal arithmetic is `2.9913e-79`; the run ends

`ALL_SCALARIZATION_DIAGNOSTIC_CHECKS_PASS = True`.

For scale only, `Delta_inner` is about `100.3684` times the source's printed rounded log margin.  It is about `94.64%` of the preceding strongest ranked-plus-`j>=2` local correction.  Neither comparison is a global endpoint certificate.

## 9. Source metric, mechanism metric, and what remains

### Source-level metric

Externally published explicit-decimal bracket:

`[3.52,4.4898] -> [3.52,4.4898]`.

Width:

`0.9698 -> 0.9698`.

Exact `k=3` limiting threshold identification/existence: **OPEN**.

Carenini's `O(n/log n)` scaling-window theorem is sharper window information but does not identify a limiting center.

The separate NM13-13 project candidate is currently `4.3906`, **CANDIDATE_FULL pending independent review**.  It is not counted as this worker's source-metric movement and is not rederived here.

### Mechanism progress

Before this run, the missing global reoptimization retained a 23-component coupled degree split.

After this run:

- iid-priority correction: **23 split variables -> one scalar `E` plus uniquely determined `z(E)`**, with a complete proof;
- full ranked correction: **23 split variables -> one-dimensional tail-state Bellman recursion over 23 stages**, with a complete proof;
- rounded fixed-outer scalar reoptimization retains `99.9884%` of the iid local penalty.

### Exact unresolved full-scope gap

The source endpoint still requires a certified **outer** optimization.  Specifically, `q=Q_safe/P` and `beta=B_can/U` depend on the Díaz clause-type macrostate, not only on the `j=1` degree split.  A valid endpoint below `4.4898` therefore needs all of the following in one proof:

1. insert either Theorem 6.1 or Proposition 7.1 into the complete Díaz objective, including clause-type variables and all existing light/heavy truncation terms;
2. interval-certify every interior outer box at a chosen `alpha<4.4898`;
3. separately certify all boundary faces where `P,U,L,Q` can degenerate and the interior parameterization is unavailable;
4. retain the source's finite-`M=23` tail/heavy-variable error terms and the `(1+10^{-7})` continuity slack;
5. only then transfer the resulting simple-formula bound to the iid-with-replacement owner model via the `O(1/n)` collision estimate above.

That is the next mathematical obligation.  More rounded-saddle checker tuning without the outer certificate would not move the source metric.

## 10. Honest verdict

**PARTIAL / source OPEN.**

This run proves two exact structural reductions and executes one diagnostic after the mathematics.  It does **not** claim a new 3-SAT threshold endpoint, does **not** call the physics value a theorem, does **not** promote the neighboring unaudited `4.3906` candidate, and does **not** confuse a sharp scaling window with existence/identification of an exact limiting threshold.

The most promising continuation inside this scoped route is now clear: port the original Díaz outer three-dimensional box certification to the iid-priority scalar inner objective first.  If that succeeds, the full-ranked Bellman correction can be substituted later for additional slack.