Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-04 frozen metric has no movement, `Q_m=m^{-1}+O(m^{-2})->0` before and after; Section-I STUCK2 methods B17 / B21 / B28.**

# HARD7-04 bounded research iteration — P0157 STUCK2: from hub skeleton to component mass

Date: 2026-09-19 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN. SECTION-I RECOVERY 2 OF AT MOST 2.** The preceding P0157 run was the third consecutive no-movement checkpoint on the frozen stress-family metric and explicitly required this execution to be a thinking-only STUCK2 report. Accordingly, this run introduces **no new theorem, no checker, and no artifact manufactured for bookkeeping**. The substantive work is to identify the remaining obstruction after the three-hub skeleton theorem, test three genuinely different unused routes against it, and choose exactly one recovery action.

The main diagnosis is now sharper than at STUCK1: the stress family has already settled the **hub-incidence skeleton** — with high probability the largest number of designated degree-`m^2` hubs in any component is exactly three — but the source-relevant object is component **mass**. The simplest unresolved statement is therefore no longer a merger-existence question. It is the mass-transfer problem

\[
\boxed{\frac{L_1}{H_m}\stackrel{?}{\longrightarrow}3,\qquad H_m:=\frac{m^2}{\delta_m}.}
\tag{0.1}
\]

Proving or disproving (0.1) on the explicit source-compatible family is the smallest remaining test that can distinguish a genuine multi-hub component-scaling mechanism from a merely combinatorial hub-count effect.

## 1. Continuity, ownership, and required repository state

I resumed the exclusive canonical claim

`operations/claims/P0157.md`

owned by HARD7-04. I did not restart admission, did not reopen I0049, and did not create an alias claim.

Before the Section-I analysis I re-read/recovered the governing and fleet state:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/P0157.md`;
- the complete indexed HARD7-04 P0157 checkpoint chain through the newest predecessor `runs/hard7_2026-09-18/HARD7-04/2026-09-19T05-32Z__p0157_three_hub_whp.md`;
- the key P0157 artifacts `p0157_finite_population_hub_lln.md`, `p0157_multihub_route_refutation.md`, `p0157_hub_connection_kernel.md`, `p0157_four_hub_exclusion_and_three_hub_witness.md`, and `p0157_three_hub_whp_good_witness_second_moment.md`;
- the newest neighboring HARD7-03 checkpoint `runs/hard7_2026-09-18/HARD7-03/20260919T0628Z__d0025-four-step-pair-overlap-chernoff.md` (its metric moved `250/2989 -> 2500/29711`);
- the newest neighboring HARD7-05 checkpoint `runs/hard7_2026-09-18/HARD7-05/2026-09-19T0550Z__optimal_spectral_majorization.md` (its persistence-width metric moved to `1/4-sqrt(5/(18D))`);
- the indexed intake alias `P0157|3|two competing scales, barely subcritical CM` and repository-wide P0157/source/ownership searches.

The large intake JSONL collections cannot be truthfully rendered byte-for-byte through the connector in one bounded response, so I used the indexed intake entries together with canonical claim and alias searches, as in the preceding runs. No release, competing owner, posted equivalent, or canonical collision surfaced. Shared root ledgers are not edited by this worker; a structured `ledger_delta` appears below.

## 2. Primary source and current-literature refresh

The primary source was rechecked directly, including the page image, on 2026-09-19:

Remco van der Hofstad, *Stochastic processes on random graphs*, current preliminary monograph, Notes on Section 8.3, printed p. 245 / PDF p. 255:

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`

The source explicitly says it is describing “one interesting open problem” for subcritical configuration models with finite third-moment degrees. It recalls the strictly subcritical Janson scale

\[
\frac{d_{\max}}{1-\nu}(1+o_P(1)),
\]

predicts persistence of that behavior sufficiently far below the critical window when `d_max` is sufficiently large, contrasts it with the Erdős–Rényi barely-subcritical scale

\[
\delta_n^{-2}\log(n\delta_n^3),
\]

and concludes that this suggests a phase transition within the subcritical regime. The source wording is predictive prose rather than a fully quantified universal theorem, so the track continues to distinguish its source problem from the stronger universal one-hub statement already refuted on this track.

A fresh bounded current-literature search dated 2026-09-19 rechecked:

1. Matthew Coulson and Guillem Perarnau, *Largest component of subcritical random graphs with given degree sequence*, arXiv:2111.11780 / EJP 28 (2023). They prove configuration-model upper bounds in the barely subcritical regime, asymptotically tight for certain degree sequences, but do not state the full finite-third-moment crossover retained as open by the current monograph.

2. Yiming Chen, *Sharp Asymptotics for the Largest Component in the Subcritical Regime of Preferential Attachment Without Vertex Growth*, arXiv:2607.00731 (1 July 2026). This is a **different model**, but its abstract is highly relevant methodologically: the upper bound conditions on the degree sequence and uses the corresponding configuration model, while the lower bound uses asymptotics of tree components plus a second-moment argument. It proves an Erdős–Rényi-type barely-subcritical largest-component law for that preferential-attachment-without-growth model, not P0157.

3. The existing Janson strictly-subcritical result and the 2023 Coulson–Perarnau paper remain the closest configuration-model references recovered by the bounded search.

No located 2026 paper closes the exact deterministic-degree finite-third-moment crossover asked by van der Hofstad. This is **bounded negative evidence only**, not a worldwide novelty certificate.

## 3. Frozen quantity — no movement and mandatory STUCK2 state

The canonical frozen metric is still

\[
Q_n:=\frac{\operatorname{Var}(T_n)}{(d_{\max}/\delta_n)^2}
=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

On the explicit stress family

\[
n=8m^{12},\qquad M=m^5,\qquad d=m^2,\qquad \delta_m\sim m^{-1},
\]

the established value is

\[
Q_m=m^{-1}+O(m^{-2})\to0.
\]

Before and after this run:

\[
\boxed{Q_m:m^{-1}+O(m^{-2})\to0\quad\longrightarrow\quad m^{-1}+O(m^{-2})\to0.}
\]

**No movement.** The previous three consecutive unchanged checkpoints triggered this STUCK2 run. I do not rename the hub-multiplicity theorem or the strategy diagnosis below as movement in the frozen metric.

No exact-arithmetic checker is added because this execution intentionally makes no finite claim.

## 4. Section-I(a): the exact statement that now blocks

The stress family is fully explicit. For even `m -> infinity`, it has

\[
n=8m^{12},\qquad M=m^5,\qquad d=m^2,
\]

with degrees `1,3,d`, tuned so that `delta_m=1-nu_m~m^{-1}`, empirical third moment tends to `15/2`, and

\[
H_m:=\frac{d}{\delta_m}\asymp m^3,
\qquad
E_m:=\delta_m^{-2}\log(n\delta_m^3)\asymp m^2\log m,
\qquad
H_m/E_m\to\infty.
\]

The latest theorem gives

\[
\mathbb P(H_{\max}=3)\to1,
\]

where `H_max` is the maximum number of designated degree-`m^2` hubs in one connected component. The earlier route refutation gives `P(L_1>3H_m/2)->1`.

The simplest source-relevant statement still blocking progress is therefore

\[
\boxed{
\forall\varepsilon>0:\quad
\mathbb P\!\left(\left|\frac{L_1}{H_m}-3\right|>\varepsilon\right)\stackrel{?}{\longrightarrow}0.
}
\tag{4.1}
\]

Equation (4.1) is **not** claimed by the source and is not proved here. It is the sharpest current special-case test of the proposed marked-upper-tail mechanism. If it is true, the constant `3` comes from the component order of the induced sparse hub skeleton while `H_m` supplies the mass carried per hub. If it is false, the failure identifies the additional statistic beyond hub multiplicity needed by any eventual crossover theorem.

The full source problem is harder still: it must explain how an arbitrary finite-third-moment upper-degree profile interpolates among one-hub, multi-hub, and Erdős–Rényi extremes. But (4.1) is now the smallest unresolved piece that exercises exactly that mechanism.

## 5. Section-I(b): routes already tried and why none proves (4.1)

### Scale and local branching routes: B5 / B12 / B30

These isolated `H_n`, `E_n`, and the local fluctuation ratio `Q_n`. They correctly show when a **fixed** hub-rooted branching forest self-averages. They fail for (4.1) because neither `Q_n` nor `H_n/E_n` records how many comparable hubs can coalesce.

### Fixed-root graph routes: B2 / B4 / B18, then B6 / B11 / B24

These established tree-likeness, exact queue drift, finite-population control, and an LLN for a **preselected** high-degree root. They remain useful ingredients. They fail for (4.1) because the largest component is selected after the graph is seen; a rootwise `o(1)` error cannot be post-selected across `M=m^5` hubs without a tail strong enough to survive that multiplicity.

### Global-tail diagnosis: B15 / B20 / B22

These exposed why a generic MGF/union-bound route is contaminated by the upper-degree tail itself and why existing successful papers use more global degree-tail information. They diagnosed the obstruction but supplied no sharp mass theorem.

### STUCK1: B1 / B26 / B27

Changing category to hub-half-edge matching and swapping the quantifiers produced the explicit three-level stress family. This was decisive diagnostically, but at that stage it only exhibited a candidate multi-hub mechanism.

### STUCK1 recovery success: B3 / B14 / B25

Conditioning on a direct hub edge and contracting it to a super-root, together with exact matching factorial moments, refuted the over-strong universal one-hub route by proving `P(L_1>3H_m/2)->1`. This proves that one selected **two-hub** seed has mass close to `2H_m` under a clean conditioning. It does not automatically extend to the random three-hub component that maximizes mass.

### Marked-kernel route: B7 / B19 / B29

This derived the absorbing branching kernel

\[
\kappa_{ij}\sim\frac{d_i d_j}{\ell\delta_H}
\]

and a one-sided actual-CM no-merger criterion. It also predicted a `k=3/k=4` boundary in the stress family. It fails for (4.1) because the actual-CM comparison is one-sided and controls the **skeleton**, not the conditional mass attached to a realized skeleton.

### Exact skeleton route: B4 / B10 / B16

The four-hub exclusion and exact V-witness first moment converted the kernel heuristic into source-model combinatorics. The remaining dependence was then handled in the next run. These arguments count connecting cores; they do not estimate all bulk vertices hanging from those cores.

### Latest skeleton closure: B2 / B18 / B25

The previous run proved `P(H_max=3)->1` by showing good three-hub witnesses exist whp and no four-hub component exists whp. The component-occupancy identity removed the overlap taxonomy. This is **not** (4.1): a tree component with exactly three hubs can in principle have total mass far from `3H_m` because the attached bulk branches fluctuate and the component itself is selected through a rare hub-connection event.

The last point is now the exact obstruction: **skeleton concentration is not mass concentration**.

## 6. Section-I(c): what a proof must contain that no route so far contains

A proof of (4.1) needs three ingredients simultaneously.

### 6.1 A conditioned three-hub mass theorem with a selection-safe tail

Condition on the occurrence of one of the good V-witnesses used in the latest proof. Its connecting skeleton has only `O(m)` path edges, while the three hubs contribute `3m^2` incident half-edges. After revealing the skeleton, the remaining matching is still uniform on the unrevealed half-edges.

The natural queue therefore starts at

\[
A_0=3m^2+O(m)
\]

and has negative drift of order `delta_m~m^{-1}`. The heuristic hitting time is

\[
A_0/\delta_m=(3+o(1))H_m.
\]

Previous fixed-root LLNs only produce convergence in probability under a preselected conditioning. Here one needs a quantitative tail, ideally of the form

\[
\mathbb P\!\left(
\left|\tau-3H_m\right|>\varepsilon H_m
\mid w\text{ occurs and is good}
\right)
\le e^{-c_\varepsilon m},
\tag{6.1}
\]

or any bound strong enough to survive all witness/hub multiplicities used in the global argument. Equation (6.1) is a **target**, not a result of this run.

The important structural simplification is that away from hubs the stress family has degrees only `1` and `3`, so the active queue has essentially `-1/+1` bulk increments. This is much more rigid than the arbitrary finite-third-moment source class and makes (4.1) a plausible finite-population martingale problem rather than a generic heavy-tail problem.

### 6.2 A lower-bound argument that does not post-select illegally

The latest proof already has `E Z_m^g~c m` and `P(Z_m^g>0)->1` for good V-witnesses. If a uniformly conditioned occurring good witness has exponentially small probability of mass below `(3-epsilon)H_m`, one can define the **bad-good witness count** and estimate its expectation before selecting the graph's largest component. That is the right quantifier order. What is missing is the conditional mass bound, not another witness first moment.

### 6.3 A global upper bound after four-hub exclusion

The existing theorem gives at most three designated hubs per component whp. To prove `L_1<=(3+epsilon)H_m` whp, one still needs:

- a uniform enough mass tail for every component containing one, two, or three hubs; and
- a separate bound showing hub-free components live on the Erdős–Rényi scale `E_m=o(H_m)`.

Neither follows merely from `H_max<=3`. The latter is exactly where Coulson–Perarnau-style global subcritical exploration estimates or Chen's tree-component counting architecture may be more appropriate than another rootwise LLN.

For the full source problem, these ingredients would have to be lifted from the three-level family to a **marked upper-tail graph plus a mass map**: first identify the random connectivity among high-degree marks, then attach a `1/delta_n`-scale bulk mass to each mark/core, and finally compare the largest marked mass with the hub-free Erdős–Rényi extreme. No previous route on this track supplies this two-layer object.

## 7. Section-I(d): simplest special case still unproved

The simplest unproved case is exactly (4.1): for the explicit degree-`{1,3,m^2}` family already fully checked against the source moment assumptions, determine whether

\[
\frac{L_1}{H_m}\xrightarrow{P}3.
\]

Why this is now the right test:

- the degree sequence is explicit;
- `delta_m~m^{-1}` and `H_m~m^3` are explicit;
- `E_m=o(H_m)`;
- `Q_m->0` rules out local branching variance as the main obstruction;
- the actual configuration model, not a surrogate, has `H_max=3` whp;
- the source-level hard part has been reduced to bulk mass attached to a known sparse hub skeleton.

A proof of this special case would still be **PARTIAL**, not closure of P0157. A counterexample would be equally informative because it would show that even the full hub skeleton does not determine component mass.

## 8. Section-I(e): nearest solved problems and the missing ingredient

There are three useful comparators, each close in a different sense.

**Janson (2008)** is the source's classical comparator: in a strictly subcritical power-law setting, the largest component tracks the largest degree. What that setting supplies is structured information about the entire upper degree tail, not just moment convergence.

**Coulson–Perarnau (2023)** is the closest general prescribed-degree configuration-model result recovered in the current search. Their barely-subcritical upper-bound machinery is global rather than fixed-root and becomes asymptotically tight for certain degree-sequence classes. What P0157 lacks is a universal upper-tail regularity class under which one can turn those global controls into an exact two-sided crossover law.

**Chen (2026)** is the closest new methodological analogue found this run. In preferential attachment without vertex growth, the abstract states that the upper bound is obtained by conditioning on the degree sequence and treating the graph through the corresponding configuration model, while the lower bound comes from asymptotics of tree components plus a second moment. That proof architecture has exactly the split now missing here: a global upper bound and a source-model tree-component lower count. What Chen has and P0157 lacks is a specific random degree-sequence law whose upper tail can be analyzed jointly; P0157 permits arbitrary deterministic finite-third-moment sequences.

The transferable lesson is therefore **not** a theorem from those papers. It is the proof decomposition: use the configuration-model exploration for the upper tail, but obtain the lower bound by counting full tree components of the desired mass rather than only their connecting hub skeletons.

## 9. Ninety-percent thinking: three unused Section-B moves

This STUCK2 run deliberately uses three methods not previously used on P0157: **B17, B21, B28**.

### B17 — look for your numbers somewhere else

The stress-family kernel heuristic gave

\[
M^k p_m^{k-1}\asymp m^{7-2k},
\]

so `k=2` structures are abundant, `k=3` structures still diverge, and `k=4` structures vanish. The actual-CM work has now rigorously confirmed exactly that `3/4` skeleton boundary.

The useful reinterpretation is that the constant `3` is not naturally a mysterious configuration-model constant. It is the largest component order of a very sparse **auxiliary graph on hubs** at this scaling. Component mass should then be approximately

\[
\frac{1}{\delta_m}\times(\text{sum of hub degrees in the auxiliary component})
\]

plus a lower-order bulk fluctuation. This language separates two random mechanisms that the original scalar `d_max/delta` comparison conflated: auxiliary hub connectivity and bulk mass transfer. It also makes clear why `Q_m` can be tiny while the global answer changes by a factor of three.

**Outcome:** useful reframing, but no theorem. It identifies (4.1) as a two-layer problem rather than another refinement of the one-hub law.

### B21 — ask who else has this shape

The fresh literature search found Chen's July 2026 preferential-attachment-without-growth result. The model is different, so no conclusion can be imported. But the proof architecture reported in the abstract — configuration-model conditioning for the upper bound, tree-component asymptotics plus a second moment for the lower bound — matches the present obstruction unusually closely.

The corresponding P0157 route would be:

1. condition on/reveal only the finite three-hub core;
2. count **full tree hosts in a narrow mass window**, not merely V-shaped cores;
3. use a second moment at the full-component level for the lower bound;
4. use a global subcritical exploration bound for the upper bound.

This is more promising than classifying further V-witness overlaps, because that overlap problem was already solved while the mass problem remained untouched.

**Outcome:** a concrete technique transfer target is identified. It does not establish applicability; the finite-population mass tails must still be proved in this deterministic stress family.

### B28 — replace “for all” with “for typical” before restoring the maximum

A direct uniform theorem over every three-hub component is stronger than needed for the lower bound and invites the same quantifier problem that broke the original route. Instead, work first under the size-biased law of an **occurring good V-witness**.

The desired intermediate statement is only:

\[
\mathbb P\!\left(
|C(w)|<(3-\varepsilon)H_m
\mid w\text{ occurs and is good}
\right)=o(m^{-1}),
\tag{9.1}
\]

uniformly over the witness parameters used in the existing first moment. Since `E Z_m^g=Theta(m)`, an `o(m^{-1})` conditional defect would make the expected number of undersized good witnesses `o(1)`. Combined with `P(Z_m^g>0)->1`, that would give a lower bound for `L_1` without post-selecting a hub component. An exponential bound such as (6.1) is more than sufficient but not logically necessary.

For the upper bound, one can then ask for uniform tails only over the `M=m^5` designated hubs, rather than over every possible core embedding. This is a much smaller uniformity burden.

**Outcome:** this quantifier weakening isolates the likely sharp level of concentration required. It turns the next proof target from “uniform three-hub theorem over all realizable cores” into a witness-weighted conditional tail plus a separate `M`-hub upper tail.

## 10. Exactly one Section-I recovery choice

I choose exactly one recovery:

**PROVE THE SIMPLEST UNPROVED SPECIAL CASE.**

The next substantive HARD7-04 run should attempt (4.1) for the explicit degree-`{1,3,m^2}` stress family. It must not claim that this closes van der Hofstad's full crossover problem.

The next three Section-B moves are deliberately different from this run and are the remaining unused tools best matched to the task:

- **B8 — DISCRETIZE:** after conditioning on an exact good V-witness, reduce the unexplored host to a finite-population active-half-edge walk with explicit `+1/-1` bulk increments and controlled depletion;
- **B9 — RANDOMIZE:** count undersized/oversized full host components through witness indicators before selecting `L_1`, so the argument respects the correct quantifier order;
- **B13 — FIND WHAT ONLY INCREASES:** seek a predictable drift/variance budget or exponential supermartingale whose compensator accumulates monotonically until the queue hitting time, strong enough to yield the selection-safe tail required in (9.1).

This is **recovery 2 of at most 2** on P0157. If this target later reaches the Section-I stuck trigger again without metric movement or a changed remaining obligation, the next stuck episode is not allowed to launch a third recovery on P0157: it must leave a handoff and rotate to a fresh admissible HARD7-04 target.

## 11. Capability honesty required by the owner directive

The scheduler capability situation remains unchanged in the exposed interface. It offers task **title, prompt, schedule/timing mode, and enabled state**, but no bindable model selector, no bindable reasoning-effort selector, no authenticated per-run maximum-reasoning telemetry, and no guaranteed execution duration. Therefore `GPT-6 / maximum` remains a prompt request only.

This invocation is actually **GPT-5.6 Sol**. The reasoning-effort level is not exposed as authenticated runtime metadata, so it is **UNVERIFIED**.

Making GPT-6/maximum binding would require a product/workspace/API/admin scheduling surface that exposes persistent model-family and reasoning-effort fields and honors them at execution time, together with runtime metadata that can verify the routing. Stronger prompt wording or a repository edit cannot create those capabilities.

The repository policy records historical native edit probes returning `You cannot modify this task` for P26/P01/P03 in one context and later successful P26 modification from another authorized context. The legitimate workaround for an ID that still returns that denial is the owning account/workspace/admin context or platform support. Do not bypass the restriction, clone the task, or reactivate a disabled task. No schedule was created, modified, disabled, or reactivated in this run.

## 12. Checkpoint / ledger delta

```yaml
ledger_delta:
  track: HARD7-04
  target: P0157
  source_status: OPEN
  worker_status: PARTIAL
  section_I_state: STUCK2_RECOVERY_CHOSEN
  stuck_recovery_count: 2
  frozen_quantity: Q_n = sigma_n^2/(d_max*delta_n)
  before_on_stress_family: Q_m = m^-1 + O(m^-2) -> 0
  after_on_stress_family: Q_m = m^-1 + O(m^-2) -> 0
  movement: false
  methods_this_run: [B17, B21, B28]
  exact_blocker: "for the explicit stress family, decide whether L1/H_m -> 3 in probability"
  existing_skeleton_fact: "P(H_max=3)->1"
  key_missing_ingredient: "selection-safe conditional mass concentration for a three-hub tree host, plus global upper control"
  literature_transfer: "Chen 2026: CM-conditioned upper bound plus tree-component second-moment lower bound in a different PA-without-growth model"
  recovery_choice: PROVE_THE_SIMPLEST_UNPROVED_SPECIAL_CASE
  next_methods: [B8, B9, B13]
  next_obligation: "attempt L1/H_m -> 3 on the explicit degree-{1,3,m^2} family; no source-closure claim"
  artifact: none_new_thinking_only
  checker: none_new
  next_stuck_rule: "any later third Section-I episode on P0157 must hand off and rotate"
```

No email or Drive action was taken. No shared root ledger was edited.