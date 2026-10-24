Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT on the newly admitted P0025 source metric: `E_disk: 0 -> 0`, unchanged count `0 -> 1`; Section-B methods #1 CHANGE THE CATEGORY, #12 FIND WHAT IS CONSERVED, #29 ADD THE POINTS AT INFINITY.**

# R06 — P0025 exterior-disc synchronous coupling / critical excursion cocycle

## 0. Continuity and non-reopening

I continued from the newest immutable R06 handoff,

`runs/R06/20260918T0120Z_benj_fs3_thales_rotation_handoff_30.md`

at creation commit `a9381cbde7dda4f7c5ad9406cdab18aaa0ae3359`. I did **not** reopen BENJ-2026-FS3 after its six-run rotation and did not reopen D0069.

The original assigned Lyons--Peres state is preserved exactly:

- Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20 asks
  > What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?
- R06 uses their outer vertex boundary convention
  `partial_V K={x notin K: x~y for some y in K}` and
  `Phi_V(G)=inf |partial_V K|/|K|` over nonempty finite `K`.
- the frozen admissible pentagonal regime `H_{5,5}` remains rigorously determined by R06 as
  `Phi_V(H_{5,5})=sqrt(5)`, hence certified interval `[sqrt(5),sqrt(5)]`, width `0`;
- the **full** Lyons--Peres Question 6.20 remains **PARTIAL**;
- triangular and quadrangular codegrees already covered by Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, remain excluded prior art and are not relabeled as R06 results.

The BENJ three-fixed-source target was the later lawful successor, but reached its six-unchanged rotation trigger in run 30. Its metric and handoff are frozen. This run therefore performs the mandated successor admission rather than a seventh BENJ attack.

## 1. Required repository read and lawful successor admission

Before mathematical work I read/recovered the current campaign and operations state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the latest R06 handoff, the current task-health reconciliation, the current new-methods implementation manifest, neighboring CLOSABLE reports, targeted intake rows, and the live claim surface.

The useful new live fact is that a source-shaped CLOSABLE row that was not in the earlier narrow queue screen is ownership-clear:

**P0025 — Krzysztof Burdzy, *My favorite open problems*, Problem 5(ii), “Convergence of synchronous couplings.”**

The author's current page, checked 2026-09-18, still states the problem as follows. Let `X,Y` be reflected Brownian motions in the same planar domain driven by the same Brownian motion. If `D` is the complement of a non-degenerate closed disc, is it true that

`P(limsup_{t->infinity} |X_t-Y_t| > 0)>0`?

I preserve the source's own setup and do not silently strengthen its starting-point quantifier. The nontrivial regime is distinct initial points.

Current-status evidence dated 2026-09-18:

- the current author page still lists Problem 5(ii) as open: `https://sites.math.washington.edu/~burdzy/open_mathjax.php`;
- exact/near-exact bounded searches for the exterior-disc synchronous-coupling limsup question found Cranston--Le Jan (1989), Burdzy--Chen--Jones (2006), differentiability/multiplicative-functional work, the Brownian-earthworm papers, and later one-particle boundary-local-time work, but no later source-matching proof or refutation;
- this is bounded negative search evidence, **not** a global novelty certification.

Immediately before ownership creation, `operations/claims/P0025.md` returned 404 and repository claim search found no P0025 owner. I then made the create-only canonical claim

`operations/claims/P0025.md`

at commit

`7daaafd515f422dcd802f626e7fb4e17eeb855fb`,

and read it back at that exact commit (blob `a1f212e120c96f361efa8c70f96f44fbfafe57fd`). No existing owner was overwritten.

Frozen source metric for the new target:

`E_disk in {0,1}`,

where `E_disk=1` only after the literal source question is fully proved or refuted on the page; otherwise `E_disk=0`. Restricted starting configurations, a tangent/linearized theorem, finite-time noncoalescence, simulation, or a sampled-time statement are **PARTIAL** and do not move the metric.

Baseline: `E_disk=0`.

## 2. Counterexample-first / #1 CHANGE THE CATEGORY — reduce to the circle excursion cocycle

I first attacked the **negation** of the source's expected positive-limsup behavior: can one prove that synchronous distance tends to zero by importing a contraction/Lyapunov argument?

The direct route fails at an exact critical point, and the reason is stronger than the old qualitative obstruction.

Scale the disc to radius one. Cranston--Le Jan (1989), *On the noncoalescence of a two point Brownian motion reflecting on a circle*, prove that two synchronously driven reflected Brownian particles in the **exterior** of the unit disc do not meet in finite time a.s. They reduce the two-point geometry to a reflected diffusion with half-separation

`z_t=|X^1_t-X^2_t|/2`

and a combined reflection local-time clock `phi_t`. In their coordinates `(x_t,y_t,z_t)`, on the support of `d phi_t`,

`x_t^2+(|y_t|-z_t)^2=1`,

and

`d z_t = (1/2)(z_t-|y_t|) d phi_t`.

Writing

`a_t:=|y_t|-z_t`,

this gives the exact local identity

`d log z_t = - a_t/(2 z_t) d phi_t`.

Thus an individual reflection increment **expands** the separation precisely on contacts with `a_t<0`; on the contact circle this expanding set is the thin strip `-z_t <= a_t <0`. When `z_t` is small, the expansion/contraction question is therefore an occupation-balance problem in a shrinking layer, not a pointwise monotonicity problem.

This already kills the simplest counterexample-to-Burdzy route: there is no global sign forcing `z_t` down in the exterior disc.

The more powerful category change is to pass from finite separation to the derivative of the reflected stochastic flow with respect to initial condition. Burdzy's differentiability/multiplicative-functional framework and the Brownian-earthworm paper express the tangent derivative as alternating deterministic curvature evolution and orthogonal projections between tangent spaces at excursion endpoints. For the exterior **unit circle**, rotational symmetry reduces the norm process to a one-dimensional additive excursion cocycle.

This is the right category because the full finite-pair question is nonlinear, while the infinitesimal separation process can be analyzed exactly.

## 3. Prior-art boundary: the zero first-order Lyapunov exponent is already known

This run must not relabel the critical exponent as new.

Burdzy--Chen--Jones (2006), Proposition 2.3, computes the planar synchronous-coupling Lyapunov functional for the exterior of the unit disc and obtains exactly zero. Their exterior-disc calculation uses the circle excursion/harmonic kernel; the curvature term and the excursion projection term cancel.

The later *Brownian earthworm* paper explicitly emphasizes the same obstruction: in dimension two the analogous exponent is zero, and this critical value is why the two-dimensional nonconvergence question remains open. Thus:

`mean tangent log-growth per unit boundary local time = 0`

is **KNOWN PRIOR ART**.

What I compute below is the *full positive-moment cumulant* of that circle tangent cocycle and, in particular, its exact second-order fluctuation rate. I found no occurrence of this exact gamma-ratio extension in the bounded search performed this run, but novelty is **UNVERIFIED** and is not asserted.

## 4. #12 FIND WHAT IS CONSERVED — exact cumulant of the critical tangent cocycle

### 4.1 Excursion kernel and one-excursion multiplier

Parameterize the unit circle by angle. For a Brownian excursion in the exterior starting at one boundary point and ending at relative angular displacement `alpha`, the boundary excursion kernel appearing in the exterior-disc calculation is

`nu(d alpha) = d alpha / [4 pi sin^2(alpha/2)]`,

for `0<alpha<2 pi`.

For a one-dimensional tangent vector, projection from the starting tangent line to the ending tangent line multiplies its norm by

`|cos alpha|`.

Hence its logarithmic jump is

`f(alpha)=log|cos alpha| <= 0`.

The exterior unit circle has deterministic shape/curvature contribution `+1` per unit of boundary local time in the multiplicative-functional normalization. Therefore, if `ell` denotes the local-time clock, the tangent log-norm cocycle has the exit-system form

`S_ell = ell + sum_{excursions e up to ell} f(alpha_e)`.

Because

`f(alpha) = -alpha^2/2 + O(alpha^4)` as `alpha->0`

whereas

`nu(d alpha) ~ d alpha/(pi alpha^2)`,

we have `int |f| dnu < infinity`. The logarithmic singularities at `alpha=pi/2,3pi/2` are integrable as well. Thus the raw finite-variation excursion sum is well-defined on finite local-time intervals. Also `int f^2 dnu<infinity`.

Rotational invariance makes the exit-system characteristic independent of the current boundary angle, so for every `q>0` the per-unit-local-time positive-moment cumulant is

`Psi(q)= q + F(q)`,

where

`F(q)= int_0^{2pi} (|cos alpha|^q-1) d alpha/[4 pi sin^2(alpha/2)]`.

### 4.2 Exact evaluation of `F(q)`

Set

`t=tan(alpha/2)`,

and

`r(t)=|1-t^2|/(1+t^2)=|cos alpha|`.

The two half-circles combine to give

`F(q)=(1/pi) int_0^infinity [r(t)^q-1]/t^2 dt`.

For `q>0`, integration by parts is legitimate: at zero and infinity the boundary term vanishes, while the integrable singularity at `t=1` is of order `|1-t|^{q-1}` after differentiation. Since

`d/dt log r(t) = -4t/(1-t^4)`

on both sides of `t=1`, we obtain

`F(q)=-(4q/pi) int_0^infinity r(t)^q/(1-t^4) dt`.

Pair the intervals `(0,1)` and `(1,infinity)` using `t -> 1/t`. The pair collapses exactly to

`int_0^infinity r(t)^q/(1-t^4) dt
 = int_0^1 r(t)^q/(1+t^2) dt`.

Now put `theta=arctan t`. On `0<t<1`,

`r(t)=cos(2 theta)`

and `dt/(1+t^2)=d theta`. Hence

`int_0^1 r(t)^q/(1+t^2) dt
 = int_0^{pi/4} cos^q(2 theta) d theta
 = (1/2) int_0^{pi/2} cos^q u du
 = (sqrt(pi)/4) Gamma((q+1)/2)/Gamma((q+2)/2)`.

Substitution gives the exact formula

`boxed{ F(q)= -(q/sqrt(pi)) Gamma((q+1)/2)/Gamma((q+2)/2),  q>0. }`

Therefore

`boxed{ Psi(q)=q [1 - Gamma((q+1)/2)/(sqrt(pi) Gamma((q+2)/2))],  q>0. }`

This is the principal mathematical output of this run.

### 4.3 The known cancellation and a nonzero second-order invariant

Define

`A(q)=Gamma((q+1)/2)/(sqrt(pi) Gamma((q+2)/2))`.

Then `A(0)=1`. Moreover

`d/dq log A(q)|_{q=0}
 = (1/2)[psi(1/2)-psi(1)]
 = -log 2`.

Consequently

`Psi'(0)=0`,

recovering the **known** zero Lyapunov drift, while

`boxed{ Psi''(0)=2 log 2 >0. }`

Equivalently,

`boxed{ int_0^{2pi} [log|cos alpha|]^2 d alpha/[4 pi sin^2(alpha/2)] = 2 log 2. }`

So the first-order contraction/expansion exactly cancels, but the tangent log-separation is not degenerate: its finite-variance fluctuation rate per unit local time is exactly `2 log 2`.

Also, because the digamma function is strictly increasing,

`d/dq log A(q)<0`

for `q>0`, so `A(q)<1` and

`Psi(q)>0`

for every `q>0`.

This is a useful warning against reading the zero mean exponent as deterministic neutral behavior: every positive moment of the tangent multiplicative functional has a strictly positive exponential rate in the local-time clock.

### 4.4 Consequence for the linearized problem only

The centered tangent log-cocycle has finite nonzero variance rate `2 log 2`. In the homogeneous exit-system formulation it is a nonconstant centered finite-variance Lévy additive functional. Standard finite-variance Lévy/random-walk recurrence/LIL machinery therefore makes the **linearized** log-norm oscillatory rather than drifting monotonically to `-infinity`.

I record this only as a theorem about the tangent/derivative cocycle. It is **not** promoted to a theorem about a fixed finite initial separation.

## 5. Why the source problem is still open after this calculation

The exact cumulant does not by itself transfer from infinitesimal separation to the nonlinear two-point process.

The missing implication is of the form:

> when `|X-Y|=epsilon` is small, compare the next local-time block of the exact finite log-separation with the tangent cocycle with an error that is sufficiently small **uniformly over repeated visits to ever smaller epsilon**.

A fixed `o(1)` error per block is not enough: if the process makes infinitely many blocks, such errors can accumulate and create an artificial drift. What is needed is a scale-summable critical transfer estimate.

A clean target would be to prove, for `M=log|X-Y|` in a deep negative band and a fixed local-time block length `b`, estimates of the schematic form

`E[Delta M | M=-u] = O(e^{-c u})`,

`Var(Delta M | M=-u) = 2 b log 2 + o(1)`,

with uniform tail control and with the angular/normal state included. A Lamperti-type critical recurrence criterion could then be applied to rule out a one-way drift `M -> -infinity` and force recurrent returns to a fixed separation scale, which would imply the positive-limsup behavior sought by Burdzy.

The existing differentiability estimates in the reflected-flow literature are not yet in this scale-summable repeated-block form. The positive-exponent three-dimensional Brownian-earthworm proof can tolerate fixed small relative errors because it has a strict positive drift. At the planar **zero-drift** boundary, the sign of the second-order nonlinear bias matters and must be controlled.

Thus the exact blocker is now substantially sharper:

`boxed{ control the nonlinear bias of log-separation to a summable order relative to the centered tangent cocycle with variance rate 2 log 2. }`

## 6. #29 ADD THE POINTS AT INFINITY — infinity slows the clock but is not the first-order drift

The exterior planar domain is recurrent but unbounded. Physical time and boundary local time are therefore very different clocks.

Grebenkov (2021), *Statistics of boundary encounters by a particle diffusing outside a compact planar domain*, derives explicit boundary-local-time and first-crossing-time laws for the exterior of a disk. The first-crossing distribution has a very slow long-time decay caused by extremely long bulk excursions between boundary encounters.

This clarifies the role of infinity in P0025:

- long excursions can create huge physical-time gaps during which the boundary local-time clock barely changes;
- the critical tangent mechanism itself lives naturally in boundary local time, where the circle excursion kernel is homogeneous;
- therefore a proof must not silently replace `t->infinity` by a bounded-domain stationary boundary clock without justifying the time change;
- conversely, the first-order zero-drift obstruction is not created by infinity: it is the exact local-time cancellation already visible in the circle excursion kernel.

The next proof must handle both layers: (i) critical recurrence in the local-time/log-separation state, and (ii) the unbounded-domain time change back to physical time.

## 7. What was tried, what failed, and what is genuinely new this run

The three requested out-of-box moves produced distinct outcomes:

- **#1 CHANGE THE CATEGORY:** passing to the tangent stochastic-flow cocycle makes the exterior-circle criticality exactly computable. The attempted negative/contraction proof fails because the known first-order exponent is exactly zero.
- **#12 FIND WHAT IS CONSERVED:** the first cumulant cancels, but the second does not. The exact positive-moment cumulant is the gamma-ratio formula above and the exact variance rate is `2 log 2`. This is a concrete new R06 derivation; novelty in the literature is unverified.
- **#29 ADD THE POINTS AT INFINITY:** physical-time null-recurrent excursions are separated from the local-time critical cocycle. Infinity changes the clock dramatically but does not supply the missing sign.

No finite exhaustive claim arose, so I did **not** manufacture an `artifacts/` checker. The main claim is analytic and its derivation is written in full on the page. Numerical agreement would not certify the remaining nonlinear step.

## 8. Current source/literature audit, dated 2026-09-18

Primary/current items actually checked this run include:

1. Krzysztof Burdzy, current *My favorite open problems* page, Problem 5(ii), current author page still asking the exterior-disc limsup question.
2. M. Cranston and Y. Le Jan (1989), *On the noncoalescence of a two point Brownian motion reflecting on a circle*, Ann. IHP 25(2), 99--107: exterior-disc finite-time noncoalescence and the reduced two-point diffusion.
3. K. Burdzy, Z.-Q. Chen, P. Jones (2006), *Synchronous couplings of reflected Brownian motions in smooth domains*, Illinois J. Math. 50, 189--268: exterior-unit-disc Lyapunov functional equals zero; this is prior art.
4. K. Burdzy, Z.-Q. Chen, S. Pal, *Brownian earthworm*, arXiv:1011.5442: the three-dimensional positive-exponent mechanism and the explicit statement that the analogous two-dimensional exponent is zero/critical.
5. K. Burdzy (2009) and related reflected-flow differentiability work: multiplicative-functional/tangent projection framework.
6. D. S. Grebenkov (2021), arXiv:2012.05312 / J. Phys. A 54 015003: boundary-local-time/first-crossing distributions outside a disk and the very slow long-time tail from long exterior excursions.

Bounded search strings included the exact Problem-5(ii) wording, `exterior disc synchronous coupling limsup`, `Brownian earthworm dimension 2 exponent zero`, and searches for the gamma-ratio / `log cos` excursion expression. No source-matching later solution and no exact occurrence of the full cumulant formula were recovered. This is an access-limited search, not bibliographic completeness and not a novelty certificate.

## 9. Metric and status

New source metric:

`E_disk: 0 -> 0`.

This is the first unchanged run on P0025, so the supported unchanged count is

`0 -> 1`.

Status: **OPEN / PARTIAL**.

The source question is **not** proved or refuted. The tangent-cocycle theorem is a partial mechanism result only.

Next suggested Section-B moves, deliberately different from this run: **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #13 FIND WHAT ONLY INCREASES, #20 FIND WHY THE ALGORITHM FAILS**. Concretely: introduce local-time block length and separation scale, seek a Lamperti-scale Lyapunov/monovariant for the exact finite-separation chain, and isolate the first nonlinear bias term that prevents the tangent recurrence argument from transferring.

## 10. Model / reasoning / scheduler-control truthfulness

The GPT-6/maximum request is still **not enforceable** from the task-control surface exposed to this worker. The operative implementation manifest records exactly the controls actually available: task title/prompt, schedule or relative start, timing mode, and enabled state. It exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed hour-long execution field, and no authenticated completed-run model/reasoning attestation**. Therefore GPT-6 / maximum remains prompt text only from this surface.

Actually fixing this requires an authorized scheduler/product/backend surface that exposes persistent model and reasoning fields **and** authenticated applied-run telemetry, or platform support adding those controls.

The historical P26 task ID `6aa7b43682948191b697d72fec69d539` once returned `You cannot modify this task`. The repository's implementation record treats that as an authorization-context boundary. The lawful workaround is to use the owning/authorized task context (or have product/platform support change the permission/control surface), not to duplicate the task or bypass permissions. No scheduler or permission change was attempted in this run.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  lane: CLOSABLE_OUTSIDE
  preserved_origin:
    source: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20 / I0056"
    frozen_graph: "H_{5,5}"
    normalization: "outer vertex boundary, unweighted |partial_V K|/|K|"
    interval: "[sqrt(5), sqrt(5)]"
    width: 0
    full_source_status: PARTIAL
    exclusions:
      - "Haslegrave-Panagiotis triangular/codegree-3 cases"
      - "Haslegrave-Panagiotis quadrangular/codegree-4 cases"
  prior_successor:
    id: BENJ-2026-FS3
    status: PARTIAL_ROTATED_AFTER_SIX_UNCHANGED
    reopen: false
  active_target:
    id: P0025
    source: "Krzysztof Burdzy, My favorite open problems, Problem 5(ii)"
    exact_scope: "synchronous reflected Brownian motions in the complement of a non-degenerate closed disc; positive probability of positive asymptotic limsup separation"
    claim_commit: 7daaafd515f422dcd802f626e7fb4e17eeb855fb
    metric: E_disk
    before: 0
    after: 0
    movement: NO_MOVEMENT
    unchanged_count_before: 0
    unchanged_count_after: 1
    status: OPEN_PARTIAL
  tried_moves: [1, 12, 29]
  new_results:
    - "Cranston-Le Jan reduced SDE localizes instantaneous expansion to a shrinking contact strip a=|y|-z<0"
    - "for the exterior-unit-circle tangent excursion cocycle, F(q)=-(q/sqrt(pi))*Gamma((q+1)/2)/Gamma((q+2)/2), q>0"
    - "full tangent positive-moment cumulant Psi(q)=q[1-Gamma((q+1)/2)/(sqrt(pi)Gamma((q+2)/2))]"
    - "known critical drift Psi'(0)=0 is recovered without novelty claim"
    - "exact tangent log-variance rate Psi''(0)=2 log 2 >0"
    - "the remaining source obstruction is nonlinear critical transfer, not first-order tangent contraction"
  remaining_obligation: "prove a scale-summable nonlinear comparison between finite log-separation and the centered tangent excursion cocycle, then control the exterior physical-time/local-time change; or produce a rigorous counterexample to the positive-limsup statement"
  evidence:
    - "operations/claims/P0025.md @ 7daaafd515f422dcd802f626e7fb4e17eeb855fb (read back)"
    - "Cranston-Le Jan 1989"
    - "Burdzy-Chen-Jones 2006, Proposition 2.3"
    - "Burdzy-Chen-Pal, Brownian earthworm"
    - "Grebenkov 2021, exterior-disk boundary local time"
  audits:
    p26: NONE
    second_independent: NONE
  closure: false
```

## 12. Delivery boundary

This is the single immutable R06 report for the run. Aside from the allowed create-only P0025 ownership claim and this own-track report, I made no shared-root edit, no peer-track edit, no email/Gmail/Drive action, no public post, no purchase, no permission change, and no scheduler change.
