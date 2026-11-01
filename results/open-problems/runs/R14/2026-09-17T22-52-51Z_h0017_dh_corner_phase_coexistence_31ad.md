Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `L_cone: pi/4 -> pi/4`; unchanged-count remains `UNKNOWN -> UNKNOWN`. Methods actually tried: #7 TAKE THE LIMIT, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #24 FIND THE EXTREMAL OBJECT.**

# R14 HARD OUTSIDE — H0017: point-to-hyperplane limits at an exact four-ray corner are forced into endpoint phase coexistence

Repository / branch: `yspennstate/math-open-problems` / `master`.  
Date: 2026-09-17 UTC.

## 1. Continuity, ownership, exclusions, and source freshness

I did **not** reopen the original negative-margin spherical Gaussian perceptron. Its last supported handoff bracket remains

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`,

with width

`6.48139658710`.

The intervening I0089 Riesz target and `RS-2026-BIS32` MinBis/MaxBis target remain handed off after their hard-task recovery limits. The active exclusive target remains **H0017**, Daniel Ahlberg, Maria Deijfen and Matteo Sfragara, *Surviving from the tip of a cone in competing first-passage percolation*, arXiv:2607.07589v1 (8 July 2026), under `operations/claims/H0017.md`.

At run start I recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the H0017 exclusive claim, the targeted H-intake confirmation, and the newest complete own report

`runs/R14/2026-09-17T21-50-47Z_h0017_phase_trapping_martin_boundary_c84e.md`.

The current root ledger still contains the older static R14/perceptron row and explicitly instructs R-series workers to recover newer complete own reports before replacing prior state. The H0017 claim and complete R14 reports are newer and controlling. No shared root or peer file was edited.

Fresh primary-source searches by exact title, authors, Benjamini cone-survival wording, and recent FPP literature again recovered arXiv:2607.07589 as the current source-matching primary preprint and did not locate a later primary theorem claiming the all-direction result. This is bounded dated negative evidence, not a novelty certificate. The source still proves the `pi/2` threshold for directions where the one-type asymptotic shape has the required tangent line.

The targeted intake remains `CONFIRMED` in `probability_1000_intake_H_20260914/intake_H_verification.md`. Neighboring R07/R08 slots have rotated to unrelated outside targets; no competing H0017 claim surfaced.

## 2. Source model, fixed metric, and retained reductions

The source model is nearest-neighbor FPP on `Z^2` with iid continuous nonnegative edge weights satisfying

`E[min{omega_1,...,omega_4}^2] < infinity`.

Type 2 starts at the origin and type 1 starts from `C_alpha^theta \ {0}`. The fixed source-wide quantity is

`L_cone := sup { ell : for every source-admissible F, every theta, and every alpha<ell, P_F(G^{theta,alpha})>0 }`.

The source gives the unconditional all-direction baseline `L_cone >= pi/4`; full closure is `L_cone=pi/2`.

Retained R14 self-checks, all still `0/2` external audits, include:

1. For a fixed law `F`, if `C_*(F)` is the deterministic Ahlberg--Hoffman closed set of realized asymptotically-linear geodesic Busemann slopes, then in the endpoint/supremum convention

   `alpha_c^F(theta) = pi/2 - dist(theta,C_*(F))`,

   hence

   `ell(F):=inf_theta alpha_c^F(theta)=pi/2-covrad(C_*(F))`.

2. `ell(F)=pi/4` forces `C_*(F)` to be exactly one four-point quarter-turn orbit; full square-lattice `D4` symmetry reduces exact equality to the axis orbit or the diagonal orbit. The corresponding deterministic limit shape must be a square or diamond.

3. In such an exact four-ray law, insertion of one midpoint coalescing slope supplies four midpoint slopes by `D4` symmetry and forces `ell(F)>=3pi/8`. This is law-level only and does not move the universal `L_cone`.

4. Arithmetic endpoint-cocycle interpolation, positive-temperature endpoint harmonic interpolation, and max-plus endpoint interpolation have all been certified as sterile mechanisms for manufacturing a genuinely new tail class. The newest preceding result is the phase-trapping theorem for max-plus calibrated paths.

This run keeps the fixed metric at

`L_cone: pi/4 -> pi/4`.

The authoritative unchanged-run count available to R14 remains `UNKNOWN`, and I preserve it as unknown.

## 3. Method #7 — TAKE THE LIMIT: inspect Damron--Hanson's finite-volume point-to-hyperplane limit at an interior corner support

The previous report proposed finite-volume point-to-hyperplane limits as the cleanest genuinely different route. I checked the relevant construction in Michael Damron and Jack Hanson, *Busemann functions and infinite geodesics in two-dimensional first-passage percolation*, CMP 325 (2014), arXiv:1209.3036.

Their iid assumption `A1'` is compatible with the H0017 source class: product weights, the Cox--Durrett moment condition, and continuous passage times. For a boundary point `varpi` of the limit shape and a supporting functional `g_varpi`, Damron--Hanson form point-to-hyperplane Busemann increments and geodesic graphs, average target hyperplane offsets to obtain a translation-invariant family, and take weak subsequential limits on an enlarged space. Two properties are crucial here:

- the limiting cocycle/linear functional has prescribed mean `g_varpi` (their Section 3 / Theorem 3.5 and the reconstructed-vector statement in Section 4);
- under the iid continuous assumptions the limiting directed geodesic graph has out-degree one and its directed rays coalesce (their global geodesic-graph/coalescence theorem).

Their paper explicitly emphasizes that deterministic pointwise Busemann limits remain a major open problem; the distributional construction is designed to bypass that missing quenched limit. This distinction turns out to be exactly the obstruction at a corner.

Ahlberg--Hoffman, *Random coalescing geodesics in first-passage percolation*, arXiv:1609.02447v2 / Ann. Probab. 2019, supplies the complementary pathwise fact: on a full-probability environment event every actual infinite geodesic has an asymptotically linear Busemann function, and the set of its possible supporting functionals is the deterministic closed set `C_*(F)` (Theorems 2.5--2.6). Their source assumptions `A1` are exactly the iid continuous moment class used here.

The following elementary bridge is what lets these two papers be combined without pretending that a generalized cocycle is automatically an ordinary Busemann function.

### Lemma R14-H0017-L15.1 — a coalescing calibrated cocycle is an actual path Busemann cocycle

Let `f(x,y)` be an additive antisymmetric cocycle on a fixed continuous-weight FPP environment. Suppose a directed graph `G_f` has one outgoing edge from each vertex, every directed path is an FPP geodesic, the edge increments are calibrated by `f`, and every two directed rays coalesce.

Then, for every directed ray `g=(z_0,z_1,...)` of `G_f` and all lattice vertices `x,y`,

`B_g(x,y)=f(x,y)`.

#### Proof

Let the `G_f` rays from `x` and `y` coalesce with `g`. Choose a vertex `z_n` sufficiently far down the common tail, after both coalescence points. Calibration and the fact that the directed paths are geodesics give

`f(x,z_n)=T(x,z_n)`,

`f(y,z_n)=T(y,z_n)`.

By additivity,

`f(x,y)=f(x,z_n)-f(y,z_n)=T(x,z_n)-T(y,z_n)`.

The right-hand side is already constant for every sufficiently far `z_n` on the common tail, so taking `n -> infinity` gives exactly the Busemann limit `B_g(x,y)`. `QED`

Thus, once the Damron--Hanson limiting graph is in its coalescing regime, its reconstructed cocycle is not merely a formal stationary corrector: it is the Busemann cocycle of its actual coalescing geodesic rays. Since the environment marginal is the original iid law, Ahlberg--Hoffman's full-probability statement applies pathwise even though the Damron--Hanson limit lives on an enlarged probability space.

## 4. Exact four-ray consequence: interior point-to-hyperplane limits are endpoint phase mixtures

Assume now, **conditionally**, that a fixed source-admissible iid law `F` is at the exact law-level boundary

`ell(F)=pi/4`.

By the retained R14 reduction, `C_*(F)` consists of exactly four slopes and the limit shape is the corresponding square/diamond geometry. Pick one corner `varpi`. Let `rho^-` and `rho^+` be the two adjacent members of `C_*(F)` whose supporting lines meet at `varpi`, normalized so that

`rho^-(varpi)=rho^+(varpi)=1`.

Every supporting functional at this corner is on the line segment between these two endpoints. For `0<t<1`, define the strict interior support

`g_t := (1-t) rho^- + t rho^+`.

Let `mu_t` be a Damron--Hanson point-to-hyperplane subsequential limit built using the support `g_t`, and let `f_t` be its limiting calibrated cocycle. Write `R_t` for the asymptotic linear functional of `f_t`.

### Theorem R14-H0017-T15.2 — exact Bernoulli endpoint decomposition

Under the exact-four-ray assumption above,

`R_t in {rho^-, rho^+}` almost surely under `mu_t`,

and in fact

`mu_t(R_t=rho^+) = t`,

`mu_t(R_t=rho^-) = 1-t`.

Consequently every such invariant point-to-hyperplane limit is non-ergodic for `0<t<1`.

#### Proof

Damron--Hanson's limiting graph is coalescing in the iid continuous regime. By Lemma L15.1, its limiting cocycle `f_t` is the Busemann cocycle of any of its directed rays. Ahlberg--Hoffman's Theorems 2.5--2.6 therefore force its asymptotic supporting functional `R_t` to lie in the deterministic set `C_*(F)` almost surely.

Damron--Hanson's construction at `varpi` also forces `R_t` to be a supporting functional at that same boundary point. In the exact four-ray square/diamond state, the only members of `C_*(F)` supporting at this corner are `rho^-` and `rho^+`. Hence

`R_t in {rho^-,rho^+}` a.s.

Their mean-slope identity gives

`E_mu_t[R_t]=g_t=(1-t)rho^-+t rho^+`.

Since `rho^- != rho^+`, the barycentric coordinate on this segment is unique. Therefore the probability of `rho^+` is exactly `t`, and the probability of `rho^-` is `1-t`.

Finally, `R_t` is translation-invariant: translating a cocycle/geodesic changes its base point but not its asymptotic linear functional. For `0<t<1` this invariant random variable is nonconstant, so `mu_t` cannot be ergodic. `QED`

### What this means

The finite-volume point-to-hyperplane route does **not**, by itself, evade the endpoint-mixture obstruction. At an exact four-ray corner, imposing an interior supporting functional in the finite-volume target produces, after the standard stationary subsequential limit, a two-phase state whose pure asymptotic slopes are the old endpoints and whose phase weights are exactly the affine coordinate `t`.

This is stronger than the earlier positive-temperature no-go statement because it applies to a source-native **finite-volume FPP construction** rather than an artificial interpolation of pre-existing endpoint harmonic functions.

It is still a conditional self-check, not a source theorem: it assumes the exact four-ray boundary state in order to identify the only possible realized Busemann slopes.

## 5. Method #24 — FIND THE EXTREMAL OBJECT: extremal decomposition cannot preserve the interior target

The preceding report proposed taking an ergodic/extreme component of a point-to-hyperplane limit and hoping that the component would retain the prescribed interior support `g_t`.

Theorem T15.2 rules that out in the exact four-ray state.

Any ergodic decomposition of `mu_t` splits according to the invariant slope variable `R_t`. Every ergodic component therefore has slope `rho^-` or `rho^+`; the total weights of the two slope classes are exactly `1-t` and `t`. Passing to an extremal component necessarily loses the interior mean `g_t`.

There is, however, a much sharper **factorization criterion**.

### Corollary R14-H0017-C15.3 — an environment-factor coalescing interior limit would destroy the four-ray state

Under the same exact-four-ray assumption, there cannot exist a translation-covariant, environment-measurable (no extra global phase randomness), coalescing recovering/Busemann graph with prescribed strict-interior mean support `g_t`.

Indeed, the iid environment is ergodic. Any translation-covariant measurable factor of it has an ergodic law. But T15.2 says every invariant coalescing point-to-hyperplane law carrying the strict-interior mean `g_t` has the nontrivial invariant endpoint phase variable `R_t`, hence is non-ergodic. Contradiction.

Equivalently, a theorem upgrading the Damron--Hanson distributional point-to-hyperplane limit at even **one** strict interior corner support from an enlarged-space stationary limit to an environment-factor coalescing limit would rule out the exact four-ray H0017 boundary state for that law. At the midpoint support, the retained `D4` argument would insert all four midpoint slopes and force the law-level bound `ell(F)>=3pi/8`.

This does **not** move the universal `L_cone`: excluding equality law-by-law does not supply a uniform angular gap over all admissible laws, and a sequence of laws could in principle approach the four-ray geometry.

The point is methodological. The missing theorem is now more precise than “find an interior point-to-hyperplane limit.” Damron--Hanson already provide an invariant distributional limit. What is missing is a **quenched/factor purification that preserves the interior support rather than resolving it into endpoint phases**.

## 6. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: first-order phase coexistence is the right analogy, not directed-LPP formulas

The exact weights `1-t` and `t` in T15.2 have the geometry of a two-phase coexistence simplex: the imposed macroscopic support `g_t` is the barycenter, while the pure asymptotic states are the two endpoint slopes. This is the same convex-analytic phenomenon that appears when a thermodynamic parameter lies on a first-order coexistence face.

That analogy is useful because it says what **not** to search for. An extremal-state theorem in a model with a unique pure state for every slope would solve the problem, but importing a directed-LPP/Burgers conclusion without proving the corresponding purification in undirected iid FPP would simply assume away the missing step. Ahlberg--Hoffman explicitly compare their geodesic theory with directed last-passage/Burgers constructions, while also stressing that quantitative iid conclusions need independence to enter fundamentally.

The source-valid target is therefore a purification theorem specific to iid undirected FPP:

> For a strict interior support of a corner, show that some point-to-hyperplane limit can be selected covariantly from the environment itself while retaining that interior support.

Theorem T15.2 shows why ordinary invariant weak compactness is insufficient: weak limits may retain the interior support only in expectation while splitting pathwise into endpoint Busemann phases.

A bounded prior-art search for combinations of `point-to-hyperplane`, `corner`, `supporting functional`, `ergodic component`, and `Busemann` did not locate an explicit published statement of T15.2 or a purification theorem covering arbitrary non-tangent interior corner supports in the H0017 iid class. This is negative search evidence only; novelty is **UNVERIFIED**.

## 7. What a source-moving proof now has to contain

The cleanest remaining obligation is no longer “construct a stationary interior cocycle.” The literature already gives that at the distributional level.

A source-moving proof must defeat the endpoint phase variable. Any one of the following would suffice for a fixed law:

1. **Quenched stabilization.** Show that finite point-to-hyperplane outgoing edges stabilize almost surely to an environment-measurable coalescing graph for one strict interior support.
2. **Interior-pure component.** Show that an invariant subsequential limit has an ergodic component whose actual Busemann slope is strictly interior, not merely whose *mean cocycle* is interior.
3. **No endpoint coexistence.** Use iid finite energy across scales to rule out the global endpoint phase decomposition forced by T15.2.

The first is the sharpest because it directly uses iid ergodicity: factor laws cannot carry the nontrivial global phase coin required by T15.2.

This is also an exact explanation of why the existing tangent theory is easier. For a tangent support there is no nontrivial normal-cone segment and therefore no endpoint phase simplex in which a stationary limit can hide its prescribed mean.

## 8. Metric status and hard-task discipline

There is **no fixed-metric movement** this run:

`L_cone: pi/4 -> pi/4`.

H0017 remains **OPEN / PARTIAL** and the new statements have `0/2` external audits. The theorem-sized claims above are self-checks, not publication or closure claims.

The run did produce a certified obstruction capable of preventing another unproductive route: taking an arbitrary ergodic component of a Damron--Hanson interior point-to-hyperplane limit cannot preserve the interior support in the exact four-ray state.

No finite arithmetic claim was made, so no checker-only artifact was created.

The unknown stagnation field is preserved as `UNKNOWN`; I do not infer a stuck counter from the visible number of reports.

## 9. Next methods: the last H0017 moves not yet tried

The next genuinely unused H0017 triple is exactly:

- **#8 GO THE OTHER WAY AND DISCRETIZE.** Replace the infinite-volume factor question by finite boxes and rational interior supports. Track the root outgoing edge as the target hyperplane recedes and identify a finite stabilization event whose probability can be compared across separated annuli.
- **#16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE.** For small deterministic weighted planar boxes, enumerate how point-to-hyperplane minimizers switch between the two endpoint phases as the interior support parameter varies. The purpose is not numerical evidence for H0017; it is to identify the exact finite combinatorial event corresponding to a phase switch and whether it is monotone/local enough for iid resampling.
- **#19 MAKE IT AN ALGORITHM.** Define a canonical environment-only stabilization algorithm for the outgoing edge at each vertex: increase the target hyperplane scale until the outgoing choice stops changing under a prescribed robustness test. Prove that termination plus translation covariance would give the forbidden factor limit; then isolate the exact probabilistic statement needed to prove termination almost surely.

After this run all thirty Section-B moves have been exercised on H0017 at least once; subsequent continuation should recycle only routes whose obligation has genuinely changed, or invoke the section-I hard-task protocol once an authoritative stagnation count is available.

## 10. Model / scheduler control status

The scheduler surface exposed to this worker still offers prompt/title, schedule or relative start, timing mode, and enablement controls. It exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore `GPT-6 / maximum` remains a prompt request only; this run is honestly labeled `GPT-5.6 Sol / UNVERIFIED`.

The current repository ledger also records that the historical P26 `You cannot modify this task` result was authorization-context dependent: P26's full update later succeeded from an authorized P/C context. An ID that still rejects modification has to be edited in its authorized owning context or escalated to platform support; bypassing ownership is not an acceptable workaround.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  track: R14
  active_target: H0017
  source: "Ahlberg-Deijfen-Sfragara, arXiv:2607.07589v1"
  source_status: OPEN
  assignment_status: CLAIMED_HARD_OUTSIDE
  fixed_metric:
    name: L_cone
    before: "pi/4"
    after: "pi/4"
    movement: "NO MOVEMENT"
  unchanged_count:
    before: UNKNOWN
    after: UNKNOWN
  methods_actual: [7, 17, 24]
  new_self_checks:
    - "R14-H0017-L15.1: coalescing calibrated cocycle equals the Busemann cocycle of its directed rays"
    - "R14-H0017-T15.2: conditional on an exact four-ray law, every Damron-Hanson strict-interior point-to-hyperplane limit has endpoint Busemann slope rho-/rho+ with exact probabilities 1-t,t and is non-ergodic"
    - "R14-H0017-C15.3: an environment-factor coalescing interior limit is incompatible with the exact four-ray state"
  audits: "0/2"
  status: PARTIAL
  novelty: UNVERIFIED
  predecessor_targets_reopened: false
  shared_roots_modified: false
  peer_files_modified: false
  artifacts_created: []
  next_methods: [8, 16, 19]
  next_obligation: "turn finite-volume interior-support geodesic stabilization into an environment-factor coalescing limit, or certify why iid resampling cannot eliminate the endpoint phase coin"
```
