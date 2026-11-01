Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `L_cone: pi/4 -> pi/4`; unchanged-count field remains `UNKNOWN -> UNKNOWN`. Methods actually tried: #3 PROVE SOMETHING STRONGER, #12 FIND WHAT IS CONSERVED, #30 ONE DIRECTION AT A TIME.**

# R14 HARD OUTSIDE — H0017: first-moment Busemann flux is tautological; a maximal gap is a cocycle-realization problem

Repository / branch: `yspennstate/math-open-problems` / `master`.  
Date: 2026-09-17 UTC.

## 1. Continuity, ownership, exclusions, and source freshness

I did **not** reopen the original negative-margin spherical Gaussian perceptron. Its supported handoff bracket remains

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`,

with width `6.48139658710`. I0089 and RS-2026-BIS32 likewise remain handed off after their hard-task recovery limits.

The active exclusive R14 target remains **H0017**, Daniel Ahlberg, Maria Deijfen and Matteo Sfragara, *Surviving from the tip of a cone in competing first-passage percolation*, arXiv:2607.07589v1 (8 July 2026), under `operations/claims/H0017.md`.

At run start I recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the controlling owner directive, the H0017 claim, and the newest own report

`runs/R14/2026-09-17T17-53-20Z_h0017_square_diamond_orbit_gap_c6e4.md`.

A targeted repository scan also checked neighboring FPP work. The old R08 strict-convexity route is explicitly retired from the R08 slot rather than solved; current neighboring reports do not claim H0017. I did not edit peer files or shared ledgers.

Fresh primary-source checking on 2026-09-17 found no later source-matching resolution. The arXiv record for 2607.07589 still gives the July 8, 2026 manuscript and states only the tangent-direction theorem. Ahlberg--Hoffman, arXiv:1609.02447, remains the structural source for random coalescing geodesics and the deterministic closed set `C_*` of realized Busemann supporting functionals. Their assumption A1 is exactly the source product/continuous/minimum-of-four square-moment class. Their paper explicitly says that its general stationary/ergodic theory is qualitative, and that quantitative estimates in the independent setting would have to use independence in a fundamental way.

I also checked Groathouse--Janjigian--Rassoul-Agha, arXiv:2306.17714v2 / Trans. AMS 378 (2025), which establishes generalized Busemann functions for a broad random-potential framework encompassing FPP. This is relevant language for the new obstruction below, but the material recovered this run does **not** give the source-matching theorem needed here: it does not identify every convex average of two undirected FPP geodesic Busemann cocycles with the Busemann cocycle of an actual random coalescing geodesic. I therefore do not promote that paper to a closure theorem.

This is a bounded dated search, not a novelty certificate.

## 2. Frozen metric and retained reductions

For a source-admissible iid continuous passage-time law `F`, let

`alpha_c^F(theta) := sup { alpha : P_F(G^{theta,alpha}) > 0 }`.

The fixed source-wide metric is

`L_cone := inf_F inf_theta alpha_c^F(theta)`.

The source certifies `L_cone >= pi/4`; full source closure is `L_cone=pi/2`.

The retained R14 self-check reductions remain:

`alpha_c^F(theta) = pi/2 - dist(theta,C_*(F))`                            (R2)

in the endpoint sense (survival below / extinction above), and hence

`ell(F) := inf_theta alpha_c^F(theta) = pi/2 - covrad(C_*(F))`;           (R2')

`ell(F)=pi/4  <=>  C_*(F) is exactly one four-point quarter-turn orbit`; (R4)

`ell(F)=pi/4  =>  Ball(F) is square or diamond`;                         (R5)

and if two slopes in `C_*` have separation `delta` modulo `pi/2`, then

`ell(F) >= pi/4 + delta/2`.                                               (R6)

Thus a direct source-moving theorem would be

`exists delta_0>0 such that for every admissible F, s(F)>=delta_0`,      (U)

where

`s(F)=max_{rho,rho' in C_*(F)} d_Q(rho,rho')`.

Then R6 would give `L_cone >= pi/4+delta_0/2`.

Metric this run:

`L_cone: pi/4 -> pi/4`.

The supported unchanged-run field remains unknown, so it stays `UNKNOWN -> UNKNOWN`; no streak is manufactured.

## 3. Method #3 — prove something stronger: sharpen the exact boundary state using the full D4 action

The previous R4 used only quarter-turn invariance. The iid square-lattice model has the full dihedral symmetry `D4`, including reflections. This gives an exact sharpening of the `pi/4` equality case.

### R14-H0017-R7 — the only four-slope boundary states are the axis orbit and diagonal orbit

For every source-admissible iid law `F`, if

`ell(F)=pi/4`,

then the deterministic slope set `C_*(F)` is **either**

`{0, pi/2, pi, 3pi/2}`

(up to the standard angular parametrization of supporting normals), **or**

`{pi/4, 3pi/4, 5pi/4, 7pi/4}`.

In particular there is no generic tilted four-ray equality state in the iid source class.

#### Proof

By retained R4, equality `ell(F)=pi/4` forces

`C_* = {rho+k*pi/2 : k=0,1,2,3}`

for one angle `rho`, modulo `2pi`.

Because the iid edge law and the square lattice are invariant under reflection, and `C_*` is deterministic, reflection sends `C_*` to itself. Hence `-rho` must lie in the same quarter-turn orbit as `rho`:

`-rho = rho + k*pi/2  (mod 2pi)`

for some integer `k`. Thus

`2rho = -k*pi/2  (mod 2pi)`,

so modulo `pi/2` we have `rho=0` or `rho=pi/4`. These are exactly the axis and diagonal orbits. QED.

This is a complete elementary self-check. It sharpens R5 but does not move the universal metric: excluding either exact state for each law, even if achieved, need not yield a uniform angular separation over all laws.

### Why the stronger universal second-orbit theorem did not close

I tried to make (U) follow from symmetry plus coalescence plus the neighboring-geodesic structure. This fails for a structural reason already visible in Ahlberg--Hoffman's paper: their general theory is qualitative and explicitly says quantitative estimates in the iid case require independence to enter fundamentally. Convex/D4 geometry alone permits closed invariant slope sets arbitrarily close to the two four-ray configurations. Stationary/ergodic non-product FPP models are known to realize very sparse geodesic structures. Therefore any positive universal `delta_0` must use genuinely quantitative product-measure input, not merely the topology/order of coalescing geodesics.

So method #3 identifies the correct stronger source-moving target but does not prove it.

## 4. Method #12 — conserved first-moment Busemann flux collapses to a tautology

This run next tested the most natural translation-covariant invariant attached to a missing Busemann-slope interval.

Assume `rho^-` and `rho^+` are two realized supporting slopes in `C_*`, with random coalescing geodesics `G^-`, `G^+` and Busemann cocycles `B^-`, `B^+`. Let

`D := B^+ - B^-`,

and let

`bar B := (B^-+B^+)/2`,   `bar rho := (rho^-+rho^+)/2`.

Ahlberg--Hoffman's Busemann lemma gives, for every lattice displacement `z` and every `n`,

`B^-(0,nz) <= T(0,nz)`,  `B^+(0,nz) <= T(0,nz)`.

Define the nonnegative deficits

`a_n := T(0,nz)-B^-(0,nz)`,

`b_n := T(0,nz)-B^+(0,nz)`.

Then

`D(0,nz)=a_n-b_n`,

so exactly

`|D(0,nz)| <= a_n+b_n`

and therefore

`|D(0,nz)| <= 2T(0,nz)-B^-(0,nz)-B^+(0,nz)`.             (5)

For a random coalescing geodesic, the mean of its stationary Busemann cocycle is its deterministic linear slope. Additivity and stationarity give

`E B^±(0,nz)=n rho^±(z)`.

Taking expectations in (5), using `|E D|<=E|D|`, dividing by `n`, and using the L1 shape theorem `E T(0,nz)/n -> mu(z)`, gives

`|rho^+(z)-rho^-(z)| <= 2mu(z)-rho^-(z)-rho^+(z)`.       (R8)

### R14-H0017-R8 — exact obstruction: first-moment flux carries no information beyond support geometry

I initially hoped (R8) would constrain the angular width between two neighboring slopes. It does not. Since `rho^-` and `rho^+` are supporting functionals of the norm ball,

`rho^-(z) <= mu(z)`,   `rho^+(z) <= mu(z)`.

For any two real numbers `u,v <= m`,

`|u-v| <= (m-u)+(m-v)=2m-u-v`.

Thus (R8) is **exactly** the scalar support inequality with

`u=rho^-(z)`, `v=rho^+(z)`, `m=mu(z)`.

No quantitative iid information survives this first-moment conservation law. In particular, any mass-transport argument whose only numerical input is the mean Busemann flux `E[B(0,z)]` cannot by itself shrink a missing interval of `C_*`: after taking expectation, it reduces to deterministic convex support geometry.

This is the certified obstruction requested by the previous report: the most obvious translation-covariant flux is sterile, for an exact algebraic reason rather than because a constant estimate is weak.

No finite checker was created because (5)--(R8) are direct analytic identities/inequalities.

## 5. Method #30 — one maximal missing interval at a time: midpoint cocycle realization

The failure of first moments suggests keeping the random cocycle rather than averaging it down to its slope.

Let `I=(rho^-,rho^+)` be a connected component of the complement of `C_*` in the circle of supporting functionals. Ahlberg--Hoffman prove that **all tangent supporting functionals belong to `C_*`**. Consequently an open missing interval can contain no tangent functional. In planar convex geometry, such a connected interval of non-tangent supporting functionals is contained in the normal cone of a single corner `v` of the deterministic limit shape. Thus its endpoint slopes `rho^-` and `rho^+` support `Ball` at the same corner, and so does their midpoint

`rho^0 := (rho^-+rho^+)/2`.

Now form the midpoint cocycle

`B^0 := (B^-+B^+)/2`.

It has the following exact properties:

1. **additivity:** `B^0(x,z)=B^0(x,y)+B^0(y,z)`;
2. **translation covariance/stationarity:** inherited from `B^-` and `B^+`;
3. **metric domination:** `|B^0(x,y)| <= T(x,y)`;
4. **mean slope:** `E B^0(0,z)=rho^0(z)`.

Thus `B^0` has precisely the elementary cocycle/support properties one would want from a Busemann object at the midpoint of the missing interval.

But `rho^0` is, by definition of the gap, **not** in `C_*`. Therefore `B^0` cannot simply be identified with the Busemann cocycle of a random coalescing geodesic by the existing Ahlberg--Hoffman theory.

This isolates the one-direction-at-a-time problem:

> **Midpoint cocycle realization problem.** Given neighboring realized geodesic Busemann cocycles `B^-`, `B^+` whose slopes are the endpoints of one missing corner interval, find an iid-specific condition forcing their midpoint cocycle (or another stationary cocycle with the same midpoint mean slope) to calibrate an actual random coalescing geodesic.

If such a theorem held, `rho^0` would belong to `C_*`, contradicting that `I` is a gap. Repeating would fill every gap and give the source conjecture.

This is a substantially sharper obstruction than “prove limit-shape differentiability”: it asks for a **cocycle-to-geodesic realization principle at one corner**, and it is exactly where independence has to enter.

### Calibration defect

For an oriented nearest-neighbor edge `e=(x,y)`, define

`q_e := omega_e - B^0(x,y)`.

Since `B^0(x,y) <= T(x,y) <= omega_e`, we have

`q_e >= 0`.

An actual geodesic calibrated by `B^0` would require an infinite directed path along which the relevant cocycle/metric slack vanishes in the appropriate sense. The missing theorem is not existence of a stationary additive cocycle — `B^0` already supplies one — but existence of an **infinite calibrated path/coalescence class** selected from that cocycle in the undirected iid metric.

Groathouse--Janjigian--Rassoul-Agha prove existence of generalized Busemann functions/Gibbs measures in a framework encompassing FPP. That makes their machinery the nearest language I found for this obstruction, but the current source check does not give the needed implication “this midpoint cocycle yields an actual random coalescing FPP geodesic of slope `rho^0`.” Treating generalized cocycle existence as if it filled `C_*` would therefore be an unjustified leap.

## 6. What changed mathematically this run

The fixed metric did not move, but the route is narrower and one major dead end is now certified.

Before this run, the source-moving obligation was phrased as a uniform second Busemann orbit. After this run:

- the exact equality state is reduced by full `D4` symmetry to only two configurations (axis or diagonal four-ray states);
- the natural conserved first-moment difference of two endpoint Busemann cocycles is proved to yield **only** the tautological support inequality, so there is no reason to spend another run optimizing that flux;
- one maximal missing interval is converted into a precise **midpoint stationary-cocycle realization problem**.

The remaining missing ingredient is now second-order/pathwise rather than first-moment: use iid finite energy/resampling to prove that a stationary dominated cocycle with midpoint support slope has an infinite calibrated path which is a genuine coalescing geodesic, or prove a weaker midpoint-insertion statement directly for neighboring endpoint geodesics.

## 7. Honest status and nearest solved machinery

H0017 remains **OPEN / PARTIAL**.

The new R7/R8 and the midpoint reduction are self-checks with `0/2` external audits. They are not source closure, and no claim of literature novelty is made.

The nearest rigorous ingredients remain:

- Ahlberg--Hoffman: every geodesic has an asymptotically linear Busemann functional; the realized deterministic closed set `C_*` contains every tangent functional; random coalescing geodesics have strong order/coalescence structure, but the theory is qualitative under general ergodic assumptions and explicitly flags quantitative iid input as missing.
- Ahlberg--Deijfen--Sfragara: survival at all openings below `pi/2` is proved when the relevant tangent/Busemann direction is available; their all-direction conjecture is exactly what H0017 targets.
- Groathouse--Janjigian--Rassoul-Agha: generalized Busemann objects exist broadly, including in FPP-type models, but this does not presently supply the required actual-geodesic realization of `B^0` in the source model.

A proof of the midpoint realization principle for every missing interval would bypass global differentiability of the FPP limit shape. Conversely, a proof that such realization can fail in a source-admissible iid law would expose a plausible mechanism for a genuine counterexample to Benjamini's conjecture.

## 8. Next new-method triple

Do not repeat #3/#12/#30 next run. The strongest genuinely different triple is:

- **#10 DERANDOMIZE:** start from the generalized/stationary midpoint cocycle and seek a measurable deterministic rule selecting a zero-defect outgoing edge at every vertex, then prove the selected path is infinite and coalescing; identify exactly which zero-defect existence step fails if it cannot be done.
- **#13 FIND WHAT ONLY INCREASES:** expose the environment in annuli and track a calibration-defect or endpoint-order quantity that is monotone under local surgery; the goal is to force a midpoint path rather than merely change the entrance to an existing tail class.
- **#26 HUNT THE SPORADIC CASE:** treat the only two exact `pi/4` boundary states from R7 separately — axis four-ray and diagonal four-ray — and test whether product-measure finite energy rules out one of them by an orientation-specific surgery.

If these produce no metric movement for the required number of consecutive runs, apply the HARD stuck protocol without inventing a streak value.

## 9. Model / scheduler control status

The exposed scheduling interface still offers title, prompt, schedule or relative start, timing mode, and enablement. It exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore GPT-6/maximum remains request text only and is not claimed for this run.

The repository's current `RESULTS.md` records that P26's earlier `You cannot modify this task` failure was context-dependent: its full update later succeeded in an authorized P/C context. If an ID still rejects modification, the legitimate route is the authorized owning workspace/account context or platform support. No scheduler changes, permission changes, duplicate tasks, or bypasses were attempted in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R14
  allocation: HARD OUTSIDE
  active_target: H0017
  source: arXiv:2607.07589v1
  status: OPEN/PARTIAL
  fixed_metric: L_cone
  before: pi/4
  after: pi/4
  movement: none
  unchanged_count_before: UNKNOWN
  unchanged_count_after: UNKNOWN
  methods_tried: [3, 12, 30]
  new_self_checks:
    - "R14-H0017-R7: under full D4 symmetry, ell(F)=pi/4 leaves only the axis or diagonal four-slope orbit"
    - "R14-H0017-R8: the natural first-moment Busemann difference flux reduces exactly to the deterministic support inequality"
    - "R14-H0017-R9: a maximal missing corner interval reduces to realization of the midpoint stationary cocycle as an actual coalescing geodesic Busemann cocycle"
  external_audits_for_new_checks: "0/2"
  checker_created: false
  reason_no_checker: "analytic cocycle/convexity identities; no finite computational claim"
  next_methods: [10, 13, 26]
  original_negative_margin_perceptron:
    state: HANDOFF_PRESERVED
    alpha_lower: 6.30297437506
    alpha_upper: 12.78437096216
    bracket_width: 6.48139658710
  prior_targets:
    I0089: HANDOFF_PRESERVED
    RS-2026-BIS32: HANDOFF_PRESERVED
```
