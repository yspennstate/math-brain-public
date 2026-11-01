Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `n_all: 9 -> 9`; this is the sixth consecutive unchanged BMO run after the `8 -> 9` reset, so the CLOSABLE six-run rule triggers an operational handoff. Methods #1 CHANGE THE CATEGORY, #15 BREAK THE SYMMETRY ON PURPOSE, #27 SWAP THE QUANTIFIERS.**

# R20 — six-run BMO handoff: deficit-sum reformulation and the exact remaining mixed-branch obstruction

Repository / branch: `yspennstate/math-open-problems` / `master`.

## 0. Continuity, ownership, stale scheduler title, and lifecycle decision

I continued from the newest complete R20 report

`runs/R20/2026-09-19T05-52-13Z_bmo_full_branch_cycle_dp_slack_7f3b91.md`

rather than restarting from the native scheduler title. The current exclusive R20 claim remains

`operations/claims/BMO-2025-PUSHING-DELTA.md`,

which is `CLAIMED / READY / CLOSABLE OUTSIDE` for Bensmail--Marcille--Orenga, *Pushing Vertices to Make Graphs Irregular*, DMTCS 27:3 (2025), Conjecture 2.6. The source target is

\[
P^\ell(G)\le \Delta(G)
\]

for every nice finite simple graph.

The older `operations/claims/I0100.md` is still present because claim records are preserved, but later immutable R20 history records the Bandeira / Randomstrasse Conjecture 26 Paley one-localization program as a terminal six-unchanged-run handoff for this worker. Its exact finite frontier remains frozen at

`p_max=1213`

with retained covered set

`{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`.

Those exact finite certificates did **not** prove the Paley asymptotic. I therefore do not reopen I0100, P04's two-localization, R12's degree-four SOS line, or C28's ETF line.

At run start I reread/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the BMO and I0100 canonical claims, the newest R20 report, the newest relevant neighboring CLOSABLE admission report, and current post-neighbor Git delta. The root records remain historical/coordinator surfaces; this worker edits none of them.

The previous fixed-metric movement was `n_all: 8 -> 9`. The subsequent supported BMO unchanged counts are 1, 2, 3, 4, 5 in the five preceding runs; this run is count **6**. Under `NEW-METHODS-2026-09-16`, a CLOSABLE target rotates after six unchanged runs. Therefore the mathematical work below is a handoff-quality route extraction, not another attempt to reset the stagnation counter by producing a restricted lemma.

No canonical claim is edited or implicitly released here. Repository precedent distinguishes a terminal handoff from an explicit owner-authorized `RELEASED / UNASSIGNED` claim transition.

## 1. Fresh current-source and prior-art check — 19 September 2026

### Active BMO source

The DMTCS source page remains current for Julien Bensmail, Clara Marcille and Mano Orenga, *Pushing Vertices to Make Graphs Irregular*, DOI `10.46298/dmtcs.14963`. The current published follow-up Dieter Rautenbach, Laurin Schwartze and Florian Werner, *Coloring by pushing vertices*, Ars Combinatoria 167 (published online 17 June 2026), still describes the general `P^l(G) <= Delta(G)` statement as a conjecture and proves it for cubic graphs and regular bipartite graphs. Bounded dated searches for the exact title/conjecture, `proper pushing scheme subcubic`, and later-author/citing work recovered these sources and no later source-matching general resolution. This is bounded negative evidence only, not a worldwide novelty certificate.

### Stale Paley scheduler source

The current Randomstrasse page still prints Conjecture 26 as

\[
\vartheta(\overline{G_{p,1}})\sim\sqrt{p/2}.
\]

A current public formalization/status page also continues to label that asymptotic open while recording partial implications/certificate work. Thus I make no claim that the source was secretly resolved; I simply preserve R20's prior six-run handoff rather than violating lifecycle continuity.

### Nearest established weighting technology

The algebra below lands close to neighbor-sum-distinguishing edge weighting. Ralph Keusch, *A Solution to the 1-2-3 Conjecture* (JCTB 2024; arXiv:2303.02611), proves that every graph without an isolated edge admits a neighbor-sum-distinguishing edge weighting from `{1,2,3}`. That theorem is not directly applicable here because the BMO reduction freezes one class of incidences and weights only the complementary path ports.

The distinction is real rather than cosmetic: Shubhada Aute, Fahad Panolan and Geevarghese Philip, *The Parameterized Complexity of Vertex-Coloring Edge-Weighting* (arXiv:2604.12363, April 2026), treats **pre-edge-weighting extension** as a separate problem and studies its complexity. I found no theorem in the bounded search that supplies the exact universal preassigned-zero extension needed below.

## 2. Exact new language: branch deficits

This is the useful mathematical content of the handoff.

Let `G` be a connected nice subcubic graph, `C` its nonempty 2-core, and

\[
B=\{b\in V(C): d_C(b)=3\}.
\]

Let `D=C[B]` be the graph of **direct branch edges**. For a branch `b`, write

\[
d=d_D(b),\qquad r=3-d.
\]

The `r` remaining incidences at `b` enter maximal paths through degree-two core vertices. Give branch `b` a push

\[
\rho(b)=3-\delta_b,\qquad \delta_b\in\{0,1,2,3\}.
\]

For every subdivided-path incidence at `b`, let `p` be the push of the first degree-two vertex on that path and define its **deficit**

\[
q=3-p\in\{0,1,2,3\},\qquad Q_b=\sum q,
\]

where the sum ranges over all subdivided incidences at `b`.

Then the branch color has the exact identity

\[
\begin{aligned}
\sigma(b)
&=3(1+\rho(b))
  +\sum_{z\in N_D(b)}\rho(z)
  +\sum_{\text{subdivided incidences}}p\\
&=12-3\delta_b+3d-\sum_{z\in N_D(b)}\delta_z
  +3r-Q_b\\
&=21-\left(Q_b+3\delta_b+\sum_{z\in N_D(b)}\delta_z\right).
\end{aligned}
\]

Define

\[
\boxed{T_b:=Q_b+3\delta_b+\sum_{z\in N_D(b)}\delta_z.}
\tag{2.1}
\]

For every direct branch edge `uv`, properness is now exactly

\[
\boxed{T_u\ne T_v.}
\tag{2.2}
\]

This removes the distracting degree terms completely. It is the cleanest language I found for the mixed branch case.

For the already proved binary boundary regime `delta in {0,1}`, the retained chain-transfer lemma from the preceding R20 work becomes, in deficit variables,

\[
\boxed{
\begin{array}{ll}
k=1:&q_u=q_v,\\
k=2:&q_u+\delta_u\ne q_v+\delta_v,\\
k\ge3:&\text{every endpoint deficit pair }(q_u,q_v)\in\{0,1,2,3\}^2\text{ is realizable.}
\end{array}}
\tag{2.3}
\]

Here `k` is the number of internal degree-two vertices on the branch-to-branch path. Equation (2.3) is only asserted in the boundary-push regime for which the earlier transfer lemma was proved; extending it uniformly to arbitrary `delta in {0,1,2,3}` is a genuine future obligation, not silently assumed.

## 3. Method #1 — CHANGE THE CATEGORY

Set all branch defects to zero first. Then (2.1) becomes simply

\[
T_b=Q_b,
\]

so the direct-edge problem asks for a proper vertex coloring of `D` by **incident half-edge deficit sums**.

If a branch has direct degree `d`, then it has `r=3-d` subdivided incidences. Ignoring endpoint coupling for a moment, its complete possible sum set is

\[
Q_b\in\{0,1,\ldots,3r\},
\]

of cardinality

\[
3r+1=10-3d.
\tag{3.1}
\]

Thus the raw list sizes by direct degree are

\[
 d=0,1,2,3:\qquad 10,7,4,1.
\tag{3.2}
\]

This exposes the structural frontier immediately: every non-cubic branch has local list slack, while a branch with three direct branch neighbors has no port freedom at all under the zero-defect scheme.

When every relevant subdivided path has `k=1`, the shared-deficit condition `q_u=q_v` turns the problem into a neighbor-sum edge-weighting on the graph formed by those subdivided connections, while the inequalities are demanded across the *different* direct-edge graph `D`. Equivalently, one can view the direct edges as frozen zero-weight incidences in a pre-edge-weighting extension problem. This is close to the solved 1-2-3 theorem but not the same theorem: Keusch's result is free to weight all edges, whereas our reduction must respect a preassigned/frozen partition.

**Outcome:** category change succeeded in locating the missing theorem. The remaining issue is not another path word. It is a constrained/preassigned neighbor-sum extension theorem for a cubic incidence decomposition.

## 4. Method #15 — BREAK THE SYMMETRY ON PURPOSE

The preceding run used binary defects `delta in {0,1}` to destroy the short-theta symmetry. I attacked that binary scheme itself before trying to generalize it.

On an all-direct `K4`, there are no ports, so `Q_b=0`. Let

\[
E=\sum_{v\in V(K_4)}\delta_v,
\qquad \delta_v\in\{0,1\}.
\]

Because every vertex sees the other three,

\[
T_v=3\delta_v+\sum_{u\ne v}\delta_u
   =E+2\delta_v.
\tag{4.1}
\]

Hence binary defects produce at most two distinct values on four pairwise adjacent vertices. They can never make `K4` proper. This **refutes the binary-defect subroute**, not the BMO conjecture.

I exact-checked all `2^4=16` binary assignments. The checker/output are

- `artifacts/R20/2026-09-19T06-47-48Z_bmo_binary_defect_k4_exact.py`, creation commit `e8efc456c0957873dba0804006b50215098a1832`;
- `artifacts/R20/2026-09-19T06-47-48Z_bmo_binary_defect_k4_exact.out`, archive commit `1a3790b4cb91464377c74f3de04a41c4433b9596`.

The archived result is

`proper_binary_defect_assignments=0`

and

`VERDICT=PASS_BINARY_SUBROUTE_OBSTRUCTION`.

This is consistent with, and explains why one should not try to extend, the short-theta binary trick indiscriminately. The published cubic theorem says the *source problem* is solvable on all-direct cubic blocks; what is missing for R20's induction is a **boundary-compatible** version of that cubic solution, or else a transfer lemma allowing the full four-state branch defect `delta in {0,1,2,3}`.

**Outcome:** symmetry breaking is necessary but binary symmetry breaking is provably too weak already on `K4`.

## 5. Method #27 — SWAP THE QUANTIFIERS

Instead of first choosing every local port and hoping the sums become proper, choose the target branch colors `T_b` (or `Q_b` after a defect pattern is fixed) first, and only afterward ask whether those sums can be realized by half-edge deficits.

In the zero-defect picture this suggests two stages:

1. choose `Q_b in {0,...,3(3-d_D(b))}` so that `Q_u != Q_v` on every direct edge;
2. realize each chosen `Q_b` as a sum of incident deficits while satisfying the path couplings.

Stage 1 has enormous apparent slack away from direct degree three, by (3.2). Stage 2 is the actual obstruction. The path constraints are not independent:

- a `k=1` path identifies two endpoint deficit variables;
- a `k=2` path forbids one translated equality in the binary-defect regime;
- a `k>=3` path is endpoint-free in that regime.

So an arbitrary list-coloring of `D` need not lift to actual half-edge variables. The needed statement is a **sum-correspondence extension lemma**: after fixing (or partially fixing) branch defects, prove that a proper target vector `T` inside the local sum ranges has a realization by bounded half-edge deficits subject to all `k=1/2` correspondences, possibly after choosing `T` from a controlled sublist.

The simplest genuinely mixed structural test not covered by R20's preceding `Delta(D)<=1` and 2-regular theorems is a four-branch component with

\[
D=P_4
\]

and the remaining suppressed cubic incidences supplied by short subdivided paths. That is the first place I would test an exact sum-correspondence extension theorem before returning to arbitrary `D`.

**Outcome:** swapping quantifiers clarifies the missing lemma, but does not yet prove it. It also explains why merely quoting the solved 1-2-3 theorem is insufficient: the frozen/preassigned edge partition must survive the lift.

## 6. What a future proof must contain

The immediate mixed-subcubic gap has now been reduced to one of two credible mechanisms.

**Route A — full-defect transfer.** Extend the exact chain-transfer calculus from boundary branch pushes `{2,3}` to all branch pushes `{0,1,2,3}`. Then use the published cubic solution (or a strengthened boundary version of it) on direct-degree-three blocks and use the large deficit-sum lists (3.2) to extend across lower-direct-degree vertices.

**Route B — pre-edge-weighting / sum-correspondence theorem.** Work directly with (2.1)--(2.3). Prove an extension theorem for the cubic incidence decomposition in which direct edges are the inequality graph and subdivided-path ports are the bounded weighting variables. The 1-2-3 theorem is the nearest solved shape, but the preassigned/frozen variant must be handled rather than assumed.

What neither current route contains is the needed **boundary extension guarantee** across a mixed direct-degree component. Producing another isolated path word or another finite graph census would not address that obstruction.

## 7. Fixed metric, six-run terminal handoff, and successor gate

The fixed all-graphs metric stays honestly

\[
\boxed{n_{\rm all}=9}.
\]

Nothing in Sections 2--6 certifies every nice ten-vertex graph, so there is no metric movement. This is supported unchanged count **6** after the previous `8 -> 9` movement. Therefore the BMO attack enters

`PARTIAL / RETIRED_AFTER_SIX_UNCHANGED / HANDOFF`

as an **operational** state. The mathematical source remains OPEN-looking in the bounded current literature check; this is not a source closure or refutation.

I then checked the lawful CLOSABLE successor gate rather than stealing a queue row. The most recent neighboring admission report found three newly admitted CLOSABLE targets, all already exclusively owned. A fresh exact Git comparison after that report now shows one additional CLOSABLE canonical claim, `P0411`, but it too is already owned (`proofnet24/NM13-05`). The same post-neighbor delta contains an explicit release of a **HARD-shaped** dimensional Brunn--Minkowski claim, not a free CLOSABLE successor. No current root/intake change in that comparison creates an owner-clear READY CLOSABLE target for R20.

Accordingly

\[
E_{\rm READY\ successor}:0\to0.
\]

I do **not** promote a PENDING queue candidate, duplicate another worker's claim, infer release from a terminal handoff, or overwrite the preserved BMO claim. The correct next state is

`TERMINAL_WAITING_FOR_NEW_READY_DELTA`.

If a future invocation sees a literal new owner-clear, source-exact, current-open-looking CLOSABLE admission or an explicit release/reassignment event, it should claim that successor create-only and begin with the source-valid counterexample search. Otherwise it should not reopen BMO or I0100 merely because their native scheduler titles remain visible.

## 8. Model / scheduler-control truth

The actual model exposed for this run is **GPT-5.6 Sol**. The applied reasoning level is **UNVERIFIED**. I therefore do not claim GPT-6 maximum.

The currently exposed scheduled-task control surface still has fields for task identity/title, prompt, schedule or relative start, timing mode, enabled state, and list/update operations. It exposes **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/applied-effort receipt, and no guaranteed hour-long execution setting**. To make GPT-6 / maximum binding rather than aspirational prompt text, the product/backend would need to expose persistent model and reasoning fields (or equivalent authorized admin/API controls) and authenticated per-run telemetry.

The operative implementation record preserves the historical P26 update failure `You cannot modify this task`. Root `RESULTS.md` also records that a later authorized P/C context successfully updated P26, so the failure is context/authorization-specific rather than evidence that the task can never be changed. The lawful workaround is the owning/authorized account/workspace or product/admin surface for that same task, not task duplication, permission escalation, identity substitution, or bypass.

## 9. Validation / delivery budget

Research idea came first. Validation was limited to the exact 16-case binary-defect stress test, current-source/literature checks, current repository/ownership delta, and this immutable handoff. No new all-graphs census, audit request, receipt-only commit, email, Drive write, public post, purchase, permission change, shared-root edit, peer-track edit, or scheduler change was made.

```yaml
ledger_delta:
  source: "Bensmail--Marcille--Orenga (DMTCS 27:3, 2025), Conjecture 2.6"
  metric_name: "n_all = largest n for which every nice simple graph on at most n vertices is exactly certified with max rho <= Delta"
  before: 9
  after: 9
  movement: "none"
  unchanged_count_after_n9_reset: 6
  status: "PARTIAL / RETIRED_AFTER_SIX_UNCHANGED / HANDOFF / TERMINAL_WAITING_FOR_NEW_READY_DELTA"
  tried_moves: [1, 15, 27]
  route_result:
    - "exact branch deficit identity sigma(b)=21-T_b"
    - "binary-defect subroute exactly fails on all-direct K4; this is not a source counterexample"
    - "remaining mixed-subcubic obligation isolated as a sum-correspondence / pre-edge-weighting extension theorem"
  simplest_unproved_structural_test: "mixed four-branch direct graph D=P4 with remaining suppressed incidences supplied by short subdivided paths"
  remaining_obligation:
    - "do not reopen BMO after the six-run handoff without an explicit lifecycle reassignment"
    - "future mathematical handoff route A: extend chain transfer to all four branch-defect states and obtain a boundary-compatible cubic block extension"
    - "future mathematical handoff route B: prove a preassigned/frozen neighbor-sum sum-correspondence extension theorem"
    - "successor gate: react only to an owner-clear READY CLOSABLE source or explicit release/reassignment event"
  successor_gate_before: 0
  successor_gate_after: 0
  evidence:
    - "latest complete R20 predecessor: runs/R20/2026-09-19T05-52-13Z_bmo_full_branch_cycle_dp_slack_7f3b91.md"
    - "exact K4 binary checker commit e8efc456c0957873dba0804006b50215098a1832"
    - "exact K4 output archive commit 1a3790b4cb91464377c74f3de04a41c4433b9596"
    - "fresh BMO primary/follow-up search dated 2026-09-19"
    - "fresh Randomstrasse Conjecture 26 source/status check dated 2026-09-19"
    - "post-neighbor exact Git delta: new P0411 CLOSABLE claim already owned; no free CLOSABLE release recovered"
  audits:
    source_closure: "none claimed"
    current_run: "SELF_CHECK_ONLY finite subroute obstruction; no independent audit requested"
```
