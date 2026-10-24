Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MATHEMATICAL MOVEMENT: `b_NUV >= 0.629258017893725262672179871102... -> b_NUV >= 0.629258030552741666144008725369... > 0.62925803`; actual Section-B methods tried: #6, #21, #29.**

# NM13-11 — P0257 shape-dependent capsule-guard movement

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-11` / `proofnet24/NM13-11/`  
Category: **HARD OUTSIDE**  
Canonical source / claim: **P0257** / `operations/claims/P0257.md`  
Status after this run: **PARTIAL / SOURCE OPEN**

## 1. Frozen source model and metric

The source remains David J. Aldous, *The Nearest Unvisited Vertex Walk on Random Graphs*, arXiv:1912.13175; *Probability in the Engineering and Informational Sciences* 36 (2022), 851–867. The exact admitted Euclidean model is unchanged: `n` iid uniform points in the unit square, complete Euclidean graph, a uniform random starting vertex, and the nearest-unvisited-vertex walk. With `L_n = sqrt(n)L_n^*` in the source's area-`n` scaling, the frozen NM13-11 metric is

`b_NUV = explicit certified endpoint in liminf_{n->infinity} E[L_n]/n >= b_NUV`.

The source asks for sharper first-order information, including existence/identification of the proposed limit `c = lim L_n/n`. This run does **not** prove that limit exists and does not identify it.

Before this run the certified endpoint was

`B_prev =`

`67912972013875969263511036761749020093804681381152096968758979249620085662158905166455464312429913990367412237074967475168634442739 /`

`107925477439598903973574775478848995038155897130780425053567086312912915161198061867187500000000000000000000000000000000000000000000`

`= 0.62925801789372526267217987110237913641578561212661126751467997140556...`.

This run proves the strict net improvement

`NET =`

`1207847451541900648780089152 / 95414004772964790053367229345754775`

`= 1.2659016403471828854267084934929984...e-8 > 1e-8`.

Therefore

`B_new =`

`12234885369899315774910192590367613149468633559630832101342942986342507415367247043258638762394714330725215296855853141419683832042798882673372297 /`

`19443351973040638050987304673433346221975007518723198189172396736647229533566751930247359385542476562500000000000000000000000000000000000000000000`

`= 0.62925803055274166614400872536946407134576963775759390287615784963581... > 0.62925803`.

This is movement in the same frozen source-relevant metric; no metric substitution occurred.

## 2. Authoritative continuity, ownership and required reads

The controlling predecessor is

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T19-00-00Z__p0257-nonc4-chain-sink-movement.md`

created at commit `3f2171449edf3c93155079ab659a87908a73f0b7`.

Before substantive work I freshly read or directly recovered:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the controlling NM13-11 predecessor above;
- the newest neighboring NM13-10 and NM13-12 reports recovered before research;
- current canonical `operations/claims/P0257.md`;
- targeted P0257 canonical-key / attempted-unsolved history searches; and
- a predecessor-commit-to-prewrite Git comparison plus branch-head race checks.

The append-only intake/source/attempt corpora are too large for an honest claim that every unchanged historical byte was re-rendered model-visible in one connector invocation. I make no such claim. Candidate-specific P0257 identity, ownership, attempt status and current claim were reopened directly; unchanged bulk state is carried by the complete Git delta.

Final frozen pre-report `master` used for continuity was `527aa6c296f809a51e3be7b3bfb78e2b5193378c`. Exact comparison

`3f2171449edf3c93155079ab659a87908a73f0b7 .. 527aa6c296f809a51e3be7b3bfb78e2b5193378c`

returned `ahead_by=112`, `behind_by=0`, `total_commits=112`. The interval contains unrelated fleet work and at least one unrelated new canonical claim; it does **not** contain a P0257 ownership release, handoff or retirement recovered by the target-specific checks. Current P0257 remains `CLAIMED / ADMITTED / HARD OUTSIDE`, owner `proofnet24/NM13-11/`, canonical key `law_of_large_numbers_and_constants_for_nuv_lengths`, SHA-256 `75bdfbc93f05ad07b271ad7a5a8046a16f0bb29d10236cbc1ebf0b8889fdf5e5`, residue `10 mod 13`.

The historical intake status remains `attempted_unsolved`; the pre-NM13 structural route was the nearest-neighbor floor. This run does not relabel that history or duplicate ownership under another ID.

## 3. Actual Section-B methods and outcomes

All thirty Section-B methods have appeared previously on P0257, so this invocation uses a **recycled, nonconsecutive** triple rather than falsely calling it unused. The immediate predecessor used #2/#20/#30.

### #6 DEFORM TO A POINT YOU CAN SOLVE — succeeded

The predecessor's non-C4 chain sink-SCC family used one uniform external radius `H=57/20` around every gadget vertex and then bounded the union of those four disks by the `H`-parallel body of a large containing rectangle. That guard coefficient was

`Q_old = 147939/2800 = 52.835357142857...`.

Instead of subdividing the entire atlas more finely, deform only a positive-measure central subfamily and solve its guard geometry explicitly with unequal radii. Keep the predecessor certificate unchanged on the complement. This yields a strict replacement gain on a fixed positive-measure part of the old family.

### #21 ASK WHO ELSE HAS THIS SHAPE — literature comparison, no theorem imported

I checked adjacent continuum nearest-neighbor stochastic-geometry work: Poisson `k`-nearest-neighbor component asymptotics and recent nearest-neighbor embracing-graph limit theory use local finite components, stabilization and void regions as natural geometric objects. These are useful analogies for the capsule/guard viewpoint, but their hypotheses and functionals do not directly prove an NUV-length correction. No constant or theorem from that literature is counted as mathematical movement here. The source-valid proof below remains an explicit finite-binomial calculation.

### #29 ADD THE POINTS AT INFINITY — succeeded

The scale variable is not truncated numerically. For each fixed cutoff `M` the argument is proved in the exact `n`-point binomial model; then `n -> infinity`, and only afterward `M -> infinity`. The resulting integral is taken over the full scale half-line `s in (0,infinity)` and evaluated exactly. Thus the compactified tail is part of the theorem, not a plot or simulation.

## 4. Predecessor chain family and the central subfamily

Use the predecessor's normalized ordered quadruple

`p1=(0,0), p2=(1,0)`,

`p3=(x3,y3)`, with `71/40 <= x3 <= 89/40`, `-1/2 <= y3 <= 1/2`,

`p4=(x4,y4)`, with `111/40 <= x4 <= 129/40`, `-1/2 <= y4 <= 1/2`.

Throughout this box the predecessor exact interval proof gives the same strongly connected non-C4 directed two-nearest-neighbor topology. The full normalized shape volume is

`V_total = 81/400`.

Restrict to the central positive-measure subfamily

`|y3| <= a, |y4| <= a`, where `a=36/125`.

Its fraction of the old shape box is

`f = (2a)^2 = 5184/15625`,

and its absolute normalized volume is

`V_cap = V_total f = 26244/390625`.

The predecessor interval bounds permit sharper vertex-wise second-neighbor radii on this same topology:

`U1=U4=229/100`, `U2=133/100`, `U3=177/100`.

The exact squared slacks are

`U1^2 - 8321/1600 = 1739/40000 > 0`,

`U2^2 - 2801/1600 = 731/40000 > 0`,

`U3^2 - 1241/400 = 19/625 > 0`.

## 5. Vertex-wise guards and capsule containment

Choose a common desired path-boundary surplus

`delta = 1/2`

and guard radii

`R1=R4=279/100`, `R2=183/100`, `R3=227/100`.

Thus `Ri-Ui=1/2` for each vertex. Requiring no external source point inside the union of the four physical disks `B(p_i,R_i s)` forces all global `D_2` outgoing arcs to remain within the quadruple, because every internal second-neighbor radius is `< U_i s < R_i s`. Combined with the preserved strong connectivity, the four-set is a global sink SCC.

The geometric gain is that this unequal-radius guard union lies inside one capsule around the endpoint segment `S=[p1,p4]` with radius

`R=R1=279/100`.

For `p2`, the point `(1,y4/x4)` lies on `S`, so

`dist(p2,S) <= |y4|/x4 <= (36/125)/(111/40) = 96/925`.

Since

`R-R2 = 24/25`,

the exact containment slack is

`24/25 - 96/925 = 792/925 > 0`.

For `p3`, the point `(x3,(x3/x4)y4)` lies on `S`, hence

`dist(p3,S) <= |y3| + (x3/x4)|y4|`

`<= (36/125)(1+89/111) = 96/185`.

Here

`R-R3 = 13/25`,

and the exact slack is

`13/25 - 96/185 = 1/925 > 0`.

Therefore the two smaller middle disks lie inside `S+B_R`; the endpoint disks do so trivially. Hence the whole unequal-radius guard union is contained in the radius-`R` capsule of the segment `S`.

On the central shape family,

`|p1-p4|^2 <= (129/40)^2 + (36/125)^2`.

Set `D=81/25`; then the exact square slack is

`D^2 - [(129/40)^2+(36/125)^2] = 14031/1000000 > 0`.

The capsule area is at most

`2 R D + pi R^2`.

Using only `pi < 22/7`,

`Q_cap := 2*(279/100)*(81/25) + (22/7)*(279/100)^2`

`= 1489023/35000`

`= 42.543514285714... < Q_old`.

For the later exact lower bound on `Q_cap^(-7/2)`, use

`sqrt(Q_cap) < 261/40`,

whose exact squared slack is

`(261/40)^2 - Q_cap = 8991/280000 > 0`.

## 6. Hamiltonian boundary charge

Use the already-proved sink-SCC boundary lemma from the predecessor: every proper sink SCC not containing a global Hamiltonian-path endpoint has at least two path-boundary crossings. For the NUV path each crossing incident to gadget vertex `i` has length at least `R_i s`, while its degree-two nearest-neighbor baseline contribution is at most `U_i s`.

Because every `R_i-U_i=delta=1/2`, each of the two crossings contributes at least `delta s` to the `2L` surplus. Thus the component contributes at least

`2 delta s`

to the `2L` surplus, equivalently

`delta s = s/2`

to the `L`-side surplus.

At most two sink SCCs can contain the two global Hamiltonian-path endpoints; their deletion is negligible after normalization under any fixed scale cutoff.

## 7. Exact-binomial transfer and full scale integral

Work in Aldous's exact area-`n` source scaling: `n` iid uniform points in a square of area `n`. For fixed `M`, restrict scale to `s<=M` and anchors to an interior region containing every required finite guard. The excluded boundary area is `O(sqrt(n))`, hence is `o(n)` after normalization for fixed `M`.

For an ordered quadruple the relative-coordinate Jacobian remains `s^5 ds dtheta d(shape)`. The exact binomial factor is `(n)_4/n^4`. Conditional on the four selected points, the probability that the other `n-4` points avoid a guard of area `A` is

`(1-A/n)^(n-4)`.

On the central family `A <= Q_cap s^2`, so for fixed shape and scale the limiting avoidance factor is bounded below by `exp(-Q_cap s^2)`. Divide ordered quadruples by `4!`; multiple accepted orderings only make this a lower count. After `n->infinity`, let `M->infinity` by monotone convergence.

The central-family correction is therefore

`Delta_cap_new >= (1/4!)*(2*pi)*V_cap*(1/2) * integral_0^infinity s^6 exp(-Q_cap s^2) ds`.

Since

`integral_0^infinity s^6 exp(-Q s^2) ds = 15 sqrt(pi)/(16 Q^(7/2))`,

this becomes

`Delta_cap_new >= (5*pi^(3/2)/64)*V_cap*(1/2)*Q_cap^(-7/2)`.

Use the rational one-sided bounds

`pi^(3/2) > 3*(17/10) = 51/10`,

`sqrt(Q_cap) < 261/40`.

The exact certificate gives

`Delta_cap_new >= 1166200000 / 43777749624439689`

`= 2.6639103425931893882260909508618066...e-8`.

## 8. Replacement accounting — no double counting

This central family is **not added on top of** the predecessor's full chain term. Decompose the predecessor chain integral into the central shape subfamily plus its complement. Keep the predecessor bound unchanged on the complement, remove the predecessor's old central share, and insert the stronger capsule certificate on that same central share.

Because the predecessor correction is linear in shape volume, its old central share is exactly

`Delta_cap_old = Delta_chain_old * f`

`= (3673530000/87180364995004919)*(5184/15625)`

`= 30469727232 / 2179509124875122975`

`= 1.3980087022460065027993824573688082...e-8`.

Therefore the strict net gain is

`NET = Delta_cap_new - Delta_cap_old`

`= 1207847451541900648780089152 / 95414004772964790053367229345754775`

`= 1.2659016403471828854267084934929984...e-8`.

All older topology-disjoint triple/C4/five-set charges are left exactly as in the predecessor. This replacement changes only the certificate on a subset of the already-counted non-C4 chain family, so there is no duplicate component charge.

## 9. Exact self-check artifacts

The mathematical route was written before checker code:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T19-56-30Z__p0257_capsule_guard_idea.md`

creation commit `2e2bfa76fbd3676479bc8268bee5da989ced1a31`.

Exact-arithmetic checker:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T19-57-30Z__p0257_capsule_guard_exact.py`

creation commit `e0ec6d9b871cb6afdc5547c5c788e858ab5c02f1`.

Archived executed output:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T19-57-30Z__p0257_capsule_guard_exact.out`

creation commit `2db330a0fd6b052a6629fdcb10f30da1d1c5db1e`.

The execution verifies every rational slack above, `Q_cap<Q_old`, the old central share, the stronger new central correction, `NET>1e-8`, the exact endpoint, `B_NEW_GT_0.62925803 = True`, and terminates

`ALL_EXACT_FINITE_CHECKS_PASS`.

This is a **self-check**, not an independent audit.

## 10. Current literature/status check — 2026-09-19

Fresh bounded checks used the exact title, `nearest unvisited vertex walk`, Aldous's current research/open-problem page, and adjacent `k`-nearest-neighbor / Poisson-component terminology.

- Aldous's published paper still states in its abstract that establishing sharper results is challenging.
- Aldous's currently crawled Berkeley page still lists the NUV problem and explicitly says the challenge is to improve beyond order-of-magnitude for random-graph models.
- Falgas-Ravry's `k`-nearest-neighbor random geometric graph work gives Poisson component asymptotics below connectivity threshold, and a 2025 nearest-neighbor embracing-graph paper develops stabilizing Poisson geometric functionals. These are adjacent local-component theories, not resolutions of Aldous's Euclidean NUV first-order constant.

The bounded search did not surface a checked later primary source resolving the exact Euclidean first-order constant. This is **bounded negative evidence only**, not proof of worldwide openness, novelty, or priority.

## 11. Status, counters and next route

P0257 remains **PARTIAL / SOURCE OPEN**. The source's existence/identification question for the first-order NUV constant is not closed.

Because the frozen metric moved this run:

- `unchanged_runs: 0 -> 0`;
- HARD stuck recoveries: `0/2 -> 0/2`;
- no stuck-recovery episode is triggered;
- P26 audit: **NOT REQUESTED / NOT PRESUMED**;
- NM13-12 secondary audit: **NOT REQUESTED / NOT PRESUMED**.

The next Section-B triple is **#3 / #15 / #25**. The intended route is no longer to tighten this capsule constant. Instead: prove a stronger topology-level boundary theorem for several directed `D_2` sink types at once (#3), deliberately break the near-collinear symmetry to seek a much larger positive-measure component family (#15), and derive a mass-transport/double-counting identity that counts sink-component boundary surplus without a coordinate-box atlas (#25). If that route does not move `b_NUV`, abandon it rather than producing another certificate for the same endpoint.

## 12. Model / scheduler-control truth

The prompt requests `Model: GPT-6. Reasoning: maximum`, but this invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is unavailable, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 maximum, a binding maximum-reasoning setting, a guaranteed hour-long execution, or a support escalation.

The exposed scheduled-task control surface still provides title/prompt, schedule/start configuration, timing mode, enabled state and ordinary update operations, but exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated per-run applied-model/applied-effort receipt**. Making GPT-6/maximum binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists those inference controls and returns trustworthy run attestation.

The historical P26 `You cannot modify this task` response remains an authorization-context boundary, not permission to bypass controls. The compliant routes are the same task's owning or otherwise authorized context, supported ownership/permission transfer where available, or authorized platform support. Task duplication, identity substitution or permission bypass is not a workaround.

This invocation made **no scheduler/task update**, no permission change, no workflow execution, no shared-root edit, no peer-file edit, no email/Gmail or Drive action, no public posting, and no paid-compute request.

```yaml
ledger_delta:
  worker: NM13-11
  namespace: proofnet24/NM13-11/
  category: HARD_OUTSIDE
  source_id: P0257
  claim_id: P0257
  canonical_key: law_of_large_numbers_and_constants_for_nuv_lengths
  shard_residue_mod_13: 10
  status_before: PARTIAL_SOURCE_OPEN
  status_after: PARTIAL_SOURCE_OPEN
  predecessor_report: proofnet24/NM13-11/runs/2026-09-19/2026-09-19T19-00-00Z__p0257-nonc4-chain-sink-movement.md
  predecessor_creation_commit: 3f2171449edf3c93155079ab659a87908a73f0b7
  frozen_prewrite_master: 527aa6c296f809a51e3be7b3bfb78e2b5193378c
  metric_name: b_NUV
  metric_definition: explicit certified endpoint in liminf E[L_n]/n >= b_NUV
  metric_before_decimal: 0.62925801789372526267217987110237913641578561212661126751467997140556
  metric_after_decimal: 0.62925803055274166614400872536946407134576963775759390287615784963581
  movement: true
  net_movement_exact: 1207847451541900648780089152/95414004772964790053367229345754775
  methods_tried: [6, 21, 29]
  method_outcomes:
    6: SUCCESS_positive_measure_vertexwise_capsule_guard
    21: ADJACENT_LITERATURE_FOUND_NO_DIRECT_TRANSFER
    29: SUCCESS_full_scale_tail_integrated_source_validly
  unchanged_runs_before: 0
  unchanged_runs_after: 0
  hard_recoveries_before: 0/2
  hard_recoveries_after: 0/2
  audit_p26: NOT_REQUESTED_NOT_PRESUMED
  audit_nm13_12: NOT_REQUESTED_NOT_PRESUMED
  idea_commit: 2e2bfa76fbd3676479bc8268bee5da989ced1a31
  checker_commit: e0ec6d9b871cb6afdc5547c5c788e858ab5c02f1
  checker_output_commit: 2db330a0fd6b052a6629fdcb10f30da1d1c5db1e
  checker_result: ALL_EXACT_FINITE_CHECKS_PASS_SELF_CHECK_ONLY
  literature_check_date: 2026-09-19
  literature_scope: exact source title; Aldous current NUV page; k-nearest-neighbor Poisson components; 2025 nearest-neighbor embracing graph
  literature_verdict: no checked later primary resolution surfaced in bounded search; not worldwide-openness evidence
  next_methods: [3, 15, 25]
  next_step: topology-level multi-sink boundary theorem plus asymmetric positive-measure family and double-counting identity; no further capsule constant polishing
```
