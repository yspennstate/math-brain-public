Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MATHEMATICAL MOVEMENT: `b_NUV >= 0.629257904831905249113843468172... -> b_NUV >= 0.629257975756599543934040198570... > 0.62925797`; actual Section-B methods tried: #12, #25, #28.**

# NM13-11 — P0257 sink-SCC Hamiltonian-boundary movement

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-11` / `proofnet24/NM13-11/`  
Category: **HARD OUTSIDE**  
Canonical source / claim: **P0257 / `operations/claims/P0257.md`**  
Canonical dedup key: `law_of_large_numbers_and_constants_for_nuv_lengths`  
Exclusive shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 10`  
Status after this invocation: **PARTIAL / SOURCE OPEN**

## 1. Result

This invocation continues the already-admitted source P0257, David J. Aldous, *The Nearest Unvisited Vertex Walk on Random Graphs* (arXiv:1912.13175; *Probability in the Engineering and Informational Sciences* 36 (2022), 851–867). It does not reopen intake or select a replacement source.

The frozen metric is unchanged:

`b_NUV` = the explicit certified endpoint in

`liminf_{n -> infinity} E[L_n]/n >= b_NUV`

for the exact Euclidean source model in area-`n` scaling.

Controlling predecessor:

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T17-05-00Z__p0257-palm-five-family-movement.md`

created at commit

`a8a47c5a7dc7fe5d24a55bfa4254e634c7600c30`.

Metric before:

`641377705174267468101274433764131457347844713295231130249870907152717283443310373029072200251405407093773621126563697479 / 1019260465779289339534879501998404060107472660571426304187235311834417648437500000000000000000000000000000000000000000000`

`= 0.629257904831905249113843468172313962675070990127267...`.

Metric after:

`1036840803576585538238788458409057357623753998433226173823634661443281840749793585890028594106544121959770829209188511 / 1647719764425586367726663550234487807993856583136701789232573772690085937500000000000000000000000000000000000000000000`

`= 0.6292579757565995439340401985708380554211313369994555292787087385...`

and in particular

`b_NUV > 0.62925797`.

The exact net movement is

`944571941717997011472301284909577998671875 / 13317955771393171902911839310485773138454004553648`

`= 7.092469429482019673039852409274606...e-8 > 7e-8`.

This run replaces the predecessor's four-point closed-3NN atlas term by a stronger sink-SCC Hamiltonian-boundary term. It does **not** add the new term on top of the old four-point term.

## 2. Runtime/model-control truth

The prompt requests `Model: GPT-6. Reasoning: maximum`. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, a binding maximum-effort setting, an hour-long execution, or a support escalation.

The currently exposed task-control surface offers title/prompt, schedule or relative-start data, timing mode, enabled state, listing and ordinary updates. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated per-run applied-model/applied-effort receipt**. GPT-6/maximum therefore remains prompt text only.

Making the request binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists explicit model-family and reasoning-effort fields into inference routing and returns trustworthy applied-model/applied-effort attestation for each run.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary, not evidence of universal immutability. The compliant workaround is the same task's owning or otherwise authorized product/workspace/API/admin context, supported ownership/permission repair where available, or authorized platform support. It is not duplication, identity substitution, permission bypass, or a repository-side scheduler substitute.

No scheduler, task configuration, permission, credential, workflow, email/Gmail, Drive resource, public posting, or paid-compute resource was modified in this invocation.

## 3. Authoritative continuity, ownership and race check

I freshly read or directly recovered the material required to continue the admitted target:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the controlling NM13-11 predecessor above;
- newest relevant neighboring reports, including NM13-10's 17:50Z admission screen and NM13-12's 17:57:30Z successor screen;
- current canonical `operations/claims/P0257.md`;
- repository-wide exact-ID / canonical-key searches for P0257 and its aliases; and
- the exact predecessor-commit to frozen-prewrite master comparison.

The append-only intake/source/attempt corpora are too large for an honest assertion that every historical row was newly rendered model-visible in this invocation. I make no such claim. Canonical P0257 identity and attempts were reopened through the claim/search records, and the exact complete Git comparison below has `too_large=null`; it shows no mutation of P0257's canonical claim, no screened probability-intake `problems.jsonl` mutation, no probability-attempt-ledger mutation, and no root QUEUE/POSTED/RESULTS or campaign INDEX/RANKING mutation material to P0257. Thus unchanged historical intake continuity is carried forward rather than invented.

The current claim still records:

- owner `proofnet24/NM13-11/`;
- canonical title **Law of large numbers and constants for NUV lengths**;
- canonical dedup key `law_of_large_numbers_and_constants_for_nuv_lengths`;
- SHA-256 `75bdfbc93f05ad07b271ad7a5a8046a16f0bb29d10236cbc1ebf0b8889fdf5e5`;
- shard residue 10 modulo 13;
- source status OPEN / claim ADMITTED HARD OUTSIDE.

Final prewrite head after the exact-check artifacts and final ownership reread:

`d878fb0f04b1b191b7359bb7ba4994b7ac0897a7`.

Exact comparison

`a8a47c5a7dc7fe5d24a55bfa4254e634c7600c30 .. d878fb0f04b1b191b7359bb7ba4994b7ac0897a7`

returned `ahead_by=114`, `behind_by=0`, `total_commits=114`, and `too_large=null`. The complete changed-file set contains no `operations/claims/P0257.md` mutation and no second P0257 owner. Two unrelated canonical claims were added and later VDH/P0157 lifecycle files changed; none touches this target. The two new NM13-11 artifact files in that comparison are the substantive exact checker/output for the theorem proved below.

No private-repository history known to be material to P0257 was inaccessible.

## 4. Section-B methods actually tried

All thirty menu methods have already appeared at least once in P0257's history, so this run legitimately recycles a nonconsecutive triple rather than falsely calling it unused.

### #12 FIND WHAT IS CONSERVED — SUCCESS

Replace the previous “closed component forces consecutive NUV consumption” viewpoint by the directed two-nearest-neighbor graph `D_2`: every point has arcs to its first and second nearest neighbors.

A strongly connected component with no outgoing `D_2` arc is a **sink SCC**. This is a path-independent invariant of the point configuration. Distinct sink SCCs are vertex-disjoint. A closed two-nearest triple is exactly a size-3 sink SCC; the predecessor's C5 five-point Palm family is a size-5 sink SCC. The four-point atlas below produces size-4 sink SCCs. This gives a clean disjoint charging partition by SCC size.

### #25 COUNT THE SAME THING TWICE — SUCCESS

Count the boundary edges of a sink SCC in the Hamiltonian path underlying NUV. The old four-point proof charged only a forced exit. The new argument charges **every path crossing of the SCC boundary** relative to the degree-two nearest-neighbor baseline. A proper component not containing a global path endpoint has at least two such crossings, producing a factor-of-two structural gain at the local level.

### #28 REPLACE “FOR ALL” WITH “FOR TYPICAL” — SUCCESS

Do not prove a universal statement for every four-point shape. Reuse the already certified positive-measure 1796-cell four-point atlas, now only asking that the internal two-nearest-neighbor graph be the robust cycle `C4` and that a finite guard make it a global sink SCC. Campbell–Mecke / exact binomial factorial moments then turn this positive-measure family into a source-valid asymptotic density.

## 5. The sink-SCC Hamiltonian boundary lemma

Assume a tie-free finite metric configuration; ties occur with probability zero in the source model. Let `P` be any Hamiltonian path through the points — in particular the NUV path. For a vertex `v`, let `r_1(v) <= r_2(v)` be its first and second nearest-neighbor distances.

The usual degree-two baseline is pointwise:

- if `v` is not a global path endpoint, the two incident path edges are distinct and their length sum is at least `r_1(v)+r_2(v)`;
- if `v` is a global path endpoint, its one incident edge is at least `r_1(v)`.

Summing over vertices gives the familiar `2L` baseline, with only the two endpoint `r_2` terms omitted.

Now let `S` be a sink SCC of `D_2`. Suppose for some scale `s>0` that

`r_2(v) <= U s` for every `v in S`,

and every point outside `S` is at distance at least `H s` from every `v in S`, where `H>U`.

Write `m(v)` for the number of path edges incident to `v` that cross from `S` to its complement.

If `v` is not a global endpoint and `m(v)=1`, its incident-edge sum is at least

`H s + r_1(v)`,

so its surplus above `r_1(v)+r_2(v)` is at least

`(H-U)s`.

If `m(v)=2`, both incident edges are external, hence their sum is at least `2Hs`; since `r_1+r_2 <= 2Us`, the surplus is at least

`2(H-U)s`.

If `v` is a global path endpoint and `m(v)=1`, the endpoint baseline is only `r_1(v) <= Us`, so its surplus is again at least

`(H-U)s`.

Therefore, summing over `v in S`, the `2L`-side surplus contributed by `S` is at least

`cross_P(S) (H-U)s`,

where `cross_P(S)` is the number of Hamiltonian-path edges crossing the cut `(S,S^c)`.

A proper nonempty subset of a Hamiltonian path that contains no global path endpoint has at least two boundary crossings. Hence every sink SCC containing neither endpoint contributes at least

`2(H-U)s`

on the `2L` side, i.e. at least

`(H-U)s`

on the `L` side.

There are at most two sink SCCs containing global path endpoints because sink SCCs are disjoint. With a fixed scale cutoff `s<=M`, discarding all contributions from endpoint-containing SCCs loses at most `O(M)` total length; after division by `n` this vanishes. Thus endpoint exceptions do not affect the asymptotic lower endpoint.

Crucially, this lemma does **not** require NUV to stay inside `S` after entry. It is a Hamiltonian-path boundary statement and is therefore stronger than the earlier trap-only mechanism.

## 6. Exact four-point typical family

Reuse the predecessor's exact normalized coordinates

`p1=(0,0), p2=(1,0), p3=(a,b), p4=(c,d)`

with 0.1-grid cells

`a in [-1/2,1/2]`,

`b,c,d in [2/5,8/5]`.

There are exactly

`10*12^3 = 17280`

cells. A cell is accepted when the matching edges `p1-p4` and `p2-p3` are uniformly longer than all four complementary cycle edges. Then at each vertex the two nearest **internal** neighbors are its two cycle neighbors, so the internal directed 2NN graph is the bidirected cycle `C4`, hence strongly connected.

The new exact checker re-enumerates all 17280 cells from scratch and certifies:

`accepted_cells = 1796`,

`V_4 = 1796*(1/10)^4 = 449/2500`,

`min(diagonal^2 - side^2) = 1/100`,

`max internal second-neighbor distance^2 = 401/100`,

`max shape diameter^2 = 128/25`.

Choose exact rational envelopes

`Ubar = 801/400`,

`Dbar = 2263/1000`.

Then

`Ubar^2 > 401/100`,

`Dbar^2 > 128/25`.

Take the external guard radius

`H=5/2`.

The rank gap used by the boundary lemma is therefore

`delta = H-Ubar = 199/400`.

If the union of the four radius-`Hs` disks around the selected vertices contains no external point, every selected vertex has its two global nearest neighbors inside the C4. Thus the selected four-set is a global size-4 sink SCC of `D_2`.

Although this particular rational `H` also exceeds the certified shape diameter, the proof no longer uses closed-3NN consecutive-consumption. Its gain comes from counting the two Hamiltonian boundary crossings, which is why the old four-point term is strictly improved.

## 7. Deterministic guard-area bound

Let `K` be the convex hull of an accepted normalized quadruple and let `D=diam(K)`. The union of the four radius-`H s` guard disks is contained in the parallel body

`K + B_{Hs}`.

For a planar convex body, Steiner's formula gives

`|K+B_{Hs}| = A(K) + Hs P(K) + pi H^2 s^2`.

The predecessor already recorded the exact small-quadrilateral prior art: for diameter `D`, the maximal perimeter is `2+sqrt(6)-sqrt(2)` times `D`; the historical small-polygon literature includes Griffiths–Culpin, *Pi-optimal polygons*, Math. Gaz. 59 (1975), 165–175. For exact rational certification it suffices that

`P(K) < (61/20)D`.

Also `A(K) <= D^2/2`, and `pi < 22/7`. Using the exact atlas bound `D^2 <= 128/25` and the rational `Dbar`,

`|K+B_{Hs}| <= Q s^2`,

where

`Q = (128/25)/2 + (61/20)*(5/2)*(2263/1000) + (22/7)*(5/2)^2`

`= 2209661/56000`.

For the `Q^(7/2)` denominator, the checker certifies

`3926/625 > sqrt(Q)`.

All inequalities are one-sided in the direction needed for a lower bound on the void probability.

## 8. Campbell–Mecke / exact-binomial density calculation

Parameterize an ordered accepted quadruple by an anchor `x`, scale `s`, rotation `theta`, and normalized shape `(a,b,c,d)`. The six-dimensional relative-coordinate Jacobian is

`s^5 ds dtheta da db dc dd`.

For a successful shape the L-side boundary bonus is at least `delta*s`. The empty-guard probability in the unit-intensity Poisson limit is at least `exp(-Q s^2)`.

The ordered-to-unordered division by `4!` is safe even when one physical sink SCC admits several atlas labelings: an unordered four-set has at most 24 ordered labelings, while its actual Hamiltonian-boundary surplus is at least the maximum of the labelwise certified bonuses, hence at least their average after division by 24.

Therefore the asymptotic four-point correction is at least

`(1/4!)*(2*pi)*V_4*delta* integral_0^infinity s^6 exp(-Q s^2) ds`.

Since

`integral_0^infinity s^6 exp(-Q s^2) ds = 15 sqrt(pi)/(16 Q^(7/2))`,

the coefficient is

`(5 pi^(3/2)/64) V_4 delta Q^(-7/2)`.

Using only exact rational lower/upper bounds

`pi > 3`, `sqrt(pi) > 17/10`, and `sqrt(Q) < 3926/625`,

the checker obtains

`Delta_sink4 >= 1953771303750000 / 21178600162983614506103`

`= 9.22521455013273719816576885464...e-8`.

The predecessor's four-point term was

`Delta_old4 = 13411559295654296875 / 628840228764059875161752016`

`= 2.13274512065071752512591644537...e-8`.

Thus

`Delta_sink4 > Delta_old4`

and the exact replacement gain is the metric movement displayed in Section 1.

## 9. Transfer back to the exact finite source model

No Poissonization theorem, NUV stabilization theorem, or unproved existence of `lim L_n/n` is assumed.

Work directly in the source's area-`n` square containing exactly `n` iid uniform points. Fix a scale cutoff `M`. Restrict the anchor to points at distance larger than a deterministic `O(M)` margin from the square boundary, so every selected atlas quadruple and its `Hs` guard lie wholly inside the square.

For each bounded ordered quadruple configuration the exact factorial density contributes

`(n)_4/n^4`,

and, conditional on the four selected points, the probability that the other `n-4` points avoid a guard union of area `A` is exactly

`(1-A/n)^(n-4)`.

For fixed `M`, uniformly on the bounded configuration domain,

`(n)_4/n^4 -> 1`

and

`(1-A/n)^(n-4) -> exp(-A)`.

The interior anchor area divided by `n` tends to 1. Hence dominated convergence gives the truncated Campbell–Mecke integral above as the `n->infinity` lower density in the exact binomial source model.

Sink SCCs are vertex-disjoint, so their local `2L` surplus inequalities sum without vertex overcharge. Discard the at most two sink SCCs that contain a global path endpoint; with `s<=M` the discarded L-side bonus is `O(M)`, hence `o(n)` after normalization. Only after taking `n->infinity` do we let `M->infinity`; monotone convergence recovers the full positive integral.

This proves the claimed source-valid liminf improvement.

## 10. Why the new charge is disjoint from the existing corrections

A size-3 closed-two-nearest triple is a sink SCC of `D_2`: each vertex's two nearest neighbors are the other two, and the induced directed graph is strongly connected.

The new accepted four-point family is a size-4 sink SCC because its global two-nearest graph is the bidirected C4.

The predecessor's five-point Palm family has global two-nearest graph C5 and is therefore a size-5 sink SCC.

Distinct sink SCCs of one directed graph are vertex-disjoint. A sink SCC cannot properly contain another sink SCC because any arc needed to make the larger set strongly connected would leave the smaller sink set. Consequently the size-3, size-4, and size-5 charges are mutually vertex-disjoint. This is a stronger bookkeeping fact than the earlier ad hoc internal-triple / internal-quad exclusion checks.

For metric arithmetic this run **replaces only** `Delta_old4` by `Delta_sink4`. It retains the predecessor's already certified size-3 and size-5 contributions unchanged. No term is counted twice.

## 11. Exact self-check artifacts

Substantive exact checker created at commit

`9dfe033932e5fe962057bac1d1758256ca06eec0`:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T17-58-30Z__p0257_sink_scc_boundary_exact.py`

Executed locally with Python's exact `Fraction` arithmetic; archived stdout created at commit

`7c2fd9e4e14deb010d60b35242cb6f571547cab8`:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T17-58-30Z__p0257_sink_scc_boundary_exact.out`

The execution re-enumerates all 17280 atlas cells and verifies, among other lines:

- `accepted_cells = 1796`;
- `accepted_shape_volume = 449/2500`;
- `max_internal_2NN_side_squared = 401/100`;
- `Ubar_squared_gt_max_U2 = True`;
- `max_shape_diameter_squared = 128/25`;
- `Dbar_squared_gt_max_R2 = True`;
- `guard_Q = 2209661/56000`;
- `qroot_upper_squared_gt_Q = True`;
- `sink4_lower_exact = 1953771303750000/21178600162983614506103`;
- `sink4_gt_old_quad = True`;
- `metric_movement_gt_7e-8 = True`;
- `B_after_gt_0.62925797 = True`;
- terminal line `ALL_EXACT_FINITE_CHECKS_PASS`.

This is explicitly a **self-check**, not an independent P26 or NM13-12 audit.

## 12. Fresh bounded literature / source check — 2026-09-19

Original source: Aldous, *The Nearest Unvisited Vertex Walk on Random Graphs*, Cambridge / PEIS 36(3), July 2022, pp. 851–867, DOI `10.1017/S0269964821000115`. The current Cambridge abstract still says that establishing sharper results appears challenging.

Current author page: Aldous's Berkeley page, crawled on 2026-09-19, still lists *The Nearest Unvisited Vertex Walk on Random Graphs* and states the challenge as improving beyond order-of-magnitude for random-graph models.

Current exact-title / phrase searches for `nearest unvisited vertex`, NUV, Euclidean random points, first-order constant, and 2023–2026 follow-up work recovered the original paper / mirrors and adjacent nearest-neighbor literature, but no checked later primary source resolving the Euclidean first-order constant. This is **bounded negative evidence only**; it is not proof of worldwide openness, novelty, or priority.

Adjacent literature checked because this run uses `D_2` components: Victor Falgas-Ravry, *Distribution of components in the k-nearest neighbour random geometric graph for k below the connectivity threshold*, EJP 18 (2013), arXiv:1211.5918, concerns Poisson asymptotics for components in a kNN random geometric graph. It does not prove the NUV path-length bound here, and no result from it is imported into the mathematical proof. The sink-SCC Hamiltonian-boundary lemma above is proved directly on the page.

The small-quadrilateral perimeter inequality used in the guard estimate is prior art carried from the preceding diameter-guard run, not claimed as new.

## 13. Status, counters, audits and next route

Source verdict remains **OPEN**. Worker result is **PARTIAL**: one explicit rigorous lower endpoint for `liminf E[L_n]/n` has improved, but existence or identification of Aldous's proposed limit `c` is not proved.

Because the frozen metric moved in this invocation:

- substantive unchanged-run counter: `0 -> 0`;
- HARD stuck-recovery episodes consumed: `0/2 -> 0/2`;
- no Section-I stuck episode is triggered.

Required independent audits remain:

- P26: **NOT REQUESTED / NOT PRESUMED**;
- NM13-12: **NOT REQUESTED / NOT PRESUMED**.

The next research run should not numerically polish this 1796-cell certificate. The next recycled, nonconsecutive Section-B triple is **#2 / #20 / #30**:

- **#2 ATTACK THE NEGATION FIRST:** try to build a sink SCC whose two-neighbor closure gives no positive path-boundary surplus once the explicit empty guard is removed; identify the exact failure mode.
- **#20 FIND WHY THE ALGORITHM FAILS:** characterize what prevents replacing the empty-guard condition by an intrinsic D2 sink-component test with positive Palm density and no exponential guard penalty.
- **#30 LOCALIZE:** stratify sink SCCs by one scale and one boundary-rank deficit at a time, seeking a mass-transport identity over *all* typical size-4 sink components rather than a fixed atlas.

If that route does not move `b_NUV`, abandon it rather than refining the present rational constants.

## 14. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: NM13-11
  namespace: proofnet24/NM13-11/
  category: HARD_OUTSIDE
  source_id: P0257
  claim_id: P0257
  claim_path: operations/claims/P0257.md
  owner: proofnet24/NM13-11/
  canonical_dedup_key: law_of_large_numbers_and_constants_for_nuv_lengths
  canonical_sha256: 75bdfbc93f05ad07b271ad7a5a8046a16f0bb29d10236cbc1ebf0b8889fdf5e5
  shard_mod_13: 10
  source_status: OPEN
  worker_status: PARTIAL
  metric_name: b_NUV
  metric_definition: explicit_certified_endpoint_in_liminf_E_Ln_over_n
  metric_before_exact: "641377705174267468101274433764131457347844713295231130249870907152717283443310373029072200251405407093773621126563697479/1019260465779289339534879501998404060107472660571426304187235311834417648437500000000000000000000000000000000000000000000"
  metric_before_decimal: "0.629257904831905249113843468172313962675070990127267..."
  metric_after_exact: "1036840803576585538238788458409057357623753998433226173823634661443281840749793585890028594106544121959770829209188511/1647719764425586367726663550234487807993856583136701789232573772690085937500000000000000000000000000000000000000000000"
  metric_after_decimal: "0.6292579757565995439340401985708380554211313369994555..."
  movement_exact: "944571941717997011472301284909577998671875/13317955771393171902911839310485773138454004553648"
  movement_decimal: "7.092469429482019673039852409274606e-8"
  replacement_old_quad_exact: "13411559295654296875/628840228764059875161752016"
  replacement_sink4_exact: "1953771303750000/21178600162983614506103"
  section_B_methods_actual:
    - 12
    - 25
    - 28
  section_B_outcomes:
    12: "SUCCESS: directed 2NN sink SCC gives a configuration invariant and disjoint size-3/4/5 charging classes"
    25: "SUCCESS: Hamiltonian boundary crossings counted vertexwise give at least two rank-gap payments for non-endpoint components"
    28: "SUCCESS: positive-measure 1796-cell typical C4 family transfers by exact finite-binomial factorial moments"
  unchanged_runs_before: 0
  unchanged_runs_after: 0
  hard_recoveries_before: "0/2"
  hard_recoveries_after: "0/2"
  artifacts:
    checker:
      path: proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T17-58-30Z__p0257_sink_scc_boundary_exact.py
      commit: 9dfe033932e5fe962057bac1d1758256ca06eec0
    output:
      path: proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T17-58-30Z__p0257_sink_scc_boundary_exact.out
      commit: 7c2fd9e4e14deb010d60b35242cb6f571547cab8
      terminal: ALL_EXACT_FINITE_CHECKS_PASS
  audits:
    P26: NOT_REQUESTED_NOT_PRESUMED
    NM13-12: NOT_REQUESTED_NOT_PRESUMED
  next_methods:
    - 2
    - 20
    - 30
  next_step: "seek an intrinsic Palm/mass-transport count for typical size-4 D2 sink SCCs that removes the explicit empty-guard penalty; do not refine the current atlas mesh"
  frozen_prewrite_master: d878fb0f04b1b191b7359bb7ba4994b7ac0897a7
  predecessor_report_commit: a8a47c5a7dc7fe5d24a55bfa4254e634c7600c30
  prewrite_compare:
    ahead_by: 114
    behind_by: 0
    too_large: null
```

No shared root, peer namespace, canonical claim, scheduler, permission, workflow, email/Drive resource, public surface, or paid compute was edited by NM13-11 in this invocation.
