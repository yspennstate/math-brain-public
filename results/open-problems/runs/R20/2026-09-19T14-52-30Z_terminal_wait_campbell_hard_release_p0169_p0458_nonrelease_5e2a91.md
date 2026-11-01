Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. R20 successor-gate metric `E_READY_SUCCESSOR: 0 -> 0`; frozen Paley `p_max=1213` and frozen BMO `n_all=9` do not move; NO RESEARCH-TARGET MOVEMENT; methods #13 FIND WHAT ONLY INCREASES, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #26 HUNT THE SPORADIC CASE, all marked SECOND-CYCLE REUSES because the preserved terminal-wait history has already used these moves before.**

# R20 — terminal wait: explicit Campbell release is HARD; P0169/P0458 retirements are not releases

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Track: `R20` / `CLOSABLE OUTSIDE`

## 1. Continuity and frozen source state

I continued from the newest immutable R20 report rather than restarting either retired source route:

`runs/R20/2026-09-19T13-56-30Z_terminal_wait_p0336_local_handoff_no_release_2f7a91.md`

at commit

`9e3732d12ef702ebf2b8e6d01d62b5aa9945a0cd`.

The original R20 source remains Afonso S. Bandeira, Randomstrasse 2025, Conjecture 26 / intake I0100. Its retained exact finite-certificate frontier is

`p_max = 1213`,

with complete covered admissible-prime set

`{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`.

Those matching exact primal/dual finite certificates remain **PARTIAL** evidence only; they do not prove

`theta(complement G_{p,1}) ~ sqrt(p/2)`.

R20 already exhausted the six-unchanged-run CLOSABLE lifecycle on I0100 and later on the Bensmail–Marcille–Orenga successor (`n_all=9`). Neither source is reopened merely because the recurring scheduler title still names Paley.

## 2. Whole-repository continuity read

Before successor dispatch I reread the current campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the operative `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the newest own R20 report, and the newest neighboring CLOSABLE/handoff reports. I also inspected the complete Git delta below rather than interpreting missing reports as permission to restart.

Fresh prewrite master was

`c50bb20a190bb331edfb636bbc2edf31d7d48c51`.

Exact comparison

`9e3732d12ef702ebf2b8e6d01d62b5aa9945a0cd .. c50bb20a190bb331edfb636bbc2edf31d7d48c51`

returns **113 commits ahead, 0 behind, `too_large=null`**, so the returned changed-file set is complete.

Exactly two canonical claim files mutate in that full interval:

1. `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md` changes to an explicit `UNASSIGNED AFTER HARD7-02 HANDOFF` release. This is a genuine ownership release, but the canonical classification remains **HARD OUTSIDE**, source OPEN/PARTIAL, with retained metric `S=5`. It therefore fails R20's CLOSABLE lane gate.
2. `operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md` is newly created as **HARD OUTSIDE / ADMITTED_ACTIVE** and is already owned by HARD7-02. It is neither CLOSABLE nor owner-clear.

There is **no CLOSABLE canonical claim mutation** in the complete interval.

## 3. New local CLOSABLE handoffs do not create inventory

Two new six-run lifecycle events are tempting because they concern CLOSABLE sources:

- `P0169` (O'Donnell, Linear Coefficients versus Total Degree) reaches its R7-02 six-unchanged-run handoff at frozen `D_weak=4`, source status PARTIAL/OPEN. Its handoff explicitly says the canonical claim remains historical ownership evidence and is **not** a general release.
- `P0458` (Dabirian–Subramanian bilateral-preference degree limits) reaches its R7-03 six-run handoff after internal source-scope proof with `R_unresolved=0`, but protocol audits remain `0/2`. Its handoff likewise says the canonical claim is not released by worker-local retirement.

Neither canonical claim file changes in the exact 113-commit comparison. Under the owner protocol, a worker-local retirement is not an owner-clear lifecycle event. R20 therefore cannot duplicate or steal either problem.

## 4. Section-B method outcomes

### #13 FIND WHAT ONLY INCREASES — canonical lifecycle state is the operative monovariant

The useful monotone object is not the number of workers that say “retired”; it is the set of sources with an **explicit owner-clear canonical release**. This interval increases that set by Campbell–O'Rourke Question 1.8, but that release remains HARD. The set of owner-clear READY CLOSABLE targets does not increase.

**Outcome:** `E_READY_SUCCESSOR` stays 0.

### #23 DO WHAT THE PROPOSER DID NOT EXPECT — assume each tempting shortcut is legal

I tested both tempting opposites:

- “Explicitly released means R20 may claim it.” Campbell Q1.8 refutes this shortcut because release does not change the canonical **HARD OUTSIDE** classification.
- “Six-run-retired CLOSABLE means free.” P0169 and P0458 refute this shortcut because neither retirement mutates canonical ownership.

The lawful conjunction remains:

`eligible_R20 = source_exact AND current_open-looking AND nonexcluded AND READY AND CLOSABLE AND owner_clear`.

No candidate satisfies all terms.

### #26 HUNT THE SPORADIC CASE — classify only events capable of changing dispatch

The 113-commit interval contains much mathematical work on other owned targets, but the only direct dispatch-changing events are canonical claim mutations or an explicit CLOSABLE owner release. The exhaustive event census is:

- one canonical release: Campbell Q1.8 — **HARD**;
- one new canonical claim: Campbell Q1.9 — **HARD and owned**;
- two CLOSABLE local retirements: P0169 and P0458 — **not canonical releases**;
- zero owner-clear READY CLOSABLE canonical events.

**Outcome:** the zero successor gate survives a direct attempt to falsify it.

## 5. Current Paley source check

The current Randomstrasse source was checked again on 2026-09-19. It still states Conjecture 26 for primes `p == 1 (mod 4)` as

`theta(complement G_{p,1}) ~ sqrt(p/2)`,

with `G_{p,1}` the induced graph on neighbors of 0, and it explicitly notes that the 1-localization is circulant so the theta SDP reduces to an LP. The same source separately states Conjecture 27 (two-localization), Conjecture 28 (degree-four SOS), and Conjecture 29 (Paley ETF), so those scopes remain distinct from R20.

This is a bounded current-source check, not a worldwide novelty certificate. No new primary-source resolution was found in the checked current source, and nothing in the repository delta authorizes a seventh I0100 research run.

## 6. Why there is no new checker

No new finite mathematical claim was made. Creating another checker for an unchanged, already-retired source metric would violate the requested 90/10 research-to-validation discipline. The exact finite Paley certificates already archived remain the correct finite evidence; their existence does not upgrade the asymptotic conjecture from PARTIAL.

## 7. Model / scheduler control truth

This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so reasoning is **UNVERIFIED**. I do not claim GPT-6 or verified maximum reasoning.

The live task-management surface inspected this run exposes task text/title, scheduling/timing, enabled state, notification/email state and ordinary task identity/update controls. It still exposes **no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/applied-effort receipt, and no guaranteed hour-long execution field**. Thus `GPT-6 / maximum` remains a prompt request on this surface, not a binding scheduler setting.

The historical P26 `You cannot modify this task` result remains an authorization-context boundary. Repository continuity records a later successful P26 update from another authorized context. The lawful remedy for a repeated denial is the owning/authorized workspace/account/API/admin surface or platform support for that same task — never permission bypass, task duplication, or identity substitution.

No scheduler, permission, email, Drive, public-posting, purchase, or external-access mutation was made by R20.

## 8. Disposition

R20 remains

`TERMINAL_WAITING_FOR_NEW_READY_DELTA`.

The next lawful trigger is a canonical lifecycle event producing a source-exact, current-open-looking, nonexcluded, **READY CLOSABLE OUTSIDE** target that is explicitly owner-clear. A local handoff without canonical release is insufficient; an explicit HARD release is also insufficient. Until such a trigger appears, R20 must not reopen I0100 or BMO.

## ledger_delta

```yaml
ledger_delta:
  track: R20
  actual_model: GPT-5.6 Sol
  reasoning: UNVERIFIED
  lane: CLOSABLE_OUTSIDE
  frozen_paley:
    source: Afonso S. Bandeira, Randomstrasse 2025, Conjecture 26
    intake: I0100
    metric_name: largest admissible prime with matching exact primal/dual certificates
    p_max: 1213
    covered_primes: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213]
    mathematical_status: PARTIAL_OPEN
  frozen_bmo:
    metric_name: n_all
    value: 9
    mathematical_status: PARTIAL
  successor_gate:
    name: E_READY_SUCCESSOR
    before: 0
    after: 0
    movement: NO_MOVEMENT
  operational_status: TERMINAL_WAITING_FOR_NEW_READY_DELTA
  unchanged_count: PRESERVED_TERMINAL_AFTER_SIX_RUN_HANDOFFS
  tried_moves:
    - 13 SECOND_CYCLE_REUSE
    - 23 SECOND_CYCLE_REUSE
    - 26 SECOND_CYCLE_REUSE
  predecessor_report: runs/R20/2026-09-19T13-56-30Z_terminal_wait_p0336_local_handoff_no_release_2f7a91.md
  predecessor_commit: 9e3732d12ef702ebf2b8e6d01d62b5aa9945a0cd
  fresh_prewrite_head: c50bb20a190bb331edfb636bbc2edf31d7d48c51
  exact_delta:
    ahead: 113
    behind: 0
    too_large: false
    canonical_claim_mutations: 2
    canonical_events:
      - CAMPBELL-OROURKE-2022-Q1.8 explicit_release_UNASSIGNED_but_HARD
      - CAMPBELL-OROURKE-2022-Q1.9 new_claim_HARD7-02_HARD
    closable_canonical_claim_mutations: 0
    p0169_local_retirement: true
    p0169_canonical_release: false
    p0458_local_retirement: true
    p0458_canonical_release: false
  remaining_obligation: >-
    Wait for an explicitly owner-clear READY CLOSABLE OUTSIDE canonical lifecycle
    event. Do not reopen I0100 or BMO after their completed six-run handoffs and
    do not promote local retirement, PENDING rows, or HARD releases into R20 inventory.
  evidence:
    - runs/R20/2026-09-19T13-56-30Z_terminal_wait_p0336_local_handoff_no_release_2f7a91.md
    - operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md
    - operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md
    - research7_2026-09-17/R7-02/handoffs/2026-09-19T144900Z__P0169_sixrun_handoff.md
    - research7_2026-09-17/R7-03/handoffs/2026-09-19T143800Z__P0458_sixrun_handoff.md
    - operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md
    - Randomstrasse Conjecture 26 source checked 2026-09-19
  audit_ids: []
```
