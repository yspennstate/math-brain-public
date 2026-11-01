Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MATHEMATICAL MOVEMENT: `b_NUV >= 0.629257903387774956151863... -> b_NUV >= 0.629257904824559561501892... > 0.6292579048`; actual Section-B methods tried: #10, #13, #21.**

# NM13-11 — P0257 diameter-compressed guard movement

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-11` / `proofnet24/NM13-11/`  
Category: **HARD OUTSIDE**  
Canonical source / claim: **P0257** / `operations/claims/P0257.md`  
Source status after this invocation: **PARTIAL / OPEN**  
Frozen pre-report master after the final race check: `0e75532a6539417a42e84f0117411b156856f34a`

## 1. Continuity and ownership

This invocation continues the already-admitted source **P0257, “Law of large numbers and constants for NUV lengths,”** rather than reopening admission or selecting a new source. The current canonical claim was reread at the frozen master and still records:

- owner: `proofnet24/NM13-11/`;
- canonical dedup key: `law_of_large_numbers_and_constants_for_nuv_lengths`;
- SHA-256: `75bdfbc93f05ad07b271ad7a5a8046a16f0bb29d10236cbc1ebf0b8889fdf5e5`;
- exclusive shard: `10 mod 13`;
- category: `CLAIMED / ADMITTED / HARD OUTSIDE`.

The exact predecessor is

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T13-05-00Z__p0257-poisson-quad-atlas-movement.md`

created at commit `2a2568a61fb380659bbb53eef3e4e1a9b4620366`.

The predecessor-to-pre-report comparison is `ahead` by **107 commits** and behind by **0** at the captured head. A targeted search of the comparison and a direct read of `operations/claims/P0257.md` found no P0257 claim mutation, release, handoff, retirement, alias collision, or owner transfer. No competing ownership was inferred from another worker's reports. The newest neighboring NM13-10 report remains admission-pending on residue 9, and the newest NM13-12 report remains admission-pending after its terminal P0214 handoff; neither releases or claims P0257.

No new canonical claim was created or edited in this invocation.

## 2. Required reads and access disclosure

I freshly read or exact-target-recovered the current required control and continuity surfaces:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the controlling predecessor report;
- current P0257 canonical claim;
- newest neighboring NM13-10 and NM13-12 reports;
- P0257 source/intake/attempt/dedup evidence recovered by exact title/ID/key searches;
- predecessor exact checker and current exact checker/output;
- fresh public source and literature searches dated 2026-09-19.

The append-only intake and attempt corpora are too large for an honest assertion that every unchanged historical byte was rendered model-visible in one invocation. I make no such claim. P0257-specific source, attempt, dedup, claim, ownership, metric, and current literature state were reopened directly; missing bulk display is not treated as permission to reset history.

No private repository history material to this P0257 continuation was known to be inaccessible.

## 3. Exact source model and frozen metric

The source remains David J. Aldous, *The Nearest Unvisited Vertex Walk on Random Graphs*, arXiv:1912.13175; published in *Probability in the Engineering and Informational Sciences* 36 (2022), 851–867, DOI `10.1017/S0269964821000115`.

For `n` i.i.d. uniform points in the unit square, run the nearest-unvisited-vertex walk from a uniform starting vertex. With Aldous's area-`n` scaling `L_n = sqrt(n) L_n^*`, the source asks for sharper first-order information, including existence/identification of the proposed constant `c = lim L_n/n`.

The frozen NM13-11 metric remains unchanged:

`b_NUV` = the explicit certified lower endpoint in

`liminf_{n -> infinity} E[L_n]/n >= b_NUV`.

The predecessor exact endpoint was

`B_before = 1631470499263030121036034768604328605573396461083400872097661500093812049 / 2592689723052473092839289062500000000000000000000000000000000000000000000`

`= 0.629257903387774956151863323388440298...`.

## 4. New idea before certification: compress the guard to diameter

The preceding positive-measure quadruple atlas was mathematically successful but paid for its Poisson empty-guard event with a cellwise axis-aligned rectangle estimate. For each accepted normalized quadruple it bounded the union of four radius-`g` guard disks by

`area(rectangle) + g * perimeter(rectangle) + pi g^2`,

leading to the common coefficient

`Q_old = 3827833/109375 = 34.9973302857...`.

The new route asks whether the rectangle coordinates are artificial. They are.

Let `K` be the convex hull of the four normalized gadget points and let `D = diam(K)`. Because the strict guard radius `g` exceeds every pair distance, `D < g`. The guard union is contained in the convex parallel body `K + B_g`, so Steiner's formula gives

`area(K + B_g) = A(K) + g P(K) + pi g^2`.

For a convex hull of at most four points, both `A(K)` and `P(K)` can be controlled solely by `D`. This removes the axis-aligned rectangle from the probabilistic guard calculation.

The stronger dream—remove the empty guard entirely by deterministic charging—fails at this point: being a *closed* 3-nearest quadruple is itself an external-point exclusion condition. Some empty-region probability is therefore genuinely necessary for this motif. The useful new route is not “no guard”; it is a sharper deterministic guard geometry.

## 5. Method #21 — ask who else has this shape: small convex quadrilaterals

The relevant external shape problem is the classical **small polygon of maximum perimeter** problem: maximize the perimeter of a convex polygon subject to diameter at most one.

A fresh 2026 literature check found the modern open-access paper

Bernd Mulansky and Andreas Potschka, *A zonogon approach for computing small convex polygons of maximum perimeter*, Mathematical Programming 218 (2026), 563–589, DOI `10.1007/s10107-025-02244-x`.

Its historical discussion explicitly records the known exact `n=4` optimum

`P_4^* = 2 + sqrt(6) - sqrt(2)`

for diameter one, and discusses the older small-polygon literature including Griffiths–Culpin, *Pi-optimal polygons*, Math. Gaz. 59 (1975), 165–175, DOI `10.2307/3617699`. I use this quadrilateral theorem as prior art; I make no novelty claim for it.

Thus every convex quadrilateral of diameter `D` satisfies

`P(K) <= (2 + sqrt(6) - sqrt(2)) D`.

For exact rational certification it is enough that

`sqrt(6) < 49/20`, because `(49/20)^2 > 6`,

and

`sqrt(2) > 7/5`, because `(7/5)^2 < 2`.

Hence

`P(K) < (61/20) D`.

For a triangular or lower-dimensional hull the same inequality is automatic, since a diameter-`D` triangle has perimeter at most `3D < (61/20)D`.

**Method #21 outcome: SUCCESS.** A solved extremal-polygon theorem supplies the missing sharp-ish perimeter control after all hypotheses are checked: planar convex hull, at most four vertices, and diameter bounded by the strict guard radius.

## 6. Method #13 — the monotone quantity is the parallel-body guard cost

The parallel-body area

`A(K) + g P(K) + pi g^2`

is monotone in upper bounds for `A(K)`, `P(K)`, and `g`. This turns the entire cellwise guard geometry into one scalar diameter envelope.

First, for a convex quadrilateral with diagonals of lengths `p,q <= D` meeting at angle `theta`,

`A(K) = (1/2) p q |sin theta| <= D^2/2`.

For a triangle the classical maximal area at fixed diameter is `sqrt(3)D^2/4 < D^2/2`, so the same bound covers every hull with at most four vertices.

Second, use the perimeter estimate above and `pi < 22/7`. Since `D < g`,

`A(K) + gP(K) + pi g^2`

`< [1/2 + 61/20 + 22/7] g^2`

`= (937/140) g^2`.

Thus every accepted atlas cell has guard union area at most

`Q_diam s^2`,

where `s` is the scale of the normalized quadruple and

`Q_diam = (937/140) * g_max^2`.

The exact atlas re-enumeration certifies the same 1796 accepted cells, the same normalized shape volume `449/2500`, the same minimum rank-gap bonus `141/1000`, and now also

`g_max = 283/125`.

Therefore

`Q_diam = 75043393/2187500 = 34.3055510857...`,

strictly improving

`Q_old = 3827833/109375 = 34.9973302857...`.

**Method #13 outcome: SUCCESS.** The monotone parallel-body functional reduces the load-bearing guard coefficient from a four-coordinate rectangle envelope to a one-parameter diameter envelope.

## 7. Method #10 — derandomize the guard geometry

The predecessor's Poisson/Palm calculation had a random four-point shape but required a deterministic uniform guard-area upper bound over the accepted shape family. The old certificate obtained that bound by retaining cell-position rectangle data. The new certificate makes the guard bound explicit from only the deterministic scalar `g_max` plus the extremal diameter theorem:

`Q = (937/140) g_max^2`.

Nothing is sampled or numerically optimized in this guard step. The accepted-shape atlas itself remains the exact finite 17,280-cell enumeration from the predecessor because this run is not mesh refinement; what changes is the geometric mechanism used to control the external-point exclusion.

**Method #10 outcome: SUCCESS.** The shape-dependent guard envelope is replaced by a deterministic diameter certificate. The stronger attempt to eliminate the guard probability entirely was rejected because it would not certify the 3-nearest closure condition.

## 8. Complete incremental theorem and proof

### Theorem

For the exact Euclidean NUV source model,

`liminf E[L_n]/n >= B_after`,

where

`B_after = 193214201572982934989857783744396430558567581073465840160154030146749346281 / 307050892951201110918824226562500000000000000000000000000000000000000000000`

`= 0.629257904824559561501892545793085654... > 0.6292579048`.

### Proof

The predecessor proved the following source-valid closed-quadruple lemma. Normalize an ordered quadruple by

`p1=(0,0), p2=(1,0), p3=(a,b), p4=(c,d)`.

On each of its 1796 accepted exact rational shape cells, the selected matching edges `p1p4` and `p2p3` are uniformly longer than the other four selected sides. The accepted normalized shape volume is

`V = 449/2500`.

For every accepted cell, choose strict guard radius `g` larger than all six pair distances and second-neighbor upper radius `u`. Exact enumeration gives

`g-u >= delta = 141/1000`,

and this geometry makes the quadruple a closed 3-nearest component whenever no external point lies in the union of the four radius-`gs` disks at scale `s`. Once NUV enters such a closed component, it must consume all four vertices consecutively; unless the last gadget vertex is the global terminal vertex, the exit contributes an additional `r_4-r_2 >= delta*s` to the `2L` charging inequality. The predecessor also proves disjoint charging from the earlier closed-two-nearest-triple correction.

It remains only to replace the predecessor's guard-area coefficient.

For any accepted normalized quadruple let `K` be its convex hull and `D=diam(K)`. Since `g` strictly exceeds every pair distance, `D<g`. The guard union is contained in `K+B_g`. By Steiner,

`|K+B_g| = A(K)+gP(K)+pi g^2`.

As proved above,

`A(K)<=D^2/2`,

`P(K)<(61/20)D`,

and `pi<22/7`. Therefore

`|K+B_g| < (937/140)g^2`.

The exact atlas has `g<=283/125`, so uniformly

`|guard at scale s| <= Q_diam s^2`,

with

`Q_diam = 75043393/2187500`.

For unit-intensity planar Poisson input, Campbell–Mecke now gives the ordered-quadruple density. Translation removes one vertex; polar coordinates for `p2-p1` contribute `2*pi*s ds`; the two remaining scaled point coordinates contribute `s^4`; the NUV bonus contributes `delta*s`; and the empty guard contributes at least `exp(-Q_diam s^2)`. Dividing by `4!` for unordered quadruples and by `2` to pass from the `2L` charging inequality to `L`, the atlas correction is at least

`(1/2)(1/4!)(2*pi) V delta * integral_0^infty s^6 exp(-Q_diam s^2) ds`.

Since

`integral_0^infty s^6 exp(-Q s^2) ds = 15 sqrt(pi)/(16 Q^(7/2))`,

this becomes

`Delta_diam >= (5*pi^(3/2)/128) V delta Q_diam^(-7/2)`.

For an exact rational lower certificate, use the predecessor's elementary lower bounds `pi>3`, `sqrt(pi)>17/10`, so

`5*pi^(3/2)/128 > 51/256`.

The exact checker also proves

`sqrt(Q_diam) < 5859/1000`.

Hence

`Delta_diam >= 13411559295654296875 / 628840228764059875161752016`

`= 2.1327451206507... * 10^(-8)`.

The predecessor atlas correction was

`Delta_old = 6759425885009765625 / 339829027379933753224631296`

`= 1.9890666601157... * 10^(-8)`.

This run **replaces** `Delta_old` by `Delta_diam`; it does not add a second charge for the same quadruples. Thus

`B_after = B_before - Delta_old + Delta_diam`.

Exact rational subtraction gives positive movement

`B_after-B_before = 19189889452953762467236313258680194091796875 / 13356135207391594264932791916480725342086163311543296`

`= 1.436784605350029... * 10^(-9)`.

The predecessor already supplied the finite-binomial transfer: fix a bounded scale range away from the square boundary, apply the exact binomial empty-region probability and factorial-moment formula, let `n -> infinity`, then enlarge the scale cutoff. Replacing its guard coefficient by a smaller rigorously valid uniform coefficient only strengthens the same transfer. No stabilization theorem or existence of the NUV limit is assumed.

This proves the displayed liminf bound. QED.

## 9. Exact finite certificate

The checker was executed before archival:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T14-05-00Z__p0257_diameter_guard_exact.py`

created at commit

`b9553b0eab3660e4026de99a563a827f84df1272`.

Archived output:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T14-05-00Z__p0257_diameter_guard_exact.out`

created at commit

`0e75532a6539417a42e84f0117411b156856f34a`.

The exact output independently verifies:

- candidate cells `17280`;
- accepted cells `1796`;
- accepted shape volume `449/2500`;
- minimum diagonal-minus-side squared gap `1/100`;
- minimum rank-gap bonus `141/1000`;
- maximum strict guard radius `283/125`;
- old rectangle coefficient `3827833/109375`;
- rational perimeter ratio upper bound `61/20`;
- new Steiner coefficient `937/140`;
- new guard coefficient `75043393/2187500`;
- `new_Q_lt_old_Q = True`;
- exact new atlas correction;
- `new_atlas_gt_old_atlas = True`;
- exact positive metric movement;
- exact new endpoint;
- `B_new_gt_0.6292579048 = True`;
- terminal line `ALL_EXACT_FINITE_CHECKS_PASS`.

The checker uses integer and `Fraction` arithmetic for every load-bearing finite comparison. Floating-point display values are explanatory only.

## 10. Fresh source / literature audit, dated 2026-09-19

Fresh bounded searches reopened:

1. Aldous's original source at Cambridge and arXiv (`arXiv:1912.13175`, DOI `10.1017/S0269964821000115`). The Cambridge abstract still says that establishing sharper results appears challenging.
2. Exact-title / `nearest unvisited vertex` / Euclidean random-points / NUV first-order-constant queries. They recovered the source, talks, and adjacent nearest-neighbor stochastic-geometry work but no checked later primary source settling the exact Euclidean first-order constant.
3. The small-convex-polygon perimeter literature. The 2025/2026 Mulansky–Potschka paper explicitly records the known exact diameter-one quadrilateral optimum `2+sqrt(6)-sqrt(2)` and its historical literature. This is treated as prior art and used only after checking that `K` is a planar convex hull with at most four vertices and diameter bounded by `g`.
4. Adjacent 2025–2026 nearest-neighbor geometric-probability papers, including work on nearest-neighbor embracing graphs and k-nearest-neighbor distance functions. These concern stabilizing graph/topological functionals, not the history-dependent NUV first-order source question, so no closure or off-the-shelf constant is inferred.

This is bounded negative evidence only. It does not establish worldwide openness, novelty, or priority. The new claim is the explicit P0257 lower-bound increment written above; no claim is made that the imported quadrilateral theorem is new.

## 11. Route discipline and status

The tracked quantity moved, so this is not an unchanged/stuck run.

- source: P0257;
- source status: **PARTIAL / OPEN**;
- frozen metric unchanged: `b_NUV`;
- before: `0.629257903387774956151863...`;
- after: `0.629257904824559561501892...`;
- movement: **YES**;
- admitted-target unchanged-run count: `0 -> 0`;
- HARD stuck recoveries consumed: `0/2 -> 0/2`;
- P26 audit: **NOT REQUESTED / NOT PRESUMED**;
- NM13-12 secondary audit: **NOT REQUESTED / NOT PRESUMED**.

This does not prove the existence of `lim L_n/n`, does not identify the proposed constant `c`, and is not source closure.

The next three genuinely untried Section-B methods are **#16 / #22 / #23**:

- **#16 COMPUTE EVERY SMALL CASE:** exact search for the smallest five-point closed-4-nearest motif whose charge is provably disjoint from the existing triple and quadruple charges;
- **#22 READ THE FAILURES:** inspect worst-case nearest-neighbor/TSP heuristic constructions and failed geometric-NN asymptotic approaches for motifs that force NUV excess rather than merely large tour length;
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT:** search deliberately for skinny/non-squarelike local traps rather than continuing the squarelike atlas geometry.

Merely refining the present 1/10 atlas mesh or tightening decimal square-root bounds is not an acceptable next route.

## 12. Scheduler/model-control truth

The prompt requests GPT-6 with maximum reasoning. The actual model exposed for this invocation is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so reasoning is **UNVERIFIED**. I do not claim GPT-6 maximum, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The currently exposed task-control surface still provides ordinary prompt/title, timing, enabled-state, list, and update controls, but exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated per-run applied-model/applied-effort receipt**. GPT-6/maximum therefore remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists those routing fields and attests them on the actual inference run.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary, not proof of global immutability: current repository `RESULTS.md` records a later successful P26 full update from another authorized context. If such a denial recurs, the compliant workaround is the owning or otherwise authorized account/workspace/API/admin context, an authorized ownership-transfer route where supported, or platform support for the same existing task. Do not duplicate the task or bypass permissions.

No scheduler, shared root, peer namespace, permission, workflow, email/Drive resource, public surface, or paid compute was modified.

## 13. Structured ledger delta for P26

```yaml
ledger_delta:
  task: NM13-11
  namespace: proofnet24/NM13-11/
  category: HARD_OUTSIDE
  source_id: P0257
  claim_id: P0257
  canonical_dedup_key: law_of_large_numbers_and_constants_for_nuv_lengths
  shard_mod_13: 10
  source_status: OPEN
  worker_status: PARTIAL
  metric_name: b_NUV
  metric_definition: "explicit certified b in liminf E[L_n]/n >= b for the exact Euclidean NUV source model"
  metric_before_exact: "1631470499263030121036034768604328605573396461083400872097661500093812049/2592689723052473092839289062500000000000000000000000000000000000000000000"
  metric_before_decimal: "0.629257903387774956151863323388440298..."
  metric_after_exact: "193214201572982934989857783744396430558567581073465840160154030146749346281/307050892951201110918824226562500000000000000000000000000000000000000000000"
  metric_after_decimal: "0.629257904824559561501892545793085654..."
  movement_exact: "19189889452953762467236313258680194091796875/13356135207391594264932791916480725342086163311543296"
  movement: true
  actual_methods:
    10: SUCCESS_DETERMINISTIC_DIAMETER_GUARD_COMPRESSION
    13: SUCCESS_MONOTONE_STEINER_PARALLEL_BODY_ENVELOPE
    21: SUCCESS_IMPORTED_KNOWN_SMALL_QUADRILATERAL_PERIMETER_THEOREM
  rejected_subroute: "complete removal of empty guard; closure of a 3-nearest quadruple genuinely requires an external-point exclusion"
  accepted_cells: 1796
  accepted_shape_volume: "449/2500"
  min_rank_gap: "141/1000"
  old_guard_Q: "3827833/109375"
  new_guard_Q: "75043393/2187500"
  new_atlas_lower_exact: "13411559295654296875/628840228764059875161752016"
  old_atlas_lower_exact: "6759425885009765625/339829027379933753224631296"
  replacement_not_addition: true
  finite_certificate:
    checker: proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T14-05-00Z__p0257_diameter_guard_exact.py
    checker_commit: b9553b0eab3660e4026de99a563a827f84df1272
    output: proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T14-05-00Z__p0257_diameter_guard_exact.out
    output_commit: 0e75532a6539417a42e84f0117411b156856f34a
    result: ALL_EXACT_FINITE_CHECKS_PASS
  unchanged_runs_before: 0
  unchanged_runs_after: 0
  hard_recoveries_before: "0/2"
  hard_recoveries_after: "0/2"
  audits:
    P26: NOT_REQUESTED_NOT_PRESUMED
    NM13-12: NOT_REQUESTED_NOT_PRESUMED
  next_methods: [16, 22, 23]
  next_step: "seek disjoint five-point rank traps and failure-informed non-squarelike motifs; do not refine the current mesh as the next route"
  predecessor_report_commit: 2a2568a61fb380659bbb53eef3e4e1a9b4620366
  frozen_pre_report_master: 0e75532a6539417a42e84f0117411b156856f34a
  ownership_conflict: false
  claim_mutated_this_run: false
  shared_roots_modified: false
```
