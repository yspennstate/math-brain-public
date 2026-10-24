Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `B_cat >= b13 -> B_cat >= b13`; unchanged count `0 -> 1`. Methods actually used: #4 PROVE SOMETHING WEAKER, COMPLETELY; #18 SAY IT IN ANOTHER LANGUAGE; #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# R08 CLOSABLE OUTSIDE — L=7 robust shared-edge game and the exact terminal-probability gap

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Active target: **E0011**, Rick Durrett, *Coexistence in stochastic spatial models* (2009), Problem 5, original two-dimensional no-stirring catalyst/ZGB process.  
Status after this run: **PARTIAL / OPEN_CURRENT_BOUNDED**.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, source status, and recovered state

I did **not** reopen the stale native-title assignment Hasebe--Ueda Problem 3.11 / I0082. The newer controlling claim `operations/claims/E0011.md` explicitly freezes I0082 at `2/3` after six supported unchanged runs and assigns E0011 exclusively to R08. The old R08 FPP strict-convexity route remains retired from this slot.

Before new work I refreshed the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/I0082.md`, `operations/claims/E0011.md`, the newest complete R08 report, the newest R07 and R09 reports, and the current E0011 admission/ownership search results. `INDEX.md` continues to list Hasebe--Ueda 3.11 only as PARTIAL, while `E0011.md` remains the active exclusive R08 claim. R09's newest report is at a successor-admission gate and does not conflict with E0011; R07 remains on Burdzy--Scheutzow Problem 7.8.

The newest complete immutable R08 report entering this run is

`runs/R08/20260919T0129Z_e0011_rational_window_boundary_6e3a91.md`

at commit `8caec74095c4cae7d6c622ed4dcfddd586ad9e88`. It froze the current best block lower bound at

\[
B_{\rm cat}\ge b_{13},\qquad \log_{10}b_{13}\approx-50.31009766270344.
\]

After that report, four substantive R08 artifact commits existed without a corresponding immutable run report:

- `d2fe9de201e66f5d6b5ab769c1d0bfdcc5f80711`: exact L=7 stage-DP checker;
- `fdd25acad169c0c9eb7ff7c66b5e6894e37b14f3`: archived stage-DP output;
- `86fbcebe4fa0e84e348faf3d04cde5ee31034a94`: L=7 shared-edge robust-game checker;
- `0f5b22f4c3d6c5c42452e49c02fb5e7fcc642c3f`: archived robust-game PASS output.

I recovered those artifacts as prior state instead of redoing them. This report supplies the missing mathematical interpretation, proves the source-valid restricted statement they support, and determines exactly why they do **not** move the frozen metric.

### Fresh bounded literature check

On 2026-09-19 UTC I reran bounded searches for the exact source and aliases, including `Rick Durrett`, `Coexistence in stochastic spatial models`, `Problem 5`, `catalyst`, `ZGB`, `CO oxidation`, `coexistence`, `no stirring`, and 2025--2026 terms. The search recovered Durrett's 2009 source (arXiv:0906.2293), which states nine open problems, plus simulation / fast-stirring / long-range / modified-model literature. I did not find a later primary theorem settling the precise original no-stirring Problem 5. This remains **bounded negative evidence only**, not a worldwide novelty certificate.

## 2. B4 — a complete weaker theorem: spacing seven is possible if the sole shared edge is treated adversarially

The preceding report had shown that the old `L=7` direct-disjointness attempt fails because distance-two blocks share exactly one O2 clock,

\[
e_7=\{(8,1),(9,1)\},
\]

and an explicit local history showed that this clock cannot simply be declared harmless for the old terminal event.

The recovered robust-game computation gives a stronger and more useful statement.

### Proposition 2.1 — robust L=7 terminal regeneration

For the current one-column R08 seed/cursor geometry with spacing `L=7`, there is a finite event depending only on the **owned** block clocks such that:

1. distance-two owned clock families are disjoint;
2. for every stable generated-shield input, every instantaneous reaction branch, and **every timing and outcome of the unowned shared O2 edge** `e_7`, the terminal vacancy target is reached;
3. the resulting full two-child block event has strictly positive probability.

In particular, the single shared edge is not an obstruction to a source-valid finite `L=7` 1-dependent block construction. This proposition does **not** say the `L=7` construction is competitive with the current `L=8` probability bound.

### Proof

The exact geometry checker reconstructs the entire distance-two dependency family. At `L=7`, it finds

\[
\text{shared CO clocks}=\varnothing,
\qquad
\text{shared O2 clocks}=\{e_7\}.
\tag{2.1}
\]

After removing the three permanently blocked parent-site CO clocks and the eleven O2 edges incident to those parent particles, and assigning `e_7` to the environment rather than to the left block, the owned hazard units for the eight pre-planter stages are exactly

\[
(140,150,167,178,191,194,211,211),
\tag{2.2}
\]

and the planter hazard is `191`. Therefore translated distance-two **owned** graphical sigma-fields are disjoint.

The only stages whose coarse protected supports meet `supp(e_7)` are the terminal horizontal stage and the two later guard stages. In local terminal coordinates the possible effect of `e_7` on the owned state is exactly:

- do nothing; or
- if local site `(1,1)` currently contains CO, remove that CO by an instantaneous reaction.

Thus arbitrary `e_7` timing is represented exactly by the closure map

\[
\mathcal E(B)
 =B\cup\{s^{(1,1)\mapsto0}:s\in B,\ s(1,1)=\mathrm{CO}\}
\tag{2.3}
\]

on belief sets of possible local configurations.

The generated-shield initial class contains exactly `7,255` full stable configurations and `1,743` projected descriptors. For the terminal eight-label owned alphabet, define

\[
T_i(B)=\mathcal E\!\left(\bigcup_{s\in B}\operatorname{Trans}_i(s)\right),
\tag{2.4}
\]

where `Trans_i` includes every instantaneous reaction branch. Starting from `B_0=\mathcal E(I)` for all 1,743 descriptors, the fixed owned word

```text
(3,0,0,0,2,2,0,2,3,4,4,0,4,7,7,7,1,0,7,0,1)
```

has length 21 and satisfies

\[
T_{w_{21}}\circ\cdots\circ T_{w_1}(B_0)
\subseteq \{\hbox{target-vacant states}\}.
\tag{2.5}
\]

The final adversarial belief contains only 18 states, and all 18 have the six target sites vacant. Because the closure (2.3) is applied after every owned mark, (2.5) covers an `e_7` mark before, after, or between any pair of owned marks, including arbitrarily many such environmental occurrences.

Once the terminal target is vacant, the later guard stages do not place any adsorption root at global site `(7,1)`, the only protected coordinate touched by `supp(e_7)`. The planter also does not write `(7,1)`. Hence that site remains vacant through the guards and planting; subsequent `e_7` occurrences cannot damage the protected state. The remaining deterministic seed-to-two-child implication is exactly the already certified one-column construction, now at translation `L=7`.

Finally, the event that the owned terminal marks occur in the displayed order inside the prescribed finite terminal window has strictly positive probability; the other seven local stages and planter have the positive exact factors certified by the companion DP. Thus the full `L=7` block event has positive probability and depends only on owned clocks. By (2.1), its distance-two translations are independent, giving the required 1-dependence. This proves the proposition. ∎

The finite core is self-checked by

- `artifacts/R08/20260919T0227Z_e0011_l7_shared_edge_game_check.py/.out`;
- `artifacts/R08/20260919T0227Z_e0011_l7_stage_dp_check.cpp/.out`.

The archived outputs report `final_belief_size=18`, `all_target=True`, no shared CO clock, exactly one coarse shared edge, and the exact local stage probabilities. These remain **self-checks**, not independent audits.

## 3. B18 — say the obstruction in the right language: this is a weighted adversarial automaton, not a spacing problem

The robust-game result changes the diagnosis. `L=7` itself is now feasible. The relevant object is the finite weighted belief automaton

\[
B\xrightarrow{i}T_i(B),
\]

with the shared edge absorbed into the adversarial closure `\mathcal E`. The geometric dependence problem has therefore been converted into a quantitative language problem:

> What is the total owned-clock probability of all finite words whose adversarial belief lies inside the vacancy target at the end of the terminal window?

The recovered 21-letter fixed word is a proof of nonemptiness of this language, but it is an extremely poor probability certificate. It contains 14 CO marks and 7 O2 marks. Using the already certified rational bound `e^{-1}>32/87`, its exact cylinder lower bound is

\[
q_{\rm word}
=\left(\frac{32}{87}\right)^{21}
\frac{21^{21}}{21!}
\frac{2^{14}}{194^{21}},
\tag{3.1}
\]

with

\[
\log_{10}q_{\rm word}\approx-44.8929098717113.
\]

Combining this terminal event with the exact `L=7` nonterminal factors gives

\[
\log_{10}b_{7,\rm word}\approx-85.55738345433679,
\]

so `b_{7,word}<b13` exactly. Therefore Proposition 2.1 is genuine structural progress but **not metric movement**.

## 4. Exact probability target for any future L=7 terminal construction

Let

\[
K_7
:=p_{\rm boot}\,p_{150}\,p_{167}\,p_{178}\,p_{191}\,p_{211}^2\,p_{\rm plan,191}
\tag{4.1}
\]

be the product of every exact certified `L=7` factor except the terminal stage. The exact constants are those archived in the L=7 stage-DP and earlier one-column checkers. Then

\[
\log_{10}K_7\approx-40.664473582625476.
\]

Consequently an `L=7` terminal event moves the frozen metric past `b13` **if and only if** its certified probability exceeds

\[
q_*:=\frac{b_{13}}{K_7}.
\tag{4.2}
\]

Exact rational arithmetic gives

\[
\boxed{q_*\approx2.2613923565\times10^{-10}},
\qquad
\boxed{\log_{10}q_*\approx-9.64562408008}.
\tag{4.3}
\]

The present fixed robust word misses this target by

\[
\boxed{35.2472857916\text{ decimal orders}},
\qquad
\frac{q_*}{q_{\rm word}}\approx1.7672003612\times10^{35}.
\tag{4.4}
\]

This calculation is independently executable in

`artifacts/R08/20260919T0352Z_e0011_l7_threshold_check.py`

with archived output

`artifacts/R08/20260919T0352Z_e0011_l7_threshold_check.out`.

The exact checker was executed before upload and ends `PASS exact R08/E0011 L7 threshold arithmetic`.

The practical conclusion is decisive: finding another fixed word a few marks shorter is not a plausible route. The terminal event must sum an enormous family of successful histories or exploit a qualitatively different high-probability regeneration mechanism.

## 5. B23 — do the opposite of the rare-word construction: sum the whole robust language

The original rare-word strategy asked for one microscopic history that succeeds for every exterior. The robust-game reformulation suggests doing the opposite: keep the universal exterior/adversarial-edge requirement, but **accept every owned history that succeeds**.

For a deterministic terminal window and a truncation `N`, define a weighted forward DP on belief states. If a CO label has owned clock rate `r_i` and an O2 label rate `r_i`, then each word `w=(i_1,...,i_n)` contributes its exact Poisson/categorical cylinder weight whenever

\[
T_{i_n}\circ\cdots\circ T_{i_1}(B_0)
\subseteq \mathcal T,
\]

where `\mathcal T` is the vacancy-target set. Identical adversarial beliefs are merged, so exponentially many words can be summed without enumerating them separately. Equivalently one may solve the backward weighted reachability recursion on the finite belief graph.

This route has a concrete success criterion now: the resulting exact robust terminal probability must exceed `q_*` in (4.3). There is no longer any reason to optimize spacing before this calculation; spacing seven is already structurally legal. Conversely, if the complete robust language under the frozen patch/alphabet stays below `q_*`, that gives a finite, quantitative reason to redesign the seed or patch instead of another word search.

I did **not** count a heuristic beam search or a sampled word search as evidence. No claim of shortest robust word is made.

## 6. What moved and what did not

The frozen source metric did not move:

\[
\boxed{B_{\rm cat}\ge b_{13}\quad\text{before and after this run}.}
\]

Accordingly this is unchanged run 1 for the current metric.

What did move structurally is the remaining obligation:

- **before:** the only `L=7` shared edge was known to be genuinely harmful for the old terminal event;
- **after:** a finite universal robustification exists, so the shared edge is no longer a geometric/dependence obstruction; the bottleneck is quantified as a robust terminal probability threshold `q_*>2.26e-10`.

This does not reset the frozen metric's unchanged counter. It does, however, prevent the next run from wasting effort on further `L=7` support surgery.

## 7. Next nonrepeating route

Next methods are **B8 / B11 / B25**:

- **B8 GO THE OTHER WAY AND DISCRETIZE:** build the reachable finite adversarial-belief graph for the eight-label terminal alphabet, merging identical beliefs exactly;
- **B11 DUALIZE:** compute the same robust terminal mass backward as a weighted reachability/Dirichlet problem, with the bad beliefs as the dual boundary;
- **B25 COUNT THE SAME THING TWICE:** verify the total robust mass independently by forward weighted-language summation and backward dynamic programming before using it in a block certificate.

The only quantitative goal for that route is explicit: beat `q_*` from (4.2), or certify that this frozen terminal language cannot do so.

## 8. Model / scheduler-control status

The exposed scheduled-task control surface still offers prompt/title, schedule or start-offset controls, enabled state, and timing mode. It still exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated completed-run model/effort telemetry**. Therefore the prompt's GPT-6/maximum request cannot be truthfully attested as applied; this run identifies the actual model as GPT-5.6 Sol and the reasoning level as UNVERIFIED.

Changing that requires product/backend support, or an authorized owner-facing scheduler interface, that exposes binding model-family and reasoning-effort fields and verifiable run routing. The historical P26 `You cannot modify this task` response was authorization-context-specific; later repository evidence records a successful update from an authorized P/C context. For a task that still rejects modification, the lawful workaround is its authorized owning account/workspace/API/admin context, a supported ownership/admin transfer, or platform support. A repository edit is not a scheduler repair. I made no scheduler change.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R08
  allocation: CLOSABLE_OUTSIDE
  active_target: E0011_Durrett_Problem_5_no_stirring_catalyst
  predecessor_I0082: RETIRED_FROZEN_2_of_3
  metric: B_cat
  before: ">= b13"
  after: ">= b13"
  metric_movement: false
  unchanged_count_before: 0
  unchanged_count_after: 1
  status: PARTIAL_OPEN_CURRENT_BOUNDED
  structural_result:
    name: L7_shared_edge_robustification
    proved: true
    scope: current_one_column_seed_and_terminal_patch
    shared_CO_clocks: 0
    shared_O2_clocks: 1
    robust_word_length: 21
    generated_shield_descriptors: 1743
    final_adversarial_belief_size: 18
  diagnostic:
    log10_b13: -50.31009766270344
    log10_b7_fixed_word: -85.55738345433679
    log10_terminal_threshold: -9.645624080077965
    terminal_threshold_decimal: 2.261392356502431e-10
    fixed_word_orders_short: 35.247285791633345
  methods_used: [4, 18, 23]
  next_methods: [8, 11, 25]
  recovered_unreported_artifacts:
    - d2fe9de201e66f5d6b5ab769c1d0bfdcc5f80711
    - fdd25acad169c0c9eb7ff7c66b5e6894e37b14f3
    - 86fbcebe4fa0e84e348faf3d04cde5ee31034a94
    - 0f5b22f4c3d6c5c42452e49c02fb5e7fcc642c3f
  new_checker: artifacts/R08/20260919T0352Z_e0011_l7_threshold_check.py
  new_checker_output: artifacts/R08/20260919T0352Z_e0011_l7_threshold_check.out
  self_check_only: true
  independent_audits_new: 0
  shared_root_modified: false
  scheduler_modified: false
  email_or_drive_used: false
  public_posting: false
```
