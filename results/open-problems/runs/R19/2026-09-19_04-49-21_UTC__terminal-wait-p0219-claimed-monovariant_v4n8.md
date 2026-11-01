Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. I0084 fixed metric `2/2 → 2/2`; successor gate `E_READY_SUCCESSOR: 0 → 0`; NO MOVEMENT; methods #4, #13, #29.**

Status: **TERMINAL_WAITING_FOR_NEW_READY_DELTA**. This run does not reopen I0084 theorem work, does not restart rotated I0120, and does not appropriate another slot's claim.

## Idea before code

The useful new way to view successor admission is as a finite state graph rather than a repeated queue scan. A candidate can move through

`PENDING → READY/CLOSABLE → CLAIMED`,

while R19's lawful inventory is not “all READY candidates” but only the boundary state

`READY/CLOSABLE + source-exact + current-open-looking + nonexcluded + ownership-clear-for-R19`.

Thus fleet-wide admission can improve while the R19-free successor count stays zero. Canonical claim occupation is a one-way obstruction for this worker unless there is a literal owner-authorized release; a rotation/handoff alone is not such a release.

## Method #4 — prove something weaker, completely

I did not try to solve a new source problem from a candidate I do not own. I instead checked the smaller exact operational proposition that matters now: whether the candidate that was pending last run has become a lawful R19 successor.

It has not. `operations/claims/P0219.md` now exists and says:

- source: David Aldous, *A discrete Hammersley process as an extreme case of oriented percolation flows*;
- source target: `1-v(p) ~ sqrt(2(1-p))` as `p -> 1`;
- status: **CLAIMED / MANUALLY ADMITTED / CLOSABLE OUTSIDE**;
- owner/native slot: **`6aa7ebbe26308191a40003a950a2307a`**;
- claim date: 2026-09-19.

This is a genuine lifecycle change from the previous `PENDING_NOT_READY` state, but it creates no free R19 edge. I therefore preserve `E_READY_SUCCESSOR=0`.

## Method #13 — find what only increases

For this terminal-wait route, occupancy of a canonical create-only claim acts as a monovariant with respect to R19 availability: once a CLOSABLE candidate is claimed by another native slot, it cannot become R19 inventory merely because that owner later writes a handoff or rotates. A literal release/reassignment is required.

P0219 demonstrates why this distinction matters. The fleet's certified CLOSABLE inventory improved, but the free-to-R19 inventory did not. Treating those as the same quantity would cause ownership theft and would falsely report metric movement.

## Method #29 — add the points at infinity

I completed the admission-state boundary explicitly:

1. `PENDING_NOT_READY`: source may be promising but cannot be dispatched;
2. `READY/CLOSABLE + unowned`: admissible successor candidate;
3. `CLAIMED`: unavailable to R19 absent an explicit release/reassignment;
4. `HARD`: wrong lane for this CLOSABLE worker;
5. `KNOWN/RESOLVED/POSTED`: excluded;
6. `TERMINAL_HANDOFF/ROTATED`: preserves work but is **not** synonymous with `RELEASED`.

The missing boundary point in several earlier scans was the last one. Adding it removes the temptation to treat a terminal handoff as free ownership.

## I0084 frozen source preserved exactly

I re-read Hasebe--Ueda arXiv:1710.08240v2, Conjecture 5.5. The source allows `S_t` to be the law of a **classical or free** alpha-stable process, assumes exactly

`∫ |x|^(2+alpha) dμ(x) < ∞`,

and conjectures eventual unimodality of the **ordinary classical convolution**

`μ * S_t`.

The asterisk is not free convolution, including in the free-stable-law branch. No `\boxplus` substitution is made here. The frozen alpha=1/2 source metric remains **2/2** and no stronger-moment, compact-support, posted additive-Brownian, or already-known stable special case receives new credit.

## Fresh literature / source-status check — 2026-09-19

Queries checked this run included:

- `"Conjecture 5.5" Hasebe Ueda unimodality stable convolution`;
- `Hasebe Ueda arXiv 1710.08240 eventual unimodality stable later resolution`;
- `Takahiro Hasebe Yuki Ueda unimodality stable 2024 2025 2026`.

The bounded search recovered the original arXiv/ALEA paper and later related Hasebe--Ueda work, but did not recover a later primary source explicitly proving or refuting the exact frozen arXiv-v2 ordinary-`*` formulation. This is **bounded negative evidence only**, not a worldwide novelty or current-openness certificate.

## Audit gate remains version-specific

Fresh repository search still does not produce the two required frozen-arXiv ordinary-`*` end-to-end audits. The following existing evidence remains non-substitutable:

- `R18-I0084-C001=PASS`: independent finite/symbolic core audit for the classical positive-half-stable endpoint, not a complete frozen-source end-to-end audit;
- `R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF`: explicitly the different ALEA free-`\boxplus` scope, not the frozen arXiv ordinary-`*` free-stable branch.

Hence the version-matching closure gate remains **0/2**. The required pair is still: one P26 frozen-arXiv ordinary-`*` end-to-end PASS plus one distinct OTHER-track frozen-arXiv ordinary-`*` end-to-end PASS.

## Repository continuation/read record

Before deciding the run state I read or refreshed:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- newest R19 report `runs/R19/2026-09-19_03-42-00_UTC__terminal-wait-p0169-owned_p5d7.md`;
- current claims and neighboring admission/coordinator reports relevant to CLOSABLE inventory;
- all seven `probability_1000_intake_*/problems.jsonl` ledgers (`claude`, `D`, `E`, `F`, `G`, `H`, `I`). The connector retrieved these large ledgers but truncated their displayed bodies; I do not treat truncation as proof that unseen rows are absent.

Current master was refreshed during the run; the relevant new canonical fact is the create-only P0219 claim above. No shared root, peer file, or claim file was edited by R19.

## Model / scheduler control truth

The exposed scheduler/task-control surface still provides prompt/title/schedule/timing/enabled and notification controls, but **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long runtime control**. Therefore GPT-6 maximum is only requested in prompt text on this interface and must not be reported as applied. Actual model exposed for this run is GPT-5.6 Sol; reasoning level is UNVERIFIED.

For a task that returns `You cannot modify this task`, including the historical P26 case, the lawful workaround is the owning/authorized scheduler context or platform/product/admin support. Do not duplicate the task to evade ownership, change permissions, or bypass authorization. To make GPT-6/maximum binding rather than aspirational, the product/scheduler would need to expose a model selector and reasoning-effort setting (or an equivalent authorized API/admin control) with applied-model attestation.

## Validation budget

No checker was created. This run made no new finite mathematical theorem claim; manufacturing a checker for the unchanged I0084 metric would violate the 90%-new-methods rule. The only delivery validation is the create-only immutable report and exact-commit readback.

```yaml
ledger_delta:
  source: "Hasebe--Ueda arXiv:1710.08240v2, Conjecture 5.5 / intake I0084"
  metric_name: "complete classical-stable/free-stable alpha=1/2 source cases proved"
  metric_before: "2/2"
  metric_after: "2/2"
  status: "TERMINAL_WAITING_FOR_NEW_READY_DELTA"
  unchanged_count: "TERMINAL_HANDOFF; not incremented after move-on"
  tried_moves: [4, 13, 29]
  successor_gate_before: 0
  successor_gate_after: 0
  remaining_obligation:
    - "wait for an explicit owner-clear, source-exact, full-source CLOSABLE successor or an authorized release/reassignment"
    - "retain frozen I0084 ordinary-* package; before repository closure obtain two independent version-matching end-to-end audits"
  evidence:
    - "P0219 changed from PENDING_NOT_READY to CLAIMED / MANUALLY ADMITTED / CLOSABLE OUTSIDE"
    - "P0219 canonical owner/native slot is 6aa7ebbe26308191a40003a950a2307a, not R19"
    - "Conjecture 5.5 re-read in arXiv v2: ordinary mu*S_t, exact (2+alpha)-moment, classical-or-free stable S_t law"
  audit_ids:
    frozen_I0084_version_matching: "0/2"
    noncounting:
      - "R18-I0084-C001=PASS [finite/symbolic core only]"
      - "R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF [ALEA free-boxplus scope]"
```

No email, Drive, public posting, purchase, permission change, workflow dispatch, scheduler change, shared-root edit, other-track edit, or claim overwrite was made.
