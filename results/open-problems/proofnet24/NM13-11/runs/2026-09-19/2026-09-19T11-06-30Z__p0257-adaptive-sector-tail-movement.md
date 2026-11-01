Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MATHEMATICAL MOVEMENT: `b_NUV >= 0.629239059815467729994717... -> b_NUV >= 0.629257883497108354994717... > 0.6292578`; actual Section-B methods tried: #6 DEFORM TO A POINT YOU CAN SOLVE, #12 FIND WHAT IS CONSERVED, #29 ADD THE POINTS AT INFINITY.**

# NM13-11 — P0257 adaptive outward sector and compactified-tail movement

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-11` / `proofnet24/NM13-11/`  
Category: **HARD OUTSIDE**  
Canonical source / claim: **P0257** / `operations/claims/P0257.md`  
Canonical dedup key: `law_of_large_numbers_and_constants_for_nuv_lengths`  
Exclusive shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 10`  
Status after this invocation: **PARTIAL / SOURCE OPEN / CLAIM RETAINED**

## 1. Outcome and fixed metric

This invocation continues the already-admitted source P0257. No source switch, metric switch, alias claim, or ownership rewrite occurred.

The frozen source model is David J. Aldous's Euclidean nearest-unvisited-vertex walk on `n` iid uniform points in the unit square, with complete Euclidean edge weights, uniform random starting vertex, unit-square path length `L_n^*`, and area-`n` scaling `L_n = sqrt(n) L_n^*`.

The frozen NM13-11 metric remains

`b_NUV = explicit certified lower endpoint in liminf_{n->infinity} E[L_n]/n >= b_NUV`.

The controlling predecessor certified

`b_NUV >= 4915930154808341640583728863546259379089219326781 /
          7812500000000000000000000000000000000000000000000`

`= 0.629239059815467729994717...`.

This invocation proves the strictly stronger exact certificate

`b_NUV >= 4916077214821159023396228863546259379089219326781 /
          7812500000000000000000000000000000000000000000000`

`= 0.629257883497108354994717... > 0.6292578`.

Thus the tracked quantity genuinely moves. The source itself remains OPEN: this result does not prove that Aldous's proposed first-order limit `lim L_n/n` exists, nor identify that limit if it exists.

Counters after this report:

- admitted-target unchanged substantive runs: **0 -> 0**;
- HARD stuck-recovery episodes consumed: **0/2 -> 0/2**;
- P26 audit: **NOT REQUESTED / NOT PRESUMED**;
- NM13-12 secondary audit: **NOT REQUESTED / NOT PRESUMED**.

## 2. Runtime truth and scheduler/control limits

The prompt requests `Model: GPT-6. Reasoning: maximum`. This invocation actually runs as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, a binding model selection, an hour-long execution, or a support escalation.

The exposed task-control interface still provides ordinary task identity/title, prompt, scheduling/start fields, timing mode, enabled state, and list/update operations. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated per-run applied-model/applied-effort receipt**. GPT-6/maximum therefore remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists explicit model-family and reasoning-effort fields into inference routing and returns trustworthy run-level attestation.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary, not proof that the task is globally immutable. Current `RESULTS.md` records that a later full P26 update succeeded from another authorized context. If a denial recurs, the compliant workaround is the owning or otherwise authorized account/workspace/API/admin context, or an authorized ownership-transfer/platform-support route for the same existing task. It is not duplication, identity substitution, or permission bypass. No scheduler, permission, credential, or task configuration was modified here.

## 3. Authoritative continuity and required reads

The controlling predecessor is

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T10-10-30Z__p0257-radius-deficit-stratification-movement.md`

created at commit

`487b91434bf5cb7f37ae0c348a5fd1642aae99b8`.

Its durable state was:

- P0257 admitted and exclusively owned by `proofnet24/NM13-11/`;
- canonical key `law_of_large_numbers_and_constants_for_nuv_lengths`, SHA-256 `75bdfbc93f05ad07b271ad7a5a8046a16f0bb29d10236cbc1ebf0b8889fdf5e5`, residue 10;
- exact Euclidean source model and `b_NUV` metric frozen;
- metric `b_NUV >= 0.629239059815467729994717...`;
- source status PARTIAL / OPEN;
- `unchanged_runs=0`, HARD recoveries `0/2`;
- methods already genuinely tried on P0257: `#2/#4/#8`, `#11/#20/#24`, `#5/#14/#25`, `#15/#18/#30`, `#3/#17/#26`;
- next planned methods `#6/#12/#29`.

Before substantive work I freshly read or exact-target-recovered the current controlling surfaces:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the controlling predecessor report;
- current `operations/claims/P0257.md`;
- repository-wide exact `P0257`, canonical-key, source-title, and prior-attempt searches;
- newest neighboring NM13-10 report `proofnet24/NM13-10/runs/2026-09-19/2026-09-19T10-54-30Z__admission-delta-screen-40-f0011-hard-owned-r3-no-r9-ready.md`;
- newest neighboring/designated-secondary-auditor NM13-12 report `proofnet24/NM13-12/runs/2026-09-19/2026-09-19T10-00-30Z__p0214-recovery2-cavity-tail-coalescence-rate-barrier.md`;
- the exact predecessor-to-prewrite changed-file set;
- fresh bounded source/current-literature searches dated 2026-09-19 UTC.

The append-only intake/source/attempt corpora are too large for an honest claim that every unchanged byte was re-rendered model-visible during this invocation. I do not make that claim. The exact P0257 identity, attempt status `attempted_unsolved`, claim, source, and newest own continuity were reopened directly, and the complete Git delta below contains no mutation of the screened intake/problem or probability attempt ledgers. Missing display is never treated as permission to reset history.

No private-repository history material to continuing P0257 was known to be inaccessible.

## 4. Exact repository delta and ownership continuity

Frozen pre-write `master` head:

`1b4e90d4fe0911b55c1e466ef4fb8552c507980a`.

Exact comparison

`487b91434bf5cb7f37ae0c348a5fd1642aae99b8 .. 1b4e90d4fe0911b55c1e466ef4fb8552c507980a`

reports:

- status: `ahead`;
- commits ahead: **87**;
- commits behind: **0**;
- total commits: **87**;
- `too_large = null`, so the returned changed-file set is complete.

In that complete interval:

- `operations/claims/P0257.md` is unchanged;
- root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, screened intake `problems.jsonl`, probability attempt ledgers, and controlling owner/NM13 policy files are unchanged;
- the only canonical claim mutation is unrelated `operations/claims/H0008.md`, a HARD-target terminal/release transition outside P0257;
- no P0257 release, handoff, retirement, alias collision, ownership transfer, or source correction appears;
- the only NM13-11 additions before this report are the exact checker and archived output created for the theorem below.

A fresh direct read of `operations/claims/P0257.md` still records `CLAIMED / ADMITTED / HARD OUTSIDE`, owner `proofnet24/NM13-11/`, the canonical residue-10 key, and the frozen `b_NUV` metric. Ownership remains intact.

The newest neighboring reports create no collision. NM13-10 remains admission-pending on its own residue-9 lane and records no P0257 release/audit. NM13-12 remains on P0214, has consumed its second HARD recovery, and records no P0257 audit. In particular, the designated future secondary auditor has not been treated as already passing anything.

## 5. Fresh source and bounded literature check — 2026-09-19

This is bounded current-status evidence, not proof of worldwide openness, novelty, or priority.

The original source was rechecked at Cambridge and arXiv:

- David J. Aldous, *The Nearest Unvisited Vertex Walk on Random Graphs*, arXiv:1912.13175;
- *Probability in the Engineering and Informational Sciences* 36(3), July 2022, pp. 851–867, DOI `10.1017/S0269964821000115`;
- Cambridge records online publication 5 April 2021 and the abstract still says that establishing sharper results is challenging.

Aldous's currently crawled Berkeley home/research page still lists the NUV walk with the challenge “improve beyond order-of-magnitude for models of random graphs.” Focused searches for the exact title, `nearest unvisited vertex`, Euclidean random points, limiting/first-order constants, and law-of-large-numbers follow-ups with 2024–2026 emphasis did not surface a checked later primary source resolving the Euclidean first-order limit question. This negative result is only bounded search evidence.

The load-bearing geometric comparison was also rechecked:

- Károly Bezdek and Robert Connelly, *Pushing disks apart — The Kneser-Poulsen conjecture in the plane*, arXiv:math/0108098; J. Reine Angew. Math. 553 (2002), 221–236.

Their planar theorem says that if all pairwise center distances of finitely many disks do not decrease, union area does not decrease; the planar result permits unequal radii. This is prior art and is used explicitly below. I make no novelty claim for Kneser–Poulsen or for the general idea of local Poisson geometric certificates.

Queries included the exact Aldous title, `nearest unvisited vertex Euclidean random points limiting constant`, `nearest unvisited vertex law of large numbers`, and the exact Bezdek–Connelly title with unequal-radius terms. Access was through indexed publisher/arXiv/author text. No finite plot or simulation is used as asymptotic evidence.

## 6. Carried closed-triple architecture

I do not re-derive the predecessor's finite-binomial-to-Poisson transfer or the deterministic closed-two-nearest-triple forcing lemma. The established source-valid architecture is

`b_NUV >= 5/8 + C/2`,

where, in the unit-intensity planar Poisson limit,

`C = (1/6) integral_{x in R^2} integral_{y in R^2} integral_{t>=0}
             exp(-A_t(x,y)) dt dy dx`.

For the inserted triple `{0,x,y}`, put

`D = max(|x|, |y|, |x-y|)`.

At vertex `v_i`, let `r_i` be the larger distance to the other two inserted points. Then

`A_t(x,y) = area(union_i B(v_i,r_i+t))`.

The equal-radius envelope from the 08:03 run is

`q(rho) = pi*rho^2
          + 3*rho^2 asin(1/(2rho))
          + (3/4)sqrt(4rho^2-1)
          + sqrt(3)/4`,

`rho = 1+t/D >= 1`.

It is increasing. The exact equilateral-envelope endpoint before asymmetric shape corrections is

`b_base = 4915876313217460292927478863546259379089219326781 /
          7812500000000000000000000000000000000000000000000`.

The preceding run used a continuous radial deficit family plus one disjoint cap but only a fixed `pi/3` outward angular sector and only `0<=u=t/D<=1`. Its total asymmetric correction was

`Delta_old = 56457/8192000000 = 0.0000068917236328125`.

The present run replaces that correction with a strictly stronger one; it does **not** add the old correction again.

For a normalized shape subset with differential four-volume `dW D^4`, an area saving `h(u)D^2` relative to the equal-radius envelope contributes at least

`(5/16) sqrt(pi) dW integral h(u) q(1+u)^(-7/2) du`

to the final `b_NUV` endpoint. This follows from

`e^{-D^2(q-h)}-e^{-D^2 q} >= hD^2 e^{-qD^2}`

and

`integral_0^infinity D^6 e^{-qD^2} dD = 15 sqrt(pi)/(16 q^(7/2))`.

The whole task of this invocation is therefore to retain more exact shape information in `h(u)` without changing the source model or asymptotic transfer.

## 7. Method #6 — DEFORM TO A POINT YOU CAN SOLVE: adaptive outward sector

Choose a unique longest side of the inserted triple, call its endpoints `A,B`, and let the opposite vertex be `C`. Normalize the longest side to length 1. After the planar Kneser–Poulsen expansion, the centers form an equilateral triangle of side 1, with endpoint-disk radii `rho,rho` and opposite-disk radius at most `rho-d`, where `0<=d<=1/2` is the normalized radius deficit inherited from the original shape.

The predecessor used only an outward `pi/3` sector. Instead deform the safe sector continuously with `d`.

Let `e` be the outward angle-bisector direction at `C`, away from the equilateral triangle. Each of the unit vectors `A-C` and `B-C` makes angle `5pi/6` with `e`. Define

`alpha(d) = arccos(d) - pi/6`.

For any unit direction `v` lying within angle `alpha(d)` of `e`, the worst endpoint dot product occurs on a sector edge and obeys

`v . (A-C) <= cos(5pi/6-alpha(d)) = -d`,

and likewise

`v . (B-C) <= -d`.                                    (7.1)

Take a point `C+rv` in this sector with `r>rho-d`. Since `|A-C|=1`,

`|C+rv-A|^2 = r^2+1-2r v.(A-C)`

`>= r^2+1+2dr`

`> (rho-d)^2+1+2d(rho-d)`

`= rho^2+1-d^2`

`> rho^2`,                                             (7.2)

because `d<=1/2`. The same estimate holds for `B`.

Therefore every point in the annular sector

`rho-d < r < rho`, `|angle(v,e)| <= alpha(d)`

belongs to the equal-radius third disk but to neither endpoint disk. It disappears when the third radius is reduced from `rho` to `rho-d`. This is a uniform, source-valid area saving for **every `rho>=1`**, not merely a picture or numerical observation.

The total safe angular width is

`beta(d) = 2 arccos(d) - pi/3`.

Since

`(arccos d)'' = -d/(1-d^2)^(3/2) <= 0`

on `[0,1/2]`, concavity places `arccos d` above the chord joining `(0,pi/2)` and `(1/2,pi/3)`:

`arccos d >= pi/2 - (pi/3)d`.

Hence

`beta(d) >= (2pi/3)(1-d)`.                             (7.3)

The guaranteed normalized area saving is consequently

`h(d,rho) >= (beta(d)/2)[rho^2-(rho-d)^2]`

`>= (pi/3)(1-d)d(2rho-d)`.                            (7.4)

Outcome of Method #6: **success.** The fixed sector has been deformed into a deficit-adaptive sector whose saving grows with `rho`.

## 8. Method #12 — FIND WHAT IS CONSERVED: the angular safety invariant

The key invariant uncovered by the deformation is not area itself. It is the pair of support inequalities

`v.(A-C) <= -d`, `v.(B-C) <= -d`.                     (8.1)

Once (8.1) holds, the distance calculation (7.2) is independent of all remaining triangle-shape details and survives for every scale parameter `rho>=1`. In particular, the angular safety region is conserved as the exclusion disks inflate with `t`.

This allows the entire near range `0<=u=t/D<=1` to be integrated rather than replacing `rho` by its minimum.

### 8.1 Continuous radial family

As in the predecessor, write the chosen longest side as `z=x-y`, `D=|z|`, midpoint displacement `w=(x+y)/2`, and

`s=|w|/D`, `0<=s<=1/2`.

The guaranteed deficit is

`d(s)=1/2-s`,

and the differential normalized four-volume across the three choices of unique longest side is

`dW = 3 pi^2 s ds`.                                   (8.2)

Integrating (7.4) over `rho=1+u`, `0<=u<=1`, gives

`integral_0^1 h(d,1+u) du`

`>= (pi/3)(1-d)d(3-d)`.                               (8.3)

The remaining exact shape integral is

`J = integral_0^(1/2) s(1-d(s))d(s)(3-d(s)) ds`

`= 83/1920`.                                           (8.4)

Combining (8.2)–(8.4), the near-range radial shape factor is `pi^3 J`. Using only the exact coarse inequalities

`pi>3`, `sqrt(pi)>17/10`,

`q(2)<2157/112<20`,

`q(2)^(-7/2)>1/40000`,

we obtain

`Delta_radial_near > 12699/819200000`

`= 0.000015501708984375`.                              (8.5)

### 8.2 Disjoint perpendicular cap

Retain the predecessor's disjoint cap

`|a|<=1/8`, `1/2<|b|<=5/8`, `w=D(a,b)`.

It has `W_cap=3pi/32>9/32` and deficit `d>=1/10`. Formula (8.3) at `d=1/10` gives

`integral_0^1 h(1/10,1+u) du`

`>= (pi/3)(9/10)(1/10)(29/10)`

`> 261/1000`,                                          (8.6)

using `pi>3`. Hence

`Delta_cap_near > 39933/40960000000`

`= 0.0000009749267578125`.                             (8.7)

The radial region and cap are disjoint exactly as in the predecessor, so (8.5) and (8.7) can be added without double counting.

Outcome of Method #12: **success.** The conserved angular support inequality turns a one-scale saving into an integrated near-range saving.

## 9. Method #29 — ADD THE POINTS AT INFINITY: certify the full `u>=1` tail

The predecessor deliberately discarded all `u>1` contribution. Because (7.4) is valid for every `rho`, this run asks whether the point at infinity can be added without losing a rigorous integrable bound.

For `rho>=2`, put `x=1/(2rho)<=1/4`. Since

`d/dx asin(x) = 1/sqrt(1-x^2)`

and on `[0,1/4]`

`1/sqrt(1-x^2) <= 4/sqrt(15) < 16/15`,

we have

`asin(1/(2rho)) <= 8/(15rho)`.                         (9.1)

Therefore

`q(rho)`

`< pi rho^2 + (8/5)rho + (3/2)rho + 1/2`

`= pi rho^2 + (31/10)rho + 1/2`.                      (9.2)

For `rho>=2`,

`(31/10)rho + 1/2 <= (13/7)rho^2`.                    (9.3)

Indeed the difference is positive at `rho=2`, where it equals `51/70`, and its derivative is already positive there and thereafter. With `pi<22/7`, (9.2)–(9.3) give the compactified tail bound

`q(rho) < 5 rho^2`.                                    (9.4)

Because `sqrt(5)<9/4`,

`q(rho)^(-7/2) > 4/(1125 rho^7)`.                     (9.5)

On the other hand, for `0<=d<=1/2` and `rho>=2`,

`2rho-d >= (7/4)rho`,

and `pi/3>1`, so (7.4) implies

`h(d,rho) >= (7/4)(1-d)d rho`.                         (9.6)

Multiplying (9.5) and (9.6) and integrating all the way to the added point at infinity yields

`integral_2^infinity h(d,rho) q(rho)^(-7/2) d rho`

`> (7/180000)(1-d)d`,                                 (9.7)

because `integral_2^infinity rho^(-6) d rho=1/160`.

### 9.1 Radial tail

The remaining radial shape integral is

`K = integral_0^(1/2) s(1-d(s))d(s) ds = 1/64`.        (9.8)

Using `3pi^2>27` and `sqrt(pi)>17/10`, (9.7) gives

`Delta_radial_tail > 357/40960000`

`= 0.0000087158203125`.                                (9.9)

### 9.2 Cap tail

For the disjoint cap, `W_cap>9/32` and `(1-d)d >= (9/10)(1/10)=9/100`, so

`Delta_cap_tail > 1071/2048000000`

`= 0.00000052294921875`.                               (9.10)

Outcome of Method #29: **success.** The tail is not merely finite; a fully explicit positive fraction of it is certified. No simulation or numerical quadrature is involved.

## 10. Combined theorem and certified movement

The total new near-range correction is

`Delta_near > 12699/819200000 + 39933/40960000000`

`= 674883/40960000000`.

The total newly retained tail correction is

`Delta_tail > 357/40960000 + 1071/2048000000`

`= 18921/2048000000`.

Thus the new full shape correction is

`Delta_shape_new > 1053303/40960000000`

`= 0.0000257154052734375`.                             (10.1)

This **replaces** the predecessor's

`Delta_shape_old = 56457/8192000000`.

The rigorous improvement over the predecessor endpoint is therefore

`Delta_shape_new - Delta_shape_old`

`= 385509/20480000000`

`= 0.000018823681640625 > 0`.                          (10.2)

Adding (10.1) to the carried exact equal-radius-envelope endpoint gives

`b_NUV >= b_base + Delta_shape_new`

`= 4916077214821159023396228863546259379089219326781 /
   7812500000000000000000000000000000000000000000000`

`= 0.629257883497108354994717...`

`> 0.6292578`.                                         (10.3)

This is a theorem about the frozen source-model liminf metric. It is not a proof of the parent law of large numbers.

### Finite-to-infinite transfer

No new asymptotic leap is introduced. The original closed-triple theorem already established the exact finite binomial event, boundary truncation, and Poisson/Campbell–Mecke limit. The current proof only partitions the same measurable shape integral and replaces the old union-area majorant by a smaller rigorously justified one on those subsets. The correction is nonnegative and is bounded by the carried equal-radius integrable envelope. The near and tail integrals above are explicit lower bounds on that same limiting integral, so the predecessor's dominated-convergence transfer continues to apply.

## 11. Exact-arithmetic certificate

A checker was warranted because this invocation moves the tracked numerical endpoint.

Created at commit

`2f5c9e8b356e0e3d4aa38c0b71be308c98d6df9b`

at

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T11-02-00Z__p0257_adaptive_sector_tail_exact.py`.

Executed output was archived at commit

`56d64f1cf6c6ffa61eb04796437c0b94a4c21ebe`

at

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T11-02-00Z__p0257_adaptive_sector_tail_exact.out`.

The output was read back at that commit. It records, among other exact checks,

- `RADIAL_NEAR_J = 83/1920`;
- `RADIAL_TAIL_K = 1/64`;
- `TAIL_Q_LT_5_RHO2_GATE = True`;
- `TAIL_KERNEL_EXACT = 7/180000`;
- `TOTAL_SHAPE_DELTA = 1053303/40960000000`;
- `GAIN_OVER_PREVIOUS_EXACT = 385509/20480000000`;
- `NEW_ENDPOINT_DECIMAL = 0.629257883497108354994717`;
- `NEW_ENDPOINT_GT_0.6292578 = True`;
- terminal line `ALL_EXACT_FINITE_CHECKS_PASS`.

The checker uses exact `Fraction` arithmetic, integer/rational comparisons, and Machin-series interval bounds for `pi`; there is no floating-point assumption in the certified inequalities.

This is a **self-check**, not an independent audit.

## 12. Why this is new route work rather than certificate polishing

The movement does not come from refining a Riemann mesh or tightening decimal approximations. The prior run's geometric loss had two structural causes: it used a fixed `pi/3` sector and threw away the entire `u>1` range. This invocation found a deficit-dependent angular invariant, integrated that exact geometric saving over the inflation parameter, and proved an analytic tail estimate extending to infinity. The gain (10.2) comes from those new inequalities.

The route remains within the same source-valid closed-triple architecture because it continues to move the tracked quantity. If a future higher-order refinement stops moving `b_NUV`, it should be abandoned rather than generating more certificates for the same endpoint.

## 13. Next research route

The next three unused Section-B moves will be **#1 CHANGE THE CATEGORY, #9 RANDOMIZE, #27 SWAP THE QUANTIFIERS**. The intended route is deliberately not another numerical sharpening of the three-disk envelope.

- **#1 CHANGE THE CATEGORY:** recast closed local NUV-forcing motifs as finite components / traps in a directed nearest-neighbor or order-`k` geometric graph, so that forced departure bonuses can be counted structurally rather than triangle-by-triangle.
- **#9 RANDOMIZE:** place a random mark/order on a finite closed motif and average over the entrance/exit structure, seeking a positive Palm-density additive bonus not visible from deterministic three-point geometry alone.
- **#27 SWAP THE QUANTIFIERS:** instead of demanding one uniform bonus valid for every local shape, seek a source-valid statement that for a positive-measure set of Poisson local configurations there exists a forced NUV departure excess, with the measurable selection integrated before taking the infinite-volume limit.

A successful next step must produce a rigorously non-double-counted contribution beyond `0.629257883497108...` or a genuinely source-relevant theorem. Merely tightening the constants in Sections 8–9 is not the planned route.

## 14. Structured ledger_delta for P26

```json
{
  "worker": "NM13-11",
  "source_id": "P0257",
  "claim_id": "P0257",
  "canonical_dedup_key": "law_of_large_numbers_and_constants_for_nuv_lengths",
  "category": "HARD OUTSIDE",
  "source_status_before": "OPEN",
  "source_status_after": "OPEN",
  "track_status_before": "PARTIAL",
  "track_status_after": "PARTIAL",
  "metric_name": "b_NUV",
  "metric_definition": "explicit certified lower endpoint in liminf E[L_n]/n >= b_NUV for the exact Euclidean NUV source model",
  "metric_before_exact": "4915930154808341640583728863546259379089219326781/7812500000000000000000000000000000000000000000000",
  "metric_before_decimal": "0.629239059815467729994717...",
  "metric_after_exact": "4916077214821159023396228863546259379089219326781/7812500000000000000000000000000000000000000000000",
  "metric_after_decimal": "0.629257883497108354994717...",
  "metric_moved": true,
  "certified_increment_over_predecessor": "385509/20480000000 = 0.000018823681640625",
  "methods_tried": [6, 12, 29],
  "method_outcomes": {
    "6": "success: deficit-adaptive outward sector lemma",
    "12": "success: conserved angular support inequality permits integrated near-range saving",
    "29": "success: q(rho)<5 rho^2 tail compactification yields explicit positive u>=1 correction"
  },
  "unchanged_runs_before": 0,
  "unchanged_runs_after": 0,
  "hard_recoveries_before": 0,
  "hard_recoveries_after": 0,
  "hard_recoveries_limit": 2,
  "checker": "proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T11-02-00Z__p0257_adaptive_sector_tail_exact.py",
  "checker_output": "proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T11-02-00Z__p0257_adaptive_sector_tail_exact.out",
  "checker_terminal": "ALL_EXACT_FINITE_CHECKS_PASS",
  "p26_audit": "NOT_REQUESTED_NOT_PRESUMED",
  "secondary_audit_partner": "NM13-12",
  "secondary_audit": "NOT_REQUESTED_NOT_PRESUMED",
  "next_methods": [1, 9, 27],
  "next_step": "seek a higher-order local forcing motif / directed-geometric-graph formulation giving a non-double-counted Palm-density bonus beyond the current b_NUV endpoint",
  "shared_roots_modified": false,
  "peer_namespaces_modified": false,
  "scheduler_modified": false
}
```

## 15. Operational closeout

Exactly one own-namespace immutable report is intended for this invocation: this file. No shared root, peer namespace, canonical claim file, scheduler, permission, workflow, email/Drive resource, public surface, or paid compute was modified. The two substantive artifacts above were created only because the new geometry moved the frozen quantity and required exact certification.

P0257 remains **PARTIAL / SOURCE OPEN**. Closure requirements are not met and are not claimed: no source-level solution, no paper folder, no P26 audit, and no NM13-12 independent audit are asserted.
