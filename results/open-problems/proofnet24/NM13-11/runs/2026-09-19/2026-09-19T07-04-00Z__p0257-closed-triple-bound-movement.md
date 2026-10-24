Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MATHEMATICAL MOVEMENT after correcting the carried literature baseline: `b_NUV >= 0.6289 -> b_NUV >= 15726690474745880958345733429927955202801271874129 / 25000000000000000000000000000000000000000000000000 > 0.62906`; actual Section-B methods tried: #11 DUALIZE, #20 FIND WHY THE ALGORITHM FAILS, #24 FIND THE EXTREMAL OBJECT.**

# NM13-11 — P0257 closed-two-nearest-triple lower bound

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-11` / `proofnet24/NM13-11/`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `P0257` / `operations/claims/P0257.md`  
Source status: `OPEN`  
Track status after this run: `PARTIAL`

## 1. Runtime truth, continuity, ownership, and the corrected baseline

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. The exposed runtime provides no authenticated reasoning-effort telemetry, so reasoning is **UNVERIFIED**. I do not claim GPT-6 maximum, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still has prompt/title, schedule/timing, enablement and update/list operations, but no bindable model-family field, no bindable reasoning-effort field, and no authenticated per-run applied-model/effort attestation. Therefore GPT-6 / maximum remains prompt text only. Making it binding would require an authorized product/workspace/API/admin scheduling surface that persists those fields into inference routing and returns trustworthy per-run attestation. The historical P26 `You cannot modify this task` event remains an authorization-context boundary; current `RESULTS.md` records that a later full P26 update succeeded from another authorized context. The lawful workaround for a denied task is therefore the owning/authorized context or an authorized platform/admin route for that same task, not task duplication or permission bypass. No schedule was modified here.

I reread the controlling fleet material and current research state: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the newest own report; newest neighboring NM13-10 and NM13-12 reports; the P0257 claim; campaign/intake/attempt evidence recovered by the admitted claim; and current ownership searches. The exact pre-write master snapshot used for the final ownership read was `fe14e2db92625b3f6259dab1cdeb597b2e025595`. At that commit `operations/claims/P0257.md` still reads `CLAIMED / ADMITTED / HARD OUTSIDE`, owner `proofnet24/NM13-11/`, canonical key `law_of_large_numbers_and_constants_for_nuv_lengths`, residue 10. No ownership release or collision was found. The repository is concurrently active; this snapshot statement is deliberately commit-specific.

The controlling predecessor is

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T06-05-30Z__p0257-admission-guarded-pair-nonmovement.md`

at creation commit `fb2b84d30dbc13e64ca85535b8da182b92566d02`. It admitted P0257, recovered a then-known TSP lower endpoint `0.6277`, proved a weaker guarded-pair bound `0.5000384197...`, correctly recorded no metric movement, and set the next methods to #11/#20/#24. Its P0257 unchanged-run count was 1 and stuck recoveries 0/2.

A fresh literature check changed the **baseline before new mathematics**, not by worker credit. Draganov--Edelsbrunner--Rosenmeier--Saghafian, arXiv:2510.23373 (submitted 2025-10-27), state and prove a new planar Euclidean MST asymptotic lower bound `c_MST >= 0.6289`, improving the previous `0.6008`. Any NUV Hamiltonian path is itself a spanning tree, so in the exact source model `L_NUV >= L_MST` pointwise. Hence the correct pre-research metric for this run is at least `0.6289`, superseding the carried `0.6277`. This is a literature correction, not NM13-11 progress.

Fresh bounded searches dated 2026-09-19 for the exact Aldous title, `nearest unvisited vertex`, NUV Euclidean random points, later citing work, and local `two-nearest` / triple mechanisms recovered Aldous's original paper and maintained homepage plus adjacent nearest-neighbor literature, but no checked primary source resolving the Euclidean Equation-(4) first-order constant or giving the closed-triple bound proved below. Aldous's maintained page still describes improving beyond order of magnitude for NUV random-graph models as a challenge. A 2026 follow-up by the EMST authors still describes the classic EMST constant as not precisely known. These are bounded searches, not proof of worldwide openness, novelty, or priority. Poisson void probabilities, Palm/Mecke counting, nearest-neighbor order statistics, and the convex parallel-body formula used below are standard mechanisms; no novelty is claimed for those ingredients individually.

## 2. Frozen source model and metric

Use Aldous's Euclidean random-points model in area-`n` scaling. Let

`Q_n = [0,sqrt(n)]^2`

and sample exactly `n` iid uniform points in `Q_n`. Start the NUV rule from the source's uniformly chosen starting vertex; at each step move to the closest unvisited point. Let `L_n` be the resulting Hamiltonian-path length. This is exactly `sqrt(n)` times the source's unit-square length.

The frozen metric remains unchanged in definition:

`b_NUV = explicit certified lower endpoint in liminf_{n->infinity} E[L_n]/n >= b_NUV.`

Carried predecessor endpoint: `0.6277`.  
Corrected literature endpoint before new proof: `0.6289`.  
Certified endpoint after this run:

`B_cert = 15726690474745880958345733429927955202801271874129 / 25000000000000000000000000000000000000000000000000`

with exact checker output showing

`B_cert = 0.629067618989835238333829... > 0.62906 > 0.6289`.

Thus the research metric genuinely moves after the baseline correction.

## 3. What methods #11/#20/#24 did

### #20 — find why the obvious lower algorithm fails

The predecessor's proposed TSP / Held--Karp direction contains a structural defect for this source: a generic spanning-tree, 2-factor or tour relaxation forgets the **greedy order constraint** that distinguishes NUV from an arbitrary Hamiltonian path. Improving such a relaxation can improve a universal route lower bound, but it need not capture any NUV-specific excess.

The first deterministic order witness I found that survives this objection is a **closed two-nearest triple**. In such a triple, once NUV enters the triple it is forced to consume all three vertices consecutively. That creates a forced third-neighbor exit at the last vertex of the triple and therefore an additive gap which an arbitrary Hamiltonian-path degree bound misses.

Outcome: the route obstruction was identified and converted into a positive NUV-specific correction rather than another generic tour certificate.

### #11 — dualize into a local degree-incidence lower functional

Instead of optimizing the path itself, charge twice its total length to incident edge lengths at vertices. The generic dual-style local lower functional is the sum of the first two neighbor distances, with endpoint corrections. Closed triples contribute an additional nonnegative local slack because the last vertex in each forced triple must exit past its two nearest neighbors.

Outcome: this gives the deterministic inequality in Lemma 4.1 below and separates a universal `5/8` Poisson degree floor from an NUV-only correction density.

### #24 — find the extremal geometric object

For a closed triple of diameter `D`, the exact external-void region is a union of three unequal disks. Rather than evaluate every triangle shape, dominate that union by the parallel body of the triangle. At fixed diameter, the needed upper bounds are attained at the extremal equilateral geometry: area at most `sqrt(3) D^2/4` and perimeter at most `3D`. This turns the four-dimensional triangle-shape integral into one explicit one-dimensional integral.

Outcome: the resulting correction is large enough to clear the corrected `0.6289` literature baseline.

## 4. Full proof of the new quantitative theorem

### Theorem 4.1 — closed-two-nearest-triple NUV bound

For the exact Euclidean P0257 model,

`liminf_{n->infinity} E[L_n]/n >= B_cert > 0.62906.`

In particular the frozen metric satisfies `b_NUV >= B_cert`.

### 4.1 Deterministic path inequality

Fix a finite point set in general position, so every vertex has distinct distances to all other vertices. For a vertex `v`, write

`r_1(v) < r_2(v) < r_3(v)`

for its first, second and third nearest-neighbor distances.

Call an unordered three-set `T={a,b,c}` a **closed two-nearest triple** if, for every `v in T`, the two nearest neighbors of `v` are exactly the other two members of `T`. Define

`g(T) = min_{v in T} (r_3(v)-r_2(v)).`

Closed two-nearest triples are pairwise vertex-disjoint: if two shared a vertex, that vertex's unique unordered pair of two nearest neighbors would determine both triples.

Let `P` be the NUV path and let `s,t` be its first and last vertices. First ignore the NUV rule and use only that `P` is a Hamiltonian path. At each internal vertex the two incident path edges are two distinct edges from that vertex, so their length sum is at least `r_1(v)+r_2(v)`. At an endpoint there is only one incident edge, of length at least `r_1(v)`. Since summing incident path-edge lengths over all vertices counts each path edge twice,

`2 L(P) >= sum_v (r_1(v)+r_2(v)) - r_2(s)-r_2(t).`      (4.1)

Now use the NUV order. Suppose NUV first enters a closed triple `T` at `x`. Both other members are still unvisited and are the two nearest points to `x`, so the next vertex is another member, say `y`. At `y`, one member of the triple has just been visited and the remaining member `z` is one of the two globally nearest points to `y`; every external point is farther. Hence NUV next visits `z`. Thus every closed triple is consumed in three consecutive visits.

If `z` is not the terminal vertex `t`, its outgoing NUV edge goes to an external point and therefore has length at least `r_3(z)`. Its incoming edge from `y` has length either `r_1(z)` or `r_2(z)`. In either case the incident-edge sum at `z` exceeds the generic `r_1(z)+r_2(z)` charge by at least

`r_3(z)-r_2(z) >= g(T).`

Because closed triples are disjoint, these bonuses do not double count vertices. At most one closed triple contains the terminal NUV vertex and therefore misses its bonus. Its missed `g(T)` is at most the diameter of the point set. Hence

`2L(P) >= sum_v(r_1(v)+r_2(v)) - r_2(s)-r_2(t) + sum_T g(T) - diam(S).`      (4.2)

This is the source-specific deterministic gain.

### 4.2 The generic local-degree term contributes `5/8`

Return to the iid sample in `Q_n`. For the unit-intensity planar Poisson process, if `R_k` is the distance from a Palm point to its `k`th nearest other point, then

`pi R_k^2 ~ Gamma(k,1)`

and therefore

`E R_1 = 1/2`,     `E R_2 = 3/4`.      (4.3)

For completeness, the binomial source model transfers to these numbers without assuming full moment convergence. Fix `R<infinity` and condition on a sampled anchor point whose distance from the boundary of `Q_n` exceeds `R`. For `0<=r<=R`, the number of other sample points in its radius-`r` disk is `Bin(n-1, pi r^2/n)`, which converges uniformly on bounded `r` to `Poisson(pi r^2)`. Integrating the tail probabilities gives convergence of each truncated nearest-neighbor distance `min(r_k,R)` to `min(R_k,R)`. The fraction of anchors within distance `R` of the boundary tends to zero. Since the untruncated distances are nonnegative,

`liminf_n (1/n) E[sum_v (r_1(v)+r_2(v))] >= E R_1 + E R_2 = 5/4`      (4.4)

by letting `R -> infinity` and monotone convergence.

The endpoint terms in (4.2) are each at most `diam(Q_n)=sqrt(2n)`, and so is the possible missed terminal-triple bonus. After division by `2n` all three vanish.

Thus it remains to give a positive asymptotic lower bound on `n^{-1} E sum_T g(T)`.

### 4.3 Exact Poisson representation of the closed-triple correction density

Insert three points at locations `0,x,y` in a unit-intensity planar Poisson process. Let

`D = max(|x|, |y|, |x-y|)`

be the triangle diameter. For each of the three vertices `v_i`, let `r_i` be the larger of its two distances to the other inserted vertices; this is the second-neighbor radius within the triple. For `t>=0`, let

`U_t = union_i B(v_i, r_i+t)`,      `A_t = area(U_t)`.

The inserted triple is closed two-nearest and has `g(T)>t` exactly when the rest of the Poisson process has no point in `U_t` (ties have probability zero). The Poisson void probability is therefore `exp(-A_t)`. Layer cake and Campbell--Mecke give the correction density

`C = (1/6) int_{R^2} int_{R^2} int_0^infinity exp(-A_t(x,y)) dt dx dy.`      (4.5)

The factor `1/6` converts ordered inserted triples to unordered triples.

Here is a direct binomial-to-Poisson transfer, so (4.5) is not being used as an unproved thermodynamic-limit slogan. Fix `R`. Restrict to triples with `D<=R`, `0<=t<=R`, and anchors at distance at least `3R` from the boundary of `Q_n`. Then every disk in `U_t` lies inside `Q_n`, because its center is within `R` of the anchor and its radius is at most `D+t<=2R`. For a fixed inserted triple, the exact probability that the other `n-3` iid points avoid `U_t` is

`(1-A_t/n)^(n-3)`.

After multiplying by `choose(n,3)/n^3`, integrating the anchor and relative locations, dividing by `n`, and letting `n->infinity`, the anchor interior fraction tends to one, `choose(n,3)/n^3 -> 1/6`, and the displayed avoidance probability converges uniformly on this bounded domain to `exp(-A_t)`. Therefore

`liminf_n (1/n) E[sum_T g(T)] >= (1/6) int_{D<=R} int_0^R exp(-A_t) dt dx dy.`

Letting `R->infinity` and applying monotone convergence yields (4.5) as a rigorous lower bound for the source binomial model.

### 4.4 Extremal parallel-body bound

Let `K=conv{0,x,y}`. Since every `r_i<=D`,

`U_t subset K + B(0,D+t)`.

For a convex planar set, the parallel-body formula gives

`area(K+B(0,R)) = area(K) + perimeter(K) R + pi R^2.`

For any triangle of diameter `D`,

`area(K) <= (sqrt(3)/4) D^2`,     `perimeter(K) <= 3D`.

Consequently

`A_t <= alpha D^2 + beta D t + pi t^2`,      (4.6)

where

`alpha = pi + 3 + sqrt(3)/4`,     `beta = 2pi+3`.

The four-dimensional volume of ordered pairs `(x,y)` with triangle diameter at most `D` equals `V D^4`, with

`V = int_{|x|<=1} area(B(0,1) intersect B(x,1)) dx`

`  = 2pi int_0^1 r [2 arccos(r/2) - (r/2)sqrt(4-r^2)] dr`

`  = pi(4pi-3sqrt(3))/4.`      (4.7)

Hence the diameter shell has measure `4V D^3 dD`. Put `t=Du`, so `dt=D du`, and define

`q(u)=alpha+beta u+pi u^2`.

Using (4.6) in (4.5), then integrating over `D`,

`C >= (1/6) int_0^infinity 4V D^3 int_0^infinity exp(-D^2 q(u)) D du dD`

`  = (V sqrt(pi)/4) int_0^infinity q(u)^(-5/2) du`,      (4.8)

because

`int_0^infinity D^4 exp(-qD^2) dD = 3sqrt(pi)/(8 q^(5/2)).`

Combining (4.2), (4.4), the vanishing endpoint terms, and (4.8) gives the fully explicit analytic lower bound

`liminf E[L_n]/n >= 5/8 + (V sqrt(pi)/8) int_0^infinity q(u)^(-5/2) du.`      (4.9)

### 4.5 Exact finite certificate for `>0.62906`

Only the last numerical comparison is delegated to a checker. No simulation is used.

The checker uses exact Python `Fraction` arithmetic and integer square roots. It bounds `pi` by the alternating Machin identity

`pi/4 = 4 arctan(1/5) - arctan(1/239)`,

constructs rational one-sided bounds for `sqrt(3)` and `sqrt(pi)`, and lower-bounds the integral in (4.8) by the right Riemann sum on `[0,10]` with step `1/100`. Since `q'(u)=beta+2pi u>0` for `u>=0`, `q(u)^(-5/2)` is decreasing, so this right sum is rigorously below the integral; the omitted tail is positive. Every square-root bound is proved by integer squaring, and every decimal grid is rounded in the safe direction.

Executed checker:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T06-49-00Z__p0257_closed_triple_exact.py`

created at commit `a0f9e65e26241079e4fe0c27d60d0a21cbb86789`.

Archived output:

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T06-49-00Z__p0257_closed_triple_exact.out`

created at commit `908c4d61810137b6278aa61897c5a43279e34e21`.

The executed output records

`I_LO_DECIMAL = 0.003171648792112180735027`

`C_LO_DECIMAL = 0.008135237979670476667658`

and the exact rational

`B_LO_EXACT = 15726690474745880958345733429927955202801271874129 / 25000000000000000000000000000000000000000000000000`,

with exact assertions

`B_LO_GT_0.62906 = True`,

`B_LO_GT_0.6289 = True`,

and terminal line

`ALL_EXACT_FINITE_CHECKS_PASS`.

This proves Theorem 4.1.

## 5. What this does and does not solve

This is real movement of the frozen source-relevant metric, but it does **not** prove Aldous's proposed law of large numbers or identify the constant `c`. The source remains OPEN and this track remains PARTIAL. If the source convergence `L_n/n -> c` is eventually proved, Aldous's deterministic linear bound supplies uniform integrability as already recorded in the claim, so the present theorem would imply `c >= B_cert`.

The proof is NUV-specific in the precise sense that the additional closed-triple term comes from forced greedy ordering, not merely from the fact that the path spans all points. The baseline `0.6289` from EMST is prior art; the increment above it is the new worker theorem. The bounded prior-art search did not locate this exact closed-two-nearest-triple inequality, but that does not establish novelty. Before any publication claim, the proof needs independent literature review and the required external audits.

I did **not** spend the run tightening the predecessor's guarded-pair certificate, and I will not spend the next run merely making the Riemann mesh finer. The mesh already certifies the movement; further checker precision without a stronger analytic route would violate the research-first rule.

## 6. Stagnation, audit state, and next route

Because the tracked quantity moved, the admitted P0257 unchanged-run counter resets from `1` to `0`. Stuck recoveries remain `0/2`. There is no stuck episode this run.

P26 audit: `NOT_REQUESTED / NOT_PRESUMED`.  
NM13-12 audit: `NOT_REQUESTED / NOT_PRESUMED`.

No closure is claimed. The theorem is audit-eligible as a quantitative milestone, but the parent source remains open.

Next Section-B methods, not yet tried on this P0257 route and therefore **not counted as attempted in this report**: **#5 ADD A PARAMETER AND DIFFERENTIATE, #14 FIND THE GROUP ACTING, #25 COUNT THE SAME THING TWICE.** The next mathematical step is to parameterize normalized triangle shape rather than collapse it to diameter alone, quotient by Euclidean similarity/symmetry, and derive a second exact count of the closed-triple correction. Continue only if that improves the certified endpoint beyond `B_cert` or feeds the source limit-existence question; otherwise abandon that local-cluster route rather than manufacture a denser certificate for the same bound.

## 7. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: NM13-11
  namespace: proofnet24/NM13-11/
  category: HARD_OUTSIDE
  source_id: P0257
  claim_path: operations/claims/P0257.md
  canonical_dedup_key: law_of_large_numbers_and_constants_for_nuv_lengths
  source_status: OPEN
  track_status_before: PARTIAL
  track_status_after: PARTIAL
  metric_name: b_NUV
  metric_definition: explicit certified endpoint in liminf E[L_n]/n >= b_NUV for the exact Euclidean NUV source model
  predecessor_carried_endpoint: ">= 0.6277"
  corrected_literature_endpoint_before_new_proof: ">= 0.6289"
  metric_after_exact: ">= 15726690474745880958345733429927955202801271874129/25000000000000000000000000000000000000000000000000"
  metric_after_short: "> 0.62906"
  mathematical_movement: true
  baseline_correction_is_worker_progress: false
  actual_section_B_methods:
    - 11
    - 20
    - 24
  method_outcomes:
    11: "SUCCESS: degree-incidence lower functional plus disjoint forced-triple slack."
    20: "SUCCESS: generic tour relaxations identified as forgetting NUV order; closed 2-nearest triples isolate the missing greedy constraint."
    24: "SUCCESS: diameter-extremal triangle area/perimeter bounds reduce the correction to an explicit one-dimensional integral."
  theorem_claim: "liminf E[L_n]/n >= B_cert > 0.62906"
  finite_checker: proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T06-49-00Z__p0257_closed_triple_exact.py
  checker_output: proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T06-49-00Z__p0257_closed_triple_exact.out
  checker_terminal: ALL_EXACT_FINITE_CHECKS_PASS
  unchanged_runs_before: 1
  unchanged_runs_after: 0
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
  hard_recovery_budget_remaining: 2
  p26_audit: NOT_REQUESTED_NOT_PRESUMED
  nm13_12_audit: NOT_REQUESTED_NOT_PRESUMED
  next_section_B_methods:
    - 5
    - 14
    - 25
  next_step: "Exploit normalized triangle-shape symmetry and a second counting formula to strengthen the analytic correction; do not spend a run only refining the existing Riemann mesh."
  prewrite_master: fe14e2db92625b3f6259dab1cdeb597b2e025595
  shared_roots_edited: false
  peer_namespaces_edited: false
  scheduler_modified: false
  email_or_drive_used: false
  public_posting: false
  paid_compute: false
```

## 8. Write discipline

This invocation created only the two substantive exact-certificate artifacts above and this one immutable own-namespace report. It did not edit `RESULTS.md`, `QUEUE.md`, `POSTED.md`, campaign roots, another worker's claim/report, permissions, workflows, schedules, email/Drive resources, or public surfaces. The report is to be read back at its creation commit; no receipt-only follow-up commit is authorized.
