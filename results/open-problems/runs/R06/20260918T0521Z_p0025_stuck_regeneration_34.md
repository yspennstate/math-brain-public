Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT on P0025: `E_disk: 0 -> 0`, unchanged count `3 -> 4`; mandatory Section-I THINKING-ONLY / STUCK_RECOVERY_1; Section-B methods #2 ATTACK THE NEGATION FIRST, #21 ASK WHO ELSE HAS THIS SHAPE, #27 SWAP THE QUANTIFIERS.**

# R06 — P0025 exterior-disc synchronous coupling / mandatory stuck recovery 1

Run ID: `20260918T0521Z_p0025_stuck_regeneration_34`
Repository / branch: `yspennstate/math-open-problems` / `master`
Track: `R06`, lane `CLOSABLE OUTSIDE`

## 0. Continuity and frozen states

This is the mandatory thinking-only run triggered by the third consecutive unchanged P0025 run. I continue from

`runs/R06/20260918T0421Z_p0025_mellin_lamperti_33.md`

and the create-only ownership claim

`operations/claims/P0025.md`.

I do **not** reopen any rotated predecessor.

The current R06 target is Krzysztof Burdzy, *My favorite open problems*, Problem 5(ii), “Convergence of synchronous couplings.” The current author page, rechecked 2026-09-18, still asks:

> If `D` is the complement of a non-degenerate closed disc, is it true that with positive probability `limsup_{t->infinity}|X_t-Y_t|>0` for the synchronous reflected-Brownian coupling?

The frozen source metric is binary:

`E_disk = 1`

only when the literal source question is fully proved or refuted on the page. It remains `0`.

The original scheduler title still names Lyons--Peres Question 6.20 / I0056, but that target was rotated after its own six-unchanged sequence and is not restarted. Its exact source question is preserved as:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

R06's frozen admissible pentagonal case remains the `{5,5}` hyperbolic tessellation, under the outer vertex-boundary normalization

`Phi_V(G)=inf_{nonempty finite K} |partial_V K|/|K|`,

with certified interval `[sqrt(5),sqrt(5)]`, width `0`. This is only PARTIAL for the full source question. Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, already cover the triangular/codegree-3 and quadrangular/codegree-4 regimes and are not relabeled as new.

The rotated BENJ three-source target is likewise not reopened.

## 1. Required repository / source / literature read

Before the thinking analysis I reread or recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- `operations/claims/P0025.md`;
- the newest R06 report `runs/R06/20260918T0421Z_p0025_mellin_lamperti_33.md`;
- the neighboring Burdzy Problem 5(i) claim `operations/claims/P0024.md` and current R19 state;
- the campaign catalogue row for P0025 and its neighboring reflected-Brownian problems.

Fresh dated literature/source checks on 2026-09-18 included:

1. Burdzy's live open-problems page, `https://sites.math.washington.edu/~burdzy/open_mathjax.php`, which still displays Problem 5(ii) as an open problem.
2. M. Cranston and Y. Le Jan, *On the noncoalescence of a two point Brownian motion reflecting on a circle*, Ann. IHP 25 (1989), 99--107, Numdam `AIHPB_1989__25_2_99_0`.
3. K. Burdzy, Z.-Q. Chen, P. Jones, *Synchronous couplings of reflected Brownian motions in smooth domains*, arXiv `math/0501486`, Illinois J. Math. 50 (2006), 189--268.
4. K. Burdzy, *Differentiability of stochastic flow of reflected Brownian motions*, arXiv `0806.0119`, EJP 14 (2009), 2182--2240.
5. Denisov--Korshunov--Wachtel, *Markov Chains with Asymptotically Zero Drift: Lamperti's Problem* (Cambridge, 2025), used only as nearby recurrence language.
6. Current general Markov-additive-process searches, including work on Polish-space modulators, used only to identify the right category, not as a source solution.

The bounded current search found no later primary source explicitly resolving Burdzy Problem 5(ii). This is dated negative evidence, not a novelty certificate.

## 2. Section-I blocker — freeze it exactly

No new theorem is asserted in this run. The exact blocking statement inherited from run 33 is the following uniform nonlinear one-block estimate, or a source-valid replacement strong enough to imply recurrence of the logarithmic separation.

Let

`r=|X-Y|`, `U=-log r`,

and sample after a fixed positive amount of an admissible boundary-local-time clock. For the resulting nonlinear increment `Delta U`, the previous Lamperti compiler would close the long-time step if there were constants `eta,delta,C,v>0`, independent of the remaining full state, such that for all sufficiently small `r`,

\[
\boxed{
 E[\Delta U\mid \text{full state}]\le C r^\eta,\qquad
 E[(\Delta U)^2\mid \text{full state}]\ge v,\qquad
 E[|\Delta U|^{2+\delta}\mid \text{full state}]\le C.
}
\]

The tangent process has the needed zero mean and nonzero variance, but no R06 argument proves the displayed estimates for the **moving finite-separation pair uniformly over midpoint/orientation/contact states**.

## 3. Every route tried so far, and the exact reason it stops

This is the required stuck inventory rather than another lemma.

### Route A — global monotonicity of the distance

Historical campaign work already observed that an exterior-circle reflection can either increase or decrease synchronous separation, depending on the relative location of the other particle. Therefore there is no global pathwise contraction/expansion monovariant.

**Failure:** the sign is state-dependent.

### Route B — tangent Lyapunov exponent

The infinitesimal tangent cocycle has zero mean log growth. Burdzy--Chen--Jones' circle calculation is critical rather than strictly expanding or contracting.

**Failure:** a zero first-order exponent by itself does not decide whether finite separation tends to zero.

### Route C — exact tangent cumulant / fluctuation route

Run 31 obtained the exact tangent cumulant and nonzero variance rate; run 33 extended the Mellin strip and obtained inverse moments of order `<1`.

**Failure:** these are statements for the infinitesimal cocycle. They do not provide the conditional nonlinear drift or moment estimates for the actual pair.

### Route D — frozen finite-separation conformal “peanut” reduction

Run 32 conformally identified the exterior of the two overlapping unit discs associated with a **frozen** separation and converted its symmetric excursion trace to a universal Cauchy form. The physical speed measure was shown to be an `L1` perturbation of the zero-separation speed.

**Failure:** the real pair changes separation and frame during a block. Freezing `z` does not control the accumulated moving-frame/corner error.

### Route E — count the instantaneous expansion set

Run 32 localized the part of the boundary geometry where the instantaneous local-time term expands the separation.

**Failure:** arclength of an expansion region does not determine its occupation law, and therefore does not determine averaged log drift.

### Route F — Cranston--Le Jan finite-variation sign shortcut

Run 32 initially summarized one source identity as a favorable global finite-variation sign. Run 33 reread the primary paper and retracted that: the displayed differential has mixed-sign terms.

**Failure:** no global submartingale sign is available from that identity.

### Route G — one-block positive rebound probability

A fixed positive chance to move to a larger-separation band is too weak.

**Failure:** a process can have repeated local rebounds and nevertheless drift to zero in the long run.

### Route H — Lamperti moment compiler

Run 33 proved a direct recurrence criterion for `U=-log r` from exponentially small positive drift, nondegenerate variance and a uniform `2+delta` moment.

**Failure:** the criterion is only a compiler. Its hypotheses are exactly the missing finite-separation estimates.

### Route I — discard spatial infinity by an excursion tail

For one exterior-disc excursion the probability, in local-time normalization, of reaching radius `R` has `1/log R` decay, so run 33 showed that choosing an enormous cutoff can make far excursions polynomially rare in `r`.

**Failure:** importing a bounded-domain differentiability theorem after truncating at a radius depending on `r` is invalid unless all constants are controlled uniformly in that radius. R06 has not proved that.

### Route J — quote Burdzy 2009 differentiability

Burdzy 2009 proves differentiability of the reflected stochastic flow at fixed local-time stopping times in a smooth **bounded** domain and obtains the kind of superlinear approximation estimates that would be useful here.

**Failure:** the paper assumes boundedness and does not directly supply the exterior-disc, all-state, finite-separation moment bounds needed above. It also does not make `U` a one-dimensional Markov chain; the midpoint/orientation/contact state remains a modulator.

## 4. #2 ATTACK THE NEGATION — try to break the uniform-block formulation

The first new thinking move is to attack the **formulation** of the missing estimate rather than the source statement.

Cranston--Le Jan's reduced exterior variables retain a genuine modulating state. In their boundary-local-time equation the separation coordinate has a term of the form

`dz = (1/2)(z-|y|) dphi`,

so even at a fixed small `z`, the instantaneous sign depends on the angular/contact coordinate `y`. That is a warning that the first inequality in the boxed all-state estimate may be stronger than necessary and may even fail for badly chosen short blocks or entrance states.

I did **not** obtain a rigorous family violating the all-state estimate, so this is not a counterexample and does not move `E_disk`. What the negation attack establishes operationally is the correct burden: a future proof cannot replace occupation/mixing of the modulator by pointwise sign control.

The potentially dangerous state families to test next are:

- both particles near the boundary with separation direction close to the instantaneous expanding sector;
- near-simultaneous boundary contacts where the reduced coordinates approach the singular/corner geometry in the Cranston--Le Jan parametrization;
- states whose common midpoint is far from the circle, where a local-time block begins only after a long bulk excursion and may return with a highly nonuniform orientation.

A single rigorous family with non-summable positive averaged drift would refute the **current compiler route**, but would still not refute Burdzy's source question.

## 5. #21 ASK WHO ELSE HAS THIS SHAPE — the state should be treated as a modulated critical process

The scalar coordinate `U=-log|X-Y|` is not the natural Markov state. The correct object is closer to

`(U,J)`,

where `J` records the scale-free midpoint/orientation/contact data. At `U=+infinity` (zero separation) the ordinate has the critical tangent Lévy law; for large finite `U` the transition law should be viewed as an asymptotic perturbation whose coefficients depend on `J`.

This has the **shape** of a critical Markov-additive / asymptotically-zero-drift problem, but existing Lamperti theory does not immediately solve it. The standard scalar theory assumes drift and variance asymptotics for the actual Markov chain. General Markov-additive results allow a modulator, but R06 has not proved that the exterior coupling is exactly Markov-additive or that its modulator has a scale-independent stationary law with the required uniform mixing near `r=0`.

Thus the nearby literature supplies the right language, not the missing estimate.

The nearest solved quantitative reflected-flow result remains Burdzy 2009. Its proof has exactly what this problem currently lacks: a bounded smooth geometry in which excursion/projection estimates can be made uniform before a geometric-scale Borel--Cantelli argument is applied.

## 6. #27 SWAP THE QUANTIFIERS — do not demand estimates from every angular state

The strongest conceptual correction from this stuck run is to stop requiring

`for every small-r full state, one fixed block is almost centered`.

That is substantially stronger than the literal long-time source question appears to need.

A more natural target is a **regenerative entrance law** for the modulator. Let `J` denote the scale-free part of the reduced state and let `r` lie in a geometric band. Instead of the boxed all-state estimates, seek stopping times at which the process re-enters a compact good set `K` of modulator states and an entrance law `mu_r` on `K`. The desired comparison would then be averaged under `mu_r`.

A scale-band formulation is especially compatible with run 33's tangent scale function. Fix a logarithmic band half-width `A>0`. For the tangent process, the two-sided exit law is governed by its zero-scale function `W`; in particular the relevant tangent exit probability is

`p_*(A)=W(A)/W(2A)`,

not naively `1/2` at fixed `A`.

A future finite-separation target could therefore be:

\[
\left|
 \mathbb P_{\mu_r}\{\text{upper log-band exit before lower log-band exit}\}
 -p_*(A)
\right|
\le C r^\eta,
\]

plus a summable control of overshoots and of the law of the next modulator state. This would compare the **stopped band kernel** to the recurrent tangent kernel rather than force pointwise drift estimates for every state.

No such estimate is proved here. It is recorded because it removes two artificial burdens at once: pointwise angular uniformity and direct control of the raw first moment of a singular log increment.

The source quantifier is kept conservative. Burdzy's page fixes arbitrary starting points `x_0,y_0` before posing Problem 5 and does not explicitly restate an existential starting-point quantifier in part (ii). Therefore a result only for a randomized stationary entrance law would be PARTIAL unless one also proves a source-faithful bridge from fixed distinct starting points.

## 7. What a proof has to contain that none of the existing routes contains

The missing object is now more precise than “better linearization.” A successful positive proof needs a **regeneration/entrance-law theorem for the full reduced state**, with three components:

1. **Entrance control.** From a source-valid fixed initial pair, reach a scale-free compact good state with positive probability without a catastrophic one-sided change in log separation.
2. **Critical-kernel comparison.** On geometric separation scale `r`, compare the stopped nonlinear band kernel, averaged under its entrance law, to the exact tangent critical kernel with error `O(r^eta)` or another summable rate.
3. **Iteration.** Show that the entrance-law error, band overshoot and corner/far-excursion exceptional probabilities remain summable under repeated returns so that critical recurrence survives the perturbation.

Every previous route supplies at most one of these pieces. None supplies all three.

## 8. Simplest special case still unproved

The simplest nontrivial special case I would now isolate is:

- unit exterior disc;
- very small deterministic initial separation `r`;
- both particles start on/near the circle in the post-projection tangent regime;
- the scale-free modulator is initialized from the limiting stationary/reversible entrance law suggested by the zero-separation circle excursion trace;
- prove recurrence of the geometric separation-band skeleton, or equivalently prove a summable comparison of its stopped band kernel with the critical tangent kernel.

This is deliberately weaker than Burdzy's literal fixed-start question and therefore would be labeled **PARTIAL**. It removes the fixed-start-to-regeneration issue and isolates the finite-separation kernel comparison itself.

## 9. Nearest solved problem and what it has that this problem lacks

The nearest solved **quantitative mechanism** is Burdzy's 2009 bounded-domain differentiability theorem for reflected stochastic flows. It proves differentiability at stopping times defined by boundary local time and develops excursion estimates strong enough for geometric-scale control.

What that proof has that P0025 lacks is **compact global geometry**: the domain is smooth and bounded, so constants controlling excursions, boundary charts and projection errors can be made uniform globally. The exterior disc has a compact boundary but unbounded bulk, and the actual two-particle reduced state also carries an orientation/contact modulator. Run 33's `1/log R` tail only shows that far excursions can be made rare; it does not show that Burdzy's bounded-domain constants remain stable under a radius cutoff tending to infinity.

The closest recurrence literature is Lamperti/asymptotically-zero-drift theory, but that literature starts after the drift/variance or modulated-kernel hypotheses have been proved. Those hypotheses are exactly what is missing here.

## 10. Exactly one Section-I recovery choice

**RECOVERY CHOICE: PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

The next theorem-producing P0025 run should not retry the all-state Lamperti bounds. It should port the **local-time differentiability / excursion decomposition** from Burdzy 2009 to a stopped, regenerative exterior-circle block.

The intended route is:

1. work only in a fixed compact annulus near the unit circle and stop when the base excursion leaves it, so no constant depends on a radius `R(r)->infinity`;
2. use the exact exterior-circle excursion return law to restart after a bulk excursion rather than estimate the full physical-time excursion path;
3. use run 32's conformal frozen trace and speed-measure comparison to propose a scale-free entrance law for the angular modulator;
4. prove one stopped **band-kernel** comparison to the tangent process, including the corner layers;
5. only after that comparison exists, apply a critical recurrence compiler.

This is a route specification, not a theorem claim.

## 11. Next Section-B moves

If the next invocation remains on P0025, the recorded next triple is new for this target:

- **#7 TAKE THE LIMIT:** identify the limiting modulator/entrance kernel as `r downarrow 0`, not merely the limiting scalar multiplier;
- **#19 MAKE IT AN ALGORITHM:** explicitly define the regeneration and band-exit stopping rule so every failure mode is visible;
- **#28 REPLACE FOR ALL WITH TYPICAL:** prove the kernel estimate under the entrance law first, then separately attack the fixed-start bridge.

Do not replace these by another pointwise local lemma unless the band/regeneration construction itself produces one.

## 12. Status, audits, and validation budget

No theorem-sized or finite exhaustive claim is newly asserted in this mandatory thinking run. Therefore no new checker is appropriate, and none was manufactured merely to show the task executed.

Current source status: **OPEN**.
Current track status: **OPEN / STUCK_RECOVERY_1**.
Metric: `E_disk: 0 -> 0`.
Unchanged count: `3 -> 4`.
Independent source-closure audits: none applicable; no closure candidate exists.

This leaves two unchanged runs before the CLOSABLE six-run rotation threshold. A future restricted/regenerative theorem is PARTIAL unless it is bridged to the literal fixed-start source statement.

## 13. Scheduler/model control status

The platform limitation is still present. The exposed scheduler/task-update interface offers title, prompt, schedule (or relative start), timing mode, enabled state, and related task metadata. It exposes **no binding model-family field, no reasoning-effort field, no authenticated applied-run model telemetry, and no guaranteed hour-long execution field**. Thus `GPT-6 / maximum` remains prompt text only here; this run is GPT-5.6 Sol with reasoning level UNVERIFIED.

The operative implementation manifest also records the earlier P26 task ID `6aa7b43682948191b697d72fec69d539` returning `You cannot modify this task` in one context. That is an authorization/context boundary. Another authorized context may edit the task prompt, but there is no legitimate worker-side bypass. Enforcing GPT-6/maximum requires an owner/admin or product/backend scheduler surface that exposes persistent model/reasoning selectors and authenticated completed-run telemetry.

## 14. Structured ledger_delta

```yaml
ledger_delta:
  track: R06
  portfolio: CLOSABLE_OUTSIDE
  active_source:
    id: P0025
    citation: "Krzysztof Burdzy, My favorite open problems, Problem 5(ii)"
    source_status: OPEN
    current_status_checked: 2026-09-18
  original_assignment_preserved:
    id: I0056
    citation: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20"
    frozen_pair: "H_{5,5}, d=5, face_degree=5"
    normalization: "outer vertex boundary |partial_V K|/|K|"
    certified_interval: "[sqrt(5), sqrt(5)]"
    width: 0
    full_source_status: PARTIAL
    exclusions:
      - "Haslegrave-Panagiotis DOI 10.1002/rsa.20946 triangular/codegree-3 cases"
      - "Haslegrave-Panagiotis DOI 10.1002/rsa.20946 quadrangular/codegree-4 cases"
  metric:
    name: E_disk
    before: 0
    after: 0
  unchanged_count:
    before: 3
    after: 4
  status: OPEN_STUCK_RECOVERY_1
  tried_moves: [2, 21, 27]
  recovery_choice: PORT_TECHNIQUE_FROM_NEAREST_SOLVED_PROBLEM
  simplest_unproved_special_case: "small separation with limiting stationary/reversible modulator entrance law; recurrent separation-band skeleton"
  remaining_obligation: "prove a regenerative full-state entrance law and a summable stopped-band-kernel comparison between the finite-separation exterior coupling and the critical tangent process, then bridge from fixed source starting points"
  evidence:
    - "Burdzy live open-problems page rechecked 2026-09-18"
    - "Cranston-Le Jan 1989 primary paper"
    - "Burdzy-Chen-Jones 2006 primary preprint/paper"
    - "Burdzy 2009 differentiability paper"
    - "runs/R06/20260918T0421Z_p0025_mellin_lamperti_33.md"
    - "operations/claims/P0025.md"
  audit_ids: []
  checker: NOT_APPLICABLE_THINKING_ONLY
```
