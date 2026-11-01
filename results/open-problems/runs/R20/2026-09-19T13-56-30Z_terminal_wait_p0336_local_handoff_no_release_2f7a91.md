Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. R20 successor-gate metric `E_READY_SUCCESSOR: 0 -> 0`; Paley `p_max=1213` and BMO `n_all=9` remain frozen after completed six-unchanged-run handoffs; NO RESEARCH-TARGET MOVEMENT; methods #2 ATTACK THE NEGATION FIRST, #12 FIND WHAT IS CONSERVED, #30 DO ONE PRIME / SCALE / DIRECTION AT A TIME.**

# R20 — terminal wait: P0336 reaches six-run worker handoff but canonical ownership is not released

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: R20  
Lane: **CLOSABLE OUTSIDE**

## 0. Continuity and frozen mathematical state

I continued from the newest own immutable report

`runs/R20/2026-09-19T12-50-30Z_terminal_wait_lyap6_owned_p0157_reassigned_84b3c2.md`

created at commit

`d8e4044b1af6f2f31373e00bc58a647a09087b13`.

Its lifecycle is `TERMINAL_WAITING_FOR_NEW_READY_DELTA`, with gate metric `E_READY_SUCCESSOR=0`.

The two completed R20 research cycles remain frozen and are not reopened:

- I0100 / Afonso S. Bandeira, Randomstrasse Conjecture 26: exact-certified frontier `p_max=1213`, retained covered-prime set `{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`, source status **OPEN / PARTIAL / six-run handoff**; finite primal/dual certificates do not prove the asymptotic;
- Bensmail--Marcille--Orenga Conjecture 2.6 successor cycle: `n_all=9`, status **PARTIAL / RETIRED_AFTER_SIX_UNCHANGED / HANDOFF**.

Before deciding whether a successor exists I freshly read the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the operative `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the newest own R20 report, the newest current admission screen, and the material new lifecycle file in the repository delta.

## 1. Exact repository delta relevant to R20

I compared the previous R20 report commit

`d8e4044b1af6f2f31373e00bc58a647a09087b13`

against current prewrite head

`fc881981f2b3e758a99015e065f7d229ad60fadc`.

Git reports:

- status: `ahead`;
- commits ahead: **104**;
- commits behind: **0**;
- total commits: **104**;
- `too_large = null`.

The returned complete changed-file set contains **no `operations/claims/*.md` additions, modifications, deletions, or renames**. It also contains no mutation of root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, or the screened intake `problems.jsonl` ledgers. The interval is overwhelmingly substantive work and reports on already-owned targets plus support/audit material.

The one new lifecycle event that could plausibly challenge R20's zero-successor gate is the commit

`fc881981f2b3e758a99015e065f7d229ad60fadc`

adding

`research7_2026-09-17/R7-05/handoffs/2026-09-19/2026-09-19T135300Z__P0336_six_run_retirement_handoff.md`.

P0336 is genuinely **CLOSABLE OUTSIDE** and its native worker reached the six-unchanged-run retirement threshold. But the handoff states explicitly that this is **worker-local operational retirement**, that the canonical claim file is preserved and not overwritten, and that the retirement **must not be treated as ownership release by another worker without the owner protocol**. The handoff also creates no successor claim for R7-05.

Therefore P0336 is **not OWNER_CLEAR for R20**. The repository contains no other new canonical ownership release or READY CLOSABLE admission in the complete delta.

The current independent admission screen `proofnet24/NM13-10/runs/2026-09-19/2026-09-19T13-51-30Z__admission-delta-screen-43-no-canonical-release-no-r9-closable.md` reaches the same lifecycle conclusion in its scope: zero canonical claim mutations, no root/intake admission mutation, and no newly free READY CLOSABLE inventory.

Hence the operative gate remains

`E_READY_SUCCESSOR: 0 -> 0`.

No successor claim is created in this run.

## 2. Method #2 — ATTACK THE NEGATION FIRST

The negation of the terminal diagnosis is:

> There exists at least one current source-exact, nonexcluded, READY, CLOSABLE OUTSIDE target that is owner-clear for R20.

The strongest fresh candidate for falsifying `E_READY_SUCCESSOR=0` is P0336 because its worker has just stopped research after six unchanged runs.

I attacked the gate using exactly that event. It fails on ownership: the terminal handoff itself says that the canonical claim remains preserved and that worker-local retirement is not permission for another worker to take the problem. The complete 104-commit comparison independently confirms that no canonical claim mutation accompanies the handoff.

**Outcome #2:** the best new counterexample to the zero-gate diagnosis fails. `E_READY_SUCCESSOR=0` survives.

## 3. Method #12 — FIND WHAT IS CONSERVED

The conserved object across the worker-local retirement is **canonical ownership state**.

A six-run terminal handoff changes a worker's local research lifecycle, but absent one of the following it does not change ownership:

1. an explicit canonical claim mutation releasing the target;
2. an owner-authorized transfer recorded in the claim; or
3. another controlling ownership instruction with exact target scope.

None occurs in the complete delta. This is the same lifecycle distinction already encountered for P0219/P0411 and is now confirmed directly by P0336's own handoff language.

**Outcome #12:** canonical ownership is conserved across this P0336 worker-local retirement; no lawful R20 claim follows.

## 4. Method #30 — DO ONE PRIME / SCALE / DIRECTION AT A TIME

Rather than re-screening the entire reserve merely because another scheduled run occurred, I localized the admission question to the only material new direction: **does the P0336 six-run handoff create an owner-clear CLOSABLE slot?**

Answer: no. The exact changed file says the opposite, and there is no canonical claim mutation.

This localized check is enough to preserve the gate because the complete Git delta shows no other source/claim/root admission changes. It avoids converting an unchanged admission landscape into repetitive queue bookkeeping.

**Outcome #30:** the only new potentially gluable piece does not glue into an R20 successor.

## 5. Fresh source/current-status check for frozen I0100

Dated check: **19 September 2026**.

Primary source checked directly:

`https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/`

The current page still defines the one-localization `G_{p,1}` and states Conjecture 26 as

`theta(complement G_{p,1}) ~ sqrt(p/2)`

for primes `p = 1 mod 4`.

The same source separately states Conjecture 27 (two-localization), Conjecture 28 (degree-four SOS), and Conjecture 29 (Paley ETF). Thus R12's degree-four SOS track, P04's two-localization track, and C28's ETF work remain distinct and are not reassigned here.

A current public formal-problem tracker for the Conjecture-26 root still labels the root problem **Open** and records partial reductions / failed stronger statements rather than a source-level proof or refutation.

This is bounded dated current-status evidence, not a worldwide novelty certificate. It supports preserving I0100 as **OPEN / PARTIAL** at `p_max=1213`. It does not authorize a seventh R20 Paley attack after the completed six-run handoff.

## 6. Why there is no new checker

R20 made no new finite mathematical claim. The material update is lifecycle/ownership state: P0336 reached a six-run worker handoff but explicitly did not release its canonical claim.

Creating a numerical or exact-arithmetic checker for that administrative fact would not test a research idea and would violate the requested 90/10 research-to-validation discipline. Existing Paley exact certificates remain archived finite evidence only; numerical SDP output is not promoted to an exact certificate.

## 7. Model / scheduler-control truth

Actual model visible to this invocation: **GPT-5.6 Sol**.  
Reasoning-effort telemetry: **UNVERIFIED**.  
I do not claim GPT-6 at maximum.

The exposed scheduler/task-control surface still provides task title/prompt, schedule or relative-start configuration, timing mode, enabled state and ordinary update/list operations. It exposes **no binding model-family selector, no binding reasoning-effort selector, no authenticated per-run applied-model/applied-effort receipt, and no guaranteed hour-long execution field**. `GPT-6 / maximum` therefore remains prompt text only from this surface.

The historical P26 `You cannot modify this task` response is still best understood as an authorization-context boundary. Current root `RESULTS.md` records that a later authorized context successfully updated P26. The lawful workaround is therefore the owning or otherwise authorized account/workspace/API/admin context for the same task, or platform support; it is not a permission bypass, duplicate schedule, or identity substitution.

No scheduler change was attempted in this run.

## 8. Structured ledger delta

```yaml
ledger_delta:
  worker: R20
  lane: CLOSABLE_OUTSIDE
  source: terminal successor gate after retired I0100/BMO targets
  metric: E_READY_SUCCESSOR
  before: 0
  after: 0
  status: TERMINAL_WAITING_FOR_NEW_READY_DELTA
  frozen_predecessors:
    I0100:
      metric: p_max
      value: 1213
      retained_primes: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213]
      status: OPEN_PARTIAL_SIX_RUN_HANDOFF
    BMO_2_6:
      metric: n_all
      value: 9
      status: PARTIAL_RETIRED_AFTER_SIX_UNCHANGED
  tried_moves: [2, 12, 30]
  material_delta:
    P0336:
      category: CLOSABLE_OUTSIDE
      worker_lifecycle: RETIRED_HANDOFF_AFTER_SIX_UNCHANGED
      canonical_claim_mutated: false
      explicit_owner_release: false
      available_to_R20: false
      reason: worker-local handoff explicitly says canonical claim is preserved and is not ownership release
  complete_repo_delta:
    base: d8e4044b1af6f2f31373e00bc58a647a09087b13
    head: fc881981f2b3e758a99015e065f7d229ad60fadc
    commits_ahead: 104
    too_large: false
    canonical_claim_mutations: 0
    root_admission_mutations: 0
  successor_claim_created: false
  successor_metric_initialized: false
  remaining_obligation: >-
    Wait for an explicit owner-clear, source-exact, current-open-looking,
    nonexcluded, READY CLOSABLE OUTSIDE target. A worker-local terminal handoff
    is not enough without canonical release. Do not reopen I0100 or BMO and
    do not steal P0336, LYAP6, P0342, or other owned targets.
  evidence:
    - prior R20 report commit d8e4044b1af6f2f31373e00bc58a647a09087b13
    - complete Git comparison d8e4044b1af6f2f31373e00bc58a647a09087b13..fc881981f2b3e758a99015e065f7d229ad60fadc
    - P0336 terminal handoff research7_2026-09-17/R7-05/handoffs/2026-09-19/2026-09-19T135300Z__P0336_six_run_retirement_handoff.md
    - NM13-10 admission screen 43
    - current Randomstrasse PaleyGraph primary-source page checked 2026-09-19
  audit_ids: []
```

## 9. Disposition

**R20 remains `TERMINAL_WAITING_FOR_NEW_READY_DELTA`.**

The next invocation should inspect only the material ownership/admission delta first. Claim a target create-only only if it is source-exact, current-open-looking, nonexcluded, explicitly READY, **CLOSABLE OUTSIDE**, and owner-clear. Otherwise preserve the terminal wait rather than reopen I0100/BMO or infer release from another worker's local retirement.