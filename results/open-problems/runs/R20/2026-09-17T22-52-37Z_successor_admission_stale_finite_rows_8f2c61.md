Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** **NO SUCCESSOR-ADMISSION MOVEMENT: `E_ready: 0 -> 0`; I0100 remains frozen at `p_max=1213` with retirement count `6` and was not reopened. Methods used: #8 GO THE OTHER WAY AND DISCRETIZE, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, #26 HUNT THE SPORADIC CASE.**

# R20 CLOSABLE OUTSIDE — successor-admission pass: stale finite-looking rows and current-literature exclusions

Date checked: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity: do not reopen I0100

I continued from the mandatory I0100 handoff

`runs/R20/2026-09-17T20-50-47Z_i0100_stuck_recovery2_rotation_handoff_c6f2a9.md`

and the first successor-admission screen

`runs/R20/2026-09-17T21-58-30Z_successor_admission_screen_4f9c2d.md`.

The stale native task title still names Bandeira / Randomstrasse Conjecture 26, but repository continuity controls. I0100 reached the owner-directed six-unchanged CLOSABLE limit and is retired from active R20 attack unless a later explicit reassignment occurs.

Preserved predecessor state:

- outside source: Afonso Bandeira et al., *Randomstrasse101: Open Problems of 2025*, Conjecture 26;
- source target: `theta(complement G_{p,1}) ~ sqrt(p/2)` for admissible primes;
- graph normalization and one-localization remain exactly as in the prior reports;
- frozen exact metric: `p_max = 1213`;
- retained exact-certified prime set:
  `{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`;
- retirement / unchanged count: `6`, frozen and **not incremented** in this admission run;
- mathematical status: `OPEN / PARTIAL / RETIRED-HANDOFF`.

A fresh 2026-09-17 public-source check recovered the current Jig entry `Jig #7: Open`, whose title is exactly “Is the Lovasz theta of the Paley 1-localization asymptotic to sqrt(p/2)? — Randomstrasse101 Conjecture 26.” The page contains kernel-checked reductions/partial statements but no source-level resolution. Thus I do not relabel the source as solved or refuted.

Before screening I reread the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current operations implementation manifest, the newest own R20 report, the newest task-health queue reconciliation, and recent neighboring successor screens. The intake corpus is too large for a literal byte-for-byte visual read through the connector; exact-ID/source retrieval was used for candidates reached here, and no stronger access claim is made.

## 2. Admission metric

There is no active successor theorem, so the only honest metric in this run is the admission gate

`E_ready := number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded pass.`

Before: `0`.  
After: `0`.

The newest task-health screen at `operations/task_health/runs/2026-09-17T215000Z/queue_screening.md` independently reports zero free `READY + CLOSABLE OUTSIDE + UNASSIGNED` successors on its screened front. I treat that as a snapshot, not as proof that every intake row is impossible, and therefore pushed the screen into stale finite-looking queue entries rather than stopping.

## 3. Method #8 — DISCRETIZE: I0048's finite threshold is now solved, while the residual clause is not a finite closure target

Candidate: `I0048`, van der Hofstad's older preferential-attachment percolation Open Problem 4.3.

The tempting CLOSABLE interpretation is to isolate the critical percolation threshold as a finite formula and certify it. That would now be stale work. Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models* (arXiv:2312.14085; EJP 31 (2026), DOI 10.1214/26-EJP1557), proves for the fixed-edge affine preferential-attachment model

`pi_c = delta / [2(m(m+delta)+sqrt(m(m-1)(m+delta)(m+1+delta)))]` for `delta>0`,

and `pi_c=0` for `delta<=0`, and proves equality of the finite-graph threshold with that of the Pólya-point-tree local limit.

So the main threshold/sign/local-limit part of the old source question is already answered. The neighboring R08 source reconciliation further notes that the only potentially residual wording is the comparison with an older conditionally-independent-edge variant; exact model/parameter matching for that comparison has not been frozen as a source-level standalone problem. Turning the already-solved threshold into a finite checker would therefore not close the remaining source wording.

**Disposition:** `I0048 = HOLD_LARGELY_RESOLVED / NOT READY / no claim`.

The useful lesson from discretizing is negative: a solved finite constant inside a broader historical source question is not a new CLOSABLE target.

## 4. Method #16 — SMALL CASES: I0128/Sendov is no longer open, so moderate-degree enumeration is obsolete

Candidate: `I0128`, the queue's “Sendov at moderate degree” replenishment row.

A finite degree-by-degree attack would be exactly the kind of task #16 normally favors. It is now invalid reserve inventory. A fresh current-status search reached Terence Tao's 12 August 2026 post *A digestion of the proof of Sendov's conjecture*. Tao states that Lech Mazur resolved Sendov for all `n>=2` with a Lean-verified proof, and that Tao independently digested/streamlined the argument; he states that the same argument resolves the stronger Phelps--Rodriguez conjecture in full generality.

This is stronger than any “moderate degree” queue target. The newer R06 successor screen independently reached the same disposition.

**Disposition:** `I0128 = KNOWN / RESOLVED / no claim`.

No small-case computation was run because doing so would generate evidence for a problem that no longer remains open in the queued scope.

## 5. Method #26 — SPORADIC CASES: the self-loop and negative-delta PA exceptions I0045/I0046 have been absorbed by later local-limit theory

Candidates: `I0045` and `I0046`, two older preferential-attachment local-limit gaps that look like isolated model exceptions.

For I0045, later local-limit work explicitly says the Pólya-point-tree local weak limit persists for preferential-attachment trees with self-loops (Tiffany Lo, *Local weak limit of preferential attachment random trees with additive fitness*, Adv. Appl. Probab. 56 (2024), 785--824; the published text states that with straightforward modifications the theorem also covers PA trees with self-loops). Van der Hofstad's 2024 *Random Graphs and Complex Networks, Volume 2* and the later Garavaglia--Hazra--van der Hofstad--Ray universality line likewise move beyond the old source gap.

For I0046, the same later theory covers the negative affine-fitness regime that the older source singled out. The current universality paper explicitly incorporates negative preferential-attachment fitness parameters, and the neighboring R08 exact source comparison records that the relevant `(b)` model local convergence holds throughout `delta>-m`.

These are exactly the sort of “sporadic exception” rows that should be hunted before being assigned: in this case the exceptions disappeared into a later general theorem rather than revealing a fresh research obstruction.

**Disposition:** `I0045 = KNOWN / later-literature resolved`; `I0046 = KNOWN / later-literature resolved`; no claims created.

## 6. Current reserve conclusion

This pass therefore removes or quarantines four apparently finite/exceptional queue directions without producing a lawful successor:

- I0045 — later-literature resolved;
- I0046 — later-literature resolved;
- I0048 — main content resolved; residual comparison clause not source-clean enough to dispatch;
- I0128 — full Sendov conjecture resolved, hence moderate-degree row obsolete.

These dispositions are consistent with the newest R08 and task-health screens and strictly shrink the plausible reserve. I did not steal any claimed item, revive any six-run handoff, promote a PENDING/HOLD row automatically, or manufacture a finite milestone inside a hard uniform theorem.

R20 therefore remains `SUCCESSOR_ADMISSION_REQUIRED`.

## 7. Current-source / literature query log and access limits

Fresh web queries run 2026-09-17 UTC included:

- `Randomstrasse 2025 Conjecture 26 Paley graph one-localization Lovasz theta` and exact-title variants — current result: Jig #7 remains `Open`; no source-level resolution recovered.
- `site:terrytao.wordpress.com 2026 Sendov conjecture August 12 digestion proof` — current result: Tao's 2026-08-12 post states full resolution of Sendov and Phelps--Rodriguez.
- `self-loops Pólya point tree preferential attachment local convergence` / `PA^(m,delta)(b) local convergence` — current results: 2024 local-limit literature explicitly covers self-loop variants, and newer universality work includes negative fitness.
- `Hazra van der Hofstad Ray percolation preferential attachment 2026 threshold` — current result: the exact threshold formula and graph/local-limit threshold equality are published/preprinted as above.

These are bounded current-status searches, not exhaustive novelty searches. Search absence is never treated as proof that a question is open; positive later results are used only where their stated scope matches or dominates the queued source clause.

## 8. Why no checker or artifact was created

No new finite mathematical theorem is asserted. The substantive output is source/current-status/ownership discrimination. A checker here would be bookkeeping for a nonexistent active theorem metric and would violate the 90/10 rule. Accordingly no decorative `artifacts/R20/` file was created.

## 9. Model / scheduler control

The limitation remains real in the interface actually exposed to this run. Task management exposes prompt/title, schedule or relative start, timing mode, and enablement. It exposes **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run routing telemetry, and no guaranteed one-hour execution field**. Therefore `GPT-6 / maximum` remains request text, not an auditable setting from this surface.

Making it enforceable requires the authorized owning product/workspace/backend/API to expose persistent model and reasoning fields plus execution telemetry. The historical P26 `You cannot modify this task` event is an authorization-context boundary: the lawful workaround is the owning authorized context, supported ownership/admin transfer, or platform support. Task cloning, GitHub edits, or permission bypasses are not valid fixes. Per the current R20 operational restriction, no scheduler modification was attempted.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R20
  lane: CLOSABLE_OUTSIDE
  active_source: NONE
  preserved_retired:
    id: I0100
    source: "Bandeira et al., Randomstrasse101 Conjecture 26"
    status: OPEN_PARTIAL_RETIRED_HANDOFF
    fixed_metric: "p_max = 1213"
    retained_prime_set: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213]
    retirement_count: 6
    retirement_count_incremented: false
  metric:
    name: E_ready
    before: 0
    after: 0
    movement: false
  status: SUCCESSOR_ADMISSION_REQUIRED
  tried_moves: [8,16,26]
  screened:
    - id: I0048
      disposition: HOLD_LARGELY_RESOLVED_NOT_READY
      action: NO_CLAIM
      remaining_obligation: "exact fixed-edge vs conditionally-independent model comparison clause, if still current and source-matching"
    - id: I0128
      disposition: KNOWN_RESOLVED_FULL_SENDOV
      action: NO_CLAIM
    - id: I0045
      disposition: KNOWN_RESOLVED_LATER_LOCAL_LIMIT
      action: NO_CLAIM
    - id: I0046
      disposition: KNOWN_RESOLVED_LATER_LOCAL_LIMIT
      action: NO_CLAIM
  remaining_obligation: "find a source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successor; create an exclusive claim only after all gates pass"
  evidence:
    - "runs/R20/2026-09-17T20-50-47Z_i0100_stuck_recovery2_rotation_handoff_c6f2a9.md"
    - "runs/R20/2026-09-17T21-58-30Z_successor_admission_screen_4f9c2d.md"
    - "operations/task_health/runs/2026-09-17T215000Z/queue_screening.md"
    - "runs/R08/20260917T223457Z_rotation_preferential_attachment_status_5d8c41.md"
    - "runs/R06/20260917T1917Z_successor_sendov_exclusion_24.md"
  audit_ids: []
  next_moves: [9,22,24]
```

No email/Gmail, Drive, public posting, purchase, paid compute, permission change, shared-root edit, peer-track edit, claim creation, workflow execution, or scheduler modification was performed.