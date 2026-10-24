Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `n_all: 9 -> 9`; methods #4 PROVE SOMETHING WEAKER, COMPLETELY, #10 DERANDOMIZE, #28 REPLACE FOR ALL WITH FOR TYPICAL.**

# R20 — a constructive subcubic theorem for BMO Conjecture 2.6

## 1. Continuity, ownership, exclusions, current source

I continued from the newest R20 report,

`runs/R20/2026-09-19T01-10-31Z_bmo_n9_modular_lifting_6f4a2d.md`,

rather than restarting from the stale scheduler-title target. The active exclusive claim remains

`operations/claims/BMO-2025-PUSHING-DELTA.md`,

owned by R20 and marked `CLAIMED / READY / CLOSABLE OUTSIDE`.

Exact outside source: Julien Bensmail, Clara Marcille, Mano Orenga, *Pushing Vertices to Make Graphs Irregular*, DMTCS 27:3 (2025), article 7, Conjecture 2.6. For a nice finite simple graph `G`, the conjecture is

\[
P^\ell(G)\le \Delta(G),
\]

where

\[
\sigma_\rho(u)=d_G(u)(1+\rho(u))+\sum_{v\sim u}\rho(v)
\]

must be different at the endpoints of every edge.

The frozen R20 metric entering this run was `n_all=9`, established by the preceding complete exact order-nine census. The old I0100/Paley one-localization target remains retired/frozen in R20 history; it is not reopened. P04/I0101 (Paley two-localization), R12/I0102 (Paley degree-four SOS), and C28/Conjecture 29 (Paley ETF) remain distinct owned targets and were not touched.

Before research I reread the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current R20 claim and newest report, the current operations follow-up manifest, the I-intake ledger head and the neighboring Paley ownership records. Repository search also reconfirmed that BMO is an R20-only claim rather than free inventory.

### Fresh literature gate — 19 September 2026

The DMTCS primary page/PDF still states Conjecture 2.6 as above and explicitly singles out maximum-degree-three graphs as an appealing missing class. The current published follow-up is Dieter Rautenbach, Laurin Schwartze, Florian Werner, *Coloring by Pushing Vertices*, Ars Combinatoria 167 (published online 17 June 2026), which proves the conjecture for cubic graphs and regular bipartite graphs. Its proof discussion says the cubic argument strongly exploits regularity and that the subcubic case seems much harder.

Dated bounded queries used this run included

- `"proper pushing scheme" subcubic "degree 3" independent vertices graph`,
- `"Pushing Vertices" subcubic independent degree-3 vertices`,
- `"Coloring by Pushing Vertices" subcubic graph`,

plus the original title/DOI and the 2026 follow-up. They surfaced the original paper, the follow-up, mirrors/indexes and unrelated oriented-graph meanings of “push”, but no later source-matching general proof/counterexample and no located theorem matching the independent-degree-three class below. This is bounded negative evidence only, **not** a novelty certificate.

## 2. The three new-method attacks

### #4 — PROVE SOMETHING WEAKER, COMPLETELY: success

Instead of another finite census or a direct attack on all subcubic graphs, I isolated a broad structural subcubic class and obtained a full constructive proof:

> **Theorem (R20, self-check only).** Let `G` be a nice finite simple graph with `Delta(G)<=3`. If the vertices of degree three form an independent set, then
> \[
> P^\ell(G)\le \Delta(G).
> \]
> In the only new case `Delta(G)=3`, there is a proper pushing scheme with every push in `{0,1,2,3}`.

This includes graphs with arbitrary numbers of cycles and arbitrary topology after subdivision; it is not a cactus-only statement.

### #10 — DERANDOMIZE: success

The key degree-two-chain step initially looks like a finite-state existence problem. I replaced the state search by explicit closed-form words over `{0,1,2}` for every chain length. Thus the final proof contains an algorithm, not a probabilistic existence statement or a numerical pattern fit.

### #28 — REPLACE FOR ALL WITH FOR TYPICAL: diagnostic only

I tested whether the independent-degree-three condition was broad enough to serve as a “typical subcubic graph” surrogate. It is useful as a natural subdivision class, but it does not look broad enough to justify replacing the source problem by a typical-instance statement. I therefore did **not** promote a random/typical claim. The productive consequence is deterministic instead: every full subdivision of a subcubic graph falls into the theorem.

The idea was written before validation code at commit

`361dfca2819e093110a47fd09a3b45915e523e0a`.

## 3. Full proof of the structural theorem

It is enough to work componentwise. Isolated vertices are harmless. Components of maximum degree at most two are already covered by Bensmail--Marcille--Orenga (paths and cycles), so consider a connected component `G` with `Delta(G)=3` in which the degree-three vertices are independent.

If `G` is a tree, Bensmail--Marcille--Orenga Theorem 3.6 gives the stronger `P^ell(G)<=1`. Hence assume `G` contains a cycle.

Let `C` be the 2-core of `G`, obtained by repeatedly deleting leaves. Every vertex of `C` has degree two or three in `C`; moreover its degree-three vertices are still independent. If `C` has no degree-three vertex, then `C` is a cycle, so it has a proper pushing scheme with pushes at most two by Bensmail--Marcille--Orenga Theorem 3.4. We will later reattach the deleted forest. Thus the only new core case is when

\[
B:=\{b\in V(C):d_C(b)=3\}\ne\varnothing.
\]

Because `B` is independent, every component of `C-B` is a path of degree-two vertices whose two boundary incidences go to vertices of `B` (the two incidences may return to the same branch vertex). Write such a maximal chain as

\[
b_0,x_1,\dots,x_k,b_1,\qquad k\ge1.
\]

Set

\[
\rho(b)=3\qquad(b\in B).
\]

For a chain of length `k` (number of degree-two vertices), use the following word `w_k=(rho(x_1),...,rho(x_k))`:

\[
\begin{array}{c|c}
k&w_k\\ \hline
1&1\\
2&12\\
3&101\\
4&1011.
\end{array}
\]

For `k>=5`, put

\[
\begin{aligned}
w_{4t+1}&=1(0001)^t &&(t\ge1),\\
w_{4t+2}&=1(0001)^t1 &&(t\ge1),\\
w_{4t+3}&=1(0001)^t11 &&(t\ge1),\\
w_{4t}&=1(0001)^{t-1}021 &&(t\ge2).
\end{aligned}
\tag{3.1}
\]

All entries lie in `{0,1,2}` and both end entries are positive.

For a degree-two chain vertex, with the boundary convention `rho(b_0)=rho(b_1)=3`, its sum is

\[
\sigma(x_i)=2(1+\rho(x_i))+\rho(x_{i-1})+\rho(x_{i+1}).
\tag{3.2}
\]

We now check adjacent chain sums directly from (3.1). The short cases `k=1,2,3,4` give respectively

\[
(10),\qquad (9,10),\qquad (7,4,7),\qquad (7,4,5,8),
\]

so consecutive values differ. In a repeated block `0001`, away from the two global ends, the corresponding sums run through the alternating pattern

\[
3,2,3,4,
\]

and the junction to the next block is `4,3`. At the global left end the first sum is `7`. The four possible terminal corrections give:

- residue `1 mod 4`: the final `0001` ends with `...,3,7`;
- residue `2 mod 4`: the extra `1` gives `...,3,5,8`;
- residue `3 mod 4`: the two extra `1`'s give `...,3,5,6,8`;
- residue `0 mod 4`: the terminal `021` gives `...,3,4,5,7,9`.

Thus every pair of consecutive degree-two vertices on every chain has distinct sums. Also every degree-two sum is at most `14` (in fact the displayed construction never exceeds `10`).

Now consider a branch vertex `b in B`. It has degree three in `C`, push value three, and each of its three neighbors is a chain endpoint whose push is at least one. Therefore

\[
\sigma_C(b)=3(1+3)+\sum_{x\sim_C b}\rho(x)\ge12+3=15.
\tag{3.3}
\]

Every neighbor of `b` is degree two and has sum at most `14`, so every branch-chain edge is proper. There are no branch-branch edges because `B` is independent. Together with the chain check, this proves that `rho` is a proper 3-pushing scheme of the entire 2-core `C`.

It remains to reattach the forest deleted during 2-core pruning. The following extension lemma supplies this step.

### Leaf-extension lemma

Let `H` have a proper pushing scheme `rho:V(H)->{0,1,2,3}`. Let `u` be a nonisolated vertex of `H` with `d_H(u)<=2`, and let `H+uw` be obtained by attaching one new leaf `w` to `u`. Then `rho` extends to a proper `{0,1,2,3}`-valued pushing scheme of `H+uw`.

**Proof.** Keep all old pushes and set `rho(w)=x`. For every old vertex other than `u`, its sum is unchanged. At `u`,

\[
\sigma_{H+uw}(u)=\sigma_H(u)+(1+\rho(u))+x.
\tag{3.4}
\]

For each old neighbor `z` of `u`, equality `sigma_{H+uw}(u)=sigma_H(z)` forbids at most one integer value of `x`. There are at most two old neighbors, so at most two of the four choices `x in {0,1,2,3}` are forbidden.

For the new leaf,

\[
\sigma_{H+uw}(w)=1+x+\rho(u),
\]

and hence

\[
\sigma_{H+uw}(u)-\sigma_{H+uw}(w)=\sigma_H(u)>0,
\tag{3.5}
\]

because `u` is nonisolated. Thus the new leaf edge is automatically proper, independently of `x`. Choose any nonforbidden `x`. QED.

The vertices outside the 2-core form a forest rooted at the core. Add them in increasing distance from the core. Each new vertex is then a leaf attached to a currently nonisolated vertex of degree at most two, so the lemma applies at every step. The final scheme is a proper `{0,1,2,3}`-valued pushing scheme of `G`. This proves the theorem.

### Corollary — full subdivisions

If every edge of a subcubic graph is subdivided at least once, then in the resulting graph no two degree-three vertices are adjacent. Therefore every nice full subdivision of a subcubic graph satisfies BMO Conjecture 2.6 (using the already known maximum-degree-two case when the resulting maximum degree is at most two).

## 4. Exact validation after the proof idea

Only after writing the route did I add a small exact checker:

`artifacts/R20/bmo_independent_degree3_exact.py`

creation commit

`03eee4d28ce7130872cf3690079af0da96c8a177`.

It uses only integer arithmetic for the pushing sums. It performs two checks:

1. verifies the closed-form chain words and adjacent-sum inequalities for every `1<=k<=1000`;
2. applies the constructive 2-core/leaf-extension algorithm to every connected nice graph in NetworkX's complete unlabeled graph atlas through seven vertices that is subcubic and has independent degree-three vertices.

Executed output was archived at

`artifacts/R20/bmo_independent_degree3_exact.out`

commit

`19054e7ab15db86c57e4454f9d9da3b9cf309e90`.

The exact output is

```text
chain_templates_checked=1..1000
max_chain_sigma_seen=10
atlas_eligible_connected_nice_subcubic_independent_deg3=38
atlas_counts_by_order={1: 1, 3: 2, 4: 4, 5: 6, 6: 9, 7: 16}
atlas_failures=0
VERDICT=PASS
STATUS=SELF_CHECK_ONLY_PARTIAL_FOR_BMO_CONJECTURE_2_6
```

This checker is a self-check of the finite core and small instances. The infinite theorem rests on the proof above, not on testing 1000 chain lengths.

## 5. What moved and what did not

The frozen all-graphs metric is still

\[
\boxed{n_{\rm all}=9}.
\]

This run proves a new infinite structural class but does not certify *all* graphs on ten vertices, so changing `n_all` would be dishonest. The preceding run moved `8 -> 9` and reset stagnation to zero; this is therefore unchanged run 1 after that reset.

This result remains **PARTIAL** for Conjecture 2.6. It does not prove all subcubic graphs, let alone all nice graphs. No independent audit is claimed.

## 6. Why the route stops here, and the next route

The proof works because each degree-three branch is insulated from every other branch by at least one degree-two vertex. With branch push three and positive chain endpoint pushes, branch sums lie at least at 15 while all degree-two sums lie at most 14.

The first missing case is a direct edge between two degree-three vertices. On such an edge the `rho=3` branch values no longer separate automatically; their sums depend on the other two incident “port” values and can coincide. This is the exact obstruction to extending the current proof to all subcubic graphs.

A useful next parameter is

\[
a(G)=|E(G[V_3])|,
\]

where `V_3` is the degree-three vertex set. This run proves the `a(G)=0` case. The next run should attack `a(G)=1` completely before attempting arbitrary branch adjacency. The degree-two-chain analysis already shows that, for chains of length at least three, arbitrary positive endpoint port values can be connected; length one enforces equal endpoint ports and length two enforces unequal endpoint ports. That converts the next case into a small port-state gluing problem rather than another whole-graph census.

Next nonrepeating Section-B moves:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** use `a(G)` and prove the one-direct-branch-edge case;
- **#20 FIND WHY THE ALGORITHM FAILS:** classify exactly which endpoint-port patterns make a direct degree-three edge collide;
- **#27 SWAP THE QUANTIFIERS:** seek one finite port rule that works for every chain length/type, rather than choosing a global graph witness separately.

## 7. Scheduler/model-control status

The limitation recorded in the operations manifest is still true in this runtime. The exposed task-control interface offers title, prompt, schedule/timing mode and enabled state, but **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long execution setting**. Therefore the prompt request “GPT-6 / maximum” cannot be truthfully upgraded into a runtime claim here.

The historical P26 task-modification attempt returned `You cannot modify this task`. The legitimate workaround is an owner/admin-authorized product or backend context that owns the task and exposes the desired control; it is not a permission bypass or a duplicate schedule. A later authorized context was able to perform some task edits, so the old refusal should be read as authorization-context-specific, not as a mathematical blocker. No scheduler or permission changes were attempted in this run.

## 8. Structured `ledger_delta`

```yaml
ledger_delta:
  worker: R20
  source: "Bensmail--Marcille--Orenga, DMTCS 27:3 (2025), Conjecture 2.6"
  source_status_check_date: "2026-09-19"
  ownership: "R20 exclusive; operations/claims/BMO-2025-PUSHING-DELTA.md"
  stale_predecessor: "I0100 Paley one-localization remains retired/frozen in R20 history"
  metric: n_all
  before: 9
  after: 9
  movement: false
  unchanged_count_before: 0
  unchanged_count_after: 1
  status: "PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY"
  tried_moves: [4, 10, 28]
  results:
    - "proved on page: BMO Conjecture 2.6 for every nice subcubic graph whose degree-three vertices are independent"
    - "explicit closed-form degree-two-chain words for every chain length"
    - "proved leaf-extension lemma preserving max push 3"
    - "corollary: every nice full subdivision of a subcubic graph satisfies the source bound"
    - "exact checker PASS on chain lengths 1..1000 and all eligible connected graph-atlas instances through order 7"
  remaining_obligation: "prove Conjecture 2.6 for all nice graphs or produce an exact source-valid counterexample; immediate structural frontier is subcubic graphs with at least one direct degree-three/degree-three edge"
  evidence:
    idea_before_code: "361dfca2819e093110a47fd09a3b45915e523e0a"
    checker: "03eee4d28ce7130872cf3690079af0da96c8a177"
    executed_output: "19054e7ab15db86c57e4454f9d9da3b9cf309e90"
  audit_ids: []
  closure_claimed: false
```

**Bottom line:** a new constructive infinite-family theorem was obtained and exactly self-checked, but the fixed all-graphs metric remains `n_all=9`; the source conjecture remains PARTIAL/open-looking and unaudited.