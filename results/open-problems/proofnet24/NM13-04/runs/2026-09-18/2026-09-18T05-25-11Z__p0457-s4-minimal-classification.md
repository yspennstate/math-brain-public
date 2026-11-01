Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-METRIC MOVEMENT: `S_exact = 3 -> 4`. Section-B methods actually tried: #10, #16, #26.**

# NM13-04 / P0457 — exact co-degree-four classifier and minimal-order sporadic class

Run UTC: 2026-09-18T05:25:11Z  
Track: `NM13-04 Graph Counterexamples`, CLOSABLE OUTSIDE  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Canonical source/claim: `P0457`, `operations/claims/P0457.md`

## 1. Runtime, continuity, ownership, and required reads

The requested `GPT-6 / maximum` remains prompt text only. The exposed task-control surface provides prompt/title, schedule/timing, enabled state and timing mode, but **no bindable model-family selector, no reasoning-effort selector, and no authenticated per-run applied-effort telemetry**. This invocation therefore reports the model actually exposed to it, GPT-5.6 Sol, with reasoning level `UNVERIFIED`; it does not claim GPT-6 maximum. The historical P26 `You cannot modify this task` response remains an authorization-context boundary. `RESULTS.md` records a later successful P26 update from another authorized context, so the legitimate workaround is the owning/authorized account/workspace/product/admin/API surface or platform support, not task duplication or access-control bypass. No support escalation is claimed here.

This invocation continued the already admitted P0457 source. Intake was **not** reopened and no second claim was created.

Canonical identity remains:

- campaign ID: `P0457`;
- canonical dedup key: `diameter_near_the_newly_established_bilateral_connectivity_threshold`;
- SHA256: `839d9617dd11661f03c25aa6c4d2e47c012b337f35570dde06ca7695f66ff561`;
- residue: `3 mod 13`, matching NM13-04's exclusive selection shard;
- source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (2026), 552–579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025;
- exact source question: characterize the diameter of `LK(n,k)` in the additional range of `k(n)` from the paper's Theorem 6 where connectivity holds;
- owner: NM13-04 under create-only canonical claim `operations/claims/P0457.md`.

Before new mathematics I reread/recovered the required current state from `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the canonical P0457 claim; exact-ID/dedup ownership and historical attempt surfaces; the newest own report `proofnet24/NM13-04/runs/2026-09-18/2026-09-18T04-16-59Z__p0457-two-round-capacity-attachment.md`; the newest visible neighboring NM13-03 admission report; and the newest visible neighboring NM13-05 D0004 report. Large aggregate files can be connector-truncated, so exact-path/exact-ID/dedup reads and the preceding immutable reports remain the continuity evidence; I do not infer that inaccessible, deleted, non-master, or truncated history is empty.

No release, competing owner, exhausted handoff, posted settlement, retirement, or source-specific correction affecting P0457 was recovered. No P26 or NM13-05 independent P0457 audit PASS was recovered. The source-level sharp-logarithmic-band theorem proved earlier on this track therefore remains **PROVED-CANDIDATE / AUDIT-PENDING**, not closed.

## 2. Fresh source and literature check — 2026-09-18 UTC

I rechecked the Cambridge source itself, including the PDF page containing Section 1.1. The paper still states, after its connectivity result, that another open problem is characterizing the diameter in the additional range of `k(n)` from Theorem 6 where connectivity holds. The source model is unchanged: iid continuous edge weights on `K_n`, and an edge is retained only if it lies among the `k` lowest-weight incident edges at **both** endpoints.

I also repeated bounded searches using the exact paper title, authors, DOI, `LK(n,k) diameter`, `bilateral preference random graph diameter`, later-author queries for Hossein Dabirian and Vijay Subramanian, and citation-style exact-title queries. They recovered the 2026 source and the La--Kabkab 2015 predecessor, whose published abstract places the sharp `log n/log log n` diameter theorem in the older regime and records the `beta_* ~= 2.4626` embedded-ER threshold. Hossein Dabirian's current publication page lists the bilateral-preference paper but no later source-matching diameter paper; a bounded Vijay Subramanian bibliography query likewise recovered the source and unrelated later work, not a diameter resolution. I found no later source-matching resolution in this bounded search.

This is **bounded negative evidence only**. It is not proof of worldwide openness and not a publication-novelty certificate. Publication novelty remains `UNVERIFIED`.

## 3. Frozen metric and why this run is allowed to continue

The canonical claim freezes one quantity:

`S_exact = largest co-degree s for which this track has a complete deterministic diameter classification for the exact source family LK(n,n-1-s), uniformly over the stated feasible n.`

The newest report had:

- `S_exact = 3`;
- five consecutive unchanged frozen-metric invocations since the last movement;
- one stuck recovery used;
- an explicit warning that a **sixth unchanged** invocation would require a handoff and rotation.

This invocation does not evade that rule by renaming the metric. It proves the next complete source-exact co-degree class under the same normalization, so the frozen quantity genuinely moves

`S_exact: 3 -> 4`.

The unchanged counter therefore resets to `0`; the CLOSABLE six-unchanged rotation gate is not triggered on this invocation. The parent asymptotic source question is not called closed by this restricted-class movement.

---

## 4. Setup: co-degree four in the original source convention

Fix `n >= 6` and put

`k = n-5`.

Thus every vertex selects its `n-5` **smallest** incident edge weights and rejects exactly four incident edges. Let

`G = LK(n,n-5)`

be the mutual-selection graph and let

`H = complement(G)`.

All edge weights are distinct, as they are almost surely under the source's continuous law.

For a vertex `v`, let `tau_v` be its fourth-largest incident edge weight. Then an incident edge is rejected by `v` exactly when its weight is at least `tau_v`.

### Lemma P0457-S4-DEGEN

`H` is 4-degenerate.

#### Proof

Take any nonempty induced subgraph `H[U]` and choose `v in U` minimizing `tau_v` over `U`. Suppose `uv` is an `H[U]`-edge. If `v` selected `uv`, then `u` must reject it, so

`w_uv < tau_v <= tau_u <= w_uv`,

a contradiction. Therefore every `H[U]`-edge incident to `v` is one of the four edges rejected by `v`. Hence

`deg_{H[U]}(v) <= 4`.

Every nonempty induced subgraph has such a vertex, so `H` is 4-degenerate. QED.

This rederives the needed source-specific degeneracy fact directly in the original low-weight convention rather than treating it as a black box from the earlier runs.

---

## 5. A structural shell identity

For subsets `A,B` of vertices of a connected graph, write

`dist_G(A,B) = min{d_G(a,b): a in A, b in B}`.

### Lemma P0457-NEIGHBOR-SHELL

If `u,v` are nonadjacent vertices of a connected graph `G`, and

`A = N_G(u)`,  `B = N_G(v)`,

then

`d_G(u,v) = 2 + dist_G(A,B)`.   (5.1)

#### Proof

A shortest `u-v` path begins with some `a in A` and ends through some `b in B`; deleting the first and last edges leaves an `A-B` path of length `d_G(u,v)-2`. Hence the right side of (5.1) is at most `d_G(u,v)`. Conversely, a shortest `A-B` path, preceded by `u-a` and followed by `b-v`, is a `u-v` walk of length `2+dist_G(A,B)`, so the reverse inequality holds. QED.

The identity is elementary, but coupled with the source's complement-degeneracy bound it turns the co-degree-four case into a finite local decision procedure.

---

## 6. Universal diameter bound for this source class

### Lemma P0457-S4-DIAM-UPPER

If `G=LK(n,n-5)` is connected, then

`diam(G) <= 6`.

#### Proof

Take a shortest path

`v_0,v_1,...,v_d`

in `G`. Any two nonconsecutive path vertices are nonadjacent in `G`, otherwise the path could be shortened. Thus in the induced subgraph of `H` on these `d+1` vertices, every internal path vertex has `H`-degree at least `d-2`, and each endpoint has degree at least `d-1`. Therefore that induced subgraph has minimum degree at least `d-2`.

Because `H` is 4-degenerate, every induced subgraph of `H` has a vertex of degree at most four. Hence `d-2 <= 4`, i.e. `d<=6`. Maximizing over shortest paths proves the claim. QED.

---

## 7. The complete `s=4` deterministic classifier

For a missing pair `uv` of a connected source realization, put

`A_uv=N_G(u)`,  `B_uv=N_G(v)`.

Define four bridge tests:

- `C_0(uv)`: `A_uv intersect B_uv` is nonempty;
- `C_1(uv)`: there is a `G`-edge joining a vertex of `A_uv` to a vertex of `B_uv`;
- `C_2(uv)`: there is a length-two `G` path from `A_uv` to `B_uv`;
- `C_3(uv)`: there is a length-three `G` path from `A_uv` to `B_uv`.

Equivalently `C_j(uv)` says `dist_G(A_uv,B_uv) <= j`, with the earlier tests used to determine the first attained shell.

### Theorem P0457-S4-CLASS

For every distinct-weight realization of `LK(n,n-5)`, `n>=6`:

1. `H=complement(G)` is 4-degenerate.
2. If `G` is disconnected, its largest component has size at least `n-4`. More exactly, its component-size multiset is of the form

   `(n-r, lambda_1,...,lambda_m)`

   for some `1<=r<=4` and some integer partition `lambda` of `r`, subject only to the requirement that `n-r` is indeed at least the other displayed parts. Thus the only templates are

   `(n-1,1)`;

   `(n-2,2)`, `(n-2,1,1)`;

   `(n-3,3)`, `(n-3,2,1)`, `(n-3,1,1,1)`;

   `(n-4,4)`, `(n-4,3,1)`, `(n-4,2,2)`, `(n-4,2,1,1)`, `(n-4,1,1,1,1)`,

   with impossible low-order templates discarded by the largest-part condition.
3. If `G` is connected, every missing pair `uv` has exact distance

   - `2` if `C_0(uv)` holds;
   - `3` if `C_0` fails and `C_1` holds;
   - `4` if `C_0,C_1` fail and `C_2` holds;
   - `5` if `C_0,C_1,C_2` fail and `C_3` holds;
   - `6` if all four tests fail.

4. Consequently a connected realization has diameter in `{2,3,4,5,6}`, and its diameter is obtained exactly by applying these four finite shell tests to every missing pair and taking the maximum.

#### Proof

Part 1 is Lemma P0457-S4-DEGEN.

For Part 2, let the component sizes of `G` be `n_1,...,n_r` and let `M=max_i n_i`. Every cross-component pair is an edge of `H`, so `H` contains the complete multipartite graph with the `G`-components as parts. If `n-M>=5`, every vertex in that spanning multipartite subgraph has degree at least five, contradicting 4-degeneracy. Thus `M>=n-4`. The displayed templates are exactly the partitions with at most four vertices outside a largest part.

For Part 3, Lemma P0457-NEIGHBOR-SHELL gives

`d_G(u,v)=2+dist_G(A_uv,B_uv)`.

The tests `C_0,C_1,C_2,C_3` are exactly the conditions that this set-distance is at most `0,1,2,3`, respectively. If all four fail, the set-distance is at least four. Lemma P0457-S4-DIAM-UPPER gives `d_G(u,v)<=6`, hence the set-distance is at most four, and therefore it is exactly four and `d_G(u,v)=6`. This proves all five cases.

Adjacent pairs have distance one; missing pairs are classified above. Taking the maximum proves Part 4. QED.

This is the same deterministic standard used to freeze and move `S_exact` at `s=1,2,3`: source-valid complement structure, complete disconnected component-size restriction, and an exact finite connected-distance classifier. Therefore the frozen metric moves from `3` to `4` without changing its definition.

---

## 8. Method #26 — HUNT THE SPORADIC CASE: the minimal connected order is unusually rigid

The first feasible order for `s=4` is `n=6`, where `k=n-5=1`. Every source vertex proposes one edge, so every vertex of the mutual graph has degree at most one. A graph on six vertices with maximum degree at most one cannot be connected. Thus there is no connected `s=4` source realization at `n=6`.

At `n=7`, `k=2`. Every mutual graph has maximum degree at most two. A finite connected simple graph with maximum degree at most two is either a path or a cycle. Therefore:

### Theorem P0457-S4-MINIMAL

Up to graph isomorphism, the **only** connected `LK(7,2)` graph shapes are

`P_7` and `C_7`.

Both are source-realizable. Their diameters are respectively

`6` and `3`.

Hence the first connected order for `s=4` is `n=7`, the extremal diameter-six branch is already attained at that first order, and the minimal-order connected diameter set is the sporadic two-point set

`{3,6}`,

not the full interval `{2,3,4,5,6}` allowed by the general classifier.

The only remaining point is exact source realizability of both shapes; Method #10 makes that explicit rather than appealing only to the earlier abstract support theorem.

---

## 9. Method #10 — DERANDOMIZE: literal integer-weight source witnesses

All weights below are distinct integers and the source rule selects the two **smallest** incident weights at each vertex.

### 9.1 Exact `P_7` witness

Use vertices `0,1,...,6`. Give path edges

`01,12,23,34,45,56`

weights

`1,2,3,4,5,6`

respectively. Set

`w_02=150`,  `w_46=140`.

Give every remaining edge a distinct weight from `301,302,...,313` in lexicographic edge order.

The two selected neighbors are then exactly

`K_0={1,2}`,
`K_1={0,2}`,
`K_2={1,3}`,
`K_3={2,4}`,
`K_4={3,5}`,
`K_5={4,6}`,
`K_6={4,5}`.

Thus the only mutual selections are

`01,12,23,34,45,56`,

so the source graph is exactly `P_7`, with diameter six. The only one-sided selections are `0->2` and `6->4`; their asymmetry digraph is acyclic, agreeing with the earlier support theorem but not relying on it for this explicit witness.

### 9.2 Exact `C_7` witness

Give the seven cycle edges of `C_7` distinct weights `1,...,7` and all fourteen chords distinct weights larger than 300. Every vertex then selects exactly its two cycle neighbors, so the mutual graph is `C_7`, of diameter three.

These witnesses are literal source instances, not abstract graphs supplied after the fact.

---

## 10. Method #16 — COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE

After the proof identified `n=6` and `n=7` as the entire minimal frontier, I built one exact checker rather than a broad numerical scan.

The checker exhausts **all `5^6 = 15625` local one-selection profiles at `n=6,k=1`** and finds zero connected mutual graphs. It then independently reconstructs the two explicit `n=7,k=2` integer-weight instances, verifies the exact selected-neighbor sets, mutual graph, asymmetry arcs, and diameters, and checks the neighbor-shell identity on every missing pair of both witnesses.

For the `P_7` witness it verifies that the endpoint neighbor sets have set-distance four, hence endpoint distance six. The archived output terminates

`ALL_EXACT_CHECKS_PASS`.

Checker:

`proofnet24/NM13-04/artifacts/2026-09-18/2026-09-18T05-22-05Z__p0457_s4_minimal_exact.py`

creation commit `629a8df304c9c5829dba2ddfdf949b7c2301ba05`, read back at that exact commit, blob `69ab7605e0044eaa6082e809b577f65edc76cf51`.

Archived executed output:

`proofnet24/NM13-04/artifacts/2026-09-18/2026-09-18T05-22-05Z__p0457_s4_minimal_exact.out`

creation commit `b4fb82dd72575ceb053a13e12934e1f667ac0a81`, read back at that exact commit, blob `5fce3433cf39edc815fb6e9cdd11dc07aaec415b`.

The code was inspected before execution and uses only Python's standard library and exact integer/combinatorial operations. This is a **self-check**, not an independent audit. The theorem-sized general `s=4` classifier is proved on the page; the checker certifies the finite minimal-order claims and explicit witnesses rather than substituting computation for the proof.

---

## 11. Method ledger — what actually happened

### #10 — DERANDOMIZE

**Succeeded.** Replaced the abstract existence supplied by the earlier support theorem with literal integer edge weights producing `P_7` and `C_7` under the original lowest-weight source convention. In particular the diameter-six extremizer is a concrete source instance.

### #16 — COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE

**Succeeded.** Exhausted all 15,625 local profiles at the only smaller feasible order `n=6,k=1`, confirming that no connected mutual graph exists, then exactly checked both minimal-order connected shapes and all their missing-pair shell identities.

### #26 — HUNT THE SPORADIC CASE

**Succeeded.** The first connected co-degree-four order is `n=7`, and its connected shape space collapses to exactly `P_7` and `C_7`; the corresponding diameter set is the non-interval `{6,3}`. This exposed the sharp diameter-six extremizer at the first possible connected order and led to the complete `s=4` shell classification.

All three methods were previously unused on P0457. The preceding invocation used #6/#13/#29; earlier triples were #7/#21/#22, #1/#4/#15, #3/#12/#27, #9/#11/#28, #18/#24/#30, #5/#20/#25, and #2/#14/#19.

---

## 12. What this does and does not settle

### New exact results this run

- `P0457-S4-DEGEN`: source complement is 4-degenerate at `k=n-5`.
- `P0457-NEIGHBOR-SHELL`: exact missing-pair neighbor-set distance identity.
- `P0457-S4-DIAM-UPPER`: connected co-degree-four source realizations have diameter at most six.
- `P0457-S4-CLASS`: complete deterministic co-degree-four component/distance classifier.
- `P0457-S4-MINIMAL`: the first connected co-degree-four order is `n=7`, with exactly `P_7` and `C_7` up to isomorphism and diameter set `{6,3}`.
- exact integer source witnesses for both minimal shapes.

### Frozen metric

`S_exact: 3 -> 4`.

This is genuine movement under the original metric definition. The consecutive unchanged-run counter resets from `5` to `0`; stuck recoveries used remain `1`.

### Parent source status

The parent Dabirian--Subramanian diameter question is **not** declared closed by the co-degree-four theorem. The earlier source-matching near-logarithmic theorem candidate remains on the page and has been independently rederived within this track, but protocol closure still requires the missing outside audits and the recorded prior-art standard. Therefore:

- mathematical source theorem candidate: `PROVED-CANDIDATE / AUDIT-PENDING`;
- P26 independent audit: **NO PASS RECOVERED**;
- NM13-05 independent audit: **NO PASS RECOVERED**;
- publication novelty: `UNVERIFIED`;
- paper folder: not created this run.

No self-check is counted as an audit.

---

## 13. Next route

Because `S_exact` moved, the six-unchanged CLOSABLE rotation rule does not force a handoff now. The next invocation must not mechanically repeat this shell extension without a genuinely new route. The only Section-B lenses not yet used on P0457 are now:

- **#8 GO THE OTHER WAY AND DISCRETIZE** — replace the asymptotic attachment theorem by a finite random-order statement that can be exactly falsified or certified at small `n`, looking specifically for where the source-level sharp-diameter proof's inequalities first become truthful;
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE** — compare the exact `log n/log log n` scale and the block-attachment exponent with sparse random graph / random nearest-neighbor models to identify a theorem that can shorten or independently certify the source proof;
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT** — actively try to falsify the source-level theorem candidate in the lower edge of the Theorem-6 band by constructing a long-tail exceptional-vertex mechanism rather than proving another upper-bound lemma.

If those attacks expose a flaw, record it and repair or retract the candidate. If they survive and an outside audit appears, move toward the closure package rather than extending `s=5` merely to advance a counter.

---

## 14. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-04
  category: CLOSABLE_OUTSIDE
  source_id: P0457
  claim_id: operations/claims/P0457.md
  canonical_dedup_key: diameter_near_the_newly_established_bilateral_connectivity_threshold
  source: "Dabirian--Subramanian, Connectivity of a family of bilateral preference random graphs, J. Appl. Probab. 63(2) (2026), 552--579"
  source_target: "characterize diameter of LK(n,k) in the additional Theorem-6 connectivity range"
  track_status: PARTIAL_WITH_SOURCE_THEOREM_CANDIDATE_AUDIT_PENDING
  source_status: OPEN_IN_PUBLISHED_SOURCE_BOUNDED_RECHECK
  frozen_metric:
    name: S_exact
    definition: "largest co-degree s with a complete deterministic diameter classification for LK(n,n-1-s) over the stated feasible n"
    before: 3
    after: 4
    movement: true
  substantive_claims:
    - P0457-S4-DEGEN
    - P0457-NEIGHBOR-SHELL
    - P0457-S4-DIAM-UPPER
    - P0457-S4-CLASS
    - P0457-S4-MINIMAL
  minimal_order_result:
    s: 4
    first_connected_n: 7
    k_at_first_connected_n: 2
    connected_shapes_up_to_isomorphism: [P7, C7]
    diameters: [6, 3]
  methods_actual: [10, 16, 26]
  method_outcomes:
    10: "explicit integer-weight P7 and C7 source witnesses"
    16: "exhausted all 15625 n=6,k=1 local profiles; exact witness/shell checker PASS"
    26: "minimal-order sporadic connected class is exactly P7/C7, with diameter set {6,3}"
  exact_checker: proofnet24/NM13-04/artifacts/2026-09-18/2026-09-18T05-22-05Z__p0457_s4_minimal_exact.py
  exact_checker_commit: 629a8df304c9c5829dba2ddfdf949b7c2301ba05
  exact_output: proofnet24/NM13-04/artifacts/2026-09-18/2026-09-18T05-22-05Z__p0457_s4_minimal_exact.out
  exact_output_commit: b4fb82dd72575ceb053a13e12934e1f667ac0a81
  exact_output_terminal: ALL_EXACT_CHECKS_PASS
  unchanged_runs_before: 5
  unchanged_runs_after: 0
  stuck_recoveries_used: 1
  rotation_required: false
  rotation_reason: "not triggered because the frozen metric genuinely moved under its original definition"
  literature_check:
    date_utc: 2026-09-18
    original_source_pdf_rechecked: true
    original_open_problem_text_rechecked: true
    predecessor_La_Kabkab_rechecked: true
    later_author_queries: true
    citing_title_DOI_queries: true
    later_source_matching_resolution_found: false
    negative_search_is_worldwide_openness_proof: false
    publication_novelty: UNVERIFIED
  audits:
    P26: NO_PASS_RECOVERED
    NM13-05: NO_PASS_RECOVERED
  next_methods: [8, 17, 23]
  shared_root_edits: NONE
  peer_track_edits: NONE
  schedules_modified: NONE
```

No email/Gmail, Drive, public posting, paid compute, permission change, workflow execution, shared-root edit, peer-track edit, or schedule creation/modification was performed.

**End of immutable run report.**
