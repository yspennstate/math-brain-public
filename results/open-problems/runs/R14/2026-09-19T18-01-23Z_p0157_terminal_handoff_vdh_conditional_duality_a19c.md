Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on P0157: `Q_m -> 0` before and after; TERMINAL HANDOFF executed after both allowed stuck recoveries were consumed. Methods actually used on the proof-capable P0157 step: #1 CHANGE THE CATEGORY, #19 MAKE IT AN ALGORITHM, #27 SWAP THE QUANTIFIERS.**

# R14 HARD OUTSIDE — P0157 terminal handoff, then VDH-8.3-DUALITY reassignment and fixed-set conditional-duality reduction

Run date: 2026-09-19 UTC. Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status at end of run:

- **P0157:** SOURCE OPEN / PARTIAL / **RELEASED BY R14 AFTER SECTION-I EXHAUSTION**;
- **VDH-8.3-DUALITY:** SOURCE OPEN / PARTIAL / **EXCLUSIVELY REASSIGNED TO R14**;
- no closure, refutation, posting, audit, scheduler, email, Drive, workflow or permission claim.

The scheduler title still names the negative-margin spherical perceptron, but that target was terminally handed off earlier, as was H0008. Repository continuity, the latest owner directive and canonical ownership state therefore controlled this invocation rather than the stale title.

## 1. Required continuity/source reads

Before research I recovered/read:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/claims/P0157.md` and the latest R14 P0157 report `runs/R14/2026-09-19T16-52-42Z_p0157_stuck_recovery2_online_contiguity_e83a.md`;
- the previous R14 one-root Poissonization artifact and the staircase/matched-tail/dyadic chain;
- the released HARD OUTSIDE claim `operations/claims/VDH-8.3-DUALITY.md` and the newest HARD7-04 VDH report `runs/hard7_2026-09-18/HARD7-04/2026-09-19T1530Z__vdh_quantitative_histogram_duality.md`;
- current neighboring ownership/release reports recovered through repository search;
- intake/queue evidence relevant to successor admission.

`QUEUE.md` still says its listed candidates are not automatically dispatchable and newly certified READY entries are zero. I therefore did not promote a PENDING row. The successor below was instead already a canonical **explicitly released HARD OUTSIDE** claim.

The posting register excludes the owner's already written/posted work and does not list either P0157 or VDH-8.3-DUALITY as a closed source-equivalent result.

## 2. Current primary-source / literature screen

### P0157

The controlling source remains Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, where the finite-third-moment barely-subcritical configuration-model discussion contrasts the high-degree and Erdős--Rényi scales and says this suggests a phase transition within the subcritical regime.

The nearest checked results remain Coulson--Perarnau (EJP 2023), which gives strong subcritical configuration-model upper bounds, Hatami--Molloy on the scaling window, and Olvera-Cravioto on fixed-depth strong couplings. A bounded 2026-09-19 search found no theorem closing the exact source crossover residual. This is negative search evidence only, not a worldwide novelty certificate.

### VDH-8.3-DUALITY

The same **4 August 2026** monograph, printed p. 245 / PDF p. 255, explicitly asks in the barely-supercritical finite-third-moment configuration-model discussion:

> “Does the discrete duality principle still hold?”

The 2019 van der Hofstad--Janson--Luczak paper *Component structure of the configuration model: Barely supercritical case* proves precise giant-component asymptotics and related critical results but does not state the requested sharp second-largest-component/discrete-duality theorem. Fixed-supercritical configuration-model duality and independent-edge inhomogeneous-graph duality are prior art in different regimes/models. A fresh bounded 2026-09-19 search found no later source-matching closure. Again, this is bounded negative evidence, not a novelty certificate.

---

# Part I. P0157 proof-capable follow-up and mandatory terminal handoff

## 3. Frozen metric

The P0157 fixed quantity remained

\[
Q_n:=\frac{\sigma_n^2}{d_{\max}\delta_n},
\]

with supported stress-family baseline

\[
Q_m=m^{-1}+O(m^{-2})\to0.
\]

This run did not change it:

\[
\boxed{Q_m\to0\quad\longrightarrow\quad Q_m\to0.}
\]

Thus the first line correctly says **NO FIXED-METRIC MOVEMENT**.

Both allowed P0157 stuck recoveries had already been consumed. The preceding recovery authorized one proof-capable attempt using fresh methods #1, #19 and #27, with the explicit warning that if the blocker remained then P0157 had reached terminal-handoff territory. I carried out that attempt below, then released the target rather than attempting a third recovery.

## 4. #1 CHANGE THE CATEGORY — from collision-free iid coupling to predictable characteristics

The prior one-root theorem coupled the actual configuration-model exploration to an iid with-replacement branching process until the first finite-population mismatch/repeated bulk label. At `R` pairings this naturally paid a birthday error `R^2/ell`, which artificially forced `R=o(sqrt ell)`.

The new route stops treating collisions as coupling failures. Work directly in the actual adaptive pairing process and track the residual unseen-vertex measure.

Fix a deterministic marked set `H`, bulk `B`, and

\[
\delta_H=1-\frac1\ell\sum_{v\in B}d_v(d_v-1)>0.
\]

Let `V_t` be the bulk vertices first discovered by time `t`,

\[
D_t:=\sum_{v\in V_t}d_v(d_v-1),
\]

and let `Y_t` be the number of **new** active half-edges generated by the partner at step `t`. Then, for every adapted rule for choosing the next active half-edge,

\[
\boxed{
\mathbb E[Y_t\mid\mathcal F_t]
=\frac{\ell(1-\delta_H)-D_t}{\ell-2t-1}.
}
\tag{4.1}
\]

This is exact. Repeated bulk labels, cycles and already exposed vertices simply contribute zero new offspring and are absorbed into the residual state; no “first defect kills the coupling” rule is needed.

Under

\[
\sum_vd_v^3\le Cn,\qquad \ell\ge cn,
\]

the same actual pairing calculation gives, for `b<=ell/4`,

\[
\boxed{\mathbb E D_b\le2(C/c)b.}
\tag{4.2}
\]

Consequently, whenever

\[
b=o(\ell\delta_H),
\]

one has

\[
\boxed{
\sup_{t\le b\wedge\tau}
\frac{|\mathbb E[Y_t\mid\mathcal F_t]-(1-\delta_H)|}{\delta_H}
\xrightarrow{\mathbb P}0.
}
\tag{4.3}
\]

This proves that the residual process keeps essentially the same negative drift on a window parametrically larger than the old `o(sqrt ell)` pathwise-coupling window.

The complete proof is in

`artifacts/R14/p0157_online_drift_budget_and_mark_hazard.md`

creation commit

`196c95171187e0d16339abbb007aac1dbca3865c`.

## 5. #19 MAKE IT AN ALGORITHM — an actual-CM component budget

Let `A_t` be the active-half-edge queue, start with `a_0` active half-edges, and let `tau` be the extinction time. Because `D_t>=0`, the exact drift identity yields a conservative bound

\[
\mathbb E[Y_t\mid\mathcal F_t]\le1-\delta_H/2
\]

through every deterministic budget satisfying

\[
2b+1\le\ell\delta_H/4.
\]

Since always

\[
A_{t+1}-A_t\le-1+Y_t,
\]

the stopped queue gives

\[
\boxed{
\mathbb E[\tau\wedge b]\le\frac{2a_0}{\delta_H},
\qquad
\mathbb P(\tau>b)\le\frac{2a_0}{\delta_H b}.
}
\tag{5.1}
\]

Thus if

\[
a_0=o(\ell\delta_H^2),
\]
there exists a deterministic window

\[
\frac{a_0}{\delta_H}=o(b),
\qquad b=o(\ell\delta_H),
\]
inside which the actual component exploration closes with probability tending to one.

Under the finite-third-moment source regime, `d_max=O(n^{1/3})`, `ell=Theta(n)`, and `n delta_n^3->infinity`, so a **preselected** maximum-degree-root exploration satisfies `d_max=o(ell delta_n^2)` and hence fits this window. This is not selection-safe for the graph-wide largest component; I retain that qualification explicitly.

## 6. #27 SWAP THE QUANTIFIERS — one realized adaptive component, exact marked labels

Let `U_t` be the marked vertices not yet hit and

\[
S_t=\sum_{h\in U_t}d_h.
\]

At every step of the actual exploration,

\[
\boxed{
\Pr(\text{next partner is in }U_t\mid\mathcal F_t)
=\frac{S_t}{\ell-2t-1},
}
\tag{6.1}
\]

and, conditional on a new marked vertex being hit,

\[
\boxed{
\Pr(\text{new mark}=h\mid\mathcal F_t,\text{ new mark hit})
=\frac{d_h}{S_t}.
}
\tag{6.2}
\]

So the **identity** of the next tail vertex already has the exact degree-size-biased law needed by a rank-one exploration. The remaining problem is not row independence or label choice. It is the random **clock**: how many bulk pairing opportunities are generated between marked discoveries, especially after conditioning on the rare multi-hub coalescences that create an extremal component.

This sharply isolates the remaining P0157 obligation:

> prove, under the selection/rare-event conditioning relevant to the maximum, that the pairing-opportunity clock generated by a discovered marked mass is asymptotic to `mass/delta_H`, uniformly on the relevant skeleton sizes.

If that held, the integrated hazard to a marked vertex `h` would have the desired rank-one scale `W d_h/(ell delta_H)`.

The staircase and scalar-matched-pair obstructions explain why an unconditional preselected-root clock law is not enough.

## 7. P0157 terminal handoff

The proof-capable attempt made genuine structural progress, but it did not move the frozen metric and did not close the source. Both allowed stuck recoveries had already been consumed. Per the hard-task rule, I therefore **did not perform a third recovery**.

I updated the canonical P0157 claim to

- owner: `UNASSIGNED AFTER R14 HANDOFF`;
- status: `SOURCE OPEN / PARTIAL / RELEASED BY R14 AFTER SECTION-I EXHAUSTION`;
- preserved metric: `Q_m=m^{-1}+O(m^{-2})->0`;
- preserved terminal obstruction: the selection-safe clock theorem above.

Release commit:

`32204f4e94b97b877b1df42a757edc6dc7195471`.

A future fresh worker is directed toward Doob-transform/spine/skeleton-first-switching ideas for the conditioned clock rather than the exhausted one-root collision-free coupling route.

---

# Part II. Successor gate and first VDH-8.3-DUALITY attack

## 8. Why this successor was eligible

`QUEUE.md` had no newly certified READY row to take automatically. Repository search did, however, recover the canonical claim

`operations/claims/VDH-8.3-DUALITY.md`

in the exact state

`Owner: UNASSIGNED AFTER HARD7-04 HANDOFF`,

`SOURCE OPEN / PARTIAL / HANDED OFF`,

`HARD OUTSIDE`.

The source and current literature were rechecked before reassignment. No competing owner or posting exclusion was found. I therefore took this already released canonical claim rather than creating an alias.

Reassignment commit:

`d878fb0f04b1b191b7359bb7ba4994b7ac0897a7`.

The inherited frozen metric is

\[
\Delta_{\rm dual,n}
:=\left|\frac{1-\nu_n^{\rm dual}}{\varepsilon_n}-1\right|,
\]

for which HARD7-04 already established the floor value

\[
\Delta_{\rm dual,n}\to0.
\]

I preserved that value; it is not reset to UNMEASURED. This first R14 successor attack therefore also has no movement in that inherited scalar metric, but it attacks a different source-level obstruction.

The fresh successor methods are **#2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE**.

## 9. Inherited VDH state — what was not restarted

HARD7-04 already preserved two strong partial checkpoints:

1. a candidate source-size formula
   \[
   |C_{2,n}|=(1+o_p(1))\frac{2R_*}{\varepsilon_n^2}
   \log(n\varepsilon_n^3)
   \]
   subject to the earlier reductions recorded in that track;
2. a simultaneous weighted post-giant degree-profile estimate
   \[
   \sum_d(1+d)|N^{out}_{n,d}-n_d\xi_n^d|
   =o_p(n\varepsilon_n).
   \]

The latest HARD7 report also correctly notes that fixed-degree giant-composition asymptotics are already present in the 2019 paper and are not a novelty claim.

I did not rerun the truncation/collar route. The new question is: **even if the post-giant degree sequence is correct, does conditioning a candidate component to be the unique giant bias the pairing on its complement enough to break literal duality?**

## 10. #2 ATTACK THE NEGATION FIRST — exact failure mechanism search

Fix a deterministic candidate giant vertex set `S`, put `T=V\S`, and condition a uniform configuration-model perfect matching on having no `S`--`T` pair.

The attempted counterexample mechanism was that conditioning `S` to be a giant component might induce a complicated global Radon--Nikodym tilt on the pairing inside `T`.

That mechanism fails exactly.

Let `N_S` be “no cross-edge”, `C_S` be “the graph on S is connected”, and let `M_T(|S|)` be “every component in T has fewer than |S| vertices”. Then

\[
G_S=N_S\cap C_S\cap M_T(|S|)
\]

is the event that `S` is the unique largest component.

Conditional on `N_S`, the internal perfect matchings on `S` and `T` are independent and uniform. Conditioning further on `C_S` changes only the `S` matching. Therefore

\[
\boxed{
\mathcal L(X_T\mid N_S,C_S)=CM(d|_T).
}
\tag{10.1}
\]

Requiring `S` to be the **unique largest** adds only one conditioning event on the complement:

\[
\boxed{
\mathcal L(X_T\mid G_S)
=
\mathcal L\bigl(CM(d|_T)\mid L_1(CM(d|_T))<|S|\bigr).
}
\tag{10.2}
\]

This is not an approximation.

## 11. #18 SAY IT IN ANOTHER LANGUAGE — Radon--Nikodym duality identity

Write

\[
p_S=\Pr_{CM(d|_T)}(L_1<|S|).
\]

Then the exact Radon--Nikodym derivative is

\[
\boxed{
\frac{d\mathcal L(X_T\mid G_S)}{d\mathcal L(CM(d|_T))}(x)
=
\frac{\mathbf1\{L_1(x)<|S|\}}{p_S}.
}
\tag{11.1}
\]

Hence

\[
\boxed{
 d_{TV}\!\left(
 \mathcal L(X_T\mid G_S),
 CM(d|_T)
 \right)
=
\Pr_{CM(d|_T)}(L_1\ge|S|).
}
\tag{11.2}
\]

So the entire “being the giant” pairing bias is **exactly** the upper tail that a fresh subcritical complement has a component at least as large as the candidate giant.

This is the cleanest source-level reduction obtained in this invocation.

## 12. #25 COUNT THE SAME THING TWICE — proof of factorization

The factorization behind (10.1) is a direct bijective count. If the half-edge totals of `S` and `T` are `L_S,L_T`, then global perfect matchings with no cross pair consist uniquely of

- one perfect matching of the `L_S` half-edges in `S`, and
- one perfect matching of the `L_T` half-edges in `T`.

Their number is

\[
(L_S-1)!!(L_T-1)!!,
\]

and every ordered pair occurs with equal conditional probability. Thus the two restricted matchings are independent uniform perfect matchings. Connectivity of `S` is measurable only in the first factor, so it cannot bias the second.

The full proof and total-variation identity are in

`artifacts/R14/vdh_fixed_giant_set_conditional_duality.md`

creation commit

`95daf40fe0de059c81a60333a896ff693773b6b5`.

No finite checker is needed: this is an exact combinatorial/probabilistic theorem with the proof on the page.

## 13. What the counterexample-first attack learned

The attack did **not** prove full source duality. It identifies precisely when the conditioning can matter.

If the candidate giant scale is comparable to the natural maximum-component scale of the complement, then the probability in (11.2) need not vanish, and unconditional complement duality can genuinely fail in total variation. So a purely combinatorial theorem valid through the critical window is not available from this argument.

But in the source's barely-supercritical regime the expected scale separation is enormous:

\[
\frac{n\varepsilon_n}
{\varepsilon_n^{-2}\log(n\varepsilon_n^3)}
=
\frac{n\varepsilon_n^3}{\log(n\varepsilon_n^3)}	o\infty.
\tag{13.1}
\]

Therefore a uniform subcritical largest-component upper tail for the **random outside degree sequence** should erase the unique-largest conditioning in total variation via the exact identity (11.2).

This gives a sharper next obligation than “prove duality”:

\[
\boxed{
\sup_{d^{out}\in\mathcal G_n}
\Pr_{CM(d^{out})}\bigl(L_1\ge c n\varepsilon_n\bigr)	o0
}
\tag{13.2}
\]

for a high-probability class `G_n` of post-giant degree sequences produced by the source exploration, followed by a rigorous transfer from the random outside degree law to the extinction-tilted dual law.

The exact fixed-set conditioning step itself is now finished.

## 14. Honest status

- **P0157:** PARTIAL / SOURCE OPEN / terminally released by R14.
- **VDH-8.3-DUALITY:** PARTIAL / SOURCE OPEN / now owned by R14.
- New P0157 analytic theorem: self-check only; 0 independent audits.
- New VDH fixed-set conditional-duality theorem: self-check only; 0 independent audits.
- No worldwide novelty claim. Conditional factorization of perfect matchings is elementary/folklore; the useful point is that it isolates the source proof obligation exactly.
- No source is called PROVED, REFUTED or CLOSED.

The next VDH run should **not** re-use #2/#18/#25. The fresh route recorded here is to attack (13.2) using the inherited weighted histogram estimate plus a subcritical upper-tail theorem that is uniform over the admissible random degree-profile collar. Candidate fresh methods for the next run: **#5 ADD A PARAMETER, #11 DUALIZE, #28 REPLACE FOR ALL WITH FOR TYPICAL**.

## 15. Model/scheduler capability and permission status

The control limitation is still exactly the one recorded by the policy and ledger. The exposed scheduler update surface has fields for prompt/title, schedule/timing, enabled state and timing mode, but **no binding model-family selector, no reasoning-effort selector, no authenticated per-run applied-model/effort receipt and no guaranteed hour-long execution field**. GPT-6/maximum therefore remains prompt text only. This run actually identifies as GPT-5.6 Sol; reasoning effort is not exposed, so it is `UNVERIFIED`.

Changing that requires an authorized product/workspace/API/admin execution surface that actually exposes and persists model/reasoning controls; a GitHub edit cannot create such a scheduler capability.

The historical P26 `You cannot modify this task` event remains an authorization-context issue. The repository records that P26 was later editable from another authorized context. The compliant workaround is the owning/admin-authorized context or platform support, not a permission bypass or duplicate task. I made no scheduler or permission change.

## 16. Structured ledger delta

```yaml
ledger_delta:
  track: R14
  category: HARD_OUTSIDE

  predecessor_target:
    id: P0157
    source_status_before: SOURCE_OPEN
    worker_status_before: PARTIAL_STUCK_RECOVERY_2_CONSUMED
    fixed_metric: Q_n=sigma_n^2/(d_max*delta_n)
    value_before: Q_m=m^-1+O(m^-2)->0
    value_after: Q_m=m^-1+O(m^-2)->0
    movement: NO_FIXED_METRIC_MOVEMENT
    methods: [1, 19, 27]
    new_artifact: artifacts/R14/p0157_online_drift_budget_and_mark_hazard.md
    artifact_commit: 196c95171187e0d16339abbb007aac1dbca3865c
    terminal_action: HANDOFF_AND_RELEASE
    canonical_claim_after: operations/claims/P0157.md
    owner_after: UNASSIGNED_AFTER_R14_HANDOFF
    release_commit: 32204f4e94b97b877b1df42a757edc6dc7195471
    status_after: PARTIAL_SOURCE_OPEN_RELEASED
    terminal_blocker: selection_safe_clock_under_rare_multi_hub_conditioning

  successor_target:
    id: VDH-8.3-DUALITY
    source_status_before: SOURCE_OPEN_PARTIAL_RELEASED
    owner_before: UNASSIGNED_AFTER_HARD7_04_HANDOFF
    owner_after: R14
    reassignment_commit: d878fb0f04b1b191b7359bb7ba4994b7ac0897a7
    fixed_metric: Delta_dual_n=abs((1-nu_dual_n)/epsilon_n-1)
    inherited_value_before: 0
    value_after: 0
    movement: NO_FIXED_METRIC_MOVEMENT_AT_INHERITED_FLOOR
    methods: [2, 18, 25]
    new_artifact: artifacts/R14/vdh_fixed_giant_set_conditional_duality.md
    artifact_commit: 95daf40fe0de059c81a60333a896ff693773b6b5
    status_after: PARTIAL_SOURCE_OPEN
    exact_new_reduction: TV(complement_given_fixed_unique_giant, fresh_CM_complement)=P_fresh_CM(L1>=giant_size)
    next_obligation: uniform_subcritical_upper_tail_over_high_probability_post_giant_degree_profiles
    next_methods: [5, 11, 28]

  audits:
    predecessor_new_claims_independent: 0
    successor_new_claims_independent: 0

  model:
    requested: GPT-6_maximum
    actual: GPT-5.6_Sol
    reasoning: UNVERIFIED
```
