Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `U_T: 3/4 -> 3/4`; STUCK RECOVERY EPISODE #2 completed; actual Section-B methods tried: #4 PROVE SOMETHING WEAKER, COMPLETELY, #7 TAKE THE LIMIT, #22 READ THE FAILURES, NOT THE SUCCESSES.**

# NM13-12 — P0214 Section-I recovery #2: quantitative cavity localization and the surviving coalescence-rate barrier

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-12` / `proofnet24/NM13-12/`  
Category: **HARD OUTSIDE**  
Canonical source / claim ID: **P0214**  
Canonical dedup key: `fluctuations_of_shortest_routes_in_poisson_proximity_networks`  
Exclusive shard: **11 mod 13**  
Status after this invocation: **PARTIAL / SOURCE OPEN / CLAIM RETAINED / STUCK-RECOVERY-2-CONSUMED / HANDOFF-AND-ROTATION REQUIRED BEFORE ANY THIRD RECOVERY**

## 1. Fixed target, metric, and honest outcome

The admitted source, process, and metric are unchanged.

- Source: David Aldous, maintained problem *Shortest routes in random proximity networks*.
- Frozen process: the unit-intensity planar Poisson--Delaunay triangulation, Euclidean edge lengths, Euclidean shortest paths, with the bounded-local endpoint convention in `operations/claims/P0214.md`.
- Frozen metric:

  `U_T = best certified polynomial upper exponent for transversal deviation`,

  where `a` is certified only by a complete source-valid proof that for every `epsilon>0`, almost surely all sufficiently long relevant geodesics satisfy

  `T_r <= r^(a+epsilon)`.

The recovered baseline and current value remain

`U_T = 3/4`,

from Hirsch--Neuhaeuser--Schmidt's `3/4+epsilon` transversal tube theorem for the Poisson--Delaunay model class. This invocation proves no smaller exponent.

Counters after this report:

- unchanged substantive runs after admission: **4 -> 5**;
- HARD stuck-recovery episodes consumed: **1/2 -> 2/2**;
- source status: **OPEN**;
- track status: **PARTIAL**;
- P26 audit: **NOT REQUESTED / NOT PRESUMED**;
- NM13-13 secondary audit: **NOT REQUESTED / NOT PRESUMED**.

The previous report mandated recovery #2 on the simplest same-model quantitative special case: obtain a polynomial tail for coalescence distance of two `O(1)`-separated semi-infinite Poisson--Delaunay geodesics with the same fixed asymptotic direction. I did not prove that tail. I did prove, completely, that the large-cavity / long-local-edge part of the obstruction has a Gaussian-in-scale Poisson tail, so the remaining obstruction is genuinely global directional geodesic competition rather than rare huge local Delaunay cells.

Because this is the second permitted HARD recovery and the source-level metric has still not moved, **the next NM13-12 invocation may not perform recovery #3 on P0214**. It must preserve this report as handoff state and rotate to a different eligible unclaimed source under the residue-11 admission protocol. This report does not release the canonical claim in-place; no shared claim file is overwritten in this invocation.

## 2. Runtime and task-control truth

The prompt requests GPT-6 with maximum reasoning, but the exposed scheduler/task interface still has no bindable model-family selector, no reasoning-effort selector, and no authenticated per-run applied-model/applied-effort receipt. This invocation identifies as **GPT-5.6 Sol**; reasoning effort is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, an hour-long execution, or a support escalation.

The currently exposed task-control surface offers task title/prompt, schedule/start fields, timing mode, enabled state, list, and update operations. It does not expose model or reasoning fields. Making GPT-6/maximum binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists those fields into inference routing and returns authenticated run telemetry.

The historical P26 response `You cannot modify this task` remains an authorization-context issue. Current `RESULTS.md` records that a later P26 update succeeded from another authorized context. The lawful workaround for a future denial is the owning or otherwise authorized account/workspace/API/admin context, or authorized platform support for the same existing task; it is not task duplication, identity substitution, or permission bypass. No scheduler or permission was modified here.

## 3. Authoritative continuity and repository reads

The controlling predecessor is

`proofnet24/NM13-12/runs/2026-09-19/2026-09-19T09-00-30Z__p0214-recovery1-poisson-noise-overlap-gate.md`

at creation commit

`62982d2eba895dc6bb9f2509699064f3ad0fa7e8`.

Its durable state was:

- P0214 admitted and exclusively owned by NM13-12;
- `U_T=3/4` after four unchanged substantive runs;
- one HARD recovery consumed;
- methods already genuinely tried on P0214: `#2/#6/#30`, `#11/#20/#24`, `#5/#12/#28`, then recovery #1 `#1/#18/#21`;
- local deterministic resampling repair and purely logarithmic entropy routes abandoned as exponent-stuck;
- exact soft-min / route-gap formulas obtained, but no source-point anti-concentration;
- Poisson Ornstein--Uhlenbeck variance representation derived;
- polynomial noise-decorrelation gate `ND_{kappa,p}` isolated but not proved;
- recovery #2 explicitly assigned methods `#4/#7/#22` and the same-direction coalescence-tail special case.

Before substantive work this invocation freshly read or recovered:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the controlling predecessor report;
- current `operations/claims/P0214.md`;
- repository-wide exact P0214 key/title/attempt hits, including the canonical F-intake dedup key and carried Codex `attempted_unsolved` status;
- newest recovered neighboring reports `proofnet24/NM13-11/runs/2026-09-19/2026-09-19T08-58-00Z__p0257-asymmetric-core-movement.md` and `proofnet24/NM13-13/runs/2026-09-19/2026-09-19T09-09-11Z__p0083-whisker6-to2-conservation-depth.md`.

The append-only intake and attempt corpora are too large to claim that every unchanged historical byte was re-rendered model-visible. I make no such claim. P0214's source, canonical identity, prior attempt, ownership, and newest own continuity were reopened directly; the complete Git delta below contains no P0214 claim mutation and no mutation of the admission-critical root ledgers.

No private-repository history required for this continuation was known to be inaccessible.

## 4. Exact predecessor-to-prewrite Git delta and ownership

Frozen prewrite `master` head:

`13b623132250e526bf18294cef8b502ea145d30f`.

Exact comparison

`62982d2eba895dc6bb9f2509699064f3ad0fa7e8 .. 13b623132250e526bf18294cef8b502ea145d30f`

reports:

- status: `ahead`;
- commits ahead: **98**;
- commits behind: **0**;
- total commits: **98**;
- `too_large = null`, so the returned changed-file set is complete.

The complete delta contains no `operations/claims/P0214.md` mutation and no mutation of root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, screened `probability_1000_intake_*/problems.jsonl`, or P0214 attempt/source ledger. The only canonical claim additions in the returned interval are unrelated (`G0004` and `P0342`).

A fresh direct read of `operations/claims/P0214.md` still records owner NM13-12, namespace `proofnet24/NM13-12/`, category HARD OUTSIDE, canonical key `fluctuations_of_shortest_routes_in_poisson_proximity_networks`, SHA-256 `7707fc4888eade0e22136663abfefe5b2eddf2d482cc0bba1a943a3dcac811ff`, residue 11, status CLAIMED. No release, handoff by another owner, retirement, alias collision, or duplicate ownership was recovered. The claim therefore remains valid for this second recovery.

## 5. Fresh source and bounded literature check — 2026-09-19

This is a bounded current-status check, not a proof of worldwide openness, novelty, or priority.

### 5.1 Original source

Aldous's maintained page

`https://www.stat.berkeley.edu/~aldous/Research/OP/random_proximity.html`

still defines shortest within-network route length `D_r` and transversal deviation `T_r`, notes the general SLLN for `D_r`, and states that rigorous study of the orders of `T_r` and `Var(D_r)` remains an open problem. His maintained open-problem index still lists *Shortest routes in random proximity networks* and warns elsewhere that the collection is updated haphazardly.

Focused 2025--2026 searches for Poisson--Delaunay shortest-path transversal exponents, geodesic coalescence rates, and quantitative same-direction coalescence did not recover a checked theorem giving a Poisson--Delaunay polynomial coalescence tail or a transversal exponent below `3/4`. Recent Poisson--Delaunay work found in the search concerns tessellation limits and geometric approximation, not the source fluctuation order. Negative search evidence is recorded only as bounded evidence.

### 5.2 Same-model qualitative coalescence

David Coupier and Christian Hirsch, *Coalescence of Euclidean geodesics on the Poisson-Delaunay triangulation*, Bernoulli 24 (2018), 2721--2751, DOI `10.3150/17-BEJ943`, proves almost-sure coalescence of any two semi-infinite geodesics with the same asymptotic direction and sublinear expected growth of the number of semi-infinite branches leaving a large disk. The checked abstract/source statement is qualitative/sublinear, not a polynomial coalescence-rate theorem.

I also inspected the paper's Section 4 through indexed PDF text extraction. Its local radial-tree-to-directed-forest comparison and its no-bi-infinite-geodesic/dominated-convergence step end in qualitative `o(1)` limits; the proof separately controls rare long Delaunay edges by Poisson void events. The PDF screenshot renderer returned a cache/fetch failure in this invocation, so no visual-only PDF detail is treated as evidence. The theorem below is self-contained and does not depend on trusting an unviewed diagram or numerical PDF table.

### 5.3 Quantitative comparison models

Two solved comparison regimes sharpen what is missing here.

1. Basu--Sarkar--Sly, *Coalescence of Geodesics in Exactly Solvable Models of Last Passage Percolation* (J. Math. Phys. 60 (2019)), proves polynomial upper tails for coalescence and, for the semi-infinite exponential-LPP problem at the KPZ separation scale, the optimal `R^(-2/3)` coalescence tail. The proof has exact-solvable / stationary structure unavailable in Poisson--Delaunay FPP.
2. Dembin--Elboim--Peled, *Coalescence of Geodesics and the BKS Midpoint Problem in Planar First-Passage Percolation* (GAFA 34 (2024)), proves power-law geodesic overlap and point-hit bounds for iid planar lattice FPP under its hypotheses. Their quantitative mechanism works with independent primitive edge weights and product-measure concentration/perturbation tools. In Poisson--Delaunay, edge lengths and even adjacency are induced jointly by the same Poisson point configuration.

These are technique comparisons, not evidence that the Delaunay source already has the same rate.

## 6. Section-I exact blocker after recovery #1

The recovery target inherited from the preceding report is the following source-valid special case.

Fix a deterministic direction `u`. Start two almost-surely unique semi-infinite Poisson--Delaunay geodesics with asymptotic direction `u` from vertices selected in two bounded sets at `O(1)` mutual separation. Let `R_coal` be a Euclidean distance by which they have coalesced. The desired quantitative statement is

```text
(COAL_c)  There exist c,C>0 such that
          P(R_coal > R) <= C R^(-c)
          for all sufficiently large R.
```

This invocation does **not** prove `(COAL_c)`.

The main new information is that one large class of possible obstructions to `(COAL_c)` is quantitatively negligible: exceptionally large local Delaunay empty circles and the long edges they create have a Gaussian-in-radius Poisson tail. Therefore a proof of `(COAL_c)` cannot be replaced by another cavity-tail estimate; it needs a global mechanism making two directional optimizers merge.

## 7. Method #4 — PROVE SOMETHING WEAKER, COMPLETELY: a self-contained Poisson--Delaunay cavity-tail theorem

The first recovery move was to prove a complete quantitative statement that removes rare huge local Delaunay cells from the list of plausible polynomial bottlenecks.

### Proposition 7.1 — local Delaunay circumradius tail

Let `eta` be a unit-intensity planar Poisson point process and `Del(eta)` its Delaunay triangulation. Let `Q` be any unit square. There exist universal constants `C,c>0` such that for all `s>=2`,

```text
P( there exists a Delaunay triangle tau with a vertex in Q
   and circumradius rho(tau) >= s ) <= C exp(-c s^2).
```

One may take a non-optimized `c = 225*pi/256` after enlarging `C`.

#### Proof

Translate coordinates so `Q` lies inside the unit disk about the origin. Work on the probability-one general-position event for the Poisson process, so every Delaunay face is a triangle and its open circumdisk contains no Poisson points.

Split by dyadic circumradius. For `k>=0` put

`S = 2^k s`

and let `E_k` be the event that there is a Delaunay triangle `tau` with a vertex `x in Q` and

`S <= rho(tau) < 2S`.

Let `z` be its circumcenter. Because `|x|<=1` and `|z-x|=rho(tau)<2S`,

`|z| <= 1+2S <= 3S`

for `S>=2`.

Consider the deterministic square grid of mesh `S/16` covering `[-3S,3S]^2`. It contains fewer than `10000` grid points. Choose a grid point `g` nearest to `z`. Then

`|g-z| <= sqrt(2) S/32 < S/16`.

Since `rho(tau)>=S`, the deterministic disk

`B(g,15S/16)`

lies strictly inside the empty circumdisk `B(z,rho(tau))`. Hence `B(g,15S/16)` contains no Poisson point. For each fixed grid point, the unit-intensity Poisson void probability is

`exp( -pi (15S/16)^2 ) = exp( -225*pi*S^2/256 )`.

A union bound over the fewer than `10000` grid points gives

`P(E_k) <= 10000 exp( -225*pi*4^k*s^2/256 )`.

Summing in `k` gives

`P(union_k E_k) <= C exp(-c s^2)`

with universal `C` and `c=225*pi/256` after increasing `C`. This proves the proposition.  QED.

### Corollary 7.2 — logarithmic-radius localization in polynomial windows

For every `M>0` there is `A_M<infinity` such that, for all large `R`, with probability at least `1-O(R^(-M))`, every Delaunay triangle having a vertex in `B_R(0)` has circumradius at most

`A_M sqrt(log R)`.

Indeed, cover `B_R` by `O(R^2)` unit squares and apply Proposition 7.1 with `s=A sqrt(log R)`. The union failure probability is

`O( R^2 exp(-c A^2 log R) ) = O( R^(2-cA^2) )`,

and choosing `A` sufficiently large gives any prescribed polynomial power. On the same event every Delaunay edge with an endpoint in `B_R` has length at most `2 A_M sqrt(log R)`, since a Delaunay edge is a chord of an adjacent Delaunay circumcircle.

### What this does and does not prove

This is a complete theorem-sized argument on the page. No finite arithmetic core is being asserted, so no checker is warranted. The empty-circle mechanism is standard stochastic-geometry folklore; I do **not** claim novelty for that mechanism or for the existence of exponential/Gaussian local stabilization tails in Poisson--Delaunay geometry. The useful point for this track is the explicit consequence for route selection:

> on every polynomial-size region relevant to a putative coalescence estimate, huge local Delaunay circumcircles can be truncated at `O(sqrt(log R))` at super-polynomially small cost.

Thus the order-cavity-radius deterministic flip obstruction from the second P0214 run is a real worst-case obstruction but not, by itself, the source of a polynomial coalescence tail in the Poisson environment.

Outcome of Method #4: **SUCCESS AS A COMPLETE WEAKER THEOREM; NO `U_T` MOVEMENT.**

## 8. Method #7 — TAKE THE LIMIT: intensity is a fake deformation parameter, and the real infinity limit has no modulus

I tried two limit routes.

### 8.1 Poisson intensity does not produce a new perturbative regime

Let `eta_lambda` be a planar Poisson process of intensity `lambda`. Under the deterministic scaling

`S_lambda(x) = sqrt(lambda) x`,

`S_lambda eta_lambda` is a unit-intensity Poisson process. Delaunay adjacency is covariant under Euclidean similarities, and Euclidean edge/path lengths and transverse distances scale by the same factor. Therefore changing Poisson intensity is exactly spatial rescaling of the same random metric. In dimensionless variables, a high-intensity limit is merely the large-distance limit already present in P0214 (with endpoint windows scaled accordingly).

So `lambda -> infinity` or `lambda -> 0` is **not** a solvable interpolation point from which to perturb back. I abandon intensity as a deformation parameter for this target.

### 8.2 The directed-forest limit isolates, rather than removes, the missing rate

Coupier--Hirsch's same-model proof compares the radial shortest-path tree viewed near a point escaping to infinity with a directed forest of semi-infinite geodesics. Qualitatively, the local laws converge; then coalescence / absence of a bi-infinite geodesic makes the relevant branch-crossing probability tend to zero.

For a quantitative version, one needs a modulus for two separate limits:

1. a rate for local radial-tree `->` directed-forest approximation; and
2. a rate at which the directed forest loses distinct ancestral lines, equivalently a quantitative one-endedness/coalescence estimate.

Proposition 7.1 makes the first problem easier only in one respect: local very-large-circumcircle errors are already super-polynomially small after `sqrt(log R)` truncation. It does not provide either directional-geodesic cone convergence or a merging hazard.

The second limit remains the exact blocker. A useful finite-window formulation is

```text
A(R) = P( two fixed-direction semi-infinite geodesics started O(1) apart
          are still disjoint when they first exit B_R ).
```

Coupier--Hirsch proves `A(R) -> 0` qualitatively through coalescence. What this track needs is a modulus such as `A(R) <= C R^(-c)`.

Outcome of Method #7: **NEGATIVE BUT DECISIVE.** Intensity scaling is tautological; taking the geometric infinity limit exposes the missing quantitative one-endedness modulus rather than generating it.

## 9. Method #22 — READ THE FAILURES, NOT THE SUCCESSES: the easy errors are already small; global merging is the missing ingredient

The same-model and comparison proofs explain why another local estimate is unlikely to move the metric.

### 9.1 What the Poisson--Delaunay coalescence proof does not quantify

The Coupier--Hirsch argument succeeds qualitatively despite the fact that ordinary local-modification arguments are awkward for Delaunay geometry: deleting or adding points changes both edge lengths and graph topology, and the graph can reconnect around the modified region. The proof uses concentration and a directed-forest limit, then excludes persistent multiple ancestral lines / bi-infinite geodesics by stationarity and Burton--Keane-type reasoning.

The rate disappears exactly at the global step: stationarity plus no bi-infinite geodesic gives convergence to zero but supplies no polynomial modulus. Proposition 7.1 shows that this is not because the proof forgot to optimize a Poisson void estimate. The rare-cavity terms can already be made smaller than any power on polynomial windows.

### 9.2 Why a slab-by-slab renewal attempt fails

After truncating local circumradii at `O(sqrt(log R))`, it is tempting to divide a long directional corridor into slabs and ask for a positive conditional probability that two geodesics merge in each slab. This would give a renewal tail.

The missing statement is precisely the conditioning problem: geodesicity is a global optimization event. Conditioning on the incoming geodesic history biases the Poisson configuration in the future through the requirement that no alternative shorter route exists, and no uniform finite-energy local event was found that forces two globally optimal routes to merge while preserving the Delaunay structure. A local `funnel` can be bypassed outside the modified box unless one already has transverse confinement of the kind P0214 is trying to prove. Thus the naive regeneration argument is circular.

### 9.3 What the nearest solved models have that this one lacks

- In exactly solvable exponential last-passage percolation, Basu--Sarkar--Sly obtain polynomial and optimal `R^(-2/3)` semi-infinite coalescence tails using integrable/stationary structure unavailable here.
- In generic iid planar lattice FPP, Dembin--Elboim--Peled obtain quantitative overlap and point-hit power laws using independent primitive edge weights, concentration, perturbation, and monotonicity/correlation tools. Poisson--Delaunay has independent primitive **points**, but the shortest-path edge weights and the adjacency relation are nonlinear functions of the same points.

The port therefore needs a new object at the Poisson-point level: for example a Busemann/corrector gap with quantitative anti-concentration, or a Poisson-noise two-replica overlap inequality strong enough to turn the qualitative one-endedness statement into a power law. Recovery #1's `ND_{kappa,p}` is exactly one analytic form such a mechanism could take; it remains unproved.

Outcome of Method #22: **SUCCESS IN LOCATING THE FAILURE; NO SOURCE METRIC MOVEMENT.** The rate loss is global coalescence/competition, not a missing local cavity bound.

## 10. Section-I stuck report after the second and final permitted recovery

### (a) Exact statement that blocks

The simplest same-model blocker remains

```text
There exist c,C>0 such that
P(R_coal > R) <= C R^(-c)
```

for two `O(1)`-separated semi-infinite Poisson--Delaunay geodesics with a common deterministic asymptotic direction.

A slightly more localized version, now equivalent up to a super-polynomial error for route-selection purposes, is to prove the same inequality on the high-probability event that every Delaunay triangle touching `B_{2R}` has circumradius at most `A sqrt(log R)`.

### (b) Routes tried and precise reasons they failed

1. Legacy deterministic Euclidean excess: linear deterministic Delaunay stretch destroys sublinear wandering information.
2. #2 counterexample/curvature: diffusive passage error implies at best exponent `3/4` through quadratic curvature.
3. #6 deformation to sublinear variance: logarithmic variance improvement changes only logarithms, not `U_T`.
4. #30 one-scale passage gate: exact polynomial passage error needed, not proved.
5. #11 shortest-path dual: no polynomial decorrelation follows from the dual alone.
6. #20 local resampling repair: sensitivity is proportional to random cavity radius; no polynomial integrated-energy gain.
7. #24 extremal flip: unit perturbation can cause order-cavity route change; deterministic `O(1)` sensitivity is false.
8. #5 soft-min gap: exact susceptibility formula, but no source-point route-gap anti-concentration.
9. #12 Euclidean slack invariant: `mu_D>1` leaves linear deterministic slack; quantitative corrector is missing.
10. #28 pointwise typical pivotality: summing visits still gives order-`r` influence energy.
11. Recovery #1 #1/#18/#21: Poisson OU/noise representation isolates `ND_{kappa,p}`, but the polynomial two-environment overlap bound, centering, and high-moment lift remain missing.
12. Recovery #2 #4: local circumradius / long-edge tails are now completely controlled by `exp(-c s^2)`; this removes an easy obstruction but does not make global geodesics merge.
13. Recovery #2 #7: intensity scaling is exactly spatial scaling; the directed-forest infinity limit is qualitative without a coalescence modulus.
14. Recovery #2 #22: comparison proofs require either integrable stationary structure or product-edge perturbation/monotonicity that has no direct Delaunay analogue.

### (c) What a successful proof would have to contain that no route so far contains

At least one genuinely global polynomial mechanism, for example:

- a quantitative Busemann/corrector construction giving a polynomial anti-concentration bound for competing directional routes;
- a regeneration theorem with a **uniform conditional** merging probability after conditioning on the geodesic past, avoiding the circular use of transverse confinement;
- or a Poisson-space two-replica/noise-sensitivity inequality strong enough to prove `ND_{kappa,p}` or directly give a polynomial coalescence tail.

Local empty-circle, long-edge, and stabilization-style truncations alone are insufficient: those errors are already super-polynomially small on the relevant windows.

### (d) Simplest special case still unproved

For a fixed direction `u`, take two starting vertices selected from two adjacent unit boxes near the origin. Prove that, on the event that all Delaunay circumradii touching `B_{2R}` are at most `A sqrt(log R)`, the two `u`-directed semi-infinite geodesics coalesce before leaving `B_R` with probability at least `1-C R^(-c)`.

Even this truncated finite-scale statement is unproved.

### (e) Nearest solved problem and what its proof has that this problem lacks

The sharpest solved coalescence analogue is exponential directed last-passage percolation, where Basu--Sarkar--Sly prove polynomial/optimal coalescence tails using exactly solvable stationary structure. The more robust analogue is Dembin--Elboim--Peled's iid planar FPP, which proves power-law overlap/point-hit bounds using product edge weights plus concentration/perturbation/correlation machinery. Poisson--Delaunay lacks both the integrable stationary description and independent primitive edge weights; its primitive independent variables are points that jointly determine weights and topology.

## 11. Route verdict and mandatory next action

The tracked quantity did not move:

`U_T: 3/4 -> 3/4`.

The run did produce a complete source-valid local-cavity theorem and a sharper diagnosis of the obstruction, but under the owner policy that is not metric movement. This was the **second and final permitted stuck-recovery episode** for this HARD source.

Therefore:

- **P0214 substantive research must stop after this report unless a later owner-authorized reassignment explicitly reopens it with a fresh route.**
- The next NM13-12 invocation must preserve this report as the P0214 handoff and rotate to another eligible unclaimed canonical residue-11 source.
- It must rerun source/current-literature/prior-attempt/ownership checks before any successor claim.
- A pending lead is still not READY.
- It must not count successor screening as mathematical progress.
- No third P0214 recovery is permitted.

I do not silently change the metric, and I do not transfer the `3/4` baseline to a future source.

## 12. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  worker: NM13-12
  namespace: proofnet24/NM13-12/
  category: HARD_OUTSIDE
  source_id: P0214
  claim_id: P0214
  canonical_dedup_key: fluctuations_of_shortest_routes_in_poisson_proximity_networks
  shard_mod_13: 11
  source_status: OPEN
  track_status: PARTIAL
  claim_state: RETAINED_FOR_THIS_REPORT_HANDOFF_REQUIRED_NEXT
  metric_name: U_T_best_certified_transversal_upper_exponent
  metric_before: "3/4"
  metric_after: "3/4"
  metric_movement: false
  actual_methods:
    - 4_PROVE_SOMETHING_WEAKER_COMPLETELY
    - 7_TAKE_THE_LIMIT
    - 22_READ_THE_FAILURES_NOT_THE_SUCCESSES
  method_outcomes:
    B4: "proved complete Gaussian-in-radius local Delaunay circumradius tail and polynomial-window sqrt(log R) localization; no U_T movement"
    B7: "proved intensity deformation is exact spatial rescaling; infinity/direct-forest limit still lacks quantitative coalescence modulus"
    B22: "isolated global directional merging as the rate-losing step; local cavity errors already super-polynomial"
  unchanged_substantive_runs_after_admission: 5
  hard_stuck_recoveries_consumed: "2/2"
  p26_audit: NOT_REQUESTED_NOT_PRESUMED
  secondary_audit_nm13_13: NOT_REQUESTED_NOT_PRESUMED
  new_complete_claims:
    - "local Delaunay circumradius tail P(rho>=s for a face touching a unit square) <= C exp(-c s^2)"
    - "for every M, all Delaunay circumradii touching B_R are O_M(sqrt(log R)) with failure O(R^-M)"
  source_level_blocker: "polynomial same-direction coalescence tail / quantitative one-endedness, or an equivalent Poisson-noise overlap mechanism"
  next_step: "MANDATORY HANDOFF AND ROTATION; screen a new eligible unclaimed residue-11 source before any further mathematics; no P0214 recovery #3"
  literature_check_date: 2026-09-19
  literature_scope: "Aldous live source; Poisson-Delaunay coalescence; 2025-2026 quantitative coalescence/transversal searches; solved iid-FPP and exactly-solvable-LPP comparisons"
  literature_limit: "bounded negative evidence only; no worldwide-openness or novelty certificate"
  prewrite_master: 13b623132250e526bf18294cef8b502ea145d30f
  predecessor_commit: 62982d2eba895dc6bb9f2509699064f3ad0fa7e8
  predecessor_to_prewrite_ahead: 98
  predecessor_to_prewrite_behind: 0
```

## 13. Delivery boundary

This invocation creates exactly this one immutable report under the NM13-12 `runs/` namespace. No new checker is manufactured because the mathematical content is a written theorem, not a finite certificate. No shared `RESULTS.md`, `QUEUE.md`, `POSTED.md`, campaign ledger, claim file, peer immutable file, workflow, permission, public post, email/Gmail item, Drive item, paid-compute resource, or scheduler is edited.
