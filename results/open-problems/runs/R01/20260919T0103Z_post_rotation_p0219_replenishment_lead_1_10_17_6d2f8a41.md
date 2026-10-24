Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT: frozen Aldous–Fill I0024 remains `C=1`; R01 successor metric remains `UNMEASURED -> UNMEASURED`; status `PENDING_ADMISSION`; methods #1 CHANGE THE CATEGORY, #10 DERANDOMIZE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE.**

# R01 CLOSABLE OUTSIDE — post-rotation admission screen and P0219 replenishment lead

Repository / branch: `yspennstate/math-open-problems`, `master`.
Deployment: `NEW-METHODS-2026-09-16`.

## 1. Continuity: I0024 remains frozen and is not reopened

I recovered the current campaign roots `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, current `QUEUE.md`, the operative implementation manifest `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the newest own R01 report, current canonical ownership records relevant to the queue screen, and the current intake/catalog evidence needed below.

Aldous–Fill Open Problem 3.44 still asks, in the live source,

> Does there exist a characterization of the relaxation time as exactly an inf over flows?

and Chapter 4 still contrasts this with the non-exact distinguished-path/flow upper bound. The retained R01 characterization remains

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^T C^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

with the frozen source metric `C=1`. The distinct R20 and P26 source-level PASS audits remain the closure evidence already recovered in prior R01 history. I did not re-prove, re-audit, or modify this package.

Live source checked 2026-09-19:
`https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch3.S8.html`.

The terminally handed-off KPS/Nielsen successor is also not reopened. R01 is still waiting for a lawful new CLOSABLE OUTSIDE successor.

## 2. Repository delta since the preceding R01 report

The preceding immutable R01 report is

`runs/R01/20260919T0008Z_post_rotation_boundary_residue_screen_16_23_24_4f8c2a71.md`.

There is one material new canonical-claim delta in the immediately subsequent claim history that affects admission inventory: commit

`b417382e9b9603be16eec70470f90c4292243d3e`

created `operations/claims/P0220.md`, assigning David Aldous's leftmost Hammersley drift-jump stationary-law problem to R7-04 as `CLOSABLE OUTSIDE / CURRENT-OPEN-LOOKING / SOURCE-EXACT`. Thus P0220 is owner-bound and cannot be used as R01's successor.

The current queue continues to warn that a listed candidate is not automatically READY and that absence of a same-ID claim is not sufficient for dispatch. The latest coordinator-era evidence recovered before this run likewise had no lawful free CLOSABLE successor. I therefore treated this run as a source/admission research pass, not as permission to invent a target.

## 3. Method #1 — CHANGE THE CATEGORY

I changed the admission search away from broad probability asymptotics and into the queue's most finite/exact/formalizable categories, because a genuinely CLOSABLE target should be capable of a fixed certificate or exact counterexample rather than another indefinitely moving asymptotic program.

The result is negative but concrete:

- `RS-2026-DC34` is already canonically reserved by C29.
- `RS-2026-DC35` is already canonically owned in a HARD lane.
- In the owner-added famous finite block `I0120`–`I0129`, current canonical claims already own I0120, I0121, I0122, I0123, I0124, I0125, I0126, I0127 and I0129.
- `I0128` (Sendov) has no current same-ID claim, but it is no longer a lawful open-problem successor: by August 2026 the full all-degree Sendov statement had a Lean-checked proof package and Terence Tao's independent digestion/formalization. Current September 2026 literature even treats Sendov as resolved while proving stronger quantitative inequalities. I therefore do not promote I0128 from the stale queue wording.

This category change closes off the obvious “finite famous problem” escape hatch for R01 without stealing another track's work or reviving a now-resolved conjecture.

## 4. Method #10 — DERANDOMIZE

I then tested whether one of the remaining broad random/asymptotic queue rows could be turned into a deterministic finite target without changing the source quantifiers. That shortcut is not lawful in general: a finite deterministic special case is only PARTIAL when the author asks for an asymptotic statement or a classification over all inputs.

The useful positive takeaway is a criterion for future CLOSABLE screening: a deterministic surrogate is admissible only if a proved stability/uniformity theorem converts its finite certificate back to the source statement. Merely enumerating finite instances or freezing one parameter does not do so. I therefore created no artificial metric from a convenient finite proxy.

This matters for the new lead in the next section: its finite max-flow/path-cover instances are exact, but the actual conjecture is an interchange-of-limits statement. A real proof must control that interchange uniformly rather than just compute finite grids.

## 5. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

A more promising source-exact numerical target exists in the repository's older sourced catalog even though it is not presently a dispatchable row of the current `QUEUE.md`:

**P0219 — David Aldous, “A discrete Hammersley process as an extreme case of oriented percolation flows.”**

The live author page defines the oriented-percolation maximal-flow constant `v(p)` by

\[
\frac{V(n,p)}{2n}\to v(p)
\quad\text{in }L^1
\]

and explicitly conjectures

\[
\boxed{1-v(p)\sim \sqrt{2(1-p)}\qquad(p\uparrow1).}
\]

The page explains the expected constant by complementing to a minimum oriented path cover of the closed edges, Poissonizing the rare closed edges at intensity `2(1-p)`, scaling to the continuum Hammersley process, and then notes that the missing step is precisely a difficult interchange of limits. The conjecture was formulated with Jason Lenderman in 2004.

Live source checked 2026-09-19:
`https://www.stat.berkeley.edu/~aldous/Research/OP/hammersley_flow.html`.

Repository evidence already catalogs this exact source as `P0219`, “High-density oriented percolation flow asymptotics,” with status historically attempted-unsolved/current-unverified. A direct current fetch of `operations/claims/P0219.md` returned 404. A bounded fresh web search for the exact formula/title did not recover a later source-matching proof or refutation; the author page remains the dominant exact hit. This negative search is **not** a worldwide-openness or novelty certificate.

This is a substantially better *replenishment lead* than the broad candidates screened in recent R01 runs because it has a source-fixed numerical endpoint. If a coordinator admits it, a natural frozen quantity would be

\[
K_{\rm flow}:=\lim_{p\uparrow1}\frac{1-v(p)}{\sqrt{1-p}},
\]

with target `sqrt(2)`, but **R01 does not initialize this metric now** because P0219 is not currently an admitted/claimed R01 successor.

The most promising actual research route, if admitted later, is not another simulation. It is to prove a uniform de-Poissonization/stability estimate for the minimum oriented path cover which is strong enough to justify

\[
\lim_{p\uparrow1}\lim_{n\to\infty}
\frac{U(n,p)}{2n\sqrt{1-p}}
=
\lim_{m\to\infty}\frac{U^*(m,1)}m\cdot\frac1{\sqrt2},
\]

in the source normalization. The source itself identifies this interchange as the obstruction. That is a concrete route, not a proof claim.

## 6. Admission decision

I did **not** create a successor claim this run.

Reasons:

1. Current canonical queue candidates checked under method #1 are owned, HARD, resolved, or otherwise not READY/free.
2. P0219 is an exact, source-explicit, apparently unowned replenishment lead, but it is not presently a READY row in the controlling queue and has not received a complete coordinator-grade current-literature/later-author/citing-paper admission.
3. The owner contract forbids turning an attractive lead into READY automatically.

So R01 remains `PENDING_ADMISSION`. No checker, audit request, shared-root edit, email, Drive action, public posting, permission change or scheduler change was made.

## 7. Model / scheduler boundary

The operative implementation manifest still records that the exposed scheduler has no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution setting. GPT-6 / maximum therefore remains a prompt request on this surface. The historical P26 `You cannot modify this task` response remains an authorization boundary; the lawful workaround is an owning/authorized product/workspace/API/admin context or platform support, not duplication or permission bypass.

## 8. Structured ledger_delta

```yaml
ledger_delta:
  worker: R01
  lane: CLOSABLE_OUTSIDE
  deployment: NEW-METHODS-2026-09-16
  frozen_source:
    id: I0024
    source: Aldous-Fill Open Problem 3.44
    metric: C
    before: 1
    after: 1
    status: PROVED_FROZEN_DO_NOT_REOPEN
    audit_ids:
      - R20_SOURCE_PASS
      - P26_SOURCE_PASS
  current_status: PENDING_ADMISSION
  successor_source_id: null
  successor_claim_id: null
  metric:
    name: successor_metric
    before: UNMEASURED
    after: UNMEASURED
  unchanged_count: UNKNOWN
  tried_moves: [1, 10, 17]
  mathematical_progress_on_active_successor: false
  admission_progress:
    new_owner_delta:
      P0220: CLAIMED_R7_04_AT_b417382e9b9603be16eec70470f90c4292243d3e
    finite_queue_screen:
      RS-2026-DC34: CLAIMED_C29
      RS-2026-DC35: CLAIMED_HARD
      I0120: CLAIMED
      I0121: CLAIMED
      I0122: CLAIMED
      I0123: CLAIMED
      I0124: CLAIMED
      I0125: CLAIMED
      I0126: CLAIMED
      I0127: CLAIMED
      I0128: RESOLVED_NOT_ADMISSIBLE
      I0129: CLAIMED
    replenishment_lead:
      id: P0219
      source: David Aldous, A discrete Hammersley process as an extreme case of oriented percolation flows
      exact_target: "1-v(p) ~ sqrt(2(1-p)) as p -> 1"
      claim_path: ABSENT_AT_SCREEN
      disposition: OPEN_LOOKING_REPLENISHMENT_LEAD_NOT_READY
  remaining_obligation: >-
    Obtain a source-current, full-scope, CLOSABLE OUTSIDE candidate that is formally admitted
    and unowned under the controlling queue/claim policy. P0219 is a strong replenishment lead
    but must first pass coordinator-grade admission; do not auto-promote it.
  evidence:
    - probability_campaign_2026_09/INDEX.md
    - probability_campaign_2026_09/RANKING.md
    - POSTED.md
    - RESULTS.md
    - QUEUE.md
    - operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md
    - runs/R01/20260919T0008Z_post_rotation_boundary_residue_screen_16_23_24_4f8c2a71.md
    - operations/claims/P0220.md
    - operations/claims/RS-2026-DC34.md
    - operations/claims/RS-2026-DC35.md
    - operations/claims/I0120.md
    - operations/claims/I0121.md
    - operations/claims/I0122.md
    - operations/claims/I0123.md
    - operations/claims/I0124.md
    - operations/claims/I0125.md
    - operations/claims/I0126.md
    - operations/claims/I0127.md
    - operations/claims/I0129.md
    - probability_campaign_2026_09/report_2026-09-12/chapters/catalog_02_codex_P0151_P0300.md
```

Next nonrepeating methods if R01 remains pending: **#6 DEFORM TO A POINT YOU CAN SOLVE, #20 FIND WHY THE ALGORITHM FAILS, #29 ADD THE POINTS AT INFINITY**. Apply them to fresh admission/replenishment candidates, not to reopen I0024 or the terminal KPS target.