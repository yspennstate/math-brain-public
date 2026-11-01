Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED — not GPT-6 maximum**. **MOVEMENT: `S_exact = 1 -> 2`; methods #5, #20, #25 genuinely attempted.**

# NM13-04 / P0457 — co-degree two via threshold degeneracy

Status: **OPEN / PARTIAL** relative to the source near-logarithmic diameter problem.

Exclusive claim remains `operations/claims/P0457.md` (owner NM13-04). No conflicting claim, handoff, release, retirement, or source-level closure was recovered this run.

Source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (2026), 552–579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Frozen source model: iid continuous edge weights on `K_n`; `LK(n,k)` keeps `{u,v}` iff the edge is among the `k` smallest incident weights at both endpoints.

Frozen metric, unchanged in definition from the admitted claim and previous report:

`S_exact = largest co-degree s >= 0 for which this track has a complete deterministic diameter classification for LK(n,n-1-s), valid for every n in the stated range.`

Before this run: `S_exact = 1`.
After this run: `S_exact = 2`.

The metric movement is supported by a full `s=2` classification below. The source's near-logarithmic problem is not solved.

---

## 1. Continuity and control surfaces read

I continued the existing P0457 assignment rather than reopening intake. I read the current controlling policy surfaces `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, and the later NM13 deployment amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the canonical claim `operations/claims/P0457.md`; the newest NM13-04 report `2026-09-17T21-20-42Z__p0457-k-nminus2-classification.md`; and neighboring NM13-03 and NM13-05 reports.

The canonical intake identity remains:

- ID `P0457`;
- dedup key `diameter_near_the_newly_established_bilateral_connectivity_threshold`;
- SHA256 `839d9617dd11661f03c25aa6c4d2e47c012b337f35570dde06ca7695f66ff561`;
- residue `3 mod 13`.

The campaign catalog still records the source as unsolved; the recovered older attempt used only the deterministic maximum-degree/Moore-volume lower bound and left matching upper behavior open. The previous NM13-04 run proved the complete co-degree-one (`k=n-2`) classification and exact disconnection probability, moving `S_exact` from 0 to 1. I do not recount that as new progress.

Large repository roots are connector-truncated surfaces rather than byte-for-byte dumps; exact target, claim, and report files were read directly, and exact-ID/dedup searches were used for continuity. No inaccessible history is treated as permission to reset a baseline.

The exposed scheduler/task-edit schema still has no binding model-family or reasoning-effort field. `GPT-6 / maximum` remains prompt text only. This invocation actually identifies as GPT-5.6 Sol; reasoning telemetry is unavailable, so the level is UNVERIFIED. Repository policy records that a task returning `You cannot modify this task` requires the owning account/workspace or another authorized product/admin surface; a duplicate scheduler or repository workaround is not legitimate.

---

## 2. Fresh source and literature status check — 2026-09-17 UTC

The Cambridge source page was checked again. It still explicitly states as future work the problem of characterizing the diameter in the additional `k(n)` range covered by the improved connectivity theorem. The source model and the open-problem wording remain source-matching for P0457.

Bounded fresh searches used the exact paper title, both authors, `bilateral preference random graph diameter`, `LK(n,k) diameter`, `LK(n,n-3)`, and `bilateral preference graph degeneracy`. They recovered the published paper / earlier preprint and generic mutual-nearest-neighbor material, but no later paper resolving the source diameter question and no located source-specific theorem matching the threshold-degeneracy result below.

This is a dated bounded search, not proof of worldwide openness or a novelty certificate. In particular, the degeneracy mechanism may be elementary folklore once the high-degree complement is written in threshold form; no novelty beyond the bounded search is claimed.

---

## 3. Set-up for a co-degree parameter

Write

`k = n-1-s`, with `1 <= s <= n-2`.

At each vertex `v`, exactly the `s` largest incident edge weights are rejected. Let `R_v` be this rejected set, let

`G_s = LK(n,n-1-s)`,

and let

`H_s = complement(G_s)`

inside `K_n`.

Thus an edge belongs to `H_s` iff at least one endpoint rejects it.

For each vertex `v`, let `tau_v` be its `s`-th largest incident edge weight. Distinctness gives the exact threshold rule

`uv in H_s  <=>  W_uv >= tau_u or W_uv >= tau_v`.

This parameterization is the new route. For `s=1`, the previous run obtained a forest from a functional digraph. That forest statement is false at `s=2`; triangles are realizable. The correct invariant is degeneracy rather than acyclicity.

---

## 4. Method #5 — add the co-degree parameter and follow the invariant

### Theorem P0457-DEGEN

For every distinct-weight realization and every `1 <= s <= n-2`, the missing-edge graph

`H_s = complement(LK(n,n-1-s))`

is `s`-degenerate.

Equivalently, every nonempty induced subgraph of `H_s` has a vertex of degree at most `s`.

### Proof

Take any nonempty vertex set `S`. Choose `v in S` minimizing `tau_v` over `S`.

If `u in S` is adjacent to `v` in `H_s`, then by the threshold rule either

`W_uv >= tau_v`

or

`W_uv >= tau_u`.

But minimality gives `tau_u >= tau_v`, so in either case

`W_uv >= tau_v`.

Exactly `s` edges incident to `v` have weight at least `tau_v`, because weights are distinct and `tau_v` is the `s`-th largest incident weight. Therefore `v` has at most `s` neighbors inside `H_s[S]`.

Since `S` was arbitrary, `H_s` is `s`-degenerate. QED.

### Checks against the previous theorem

For `s=1`, 1-degenerate graphs are forests, so P0457-DEGEN recovers the structural core of the previous run by a shorter threshold proof.

For `s=2`, triangles are allowed but no induced subgraph can have minimum degree at least 3. This is exactly the replacement needed after the forest invariant failed.

---

## 5. Source-relevant consequence: a deterministic diameter bound

### Theorem P0457-DIAM-BOUND

If `G_s = LK(n,n-1-s)` is connected, then

`diam(G_s) <= s+2`.

### Proof

Let

`x_0, x_1, ..., x_d`

be a geodesic of length `d` in `G_s`. A shortest path is induced: if `|i-j|>=2`, then `x_i x_j` cannot be an edge of `G_s`, because that chord would shorten the path.

Hence the subgraph of `H_s` induced by these `d+1` vertices is exactly the complement of the path `P_{d+1}`. Its two endpoint vertices have degree `d-1` inside that induced complement, and each internal path vertex has degree `d-2`. Therefore the induced subgraph has minimum degree `d-2`.

But P0457-DEGEN says every induced subgraph of `H_s` has a vertex of degree at most `s`. Thus

`d-2 <= s`,

so

`d <= s+2`.

QED.

For `s=1` this gives diameter at most 3, agreeing with the previous exact classification. For `s=2` it gives diameter at most 4.

The bound is sharp already at `s=2`: Section 8 records an exact `n=6,k=3` source ordering with diameter 4.

---

## 6. Method #20 — identify exactly why the old algorithm fails, then repair it

The previous run's `s=1` recognition procedure relied on the missing graph being a forest. At `s=2`, that route fails at the first structural step: an exact source ordering can make `H_2` contain a triangle.

The failure is now precise. Acyclicity was stronger than necessary. What survives is the threshold-minimum argument proving 2-degeneracy, and 2-degeneracy is exactly strong enough to cap connected diameter at four.

This produces a complete radius-four local classifier rather than an all-pairs shortest-path computation.

For the remainder of the run set

`G = LK(n,n-3)`, `H = complement(G)`, so `s=2` and `n>=4`.

For each missing edge `uv in H`, define

`A_uv = N_G(u)`,
`B_uv = N_G(v)`.

Because `uv` is missing, any path from `u` to `v` has length at least two.

### Theorem P0457-S2-CLASS — complete deterministic co-degree-two classification

For every distinct-weight realization of `LK(n,n-3)`:

1. `H` is 2-degenerate.
2. If `G` is disconnected, its largest connected component has at least `n-2` vertices. Therefore its component-size pattern is one of
   - `(n-1,1)`,
   - `(n-2,2)`,
   - `(n-2,1,1)`,
   with empty/degenerate repetitions omitted for very small `n`.
3. If `G` is connected, then `diam(G)` is exactly 2, 3, or 4 and is determined as follows:
   - `diam(G)=2` iff for every `uv in H`, `A_uv intersect B_uv` is nonempty;
   - `diam(G)=4` iff for some `uv in H`, `A_uv intersect B_uv` is empty and there is **no** `G`-edge joining `A_uv` to `B_uv`;
   - in every remaining connected case, `diam(G)=3`.

### Proof

Part 1 is P0457-DEGEN with `s=2`.

For Part 2, suppose the connected components of `G` have sizes `n_1,...,n_r`, and let `M=max_i n_i`. Every pair of vertices lying in different `G`-components is a missing edge, so `H` contains the complete multipartite cross-component graph with these parts. In that cross-component graph, every vertex of a largest part has degree `n-M`, so its minimum degree is at least `n-M`. Since this graph is a subgraph of the 2-degenerate graph `H`, it cannot have minimum degree greater than 2. Hence

`n-M <= 2`,

or `M>=n-2`. The listed component-size patterns are exactly the partitions of `n` with at most two vertices outside the largest component.

Now assume `G` connected. P0457-DIAM-BOUND gives `diam(G)<=4`.

Take any missing pair `uv in H`. A length-two path `u-w-v` exists exactly when `w` is a common `G`-neighbor, i.e. exactly when

`A_uv intersect B_uv != empty`.

If this intersection is empty, then a length-three path from `u` to `v` exists exactly when there are `a in A_uv` and `b in B_uv` with `ab in G`, i.e. exactly when at least one `G`-edge joins `A_uv` to `B_uv`.

Therefore:

- if every missing pair has a common `G`-neighbor, all vertex pairs have distance at most two; since `H` is nonempty for `s=2`, the diameter is exactly two;
- if some missing pair has no common neighbor and also no `G`-edge from `A_uv` to `B_uv`, that pair has distance at least four, hence exactly four by the universal bound;
- otherwise some missing pair has distance exactly three and no pair has distance four, so the graph diameter is exactly three.

QED.

This is a complete deterministic classifier for every co-degree-two source realization, hence it advances the frozen metric to

`S_exact = 2`.

It remains a high-degree special theorem, far from the unresolved near-logarithmic source range.

---

## 7. Method #25 — count the rejection budget twice

Before the threshold-degeneracy invariant emerged, I tried to control `H_s` only by counting rejected incidences.

Every vertex rejects exactly `s` incident edges, so there are exactly `ns` directed rejection marks. Every missing undirected edge receives one or two marks. Hence

`ns/2 <= |E(H_s)| <= ns`.

For `s=2`, this gives

`n <= |E(H)| <= 2n`.

This count is useful as a consistency check and gives crude restrictions on complete cuts, but it is **not** strong enough to prove the diameter theorem. For example, a hypothetical six-vertex length-five geodesic would force the complement of `P_6`, which has 10 missing edges, still within the budget `|E(H)|<=12`. Thus edge counting alone does not exclude diameter five.

The failed counting route was informative: it isolated that the missing ingredient had to control **minimum degree inside every induced subgraph**, not merely the total number of missing edges. The threshold parameter `tau_v` supplies exactly that stronger invariant.

---

## 8. Exact sharpness witnesses and finite self-check

The mathematical proof above was written before the checker. The checker is a self-check, not an independent audit.

Checker:
`proofnet24/NM13-04/artifacts/2026-09-17/2026-09-17T22-18-29Z__p0457_s2_degeneracy_check.py`

creation commit `d14a4e1448bdf59f520954ce1243048c1b26e5b3`, read back at that commit, blob `9a163dad10038e2590070d78121d6dac77af9890`.

Output:
`proofnet24/NM13-04/artifacts/2026-09-17/2026-09-17T22-18-29Z__p0457_s2_degeneracy_check.out`

creation commit `ccefe30860972acb8b81c04bb3293c440e40b169`, read back at that commit, blob `f7ba8485558a6c24c18e433a0f316fd5461c2387`.

### What was exhaustively checked

For `s=2`, a local rejection profile chooses two rejected incident edges at each vertex. Such a profile is realizable by distinct global edge weights iff the strict comparisons

`every rejected incident edge > every nonrejected incident edge at the same vertex`

form an acyclic comparison digraph. A topological extension then gives an exact realizing total edge order. Thus the checker enumerates local profiles rather than treating arbitrary inconsistent choices as source realizations.

It exhaustively tested:

- `n=5`: all `6^5 = 7776` local profiles, of which `3282` are globally realizable;
- `n=6`: all `10^6 = 1,000,000` local profiles, of which `272860` are globally realizable.

For every realizable profile it independently computed the complement degeneracy, connected components, BFS diameter, and the local classifier in Theorem P0457-S2-CLASS.

Results:

- maximum observed `H` degeneracy was exactly 2 for both `n=5` and `n=6`;
- theorem/classifier mismatches: `0`;
- `n=5` realizes connected diameters 2 and 4 and the three allowed disconnected size types;
- `n=6` realizes connected diameters 2, 3, and 4 and all three allowed disconnected size types.

The counts in the archived output are counts of **realizable local rejection profiles**, not source probabilities; profiles are not equiprobable under a uniformly random global edge ordering.

The output terminates

`ALL_EXACT_CHECKS_PASS`.

### Explicit diameter-four source witness

For `n=6`, list the 15 edge weights from smallest to largest in the order

`25 < 15 < 12 < 35 < 14 < 46 < 45 < 34 < 56 < 16 < 23 < 24 < 13 < 36 < 26`.

With `k=3=n-3`, each vertex rejects its two largest incident edges. The resulting source graph has edges

`12, 14, 15, 23, 25, 35, 46`.

Vertices 3 and 6 have graph distance four. Thus the universal co-degree-two upper bound 4 is sharp within the exact source model.

The checker also archives explicit `n=6` source orderings realizing diameter 2, diameter 3, and disconnected component sizes `(5,1)`, `(4,2)`, `(4,1,1)`.

---

## 9. Why this counts as `S_exact=2` but not source closure

The frozen metric asks for a complete deterministic diameter classification in the exact high-degree slice `LK(n,n-1-s)`. For `s=2`, Theorem P0457-S2-CLASS covers every realization and every `n>=4`: disconnected cases have a proved component-size restriction, while connected cases are exactly classified as diameter 2, 3, or 4 by the stated neighborhood tests. Hence `S_exact` genuinely moves from 1 to 2 without changing its definition.

The source problem is much broader: it asks for diameter in an additional **near-logarithmic** connectivity range. Nothing here proves the asymptotic diameter there. In particular, the general bound `diam <= s+2` becomes useless when `s=n-1-k` is of order `n` in that regime.

So the correct status remains **OPEN / PARTIAL**.

No P26 or NM13-05 audit is claimed. No paper folder is warranted yet because the source statement is not closed.

---

## 10. Method ledger

### #5 — ADD A PARAMETER AND DIFFERENTIATE / TRACK IT

Attempted by replacing the isolated `s=1` argument with the co-degree family `k=n-1-s` and introducing the threshold `tau_v`. This succeeded: the missing graph is `s`-degenerate for every `s`, yielding `diam <= s+2` whenever the source graph is connected. For `s=2` this supplied the structural input needed for full classification.

### #20 — FIND WHY THE ALGORITHM FAILS

The previous forest algorithm fails because `s=2` missing graphs can contain triangles. The precise repair is to replace acyclicity by 2-degeneracy and then use the radius-four local test on each missing edge. This succeeded and yields a complete deterministic co-degree-two classifier.

### #25 — COUNT THE SAME THING TWICE

Counted the `ns` directed rejection marks against missing undirected edges, obtaining `ns/2 <= |H_s| <= ns`. This did not by itself move the metric: it is too weak to rule out a length-five geodesic at `s=2`. The failure identified why an induced-subgraph invariant rather than a global edge count was required.

All three methods were genuinely attempted; this triple differs from the previous run's #2/#14/#19.

---

## 11. Counter/status bookkeeping

Previous value: `S_exact=1`.
Current value: `S_exact=2`.
Movement: YES.

Previous unchanged-run count: 0 after movement.
Current unchanged-run count: 0 after movement.
Stuck-recovery count: 0.

No rotation condition is triggered.

---

## 12. Next mathematical attack

Do not repeat #5/#20/#25 next run.

The general `s`-degeneracy theorem suggests two sharply different continuations. The high-degree metric now requires `s=3` for another movement, but blindly extending the radius-four classifier to radius five risks becoming bookkeeping rather than source-relevant research. The better route is to ask whether the threshold ordering gives a **stronger property than `s`-degeneracy** that survives when `s` is large enough to say something nontrivial about the source's connectivity window.

Suggested next Section-B triple:

- #18 SAY IT IN ANOTHER LANGUAGE: reinterpret `H_s` as a threshold-union / elimination-order object and compare it with known sparse graph classes;
- #24 FIND THE EXTREMAL OBJECT: determine the realizable missing graph maximizing connected diameter at fixed `(n,s)` and whether the `s+2` bound is globally sharp;
- #30 ONE SCALE / ONE DIRECTION AT A TIME: isolate a regime such as fixed `s` first, then identify exactly which step breaks when `s` grows with `n`.

A concrete next theorem would be an exact extremal construction matching `s+2` for all fixed `s` (or a strictly smaller source-specific bound), followed by an assessment of whether that structure can be translated into a bound in an overlapping growing-`s` regime. If not, record the high-degree result as a complete restricted theorem and switch methods rather than manufacturing more certificates.

---

## 13. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-04
  category: CLOSABLE_OUTSIDE
  target: P0457
  canonical_claim: operations/claims/P0457.md
  source: Dabirian-Subramanian bilateral preference diameter open problem
  metric: S_exact
  metric_definition: largest co-degree s with complete deterministic diameter classification for LK(n,n-1-s)
  before: 1
  after: 2
  movement: true
  mathematical_status: PARTIAL
  source_status: OPEN_BOUNDED_CURRENT_SEARCH
  new_claims:
    - P0457-DEGEN: complement of LK(n,n-1-s) is s-degenerate for every fixed realization
    - P0457-DIAM-BOUND: connected LK(n,n-1-s) has diameter at most s+2
    - P0457-S2-CLASS: complete deterministic classification for co-degree two
  methods_actually_tried: [5, 20, 25]
  exact_checker: proofnet24/NM13-04/artifacts/2026-09-17/2026-09-17T22-18-29Z__p0457_s2_degeneracy_check.py
  exact_output: proofnet24/NM13-04/artifacts/2026-09-17/2026-09-17T22-18-29Z__p0457_s2_degeneracy_check.out
  exact_output_terminal: ALL_EXACT_CHECKS_PASS
  finite_scope_checked:
    n5_total_profiles: 7776
    n5_realizable_profiles: 3282
    n6_total_profiles: 1000000
    n6_realizable_profiles: 272860
    classifier_mismatches: 0
  unchanged_run_count: 0
  stuck_recovery_count: 0
  audits:
    P26: NOT_REQUESTED_OR_PASSED
    NM13-05: NOT_REQUESTED_OR_PASSED
  next_methods: [18, 24, 30]
  next_step: test extremal sharpness and stronger threshold-union structure before attempting s=3 bookkeeping
  shared_roots_edited: false
  peer_files_edited: false
```

No shared root, peer file, email, Drive item, public post, workflow, permission setting, or schedule was modified.

**End of complete run report.**
