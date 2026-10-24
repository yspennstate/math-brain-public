Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `U_T: 3/4 -> 3/4`; STUCK RECOVERY EPISODE #1 completed; actual Section-B methods tried: #1 CHANGE THE CATEGORY, #18 SAY IT IN ANOTHER LANGUAGE, #21 ASK WHO ELSE HAS THIS SHAPE.**

# NM13-12 — P0214 Section-I recovery #1: Poisson noise spectrum and a quantitative overlap gate

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-12` / `proofnet24/NM13-12/`  
Category: **HARD OUTSIDE**  
Canonical source / claim ID: **P0214**  
Canonical dedup key: `fluctuations_of_shortest_routes_in_poisson_proximity_networks`  
Exclusive shard: **11 mod 13**  
Status after this invocation: **PARTIAL / SOURCE OPEN / CLAIM RETAINED / STUCK-RECOVERY-1-CONSUMED**

## 1. Fixed source, metric, and outcome

The admitted source and frozen model are unchanged. P0214 is David Aldous's maintained problem *Shortest routes in random proximity networks*. This track fixes the unit-intensity planar Poisson-Delaunay triangulation, Euclidean edge lengths, and the bounded-local endpoint convention recorded in `operations/claims/P0214.md`.

The frozen metric remains

`U_T = best certified polynomial upper exponent for transversal deviation`,

where a value `a` is certified only by a complete source-valid proof that, for every `epsilon>0`, almost surely all sufficiently long relevant geodesics satisfy

`T_r <= r^(a+epsilon)`.

The recovered rigorous baseline and current track value remain

`U_T = 3/4`,

from Hirsch--Neuhaeuser--Schmidt's `3/4+epsilon` tube theorem for the Poisson-Delaunay model class. This invocation does **not** prove a smaller exponent.

Counters after this report:

- unchanged substantive runs after admission: **3 -> 4**;
- hard stuck-recovery episodes consumed: **0/2 -> 1/2**;
- source status: **OPEN**;
- track status: **PARTIAL**;
- P26 audit: **NOT REQUESTED / NOT PRESUMED**;
- NM13-13 secondary audit: **NOT REQUESTED / NOT PRESUMED**.

The previous invocation hit the three-unchanged-run trigger and explicitly required this run to be a Section-I thinking/recovery run. The selected recovery action was **port the technique from the nearest solved problem**, not another local-resampling lemma.

## 2. Runtime and scheduler-control truth

The requested `GPT-6 / maximum` line in the prompt is not an enforceable scheduler setting in the exposed task-control surface. This invocation identifies as **GPT-5.6 Sol**. The runtime exposes no authenticated reasoning-effort receipt, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, an hour-long execution, or a support escalation.

The exposed task-control interface continues to offer task title/prompt, schedule/start fields, timing mode, enabled state, listing, and update operations. It exposes **no bindable model-family field, no bindable reasoning-effort field, and no authenticated applied-model/applied-effort telemetry**. Making GPT-6/maximum binding would require an owner-authorized product/workspace/API/admin scheduling surface which persists those fields into inference routing and returns trustworthy per-run attestation.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary, not a mathematical state change. Current `RESULTS.md` records that a later full P26 update succeeded from another authorized context. The lawful workaround for a future denial is the owning or otherwise authorized account/workspace/API/admin context, or authorized platform support for the same existing task; it is not duplication, identity substitution, or permission bypass. No scheduler or permission was modified here.

## 3. Authoritative continuity and required repository reads

The controlling predecessor is

`proofnet24/NM13-12/runs/2026-09-19/2026-09-19T07-53-25Z__p0214-softmin-progress-typical-stuck-trigger.md`

created at commit

`38d0d6126880e0e025174deeb0a13e2d52376218`.

Its durable state was:

- P0214 admitted and exclusively owned by NM13-12;
- `U_T=3/4` unchanged for three substantive runs;
- methods already genuinely tried on P0214: #2/#6/#30, then #11/#20/#24, then #5/#12/#28;
- the local resampling/logarithmic-entropy route abandoned as exponent-stuck;
- exact zero-temperature block-gap and two-replica Gibbs identities derived but no near-zero route-gap anti-concentration at the source point;
- pointwise typical-block pivotality shown insufficient because the integrated route-visit budget remains order `r`;
- stuck trigger reached; recovery #1 mandated with methods #1/#18/#21 and action `port the technique from the nearest solved problem`.

Before substantive work this invocation freshly read or recovered:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the controlling predecessor report;
- current `operations/claims/P0214.md`;
- repository-wide P0214 canonical-key/title/attempt searches, including the F-intake dedup index and the carried Codex `attempted_unsolved` history;
- the newest visible neighboring NM13-11 report (`P0257` equilateral-envelope movement) and NM13-13 report (`P0083` whisker threshold movement).

The append-only intake and attempt corpora are too large to honestly claim that every unchanged historical byte was re-rendered in this one connector invocation. I make no such claim. Candidate-specific P0214 canonical identity, prior attempt state, current claim, source status, and ownership were reopened; the exact Git delta below contains no P0214 claim mutation and no source-selection-root mutation requiring a reset of continuity.

No private-repository history needed for this continuation was known to be inaccessible.

## 4. Exact predecessor-to-prewrite repository delta and ownership

A frozen prewrite master snapshot was captured at

`23651c21f9e2fdfb24f5e13aa5bf4e7a8f8bcb65`.

Exact comparison

`38d0d6126880e0e025174deeb0a13e2d52376218 .. 23651c21f9e2fdfb24f5e13aa5bf4e7a8f8bcb65`

reported:

- status: `ahead`;
- commits ahead: **108**;
- commits behind: **0**;
- total commits: **108**.

The returned changed-file material contains no `operations/claims/P0214.md` mutation. Direct current readback of `operations/claims/P0214.md` still says owner `NM13-12`, namespace `proofnet24/NM13-12/`, category HARD OUTSIDE, canonical residue 11, status CLAIMED. Repository-wide exact-key search still finds P0214 as this track's owned source rather than a competing assignment.

The currently read root/campaign exclusion surfaces do not mark P0214 posted, settled, retired, released, or reassigned. No ownership collision or owner-authorized handoff was recovered. Therefore the claim remains valid and this run continues P0214 rather than screening a successor.

## 5. Fresh source and bounded literature check — 2026-09-19

This is a bounded current-status check, not a proof of worldwide openness, novelty, or priority.

### 5.1 Original source

Aldous's maintained page

`https://www.stat.berkeley.edu/~aldous/Research/OP/random_proximity.html`

still says that, although a general SLLN for route length `D_r` is known, rigorous orders of magnitude for the transversal deviation `T_r` and `Var(D_r)` remain open. His index

`https://www.stat.berkeley.edu/~aldous/Research/OP/index.html`

still lists *Shortest routes in random proximity networks* among open research problems and separately warns that the site is updated haphazardly and may omit current work.

Focused 2025--2026 searches for Poisson-Delaunay shortest-route variance, transversal fluctuation exponents, and geodesic wandering did not recover a checked source-matching theorem with a transversal upper exponent below `3/4`. Recent Delaunay papers surfaced, including the September 2026 deterministic stretch-factor improvement, but not a solution of Aldous's stochastic fluctuation question. Negative search evidence is recorded only as bounded evidence.

### 5.2 Same-model coalescence prior art

David Coupier and Christian Hirsch, *Coalescence of Euclidean geodesics on the Poisson-Delaunay triangulation*, Bernoulli 24 (2018), DOI `10.3150/17-BEJ943`, proves almost-sure coalescence of any two semi-infinite geodesics with the same asymptotic direction by an adapted Burton--Keane argument plus passage-length concentration. It also proves that the expected number of semi-infinite geodesics leaving a disk is sublinear in the radius. The checked statement supplies qualitative/sublinear coalescence but no explicit power-law coalescence tail strong enough for the present metric.

### 5.3 Nearest solved quantitative overlap problem

Barbara Dembin, Dor Elboim and Ron Peled, *Coalescence of Geodesics and the BKS Midpoint Problem in Planar First-Passage Percolation*, GAFA 34 (2024), DOI `10.1007/s00039-024-00672-z`, studies planar iid edge-weight FPP. It proves power-law geodesic overlap/coalescence and quantitative midpoint/point-hit estimates. In particular the published article gives, under its limit-shape hypothesis, point-hit probability of order at most `log^2(D)/D^(1/16)` and a horizontal-family hit bound of order `log^2(n)/n^(1/24)`.

The proof of its central attractive-geodesic estimate explicitly depends on three ingredients: Talagrand concentration for iid edge weights, a Mermin--Wagner-style perturbation of the edge-passage-time product measure to force restricted-passage-time fluctuations, and Harris correlation for monotone events in independent variables. The paper explicitly uses the fact that weights off a conditioned path remain independent after conditioning on weights on the path.

### 5.4 Poisson-space analytic machinery

Günter Last and Mathew Penrose, *Poisson process Fock space representation, chaos expansion and covariance inequalities* (arXiv:0909.3205), gives the Wiener--Itô/Fock-space and Poisson difference-operator framework. Günter Last, Giovanni Peccati and Matthias Schulte, *Normal approximation on Poisson spaces: Mehler's formula, second order Poincare inequalities and stabilization* (PTRF 165 (2016), arXiv:1401.7568), gives an integrated Mehler formula representing the Poisson Ornstein--Uhlenbeck semigroup by thinning plus independent replenishment and emphasizes compatibility with stabilizing geometric functionals.

These papers supply a natural category in which the Delaunay environment still has independent primitive coordinates: the Poisson points, not the induced Delaunay edge weights.

## 6. Section-I stuck report

### (a) Exact blocking statement

For a finite-window, endpoint-regularized Poisson-Delaunay passage length `F_r=F_r(eta)` (large enough window that the source geodesic is captured on the stabilization-good event), let

`D_x F_r(eta) := F_r(eta + delta_x) - F_r(eta)`

and let `eta_t` be the stationary Poisson Ornstein--Uhlenbeck coupling obtained by retaining each point independently with probability `e^(-t)` and adding an independent Poisson process of intensity `1-e^(-t)`.

The quantitative statement now isolated as the first missing polynomial gate is

```text
(ND_{kappa,p})   There exist kappa>0, p>1, C<infinity such that,
for all sufficiently large r and all t>=0,

Integral_{R^2} E[ |D_x F_r(eta) D_x F_r(eta_t)| ] dx
    <= C r (1 + t r^kappa)^(-p).
```

This is **not proved**. It is the exact new blocker. It asks for polynomial decay, under Poisson noise, of the *integrated correlation of local passage influences*, rather than a pointwise pivotality estimate in one fixed environment.

Even `ND_{kappa,p}` alone would not yet close the source metric: the curvature transfer also needs a source-valid centering estimate and sufficiently high moments/tails, uniformly over the polynomial family of endpoint/junction locations. Those extra obligations are stated explicitly below rather than hidden in a multiscale step.

### (b) Routes tried and precise failure reason

1. **Legacy Codex Euclidean relation.** It controls transverse height by raw path-length excess. Failure: the Delaunay time constant is strictly larger than one, leaving a linear deterministic stretch term and no sublinear control.
2. **#2 counterexample/curvature route.** Polynomial-size Poisson voids are too rare, while the exact curvature lemma shows that passage error exponent `chi` yields at best wandering exponent `(1+chi)/2`. Failure: the available diffusive-scale passage error locks the architecture at `3/4`.
3. **#6 deformation to Howard--Newman / sublinear variance.** A logarithmic variance improvement such as `r/log r` changes only logs after curvature. Failure: no polynomial movement of `U_T`.
4. **#30 one-scale MD gate.** It isolated the exact passage-error exponent and summable endpoint union bound required. Failure: the needed polynomial passage-deviation bound was not proved.
5. **#11 shortest-path dual.** It rewrote route length as a Lipschitz-potential optimization. Failure: the dual alone gives no polynomial decorrelation of block influences.
6. **#20 shielded local resampling.** HNS stabilization plus deterministic Delaunay stretch gives a local repair bound proportional to the stabilization/cavity radius. Failure: no polynomial gain in the integrated influence budget.
7. **#24 extremal Delaunay flip.** An explicit near-cocircular four-point family shows a unit perturbation can change the route by order the cavity radius. This is a successful obstruction: deterministic `O(1)` block sensitivity is false, so that route was abandoned.
8. **#5 soft-min/gap susceptibility.** Exact finite-temperature and zero-temperature formulas reduce a block perturbation to near-zero route-gap anti-concentration. Failure: no source-valid anti-concentration at penalty `t=0` was obtained.
9. **#12 conserved Euclidean slack.** The exact prefix relation `h^2 <= L^2-r^2` was recovered. Failure: `mu_D>1` makes the unrenormalized slack linear; a quantitative Busemann/corrector subtraction is missing.
10. **#28 typical-block pivotality.** A pointwise power-law hit probability is not enough because the sum of hit probabilities is the expected number of route blocks, still order `r`. Failure: standard Efron--Stein energy remains linear; maximum-influence decay alone buys at most logarithms.
11. **Current #1/#18/#21 recovery.** The new Poisson-noise representation below converts the problem to an integrated *two-environment* overlap/noise-sensitivity estimate. Failure so far: `ND_{kappa,p}`, the high-moment lift, and centering are not yet proved.

### (c) What a successful proof must contain that no route yet contains

A metric-moving proof must contain **a global polynomial anti-pivotality mechanism**, not merely a smaller worst-case local constant. Concretely it must show that after Poisson thinning/replenishment at a noise level `t` of polynomial order `r^{-kappa}`, the passage influences in the original and noisy environments have already decorrelated enough that their *integrated correlation* is `o(r)` by a power. It must do this despite random Delaunay topology and rare large cavities.

Then it must lift the resulting `L^2` improvement to source-valid high moments or tails and control the deterministic centering error `|E F_r - mu_D r|` at the same polynomial scale. Only after those two independent obligations are displayed can the earlier curvature lemma be applied.

### (d) Simplest special case still unproved

The nearest same-model quantitative special case is:

```text
Find c,C>0 such that for two semi-infinite Poisson-Delaunay geodesics
with one fixed asymptotic direction and starting vertices at O(1) separation,

P( coalescence distance > R ) <= C R^(-c)

for all large R.
```

Coupier--Hirsch proves almost-sure finite coalescence and a sublinear mean density statement, but the bounded literature check did not recover this explicit polynomial tail. This is simpler than the noisy-environment gate because it keeps one environment and only asks for a rate on the already-known coalescence phenomenon.

### (e) Nearest solved problem and the ingredient it has that P0214 lacks

The nearest solved quantitative analogue is Dembin--Elboim--Peled 2024 on iid planar lattice FPP. Its power-law overlap proof has a fixed graph with independent edge weights. After conditioning on the weights of one candidate path, off-path weights remain independent, the relevant path event has a usable monotonicity, Harris correlation applies, and a coordinatewise Mermin--Wagner perturbation of the product edge-weight law creates a quantitative restricted-passage-time fluctuation.

Poisson-Delaunay Euclidean FPP lacks exactly that package. Edge lengths and adjacency are both induced by the same Poisson points; conditioning on a route does not leave a product family of off-route edge weights, point insertion/deletion can change topology across a random cavity, and the shortest-route event has no checked monotonicity under point addition suitable for the DEP Harris step. HNS stabilization controls how far a point perturbation propagates, but it does not replace DEP's quantitative product-measure fluctuation/correlation mechanism.

## 7. Method #1 — CHANGE THE CATEGORY: Poisson Ornstein--Uhlenbeck noise

The preceding block-resampling view treated local modifications as adversarial coordinates of a random graph. This recovery instead moves to the Poisson configuration itself and uses its canonical noise semigroup.

For a square-integrable finite-window Poisson functional `F`, write its Wiener--Itô chaos expansion

`F - E F = Sum_{n>=1} I_n(f_n)`.

The add-one difference has expansion

`D_x F = Sum_{n>=1} n I_{n-1}(f_n(x,.))`.

Let `P_t` be the Poisson Ornstein--Uhlenbeck semigroup, so that

`P_t I_n(f_n) = e^(-nt) I_n(f_n)`.

Then orthogonality of chaoses gives

`E Integral D_x F P_t(D_xF) dx
   = Sum_{n>=1} n n! e^{-(n-1)t} ||f_n||^2`.

Multiplying by `e^{-t}` and integrating over `t>=0` gives the exact identity

```text
Var(F)
 = Integral_0^infinity e^{-t}
     E Integral D_xF(eta) P_t(D_xF)(eta) dx dt
 = Integral_0^infinity e^{-t}
     Integral E[D_xF(eta) D_xF(eta_t)] dx dt.
```

Proof of the last equality: Mehler's formula realizes `P_t(D_xF)(eta)` as the conditional expectation of `D_xF(eta_t)` given `eta`; then take expectation. Proof of the first equality is the displayed chaos calculation, since

`Integral_0^infinity e^{-nt} dt = 1/n`.

This is a specialization/derivation of standard Poisson Fock-space and Mehler machinery, **not a novelty claim**. It is written out because it changes the research target in a useful way.

Outcome of method #1: **route advance, no metric movement.** The variance is not controlled by the raw `t=0` influence energy alone; it is the integral of influence correlation across noise scales. This creates room for a polynomial gain even when the one-environment Efron--Stein energy is order `r`.

## 8. Method #18 — SAY IT IN ANOTHER LANGUAGE: noise spectrum instead of pivotal blocks

Define the signed influence-correlation profile

`C_r(t) = Integral E[D_xF_r(eta) D_xF_r(eta_t)] dx`.

The exact identity above says

`Var(F_r) = Integral_0^infinity e^{-t} C_r(t) dt`.

Equivalently, in chaos language,

`e^{-t} C_r(t) = Sum_{n>=1} n n! e^{-nt} ||f_{r,n}||^2`.

Thus the missing polynomial improvement can be stated as a **noise-sensitivity / high-effective-chaos** property of the passage-length functional. The old pointwise-pivotal question asked whether any single block is rarely used. The new question asks how fast *the same local influence remains correlated after the primitive Poisson environment is slightly noised*.

This formulation gives a complete quantitative implication. If `ND_{kappa,p}` holds with `p>1`, then by the exact variance identity and absolute values,

```text
Var(F_r)
 <= Integral_0^infinity e^{-t} C r (1+t r^kappa)^(-p) dt
 <= C r^(1-kappa) Integral_0^infinity (1+s)^(-p) ds
 = C/(p-1) * r^(1-kappa).
```

So `ND_{kappa,p}` would produce a genuine polynomial variance exponent gain `delta=kappa`.

However, **variance alone does not move `U_T`**. To feed the earlier curvature lemma at the source quantifiers, one still needs, for every fixed small `epsilon>0`, sufficiently high centered moments or an exponential/stretched-exponential deviation estimate at passage scale

`r^((1-kappa)/2 + epsilon)`

plus a centering estimate of the same order, uniformly over the polynomial family of relevant endpoint/junction locations. With such a tail/centering lift, the curvature lemma would yield

`T_r <= r^( 3/4 - kappa/4 + O(epsilon) )`,

hence a certified `U_T <= 3/4-kappa/4` after the usual `epsilon` bookkeeping. No such lift is asserted here.

A useful low-frequency warning also emerges. If the passage functional carries an order-`r` first/low-chaos component, `C_r(t)` cannot decay on the required `r^{-kappa}` scale. The next proof attempt must therefore identify a geometric cancellation or coalescence mechanism which suppresses low-noise influence correlation; simply re-running Poincare/Efron--Stein cannot do it.

Outcome of method #18: **success as a reduction, no source-level exponent move.** The tracked quantity remains `3/4` because the new `ND` gate is unproved and because high-moment/centering obligations remain explicit.

## 9. Method #21 — ASK WHO ELSE HAS THIS SHAPE: audit the DEP overlap proof against Delaunay geometry

The quantitative shape closest to the desired gate is not another Delaunay stretch theorem; it is DEP's attractive-geodesic mechanism in iid planar FPP.

The published DEP proof was inspected at the load-bearing steps rather than cited only by abstract. Their Section 2.1 states that the attractive-geodesic estimate is built from:

1. a Talagrand upper deviation/concentration estimate for many subgeodesics;
2. a Mermin--Wagner-style coordinate perturbation of the product edge-weight distribution to force a lower-tail fluctuation for restricted passage time;
3. Harris correlation for monotone events in independent variables.

Their conditional Harris lemma explicitly uses that, after conditioning on the edge weights of a fixed path `p`, the off-path edge weights remain independent. Their perturbation lemma acts coordinatewise on `nu^n`.

This audit identifies the exact transfer failure for P0214:

- Delaunay edge lengths are not independent primitives;
- route conditioning reveals information about surrounding Poisson points and hence about many induced edges;
- a point resampling changes both weights and topology;
- the previous near-cocircular flip example proves that the deterministic effect can scale with cavity radius;
- there is no checked point-addition monotonicity matching DEP's Harris step.

The same-model Coupier--Hirsch theorem contributes the missing *qualitative* geometry: same-direction Delaunay rays do coalesce. Last--Penrose / Last--Peccati--Schulte contribute the missing *independent primitive noise*: Poisson thinning/replenishment. The proposed port is therefore a hybrid rather than a literal DEP copy:

```text
Poisson attractive-geodesic program:
  (i) use HNS stabilization to localize topology changes;
 (ii) obtain a polynomial same-direction coalescence rate (first special case);
(iii) upgrade to two-environment overlap under Poisson OU noise;
 (iv) convert overlap to decay of integrated add-one influence correlation;
  (v) use Poisson semigroup/moment machinery for passage tails;
 (vi) feed the already-proved curvature transfer.
```

No step (ii)--(v) is silently assumed. In particular, the currently checked Coupier--Hirsch result gives sublinearity/a.s. coalescence but no polynomial rate, and DEP's iid-edge Harris/Mermin--Wagner argument does not transplant automatically.

Outcome of method #21: **the nearest solved technique was ported down to its exact missing lemma; no metric movement.**

## 10. Recovery decision, route abandonment, and next invocation

This invocation executed the mandated recovery choice **port the technique from the nearest solved problem**. It produced a genuinely new source-valid analytic target `ND_{kappa,p}` and identified the precise product-structure obstruction in the nearest solved proof. It did not certify `U_T<3/4`.

The old standalone routes remain abandoned as metric routes:

- deterministic `O(1)` local block repair;
- logarithmic-only variance improvements;
- pointwise pivotality without integrated overlap;
- raw Euclidean-excess conservation without a corrector.

Hard recovery counter is now **1/2**. Because the metric still did not move, the next invocation must be **recovery episode #2**, not an ordinary lemma-accumulation run. The selected next recovery action is **prove the simplest unproved special case from Section 6(d)**: obtain a quantitative rate, or a rigorous no-go barrier, for same-direction Poisson-Delaunay coalescence before attempting the full noisy-environment gate.

Planned genuinely new Section-B methods for that recovery are:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY** — target a one-direction polynomial coalescence-tail statement before the full OU-noise overlap theorem;
- **#7 TAKE THE LIMIT** — work directly with the stationary semi-infinite directional geodesic forest where Coupier--Hirsch already proves qualitative coalescence;
- **#22 READ THE FAILURES, NOT THE SUCCESSES** — inspect exactly where the Burton--Keane/sublinearity proof loses quantitative rate and whether the loss is structural or only due to nonquantitative density/ergodic input.

If recovery #2 also fails to move `U_T` and the same source-level obligation remains, a third stuck-recovery episode is forbidden by the HARD policy: the subsequent invocation must preserve a full P0214 handoff and rotate to another eligible unclaimed source rather than produce another lemma on P0214.

## 11. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-12
  namespace: proofnet24/NM13-12/
  source_id: P0214
  claim_id: P0214
  canonical_dedup_key: fluctuations_of_shortest_routes_in_poisson_proximity_networks
  shard_mod_13: 11
  category: HARD_OUTSIDE
  source_status_before: OPEN
  source_status_after: OPEN
  track_status_before: PARTIAL_STUCK_TRIGGERED
  track_status_after: PARTIAL_STUCK_RECOVERY_1_CONSUMED
  metric_name: U_T
  metric_definition: best certified polynomial upper exponent for Poisson-Delaunay transversal deviation under frozen source quantifiers
  metric_before: 3/4
  metric_after: 3/4
  metric_movement: false
  unchanged_runs_after_admission_before: 3
  unchanged_runs_after_admission_after: 4
  stuck_recoveries_before: 0
  stuck_recoveries_after: 1
  stuck_recovery_limit: 2
  recovery_action: port_technique_from_nearest_solved_problem
  methods_actual:
    - 1_CHANGE_THE_CATEGORY
    - 18_SAY_IT_IN_ANOTHER_LANGUAGE
    - 21_ASK_WHO_ELSE_HAS_THIS_SHAPE
  method_outcomes:
    method_1: exact Poisson OU/Fock variance identity specialized to finite-window Delaunay passage functional; new integrated noise-correlation target
    method_18: ND_kappa_p implies Var(F_r)=O(r^(1-kappa)); high-moment and centering lift explicitly still missing
    method_21: DEP attractive-geodesic proof audited; iid product/Harris/Mermin-Wagner mechanism isolated as exact nonportable ingredient; Poisson hybrid port specified
  exact_blocker: ND_kappa_p integrated add-one influence correlation decay
  simplest_unproved_special_case: polynomial tail for coalescence distance of two O(1)-separated same-direction Poisson-Delaunay semi-infinite geodesics
  nearest_solved_problem: Dembin-Elboim-Peled 2024 planar iid FPP quantitative geodesic overlap
  same_model_prior_art: Coupier-Hirsch 2018 qualitative Poisson-Delaunay coalescence and sublinear geodesic density
  p26_audit: NOT_REQUESTED_NOT_PRESUMED
  nm13_13_audit: NOT_REQUESTED_NOT_PRESUMED
  next_recovery: 2_of_2_if_no_metric_move
  next_action: prove_simplest_unproved_special_case
  next_methods:
    - 4_PROVE_SOMETHING_WEAKER_COMPLETELY
    - 7_TAKE_THE_LIMIT
    - 22_READ_THE_FAILURES_NOT_THE_SUCCESSES
  predecessor_report_commit: 38d0d6126880e0e025174deeb0a13e2d52376218
  frozen_prewrite_master: 23651c21f9e2fdfb24f5e13aa5bf4e7a8f8bcb65
  compare_ahead_by: 108
  compare_behind_by: 0
  claim_retained: true
  shared_root_edits: false
  peer_file_edits: false
  scheduler_edits: false
  workflow_execution: false
  public_posting: false
  email_or_drive: false
  paid_compute: false
```

## 12. Operational safeguards and claim scope

No finite asymptotic exponent claim was promoted from computation. No checker was manufactured merely to document nonmovement. The Poisson OU variance identity is a standard prior-art identity specialized and proved on the page; it is not labeled as a new theorem. `ND_{kappa,p}` is explicitly an **unproved gate**, not a result.

No shared root ledger, peer namespace, existing claim, workflow, permission, public surface, email/Drive resource, paid-compute resource, or schedule was modified. No task was duplicated to bypass authorization. Exactly one immutable report is written by this invocation in the NM13-12 `runs/` namespace and is to be read back at its creation commit.
