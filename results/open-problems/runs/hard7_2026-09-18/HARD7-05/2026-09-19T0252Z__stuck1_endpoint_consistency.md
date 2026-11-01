Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-05 frozen source metric has no movement, `W_{1/4}=0 -> 0`; Section-I STUCK1 methods: B20 / B22 / B23.**

# HARD7-05 bounded research iteration — STUCK1: endpoint-consistency barrier for the global Slepian route

Status: **PARTIAL / source OPEN / STUCK1**. This is the required Section-I thinking run after three consecutive runs with no movement in the fixed admission metric. In accordance with the owner directive, this report deliberately does **not** manufacture another theorem/checker or promote a narrower lemma as metric movement. It identifies the precise obstruction, audits the route against the closest rigorous literature, and chooses exactly one recovery action for the next bounded run.

## 1. Continuity, repository state, source status, and ownership

I resumed the exclusive claim

`operations/claims/MOLCHAN-2025-THETA2H.md`

owned by HARD7-05. I read the controlling hard7 file, the latest new-methods policy and owner directive, `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the latest HARD7-05 checkpoint, and the newest neighboring HARD7-04/HARD7-06 state visible on `master`. No ownership collision or posting exclusion was found for the precise Molchan target.

The source remains G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265, now indexed as **v11**. The current PDF still states, for the one-sided interval `(0,T)`, that the exponent values for `alpha=2, H != 1/2` remain an unsolved problem. Thus this track must remain OPEN/PARTIAL rather than CLOSED.

A fresh bounded literature check searched the exact arXiv identifier/title, `theta_{2,H}`, integrated-fBM persistence, and 2026 follow-ups. It found the same source and the established boundary-asymptotic paper

- F. Aurzada and M. Kilian, *Asymptotics of the persistence exponent of integrated fractional Brownian motion and fractionally integrated Brownian motion*, Theory Probab. Appl. 67(1) (2022), arXiv:2007.01254,

but no later exact formula for the full interior function `H -> theta_{2,H}`. This is bounded negative evidence only, not proof of worldwide novelty/openness.

The fixed tracked quantity remains the admission quantity

\[
W_{1/4}=U_{1/4}-L_{1/4}.
\]

The track's previous exact special-point argument gave `W_{1/4}=0`, so this run is necessarily

\[
\boxed{W_{1/4}:0\longrightarrow 0.}
\]

That saturation is exactly why Section I now governs the run.

## 2. B20 — find why the current algorithmic route cannot be global

Run 6 proposed the following global comparison direction. Write `R_H(t)` for the variance-one Lamperti covariance of integrated fBM and

\[
K_m(s)=\frac{\cosh((1-2m)s/2)}{\cosh(s/2)},\qquad 0<m\le \frac12.
\]

Molchan v11, Statement 1.4, assigns the stationary comparison family the exact persistence rate

\[
\theta(K_m)=\frac{3m}{8}.
\]

If we time-rescale by

\[
c(H,m)=\frac{4H}{3m},
\]

then the rescaled reference process has persistence rate

\[
 c(H,m)\,\theta(K_m)=\frac H2.
\]

Thus an all-lag covariance domination

\[
\boxed{
R_H(t)\ge K_m\!\left(\frac{4H}{3m}t\right)\quad\text{for every }t\ge0
}
\tag{BLOCK-COMP}
\]

would combine with Slepian and the classical lower bound `theta_{2,H} >= H/2` for `H<1/2` to force `theta_{2,H}=H/2` at that `H`.

The crucial consistency check comes from Aurzada--Kilian's rigorous Theorem 1:

\[
\frac{\theta_{2,H}}{H}\longrightarrow 1\qquad(H\downarrow0).
\tag{AK}
\]

Therefore **(BLOCK-COMP) cannot be available with persistence rate `H/2` for all sufficiently small `H`**. If it were, Slepian would imply `theta_{2,H}/H <= 1/2` along those same `H`, contradicting (AK). This is not a new source theorem; it is a necessary consistency consequence of an existing published theorem.

This observation sharply localizes what was wrong with the *global* ambition in run 6. The scalar limiting comparison with an exponential kernel is **not** refuted here. What is ruled out is upgrading that limiting picture to a finite-`m`, all-lag comparison of rate `H/2` uniformly through the small-`H` regime. Somewhere in the finite-`m` comparison hypotheses/order there must be an `H`-dependent boundary layer or another failure. That failure has not yet been located explicitly.

This is the main B20 outcome: do not spend another run trying to prove a theorem that would contradict the established endpoint asymptotic. The next useful action is to expose the exact comparison failure.

The previous exact interior points `H=1/5,1/4,1/3` and their certified local neighborhoods are not contradicted by (AK), because they are bounded away from `H=0`. This report does not retract them.

## 3. B22 — read the solved mechanisms and the failure modes, not only the successful inequalities

Two nearby solved regimes explain what is missing.

### 3.1 Source-matched endpoint asymptotics: Aurzada--Kilian

Aurzada--Kilian normalize the Lamperti transform `U^H` of integrated fBM and rescale time by `1/H` as `H downarrow 0`. They prove pointwise covariance convergence

\[
\rho_H(\tau/H)\longrightarrow e^{-\tau},
\]

the Ornstein--Uhlenbeck covariance, and then verify the **uniform tail and local-regularity hypotheses** required by a persistence-exponent continuity theorem. Because the OU persistence rate is `1`, this yields (AK).

What this proof has that the current exact-comparison route lacks is a theorem that remains stable under the singular parameter-dependent time rescaling. Pointwise covariance convergence alone is not enough. The local regularity and tail conditions have to remain uniform. The Molchan `K_m` comparison family becomes singular as `m downarrow 0`, exactly the kind of regime in which naive pointwise comparison/limit intuition can be misleading.

### 3.2 Nearest fully exact non-Brownian integrated-process analogue: Profeta--Simon

C. Profeta and T. Simon, *Persistence of integrated stable processes*, Probab. Theory Relat. Fields 162 (2015), solve the stable-Levy analogue. For a strictly `alpha`-stable Levy driver with positivity parameter `rho`, their Theorem A gives

\[
\theta=\frac{\rho}{1+\alpha(1-\rho)}.
\]

Their proof explicitly exploits the Markov property of the bivariate process `(X,L)`, where `X_t=\int_0^tL_s\,ds`, and studies the hitting place `L_{T_0}` using Mellin/Fourier structure. The paper says directly that the tail analysis is tied to the law of this hitting place and uses the Markov property in its reductions.

The integrated-fBM pair `(I_H,B_H)` loses that finite-dimensional Markov/independent-increment structure whenever `H != 1/2`. That is the precise ingredient the stable proof has and the Gaussian fractional problem lacks. Merely copying the hitting-place argument therefore does not port.

This B22 literature pass changes the research priority: the useful object is no longer another isolated polynomial factorization. It is the missing **parameter-uniform comparison/continuity mechanism**, or else an explicit demonstration of where the finite-`m` comparison breaks.

## 4. B23 — assume the opposite of the run-6 global picture

Instead of assuming the `theta=H/2` comparison mechanism extends throughout `0<H<1/2`, impose the published endpoint behavior (AK) as a non-negotiable constraint.

Then any exact-comparison architecture must have at least two regimes:

1. an interior regime where rate-`H/2` comparators may dominate and can close isolated points/open neighborhoods; and
2. a small-`H` regime where that domination must fail and the normalized rate rises toward `1` after `1/H` Lamperti rescaling.

This makes the hidden transition itself a concrete object. One should seek the first `(H,m,t)` at which the finite comparison reverses, rather than try to prove it globally.

No source claim is labeled REFUTED. The **global comparison route** is what is being abandoned; the Molchan source problem remains OPEN.

## 5. Section-I five-part stuck diagnosis

### (a) Exact blocking statement

The present comparison program needs, at a new interior `H`, an all-lag domination of the form

\[
\boxed{
\exists m\in(0,1/2]\quad
R_H(t)\ge K_m\!\left(\frac{4H}{3m}t\right)
\quad\forall t\ge0,
}
\tag{S}
\]

with the known reference exponent then matching the lower bound `H/2`. For the simplest next rational point proposed below, `H=2/5`, no such full certificate is currently in this track.

At the same time, (AK) proves that (S) cannot remain true with this rate mechanism throughout all sufficiently small `H`. A complete proof program must therefore explain both the interior successes and the forced endpoint failure.

### (b) Every route tried and the precise reason it has not closed the source

- **B2/B5/B11 (run 1):** covariance-boundary attacks, Hurst interpolation and covariance-operator duality. They produced structural formulas/barriers but no exact new `H` and no full function.
- **B6/B17/B30 (run 2):** deformation from `H=1/2`, exact positive covariance tangent, Markov-anchor analysis and spectral scale split. The tangent is only first-order at one parameter; finite all-lag order over a nontrivial interval was not obtained.
- **B3/B15/B24 (run 3):** stronger comparison, symmetry breaking and extremal covariance defect. This closed the tracked special point `H=1/4`, but a special point is PARTIAL for the source.
- **B1/B4/B13 (run 4):** category change, weaker complete theorem, monotonicity. This produced a second exact point `H=1/3`, still not the full source.
- **B21/B27/B29 (run 5):** analogy search, quantifier swap and boundary compactification. Strict comparison gave nonempty exact neighborhoods around certified anchors, but no explicit covering of the whole Hurst interval.
- **B7/B16/B18 (run 6):** scaling limit, exact small case and reformulation into a two-variable scalar inequality. This produced the `H=1/5` point and suggested a global route, but the global extension is incompatible with the rigorous small-`H` asymptotic (AK); its finite-`m` upgrade must fail somewhere.
- **B20/B22/B23 (this run):** located the literature-imposed endpoint barrier, identified the missing uniformity mechanism, and deliberately reversed the global hypothesis. This is a thinking diagnosis, not a new theorem.

### (c) What a proof must contain that no route so far contains

A successful source-level method needs at least one of the following genuinely new ingredients:

1. a parameter-uniform variational/differential formula for the persistence exponent itself, not merely binary covariance order;
2. a family of solvable comparators whose known persistence rates interpolate with the **correct** endpoint normalization `theta/H -> 1`, while retaining all-lag covariance control; or
3. a rigorous decomposition of the `(H,t)` plane into interior and endpoint boundary layers, with exact control of the transition and no loss in Slepian direction.

Every current route lacks this global compatibility. Exact factorization at isolated rational `H` is not enough.

### (d) Simplest special case still unproved in this track

A concrete next source-valid point is

\[
\boxed{H=\frac25.}
\]

No existing HARD7-05 report certifies an exact value at `H=2/5`, and the nonempty neighborhoods proved earlier have not been given radii large enough to include it. The source lower bound gives `theta_{2,2/5} >= 1/5`; an exact comparison with a known-rate process at `1/5` would settle that point, but no such all-lag certificate is currently available.

### (e) Nearest solved problem and the ingredient it has that this one lacks

The closest *fully exact* non-Brownian integrated-process theorem I found is Profeta--Simon (2015), integrated stable Levy processes. Their exact exponent comes from the finite-dimensional Markov structure of `(X,L)` and the distribution/Mellin transform of the hitting place `L_{T_0}`. Integrated fBM has no finite-dimensional Markov pair `(I_H,B_H)` for `H != 1/2`, so their exact first-passage machinery does not transfer directly.

The closest *source-matched solved regime* is Aurzada--Kilian's `H downarrow 0` and `H upward 1` asymptotics. Their proof has a uniform persistence-continuity theorem after H-dependent Lamperti rescaling; the current exact-comparator route has no corresponding uniform control in its singular small-parameter family.

## 6. Exactly one Section-I recovery choice

**Chosen recovery: REFUTE INSTEAD OF PROVE — refute the proposed global finite-`m` comparison route, not the source problem.**

The next bounded run should hunt an explicit exact counterexample to the rate-`H/2` covariance domination forced to fail by (AK): find rational/algebraic data `(H,m,t)` with small `H` such that

\[
K_m\!\left(\frac{4H}{3m}t\right)>R_H(t).
\]

The goal is to expose the hidden boundary layer and thereby prevent further work on an impossible global route. A finite candidate is not source progress until checked exactly; if found, it should receive an exact arithmetic/symbolic checker under `artifacts/hard7_2026-09-18/HARD7-05/`. If no explicit counterexample emerges, the run should prove a structural reason that one must occur without mislabeling the source as refuted.

The next Section-B triple is **B8 / B19 / B26**:

- **B8 (discretize):** reduce the `(H,m,t)` search to rational/algebraic test points with rigorous enclosure.
- **B19 (make it an algorithm):** construct a certified search that isolates sign changes in the covariance defect rather than a floating-point grid.
- **B26 (hunt the sporadic case):** seek the first small-H boundary-layer failure, since endpoint asymptotics guarantee the global mechanism cannot survive all the way to zero.

This is one recovery choice, not three separate recovery actions.

## 7. Capability honesty / scheduler issue requested by the owner

The situation is still as follows in the interface exposed to this run: the automation surface provides prompt/title/schedule/timing/enabled controls but **no model-family selector, no reasoning-effort selector, no authenticated model telemetry, and no guaranteed execution duration**. Consequently GPT-6 maximum cannot be set or verified here; the prompt request does not change the actual runtime identification stated on line 1.

The repository's latest `RESULTS.md` also reconciles an important nuance about the historical P26 error: one context had returned `You cannot modify this task`, while a later authorized context successfully updated P26. Therefore the correct workaround for a task that rejects modification is to use the task-owning/authorized workspace or account context (or platform support), not clone the job, bypass ownership, or claim a denied edit succeeded. This run was expressly instructed not to modify/create schedules, so no scheduler edit was attempted.

To actually guarantee GPT-6/maximum for these jobs would require the platform/native scheduler to expose a model selector plus reasoning-effort selector (or authenticated runtime policy/telemetry) in the authorized task context. Those controls are not exposed here.

## 8. Bookkeeping kept to the final ten percent

No new finite theorem is claimed in this STUCK1 thinking run, so no redundant checker/output artifact was created. The mathematical work was the route diagnosis and literature consistency audit above. This obeys the owner directive that a stuck thinking run should not manufacture another lemma/certificate merely to prove that it ran.

```yaml
ledger_delta:
  track: HARD7-05
  source_id: MOLCHAN-2025-THETA2H
  status: PARTIAL
  stuck_stage: STUCK1
  metric: W_{1/4}
  before: 0
  after: 0
  movement: no movement
  methods: [B20, B22, B23]
  source_status: OPEN
  key_obstruction: "A global finite-m Slepian comparison with reference rate H/2 is incompatible with the rigorous Aurzada-Kilian asymptotic theta_{2,H}/H -> 1 as H downarrow 0; the finite-m all-lag comparison must fail in an H-dependent regime."
  simplest_unproved_special_case: "H=2/5"
  recovery_choice: "REFUTE INSTEAD OF PROVE: expose an exact small-H covariance-order counterexample to the global rate-H/2 comparison route"
  next_methods: [B8, B19, B26]
  checker_created: false
  closure: false
```
