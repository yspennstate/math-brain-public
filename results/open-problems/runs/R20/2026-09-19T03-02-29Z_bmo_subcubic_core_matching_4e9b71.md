Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `n_all: 9 -> 9`; methods #5 ADD A PARAMETER, #20 FIND WHY THE ALGORITHM FAILS, #27 SWAP THE QUANTIFIERS.**

# R20 — subcubic core-matching theorem for BMO Conjecture 2.6

## 1. Continuity, ownership, exclusions, and current source

I continued from the newest complete R20 report,

`runs/R20/2026-09-19T02-24-00Z_bmo_subcubic_independent_deg3_5a8c31.md`,

rather than restarting from the stale scheduler-title Paley target. The active exclusive claim is still

`operations/claims/BMO-2025-PUSHING-DELTA.md`,

owned by R20 and marked `CLAIMED / READY / CLOSABLE OUTSIDE`.

Exact outside source: Julien Bensmail, Clara Marcille, Mano Orenga, *Pushing Vertices to Make Graphs Irregular*, DMTCS 27:3 (2025), article 7, Conjecture 2.6. For a nice finite simple graph `G`,

\[
P^\ell(G)\le \Delta(G)
\]

is conjectured, where a pushing scheme `rho` induces

\[
\sigma_\rho(u)=d_G(u)(1+\rho(u))+\sum_{v\sim u}\rho(v)
\]

and must make adjacent vertex sums distinct.

The old I0100/Randomstrasse-26 one-localized Paley target remains historical/frozen in R20's earlier state and is not reopened by this report. I make no new statement here about whether any Paley prime or the source asymptotic remains unresolved. P04/I0101, R12/I0102 and the Paley ETF line remain distinct and untouched.

Before research I reread the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, current `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the current R20 claim, and the newest R20 report.

### Fresh literature gate — 19 September 2026

The current DMTCS primary page still presents the Bensmail--Marcille--Orenga paper and Conjecture 2.6. The current published follow-up is Dieter Rautenbach, Laurin Schwartze and Florian Werner, *Coloring by Pushing Vertices*, Ars Combinatoria 167, pp. 147--157, published online 17 June 2026. Its abstract still states the general `P^ell(G)<=Delta(G)` bound as conjectural and proves it for cubic graphs and regular bipartite graphs; its discussion explicitly says the cubic proof uses regularity heavily and that the subcubic case seems much harder.

Bounded dated queries this run included

- `"Pushing Vertices to Make Graphs Irregular" degree three matching subcubic pushing scheme`,
- `"Coloring by Pushing Vertices" subcubic degree 3 matching`,
- `"P^l(G)" subcubic pushing vertices`,

plus the exact source title/DOI and the follow-up title. They surfaced the original paper, the 2026 follow-up, mirrors/indexes and unrelated graph-push terminology, but no later source-matching general proof/counterexample and no located theorem matching the 2-core matching class proved below. This is bounded negative evidence only, **not** a novelty certificate.

## 2. Idea-before-code and the three method moves

The research idea was written before validation code at

`artifacts/R20/2026-09-19T02-55-00Z_bmo_a1_asymmetric_branch_idea.md`

creation commit

`0f740e22bc7717b6fbf245521bf018d882de3e5c`.

The initial goal was the parameter

\[
a(G)=|E(G[V_3])|
\]

and the first missing case `a(G)=1` from the preceding report. The route became stronger than planned.

### #5 — ADD A PARAMETER: success, then strengthen

The one-direct-branch-edge obstruction can be broken asymmetrically by giving its two degree-three core endpoints pushes 3 and 2 rather than 3 and 3. Once the local port inequalities were written out, the same construction worked simultaneously on **any matching of direct branch edges**, not merely one edge.

### #20 — FIND WHY THE ALGORITHM FAILS: success

The old all-3 construction fails on a direct edge `bc` because the branch sums can coincide when the two remaining incident port sums coincide. With `rho(b)=3` and `rho(c)=2`, the direct-edge separation reduces to controlling only the two non-direct port sums. The sole dangerous phenomenon is a push-2 branch receiving value 2 on both of its chain ports. That obstruction is exactly a maximum-indegree-one orientation problem in an auxiliary degree-at-most-two pseudograph.

### #27 — SWAP THE QUANTIFIERS: success

Instead of choosing a whole-graph witness separately, I found one finite chain rule valid for every chain length and every boundary type in `{2,3}^2`, then glued the local rules. This yields the theorem below.

## 3. New theorem — full written proof

> **Theorem (R20, SELF_CHECK_ONLY).** Let `G` be a nice finite simple graph with `Delta(G)<=3`. Let `C` be its 2-core, and let
> \[
> B=\{v\in V(C):d_C(v)=3\}.
> \]
> If the induced graph `C[B]` has maximum degree at most one, equivalently the degree-three vertices of the 2-core induce a matching, then
> \[
> P^\ell(G)\le \Delta(G).
> \]
> In the new `Delta(G)=3` case there is a proper pushing scheme with all pushes in `{0,1,2,3}`.

This strictly contains the preceding R20 theorem where `C[B]` had no edges. It also permits arbitrarily many disjoint direct edges between degree-three core vertices.

### 3.1 Reduction to the nontrivial 2-core

Work componentwise. Isolated vertices are vacuous and nice graphs have no `K2` component. Trees satisfy the stronger source theorem `P^ell<=1`. If a connected non-tree component has 2-core `C` with no degree-three vertex, then `C` is a cycle, covered by the source maximum-degree-two result; the leaf-extension lemma in Section 3.5 reattaches the pruned forest.

It therefore remains to treat a connected component whose nonempty 2-core `C` has branch set `B` as above. Every vertex in `C-B` has core degree two. Since `C` is connected, every component of `C-B` is a path whose boundary incidences end in `B`. Write such a maximal chain as

\[
a,x_1,\ldots,x_k,b,\qquad k\ge1.
\]

The boundary branches `a,b` may coincide for a chain returning to the same branch.

### 3.2 Branch pushes

The graph `D=C[B]` is a matching. Give every unmatched branch push 3. For every matching edge `bc`, choose one endpoint `b` and set

\[
\rho(b)=3,\qquad \rho(c)=2.
\]

Thus every push-2 branch has exactly one direct push-3 branch neighbor and exactly two non-direct chain incidences.

### 3.3 A uniform degree-two-chain rule

For a chain with boundary branch pushes `alpha,beta in {2,3}`, use the following internal word.

For `k=1`, use

\[
W_1=1.
\]

For `k=2`, use

\[
W_2=\begin{cases}
12,&(\alpha,\beta)=(3,3),\\
11,&\{\alpha,\beta\}=\{2,3\},\\
12\text{ or }21,&(\alpha,\beta)=(2,2).
\end{cases}
\tag{3.1}
\]

For `k>=3`, use the closed-form words already exposed by the preceding run:

\[
W_3=101,\qquad W_4=1011,
\]

and, for larger `k`,

\[
\begin{aligned}
W_{4t+1}&=1(0001)^t,\\
W_{4t+2}&=1(0001)^t1,\\
W_{4t+3}&=1(0001)^t11,\\
W_{4t}&=1(0001)^{t-1}021.
\end{aligned}
\tag{3.2}
\]

All entries are in `{0,1,2}`. For a degree-two chain vertex,

\[
\sigma(x_i)=2(1+\rho(x_i))+\rho(x_{i-1})+\rho(x_{i+1}),
\tag{3.3}
\]

with boundary convention `rho(x_0)=alpha`, `rho(x_{k+1})=beta`.

For `k=1` there is no internal chain edge. For `k=2`, direct substitution into (3.3) gives distinct pairs

\[
(9,10),\quad (7,8),\quad (8,9)\text{ or }(9,8)
\]

for the three cases in (3.1). For `k=3`, `101` gives

\[
(4+\alpha,4,4+\beta),
\]

and for `k=4`, `1011` gives

\[
(4+\alpha,4,5,5+\beta),
\]

so consecutive sums are distinct for all `alpha,beta in {2,3}`.

In the repeated `0001` part of (3.2), the interior pattern of sums is `3,2,3,4`, with adjacent block junction `4,3`. The global left end is `4+alpha`, hence 6 or 7. The four terminal types end respectively in

\[
\ldots,3,4+\beta;
\qquad
\ldots,3,5,5+\beta;
\qquad
\ldots,3,5,6,5+\beta;
\qquad
\ldots,3,4,5,7,6+\beta.
\]

Every neighboring pair is unequal, and every degree-two chain sum is at most 10.

The only choice still unspecified is which orientation `12` or `21` to use on a length-two chain whose two boundary branches both have push 2.

### 3.4 Orienting the exceptional 2--2 chains

Build an auxiliary pseudograph `J` on the push-2 branches. For every length-two chain joining two push-2 branches, put one edge in `J`; if the chain leaves and returns to the same branch, this is a loop.

Each push-2 branch has exactly two chain incidences total, so

\[
\Delta(J)\le2
\]

with loops counted twice. Every component of `J` is therefore a path, a cycle (parallel pairs included), or an isolated loop. Orient path edges consistently, orient cycle edges cyclically, and orient a loop toward its unique vertex. Then every vertex has indegree at most one.

For an oriented exceptional chain `u->v`, choose its word so that the port value 2 is at `v` and the other port is 1. A loop gets one port 1 and one port 2. Consequently every push-2 branch receives at most one port value 2 among its two chain incidences, hence the sum `s_c` of its two non-direct port pushes satisfies

\[
2\le s_c\le3.
\tag{3.4}
\]

All other chains incident with a push-2 branch use port value 1 at that end.

### 3.5 Separating every core edge

All degree-two chain sums are at most 10.

An unmatched push-3 branch has three positive chain ports, so

\[
\sigma(b)\ge3(1+3)+1+1+1=15.
\]

A matched push-3 branch has one direct neighbor of push 2 and two positive chain ports, so

\[
\sigma(b)\ge12+2+1+1=16.
\tag{3.5}
\]

A matched push-2 branch has one direct push-3 neighbor and two chain ports whose sum obeys (3.4), so

\[
\sigma(c)=3(1+2)+3+s_c=12+s_c\in\{14,15\}.
\tag{3.6}
\]

Thus every branch--chain edge is proper because branch sums are at least 14 while chain sums are at most 10. There are no unmatched branch--branch edges. On every direct matching edge `bc`, (3.5)--(3.6) give

\[
\sigma(b)\ge16>15\ge\sigma(c).
\]

Hence the constructed scheme is proper on the entire 2-core `C`.

### 3.6 Leaf-extension lemma

Let `H` already have a proper pushing scheme with values in `{0,1,2,3}`, let `u` be nonisolated with `d_H(u)<=2`, and attach a new leaf `w`. Keep all old pushes and set `rho(w)=x`. Then only the sum at `u` changes among old vertices, and

\[
\sigma_{H+uw}(u)=\sigma_H(u)+(1+\rho(u))+x.
\]

Each old neighbor of `u` forbids at most one value of `x`; there are at most two such neighbors, so among `x=0,1,2,3` at least two choices remain. The new leaf edge is automatically safe because

\[
\sigma_{H+uw}(u)-\sigma_{H+uw}(w)=\sigma_H(u)>0.
\]

Reattach the forest deleted in forming the 2-core in increasing distance from `C`. Immediately before each new leaf is attached, its parent has current degree at most two, and it is nonisolated. Repeated application of the lemma therefore extends the proper `{0,1,2,3}`-valued scheme from `C` to the whole component. This completes the theorem.

## 4. Exact validation after the idea

Only after the idea note was committed did I add

`artifacts/R20/bmo_core_degree3_matching_exact.py`

creation commit

`652c9ecbb2f1bff176bf3df33ee1d4cc4b76f223`.

The script uses integer arithmetic for every pushing sum. It checks:

1. all boundary types `(alpha,beta) in {2,3}^2` for the closed-form chain rule through length 1000;
2. the exact small-chain port rules;
3. the constructive theorem on every eligible connected nice subcubic graph in NetworkX's complete unlabeled graph atlas through seven vertices.

The executed output is archived at

`artifacts/R20/bmo_core_degree3_matching_exact.out`

commit

`c51a30c3253babcb2478a9021df37c200fc371f5`.

Its exact output records

```text
networkx_version=3.6.1
chain_boundary_instances_checked=4001
chain_lengths_closed_form_checked=3..1000
max_chain_sigma_seen=10
atlas_eligible_connected_nice_subcubic_core_matching=84
atlas_counts_by_order={1: 1, 3: 2, 4: 5, 5: 9, 6: 22, 7: 45}
atlas_counts_by_kind={'branch_independent_core': 10, 'branch_matching_core': 25, 'cycle_core': 33, 'tree': 16}
atlas_failures=0
VERDICT=PASS
STATUS=SELF_CHECK_ONLY_PARTIAL_FOR_BMO_CONJECTURE_2_6
```

The 25 `branch_matching_core` atlas instances are the genuinely new direct-branch-edge validation class relative to the preceding independent-branch theorem. The finite computation is a self-check only; the infinite theorem rests on Section 3.

## 5. Metric, status, and remaining obligation

The frozen fleet metric remains

\[
\boxed{n_{\rm all}=9}.
\]

This run proves a stronger infinite structural subclass, but it does not certify all nice graphs on ten vertices and therefore does not move the fixed metric. The preceding report was unchanged run 1 after the `8->9` reset, so this is **unchanged run 2**. The Section-I stuck trigger has not yet fired.

The source conjecture remains **PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY**. No independent audit is claimed and no novelty certification is claimed.

The next structural frontier is to allow the degree-three core graph `C[B]` to have maximum degree two, i.e. paths and cycles of consecutive branch vertices. The matching proof succeeds because push-2 branches can be isolated by a one-incoming-port orientation. With branch paths/cycles, the next task is to find a finite-state rule for branch pushes in `{2,3}` plus chain endpoint ports in `{1,2}` that keeps consecutive branch sums distinct.

Next nonrepeating Section-B moves: **#3 PROVE SOMETHING STRONGER, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, #19 MAKE IT AN ALGORITHM**. The intended target is a finite automaton for branch paths/cycles, followed by a symbolic periodic construction rather than a whole-graph census.

## 6. Model/scheduler control status

The implementation limitation remains exactly as documented. The exposed task-control surface provides title, prompt, schedule/timing and enabled-state controls, but **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long execution control**. Therefore `GPT-6 / maximum` in prompt text cannot be truthfully upgraded into a runtime claim.

The historical P26 update attempt returned `You cannot modify this task`. Repository operations records show that this was authorization-context-specific and that a later authorized context could update P26. The legitimate remedy for a denied task is an owner/admin-authorized product or backend context with the needed task permission; it is not a permission bypass or duplicate schedule. No scheduler or permission changes were attempted in this run.

## 7. Structured ledger delta

```yaml
ledger_delta:
  track: R20
  source: "Julien Bensmail, Clara Marcille, Mano Orenga, Pushing Vertices to Make Graphs Irregular, DMTCS 27:3 (2025), Conjecture 2.6"
  canonical_claim: "operations/claims/BMO-2025-PUSHING-DELTA.md"
  fixed_metric: n_all
  before: 9
  after: 9
  movement: "no movement"
  unchanged_count: 2
  status: "PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY"
  tried_moves: [5, 20, 27]
  new_result: "Every nice subcubic graph whose 2-core degree-3 vertices induce a matching has P^ell(G)<=Delta(G); in the Delta=3 case an explicit {0,1,2,3}-valued scheme is constructed."
  remaining_obligation: "Prove or refute BMO Conjecture 2.6. Immediate frontier: subcubic graphs whose 2-core degree-3 induced graph contains paths/cycles of branch adjacency (maximum degree 2 rather than 1)."
  evidence:
    idea_before_code_commit: "0f740e22bc7717b6fbf245521bf018d882de3e5c"
    exact_checker_commit: "652c9ecbb2f1bff176bf3df33ee1d4cc4b76f223"
    exact_output_commit: "c51a30c3253babcb2478a9021df37c200fc371f5"
    checker_verdict: PASS
    atlas_eligible: 84
    atlas_new_branch_matching_core: 25
  audits: []
  next_moves: [3, 16, 19]
  shared_roots_edited: false
  peer_files_edited: false
  scheduler_changed: false
```

**Verdict for this run:** real infinite-family progress from independent branch vertices to a matching of direct branch edges, but no fixed-metric movement and no source closure.
