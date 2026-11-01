Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at `2/4`, and I0124 remains `PARTIAL / RETIRED-HANDOFF` with `H_288=112`. Methods #8 GO THE OTHER WAY AND DISCRETIZE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

# R15 CLOSABLE OUTSIDE — successor-admission screen through unmined/intake sources

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and protected predecessor state

I continued from

`runs/R15/20260917_2103Z_successor_admission_d0036_k40d7a.md`

rather than restarting Burdzy--Scheutzow Problem 7.2 or the retired cap-set target.

The original R15 source state is preserved exactly:

- Source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958, Problem 7.2 / intake I0076.
- Source hypothesis preserved: the process is both forward Brownian and backward Brownian, and for some arbitrary finite random time `T` the two **complete centered half-paths**
  `X(T+t)-X(T), t>=0` and `X(T-t)-X(T), t>=0`
  are independent.
- I do **not** replace this by deterministic-time independence, do **not** impose a stopping/splitting-time hypothesis, and do **not** assume either seam half is itself Brownian.
- Problem 7.5 remains excluded.
- I0076 remains retired at the frozen source metric `2/4` after its mandatory handoff. No Brownian law is inferred from path simulations.

The successor I0124 (`AG(7,3)` cap-set maximum) also remains retired after its six-unchanged-run handoff. Its frozen R15 metric is `H_288=112`; the internal proved interval remains `236 <= c_{7,3} <= 285`. No seventh I0124 attack was made.

Before screening I recovered the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the latest operations implementation manifest, the latest R15 report, the newest task-health queue/status reconciliation, current claim hits for candidates reached in this pass, and the relevant intake/source records. Oversized JSONL ledgers are connector-truncated when rendered wholesale; I used exact-ID/source retrieval and do not claim a literal byte-for-byte visual read of all ~780 rows.

The newest task-health reconciliation still reports no free target at its already-screened `READY + CLOSABLE + UNASSIGNED` front. That is a snapshot, not proof that a deeper intake row cannot qualify, so this run advanced into previously unmined and under-screened source material instead of stopping.

## 2. Admission metric

There is no active mathematical successor, so I do not manufacture a theorem metric or inherit a stagnation count from a retired problem.

For this admission run the operational gate remains

`E_ready := number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded screen.`

Before: `0`.  
After: `0`.

This is an admission gate only. The first actual research run on a lawfully claimed successor must define a source-level mathematical metric.

## 3. Method #8 — DISCRETIZE: the finite-matrix-looking source is still a uniform theorem, not a finite closure

I moved beyond the root queue to a source which intake F explicitly records as **unmined**:

Mark Rudelson and Roman Vershynin, *Non-asymptotic theory of random matrices: extreme singular values*, ICM 2010 / arXiv:1003.2990.

The source's compressed-sensing section states the open deterministic-RIP problem: construct deterministic matrices with the restricted isometry property at essentially the random-matrix scale. In the source normalization, a random subgaussian `m x n` matrix has RIP once

`m >= C s log(2n/s)`,

while the contemporaneous random Fourier result loses additional logarithms; the text explicitly says deterministic constructions comparable with the random theorem are open.

This is exactly the sort of source that can be misclassified as CLOSABLE because every fixed `(m,n,s)` instance is finite. Discretizing exposes the quantifier mismatch: certifying one finite matrix, or even an infinite family with suboptimal parameters, does not close the source's uniform near-optimal construction problem. The source-wide obligation is asymptotic and all-scale.

Fresh literature/status screening recovered later deterministic-RIP hardness/explicit-construction work, including Gamarnik's `Explicit Construction of RIP Matrices Is Ramsey-Hard`, and modern deterministic low-coherence/RIP constructions, but no source-matching optimal deterministic construction in the bounded retrieval. That negative search is not a global openness certificate; it is enough to reject immediate CLOSABLE dispatch.

The same source contains a short-Khinchin sparse-vector question, but the source text itself immediately records Johnson--Schechtman and later work solving that existence problem. I therefore do not extract a fake open target from it.

**Disposition:** `rudelson_vershynin_icm_2010 = HARD / NOT CLOSABLE FOR R15 / no claim`.

A second finite-looking possibility, H0020 (Neri--Pinto Remark 3.7 on truncated-norm contractivity for generalized Pólya urns), is already answered by the campaign's explicit five-colour counterexample package. It is not reserve inventory and was not reopened.

## 4. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: an unmined Smirnov question has later special-class coverage, not a clean source endpoint

Intake F also marks as unmined:

Stanislav Smirnov, *Discrete complex analysis and probability*, ICM 2010.

I read the source question section rather than guessing from the title. Question 1 asks, in substance, for a satisfactory discrete-complex-analysis framework beyond the special rhombic/isoradial setup, including whether general topological quadrangulations can be embedded so that the discrete analytic theory has the needed properties. The later questions range over parafermionic observables, O(N) critical points, random planar maps/LQG and other broad model-universality directions.

The useful status transfer is that later work on discrete analytic boundary-value problems for quadrilateral graphs with orthogonal diagonals explicitly presents itself as solving a problem of Smirnov from 2010 for that special geometric class and proves corresponding convergence statements. That is real progress on the source shape, but it does not identify a complete answer to the universal-embedding/general-framework quantifier of Question 1.

So the source is not a hidden one-witness CLOSABLE item. The right lesson from the later result is a scope boundary: **orthogonal-diagonal quadrilateral graphs are a solved/special tractable category; arbitrary topological quadrangulations/general discrete-complex-analysis setup remain a much broader source direction.**

**Disposition:** `smirnov_icm_2010 = BROAD / PARTIALLY COVERED BY LATER SPECIAL-CLASS RESULTS / NOT CLOSABLE FOR R15 / no claim`.

No new theorem is claimed here; this is a source-status and quantifier reconciliation.

## 5. Method #30 — ONE SCALE / ONE DIRECTION AT A TIME: HPPS stable Poisson matching exposes why a single-scale certificate cannot close the conjectured exponent

I then screened the exact intake source row

`F0081`: Holroyd--Pemantle--Peres--Schramm, *Poisson Matching*, Open Problems (i), Section 8.

The source asks for the correct tail exponent of the matching distance `X` in the two-colour stable matching of two independent unit-intensity Poisson processes in `R^d`, `d>=2`, conjecturing

`E^* X^alpha < infinity  iff  alpha < d/2`.

The existing intake attempt already isolates the key source mechanism: colour-count discrepancy in a ball of radius `r` is naturally of order `r^(d/2)`, forcing many edges to cross a large boundary, but stability does not give a monotone coupling in the scale `r` because adding/looking farther can reroute matching chains globally.

The one-scale attack therefore fails for a precise reason. A finite-radius exact calculation can count the discrepancy and local competitions, but the source exponent is controlled by the probability that the resulting reassignment chains propagate to macroscopic distance across **all scales**. There is no local certificate whose verification at one radius automatically glues to the required tail law.

Fresh bounded literature screening recovered the HPPS source and later high-dimensional stable-matching/PWIT work, including Holroyd--Martin--Peres, but did not recover a theorem resolving the source's fixed-d `d/2` moment threshold in all `d>=2`. Again, this is bounded negative evidence only.

**Disposition:** `F0081 = OPEN-looking / HARD / NOT CLOSABLE FOR R15 / no claim`.

This screen is useful because it rules out a tempting but dishonest metric such as `largest radius checked`: that quantity can move forever without addressing the source's all-scale power law.

## 6. Independent current-reserve cross-check

The newest visible task-health reconciliation and the newer NM13 admission screens independently agree with the present gate state: the obvious CLOSABLE front is occupied, resolved, retired, held, or genuinely HARD. In particular, current screens have already removed stale attractive rows such as I0087 (`H^2 x R` IPVT later covered), I0128 (Sendov later solved), and several famous finite rows that now have owners or six-run handoffs.

A particularly useful newer NM13 screen reaches F0110 (Talagrand's up-class polynomial-majorant problem) and likewise declines to label it CLOSABLE: the literal source quantifies over all up-classes and a positive solution would imply a major source conjecture; no finite source-closing obstruction was recovered. I preserve that classification rather than duplicating the target.

Therefore this run finds no candidate satisfying all of:

1. exact outside source and full quantifiers recovered;
2. current-open status checked against later work;
3. no current owner / no retired handoff / no posted exclusion;
4. source-level CLOSABLE shape, not merely a finite-looking subproblem of a uniform theorem;
5. recoverable prior-attempt history and a defensible frozen source metric.

R15 remains **SUCCESSOR_ADMISSION_REQUIRED**.

## 7. Why no checker was created

No new finite mathematical theorem is asserted in this run. The substantive output is source/quantifier discrimination and three new route diagnoses. Creating a numerical checker here would reverse the owner's 90/10 rule and manufacture evidence for a metric that does not exist. Accordingly no decorative artifact/checker was created.

For the next admission pass, do not repeat these three screens absent a source/ownership change. Reserved next methods: **#9 RANDOMIZE, #14 FIND THE GROUP ACTING, #22 READ THE FAILURES, NOT THE SUCCESSES**. Priority should be a genuinely one-witness source statement (explicit counterexample/construction), an exact finite constant whose full source quantifier is finite, or a short universal statement with a known reduction to finitely many cases.

## 8. Model / scheduler / authorization boundary

The model-control limitation remains unchanged. The exposed task-management surface provides title/prompt, schedule or relative start, timing mode and enabled state, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model telemetry and no guaranteed hour-long execution field. GPT-6/maximum is therefore request text only here.

Making it enforceable requires an authorized product/backend or owning workspace surface that exposes persistent model/reasoning controls and returns execution telemetry. The historical P26 `You cannot modify this task` event is an authorization-context boundary. The lawful workaround is the owning authorized context, supported ownership/admin reassignment, or platform support; cloning the task or bypassing permissions is not authorized. No scheduler change was attempted.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE_OUTSIDE
  active_source: NONE
  preserved_retired:
    I0076:
      source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.2"
      status: OPEN_PARTIAL_RETIRED_HANDOFF
      metric: "2/4 source-matching obligations"
    I0124:
      source: "maximum cap in AG(7,3)"
      status: PARTIAL_RETIRED_HANDOFF
      metric: "H_288 = 112"
      proved_interval: "236 <= c_7,3 <= 285"
  metric:
    name: E_ready
    before: 0
    after: 0
    movement: false
  status: SUCCESSOR_ADMISSION_REQUIRED
  tried_moves: [8, 17, 30]
  screened:
    - candidate: rudelson_vershynin_icm_2010
      disposition: HARD_NOT_CLOSABLE
      ownership: NO_CLAIM_CREATED
      remaining_obligation: "uniform near-optimal deterministic RIP construction; fixed finite instances do not close source"
    - candidate: smirnov_icm_2010
      disposition: BROAD_PARTIALLY_LATER_COVERED_NOT_CLOSABLE
      ownership: NO_CLAIM_CREATED
      remaining_obligation: "general discrete-complex-analysis / embedding quantifier beyond solved special graph classes"
    - candidate: F0081
      disposition: OPEN_LOOKING_HARD_NOT_CLOSABLE
      ownership: NO_CLAIM_CREATED
      remaining_obligation: "all-scale d/2 tail/moment law for stable two-colour Poisson matching"
  remaining_obligation: "find a source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successor; create a canonical claim only then"
  evidence:
    - "runs/R15/20260917_2103Z_successor_admission_d0036_k40d7a.md"
    - "operations/task_health/runs/2026-09-17T210000Z/queue_delta.md"
    - "probability_1000_intake_F_20260908/README.md"
    - "probability_1000_intake_F_20260908/batches/b06_forests_matchings_determinantal.json"
    - "proofnet24/NM13-09/runs/2026-09-17/2026-09-17T22-07-00Z__admission-screen-2.md"
  audit_ids: []
  next_moves: [9, 14, 22]
```

No email/Gmail, Drive, public posting, purchase, paid compute, workflow execution, permission change, force-push, shared-root edit, peer-track edit, claim creation, or scheduler modification was performed.
