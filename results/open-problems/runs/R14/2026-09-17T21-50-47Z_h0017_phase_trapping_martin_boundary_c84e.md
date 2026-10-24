Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `L_cone: pi/4 -> pi/4`; unchanged-count remains `UNKNOWN -> UNKNOWN`. Methods actually tried: #1 CHANGE THE CATEGORY, #22 READ THE FAILURES NOT THE SUCCESSES, #28 REPLACE FOR ALL WITH FOR TYPICAL.**

# R14 HARD OUTSIDE — H0017: tropical shock paths are phase-trapped; spatial Palm interpolation cannot manufacture a new corner tail class

Repository / branch: `yspennstate/math-open-problems` / `master`.  
Date: 2026-09-17 UTC.

## 1. Continuity, ownership, exclusions, and source freshness

I did **not** reopen the original negative-margin spherical Gaussian perceptron. Its last supported handoff bracket remains

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`,

with width

`6.48139658710`.

The intervening I0089 Riesz target and `RS-2026-BIS32` MinBis/MaxBis target also remain handed off after their hard-task recovery limits. In particular, the source statement printed in the native scheduler prompt is historical rather than the controlling current R14 repository assignment.

The active exclusive target remains **H0017**, Daniel Ahlberg, Maria Deijfen and Matteo Sfragara, *Surviving from the tip of a cone in competing first-passage percolation*, arXiv:2607.07589v1 (8 July 2026), under `operations/claims/H0017.md`.

At run start I recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the H0017 exclusive claim, the targeted H-intake record, and the newest complete R14 report

`runs/R14/2026-09-17T20-52-43Z_h0017_positive_temp_mixture_no_go_4fa7.md`.

The current root ledger still contains the older static R14/perceptron row and explicitly instructs R-series workers to recover newer complete own reports before replacing prior state. The H0017 claim and the complete R14 report are newer and controlling for this worker. No peer file or shared root was edited.

A fresh primary-source search again found arXiv:2607.07589v1 as the source-matching cone-survival preprint. I found no later primary paper claiming the full all-direction theorem. The source still proves the `pi/2` survival threshold in directions whose one-type asymptotic shape has the required tangent line, while the general all-direction question remains the stated Benjamini problem. This is bounded negative evidence only, not a novelty certificate.

The targeted intake read remains honest rather than pretending the connector rendered roughly 780 JSONL rows: H0017 is `CONFIRMED` in `probability_1000_intake_H_20260914/intake_H_verification.md`, with its canonical row in `probability_1000_intake_H_20260914/problems.jsonl`.

I also checked neighboring FPP work. The old R07 fluctuation/KPZ and R08 strict-convexity tracks have rotated to other outside problems, and no competing H0017 claim surfaced. Historical R07/R08 reports remain useful failure evidence but do not create ownership overlap.

## 2. Source model, fixed metric, and retained reductions

The H0017 source model is nearest-neighbor FPP on `Z^2` with iid continuous nonnegative edge weights satisfying

`E[min{omega_1,...,omega_4}^2] < infinity`.

Type 2 starts at the origin and type 1 starts from an infinite cone with opening parameter `alpha` and axis/direction `theta`. Let `G^{theta,alpha}` denote survival of type 2.

For a fixed source-admissible law `F`, write

`alpha_c^F(theta) := sup{alpha : P_F(G^{theta,alpha})>0}`

in the endpoint convention used by the source. The frozen source-wide metric is

`L_cone := inf_F inf_theta alpha_c^F(theta)`.

The source gives the unconditional all-direction baseline

`L_cone >= pi/4`,

and full closure is `L_cone = pi/2` because the flat half-plane case is already extinct and the survival side is monotone in the cone opening.

Retained R14 self-check reductions, all still `0/2` external audits, are:

1. If `C_*(F)` is the deterministic closed Ahlberg--Hoffman set of supporting functionals realized by random coalescing geodesics, then in the endpoint sense

   `alpha_c^F(theta) = pi/2 - dist(theta,C_*(F))`.

2. Therefore

   `ell(F):=inf_theta alpha_c^F(theta)=pi/2-covrad(C_*(F))`.

3. `ell(F)=pi/4` forces `C_*(F)` to be one four-point quarter-turn orbit; full `D4` symmetry further reduces the exact boundary states to the axis orbit or the diagonal orbit.

4. One genuinely new midpoint coalescing slope in an exact four-ray law would, by `D4` symmetry, supply four new midpoint slopes and force `ell(F)>=3pi/8`. This is law-level only and does not move the universal `L_cone`.

5. Ordinary arithmetic interpolation of endpoint Busemann cocycles cannot create a new calibrated edge: for `B^t=(1-t)B^-+tB^+`, zero calibration defect requires zero defect at both endpoints.

6. Ordinary positive-temperature harmonic interpolation is exactly a path-law endpoint mixture. If `h_c=h^-+exp(beta c)h^+`, then the Doob path law satisfies

   `Q_c^x=(1-q_c(x))Q_-^x+q_c(x)Q_+^x`,

   and the natural one-point response/Palm bias integrates exactly to the half-half endpoint mixture.

This run keeps the metric fixed:

`L_cone: pi/4 -> pi/4`.

The authoritative unchanged-run field available to this worker is still `UNKNOWN`, so I preserve `UNKNOWN -> UNKNOWN` rather than inventing a streak.

## 3. Fresh structural literature check

The current source remains Ahlberg--Deijfen--Sfragara, arXiv:2607.07589. Their theorem uses Busemann-linear infinite geodesics and local modification to obtain the `pi/2` threshold in tangent directions.

Ahlberg--Hoffman, *Random coalescing geodesics in first-passage percolation* (arXiv:1609.02447; Ann. Probab. 2019), is the structural reference for the realized slope set. Their terminology is important here: a supporting functional need not be tangent. A functional is tangent when its supporting line is the unique supporting line at some boundary point. Their deterministic closed set `C_*` of Busemann slopes contains all tangent functionals, but the theorem does not state that all supporting functionals inside the normal cone of a corner belong to `C_*`. They also show that every ordinary infinite geodesic has an asymptotically linear Busemann functional lying in the realized closed set.

Damron--Hanson, *Busemann functions and infinite geodesics in two-dimensional first-passage percolation* (arXiv:1209.3036; CMP 2014), remains the closest positive construction theorem. Their distributional point-to-hyperplane/geodesic-graph framework produces coalescing geodesic graphs and no infinite backward paths in the limits they construct. What I did **not** find is a theorem saying that an arbitrary non-tangent supporting functional strictly inside a corner normal cone is realized by such a point-to-hyperplane limit in the present iid model.

The most useful negative comparison this run is Kenneth Alexander and Quentin Berger, *Geodesics Toward Corners in First Passage Percolation* (arXiv:1709.09072; J. Stat. Phys. 2018). They construct a stationary planar FPP example with an octagonal limit shape in which semi-infinite geodesics exist only in the four coordinate-axis directions, with multiple geodesics in each such direction. It is not the H0017 iid source model, but it proves that stationarity, planarity, Bellman/recovery structure, and polygonal convex geometry alone cannot force geodesics corresponding to all corner supports. Any source-valid completion has to use iid/finite-energy information in an essential way.

## 4. Method #1 — CHANGE THE CATEGORY: from cone geometry to the extremal max-plus boundary

The preceding positive-temperature run showed that linear combinations of two endpoint harmonic functions live inside a two-ray positive cone and are path-law mixtures. This run tests the zero-temperature analogue more sharply.

Use the same sign convention as the preceding R14 reports. Let `h^-` and `h^+` be two endpoint recovering/Busemann potentials associated with the two sides of a missing supporting-functional interval. For every vertex `x`,

`h^\pm(x) = max_{y~x} { h^\pm(y) - omega_xy }`.                         (14.1)

Write

`D(x):=h^+(x)-h^-(x)`.

For `c in R`, form the max-plus/tropical interpolation

`H_c(x):=max{h^-(x), h^+(x)+c}`.                                      (14.2)

Because the Bellman operator commutes with finite maxima,

`H_c(x)=max_{y~x}{H_c(y)-omega_xy}`.                                  (14.3)

Thus `H_c` is again a recovering potential. This fact alone once made the tropical shock look promising: perhaps a spatial Palm measure on the interface of the two phases could select a new geodesic state.

The exact result below rules out that naive interpretation.

### Lemma R14-H0017-L14.1 — endpoint calibration makes the Busemann difference monotone

If an oriented edge `x -> y` is `h^-`-calibrated, meaning

`h^-(x)=h^-(y)-omega_xy`,                                              (14.4)

then

`D(y) <= D(x)`.                                                        (14.5)

If `x -> y` is `h^+`-calibrated, then

`D(y) >= D(x)`.                                                        (14.6)

#### Proof

For a minus-calibrated edge, the Bellman inequality for `h^+` gives

`h^+(x) >= h^+(y)-omega_xy`.

Subtracting (14.4) yields

`h^+(x)-h^-(x) >= h^+(y)-h^-(y)`,

which is (14.5). The plus case is symmetric. `QED`

This is an elementary but useful monovariant: the shock coordinate can only move one way while a path follows one endpoint calibration graph.

### Lemma R14-H0017-L14.2 — phase trapping for every tropical calibrated path

Define the three phases

`A_c^- := {x : D(x)+c < 0}`,

`I_c   := {x : D(x)+c = 0}`,

`A_c^+ := {x : D(x)+c > 0}`.                                         (14.7)

Let `x_0,x_1,...` be any infinite `H_c`-calibrated path, i.e.

`H_c(x_k)=H_c(x_{k+1})-omega_{x_k x_{k+1}}` for all `k`.              (14.8)

Then the following pathwise classification holds.

**(a) Minus phase is forward absorbing.** If `x_k in A_c^-` for some `k`, then every `x_j` with `j>=k` lies in `A_c^-`, and every subsequent edge is `h^-`-calibrated.

**(b) Plus phase is forward absorbing.** If `x_k in A_c^+`, then every later vertex lies in `A_c^+`, and every subsequent edge is `h^+`-calibrated.

**(c) A tie-to-tie calibrated edge is calibrated by both endpoint potentials.** If `x_k,x_{k+1} in I_c`, then the edge is simultaneously `h^-`- and `h^+`-calibrated.

Consequently, every infinite `H_c`-calibrated path has exactly one of the following forms:

- it stays in `I_c` forever, using only edges calibrated by **both** endpoints; or
- it follows a finite (possibly empty) tie segment, exits once into `A_c^-`, and thereafter is a minus-endpoint calibrated path forever; or
- it follows a finite (possibly empty) tie segment, exits once into `A_c^+`, and thereafter is a plus-endpoint calibrated path forever.

In particular an `H_c`-calibrated path can never enter a strict phase and later return to the interface or cross to the other phase.

#### Proof

Suppose first that `x in A_c^-` and `x -> y` is `H_c`-calibrated. Since `H_c(x)=h^-(x)`, there are three possibilities for `y`.

If `y in A_c^+`, then

`h^-(x)=H_c(x)=H_c(y)-omega_xy=h^+(y)+c-omega_xy`.

The Bellman inequality for `h^+` gives

`h^+(x) >= h^+(y)-omega_xy`,

hence

`h^+(x)+c >= h^-(x)`,

contradicting `x in A_c^-`.

If `y in I_c`, then `H_c(y)=h^-(y)=h^+(y)+c`, so (14.8) says the edge is `h^-`-calibrated. Lemma L14.1 then gives

`D(y) <= D(x)`.

But `D(y)+c=0` while `D(x)+c<0`, so `D(y)>D(x)`, a contradiction.

Therefore `y in A_c^-`. In that case `H_c(y)=h^-(y)` and (14.8) is exactly minus calibration. Iteration proves (a). Part (b) is symmetric.

For (c), if both endpoints lie in `I_c`, then

`H_c(x)=h^-(x)=h^+(x)+c`,

`H_c(y)=h^-(y)=h^+(y)+c`.

Equation (14.8) therefore gives both

`h^-(x)=h^-(y)-omega_xy`

and

`h^+(x)=h^+(y)-omega_xy`.

Finally, a path beginning on `I_c` either never leaves it, or has a first exit time. A tie-to-strict edge is calibrated by the target endpoint potential, and parts (a)/(b) then trap the path in that phase forever. `QED`

### Categorical consequence

This lemma is stronger than the previous one-edge statement “a calibrated edge cannot cross directly from strict minus to strict plus.” It classifies the **entire tail** of every tropical interpolant path.

The zero-temperature max of two endpoint recovering states therefore does not manufacture a third path geometry. Any calibrated ray of `H_c` is, after a finite initial interface segment, already a ray in one endpoint calibration graph; the only alternative is an infinite path whose every edge is calibrated by both endpoint potentials.

I do **not** claim that the common-calibrated alternative is impossible. At a corner the two endpoint support functionals can agree on the primal corner ray, so a common-calibrated corner-directed geodesic is precisely one of the geometries that may exist. The point is narrower and exact: the tropical max does not *create* such a path. Its existence must already be proved inside the intersection of the endpoint calibration graphs.

This changes the useful category. The missing corner state is not obtainable by an ordinary convex combination at positive temperature, nor by the max-plus semilattice generated by two endpoint potentials at zero temperature. A successful construction must provide a genuinely new extremal/minimal recovering state outside those two generated objects. “Minimal Martin/max-plus boundary point” is the right analogy, although I am not promoting that analogy to a theorem identifying a pre-existing FPP Martin boundary.

## 5. Method #28 — REPLACE FOR ALL WITH FOR TYPICAL: the spatial-Palm shock proposal is also trapped

The previous run left one possible loophole: perhaps an ordinary endpoint interpolation is nonextremal, but Palm conditioning on a **typical spatial crossing** of the shock interface could produce an extremal interior state.

Lemma L14.2 is pathwise, before any averaging or conditioning. Therefore any Palm law built from pairs `(omega,c)` and an `H_c`-calibrated path remains supported on the same three path types above:

1. endpoint-minus tail after a finite interface prefix;
2. endpoint-plus tail after a finite interface prefix;
3. an infinite common-calibrated path in `I_c`.

A Palm bias can change the frequency with which these possibilities are sampled, and it might expose an exceptional common-calibrated path that was hard to select under the original law. But it cannot create a new calibrated tail outside the endpoint/common calibration graphs. To turn such a Palm object into an H0017 solution one would still have to prove, under the **original iid law** and with a source-valid covariant selection, that a common-calibrated interior-corner geodesic exists and yields the required coalescing Busemann slope.

Thus the “typical crossing rather than every `c`” quantifier swap does not by itself evade the corner-geodesic problem. It merely changes the sampling of paths whose geometry was already present before conditioning.

This is the certified obstruction produced by method #28. It is useful because it prevents a future run from spending another hour on a more elaborate Palm normalization of the same max-plus endpoint shock.

## 6. Method #22 — READ THE FAILURES: what an iid proof must contain that stationary geometry does not

Alexander--Berger's *Geodesics Toward Corners in First Passage Percolation* is the cleanest failure model for the current route. Their stationary planar construction has an octagonal limit shape but semi-infinite geodesics only in the four axis directions, with multiple geodesics in each axis direction. In particular, corner geometry plus stationarity does not force a geodesic for each support direction.

This failure has a direct methodological consequence. Any argument for H0017 based only on the following ingredients is too weak:

- planar ordering/non-crossing;
- stationarity or translation covariance;
- deterministic convex geometry of the limit shape;
- Bellman/recovering cocycle identities;
- compactness of infinite geodesics;
- interpolation of already available endpoint states.

All of these structures can coexist with a polygonal shape and missing corner geodesic directions outside the iid source class.

What Alexander--Berger do **not** have, and what H0017 does have, is iid finite-energy randomness on every scale. Therefore a credible new route has to use independence in a way that cannot be reproduced by a coherent stationary highway construction. The likely shape of such an argument is not a one-box local surgery: a finite resampling can change an initial segment but cannot by itself create a new asymptotic coalescence class. The missing ingredient should be an infinite-scale use of iid, for example independent opportunities in separated annuli, a uniqueness/extremality argument for point-to-hyperplane states, or a zero-one/mass-transport mechanism that makes a missing normal interval incompatible with infinitely many independent local perturbations.

This literature failure also prevents an overclaim about the current reduction: “every supporting functional should have a geodesic” is false for stationary FPP in general. It is specifically an **iid strengthening** that has to be proved.

## 7. A sharper source-valid target: interior point-to-hyperplane extremality

Damron--Hanson suggest a way to separate the two hard obligations that earlier R14 reports treated together. Their distributional limits of geodesic graphs have strong coalescence and backward-finiteness properties. Ahlberg--Hoffman use tangent functionals to enter this framework and then classify the resulting random coalescing geodesics.

This suggests the following smallest source-moving target for a future run.

Let `rho^-` and `rho^+` be the two realized endpoint support functionals bounding a nonempty gap of `C_*(F)`, and let `rho` lie strictly between them in the normal cone of the same corner. Construct, using iid point-to-hyperplane finite-volume geodesics rather than interpolation of existing infinite states, a subsequential invariant geodesic-graph limit whose mean/asymptotic support functional is **rho itself** and whose law is extremal rather than an endpoint mixture.

If this object can be put inside the Damron--Hanson class for which the geodesic graph coalesces and has no infinite backward paths, then the second obstruction may come for free: one would have a new random coalescing geodesic with an interior support functional, contradicting that `(rho^-,rho^+)` is a gap of `C_*`.

I did not find a published theorem that performs this construction for an arbitrary **non-tangent** functional in the interior of a corner normal cone under only the H0017 source assumptions. Existing tangent-function constructions therefore do not already solve the source.

The key distinction from every exhausted R14 interpolation is that `rho` would be imposed at **finite volume through the target hyperplanes/boundary condition before taking the infinite-volume limit**. It would not be synthesized afterward from two already-existing endpoint infinite-volume states.

This is the most promising remaining route because it uses a source-native finite-volume object and gives iid randomness a chance to select a new extremal state before convex decomposition occurs.

## 8. What moved intellectually, and what did not move metrically

There is **no fixed-metric movement** this run. The rigorous universal endpoint remains

`L_cone = at least pi/4`,

so the tracked value is

`pi/4 -> pi/4`.

What did change is the route classification:

- positive linear endpoint interpolation is already known to be an exact endpoint path-law mixture;
- this run proves that zero-temperature max-plus endpoint interpolation is also sterile at the **tail geometry** level: every calibrated path is phase-trapped into one endpoint graph after a finite interface segment, unless it was common-calibrated all along;
- a spatial Palm conditioning of that same tropical interface cannot bypass the pathwise classification;
- Alexander--Berger shows that stationarity/planarity/corner geometry alone cannot force the missing state;
- therefore a source-moving proof has to use iid randomness before the infinite-volume state has decomposed, with finite-volume point-to-hyperplane extremal limits now the cleanest target.

This is a certified obstruction and a sharper handoff, not a theorem closing H0017.

## 9. Next genuinely different methods

The next unused H0017 triple is:

- **#7 TAKE THE LIMIT.** Start with finite-volume point-to-hyperplane geodesic graphs aimed at one strictly interior corner functional `rho`; vary the boundary condition in finite volume and take subsequential limits before comparing with the endpoint states.
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE.** Search directed LPP/Burgers/second-class-particle and minimal-boundary literature only for an extremality-selection mechanism that survives the undirected iid FPP setting. Do not import integrable formulas or directed-model conclusions as source theorems.
- **#24 FIND THE EXTREMAL OBJECT.** Among all invariant point-to-hyperplane subsequential limits with prescribed interior support functional, choose an ergodic/extreme law and test whether endpoint decomposition is compatible with its prescribed mean slope. The target is a genuinely new extreme state, not another interpolant.

The remaining unused H0017 moves after that triple are #8, #16, #19.

## 10. Honest status and closure discipline

H0017 remains **OPEN / PARTIAL**.

New theorem-sized self-check this run:

`R14-H0017-L14.2`: every calibrated path of the max-plus endpoint interpolant `H_c=max(h^-,h^++c)` is phase-trapped; after a finite tie segment it stays forever in one endpoint calibration graph, unless it remains forever on common-calibrated tie edges.

Supporting self-check:

`R14-H0017-L14.1`: the Busemann difference `D=h^+-h^-` is nonincreasing on minus-calibrated edges and nondecreasing on plus-calibrated edges.

These are full elementary proofs on the page. No exact-arithmetic checker was created because there is no finite computational core. External audits remain `0/2`. No paper folder is created and no closure label is used.

The bounded prior-art search found no later primary H0017 resolution and no published iid theorem filling arbitrary non-tangent corner support functionals by random coalescing geodesics. Negative search evidence does not establish novelty.

## 11. Model / scheduler-control truthfulness

The exposed task interface still has prompt/title/schedule/timing/enablement controls but no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry. The actual model exposed to this run is **GPT-5.6 Sol**; reasoning effort is not exposed and is therefore reported as `UNVERIFIED`. GPT-6/maximum remains prompt text only on this surface.

The repository ledger also records that the historical P26 `You cannot modify this task` result was authorization-context dependent: P26 later updated successfully from an authorized P/C context. If a task ID still rejects modification, the legitimate path is its authorized owning workspace/account context or platform support, not duplication or permission bypass. No scheduler or permission change was attempted here.

## 12. Structured ledger delta

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
  methods_this_run: [1, 22, 28]
  new_self_checks:
    - R14-H0017-L14.1 endpoint-calibrated edges make D=h_plus-h_minus monotone
    - R14-H0017-L14.2 full phase-trapping classification for tropical calibrated paths
    - spatial Palm conditioning on the same tropical endpoint shock cannot create a calibrated tail outside endpoint/common calibration graphs
  external_audits: 0/2
  certified_obstruction: >-
    Both ordinary positive harmonic interpolation and zero-temperature max-plus interpolation
    of two existing endpoint states are structurally sterile for creating a new corner tail class.
    The max-plus case is pathwise: a calibrated path exits the tie set at most once and is then
    trapped forever in one endpoint calibration graph, unless it is common-calibrated forever.
  literature_failure: >-
    Alexander-Berger give a stationary non-iid planar FPP model with an octagonal limit shape
    but semi-infinite geodesics only in the four axis directions, so stationarity, planarity,
    Bellman recovery, and corner geometry alone cannot force the missing corner state.
  remaining_obligation: >-
    Use iid randomness essentially to construct a genuinely new extremal state for a strictly
    interior non-tangent corner supporting functional, preferably as a finite-volume
    point-to-hyperplane subsequential limit; then place it in a coalescing geodesic-graph class.
  next_methods: [7, 17, 24]
```
