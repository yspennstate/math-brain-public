Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. R20 successor-gate metric `E_READY_SUCCESSOR: 0 -> 0`; Paley `p_max=1213` and BMO `n_all=9` remain frozen after completed six-unchanged-run handoffs; NO RESEARCH TARGET MOVEMENT; methods #12 FIND WHAT IS CONSERVED, #26 HUNT THE SPORADIC CASE, #30 DO ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME.**

# R20 — terminal wait: F0011 is HARD/owned and P0219 retirement is not a canonical release

Repository / branch: private `yspennstate/math-open-problems` / `master`.
Worker: R20.
Lane: **CLOSABLE OUTSIDE**.

## 0. Continuity and controlling state

I continued from the newest own immutable report

`runs/R20/2026-09-19T09-52-30Z_terminal_wait_p0342_owned_g0004_hard_8c41e2.md`

created by commit

`0f7c7acc5329d68611fa404182c41e875374e818`.

Its lifecycle is

`TERMINAL_WAITING_FOR_NEW_READY_DELTA`

with operative gate metric

`E_READY_SUCCESSOR=0`.

The two preceding R20 mathematical targets remain frozen and are not reopened:

- I0100 / Afonso S. Bandeira, Randomstrasse Conjecture 26: exact-certified frontier `p_max=1213`, retained covered-prime set `{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`, status **PARTIAL / six-run handoff** for the source asymptotic;
- Bensmail--Marcille--Orenga Conjecture 2.6 successor: `n_all=9`, status **PARTIAL / RETIRED_AFTER_SIX_UNCHANGED / HANDOFF**.

The canonical I0100 ownership file still names R20 and still distinguishes Conjecture 26 from R12's Conjecture 28, P04's Conjecture 27 and C28's Paley ETF/RIP work. A worker-local retirement does not authorize another attack, and it does not by itself release canonical ownership.

Required current-state surfaces read/recovered in this invocation include `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, `operations/claims/I0100.md`, the newest own R20 report, the newest neighboring R19 terminal-gate report, the latest coordinator status, the new F0011 claim, and the exact changed-file delta from the preceding R20 commit. The large intake ledgers were not falsely represented as visually rerendered byte-for-byte: the exact Git delta proves the screened `probability_1000_intake_*/problems.jsonl` surfaces did not mutate, so the prior completed intake reconciliation is preserved rather than restarted.

## 1. Exact repository delta

I froze the final pre-write `master` head at

`9c27e1ecc3a0ab3dfc132a8c6afbb3500c8a2069`.

The exact comparison

`0f7c7acc5329d68611fa404182c41e875374e818 .. 9c27e1ecc3a0ab3dfc132a8c6afbb3500c8a2069`

reports **114 commits ahead, 0 behind**.

The admission-critical static surfaces remain unchanged in this interval: root `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md` / `RANKING.md`, and screened intake `problems.jsonl` files have no mutation that could silently convert a PENDING row into READY.

The canonical claim-file events in the complete interval are exactly three additions:

1. `operations/claims/P0342.md` — CLOSABLE OUTSIDE, but exclusively owned by P13;
2. `operations/claims/G0004.md` — HARD OUTSIDE, exclusively owned by R17;
3. `operations/claims/F0011.md` — HARD OUTSIDE, exclusively owned by R7-06.

There is no canonical claim deletion, no canonical modification into an explicit owner-clear release, and no free CLOSABLE ownership transition.

The new F0011 claim is Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4 on integral spectrum. Its claim file explicitly labels it `CLAIMED / HARD OUTSIDE`, owner `R7-06`, so it fails R20's gate independently on both category and ownership.

A second material lifecycle event is P0219, Aldous's high-density Hammersley-flow conjecture. Its current worker reached the six-supported-unchanged-run CLOSABLE retirement boundary. But `operations/claims/P0219.md` remains unchanged and still says `CLAIMED / MANUALLY ADMITTED / CLOSABLE OUTSIDE` with the same native owner. The newest neighboring R19 report independently records the same distinction: local retirement is not canonical release. P0219 therefore does not become lawful R20 inventory.

Hence

`E_READY_SUCCESSOR: 0 -> 0`.

## 2. Method #12 — FIND WHAT IS CONSERVED

The conserved object in the present lifecycle protocol is canonical exclusive ownership under worker-local status changes.

P0219 is the clean current witness. Its research route can cross from active to `RETIRED / HANDOFF` after six unchanged runs while its canonical claim remains owned by the same native slot. Therefore the property

`owner_clear = false`

is invariant under that worker-local retirement event unless a separate canonical ownership mutation occurs.

The same principle applies to R20's I0100 history: a six-run mathematical handoff prevents a seventh attack by this worker, but the old claim file does not thereby become an unassigned reserve row. These are two different lifecycle facts and must not be conflated.

**Outcome #12:** canonical ownership is conserved across the newly observed local P0219 retirement. No successor is freed.

## 3. Method #26 — HUNT THE SPORADIC CASE

I searched the new delta for an exceptional event that could defeat the terminal-wait conclusion.

The strongest candidate is not a random old queue row but the genuinely new canonical claim F0011. It is source-exact and current-looking, but it is explicitly HARD and already owned. It is therefore an instructive near-miss, not a successor.

The other exceptional-looking event is P0219's retirement. This looks superficially like a release, but exact inspection of the canonical claim shows it is not. Thus the two newest lifecycle anomalies fail for complementary reasons:

- F0011: wrong lane + occupied;
- P0219: right lane historically, but still occupied because retirement did not mutate ownership.

P0342 remains the best recent CLOSABLE-shaped new source, but its exact claim still assigns it to P13.

**Outcome #26:** every sporadic-looking event in the current delta fails an explicit gate. There is no hidden free CLOSABLE successor.

## 4. Method #30 — DO ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME

I localized the successor question to one lifecycle event at a time rather than treating repository commit volume as research progress.

For each event `e`, define

`Delta_e E = 1`

only if the event creates or releases a target that is simultaneously source-exact, current-open-looking, nonposted/nonexcluded, READY, CLOSABLE OUTSIDE, and explicitly owner-clear.

Across the current canonical events:

- P0342 addition: `Delta_e E=0` because owner=P13;
- G0004 addition: `Delta_e E=0` because HARD and owner=R17;
- F0011 addition: `Delta_e E=0` because HARD and owner=R7-06;
- P0219 worker-local retirement: `Delta_e E=0` because the canonical claim does not change.

Thus the exact eventwise gate remains zero. This is the appropriate localized measurable quantity while R20 is between lawful research assignments.

**Outcome #30:** no event glues into an owner-clear READY CLOSABLE successor. No mathematical checker was manufactured because there is no new finite mathematical claim to validate.

## 5. Fresh source-status check for frozen I0100

Dated check: **19 September 2026**.

Primary source checked directly:

`https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/`

The current Randomstrasse page still defines the Paley 1-localization and prints Conjecture 26 as

`theta(complement G_{p,1}) ~ sqrt(p/2)`

for primes `p = 1 mod 4`. On the same page Conjecture 27 is the distinct two-localization problem, Conjecture 28 is the distinct degree-four SOS problem, and Conjecture 29 is the distinct Paley ETF/RIP problem.

A current public Jig root page for this exact 1-localization statement still labels the root **Open** and records kernel-checked reductions and partial bounds rather than a source-level proof or refutation. In particular, it records one-sided/spectral reductions while preserving the asymptotic root as residual.

This is bounded dated current-status evidence, not a worldwide novelty certificate. It supports keeping the source verdict OPEN/PARTIAL rather than claiming a resolution. It does **not** override the completed six-run R20 handoff or authorize another I0100 attack.

## 6. Model / reasoning / scheduler-control truth

Actual model visible to this invocation: **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so reasoning is **UNVERIFIED**. I do not claim GPT-6 or verified maximum reasoning.

The exposed task-control surface still has task identity/title, prompt, schedule/timing and enabled-state controls, but no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/applied-effort receipt, and no guaranteed hour-long runtime setting. Therefore `GPT-6 / maximum` remains prompt text only from this surface.

The historical P26 `You cannot modify this task` response was authorization-context-specific: repository configuration records a later successful P26 update from another authorized context. If that denial recurs, the lawful workaround is the owning/authorized account, workspace, admin/API/product surface, supported ownership transfer, or platform support for the same task. It is not a permission bypass and not creation of a duplicate protected task.

No scheduler, permission, email, Drive, public-posting, purchase, or access mutation was made in this invocation.

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
      status: "PARTIAL / six-run handoff; source root remains open-looking in bounded 2026-09-19 check"
    BMO_2025_PUSHING_DELTA:
      n_all: 9
      status: "PARTIAL / RETIRED_AFTER_SIX_UNCHANGED / HANDOFF"
  tried_moves: [12, 26, 30]
  delta_base: "0f7c7acc5329d68611fa404182c41e875374e818"
  delta_head_observed: "9c27e1ecc3a0ab3dfc132a8c6afbb3500c8a2069"
  delta_commits_ahead: 114
  canonical_claim_mutations:
    P0342: "CLOSABLE OUTSIDE; owned by P13"
    G0004: "HARD OUTSIDE; owned by R17"
    F0011: "HARD OUTSIDE; owned by R7-06"
  material_nonclaim_lifecycle:
    P0219: "local six-run retirement/handoff; canonical claim unchanged and still owned"
  newly_owner_clear_ready_closable: []
  remaining_obligation: "wait for the first source-exact current-open nonexcluded READY CLOSABLE target that becomes explicitly owner-clear; claim it create-only; do not reopen I0100 or BMO from stale task-title state"
  evidence:
    - "runs/R20/2026-09-19T09-52-30Z_terminal_wait_p0342_owned_g0004_hard_8c41e2.md"
    - "operations/claims/I0100.md"
    - "operations/claims/P0342.md"
    - "operations/claims/G0004.md"
    - "operations/claims/F0011.md"
    - "operations/claims/P0219.md"
    - "operations/task_health/runs/2026-09-19T101100Z/status.md"
    - "runs/R19/2026-09-19_10-36-30_UTC__terminal-wait-f0011-hard-p0219-retired-owned_c5m2.md"
    - "QUEUE.md"
    - "POSTED.md"
    - "RESULTS.md"
    - "probability_campaign_2026_09/INDEX.md"
    - "probability_campaign_2026_09/RANKING.md"
    - "operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md"
  audits: []
```

## 8. Next invocation

Resume from this report commit and inspect the new lifecycle delta first. If a source-exact, current-open, nonexcluded, READY CLOSABLE target has become explicitly owner-clear, claim it create-only and begin counterexample-first research with a nonrepeating Section-B triple. Otherwise preserve `TERMINAL_WAITING_FOR_NEW_READY_DELTA` without restarting I0100 or BMO and without producing a receipt-only mathematical checker.
