Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `B_cat >= b19_full -> B_cat >= b19_full`, with `log10 b19_full ~= -49.86198560335649`; unchanged count `0 -> 1`. Methods actually used: B1, B13, B30.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: stopping-frontier corridor and the fixed-top obstruction

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Active target: **E0011**, Rick Durrett, *Coexistence in stochastic spatial models* (2009), Problem 5, original two-dimensional no-stirring catalyst/ZGB process.  
Status after this run: **PARTIAL / source OPEN under bounded current-literature checking**.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, source gate, and ownership

I continued from the newest complete R08 report on `master`,

`runs/R08/20260919T1054Z_e0011_full_robust_bootstrap_b19_c8f41d.md`,

rather than restarting from the stale native scheduler title.

The controlling ownership file `operations/claims/E0011.md` still assigns E0011 exclusively to R08 and records the predecessor Hasebe--Ueda Problem 3.11 / `I0082` as **RETIRED/FROZEN at `2/3` after six supported unchanged runs**. I did not reopen I0082, its finite-variance exclusion, the posted Hasebe--Ueda Problem 3.3 work, R19's classical stable-law exclusion, or the old R08 FPP route.

Before new mathematics I refreshed the required repository state: campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the E0011 claim, the newest own report/artifacts, and the newest visible neighboring R07/R09 state. R07 has reached its six-run retirement/successor gate on a different source; R09 is likewise in successor admission/gating on distinct material. Neither owns E0011.

The source/current-literature screen was refreshed on 2026-09-19. Durrett's arXiv:0906.2293 still advertises nine challenging open problems. Bounded searches for the exact catalyst/ZGB Problem 5, no-stirring coexistence, and 2025--2026 ZGB work again recovered modified/simulation models but no later primary theorem proving the original source statement. This is **bounded negative evidence only**, not a worldwide-open or novelty certificate.

## 2. Entering metric and why another local constant is not the right target

The frozen metric remains

\[
B_{\rm cat}=\sup_C b(C),
\]

where `C` ranges over complete source-valid finite protected two-child Harris-block certificates at `p=1/2` with a deterministic seed-reproduction implication and translated 1-dependent block field.

The entering certified value is

\[
B_{\rm cat}\ge b_{19,\rm full},
\qquad
\log_{10}b_{19,\rm full}\approx-49.86198560335649.
\]

The preceding run already solved the eight-arrival robust bootstrap Bellman problem for the current local alphabet and gained only another `8.37%`. Earlier architecture-cap work also showed that optimizing one terminal factor cannot bridge the dozens-of-orders gap to the sufficient `63/64` threshold. Therefore this run did **not** spend its research budget on another local alphabet tweak.

## 3. B1 — change category: from separately timed cylinders to a stopping-frontier process

The current spacing-eight one-column block still clears the corridor by multiplying several separately timed local cylinder events. Each local event asks that, at a prescribed deterministic micro-window endpoint, a `2x3` vacancy target be present.

That endpoint synchronization is not intrinsic to the dynamics. If the target is reached earlier, the natural control action is to advance the active window immediately to the next spatial stage.

For one local stage with protected hazard `D`, let `A` be the six-vacancy `2x3` target, and let `L` be the already certified maximal support-preserving local alphabet (10 labels, except the terminal trimmed stage's certified 8-label alphabet). Every protected arrival outside `L` is sent to a cemetery state. Define

\[
\tau_A=\inf\{m:\text{the local state after protected arrival }m\text{ lies in }A\},
\]

and let `tau_dag` be the first protected arrival whose clock is outside the accepted alphabet.

For an entrance descriptor `s`, define the stopping-frontier value

\[
h_m(s)=\Pr_s\{\tau_A<\tau_\dagger,\ \tau_A\le m\}.
\]

This is a different category of object from the existing fixed-window endpoint probability: the stage stops as soon as its spatial frontier is successfully advanced.

With the established integer reaction weights and `H=36D`, the exact recurrence is

\[
G_0(s)={\bf1}_A(s),
\]

\[
G_m(s)=H^m\quad(s\in A),
\]

and, for `s notin A`,

\[
G_m(s)=\sum_{\ell\in L}\sum_t w(s,\ell,t)G_{m-1}(t),
\qquad
h_m(s)=\frac{G_m(s)}{H^m}.
\tag{3.1}
\]

The omitted protected-clock mass is exactly the cemetery probability, so (3.1) is an exact killed-chain calculation, not simulation.

## 4. B13 — the stage index is the missing monovariant

The useful monotone quantity is not particle number or vacancy parity; both can move in either direction. It is the **frontier stage index**.

On the successful stopping-frontier event, once stage `j` hits its vacancy target, the active local module is translated/rotated to stage `j+1` immediately. The previous stage never needs to be solved again. Later protected sets already contain the previously required cleared cells, so a good later history preserves the pieces needed by the final child planter.

Thus, on the controlled event,

\[
J_t\in\{3,4,5,6,7,8,g_\downarrow,g_\uparrow\}
\]

is nondecreasing and increases whenever the active vacancy target is hit.

This is source-compatible because the next-stage bounds are uniform over their full certified stable entrance classes. Material farther ahead may evolve arbitrarily before activation; when that stage starts, its state is simply one of the stable adversarial entrance descriptors already minimized over. There is no need to freeze the whole future corridor in advance.

This is the main conceptual advance of the run: the repeated rare-window product should be replaced by one monotone frontier process.

## 5. B30 — solve one direction first: exact post-bootstrap stopping probabilities

I did not attempt the full two-child automaton before testing whether the new category buys anything quantitatively. I solved exactly the eight **post-bootstrap clearing stages** of the current spacing-eight architecture:

\[
D=(150,167,178,187,197,201,218,222).
\]

The first five horizontal stages use the generated-shield entrance class of **1,743** descriptors and the maximal 10-label alphabet. The terminal horizontal stage uses the same 1,743 entrances and the certified 8-label trimmed alphabet. The two rotated guard stages use the full base class of **12,201** descriptors and the 10-label alphabet.

For every stage I computed

\[
q_j:=\min_s h_8(s)
\]

exactly. The results are:

| stage | `D` | exact `q_j` | decimal |
|---|---:|---|---:|
| `h3` | 150 | `16074639051680369/124556484375000000000` | `1.2905501574e-4` |
| `h4` | 167 | `30344586508740575/294014018843111629926` | `1.0320795800e-4` |
| `h5` | 178 | `44282206001815193/489774632850230109696` | `9.0413433101e-5` |
| `h6` | 187 | `59326158916448255/726723361761569191206` | `8.1635133860e-5` |
| `h7` | 197 | `80812237507711895/1102468218239207857446` | `7.3301194693e-5` |
| terminal `h8` | 201 | `11115007398201754/215801012628378849681` | `5.1505816691e-5` |
| `g_down` | 218 | `335516236200631/5685932881388232576` | `5.9008124647e-5` |
| `g_up` | 222 | `40748997767361727/716803427892952381824` | `5.6848218328e-5` |

Every exact sequence `min_s h_m(s)` is nondecreasing in `m`, as it must be.

The worst generated-shield state is strikingly stable across `D=150,167,178,187,197`:

```text
(0,0,0,0,0,0,2,0,0,2,2,2,2,2)
```

while the two guard stages share the worst base descriptor

```text
(0,2,0,0,0,2,1,0,0,0,0,1,0,0).
```

This persistence suggests that the next full-corridor Bellman problem may admit a small extremal boundary family rather than requiring all descriptors at every frontier level.

## 6. How large is the synchronization loss?

For comparison only, I reconstructed the existing separately timed eight-arrival endpoint factor at each of the same stages, with its certified `lambda=2` and `e^{-2}>(32/87)^2` bound.

The ratio

\[
\frac{q_j}{p_j^{\rm fixed}}
\]

lies between `3.6966` and `3.7372` at every one of the eight stages. Multiplying these eight ratios gives

\[
\boxed{
\prod_j\frac{q_j}{p_j^{\rm fixed}}
\approx 36019.92590443762,
}
\]

or about **4.5565 decimal orders**.

The exact product of the stopping-frontier probabilities is

\[
\prod_j q_j\approx1.2450710765623625\times10^{-33},
\]

whereas the product of the corresponding fixed-window factors is approximately

\[
3.4566175395962456\times10^{-38}.
\]

This comparison is a route diagnostic, **not** a `B_cat` improvement: the `q_j` events finish at random stopping times, while the frozen block metric requires a source-valid finite block event whose child seed is available at the block top.

## 7. A rigorous deterministic-time hitting theorem — but still not a block-top theorem

The stopping formulation does give one clean finite-time theorem.

By the strong Markov property and the worst-entrance minimizations above, the probability that all eight post-bootstrap stages succeed sequentially is at least

\[
Q:=\prod_jq_j.
\]

On this event, stage `j` uses at most eight protected arrivals. Its protected arrival rate is `D_j/4`. Conditional on the mark identities/reaction races that make the stage successful, the exponential interarrival times remain independent of those identities. Hence the conditional expected traversal time satisfies

\[
\mathbf E[T_{\rm trav}\mid\text{successful mark history}]
\le\sum_j\frac{8}{D_j/4}
=\sum_j\frac{32}{D_j}
\]

\[
=\boxed{
\frac{15184435759212032}{11096310444002025}
}\approx1.368422038644367.
\]

Markov's inequality therefore gives the source-valid hitting statement

\[
\boxed{
\Pr\left(\text{final guard target is hit by }T_*\right)
\ge \frac12Q,
}
\]

with

\[
T_*=2\sum_j\frac{32}{D_j}
\approx2.736844077288734.
\tag{7.1}
\]

This is genuinely finite-time and universal over the certified entrance classes. But it says the final guard target is **hit by** `T_*`; it does not say the completed child seed is still present **at exactly** `T_*`.

That distinction is precisely why I do not move the metric.

## 8. The exact blocker now exposed

The route has moved from an amorphous probability gap to one sharp theorem-sized obligation:

\[
\boxed{
\text{convert the monotone stopping-frontier traversal into one deterministic-top two-child Harris event without paying back the stagewise synchronization loss.}
}
\tag{8.1}
\]

The naive repair—after reaching the final target, forbid every relevant mark until a deterministic top time—can be exponentially expensive and would throw away the gain just found. Likewise, simply declaring the target absorbing in the calculation would not represent the source process.

A legitimate next proof must do one of two things:

1. build a **single fixed-horizon progress-state automaton** whose state contains `(frontier stage, local descriptor)` and whose last stage is evaluated at the deterministic horizon, so early stage successes automatically donate their unused time to later stages; or
2. prove a stopping-time block comparison in which children born at controlled random times still dominate a supercritical oriented process while retaining the required spatial dependence bounds.

The first route is finite and auditable and is now preferred.

## 9. What the three methods did

**B1 CHANGE THE CATEGORY — succeeded.** The repeated fixed-window product was recast as a killed Markov-renewal/frontier process. This removes the artificial requirement that every intermediate vacancy target survive until a separately prescribed micro-window endpoint.

**B13 FIND WHAT ONLY INCREASES — succeeded.** The correct monovariant is the corridor frontier stage `J_t`, not a species count. Under the good-event dynamics it only advances, and the next-stage boundary can remain adversarial because the local theorem is boundary-uniform.

**B30 ONE SCALE / ONE DIRECTION AT A TIME — succeeded as a route theorem.** All eight post-bootstrap clearing stages were solved exactly at the `m<=8` stopping level. The result quantifies a ~`3.7x` stagewise synchronization loss and isolates the deterministic-top gluing problem. It does **not** by itself move the frozen metric.

## 10. Exact artifacts and validation status

Idea-before-code note:

- `artifacts/R08/20260919T1130Z_e0011_stopping_frontier_idea.md`

Exact reproduction checker and archived output:

- `artifacts/R08/20260919T1130Z_e0011_stopping_frontier_check.py`
- `artifacts/R08/20260919T1130Z_e0011_stopping_frontier_check.out`

The exact calculation was executed in-session with `Fraction` arithmetic; the repository checker reproduces the same finite enumeration/recurrences and asserts the archived rational values. The output records `PASS exact R08/E0011 stopping-frontier local theorem`.

These are **self-checks**, not independent OTHER-track audits. No closure or audit credit is claimed.

## 11. Status and next methods

The frozen metric does not move:

\[
\boxed{B_{\rm cat}\ge b_{19,\rm full}}
\]

before and after this run, so the supported unchanged count is `1`.

The source remains **PARTIAL / OPEN_CURRENT_BOUNDED**. The new work is not a coexistence proof.

The next nonrepeating methods should be **B8 / B11 / B25**:

- **B8 DISCRETIZE:** build the finite progress-state automaton `(stage, descriptor)` for the whole post-bootstrap corridor at one deterministic global horizon; use a common uniformization clock and stage-dependent null moves so unused time from early successes flows to later stages.
- **B11 DUALIZE:** solve the corresponding backward Dirichlet/Bellman recursion from the deterministic block top rather than multiplying forward stage probabilities.
- **B25 COUNT THE SAME THING TWICE:** independently verify the global value by a forward decomposition over first-hitting stage-transition times. Agreement of backward and forward counts is the audit target for the finite core.

If the fixed metric then remains unchanged for two more consecutive runs, the Section-I stuck protocol triggers on the third unchanged run.

## 12. Model / scheduler-control status

The exposed scheduler/update surface still provides prompt/title/schedule-or-start-offset/enabled/timing controls but **no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model/effort telemetry**. Therefore `GPT-6 / maximum` remains prompt-only here and cannot honestly be claimed.

The current root ledger records that the historical P26 `You cannot modify this task` failure was context-specific and that a later full P26 update succeeded from an authorized P/C context. For any task that still rejects modification, the legitimate routes remain its authorized owning context, a supported ownership/admin transfer, or platform support. No scheduler modification was attempted.

## 13. Structured ledger delta

```yaml
ledger_delta:
  worker: R08
  lane: CLOSABLE_OUTSIDE
  predecessor: I0082
  predecessor_state: RETIRED_FROZEN
  predecessor_metric: 2/3
  predecessor_retirement_count: 6
  target: E0011
  source: Durrett_2009_no_stirring_catalyst_ZGB_problem_5
  owner: R08
  metric: B_cat
  before: ">= b19_full; log10 ~= -49.86198560335649"
  after: ">= b19_full; log10 ~= -49.86198560335649"
  movement: NO
  unchanged_count_before: 0
  unchanged_count_after: 1
  status: PARTIAL
  methods: [1,13,30]
  exact_new_fact: "for the 8 post-bootstrap clearing stages, exact worst-entrance first-hit-before-cemetery probabilities within 8 protected arrivals are certified; their product is about 1.24507107656e-33"
  deterministic_time_hitting_fact: "conditional expected successful traversal time <= 15184435759212032/11096310444002025, hence final guard target is hit by twice this time with probability >= (1/2)*product(q_j)"
  metric_blocker: "child availability at a deterministic block top, not mere hitting by a deadline"
  diagnostic_stagewise_gain_vs_old_fixed_windows: 36019.92590443762
  artifacts:
    - artifacts/R08/20260919T1130Z_e0011_stopping_frontier_idea.md
    - artifacts/R08/20260919T1130Z_e0011_stopping_frontier_check.py
    - artifacts/R08/20260919T1130Z_e0011_stopping_frontier_check.out
  self_checks_only: true
  independent_audits_new: 0
  shared_root_modified: false
  next_methods: [8,11,25]
```
