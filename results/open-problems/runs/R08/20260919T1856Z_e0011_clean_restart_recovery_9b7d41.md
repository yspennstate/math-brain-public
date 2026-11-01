Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `B_cat >= b21_desc -> B_cat >= b21_desc`, diagnostic `log10(b21_desc) ~= -48.42893853604687`; supported unchanged count `4 -> 5`. Methods actually used: B2, B8, B20.**

# R08 CLOSABLE OUTSIDE — E0011 recovery after stuck episode 1: exact clean-manifold restart failure and full-state explosion

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Active source target: **E0011**, Rick Durrett, *Coexistence in stochastic spatial models*, Ann. Appl. Probab. 19 (2009), Problem 5, original two-dimensional no-stirring catalyst/ZGB process.  
Status after this run: **PARTIAL / source OPEN under bounded current-literature checking**.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

This run executes the single recovery selected by the preceding mandatory Section-I stuck report: reduce the width-ten restart obstruction to a finite computation and run it. It does not return to another rare-word optimization.

## 1. Continuity, source, ownership, and exclusions

I continued from

`runs/R08/20260919T1726Z_e0011_stuck1_restart_mdp_6f2c91.md`

rather than restarting from the stale native title. The later controlling file `operations/claims/E0011.md` still assigns E0011 exclusively to R08 and explicitly records Hasebe--Ueda Problem 3.11 / `I0082` as **RETIRED/FROZEN at `2/3` after six supported unchanged runs**. I0082 was not reopened and its excluded finite-variance theorem was not reproved.

Before research I refreshed or recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the E0011 ownership file, the newest own report and artifacts, and the newest neighboring R07/R09 lifecycle state. R07 is already at a successor gate after its own retirement boundary and R09 remains at a successor/admission gate; neither owns E0011. The large intake collection was checked through the active exact-ID/source/ownership trail rather than falsely claiming a visual reread of every unrelated JSONL row.

A fresh bounded literature search on **2026-09-19** again recovered Durrett's source `arXiv:0906.2293`, which advertises nine challenging open problems, and no later primary theorem proving coexistence for the exact original no-stirring model. Recent material recovered included the 2025 numerical finite-time ZGB study and the 18 August 2026 *Physical Review E* paper adding reactive sulfur; those are not source-matching no-stirring coexistence theorems. This remains bounded negative evidence only, not a worldwide-open or novelty certificate.

## 2. Frozen metric

The stable track metric remains

\[
B_{\rm cat}:=\sup_C b(C),
\]

where `C` ranges over complete source-valid finite protected two-child Harris-block certificates at `p=1/2`, with deterministic seed reproduction and a translated 1-dependent good-block field.

Entering and leaving this run,

\[
\boxed{B_{\rm cat}\ge b_{21,\rm desc}},
\qquad
\log_{10}b_{21,\rm desc}\approx -48.42893853604687.
\]

The finite computation below is a **fixed all-CO boundary, one-child deformation**, not a universal-exterior two-child certificate, so it does not move `B_cat`. The supported unchanged count therefore goes from `4` to `5`.

## 3. B2 — attack the proposed restart class from the negative side

The preceding run identified the simplest recovery object: the width-ten oriented fuel seed under a fixed hostile all-CO exterior, with all owned internal clocks allowed.

The finite protected patch used here consists of:

- two vacant rows `y=0,1`, `x=0,...,9`;
- a first CO fuel rail `y=2`;
- a second CO rail `y=3`;
- four lateral vacant guards `(-1,1),(10,1),(-1,2),(10,2)`;
- every site outside the 44 dynamic cells frozen to CO for this deformation.

At the source anchor `p=1/2`, site-CO clocks have rate `1/2` and internal vacant-vacant `O_2` edge clocks have rate `1/4`.

I deliberately attacked the most natural **pure-vacancy fuel-subset restart class** first. A clean state is indexed by

\[
A\subseteq\{0,\dots,9\},
\]

where `x in A` means that the first-rail CO at `(x,2)` has already been consumed. The two original strip rows and all four guards must still be vacant, the second rail must still be all CO, and no O defect is allowed. Thus there are exactly `2^10=1024` clean states.

A full legal internal adsorption event is then classified exactly:

- if the resulting 44-cell state is another clean state `A'`, it is a clean progress/backtrack transition;
- if it is exactly the same clean state, it is RETRY;
- otherwise it is FATAL for this candidate restart class;
- `A={0,...,9}` is SUCCESS, because the one-row translated two-vacant-row seed has been produced while the second rail is intact.

This is not an upper bound on the true full-state success probability: a trajectory that leaves the clean manifold might later repair itself. It is an exact decision of this **specific** restart architecture.

## 4. B8 — exact 1024-state full-event kernel and certified hitting interval

The checker does **not** use a hand-written reduced transition table. For every one of the 1024 clean masks it reconstructs the literal 44-cell configuration and enumerates every effective internal CO adsorption and every effective internal `O_2` adsorption, including the exact uniform reaction-choice branches. The exterior is represented as fixed CO only when a newly adsorbed O chooses a neighbor outside the protected patch.

For each mask, a separate total-rate identity checks

\[
\sum_{\text{all one-event outcomes}} r
=
\frac12\,N_{\rm vac}
+
\frac14\,E_{\rm vv}.
\]

All **1024** states pass this exact rational check.

At the initial seed the exact rate decomposition is

\[
\boxed{r_{\rm retry}=\frac{31}{12}},
\qquad
\boxed{r_{\rm progress}=\frac{65}{12}},
\qquad
\boxed{r_{\rm fatal}=12},
\qquad
r_{\rm total}=20.
\]

The hitting probability `h(A)` of SUCCESS before FATAL satisfies, after cancelling literal RETRY self-loops,

\[
h(A)=
\frac{\sum_{B\ne A}r(A,B)h(B)}
{r_{\rm fatal}(A)+\sum_{B\ne A}r(A,B)},
\qquad
h(\{0,\dots,9\})=1.
\]

Every nonterminal clean state has positive fatal rate. The checker scales each exact rational row to integers and runs two monotone fixed-grid iterations at scale `10^15`: floor updates from zero are certified lower bounds and ceiling updates from one are certified upper bounds. After 24 iterations every state has interval width at most `2/10^15`.

For the initial seed,

\[
\boxed{
1.65919246\times10^{-7}
\le h(\varnothing)
\le
1.65919248\times10^{-7}
}.
\]

In particular the exact integer comparisons certify

\[
\boxed{h(\varnothing)<\frac1{6,000,000}}
\]

and, because this clean trial eventually ends in SUCCESS or FATAL,

\[
\boxed{
\frac{h(\varnothing)}{1-h(\varnothing)}
<\frac1{6,000,000}.
}
\]

The restart criterion sought in the stuck report needs a success/fatal ratio **greater than `63`**. Therefore this pure-vacancy fuel-subset restart class misses the required ratio by a factor exceeding

\[
63\cdot 6,000,000=378,000,000.
\]

This is a decisive negative result for the clean candidate class. The five-edge fuel mechanism itself was not the main issue; ordinary CO defects and O-defect excursions must be admitted and repaired by any viable restart class.

## 5. B20 — why the literal full-state algorithm fails

The natural response is to stop declaring defect excursions fatal and solve the entire fixed-boundary 44-cell process. I therefore ran a separate exact **reachability-only** expansion of the literal state graph, allowing every cell to be vacant/CO/O and every reaction choice.

The number of distinct states reachable after exactly `d` effective transitions is

\[
\begin{array}{c|rrrrrr}
d&0&1&2&3&4&5\\ \hline
N_d&1&44&1006&15488&178361&1626099.
\end{array}
\]

Thus a naive full-state Bellmanization already exceeds **1.6 million distinct states at depth five**, before the minimum five-event clean translation scale has had time to develop arbitrary repairs. This does not prove that exact full-state computation is impossible; it identifies why the obvious flat representation is the wrong algorithm.

The combination of the two computations is more useful than either alone:

1. the 1024-state clean manifold is far too brittle (`<1/6,000,000` success/fatal ratio);
2. the unrestricted flat state space explodes immediately (`1,626,099` states by depth five).

So the next object must sit between them: it must admit a controlled number of defects while exploiting one-dimensional strip locality rather than tracking every 44-cell configuration flatly.

## 6. What changed mathematically

No source-level metric changed, but the restart program is substantially narrower than before.

The preceding stuck report left open the possibility that the width-ten fuel strip might already be almost self-renewing once ordinary marks were accepted. The exact calculation rules that out for the most natural pure-vacancy restart manifold by more than eight orders of magnitude relative to the required ratio. The exact reachability count also rules out a naive brute-force response as the obvious next computation.

The missing states are now identified concretely: **repairable CO/O defects near the strip/fuel interface**. A viable finite class must absorb a small number of those excursions without opening the full `3^44` state space.

## 7. Next route and retirement boundary

The next nonrepeating method triple is **B5 / B18 / B30**.

- **B5 — add a parameter:** introduce a defect budget `k=0,1,2,...`, with the present clean manifold equal to `k=0`, and compute how the success/fatal ratio changes with `k`. The first target is the exact `k=1` class.
- **B18 — say it in another language:** encode the four-row protected strip as a one-dimensional chain of width-ten column states and use a frontier/transfer representation rather than a flat 44-cell state hash.
- **B30 — one scale/direction at a time:** localize a repair excursion to one column or one adjacent column pair and determine exactly which defect types must be retained to glue neighboring local repairs.

The closable-target unchanged count is now `5`. Under the controlling six-unchanged-run rule, **if the next invocation does not improve the frozen source metric, E0011 must be retired with an immutable handoff and R08 must rotate to the next fully admitted, unowned CLOSABLE OUTSIDE target.** A new local theorem alone will not reset that count.

## 8. Exact artifacts and self-check status

Idea-before-code note:

- `artifacts/R08/20260919T1856Z_e0011_restart_clean_manifold_idea.md`

Exact clean-manifold checker and archived output:

- `artifacts/R08/20260919T1856Z_e0011_clean_restart_exact_check.py`
- `artifacts/R08/20260919T1856Z_e0011_clean_restart_exact_check.out`

Literal full-state reachability checker and archived output:

- `artifacts/R08/20260919T1856Z_e0011_full_state_growth_check.cpp`
- `artifacts/R08/20260919T1856Z_e0011_full_state_growth_check.out`

Both archived outputs end in `PASS`. These are **R08 self-checks only**. No independent OTHER-track audit credit is claimed.

## 9. Model / scheduler control status

The actual run model visible here is GPT-5.6 Sol; reasoning level is not authenticated and is therefore reported as **UNVERIFIED**. The exposed scheduler interface still offers title/prompt, schedule or start-offset, enabled state, and timing mode, but **no binding model-family selector, no reasoning-effort selector, no guaranteed execution-duration control, and no authenticated completed-run model telemetry**. Therefore GPT-6/maximum remains prompt text only and cannot be truthfully claimed as the actual runtime.

The historical P26 `You cannot modify this task` denial remains a task-ownership/context issue. The supported workarounds remain: modify from the authorized owning context, use a supported ownership/admin transfer if the product exposes one, or escalate to platform support. A repository edit is not a scheduler-permission workaround. No scheduler change was attempted in this run.

```yaml
ledger_delta:
  worker: R08
  allocation: CLOSABLE_OUTSIDE
  active_target: E0011_Durrett_Problem_5_no_stirring_catalyst
  predecessor_I0082: RETIRED_FROZEN_2_of_3
  metric_name: B_cat
  metric_before: ">= b21_desc; log10 ~= -48.42893853604687"
  metric_after: ">= b21_desc; log10 ~= -48.42893853604687"
  metric_movement: false
  supported_unchanged_count_before: 4
  supported_unchanged_count_after: 5
  status: PARTIAL
  methods_actual: [B2, B8, B20]
  recovery_from_stuck_episode: 1
  new_exact_result: "pure-vacancy width-10 fixed-all-CO restart success in [1.65919246e-7,1.65919248e-7], hence success/fatal < 1/6000000"
  full_state_growth_depth5: 1626099
  next_methods: [B5, B18, B30]
  retirement_if_next_no_movement: true
  source_current_search_date: 2026-09-19
  source_resolution_found_in_bounded_search: false
  self_checks_only: true
```
