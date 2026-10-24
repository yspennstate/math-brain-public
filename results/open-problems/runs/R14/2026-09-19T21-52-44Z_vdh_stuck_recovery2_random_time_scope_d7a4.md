Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen VDH metric `lim Delta_dual,n`: `0 -> 0`; STUCK-RECOVERY-2/2, THINKING-ONLY; methods actually used: B10 DERANDOMIZE, B13 FIND WHAT ONLY INCREASES, B16 COMPUTE EVERY SMALL CASE.**

# R14 HARD OUTSIDE — VDH-8.3-DUALITY STUCK-RECOVERY-2: random-time profile diagnosis and source-level route correction

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN / mandatory second and final stuck-recovery / no new theorem claim.**

## 1. Continuity, ownership, and required reads

I resumed the canonical R14 assignment `VDH-8.3-DUALITY`; I did **not** reopen the stale native-title negative-margin perceptron, H0008, or P0157. The canonical claim still lists `R14` as exclusive owner after the HARD7-04 handoff.

Before this thinking run I reread/recovered the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the controlling new-methods owner directive, the current VDH claim, the newest R14 report, and the inherited HARD7-04 VDH quantitative-histogram report. I also checked recent R14 commit history to ensure there was no newer own report after the 20:49:59Z obstruction report.

The frozen metric remains

\[
\Delta_{\rm dual,n}
=\left|\frac{1-\nu_n^{\rm dual}}{\varepsilon_n}-1\right|,
\]

and remains at its inherited floor `0 -> 0`.

This run is deliberately **thinking-only** under Section I. I created no theorem artifact, checker, certificate, audit request, shared-root edit, peer-track edit, scheduler change, email, Drive item, or public post.

## 2. Current primary-source and prior-art check

I reopened the current source directly: Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated 4 August 2026, Notes on Section 8.3, printed p. 245 / PDF p. 255. The page still says that the bounded-degree near-critical configuration model was analyzed by Riordan, that bounded degrees miss the interesting finite-third-moment phenomena, and then asks about the supercritical second-largest component and whether **“the discrete duality principle still hold[s]?”**

I also reopened Oliver Riordan, *The phase transition in the configuration model* (CPC 21 (2012), arXiv:1104.0613). In the bounded-degree barely-supercritical regime Riordan proves the giant CLT, records degree-by-degree giant counts to `O_p(sqrt(n/epsilon_n))`, and obtains the supercritical `L_2` statement by applying his subcritical theorem to the remaining graph with the dual degree distribution. This is exactly the nearest solved mechanism the present route should imitate, but only at the source-relevant scale.

A second important current-status point comes from van der Hofstad--Janson--Luczak, *Component structure of the configuration model: Barely supercritical case* (RSA 55 (2019)). Under the finite-third-moment condition formulated as uniform integrability of `D_n^3`, the paper explicitly notes that a CLT for the barely-supercritical giant would be interesting and is not obtained by their method. Thus a full second-order random-profile duality theorem in the present unbounded-degree regime would require, or nearly contain, an additional open fluctuation theorem that is stronger than the source question R14 is assigned to close.

A bounded fresh search through the current date again did not locate a later primary theorem closing this precise finite-third-moment shrinking-window configuration-model duality question. This is bounded negative evidence, not a novelty certificate.

## 3. The exact blocking statement

The random-time idea from the preceding run would ideally upgrade the first-order residual profile to a fluctuation-level representation of the form

\[
\boxed{
N_{n,d}^{\rm out}
=
 n_d\xi_n^d
-
 a_{n,d}\bigl(L_{1,n}-\rho_n n\bigr)
+r_{n,d},
\qquad
 a_{n,d}
=\frac{d\,p_{n,d}\,\xi_n^{d-1}}{f_n'(\xi_n)},
}
\tag{3.1}
\]

in a topology strong enough that

\[
\|r_n\|_\star=o_p\!\left(\sqrt{n/\varepsilon_n}\right)
\tag{3.2}
\]

and strong enough to preserve the subcritical extreme-component law.

This is the exact stronger statement that currently blocks the random-time route. I am **not claiming (3.1)--(3.2)**.

The inherited first-order histogram theorem is much coarser:

\[
\sum_d(1+d)
\left|N_{n,d}^{\rm out}-n_d\xi_n^d\right|
=o_p(n\varepsilon_n).
\tag{3.3}
\]

Since

\[
\frac{n\varepsilon_n}{\sqrt{n/\varepsilon_n}}
=\sqrt{n\varepsilon_n^3}\longrightarrow\infty,
\tag{3.4}
\]

(3.3) cannot by itself resolve fluctuation-scale random-time duality. This is the precise scale mismatch.

## 4. B10 — DERANDOMIZE: isolate the single latent fluctuation instead of adding iid profile noise

The preceding run proved that independent extinction thinning has the wrong marginal fluctuation scale: it produces only `sqrt(n epsilon_n)` total-count noise whereas the bounded-degree actual complement has `sqrt(n/epsilon_n)` noise.

The smallest plausible correction is not to add more independent randomness. It is to expose the **one common stopping-time fluctuation** already present in the exploration. In Riordan's bounded-degree clock parametrization, the deterministic survivor curve satisfies

\[
f_n(z(\tau))+\tau=1,
\qquad
z'(\tau)=-\frac1{f_n'(z(\tau))}.
\tag{4.1}
\]

Linearizing the degree-`d` survivor profile `n_dp z(\tau)^d` around the deterministic extinction time gives exactly the coefficient shape in (3.1). At bounded support, the clock noise transverse to this common time is lower order than the giant fluctuation scale, so the leading covariance is expected to be essentially rank one.

**Outcome of B10:** the previous iid-thinning proxy was over-randomized in the wrong direction. The natural latent variable is one common exploration-time displacement. But promoting that observation to the full unbounded-degree source regime would demand fluctuation-level control that the 2019 finite-third-moment theory does not supply.

## 5. B13 — FIND WHAT ONLY INCREASES: monotone survivor curves identify the common mode

For each degree class, the exponential-clock survivor count

\[
M_{n,d}(t)=\sum_{i:d_i=d}{\bf1}\{E_i>t\}
\]

is monotone decreasing in `t`. The deterministic comparison curve `n_d e^{-dt}` is also monotone. This makes the common stopping time a genuine one-dimensional order parameter: moving `t` shifts **every** degree class in a prescribed direction at once.

That monotonicity explains why the common-time mode can create the missing `sqrt(n/epsilon_n)` residual-size fluctuation without requiring independent classwise noise of that size. It also shows what an eventual second-order theorem would have to separate:

1. motion **along** the deterministic extinction curve, driven by the random giant stopping time; and
2. clock/exploration noise **transverse** to that curve.

Under the source's uniform integrability of `D_n^3`, the obvious adversarial mesoscopic tail `d\asymp1/epsilon_n` cannot carry order-one third-moment mass. This strongly suggests that transverse high-degree clock noise can be made negligible in low-order source observables at the giant-CLT scale, but proving the full vector statement would still amount to new fluctuation theory. I record this only as route evidence, not a theorem.

**Outcome of B13:** there is a clean monotone decomposition, but it points toward a stronger fluctuation problem than the source requires.

## 6. B16 — COMPUTE EVERY SMALL CASE: what finite-support models say, and why that does not close the source

I used finite-support symbolic scratch calculations only as a route diagnostic, not as a promoted finite claim or certificate. Across simple critical supports, the linearized extinction-time coefficients form a probability vector (`sum_d a_d=1`), exactly as required for the residual total-count fluctuation to be the negative of the giant-size fluctuation. This is consistent with Riordan's bounded-degree CLT mechanism and gives no evidence for an additional leading fluctuation direction in the bounded-support case.

Because this is a mandatory thinking-only run, I did **not** turn those scratch computations into an exact-arithmetic artifact. The useful conclusion is conceptual: finite support confirms that the random-time mode is the right second-order object where the CLT is already known, but it gives no legitimate shortcut through the source's unbounded-degree finite-third-moment regime.

**Outcome of B16:** the small cases support the random-time picture but also confirm that pursuing it now would mainly re-solve/extend the giant CLT rather than attack the source's minimal duality obligation.

## 7. Every route tried on this blocker, and why it failed

The VDH route has now tried the following distinct mechanisms.

1. **Scalar dual drift / branching duality.** This reached `Delta_dual,n -> 0` but cannot by itself identify the second-largest component.
2. **Collared component counting / truncation.** HARD7-04 obtained a leading source-size candidate for `C_2`, but the graph-level duality interpretation remained.
3. **Simultaneous weighted extinction histogram.** This yielded the first-order profile estimate (3.3), but it is too coarse for full marginal fluctuation equivalence.
4. **Conditional fresh-pairing duality.** R14 removed the unique-largest conditioning obstruction: conditional on the realized residual degree sequence, the complement is asymptotically a fresh CM. This solves the pairing-law issue, not the random-profile issue.
5. **Independent extinction thinning.** Refuted as a full marginal proxy by the variance-scale mismatch; total variation of the residual vertex counts tends to one in Riordan's bounded-degree regime.
6. **Random-time extinction tilt.** Structurally plausible and correct in spirit in bounded degree, but a source-regime theorem at the needed second-order scale runs into the still-missing barely-supercritical giant CLT / empirical-process fluctuation theory for unbounded degrees.

The decisive lesson is that **full marginal profile duality is stronger than necessary and currently points at a second open problem**. Continuing to chase (3.1) would violate the 90-percent rule by deepening an over-strong route rather than moving toward source closure.

## 8. What a source-level proof still has to contain

The source does not require a second-order CLT for the entire residual degree profile. The weakest useful missing bridge is instead a **uniform subcritical extreme-component stability theorem** over the random high-probability class of post-giant degree profiles.

Concretely, combine the already available ingredients:

- quenched fresh-pairing duality after deleting the giant;
- first-order weighted profile closeness (3.3);
- reflected subcritical drift `1-nu_n^{out}=epsilon_n(1+o_p(1))`;
- finite-third-moment uniform integrability and the inherited collar/high-degree controls;
- the source-size candidate
  \[
  |C_{2,n}|
  =(1+o_p(1))
  \frac{2R_*}{\varepsilon_n^2}
  \log(n\varepsilon_n^3).
  \]

What remains is a theorem of the following **type**, not yet proved here: uniformly over residual degree sequences in the high-probability class generated by giant deletion, the largest component of the fresh subcritical CM has the same leading extreme asymptotic. Such a stability theorem would close the source-level discrete-duality bridge without first solving the stronger fluctuation-level random-profile problem.

## 9. Simplest special case still unproved

The simplest useful special case is **not bounded degree** (Riordan already did that). It is a one-tail finite-third-moment class with an explicit cutoff `K_n -> infinity`, where degrees `<=K_n` are treated by Riordan-style dual-distribution arguments and the tail above `K_n` is controlled uniformly by the source's `D_n^3` uniform integrability plus the inherited collar estimates.

The target should be only the **leading largest-component extreme**, not whole-profile total variation or a giant CLT. The cutoff is to be chosen so that both the bounded core and the tail error are visible on the `epsilon_n^{-2} log(n epsilon_n^3)` component scale.

## 10. Nearest solved problem and what it has that the source lacks

Nearest solved problem: Riordan's 2012 bounded-degree near-critical configuration model.

What Riordan has that the present source lacks is uniform boundedness of the degrees. That allows the residual dual sequence to be controlled uniformly and lets the subcritical extreme theorem be applied directly after deleting the giant. In the present finite-third-moment source regime, the tail is unbounded and the residual sequence is random/selected by the giant exploration. The missing work is therefore **uniformity over that selected unbounded tail**, not another scalar duality identity and not a full marginal CLT.

## 11. Section-I choice and next proof-capable route

This recovery chooses exactly one Section-I action:

**PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

Port Riordan's bounded-degree dual-distribution/extreme-component argument only at the first-order source scale, using a moving cutoff and the existing finite-third-moment tail controls. Do **not** attempt to prove the stronger random-time CLT first.

The next proof-capable R14 run, if ownership remains unchanged, should target a uniform one-cutoff stability lemma for the largest component of the post-giant fresh CM. Fresh Section-B methods recorded for that attack:

- **B4 — PROVE SOMETHING WEAKER, COMPLETELY:** prove the one-cutoff stability theorem before any full profile process statement;
- **B21 — ASK WHO ELSE HAS THIS SHAPE:** port the exact bounded-degree extreme argument / subcritical given-degree technology, not the unrelated iid-profile law;
- **B30 — ONE SCALE AT A TIME:** first degrees `<=K_n`, then the tail, then glue only at the leading extreme scale.

Both permitted VDH stuck recoveries are now consumed. There is **no third recovery available** on this target. If the next proof-capable attempt leaves the same source-level obstruction and a later stuck episode occurs, R14 must terminally hand VDH off rather than create another recovery lemma.

## 12. Capability / scheduler-control honesty

The exposed automation control surface still has no binding model-family selector and no reasoning-effort selector. GPT-6/maximum therefore remains prompt text only; this run actually identifies as GPT-5.6 Sol and exposes no reasoning-effort telemetry, hence `UNVERIFIED`.

Changing that requires an authorized product/workspace/API/admin execution surface that actually exposes and persists model and reasoning controls. Historical `You cannot modify this task` errors such as the P26 case require the task's owning/admin-authorized context or platform support; the compliant workaround is **not** a permission bypass or duplicate task.

No scheduler or permission state was changed in this run.

## 13. Structured ledger delta

```yaml
ledger_delta:
  worker: R14
  lane: HARD_OUTSIDE
  source: VDH-8.3-DUALITY
  ownership: R14_EXCLUSIVE_UNCHANGED
  fixed_metric: "Delta_dual,n = |(1-nu_dual,n)/epsilon_n - 1|"
  fixed_metric_before: 0
  fixed_metric_after: 0
  movement: NO_MOVEMENT
  source_status: OPEN_PARTIAL
  run_kind: STUCK_RECOVERY_2_OF_2_THINKING_ONLY
  methods:
    - B10_DERANDOMIZE
    - B13_FIND_WHAT_ONLY_INCREASES
    - B16_COMPUTE_EVERY_SMALL_CASE
  exact_blocker: "second-order random-time residual-profile approximation strong enough for extremes; current weighted-l1 error o_p(n epsilon) is much larger than sqrt(n/epsilon)"
  route_diagnosis:
    iid_extinction_thinning: REJECTED_AS_FULL_MARGINAL_PROXY
    common_random_time: STRUCTURALLY_PLAUSIBLE_BUT_OVERSTRONG_FOR_SOURCE
    finite_third_moment_giant_CLT: NOT_AVAILABLE_IN_INHERITED_PRIMARY_THEORY
  section_I_choice: PORT_NEAREST_SOLVED_TECHNIQUE
  next_target: "uniform one-cutoff leading-extreme stability for fresh subcritical CM on post-giant residual profiles"
  next_methods:
    - B4
    - B21
    - B30
  stuck_recoveries_consumed: 2
  third_recovery_allowed: false
  closure: false
  independent_audits_for_this_route: 0
  artifacts_created_this_run: 0
```
