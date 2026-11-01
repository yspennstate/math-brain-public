Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. PENDING_ADMISSION / NO SOURCE-METRIC MOVEMENT: frozen I0056/H_{5,5} width `0 -> 0`; successor metric `UNMEASURED -> UNMEASURED`; `E_READY_CLOSABLE: 0 -> 0`; methods #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #22 READ THE FAILURES NOT THE SUCCESSES, #25 COUNT THE SAME THING TWICE.**

# R06 — successor-admission screen: P0219 survives source/current checks but is not READY

Repository / branch: private `yspennstate/math-open-problems` / `master`.
Deployment: `NEW-METHODS-2026-09-16`.
Predecessor R06 report: `runs/R06/20260919T0021Z_successor_admission_three_fresh_source_shape_screen_53_8b2e.md` @ `198aa744746a6401ea7db3200ff14d3d85c3f86d`.
Fresh prewrite master captured for the exact delta: `590ca571f7a82889f59f020261c653177042a323`.

## 1. Continuity: do not reopen the frozen R06 targets

The original R06 source remains Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20. The question asks for the vertex-isoperimetric constant of regular co-regular plane graphs and, more generally, the edge- and vertex-isoperimetric constants of transitive plane graphs. The frozen R06 subtarget is the regular co-regular tessellation `H_{5,5}` with **outer vertex boundary** normalization. Its rigorously certified interval remains

\[
[L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

The `H_{5,5}` subclass is PROVED/audit-complete in R06 history; the full source question remains PARTIAL. The triangular and quadrangular regimes already covered by Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, remain excluded from any novelty claim.

The later Nielsen-Theorem-4 successor remains `OPEN / PARTIAL / TERMINAL_HANDOFF / ROTATED` after six unchanged runs. It is not reopened here.

## 2. Whole-repository delta and ownership gate

I recovered the controlling roots and current operational state needed for dispatch: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the newest own R06 report, current coordinator/task-health evidence, the fresh neighboring admission reports, and the canonical records for the newly material candidates.

The exact compare from the predecessor commit `198aa744746a6401ea7db3200ff14d3d85c3f86d` to fresh prewrite master `590ca571f7a82889f59f020261c653177042a323` is complete: `ahead_by=105`, `behind_by=0`, `too_large=null`.

Material admission events in that interval:

1. `operations/claims/P0220.md` was created and assigns P0220 exclusively to **R7-04** as CLOSABLE OUTSIDE. R7-04 has already made substantive source-adjacent progress. P0220 is therefore not free inventory and R06 did not duplicate it.
2. R01 surfaced **P0219 — High-density oriented percolation flow asymptotics** as a replenishment lead, but explicitly left it `OPEN_LOOKING_REPLENISHMENT_LEAD_NOT_READY` and created no claim.
3. R7-02 reached a six-run retirement/handoff on **C0134**, but the canonical `operations/claims/C0134.md` still assigns that source to R7-02. A terminal handoff is not an owner-authorized release; C0134 is not free inventory.
4. A direct current fetch of `operations/claims/P0219.md` is still `404 / absent`.
5. The newest coordinator status recovered in this run still records **`E_READY_CLOSABLE: 0 -> 0`** and explicitly forbids creating fictitious READY inventory from stale queue labels or search misses.

Thus the repository ownership gate has not opened a lawful successor for R06.

## 3. P0219 exact outside source and current-status refresh

P0219 is David Aldous's author-hosted open problem, *A discrete Hammersley process as an extreme case of oriented percolation flows*. The live source defines the oriented square-lattice max-flow constant `v(p)` by

\[
\frac{V(n,p)}{2n}\to v(p)\quad\text{in }L^1,
\]

and explicitly conjectures

\[
\boxed{1-v(p)\sim \sqrt{2(1-p)}\qquad(p\uparrow1).}
\]

The page says the conjecture was formulated with Jason Lenderman in 2004, supported by simulation, and identifies the obstruction as an interchange of limits. The author-maintained open-problem index still lists this problem as item 3.4.

Fresh public-source checks dated **2026-09-19 UTC**:

- live source: `https://www.stat.berkeley.edu/~aldous/Research/OP/hammersley_flow.html`;
- author open-problem index: `https://www.stat.berkeley.edu/~aldous/Research/OP/index.html`;
- exact-title query: `"A discrete Hammersley process as an extreme case of oriented percolation flows"`;
- exact-formula query: `"1-v(p)" "sqrt(2(1-p))" oriented percolation flow`;
- author/coauthor query: `"Jason Lenderman" Hammersley oriented percolation flow`;
- mechanism query: `"oriented percolation flows" Hammersley path cover`.

The exact title/formula searches returned the live Aldous page as the source-matching hit and did not expose a later proof or refutation. Related discrete-Hammersley literature, including Ciech--Georgiou (2019) on variance with boundaries, concerns different passage-time questions and does not on its face resolve this max-flow asymptotic. This is bounded negative evidence only: it is **not** a worldwide-openness, novelty, or priority certificate.

Disposition after this refresh: **SOURCE-EXACT / CURRENT-OPEN-LOOKING / UNOWNED-BY-SAME-ID, but still PENDING_NOT_READY under the controlling admission policy.**

## 4. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

The source's heuristic constant should be checked against the actual Hammersley width constant before any future proof attempt.

The repository's prior P0219 attempt already identified two normalization slips in the author-page heuristic. For a Poisson process of intensity `delta` in `[0,n]^2`, scaling coordinates by `sqrt(delta)` gives a unit-intensity process in `[0,n sqrt(delta)]^2`, so

\[
U^*(n,\delta)\stackrel d=U^*(n\sqrt\delta,1),
\]

not `U^*(n/sqrt(delta),1)`. Also, by the chain-cover/antichain correspondence, the unit-intensity square width has leading constant `2m`, not `m`. These two slips cancel at the conjectural endpoint:

\[
\frac{U^*(n,2(1-p))}{2n}
\sim
\frac{2n\sqrt{2(1-p)}}{2n}
=
\sqrt{2(1-p)}.
\]

So the fixed source constant `sqrt(2)` survives the normalization audit. This is not new R06 mathematics; it is recovered prior campaign work that matters for deciding whether P0219 is a clean scalar target.

## 5. Method #22 — READ THE FAILURES, NOT THE SUCCESSES

The prior exact attempt is much more informative than a fresh simulation. Its recorded obstruction is that one still needs a **uniform comparison** of the lattice closed-edge path-cover problem with the continuum antichain problem as `n -> infinity` and `p -> 1`.

That matches the live source's own warning that the heuristic requires a difficult interchange of limits. Finite-grid exact optimization or fixed-`p` convergence is therefore not enough. Any full proof has to control the discrete-to-Poisson approximation on a window that grows with `n` strongly enough to exchange

\[
\lim_{p\uparrow1}\lim_{n\to\infty}.
\]

This is a useful admission fact: the target is a single numerical asymptotic, but its hard step is genuinely uniform and not reducible to a sampled interval or one finite computation.

## 6. Method #25 — COUNT THE SAME THING TWICE

The cleanest prospective route, if P0219 is later admitted, is to make the source complement identity quantitative in two representations of the same obstruction:

1. lattice: minimum number `U(n,p)` of oriented boundary-to-boundary paths needed to cover all closed edges;
2. continuum/poset: minimum increasing-chain cover, equivalently the largest antichain / longest decreasing subsequence of the Poissonized rare-defect set.

The continuum side has the required first-order constant after the normalization correction above. Therefore a source-level proof would follow from a **uniform de-Poissonization / stability estimate** showing that the lattice path-cover density differs from the corresponding Poisson width density by `o(sqrt(1-p))` after taking the infinite-volume limit, uniformly as `p -> 1`.

I do **not** claim such an estimate here. This run is an admission screen, and the owner contract forbids starting substantive research on an unadmitted PENDING lead. The point of method #25 is to isolate exactly what a future admitted proof would have to compare, rather than to manufacture a smaller finite proxy.

## 7. Admission decision

No successor claim was created.

P0219 has now passed a stronger screen than in the preceding R06 report: exact source recovered, current author page and index checked, fixed scalar target retained, prior attempt and obstruction recovered, direct same-ID claim absent, and bounded current literature queries did not reveal a source-matching resolution. Nevertheless, the controlling coordinator still has `E_READY_CLOSABLE=0`, R01 explicitly left P0219 PENDING rather than READY, and the owner directive says **do not promote PENDING to READY automatically**.

Therefore R06 remains:

- status: `PENDING_ADMISSION`;
- successor source: none admitted;
- successor metric: `UNMEASURED -> UNMEASURED`;
- pending-admission waiting does not increment a mathematical stagnation counter.

No checker was made because there is no finite new claim to certify. No email, Drive action, public posting, purchase, permission change, scheduler change, shared-root edit, or other-track edit was made.

## 8. Model / scheduler control boundary

The operative implementation record and current coordinator status remain consistent: the exposed scheduler surface has controls for task identity/title, prompt, schedule/timing mode, and enabled state, but **no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort attestation, and no guaranteed hour-long execution control**. `GPT-6 / maximum` is therefore prompt-only on this surface.

The historical P26 `You cannot modify this task` event was an authorization-context boundary. The lawful workaround is an owning/authorized product/workspace/admin context or platform support, not a worker-side bypass. A real model-control fix would require the scheduler/product/backend to expose persistent model and reasoning fields plus per-run attestation.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  lane: CLOSABLE_OUTSIDE
  deployment: NEW-METHODS-2026-09-16
  frozen_source:
    id: I0056
    source: Lyons-Peres Question 6.20
    graph_class: regular_co-regular_plane_tessellation_H_5_5
    parameters: [5, 5]
    normalization: outer_vertex_boundary
    interval_before: "[sqrt(5), sqrt(5)]"
    interval_after: "[sqrt(5), sqrt(5)]"
    width_before: 0
    width_after: 0
    subclass_status: PROVED_AUDIT_COMPLETE_FROZEN
    full_source_status: PARTIAL
    exclusions:
      - Haslegrave-Panagiotis face degree 3
      - Haslegrave-Panagiotis face degree 4
  current_status: PENDING_ADMISSION
  successor_source_id: null
  successor_claim_id: null
  metric:
    name: successor_metric
    before: UNMEASURED
    after: UNMEASURED
  unchanged_count: UNKNOWN
  coordinator_metric:
    E_READY_CLOSABLE_before: 0
    E_READY_CLOSABLE_after: 0
  tried_moves: [17, 22, 25]
  admission_progress:
    P0220:
      disposition: OWNED_R7_04_NO_DUPLICATE
    C0134:
      disposition: TERMINAL_HANDOFF_BUT_CANONICAL_CLAIM_STILL_R7_02_NO_RELEASE
    P0219:
      title: High-density oriented percolation flow asymptotics
      exact_target: "1-v(p) ~ sqrt(2(1-p)) as p -> 1"
      source_state: SOURCE_EXACT_CURRENT_OPEN_LOOKING
      same_id_claim: ABSENT_AT_SCREEN
      prior_attempt: ATTEMPTED_UNSOLVED
      prior_obstruction: uniform lattice-to-continuum path-cover/antichain comparison
      current_readiness: PENDING_NOT_READY
      disposition: DO_NOT_AUTO_PROMOTE_NO_CLAIM
  remaining_obligation: >-
    Wait for or recover a formally admitted, source-current, full-scope, ownership-clear
    CLOSABLE OUTSIDE successor. P0219 is now a well-supported replenishment candidate,
    but the controlling coordinator/queue has not admitted it and the worker must not
    auto-promote PENDING to READY.
  evidence:
    predecessor_commit: 198aa744746a6401ea7db3200ff14d3d85c3f86d
    prewrite_master: 590ca571f7a82889f59f020261c653177042a323
    compare: "ahead_by=105 behind_by=0 too_large=null"
    coordinator_status: operations/task_health/runs/2026-09-19T005400Z/status.md
    prior_P0219_attempt: probability_1000_intake_claude_20260907/raw/rank_sheet_2026-09-07.txt
    P0219_catalog: probability_campaign_2026_09/report_2026-09-12/chapters/catalog_02_codex_P0151_P0300.md
    P0219_lead: runs/R01/20260919T0103Z_post_rotation_p0219_replenishment_lead_1_10_17_6d2f8a41.md
    P0220_claim: operations/claims/P0220.md
    C0134_claim: operations/claims/C0134.md
```

Next nonrepeating methods if R06 remains pending: **#6 DEFORM TO A POINT YOU CAN SOLVE, #20 FIND WHY THE ALGORITHM FAILS, #29 ADD THE POINTS AT INFINITY**. Apply them to newly admitted/replenishment candidates, not to reopen I0056 or the terminal Nielsen track.