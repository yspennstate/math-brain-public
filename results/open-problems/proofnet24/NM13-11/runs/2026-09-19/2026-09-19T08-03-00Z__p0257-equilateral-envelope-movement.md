Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MATHEMATICAL MOVEMENT: `b_NUV >= 15726690474745880958345733429927955202801271874129/25000000000000000000000000000000000000000000000000 = 0.629067618989835238333829...` -> `b_NUV >= 4915876313217460292927478863546259379089219326781/7812500000000000000000000000000000000000000000000 = 0.629232168091834917494717... > 0.629232`; actual Section-B methods tried: #5 ADD A PARAMETER AND DIFFERENTIATE, #14 FIND THE GROUP ACTING, #25 COUNT THE SAME THING TWICE.**

# NM13-11 — P0257 equilateral-envelope refinement of the closed-triple bound

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-11` / `proofnet24/NM13-11/`  
Category: **HARD OUTSIDE**  
Canonical source / claim ID: **P0257**  
Status after this invocation: **PARTIAL / SOURCE OPEN / CLAIM RETAINED**

## 1. Result and fixed metric

This invocation continues the already-admitted canonical source `P0257`, David J. Aldous, *The Nearest Unvisited Vertex Walk on Random Graphs* (arXiv:1912.13175; *Probability in the Engineering and Informational Sciences* 36 (2022), 851–867). The exact Euclidean model and the frozen metric are unchanged:

- `n` i.i.d. uniform points in the unit square;
- uniform random starting vertex;
- NUV greedily moves to the nearest unvisited vertex;
- in the source's area-`n` scaling, total walk length is `L_n`;
- source first-order question: existence/identification of `c = lim L_n/n`;
- worker metric: `b_NUV`, the explicit certified endpoint in

`liminf_{n -> infinity} E[L_n]/n >= b_NUV`.

Before this run the strongest NM13-11 certificate was

`b_prev = 15726690474745880958345733429927955202801271874129 / 25000000000000000000000000000000000000000000000000`

`= 0.629067618989835238333829...`.

This run proves and exactly certifies

`b_NUV >= 4915876313217460292927478863546259379089219326781 / 7812500000000000000000000000000000000000000000000`

`= 0.629232168091834917494717... > 0.629232`.

The certified gain over the previous worker endpoint is approximately

`0.000164549101999679160888...`.

This is genuine movement of the frozen metric. It is not a literature-baseline correction. The source question remains open because this lower bound does **not** establish existence of `lim L_n/n`.

Admitted-target counters after this report:

- unchanged runs after admission: **0 -> 0** (movement resets/keeps the counter at zero);
- stuck-recovery episodes: **0 / 2**;
- source status: **PARTIAL / OPEN**;
- P26 audit: **NOT REQUESTED / NOT PRESUMED**;
- NM13-12 secondary audit: **NOT REQUESTED / NOT PRESUMED**.

## 2. Runtime and scheduler-control truth

The requested `GPT-6 / maximum` text is not an enforceable runtime setting in the exposed scheduler surface. This invocation actually identifies as **GPT-5.6 Sol**. There is no authenticated reasoning-effort telemetry, so reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, an hour-long execution, or a support escalation.

The exposed task-control surface provides task identity/title, prompt, schedule or relative-start fields, timing mode, enabled state, and list/update operations. It exposes **no bindable model-family selector and no bindable reasoning-effort selector**, and no authenticated applied-model/applied-effort receipt. Making GPT-6/maximum binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists those fields into inference routing and returns trustworthy per-run attestation.

The historical P26 response `You cannot modify this task` is an authorization-context boundary. Current `RESULTS.md` records that a later full P26 update succeeded from another authorized context. The lawful workaround for a future denial is the owning or otherwise authorized account/workspace/API/admin context, or authorized platform support for that same existing task—not duplication, identity substitution, or permission bypass. No scheduler or permission was modified here.

## 3. Authoritative continuity and required repository reads

The controlling predecessor is

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T07-04-00Z__p0257-closed-triple-bound-movement.md`

created at commit

`b9511f0f63760f278d9bb468f5e39465eb8861a4`.

Its durable state was:

- P0257 admitted and exclusively owned by NM13-11;
- canonical dedup key `law_of_large_numbers_and_constants_for_nuv_lengths`, residue 10 modulo 13;
- exact Euclidean NUV source model frozen;
- metric `b_NUV` frozen;
- literature baseline corrected to the rigorous planar EMST lower bound `0.6289` before worker-credit accounting;
- NM13-11 closed-two-nearest-triple certificate moved the worker endpoint to `b_prev = 0.629067618989835...`;
- prior run genuinely used methods #11/#20/#24;
- next planned methods were #5/#14/#25;
- unchanged count 0, stuck recoveries 0/2.

Before substantive work I freshly read or recovered the controlling fleet/state surfaces: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the controlling NM13-11 report; current `operations/claims/P0257.md`; candidate-specific intake/catalog/ranking evidence and prior-attempt state (`attempted_unsolved`, including the older nearest-neighbor lower inequality); and the newest neighboring NM13-10 and NM13-12 reports visible before this write.

Newest neighboring records recovered were:

- NM13-10: `proofnet24/NM13-10/runs/2026-09-19/2026-09-19T07-58-30Z__admission-delta-screen-37-p0336-p0458-p0459-owned-offshard-p0220-not-release.md` — still admission-pending and no collision with P0257;
- NM13-12: `proofnet24/NM13-12/runs/2026-09-19/2026-09-19T07-10-00Z__p0214-dual-resampling-flip-barrier.md` — P0214 retained independently; no P0257 audit or ownership mutation is recorded there.

The append-only intake/attempt corpora are too large to honestly claim every unchanged historical byte was re-rendered model-visible in this invocation. Candidate-specific P0257 source, canonical dedup identity, rank/catalog state and prior attempt were recovered; the exact Git delta below contains no changed intake `problems.jsonl` or probability attempt ledger, so unchanged historical rows are carried rather than silently reset.

No private-repository history needed for this P0257 continuation was known to be inaccessible.

## 4. Exact repository delta and ownership check

Frozen pre-report `master` head after writing and reading back this run's two substantive artifacts:

`e3664aaa0ccac0cd54d889c0fad2132410f3ad7f`.

Exact comparison

`b9511f0f63760f278d9bb468f5e39465eb8861a4 .. e3664aaa0ccac0cd54d889c0fad2132410f3ad7f`

reports:

- status: `ahead`;
- commits ahead: **95**;
- commits behind: **0**;
- total commits: **95**;
- `too_large = null`, so the connector returned the complete changed-file set.

In that complete set:

- `operations/claims/P0257.md` is absent;
- root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, intake `problems.jsonl`, probability attempt ledgers, and controlling owner/NM13 policy files are absent;
- new canonical claims `P0336` and `P0459` are owned by other workers and do not affect P0257;
- no canonical P0257 release, handoff, retirement, or alias collision appears.

A direct read of `operations/claims/P0257.md` at this frozen head still says `CLAIMED / ADMITTED / HARD OUTSIDE`, owner `proofnet24/NM13-11/`, canonical residue 10. Ownership therefore remains intact.

## 5. Fresh source and literature check, dated 2026-09-19

Public-web checks this invocation included the original source, current source publication page, the load-bearing disk-union comparison theorem, the current EMST baseline paper, and focused 2024–2026 NUV searches.

Checked sources/results:

1. **Aldous, NUV source.** arXiv:1912.13175 still describes the order-of-magnitude theory and explicitly says that establishing sharper results is challenging. Cambridge records the article as published online 5 April 2021 and in the July 2022 issue. The source text around Equation (4) proposes the Euclidean first-order constant and says only an `O(n)` bound is rigorous there.
2. **Kneser–Poulsen in the plane.** Károly Bezdek and Robert Connelly, *Pushing disks apart — The Kneser-Poulsen conjecture in the plane*, arXiv:math/0108098, J. reine angew. Math. 553 (2002), prove that if a finite collection of planar disks is rearranged so that every pairwise center distance does not decrease, then the area of the union does not decrease. This theorem is used below as prior art; it is not claimed as new.
3. **EMST baseline.** Draganov–Edelsbrunner–Rosenmeier–Saghafian, arXiv:2510.23373 (27 October 2025), prove the rigorous planar Euclidean-MST lower constant `0.6289`. That remains below both the preceding NM13-11 certificate and the new one here; it is background, not worker movement in this invocation.
4. **Focused current-status search.** Queries such as `"nearest unvisited vertex" 2024 2025 2026 Aldous random points limit constant`, `"Nearest Unvisited Vertex Walk" law of large numbers constant`, and exact-title/source searches did not recover a checked later primary-source proof or refutation of Aldous's Euclidean Equation-(4) limit question. This is bounded negative evidence only, not proof of worldwide openness or novelty.

The geometry below is therefore presented as a proved route/certificate in this repository, with no claim that the mechanism is absent from all prior literature.

## 6. Carried closed-triple inequality from the preceding report

I do not restart the already-proved closed-triple argument. The controlling predecessor established, for a unit-intensity planar Poisson process and then by a finite-binomial-to-Poisson transfer for the source model, that

`b_NUV >= 5/8 + C/2`,

where

`C = (1/6) integral_{x in R^2} integral_{y in R^2} integral_{t>=0} exp(-A_t(x,y)) dt dy dx`.

For the inserted triple `{0,x,y}`, let

`D = max(|x|, |y|, |x-y|)`

and at each of its three vertices let `r_i` be the larger distance to the other two inserted vertices. The exclusion area is

`A_t(x,y) = area( union_{i=1}^3 B(v_i, r_i+t) )`.

The previous report bounded this union by the parallel body of the convex hull and obtained the old normalized area majorant

`q_old(rho) = pi*rho^2 + 3*rho + sqrt(3)/4`,  `rho = 1+t/D >= 1`.

This run changes the geometry rather than merely refining the preceding Riemann mesh.

## 7. Method #14 — FIND THE GROUP ACTING: reduce shape to the equilateral expansion

The useful symmetry is the planar similarity group together with permutation symmetry of the three inserted points.

For `D>0`, scale the configuration by `1/D`. Every pairwise center distance is then at most 1. Also `r_i <= D`, so for `R=D+t`,

`B(v_i, r_i+t) subseteq B(v_i, R)`

for every `i`. Consequently

`A_t(x,y) <= area( union_i B(v_i,R) )`.

Now move the three centers to the vertices of an equilateral triangle of side `D`, keeping the common radius `R` fixed. Every one of the three pairwise center distances weakly increases, because each original pair distance is at most `D`. The planar Bezdek–Connelly Kneser–Poulsen theorem therefore gives

`area( union_i B(v_i,R) ) <= area( union_i B(w_i,R) )`,

where the `w_i` form an equilateral triangle of side `D`.

Thus all triangle-shape variables are rigorously dominated by a one-parameter equilateral envelope. Writing

`rho = R/D = 1+t/D`,

we have

`A_t(x,y) <= D^2 q_Delta(rho)`

for an explicit scalar function `q_Delta`. This verifies the comparison hypotheses instead of assuming that an equilateral triple is extremal by symmetry alone.

Outcome of method #14: **success; arbitrary triangle shape collapses to one scalar parameter without changing the source model or quantifiers.**

## 8. Method #25 — COUNT THE SAME THING TWICE: exact equilateral union formula

For three congruent disks of radius `rho >= 1` centered at the vertices of a unit equilateral triangle, define their union area `q_Delta(rho)`.

### First count: inclusion-exclusion

Let

`alpha = acos(1/(2rho))`,  `s = sqrt(4rho^2-1)`.

The overlap area of one pair of disks is

`I_2 = 2 rho^2 alpha - s/2`.

A direct decomposition of the common three-disk intersection into its central triangle and three circular segments gives

`I_3 = (3/2) rho^2 (2alpha - pi/3) + sqrt(3)/4 - (3/4)s`.

Inclusion-exclusion yields

`q_Delta = 3pi rho^2 - 3I_2 + I_3`

and, using `alpha = pi/2 - asin(1/(2rho))`, simplifies to

`q_Delta(rho) = pi rho^2 + 3 rho^2 asin(1/(2rho)) + (3/4)sqrt(4rho^2-1) + sqrt(3)/4`.   (1)

### Second count: parallel body minus the three side gaps

The parallel body of the unit equilateral triangle by radius `rho` has Steiner area

`pi rho^2 + 3rho + sqrt(3)/4`.

Along each of the three sides, the parallel body contains one congruent curvilinear gap not covered by the two endpoint disks. Its area is

`g(rho) = rho - rho^2 asin(1/(2rho)) - (1/4)sqrt(4rho^2-1)`.

For `rho>=1` the three gaps are disjoint and the triangle itself is covered by the vertex disks, so subtracting the three gaps gives

`q_Delta(rho) = pi rho^2 + 3rho + sqrt(3)/4 - 3g(rho)`,

which is exactly formula (1).

Moreover

`g'(rho) = 1 - 2rho asin(1/(2rho)) < 0`

because `asin z > z` for `z>0`, and `g(rho) -> 0` as `rho -> infinity`. Hence `g(rho)>0` for every finite `rho>=1`, proving pointwise that

`q_Delta(rho) < q_old(rho)`.

Outcome of method #25: **success; two independent geometric counts agree and prove that the new envelope is strictly sharper than the preceding parallel-body envelope.**

## 9. Method #5 — ADD A PARAMETER AND DIFFERENTIATE: monotonicity and the corrected integral

Differentiate formula (1). If `s=sqrt(4rho^2-1)`, then

`d/drho [3rho^2 asin(1/(2rho))] = 6rho asin(1/(2rho)) - 3rho/s`,

while

`d/drho [(3/4)s] = 3rho/s`.

The singular-looking terms cancel exactly, leaving

`q_Delta'(rho) = 2pi rho + 6rho asin(1/(2rho)) > 0`.   (2)

Thus the new normalized integrand `q_Delta(1+u)^(-5/2)` is strictly decreasing in `u>=0`. This is what permits a rigorous right-Riemann lower certificate with only upper enclosures on `q_Delta`.

The diameter shell calculation from the preceding report is unchanged. The four-dimensional volume of ordered pairs `(x,y)` with `max(|x|,|y|,|x-y|)<=D` is `V D^4`, where

`V = pi(4pi-3sqrt(3))/4`.

Therefore the shell density is `4V D^3 dD`. Substitute `t=Du`, apply the area majorant `A_t <= D^2 q_Delta(1+u)`, and integrate in `D`:

`C`
`>= (1/6) integral_0^infinity integral_0^infinity 4V D^4 exp(-D^2 q_Delta(1+u)) dD du`
`= (V sqrt(pi)/4) integral_0^infinity q_Delta(1+u)^(-5/2) du`.

Combining this with the carried deterministic/Poisson closed-triple inequality gives the new theorem

`liminf E[L_n]/n`
`>= 5/8 + (V sqrt(pi)/8) integral_0^infinity q_Delta(1+u)^(-5/2) du`,   (3)

with `q_Delta` given by (1).

Outcome of method #5: **success; differentiation exposes an exact cancellation, proves the monotonicity needed for certified quadrature, and the resulting source-valid bound beats the tracked endpoint.**

## 10. Exact-arithmetic certificate

Only after the analytic route moved the quantity did I build an exact checker.

Artifacts:

- code: `proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T07-50-00Z__p0257_equilateral_envelope_exact.py`, create commit `3809374a8427ec30e019d2e7bf151d4a7924dcf0`;
- output: `proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T07-50-00Z__p0257_equilateral_envelope_exact.out`, create commit `e3664aaa0ccac0cd54d889c0fad2132410f3ad7f`.

Both were read back at their creation commits. The checker uses no floating-point arithmetic in any assertion. It supplies:

- rational Machin-series enclosures for `pi`;
- integer-square-root enclosures for radicals;
- for `0<=x<=1/2`, a positive Taylor upper bound for `asin(x)` through `j=20`, with omitted tail bounded by `x^(43)/(1-x^2)`;
- exact upper bounds on `q_Delta` at right endpoints;
- the monotonicity (2) to justify a right-Riemann lower sum;
- `N=20000` intervals on `u in [0,20]`, step `1/1000`;
- the positive tail `u>20` is simply discarded, so no asymptotic tail estimate is needed for rigor.

Archived output:

`I_LO_DECIMAL = 0.003299952834822327985589`

`C_LO_DECIMAL = 0.008464336183669834989434`

and

`B_LO_EXACT = 4915876313217460292927478863546259379089219326781/7812500000000000000000000000000000000000000000000`

`B_LO_DECIMAL = 0.629232168091834917494717`

with exact assertions

`B_LO_GT_PREVIOUS_CERT = True`

`B_LO_GT_0.629232 = True`

`B_LO_GT_0.6289 = True`

and terminal line

`ALL_EXACT_FINITE_CHECKS_PASS`.

This checker is a self-check/certificate for the finite arithmetic core. It is not an independent audit and is not represented as one.

## 11. What changed mathematically, and what did not

The movement is specifically the sharpening of the closed-triple exclusion-area comparison:

`q_old(rho) = pi rho^2 + 3rho + sqrt(3)/4`

is replaced by the strictly smaller source-valid equilateral disk-union envelope

`q_Delta(rho) = pi rho^2 + 3rho^2 asin(1/(2rho)) + (3/4)sqrt(4rho^2-1) + sqrt(3)/4`.

That one geometric change raises the certified worker endpoint from `0.6290676189...` to `0.6292321680...`.

What is **not** proved:

- existence of the Aldous limit `c`;
- identification of `c`;
- concentration or a CLT for `L_n`;
- optimality of the new lower bound;
- novelty in the worldwide literature beyond the bounded searches recorded above.

Therefore the honest status remains **PARTIAL / source OPEN**, not PROVED or KNOWN.

## 12. Route discipline and next methods

The preceding route did move, so the HARD stuck protocol is not triggered. I also do **not** spend another run merely making the `u` mesh finer: that would be checker polishing rather than research.

The next route will attack information discarded before the Kneser–Poulsen envelope. Planned Section-B methods are:

- **#15 BREAK THE SYMMETRY ON PURPOSE:** retain the unequal radii `r_i+t` rather than enlarging all three to `D+t`; identify which scalene/isosceles triangle classes contribute the largest avoidable area loss.
- **#18 SAY IT IN ANOTHER LANGUAGE:** rewrite the three-disk union correction in side-length / Voronoi-power coordinates so the exact union area can be integrated or bounded by cells rather than by a global diameter envelope.
- **#30 DO ONE SCALE, ONE DIRECTION AT A TIME:** partition normalized triangle shape by longest side and angle/height ranges and seek a finite family of exact area majorants whose Campbell–Mecke contributions add without overlap.

The success criterion is another strict increase of `b_NUV` (or a source-level theorem such as limit existence). If those routes cease to move the tracked quantity, they will be abandoned rather than converted into more certificates for the same bound.

## 13. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-11
  source_id: P0257
  claim_id: P0257
  category: HARD_OUTSIDE
  canonical_dedup_key: law_of_large_numbers_and_constants_for_nuv_lengths
  canonical_shard_mod_13: 10
  source_status_before: PARTIAL_OPEN
  source_status_after: PARTIAL_OPEN
  metric_name: b_NUV
  metric_definition: "explicit certified endpoint in liminf E[L_n]/n >= b_NUV"
  metric_before_exact: "15726690474745880958345733429927955202801271874129/25000000000000000000000000000000000000000000000000"
  metric_before_decimal: "0.629067618989835238333829..."
  metric_after_exact: "4915876313217460292927478863546259379089219326781/7812500000000000000000000000000000000000000000000"
  metric_after_decimal: "0.629232168091834917494717..."
  movement: true
  movement_kind: "new theorem/certificate; not literature-baseline correction"
  methods_tried:
    - 5
    - 14
    - 25
  method_outcomes:
    5: "success: derivative cancellation proves q_Delta increasing and enables exact lower quadrature"
    14: "success: similarity/S3 plus planar Kneser-Poulsen reduces arbitrary triple shapes to an equilateral common-radius envelope"
    25: "success: inclusion-exclusion and parallel-body-minus-gaps give the same exact equilateral union formula"
  unchanged_runs_before: 0
  unchanged_runs_after: 0
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
  hard_recovery_limit: 2
  p26_audit: NOT_REQUESTED
  nm13_12_audit: NOT_REQUESTED
  source_closed: false
  next_methods:
    - 15
    - 18
    - 30
  next_step: "retain unequal radii and normalized triangle shape; seek a finite exact shape-cell envelope that strictly raises b_NUV"
  artifacts:
    checker: "proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T07-50-00Z__p0257_equilateral_envelope_exact.py"
    checker_commit: "3809374a8427ec30e019d2e7bf151d4a7924dcf0"
    output: "proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T07-50-00Z__p0257_equilateral_envelope_exact.out"
    output_commit: "e3664aaa0ccac0cd54d889c0fad2132410f3ad7f"
```

## 14. Prohibited-action audit

This invocation created only the two warranted exact-arithmetic artifacts above and this single immutable NM13-11 run report. It did not edit `operations/claims/P0257.md`, shared root ledgers, peer namespaces, other claims, permissions, schedules, workflows, public surfaces, email/Gmail, Drive, or paid-compute resources. No owner was overwritten and no audit was presumed.
