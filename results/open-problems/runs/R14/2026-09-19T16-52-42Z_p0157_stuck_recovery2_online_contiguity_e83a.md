Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on P0157: `Q_m -> 0` before and after. STUCK-RECOVERY-2/2, THINKING-ONLY; methods actually used: #6 DEFORM TO A POINT YOU CAN SOLVE, #15 BREAK THE SYMMETRY ON PURPOSE, #29 ADD THE POINTS AT INFINITY.**

# R14 HARD OUTSIDE — P0157 STUCK-RECOVERY-2/2: online component coupling and defect-compensator route

Run date: 2026-09-19 UTC. Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN / STUCK-RECOVERY-2 OF AT MOST 2 / THINKING-ONLY.** This execution intentionally introduces **no new theorem claim, no finite certificate, and no checker-only artifact**. Its purpose is the second and final Section-I recovery on R14's current P0157 route after the one-root theorem left the frozen metric unchanged.

The stale scheduler title still names the negative-margin spherical perceptron. That target and the later H0008 target were already terminally handed off. The current canonical claim `operations/claims/P0157.md` records **Owner: R14**, **HARD OUTSIDE**, and the frozen quantity

\[
Q_n:=\frac{\operatorname{Var}(T_n)}{(d_{\max}/\delta_n)^2}
=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

On the inherited degree-`{1,3,m^2}` stress family,

\[
Q_m=m^{-1}+O(m^{-2})\to0.
\]

That value remains unchanged here.

## 1. Continuity, ownership, source, and current literature

Before doing new thinking I recovered/read the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the current canonical `operations/claims/P0157.md`, the latest R14 report `runs/R14/2026-09-19T15-50-28Z_p0157_single_root_poissonization_stuck2_trigger_4e91.md`, the preceding R14 stuck recovery and P0157 staircase/matched-tail/dyadic reports, the inherited HARD7-04 P0157 chain, the current intake alias `P0157|3|two competing scales, barely subcritical CM`, and the latest neighboring R17/R19/R20 activity/ownership evidence. No competing P0157 owner, release, posting exclusion, or source closure surfaced.

I reopened the controlling primary source itself: Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, printed p. 245. The page still says that the finite-third-moment subcritical configuration model contains an “interesting open problem,” contrasts the strictly subcritical high-degree scale with the Erdős--Rényi barely-subcritical scale, and says this suggests a phase transition within the subcritical regime. Thus P0157 remains source-open in the exact bounded screen used by this track.

Fresh bounded literature recheck dated 2026-09-19:

- Hatami--Molloy, *The scaling window for a random graph with a given degree sequence* (RSA 2012 / arXiv:0907.4211), establishes the scaling window under its degree-sequence conditions and gives a coarse barely-subcritical largest-component bound outside it.
- Coulson--Perarnau, *Largest component of subcritical random graphs with given degree sequence* (EJP 28 (2023), arXiv:2111.11780), gives stronger configuration-model upper bounds, asymptotically tight for certain degree sequences, and explicitly describes its result as improving Hatami--Molloy rather than as the complete finite-third-moment crossover in the source.
- Olvera-Cravioto, *Strong couplings for static locally tree-like random graphs* (JAP 59 (2022), arXiv:2102.10673), couples configuration-model explorations to marked Galton--Watson local limits at **fixed breadth-first depth**. It does not supply the growing-component marked-tail coupling needed here.
- A bounded search for a 2026 source-matching closure did not find one. This is negative search evidence only, not a worldwide novelty certificate.

## 2. Frozen metric: no movement

The measurable quantity remains

\[
Q_m\to0\quad\longrightarrow\quad Q_m\to0.
\]

No movement. The route diagnosis below is not substituted for movement in `Q_n`.

---

# Section-I stuck report

## (a) Exact statement that blocks

The preceding proof-capable run established an actual-configuration-model **single-root** marked-hit vector approximation. For one deterministic marked root `i`, with

\[
\mu_{ih}=\frac{d_i d_h}{\ell\delta_H},
\]

the clean first-hit vector is close in total variation to independent Poisson coordinates under explicit one-root conditions.

What is still absent is not another one-row estimate. The source route needs a component-level comparison that is consistent across all rows revealed inside **one growing marked component**. A useful target formulation is:

\[
\boxed{
\begin{gathered}
\text{construct an online coupling or mutual-contiguity comparison between}\
\text{the marked configuration-model component exploration and a rank-one}\
\text{marked exploration, stopped at }\tau\le b_n,\qquad b_n=o(\ell\delta_H),
\end{gathered}}
\tag{B1}
\]

followed by a selection-safe bulk-mass map

\[
\boxed{
|C|=(1+o_{\mathbb P}(1))\frac1{\delta_n}
\sum_{i\in C\cap H}d_i
}
\tag{B2}
\]

on the components that can actually compete for the maximum.

`(B1)` is deliberately weaker than global total variation for the entire induced high-degree graph. It asks only for the law of one sequentially exposed marked component, on the exploration budget relevant to an extreme component. Neither `(B1)` nor `(B2)` is claimed here.

### The new diagnosis inside the blocker: the birthday barrier is probably self-inflicted

The one-root proof declared the coupling failed at the first repeated bulk label or finite-population mismatch. For `R` pairings this naturally produced terms of order

\[
R^2/\ell.
\]

That is excellent for a fixed root, but it asks for `R=o(\sqrt\ell)` if used naively at component scale. The full problem does **not** require the actual exploration to be collision-free. A large component may contain many ordinary collision opportunities while its **drift and marked-hit compensators** remain close to the undepleted process.

The scale suggested by the queue is instead

\[
\boxed{R=o(\ell\delta_H).}
\tag{B3}
\]

Why this scale appears: after `t` pairings, the residual half-edge population has changed by a relative amount of order `t/\ell`; the baseline negative drift is order `\delta_H`. Over a budget `b`, a cumulative first-order depletion/collision correction has the schematic size `b^2/\ell`, while the deterministic subcritical drift has size `\delta_H b`. Their ratio is

\[
\frac{b^2/\ell}{\delta_H b}=\frac{b}{\ell\delta_H}.
\]

Thus the route should not kill the comparison at the first collision; it should show that the **aggregate defect** is negligible relative to subcritical drift when `(B3)` holds. This is a route calculation, not a proved theorem.

There is a strong feasibility reason to pursue exactly this window. Under the bounded-third-moment form used throughout R14's P0157 artifacts,

\[
\sum_v d_v^3=O(n),\qquad \ell=\Theta(n),\qquad n\delta_n^3\to\infty,
\]

we have the immediate scale checks

\[
d_{\max}=O(n^{1/3}),
\]

and therefore for the two source candidate scales

\[
H_n=\frac{d_{\max}}{\delta_n},
\qquad
E_n=\delta_n^{-2}\log(n\delta_n^3),
\]

one formally obtains

\[
\frac{H_n}{n\delta_n}
=O\!\left(\frac1{(n^{1/3}\delta_n)^2}\right)\to0,
\qquad
\frac{E_n}{n\delta_n}
=\frac{\log(n\delta_n^3)}{n\delta_n^3}\to0.
\tag{B4}
\]

I record `(B4)` only as a sanity check that the proposed budget is compatible with the source's two advertised scales, not as a new result. Under the additional assumptions of Hatami--Molloy's coarse barely-subcritical bound,

\[
L_1=O\!\left(\sqrt{n/\delta_n}\right),
\]

the same compatibility reads

\[
\frac{L_1}{n\delta_n}=O\!\left((n\delta_n^3)^{-1/2}\right)\to0.
\]

The exact hypothesis match for importing that bound must be checked in the proof-capable follow-up; it is not silently assumed here.

## (b) Routes tried and the precise reason each failed

### 1. The frozen branching scalar `Q_n`

It measures self-averaging of one ideal high-degree-root branching forest. The stress family and later growing staircase show that `Q_n -> 0` can coexist with substantial or diverging multi-hub coalescence. Therefore it cannot be the state variable for the full crossover.

### 2. Fixed-root finite-population LLN and compensated queue

These routes control the mass attached to a **preselected** high-degree root and were strong enough to prove the inherited stress-family constants. They do not control the largest component after graph-wide selection among many roots.

### 3. Pairwise marked-hub kernel

The bulk calculation gives the correct pair scale

\[
\kappa_{ij}\approx \frac{d_i d_j}{\ell\delta_H}.
\]

A pair kernel is only a marginal. Shared bulk paths and finite-pairing depletion prevent one from declaring all induced tail edges independent.

### 4. Exact finite skeleton counting

It closes small explicit cores and supported the three-hub/four-hub stress analysis. It explodes combinatorially for a growing tail and therefore cannot itself be the general crossover theorem.

### 5. Stress families, growing staircase, and scalar-matched pair

These are highly informative obstructions: scalar-only characterizations fail, even when `H/E`, `Q_n`, and low moments are matched. They diagnose what the theorem must remember, but do not provide a positive general characterization.

### 6. Dyadic Steiner penalty

This suppresses genuine bulk branch points and identifies the rank-one weighted Cayley tree contribution as the leading **one-sided** object on one high-degree band. It does not manufacture the lower-law / approximate independence needed to construct the induced tail component process.

### 7. Raw tree-sum lower target

The first stuck recovery corrected this route. Once the comparison graph itself can have multiple tree witnesses or cycles, the raw sum over spanning trees is not a probability and can exceed one. The process, not a single first-moment tree expansion, must be approximated.

### 8. Single-root Poissonization

This is the strongest completed restricted theorem: it upgrades the rank-one marginal from an ideal branching surrogate to the **actual pairing model** for one root, with explicit total-variation error.

Its failure to globalize is now understood more precisely. The proof demands pathwise agreement with an iid with-replacement process until extinction. Repeating it root-by-root both double-counts the same undirected connections and incurs a birthday-type `R^2/\ell` error. That is too stringent for a growing component. The missing idea is not “get a sharper union bound”; it is **stop asking for collision-free pathwise equality**.

## (c) What a proof would have to contain that no route so far contains

A viable proof of `(B1)` needs all of the following in one argument.

### C1. Conditional residual uniformity rather than independent rows

Explore only one marked component. Conditional on the revealed pairings, the unrevealed half-edges are still uniformly paired. The comparison must be updated from the **residual** degree/half-edge measure after each step rather than restarting a fresh row law.

### C2. A time-inhomogeneous subcritical queue

Instead of the fixed with-replacement branching process from the one-root proof, introduce a process whose offspring/mark law uses the current residual half-edge empirical measure. The baseline drift is `-delta_H`; depletion perturbs it by order `t/ell`. The target estimate is a stability statement over `t<=b_n`, not exact equality of sample paths.

A schematic decomposition to aim for is

\[
A_t
=A_0+M_t-\delta_H t-\mathfrak D_t+\mathfrak r_t,
\tag{C1}
\]

where `A_t` is the active-half-edge queue, `M_t` is a martingale term, `\mathfrak D_t` records real finite-population/collision loss, and `\mathfrak r_t` is the deterministic/residual-measure correction. What is needed is an estimate of the form

\[
\sup_{t\le b_n}|\mathfrak r_t|+\mathfrak D_{b_n}
=o_{\mathbb P}(\delta_H b_n)
\tag{C2}
\]

for the relevant stopped exploration. `(C1)`--`(C2)` are a desired proof architecture, not claims established here.

### C3. Online marked-edge compensators

When the exploration first reaches a new high-degree vertex `h`, that event should be charged once to the currently active marked component. Its conditional intensity must remain asymptotic to the rank-one intensity based on the residual tail degrees. This avoids the inconsistency of generating independent rows and then trying to identify `i-j` with `j-i` afterward.

### C4. Defects must be charged, not forbidden

Repeated bulk vertices, short cycles, root self-contact, and path intersections should contribute to a cumulative defect process. Only a **macroscopic** defect should send the comparison to a cemetery state. The one-root proof's “first defect kills the coupling” is the wrong global invariant.

### C5. An a priori exploration budget

A process comparison is useful only if the component closes before `b_n` with high probability. This is where the existing configuration-model literature is more valuable than another local weak-limit theorem. Hatami--Molloy and Coulson--Perarnau already control barely-subcritical component sizes using adaptive exploration/stochastic domination. The route is to port that **budget control** while retaining R14's marked identities.

### C6. The mass map after the marked process is controlled

Even `(B1)` is not source closure. The marked component gives the set of high-degree seeds. One then needs a uniform compensated-queue statement proving `(B2)` for a component selected by the marked graph. The stress-family queue argument is the local prototype, but selection-safe uniformity is still absent.

## (d) Simplest special case still unproved

The next proof target should be smaller than global tail-graph total variation but strictly stronger than the completed one-row theorem.

Fix **one dyadic marked band**

\[
D(a)=\{v:a\le d_v<2a\}
\]

inside the absorbing tail `H(a)={v:d_v\ge a}`. Start from one specified mark `i in D(a)` and expose **its entire marked component sequentially**, always pairing from the current active component and revealing a newly hit mark only once. Stop at

\[
\tau_b:=\min\{\text{component closes},\ b_n\text{ pairings}\},
\qquad
b_n=o(\ell\delta_a).
\]

The simplest unproved statement worth attacking is:

> on tree-shaped marked-component histories up to `tau_b`, compare the actual configuration-model history to the corresponding online rank-one marked branching/exploration law with probability ratio `1+o(1)` (or at least mutual contiguity), uniformly over the histories needed to determine the largest marked component in the sparse one-band regime.

This is deliberately not a comparison of every marked pair in the graph and not a global total-variation statement. It permits ordinary bulk repeats provided their aggregate defect remains negligible. Proving it would still be **PARTIAL**, not closure of P0157.

## (e) Nearest solved problem and what its proof has that P0157 lacks

There are now three complementary nearest solved mechanisms, and this recovery changes which one should be ported.

### Hatami--Molloy / Coulson--Perarnau: useful for the budget

Their configuration-model arguments work with the actual finite-population exploration and control large component sizes in the barely-subcritical regime. Coulson--Perarnau explicitly improve the earlier Hatami--Molloy upper bound. What these proofs have that the one-root R14 coupling lacks is **adaptive queue control without requiring collision-free agreement with an iid branching process**.

What they do not retain is the marked upper-tail identity needed to manufacture the rank-one high-degree component process.

### Olvera-Cravioto: useful for local coupling language

The strong-coupling theorem covers the configuration model and rank-one graphs, but the coupling is at fixed breadth-first depth. R14 needs a growing stopped exploration whose size is itself random and may be much larger than any fixed depth neighborhood.

### Independent-edge rank-one / Norros--Reittu comparison: useful for the target law

In the rank-one model, the approximate Poisson edge structure is present by construction. That is the law R14 wants to recover after bulk compression. It supplies the destination, not the finite-pairing stability theorem.

**Chosen Section-I action:** **PORT THE TECHNIQUE FROM (e).** Specifically, port the adaptive barely-subcritical queue/depletion control of Hatami--Molloy / Coulson--Perarnau into R14's marked absorbing exploration, and use it to replace the one-root proof's `R^2/ell` collision-free coupling by a budgeted defect-compensator comparison on `b_n=o(ell delta_a)`.

This is the single chosen action for this recovery. I am not simultaneously claiming a counterexample, finite computation, or target switch.

---

# Outcomes of the three required new methods

## #6 DEFORM TO A POINT YOU CAN SOLVE — outcome: the deformation variable should be exposure fraction, not an artificial model mixture

The solved point is the with-replacement marked branching process used in the one-root theorem. The natural path back to the exact pairing model is to let the empirical half-edge law evolve with exposure time `t/ell`. At `t=0` the rank-one/branching description is exact at first order; at time `t` its drift and marked-hit rates have a correction controlled by the residual population.

This identifies the quantity to differentiate/control:

\[
\text{finite-population correction}/\text{subcritical drift}
\asymp \frac{t/\ell}{\delta_H}.
\]

Thus the deformation remains perturbative up to `t=o(ell delta_H)`, a parametrically larger window than the `o(sqrt ell)` collision-free window when `delta_H sqrt(ell)` is large. The required proof is a stability/likelihood or compensator estimate, not a zero-collision event.

## #15 BREAK THE SYMMETRY ON PURPOSE — outcome: expose one component in a directed temporal order

Do **not** generate all root rows symmetrically. Pick the next active marked vertex according to the actual queue (or a deterministic rule such as first discovery / size-biased active-half-edge order), and reveal connections only from that mark to still-unseen marks. Once `h` is discovered from `i`, the undirected relation is fixed; there is no future independent `h->i` row to reconcile.

This broken-symmetry exploration matches the deferred-decision property of the pairing model. It turns the simultaneous-coupling problem into a sequential conditional-law problem. The cost is that the comparison process becomes time-inhomogeneous, which is exactly what #6 already requires.

## #29 ADD THE POINTS AT INFINITY — outcome: a cemetery/defect coordinate should accumulate error rather than trigger at the first collision

Enlarge the comparison state by a defect coordinate `dagger` carrying mass from repeated bulk labels, cycle closures, self-contacts, and other overlap events. The process is sent to the true cemetery state only when accumulated defect exceeds a tolerance comparable with the subcritical drift budget.

This changes the desired conclusion from impossible global pathwise equality to **contiguity/stability of component observables before macroscopic defect**. The first-collision probability may be large; the only relevant question is whether the accumulated defect is `o_P(delta_H b_n)`.

The three methods therefore converge on one route rather than three cosmetic variants:

\[
\boxed{
\text{exact pairing}
\to
\text{residual-measure online queue}
\to
\text{marked rank-one component law}
\to
\text{bulk-mass transfer}.
}
\]

## 3. What changed in our understanding, without changing the metric

The blocker is **narrower and different** from the one stated after the preceding theorem.

Before this recovery, the natural wording was “prove simultaneous multi-root Poissonization.” That formulation still suggests coupling every marked row and therefore inherits the birthday barrier.

After this recovery, the route to test is instead:

> prove an online, one-component, budgeted contiguity or likelihood-ratio theorem in which finite-population collisions enter as a small cumulative drift/compensator defect, not as coupling failure.

This is a real route change but **not** metric movement and not a theorem claim.

## 4. Mandatory next state

This consumes **STUCK-RECOVERY-2/2** for R14 on P0157.

A next proof-capable run, if the target has not reached a new stuck episode, should attempt exactly the one-band **budgeted sequential component comparison** above. It should not return to independent all-row Poissonization, another stress family, or another checker for `Q_m`.

The next fresh Section-B triple recorded for that proof attempt is:

- **#1 CHANGE THE CATEGORY** — rewrite the comparison as a semimartingale/compensator or likelihood-ratio stability problem rather than a graph-edge independence problem;
- **#19 MAKE IT AN ALGORITHM** — write the coupled deferred-decision exploration explicitly, with residual half-edge state and a defect account;
- **#27 SWAP THE QUANTIFIERS** — control the law of one entire selected marked-component exploration instead of all marked rows simultaneously.

If that proof attempt leaves the same blocker and the target enters the stuck condition again, there is **no third P0157 recovery available to R14**. The next stuck episode must terminally hand P0157 off and rotate to an ownership-clear HARD OUTSIDE successor under the current queue/admission rules.

## 5. Model / scheduler-control status

The exposed scheduler control surface still provides prompt/title, timing/schedule, enabled state and related run controls, but **no binding model-family selector and no reasoning-effort selector**. GPT-6/maximum therefore remains prompt text only. This run actually identifies itself as **GPT-5.6 Sol / reasoning UNVERIFIED**.

The historical P26 `You cannot modify this task` event is an authorization-context issue, not permission to bypass access controls. The current repository ledger records that P26 was later updated successfully from an authorized context. For any currently protected task, the valid path remains its owning/admin-authorized interface or platform support.

No scheduler state, permission, email, Drive item, public posting, workflow, shared root, peer file, or other track was modified in this run.

```yaml
ledger_delta:
  track: R14
  target: P0157
  category: HARD_OUTSIDE
  status_before: PARTIAL_SOURCE_OPEN_STUCK_RECOVERY_2_DUE
  status_after: PARTIAL_SOURCE_OPEN_STUCK_RECOVERY_2_CONSUMED
  fixed_metric: Q_n = sigma_n^2/(d_max*delta_n)
  value_before: Q_m -> 0 on inherited stress family
  value_after: Q_m -> 0 on inherited stress family
  metric_movement: false
  theorem_claim_this_run: none_thinking_only
  substantive_route_change: replace global simultaneous row coupling by online one-component residual-measure contiguity with cumulative defect control on b_n=o(ell*delta_H)
  chosen_section_I_action: port_technique_from_nearest_solved_problem
  stuck_recoveries_consumed_before: 1
  stuck_recoveries_consumed_after: 2
  next_methods: [1, 19, 27]
  independent_audits: 0
  mandatory_if_next_stuck: terminal_handoff_and_rotate
```
