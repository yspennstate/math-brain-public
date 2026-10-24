Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum reasoning was requested, but this runtime exposes no authenticated applied-model / applied-effort receipt, so I do not claim otherwise. **NO R17 SOURCE-ENDPOINT MOVEMENT THIS RUN:** the repository-internal certified interval remains `L <= gamma_2 <= U_R`, with `L=0.792665992` and P02's exact four-band endpoint `U_R`; hence `W_before=W_after=U_R-L`. Status remains **OPEN / PARTIAL**. **MECHANISM MOVEMENT:** the previous R17 pathwise all-state reward-span bound `2m` is improved to the sharp bound `m` for strip length `m=2w`; consequently the finite-horizon/stationary transfer improves from `|E_s R_N-N gamma_w|<=2m` to `<=m` (in particular `C_8:16 -> 8` and `C_12:24 -> 12`). The three attacks were: centered-boundary/path geometry (succeeds generally), exact attack-on-the-negation via product-Bellman search plus an explicit extremal family (no counterexample; instead proves sharpness of `m` and refutes any universal `<m` replacement), and a stationary variational transfer using the new pathwise span (succeeds, but does not yet move `L` or `U_R`).

# PROB10-02 / R17 — sharp centered path span and a factor-two finite-to-stationary transfer

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}{n}
\]
for two independent iid uniform binary strings. Every strip update below uses one genuine fresh `Y` bit against the entire active `X` window. No independent Bernoulli matching array and no simulation confidence interval is substituted.

## 0. Continuity, ownership, source metric, and the old R17 successor

Controlling owner directive: `operations/PROB10_2026-09-20.md`.

The actual pre-refocus R17 successor H0021 remains correctly handed off and is **not edited in this run**. `operations/claims/H0021.md`, blob `e4b83b8fb97a3fc672a007eb59621d6dd8718039`, records `UNASSIGNED / RELEASED BY R17`, preserves the R16 history, R17's H0021 report `runs/R17/20260919_2216Z_h0021_portwidth_defect_barrier_c080_b42f.md`, navigation commit `c8891869a1335d67bada83f23f63f2ce09603565`, all artifacts, and the frozen metric `Delta_near=2`. No counter or claim there is reset.

The newest completed R17 PROB10-02 dependency before this run is

`runs/prob10_2026-09-20/PROB10-02/20260920T0742Z_r17_reward_flux_span_3c71.md`, blob `e128692135d4c85a49d0920d8d7f580cb32e3f87`.

That report proved two pathwise sensitivity theorems for every common future source word: one initial gradient defect changes total future strip reward by at most one, and one initial raw-symbol change changes total future strip reward by at most one. Chaining coordinates gave
\[
|R_N(s)-R_N(t)|\le 2m
\tag{0.1}
\]
for arbitrary formal states. It explicitly left the stronger `m`-span as small-width evidence only. This run proves that stronger statement for every `m=2w` and shows it is sharp.

Current same-source ownership remains complementary:

- **P02:** covering/cone variational upper-bound route;
- **P13:** dependence-preserving boundary/reset-language synchronization route;
- **R17:** correlated reward/history and pathwise geometry route.

The newest complete P02 report recovered is

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T07-11-24Z__radix-four-band-support-report.md`, blob `197be381f48ffcb8c9816cd332ab98d72ce809ce`.

It retains
\[
L=\frac{99083249}{125000000}=0.792665992
\]
and defines its exact four-band upper endpoint as follows. Put
\[
p=256717,\quad q=800000,\quad d=q-p,\quad t=p/q,\quad S=q^6d,
\]
\[
a=1995237757733917147310102692686664915858011319606812684127301,
\]
\[
b=4220452010631561279,
\]
\[
D_R=147353456536129906925733975506591175200000,
\]
\[
\beta_R=\frac ab-\frac{D_R}{2ab},\qquad
\lambda_R=\frac{t^2}{S}\beta_R,
\qquad
U_R=\frac{\log(4t^2)}{\log\lambda_R}.
\]
P02's exact positive-series logarithm certificate proves
\[
\gamma_2\le U_R
\]
and in particular
\[
U_R<0.8262759427622826250151065815372966328234619961931900238808061833125629444302995503.
\]
The retained lower endpoint is the rigorous public Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer value above. P02's stronger upper endpoint is repository-internal and is not represented here as independently audited or public.

Therefore the exact source metric in this R17 run is
\[
\boxed{W_{\rm before}=W_{\rm after}=U_R-L.}
\tag{0.2}
\]
A high-precision diagnostic evaluation is
\[
U_R-L\approx0.03360995076228262501510658153729663282346199619319002388080618\ldots,
\]
but the proof-level metric is the symbolic quantity in (0.2).

Fresh bounded source navigation on 20 September 2026 remains consistent with the exact binary coefficient being unresolved. Tiskin `arXiv:2212.01582v2` is the corrected revision; its v2 comments expressly remove erroneous stochastic-process / `gamma` claims from the earlier preprint, and none is used here. The published rigorous literature retains the problem as open. A bounded negative search is status evidence, not a novelty certificate. No novelty claim is made for the path-span lemma below without a dedicated literature audit.

Historical no-endpoint-movement and recovery accounting is preserved exactly by reference to the predecessor reports; this run does not reset it. The owner contract requires a genuine method change within LCS after repeated unchanged source metrics. The centered-path argument below is such a change: it no longer estimates coalescence/synchronization time and no longer sums coordinatewise Lipschitz bounds.

## 1. Idea before code and the three attacks

The new idea was written before checker code at

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0812Z_r17_centered_path_span_idea_a4d2.md`

(creation commit `631ec4209c5221c92463bae3b208fc7fc22411f3`).

The three mathematically distinct attacks were:

1. **Centered-boundary/path geometry.** Center the initial strip boundary at the reward cut. A path entering far to one side can exploit a larger boundary offset only by forfeiting access to a compensating number of initial raw symbols. Prove the tradeoff directly in the unrolled LCS graph.
2. **Attack the negation exactly.** Search for a common source word and two formal states with reward discrepancy greater than `m`. An exact product-state Bellman iteration finds no such example through the exhaustively feasible small widths; an explicit family instead reaches discrepancy exactly `m`, showing that any proposed universal bound `<m` is false.
3. **Stationary variational transfer.** Couple an arbitrary start to a stationary strip state under the same genuine source word. The new pathwise theorem immediately halves the exact finite-horizon error around the stationary strip mean.

Attack 1 gives the theorem. Attack 2 verifies its finite transducer consequences and supplies a general sharpness construction. Attack 3 converts it into a rigorous finite-to-stationary approximation. None by itself improves the full-source interval (0.2), so no endpoint movement is claimed.

## 2. Genuine-source strip recursion and unrolled graph

Fix a half-width `w>=1` and put
\[
m=2w.
\]
A formal boundary state is
\[
s=(x,g),\qquad x=(x_1,\ldots,x_m),\quad g=(g_1,\ldots,g_m)\in\{0,1\}^m.
\]
Define
\[
V_0=0,\qquad V_k=\sum_{i=1}^k g_i\quad(1\le k\le m).
\tag{2.1}
\]
For a fresh actual source pair `(u,v)`, set
\[
a_i={\bf1}_{\{x_{i+1}=v\}}\quad(0\le i<m),
\qquad a_m={\bf1}_{\{u=v\}}.
\]
The next unnormalized profile is
\[
Q_0=\max\{V_1,V_0+a_0\},
\tag{2.2}
\]
\[
Q_k=\max\{Q_{k-1},V_k+a_k,V_{k+1}\},\qquad1\le k<m,
\tag{2.3}
\]
\[
Q_m=\max\{Q_{m-1},V_m+a_m\}.
\tag{2.4}
\]
The next raw window and gradient are
\[
x'=(x_2,\ldots,x_m,u),
\qquad g'_k=Q_k-Q_{k-1},
\tag{2.5}
\]
and the diagonal reward is
\[
\rho(s;u,v)=Q_w-V_w\in\{0,1\}.
\tag{2.6}
\]
The same `v` is used in every match indicator in (2.2)--(2.4); this is the true dependent matching array.

Unroll these recurrences for a fixed future word of length `N`. Let `F(i,j)` be the ordinary maximum-weight LCS dynamic-programming value in the diagonal strip
\[
0\le j\le N,\qquad j\le i\le j+m,
\tag{2.7}
\]
with bottom-boundary values
\[
F(k,0)=V_k,\qquad0\le k\le m.
\tag{2.8}
\]
Horizontal and vertical edges carry weight zero; a diagonal edge into `(i,j)` carries weight one exactly when the associated actual `X_i` and `Y_j` symbols agree. Equations (2.2)--(2.5) are precisely one-column propagation of this graph, with `Q_k=F(k+1,1)` up to the common normalization that is removed when the next gradient is formed.

The cumulative reward telescopes along the central diagonal:
\[
R_N(s)=\sum_{t=0}^{N-1}\rho(S_t;u_{t+1},v_{t+1})
=F(N+w,N)-F(w,0).
\tag{2.9}
\]
This follows because the reward at time `t` is the absolute increment from the central vertex `(t+w,t)` to `(t+w+1,t+1)`; the successive profile normalizations cancel in the sum.

For a bottom index `k`, let `M_s(k)` be the maximum diagonal-match weight of a monotone strip path from `(k,0)` to
\[
E=(N+w,N),
\]
using the initial raw word `x` from state `s` and the common future source word. Define the centered boundary height
\[
A_s(k):=V_k(s)-V_w(s).
\tag{2.10}
\]
Then the max-plus path decomposition of (2.9) is
\[
\boxed{R_N(s)=\max_{0\le k\le m}\{A_s(k)+M_s(k)\}.}
\tag{2.11}
\]
The elementary centered bounds are
\[
A_s(k)=-\sum_{i=k+1}^{w}g_i\le0\quad(k<w),
\tag{2.12}
\]
\[
0\le A_s(k)=\sum_{i=w+1}^{k}g_i\le k-w\quad(k\ge w).
\tag{2.13}
\]
These inequalities are the conservation law missed by the preceding coordinatewise `2m` argument: boundary advantage and future access to the old raw window cannot both be maximal.

## 3. Main theorem: the all-state pathwise span is at most `m`

### Theorem 3.1 — sharp centered path-span bound

Let `s=(x,g)` and `t=(y,h)` be any two formal strip states of length `m=2w`. Drive them by the same arbitrary finite future word of actual source pairs
\[
(u_1,v_1),\ldots,(u_N,v_N).
\]
Then
\[
\boxed{|R_N(s)-R_N(t)|\le m.}
\tag{3.1}
\]
This is deterministic and pathwise; no probability, mixing assumption, independent-match surrogate, or asymptotic approximation is used.

#### Proof

Choose an index `k` attaining the maximum in (2.11) for state `s`, so
\[
R_N(s)=A_s(k)+M_s(k).
\tag{3.2}
\]
We compare this single maximizing path to an admissible path for `t`.

**Case 1: `k>=w`.**

Take an optimal `s`-path from `(k,0)` to `E` and use the same geometric path for `t`. Once the path has started at `x`-coordinate `k`, the only `X` symbols on which the two path weights can differ are the old initial symbols
\[
X_{k+1},\ldots,X_m.
\]
There are `m-k` of them. Every monotone alignment path uses a fixed `X` symbol in at most one diagonal edge, while all appended future `X` symbols and all future `Y` symbols are common. Hence
\[
M_s(k)\le M_t(k)+(m-k).
\tag{3.3}
\]
By (2.13),
\[
A_s(k)\le k-w,
\qquad A_t(k)\ge0.
\tag{3.4}
\]
Therefore
\[
\begin{aligned}
R_N(s)
&=A_s(k)+M_s(k)\\
&\le(k-w)+M_t(k)+(m-k)\\
&\le A_t(k)+M_t(k)+(m-w)\\
&\le R_N(t)+w\\
&\le R_N(t)+m.
\end{aligned}
\tag{3.5}
\]

**Case 2: `k<w`.**

Let `P` be an optimal `s`-path from `(k,0)` to `E`. Let `(w,j_*)` be the first vertex of `P` whose `x`-coordinate is `w`. Such a vertex exists because the endpoint has `x`-coordinate `N+w`. Since the path lies in the strip and starts at height zero,
\[
0\le j_*\le w.
\tag{3.6}
\]
Before first reaching `x=w`, the path increases its `x`-coordinate only `w-k` times. Hence its prefix contains at most `w-k` diagonal match edges and therefore has match weight at most
\[
w-k.
\tag{3.7}
\]

For state `t`, start instead at the centered boundary vertex `(w,0)`, take `j_*` vertical zero-weight edges to `(w,j_*)`, and then follow the suffix of `P`. The vertical segment is admissible by (3.6), since `0<=w-j_*<=w<=m` keeps it in (2.7).

On the copied suffix, the only old `X` symbols that may differ between `s` and `t` are
\[
X_{w+1},\ldots,X_m,
\]
so there are at most `m-w=w` potentially changed diagonal contributions. Again each initial `X` symbol can be used diagonally at most once. Therefore the `t`-weight of that suffix is at least its `s`-weight minus `m-w`. Together with (3.7),
\[
M_s(k)\le M_t(w)+(w-k)+(m-w)=M_t(w)+(m-k)\le M_t(w)+m.
\tag{3.8}
\]
Because (2.12) gives `A_s(k)<=0` and by definition `A_t(w)=0`,
\[
R_N(s)
=A_s(k)+M_s(k)
\le M_t(w)+m
=A_t(w)+M_t(w)+m
\le R_N(t)+m.
\tag{3.9}
\]

Thus in both cases `R_N(s)-R_N(t)<=m`. Interchanging `s` and `t` gives the reverse inequality, proving (3.1). QED.

### Why this is not the old coordinatewise proof

The previous report paid separately for as many as `m` raw bits and `m` gradient bits. Theorem 3.1 does not chain local sensitivities. It uses a global tradeoff at the maximizing path's entrance index: moving the entrance right may increase the centered boundary value, but it simultaneously removes old raw symbols from the path's future. Moving it left gives access to more old symbols, but the centered boundary value is then nonpositive. This is exactly what cuts `2m` to `m`.

## 4. Attack 2: exact negation search and general sharpness

Before accepting Theorem 3.1, I attacked its negation on the exact finite transducer. For a fixed `m`, define
\[
D_n(s,t)=\max_{0\le r\le n}\ \max_{\omega\in\{00,01,10,11\}^r}
\{R_r(s;\omega)-R_r(t;\omega)\}.
\tag{4.1}
\]
The exact Bellman recurrence is
\[
D_{n+1}(s,t)=\max\left\{0,\max_{(u,v)}
\bigl[\rho(s;u,v)-\rho(t;u,v)+D_n(T_{uv}s,T_{uv}t)\bigr]\right\}.
\tag{4.2}
\]
If the finite integer array stabilizes, its fixed point is the exact supremum over all finite common source words, not a finite-horizon sample.

The archived checker performs this product-state iteration and obtains
\[
\sup_{s,t,N,\omega}(R_N(s)-R_N(t))=m
\]
exactly for `m=2,3,4,5`; for the source-relevant even widths this checks `m=2,4`. The odd values are only an algebraic sanity check of the same recurrence. No discrepancy greater than `m` exists in those exhaustive cases.

More importantly, `m` is attained for every source-relevant even `m`, so no universal pathwise constant smaller than `m` can replace (3.1).

### Proposition 4.1 — an extremal family

Let
\[
s=(1^m,0^m),\qquad t=(0^m,0^m),
\]
and drive both states for `m` steps by the genuine source word
\[
(u_r,v_r)=(0,1),\qquad1\le r\le m.
\tag{4.3}
\]
Then
\[
R_m(s)=m,\qquad R_m(t)=0,
\qquad |R_m(s)-R_m(t)|=m.
\tag{4.4}
\]

#### Proof

All initial boundary values are zero because both gradients are zero. In state `s`, the first `m` `X` symbols are all one and the `m` future `Y` symbols are all one. In the unrolled strip, the monotone diagonal path from `(0,0)` to `(m,m)` collects all `m` matches, then reaches the endpoint `(m+w,m)` by horizontal zero-weight steps; it remains inside the strip throughout. Since there are only `m` `Y` symbols, the optimum is exactly `m`.

For `t`, both the initial `X` word and every appended future `u` are zero, while every future `Y` symbol is one. There is no positive-weight diagonal edge, so its optimum and cumulative reward are zero. QED.

Thus Theorem 3.1 is sharp as a deterministic all-formal-state/common-word statement. This does **not** assert that every stationary expected-bias difference attains `m`; only the pathwise universal constant is claimed sharp.

## 5. Attack 3: exact stationary variational transfer

Let `P_w` be the finite true-source strip Markov chain and let `pi_w` denote its invariant law on the unique recurrent class. The inherited synchronizing-word argument from the R17/P13 lineage guarantees uniqueness of that recurrent class. Define
\[
\gamma_w=\mathbf E_{\pi_w}\rho(S_0;U_1,V_1).
\tag{5.1}
\]
This is the exact stationary finite-width LCS growth rate; the earlier R17 variational report established the dependence-preserving finite-width hierarchy and its relation to the full constant.

### Corollary 5.1 — sharp linear finite-horizon/stationary error

For every formal start state `s` and every `N>=1`,
\[
\boxed{\left|\mathbf E_sR_N-N\gamma_w\right|\le m=2w.}
\tag{5.2}
\]
Equivalently,
\[
\boxed{
\frac{\mathbf E_sR_N-m}{N}
\le\gamma_w\le
\frac{\mathbf E_sR_N+m}{N}.}
\tag{5.3}
\]

#### Proof

Sample `T_0~pi_w`, independently of the future iid source word, and drive `s` and `T_0` by that same word. Theorem 3.1 gives pathwise
\[
|R_N(s)-R_N(T_0)|\le m.
\]
Average over `T_0` and the common source word. Stationarity gives
\[
\mathbf E R_N(T_0)=N\gamma_w,
\]
which yields (5.2)--(5.3). QED.

This immediately replaces the predecessor theorem's `2m` error by `m`. In the notation used there:
\[
\boxed{C_8:16\longrightarrow8},
\qquad
\boxed{C_{12}:24\longrightarrow12}.
\tag{5.4}
\]
At width `w=6` this is also vastly smaller than the reset-language transfer constant in the newest recovered P13 report, `820311293209/2500000=328124.5172836`; the comparison concerns an auxiliary finite-to-stationary error only, not source-level ownership or endpoint movement.

The same result can be stated as a finite-state average-reward variational fact: the bias function
\[
h(s)=\lim_{N\to\infty}\bigl(\mathbf E_sR_N-N\gamma_w\bigr)
\]
when represented on the recurrent class may be normalized with oscillation at most `m`, because every finite-horizon bias has oscillation at most `m` by Theorem 3.1. Thus the exact Bellman dual admits an `m`-oscillation potential. No numerical approximation is needed for this existence statement.

## 6. Exact checker and actual output

Code:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0812Z_r17_centered_path_span_exact_a4d2.py`

creation commit `59c1b2d67a673a9937ab3435e5f272fa68566ff0`.

Archived output:

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0812Z_r17_centered_path_span_exact_a4d2.out`

creation commit `8f7d1f8209955bb8a12cb8d041417bd23970680b`.

The checker uses exact integer rewards and exact Bellman iteration on the finite product transducer. It reports

```
PAIR_BELLMAN m=2 exact_supremum=2 stabilized_after=3
PAIR_BELLMAN m=3 exact_supremum=3 stabilized_after=5
PAIR_BELLMAN m=4 exact_supremum=4 stabilized_after=6
PAIR_BELLMAN m=5 exact_supremum=5 stabilized_after=8
```

and verifies the tight family for every `m=1,...,12`, finishing

```
THEOREM_FINITE_EXHAUSTIVE_SUPPORT_PASS
GENERAL_TIGHT_FAMILY_PASS
ALL_EXACT_CHECKS_PASS
```

The execution return code was zero. The finite checker is a self-check of the theorem's finite consequences, not an independent audit and not a substitute for the proof in Sections 2--5.

## 7. What did not move and the exact remaining full-scope gap

The full source problem remains open. The new theorem controls the **time horizon error at a fixed strip width**. It does not by itself quantify the width error `gamma_2-gamma_w` sharply enough to improve `L`, nor does it touch P02's covering/cone upper endpoint `U_R`.

To raise the current certified lower endpoint using (5.3), one now needs a width `w` and an exact or rigorously bounded finite-horizon expectation satisfying
\[
\boxed{\frac{\mathbf E_sR_N-2w}{N}>0.792665992.}
\tag{7.1}
\]
A finite expectation that fails (7.1), or a simulation suggesting it, is not source movement. Small widths already investigated in the R17 lineage lie below the retained lower endpoint, so repeating those transfer-matrix calculations would be bookkeeping rather than research.

The next nonduplicating route inside PROB10-02 is therefore not another coalescence/reset certificate. It is to exploit the same centered max-plus path representation to compress the exact finite-horizon value function `s -> E_s R_N` at a width large enough for (7.1), or equivalently to construct a structured Bellman potential with a certified lower residual above `L`. The theorem proved here makes the required horizon error only `2w/N`, so all remaining difficulty is exposed in the exact state/value compression rather than hidden in a huge mixing constant.

No source endpoint was changed, no claim is marked PROVED at full scope, and no closure/audit status is advanced.

## 8. Structured ledger delta

```yaml
ledger_delta:
  task: PROB10-02
  parent_problem: binary Chvatal-Sankoff LCS constant
  status_before: OPEN/PARTIAL
  status_after: OPEN/PARTIAL
  source_metric: certified_interval_width
  source_before: U_R - 0.792665992
  source_after: U_R - 0.792665992
  source_movement: false
  mechanism_before: "all-state common-word reward span <= 2m; |E_s R_N-N gamma_w| <= 2m"
  mechanism_after: "sharp all-state common-word reward span <= m; |E_s R_N-N gamma_w| <= m"
  exact_width_examples: "C_8 16->8; C_12 24->12"
  full_scope_gap: "construct/certify exact finite-horizon or Bellman lower residual at a useful width so that (E_s R_N-2w)/N > 0.792665992, or improve U_R by a distinct certified upper route"
  ownership: "R17 correlated reward/history/path geometry; P02 cone upper route; P13 reset-language route"
  handoff_preserved: "H0021 remains UNASSIGNED/RELEASED BY R17 with Delta_near=2"
  artifacts:
    - artifacts/prob10_2026-09-20/PROB10-02/20260920T0812Z_r17_centered_path_span_idea_a4d2.md
    - artifacts/prob10_2026-09-20/PROB10-02/20260920T0812Z_r17_centered_path_span_exact_a4d2.py
    - artifacts/prob10_2026-09-20/PROB10-02/20260920T0812Z_r17_centered_path_span_exact_a4d2.out
```

Delivery discipline: this run changes only R17/PROB10-02-owned report/artifact paths. It does not edit peer-track files, shared root ledgers, schedules, cadence, enabled state, workflows, permissions, email, Drive, or public posting.