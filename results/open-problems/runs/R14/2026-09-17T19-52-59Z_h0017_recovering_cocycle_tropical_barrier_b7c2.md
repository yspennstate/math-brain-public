Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `L_cone: pi/4 -> pi/4`; unchanged-count field remains `UNKNOWN -> UNKNOWN`. Methods actually tried: #10 DERANDOMIZE, #13 FIND WHAT ONLY INCREASES, #26 HUNT THE SPORADIC CASE.**

# R14 HARD OUTSIDE — H0017: generalized recovery already gives geodesics; coalescence is the missing bridge, and both linear and max-plus endpoint interpolation fail locally

Repository / branch: `yspennstate/math-open-problems` / `master`.  
Date: 2026-09-17 UTC.

## 1. Continuity, ownership, exclusions, and source freshness

I did **not** reopen the original negative-margin spherical Gaussian perceptron. Its supported handoff bracket remains

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`,

with width `6.48139658710`. I0089 and RS-2026-BIS32 likewise remain handed off after their hard-task recovery limits.

The active exclusive R14 target remains **H0017**, Daniel Ahlberg, Maria Deijfen and Matteo Sfragara, *Surviving from the tip of a cone in competing first-passage percolation*, arXiv:2607.07589v1 (8 July 2026), under `operations/claims/H0017.md`.

At run start I recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the current owner directive, the H0017 claim, and the newest own report

`runs/R14/2026-09-17T18-50-23Z_h0017_midpoint_cocycle_flux_7d3a.md`.

I also checked current neighboring work. The former R08 FPP strict-convexity route is no longer an active neighboring H0017 owner; R08 has rotated to F0083 and its latest report is a stuck-recovery report there. No current peer report claims H0017.

Fresh primary-source checking this run found no later source-matching resolution. The arXiv record for 2607.07589 is still v1 dated 8 July 2026. Its Theorem 1 proves the Benjamini threshold in directions where the asymptotic shape has a tangent, and its Theorem 5 proves extinction for the flat `alpha=pi/2` case in every direction. The paper itself records the unconditional all-direction `pi/4` survival baseline from lattice symmetry/convexity and available linear Busemann directions.

The most useful additional source this run is Sean Groathouse, Christopher Janjigian and Firas Rassoul-Agha, *Existence of generalized Busemann functions and Gibbs measures for random walks in random potentials*, arXiv:2306.17714v2 / Trans. AMS 378 (2025). Their framework includes first-passage percolation and proves existence of recovering cocycles; at zero temperature the recovery property can be turned, using a covariant tie-breaker, into a semi-infinite geodesic. This corrects the phrasing of my preceding report: **existence of a calibrated semi-infinite path from a recovering cocycle is not itself the missing theorem.** What is missing for H0017 is the stronger bridge to the Ahlberg--Hoffman random-*coalescing* class and its ordinary asymptotically linear Busemann functional.

I do **not** claim that every H0017 source-admissible law automatically satisfies every technical hypothesis of the generalized-Busemann theorem in exactly the form needed here. H0017 assumes continuity plus the square moment of the minimum of four incident weights; the generalized-RWRP theorem has its own integrability/ergodicity hypotheses. I therefore use it as a rigorous route on its certified overlap with the source class, not as a source-wide closure theorem.

This is a bounded dated prior-art search, not a novelty certificate.

## 2. Frozen metric and retained reductions

For a source-admissible iid continuous passage-time law `F`, retain

`alpha_c^F(theta) := sup { alpha : P_F(G^{theta,alpha}) > 0 }`

and

`L_cone := inf_F inf_theta alpha_c^F(theta)`.

The source certifies

`L_cone >= pi/4`,

and full source closure is `L_cone=pi/2`.

The retained R14 self-check reductions remain:

`alpha_c^F(theta) = pi/2 - dist(theta,C_*(F))`                              (R2)

in the endpoint sense (survival below / extinction above), where `C_*(F)` is the deterministic closed Ahlberg--Hoffman set of slopes of random coalescing geodesics;

`ell(F) := inf_theta alpha_c^F(theta) = pi/2 - covrad(C_*(F))`;             (R2')

`ell(F)=pi/4  <=>  C_*(F) is exactly one four-point quarter-turn orbit`;   (R4)

and full `D4` symmetry sharpens the equality state to exactly the axis orbit or the diagonal orbit (R7).

Metric this run:

`L_cone: pi/4 -> pi/4`.

The supported unchanged-run field is still unknown in the authoritative state available to this worker, so it remains `UNKNOWN -> UNKNOWN`; no stagnation count is invented.

## 3. Method #10 — DERANDOMIZE: generalized recovery already produces a genuine geodesic

The preceding report isolated a “midpoint cocycle realization problem” and treated existence of an infinite calibrated path as the main missing step. The generalized-Busemann literature lets us remove that part of the obstruction, subject to its hypotheses.

At zero temperature a recovering cocycle `B` satisfies a one-step recovery equation: at every vertex there is at least one admissible outgoing step on which the cocycle saturates the edge cost (up to the sign convention used in the RWRP paper). Groathouse--Janjigian--Rassoul-Agha explicitly show that a covariant deterministic tie-breaker selects one such step at every vertex, and the resulting path is a semi-infinite geodesic. The geodesic conclusion follows because recovery plus the cocycle identity makes every finite segment passage-time minimizing.

Thus, if one can construct a stationary recovering cocycle with a desired corner-interior mean slope, there is already a canonical way to **derandomize it into a geodesic forest**.

What this does *not* give is exactly what H0017 needs. Ahlberg--Hoffman's set `C_*` is defined through **random coalescing geodesics**, and their Theorem 12.1 associates to each such coalescing geodesic a unique supporting functional and an ordinary Busemann function asymptotically linear to that functional. The generalized-Busemann paper does not prove coalescence of the zero-temperature forest in undirected FPP; indeed its discussion of geodesic structure leaves such questions open.

This sharpens the missing bridge to:

> **CR (coalescing-realization problem).** Given a translation-covariant recovering cocycle in planar iid continuous FPP whose mean is a supporting functional `rho` and whose calibrated paths are directed into the corresponding primal face, find a translation-covariant selection of calibrated geodesics that has one coalescence class; then identify the cocycle with the ordinary Busemann cocycle of that class.

The last identification is straightforward *once coalescence is known*: if calibrated geodesics from `x` and `y` coalesce at `z`, then recovery gives

`B(x,z)=T(x,z)` and `B(y,z)=T(y,z)`,

so

`B(x,y)=T(x,z)-T(y,z)`,

which is exactly the stabilized passage-time difference along their common tail. Hence `B` is the ordinary Busemann cocycle of the coalescing family.

Ahlberg--Hoffman do prove a half-plane coalescence theorem for the particular random non-crossing geodesics produced by their label construction. But the proof uses additional finite-modification/label structure of that class. I found no theorem permitting me to replace their class by an arbitrary generalized recovering cocycle forest. Treating Proposition 9.2 as if it applied automatically would be an unjustified leap.

So method #10 materially narrows the obstruction: **calibrated path existence is solved machinery; coalescence plus source-assumption matching is not.**

## 4. Method #13 — FIND WHAT ONLY INCREASES: two exact interpolation obstructions, then a tropical family

This method tested whether the two endpoint Busemann cocycles of a missing corner interval can be interpolated explicitly.

Let `B^-` and `B^+` be the ordinary Busemann cocycles of the neighboring random coalescing endpoint geodesics, and use the R14 sign convention

`B^±(x,y) <= T(x,y)`.

For an oriented nearest-neighbor edge `e=(x,y)`, write

`q_e^± := omega_e - B^±(x,y) >= 0`.

### R14-H0017-R9 — strict linear interpolation can only *lose* calibrated edges

For `t in (0,1)`, set

`B^t := (1-t)B^- + t B^+`.

Then exactly

`q_e^t := omega_e - B^t(x,y) = (1-t)q_e^- + t q_e^+`.

Since both endpoint defects are nonnegative,

`q_e^t = 0  <=>  q_e^- = q_e^+ = 0`.                                   (R9)

Thus the calibrated-edge set of every strict convex interpolation is precisely the **intersection** of the endpoint calibrated-edge sets. Linear interpolation cannot create a new calibrated route; it can only discard endpoint-calibrated edges.

In particular, the midpoint average from the preceding report is recovering at a vertex only if the two endpoint cocycles possess a common zero-defect outgoing edge there. This is the local obstruction that was missing from the previous “average the cocycles and realize the midpoint” formulation.

The proof is the displayed identity; no finite checker is needed.

### A different interpolation that *does* preserve recovery: max-plus / tropical interpolation

The linear failure suggests using the algebra of the zero-temperature dynamic-programming equation rather than ordinary convexity.

Normalize endpoint potentials by

`h^±(x) := B^±(0,x)`,  so `h^±(0)=0`.

Metric domination and recovery imply the max-plus harmonic equation

`h^±(x) = max_{y~x} { h^±(y) - omega_{xy} }`.                            (6)

For a real parameter `c`, define

`H_c(x) := max{ h^-(x), h^+(x)+c }`,

up to an irrelevant additive normalization. Because the Bellman operator in (6) commutes with pointwise maximum,

`H_c(x) = max_{y~x} { H_c(y) - omega_{xy} }`.

Hence

`B_c(x,y):=H_c(y)-H_c(x)`

is again an additive metric-dominated **recovering cocycle** for every `c` (not stationary under ordinary spatial shifts at fixed `c`, but recovering pathwise).

This gives a genuine one-parameter family connecting the two endpoint correctors in the correct zero-temperature algebra.

### R14-H0017-R10 — branch phase is conserved along a calibrated path except at tie vertices

Define the two strict phases

`A_c^- := {x : h^-(x) > h^+(x)+c}`,

`A_c^+ := {x : h^+(x)+c > h^-(x)}`,

and the tie set

`I_c := {x : h^-(x)=h^+(x)+c}`.

If `x in A_c^-` and `y in A_c^+` are neighbors, then the edge `x->y` cannot be calibrated for `B_c`. Indeed,

`H_c(y)=h^+(y)+c <= h^+(x)+c+omega_{xy} < h^-(x)+omega_{xy}=H_c(x)+omega_{xy}`.

So strict inequality rules out recovery on that edge. The same argument with the signs reversed handles `A_c^+ -> A_c^-`.

Therefore every `B_c`-calibrated geodesic can switch from one endpoint phase to the other **only through the tie set `I_c`**. Away from ties, the active endpoint branch is conserved along calibrated motion.

Consequences:

1. max-plus interpolation preserves the recovery equation but generically does **not** manufacture a mixed midpoint geodesic;
2. an infinite path that genuinely mixes the two endpoint phases must encounter infinitely many vertices of one fixed level set

   `h^+(x)-h^-(x) = -c`;

3. the naive “shock corrector” route has therefore been reduced to a level-set/percolation problem for the Busemann-difference cocycle, not to another cocycle identity.

This is a certified obstruction and a more useful next object than the sterile first-moment flux from the previous run.

### Exact skew-covariance of the tropical family

Let

`D(z):=h^+(z)-h^-(z)`.

Using cocycle covariance, translating by `z` changes the tropical parameter by exactly `D(z)`:

`B_c^omega(x+z,y+z) = B_{c+D(z)}^{T_z omega}(x,y)`.                      (7)

Since `D` is itself an additive cocycle, `(omega,c) -> (T_z omega,c+D(z))` is a `Z^2` action. Lebesgue measure in `c` is translation-invariant, so `P(domega) dc` is an invariant **sigma-finite** measure for this skew product.

That observation suggests a nontrivial future route: Palm-normalize this sigma-finite ensemble on a level-set/interface crossing and study the resulting shock path. But (R10) proves that the path must be supported by repeated ties; one cannot simply choose a generic `c` and expect a new interior-slope geodesic.

R9--R10 are complete on-page self-checks, with `0/2` external audits. They do not move `L_cone`.

## 5. Method #26 — HUNT THE SPORADIC CASE: the two exact `pi/4` boundary states have a discrete midpoint jump

The retained D4 argument says that if a law attains the law-level boundary

`ell(F)=pi/4`,

then `C_*(F)` is either the four axis slopes or the four diagonal slopes. Hence every maximal missing interval has angular width exactly `pi/2`, and its midpoint is the other D4 orbit.

This gives a useful discrete jump lemma.

### R14-H0017-R11 — midpoint insertion in an exact four-ray state forces an eight-ray state

Assume `ell(F)=pi/4`, and suppose for one maximal gap we can produce a random coalescing geodesic whose Busemann slope is exactly the midpoint of that gap. By D4 invariance, all four rotated midpoint slopes lie in `C_*`. Together with the original four endpoint slopes this yields eight equally spaced slopes. Consequently

`covrad(C_*) <= pi/8`

and therefore

`ell(F) >= pi/2 - pi/8 = 3pi/8`.                                       (R11)

In particular, midpoint insertion contradicts the assumption `ell(F)=pi/4` outright.

This does **not** move the universal metric `L_cone`: even if exact equality were excluded law by law, a sequence of admissible laws could still have `ell(F_n) downarrow pi/4`. A universal metric improvement requires quantitative control that is uniform over the whole source class.

Nevertheless R11 identifies the sharp sporadic target. At the exact boundary, it is enough to construct **one** genuinely new coalescing midpoint corrector. There is no need to fill an entire corner interval at once.

Combining methods #10 and #13 shows exactly what such a proof must do:

- generalized recovering-cocycle theory can produce geodesics for suitable correctors, but coalescence is not supplied;
- ordinary convex averaging of the endpoint cocycles cannot create calibrated edges (R9);
- max-plus interpolation preserves recovery, but the endpoint branch is conserved except on a Busemann-difference level set (R10).

So the exact four-ray case has become a concrete **shock/coalescence problem**: construct a translation-covariant or Palm-stationary geodesic supported by an interface of the endpoint correctors and prove that its induced family coalesces.

## 6. Nearest solved mechanism and why it does not yet port

There are two nearby rigorous mechanisms, and the gap between them is now explicit.

1. **Generalized recovering cocycles (Groathouse--Janjigian--Rassoul-Agha).** Recovery plus a covariant tie-breaker gives semi-infinite geodesics and strong direction control under their hypotheses. What is not supplied is planar one-class coalescence for the resulting undirected-FPP forest.

2. **Ahlberg--Hoffman random coalescing geodesics.** Their Proposition 9.2 proves coalescence for their random non-crossing half-plane geodesics, and their Theorem 12.1 then gives the asymptotically linear ordinary Busemann functional. But their coalescence proof uses the special label/finite-modification structure of the geodesics constructed in their framework; I found no source saying an arbitrary recovering-cocycle forest automatically lies in that class.

The bridge to prove is therefore not “recovering cocycle -> geodesic” but

`recovering cocycle + iid planar structure -> coalescing geodesic family`.

A route that proves only existence of another semi-infinite corner-directed geodesic is PARTIAL: H0017 needs the Busemann functional controlling the whole source cone, not merely a path with the correct Euclidean direction.

## 7. What changed mathematically this run

There is no fixed-metric movement, but the obstruction has been materially refined.

Before this run the working sentence was “construct the midpoint cocycle and find an infinite calibrated path.” After this run:

- generalized-Busemann theory removes calibrated-path existence as the main conceptual obstacle (on its verified hypothesis range);
- **coalescence** is isolated as the missing structural bridge to `C_*`;
- strict linear interpolation is proved locally sterile by the exact defect identity R9;
- the natural zero-temperature max-plus interpolation is constructed explicitly, but R10 proves that its calibrated paths cannot cross between endpoint phases except through a fixed Busemann-difference level set;
- in the exact four-ray boundary state, a successful midpoint coalescence theorem would force the discrete jump `pi/4 -> 3pi/8` at the law level.

This is a better research target than another first-moment estimate or another checker.

## 8. Next route

Next genuinely different H0017 triple:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT.** Introduce positive temperature into the endpoint correctors. At finite beta, linear combinations of positive harmonic functions remain harmonic; study whether an extremal zero-temperature limit can avoid the phase-locking obstruction R10 rather than collapse to an endpoint mixture.
- **#18 SAY IT IN ANOTHER LANGUAGE.** Recast R10 as a random Hamilton--Jacobi shock/interface problem. Use the sigma-finite skew-invariant measure `P(domega)dc` and Palm-normalize on interface crossings; ask whether the Palm interface carries a geodesic/coalescing class.
- **#29 ADD THE POINTS AT INFINITY.** Compactify the family of tropical correctors/geodesic forests and analyze extremal invariant limits. The target is an extremal midpoint recovering measure, not an ordinary convex mixture of the two endpoint states.

A source-moving theorem would still need either full coalescing realization for all supporting slopes, giving `L_cone=pi/2`, or a **uniform** angular insertion bound over every admissible law. A law-dependent fifth/eighth slope alone does not move the fixed universal metric.

## 9. Honest status and closure discipline

H0017 remains **OPEN / PARTIAL**.

New self-checks this run:

- R9: strict linear interpolation has calibrated-edge set equal to the intersection of endpoint calibrated-edge sets;
- R10: max-plus interpolation is recovering, but strict endpoint phase cannot change along a calibrated edge; switching requires the tie level set;
- R11: in an exact four-ray boundary state, one midpoint coalescing slope plus D4 symmetry yields eight equally spaced slopes and `ell(F)>=3pi/8`.

External audits: `0/2`.

No checker was created because these are exact analytic Bellman/cocycle identities, not finite computational claims. No paper folder is created; closure conditions are not met.

## 10. Model / scheduler control

The exposed scheduling surface still has no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry. The actual model available to this run is GPT-5.6 Sol, and the reasoning level is not exposed, so it is reported as UNVERIFIED. GPT-6/maximum remains prompt text only on this surface.

The current repository ledger also records that the historical P26 `You cannot modify this task` result was authorization-context dependent: a later full update succeeded from an authorized owning P/C context. If a task still returns that error, the legitimate workaround is to edit from its authorized owning workspace/account context or escalate to platform support. No scheduler change, permission change, duplicate task, or bypass was attempted here.

## 11. Structured ledger delta

```yaml
ledger_delta:
  track: R14
  allocation: HARD_OUTSIDE
  active_target: H0017
  source: arXiv:2607.07589v1
  status: OPEN/PARTIAL
  metric_name: L_cone
  metric_before: pi/4
  metric_after: pi/4
  movement: no
  unchanged_count_before: UNKNOWN
  unchanged_count_after: UNKNOWN
  methods_this_run: [10, 13, 26]
  new_self_checks:
    - R9 linear-interpolation calibrated-edge intersection
    - R10 max-plus recovery plus phase-locking obstruction
    - R11 exact-four-ray midpoint insertion implies law-level 3pi/8 bound
  external_audits: 0/2
  certified_obstruction: >-
    Recovering-cocycle path existence is not the key missing step; planar coalescence is.
    Linear averaging loses calibrated edges, while max-plus interpolation preserves recovery
    but cannot switch endpoint phases except on a fixed Busemann-difference tie set.
  remaining_obligation: >-
    Prove a source-valid coalescing-realization theorem for an interior supporting slope,
    or obtain a uniform angular insertion bound over all source-admissible iid laws.
  next_methods: [5, 18, 29]
```
