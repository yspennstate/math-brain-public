Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `U_T: 3/4 -> 3/4`; actual Section-B methods tried this run: #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #12 FIND WHAT IS CONSERVED, #28 REPLACE "FOR ALL" WITH "FOR TYPICAL".**

# NM13-12 — P0214 third substantive run: soft-min susceptibility, longitudinal slack, and typical-block no-go

Date: 2026-09-19 UTC
Track: `NM13-12`
Namespace: `proofnet24/NM13-12/`
Category: HARD OUTSIDE
Canonical source/claim ID: `P0214`
Canonical dedup key: `fluctuations_of_shortest_routes_in_poisson_proximity_networks`
Exclusive shard: `11 mod 13`
Status: **PARTIAL / OPEN**

## 0. Executive result

The frozen source process remains the unit-intensity planar Poisson-Delaunay triangulation with Euclidean edge lengths and bounded-local endpoint localization. The frozen metric remains

`U_T = best certified polynomial upper exponent for transversal deviation T_r`

under the quantifier: for every `epsilon>0`, almost surely all sufficiently long relevant geodesics satisfy `T_r <= r^(U_T+epsilon)`.

**Before:** `U_T = 3/4`.

**After:** `U_T = 3/4`.

There is no metric movement. This is the **third consecutive substantive run after admission with no movement**, so P0214 is now **STUCK_TRIGGERED** under the owner rule. This run is not retroactively labelled a recovery. Recovery count remains `0/2`. The **next** invocation must be Section-I thinking/recovery episode #1, with no ordinary lemma-chaining.

The main mathematical gain is diagnostic rather than metric movement:

1. A finite-temperature block-penalty deformation gives an exact two-replica identity: the Hessian of the soft minimum is the Gibbs covariance of block occupation, and the summed diagonal curvature is exactly proportional to the expected symmetric difference of the blocks visited by two Gibbs routes.
2. The zero-temperature one-block deformation has an exact route-gap threshold. Therefore a source-point soft-min argument needs quantitative anti-concentration for the avoid-versus-visit route gap near zero; continuity/no-ties alone is not enough.
3. The natural longitudinal-progress invariant collapses to the already-preserved deterministic Euclidean excess-length relation. Because the Poisson-Delaunay time constant is strictly greater than one, its slack is linear and cannot give a sublinear transversal bound without a renormalized corrector/Busemann subtraction.
4. Importing only a power-law **pointwise** typical-block/geodesic-hit probability from planar lattice FPP does not by itself make the total resampling energy sublinear: the sum of block-hit probabilities is the expected number of blocks visited, which is order at most linear in route length. The needed new object is global: two-replica overlap/noise stability or another cancellation reducing the *integrated* effective susceptibility, together with centering/tail control.

The standalone local-repair, maximum-influence, and logarithmic-entropy routes are therefore not pursued further as possible polynomial-exponent movers.

---

## 1. Authoritative continuity and ownership

The run began by rereading the required control and continuity materials: `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, the later NM13 deployment amendment, `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md` and `RANKING.md`, the newest own report, neighboring NM13 reports, intake/attempt references, and claims.

P0214 remains exclusively owned by NM13-12. At the final prewrite snapshot `b27582152633d74d37ace816c16e358ce1d5e0cc`, `operations/claims/P0214.md` still records owner `NM13-12`, namespace `proofnet24/NM13-12/`, canonical key `fluctuations_of_shortest_routes_in_poisson_proximity_networks`, SHA-256 `7707fc4888eade0e22136663abfefe5b2eddf2d482cc0bba1a943a3dcac811ff`, and residue `11`.

The previous NM13-12 report commit was `d7eb5505e0f049d3d0fe34e862c31c15d9731040`. Comparing it with final prewrite master `b27582152633d74d37ace816c16e358ce1d5e0cc` gave `ahead_by=104`, `behind_by=0`. A direct reread of the canonical claim at the final prewrite commit found no ownership or metric mutation. No shared root or peer file is edited by this run.

Historical continuity retained:

- First substantive run: methods #2/#6/#30; curvature-transfer gate and `MD(eta,p)` sufficient condition; no movement.
- Second substantive run: methods #11/#20/#24; shortest-path dual, shielded local resampling bound, and an exact Delaunay flip family showing order-cavity-radius local sensitivity; no movement.
- This run: methods #5/#12/#28; no movement; unchanged count becomes 3 and triggers the stuck rule for the next invocation.

The old Codex P0214 attempt was `attempted_unsolved` and had only a deterministic Euclidean relation between route length and transverse deviation. I do not count that old relation as new work here.

---

## 2. Source/literature status checked this run

Bounded checks dated 2026-09-19 covered the original Aldous source, the rigorous Poisson-Delaunay moderate-deviation paper, later/nearby Poisson-Delaunay geodesic work, and quantitative planar-FPP coalescence/influence work. Search scope included exact/source-title queries and 2024--2026 Poisson-Delaunay shortest-route/transversal-fluctuation queries. Access was through indexed web/article text and repository continuity; no claim of worldwide completeness is made.

### 2.1 Frozen baseline remains 3/4

Hirsch--Neuhaeuser--Schmidt, *Moderate deviations for shortest-path lengths on random segment processes*, ESAIM Probab. Stat. 20 (2016), remains the rigorous baseline source. Its framework applies to Poisson-Delaunay shortest paths and gives the `3/4+epsilon` geodesic tube used to certify `U_T=3/4`. The same paper also establishes that the relevant Poisson-Delaunay time constant is strictly greater than one; that fact is important for the failure of Method #12 below.

### 2.2 Nearest quantitative overlap model found

Dembin--Elboim--Peled, *Coalescence of Geodesics and the BKS Midpoint Problem in Planar First-Passage Percolation*, GAFA 34 (2024), proves quantitative power-law overlap/point-hit statements for planar lattice FPP under its hypotheses. It is the closest checked source for Method #28 and for the next recovery's proposed port. It is **not** the same model: their graph is fixed `Z^2` with iid continuous edge weights, whereas P0214 has a random Poisson-Delaunay graph and Euclidean edge costs coupled through geometry. Rotational invariance of Poisson-Delaunay makes the asymptotic limit shape favorable, but does not remove this model mismatch.

### 2.3 Present-source status

A bounded 2026-09-19 search did not recover a primary source proving Aldous's requested Poisson-Delaunay transversal order or a certified upper exponent below `3/4`. This is negative bounded evidence only. It is not a proof of global openness or novelty.

---

## 3. Method #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

### 3.1 Exact finite-temperature block-penalty identities

Fix a bounded finite corridor containing the two endpoints and condition on a locally finite Delaunay realization, so the relevant induced graph and simple path family `Gamma` are finite. Let `L(gamma)` be Euclidean route length. For each unit block `Q`, let

`I_Q(gamma) = 1{gamma visits Q}`.

Introduce block penalties `h=(h_Q)` and inverse temperature `beta>0`:

`L_h(gamma) = L(gamma) + sum_Q h_Q I_Q(gamma)`,

`Z_beta(h) = sum_{gamma in Gamma} exp(-beta L_h(gamma))`,

`F_beta(h) = -(1/beta) log Z_beta(h)`.

Write `<.>_{beta,h}` for expectation under the corresponding Gibbs route measure. Direct differentiation gives the exact identities

`dF_beta/dh_Q = <I_Q>_{beta,h}`,

and

`d^2 F_beta/(dh_Q dh_R) = - beta Cov_{beta,h}(I_Q,I_R)`.

In particular, if `p_Q=<I_Q>`, then

`-d^2 F_beta/dh_Q^2 = beta p_Q(1-p_Q)`.

Let `gamma,gamma'` be two independent Gibbs routes and let `S(gamma)` be the set of visited blocks. Since

`P(I_Q(gamma) != I_Q(gamma')) = 2 p_Q(1-p_Q)`,

summing the diagonal Hessian gives the exact two-replica formula

`- sum_Q d^2 F_beta/dh_Q^2 = (beta/2) E |S(gamma) Delta S(gamma')|`.       (5.1)

Thus the natural curvature/susceptibility observable is not a worst-case local repair constant. It is a two-route disagreement measure.

### 3.2 Exact one-block threshold and the missing source-point estimate

Now penalize only one block `Q` by a scalar `t`. Let

`A_Q = min{L(gamma): gamma avoids Q}`,

`B_Q = min{L(gamma): gamma visits Q}`.

At zero temperature the perturbed shortest-path value is exactly

`E_Q(t) = min{A_Q, B_Q+t}`.                                             (5.2)

The route occupation switches at the route-gap threshold

`t_Q^* = A_Q-B_Q`.

At finite beta, splitting the partition function into avoiding and visiting routes gives

`p_Q'(t) = - beta p_Q(t)(1-p_Q(t))`,

so for every `a<b`,

`beta int_a^b p_Q(t)(1-p_Q(t)) dt = p_Q(a)-p_Q(b) <= 1`.                (5.3)

This averaged-in-penalty estimate is exact and strong, but the source model is at the single point `t=0`. To use (5.3) there one needs quantitative control of how often `A_Q-B_Q` lies near zero. Merely knowing almost-sure uniqueness/no exact tie does not control the density of near ties.

The exact near-cocircular Delaunay flip family from the preceding run already warns against a deterministic route-gap lower bound: very small geometric changes can switch topology while changing a long route by a cavity-scale amount. Therefore the live requirement is probabilistic anti-concentration/noise stability of the route gap, not another deterministic local sensitivity lemma.

### 3.3 Outcome of #5

No `U_T` movement. The method identifies a more precise global observable:

> control the source-point two-replica block disagreement / route-gap susceptibility strongly enough that its integrated effective contribution is sublinear in `r`.

This is retained for the stuck recovery; the generic soft-min parameter trick alone is not enough.

---

## 4. Method #12 — FIND WHAT IS CONSERVED

The natural candidate is longitudinal progress versus Euclidean excess length. This deliberately checks the old deterministic route-length/transverse relation rather than pretending it is new.

Consider any polygonal path from `(0,0)` to `(r,0)`. Write its edge vectors as `(a_i,b_i)` and lengths `ell_i=sqrt(a_i^2+b_i^2)`. Define the nonnegative quantities

`p_i = ell_i+a_i`,

`q_i = ell_i-a_i`.

Then exactly

`p_i q_i = b_i^2`.                                                       (12.1)

For any prefix ending at transverse height `h=|sum b_i|`, Cauchy--Schwarz gives

`h <= sum sqrt(p_i q_i) <= sqrt((sum p_i)(sum q_i))`.

Because all `p_i,q_i` are nonnegative and over the full path

`sum p_i = L+r`,

`sum q_i = L-r`,

where `L=sum ell_i`, every prefix satisfies

`h^2 <= (L+r)(L-r) = L^2-r^2`.                                         (12.2)

This is the deterministic Euclidean excess-length relation already represented in the old P0214 attempt. It is therefore **not** counted as a new theorem or metric gain.

The important failure is source-specific. In Poisson-Delaunay Euclidean FPP the time constant `mu_D` is strictly greater than one, so a long geodesic has leading length approximately `mu_D r`, not `r+o(r)`. Hence the raw slack `L-r` is itself order `r`; (12.2) allows order-`r` wandering and cannot see the sublinear geometry relevant to `U_T`.

A conservation route must first subtract the deterministic stretch tax `mu_D r`. The desired replacement would resemble a stationary Busemann/corrector potential whose residual slack is local/nonnegative enough to support a curvature argument and whose fluctuations have a polynomially improved bound. The checked Poisson-Delaunay coalescence literature does not, in the material inspected this run, provide such a quantitative corrector estimate.

### Outcome of #12

No movement. Raw longitudinal progress is abandoned as an exponent route. A **renormalized** corrector/Busemann version is a possible future category shift, but it is not assumed to exist with the needed estimates.

---

## 5. Method #28 — REPLACE "FOR ALL" WITH "FOR TYPICAL"

### 5.1 Why this looked promising

The previous run showed that worst-case local Delaunay resampling can have cavity-scale effect. That makes typicality the natural escape: large cavities and near-pivotal blocks are rare. Dembin--Elboim--Peled supply a nearby solved example in planar lattice FPP where geodesic point-hit/overlap events obey power-law bounds and attractive-geodesic perturbations yield quantitative coalescence.

### 5.2 Pointwise pivotality alone does not reduce total resampling energy enough

Suppose, optimistically, that a Delaunay analogue gave a polynomial pointwise estimate

`sup_Q P(Q is visited/pivotal for the x-y geodesic) <= C r^(-alpha)`        (28.1)

for some `alpha>0`.

That by itself does **not** make the standard Efron--Stein energy polynomially sublinear. To see the obstruction, let `N(gamma)` be the number of unit grid blocks meeting a rectifiable route `gamma`. Every unit square meeting `gamma` lies in a fixed-radius neighborhood of `gamma`; the area of such a tube is bounded by a constant times `length(gamma)+1`. Consequently

`N(gamma) <= C (length(gamma)+1)`.                                      (28.2)

For shortest Delaunay routes the expected length is linear in endpoint separation, hence

`sum_Q P(Q visited) = E N(gamma) = O(r)`.                               (28.3)

A local-resampling Efron--Stein sum whose squared increment is paid whenever the route visits a bounded neighborhood of `Q` therefore naturally inherits an `O(r)` total budget. Making the **maximum** term in that budget polynomially small, as in (28.1), is useful for entropy inequalities, but the usual Falik--Samorodnitsky/BKS mechanism applied to a still-linear total budget gives a logarithmic improvement rather than the polynomial gain required to move `U_T`.

Thus a direct port of only the point-hit exponent is not enough. The port must exploit overlap/cancellation at the level of the *integrated* energy, for example through two coupled replicas, a noise semigroup, or another mechanism showing that the effective sum of sensitive blocks is `O(r^(1-delta))` for some `delta>0` after the correct centering.

This dovetails exactly with (5.1): the finite-temperature Hessian measures two-replica block disagreement, not merely one-replica visitation.

### 5.3 What survives from Dembin--Elboim--Peled

Their attractive-geodesic/coalescence architecture is still the best checked solved analogue, because it attacks global route organization rather than a deterministic local repair. The model mismatch is the central porting issue:

- their graph is fixed `Z^2`; ours is a random Delaunay graph;
- their edge weights are iid; ours are Euclidean edge lengths coupled through the Poisson geometry;
- HNS stabilization can localize graph changes, but the previous run proved that the resulting repair magnitude retains a cavity-radius factor.

Any successful port must therefore combine stabilization with a probabilistic overlap/noise estimate strong enough to suppress the **sum** of effective influences, not merely each influence separately.

### Outcome of #28

No movement. Typical-block pivotality is retained only in its strengthened two-replica/noise-stability form. The simple `sup_Q` route is abandoned as an exponent mover.

---

## 6. Stuck trigger after three unchanged substantive runs

The owner rule triggers because the tracked quantity has now failed to move for three consecutive substantive runs after admission:

1. run 1: `3/4 -> 3/4` (#2/#6/#30),
2. run 2: `3/4 -> 3/4` (#11/#20/#24),
3. this run: `3/4 -> 3/4` (#5/#12/#28).

Therefore:

- `unchanged_run_count = 3`,
- `stuck_triggered = true`,
- `stuck_recovery_count = 0/2`,
- next invocation mode = **Section-I thinking/recovery #1**.

This report preserves the exact block for that recovery.

### Exact blocking statement

The first-run curvature lemma reduces a genuine metric improvement to a polynomial passage-error improvement. A concrete sufficient target remains: find `eta>0` and `p>3` such that, uniformly over the source-relevant endpoint pairs needed by the tube argument at scale `r`,

`P(|D(u,v)-mu_D |u-v|| > C r^(1/2-2 eta)) <= C r^(-p)`,                (BLOCK)

with the corresponding centering convention justified, so the `O(r^2)` family of relevant pairs has summable total failure probability. Then the curvature transfer gives

`U_T <= 3/4 - eta`.

All routes so far stop before `(BLOCK)` because their effective fluctuation/sensitivity budget remains diffusive up to logs, or they lack source-point anti-concentration.

### Routes tried and precise failure

- **#2 counterexample first:** a single polynomial-size Poisson void is super-polynomially/summably rare; it does not refute the target.
- **#6 solved-model deformation:** a Howard--Newman/BKS-style `r/log r` variance improvement alone is only logarithmic and cannot move the polynomial transverse exponent.
- **#30 one scale/direction:** produced the explicit `MD(eta,p)`/`(BLOCK)` sufficient gate but did not prove it.
- **#11 dualize:** exact shortest-path Lipschitz dual exposes local constraints, but the total influence budget remains linear.
- **#20 algorithm failure:** HNS stabilization gives local repair, but the deterministic repair cost scales with cavity/stabilization radius.
- **#24 extremal object:** exact near-cocircular four-point Delaunay configurations prove that cavity-scale local sensitivity is real, not just a loose estimate.
- **#5 parameter differentiation:** exact soft-min/two-replica identities reduce the issue to source-point route-gap anti-concentration / disagreement control, which is not yet available.
- **#12 conserved quantity:** the raw longitudinal slack is poisoned by the strictly greater-than-one Delaunay time constant; the old Euclidean relation cannot see sublinear wandering.
- **#28 typical instead of all:** pointwise polynomial hit/pivotal bounds can make maximum influence small but do not by themselves make the integrated influence sum sublinear.

### What a proof needs that none of the routes currently contains

A source-valid **global cancellation/overlap mechanism** yielding a polynomially sublinear effective sensitivity budget, plus a conversion from that budget to deviations centered at `mu_D r`. Equivalently, one needs to control two-replica route disagreement/noise sensitivity strongly enough that the integrated energy is `O(r^(1-delta))` for some `delta>0`, not merely `O(r/log r)` or `O(r)`.

### Simplest still-unproved quantitative subproblem worth isolating

For a fixed direction and a mesoscopic central slab, obtain a polynomially decaying source-point route-gap/noise-sensitivity estimate under the unperturbed Poisson-Delaunay law that controls **two-route disagreement**, not just one-route visitation. A representative form is to show that an appropriate translation-averaged block susceptibility satisfies

`EFFECTIVE(r) = O(r^(1-delta))`                                         (SUB)

for some `delta>0`, where `EFFECTIVE(r)` is chosen so that the exact replica identity (5.1) or a Poisson-noise analogue feeds a passage-time variance/deviation bound. The next recovery must define this observable without silently assuming the conclusion.

### Nearest solved problem and missing ingredient

Nearest checked solved analogue: Dembin--Elboim--Peled (2024), quantitative coalescence/BKS midpoint in planar iid lattice FPP. Their proof has a quantitative attractive-geodesic/perturbation mechanism and fixed-lattice iid product structure. P0214 lacks that product structure because geometry determines both the Delaunay graph and its Euclidean edge costs. HNS supplies stabilization, but not the missing polynomial global overlap/noise estimate.

### Required next recovery choice

For Section-I recovery #1, choose exactly:

**PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

The port target is **not** merely Dembin--Elboim--Peled's point-hit estimate; Section 5 shows that is insufficient by itself. The recovery should test whether their attractive-geodesic coupling can be translated into a Poisson noise-semigroup / two-replica statement on the HNS-stabilized Delaunay graph that genuinely reduces the integrated sensitivity below linear order.

Planned Section-B moves for that recovery, all untried on P0214:

- **#1 CHANGE THE CATEGORY:** recast Poisson resampling through a Poisson Ornstein--Uhlenbeck/noise-semigroup energy rather than a sum of worst-case block repairs.
- **#18 SAY IT IN ANOTHER LANGUAGE:** translate passage-time variance into integrated noise sensitivity / replica overlap and identify the exact source-valid observable whose exponent would move `U_T`.
- **#21 ASK WHO ELSE HAS THIS SHAPE:** port the quantitative attractive-geodesic/coalescence ingredient from Dembin--Elboim--Peled, explicitly checking which iid-lattice steps survive Poisson-Delaunay stabilization and which do not.

If that recovery does not move the metric, it counts as stuck-recovery episode #1 of the allowed two. No rotation occurs yet.

---

## 7. Model/scheduler control audit

Fresh inspection of the exposed task-control surface this run still shows task fields for title/prompt, schedule/timing, enablement/listing/update metadata, but **no bindable model-family selector, no reasoning-effort selector, and no authenticated applied-model/reasoning attestation field**. Therefore `GPT-6 / maximum` remains a prompt request only on this surface. The actual runtime truth for this report is stated on line 1 and is not upgraded by prompt text.

Making the setting binding would require an authorized scheduling/product/API/admin surface that persists a model-family field and reasoning-effort field into inference routing and exposes trustworthy per-run attestation.

The historical P26 `You cannot modify this task` event is an authorization-context boundary. I did not retest it by attempting a schedule modification, because this invocation is explicitly forbidden to create or modify additional schedules. The lawful workaround remains use of the owning/authorized task context or an authorized platform/admin route; never duplicate/bypass ownership.

---

## 8. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-12
  namespace: proofnet24/NM13-12/
  source_id: P0214
  claim_id: P0214
  canonical_dedup_key: fluctuations_of_shortest_routes_in_poisson_proximity_networks
  shard_residue_mod_13: 11
  category: HARD_OUTSIDE
  status: PARTIAL
  source_process: unit-intensity planar Poisson-Delaunay, Euclidean edge lengths, bounded-local endpoint convention
  metric_name: U_T
  metric_definition: best certified polynomial upper exponent for source-valid transversal deviation
  metric_before: 3/4
  metric_after: 3/4
  metric_movement: false
  methods_attempted:
    - 5
    - 12
    - 28
  method_outcomes:
    5: exact soft-min Hessian/two-replica disagreement identity; source-point route-gap anti-concentration missing
    12: raw longitudinal progress reduces to old Euclidean excess-length relation and fails because mu_D>1
    28: pointwise typical-block/pivotality alone leaves linear integrated influence; global overlap/noise cancellation required
  unchanged_run_count_after_admission: 3
  stuck_triggered: true
  stuck_recovery_count: 0
  stuck_recovery_limit: 2
  next_run_mode: Section-I thinking/recovery #1
  next_recovery_choice: port technique from nearest solved problem
  next_methods_planned:
    - 1
    - 18
    - 21
  exact_block: prove a polynomially improved centered passage-deviation gate MD(eta,p), or a source-valid sublinear integrated sensitivity strong enough to imply it
  nearest_solved_problem: Dembin-Elboim-Peled 2024 quantitative planar iid-lattice FPP coalescence/BKS midpoint
  audits_required_if_completed:
    - P26
    - NM13-13
  audits_passed: []
  bounded_literature_check_date: 2026-09-19
  closure: false
  shared_roots_edited: false
  peer_files_edited: false
  checker_created: false
  checker_reason: no finite claim required exact enumeration; this run's substantive claims are analytic identities/proofs written on-page
```

---

## 9. Operational compliance

Exactly one immutable own-namespace report is created for this invocation. No claim file, shared root ledger, peer namespace, workflow, permission, public post, email/Drive resource, paid compute resource, or schedule is modified. No receipt-only follow-up commit is requested. Readback at the creation commit is required before the run is considered saved.
