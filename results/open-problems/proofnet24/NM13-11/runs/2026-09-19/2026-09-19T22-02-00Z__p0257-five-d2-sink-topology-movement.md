Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MATHEMATICAL MOVEMENT: `b_NUV >= 0.629258046438982198074857419668... -> b_NUV >= 0.629258051845519310707290096835... > 0.6292580518`; actual Section-B methods tried: #1, #17, #26.**

# NM13-11 — P0257 five-vertex D2 sink-topology movement

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-11` / `proofnet24/NM13-11/`  
Category: **HARD OUTSIDE**  
Canonical source / claim: **P0257 / `operations/claims/P0257.md`**  
Canonical dedup key: `law_of_large_numbers_and_constants_for_nuv_lengths`  
Exclusive shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 10`  
Status after this invocation: **PARTIAL / SOURCE OPEN**

## 1. Continuity, exact source, ownership, and frozen metric

This invocation continues the already-admitted P0257 source, David J. Aldous, *The Nearest Unvisited Vertex Walk on Random Graphs* (arXiv:1912.13175; *Probability in the Engineering and Informational Sciences* 36 (2022), 851--867, DOI `10.1017/S0269964821000115`). It does **not** reopen intake, create a second claim, or select a replacement source.

I reread the current canonical claim immediately before the report write. It still records:

- status `CLAIMED / ADMITTED / HARD OUTSIDE`;
- owner `proofnet24/NM13-11/`;
- canonical dedup key `law_of_large_numbers_and_constants_for_nuv_lengths`;
- SHA-256 `75bdfbc93f05ad07b271ad7a5a8046a16f0bb29d10236cbc1ebf0b8889fdf5e5`;
- shard residue **10 mod 13**;
- the exact Euclidean iid random-points NUV model.

No P0257 release, handoff, retirement, competing owner, or alias collision was recovered. The current neighboring NM13-10 report remains in residue-9 admission-screen mode; the current neighboring/designated-secondary-auditor NM13-12 report remains `ADMISSION_PENDING` on its residue-11 successor screen and explicitly identifies this track as still active on P0257. Neither changes ownership.

The frozen metric remains

`b_NUV = explicit certified endpoint in liminf_{n->infinity} E[L_n]/n >= b_NUV`

for the source's area-`n` Euclidean square scaling.

The controlling predecessor is

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T21-05-00Z__p0257-third-d2-topology-movement.md`

created at commit

`6838ea8659440628fbbe096e1f0ec083f01d3e8a`.

Its endpoint is the exact before-value

`B_before =`

`428290077362103688393910556289374260624427851669128955928061085239297514491295131572164454010069801964500982465126129692695841537835318496791550852459470618357 /`

`680627096921253366568966735604927531896699764460645393329189347179240150914086801287321056287307690561375724195312500000000000000000000000000000000000000000000`

`= 0.62925804643898219807485741966892183185153667694165072529760564624780775011797113...`.

This run proves a new additive correction

`Delta_5sink >= 35802000 / 6621983582864573`

`= 5.4065371126324326771669787844248559859...e-9 > 5.4e-9`.

Therefore

`B_after =`

`257829989578496350414183523146605335856248997408453788237962025484814476957683136019074638921462335179814079007196663994330380573638384791944133112730116386394080336881706051 /`

`409736496533210395577129470979508748365626015570562389564441613457911228367916571422161933413348402679750261900585439123098992187500000000000000000000000000000000000000000000`

`= 0.62925805184551931070729009683590061627639266285210461589341007849834871417375502...`.

In particular,

`b_NUV > 0.6292580518`.

The source remains open. This does **not** prove existence of Aldous's proposed limit `lim L_n/n`, does not identify that limit, and does not upgrade P0257 to PROVED.

## 2. Required repository continuity and race check

Before substantive work I freshly read or directly recovered current state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the controlling NM13-11 predecessor above and the relevant earlier five-point/C4/chain sink-SCC reports;
- newest completed neighboring NM13-10 report `proofnet24/NM13-10/runs/2026-09-19/2026-09-19T20-52-30Z__admission-delta-screen-50-e0011-released-r6-no-r9-closable.md`;
- newest completed neighboring/designated-secondary-auditor NM13-12 report `proofnet24/NM13-12/runs/2026-09-19/2026-09-19T21-59-30Z__post-p0214-successor-delta-f0111-projective-p0487-offshard-p0205-ambiguous.md`;
- current `operations/claims/P0257.md`;
- repository-wide P0257 / canonical-key searches;
- the historical canonical problem/attempt continuity, including campaign row P0257 and prior attempt `P0257-A001`, whose only pre-NM13 mechanism was the old nearest-neighbor lower-bound calculation; and
- a Git comparison from the predecessor creation commit to the final prewrite branch head.

Large append-only intake/source/attempt corpora cannot honestly be claimed byte-for-byte model-visible in one connector response. I do not make that claim. Candidate-specific canonical identity, aliases, source, prior-attempt state, ownership and lifecycle were reopened directly; missing bulk rendering was not treated as permission to restart history.

Final prewrite `master` was

`87630358a230b3d765a5b53007eed98581391e6e`.

The exact GitHub comparison

`6838ea8659440628fbbe096e1f0ec083f01d3e8a .. 87630358a230b3d765a5b53007eed98581391e6e`

reported status `ahead`, **107 commits ahead**, **0 behind**. The connector response is itself truncated when rendering this large comparison, so I do not claim that every changed-path entry was visible from that one response. I separately reread the canonical P0257 claim at the prewrite head and found it unchanged and still exclusively owned by NM13-11. The required root/campaign control files read this run likewise did not disclose a P0257 release, settlement, posting, or retirement.

No private-repository history known to be material to this continuation was inaccessible.

## 3. Runtime / model-control truth

The prompt requests `Model: GPT-6. Reasoning: maximum`. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, verified maximum reasoning, a binding maximum-effort setting, a guaranteed hour-long execution, or a support escalation.

The exposed scheduled-task control schema provides title/prompt, schedule or relative-start data, timing mode, enabled state, listing and ordinary updates. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated applied-model/applied-effort receipt**. GPT-6/maximum therefore remains prompt text only on this surface.

Making the requested setting binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists explicit model-family and reasoning-effort fields into inference routing and returns trustworthy per-run attestation.

Repository continuity records that one earlier P26 context returned `You cannot modify this task`, while a later authorized context successfully updated P26. Thus the denial is authorization/context-specific rather than proof of global immutability. If it recurs, the compliant remedy is the same task's owning or otherwise authorized product/workspace/API/admin context, supported ownership/permission repair where available, or authorized platform support — not duplication, identity substitution, or permission bypass.

No scheduler, task configuration, permission, workflow, email/Gmail, Drive resource, public surface, paid-compute resource, shared root ledger, peer namespace, or canonical P0257 claim was modified in this invocation.

## 4. Fresh bounded source/literature check — 2026-09-19 UTC

This is bounded current-status evidence, not proof of worldwide openness, novelty, or priority.

Fresh public checks recovered:

1. Cambridge's current page for Aldous's NUV article, DOI `10.1017/S0269964821000115`, still gives the PEIS 36(3), July 2022 publication and says in the abstract that establishing sharper results appears challenging.
2. Aldous's currently crawled Berkeley home/research page still lists **The Nearest Unvisited Vertex Walk on Random Graphs** and the challenge to improve beyond order-of-magnitude results for models of random graphs.
3. Aldous's current publication list still lists the 2022 NUV paper; bounded exact-title / `nearest unvisited vertex` / Euclidean-random-points searches did not surface a checked later primary source resolving the Euclidean first-order constant problem.
4. For method #17, a public search for the exact finite digraph count surfaced William Ostroff's thesis *Counting Connected Digraphs with Gradings*, whose search-index rendering of Table 6 lists strongly connected loopless 2-regular digraph counts `1, 69, 5346` for `n=3,4,5`. Direct PDF opening returned HTTP 502 in this run, so that item is treated only as a bounded external cross-check, not as load-bearing proof. The exact checker independently enumerates the finite objects from first principles.

Search/access scope: public web/Cambridge/Berkeley plus bounded search indexing visible on 2026-09-19 UTC. Negative search evidence is not a bibliographic-completeness certificate.

## 5. Section-B methods genuinely attempted — #1 / #17 / #26

All thirty Section-B moves have already appeared at least once in P0257 history. This invocation therefore uses the predecessor's planned **recycled, nonconsecutive** triple #1/#17/#26 and does not misreport them as unused. The mathematical route was written before checker code in

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T21-49-00Z__p0257_five_sink_digraph_idea.md`

commit

`f8a26523b1aab7e024d09f83a42c523468210f02`.

### #1 CHANGE THE CATEGORY — success

Move from coordinate-box gadget hunting to the finite topology of the directed two-nearest-neighbor graph `D_2`. The predecessor already had three additive size-4 sink-SCC topology classes. For five vertices, a qualifying chart with one fixed labeled strongly connected 2-out digraph has an additional advantage: ordered factorial-moment tuples need only be divided by the automorphism group of that digraph, not mechanically by `5!`.

That automorphism correction is exact. If the same unordered five-set has two labelings lying in the chart, both labeled `D_2` graphs equal the same target adjacency `A`; the permutation between those labelings must therefore be an automorphism of `A`. Thus the number of valid chart labelings of one set is at most `|Aut(A)|`.

### #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE — useful cross-check, not the proof

A first-principles exact enumerator of loopless labeled outdegree-two digraphs gave strongly connected counts

`n=3: 1, n=4: 69, n=5: 5346`.

The bounded literature search surfaced the same `1,69,5346` row in Ostroff's Table 6 search-index rendering. Because direct PDF access failed in this run and because that literature count does not imply Euclidean realizability, no source progress is credited to the citation itself. It is only a sanity check on the finite enumeration convention.

### #26 HUNT THE SPORADIC CASE — success

Search for a five-vertex Euclidean `D_2` sink topology genuinely different from the already charged C5 family. The exact rational chart below realizes one with automorphism group of order **2**, giving a much smaller multiplicity penalty than `5!`.

## 6. Exact five-point positive-measure chart

Normalize an ordered five-tuple by translation, rotation and scale so that

`p0=(0,0), p1=(1,0)`.

Let

`3/10 <= x2 <= 21/50`, `-1/10 <= y2 <= 1/50`,

`-13/50 <= x3 <= -7/50`, `-3/20 <= y3 <= -3/100`,

`59/100 <= x4 <= 71/100`, `-13/100 <= y4 <= -1/100`.

The six-dimensional normalized volume is

`V = (3/25)^6 = 729/244140625 = 0.000002985984`.

Exact interval arithmetic proves uniformly on the whole chart that the global internal ranking, before adding external points, is

`N2(0)={2,3}`,

`N2(1)={2,4}`,

`N2(2)={0,4}`,

`N2(3)={0,2}`,

`N2(4)={1,2}`.

The five exact squared-distance ranking gaps are

`809/5000, 1/2, 3/1000, 26/625, 197/1250`,

so the minimum is the strict positive value

`3/1000`.

The target digraph is strongly connected. Its canonical adjacency tuple over all 120 relabelings is

`((1,2),(0,2),(0,3),(2,4),(2,3))`.

Its automorphism group has exactly two elements,

`id` and `(0 4)(1 3)` with vertex `2` fixed.

The checker also canonicalizes the previously charged five-cycle topology and proves the two canonical classes differ. Therefore a global size-5 sink SCC counted here cannot be one of the existing C5 five-point components.

For additional finite sanity checking, the same exact program enumerates every loopless labeled outdegree-two digraph and independently obtains the strongly connected counts `(1,69,5346)` for sizes 3,4,5.

## 7. Guarded sink-SCC charge

The largest certified internal second-neighbor squared distance over this chart is exactly bounded by

`1/2`.

Set

`U=71/100`, `H=21/25`.

Then

`U^2 - 1/2 = 41/10000 > 0`,

`H-U = 13/100 > 0`.

If no source point outside the selected five lies within distance `H r` of any selected vertex, where `r=|x1-x0|`, then each selected vertex's two global nearest neighbors are internal. Because the internal directed graph is strongly connected, the five-set is a **sink SCC of the global `D_2` graph**.

The predecessor's topology-independent Hamiltonian-boundary theorem applies: a proper sink SCC that contains neither global Hamiltonian-path endpoint has at least two path-boundary crossings. With internal `r_2(v) <= U r` and external distance at least `H r`, these two crossings yield an `L`-side surplus of at least

`(H-U) r`.

At most two sink SCCs can contain the two global path endpoints. Under a fixed scale cutoff `r<=M`, discarding them loses only `O(M)`, hence `o(n)` after division by `n`.

### Additive accounting

Distinct SCCs of one directed graph are vertex-disjoint. The predecessor's charged size-3 and size-4 components are `D_2` sink SCCs, and its retained five-point Palm family has the C5 `D_2` topology. The present component has size 5 and a non-C5 canonical topology. It therefore cannot overlap any of those charged SCCs. This run **adds** the new class; it does not replace or duplicate the retained C5 five-point term.

For one unordered component there can be at most two valid chart labelings. If both occur, their normalization lengths need not agree, but the actual component surplus is at least the maximum of the two labeled lower bounds, hence at least half their sum. Dividing the ordered weighted tuple count by `|Aut(A)|=2` is therefore rigorous.

## 8. Exact guard area and finite-binomial transfer

All normalized chart points lie in

`[-13/50,1] x [-3/20,1/50]`,

with width

`w=63/50`

and height

`h=17/100`.

The union of radius-`H r` guard disks lies inside the `H r` parallel body of that rectangle. Therefore its area is at most

`r^2 [w h + 2H(w+h) + pi H^2]`.

Using the classical bound `pi < 22/7`, define the exact rational envelope

`Q = 24171/5000 = 4.8342`.

Also

`(11/5)^2 - Q = 29/5000 > 0`,

so `sqrt(Q) < 11/5`.

Now work in the source-equivalent square of area `n` with exactly `n` iid uniform points. Fix `M`, restrict `0<r<=M`, and keep the anchor `x0` at distance `2M` from the boundary; the discarded boundary fraction is `o(1)` for fixed `M`. For a selected ordered five-tuple, the other `n-5` source points avoid its guard with exact conditional probability

`(1-|G|/n)^(n-5)`.

For fixed tuple geometry this tends to `exp(-|G|)` and is bounded below in the limit by `exp(-Q r^2)`. The normalized-coordinate map has Jacobian `r^6` for the three free normalized points, while `dv = r dr dtheta`. Multiplying by the `L`-side bonus `(H-U)r`, dividing by the chart multiplicity bound 2, taking `n->infinity` first, and then `M->infinity`, gives

`Delta_5sink >= (2*pi/2) V (H-U) integral_0^infinity r^8 exp(-Q r^2) dr`.

Since

`integral_0^infinity r^8 exp(-Q r^2) dr = 105 sqrt(pi)/(32 Q^(9/2))`,

we obtain

`Delta_5sink >= 105 pi^(3/2) V (H-U) / (32 Q^(9/2))`.

For a completely rational lower certificate use

`pi^(3/2) > 51/10`

because `pi>3` and `sqrt(pi)>17/10` follows from `3>(17/10)^2`, together with `sqrt(Q)<11/5`. Then

`Delta_5sink > 35802000 / 6621983582864573`

`= 5.4065371126324326771669787844248559859...e-9`.

This transfer is through the **exact finite binomial source model**. It does not assume Poissonization as a theorem, stabilization of NUV, simulation, or existence of `lim L_n/n`.

## 9. Exact checker and archived execution

Idea note first:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T21-49-00Z__p0257_five_sink_digraph_idea.md`

commit `f8a26523b1aab7e024d09f83a42c523468210f02`.

Exact-arithmetic checker:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T21-54-00Z__p0257_five_sink_digraph_exact.py`

commit `4d35d8204a3a04ff66d21cd10e2e0e2cfd0af987`.

Archived executed output:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T21-54-00Z__p0257_five_sink_digraph_exact.out`

commit `1e8e166704694787ffbe73e18d7e90a9b2de36e4`.

The output certifies, among other things:

- `MIN_RANK_GAP = 3/1000`;
- `MAX_SECOND_NEIGHBOR_SQ = 1/2`;
- exact two-element automorphism group;
- exact strong-outdegree-two counts `(1,69,5346)` for `n=3,4,5`;
- `QBAR = 24171/5000`;
- `DELTA_GT_5_4E_9 = True`;
- `B_AFTER_GT_0_6292580518 = True`; and
- terminal line **`ALL_EXACT_FINITE_CHECKS_PASS`**.

This is a **self-check**, not an independent audit.

## 10. Status, counters, and next research route

The metric moved, so

- `unchanged_runs = 0`;
- HARD stuck recoveries used remain `0/2`;
- P26 audit: **NOT REQUESTED / NOT PRESUMED**;
- NM13-12 audit: **NOT REQUESTED / NOT PRESUMED**.

P0257 remains **PARTIAL / SOURCE OPEN**.

The next recycled, nonconsecutive Section-B triple is **#14 / #16 / #24**:

- #14 FIND THE GROUP ACTING: classify five-vertex D2 sink topologies by automorphism orbit before any coordinate search;
- #16 COMPUTE EVERY SMALL CASE: exact semialgebraic/interval feasibility screen over the remaining size-5 topology classes, not a simulation;
- #24 FIND THE EXTREMAL OBJECT: optimize the certified quantity `shape-volume * boundary-gap / guard^(9/2)` over a topology class rather than tightening one already-used box.

The route should be abandoned if it ceases to move `b_NUV`; another certificate for the same bound is not progress.

```yaml
ledger_delta:
  worker: NM13-11
  source_id: P0257
  claim_path: operations/claims/P0257.md
  source_status: OPEN
  worker_status: PARTIAL
  metric_name: b_NUV
  metric_definition: explicit certified endpoint in liminf E[L_n]/n >= b_NUV
  metric_before_decimal: 0.62925804643898219807485741966892183185153667694165072529760564624780775011797113
  metric_after_decimal: 0.62925805184551931070729009683590061627639266285210461589341007849834871417375502
  movement_exact: 35802000/6621983582864573
  movement_decimal: 5.4065371126324326771669787844248559859e-9
  movement: true
  methods:
    "1": "success: recast local geometry as a fixed five-vertex D2 sink-digraph topology with automorphism-controlled counting"
    "17": "useful cross-check: exact digraph counts 1,69,5346 matched a bounded literature-search table; not load-bearing"
    "26": "success: new positive-measure non-C5 five-point Euclidean sink topology, exact guard and transfer"
  unchanged_runs: 0
  hard_recoveries_used: 0
  hard_recoveries_limit: 2
  p26_audit: NOT_REQUESTED
  nm13_12_audit: NOT_REQUESTED
  idea_commit: f8a26523b1aab7e024d09f83a42c523468210f02
  checker_commit: 4d35d8204a3a04ff66d21cd10e2e0e2cfd0af987
  output_commit: 1e8e166704694787ffbe73e18d7e90a9b2de36e4
  prewrite_master: 87630358a230b3d765a5b53007eed98581391e6e
  next_methods: [14, 16, 24]
  next_step: "classify and interval-screen remaining size-5 D2 sink topology orbits, then optimize a genuinely new feasible class"
  bounded_literature_check_date: 2026-09-19
```
