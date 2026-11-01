Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MATHEMATICAL MOVEMENT: `b_NUV >= 0.629257975756599543934040198570... -> b_NUV >= 0.629258017893725262672179871102... > 0.629258`; actual Section-B methods tried: #2, #20, #30.**

# NM13-11 — P0257 non-C4 chain sink-SCC movement

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-11` / `proofnet24/NM13-11/`  
Category: **HARD OUTSIDE**  
Source / canonical claim: **P0257** / `operations/claims/P0257.md`  
Status after this run: **PARTIAL / SOURCE OPEN**

## 1. Result and frozen metric

The frozen metric remains exactly the admitted quantity

`b_NUV = explicit certified endpoint in liminf_{n->infinity} E[L_n]/n >= b_NUV`

for Aldous's exact Euclidean random-points NUV model.

Before this run:

`b_NUV >=`

`1036840803576585538238788458409057357623753998433226173823634661443281840749793585890028594106544121959770829209188511 /`

`1647719764425586367726663550234487807993856583136701789232573772690085937500000000000000000000000000000000000000000000`

`= 0.6292579757565995439340401985708380554211313369994555292787087385...`.

This run proves an **additive**, topology-disjoint size-4 sink-component correction

`Delta_chain >= 3673530000 / 87180364995004919`

`= 4.213712571873813967253154108099...e-8`.

Therefore the new endpoint is

`b_NUV >=`

`67912972013875969263511036761749020093804681381152096968758979249620085662158905166455464312429913990367412237074967475168634442739 /`

`107925477439598903973574775478848995038155897130780425053567086312912915161198061867187500000000000000000000000000000000000000000000`

`= 0.6292580178937252626721798711023791364157856121266112675146799714...`.

So the certified metric crosses **0.629258**. The source problem remains open: this does **not** prove existence of Aldous's proposed limit `lim L_n/n`, and it does not identify that limit.

## 2. Authoritative continuity / required reads

The controlling predecessor is

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T18-00-30Z__p0257-sink-scc-boundary-movement.md`

created at commit `44302b6b1aa825ca27426fd89ccb599e8f7dcbf4`.

Before substantive work I freshly read or directly recovered:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the controlling NM13-11 predecessor above;
- newest neighboring NM13-10 report `2026-09-19T18-54-30Z__admission-delta-screen-48-p0434-owned-r11-p0157-hard-exhausted-no-r9-closable.md`;
- newest neighboring / designated-secondary-auditor NM13-12 report `2026-09-19T18-58-30Z__post-p0214-successor-delta-p0157-exhausted-vdh-r14-p0434-owned-no-admission.md`;
- canonical `operations/claims/P0257.md` after the substantive artifacts were written; and
- the exact predecessor-commit-to-prewrite Git comparison plus a final branch-head / claim read.

The complete comparison from the predecessor report commit to the initial prewrite head was `ahead 90 / behind 0 / too_large=null`. Its changed-file set contained one new unrelated canonical claim (`P0434`) and **no P0257 claim mutation, no P0257 release/handoff/retirement, no screened probability-intake mutation, and no controlling root/new-method/NM13 policy mutation**. The final canonical P0257 read still says `CLAIMED / ADMITTED / HARD OUTSIDE`, owner `proofnet24/NM13-11/`, canonical dedup key `law_of_large_numbers_and_constants_for_nuv_lengths`, SHA-256 `75bdfbc93f05ad07b271ad7a5a8046a16f0bb29d10236cbc1ebf0b8889fdf5e5`, residue `10 mod 13`.

No private-repository history known to be material to this continuation was inaccessible. The append-only historical corpora are too large for an honest claim that every unchanged byte was freshly rendered model-visible; I make no such claim. The exact complete Git delta is the continuity basis for unchanged material, with target-specific claim and neighboring state reopened directly.

## 3. Actual Section-B methods and outcomes

All thirty menu methods have appeared previously on P0257, so this run uses a **recycled, nonconsecutive** triple rather than misreporting them as unused.

### #2 ATTACK THE NEGATION FIRST — guard-free route refuted

The planned direction was to remove the explicit external empty-guard penalty from the size-4 sink-SCC construction. Attack the negation: suppose internal four-point shape data alone could certify that the four-set is a global sink SCC of the directed two-nearest-neighbor graph `D_2`.

That is false for a simple source-valid reason. Keep any four internal points fixed and place one additional point arbitrarily close to one gadget vertex `v`. That new point enters the two-nearest-neighbor set of `v`, creating an outgoing `D_2` arc from the four-set. Thus **no internal shape-only certificate can imply global sink status**. Some outside-point exclusion, or an equivalent rank condition involving the ambient process, is logically necessary.

Outcome: the stronger guard-free claim was refuted; no fake progress was assigned to it.

### #20 FIND WHY THE ALGORITHM FAILS — C4 was an unnecessary restriction

The failure above isolates the true obligation: external competition must be controlled, but the predecessor's internal bidirected-C4 topology is not required by the Hamiltonian-boundary lemma. What is actually needed is:

1. the four internal vertices induce a strongly connected `D_2` digraph; and
2. a finite guard ensures their global two-nearest neighbors remain internal.

This diagnoses a second, opposite loss in the old algorithm: it searched only square-like C4 shapes. A different robust strongly connected topology yields **new sink SCCs disjoint from the old C4 class**, so their boundary bonuses may be added instead of replacing the old term.

### #30 LOCALIZE ONE SCALE / ONE DIRECTION — success

Localize to a near-collinear four-point family with an exact rational shape box. This produces a positive-measure non-C4 topology, an exact finite guard, and a new explicit source-valid correction.

## 4. New non-C4 internal topology

Normalize an ordered quadruple by translation, rotation and scale so that

`p1=(0,0), p2=(1,0)`,

and let

`p3=(x3,y3)`, with `71/40 <= x3 <= 89/40`, `-1/2 <= y3 <= 1/2`,

`p4=(x4,y4)`, with `111/40 <= x4 <= 129/40`, `-1/2 <= y4 <= 1/2`.

The normalized shape volume is

`V_chain = (18/40)*1*(18/40)*1 = 81/400`.

Let `d_ij=|p_i-p_j|`. Exact interval bounds give

- `d13^2 <= 8321/1600`, while `d14^2 >= 12321/1600`;
- `d23^2 <= 2801/1600`, while `d24^2 >= 5041/1600`;
- `d34^2 <= 1241/400 = 4964/1600`, while `d31^2 >= 5041/1600`;
- `d42^2 <= 8321/1600`, while `d41^2 >= 12321/1600`.

Hence throughout the entire shape box the internal two-nearest-neighbor sets are exactly

`N2(p1)={p2,p3}`,

`N2(p2)={p1,p3}`,

`N2(p3)={p2,p4}`,

`N2(p4)={p3,p2}`.

The tight squared ranking slack is

`5041/1600 - 4964/1600 = 77/1600 > 0`.

This digraph is strongly connected: `p1 <-> p2 <-> p3 <-> p4` is contained in it. It is **not** the predecessor's bidirected C4 topology: for example, both endpoints point into the overlapping triangle-chain structure rather than having the C4 neighbor pattern.

Every internal second-neighbor distance is at most `sqrt(8321/1600)`. Set

`U = 229/100`.

Then

`U^2 - 8321/1600 = 1739/40000 > 0`.

## 5. Source-valid global sink guard

Set

`H = 57/20`, so `H-U = 14/25`.

For a physical scale `s`, require that no point outside the quadruple lies within distance `Hs` of any of the four gadget points. Since every internal second-neighbor distance is `< Us < Hs`, this guard forces all global `D_2` outgoing arcs of the four vertices to stay inside the four-set. Combined with the internal strong connectivity above, the set is a global size-4 sink SCC.

For every normalized shape in the family, all four centers lie in the rectangle

`[0,129/40] x [-1/2,1/2]`.

The union of four radius-`H` guard disks is contained in the `H`-parallel body of this rectangle. Its area is exactly

`wh + 2H(w+h) + pi H^2`

with `w=129/40`, `h=1`. Using `pi < 22/7`,

`Area_guard/s^2 <= Q := 147939/2800 = 52.835357142857...`.

Also

`(727/100)^2 - Q = 307/17500 > 0`,

so `sqrt(Q) < 727/100`.

This guard is explicit and finite. The run does **not** claim the logically impossible shape-only removal refuted in Section 3.

## 6. Boundary charge and disjointness

Use the predecessor's already proved sink-SCC Hamiltonian-boundary lemma. For any Hamiltonian path, in particular the NUV path, every proper sink SCC not containing a global path endpoint has at least two path-boundary crossings. Each crossing from or into a guarded component has length at least `Hs`, while the degree-two nearest-neighbor baseline at the internal endpoint is at most `Us`. Consequently the total `2L` surplus of a nonendpoint component is at least

`2(H-U)s`,

hence the `L`-side surplus is at least

`(H-U)s = (14/25)s`.

There is no double counting with the existing size-4 C4 term. In a tie-free configuration, the global `D_2` out-neighbor sets are unique, so one four-vertex sink SCC cannot simultaneously have the predecessor's bidirected-C4 internal topology and the new chain topology. Distinct sink SCCs of the same directed graph are vertex-disjoint. Therefore:

- old size-3 sink components,
- old size-4 C4 sink components,
- the new size-4 chain sink components, and
- old size-5 C5 sink components

can all be charged simultaneously without vertex overcharge.

This is why `Delta_chain` is **added** to the predecessor endpoint rather than replacing an existing term.

## 7. Exact-binomial / Campbell-Mecke transfer

Work in the exact source scaling: `n` iid uniform points in the square of area `n`, density one. Fix a scale cutoff `s<=M` and restrict anchors to an interior region whose distance from the square boundary is enough to contain the finite guard. The excluded boundary area is `O(sqrt(n))`, hence its area divided by `n` tends to zero for fixed `M`.

Parameterize an ordered quadruple by anchor `x`, scale `s`, rotation `theta`, and shape coordinates `(x3,y3,x4,y4)` above. The relative-coordinate Jacobian is

`s^5 ds dtheta dx3 dy3 dx4 dy4`.

For a fixed ordered quadruple, the exact density factor from the binomial model is `(n)_4/n^4`, and conditional on the quadruple the probability that the other `n-4` points avoid a guard of area `A` is

`(1-A/n)^(n-4)`.

For fixed shape and scale this tends to `exp(-A)`, and because `A <= Qs^2`, it is bounded below in the limit by `exp(-Qs^2)`. Divide the ordered count by `4!`; even if one unordered component admits several accepted orderings, this can only undercount it because there are at most `4!` orderings.

For fixed `M`, dominated convergence therefore gives the new asymptotic `L`-side density lower bound

`(1/4!)*(2*pi)*V_chain*(14/25) * integral_0^M s^6 exp(-Q s^2) ds`.

At most two sink SCCs contain global Hamiltonian-path endpoints. On `s<=M` discarding them costs `O(M)=o(n)` after normalization. Letting `n->infinity` first and then `M->infinity`, monotone convergence gives

`Delta_chain >= (1/4!)*(2*pi)*V_chain*(14/25) * integral_0^infinity s^6 exp(-Q s^2) ds`.

Since

`integral_0^infinity s^6 exp(-Q s^2) ds = 15 sqrt(pi)/(16 Q^(7/2))`,

we obtain

`Delta_chain >= (5*pi^(3/2)/64)*(81/400)*(14/25)*Q^(-7/2)`.

Use only the rational one-sided bounds

`pi > 3`, `sqrt(pi) > 17/10`, `sqrt(Q) < 727/100`.

The exact checker then gives

`Delta_chain >= 3673530000/87180364995004919`

`= 4.213712571873813967253154108099...e-8 > 4.2e-8`.

Adding this topology-disjoint correction to the predecessor endpoint gives the metric in Section 1.

## 8. Exact self-check artifacts

The idea was written before checker code at

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T19-05-00Z__p0257_chain_sink_idea.md`

creation commit `842b1294eeef321db2a2baa0bfec05c9f5601038`.

Exact checker:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T19-05-30Z__p0257_chain_sink_exact.py`

creation commit `d7ade15d16c11fe4c3224047cf144b1fcb1830f4`.

Archived execution output:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T19-05-30Z__p0257_chain_sink_exact.out`

creation commit `63d07f8381a3b76185f5554c76382b793946b07e`.

The output certifies, among other facts,

- `V_CHAIN = 81/400`;
- `MIN_TOPOLOGY_GAP = 77/1600`;
- `U2_SLACK = 1739/40000`;
- `H_MINUS_U = 14/25`;
- `Q_UPPER = 147939/2800`;
- `SQRTQ_SQUARE_SLACK = 307/17500`;
- `DELTA_CHAIN_EXACT = 3673530000/87180364995004919`;
- `DELTA_CHAIN_GT_4_2E_8 = True`;
- `B_NEW_GT_0_629258 = True`;
- final line `ALL_EXACT_FINITE_CHECKS_PASS`.

This is an NM13-11 **self-check**, not an independent audit.

## 9. Fresh source / literature check, dated 2026-09-19

Queries actually run this invocation included:

- exact title `"The Nearest Unvisited Vertex Walk on Random Graphs"`;
- DOI `10.1017/S0269964821000115` with 2023--2026 terms;
- `"nearest unvisited vertex" walk random graphs 2023 2024 2025 2026`;
- `"nearest unvisited vertex" Aldous Euclidean square limit`;
- Aldous's current research page for the NUV challenge.

The original Cambridge/PEIS article remains the source. Its abstract says sharper results appear challenging; Section 3 states the random-points square scaling and proposed first-order constant and says only an `O(n)` bound is known there in the source.

Aldous's currently crawled Berkeley page separately lists the NUV problem with the text that the walk has order-`n` length and the challenge is to improve beyond order-of-magnitude. The same page's 2023 improved bounds concern the **largest common subtree** item immediately above NUV, not NUV; this was checked explicitly to avoid a false literature-status inference.

The bounded 2023--2026 exact-title / DOI / Euclidean-square searches did not surface a checked later primary paper resolving the source's Euclidean first-order constant. Adjacent first-passage-percolation and nearest-neighbor work was also surfaced, but no theorem from it was used to claim the NUV limit solved. This is bounded negative evidence only: it is **not** proof of worldwide openness, novelty, priority, or correctness of the present argument.

## 10. Counters, status, and next route

- source status: **PARTIAL / SOURCE OPEN**;
- metric before: `0.6292579757565995439340401985708380554211...`;
- metric after: `0.6292580178937252626721798711023791364158...`;
- mathematical movement: **yes**, `+3673530000/87180364995004919 > 4.2e-8`;
- ordinary unchanged-run counter: **0**;
- HARD stuck-recovery episodes consumed: **0/2**;
- P26 audit: **NOT REQUESTED / NOT PRESUMED**;
- NM13-12 audit: **NOT REQUESTED / NOT PRESUMED**;
- no closure claim; no paper folder.

Next research triple: **#6 / #21 / #29** (recycled, nonconsecutive): deform the uniform `H` guard toward the exact vertex-wise `r_2` exclusion radii; check the nearest-neighbor component / Palm literature for an applicable component-intensity identity; and integrate the resulting shape-dependent guard all the way through the scale tail. Merely subdividing the present chain box or tightening decimal constants is not the next route.

## 11. Model-control / interface note

The runtime actually reports **GPT-5.6 Sol**; the reasoning-effort value is not authenticated, so it is **UNVERIFIED**. The exposed task-control interface still provides prompt/title, timing/schedule controls and enabled state, but no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated per-run applied-model/effort receipt. Thus `GPT-6 / maximum` remains a prompt request here, not an enforceable setting.

Changing that would require an owner-authorized product/workspace/API/admin task surface that persists model-family and reasoning-effort fields into inference routing and returns an authenticated applied-setting receipt. I did not claim or initiate a support escalation. The historical P26 `You cannot modify this task` event remains an authorization-context boundary; the compliant workaround is to act from the owning / otherwise authorized context for that same task, or use an authorized ownership/support repair path — not to duplicate the task or bypass permissions.

No scheduler, shared root ledger, peer namespace, permission, workflow, email/Drive resource, public posting, or paid compute was modified in this invocation.

## 12. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-11
  source_id: P0257
  claim_id: P0257
  owner: proofnet24/NM13-11/
  category: HARD_OUTSIDE
  status: PARTIAL
  source_status: OPEN
  metric_name: b_NUV
  metric_statement: "liminf_{n->infinity} E[L_n]/n >= b_NUV"
  metric_before_exact: "1036840803576585538238788458409057357623753998433226173823634661443281840749793585890028594106544121959770829209188511/1647719764425586367726663550234487807993856583136701789232573772690085937500000000000000000000000000000000000000000000"
  metric_before_decimal: "0.6292579757565995439340401985708380554211313369994555..."
  new_correction_exact: "3673530000/87180364995004919"
  new_correction_decimal: "4.213712571873813967253154108099e-8"
  metric_after_exact: "67912972013875969263511036761749020093804681381152096968758979249620085662158905166455464312429913990367412237074967475168634442739/107925477439598903973574775478848995038155897130780425053567086312912915161198061867187500000000000000000000000000000000000000000000"
  metric_after_decimal: "0.6292580178937252626721798711023791364157856121266113..."
  mathematical_movement: true
  actual_methods:
    - "#2 ATTACK THE NEGATION FIRST: refuted shape-only/guard-free sink certification by an external-intruder counterexample"
    - "#20 FIND WHY THE ALGORITHM FAILS: isolated external competition as necessary, C4 topology as unnecessary"
    - "#30 LOCALIZE: proved a positive-measure near-collinear non-C4 size-4 D2 sink family"
  artifact_checker: "proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T19-05-30Z__p0257_chain_sink_exact.py"
  artifact_output: "proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T19-05-30Z__p0257_chain_sink_exact.out"
  self_check_result: ALL_EXACT_FINITE_CHECKS_PASS
  unchanged_runs: 0
  hard_recoveries_used: 0
  hard_recoveries_limit: 2
  audits:
    P26: NOT_REQUESTED_NOT_PRESUMED
    NM13-12: NOT_REQUESTED_NOT_PRESUMED
  next_methods: ["#6", "#21", "#29"]
  next_step: "Replace the uniform external guard by vertex-wise r2 exclusion radii and seek a Palm/component identity with exact finite-binomial transfer; do not merely refine this box."
```
