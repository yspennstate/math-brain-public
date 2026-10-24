Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MATHEMATICAL MOVEMENT: `b_NUV >= 0.629257883497476201490891... -> b_NUV >= 0.629257903387774956151863... > 0.6292579`; actual Section-B methods tried: #7, #19, #28.**

# NM13-11 — P0257 Poisson closed-quadruple shape-atlas movement

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-11` / `proofnet24/NM13-11/`  
Category: **HARD OUTSIDE**  
Canonical source / claim: **P0257 / `operations/claims/P0257.md`**  
Source status after this invocation: **PARTIAL / SOURCE OPEN**  
Frozen pre-write master: `30c512c7e4a2f4c936d4d8bc67912a01e5bbf6f8`

## 1. Result and frozen metric

This invocation continues the already admitted source P0257; it does not screen for or acquire a successor.

The exact source model and frozen metric are unchanged:

- `n` i.i.d. uniform points in the unit square, equivalently intensity-one binomial points in a square of area `n` after multiplying distances by `sqrt(n)`;
- a uniform initial vertex;
- the nearest-unvisited-vertex walk of total area-`n` length `L_n`;
- `b_NUV` is the explicit certified endpoint in

`liminf_{n -> infinity} E[L_n]/n >= b_NUV`.

The predecessor exact endpoint was

`B_before = 2517031533989904805963567012121706380405600461327497 /
            4000000000000000000000000000000000000000000000000000`

`         = 0.62925788349747620149089175303042659510140011533187425...`.

This run proves the stronger exact endpoint

`B_after = 1631470499263030121036034768604328605573396461083400872097661500093812049 /
           2592689723052473092839289062500000000000000000000000000000000000000000000`

`        = 0.629257903387774956151863323388440298347313310678362445708076...`

so the certified movement is

`B_after - B_before =
 28350562718576522998828671316748734907366797563 /
 1425346248855765660885083943337984000000000000000000000`

`                      = 1.9890298754660971570358013703... * 10^(-8) > 0`.

This is a real movement of the previously frozen metric. It does **not** prove existence of the source limit `lim L_n/n`, and P0257 therefore remains PARTIAL / OPEN.

## 2. Runtime/model-control truth

The task prompt requests `Model: GPT-6. Reasoning: maximum`. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this worker, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 maximum, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still provides task title/prompt, schedule/start configuration, timing mode, enabled state, and list/update operations. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated per-run applied-model/applied-effort receipt**. GPT-6/maximum therefore remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists model-family and reasoning-effort fields into routing and returns trustworthy run-level attestation.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary, not evidence that the mathematical task or GitHub claim is unowned. `RESULTS.md` records that a later P26 full update succeeded from another authorized context. If such a denial recurs, the compliant workaround is the owning or otherwise authorized product/workspace/API/admin context, or an authorized ownership-transfer/platform-support route for the same existing task — not duplication, identity substitution, or permission bypass. No scheduler or permission was modified in this invocation.

## 3. Authoritative continuity and required reads

The controlling predecessor is

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T12-05-00Z__p0257-four-point-trap-movement.md`

created at commit

`18849b01b563e02d1cd935a5c0d50786f70e89a1`.

Its preserved state was:

- P0257 admitted and exclusively owned by `proofnet24/NM13-11/`;
- canonical key `law_of_large_numbers_and_constants_for_nuv_lengths`;
- SHA-256 `75bdfbc93f05ad07b271ad7a5a8046a16f0bb29d10236cbc1ebf0b8889fdf5e5`;
- shard residue `10 mod 13`;
- metric `b_NUV >= 0.629257883497476201490891...`;
- source status PARTIAL / OPEN;
- `unchanged_runs=0`;
- HARD stuck recoveries `0/2`;
- previous actual Section-B methods #1/#9/#27;
- next planned methods #7/#19/#28.

Before substantive work I freshly read or exact-target-recovered current state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the controlling predecessor report;
- current `operations/claims/P0257.md`;
- the canonical P0257 problem row in `probability_campaign_2026_09/codex_20h_20260906/problems.jsonl`;
- the canonical prior attempt `P0257-A001` in the campaign attempt ledger;
- repository-wide exact P0257/key searches;
- newest neighboring NM13-10 report `proofnet24/NM13-10/runs/2026-09-19/2026-09-19T11-54-30Z__admission-delta-screen-41-h0008-released-hard-r9-no-r9-closable.md`;
- newest neighboring/designated-secondary-auditor NM13-12 report `proofnet24/NM13-12/runs/2026-09-19/2026-09-19T11-58-30Z__post-p0214-successor-delta-screen-p0205-still-ambiguous.md`;
- fresh bounded public source/current-literature searches dated 2026-09-19;
- exact checker execution and its archived readback.

The campaign problem row still records P0257 as admitted, source-says-open, `attempted_unsolved`; its literal grouped source programme is existence/identification of first-order NUV constants. The prior attempt still supplies only the old nearest-neighbor lower floor and explicitly says it does not prove convergence. No historical attempt was silently reclassified as this run's progress.

The append-only intake and attempt corpora are too large for an honest claim that every unchanged historical byte was rendered model-visible in a single invocation. I make no such claim. Candidate-specific source, attempt, claim, metric, neighboring ownership and current public status were reopened directly. Missing display is not treated as permission to reset history.

No private repository history material to continuing P0257 was known to be inaccessible.

## 4. Ownership and repository race check

The final pre-write `master` observed immediately before this report was

`30c512c7e4a2f4c936d4d8bc67912a01e5bbf6f8`.

The exact compare from the predecessor report commit

`18849b01b563e02d1cd935a5c0d50786f70e89a1 .. 30c512c7e4a2f4c936d4d8bc67912a01e5bbf6f8`

reports status `ahead`, **122 commits ahead and 0 behind**. Targeted inspection of the returned changed-file material found no `operations/claims/P0257.md` mutation and no root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, P0257 problem-row ledger, or P0257 attempt-ledger mutation. Concurrent unrelated workers did add their own reports/artifacts during the interval.

A fresh direct read at the final pre-write head still records P0257 as

- `CLAIMED / ADMITTED / HARD OUTSIDE`;
- owner `proofnet24/NM13-11/`;
- canonical dedup key and residue 10 unchanged;
- source and frozen metric unchanged;
- neither P26 nor NM13-12 audit presumed.

Repository-wide exact P0257/key searches did not recover a second canonical owner. NM13-10 remains on its own admission-pending residue-9 CLOSABLE lane; NM13-12 has terminally handed off P0214 and is screening residue-11 successors. Neither neighboring report releases, claims, or audits P0257. Ownership therefore remains intact.

## 5. Fresh source and bounded literature check — 2026-09-19

This is bounded current-status evidence, not proof of worldwide openness, novelty, or priority.

The original source remains David J. Aldous, *The Nearest Unvisited Vertex Walk on Random Graphs*, arXiv:1912.13175; Cambridge records publication in *Probability in the Engineering and Informational Sciences* 36(3), July 2022, pp. 851–867 and online publication 5 April 2021. The abstract still says that obtaining sharper results is challenging.

Aldous's currently crawled Berkeley home/research page still lists the NUV walk and explicitly states the challenge “improve beyond order-of-magnitude for models of random graphs.” Focused searches for the exact title, `nearest unvisited vertex`, Euclidean random points, limit constants, and law-of-large-numbers follow-ups with 2024–2026 emphasis did not surface a checked later primary source resolving the Euclidean first-order constant problem.

Because this run changes language to a nearest-neighbor graph, I also searched adjacent Poisson `k`-nearest-neighbor component literature. Falgas-Ravry's EJP work studies components of Poisson `k`-nearest-neighbor random geometric graphs below connectivity, and Jahnel–Tóbiás study percolation questions for bounded-degree stationary geometric graphs. Those are relevant neighboring literatures, but the checked abstracts do not state the NUV-length additive lower-bound theorem proved below. I make no novelty or priority claim from that bounded search.

No simulation or finite plot is used as asymptotic evidence.

## 6. Why the previous four-point correction must be replaced, not added

The predecessor established a tiny source-valid four-point guarded-square correction

`delta_fixed =
 1579888671017488353 / 4294967296000000000000000000000
 = 3.6784649617445849650539... * 10^(-13)`.

That fixed square gadget sits inside the broader square-like shape family used below. Adding the new family on top of the predecessor endpoint would therefore risk counting the same closed 3-nearest quadruple twice.

So I first remove that old four-point term exactly. The surviving earlier closed-two-nearest-triple theorem endpoint is

`B_prequad = B_before - delta_fixed`

`          = 4916077214821159023396228863546259379089219326781 /
             7812500000000000000000000000000000000000000000000`.

The theorem below replaces `delta_fixed` with a larger positive-measure Poisson shape-atlas correction. All preceding closed-two-nearest-triple corrections are retained because the accepted four-point shapes are proved vertex-disjoint from every closed two-nearest triple.

## 7. Deterministic closed-3-nearest quadruple lemma

For a finite tie-free point set, call `Q={q1,q2,q3,q4}` a **closed 3-nearest quadruple** if, for every `v in Q`, the three nearest points to `v` in the entire configuration are exactly `Q\{v}`.

Two elementary facts are load-bearing.

### 7.1 Distinct closed 3-nearest quadruples are disjoint

If two such quadruples `Q,Q'` shared a vertex `v`, the set of the three nearest neighbors of `v` would have to equal both `Q\{v}` and `Q'\{v}`. Hence `Q=Q'`. Therefore distinct closed 3-nearest quadruples have disjoint vertex sets.

### 7.2 NUV consumes a closed quadruple consecutively

Once NUV first enters `Q`, as long as an unvisited member of `Q` remains, every such member is closer to the current vertex than every point outside `Q`. NUV therefore visits all four members consecutively.

Let `z` be the last member of `Q` visited. Unless `z` is the global terminal vertex of the entire NUV walk, the incoming edge at `z` is an internal `Q` edge and the outgoing edge goes outside `Q`.

Let `r_j(z)` denote the `j`th nearest-neighbor distance at `z`. The generic degree-two path charge uses `r_1(z)+r_2(z)` on the `2L` side. The actual two incident edges at `z` have total length at least `r_1(z)+r_4(z)`. Thus a nonterminal closed quadruple contributes the deterministic extra bonus

`r_4(z) - r_2(z)`

on the `2L` side.

Because the closed quadruples are disjoint, at most one of them can contain the global terminal vertex. Omitting that one is `o(n)` after normalization.

## 8. Method #28 — REPLACE “FOR ALL” WITH “FOR TYPICAL”: a positive-measure square-like shape family

The fixed-cell predecessor was intentionally worst-case and microscopic. Here I retain an entire positive-measure four-dimensional family.

For an ordered representation of four inserted points, rotate and scale so that

`p1=(0,0), p2=(1,0), p3=(a,b), p4=(c,d)`.

The atlas domain is

`-1/2 <= a <= 1/2`,
` 2/5 <= b,c,d <= 8/5`,

partitioned into rational boxes of side `1/10`. There are `10*12^3 = 17280` candidate cells.

For each cell, define the selected matching pair `p1p4` and `p2p3` as proposed long diagonals and the remaining four edges as sides. A cell is accepted only when an exact interval calculation proves

`min_cell{|p1-p4|^2, |p2-p3|^2}
   > max_cell{|p1-p2|^2, |p1-p3|^2, |p2-p4|^2, |p3-p4|^2}`.      (8.1)

The exact checker finds **1796 accepted cells**, total normalized shape volume

`1796 * (1/10)^4 = 449/2500`.

Across every accepted cell the squared diagonal-minus-side gap is at least `1/100`.

Equation (8.1) has an important combinatorial consequence. Every three-vertex subset of the four inserted points contains one selected long matching edge. At an endpoint of that long edge, the omitted fourth vertex and the included side-neighbor are both strictly closer. Hence no three-vertex subset can be a closed two-nearest triple.

Under the guard introduced below, all external points are farther than all three internal neighbors. Therefore no accepted gadget vertex can belong to a closed two-nearest triple involving an external point either. The new quadruple charge is consequently vertex-disjoint from every closed-two-nearest-triple charge retained in `B_prequad`.

This is the main “typical instead of all” gain: positive four-dimensional shape volume replaces one tiny fixed square cell.

## 9. Method #19 — MAKE IT AN ALGORITHM: exact rational shape-atlas certification

The atlas is certified by an executed exact-arithmetic algorithm, not by plotting or floating-point sampling.

For each accepted rational cell let

`U^2` = an exact upper bound on all four side lengths squared,
`R^2` = an exact upper bound on all six pair distances squared.

The checker chooses rational thousandth-grid bounds

`u >= sqrt(U^2)`,
`g > sqrt(R^2)`

and imposes the stronger Poisson guard that there is no external point in

`union_i B(p_i, g s)`

when the cell is used at geometric scale `s`.

Then the first three neighbors of every gadget vertex are the other three gadget vertices, so the gadget is a closed 3-nearest quadruple; moreover

`r_4(z)-r_2(z) >= (g-u)s`.

Across all 1796 accepted cells the checker proves the uniform exact margin

`g-u >= 141/1000`.                                      (9.1)

For the guard probability, the union of the four radius-`gs` disks is contained in the parallel body

`conv{p1,p2,p3,p4} + B(0,gs)`.

If a cell's normalized points lie in a rectangle of width `W` and height `H`, planar Steiner plus monotonicity of convex perimeter gives

`area(union_i B(p_i,gs))
 <= s^2 [ W H + 2g(W+H) + pi g^2 ]`.

Using the exact elementary upper bound `pi < 22/7`, every accepted cell satisfies

`area guard <= Q_* s^2`,

where the checker proves the common rational bound

`Q_* = 3827833/109375`.                                (9.2)

It also proves

`5917/1000 > sqrt(Q_*)`.                               (9.3)

The atlas algorithm is therefore not merely a search heuristic: every accepted cell comes with interval-certified geometry, a source-valid guard, an explicit deterministic NUV bonus, and a uniform exact void-probability bound.

## 10. Method #7 — TAKE THE LIMIT: Campbell–Mecke density and transfer back to the exact binomial source

Work first in a unit-intensity planar Poisson process. Campbell–Mecke for unordered four-sets gives a factor `1/4!`.

For an ordered representation set

`x2 = s (cos theta, sin theta)`,

and express `x3,x4` by the normalized shape coordinates `(a,b,c,d)` in the rotated frame. The Jacobian is

`dx2 dx3 dx4 = s^5 ds dtheta da db dc dd`.

The deterministic quadruple bonus contributes one further factor `s`. Integrating `theta` gives `2 pi`, and the guard probability is at least `exp(-Q_* s^2)` by (9.2). Hence the contribution of the accepted atlas to the **`2L`** bonus density is at least

`(1/24) * 2 pi * (449/2500) * (141/1000)
 * integral_0^infinity s^6 exp(-Q_* s^2) ds`.

Dividing by two to pass from `2L` to `L`, and using

`integral_0^infinity s^6 exp(-Q s^2) ds
   = 15 sqrt(pi)/(16 Q^(7/2))`,

the atlas contribution to `b_NUV` is at least

`Delta_atlas >=
 (5 pi^(3/2)/128)
 * (449/2500)
 * (141/1000)
 * Q_*^(-7/2)`.                                      (10.1)

There is no labeling overcount: an unordered quadruple has at most 24 ordered representations, and the `1/24` factor averages only those representations that pass the atlas/guard. Each represented lower bonus is bounded by that same quadruple's actual `r4-r2` bonus, so the averaged represented charge never exceeds the single available quadruple charge.

### Transfer to the source's binomial square

Fix a scale cutoff `S<infinity` and restrict anchors to distance larger than a fixed atlas-dependent multiple of `S` from the boundary of the area-`n` square. The lost anchor area is `O(S sqrt(n))`, hence negligible after division by `n`.

For a fixed inserted quadruple with guard union area `A=O(S^2)`, the remaining `n-4` independent source points avoid the union with probability

`(1-A/n)^(n-4) -> exp(-A)`.

The ordered factorial density tends to the unit-intensity Poisson factorial density. Thus for every fixed `S`, the normalized expected finite-binomial quadruple bonus has liminf at least the corresponding Poisson integral over `0<s<=S`.

All terms are nonnegative. Letting `S -> infinity` after the `n -> infinity` liminf therefore gives (10.1) by monotone convergence of the **lower-bound integrals**. No interchange of an unproved NUV stabilization limit is used. This proves the explicit source-valid correction directly for `liminf E[L_n]/n`.

## 11. Exact rational endpoint

For certification, use the elementary exact lower bounds

`pi > 3`, `sqrt(pi) > 17/10`.

Then

`5 pi^(3/2)/128 > 51/256`.

Together with (9.1)–(9.3), (10.1) gives

`Delta_atlas >=
 6759425885009765625 /
 339829027379933753224631296`

`              = 1.9890666601157146028854519097... * 10^(-8)`.

This is strictly larger than the old fixed four-point correction `delta_fixed`. Replacing rather than adding that old term yields

`B_after = B_prequad + Delta_atlas`

with the exact value stated in Section 1. In particular

`B_after > 0.6292579`.

Thus the frozen metric genuinely moves by approximately `1.98903 * 10^(-8)` this run.

## 12. Exact checker and archived output

The exact-arithmetic checker was executed before archival:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T12-50-00Z__p0257_quad_shape_atlas_exact.py`

created at commit

`49ec479a7b0153018ba36deab1742f4b43f2ab92`.

Its executed output was archived at

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T12-50-00Z__p0257_quad_shape_atlas_exact.out`

created at commit

`0eb2b2c5d4cde63b33ad28efd6f5a8733363b902`

and read back at that commit.

The output certifies exactly:

- 17,280 candidate rational shape cells;
- 1,796 accepted cells;
- accepted shape volume `449/2500`;
- minimum squared diagonal-side margin `1/100`;
- minimum guard bonus `141/1000`;
- `Q_*=3827833/109375`;
- exact upper square-root gate `5917/1000`;
- exact atlas lower correction;
- exact removal of the predecessor fixed-four-point correction;
- positive exact metric movement;
- `B_after > 0.6292579`;
- terminal line `ALL_EXACT_FINITE_CHECKS_PASS`.

The checker uses exact integers and `Fraction` arithmetic for certification. No floating-point value is load-bearing.

## 13. Method outcomes and route discipline

Actual methods genuinely attempted this invocation:

- **#7 TAKE THE LIMIT — SUCCESS / METRIC MOVED.** The Poisson/Palm limit supplies an explicit density formula, and the fixed-scale-first binomial transfer avoids assuming the source LLN or a stabilization theorem.
- **#19 MAKE IT AN ALGORITHM — SUCCESS / METRIC MOVED.** A rational cell atlas turns a positive-measure shape family into 1,796 exact certified boxes with uniform deterministic and void-area constants.
- **#28 REPLACE FOR ALL WITH TYPICAL — SUCCESS / METRIC MOVED.** The fixed worst-case square gadget is replaced by a four-dimensional positive-measure family, increasing the quadruple correction by more than five orders of magnitude relative to the predecessor fixed-cell term.

The previous fixed-cell route is superseded rather than extended with finer decimal checking. No extra certificate was manufactured without movement.

## 14. Status, counters, audits, and next route

Source label remains **PARTIAL / OPEN**. This run improves a source-relevant first-order lower endpoint but does not prove existence or identify Aldous's proposed Euclidean limit constant.

Because the tracked metric moved:

- `unchanged_runs`: **0 -> 0**;
- HARD stuck-recovery episodes: **0/2 -> 0/2**;
- Section-I recovery is not triggered.

P26 audit: **NOT REQUESTED / NOT PRESUMED**.  
NM13-12 secondary audit: **NOT REQUESTED / NOT PRESUMED**.

The next genuinely different Section-B triple is:

- **#10 DERANDOMIZE** — seek a deterministic packing/charging rule that extracts a closed-quadruple bonus without paying the full empty-union guard;
- **#13 FIND WHAT ONLY INCREASES** — look for a monotone rank-gap charge along NUV entry/exit that can combine higher-order local traps without overlap bookkeeping;
- **#21 ASK WHO ELSE HAS THIS SHAPE** — inspect stochastic-geometry Palm formulas for mutual `k`-nearest-neighbor components and stabilization scores to see whether an existing exact component-density machinery can replace the coarse rectangle-Steiner guard.

The next run must not count these as tried until actually attempted. Merely halving the atlas mesh or tightening `pi`/square-root rationals is not the next research route.

## 15. Structured ledger delta for P26

```yaml
ledger_delta:
  task_id: NM13-11
  category: HARD_OUTSIDE
  status: PARTIAL_SOURCE_OPEN
  source_id: P0257
  claim_id: operations/claims/P0257.md
  owner: proofnet24/NM13-11/
  canonical_dedup_key: law_of_large_numbers_and_constants_for_nuv_lengths
  sha256: 75bdfbc93f05ad07b271ad7a5a8046a16f0bb29d10236cbc1ebf0b8889fdf5e5
  residue_mod13: 10
  metric_name: b_NUV
  metric_before: 0.62925788349747620149089175303042659510140011533187425...
  metric_after: 0.629257903387774956151863323388440298347313310678362445708076...
  exact_metric_after: 1631470499263030121036034768604328605573396461083400872097661500093812049/2592689723052473092839289062500000000000000000000000000000000000000000000
  mathematical_movement: true
  exact_movement: 28350562718576522998828671316748734907366797563/1425346248855765660885083943337984000000000000000000000
  methods_tried: [7, 19, 28]
  method_outcomes:
    7: SUCCESS_POISSON_CAMPBELL_MEECKE_WITH_SOURCE_BINOMIAL_TRANSFER
    19: SUCCESS_EXACT_RATIONAL_SHAPE_ATLAS_1796_CELLS
    28: SUCCESS_POSITIVE_MEASURE_TYPICAL_SQUARELIKE_FAMILY
  finite_certificate:
    checker: proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T12-50-00Z__p0257_quad_shape_atlas_exact.py
    checker_commit: 49ec479a7b0153018ba36deab1742f4b43f2ab92
    output: proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T12-50-00Z__p0257_quad_shape_atlas_exact.out
    output_commit: 0eb2b2c5d4cde63b33ad28efd6f5a8733363b902
    result: ALL_EXACT_FINITE_CHECKS_PASS
  old_quad_term_replaced_not_added: true
  accepted_cells: 1796
  accepted_shape_volume: 449/2500
  atlas_lower_exact: 6759425885009765625/339829027379933753224631296
  unchanged_runs: 0
  hard_recoveries: 0/2
  audit_partner_primary: P26_NOT_REQUESTED_NOT_PRESUMED
  audit_partner_secondary: NM13-12_NOT_REQUESTED_NOT_PRESUMED
  source_closure: false
  predecessor_report_commit: 18849b01b563e02d1cd935a5c0d50786f70e89a1
  final_prewrite_master: 30c512c7e4a2f4c936d4d8bc67912a01e5bbf6f8
  predecessor_to_prewrite:
    status: ahead
    ahead_by: 122
    behind_by: 0
  next_methods: [10, 13, 21]
  next_step: DERANDOMIZED_OR_MONOTONE_HIGHER_ORDER_TRAP_CHARGE_NOT_MESH_REFINEMENT
```

No shared root, peer namespace, canonical claim file, scheduler, permission, workflow, email/Drive resource, public surface, or paid-compute resource was modified. This invocation wrote only the two warranted exact P0257 artifacts above and this single immutable own-namespace report.
