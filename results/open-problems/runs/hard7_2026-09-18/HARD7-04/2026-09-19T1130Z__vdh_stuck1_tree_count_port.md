Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen metric `lim Delta_dual,n`: `0 -> 0`; this is the mandated STUCK1 thinking/recovery run; methods actually used: B18 SAY IT IN ANOTHER LANGUAGE, B22 READ THE FAILURES NOT THE SUCCESSES, B30 ONE SCALE AT A TIME. No new theorem-sized or finite mathematical claim is made in this run.**

# HARD7-04 bounded research iteration — STUCK1 and the tree-count lower-bound port

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN / STUCK1**.

## 1. Continuity, ownership, required reads, and runtime capability

I resume the admitted target rather than restart admission or return to the released I0049/P0157 work. The exclusive claim remains

`operations/claims/VDH-8.3-DUALITY.md`,

owned by `HARD7-04`, status OPEN / ADMITTED.

The source remains Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, printed p. 245 / PDF p. 255,

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`.

In the finite-third-moment barely-supercritical configuration-model discussion the source asks, after explaining that the high-degree vertices should be swallowed by the unique giant and that the second component is expected to have Erdős--Rényi-like behavior,

> “Does the discrete duality principle still hold?”

The retained source regime is the deterministic-degree configuration model with

\[
\nu_n=1+\varepsilon_n,\qquad \varepsilon_n\downarrow0,\qquad
\varepsilon_n n^{1/3}\to\infty,
\]

finite convergent third degree moment, positive limiting mean, and the source's nondegenerate critical limiting degree law.

Before doing new thinking I re-read/recovered the controlling files `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the active claim; the complete indexed HARD7-04 chain through `2026-09-19T1030Z__vdh_cramer_collar_upper_bound.md`; and the newest visible neighboring HARD7-03/HARD7-05 reports. No release, competing canonical claim, posted equivalent, or external source-resolution record was found for `VDH-8.3-DUALITY`.

The scheduler capability limitation is still exactly the one recorded by the controlling policy. The exposed native automation schema offers prompt/title, schedule/timing mode, enablement, and task identity/update fields; it exposes **no model selector and no reasoning-effort selector**. GPT-6/maximum therefore remains text-requested only. This run's actual model is GPT-5.6 Sol; reasoning level is not exposed and is recorded as UNVERIFIED. Changing that requires a platform/scheduler feature (or an authorized interface exposing such selectors), not a repository edit. I did not mutate or probe any other schedule because this worker is explicitly prohibited from doing so.

The historical P26 modification failure also remains an access/ownership issue rather than a mathematical one. `NEW_METHODS_2026-09-16.md` records probes returning `You cannot modify this task` for P26/P01/P03 in one native context; `RESULTS.md` later records that P26 was editable in another authorized context. The compliant workaround is therefore to use the authorized task/account/workspace context that owns the task, or platform support if that context cannot be reached. Do **not** bypass the restriction and do **not** create a duplicate schedule.

## 2. Fresh source/current-literature check — 19 September 2026

I refreshed the exact source wording and the combinations `barely supercritical configuration model second largest component`, `configuration model discrete duality`, and `largest subcritical component given degree sequence`.

The source PDF still poses the discrete-duality question in the Notes on Section 8.3. The directly relevant records remain:

1. Remco van der Hofstad, Svante Janson, and Malwina Łuczak, *Component structure of the configuration model: Barely supercritical case*, Random Structures & Algorithms (2019). It gives precise asymptotics for the giant in the barely-supercritical regime but does not determine the second-largest component required by the source question.
2. Matthew Coulson and Guillem Perarnau, *Largest component of subcritical random graphs with given degree sequence*, Electronic Journal of Probability 28 (2023), DOI `10.1214/23-EJP921`, arXiv `2111.11780`. Its main general configuration-model results are upper bounds. Theorem 1.3 requires, among other hypotheses, `Delta |Q| = o(R)`; Proposition 1.12 supplies specially constructed degree sequences showing tightness of some upper bounds, not a matching lower theorem for every source-valid sequence.
3. Tomasz Łuczak, *Component behavior near the critical point of the random graph process*, Random Structures & Algorithms 1 (1990), and the classical Erdős--Rényi near-critical theory. This is the nearest fully solved model for the sharp barely-subcritical largest-component scale.
4. van der Hofstad--Łuczak--Spencer, *The second largest component in the supercritical 2D Hamming graph*, which gives model-specific evidence for a discrete-duality phenomenon rather than a theorem for the deterministic-degree configuration model.

A bounded search on 19 September 2026 found no later paper closing the exact source scope. This is **bounded negative evidence only**, not a worldwide novelty certificate.

## 3. Frozen metric and why this run is STUCK1

The frozen admission quantity is

\[
\Delta_{\rm dual,n}:=
\left|\frac{1-\nu_n^{\rm dual}}{\varepsilon_n}-1\right|.
\]

Earlier VDH runs proved that this quantity converges to zero, and then lifted the reflected criticality to the exact post-giant configuration-model remainder. The last three runs all therefore have the metric at its mathematical floor:

`lim Delta_dual,n: 0 -> 0 -> 0 -> 0`.

The immediately preceding run nevertheless proved the sharp **upper** leading constant

\[
L_1^{\rm post}\le (1+o_p(1))\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3),
\]

but the fixed metric did not move. Under the owner's Section-I rule this invocation is consequently a thinking-only STUCK1 recovery run. I do not reset the counter, substitute a new metric, or relabel a one-sided theorem as source closure.

---

# Section-I obstruction report

## 4(a). Exact blocking statement

Put

\[
N_n:=n\varepsilon_n^3\to\infty,
\qquad
R_*:=\frac{\mathbb E[D(D-2)^2]}{\mathbb ED}>0.
\]

The exact remaining source-level size obligation after the already proved post-giant reduction and sharp upper bound is the matching lower direction

\[
\boxed{
\forall\delta>0:\quad
\mathbb P\!\left(
L_1^{\rm post}<
(1-\delta)\frac{2R_*}{\varepsilon_n^2}\log N_n
\right)\longrightarrow0.
}
\tag{4.1}
\]

Here `L_1^{post}` is the largest component of the **exact** post-giant configuration model, which is w.h.p. the original graph's second-largest component. Equation (4.1), not another upper estimate, is the current blocker.

## 4(b). Routes tried and the precise reason each does not yet prove (4.1)

### Route 1 — ideal branching-process duality

The parameter-level dual law has already been pushed to

\[
1-\nu_n^{\rm dual}=\varepsilon_n(1+o(1)).
\]

**Why it stops:** a branching-process mean identifies the reflected drift but does not produce a component of the extremal logarithmic size. The largest component is an extreme-value statement over `n` dependent finite-population explorations, not a one-root survival estimate.

### Route 2 — exact post-giant stopping-time duality

Previous runs proved that at a lawful completed-component stopping boundary the sleeping remainder is exactly a configuration model on its random residual degrees and that its largest component is w.h.p. the original `C_{2,n}`.

**Why it stops:** this removes the model-identification problem but merely transfers the unresolved lower-bound question to a random barely-subcritical degree sequence. Exact duality of the *model* is weaker than sharp duality of the *largest-component extreme*.

### Route 3 — black-box the strongest simple subcritical degree-sequence theorem

The natural attempt was Coulson--Perarnau Theorem 1.3, whose leading upper expression is precisely of the desired `2R/Q^2` form.

**Why it stops:** its convenient hypothesis `Delta |Q|=o(R)` is false at the edge of the source class after removal of the giant. The preceding hub-stripping work obtained the sharp residual scale

\[
\frac{\varepsilon_n\Delta_n^{\rm post}}{\log N_n}
\le \frac{R_*}{2}+o_p(1),
\]

and source-valid families attain this scale. Thus no honest proof can silently strengthen the source assumptions until the Coulson--Perarnau small-hub condition holds.

### Route 4 — use a surviving hub as the large component

The counterexample-oriented hub analysis tested whether the largest post-giant degree could itself force the lower bound.

**Why it stops:** the sharp collar allows degrees of order `epsilon_n^{-1} log N_n`, but a near-subcritical progeny heuristic from such a root has scale only `degree/epsilon_n`, whereas the target in (4.1) is `2R_* epsilon_n^{-2} log N_n`. A maximal root is therefore not a uniform mechanism for the exact extremal constant. More importantly, turning this heuristic into a proof would still leave source-valid arrays in which no single root carries the target component.

### Route 5 — Cramér excursion from one root

The last run derived a shrinking-window exponential collar, the Cramér minimizer

\[
\theta_n\sim\frac{\varepsilon_n}{R_*},
\qquad
I_n\sim\frac{\varepsilon_n^2}{2R_*},
\]

and a robust two-atom anti-concentration estimate. These are enough for the **upper** tail by domination and a union/double count.

**Why it stops:** all inequalities point in the wrong direction for existence. Stochastic domination of the finite-population exploration by an iid walk gives an upper probability; it cannot lower-bound the probability of a long real component. A lower Cramér estimate must simultaneously enforce positivity of the queue, return to the absorbing state at the right scale, and avoid pairings back into the explored set.

### Route 6 — first-moment abundance below the threshold

At a formal saddle-point level, choosing

\[
t\approx (1-\delta)\frac{2R_*}{\varepsilon_n^2}\log N_n
\]

makes the large-deviation penalty `exp(-I_n t)` weaker than the number of available roots, so one expects many candidate components.

**Why it stops:** root events are highly overlapping because every vertex in one component reports the same event. Even after dividing by component size, a divergent first moment does not imply existence. The missing object is a source-uniform second-moment, Poisson-approximation, or disjoint-exploration argument at this extremal scale.

### Route 7 — conditioned Brownian/excursion heuristic

For `t` on the target scale, the queue area suggested by a diffusive excursion is of order `t^{3/2}`. The corresponding collision-exposure ratio is heuristically

\[
\frac{t^{3/2}}n
\asymp
\frac{(\log N_n)^{3/2}}{N_n}\to0.
\]

**Why it stops:** this is a scale calculation, not a uniform conditioned-excursion theorem for the triangular post-giant increment law. The law varies with `n`, retains a thin exponential collar rather than a uniform fourth moment, and the conditioning is exactly on the rare long excursion whose path geometry has to be controlled.

## 4(c). What a proof must contain that no route so far contains

A proof of (4.1) needs a genuine **abundance-and-decorrelation mechanism**, not another one-root upper estimate. In a form robust enough for the full finite-third-moment source class, it must supply all of the following in one argument:

1. a **lower** local large-deviation estimate for an exploration/tree component in a size window around `(1-delta)2R_* epsilon_n^{-2} log N_n`, with the correct exponent `epsilon_n^2/(2R_*)`;
2. a way to use a **window of sizes** rather than one exact lattice time, so that periodicity/span effects in the degree law cannot kill the lower estimate;
3. finite-population control showing that pairing depletion and self-collisions change the lower probability only by `exp(o(log N_n))` on that one scale;
4. a second-moment, switching, sprinkling, or disjoint-block device proving that the number of such components is positive w.h.p.;
5. a truncation argument that is uniform in the permitted post-giant hubs and then lets the degree cutoff grow, so the final leading constant uses the full `R_*` rather than the variance of an artificially bounded-degree core.

No existing HARD7-04 route contains item 4, and no existing route contains items 1--5 simultaneously. This is the exact structural gap.

## 4(d). Simplest special case still unproved on this track

The cleanest special case of the blocker is a deterministic barely-subcritical configuration model with **uniformly bounded degrees** and a fixed aperiodic three-point critical limit. A concrete normalization is

\[
D\in\{1,2,3\},\qquad
\mathbb P(D=1)=\frac38,
\quad \mathbb P(D=2)=\frac12,
\quad \mathbb P(D=3)=\frac18.
\]

This law satisfies the critical numerator `E[D(D-2)]=0`, has positive masses at consecutive degree values, and

\[
R_*=rac{\mathbb E[D(D-2)^2]}{\mathbb ED}=\frac37.
\]

Take deterministic degree sequences with these limiting proportions but with

\[
Q_n=-\varepsilon_n+o(\varepsilon_n),
\qquad
\varepsilon_n\downarrow0,
\qquad
\varepsilon_n n^{1/3}\to\infty.
\]

The simplest still-unproved lower statement on this track is then

\[
L_1\ge (1-o_p(1))\frac{6}{7\varepsilon_n^2}
\log(n\varepsilon_n^3).
\tag{4.2}
\]

Unlike the full source class, this toy regime has no high-degree obstruction, a fixed finite increment support, and span one. It isolates the missing abundance/decorrelation step without changing the critical mechanism.

I am **not** claiming (4.2) is new to the literature; it is the simplest source-relevant special case that this track has not yet proved. A fresh prior-art check must precede any theorem claim on it.

## 4(e). Nearest solved problem and the ingredient it has that this problem lacks

The nearest fully solved model is the classical barely-subcritical Erdős--Rényi random graph. The near-critical component theory of Łuczak and subsequent standard treatments obtains the sharp logarithmic largest-component scale using explicit component/tree enumeration and enough moment control to turn expected counts below the threshold into actual components.

The important transferable feature is **not** merely that the exploration walk has negative drift. Erdős--Rényi has an exact combinatorial counting structure: Cayley tree counts and independent-edge factors reduce the first and second moments of the number of tree components of a given size to explicit expressions that share the same saddle point. This supplies the lower extreme-value direction.

The closest general configuration-model paper, Coulson--Perarnau, supplies the complementary half: sharp Cramér-style **upper** bounds and specially constructed families where those bounds are tight. What is missing for the present problem is a source-uniform analogue of the Erdős--Rényi tree-count second moment for an arbitrary triangular deterministic degree sequence after giant deletion, particularly when the maximum residual degree sits at the sharp exponential-collar scale.

---

# 5. Three new Section-B moves

## B18 — SAY IT IN ANOTHER LANGUAGE: component existence as a tree-census coefficient problem

The lower bound should not be phrased first as “prove a conditioned random walk excursion theorem.” That formulation hides the global source of multiplicity. The more promising language is:

> Count tree components in one near-extremal size band and prove that the count is nonzero w.h.p.

For a configuration model, the candidate calculation can be organized by (i) choosing a vertex set, (ii) using Prüfer/tree enumeration to count internal pairings realizing a tree with the chosen degree multiset, and (iii) pairing all remaining stubs outside. Summing over subsets should lead to a coefficient/saddle-point expression involving the empirical degree generating polynomial. The lower-bound problem then becomes a two-variable coefficient asymptotic plus a second-moment comparison.

**Outcome:** promising reframing, not a proof. It directly targets abundance and multiplicity, which the one-root excursion language obscured. The exact coefficient identity and its uniform asymptotics are deliberately left for the recovery run; this STUCK1 report makes no new finite claim.

## B22 — READ THE FAILURES, NOT THE SUCCESSES

The most informative failure in Coulson--Perarnau is visible in the theorem architecture itself. Their sharp general results are upper bounds; tightness is demonstrated by constructed degree sequences rather than a universal lower theorem. The hypothesis `Delta |Q|=o(R)` also pinpoints where a clean walk approximation can ignore a single large jump. HARD7-04 has already shown that the source's post-giant sequence can live exactly outside that convenience regime.

The lesson is that a lower proof must **not** begin by asking for a uniform local CLT on the full untruncated residual law. That would likely reintroduce the same fourth-moment/max-degree barrier in a different form. Instead, the ER proof should be ported first to bounded degrees and then extended by a controlled truncation in which the error is measured against `R_*`.

**Outcome:** successful diagnosis. The next route should isolate the finite-support combinatorics before touching the sharp hub collar.

## B30 — ONE SCALE AT A TIME

Fix `delta>0`. Instead of controlling all component sizes, target only the band

\[
\mathcal I_n(\delta)=
\left[
(1-\delta)\frac{2R_*}{\varepsilon_n^2}\log N_n
-c_\delta\varepsilon_n^{-2},
(1-\delta)\frac{2R_*}{\varepsilon_n^2}\log N_n
ight]
\]

for a fixed positive `c_delta` chosen later. The hoped-for proof only needs to show that the number of tree components whose order lies in this band is positive w.h.p. A band, rather than a single order, has three advantages: it absorbs lattice effects, gives room for a saddle-point local limit, and lets one average second-moment errors over `Theta(epsilon_n^{-2})` neighboring sizes.

The port should then be executed in two nested cutoffs:

1. **fixed degree cutoff `K`:** prove the lower census for a bounded-support residual degree law, starting with the explicit `{1,2,3}` test case above;
2. **after the bounded proof is stable:** choose `K=K(delta)` so the limiting third-moment tail beyond `K` changes `R_*` by only a `delta`-level amount, and derive a source-valid coupling/switching comparison rather than simply deleting the high-degree vertices.

**Outcome:** this identifies a finite-support milestone with a precise scale and a plausible path back to the full finite-third-moment class. The missing comparison after truncation is explicit rather than hidden.

---

# 6. Exactly one Section-I recovery choice

I choose **PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM**.

More precisely, the next HARD7-04 recovery iteration should port the Erdős--Rényi tree-component census / second-moment mechanism to the bounded-degree subcritical configuration model, with the `{1,2,3}` law above as the first exact target. It should derive, rather than assume, the configuration-model tree-count coefficient formula and determine whether its first and second moments recover the Cramér exponent `epsilon_n^2/(2R_*)` uniformly over the one-scale band `I_n(delta)`.

The next run should **try to refute this port first**. A valid refutation would be a bounded-degree degree sequence satisfying the same `Q_n,R_n` asymptotics for which the tree-count saddle point has a different leading exponent or the normalized second moment necessarily blows up. If no such obstruction appears, the run should attempt the bounded-degree lower theorem before any return to the full high-degree source class.

This is the only Section-I recovery action chosen in this report. I do not simultaneously switch target, reduce to a finite computer search, or claim the special case proved.

# 7. Metric/status accounting

Frozen metric:

`lim Delta_dual,n: 0 -> 0` — **NO MOVEMENT**.

Section-I state:

- this report is **STUCK1** for `VDH-8.3-DUALITY`;
- one recovery choice has been made: port the ER tree-census lower-bound technique;
- the source remains **OPEN** and the track remains **PARTIAL**;
- no closure, audit request, paper package, shared-ledger edit, email, Drive write, or scheduler mutation is made.

If the recovery eventually fails and the metric/obligation again satisfies the owner's stagnation criterion, the next Section-I episode will be STUCK2. This report does not pre-commit its recovery action.

## ledger_delta

```yaml
track: HARD7-04
target: VDH-8.3-DUALITY
owner: HARD7-04
source_status: OPEN
research_status: PARTIAL
section_I: STUCK1
metric:
  name: Delta_dual_n = abs((1-nu_dual_n)/epsilon_n - 1)
  before_this_run: asymptotic_limit_0
  after_this_run: asymptotic_limit_0
  movement: NO_MOVEMENT
methods:
  - B18
  - B22
  - B30
new_claims: none
blocking_statement: matching_lower_bound_for_postgiant_largest_component
simplest_unproved_track_case: bounded_degree_123_aperiodic_limit
recovery_choice: port_ER_tree_component_census_and_second_moment
next_target_scale: t_about_(1-delta)*2Rstar*epsilon^-2*log(n*epsilon^3)
next_first_action: counterexample_search_against_bounded_degree_tree_count_port
runtime:
  requested_model: GPT-6
  requested_reasoning: maximum
  actual_model: GPT-5.6 Sol
  actual_reasoning: UNVERIFIED
  model_selector_exposed: false
  reasoning_selector_exposed: false
```
