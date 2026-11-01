Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. R20 successor-gate metric `E_READY_SUCCESSOR: 0 -> 0`; Paley `p_max=1213` and BMO `n_all=9` remain frozen; NO RESEARCH TARGET MOVEMENT; methods #11 DUALIZE, #14 FIND THE GROUP ACTING, #19 MAKE IT AN ALGORITHM.**

# R20 — terminal wait: new CLOSABLE P0290 is already owned; the only explicit release is HARD

Repository / branch: private `yspennstate/math-open-problems` / `master`.
Worker: R20.
Lane: **CLOSABLE OUTSIDE**.

## 0. Continuity and controlling state

I continued from

`runs/R20/2026-09-19T07-52-30Z_terminal_wait_owned_delta_7b2c91.md`

whose lifecycle is

`TERMINAL_WAITING_FOR_NEW_READY_DELTA`

and whose operative metric is

`E_READY_SUCCESSOR=0`.

The earlier R20 mathematical predecessors remain frozen under their completed six-unchanged-run handoffs:

- I0100 / Randomstrasse Conjecture 26: `p_max=1213`, exact covered-prime set `{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`, status PARTIAL for the asymptotic;
- Bensmail--Marcille--Orenga Conjecture 2.6 successor: `n_all=9`, status `PARTIAL / RETIRED_AFTER_SIX_UNCHANGED / HANDOFF`.

Neither worker-local handoff is a canonical ownership release. I therefore did not restart either problem and did not infer availability from the stale native task title.

Before disposition I reread the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the canonical I0100 claim, the newest R20 report, the newest neighboring terminal CLOSABLE report, and the complete repository delta from the preceding R20 report commit. I also rechecked the current primary Randomstrasse source and bounded current public follow-up material. No shared root or peer file is edited here.

## 1. Exact repository delta since the preceding R20 report

I compared the preceding report commit

`865eabc5a9b64540819e74189e957cefdc1153fe`

against observed current `master` head

`dd9d3f3f8ea4854b6c6a167b4d198a2912579b63`.

The interval is 102 commits ahead. The only canonical-claim lifecycle changes relevant to a successor gate are:

1. `operations/claims/P0290.md` — a newly admitted **CLOSABLE-BY-REFUTATION OUTSIDE / SOURCE-EXACT** target, but its canonical claim is already owned by **R7-04 Constructive Model Research**;
2. `operations/claims/P0157.md` — now explicitly **UNASSIGNED AFTER HARD7-04 HANDOFF**, but it is **HARD OUTSIDE**, not a CLOSABLE successor for R20;
3. `operations/claims/VDH-8.3-DUALITY.md` — a HARD target and already owned by **HARD7-04**.

No changed `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md` / `RANKING.md`, I0100 claim, or BMO claim appears in this interval. The current `QUEUE.md` still says newly certified READY entries remain **zero** and that PENDING rows are not dispatchable merely because they are listed.

Therefore there is still no owner-clear READY CLOSABLE item that R20 can lawfully claim:

`E_READY_SUCCESSOR: 0 -> 0`.

## 2. Method #11 — DUALIZE the successor gate into exclusion certificates

Instead of rescanning every historical candidate as if ownership had vanished, I treated each changed canonical claim as a possible witness for `E_READY_SUCCESSOR>0` and wrote down the dual reason it fails.

- `P0290`: passes source-exact / closable-type admission, fails **owner-clear** because R7-04 owns it.
- `P0157`: passes owner-clear after explicit release, fails the **lane** predicate because it is HARD OUTSIDE.
- `VDH-8.3-DUALITY`: fails both the **lane** predicate and owner-clear predicate; it is HARD and owned by HARD7-04.

Thus every new lifecycle event has an explicit disqualifying certificate. No old PENDING queue row can supply a witness because the current queue expressly keeps READY certification separate from listing.

**Outcome #11:** the successor gate remains empty for a positive reason, not because a search happened to return nothing.

## 3. Method #14 — FIND THE GROUP ACTING on lifecycle events

The useful symmetry here is not a graph automorphism but a lifecycle quotient. For R20 dispatch, canonical changes collapse into four classes:

1. new CLOSABLE + owner-clear READY;
2. new CLOSABLE + already owned;
3. explicit release to UNASSIGNED but HARD;
4. new/changed HARD + owned.

Only class (1) changes `E_READY_SUCCESSOR` from zero. The complete observed delta contains one event of class (2), one event of class (3), one event of class (4), and none of class (1).

This quotient removes irrelevant commit noise and gives an exact dispatch decision without treating scheduler activity as research progress.

**Outcome #14:** 102 commits reduce to zero eligibility-changing CLOSABLE events for R20.

## 4. Method #19 — MAKE IT AN ALGORITHM

The terminal-wait gate can now be implemented conceptually as an incremental admission algorithm:

1. start from the last verified R20 report commit;
2. inspect only canonical claim / admission lifecycle mutations plus any controlling queue-policy change;
3. reject claimed targets, HARD-only releases, excluded/posted targets, and PENDING rows;
4. if and only if a source-exact current-open nonexcluded CLOSABLE target is both READY and explicitly owner-clear, claim it create-only and begin counterexample-first research;
5. otherwise preserve terminal wait and do not restart a six-run-retired predecessor.

This algorithm is sound for the current delta because `QUEUE.md` and the controlling policy did not change, while every relevant claim mutation was directly read. It avoids the failure mode of repeatedly re-screening hundreds of unchanged rows and then manufacturing a theorem/checker merely to show that the worker ran.

**Outcome #19:** no mathematical checker is appropriate this run; the only changed objects are textual ownership/lane facts already directly certified by canonical claims.

## 5. Fresh source-status check for the frozen Paley predecessor

Dated check: **19 September 2026**.

Primary source checked:

`https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/`

The current Randomstrasse page still defines `G_{p,1}` as the 1-localization and prints Conjecture 26 as

`theta(complement G_{p,1}) ~ sqrt(p/2)`

for primes `p = 1 mod 4`.

Bounded current queries used:

- `"Randomstrasse" "Conjecture 26" Paley one-localization theta`;
- `"Paley" "1-localization" theta Lovasz 2026`.

They recovered the current Jig root page for the exact conjecture, still labelled **Open**, with kernel-checked partial reductions / certificate routes but no source-level proof of the asymptotic. In particular, the public work still distinguishes partial sufficient conditions and finite/nonasymptotic route eliminations from the surviving root asymptotic.

This is bounded dated status evidence, not a worldwide priority or novelty certificate. It does not authorize a seventh I0100 attack after R20's six-run rotation.

## 6. Model / reasoning / scheduler-control truth

Actual model visible to this run: **GPT-5.6 Sol**. The platform does not expose authenticated reasoning-effort telemetry, so reasoning is **UNVERIFIED**. I do not claim GPT-6 or verified maximum reasoning.

A fresh live inspection of the current task-control surface still exposes title, prompt, schedule, timing mode, enabled state, timezone/notification settings and task identity, but **no binding model selector, no reasoning-effort selector, no authenticated applied-model/applied-effort receipt, and no guaranteed hour-long execution control**. Therefore GPT-6 / maximum remains prompt text only from this surface.

The historical P26 `You cannot modify this task` response remains an authorization-context boundary, not a technical workaround invitation. The lawful path is the task's owning/authorized account/workspace/admin/API surface or platform support. This worker made no scheduler or permission mutation, as required by its contract.

## 7. Structured ledger delta

```yaml
ledger_delta:
  worker: R20
  lane: CLOSABLE OUTSIDE
  actual_model: "GPT-5.6 Sol"
  reasoning: "UNVERIFIED"
  lifecycle_before: "TERMINAL_WAITING_FOR_NEW_READY_DELTA"
  lifecycle_after: "TERMINAL_WAITING_FOR_NEW_READY_DELTA"
  operative_metric: E_READY_SUCCESSOR
  metric_before: 0
  metric_after: 0
  movement: false
  retired_predecessors:
    I0100:
      source: "Bandeira / Randomstrasse Conjecture 26"
      p_max: 1213
      covered_primes: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213]
      status: "PARTIAL / six-run handoff; source root still open-looking in bounded 2026-09-19 check"
    BMO_2025_PUSHING_DELTA:
      n_all: 9
      status: "PARTIAL / RETIRED_AFTER_SIX_UNCHANGED / HANDOFF"
  tried_moves: [11, 14, 19]
  delta_base: "865eabc5a9b64540819e74189e957cefdc1153fe"
  delta_head_observed: "dd9d3f3f8ea4854b6c6a167b4d198a2912579b63"
  delta_commits_ahead: 102
  relevant_claim_mutations:
    P0290: "CLOSABLE-BY-REFUTATION OUTSIDE; owned by R7-04"
    P0157: "explicitly UNASSIGNED; HARD OUTSIDE"
    VDH-8.3-DUALITY: "HARD OUTSIDE; owned by HARD7-04"
  newly_owner_clear_ready_closable: []
  remaining_obligation: "wait for the first source-exact current-open nonexcluded ownership-clear READY CLOSABLE item; claim create-only; do not reopen I0100 or BMO from a stale task title"
  evidence:
    - "runs/R20/2026-09-19T07-52-30Z_terminal_wait_owned_delta_7b2c91.md"
    - "operations/claims/I0100.md"
    - "operations/claims/P0290.md"
    - "operations/claims/P0157.md"
    - "operations/claims/VDH-8.3-DUALITY.md"
    - "QUEUE.md"
    - "operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md"
  audits: []
```

## 8. Next invocation

Resume from this exact report commit. Inspect the canonical delta first. If a genuinely READY, CLOSABLE, source-exact, current-open, nonexcluded and owner-clear target has appeared, claim it create-only and begin real counterexample-first work. Otherwise preserve `TERMINAL_WAITING_FOR_NEW_READY_DELTA` without restarting I0100 or BMO and without producing a receipt-only mathematical checker.
