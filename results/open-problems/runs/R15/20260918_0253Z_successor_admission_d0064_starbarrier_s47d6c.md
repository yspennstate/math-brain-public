Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at `2/4`, I0124 remains `PARTIAL / RETIRED-HANDOFF` with `H_288=112`. Methods #6 DEFORM TO A POINT YOU CAN SOLVE, #20 FIND WHY THE ALGORITHM FAILS, #28 REPLACE FOR ALL WITH FOR TYPICAL.**

# R15 successor admission — D0064 star-equation quantifier barrier

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

## 1. Continuity and exclusions

I did **not** reopen Burdzy--Scheutzow Problem 7.2 (`I0076`). Its controlling R15 handoff remains `OPEN / PARTIAL / RETIRED-HANDOFF` with the source-matching counterexample metric frozen at `2/4`. The source hypothesis remains exactly the one already recovered: forward Brownian + backward Brownian, and at one arbitrary finite random time `T` independence of the two complete centered half-paths. No deterministic-time substitute, stopping-time strengthening, seam-half Brownian assumption, or Problem 7.5 work was introduced.

I likewise did not reopen I0124 after its six-unchanged-run handoff. Its historical R15 scalar remains `H_288=112`.

The current successor-admission metric is

`E_ready = number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded run`.

Before: `0`. After: `0`.

I re-read the campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the current NEW-METHODS deployment manifest, the newest own R15 report, the newest available neighboring successor/admission work, exact intake rows used below, and current claim/search state. The connector does not sensibly expose the entire ~780-row intake as one complete bounded response, so I used the exact current cursor rows plus repository-wide ownership searches rather than pretending a truncated rendering was a full read.

The freshest bounded coordinator screen recovered still reports zero newly certified free `READY + CLOSABLE OUTSIDE + UNASSIGNED` successors. I treat that as a front-of-queue fact, not as proof that the full intake contains none.

## 2. Exact source: D0064

Candidate: `D0064`, Rémi Rhodes and Vincent Vargas, *Gaussian multiplicative chaos and applications: a review*, arXiv:1305.6221, Conjecture 6.4, Section 6.3.

I checked the current arXiv PDF directly, including the actual Conjecture 6.4 page. The source first states the universal quantifier: it conjectures that **all** non-trivial ergodic lognormal star-scale-invariant random measures (with a stronger dependence-decay condition) belong, up to a constant factor, to one of four families. It then lists:

1. `alpha=1`, `gamma^2<2d`: standard GMC (already Theorem 2.19);
2. `alpha=1`, `gamma^2=2d`: derivative martingale / critical chaos;
3. `alpha<1`, `gamma^2<2d`: atomic GMC of the dual phase;
4. `alpha<1`, `gamma^2=2d`: atomic GMC of the frozen phase.

The source explicitly labels situations 2, 3 and 4 as conjectural. This is a classification of every admissible fixed point of the star equation, not merely a construction or scaling-limit theorem for canonical approximations.

The intake record agrees with that scope and had only an old unverified status search.

## 3. Method #6 — DEFORM TO A POINT YOU CAN SOLVE

The natural soluble endpoint is exactly the source's case 1. The review's Definition 2.17 writes the star equation

`M(A) =_law int_A exp(omega_epsilon(x)) M_epsilon(dx)`

with `M_epsilon(A) =_law M(A/epsilon)` and independence of the multiplier field and rescaled measure. Theorem 2.19 then classifies a good lognormal star-scale-invariant stationary measure under a finite `(1+delta)`-moment assumption: it is a GMC, up to an independent scalar factor.

The same barrier is visible even more explicitly in Rhodes--Sohier--Vargas, *Levy multiplicative chaos and star scale invariant random measures* (Ann. Probab. 42 (2014), arXiv:1201.5219). Their uniqueness theorem assumes a finite moment of order `1+delta`; they state that all star-scale-invariant measures with a moment strictly greater than one are Levy multiplicative chaos up to their regularity hypotheses, and explicitly identify the no-finite-moment case as the unresolved regime requiring different measures.

So deforming the conjecture into the integrable subcritical region does close a full classification theorem — but it lands in already-known case 1, not in the source's unresolved cases 2--4. This is useful because it pins the frontier to a **moment threshold**, not to a vague lack of technique.

## 4. Method #20 — FIND WHY THE ALGORITHM FAILS

The known classification algorithm is: iterate the star equation, use stationarity/decorrelation and `L^{1+delta}` control to obtain an ergodic density/scalar factor, recover the infinitely-divisible/Gaussian generator from the scale increments, and identify the resulting chaos.

The exact place this architecture ceases to apply is the hypothesis

`E[M(B)^(1+delta)] < infinity` for some `delta>0`.

Rhodes--Sohier--Vargas make that dependence theorem-level explicit. Their proof uses the higher moment to control the iterated cascade and to derive the relevant Laplace-exponent inequalities; their paper says the general case without a finite-moment assumption needs a different class of measures. Rhodes--Vargas's review then summarizes the same dichotomy: star-equation solutions are well identified in the subcritical regime with moments larger than one, while the few-moment regime is where the new critical/atomic structures appear.

This identifies the source-level blocker more sharply than the intake did:

> To settle D0064, one needs a smoothing-transform / star-equation **uniqueness theorem in the critical and atomic low-moment regime**, not another construction of the expected candidates.

In particular, proving that derivative chaos or an atomic subordinated chaos satisfies the star equation does not prove that every admissible star-equation solution has that law.

## 5. Method #28 — REPLACE FOR ALL WITH FOR TYPICAL

This is where recent progress is strongest, but also where the quantifier mismatch is decisive.

Madaule--Rhodes--Vargas (2016), *Glassy phase and freezing of log-correlated Gaussian potentials*, proved that a canonical low-temperature log-correlated model converges to an integrated atomic random measure whose random intensity is the critical GMC. In 2025, Bertacco--Hairer, *Uniqueness of supercritical Gaussian multiplicative chaos* (now EJP 30 (2025), Paper 188 / arXiv:2504.07552), proved stable convergence for general convolution approximations of a broad class of log-correlated Gaussian fields; the limit is again an integrated atomic measure driven by critical GMC and is regularisation-independent up to a multiplicative constant.

That is a powerful **typical/canonical-construction uniqueness** theorem. It supports the families predicted in cases 3--4 and considerably expands the universality class. But it is not the universal fixed-point classification in Conjecture 6.4. In the accessible 2025 paper, the main theorems start from a specified log-correlated field and its regularisations and identify the limit; I found no theorem asserting that an arbitrary ergodic star-equation solution must arise from those regularisations. A search within the paper found no `fixed point` classification statement.

Thus the tempting inference

`canonical approximations all converge to the predicted atomic chaos`  
`=> every star-equation solution is that atomic chaos`

is invalid without an additional representation/uniqueness theorem. This is precisely the source's missing `for all` quantifier.

## 6. Current status and ownership

Fresh repository-wide search found no canonical `operations/claims/D0064.md`. However, absence of an owner is not enough for admission. An independent R7-05 successor screen already classified D0064 as `broad/HARD`, and the source/current-literature analysis above confirms why: the unresolved content is a theorem-sized all-fixed-points classification in a low-moment regime.

Therefore:

`D0064 = OPEN-LOOKING / SOURCE-SCOPE-CLARIFIED / HARD / NOT CLOSABLE-READY / NOT CLAIMED`.

This is **not** a proof that the problem is globally still open. The 2026-09-18 literature search was bounded. The positive old/new theorems are enough to establish the quantifier mismatch and moment barrier; the negative search for an all-solution classification is not a novelty certificate.

I also checked the nearby apparently attractive existential `D0072` (Grimmett--Li Question 4.5). It is not free: P20 already has the canonical claim and a source-matching explicit YES witness based on `S_3 * A_5` plus a graphical regular representation construction, with independent audit work present elsewhere in the repository. I did not duplicate it.

## 7. Dated source / literature query log and access limits

Checked 2026-09-18:

- Rhodes--Vargas, arXiv:1305.6221 current arXiv landing page and PDF, especially Definition 2.17, Theorem 2.19, and the actual Conjecture 6.4 page;
- Allez--Rhodes--Vargas, arXiv:1102.1895 / PTRF 155 (2013), lognormal star-scale-invariant classification in the integrable regime;
- Rhodes--Sohier--Vargas, arXiv:1201.5219 / Ann. Probab. 42 (2014), Theorem 12 and the explicit `1+delta`-moment/no-moment frontier;
- Madaule--Rhodes--Vargas, arXiv:1310.5574 / AAP 26 (2016), glassy-phase atomic limit;
- Bertacco--Hairer, arXiv:2504.07552 / EJP 30 (2025), stable convergence and regularisation uniqueness for supercritical GMC;
- Bertacco--Hairer, arXiv:2504.06956, local structure/freezing for star-scale-invariant fields;
- current repository ownership/history for D0064 and D0072.

Queries included exact combinations of `Conjecture 6.4`, `solutions to the star-equation`, `critical star equation multiplicative chaos uniqueness`, `moment of order strictly greater than 1 star scale invariant`, and recent `supercritical GMC uniqueness` terms.

Limits: web search is bounded and indexing can miss papers; no claim of exhaustive worldwide prior art is made. Positive theorem statements were preferred over search absence. The source PDF was visually inspected on its Conjecture 6.4 page rather than relying on OCR/search snippets alone.

## 8. Why no checker/artifact was created

No new finite mathematical claim was produced. The useful output is a source/literature quantifier reduction: `integrable fixed-point uniqueness` versus `low-moment all-fixed-point uniqueness`. Manufacturing an exact checker for that literature distinction would violate the 90/10 rule and certify nothing mathematical.

## 9. Model / scheduler-control status

The actually running model for this report is GPT-5.6 Sol; authenticated reasoning-effort telemetry is not exposed, so reasoning is UNVERIFIED. The task text requests GPT-6 / maximum, but the task-management surface exposed to this worker still provides no binding model-family selector or reasoning-effort selector and no authenticated applied-model receipt. Prompt text therefore cannot certify GPT-6 / maximum.

The historical P26 `You cannot modify this task` event was an authorization-context boundary; repository history records a later authorized context succeeding. The legitimate remedy is the owning/admin-authorized product/backend surface (or platform support) exposing persistent model/reasoning controls and runtime telemetry, not duplication or permission bypass. I made no scheduler or permission change.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  allocation: CLOSABLE_OUTSIDE
  repository: yspennstate/math-open-problems
  branch: master
  continuity:
    I0076:
      source: Burdzy_Scheutzow_Forward_Brownian_Motion_Problem_7_2
      status: OPEN_PARTIAL_RETIRED_HANDOFF_DO_NOT_REOPEN
      metric_name: source_matching_obligations_for_frozen_counterexample
      metric_before: 2
      metric_after: 2
      target: 4
      active_research_this_run: false
    I0124:
      status: PARTIAL_RETIRED_HANDOFF_DO_NOT_REOPEN
      historical_metric_name: H_288
      historical_metric_value: 112
      active_research_this_run: false
  successor:
    status: SUCCESSOR_ADMISSION_REQUIRED
    active_source: NONE
    claim_created: false
    metric_name: E_ready
    metric_before: 0
    metric_after: 0
    movement: none
    unchanged_count: UNKNOWN
  methods_actually_tried: [6, 20, 28]
  substantive_screen:
    problem_id: D0064
    source: Rhodes_Vargas_2013_Conjecture_6_4
    disposition: OPEN_LOOKING_HARD_NOT_CLOSABLE_READY
    owner_found: false
    claim_created: false
    exact_blocker: >-
      Universal classification of arbitrary ergodic lognormal star-equation
      fixed points in the critical/atomic low-moment regime; known classification
      theorems require a finite 1+delta moment, while modern supercritical
      universality identifies canonical approximation limits rather than all fixed points.
    nearest_solved_regime: alpha_1_gamma2_lt_2d_with_finite_1_plus_delta_moment
    recent_progress_checked:
      - Madaule_Rhodes_Vargas_2016_glassy_phase
      - Bertacco_Hairer_2025_supercritical_GMC_uniqueness
  ownership_exclusion:
    D0072: OWNED_P20_SOURCE_MATCHING_YES_CANDIDATE_DO_NOT_DUPLICATE
  evidence:
    source_pdf_checked: true
    current_literature_checked: true
    repository_ownership_checked: true
    finite_checker_needed: false
  audit_ids: []
  remaining_obligation: >-
    Continue successor admission beyond already-screened D0064 and the claimed D0072.
    Admit only an ownership-clear source whose full current source quantifiers are genuinely
    closable; do not convert canonical-construction universality into an all-fixed-points theorem.
  next_methods: [1, 11, 23]
  closure_claim: false
```

## 11. Next cursor

Use **#1 CHANGE THE CATEGORY, #11 DUALIZE, #23 DO WHAT THE PROPOSER DID NOT EXPECT** on new, ownership-clear intake rows, prioritizing literal existence/counterexample questions or sharp finite/equality statements whose complete source quantifiers can be discharged by one construction or short exact argument.

**NO I0076 OR I0124 REOPENING. NO D0064 CLAIM. NO SUCCESSOR CLAIM THIS RUN. R15 remains `SUCCESSOR_ADMISSION_REQUIRED`.**
