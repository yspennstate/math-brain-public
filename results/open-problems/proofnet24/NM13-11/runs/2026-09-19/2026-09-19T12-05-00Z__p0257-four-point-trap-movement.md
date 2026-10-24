Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MATHEMATICAL MOVEMENT: `b_NUV >= 0.629257883497108354994717... -> b_NUV >= 0.629257883497476201490891... > 0.629257883497476`; actual Section-B methods tried: #1, #9, #27.**

# NM13-11 run 2026-09-19T12:05:00Z — P0257 four-point directed-trap movement

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-11` / `proofnet24/NM13-11/`  
Category: **HARD OUTSIDE**  
Canonical source / claim: **P0257** / `operations/claims/P0257.md`  
Canonical dedup key: `law_of_large_numbers_and_constants_for_nuv_lengths`  
Exclusive shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 10`  
Source status: **OPEN**  
Track status after this run: **PARTIAL**  
Secondary audit partner after a completed claim: **NM13-12**, in addition to P26; neither audit is presumed to pass.

## 1. Authoritative continuity and ownership

This invocation continues the already-admitted exact Euclidean source model from David J. Aldous, *The Nearest Unvisited Vertex Walk on Random Graphs* (arXiv:1912.13175; *Probability in the Engineering and Informational Sciences* 36 (2022), 851–867). For `n` iid uniform points in the area-`n` square, the NUV walk repeatedly moves to the nearest unvisited point, and `L_n` denotes its total Euclidean length.

The frozen NM13-11 metric remains exactly

`b_NUV = explicit certified B such that liminf_{n->infinity} E[L_n]/n >= B`.

No metric change or source narrowing is made here.

The controlling predecessor is

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T11-06-30Z__p0257-adaptive-sector-tail-movement.md`

at commit `7d59ed1d8b3a46c7954d300191d384795c6e9816`. Its exact endpoint was

`B_prev = 4916077214821159023396228863546259379089219326781 / 7812500000000000000000000000000000000000000000000`

`       = 0.629257883497108354994717...`.

I freshly reread `operations/claims/P0257.md`; it still records exclusive owner `proofnet24/NM13-11/`, the same canonical key/hash/residue, and no release, handoff, retirement, or alias collision. The current source ledger row in `probability_campaign_2026_09/codex_20h_20260906/problems.jsonl` still records P0257 as admitted / source-says-open / `attempted_unsolved`; the current attempt ledger row `P0257-A001` still records only the old nearest-neighbor lower-bound calculation and explicitly leaves convergence/stabilization open.

Before substantive work I also reread or reconciled the required control/state surfaces: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the current Codex P0257 problem/attempt rows; the newest neighboring NM13-10 and NM13-12 reports; and the current P0257 claim.

The exact predecessor-report commit to frozen prewrite head `47b83817bbd8e886ba0a7d86f23f595034ee8dda` comparison was `ahead`, **106 commits ahead and 0 behind**. It contains no mutation of `operations/claims/P0257.md`; no P0257 release/handoff/retirement was found. The two own-namespace artifact commits made in this invocation before the report are included in that prewrite head. Missing or disabled scheduler state was not treated as ownership release.

## 2. Current-source and literature check, dated 2026-09-19 UTC

Fresh bounded web searches used the exact title and combinations of `Nearest unvisited vertex walk`, `Euclidean limit constant`, `nearest neighbor graph closed cluster`, and `Kneser-Poulsen disks union`.

- Cambridge still lists Aldous's article in volume 36 (2022), pp. 851–867; its abstract says sharper results remain challenging.
- Aldous's currently crawled Berkeley research page still lists improving NUV results beyond order of magnitude as a challenge.
- The exact-title/current searches did not surface a checked later primary source proving the Euclidean first-order limit or identifying its constant.
- Search around closed nearest-neighbor components found adjacent stochastic/geometric-graph literature, but no checked source establishing the exact NUV four-point additive inequality proved below.
- Bezdek–Connelly remains prior art for the planar Kneser–Poulsen theorem used by earlier P0257 runs; the present four-point block proof does **not** need Kneser–Poulsen.

This is bounded negative evidence only. It does **not** certify worldwide openness, novelty, or priority.

## 3. The new route — a closed 3-nearest-neighbor component

The preceding successful route extracted a bonus from every closed **two**-nearest triple. This run deliberately changed category (#1): treat the NUV rule as dynamics on the directed rank-nearest-neighbor graph and look for a finite component that is closed under the first **three** neighbor ranks.

Call a four-set `Q` a **closed 3-nearest quadruple** if for every `v in Q`, its three nearest points in the entire configuration are exactly `Q\{v}`.

### Lemma 3.1 — universal four-point trap

If NUV first enters a closed 3-nearest quadruple `Q`, then it consumes all four vertices consecutively, independent of which member is entered first and independent of the internal tie-free order.

Proof. At first entry all four members are unvisited. From the first vertex, all three other members are closer than every external point, so NUV chooses a member of `Q`. At the second member, the two still-unvisited members of `Q` remain closer than every external point; at the third, the final unvisited member of `Q` remains closer than every external point. Thus the fourth member is reached before the walk can leave `Q`. This proves the statement for **every** possible first-entry vertex/order, which is the run's genuine method #27 quantifier swap rather than an entry-state-specific construction. `□`

Let `z` be the last member of `Q` visited. If `z` is not the global terminal vertex of the NUV path, its outgoing edge has length at least `r_4(z)`, while its incoming edge has length at least `r_1(z)`. Relative to the generic Hamiltonian-path charge `r_1(z)+r_2(z)` in the deterministic inequality for `2L`, the local gain is at least

`r_4(z)-r_2(z)`.

The issue is to produce a positive density of such quadruples that is provably disjoint from the closed-triple bonuses already present in `B_prev`.

## 4. Exact guarded-square gadget

Tile the area-`n` source square by disjoint square blocks of side

`S = 15/8`,     `A = S^2 = 225/64`.

Inside each block put four labeled target squares, centered relative to the block center at

`(+/- c, +/- c)`,     `c = 21/100`,

with half-width

`h = 111/3200`.

Each target square therefore has exact area

`a_0 = (2h)^2 = 12321/2560000`.

Call a block **successful** when exactly one sample point lies in each of the four target squares and no other sample point lies anywhere else in that block.

### 4.1 Geometry: every successful block is a closed 3-nearest quadruple

The smallest possible distance from any target-square point to the complement of its block is

`R = S/2-(c+h) = 2217/3200`.

For a point in one target square and points in the two adjacent target squares, the squared distance is at most

`U_adj^2 = [2(c+h)]^2 + (2h)^2 = 62541/256000 < 1/4`.

Thus every gadget vertex has at least two gadget neighbors at distance `<1/2`, so

`r_2 < 1/2`.                                                   (4.1)

For opposite target squares, the maximum squared distance is

`D_diag,max^2 = 2[2(c+h)]^2 = 613089/1280000 < R^2`.

Hence **all three** other gadget points are strictly closer than every point outside the block. Because success forbids every other point inside the block, the gadget is a closed 3-nearest quadruple.

### 4.2 No gadget vertex belongs to any closed two-nearest triple

This is the load-bearing non-double-counting check.

The minimum squared distance between opposite target squares is

`D_diag,min^2 = 2[2(c-h)]^2 = 314721/1280000`,

and exact arithmetic gives

`U_adj^2 < D_diag,min^2`.                                    (4.2)

Any three of the four gadget cells contain a diagonal pair. At either endpoint of that selected diagonal, the omitted fourth gadget point is adjacent and is therefore strictly closer than the selected diagonal partner. So no three gadget points form a closed two-nearest triple.

A closed triple containing a gadget vertex and an external point is also impossible: all three other gadget points are closer to that gadget vertex than every external point, so an external point cannot be among its two nearest neighbors.

Therefore **no gadget vertex occurs in any closed two-nearest triple at all**. The new local bonus can be added to the already-certified closed-triple term without double counting a charged vertex.

### 4.3 Deterministic additive bonus

For the last gadget vertex `z`, (4.1) and the guard give

`r_4(z)-r_2(z) > 2217/3200 - 1/2 = 617/3200`.                (4.3)

Let `G_n` be the number of successful blocks. Distinct blocks have disjoint vertex sets. At most one successful gadget can contain the global terminal NUV vertex, so the predecessor deterministic inequality strengthens by

`(617/3200)(G_n-1)`

on the `2L_n` side. The `-1` is an `O(1)` terminal correction and vanishes after division by `n`.

This proves a source-valid additive improvement provided `E G_n/n` has a positive explicit lower limit.

## 5. Method #9 — exact randomized block density and finite-to-infinite transfer

Let

`M_n = floor(sqrt(n)/S)^2`.

Then `M_n/n -> 1/A`. For one fixed block, the exact binomial source-model probability of success is

`p_n = (n)_4 (a_0/n)^4 (1-A/n)^(n-4)`,                     (5.1)

because the four cells are labeled, one distinct sample point is assigned to each cell, and all remaining points must lie outside the whole block.

No independence between block events is required: by linearity,

`E G_n = M_n p_n`.

Therefore

`lim E G_n/n = a_0^4 exp(-A)/A`.                            (5.2)

For a fully explicit rational lower bound, use the elementary inequality `1-x < exp(-x)` for `0<x<1` with

`x=A/64=225/4096`.

Then

`(3871/4096)^64 < exp(-A)`.

The executed exact-arithmetic checker proves

`(3871/4096)^64 > 1/40`,

so

`exp(-A) > 1/40`.                                          (5.3)

Combining (4.3), (5.2), and (5.3), and remembering the factor `1/2` between the incident-edge inequality and `L_n`, gives the rigorous new source-model correction

`Delta b > (617/6400) * a_0^4/(40A)`

`        = 1579888671017488353 / 4294967296000000000000000000000`

`        = 3.6784649617445849650539457798004150390625e-13`. (5.4)

This is small but is a genuinely new route and a strictly positive certified movement, not numerical polishing of the three-disk envelope.

## 6. New certified endpoint

Adding (5.4) to the predecessor exact certificate gives

`B_new = 2517031533989904805963567012121706380405600461327497 /`
`        4000000000000000000000000000000000000000000000000000`

`      = 0.62925788349747620149089175303042659510140011533187425...`

and in particular

`B_new > 0.629257883497476 > B_prev`.

Hence

`liminf_{n->infinity} E[L_n]/n >= B_new`.                  (6.1)

This is **mathematical movement of the frozen metric**. It does not prove existence of Aldous's proposed limit and does not identify `c`; P0257 remains PARTIAL / source OPEN.

## 7. Exact checker and archived execution

The finite geometry, rational exponential seed comparison, correction arithmetic, and endpoint comparison were checked with exact Python `Fraction` arithmetic. No simulation or floating-point assertion is used.

Checker:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T11-58-30Z__p0257_four_point_trap_exact.py`

created at commit `9e41634ba2c0bf5368d90910f00dbf4ecff72848`.

Archived executed output:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T11-58-30Z__p0257_four_point_trap_exact.out`

created at commit `47b83817bbd8e886ba0a7d86f23f595034ee8dda`.

The output certifies

- `ADJ_LT_HALF = True`;
- `ADJ_LT_DIAG = True`;
- `DIAG_LT_GUARD = True`;
- `FINITE_EXP_LOWER_SEED_GT_1_OVER_40 = True`;
- exact `delta_b_lower_exact` as in (5.4);
- exact `new_cert_exact` as above;
- `NEW_CERT_GT_PREVIOUS = True`;
- `NEW_CERT_GT_0.629257883497476 = True`;
- terminal line **`ALL_EXACT_FINITE_CHECKS_PASS`**.

This is a self-check, not an independent audit.

## 8. Section-B methods actually tried

### #1 CHANGE THE CATEGORY — SUCCESS

I recast the greedy NUV ordering as a directed rank-nearest-neighbor trapping problem. A closed 3-nearest component of size four gives a forced consecutive excursion and a fourth-neighbor exit bonus. This supplied a new additive term not present in the closed-triple analysis.

### #9 RANDOMIZE — SUCCESS

Rather than optimize an arbitrary four-point configuration, I embedded a robust four-cell square motif into deterministic disjoint blocks of the random source sample. The exact multinomial event has a positive asymptotic density with an explicit rational lower bound, giving a rigorous finite-to-infinite transfer.

### #27 SWAP THE QUANTIFIERS — SUCCESS

The route was required to work **for every possible first entry and every possible tie-free internal NUV order**, rather than choosing a favorable entry state after seeing the configuration. Closed 3-nearestness makes the four-point trap uniform over those quantifiers.

## 9. Stagnation, audit state, and next route

Tracked metric before:

`b_NUV >= 0.629257883497108354994717...`.

Tracked metric after:

`b_NUV >= 0.629257883497476201490891...`.

Because the tracked quantity moved, `unchanged_runs` remains **0**. HARD stuck recoveries remain **0/2**. No stuck-recovery episode occurred.

P26 audit: **NOT_REQUESTED / NOT_PRESUMED**.  
NM13-12 audit: **NOT_REQUESTED / NOT_PRESUMED**.

The next genuinely different triple is **#7 / #19 / #28**: take the full Poisson/Palm limit for closed 3-nearest quadruples (#7), turn robust four-point shape certification into an algorithmic finite cell atlas with disjoint vertex charging (#19), and replace the present tiny worst-case square cell by a positive-measure typical shape family (#28). The objective is a materially larger four-point correction. Merely shrinking cells, refining decimals, or rerunning this same fixed gadget is not an acceptable next route.

## 10. Model/scheduler-control truth

The prompt requests GPT-6 with maximum reasoning, but this invocation actually identifies as **GPT-5.6 Sol** and exposes no authenticated reasoning-effort telemetry; reasoning level is therefore **UNVERIFIED**.

The exposed scheduled-task control surface still offers prompt/title, schedule or relative-start data, timing mode, enabled state, and ordinary list/update operations. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated applied-model/applied-effort receipt**. GPT-6/maximum remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists those routing fields and returns run-level attestation.

The historical P26 `You cannot modify this task` result is an authorization-context boundary; current repository policy records that a later P26 update succeeded from another authorized context. The compliant workaround is the owning/authorized account, workspace, API/admin, or platform-support context for that same task, not duplication or permission bypass. No scheduler, permission, workflow, shared root, peer namespace, email/Drive resource, public surface, or paid compute was modified in this invocation.

## 11. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: NM13-11
  category: HARD_OUTSIDE
  source_id: P0257
  claim_path: operations/claims/P0257.md
  canonical_dedup_key: law_of_large_numbers_and_constants_for_nuv_lengths
  shard_mod_13: 10
  source_status: OPEN
  track_status: PARTIAL
  metric_name: b_NUV
  metric_definition: explicit B with liminf E[L_n]/n >= B in the exact Euclidean source model
  metric_before_exact: 4916077214821159023396228863546259379089219326781/7812500000000000000000000000000000000000000000000
  metric_before_decimal: 0.629257883497108354994717...
  metric_after_exact: 2517031533989904805963567012121706380405600461327497/4000000000000000000000000000000000000000000000000000
  metric_after_decimal: 0.629257883497476201490891...
  movement: true
  methods_actual:
    - 1: directed-rank-nearest-neighbor category; closed 3-nearest quadruple trap
    - 9: exact random guarded-block positive-density event
    - 27: one gadget works for every first-entry vertex/internal order
  artifact_checker: proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T11-58-30Z__p0257_four_point_trap_exact.py
  artifact_checker_commit: 9e41634ba2c0bf5368d90910f00dbf4ecff72848
  artifact_output: proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T11-58-30Z__p0257_four_point_trap_exact.out
  artifact_output_commit: 47b83817bbd8e886ba0a7d86f23f595034ee8dda
  unchanged_runs_before: 0
  unchanged_runs_after: 0
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
  hard_recovery_limit: 2
  p26_audit: NOT_REQUESTED_NOT_PRESUMED
  secondary_nm13_12_audit: NOT_REQUESTED_NOT_PRESUMED
  next_methods: [7, 19, 28]
  next_step: continuous/Palm closed-quadruple correction with an algorithmically certified positive-measure shape atlas; no fixed-gadget decimal polishing
  literature_check_date_utc: 2026-09-19
  literature_scope: exact source/title, recent NUV searches, nearest-neighbor closed-component searches; bounded negative evidence only
  prewrite_master: 47b83817bbd8e886ba0a7d86f23f595034ee8dda
  predecessor_report_commit: 7d59ed1d8b3a46c7954d300191d384795c6e9816
  predecessor_to_prewrite_ahead: 106
  predecessor_to_prewrite_behind: 0
```
