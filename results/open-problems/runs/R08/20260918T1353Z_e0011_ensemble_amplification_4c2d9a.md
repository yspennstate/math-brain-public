Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `B_cat: >= 1/(3^432*1204^328*19264^104) -> >= 3099691319296*(35/486)*(1/72)^20*(32/26187)^328*(16/26187)^104`; unchanged count `0 -> 0`. Methods used: B9, B13, B28.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: ensemble amplification and the real synchronization bottleneck

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, repository state, source status, and exclusions

I continued from the newest complete R08 report

`runs/R08/20260918T1230Z_e0011_two_child_positive_certificate_7b91c2.md`

rather than restarting the stale native title. The active exclusive claim remains `operations/claims/E0011.md`: Rick Durrett, *Coexistence in stochastic spatial models*, Ann. Appl. Probab. 19 (2009), Problem 5, for the original two-dimensional catalyst/ZGB process with `r=infinity` and `q/2=1-p`, with **no added stirring**.

At run start I reread/refreshed `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the controlling new-methods owner directive, `operations/claims/I0082.md`, `operations/claims/E0011.md`, the newest R08 report and current neighboring R07/R09 state, plus repository exact-key searches over E0011 and the intake/admission history. E0011 remains exclusively R08-owned. Hasebe--Ueda Problem 3.11 / I0082 remains RETIRED/FROZEN at `2/3`, retirement count 6; I did not reopen it or the old FPP strict-convexity route.

I also refreshed current literature on 2026-09-18. Durrett's source still states Problem 5 and explicitly distinguishes the no-stirring target from Bramson--Neuhauser's large-polymer result and Durrett--Swindle's fast-stirring theorem. Fresh bounded searches for later rigorous no-stirring ZGB/catalyst coexistence again recovered the source and the old modified-model results but no later primary theorem settling the original Problem 5. This is bounded negative evidence, not bibliographic omniscience or a novelty certificate.

The source definition of coexistence is the existence of a stationary distribution concentrating on configurations with infinitely many sites occupied by each species. The source's simulated ZGB coexistence window remains approximately `0.389 <= p <= 0.525`; that simulation is motivation only, not evidence for closure.

## 2. Frozen metric before this run

The active metric is

\[
B_{\rm cat}=\sup_C b(C),
\]

where `C` ranges over complete source-valid finite protected Harris-block certificates at the rational anchor `p_0=1/2` and `b(C)` is an exact certified lower bound on the good-block probability.

The preceding run proved the first positive two-child certificate,

\[
b_0=\frac{1}{3^{432}1204^{328}19264^{104}},
\]

using one single 432-mark adsorption history plus a very pessimistic reaction-tie penalty. The central question this run was not to shorten that word by another few marks. It was to determine how much of the `10^{-1662}` scale is a genuine dynamical obstruction and how much is an artefact of conditioning on one microscopic realization.

The answer is sharp enough to redirect the route: **almost all of the previous reaction penalty was artificial. The dominant remaining cost is the prescribed adsorption identity/order itself.**

## 3. B28 — replace universal reaction choices by exact typical reaction probabilities

The previous finite checker fixed one legal priority for instantaneous reactions and then paid a worst-case factor `1/4` for every CO mark and `1/32` for every O2 mark, even when a mark had no reaction choice at all. That was deliberately safe, but vastly too expensive.

For `r=infinity`, the correct local law is elementary. If a newly adsorbed CO has `k` oxygen neighbors, the `k` equal-rate reaction clocks race and each neighbor is chosen with probability `1/k`. If an O2 adsorption creates two adjacent oxygen atoms with `k_1,k_2` neighboring CO atoms, the two neighbor sets are disjoint on the square lattice. Taking the finite-`r` exponential races and then `r -> infinity`, the final chosen CO neighbor at each endpoint is uniform, and the pair of choices has probability `1/(k_1 k_2)`. Thus the reaction randomness can be propagated exactly through a finite word.

I did that with exact rational arithmetic for **every stable boundary environment**, not by sampling.

### Expander

For the 21-mark boundary-uniform vacancy expander from the preceding report, over all exactly `50,785` stable one-neighborhood environments,

\[
\boxed{q_{\rm exp}:=\min_{\rm stable\ boundary}
P(\text{expander ends with all six active sites vacant}\mid\text{the 21 adsorption marks})=\frac1{72}.}
\]

The vertically reflected expander word has the same exact minimum `1/72`.

### Eraser

For the 6-mark boundary-uniform canonical-seed eraser, over all exactly `625` compatible stable environments,

\[
\boxed{q_{\rm erase}:=\min_{\rm stable\ boundary}
P(\text{eraser clears its active 2x2}\mid\text{the 6 adsorption marks})=\frac{35}{486}.}
\]

The reflection across the seed's occupied diagonal has the same exact minimum `35/486`.

### Planters

The 3-mark planter has no adverse reaction tie: the first CO has a unique oxygen reaction partner and the second CO then stays. Its reflected version inside the `4x4` vacant child box is also exact and produces the same canonical outgoing seed.

These are finite exact claims. The executed self-check is

`artifacts/R08/20260918T1353Z_e0011_ensemble_amplification_check.py`

with archived output

`artifacts/R08/20260918T1353Z_e0011_ensemble_amplification_check.out`.

The output includes

```text
q_exp_min=1/72
q_exp_mirror_min=1/72
q_erase_min=35/486
q_erase_mirror_min=35/486
```

This is a self-check, not an independent audit.

The conceptual gain is large. Instead of paying a reaction factor of

\[
4^{-328}32^{-104},
\]

we may pay only

\[
\frac{35}{486}\left(\frac1{72}\right)^{20}
\]

for the eraser and twenty expander primitives. The reaction races themselves are therefore **not** the main reason the certificate is tiny.

## 4. B9 — randomize over a rigorously disjoint ensemble of successful adsorption histories

The preceding macro used one total order of its 432 prescribed adsorption marks. But the deterministic implication survives many distinct primitive-level histories.

There are two independent length-10 expander chains, one on rows `0,1` and one on rows `2,3`. Within each row pair the columns must be opened from left to right, but the two chains may be interleaved arbitrarily. Boundary-uniformity is exactly what makes this legal: an expander only needs its own incoming `2x2` vacancy cursor, and the other row-pair operation can remove boundary particles but cannot fill that cursor. Hence the two chains admit

\[
\binom{20}{10}
\]

whole-primitive shuffles.

There are also:

- `2` exact reflected eraser choices preserving the same canonical seed;
- `2` reflected versions for each of the `20` expander applications;
- `2` orders for the two final planters;
- `2` exact planter variants for each child.

Therefore the same two-child deterministic implication is realized by at least

\[
\boxed{
K=2\cdot 2^{20}\binom{20}{10}\cdot2\cdot2^2
=2^{24}\binom{20}{10}
=3,099,691,319,296
}
\]

distinct complete 432-mark adsorption sequences.

They are disjoint events under the old 432-slot construction: two different histories differ in the identity of the required protected adsorption clock in at least one slot. Thus their probabilities may be added, not merely union-bounded.

This is the useful form of B9 here: do not ask one microscopic trajectory to carry the block; sum an exactly controlled family of trajectories that all imply the same coarse two-child event.

## 5. Exact rational slot bound, improved without floating point

The protected geometry and slot construction are unchanged from the preceding report. At `p=1/2`, a specified CO site is the unique protected adsorption mark in its slot with probability

\[
e^{-1}/301,
\]

and a specified O2 edge with probability

\[
e^{-1}/602.
\]

For a slightly sharper rational bound than the old `e<3`, write

\[
e=\sum_{k=0}^6\frac1{k!}+\sum_{k\ge7}\frac1{k!}
\le \frac{1957}{720}+\frac1{6!\,6}
=\frac{11743}{4320}<\frac{87}{32}.
\]

Hence

\[
e^{-1}>\frac{32}{87},
\]

so each prescribed CO slot contributes strictly more than

\[
\frac{32}{87\cdot301}=\frac{32}{26187},
\]

and each prescribed O2 slot contributes strictly more than

\[
\frac{32}{87\cdot602}=\frac{16}{26187}.
\]

Combining the `K` disjoint adsorption histories with the exact worst-boundary reaction probabilities gives the new finite certificate

\[
\boxed{
 b_1:=
 3,099,691,319,296\,
 \frac{35}{486}
 \left(\frac1{72}\right)^{20}
 \left(\frac{32}{26187}\right)^{328}
 \left(\frac{16}{26187}\right)^{104}.
}
\]

The exact checker cross-multiplies integers and verifies

\[
\boxed{b_1>b_0.}
\]

Therefore the frozen metric moves to

\[
\boxed{B_{\rm cat}\ge b_1.}
\]

For scale only, not as the certificate,

\[
\log_{10} b_1\approx -1315.49,
\]

versus `-1662.18` for `b_0`. Thus the ensemble/tie calculation recovers about **346.7 decimal orders of magnitude** while remaining astronomically below the supercritical block target. The exact rational expression above is the result.

## 6. B13 — a pathwise monovariant is blocked by an exact local cycle

I also tested the most natural B13 idea: seek a vacancy/interface functional that increases under every source transition. There is a simple source-valid obstruction already in the minimal interface geometry.

Take the stable horizontal pattern

\[
A:\qquad C\;0\;O
\]

at sites `0,1,2`, with the nearby exterior vacant. Then the following three legal adsorption events form a directed cycle, with unique reaction outcomes throughout:

1. `CO(1)`: the incoming CO reacts with the O at site 2, leaving only the CO at site 0;
2. `O2(1,2)`: the O at site 1 reacts with the CO at site 0 while the O at site 2 remains;
3. `CO(0)`: site 0 is distance two from the surviving O, so the CO remains and the state is again `C 0 O`.

Thus

\[
A\to A_1\to A_2\to A.
\]

The exact checker verifies this cycle. Consequently any scalar functional that is nondecreasing along **every** legal transition must be constant on this cycle. In particular vacancy count, number of occupied sites, and the elementary one-dimensional interface counts cannot be strict pathwise monovariants for the required mechanism.

This does not kill B13 entirely; it says the right object must be a **drift/submartingale, Lyapunov function in expectation, or an absorbing-probability potential**, not an eventwise increasing count. That is a useful negative result because it prevents the next run from wasting time on a deterministic vacancy-growth invariant that the source dynamics forbids locally.

## 7. What actually blocks closure now

The preceding run showed deterministic two-child reproduction exists. This run shows reaction-tie randomness is much cheaper than the old certificate suggested and that trillions of successful primitive-level adsorption histories can be summed exactly.

The remaining penalty is overwhelmingly the requirement that **the adsorption identities arrive in a highly constrained 432-step order**. Even after recovering about 346.7 decimal orders,

\[
b_1\ll 63/64.
\]

So another round of word symmetries or a modest word shortening cannot plausibly close the source. The route that now looks materially different is:

\[
\boxed{
\text{replace prescribed words by a local absorbing/hitting-probability problem that sums all successful histories.}
}
\]

The expander and eraser are already finite Markov systems with exact rational rates. Instead of certifying selected trajectories, compute or bound the probability of hitting the cleared/branched target **before** a genuinely fatal local state, allowing arbitrary successful internal event orders. If a one-column interface module has success probability bounded away from zero (or a favorable drift), then a mesoscopic renormalization can amplify that rather than paying a 432-event synchronization cost.

This is the strongest route change from the run: the exact ensemble calculation identifies precisely which randomness must be integrated out next.

## 8. Status and honest label

**Proved this run:** the two primitive worst-boundary reaction-success constants `1/72` and `35/486`; their reflected counterparts; at least `K=3,099,691,319,296` disjoint successful macro adsorption histories; the rational bound `e<87/32`; the improved exact block lower bound `b_1>b_0`; and the exact three-event interface cycle obstructing a strict pathwise monovariant.

**Not proved:** coexistence, any block probability near `63/64`, a supercritical oriented-percolation comparison, or Durrett Problem 5 itself. No closure or novelty claim is made. The finite-state control/ensemble mechanism may be folklore; priority is UNVERIFIED.

Track status remains

\[
\boxed{\text{PARTIAL / source OPEN under bounded current-literature checking}.}
\]

Because the frozen metric moved, the unchanged count remains/reset to zero and the Section-I stuck protocol is not triggered.

## 9. Next distinct methods

Do not repeat B9/B13/B28 next run. The next triple is:

- **B11 DUALIZE.** Treat local block success as an absorbing-probability/Dirichlet problem for a finite CTMC rather than a trajectory enumeration. The harmonic function of the local generator automatically sums every successful history.
- **B19 MAKE IT AN ALGORITHM.** Build a dynamic-programming/state-aggregation procedure that accepts every source-valid internal history leading from one cursor/interface seed to a cleared next-column or branched seed, with exact rational transition probabilities.
- **B30 ONE SCALE / ONE DIRECTION AT A TIME.** First solve one-column interface propagation exactly, including its failure states; only then glue columns. The present 20-expander macro is too coarse to reveal whether the one-column module has a favorable hitting probability.

The target for the next run is not another symmetry factor. It is an exact or certified lower bound for the **all-histories one-column hitting probability** that strictly dominates the fixed-word `1/72` mechanism in a way capable of iteration.

## 10. Structured ledger delta (own immutable report only)

```yaml
ledger_delta:
  worker: R08
  predecessor: I0082
  predecessor_state: RETIRED_FROZEN
  predecessor_metric: 2/3
  predecessor_retirement_count: 6
  target: E0011
  source: Durrett_2009_Problem_5
  allocation: CLOSABLE_OUTSIDE
  owner: R08
  metric: B_cat
  before: ">= 1/(3^432 * 1204^328 * 19264^104)"
  after: ">= 3099691319296*(35/486)*(1/72)^20*(32/26187)^328*(16/26187)^104"
  movement: positive
  unchanged_count_before: 0
  unchanged_count_after: 0
  source_status: OPEN_CURRENT_BOUNDED
  track_status: PARTIAL
  methods: [9, 13, 28]
  research_delta:
    - exact_worst_boundary_reaction_success_expander_1_over_72
    - exact_worst_boundary_reaction_success_eraser_35_over_486
    - reflected_primitive_families_with_same_exact_bounds
    - exact_3099691319296_disjoint_successful_macro_adsorption_histories
    - rational_e_upper_11743_over_4320_less_than_87_over_32
    - improved_exact_Bcat_lower_bound_b1_gt_b0
    - exact_three_event_C0O_interface_cycle_blocks_strict_pathwise_monovariant
  finite_core:
    checker: artifacts/R08/20260918T1353Z_e0011_ensemble_amplification_check.py
    output: artifacts/R08/20260918T1353Z_e0011_ensemble_amplification_check.out
  audits: []
  remaining_obligation: raise_a_source_valid_two_child_block_probability_to_a_certified_supercritical_1_dependent_level_then_use_parameter_continuity_to_open_a_nontrivial_p_interval
  next_methods: [11, 19, 30]
```

## 11. Model / reasoning / task-control status

The actual model visible to this run is **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so I report `UNVERIFIED` and do not claim GPT-6 maximum.

The exposed scheduler/task-management surface still offers prompt/title/schedule-or-timing/enabled controls but **no binding model-family selector and no reasoning-effort selector**, and no authenticated completed-run model telemetry or guaranteed one-hour execution control. Therefore GPT-6/maximum remains requested in prompt text only in this context. Changing that would require a native model/reasoning control in the authorized scheduler/product surface or a platform-level capability change; GitHub text cannot enforce it.

The current root ledger also records that the historical P26 `You cannot modify this task` failure was context-specific: the full P26 update later succeeded from an authorized P/C context. For a task that still refuses modification, the lawful workaround is the authorized owning context, a supported ownership/admin transfer, or platform support. Duplicating a task or editing repository prompts does not change runtime model selection.

I made no scheduler changes, no email/Drive/public-posting actions, and no edits to shared root ledgers or peer-track files in this run.
