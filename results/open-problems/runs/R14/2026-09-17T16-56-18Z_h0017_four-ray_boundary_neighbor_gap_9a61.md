Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `L_cone: pi/4 -> pi/4`; unchanged-count field remains `UNKNOWN -> UNKNOWN`. Methods actually tried: #9 RANDOMIZE, #14 FIND THE GROUP ACTING, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# R14 HARD OUTSIDE — H0017: the pi/4 boundary is exactly the four-geodesic state

Repository / branch: `yspennstate/math-open-problems` / `master`.  
Date: 2026-09-17 UTC.

## 1. Continuity, ownership, and source gate

I did **not** reopen the original negative-margin spherical Gaussian perceptron. Its supported handoff bracket remains

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`,

with width `6.48139658710`. I0089 and RS-2026-BIS32 likewise remain handed off after their hard-task recovery limits.

The active exclusive R14 target remains **H0017**, Daniel Ahlberg, Maria Deijfen and Matteo Sfragara, *Surviving from the tip of a cone in competing first-passage percolation*, arXiv:2607.07589v1 (8 July 2026), under `operations/claims/H0017.md`.

At run start I recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the controlling owner directive, the H0017 claim, the newest own H0017 report, and the newest directly neighboring FPP strict-convexity report I could recover (`runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md`). The intake corpus is too large for a literal connector rendering in one response, so I used the exact H0017 intake/source path plus repository-wide targeted searches rather than pretending to have inspected unseen truncated rows.

Fresh literature checking on 2026-09-17 found:

- arXiv:2607.07589 remains v1 dated 8 July 2026; Ahlberg's current Stockholm research page still lists it as a preprint;
- no later primary paper found by exact title/authors or all-direction cone-survival searches claims the missing theorem;
- Ahlberg--Hoffman, *Random coalescing geodesics in first-passage percolation*, arXiv:1609.02447 / Ann. Probab. 47 (2019), remains the key structural input;
- Ahlberg--Hanson--Hoffman, *The number of geodesics in planar first-passage percolation grows sublinearly*, arXiv:2208.11576, does not rule out the four-geodesic state;
- Jacquet, *Geodesics in first-passage percolation cross any pattern*, arXiv:2204.02021 / EJP 2024, supplies strong local-pattern richness in iid FPP but no theorem filling missing Busemann slopes;
- Brito--Hoffman, *Geodesic rays and exponents in ergodic planar first passage percolation*, arXiv:1912.06338, gives stationary/ergodic non-iid models with exactly four infinite geodesics and an `l1` limit shape, showing that any argument below must genuinely use independence.

This is bounded negative evidence, not a novelty certificate.

## 2. Frozen metric and retained reduction

For source-admissible iid continuous edge law `F`, write

`alpha_c^F(theta) := sup { alpha : P_F(G^{theta,alpha}) > 0 }`.

The source-wide frozen metric is

`L_cone := inf_F inf_theta alpha_c^F(theta)`

in the equivalent endpoint form used by the H0017 claim. The source certifies `L_cone >= pi/4`; full closure is `L_cone=pi/2`.

The preceding R14 report proved on page, as a self-check/reduction with 0/2 external audits, that if `C_*(F)` is the deterministic closed Ahlberg--Hoffman set of Busemann slopes, then

`alpha_c^F(theta) = pi/2 - dist(theta,C_*(F))`,                                      (R2)

with the equality interpreted as equality of supremal endpoints (survival below, extinction above; no assertion at the single endpoint).

Consequently

`ell(F) := inf_theta alpha_c^F(theta) = pi/2 - covrad(C_*(F))`,                       (1)

and

`L_cone = inf_F ell(F) = pi/2 - sup_F covrad(C_*(F))`.                              (2)

I do not re-prove R2 here. This run asks what the extremal value `ell(F)=pi/4` actually means in geodesic language, and whether iid resampling or lattice symmetry can exclude it.

Metric this run:

`L_cone: pi/4 -> pi/4`.

The prior H0017 reports deliberately left the unchanged-run counter unknown. Per owner instruction, it remains `UNKNOWN -> UNKNOWN`; I do not manufacture a streak.

## 3. Method #23 — assume the bad object exists: a missing slope interval is exactly a neighboring pair

Ahlberg--Hoffman define two random coalescing geodesics `G<G'` to be **neighboring** if with probability one there is no infinite geodesic strictly between them (equivalently their positive-probability formulation in the paper). Their neighboring-geodesic lemma states that if two random coalescing geodesics are *not* neighboring, then there exists a random coalescing geodesic strictly between them.

Their Theorems 2.5--2.6 / 12.2 also give the following facts under the present iid continuous assumptions:

1. `C_*(F)` is deterministic and closed in the circle `S` of supporting functionals;
2. every `rho in C_*` is realized by a random coalescing geodesic;
3. every infinite geodesic has an asymptotically linear Busemann functional in `C_*`;
4. a functional in `C_*` has at most one infinite geodesic from the origin;
5. the planar order of random coalescing geodesics is consistent with the circular order of their Busemann functionals.

These give the following exact reformulation.

### R14-H0017-R3 — gap / neighboring-pair correspondence

Let `I=(rho_-,rho_+)` be a connected component of the circular complement `S \ C_*`. Then the random coalescing geodesics `G_-` and `G_+` realizing its two endpoints are neighboring.

Conversely, if `G_-<G_+` are neighboring random coalescing geodesics with distinct Busemann functionals `rho_-<rho_+` in the relevant circular order, then the open functional interval `(rho_-,rho_+)` contains no point of `C_*`; in particular it lies in a component of `S\C_*`.

#### Proof

Because `C_*` is closed, the endpoints of a complement component lie in `C_*`; hence endpoint geodesics `G_-` and `G_+` exist. If they were not neighboring, Ahlberg--Hoffman's neighboring-geodesic lemma would give a random coalescing `G_0` strictly between them. Its Busemann functional belongs to `C_*` and, by order consistency, lies strictly between `rho_-` and `rho_+`, contradicting that `I` is disjoint from `C_*`.

For the converse, suppose `rho_0 in C_*` lies strictly between `rho_-` and `rho_+`. Ahlberg--Hoffman provide a random coalescing geodesic `G_0` with functional `rho_0`. Order consistency puts `G_0` strictly between `G_-` and `G_+`, contradicting neighboringness. QED.

Thus the retained cone problem can be restated without mentioning differentiability:

`C_*=S`  iff  there is no neighboring pair of random coalescing geodesics with distinct Busemann slopes.   (3)

Combined with R2, Benjamini's all-direction cone statement for a fixed law is equivalent to absence of such a distinct-slope neighboring pair.

This is recorded as a self-check structural reduction, not a novelty-certified theorem and not source closure. It has 0/2 external audits.

### Why this matters

The missing interval is not merely a convex-geometry corner. It is a **geodesic adjacency defect**. This moves the target from "prove the limit shape differentiable" to the potentially weaker statement

> iid finite-energy FPP cannot support two neighboring coalescing geodesic families with different asymptotic Busemann functionals.

Ahlberg--Hoffman's general stationary/ergodic framework does allow neighboring pairs; their paper explicitly develops a neighboring-pair lemma, and Brito--Hoffman construct non-iid ergodic models with only four infinite geodesics. Independence must therefore enter essentially.

## 4. Method #14 — use the D4 action: exact characterization of the pi/4 boundary

For an iid common edge law on the square lattice, the law is invariant under the dihedral symmetries of the lattice. Since `C_*(F)` is almost-surely deterministic and defined equivariantly, it is invariant in particular under the quarter-turn `R: rho -> rho+pi/2` on the slope circle.

The source/Ahlberg--Hoffman baseline gives

`covrad(C_*) <= pi/4`.

At equality there is much more rigidity than was previously recorded.

### R14-H0017-R4 — four-ray boundary theorem

For every source-admissible iid law `F`, the following are equivalent:

(a) `ell(F)=pi/4`;

(b) `covrad(C_*(F))=pi/4`;

(c) `C_*(F)` consists of exactly four equally spaced functionals, a single quarter-turn orbit;

(d) almost surely there are exactly four infinite geodesics from the origin (equivalently exactly four random coalescing geodesic families), and their Busemann functionals form that quarter-turn orbit.

#### Proof

`(a)<->(b)` is equation (1).

Assume (b). For a nonempty closed subset of the circle, covering radius is half the length of its largest complementary open arc. Here the radius is `pi/4`, so `S\C_*` has a component `I` of angular length `pi/2`. (The supremal gap is attained: if complementary intervals had lengths tending to a positive supremum without attainment, infinitely many would eventually have length bounded below by a fixed positive constant, impossible on a circle of finite total length.)

Because `C_*` is quarter-turn invariant, `I, RI, R^2I, R^3I` are complementary components. They cannot overlap partially: two connected components of an open set are either disjoint or equal; equality is impossible for a proper open arc under a nontrivial quarter-turn. Each has length `pi/2`, so their four lengths already total `2pi`. Therefore their union is the full circle except for their four common boundary points. Since every component endpoint lies in the closed set `C_*`, `C_*` is exactly those four quarter-turn-related points. This proves `(b)->(c)`.

Conversely, if `C_*` is four equally spaced points, every point of the circle lies within angular distance `pi/4` of one of them and the midpoints of the four gaps are exactly distance `pi/4`; hence the covering radius is `pi/4`. Thus `(c)->(b)`.

Ahlberg--Hoffman give existence of a random coalescing geodesic for every functional in `C_*`, uniqueness of an origin geodesic for each such functional, and the fact that every infinite origin geodesic has functional in `C_*`. Hence `|C_*|=4` is equivalent to exactly four origin geodesics, and the deterministic quarter-turn invariance fixes their functional orbit. This proves `(c)<->(d)`. QED.

### Consequence: the baseline obstruction is a famous iid geodesic question

The source-wide `pi/4` baseline is not an arbitrary weakness of the cone proof. For a *fixed* law it is attained exactly at the extremal **four-geodesic state**.

Ahlberg--Hoffman explicitly explain that exactly four geodesics are possible under their general stationary/ergodic assumptions and are realized by non-iid constructions, while saying those sharp examples are most likely not representative of independent models. Fresh searches this run found no later theorem excluding the exactly-four state for the present iid continuous class.

This is a certified obstruction to a naive improvement of `pi/4`:

- proving merely that each iid law has more than four geodesics would imply `ell(F)>pi/4` law-by-law;
- it would **not yet move the frozen universal metric**, because a sequence of iid laws could in principle have `covrad(C_*(F_n)) -> pi/4` without equality;
- actual movement `L_cone >= pi/4+epsilon` requires a **uniform quantitative angular separation** from the four-ray state over the entire admissible law class.

So a fixed positive movement is stronger than the qualitative conjecture "iid FPP never has exactly four geodesics."

## 5. Method #9 — randomize / resample: what local independence can and cannot buy

I tested the previous plan: assume a maximal missing interval and use iid edge resampling in separated annuli to force an intermediate Busemann slope.

The literature now makes the failure mode precise.

Jacquet's iid pattern theorem says long geodesics cross any admissible local pattern linearly often (under the relevant mild conditions; a later version removes moment assumptions in a broader setup). This is strong evidence that an iid geodesic cannot avoid a prescribed *local* environment indefinitely.

But R3 shows that filling a missing interval is not a local event. One must create a new **coalescing tail class** strictly between two neighboring tail classes. Repeated local patterns along either endpoint geodesic can be absorbed by the same asymptotic family; a single geodesic can cross arbitrarily rich local patterns while retaining one Busemann slope. Thus "every pattern occurs" does not imply "every slope occurs."

Ahlberg--Hoffman's neighboring-pair lemma is even more diagnostic. For neighboring `G_-<G_+`, finite geodesics that lie strictly between them and diverge from the boundary families within a fixed number of initial steps become asymptotically rare. Therefore an iid-resampling proof would need a finite-energy surgery that produces, with a probability bounded away from zero at arbitrarily large scales, an **early-diverging middle geodesic whose tail cannot be absorbed back into either neighboring family**. Ordinary local shortcut patterns do not provide that tail condition.

The 2022 Ahlberg--Hanson--Hoffman sublinearity theorem does not close this gap either: it proves the infinite-geodesic tree has vanishing planar density without assuming shape regularity, but four sparse rays are completely compatible with such sublinearity.

**Outcome #9:** the annulus/pattern idea does not currently yield metric movement. The exact missing ingredient is now identified: a finite-energy or mass-transport mechanism that turns independence into a *new tail/coalescence class*, not merely a local detour.

No finite computational claim arose in this run, so I did not manufacture a checker just to produce an artifact.

## 6. The strongest route after this run

The clean hierarchy is now:

1. **Source closure for fixed `F`:** prove `C_*(F)=S`.
2. **Equivalent geodesic form:** rule out all neighboring distinct-slope random coalescing pairs (R3).
3. **First qualitative milestone:** rule out the four-geodesic state; by R4 this proves `ell(F)>pi/4` for each such law.
4. **Actual frozen-metric movement:** prove a uniform angular estimate

   `covrad(C_*(F)) <= pi/4 - epsilon`

   for one explicit universal `epsilon>0` over all admissible `F`.
5. **Full metric closure:** prove `covrad(C_*)=0` for all admissible laws.

The first milestone is already a recognized hard iid-FPP structural question. The frozen metric asks for more: uniformity over the whole continuous-law class. That is why no numerical or restricted-law statement is promoted to movement.

## 7. Nearest useful literature and what it lacks

### Ahlberg--Hoffman (2019)

Provides the deterministic closed slope set, existence/uniqueness, ordering, and neighboring-pair machinery. It explicitly notes that four-geodesic examples are sharp in broader ergodic models but likely not in independent models. It does not prove iid exclusion of four slopes.

### Ahlberg--Hanson--Hoffman (2022)

Proves geodesic-tree density is sublinear without differentiability assumptions. Its result is compatible with finitely many rays and therefore does not rule out the R4 boundary state.

### Jacquet (2024/2025)

Proves strong local pattern crossing for iid geodesics. It supplies exactly the kind of independence/local-richness input absent from stationary counterexamples, but it does not convert local patterns into a new asymptotic slope or coalescence class.

### Brito--Hoffman (2021)

Constructs invariant ergodic non-iid examples with `l1` shape and exactly four infinite geodesics. These are outside H0017's iid source class but show that planarity, ergodicity, D4-like geometry, and Busemann ordering alone cannot prove the needed exclusion.

## 8. Next genuinely different methods

Do not repeat #9/#14/#23 next run. The next triple is:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY:** target the qualitative iid statement `|C_*|>4` (equivalently `ell(F)>pi/4` law-by-law) before asking for a uniform epsilon. Keep it explicitly PARTIAL because it would not yet move `L_cone`.
- **#21 ASK WHO ELSE HAS THIS SHAPE:** dissect the Brito--Hoffman exactly-four construction and identify the precise non-iid mechanism that permits four neighboring tail classes; compare it with iid pattern-crossing / finite-energy inputs.
- **#27 SWAP THE QUANTIFIERS:** first seek `for every fixed F, there exists epsilon(F)>0`; only after that investigate whether continuity/compactness in the passage-time law can make `inf_F epsilon(F)>0`. This separates the qualitative four-ray exclusion from the stronger universal metric movement.

A particularly concrete proof target is:

`iid + continuous + source moment assumption  =>  no quarter-turn orbit of four neighboring coalescing geodesic families.`

If this cannot be proved without importing an unresolved strict-convexity/geodesic-number conjecture, the next run should record that dependence explicitly rather than build another local lemma.

## 9. Status, closure discipline, and model-control state

H0017 remains **OPEN / PARTIAL**.

- frozen metric: `L_cone: pi/4 -> pi/4`;
- unchanged streak: `UNKNOWN -> UNKNOWN`;
- R3 and R4 are on-page self-check reductions with `0/2` external audits;
- no claim is called source closure;
- no finite checker was needed because no finite computational assertion was introduced;
- no email, Drive, public post, permission change, workflow execution, purchase, or scheduler modification occurred.

The scheduler/model situation remains unchanged. The exposed task interface available in this context has controls for title/prompt/schedule or relative start, timing mode and enablement, but no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry. Therefore GPT-6/maximum remains prompt-only and is not claimed here. The root ledger also records that P26's earlier `You cannot modify this task` result was authorization-context dependent and later succeeded in an authorized P/C context. The valid workaround for a currently denied task remains the authorized owning workspace/account or platform support, never duplication or permission bypass.

## 10. Structured ledger delta (own immutable report only)

```json
{
  "track": "R14",
  "active_target": "H0017",
  "source": "Ahlberg-Deijfen-Sfragara, arXiv:2607.07589v1",
  "status": "OPEN/PARTIAL",
  "metric": {
    "name": "L_cone",
    "before": "pi/4",
    "after": "pi/4",
    "movement": "NO_MOVEMENT",
    "unchanged_count_before": "UNKNOWN",
    "unchanged_count_after": "UNKNOWN"
  },
  "methods_this_run": [9, 14, 23],
  "new_on_page_results": [
    "R14-H0017-R3 gap/neighboring-pair correspondence",
    "R14-H0017-R4 pi/4 boundary iff four equally spaced Busemann slopes / four origin geodesics"
  ],
  "audits": "0/2",
  "counterexample_search": "No source-admissible iid counterexample found; exactly-four examples located are stationary/ergodic non-iid and remain outside source scope",
  "strongest_obstruction": "Uniform movement above pi/4 requires quantitative exclusion of near-four-ray iid slope sets, stronger than merely excluding exact four-geodesic laws",
  "next_methods": [4, 21, 27],
  "next_target": "First prove or obstruct the qualitative iid exclusion |C_*|=4; then test whether any lawwise angular slack can be made uniform over source laws",
  "original_perceptron": "HANDOFF_PRESERVED_NOT_REOPENED",
  "i0089": "HANDOFF_PRESERVED_NOT_REOPENED",
  "bis32": "HANDOFF_PRESERVED_NOT_REOPENED",
  "model_requested": "GPT-6 maximum",
  "model_actual_reported": "GPT-5.6 Sol",
  "reasoning_actual_reported": "UNVERIFIED"
}
```
