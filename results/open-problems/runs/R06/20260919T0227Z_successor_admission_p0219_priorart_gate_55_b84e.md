Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. PENDING_ADMISSION / NO SOURCE-METRIC MOVEMENT: frozen I0056/H_{5,5} width `0 -> 0`; successor metric `UNMEASURED -> UNMEASURED`; `E_READY_CLOSABLE: 0 -> 0`; methods #3, #16, #23.**

# R06 — successor-admission delta / P0219 prior-art gate

Repository: private `yspennstate/math-open-problems`, branch `master`.

## 1. Frozen R06 source remains frozen

I recovered the current R06 state before doing any new screening. The original source remains Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake I0056:

> What is `Phi_V(G)` for regular co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive plane graphs `G`?

The frozen R06 subclass is the regular co-regular tessellation `H_{5,5}` with outer vertex boundary normalization. Its certified interval remains

\[
[L,U]=[\sqrt 5,\sqrt 5],\qquad U-L=0.
\]

The `H_{5,5}` subtarget remains PROVED/audit-complete; the full Question 6.20 remains PARTIAL. I did not reopen the proof, rerun a checker, or relabel the full source question as solved.

Fresh dated source/literature checks on 2026-09-19 recovered the exact Question 6.20 text and Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`. Their paper explicitly establishes the vertex-isoperimetric constant for triangular and square hyperbolic lattices and describes those cases as answering a question of Lyons and Peres. Those face-degree 3/4 cases remain excluded from R06 novelty. A bounded search for later broader regular co-regular plane-graph vertex-isoperimetry found no source-status change that would reopen or supersede the frozen R06 record. This is bounded negative evidence, not a universal priority certificate.

The later Nielsen-Theorem-4 successor remains terminally handed off after six supported unchanged runs and was not reopened.

## 2. Repository continuity and exact delta

Previous own immutable report:

`runs/R06/20260919T0127Z_successor_admission_p0219_source_current_uniformity_gate_54_a53c.md`

creation commit:

`07dad0a9301d7b73e77be22c724207a41ca719b0`.

I recovered/re-read the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the operative `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the newest R06 report, newest neighboring admission reports, the current coordinator state, and the relevant P0219 source/prior-attempt records. Unchanged oversized intake ledgers were handled by exact-ID/path continuity rather than pretending to visually reread every byte.

The exact GitHub compare from the R06 predecessor commit to the captured prewrite master

`759e99c3e471e6d34f9ec94a6be93e3bc1ff945e`

is complete: **79 commits ahead / 0 behind**, `too_large=null`.

In that entire delta:

- the only added canonical claim file is `operations/claims/H0008.md`;
- H0008 is explicitly HARD OUTSIDE and owned by R14;
- there is no canonical claim deletion/release in the compared file set;
- no root `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md`/`RANKING.md`, or intake `problems.jsonl` mutation appears;
- the newest coordinator state still reports `E_READY_CLOSABLE: 0 -> 0`.

Therefore there is still no lawful ownership-clear source-current CLOSABLE successor for R06 to claim. No claim was created and no successor metric was initialized.

## 3. Neighbor update changes how P0219 must be screened

Immediately before this R06 run, R01 published

`runs/R01/20260919T0216Z_p0219_seppalainen_bridge_screen_6_20_29_c8e5f1a3.md`.

That neighboring report used the exact planned R06 triple #6/#20/#29 on P0219, so under the owner instruction to check history and replace exhausted methods I did **not** duplicate that attack. I replaced the triple with #3/#16/#23 for admission screening.

The R01 report materially sharpened P0219 without admitting it. The source is David Aldous, *A discrete Hammersley process as an extreme case of oriented percolation flows*, with

\[
1-v(p)\sim \sqrt{2(1-p)}\qquad (p\uparrow1).
\]

Aldous's live page still states the conjecture and says the obstacle is an interchange of limits. R01 found a much closer prior-art bridge: Timo Seppäläinen, *Increasing sequences of independent points on the planar lattice*, Ann. Appl. Probab. 7 (1997), DOI `10.1214/aoap/1043862416`, which exactly solves an independent Bernoulli lattice Hammersley problem and has the same low-density `2 sqrt(r)` leading law.

R01 then separated the source problem into a Bernoulli-width term and a routing-tax term. If `W(n,q)` is the width of the reachability poset of closed directed edges and `U(n,1-q)` is Aldous's minimum number of edge-disjoint covering paths, then deterministically

\[
W(n,q)\le U(n,1-q).
\]

What is still missing is (i) an exact or asymptotically controlled identification of the two-orientation edge-midpoint model with a known strict/weak Bernoulli Hammersley/LPP model, and (ii) control of the routing tax

\[
U(n,1-q)-W(n,q)=o(n\sqrt q)
\]

in the source's sequential limit.

I treat these as neighboring evidence, not as R06 discoveries.

## 4. Method #3 — prove something stronger: strengthen the admission gate, not the theorem

For P0219 it is no longer enough to certify only `source-current + unowned + explicit conjecture`. The new Seppäläinen bridge means a responsible READY certificate must be stronger:

1. identify the exact discrete partial order induced by Aldous's two edge orientations;
2. distinguish it from already solved strict and weak Bernoulli Hammersley/LPP models;
3. show that the edge-disjoint routing tax is not already covered by a known max-flow/LPP equivalence;
4. retain a single frozen source metric and a genuinely closable obligation.

This stronger gate is not yet met. Therefore P0219 remains `PENDING_NOT_READY`, despite being a very promising replenishment lead.

Outcome #3: **stronger admission criterion established; no target promotion and no metric movement.**

## 5. Method #16 — compute every small case: exact finite repository delta

I used the exact GitHub commit comparison as the finite operational enumeration rather than guessing from filenames. Across all 79 commits since the previous R06 run, every changed file is accounted for by the compare response. The only canonical claim addition is H0008 and it is already HARD-owned by R14; no canonical claim release/deletion occurs.

This finite delta check rules out a silent free CLOSABLE handoff inside the changed-file set. It does **not** prove that the entire historical queue contains no future-admissible problem; it proves only the exact operational statement needed for this run: no new release/admission trigger appeared in the repository delta.

Outcome #16: **no dispatchable CLOSABLE successor appears in the exact delta.**

## 6. Method #23 — assume the P0219 conjecture is already a disguised known theorem

I searched in the direction opposite to novelty: assume Aldous's closed-edge cover is already a standard Bernoulli Hammersley/LPP object and try to locate the identification.

Fresh dated searches on 2026-09-19 recovered:

- Aldous's live source page with the exact conjecture and interchange-of-limits warning;
- Seppäläinen 1997, which solves independent marked points on the planar square lattice;
- Georgiou 2010, which treats strictly increasing Bernoulli lattice paths and emphasizes strict/weak boundary distinctions;
- standard later Hammersley/LPP references citing Seppäläinen.

The bounded search did **not** recover a paper explicitly identifying Aldous's two-orientation closed-edge, edge-disjoint path-cover functional with Seppäläinen's solved model. That negative search result is not a novelty certificate. It instead raises the admission obligation: before P0219 can be called a fresh closable source, the exact max-flow/min-cut/poset representation must be matched against the Bernoulli-LPP literature.

Outcome #23: **P0219 remains current-open-looking but prior-art-sensitive and PENDING_NOT_READY.**

## 7. Current state / remaining obligation

R06 remains `PENDING_ADMISSION`.

No new mathematical stagnation count starts while no successor is admitted. The successor metric remains

`UNMEASURED -> UNMEASURED`.

The highest-value next event is one of:

- a coordinator-grade admission of P0219 after the Bernoulli-LPP/routing-tax identity is settled at source scope;
- an owner-authorized release of an existing CLOSABLE claim;
- or a genuinely new source-current CLOSABLE outside item with exact source, scope, metric, prior-art screen, and ownership clearance.

Until one of those occurs, R06 must not manufacture a claim, reopen I0056, or restart the rotated Nielsen target.

No checker was created because this run made no new finite mathematical claim. No audit was requested. No shared root, other-track immutable file, email, Drive item, public posting, purchase, permission, or scheduler setting was modified.

## 8. Model / scheduler control status

The limitation remains true in this run. The exposed task-control surface provides task identity/title, prompt, schedule/timing information, timing mode, notification/email flags, enabled state, and run timestamps. It exposes **no binding model-family selector, no binding reasoning-effort selector, no authenticated per-run model/effort receipt, and no guaranteed hour-long execution field**. GPT-6/maximum therefore remains prompt text only on this surface.

A real fix requires the owning product/platform scheduler or workspace API to expose persistent authorized `model` and `reasoning_effort` (or equivalent) fields and trustworthy per-run attestation. Prompt text cannot make those settings binding.

The historical P26 `You cannot modify this task` event remains an authorization/context boundary. Repository history records later successful P26 prompt work from an authorized context. The lawful workaround is the owning authorized workspace/account/admin context or platform support, not task duplication or permission bypass.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R06
  category: CLOSABLE_OUTSIDE
  frozen_source:
    id: I0056
    source: "Lyons--Peres, Probability on Trees and Networks, Question 6.20"
    graph_class: "regular co-regular plane tessellation H_{5,5}"
    parameters: [5, 5]
    normalization: "outer vertex boundary"
    metric_name: "certified interval width U-L for Phi_V(H_{5,5})"
    interval_before: "[sqrt(5), sqrt(5)]"
    interval_after: "[sqrt(5), sqrt(5)]"
    metric_before: 0
    metric_after: 0
    status: "PROVED_FROZEN_SUBCLASS; FULL_SOURCE_PARTIAL"
    excluded_prior_art: "Haslegrave--Panagiotis face degrees 3 and 4, DOI 10.1002/rsa.20946"
  active_successor:
    claim: null
    state_before: PENDING_ADMISSION
    state_after: PENDING_ADMISSION
    metric_name: UNMEASURED
    metric_before: UNMEASURED
    metric_after: UNMEASURED
    movement: false
    unchanged_runs: NOT_STARTED
  tried_moves: [3, 16, 23]
  method_scope: "ADMISSION_AND_PRIOR_ART_SCREEN"
  repository_delta:
    base: "07dad0a9301d7b73e77be22c724207a41ca719b0"
    prewrite_head: "759e99c3e471e6d34f9ec94a6be93e3bc1ff945e"
    ahead_by: 79
    behind_by: 0
    too_large: false
    added_canonical_claims: ["H0008_HARD_OWNED_R14"]
    canonical_claim_releases_seen: []
    free_ready_closable_delta: "0 -> 0"
  replenishment_lead:
    id: P0219
    title: "High-density oriented percolation flow asymptotics"
    lifecycle: PENDING_NOT_READY
    same_id_claim: ABSENT_AT_SCREEN
    source_endpoint: "1-v(p) ~ sqrt(2(1-p)) as p -> 1"
    neighbor_new_prior_art: "Seppalainen 1997 exact Bernoulli lattice Hammersley model"
    admission_blockers:
      - "exact identification/distinction of Aldous two-orientation edge model versus known strict/weak Bernoulli Hammersley/LPP"
      - "routing-tax control U-W=o(n sqrt(q)) in source sequential limit, or proof that a known theorem already gives it"
      - "coordinator-grade READY certification"
  remaining_obligation: >-
    Wait for or produce a lawful source-current ownership-clear CLOSABLE admission.
    Do not reopen I0056 or the rotated Nielsen successor, and do not promote P0219
    until its Bernoulli-LPP prior-art identity and routing-tax scope are settled.
  evidence:
    original_source_checked_utc: 2026-09-19
    current_literature_checked_utc: 2026-09-19
    exact_repo_delta_checked: true
    audits_requested: []
    checker_created: false
```
