Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-run telemetry, so I do not claim otherwise. **Tang remains RETIRED/FROZEN at `UNBOUNDED_ABOVE` with supported unchanged count `6`; successor metric remains `UNMEASURED`. Admission movement this run: `I0033: PENDING_CURRENT_STATUS -> KNOWN / RESOLVED_IN_LITERATURE`; `I0036: source-recovered/unowned -> OPEN_CURRENT_BOUNDED_SEARCH / HARD / NOT_CLOSABLE_FOR_R09`. Methods actually used: #23 DO WHAT THE PROPOSER DID NOT EXPECT, #22 READ THE FAILURES NOT THE SUCCESSES, #18 SAY IT IN ANOTHER LANGUAGE.**

# R09 CLOSABLE OUTSIDE — post-Tang successor admission: I0033 is resolved; I0036 is still a hard SAW scaling-limit problem

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity: Tang remains retired, not reopened

I continued from `runs/R09/20260917T0433Z_rotation_scope_d0012_5c7a91.md`. I did **not** run a seventh Tang research attack. The periodic-tree clause of Pengfei Tang Question 4.11 remains mathematically refuted, independently audited by R08 and P26, and packaged in `paper_tang_q411_periodic_tree_counterexample/`. The separate transitive-graph clause remains open. The frozen Tang metric remains `UNBOUNDED_ABOVE` and its supported unchanged count remains `6` under the CLOSABLE retirement rule.

The active obligation is therefore successor admission: find an exact-source, current-open, unowned, genuinely CLOSABLE outside target without silently converting a HARD asymptotic problem or a source subclass into a fake closure.

## 2. Required repository recovery before screening

I reread/recovered or exact-searched the controlling surfaces before the new status work:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- newest own R09 report `runs/R09/20260917T0433Z_rotation_scope_d0012_5c7a91.md`;
- newest visible coordinator successor screen `operations/task_health/runs/2026-09-17T045900Z/queue_screening.md`;
- newest useful neighboring admission report `proofnet24/P20-closure-log-unimodality/runs/2026-09-17/2026-09-17T05-09-15Z__successor-admission-hold.md`;
- exact I0033/I0034/I0035/I0036 intake rows in `probability_1000_intake_I_20260914/problems.jsonl`;
- canonical claim paths `operations/claims/I0033.md` and `operations/claims/I0036.md`, both returning 404 immediately before this report.

The large intake corpus is connector-truncated when rendered wholesale, so I used exact-ID/source retrieval and do not claim a byte-for-byte visible reread of all intake rows.

The current coordinator screen still says that no candidate in its most recent bounded pass simultaneously cleared READY + CLOSABLE + UNASSIGNED. It specifically left I0031 pending at that time; the newer P20 report has since corrected I0031 to KNOWN via Markowsky--Koolen. This run advances the same current-status cursor through I0033 and I0036 rather than repeating already-consumed candidates.

## 3. I0033 exact source: Aldous--Fill Open Problem 14.12

Source: David Aldous and James Allen Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 14, section 14.3.3, Open Problem 14.12.

The live source page is:

`https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch14.S3.html`

The source studies the full coalescence time `C` of coalescing random walks (equivalently voter-model consensus by duality) on regular graphs. Its exact question is:

> For a sequence of vertex-transitive graphs with `tau_2/tau_0 -> 0`, prove `E C ~ tau_0`.

This matters because the short intake title can be misread as a cover-time problem. It is **not** cover time; `C` here is the coalescence/consensus time defined in section 14.3.

The source itself records only the torus case and a fixed-`k` halfway result (Corollary 14.18).

Immediately before this report, `operations/claims/I0033.md` was absent (404), so there is no canonical owner to race. Ownership, however, is moot because current status is decisive.

## 4. Method #23 — assume the apparently open intake row is already solved

Instead of treating the intake's `open_per_source` flag as current evidence, I searched the **exact problem number and source wording** under the contrary hypothesis that the question had already been solved.

That succeeds cleanly.

Jonathan Hermon, *Some inequalities for reversible Markov chains and branching random walks via spectral optimization*, arXiv:1908.08525 (2019), later published in *Annales de l'Institut Henri Poincaré - Probabilités et Statistiques* **58** (2022), 1650--1668, DOI `10.1214/21-AIHP1208`, states in its abstract that it **resolves Aldous and Fill, Open Problem 14.12**. Hermon proves, for a sequence of reversible chains,

` t_mix^(infinity) = o(t_hit)  iff  gap * t_hit -> infinity `,

with the explicit bound

` t_mix^(infinity) <= (1/gap) log(e t_hit gap) `,

and identifies this as the missing implication needed for the transitive coalescing-time conjecture.

Primary links:

- `https://arxiv.org/abs/1908.08525`
- publication DOI: `https://doi.org/10.1214/21-AIHP1208`

Outcome of #23: **I0033 is not an open successor. It is source-numbered KNOWN / RESOLVED_IN_LITERATURE.**

## 5. Method #22 — read the near-miss that explains what was missing

The historical near-solution is Roberto Imbuzeiro Oliveira, *Mean field conditions for coalescing random walks*, arXiv:1109.5684 (later *Annals of Probability*). Its abstract proves mean-field coalescence on vertex-transitive graphs when the mixing time is much smaller than the mean meeting time and explicitly says this **nearly solves** an Aldous--Fill open problem.

Primary link:

`https://arxiv.org/abs/1109.5684`

This explains the exact historical obstruction rather than merely supplying a later citation: Oliveira had the coalescing-walk theorem under a mixing-time hypothesis; Hermon's spectral optimization establishes the mixing/hitting equivalence needed to pass from the Aldous--Fill spectral-gap condition to that mean-field regime.

Outcome of #22: the status change is not a keyword accident. It has a coherent proof-history chain: **Aldous--Fill formulation -> Oliveira near-solution -> Hermon missing spectral/mixing bridge -> explicit source-numbered resolution.**

## 6. Method #18 — translate the source notation before searching

The useful language change was to stop searching only for the printed symbols `tau_2/tau_0` and rewrite the problem in modern Markov-chain terminology: relaxation/spectral-gap scale versus hitting/meeting scale, `L^infinity` mixing, and mean-field coalescence. That translation is exactly the vocabulary of Hermon's paper.

I do not need to infer a source match solely from notation: Hermon's abstract explicitly names **Open Problem 14.12**, which removes the main scope risk.

Outcome of #18: source fidelity is stronger after translation, because it locates a paper that self-identifies the exact numbered problem rather than a merely similar coalescence theorem.

## 7. I0033 disposition

The dated 2026-09-17 disposition is:

`I0033 = KNOWN / RESOLVED_IN_LITERATURE / NOT ELIGIBLE FOR R09`.

This is the exact Open Problem 14.12 clause `EC ~ tau_0` under vertex transitivity and `tau_2/tau_0 -> 0`.

No claim is created. No checker is needed: this run's substantive conclusion is a literature/source correction, not a new finite mathematical theorem.

## 8. Cursor advance to I0036 — Schramm Problem 2.1

The next useful unclaimed row I screened is I0036.

Source: Oded Schramm, *Conformally invariant scaling limits: an overview and a collection of problems*, ICM 2006, arXiv:math/0602151, Problem 2.1.

Primary source:

`https://arxiv.org/abs/math/0602151`

The intake freezes the half-plane self-avoiding-walk statement: construct the infinite-volume limit of uniform `n`-step self-avoiding walks in the upper half-plane and prove that the small-scale rescaling limit exists and is `SLE_{8/3}` (under either topology discussed by Schramm).

Current ownership: `operations/claims/I0036.md` returned 404 immediately before this report; repository search recovered only intake copies, not a current exclusive owner.

### Current-status search, 2026-09-17

Fresh exact-phrase and SAW/SLE8/3 searches did **not** surface a source-matching later proof. The current mathematical picture remains that planar fixed-lattice SAW convergence to `SLE_{8/3}` is conjectural.

Relevant progress is substantial but not source-closing:

- Duminil-Copin--Smirnov prove the exact honeycomb connective constant and explicitly note that an additional missing discrete-holomorphic relation would imply `SLE_{8/3}` convergence; this is not the scaling-limit proof.
- Krachun--Panagiotis, arXiv:2310.17299, prove quantitative sub-ballisticity on the hexagonal lattice, still far short of a planar scaling-limit theorem.
- random-planar-map SAW-to-SLE results concern a different geometry and do not settle fixed-lattice Problem 2.1.
- recent survey/expository sources still describe existence/conformal invariance of the two-dimensional SAW scaling limit as a difficult open problem.

This is a bounded dated status screen, not a global novelty certificate.

### CLOSABLE test

The source obligation is an asymptotic scaling-limit theorem involving tightness/existence, identification, and conformal/SLE structure. There is no source-frozen finite case count, sharp scalar constant, or one finite counterexample whose verification would naturally close the statement. A special lattice estimate, exponent bound, or conditional identification would be **PARTIAL**, not source closure.

Therefore:

`I0036 = OPEN_CURRENT (bounded dated search) / UNOWNED_IN_CANONICAL_CLAIM_PATH / HARD / NOT_CLOSABLE_FOR_R09`.

No claim is created and no successor metric is started.

## 9. Admission state after this run

This run materially clears two stale possibilities without fabricating a successor:

- `I0033`: **KNOWN / literature-resolved** by Hermon, exact source number named;
- `I0036`: **OPEN-looking/current but HARD**, not a lawful CLOSABLE replacement.

R09 therefore remains:

**`ROTATION_HOLD / SUCCESSOR_ADMISSION_REQUIRED`**

with successor metric still **`UNMEASURED`**.

This is preferable to taking I0036 merely because it is famous/open, narrowing it to a tractable lemma and calling the parent solved, or reopening Tang after its six-run retirement.

The next admission pass should continue beyond already-screened/claimed rows and prioritize an explicit short counterexample/constant/construction target that is both source-exact and currently unowned. Do not rescreen I0006, I0031, I0033, D0012, or the Kireeva rows absent materially new evidence.

## 10. Model/reasoning and task-permission status

The model-control limitation is still real: the exposed task-management schema has prompt/title/schedule/timing/enabled controls but **no model-family field, no reasoning-effort field, and no authenticated applied-run telemetry**. GPT-6/maximum remains a prompt request only in this runtime.

There is, however, an important permission update in the current root ledger: the earlier P26 `You cannot modify this task` result was context-dependent. `RESULTS.md` now records that the full P26 prompt update **succeeded from a different authorized context**, while another exposed context still rejected P26/P01/P03 and all R-series edits. Thus the legitimate workaround was exactly the authorized owning context, not a duplicate schedule or a permission bypass.

Actually forcing and verifying GPT-6/maximum still requires the product/API or owning workspace to expose model and reasoning selectors plus runtime telemetry. No scheduler modification was attempted here.

## 11. Prohibited-action audit

No Gmail/email, Drive write, public posting, purchase, permission change, workflow execution, scheduler mutation, shared-root edit, peer-file edit, force-push, or extra schedule was performed. No checker-only artifact was created because there was no new finite claim to certify.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R09
  run_id: 20260917T0535Z_rotation_i0033_resolution_i0036_hard_91c7e2
  predecessor:
    source: "Tang arXiv:2012.01135, source-PDF Question 4.11"
    metric: "greatest rigorous lower bound for theta'' at a certified admissible parameter in the fixed periodic-tree family"
    before: UNBOUNDED_ABOVE
    after: UNBOUNDED_ABOVE
    unchanged_count: 6
    state: RETIRED_FROZEN
  methods_this_run: [23, 22, 18]
  successor_screen:
    I0033:
      source: "Aldous-Fill Open Problem 14.12, section 14.3.3"
      exact_scope: "vertex-transitive tau_2/tau_0 -> 0 implies mean coalescence time EC ~ tau_0"
      ownership: "operations/claims/I0033.md absent immediately before report"
      decisive_literature: "Jonathan Hermon, arXiv:1908.08525 / AIHP 58 (2022), explicitly states it resolves Open Problem 14.12"
      historical_bridge: "Oliveira arXiv:1109.5684 nearly solved the problem under a stronger mixing condition"
      disposition: KNOWN_RESOLVED_IN_LITERATURE
      claim_created: false
    I0036:
      source: "Oded Schramm, ICM 2006, Problem 2.1, arXiv:math/0602151"
      exact_scope: "half-plane planar SAW scaling limit exists and is SLE_8/3"
      ownership: "operations/claims/I0036.md absent immediately before report"
      current_status: "OPEN_CURRENT_BOUNDED_2026_09_17_SEARCH"
      lane_fit: HARD_NOT_CLOSABLE_FOR_R09
      claim_created: false
  successor_metric: UNMEASURED
  overall: ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
  new_exact_artifact: NONE_SOURCE_STATUS_ADMISSION_RUN
```
