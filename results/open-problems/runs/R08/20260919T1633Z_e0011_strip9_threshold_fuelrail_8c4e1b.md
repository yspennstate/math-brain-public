Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `B_cat >= b21_desc -> B_cat >= b21_desc`, diagnostic `log10(b21_desc) ~= -48.42893853604687`; unchanged count `2 -> 3`. Methods actually used: B3, B15, B19.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: sharp thin-strip nucleation threshold and oriented fuel-rail transport

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Active source target: **E0011**, Rick Durrett, *Coexistence in stochastic spatial models*, Ann. Appl. Probab. 19 (2009), Problem 5, original two-dimensional no-stirring catalyst/ZGB process.  
Status after this run: **PARTIAL / source OPEN under bounded current-literature checking**.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, and source gate

I continued from the newest complete R08 report

`runs/R08/20260919T1530Z_e0011_seed15_strip_stationarity_6d2a4f.md`

and did not restart from the native task title. The later controlling ownership file is `operations/claims/E0011.md`; it assigns E0011 exclusively to R08 and explicitly records the predecessor Hasebe--Ueda Problem 3.11 / `I0082` as **RETIRED/FROZEN at `2/3` after six supported unchanged runs**. I0082 was therefore not reopened, its finite-variance exclusion was not reproved, and the old R08 FPP strict-convexity route remains retired from this slot.

Before research I refreshed/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the controlling E0011 claim, the newest complete own report and artifacts, and the latest visible R07/R09 lifecycle state. R07 is at an unrelated successor gate and R09 at an unrelated empty successor gate; neither owns E0011. Large intake ledgers are not represented here as though every unrelated row were visually reread; exact-ID/source and ownership searches were used for the active target.

## 2. Dated literature refresh

The bounded current-literature check was refreshed on **2026-09-19** using the exact Durrett source title/Problem 5/catalyst/ZGB/no-stirring terms and recent ZGB terms.

- Durrett's source remains arXiv:0906.2293 / Ann. Appl. Probab. 19 (2009), whose abstract says that the paper states nine challenging and important open problems.
- The fresh search recovered no later primary theorem matching the exact original two-dimensional no-stirring Problem 5 target.
- A current primary ZGB result located in the search, de Andrade--Girardi, *Phys. Rev. E* **114**, 024136, published **18 August 2026**, explicitly studies an **extension with reactive sulfur**, hence is not a closure of the source model.

This is **bounded negative evidence only**. It is not a claim of exhaustive worldwide openness or novelty.

## 3. Entering frozen metric

The source metric remains

\[
B_{\rm cat}:=\sup_C b(C),
\]

over complete source-valid finite protected two-child Harris-block certificates at `p=1/2`, with a deterministic reproduction implication and finite-range dependence.

The entering certified bound is

\[
\boxed{B_{\rm cat}\ge b_{21,\rm desc}},
\qquad
\log_{10} b_{21,\rm desc}\approx -48.42893853604687.
\]

The previous run prescribed B3/B15/B19. This run used those three methods and did not spend the run tuning the old rare-cylinder coefficient.

## 4. B3 — a sharp closed thin-strip nucleation theorem

The preceding run identified `2 x 8` as the first small rectangle that simultaneously passes the single direct all-CO poisoning filter and has positive initial vacancy drift. That criterion is not strong enough. I replaced it by the following exact local question:

> Starting from an all-vacant **closed** `2 x w` patch at `p=1/2`, what is the probability of reaching a stable mixed CO/O configuration before either monochromatic poison state?

Before the first mixed state, every resolved configuration is necessarily one of: empty, CO-only, or O-only. Thus the pre-mixing chain has only

\[
1+2(2^{2w}-2)
\]

transient pure states. CO adsorption has relative jump weight `2` and O2 adsorption on a vacant nearest-neighbour edge has relative jump weight `1`. Instantaneous reaction choices have denominators cleared by the exact branch scale `144`.

The finite Bellman recursion was evaluated with integer arithmetic on a `10^{-9}` grid, with **every average rounded downward**. Hence every printed target probability is a rigorous lower bound.

For every width `w<=8`, the probability of reaching a monochromatic poison state **before any mixed state**, within 19 effective adsorptions, is already larger than `1/64`:

| `w` | certified lower bound for poison by 19 |
|---:|---:|
| 1 | 0.800000000 |
| 2 | 0.789985922 |
| 3 | 0.381708863 |
| 4 | 0.203955182 |
| 5 | 0.115457177 |
| 6 | 0.065557698 |
| 7 | 0.034290948 |
| 8 | **0.019651084** |

Since `0.019651084 > 1/64 = 0.015625`, for each `w<=8`

\[
\Pr(\hbox{mixed before poison})
\le 1-\Pr(\hbox{poison by 19 before mixed})
<\frac{63}{64}.
\]

For width nine, the opposite threshold is certified:

\[
\boxed{
\Pr_{2\times9}
(\hbox{mixed before poison by 35 effective adsorptions})
\ge 0.984454108
>
\frac{63}{64}=0.984375.
}
\]

Therefore:

### Sharp local thin-strip threshold

\[
\boxed{
 w=9
\text{ is the minimal width among closed }2\times w\text{ vacant strips for which the mixed-before-poison probability can exceed }63/64.
}
\]

The same exact recursion gives the useful even-width value

\[
\boxed{
\Pr_{2\times10}
(\hbox{mixed before poison by 19 effective adsorptions})
\ge0.985092878>63/64.
}
\]

For comparison the width-eight mixed-by-35 lower bound is only `0.974533587`.

This is a substantial finite architecture theorem. It **does not** move `B_cat`, because a closed local patch is not yet a source-valid two-child block against arbitrary exterior histories.

## 5. B15 — break symmetry on purpose: an oriented CO fuel rail

The new local threshold suggests width `9`; for transport, width `10` is the first even width at or above it and admits a simple deterministic decomposition into five disjoint pairs.

Use coordinates `x=0,...,9`. Start with vacant rows `y=0,1`, vacant lateral guards `(-1,1),(10,1),(-1,2),(10,2)`, a consumable CO rail on `y=2`, and a second CO rail on `y=3`. Consider the five disjoint horizontal edges in the current top vacant row

\[
(0,1)-(1,1),\ (2,1)-(3,1),\ldots,(8,1)-(9,1).
\]

If O2 adsorbs on any one of these designated edges while the other designated events have occurred in an arbitrary subset, each incoming O has **exactly one CO neighbour**, the site directly above it on `y=2`. Instantaneous reaction therefore removes those two rail CO particles and restores the two adsorption sites to vacancies.

After all five events have occurred, in **any of the `5!=120` orders**, the entire first CO rail has been converted to vacancies, the old top vacant row remains vacant, the lateral guards remain vacant, and the second CO rail is untouched. Hence the same width-ten two-row vacant strip has translated upward by one lattice row and again has a CO fuel rail immediately above it.

The exact finite permutation checker verifies all 120 orders. Consequently a finite vertical stack of CO rails gives a deterministic oriented vacancy-transport algorithm. This deliberately reverses the old viewpoint: an all-CO region can be **fuel** for propagation rather than only an adversarial poisoning environment.

This is still not a high-probability block certificate. Killing every non-designated mark would make the clean five-event word too rare. The value of the lemma is that it identifies the state variables for the next restart/minorization automaton: `(vacancy strip, consumed-fuel subset, pure/mixed status)`, with ordinary legal marks allowed rather than suppressed.

## 6. B19 — exact finite algorithm and self-checks

The production certificate consists of:

- `artifacts/R08/20260919T1633Z_e0011_strip_nucleation_threshold_check.cpp`
- `artifacts/R08/20260919T1633Z_e0011_strip_nucleation_threshold_check.out`
- `artifacts/R08/20260919T1633Z_e0011_fuel_rail_shift_check.py`
- `artifacts/R08/20260919T1633Z_e0011_fuel_rail_shift_check.out`

The C++ output ends in `PASS` for the sharp `w<=8` obstruction and `w=9` threshold. The Python output ends in `PASS` after all 120 fuel-rail event orders. These are **R08 self-checks only** and claim no independent audit credit.

A production idea note was frozen in the repository before the production certificate files:

`artifacts/R08/20260919T1633Z_e0011_strip10_nucleation_translation_idea.md`.

Exploratory scratch calculations informed that note; no claim is made that no exploratory code existed beforehand.

## 7. Why the source metric does not move

The exact local theorem crosses `63/64`, but it is not the frozen metric. What remains missing is a universal exterior, two-child, restartable Harris-block construction. In particular, a source-valid amplification must produce a finite oriented seed class `S` and a stopping rule for which, uniformly over allowable exterior histories and every `s in S`, the attempt decomposes into SUCCESS / FATAL / RETRY with RETRY returning to `S`, SUCCESS producing the two forward seed instances, and the ratio satisfying the earlier restart criterion

\[
\boxed{a>63f.}
\]

A precise blocking formulation for the next stage is:

\[
\boxed{
\inf_{s\in S,\,h\in\mathcal H}
\Pr_{s,h}(\mathrm{SUCCESS})
>
63\,
\sup_{s\in S,\,h\in\mathcal H}
\Pr_{s,h}(\mathrm{FATAL}),
}
\]

with every remaining outcome certified to return to `S`, together with the deterministic two-child implication and the finite-range/1-dependence geometry.

The current closed-strip theorem supplies a plausible local nucleation kernel and the fuel-rail lemma supplies deterministic oriented transport, but neither supplies this universal restart structure. Therefore

\[
\boxed{B_{\rm cat}\ge b_{21,\rm desc}\quad\text{remains unchanged}.}
\]

Status remains **PARTIAL**.

## 8. Stagnation rule now triggers

This is the third consecutive supported no-movement run since `b21_desc`:

`0 -> 1 -> 2 -> 3`.

Therefore, under Section I, the **next R08 run must be a thinking-only stuck report with no new mathematical claims**. It must state the blocking formula above, catalogue the routes already tried and their exact failure modes, name the simplest unproved restart special case, identify the closest literature technique and its missing ingredient here, and choose exactly one allowed recovery action.

The planned nonrepeating Section-B lenses for that mandatory stuck analysis are **B6, B11, B24**: deform to a boundary condition where restart is solvable, dualize the robust restart probability as a lower-transition/Bellman problem, and identify the extremal exterior/fatal state. The recovery choice itself should be made explicitly in that next stuck report after the five required items are written.

## 9. Model / scheduler control status

This run's actual model is GPT-5.6 Sol; the reasoning level is not authenticated by the exposed runtime and is therefore reported as **UNVERIFIED**, not as GPT-6 maximum.

The exposed scheduler control surface still offers prompt/title, schedule or start-offset, enabled state, and timing mode. It exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration control, and no authenticated completed-run model telemetry**. Thus `GPT-6 / maximum` remains prompt text only in this environment.

The repository's current reconciliation records the historical P26 modification failure as context-specific: another authorized context later succeeded in updating P26. If a task still returns `You cannot modify this task`, the supported workaround is its authorized owning context, a supported ownership/admin transfer, or platform support. A repository edit is not a scheduler-permission workaround. No scheduler modification was attempted in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R08
  allocation: CLOSABLE_OUTSIDE
  active_target: E0011_Durrett_Problem_5_no_stirring_catalyst
  predecessor_I0082: RETIRED_FROZEN_2_of_3
  metric_name: B_cat
  metric_before: ">= b21_desc; log10 ~= -48.42893853604687"
  metric_after: ">= b21_desc; log10 ~= -48.42893853604687"
  movement: false
  supported_unchanged_count_before: 2
  supported_unchanged_count_after: 3
  status: PARTIAL
  methods: [B3, B15, B19]
  finite_new_result:
    thin_strip_threshold: "closed 2xw mixed-before-poison threshold is minimal at w=9 for >63/64"
    w8_poison_by_19_lower: 0.019651084
    w9_mixed_by_35_lower: 0.984454108
    w10_mixed_by_19_lower: 0.985092878
    fuel_rail_orders_exactly_checked: 120
  metric_nonmovement_reason: "closed local nucleation and deterministic one-row transport are not yet a universal-exterior two-child 1-dependent block certificate"
  next_run: MANDATORY_SECTION_I_STUCK_THINKING_ONLY
  next_method_lenses: [B6, B11, B24]
  audits_this_run: "self-checks only; no OTHER-track audit credit"
```
