Model actually run: **GPT-5.6 Sol**. Reasoning/effort: **UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but the available scheduler interface still has no binding model-family or reasoning-effort selector. **MOVEMENT: `S_exact = 0 -> 1`; methods B2, B14, B19 genuinely attempted.**

# NM13-04 / P0457 — exact high-degree diameter classification for bilateral-preference graphs

Status: **OPEN / PARTIAL** relative to the source near-logarithmic diameter problem.

Exclusive claim: `operations/claims/P0457.md`, creation commit `1e958e64925500d0c7792408a42141d51b5f80a0`, read back at that commit.

Source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (2026), 552–579, DOI `10.1017/jpr.2025.10051` (published online 18 December 2025).

Exact source question used here: characterize the diameter of the bilateral-preference graph `LK(n,k)` in the additional near-logarithmic range of `k(n)` in which the source's Theorem 6 establishes connectivity. The theorem below is a source-model special regime, **not** a solution of that near-logarithmic asymptotic question.

Frozen metric: `S_exact`, the largest co-degree `s >= 0` for which this track has a complete deterministic diameter classification for the exact source family `LK(n,n-1-s)`, valid for every `n` in the stated range. Admission baseline `S_exact=0` is supported because `LK(n,n-1)=K_n` deterministically. This run proves the full `s=1` classification, hence `S_exact=1`.

---

## 1. Continuity, exclusions, source status, history, and ownership

I reread the current fleet rules and owner new-methods directive, root `POSTED.md`, the campaign `INDEX.md` and `RANKING.md`, the canonical probability-campaign catalog, current ownership surfaces, and neighboring Lovasz/random-graph work before admitting a target.

Two shard-3 screening points mattered:

1. `P0014`, the random-circulant Lovasz-theta conjecture, has the correct shard residue but is **not unassigned**. It is the historical alias of the live exclusive target `RS-2025-TH18`; its latest recovered report says that claim remains canonical and must be handed off/rotated by its owning native slot rather than stolen here. I therefore did not claim it.
2. `P0457` has canonical dedup key `diameter_near_the_newly_established_bilateral_connectivity_threshold` with SHA256 `839d9617dd11661f03c25aa6c4d2e47c012b337f35570dde06ca7695f66ff561`, whose integer value is `3 mod 13`. Immediately before the create-only claim, `operations/claims/P0457.md` was absent; exact-ID and dedup searches recovered catalog/ranking history but no current owner or assignment.

The old P0457 campaign attempt is recovered rather than erased. It used only the deterministic maximum-degree/Moore-volume inequality to get a lower bound of order `log n / log k` and explicitly left a matching upper bound and limiting diameter behavior open. No proof file was recorded for a stronger source result.

### Fresh literature/status check — 2026-09-17 UTC

The published Cambridge source currently states the diameter problem explicitly as future work: the earlier La–Kabkab method determines diameter only in a coarser range, and the source asks for the diameter in the additional range covered by its improved connectivity theorem. The same published article records the exact `LK(n,k)` construction by iid continuous edge weights and bilateral top-`k` preferences.

Bounded fresh searches for the exact paper title, authors, `bilateral preference random graph diameter`, and later 2026 work recovered the source publication and its connectivity/mean-degree results but no later source-matching diameter resolution. This is a dated bounded search, **not** a novelty certificate and not proof of worldwide openness.

The current runtime task surface still exposes no model selector or reasoning-effort selector. Thus GPT-6 / maximum remains prompt text only; changing it requires an authorized product/scheduler surface that actually exposes those controls. I did not attempt any permission bypass or duplicate task creation.

---

## 2. Exact source model

Let the complete graph `K_n` have iid continuous edge weights `(W_e)`. For each vertex `v`, rank the `n-1` incident edges from smallest to largest weight. The source graph `LK(n,k)` retains an edge `{u,v}` if and only if that edge lies among the `k` smallest incident edges at **both** endpoints.

Continuity of the weights implies that all incident rankings are strict almost surely. Everything below is deterministic conditional on any realization with distinct edge weights, so the distribution need only be used for the final exact probability formula.

For this run set

`k=n-2`.

Thus each vertex rejects exactly its single largest-weight incident edge.

Write `G=LK(n,n-2)` and let `H=\bar G` be its missing-edge graph inside `K_n`.

---

## 3. B2 — attack the negation first

A tempting high-degree strengthening is:

> if `G=LK(n,n-2)` is connected, then `diam(G)=2`.

This is false. Take vertices `u,v`, split the other vertices into two nonempty sets `A,B`, make `W_{uv}` the largest edge weight, make the edges `u-a` (`a in A`) and `v-b` (`b in B`) the next-highest designated incident weights, and make all other edges smaller. Then the missing graph `H` is the spanning double-star with center edge `uv`, leaves `A` attached to `u`, and leaves `B` attached to `v`. In `G`, the pair `u,v` is nonadjacent and has no common neighbor, but a length-three path exists through one leaf from each side. Hence `diam(G)=3`.

This is **not a refutation of the source question**, which asks for a characterization rather than asserting diameter two. It is a diagnostic counterexample that identifies the exact obstruction the proof must classify.

---

## 4. B14 — the hidden functional-digraph structure

For each vertex `v`, let `f(v)` be the unique neighbor joined to `v` by its largest-weight incident edge. Since `k=n-2`,

`{u,v} in E(H)` iff `f(u)=v` or `f(v)=u`.

Orient one arc `v -> f(v)` from every vertex. This is a functional digraph with outdegree one and no loops.

### Lemma 1 — no directed cycle of length at least three

There is no directed cycle

`v_1 -> v_2 -> ... -> v_r -> v_1`

with `r>=3`.

**Proof.** Put `e_i={v_i,v_{i+1}}` with indices modulo `r`. Since `f(v_i)=v_{i+1}`, edge `e_i` is the unique maximum-weight edge incident to `v_i`. In particular

`W_{e_i} > W_{e_{i-1}}`.

Going around the cycle gives

`W_{e_1}>W_{e_r}>...>W_{e_1}`,

a contradiction. `□`

Every finite functional-digraph component contains a directed cycle. Because loops are impossible and Lemma 1 excludes cycles of length at least three, every component has exactly one directed 2-cycle. After forgetting orientation, the two reciprocal arcs become one edge. A weak component on `q` vertices therefore has exactly `q-1` distinct undirected edges and is connected.

### Corollary 2 — the missing graph is a forest

For every distinct-weight realization,

`H=\overline{LK(n,n-2)}`

is a forest. Each component is a tree whose functional orientation points toward a distinguished central 2-cycle edge.

This is the structural step that the generic maximum-degree argument does not see.

---

## 5. Exact diameter classification

### Theorem 3 — complete `k=n-2` classification

Let `n>=3` and let the source edge weights be distinct. Set `G=LK(n,n-2)` and `H=\bar G`. Then:

1. `H` is a forest.
2. `G` is disconnected **iff** `H` is the spanning star `K_{1,n-1}`.
3. Conditional on `G` being connected, `diam(G)=3` **iff** `H` is a spanning non-star double-star: there is an edge `uv` such that every other vertex is adjacent in `H` to exactly one of `u,v`, and both `u` and `v` have at least one leaf.
4. In every other connected case, `diam(G)=2`.

**Proof.** Part 1 is Corollary 2.

For Part 2, suppose `G` is disconnected. Take a nontrivial vertex partition `V=A disjoint-union B` with no `G`-edge crossing it. Then every one of the `|A||B|` crossing pairs is an edge of `H`. Since `H` is a forest,

`|A||B| <= |E(H)| <= n-1`.

For positive integers `|A|+|B|=n`, one has `|A||B|>=n-1`, with equality only when one side has size one. Thus equality holds throughout, one side is a singleton, and `H` consists of exactly all `n-1` edges from that singleton to the other vertices: a spanning star. Conversely, if `H` is a spanning star, its center is isolated in `G`, so `G` is disconnected.

Now assume `G` is connected. If `u,v` are adjacent in `G`, their distance is one. Consider a nonadjacent pair, so `uv in E(H)`. They fail to have a common `G`-neighbor exactly when every `w notin {u,v}` is joined in `H` to at least one of `u,v`. Because `H` is a forest and already contains `uv`, no such `w` can be joined in `H` to both `u` and `v`, since that would form a triangle. Therefore the `n-2` remaining vertices are partitioned between the `H`-neighborhoods of `u` and `v`. Together with `uv`, this already accounts for `n-1` edges, so the forest has no further edge: it is a spanning double-star.

If all leaves lie on only one side, the double-star is a star and `G` is disconnected, contrary to assumption. Hence in the connected exceptional case both sides are nonempty. Pick `a` attached to `u` in `H` and `b` attached to `v` in `H`. Then `u-b`, `b-a`, and `a-v` are all edges of `G`, giving a length-three path from `u` to `v`. Since no length-two path exists, `d_G(u,v)=3`.

If `H` is not such a double-star, every nonadjacent pair in `G` has a common `G`-neighbor, so every pair has distance at most two. Because `H` is nonempty when `k=n-2`, the connected graph is not complete, and its diameter is exactly two. `□`

Thus the supported metric moves

`S_exact: 0 -> 1`.

This is a complete theorem for a source-model parameter regime, but `n-2` is far from the source's unresolved near-logarithmic range. The parent problem remains **OPEN / PARTIAL**.

---

## 6. Exact finite disconnection probability

The forest theorem also gives a closed finite-`n` source probability.

### Theorem 4 — exact connectivity failure at `k=n-2`

For iid continuous source weights and every `n>=3`,

`P(LK(n,n-2) is disconnected) = 2^(n-1) n! / (2n-2)!`.

**Proof.** By Theorem 3, disconnection is exactly the event that `H` is a spanning star. Fix a prospective center `c` and write `m=n-1`. By the probability-integral transform we may take all edge weights uniform on `[0,1]` without changing rankings. For each leaf `i`, put `x_i=W_{ci}`.

The missing graph is the star centered at `c` exactly when, for every pair of leaves `i<j`,

`W_{ij}<min(x_i,x_j)`.

Conditional on the star-edge weights, independence gives probability

`prod_{i<j} min(x_i,x_j)`.

Hence the probability for this fixed center is

`I_m = integral_[0,1]^m prod_{i<j} min(x_i,x_j) dx`.

Order the variables `0<x_1<...<x_m<1` and multiply by `m!`. On this chamber the product equals

`prod_{r=1}^m x_r^(m-r)`.

Successive integration gives denominators

`D_j = sum_{r=1}^j (m-r) + j = j(2m-j+1)/2`,

so

`I_m = m! / prod_{j=1}^m D_j = 2^m m!/(2m)!`.

For `n>=3` the star events for distinct centers are disjoint. Multiplying by `n` and substituting `m=n-1` yields

`n * 2^(n-1)(n-1)!/(2n-2)! = 2^(n-1)n!/(2n-2)!`. `□`

For example, at `n=4,k=2` this gives disconnection probability `4/15`.

---

## 7. B19 — make the structural theorem an exact algorithm

The proof gives an exact recognition algorithm for a realized `LK(n,n-2)` instance.

1. Scan each vertex's incident weights and record its unique maximum edge; this constructs `H` in `O(n^2)` time from the complete weight table.
2. If one vertex has `H`-degree `n-1`, report `DISCONNECTED`.
3. Otherwise, if some `H`-edge `uv` satisfies `deg_H(u)+deg_H(v)=n`, both degrees are at least two, and every other vertex has `H`-degree one, report `DIAMETER 3`.
4. Otherwise report `DIAMETER 2`.

No all-pairs shortest-path computation is needed. The algorithm is simply the theorem's obstruction test; it does not address the near-logarithmic asymptotic range.

---

## 8. Exact self-check and adversarial tests

I wrote the idea and proof before code. The checker is a **self-check**, not an independent audit and not the proof of Theorems 3–4.

Checker:
`proofnet24/NM13-04/artifacts/2026-09-17/2026-09-17T21-20-42Z__p0457_k_nminus2_check.py`
creation commit `ce26dad9e25014fa7ab2fdc8a9a2cfac850f42b5`, read back at that commit.

Output:
`proofnet24/NM13-04/artifacts/2026-09-17/2026-09-17T21-20-42Z__p0457_k_nminus2_check.out`
creation commit `97d7a2d9e6e0653493b522c81eaa1699ebb4390c`, read back at that commit.

Executed exact results:

- `n=3`: all `3!=6` edge orders are disconnected, matching the theorem and exact formula.
- `n=4`: all `6!=720` edge orders were exhausted: `144` give diameter 2, `384` give diameter 3, and `192` are disconnected. Thus the exact source probabilities are `1/5`, `8/15`, and `4/15`, respectively.
- Explicit `n=5` rank orders realize all three structural outcomes: star/disconnected, non-star double-star/diameter 3, and diameter 2.
- The tempting forest invariant does **not** extend automatically to co-degree `s=2`: an exact `n=5,k=2` ordering makes the missing graph contain a triangle.
- Output terminates `ALL_EXACT_CHECKS_PASS`.

The last obstruction matters for the next run: renaming the forest proof as an induction in `s` would be false.

---

## 9. Method ledger

### B2 — ATTACK THE NEGATION FIRST
Tried to refute the natural high-degree strengthening `connected => diameter 2`. Succeeded: a realizable non-star double-star missing graph gives diameter exactly 3. This did not refute the source question; it exposed the exact exceptional geometry.

### B14 — FIND THE GROUP ACTING / symmetry reduction
Used the full vertex-label exchangeability of the source ensemble after identifying the functional-digraph invariant. The `n` possible star centers have equal probability, reducing the exact disconnection calculation to one center. More importantly, quotienting the local rejection rule to the one-out functional digraph makes the impossible long-cycle structure visible.

### B19 — MAKE IT AN ALGORITHM
Converted the proof into the exact maximum-edge / missing-forest recognition algorithm above, and independently self-checked every edge ordering through `n=4` plus three `n=5` witnesses.

All three assigned methods were genuinely attempted; none is reported merely because it was scheduled.

---

## 10. What this does and does not establish

**PROVED in this report:**

- exact forest structure of `\overline{LK(n,n-2)}`;
- exact disconnected / diameter-3 / diameter-2 structural classification;
- exact finite-`n` formula `P(disconnected)=2^(n-1)n!/(2n-2)!`;
- exact `n=4` diameter distribution by exhaustive self-check.

**NOT proved:**

- any matching upper bound in the source's additional near-logarithmic connectivity range;
- a limiting diameter constant near `k ~ log n`;
- an extension of the forest invariant to `k=n-3` (the checker gives a triangle obstruction);
- source closure, publication novelty, or either required independent audit.

The source problem therefore remains **OPEN / PARTIAL**.

Metric: `S_exact = 0 -> 1`.
Unchanged-run count on admitted P0457: `0` (movement this run).
Stuck-recovery count: `0`.

---

## 11. Exact remaining obligation and next attack

The source-relevant obligation is still to control graph distances in the newly connected regime around logarithmic `k`, where edge dependencies invalidate a naive transfer of the older embedded-Erdos-Renyi diameter proof.

The next run should not repeat B2/B14/B19. Proposed next triple:

- **B5**: introduce co-degree / preference-budget as a parameter and identify a monotone or differentiable quantity tied to two-step neighborhood growth;
- **B20**: start from the exact failure of the `s=1` forest algorithm at `s=2` and isolate the weakest replacement invariant (for example the orientation with bounded outgoing missing edges) that survives general `s`;
- **B25**: double-count source-valid two-step paths/common neighbors under the bilateral ranking rule, aiming for a quantitative expansion estimate rather than an independent-edge surrogate.

A useful next theorem would be a nontrivial common-neighbor lower bound under an explicit `k(n)` range that overlaps the source's Theorem 6 connectivity window. If that route cannot reach the window, it must be recorded as a restricted theorem rather than promoted to source progress.

No NM13-05 or P26 audit is requested yet because the source question is not closure-ready. The theorem-sized restricted claim is fully proved on this page; future audit may be worthwhile only if it becomes part of a source-matching package.

---

## ledger_delta for P26

```yaml
track: NM13-04
claim_id: P0457
category: CLOSABLE_OUTSIDE
source: Dabirian--Subramanian bilateral preference graph diameter open problem
metric: S_exact
before: 0
after: 1
movement: true
status: PARTIAL
methods_tried: [2, 14, 19]
new_claims:
  - P0457-KNMINUS2-FOREST-DIAMETER-CLASSIFICATION-01
  - P0457-KNMINUS2-DISCONNECTION-PROBABILITY-02
exact_artifacts:
  checker: proofnet24/NM13-04/artifacts/2026-09-17/2026-09-17T21-20-42Z__p0457_k_nminus2_check.py
  output: proofnet24/NM13-04/artifacts/2026-09-17/2026-09-17T21-20-42Z__p0457_k_nminus2_check.out
  output_terminal: ALL_EXACT_CHECKS_PASS
unchanged_runs: 0
stuck_recoveries: 0
outside_audits: 0
remaining_obligation: source-near-logarithmic diameter upper bound / characterization
shared_roots_edited: false
```

**End of complete run report.**
