Model actually ran: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO R01 FIXED-METRIC MOVEMENT: I0024 C=1→1 frozen; successor UNMEASURED→UNMEASURED; status PENDING_ADMISSION; methods #4, #14, #20.

# R01 — I0024 frozen; successor admission frontier after I0130

Date: 2026-09-18 UTC
Worker: R01
Lane: CLOSABLE OUTSIDE

## 1. Recovery and frozen I0024 result

I recovered the latest R01 state before doing any new work. Aldous–Fill Open Problem 3.44 / intake I0024 remains frozen at the optimal fixed metric C=1. The exact characterization retained from the completed R01 package is

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^T C^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+.
\]

The pre-existing source-level audits remain:

- `R20-AUDIT-R01-I0024-03 = PASS_MATH_SOURCE_FIT`;
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10 = PASS`.

No new I0024 work was attempted because the metric cannot improve below 1 and the governing six-unchanged-run rotation rule requires successor admission rather than re-opening the solved target.

Fresh source check on 2026-09-18: Aldous and Fill still phrase Open Problem 3.44 as asking whether relaxation time has an exact infimum-over-flows characterization; their discussion contrasts this with the Chapter 4 upper-bound method. Fresh bounded searches for later exact formulations (`Aldous Fill Open Problem 3.44 exact infimum flows relaxation time`, `relaxation time exact flow variational principle reversible Markov chain`, `right inverse incidence Laplacian relaxation time flow characterization`) did not surface a later primary source explicitly presenting the same stationary-weighted right-inverse identity. This is negative search evidence only; publication priority remains UNVERIFIED.

## 2. Idea before code

The research question for this run was not another lemma about the frozen C=1 identity. It was:

> What is the precise structural reason the current successor-selection procedure keeps failing, and can changing proof strength, quotienting by symmetry, or analyzing the selection algorithm itself expose a lawful CLOSABLE OUTSIDE target?

I therefore used methods #4, #14, and #20 before doing any validation work. No checker was written because none of the attacks produced a new finite mathematical claim worth certifying.

## 3. Method #4 — prove something weaker, completely

I tested whether several near-leads admit a source-authorized weaker clause which is itself a complete answer rather than a restricted theorem.

### P0427 — optimal allocation between two exponential parallelism classes

The repository ranks P0427 as a specific technical problem and records useful two-job/no-arrival diagnostics. But the source question is a stationary queueing control problem with Poisson arrivals. Solving the no-arrival two-job problem, or a finite-state truncation, does not preserve the source quantifiers and therefore would be PARTIAL, not a CLOSABLE source answer.

### P0133 — torus spanning-tree dual homotopy distribution

This is computational and symmetry-rich, but the literal Schramm/Lyons source asks for the asymptotic fine-grid torus distribution. Exact enumeration on finitely many tori is evidence, not source-level closure. A previous admission screen reached the same conclusion.

### P0255 — nearest-unvisited walk length under a random start

The exact finite-start examples are tractable, but a prior source check in another CLOSABLE lane rejected the row because its literal source-level variation/concentration scope is broader than the finite examples.

Conclusion: **method #4 does not create a lawful successor unless the weaker statement is itself an explicit independent source question.** Choosing a convenient finite or special case cannot be used to relabel a broad source problem as CLOSABLE.

## 4. Method #14 — find the group acting

I then asked whether symmetry collapses any near-lead all the way to a finite exact problem.

- P0133 has torus translation/modular symmetry, but quotienting still leaves an asymptotic mesh parameter and does not eliminate the source’s scaling-limit quantifier.
- H0021/H0022/H0023 have strong permutation symmetry from G(n,p), but the quotient state still grows with n and the source assertions are whp asymptotic universality/linking-system statements.
- P0427 has job-class exchange symmetry in special two-class states, but stationary optimal control still requires the unbounded queue state and arrival process.

Thus symmetry helps representation but **does not change the closure type** of these sources. The most attractive genuinely finite/exact new source at the current frontier is I0130, but it is already exclusively owned elsewhere.

## 5. Method #20 — find why the successor algorithm fails

This produced the main durable update of the run.

The old successor algorithm was effectively: continue the canonical queue/intake cursor until the first source-exact, current-open, CLOSABLE, unowned target appears. That algorithm now fails for a concrete frontier reason:

1. R01’s sequential queue cursor already reached I0129 in the preceding run.
2. I0130 is now a real, source-checked `READY / CLOSABLE OUTSIDE` target, but `operations/claims/I0130.md` shows an exclusive owner in another native slot.
3. Fresh repository searches for `I0131` recover only admission/cursor reports stating that **no populated I0131+ source row exists**; there is no canonical I0131 source record to inspect or claim.
4. Neighboring admission screens likewise report no populated Codex `P0489+` source row.
5. Cross-shard probes in the H, D, E and old Tier-2/Codex inventories produced either broad source quantifiers, existing ownership, earlier settlement, or already-rejected CLOSABLE fits.

So “increment the ID” is no longer a research strategy. A lawful successor must arise from one of three events:

- a genuinely new populated intake/source row;
- an explicit release of an existing exclusive owner;
- a cross-shard rescreen that finds a full-source CLOSABLE row previously missed, with current-open and ownership checks passing.

This is a structural admission bottleneck, not evidence that the underlying open-problem inventory is exhausted.

## 6. Fresh source/current-literature and ownership checks

Dated 2026-09-18.

### Aldous–Fill I0024

Queries:

- `Aldous Fill Open Problem 3.44 exact infimum flows relaxation time`
- `relaxation time exact flow variational principle reversible Markov chain`
- `right inverse incidence Laplacian relaxation time flow characterization`

Result: source wording remains exact-infimum-over-flows; no later primary source explicitly giving the same R01 right-inverse identity was recovered in the bounded search. Adjacent variational/spectral-gap work exists but is not a source-matching resolution. Novelty remains UNVERIFIED.

### New-source frontier

- `operations/claims/I0130.md`: exists, source checked, `READY / CLOSABLE OUTSIDE`, **already exclusively owned**.
- `I0131`: no populated canonical source row recovered; hits are admission reports describing that absence.
- `P0489+`: neighboring admission reports likewise record no populated source row.

### Cross-shard source-fit probes

- H0021/H0022/H0023: source-exact asymptotic random-graph universality/linking problems; not finite CLOSABLE reductions.
- P0133: asymptotic fine-grid torus distribution, despite exact small-torus computation.
- P0255: source breadth prevents finite-instance closure.
- P0427: stationary Poisson-arrival optimal-control question; two-job/no-arrival result does not close it.

## 7. Stuck-rule action

The fixed metric has been unchanged for far more than three runs, so this is a thinking run. The blocking statement is

\[
\exists x:\quad
S(x)\wedge O(x)\wedge C(x)\wedge U(x)\wedge N(x),
\]

where `S` = exact outside source verified, `O` = current-open, `C` = full-source CLOSABLE, `U` = unowned, and `N` = non-excluded/non-posted.

Routes tried in the current admission phase include direct queue traversal, random shard probes, source-quantifier translation, symmetry quotienting, boundary/special-case reduction, stronger/weaker variants, and literature-shape transfer. The precise recurring failure is that near-leads fail different gates: ownership, source breadth, asymptotic quantifiers, current-status reconciliation, or exclusion.

The simplest unproved special cases of several candidates are indeed tractable, but proving them would not close their sources. The nearest solved-style mechanism is a finite exact source with a frozen scalar metric, as in I0130, but that target is already owned.

Chosen stuck-rule action for this run: **reduce the obstruction to a finite/current source-front computation and run it.** The result is the frontier statement above: I0130 is occupied and I0131+ is not yet populated.

## 8. Checking and audit budget

No exact checker was created: there is no new finite theorem-sized claim to certify.

No second independent audit was supplied: no neighboring package newly became both complete and in need of R01 as its second auditor during this run. Existing I0024 audits were not duplicated.

## 9. Model / scheduler control

Actual model for this run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. The exposed scheduler/task surface still provides prompt/title, schedule or relative-start timing, timing mode, and enabled state, but no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long execution control. Therefore GPT-6/maximum can only be requested in prompt text on this surface, not enforced or attested here.

The historical P26 `You cannot modify this task` event is consistent with an authorization-context restriction; repository history records that a later authorized context could modify it. The lawful workaround is the owning/authorized context or platform support, not duplication, permission bypass, or silent replacement. No scheduler or permission changes were attempted in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R01
  source: "Aldous-Fill Open Problem 3.44 / I0024 (frozen); successor not admitted"
  metric_name: "smallest rigorously proved uniform multiplicative distortion C"
  metric_before: 1
  metric_after: 1
  successor_metric_before: UNMEASURED
  successor_metric_after: UNMEASURED
  status: PENDING_ADMISSION
  unchanged_count: UNKNOWN
  tried_moves: [4, 14, 20]
  remaining_obligation: >-
    Find a target x with exact outside source, verified current openness,
    full-source CLOSABLE scope, no existing exclusive owner, and no posted/retired exclusion;
    claim it create-only before mathematical work.
  evidence:
    - runs/R01/20260918T1406Z_queue_tail_randomized_h_shape_4b7e2d91.md
    - operations/claims/I0130.md
    - "fresh repository search: no populated I0131+ source row"
    - "fresh neighboring-front evidence: no populated Codex P0489+ source row"
    - "P0133 source-fit rejection: asymptotic fine-grid torus distribution"
    - "P0255 source-fit rejection: broad source scope"
    - "P0427 source-fit rejection: stationary Poisson-arrival control, not two-job finite diagnostic"
  audit_ids:
    - R20-AUDIT-R01-I0024-03
    - P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10
```

## 11. Next route

All thirty section-B moves have appeared somewhere in R01 history, so I do not claim any remaining move is globally untried. The next run should avoid the immediately preceding triple and use a fresh combination on only **new admission deltas** rather than rescreening the same inventory. A reasonable next combination is #8 (discretize the admission obstruction), #15 (break symmetry in a new source candidate rather than exploit it), and #27 (swap quantifiers only when the source itself makes the stronger form equivalent). If no new source/ownership delta appears, the run should not manufacture a checker or re-open I0024.