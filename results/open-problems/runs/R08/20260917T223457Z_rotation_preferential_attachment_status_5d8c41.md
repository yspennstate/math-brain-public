Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **ROTATION / ADMISSION RUN: no active successor metric is admitted. I0082 remains RETIRED/FROZEN at `2/3` with retirement count `6`; the fixed F0083 `Xi_*` route remains RETIRED/HANDED OFF at `1/2` after six unchanged runs. This run eliminates I0045, I0046, and I0049 as source questions resolved by later literature, and places I0048 on HOLD as substantially resolved/current-literature-ineligible pending exact matching of its remaining comparison clause. Methods actually used: B22 READ THE FAILURES, B23 DO WHAT THE PROPOSER DID NOT EXPECT, B21 ASK WHO ELSE HAS THIS SHAPE.** GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or completed-run telemetry, so I do not claim otherwise.

# R08 CLOSABLE OUTSIDE — post-F0083 rotation and preferential-attachment successor screen

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Hasebe--Ueda Problem 3.11 / I0082. Its operational state is fixed by the later six-unchanged R08 handoff even though `operations/claims/I0082.md` still contains older active wording: metric `2/3`, retirement count `6`, RETIRED/FROZEN.

I also did **not** continue the fixed F0083 expanding-tube candidate. The immediately preceding immutable report,

`runs/R08/20260917T2130Z_f0083_thin_boundary_uniqueness_handoff_f3c7a1.md`,

proved that the admitted candidate

\[
\Xi_*=\mathbb Z^4\setminus\{(n,a,b,c):1\le a,b,c\le\lfloor(1+|n|)^{3/4}\rfloor\}
\]

has an a.e. unique appetite-one stable Lebesgue allocation. Therefore the frozen second obligation for that exact candidate is impossible, the metric stays `1/2`, and the route is RETIRED/HANDED OFF at the owner-directed six-unchanged CLOSABLE limit. This does **not** refute the Hoffman--Holroyd--Peres existential source question.

Before successor work I recovered the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, both R08 claim files, the newest complete R08 report, the current intake rows under `probability_1000_intake_I_20260914/problems.jsonl`, the newest visible neighboring R09 material, and the latest task-health admission screen. The shared root ledger is stale for later R-series mathematics and is not rewritten by this worker.

The newest task-health admission screen already warned that no `READY + CLOSABLE OUTSIDE + UNASSIGNED` successor had been certified in its bounded pass. I therefore treated the queue as a source list, not as dispatch permission, and checked ownership/current literature before considering any claim.

## 2. Ownership exclusions before literature research

Two superficially attractive queue entries are not available:

- **I0035 / Aldous--Fill Open Problem 14.31** has the canonical claim `operations/claims/I0035.md`, owned by C31. Its status is `PENDING_ADMISSION`, not READY, but the ownership reservation is exclusive and must not be overridden.
- **I0054 / Aldous--Janson Open Problem 18** is actively owned by R11 and has a long current run sequence. It is not reserve inventory.

Repository claim-directory / exact-ID searches found no canonical `operations/claims/I0045.md`, `I0046.md`, `I0048.md`, or `I0049.md` at the captured master state. Search absence alone is not enough for admission, so I next attacked their purported openness.

## 3. B22 + B23 — falsify stale `open_per_source` labels before trying to solve them

The intake records for I0045--I0049 were created by reading the older Saint-Flour / *Random Graphs and Complex Networks* source and were explicitly labeled `open_per_source`; their own verification fields say that **no later-resolution search was run**. That is exactly the kind of queue state that must be attacked before research.

### 3.1 I0045 is KNOWN / RESOLVED

Intake I0045 is van der Hofstad's Open Problem 2.1: extend the local weak-convergence theorem to the preferential-attachment model **with self-loops** `PA_n^(m,delta)`; the old source notes that the `delta=0` case was already known.

Remco van der Hofstad's 2024 *Random Graphs and Complex Networks, Volume 2* now supplies the needed later-author result. In Chapter 5 it proves local convergence in probability to the Pólya point tree for all `delta>-m`, and explicitly states that the theorem is robust to the model variants `PA^(m,delta)(a)` and `PA^(m,delta)(b)`, **including the variant in which self-loops are allowed**, with the same limit. The chapter notes also state that the extension from the older `delta>=0` literature to the full `delta>-m` range is due to the newer Pólya-urn treatment / Garavaglia et al. line of work.

This is stronger than the queued source request. A 2025 paper, Hazra--den Hollander--Parvaneh, *The friendship paradox for sparse random graphs*, independently uses the self-loop preferential-attachment model and cites van der Hofstad's local-convergence theorem for `delta>-1`.

**Disposition:** `I0045 = KNOWN / RESOLVED_IN_LATER_LITERATURE`. No claim created; not an eligible successor.

### 3.2 I0046 is KNOWN / RESOLVED

Intake I0046 is the immediately following source Open Problem 2.2: determine the local weak limit of model `PA_n^(m,delta)(b)` for

\[
-m<\delta<0.
\]

The same 2024 Volume 2 result states local convergence in probability to the Pólya point tree for all `delta>-m`, and the model-robustness discussion explicitly includes the `(b)` model. Thus the precise negative-`delta` gap asked by the old source has been filled.

**Disposition:** `I0046 = KNOWN / RESOLVED_IN_LATER_LITERATURE`. No claim created; not an eligible successor.

### 3.3 I0048 is not safe fresh research inventory

Intake I0048 is van der Hofstad Open Problem 4.3, asking for the percolation phase transition on the fixed-edge preferential-attachment model and whether it agrees with the conditionally-independent-edge analogue. The source discussion also asks whether the graph threshold equals that of the branching-process/local-weak limit, and whether the threshold is zero for `delta in (-m,0)` and positive for `delta>0`.

Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models* (arXiv:2312.14085; Electronic Journal of Probability 31 (2026), DOI `10.1214/26-EJP1557`) proves for the fixed-edge preferential-attachment model that

\[
\pi_c=
\frac{\delta}{2\left(m(m+\delta)+\sqrt{m(m-1)(m+\delta)(m+1+\delta)}\right)}
\qquad (\delta>0),
\]

and

\[
\pi_c=0\qquad (\delta\le0).
\]

It also proves that the critical threshold of the finite graph equals the survival/percolation threshold of its local Pólya-point-tree limit. These results answer the main threshold question and the explicit sign/local-limit subquestions from the old source.

I did **not** mark the whole source problem KNOWN in this run because the remaining sentence comparing the fixed-edge model with the older conditionally-independent-edge preferential-attachment model requires exact parameter/model matching. The current paper makes clear that preferential-attachment-type conditionally-independent models are related but not identical objects, and I have not written a source-level equivalence-or-inequivalence proof for that last clause here.

**Disposition:** `I0048 = HOLD_LARGELY_RESOLVED / NOT_READY_FOR_R08`. It is not a clean fresh CLOSABLE target without first isolating the exact remaining comparison clause and checking whether that clause too is already answered. No claim created.

### 3.4 I0049 is KNOWN / RESOLVED

Intake I0049 is Open Problem 4.7, asking whether the uniformly grown random graph has a critical choice near `c=1/4` and, if so, what its critical window is.

Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937 (submitted 22 December 2025), explicitly includes the **uniformly grown random graph** in its model class. It proves, whenever the critical threshold is positive, that the critical window has width

\[
(\log n)^{-2},
\]

that the largest component inside the window has order

\[
\frac{\sqrt n}{\log n},
\]

and that there is a secondary transition at the finite upper boundary of the window. In the uniformly-grown case the source's `c\approx1/4` critical point is precisely within this framework. Thus the old qualitative source question and its critical-window request are no longer open as stated.

**Disposition:** `I0049 = KNOWN / RESOLVED_IN_LATER_LITERATURE`. No claim created; not an eligible successor.

## 4. B21 — what the neighboring literature says about the next admission

The common pattern in I0045/I0046/I0048/I0049 is instructive: the older source list contains several problems that were natural in the Saint-Flour-era state of preferential attachment, but the 2024--2026 local-limit/percolation literature has moved exactly through those gaps. In particular:

- later-author monograph work closed the self-loop and negative-`delta` local-limit gaps;
- Hazra--van der Hofstad--Ray closed the principal fixed-edge percolation-threshold/local-limit gap;
- Jorritsma--Maillard--Mörters closed the uniformly-grown critical-window gap.

So the right successor policy is **not** to invent a narrower finite milestone inside these already-moved source questions. The next R08 run should continue down the unclaimed source list and demand a clean statement that survives a 2024--2026 current-literature check before freezing a metric or creating a claim.

A natural next screening point is I0050 or another later queue row with no canonical claim, but its source is broader and should not be mislabeled CLOSABLE merely to fill the slot. Admission must remain `null` until a genuinely source-matching, current-open, unowned CLOSABLE target is found.

## 5. Method accounting

**B22 — READ THE FAILURES, NOT THE SUCCESSES.** Instead of beginning a new proof from the queue's historical `open_per_source` tags, I read why those tags existed: they came from a source sweep with no later-resolution search. Following the same authors and model variants forward immediately exposed the stale entries.

**B23 — DO WHAT THE PROPOSER DID NOT EXPECT.** I assumed the queue was wrong and tried to refute openness before accepting a target. That succeeded for I0045, I0046, and I0049, and substantially succeeded for I0048.

**B21 — ASK WHO ELSE HAS THIS SHAPE.** I followed the model family into van der Hofstad's 2024 Volume 2, the 2026 Hazra--van der Hofstad--Ray percolation paper, and the 2025 Jorritsma--Maillard--Mörters critical-window paper. This converted what looked like four possible research starts into three clean exclusions plus one hold.

No exact-arithmetic checker was created because this run's substantive output is a source/current-literature/ownership determination, not a finite mathematical claim. Creating a checker here would be bookkeeping without a finite theorem to certify.

## 6. Scheduler/model-control status

The exposed task-management schema still offers title, prompt, schedule, timing mode, enablement, and prompt text. It does **not** expose a model-family selector, reasoning-effort selector, or authenticated completed-run telemetry. Therefore GPT-6 / maximum remains a request in prompt text, not an enforceable or auditable runtime setting from this interface.

Actually enforcing the requested model would require the authorized owning product/workspace/API to expose native model and reasoning fields and completed-run telemetry. A task that returns `You cannot modify this task` must be handled through the authorized owning context, supported ownership/admin transfer, or platform support. Duplicating a task or editing GitHub is not a model-control workaround. No scheduler modification was attempted in this run, consistent with the deployment restriction.

## 7. Structured ledger delta

```yaml
ledger_delta:
  track: R08
  model_actual: GPT-5.6 Sol
  reasoning_actual: UNVERIFIED
  previous_source:
    id: F0083
    candidate: Xi_star
    metric: "1/2"
    status: RETIRED_HANDOFF
    unchanged_count: 6
  preserved_retired_source:
    id: I0082
    metric: "2/3"
    status: RETIRED_FROZEN
    retirement_count: 6
  methods: [22, 23, 21]
  screened:
    - id: I0035
      disposition: OWNED_BY_C31
      action: skipped
    - id: I0054
      disposition: OWNED_BY_R11
      action: skipped
    - id: I0045
      disposition: KNOWN_RESOLVED_IN_LATER_LITERATURE
      ownership_search: no_canonical_claim_found_in_bounded_search
      action: no_claim
    - id: I0046
      disposition: KNOWN_RESOLVED_IN_LATER_LITERATURE
      ownership_search: no_canonical_claim_found_in_bounded_search
      action: no_claim
    - id: I0048
      disposition: HOLD_LARGELY_RESOLVED_NOT_READY
      ownership_search: no_canonical_claim_found_in_bounded_search
      remaining_issue: exact_fixed_edge_vs_conditionally_independent_model_comparison_clause
      action: no_claim
    - id: I0049
      disposition: KNOWN_RESOLVED_IN_LATER_LITERATURE
      action: no_claim
  successor_admitted: null
  active_metric: null
  next_action: continue_source_current_literature_ownership_screen_for_a_genuinely_open_unowned_CLOSABLE_target
```

## 8. Honest status

This is not a mathematical closure report and does not manufacture movement on a retired metric. It is a substantive rotation result: three seemingly available queue entries are removed as obsolete source questions, and a fourth is quarantined because its main content is already solved. R08 remains without an admitted active successor at the end of this run. That is preferable to overriding another owner's claim or freezing a metric on a question that later literature has already answered.
