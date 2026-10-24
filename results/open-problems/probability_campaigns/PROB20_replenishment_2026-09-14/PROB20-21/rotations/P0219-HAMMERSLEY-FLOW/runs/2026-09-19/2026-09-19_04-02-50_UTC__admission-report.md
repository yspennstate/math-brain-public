Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. ADMISSION MOVEMENT: successor lifecycle `PENDING_NOT_READY -> CLAIMED / MANUALLY ADMITTED / CLOSABLE OUTSIDE`; fresh metric `alpha_tax` starts at `0` with unchanged count `0`. This is an admission run, not a P0219 research run.**

# P0219 successor admission — high-density oriented percolation flow asymptotics

Date: 2026-09-19 UTC.
Native slot: `6aa7ebbe26308191a40003a950a2307a`.
Captured pre-claim master: `72ff2b7e1a2702f1d0e8219c089b72bfbc86e515`.
Canonical claim creation commit: `cbbefa596e5a70740721460505d6733626322483`.
Canonical claim: `operations/claims/P0219.md`.
Status: **OPEN / admitted CLOSABLE OUTSIDE**.
Novelty/priority: **UNVERIFIED**.

## 1. Predecessor handoff preserved

The previous target `NEUNHAEUSERER-2026-ENTROPY` is operationally RETIRED after six supported unchanged runs and was not restarted in this run.

Complete retirement handoff:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-21/rotations/NEUNHAEUSERER-2026-ENTROPY/runs/2026-09-18/2026-09-18_21-06-14_UTC__report.md`

creation commit `d9085bee2ce5ab773b3ca87448ea1036956e3687`, report blob `59b3de639bf6a3dcee1b3ee3a1650e40e49b5cba`.

Preserved predecessor mathematical state: source OPEN; track PARTIAL; `m_all=5`; remaining depth-six frontier relation rank `>=3`; independent full-claim audits `0/2`; novelty UNVERIFIED. None of those metrics or stagnation counters are inherited by P0219.

## 2. Repository-wide exclusion / ownership screen

Before admission I reread the controlling current repository state relevant to dispatch:

- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`;
- root `RESULTS.md`;
- root `QUEUE.md`, including its dated admission/disposition passes and the I0120–I0129 block;
- current canonical `operations/claims/` records for the strongest formerly-free CLOSABLE candidates;
- current P0219 reports in R01, R06, P13 and admission-screen tracks;
- the P0219 intake/catalog provenance recovered in the repository search (`P0219`, `High-density oriented percolation flow asymptotics`).

The current exact ownership screen matters because the queue contains stale historical `READY / UNASSIGNED` labels. In particular, I0004 is now claimed by P21 and I0075 is claimed by another preserved native slot. The owner-added finite block I0120–I0129 is no longer free inventory: I0120–I0127 and I0129 have canonical claims, while I0128/Sendov is resolved and not admissible. Other prominent READY-era rows are claimed, resolved, HARD, or otherwise not presently lawful CLOSABLE successors.

Immediately before P0219 claim creation, direct fetch of `operations/claims/P0219.md` returned `404`. Repository-wide exact-ID/title search found P0219 repeatedly as a `PENDING_NOT_READY` replenishment lead, but no canonical claim or exclusive owner. Therefore this admission did not steal or double-dispatch an existing source claim.

No shared `RESULTS.md`, `QUEUE.md`, `POSTED.md`, campaign `INDEX.md`, `RANKING.md`, or peer immutable report was edited by this worker.

## 3. Outside source and exact target

Outside source: David Aldous, *A discrete Hammersley process as an extreme case of oriented percolation flows*.

Live source page checked 2026-09-19:

`https://www.stat.berkeley.edu/~aldous/Research/OP/hammersley_flow.html`

Aldous defines `V(n,p)` as the maximum number of edge-disjoint open up/right paths from the left/bottom source boundary to the top/right sink boundary of the `n x n` oriented square lattice and states that

`V(n,p)/(2n) -> v(p)` in `L^1` as `n -> infinity`.

The exact source conjecture is

`1 - v(p) ~ sqrt(2(1-p))` as `p -> 1`.

The live page still labels this as `Conjecture`, says the continuum-Hammersley heuristic involves a difficult interchange of limits, and records that Aldous and Jason Lenderman formulated it in 2004 without proving it.

Aldous's live Open Problems index was also checked 2026-09-19:

`https://www.stat.berkeley.edu/~aldous/Research/OP/index.html`

and still lists this problem among the current `Open research problems`, not in the former/solved section. The index itself warns that updates can be incomplete, so this was not treated as sufficient current-status evidence by itself.

## 4. Dated current / later / citing check

Fresh bounded web searches on 2026-09-19 used the exact Aldous title, the displayed asymptotic `1-v(p) ~ sqrt(2(1-p))`, Aldous/Lenderman terms, `oriented percolation flows`, Hammersley, and same-shape Bernoulli first-passage-percolation queries. They recovered the maintained Aldous source and nearby FPP literature but no later primary source proving or refuting this exact flow asymptotic. This is bounded negative evidence only; it does not certify worldwide openness or novelty.

The most important nearby prior art recovered and checked is:

Anne-Laure Basdevant, Jean-Baptiste Gouéré, Marie Théret, *First-order behavior of the time constant in Bernoulli first-passage percolation*, Annals of Applied Probability 32 (2022), 4535–4567, DOI `10.1214/22-AAP1795`, arXiv:2106.12266.

That paper proves a first-order small-defect expansion for the ordinary Bernoulli FPP time constant. It does not directly state or settle Aldous's flow conjecture.

The current repository's 2026-09-19 P0219 work makes the distinction explicit: planar duality turns the Aldous deficit into a first-passage functional in which backward dual crossings are free, whereas ordinary Bernoulli FPP charges them. P13 has an exact finite routing-tax witness showing that this free-backstep functional can differ from the monotone Hammersley width, so a literal identification with standard FPP is false.

## 5. Preserved P0219 work before admission

Admission starts from, rather than erases, the useful pre-admission work already in the repository.

### R01: one-sided source bound and free-backstep reduction

Current R01 report:

`runs/R01/20260919T0343Z_p0219_basdevant_free_backstep_reduction_21_18_4_b7a3c912.md`.

It derives from the published 2022 FPP theorem plus planar duality the source-valid one-sided inequality

`liminf_{p->1} (1-v(p))/sqrt(1-p) >= sqrt(2)`.

It explicitly labels this as a derived corollary of prior art, not a novelty claim. It reduces the missing direction to proving first-order equivalence for the free-backstep passage model or, equivalently, that the routing-tax gain is negligible on square-root scale.

### P13: exact deterministic routing dual and finite obstruction

Current neighboring P13 work derives the exact deterministic cut/path-cover dual for `U_n(C)` and finds an exact finite witness with monotone width `W=2` but path-cover number `U=3`. Thus the stronger shortcut `U=W` is false.

### R06: sparse-defect structural theorem

Current R06 work proves, conditional only on the already written deterministic dual, that routing tax vanishes for every closed-edge set of cardinality at most three on every grid size; the first possible routing-tax obstruction has four closed edges, and at four edges the tax is at most one. This is useful structural evidence but does not by itself control the thermodynamic `n -> infinity` limit uniformly as `q=1-p -> 0`.

These results are inherited evidence. Admission itself claims no new P0219 theorem.

## 6. Why this target is classified CLOSABLE rather than HARD

The source target has an exact asymptotic exponent and leading constant and has now been reduced to one quantitative uniformity obstruction. The continuum/Hammersley coefficient is already supplied by published first-order Bernoulli-FPP machinery; the remaining difference is a specific routing/free-backstep correction whose deterministic obstruction has an exact finite dual and whose smallest nonzero local mechanism is already isolated.

That combination gives a plausible finite-to-asymptotic route: prove a cluster/routing-tax estimate strictly smaller than square-root order. This is materially more bounded than a broad open classification problem. The label is operational, not a promise that the conjecture will close.

## 7. Fresh metric

Set `q=1-p`. Let `C_q` be the Bernoulli closed-edge set. Let `U_n(C_q)` be Aldous's minimum source-to-sink path-cover count and let `W_n(C_q)` be the corresponding monotone-Hammersley/reachability-poset width appearing in the current reduction.

Define

`T(q) = limsup_{n->infinity} E[U_n(C_q)-W_n(C_q)]/n`.

The new frozen metric is

`alpha_tax = sup { alpha >= 0 : a complete source-valid proof establishes T(q)=O(q^alpha) as q->0 }`.

Admission value: **`alpha_tax: 0 -> 0`**.

Admission unchanged count: **0**.

The baseline `0` uses only the trivial order-one normalized bound and does not import any Neunhaeuserer quantity. Movement requires a written uniform asymptotic routing-tax theorem, not a finite search or isolated defect calculation. Any rigorously proved `alpha_tax>0` is meaningful progress. A bound `alpha_tax>1/2`, or directly `T(q)=o(sqrt(q))`, closes the missing first-order direction when combined with the preserved published/derived Hammersley term. Source closure still requires the full source argument and the normal closure protocol, including prior-art reconciliation and two independent audits.

## 8. First research-run methods

This admission report does not spend a research cycle. The first P0219 research run must use the following fresh triple:

- **B2 ATTACK THE NEGATION FIRST:** seek a source-valid family of defect/routing configurations whose normalized routing-tax contribution is genuinely of order `sqrt(q)`; a certified construction would directly challenge the conjectured coefficient.
- **B5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** interpolate a backward-crossing cost `lambda in [0,1]`, with `lambda=0` the P0219 free-backstep model and `lambda=1` ordinary Bernoulli FPP, then seek a derivative bound on the time constant that is `o(sqrt(q))` uniformly as `q->0`.
- **B30 DO ONE SCALE / ONE DIRECTION AT A TIME:** decompose the routing-tax gain by local defect-cluster scale and geometry; prove that the four-defect mechanism and its higher clusters contribute at an exponent strictly above `1/2` after the thermodynamic limit.

The run must read the R01/R06/P13 P0219 work above before deriving anything. It must not restart from Aldous's heuristic or regenerate a small-grid checker merely because one exists.

## 9. Model / scheduler control truth

The exposed scheduler surface still provides title, prompt, schedule/timing and enabled state but no binding model-family selector, reasoning-effort selector, authenticated applied-model receipt, or guaranteed hour-long execution setting. `GPT-6 / maximum` therefore remains a prompt request only on this surface. This report truthfully records the model actually exposed here as GPT-5.6 Sol and the reasoning level as UNVERIFIED.

A historical `You cannot modify this task` error on another task is treated as an ownership/authorization boundary. The lawful workaround remains an authorized owning context or platform/admin repair, never duplication or bypass.

## 10. Admission / successor state

P0219 is now formally admitted and exclusively claimed by native slot `6aa7ebbe26308191a40003a950a2307a`. The native slot is to rotate in place from successor-admission gate to active P0219 research; no new scheduler ID is authorized or needed.

Research status at the moment of admission: **OPEN**.
Track status: **ACTIVE / CLOSABLE OUTSIDE**.
Fresh unchanged count: **0**.
Six-supported-unchanged-run retirement rule: **applies from the first P0219 research report**.
Independent P0219 source-closure audits: **0/2**.

## ledger_delta

```yaml
ledger_delta:
  native_id: 6aa7ebbe26308191a40003a950a2307a
  predecessor:
    target: NEUNHAEUSERER-2026-ENTROPY
    lifecycle: RETIRED_PRESERVED
    handoff: probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-21/rotations/NEUNHAEUSERER-2026-ENTROPY/runs/2026-09-18/2026-09-18_21-06-14_UTC__report.md
    creation_commit: d9085bee2ce5ab773b3ca87448ea1036956e3687
    report_blob: 59b3de639bf6a3dcee1b3ee3a1650e40e49b5cba
  successor:
    id: P0219
    canonical_key: high-density_oriented_percolation_flow_asymptotics
    source: David Aldous, A discrete Hammersley process as an extreme case of oriented percolation flows
    claim: operations/claims/P0219.md
    claim_creation_commit: cbbefa596e5a70740721460505d6733626322483
    lifecycle_before: PENDING_NOT_READY
    lifecycle_after: CLAIMED_MANUALLY_ADMITTED_CLOSABLE_OUTSIDE
    source_status: OPEN
    novelty_priority: UNVERIFIED
  metric:
    name: alpha_tax
    before: 0
    after: 0
    unchanged_count: 0
    closure_threshold: "alpha_tax>1/2 or directly T(q)=o(sqrt(q)), plus full source argument"
  preserved_partial_results:
    source_liminf: ">= sqrt(2), derived from published 2022 FPP prior art plus planar duality"
    finite_routing_tax_witness: "exists; U=3, W=2"
    sparse_defect_fact: "routing tax zero for <=3 defects; first possible at 4"
  first_research_moves: [2, 5, 30]
  audits: 0/2
  captured_preclaim_master: 72ff2b7e1a2702f1d0e8219c089b72bfbc86e515
  report_path: probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-21/rotations/P0219-HAMMERSLEY-FLOW/runs/2026-09-19/2026-09-19_04-02-50_UTC__admission-report.md
```
