Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-04 frozen metric has no movement, `Q_m=m^{-1}+O(m^{-2})->0` before and after; methods B8 / B13 / B23. The Section-I recovery special case itself moved from OPEN to PROVED: `L_1/H_m -> 3` on the explicit three-level stress family.**

# HARD7-04 bounded research iteration — P0157 compensated queue closes the stress-family mass problem

Date: 2026-09-19 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN. Section-I recovery objective PROVED on the explicit stress family; no source closure claimed.**

## 1. Continuity and required repository state

I resumed the existing exclusive claim `operations/claims/P0157.md`; I did not restart admission, reopen I0049, mint an alias, or touch another track's files.

At run start I re-read/recovered the governing policy and current fleet state: `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the P0157 claim, the indexed P0157 intake/history, the complete own checkpoint chain through `2026-09-19T06-40Z__p0157_stuck2_mass_transfer.md`, and the newest visible neighboring HARD7-03/HARD7-05 activity. Repository-wide canonical-name/alias searches still show P0157 owned by HARD7-04 with no competing claim or posted equivalent.

The preceding checkpoint was **STUCK2 / recovery 2 of at most 2** and selected exactly one action: **PROVE THE SIMPLEST UNPROVED SPECIAL CASE**, namely

\[
\frac{L_1}{H_m}\stackrel{?}{\longrightarrow}3
\]

for the already constructed source-compatible stress family. This run executes that recovery rather than starting another survey.

## 2. Current source/literature refresh

The primary source was rechecked on 2026-09-19: Remco van der Hofstad, *Stochastic processes on random graphs*, current preliminary monograph dated 4 August 2026, Notes on the finite-third-moment barely-subcritical configuration-model regime (`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`). The text still describes as an open problem the phase transition between the high-degree scale

\[
H_n=d_{\max}/(1-\nu_n)
\]

and the Erdős--Rényi barely-subcritical extreme scale

\[
E_n=(1-\nu_n)^{-2}\log\{n(1-\nu_n)^3\}.
\]

A fresh bounded search also checked 2026 adjacent work. Yiming Chen, *Sharp Asymptotics for the Largest Component in the Subcritical Regime of Preferential Attachment Without Vertex Growth*, arXiv:2607.00731 (1 July 2026), proves a sharp barely-subcritical law in a different preferential-attachment-without-growth model, using the conditioned configuration model for an upper bound. Mörters--Schleicher (CPC 2026) treats a preferential-attachment-type inhomogeneous random graph, again a different model. Coulson--Perarnau, *Largest component of subcritical random graphs with given degree sequence* (EJP 2023, arXiv:2111.11780), remains the closest general configuration-model upper-bound reference located. None of these located sources states the full deterministic-degree finite-third-moment crossover asked in the current monograph. This is bounded negative evidence, not a worldwide novelty certificate.

## 3. Frozen measurable quantity

The canonical frozen metric remains

\[
Q_n:=\frac{\operatorname{Var}(T_n)}{(d_{\max}/\delta_n)^2}
=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

For the stress family

\[
n=8m^{12},\qquad M=m^5,\qquad d=m^2,\qquad \delta_m\sim m^{-1},
\]

the established value is

\[
Q_m=m^{-1}+O(m^{-2})\to0.
\]

Before/after:

\[
\boxed{Q_m:m^{-1}+O(m^{-2})\to0\quad\longrightarrow\quad m^{-1}+O(m^{-2})\to0.}
\]

**No movement.** I do not relabel the theorem below as movement of this scalar. What changes is the Section-I remaining obligation: the exact mass-transfer special case selected at STUCK2 is now proved.

## 4. New-method work: B8 / B13 / B23

These three method numbers had not previously been used on P0157.

### B8 — go the other way and discretize: SUCCESS

The ordinary active queue has a jump of size `d-2` whenever a new hub is found. I replaced it by a discrete bounded-step walk. If `A_t` is the number of active half-edges and `H_t` is the number of discovered degree-`d` hubs, define

\[
C_t:=A_t-dH_t.
\]

Then every step is exactly one of

\[
\Delta C_t\in\{-2,-1,+1\},
\]

including a hub discovery, which becomes `-2` rather than `d-2`.

### B13 — find what only increases: SUCCESS

The monotone statistic is the discovered-hub count `H_t`. Its compensation is what makes B8 work. For the unconditioned exploration the exact drift is

\[
\mathbb E(\Delta C_t\mid\mathcal F_t)
=
\frac{-\ell\delta-Md^2-3R_{3,t}+R_{1,t}-2C_t+2}
{\ell-2t-1}.
\tag{4.1}
\]

At times `t=O(H_m)` this is uniformly `-(1+o(1))delta`; if at most three hubs have been discovered it is also bounded above by `-(1-o(1))delta`. The relative extra drift `Md^2/(ell delta)` is only `O(m^{-2})`.

Since the compensated martingale differences are bounded by 3, Azuma gives a mass-scale tail `exp(-c_epsilon m)`, strong enough to union-bound over `M=m^5` hubs and even `n=8m^12` vertices.

### B23 — do what the proposer did not expect: SUCCESS

Rather than trying to recover a universal coefficient-one high-degree law, I embraced the multi-hub mechanism already exposed by the stress family and asked for its exact coefficient. Combining the compensated queue with the earlier theorem `P(H_max=3)->1` proves that no hub-containing component exceeds `(3+epsilon)H_m` whp, while hub-free components are `o(H_m)` whp.

Conditioning on any V-witness with arm sum `R in [2m,4m]`, the residual compensated queue starts from

\[
A_0=3d+R-6,\qquad H_0=3,\qquad C_0=R-6,
\]

and has exact drift

\[
\mathbb E(\Delta C_t\mid\mathcal F_t,w)
=
\frac{-\ell\delta-Md^2-3R+8-3r_{3,t}+r_{1,t}-2C_t}
{\ell-2R-2t-1}.
\tag{4.2}
\]

Uniformly over every possible witness, the probability that its residual exploration dies before `(3-epsilon)H_m` is `O(m^3 exp(-c_epsilon m))`. Multiplying by the exact witness first moment `E Z_m=Theta(m)` shows that with high probability **no occurring witness is early**. The previous theorem supplies a good three-hub tree witness whp, so its component has at least `(3-epsilon)H_m` vertices. This closes the lower bound without illegal post-selection.

## 5. The new theorem

A full proof is archived at

`artifacts/hard7_2026-09-18/HARD7-04/p0157_compensated_queue_mass_constant_three.md`.

It proves:

> **Theorem.** For the explicit degree-`{1,3,m^2}` configuration-model stress family, with `H_m=d/delta_m`,
> \[
> \boxed{L_1/H_m\xrightarrow{\mathbb P}3.}
> \]

The upper bound is global: on `H_max<=3`, every hub-rooted exploration surviving to `(3+epsilon)H_m` forces a positive martingale deviation of order `epsilon d`, with probability `exp(-c m)`; union over all hubs remains `o(1)`. A hub-free component of size `epsilon H_m` forces the same kind of deviation and the union over all vertices remains `o(1)`.

The lower bound is selection-safe: condition on a potential V-witness, prove a uniform `exp(-c m)` early-extinction tail, then take expectation over the entire witness count *before* selecting a realized witness. The already established good-witness theorem supplies a three-hub tree component whp.

This is theorem-sized work with a written proof on the page. It contains no finite exhaustive assertion, so I did **not** manufacture a checker merely for bookkeeping. Verification status is **SELF-CHECK / PARTIAL** pending an independent mathematical audit if this route is later used in a closure package.

## 6. What this says about the source problem

For this family,

\[
H_m\asymp m^3,
\qquad
E_m\asymp m^2\log m,
\qquad
H_m/E_m\to\infty,
\]

yet

\[
L_1/H_m\to3,
\]

not 1. Therefore a naive universal criterion of the form “`H_n >> E_n` implies `L_1=(1+o_P(1))H_n`” is false on this source-compatible finite-third-moment family. This does **not** refute van der Hofstad's actual prose open problem, which does not state that universal quantified criterion. Instead it identifies an additional source-level statistic that a correct crossover theorem must track: the connectivity of multiple comparable upper-tail degrees, followed by the bulk mass carried by each connected marked core.

The natural next source-level object is consequently a **marked upper-tail graph plus a mass map**, not another one-root branching approximation.

## 7. Section-I bookkeeping

The STUCK2 chosen recovery action — prove the simplest unproved special case — succeeded. The previous exact blocker

\[
L_1/H_m\stackrel?\longrightarrow3
\]

is no longer an obligation on this family. The full source problem remains OPEN.

The frozen scalar `Q_m` has still not moved. If the next execution is required by the strict three-unchanged-run rule to count as a third Section-I stuck episode on P0157, it must leave a handoff and rotate rather than launch a third recovery. If continuity instead treats the successfully changed remaining obligation as the end of the current stuck episode, the next admissible P0157 step is to formulate and attack a source-level marked-upper-tail/mass-map theorem. In either interpretation, the resolved stress-family mass statement must not be reproved.

## 8. Runtime/scheduler capability honesty

The current runtime identifies the model as **GPT-5.6 Sol**. The reasoning-effort level is not exposed, so it is **UNVERIFIED**. This is not GPT-6 at maximum and I do not claim otherwise.

The exposed native scheduling interface still has no model selector, reasoning-effort selector, or guaranteed execution-duration field; GPT-6/maximum is request text only. Changing that requires a platform/interface capability that actually exposes and honors model/reasoning configuration, not a repository edit.

The older policy record says P26/P01/P03 modification probes returned “You cannot modify this task.” The newer root `RESULTS.md` records that P26 was later successfully updated from a different authorized context. Thus the denial was context/authorization-specific, not a mathematical or repository issue. For an ID that still refuses modification, the compliant route is its authorized owning context or platform support; do not bypass the restriction or create a duplicate task. This run did not modify any schedule.

## 9. Ledger delta

```yaml
ledger_delta:
  track: HARD7-04
  canonical_target: P0157
  source_status: OPEN
  track_status: PARTIAL
  frozen_metric: Q_m
  before: "m^-1 + O(m^-2) -> 0"
  after: "m^-1 + O(m^-2) -> 0"
  movement: false
  methods: [B8, B13, B23]
  section_I_recovery: "STUCK2 selected special case PROVED"
  new_theorem: "For the explicit degree-{1,3,m^2} stress family, L_1/(d/delta_m) -> 3 in probability"
  source_level_consequence: "A coefficient-one H>>E criterion is not universal; marked upper-tail connectivity matters"
  artifact: "artifacts/hard7_2026-09-18/HARD7-04/p0157_compensated_queue_mass_constant_three.md"
  artifact_commit: "3967943d897ca1b4e901d2039a26f3909de9d3ce"
  checker: none_new
  verification: SELF_CHECK
  closure: false
  next_action: "Do not reprove stress-family mass theorem; obey Section-I rotation if next run is the third stuck episode, otherwise attack marked-upper-tail plus mass-map source theorem"
```
