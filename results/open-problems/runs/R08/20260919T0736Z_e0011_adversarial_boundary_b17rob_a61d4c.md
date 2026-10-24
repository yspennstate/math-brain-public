Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC CORRECTION + VALID MOVEMENT: the `b15`/`b16` frozen-halo terminal certificates are withdrawn after B27 exposed an unmodeled exterior-refresh gap; the last sound baseline is `B_cat >= b14`, and this run proves a new robust certificate `B_cat >= b17_rob > b14`, with exact terminal-factor gain `8279751605510032251054812913415540632217010391970559606517 / 6103178097198250600945438022675389091881789947904000000000 > 1` (about `1.3566295254125007`), so `log10(b17_rob) ~= -50.098821717670035`. Unchanged count is `0` relative to the corrected sound baseline. Methods actually used: #11 DUALIZE; #19 MAKE IT AN ALGORITHM; #27 SWAP THE QUANTIFIERS.**

# R08 CLOSABLE OUTSIDE — adversarial-boundary Bellman certificate and correction of the frozen-halo route

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Active target: **E0011**, Rick Durrett, *Coexistence in stochastic spatial models* (2009), Problem 5, original two-dimensional no-stirring catalyst/ZGB process.  
Status after this run: **PARTIAL / OPEN_CURRENT_BOUNDED**.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, source status, and ownership

I continued from

`runs/R08/20260919T0628Z_e0011_unique_top_halo_47c2a1.md`

rather than restarting the stale native task title. The current exclusive claim is `operations/claims/E0011.md`. The predecessor Hasebe--Ueda Problem 3.11 / I0082 remains **RETIRED/FROZEN at `2/3` after six supported unchanged runs** and is not reopened. The old R08 FPP strict-convexity route remains retired from this slot.

At run start I refreshed the controlling repository state: campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the E0011/I0082 claim files, the newest own report/artifacts, and neighboring-track status. E0011 remains exclusively owned by R08.

I also repeated a bounded current-literature search on 2026-09-19 for Durrett's catalyst/ZGB Problem 5, coexistence without stirring, and recent 2025--2026 ZGB variants. Durrett's 2009 source remains the source statement. The search recovered recent modified ZGB work, including a 2025 CO-desorption critical-line paper, but no later primary theorem settling the exact original no-stirring source problem. This is **bounded negative evidence only**, not a worldwide-open or novelty certificate.

## 2. B27 found a real flaw in the two preceding metric increments

The previous `b15` and `b16` terminal DPs enlarged the state patch beyond the certified 14-cell terminal core and then propagated those halo coordinates as ordinary Markov-state coordinates across several accepted arrivals. That silently assumes those halo cells cannot be changed by Harris clocks outside the block's owned family.

That assumption is false.

Let `C` be the old 14-cell full-support core used by the sound `b14` terminal event. One of the later halo cells is `(0,-2)`. The CO clock rooted at

`(0,-3)`

is outside the old owned terminal family, its support is

`{(-1,-3),(0,-4),(0,-3),(0,-2),(1,-3)}`,

and this support is disjoint from `C` but contains `(0,-2)`. Thus, for example, if the halo cell `(0,-2)` contains oxygen, an exterior CO arrival at `(0,-3)` can react with it and change that halo coordinate while leaving every core coordinate untouched. The exact geometry checker records this witness.

Therefore a finite-state recursion that freezes the halo between accepted owned arrivals is **not** a universal-exterior lower bound unless it explicitly includes or adversarializes such exterior updates. This affects the `b15` and `b16` increments. I withdraw them as certified values of the frozen metric. This is a proof correction, not a new obstruction to Durrett's source problem.

The last sound metric checkpoint is consequently the `b14` certificate from

`runs/R08/20260919T0428Z_e0011_full10_terminal_dual_9c41e2.md`,

with

`log10(b14) ~= -50.23128298239976`.

That `b14` event uses only the 14-cell core whose full reaction support is protected by the already-owned Harris family, so the boundary-refresh gap does not apply to it.

## 3. B11 — dualize the exterior into an adversarial Bellman operator

Instead of trying to freeze more boundary state, I allow the exterior to be maximally hostile.

Let `C` be the 14-cell core and add the four halo coordinates

`H = {(0,-2),(0,3),(1,2),(2,1)}`.

On `C` the maximal support-closed accepted alphabet has the old ten labels. On `C union H` there are exactly seven additional support-closed labels:

- `CO(0,-1)`,
- `O2[(0,-1),(0,0)]`,
- `CO(1,1)`,
- `O2[(0,1),(1,1)]`,
- `O2[(1,0),(1,1)]`,
- `CO(0,2)`,
- `O2[(0,1),(0,2)]`.

Every one of these seven **clock identities was already in the old owned Harris family**. Hence accepting them adds no clock to the probability denominator and no clock to the dependency sigma-field:

`D_owned = 214`,

and translated distance-two `L=8` blocks still share exactly zero CO clocks and zero O2 edge clocks.

The halo coordinates themselves are *not* assumed frozen. For a core state `s`, let `B(s)` be the set of all assignments to the four halo cells that make `C union H` locally stable. The exterior is allowed to choose a fresh element of `B(s)` adversarially before every accepted arrival. This is stronger than the actual outside dynamics, so a lower bound that survives this game is automatically uniform over every legal exterior trajectory.

Let `V_0(s)` be the indicator of the six-vacancy terminal target. For `n>=1`, define

`V_n(s) = T_old V_{n-1}(s) + min_{h in B(s)} T_new,h V_{n-1}(s)`,

where `T_old` sums the exact weighted reaction branches of the ten core labels and `T_new,h` sums the exact weighted branches of the seven halo-dependent labels at halo assignment `h`.

The quantifier order is deliberate:

1. the accepted event and its 17 labels are fixed once and for all;
2. the exterior chooses the halo state adversarially before the random next mark;
3. all random old/new label choices and all instantaneous reaction branches are summed;
4. after projecting back to the core, the exterior may refresh the halo again.

Thus the recursion does **not** use the invalid statement “for each boundary path there exists a good response.” It proves one fixed owned-clock event works with the displayed probability uniformly against every boundary trajectory. Allowing an independent arbitrary stable refresh after every arrival only enlarges the adversary, so the value is conservative.

## 4. B19 — exact robust finite algorithm

The exact C++ Bellman computation reproduces the sound `b14` entrance class:

- 7,255 stable full generated-shield entrance states;
- 1,743 projected core descriptors;
- ten old labels;
- seven halo-dependent labels;
- 81 possible halo assignments examined at every robust minimization.

For `n=0,...,8` accepted arrivals, the coordinatewise minima are

```text
0,
0,
4320,
6791040,
5415941232,
4437740167488,
3745233888265728,
3206035806673669632,
2757045203088957499392.
```

At the rational Poisson mean

`lambda = 429/200 = 2.145`,

the worst entrance descriptor is code `4764744`, with exact common-denominator polynomial

`ROBUST_POLY_NUM = 248042286707559887050495146109132661542301362814976`,

`ROBUST_POLY_DEN = 1280827612519734637295397124367921971200000000000000000`.

For the exponential factor I use only rational lower bounds,

`e^{-2} > (32/87)^2`

and the degree-seven alternating Taylor lower bound for `e^{-29/200}`. The resulting exact universal terminal probability is

`p_rob = 11357683958175627230527864078759314996182455956063867773 / 501147979136821382564885299200000000000000000000000000000000`.

Compared with the sound `b14` terminal factor `p14`, exact arithmetic gives

`p_rob/p14 = 8279751605510032251054812913415540632217010391970559606517 / 6103178097198250600945438022675389091881789947904000000000 > 1`,

numerically about `1.3566295254125007`.

Keeping every upstream and planter factor from the already-certified `b14` construction unchanged, define

`b17_rob := b14 * (p_rob/p14)`.

Then

`B_cat >= b17_rob > b14`,

with diagnostic

`log10(b17_rob) ~= -50.098821717670035`.

The new robust certificate is also numerically stronger than the withdrawn `b15` number (`-50.108706...`), although it is slightly below the withdrawn `b16` number (`-50.095735...`). The latter comparison has no metric force because `b16` no longer has a valid universal-exterior proof.

This remains **PARTIAL**. A bound of order `10^-50.10` is still astronomically below the sufficient `63/64` oriented-percolation threshold. No coexistence theorem is claimed.

## 5. What each method contributed

**B11 DUALIZE succeeded.** The uncontrolled exterior was converted from an unmodeled nuisance into a backward lower transition operator / Bellman minimization.

**B19 MAKE IT AN ALGORITHM succeeded.** The min-max recursion is finite and exact, and it sums all 17 accepted clocks through eight arrivals rather than one hand-picked word.

**B27 SWAP THE QUANTIFIERS succeeded twice.** First, it exposed why `b15`/`b16` were not universal: they propagated a particular halo trajectory. Second, it forced the corrected order “fixed event, then worst legal boundary state, then random mark/reaction,” which yields the robust certificate above.

## 6. Exact self-checks

The run began with an idea-before-code note:

`artifacts/R08/20260919T0736Z_e0011_two_cell_owned_halo_idea.md`.

That note records the initial narrower first-new-mark route; during the run the quantifier audit exposed the halo-refresh issue and the final construction was strengthened to the full adversarial Bellman recursion above.

Executed exact Bellman checker/output:

`artifacts/R08/20260919T0736Z_e0011_robust_boundary_dp.cpp`  
`artifacts/R08/20260919T0736Z_e0011_robust_boundary_dp.out`

Independent geometry/support/arithmetic checker/output:

`artifacts/R08/20260919T0736Z_e0011_robust_boundary_geometry.py`  
`artifacts/R08/20260919T0736Z_e0011_robust_boundary_geometry.out`

Both outputs report `PASS`. These are **self-checks**, not independent OTHER-track audits, and no audit credit is claimed.

## 7. Next nonrepeating route

Next methods are **B2 / B10 / B21**.

- **B2 ATTACK THE NEGATION FIRST:** try to build an exact adversarial core/halo cycle proving a nontrivial upper bound on every event that keeps the current `D=214`, `L=8`, six-vacancy terminal architecture. If such a cap is tiny, stop optimizing this architecture.
- **B10 DERANDOMIZE:** extract a compact deterministic robust policy/language from the Bellman value function that retains a large fraction of the robust mass and can be inspected/proved symbolically.
- **B21 ASK WHO ELSE HAS THIS SHAPE:** port finite lower-transition-operator / imprecise-Markov-chain machinery to compute an infinite-horizon robust hitting probability, rather than truncating at eight arrivals. A certified infinite-horizon value is the first route here that could change the scale rather than another constant.

## 8. Model / scheduler-control status

The model-control limitation is still real. The exposed scheduler update surface has fields for title/prompt, schedule or start offset, enabled state, and timing mode, but **no binding model-family field and no reasoning-effort field**. It also provides no authenticated completed-run model/effort attestation. Therefore GPT-6/maximum remains prompt text only; this worker actually ran GPT-5.6 Sol with reasoning level UNVERIFIED.

The current repository ledger adds an important correction to the older P26 story: P26's full prompt update later **succeeded from an authorized context**, while a different context had previously returned `You cannot modify this task`. Thus that denial is context/authorization-specific, not a permanent P26-wide failure. If a task still rejects modification in the current context, the legitimate routes are its authorized owning context, supported ownership/admin transfer, or platform support. A repository edit is not a scheduler workaround. No scheduler change was attempted this run.

## 9. Structured ledger delta

```yaml
ledger_delta:
  track: R08
  lane: CLOSABLE_OUTSIDE
  active_claim: E0011
  source: "Durrett 2009 Problem 5 — original no-stirring catalyst/ZGB coexistence"
  predecessor_I0082: RETIRED_FROZEN_2_of_3
  metric_name: B_cat
  previous_reported: ">= b16; log10 ~= -50.095734758579326"
  correction: "withdraw b15 and b16 as certified metric increments; frozen-halo DP omitted exterior refreshes of halo coordinates"
  sound_before: ">= b14; log10 ~= -50.23128298239976"
  sound_after: ">= b17_rob; log10 ~= -50.098821717670035"
  movement: "YES relative to corrected sound baseline; exact terminal factor gain ~= 1.3566295254125007"
  unchanged_count_after: 0
  status: PARTIAL
  exact_new_fact: "adversarial-refresh Bellman recursion on a 14-cell core plus four halo cells gives a universal terminal lower bound while retaining D=214 and zero distance-two shared clocks"
  correction_witness: "outside CO(0,-3) can alter halo (0,-2) without touching the core, invalidating frozen-halo propagation"
  artifacts:
    - "artifacts/R08/20260919T0736Z_e0011_two_cell_owned_halo_idea.md"
    - "artifacts/R08/20260919T0736Z_e0011_robust_boundary_dp.cpp"
    - "artifacts/R08/20260919T0736Z_e0011_robust_boundary_dp.out"
    - "artifacts/R08/20260919T0736Z_e0011_robust_boundary_geometry.py"
    - "artifacts/R08/20260919T0736Z_e0011_robust_boundary_geometry.out"
  self_check_only: true
  independent_audits_new: 0
  shared_root_modified: false
  next_methods: [2, 10, 21]
```
