Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `L_cone: pi/4 -> pi/4`; unchanged-count field remains `UNKNOWN -> UNKNOWN`. Methods actually tried: #4 PROVE SOMETHING WEAKER, COMPLETELY; #21 ASK WHO ELSE HAS THIS SHAPE; #27 SWAP THE QUANTIFIERS.**

# R14 HARD OUTSIDE — H0017: four-ray boundary forces square/diamond, and one extra Busemann orbit gives explicit angular slack

Repository / branch: `yspennstate/math-open-problems` / `master`.  
Date: 2026-09-17 UTC.

## 1. Continuity, ownership, and source gate

I did **not** reopen the original negative-margin spherical Gaussian perceptron. Its supported handoff bracket remains

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`,

with width `6.48139658710`. I0089 and RS-2026-BIS32 likewise remain handed off after their hard-task recovery limits.

The active exclusive R14 target remains **H0017**, Daniel Ahlberg, Maria Deijfen and Matteo Sfragara, *Surviving from the tip of a cone in competing first-passage percolation*, arXiv:2607.07589v1 (8 July 2026), under `operations/claims/H0017.md`.

At run start I recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the controlling owner directive, the H0017 claim, the newest own report

`runs/R14/2026-09-17T16-56-18Z_h0017_four-ray_boundary_neighbor_gap_9a61.md`,

and the newest directly neighboring strict-convexity FPP report I could recover,

`runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md`.

The targeted intake search recovered H0017 as `CONFIRMED` in `probability_1000_intake_H_20260914/intake_H_verification.md` and the canonical H intake JSONL. As in earlier runs, the connector cannot render all roughly 780 JSONL rows literally in one response, so I record the intake read as targeted rather than pretending to have inspected unseen truncated rows.

Fresh primary-source checking on 2026-09-17 found:

- arXiv:2607.07589 is still the July 8, 2026 cone-survival preprint; no later primary source found in bounded exact-title/author and all-direction searches claims the missing all-direction theorem;
- Ahlberg--Hoffman, *Random coalescing geodesics in first-passage percolation*, arXiv:1609.02447v2, remains the structural source for the deterministic closed Busemann-slope set `C_*` under exactly the product/continuous/moment assumption used here;
- Brito--Hoffman, arXiv:1912.06338v2, remains the explicit stationary/ergodic **non-iid** four-geodesic example, with `l1` asymptotic shape;
- Dembin--Elboim--Peled, arXiv:2204.02332 / GAFA 2024, prove strong planar coalescence under an additional `>32`-extreme-point shape hypothesis and verify that hypothesis for a specific family of iid laws, not for every admissible law.

This is bounded negative evidence, not a novelty certificate.

## 2. Frozen metric and retained reductions

For a source-admissible iid continuous passage-time law `F`, define

`alpha_c^F(theta) := sup { alpha : P_F(G^{theta,alpha}) > 0 }`.

The fixed source-wide metric is

`L_cone := inf_F inf_theta alpha_c^F(theta)`.

The source certifies `L_cone >= pi/4`; full source closure is `L_cone=pi/2`.

Retained R14 self-check reductions, each still at `0/2` external audits, are:

`alpha_c^F(theta) = pi/2 - dist(theta,C_*(F))`,                              (R2)

in the endpoint sense (survival below / extinction above), hence

`ell(F) := inf_theta alpha_c^F(theta) = pi/2 - covrad(C_*(F))`;              (1)

and, by quarter-turn invariance,

`ell(F)=pi/4  <=>  C_*(F) is exactly one four-point quarter-turn orbit`.      (R4)

The previous run also identified a complement gap of `C_*` with a neighboring pair of random coalescing geodesics with distinct Busemann slopes (R3).

Metric this run:

`L_cone: pi/4 -> pi/4`.

The prior H0017 reports deliberately preserve the unchanged-run counter as unknown. It therefore remains `UNKNOWN -> UNKNOWN`; no streak is manufactured.

## 3. Method #4 — a complete weaker theorem: the pi/4 boundary forces a four-sided limit shape

The point of this run was first to ask what R4 implies for the **ordinary FPP limit shape**, not merely for the geodesic tree.

Ahlberg--Hoffman define `S` to be the circle of supporting functionals of the deterministic asymptotic shape `Ball`. Their Theorem 2.6 gives a deterministic closed set

`C_*(F) subset S`

which contains **every tangent functional** of `Ball`.

### R14-H0017-R5 — square/diamond necessity at the pi/4 boundary

For every source-admissible iid law `F`,

`ell(F)=pi/4  =>  Ball(F) has exactly four sides; hence, by D4 symmetry, Ball(F) is a square or a diamond.`

Equivalently,

`Ball(F) is neither a square nor a diamond  =>  ell(F)>pi/4.`

#### Proof

Assume `ell(F)=pi/4`. By retained R4, `C_*(F)` consists of exactly four quarter-turn-related supporting functionals. Since every tangent functional belongs to `C_*`, `Ball` has at most four tangent supporting lines.

A compact planar convex body with nonempty interior has a tangent supporting functional for the relative interior of every nontrivial boundary side, and any non-flat boundary arc contributes infinitely many tangent supporting functionals. Therefore a convex body with at most four tangent functionals must be a polygon with at most four sides. The square-lattice `D4` symmetry forces at least four supporting sides and forces a four-sided body to be one of the two standard orientations: square or diamond. Thus it has exactly four sides. QED.

This can also be read directly against Ahlberg--Hoffman's discussion: under their general ergodic assumptions four sides means square or diamond; otherwise lattice symmetry gives at least eight sides (or infinitely many), and their geodesic machinery correspondingly has more than the extremal four classes.

### Why this is useful but does not move `L_cone`

R5 is a genuine law-by-law strict improvement statement. It reduces the qualitative milestone

`ell(F)>pi/4`

to the famous shape question of excluding an exact square/diamond limit shape for that law.

It does **not** yield a universal numerical increment. Even if every iid continuous law were known not to have an exact square or diamond, a sequence of laws could in principle approach the four-slope configuration arbitrarily closely. The frozen metric is an infimum over all admissible laws, so a law-dependent positive slack is not enough.

The neighboring R08 strict-convexity track independently exposes exactly this kind of barrier in a concrete direction: for Exp(1), even proving one strict triangle-gap inequality is still open in its frozen metric. This is evidence against pretending that R5 makes the remaining shape step routine.

## 4. A quantitative lemma: one additional quarter-turn orbit buys an explicit amount

R4 says equality occurs at a single four-point orbit. The next question is how much a **second** orbit buys.

For two slope angles `rho,rho'`, let

`d_Q(rho,rho') := min_{k in Z} |rho-rho'-k*pi/2|` reduced to `[0,pi/4]`.

### R14-H0017-R6 — extra-orbit angular gain

If `rho,rho' in C_*(F)` and

`delta := d_Q(rho,rho') in (0,pi/4]`,

then

`ell(F) >= pi/4 + delta/2`.                                                   (2)

#### Proof

Quarter-turn invariance places the two four-point orbits

`rho + k*pi/2` and `rho' + k*pi/2`, `k=0,1,2,3`,

inside `C_*`. After rotating coordinates, the gaps in this eight-point subset alternate between `delta` and `pi/2-delta`. Hence every complementary arc of the full `C_*` has length at most

`max(delta,pi/2-delta)=pi/2-delta`,

because `delta<=pi/4`. Thus

`covrad(C_*) <= (pi/2-delta)/2 = pi/4-delta/2`.

Insert this into (1):

`ell(F)=pi/2-covrad(C_*) >= pi/4+delta/2`. QED.

This is elementary circle geometry, not a finite-enumeration claim, so no checker-only artifact was manufactured.

Define the law-dependent separation parameter

`s(F) := max_{rho,rho' in C_*(F)} d_Q(rho,rho') in [0,pi/4]`.

Compactness of `C_*` gives the maximum. R6 yields the concise quantitative target

`ell(F) >= pi/4 + s(F)/2`.                                                    (3)

Moreover `s(F)=0` exactly when `C_*` is one quarter-turn orbit. Thus the qualitative four-ray exclusion is `s(F)>0`, while a source-wide fixed-metric improvement by this route requires a **uniform** lower bound

`inf_F s(F) > 0`.                                                             (4)

Equation (4), not merely `s(F)>0` law by law, is the quantity that would actually move `L_cone`.

## 5. Method #21 — what the known four-ray construction has that iid does not

Brito--Hoffman provide the nearest solved model with the exact bad geometry: a stationary/ergodic FPP family with `l1` asymptotic shape and exactly four infinite geodesics from the origin.

Inspecting their construction isolates the feature that is absent from the source model. The four-ray skeleton is organized by a **global multiscale grid/highway hierarchy**. Large-scale horizontal/vertical fast structures are coherently nested across long distances; the model then adds local randomness on top of that hierarchy. The construction is ergodic, but the hierarchy induces long-range dependence. It is not a product measure.

That matters because an iid proof cannot simply reuse their geometry with a different distribution. To mimic the four-ray state, independent edges would have to self-organize, at arbitrarily many scales, into a persistent nested hierarchy that keeps all infinite geodesics trapped in four tail classes. Local pattern richness works in the opposite direction but, as the previous run recorded, finite local resampling does not by itself create a new tail/coalescence class.

The sharp structural contrast is therefore:

- **ergodic dependent countermodel:** system-spanning coherent highways are put into the environment by a shared multiscale hierarchy;
- **iid source model:** any analogous coherence must arise spontaneously from independent edges and persist through infinitely many scales.

This explains why a Burton--Keane / finite-energy idea remains plausible, but also why a one-box modification cannot prove it: changing finitely many edges changes the entrance to a geodesic family, not its tail class.

## 6. Method #27 — swap the quantifiers: what can be proved first and what actually moves the metric

The natural statements form a strict ladder.

### Level A — one fixed law

Prove `s(F)>0` for a specific admissible iid law. Then R6 gives an explicit law-dependent strict improvement

`ell(F) >= pi/4+s(F)/2 > pi/4`.

For families where the limit shape is already rigorously known to have many extreme points, existing literature gives this kind of restricted-law progress. Dembin--Elboim--Peled, for example, verify a `>32`-extreme-point hypothesis for a specific family of iid laws. Such a result is PARTIAL for H0017 and does not move the universal metric.

### Level B — every law, qualitative

Prove merely

`forall F, s(F)>0`.

By R5/R6 every admissible law then has `ell(F)>pi/4`. This would in particular exclude the iid four-geodesic/square-diamond boundary state. It is already a serious open iid-FPP theorem.

But it still does **not** imply `L_cone>pi/4`, because the positive numbers `s(F)` could tend to zero along a sequence of laws.

### Level C — the fixed metric

To move the actual R14 quantity by this route, prove

`exists delta_0>0 such that forall admissible F, s(F)>=delta_0`.

Then

`L_cone >= pi/4 + delta_0/2`.

This is the first statement in the ladder that certifiably moves the frozen source-wide metric.

### Level D — full source closure

Full H0017 closure remains `C_*(F)=S` for every admissible `F`, equivalently zero covering radius and `L_cone=pi/2`.

This quantifier swap prevents a common bookkeeping error: a beautiful theorem for one law, or even a nonuniform theorem for every law, must not be recorded as a universal endpoint movement.

## 7. Current obstruction and honest status

The metric stays

`L_cone = pi/4` (certified lower endpoint; no larger universal endpoint proved).

The strongest newly isolated obligation capable of moving it is now quantitative and source-exact:

`find delta_0>0 such that every admissible iid law has two Busemann slopes separated modulo pi/2 by at least delta_0.`

No theorem found in the current literature provides such a uniform separation. Ahlberg--Hoffman explicitly emphasize that their general stationary/ergodic results are qualitative and that quantitative iid estimates require independence to enter fundamentally. Their discussion also says that very little is known about iid limit-shape geometry and notes that even exact simple shapes are not excluded by current theory. Dembin--Elboim--Peled obtain strong quantitative coalescence only after imposing substantial shape complexity, not as a theorem for all iid laws.

So H0017 remains **OPEN / PARTIAL**. R5 and R6 are on-page self-check reductions with `0/2` outside audits, not novelty-certified source closure.

## 8. Next new-method triple

The next H0017 run should not repeat #4/#21/#27. The strongest genuinely new triple I would use is:

- **#3 PROVE SOMETHING STRONGER:** target a universal second-orbit theorem `s(F)>=delta_0`, because that directly feeds the frozen metric instead of accumulating law-specific shape statements;
- **#12 FIND WHAT IS CONSERVED:** search for a translation-covariant mass/flux associated with a neighboring geodesic pair whose expected value is incompatible with a positive angular gap under product measure;
- **#30 ONE DIRECTION AT A TIME:** condition on a putative maximal gap and focus on its midpoint support direction, seeking one new coalescing class there rather than filling the whole gap at once.

A productive failure would be a certified theorem explaining why all translation-covariant fluxes available from the existing Busemann formalism vanish identically for a neighboring pair; that would justify abandoning the mass-transport route rather than adding another local lemma.

## 9. Model / scheduler control status

The exposed scheduling interface still offers title, prompt, schedule or relative start, timing mode, and enablement. It exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore GPT-6/maximum remains request text only and is not claimed for this run.

The repository's current `RESULTS.md` also corrects the old P26 permission story: P26's full update later succeeded in an authorized P/C context, so the earlier `You cannot modify this task` result was context-dependent. If an ID still rejects modification, the legitimate route is its authorized owning workspace/account context or platform support. No scheduler changes, permission changes, duplicate tasks, or bypasses were attempted in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R14
  active_target: H0017
  source: arXiv:2607.07589v1
  status: OPEN/PARTIAL
  fixed_metric: L_cone
  before: pi/4
  after: pi/4
  movement: none
  unchanged_count_before: UNKNOWN
  unchanged_count_after: UNKNOWN
  methods_tried: [4, 21, 27]
  new_self_checks:
    - R14-H0017-R5: ell(F)=pi/4 forces square-or-diamond limit shape
    - R14-H0017-R6: second quarter-turn Busemann orbit at separation delta gives ell(F)>=pi/4+delta/2
  external_audits_for_new_claims: 0/2
  certified_obstruction: universal metric movement by this route requires uniform second-orbit angular separation over all admissible iid laws
  next_methods: [3, 12, 30]
  original_negative_margin_target: handed_off_not_reopened
  i0089: handed_off_not_reopened
  rs_2026_bis32: handed_off_not_reopened
```

No shared root ledger, peer track file, email, Drive file, public post, paid resource, workflow, permission, or scheduler state was modified.