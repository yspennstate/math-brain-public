Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: the preceding block-constant boundary-repulsion theorem is upgraded to a heterogeneous concentration theorem: every full-support two-level `z=1+epsilon -> 1+` exact quadratic contact must put all but `O(epsilon)` of the positive-block hazard mass on a single coordinate. Thus block symmetry is not the escape; the only possible boundary escape is one-heavy. Methods #15 BREAK THE SYMMETRY ON PURPOSE, #18 SAY IT IN ANOTHER LANGUAGE, #29 ADD THE POINTS AT INFINITY.**

# R15 retained screen — heterogeneous boundary contacts collapse to one heavy coordinate

Date checked: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything about Talagrand/F0111 below remains **SELF_CHECK_ONLY / NOT CLAIMED / PENDING**. This report does not reopen Burdzy--Scheutzow Problem 7.2, does not promote F0111 to READY, does not solve Talagrand Problem 10.9, and does not satisfy the independent-audit closure rule.

## 1. Continuity, exact source, ownership and current-source check

I continued from the latest substantive R15 report

`runs/R15/20260919_2355Z_successor_screen_f0111_boundary_repulsion_i94q.md`

(commit `eca68f15775c7f46025b89600604faa385c58f62`) rather than restarting. Before new mathematics I reread/recovered `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the controlling I0076 handoff, the newest R15 report, and neighboring Burdzy/F0111 ownership state. The newest visible free-successor gates still report no lawful free READY+CLOSABLE target; I0077/Problem 7.8 remains owned elsewhere. No claim was created and no shared root or peer file was edited.

The primary Burdzy--Scheutzow PDF was rechecked directly on 2026-09-20:

- Definition 2.1: FBM means Brownian futures from random origins tending to `-infinity`; BBM is the time-reversed condition; 2BM means existence of one random time at which the complete centered past and future are independent standard Brownian motions.
- Problem 7.2 assumes FBM + BBM and existence of an arbitrary random time `T` at which the two complete centered half-processes are independent. It does **not** assume `T` is a stopping time and does **not** separately assume either half at `T` is Brownian.
- Problem 7.5 is a separate question and remains excluded.

Primary source: K. Burdzy and M. Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), University of Washington PDF `https://math.washington.edu/sites/math/files/documents/research/1302.6958.pdf`, Definition 2.1 and Problem 7.2.

Fresh dated searches on 2026-09-20 used the exact paper title, arXiv number, `Problem 7.2`, and independent-past/future terms. They recovered the original source, its published listing, and later references to the paper, but no accessible later primary source explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence, not a definitive global literature claim.

The controlling six-run handoff remains unchanged: the source-Theorem-6.1 candidate has FBM, BBM and failure of 2BM but not the Problem-7.2 independent seam; the later Brownian-prefix/BES candidate has the independent seam but was proved actually to be 2BM. Therefore there is still no surviving frozen candidate on which the four requested obligations can honestly be rescored. The historical `2/4` is only a retired positive-route value.

For the retained Talagrand screen, current 2026 primary literature was also rechecked. Ascoli--He--Park--Talagrand, arXiv:2608.11183 (11 Aug 2026), reformulate the discrete Convexity Conjecture through `k`-thresholds and prove substantial classes. Park, arXiv:2609.14681 (13 Sep 2026), gives a dimension-free comparison yielding a bound explicitly described as progress toward the conjecture. These sources do not authorize calling the present `k=2` screen a full solution.

## 2. Carried scalar/null setup

For the cardinality-two hazard write

`F(q)=sum_i q_i - log S(q)`,
`S(q)=sum_i exp(q_i) -(n-1)`.                                (2.1)

Let

`P(q)=sum_i A_i q_i + sum_{i<j} B_ij q_i q_j`,               (2.2)

with `A_i,B_ij >= 0`, be a global quadratic majorant exact at an interior point `q>0`. Put

`G=P-F`, `H=D^2 G(q) >= 0`,
`r_i=exp(q_i)/S(q)`.                                         (2.3)

Suppose `H` has a full-support two-level mixed null vector

`h=a 1_J - b 1_K`,
`a=1+delta`, `b=1-delta`, `0<delta<1`,
`J disjoint K=[n]`, `|J|=M`, `|K|=N`.                       (2.4)

Let

`x=sum_{i in J} r_i`, `y=sum_{i in K} r_i`,
`k=1-x-y=-(n-1)/S(q)`,                                      (2.5)

and use the carried scalar cubic-null parameter `z`. Along the surviving outer branch considered here, put

`z=1+epsilon`, `epsilon>0`, `epsilon -> 0`.                  (2.6)

The exact carried scalar formulas imply, uniformly when `delta` stays in a compact subinterval of `(0,1)`,

`k = -kappa_delta epsilon + O(epsilon^2)`,
`x = 1 + O(epsilon)`,
`y = nu_delta epsilon + O(epsilon^2)`,                       (2.7)

where

`kappa_delta = 4/[(1-delta^2)(delta+3)] >0`,
`nu_delta=(1+delta)^2/[2(1-delta)(delta+3)] >0`.             (2.8)

Consequently

`S(q)=Theta(1/epsilon)`                                      (2.9)

for fixed `M,N` and compact `delta`-range.

The previous report attacked (2.6) under block-constant `q`. The present run deliberately removes that symmetry completely.

## 3. Method #15 — coefficient mass balance without block symmetry

For `i != j`,

`H_ii=r_i-r_i^2`,
`H_ij=B_ij-r_i r_j`.                                        (3.1)

Since `H>=0`, testing `e_i-e_j` gives

`0 <= r_i+r_j-(r_i-r_j)^2-2B_ij`,

hence

`B_ij <= (r_i+r_j)/2`.                                      (3.2)

Let

`U=sum_{i<j, i,j in J} B_ij`,
`V=sum_{i<j, i,j in K} B_ij`,
`W=sum_{i in J,j in K} B_ij`.                               (3.3)

By (3.2) and `y=O(epsilon)`,

`V <= (N-1)y/2 = O(epsilon)`.                               (3.4)

The exact null equation `Hh=0` is

`sum_{j != i} B_ij h_j = r_i(p-h_i)`,                       (3.5)

where the carried directional mean is `p=delta+z`. Summing (3.5) over `K` gives

`a W - 2b V = y(z+1)`,                                      (3.6)

so

`W=O(epsilon)`.                                              (3.7)

Summing over `J` gives

`2a U - b W = x(z-1)=x epsilon`,                            (3.8)

hence

`U=O(epsilon)`.                                              (3.9)

Thus **all three total pair-coefficient masses are `O(epsilon)`**, with no block-constant assumption on `q`, `r`, or the coefficients.

This is where the old symmetric boundary theorem really starts: its needed small total coefficient mass is actually forced by nullity and PSD alone.

## 4. Method #18 — exact value contact is an entropy identity

Gradient contact gives

`A_i + sum_{j != i} B_ij q_j = 1-r_i`.                      (4.1)

Multiplying by `q_i`, summing, and comparing with exact value contact `P(q)=F(q)` yields the exact identity

`E := log S - sum_i r_i q_i
    = sum_{i<j} B_ij q_i q_j`.                               (4.2)

Since `q_i=log(S r_i)`, this also becomes

`E = k log S - sum_i r_i log r_i`.                           (4.3)

Equation (4.2) is the coefficient-energy language; (4.3) is the entropy language. Equating them is the key new route.

Write

`L=log(1/epsilon)`.                                          (4.4)

From `H_ii=r_i(1-r_i)>=0`, every `r_i<=1`. Therefore for `i in J`,

`0<q_i=log(S r_i) <= L+O(1)`.                               (4.5)

For `i in K`, `r_i<=y=O(epsilon)`, so

`0<q_i<=O(1)`.                                               (4.6)

Using (3.4), (3.7), (3.9), (4.5), (4.6) in (4.2),

`0<=E<=C epsilon L^2`                                       (4.7)

for some constant depending only on the fixed dimensions and compact `delta`-range.

Now normalize the `J`-mass:

`p_i=r_i/x`, `i in J`, `sum_{i in J}p_i=1`,
`H_J=-sum_{i in J} p_i log p_i`.                            (4.8)

The `J` part of (4.3) is

`-sum_{i in J} r_i log r_i = -x log x + x H_J`.             (4.9)

Solving (4.3) for `xH_J` and using `k=O(epsilon)`, `x=1+O(epsilon)`, and the fact that `sum_{K} r_i log r_i <=0`, gives

`H_J <= C epsilon L^2`.                                     (4.10)

Hence `H_J ->0`: any boundary-accumulating heterogeneous contact must already concentrate its `J` mass on one coordinate. The next step makes the scale sharp enough for a finite limiting system.

## 5. The new theorem: concentration is actually `O(epsilon)`

Let

`p_* = max_{i in J} p_i`,
`s=1-p_*`.                                                   (5.1)

### Theorem R15-F0111-HETEROGENEOUS-ONE-HEAVY

Fix `M,N` and let `delta` range in a compact subset of `(0,1)`. For every sequence of full-support interior exact contacts satisfying (2.1)--(2.6), with nonnegative quadratic coefficients, `H>=0`, and the carried two-level cubic-null outer-branch formulas,

`1-max_{i in J} r_i/x = O(epsilon)`.                         (5.2)

Equivalently, after choosing a maximizing coordinate `i_* in J`,

`r_{i_*}=1-O(epsilon)`,
`sum_{i in J\{i_*}} r_i=O(epsilon)`.                         (5.3)

In particular every coordinate other than `i_*` has `q_i=O(1)`, while

`q_{i_*}=log(1/epsilon)+O(1)`.                               (5.4)

Thus **the only possible heterogeneous escape from the preceding boundary-repulsion argument is a one-heavy contact**.

### Proof

From (4.10), `H_J->0`, hence `s->0`.

Assume for contradiction that along a subsequence

`R_epsilon:=s/epsilon -> infinity`.                          (5.5)

Choose `i_*` attaining `p_*`. Every other `J`-mass satisfies

`r_i=xp_i <= xs <= 2s`                                      (5.6)

for small `epsilon`. Since `S=Theta(1/epsilon)`, for `i != i_*` in `J`,

`q_i <= C + log(s/epsilon)
     = C+log R_epsilon`.                                     (5.7)

Also `q_{i_*}<=L+C`, every `K` coordinate has bounded `q_i`, and `log R_epsilon<=L+O(1)` because `s<=1`.

Every `J-J` edge contains either the heavy coordinate and one light coordinate, or two light coordinates. Therefore (3.9) and (5.7) improve (4.7) to

`E <= C epsilon L [1+log R_epsilon]`.                        (5.8)

The `J-K` and `K-K` contributions are only `O(epsilon L)` and `O(epsilon)`, respectively, by (3.7), (3.4), so they are absorbed in (5.8).

Returning to (4.3)--(4.9),

`H_J <= C epsilon L [1+log R_epsilon]`.                      (5.9)

On the other hand, among probability vectors with largest atom `1-s`, entropy is minimized by concentrating all remaining mass into one atom. Hence

`H_J >= -(1-s)log(1-s)-s log s
     >= s log(1/s)`.                                         (5.10)

Combining (5.9)--(5.10), writing `R=R_epsilon` and `t=log R`, gives

`R [L-t+O(1)] <= C L(1+t)`.                                  (5.11)

Because `s->0`, `L-t=log(1/s)->infinity`.

There are two cases.

1. If `t<=L/2` infinitely often, then (5.11) gives

   `R <= C'(1+t)`,                                           (5.12)

   impossible as `R=e^t->infinity`.

2. If `t>L/2` eventually, put `d=L-t=log(1/s)->infinity`. Then `d<L/2` and (5.11) gives

   `e^{L-d} d <= C L^2`.                                     (5.13)

   But `e^{L-d}>=e^{L/2}`, so the left side dominates `e^{L/2}d`, impossible since `d->infinity` while the right side is only polynomial in `L`.

Both cases contradict (5.5). Therefore `s/epsilon` is bounded, proving (5.2). Since `x=1+O(epsilon)` and PSD gives every `r_i<=1`, (5.3) follows. For a light `J` coordinate, `r_i=O(epsilon)` and `S=Theta(1/epsilon)`, giving bounded `q_i`; (4.6) handles `K`, while the heavy coordinate has `r_{i_*}=1-O(epsilon)`, giving (5.4). QED.

## 6. Method #29 — compactify the only surviving escape channel

The theorem reduces every boundary-accumulating heterogeneous sequence to one explicit finite scaling problem.

After passing to a subsequence, write the heavy coordinate as `*` and set

`r_* = 1-c epsilon+o(epsilon)`,                              (6.1)
`r_i = epsilon u_i+o(epsilon)` for `i in J\{*}`,
`r_j = epsilon v_j+o(epsilon)` for `j in K`.                 (6.2)

The exact scalar expansions give

`sum_{j in K} v_j = nu_delta`,                               (6.3)
`sum_{i in J\{*}} u_i - c
 = xi_delta`,                                                (6.4)

where

`xi_delta=(delta^2+4delta+7)/[2(1+delta)(delta+3)]`,          (6.5)

and `xi_delta+nu_delta=kappa_delta`.

Full support `q_i>0` implies

`u_i, v_j >= kappa_delta/(n-1)` in the liminf sense.          (6.6)

Moreover

`q_* = L + log((n-1)/kappa_delta)+o(1)`,                     (6.7)
`q_i -> log((n-1)u_i/kappa_delta)`,
`q_j -> log((n-1)v_j/kappa_delta)`                           (6.8)

along any subsubsequence on which the scaled masses converge.

Because `U,V,W=O(epsilon)`, every pair coefficient can be scaled as

`B_ij = epsilon b_ij+o(epsilon)`                             (6.9)

after another finite-dimensional subsequence. Dividing the exact null equations by `epsilon` gives the finite nonnegative flow system

`a sum_{i in J\{*}} b_{*i}
 - b sum_{j in K} b_{*j} = 1`,                               (6.10)

`a sum_{l in J, l != i} b_{il}
 - b sum_{j in K} b_{ij} = 0`
for every light `i in J\{*}`,                                (6.11)

`a sum_{i in J} b_{ji}
 - b sum_{l in K, l != j} b_{jl} = 2v_j`
for every `j in K`.                                          (6.12)

The value-contact entropy also has a clean leading term:

`E/(epsilon L) -> c`.                                        (6.13)

Since only edges incident to the heavy coordinate contribute at order `epsilon L`, (4.2) therefore yields

`c = sum_{i in J\{*}} b_{*i} q_i^(0)
    + sum_{j in K} b_{*j} q_j^(0)`,                          (6.14)

where `q^(0)` denotes the finite limits in (6.8).

Equations (6.3)--(6.14), together with the scaled PSD limit of `H/epsilon`, are now the complete boundary cursor. The old high-dimensional heterogeneous problem has been compressed to a finite nonnegative flow/PSD system with one distinguished heavy vertex.

This is the precise object the next run should attack. In particular, the preceding block-constant boundary theorem is now subsumed: if `M>=2` and the `J` masses remain comparable, then `s` stays bounded away from zero, contradicting (5.2).

## 7. What moved, what did not, and next route

### Native I0076

No movement. Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`. There is no surviving frozen counterexample candidate and no source-level proof of the implication. No stopping-time hypothesis was inserted, deterministic-time independence was not substituted, and Problem 7.5 was not used.

### Retained F0111 screen

Real movement: the prior theorem excluded only block-constant `z->1+` contacts. The new theorem proves that arbitrary within-block heterogeneity cannot stay diffuse. Every surviving boundary contact is forced into the one-heavy scaling (6.1)--(6.14).

The next high-value attack is therefore **not** another symmetric calculation. It is to solve/refute the finite one-heavy limiting flow/PSD system, ideally first in the sharp low-dimensional region inherited from the dimension barrier. A second route is to combine (6.10)--(6.14) with the exact arbitrary-ray global majorant cone already proved in earlier R15 reports.

No numerical path samples or finite grids are counted as proof. No new checker was made this run because the new claim is parameter-uniform and theorem-sized; its proof is written above, and there is no new finite enumeration claim.

## 8. Scheduler/model-control status

The current exposed automation surface was inspected without modifying anything. It exposes title/prompt, schedule/timing, enabled state and notification/email flags; it still exposes **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution control**. Thus GPT-6/maximum remains a prompt request only; this run is honestly labeled GPT-5.6 Sol / reasoning UNVERIFIED.

The historical P26 task ID `6aa7b43682948191b697d72fec69d539` previously returned `You cannot modify this task` in one authorization context. Repository reconciliation later records a successful full P26 update from an authorized P/C context. I did not attempt a scheduler edit in this run. The compliant workaround for an edit-denied task remains the owning/authorized workspace/account/API/admin context or platform support; there is no lawful permission-bypass or duplicate-task workaround. A real GPT-6/maximum guarantee would require a scheduler/backend/API surface that exposes, persists and attests those routing fields.

## 9. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  native_source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.2, intake I0076"
  native_metric_name: "number of four source-matching obligations proved for one frozen counterexample candidate"
  native_metric_before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_metric_after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: "RETIRED_HANDOFF; do not restart or fabricate a fresh streak"
  free_ready_closable_before: 0
  free_ready_closable_after: 0
  retained_screen: "Talagrand F0111 k=2, PENDING / SELF_CHECK_ONLY / NOT CLAIMED"
  retained_screen_before: "block-constant z->1+ boundary contacts excluded"
  retained_screen_after: "all heterogeneous z->1+ boundary contacts forced to one-heavy J mass: 1-max(r_i/x)=O(epsilon); finite one-heavy limiting flow system derived"
  tried_moves:
    - "15 BREAK THE SYMMETRY ON PURPOSE"
    - "18 SAY IT IN ANOTHER LANGUAGE"
    - "29 ADD THE POINTS AT INFINITY"
  remaining_obligation: "native I0076 has no surviving frozen candidate; retained screen must eliminate or realize the finite one-heavy limiting flow/PSD system, then still handle other Hessian-null/second-contact mechanisms"
  evidence:
    - "runs/R15/20260919_2355Z_successor_screen_f0111_boundary_repulsion_i94q.md"
    - "this report"
  audit_ids: []
  validation_label: "SELF_CHECK_ONLY; theorem proof on page; no independent audit"
```
