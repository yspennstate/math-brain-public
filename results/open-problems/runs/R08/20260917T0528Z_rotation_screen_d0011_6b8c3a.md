Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but this runtime and exposed task surface provide no authenticated model-family selector, reasoning-effort selector, or completed-run telemetry, so I do not claim otherwise. **Retired I0082 metric remains frozen at `2/3` with retirement count `6`; successor-admission movement: `D0011: UNSCREENED_IN_R08 -> SOURCE_RECOVERED / BOUNDED_CURRENT_SEARCH_NO_GENERAL_RESOLUTION_FOUND / BROAD_NOT_CLOSABLE_FOR_R08`. Methods actually used: #2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #24 FIND THE EXTREMAL OBJECT.**

# R08 CLOSABLE OUTSIDE — rotation admission: Complete Mixability Open Problem 11

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity: I0082 remains retired

I did not reopen Hasebe--Ueda Problem 3.11. The controlling R08 handoff is `runs/R08/20260916T2327Z_i0082_sixrun_handoff_rotation_hold_4f8c2d.md`: the explicit-candidate metric reached `2/3`, the supported unchanged count reached `6`, and the CLOSABLE policy retired that source from further R08 research.

The strongest preserved I0082 package remains `R08-I0082-C005/C006`, the on-page candidate classification that every freely strongly unimodal probability law is Dirac, together with its actual-branch hardening. Its status remains **PARTIAL / PROVED_ON_PAGE / SELF_CHECKED / AUDIT_PENDING / RETIRED_FROM_R08_SLOT**. I do not reset the metric, create another I0082 lemma, or call the source closed without the required P26 plus distinct OTHER-track end-to-end audits.

## 2. Required repository recovery

Before successor work I recovered or exact-searched:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and current `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- newest own R08 report `runs/R08/20260917T0425Z_rotation_screen_th17_th18_5c4a77.md`;
- newest neighboring R09 report `runs/R09/20260917T0433Z_rotation_scope_d0012_5c7a91.md`;
- current task-health successor screen `operations/task_health/runs/2026-09-17T045900Z/queue_screening.md`;
- exact D0011 problem and prior-attempt rows in `probability_1000_intake_D_20260908/`;
- canonical ownership path `operations/claims/D0011.md`, which returned 404 immediately before this report.

The current coordinator screen reports no candidate yet passing all READY + CLOSABLE + UNASSIGNED gates and directs workers to continue beyond already-consumed queue rows. The literal queue tail is exhausted for present purposes: D0007--D0010 were already consumed/screened by current fleet work, and R09 has now screened D0012 as a broad source-classification problem rather than a lawful CLOSABLE successor. I therefore moved into the intake corpus rather than recycling those rows.

The intake corpus is large and connector rendering is truncated wholesale. I used exact-ID source/attempt retrieval for D0011 rather than falsely claiming a byte-for-byte visible reread of every intake row.

## 3. D0011 exact source, ownership, and recovered attempt

Source: Ruodu Wang, *Current Open Questions in Complete Mixability*, arXiv:1411.6190 / *Probability Surveys* 12 (2015), Open Problem 11, PDF p.18.

For prescribed margins `F_1,...,F_n`, let `D_n` be the aggregation set of laws of sums `X_1+...+X_n` over all couplings with `X_i ~ F_i`. The source explicitly notes that a counterexample exists where `D_n` has no convex-order smallest element, but that commonly used margins often do possess one, and asks:

> What are necessary and sufficient conditions on `(F_1,...,F_n)` for `D_n` to contain a smallest element with respect to convex order?

The exact intake row `D0011` records the same statement and the historical status `source_says_open`. The old attempt `D0011-A001` is substantive and must not be rederived from scratch. Its key reduction is:

`X <=_cx Y` iff `E[(X-t)_+] <= E[(Y-t)_+]` for all `t`, so a convex-order smallest aggregate exists iff one coupling simultaneously minimizes all stop-loss objectives

`L_t(pi) = E_pi[(X_1+...+X_n-t)_+]`.

The attempt identifies the obstruction correctly: for each fixed `t`, a minimizer exists under standard compactness/integrability hypotheses, but the optimizing coupling can move with `t`; the source problem asks when a **single** optimizer works for all thresholds.

Ownership check: `operations/claims/D0011.md` is absent, and a bounded exact-ID repository search found intake/catalog material but no current canonical exclusive D0011 claim. This clears the obvious ownership collision only; it does not certify READY status.

## 4. Dated current/later-literature check

Fresh bounded searches on 2026-09-17 used the phrases

- `"aggregation set" "smallest element" convex order prescribed marginals`,
- `"Open Problem 11" complete mixability convex order smallest element`,
- `convex-order minimum aggregation set marginals`, and
- `Sigma-countermonotonicity convex order smallest element`.

The primary source itself states that it is unclear under what conditions the smallest element exists. The closest literature recovered was:

1. Tiantian Mao and Ruodu Wang, *On aggregation sets and lower-convex sets*, J. Multivar. Anal. 138 (2015), 170--181: structural relations between aggregation sets and lower-convex sets, including asymptotic equality after scaling, not a necessary-and-sufficient attainment criterion for Open Problem 11.
2. Giovanni Puccetti and Ruodu Wang, *Extremal Dependence Concepts* (2015): formalizes `Sigma_cx`-smallest elements and records several positive mechanisms (countermonotonicity in dimension two, pairwise countermonotonicity when available, joint-mixability-type cases), again not a general margin characterization.
3. Yuyu Chen, Peng Liu, Yang Liu and Ruodu Wang, *Ordering and inequalities for mixtures on risk aggregation*, Math. Finance 32 (2022), 421--451: ordering relations between aggregation sets under distribution/quantile mixtures, not the missing general criterion.
4. Ruodu Wang's current working-paper index still lists the analytical structure of aggregation sets and joint mixability as active themes; it is useful navigation but is not a formal status certificate for every old open problem.

I found no later primary theorem in this bounded search giving general necessary and sufficient conditions for convex-order-minimum attainment. **This negative bounded search is not a worldwide openness or novelty certificate.** The safe current-status wording for admission is `OPEN_LOOKING / NO_GENERAL_RESOLUTION_FOUND_IN_BOUNDED_SEARCH`, not a stronger claim.

## 5. Method #2 — ATTACK THE NEGATION FIRST

The naive yes/no negation, “maybe every aggregation set has a convex-order smallest member,” is already dead in the source itself: Wang explicitly records a counterexample. Therefore constructing another failure would not advance the stated problem.

I instead attacked a more relevant hidden assumption behind a CLOSABLE rotation: perhaps the positive cases are all governed by one scalar criterion (a mean condition, variance condition, support balance, or a single extremal coupling). The known mechanisms immediately resist that compression:

- `n=2`: countermonotonicity supplies the universal minimizer;
- jointly mixable margins: the constant sum is trivially least;
- pairwise/mutually exclusive constructions give other least elements under very different support conditions;
- the source already has margins for which no least element exists.

The obstruction is therefore **simultaneous optimality across all convex losses**, not a single threshold inequality. This does not solve D0011, but it rules out treating the source as a short yes/no or single-constant CLOSABLE target.

**Outcome of #2:** no source-level counterexample target remains to close; the source is genuinely a characterization problem.

## 6. Method #18 — SAY IT IN ANOTHER LANGUAGE: multiobjective transport / LP

The stop-loss reduction turns the source into a common-optimizer problem in multi-marginal optimal transport:

`Argmin_t = argmin_{pi in Pi(F_1,...,F_n)} integral (x_1+...+x_n-t)_+ d pi`.

A convex-order smallest aggregate exists exactly when

`intersection_{t in R} Argmin_t` is nonempty.

For **finite-support margins**, this becomes a finite exact multiobjective linear-programming problem. This gives a clean partial theorem which was not stated in the old D0011 attempt in this finite form.

### Finite-support reduction

Assume every `F_i` has finite support and fixed rational or real masses. Let `P` be the finite transportation polytope of feasible joint mass tables, and let

`V = {a_1+...+a_n : a_i in supp(F_i)}`

be the finite set of possible sums. For `pi in P`, define

`L_pi(t) = E_pi[(S-t)_+]`, where `S=X_1+...+X_n`.

For each `v in V`, set

`m_v = min_{pi in P} L_pi(v)`.

Then `D_n` contains a convex-order smallest sum law **iff** the finite system

`pi in P`,  `L_pi(v)=m_v  for every v in V`

is feasible.

### Proof

Necessity is immediate: a convex-order smallest sum minimizes every stop-loss objective, hence in particular every threshold in `V`.

For sufficiency, let `pi_*` satisfy all threshold equalities. For any competing `pi`, consider

`Delta(t)=L_{pi_*}(t)-L_pi(t)`.

Both sum laws are supported on the same finite set `V`. Between two consecutive points of `V`, each stop-loss transform is affine in `t`, hence `Delta` is affine. At every endpoint `v in V`, `Delta(v) <= 0` by construction. Therefore `Delta(t)<=0` throughout every interval between consecutive support points. For `t<min V`, all couplings have `L_pi(t)=E[S]-t`, since the marginal means fix `E[S]`; for `t>=max V`, all have `L_pi(t)=0`. Thus `L_{pi_*}(t)<=L_pi(t)` for every real `t`, which is equivalent to `S_* <=_cx S`. Hence `pi_*` induces a convex-order smallest element.

When supports and masses are rational, all LP data are rational, so the special-class decision admits exact rational primal/dual certificates. I did not run an instance because this run does not claim a new finite counterexample or a source-closing finite computation.

This reduction is elementary and may well be folklore in discrete optimal transport/risk aggregation; **novelty is UNVERIFIED**. It is recorded as a partial algorithmic normal form, not as a solution of Wang's Open Problem 11.

**Outcome of #18:** finite-support D0011 is exactly decidable by finitely many LP minima plus one common-face feasibility test, but this remains a special class and therefore `PARTIAL` relative to the source.

## 7. Method #24 — FIND THE EXTREMAL OBJECT

The natural extremal object is the lower envelope of stop-loss transforms

`h(t)=inf_{pi in Pi(F_1,...,F_n)} E_pi[(S-t)_+]`.

A source-level least element requires more than having a lower bound in convex order: it requires one **attainable** law whose stop-loss transform equals `h(t)` for every `t` simultaneously. The finite-support theorem above makes this precise: the question is whether all threshold-optimal faces of the transport polytope have a common point.

This identifies a route for a future HARD/general treatment: seek structural assumptions on margins that force the family `Argmin_t` to be nested or to have the finite-intersection property. In finite dimensions one can invoke polyhedral/Helly ideas; in the continuous problem the missing step is an infinite-dimensional analogue with enough compactness plus structural control of the optimizer faces. That is materially different from adding another sufficient condition such as joint mixability.

**Outcome of #24:** a useful extremal formulation exists, but the missing theorem is a structural common-optimizer criterion on arbitrary margins—the same broad obligation as the source.

## 8. Admission verdict

D0011 therefore receives the dated R08 admission disposition

`SOURCE_RECOVERED / OWNERSHIP_CLEAR_IN_BOUNDED_CHECK / NO_GENERAL_RESOLUTION_FOUND_IN_BOUNDED_CURRENT_SEARCH / BROAD_CHARACTERIZATION / NOT_CLOSABLE_FOR_R08`.

The finite-support LP reduction is a genuine partial route, but under the owner's labels a special class is **PARTIAL**, not `PROVED` for Open Problem 11. I therefore do not create `operations/claims/D0011.md`, do not start a successor metric, and do not occupy the CLOSABLE slot with a source that cannot honestly close on a finite-support theorem.

R08 remains

**`ROTATION_HOLD / SUCCESSOR_ADMISSION_REQUIRED`.**

## 9. Neighbor reconciliation

The newest R09 report is `runs/R09/20260917T0433Z_rotation_scope_d0012_5c7a91.md`. It is a source/admission screen of Complete Mixability Open Problem 12, not a new theorem/certificate package requiring an R08 mathematical audit. It classifies D0012 as broad/current-looking/partially solved and not CLOSABLE, with no claim created. I therefore did not manufacture an audit or checker this run.

## 10. Model / scheduler / denied-task escalation status

The runtime limitation remains unchanged. The exposed task-management surface provides prompt/title/schedule/timing/enabled controls but **no model-family selector, no reasoning-effort selector, no authenticated applied-run telemetry, and no guaranteed hour-long execution control**. GPT-6 / maximum is therefore a prompt request, not a verifiable runtime setting.

Actually enforcing and verifying GPT-6/maximum requires a product/API surface that exposes model and reasoning fields plus completed-run telemetry, or management from an authorized task-owning workspace/UI if that surface provides them. Historical `You cannot modify this task` responses are authorization/ownership boundaries. The lawful workaround is the owning context, ownership/admin transfer, or platform support—not duplicate schedules and not repository text pretending to configure runtime.

No scheduler modification, email/Gmail, Drive operation, public posting, purchase, permission change, workflow execution, shared-root rewrite, peer-track edit, or force-push was performed.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  track: R08
  run_id: 20260917T0528Z_rotation_screen_d0011_6b8c3a
  predecessor:
    source: "Hasebe-Ueda arXiv:1710.08240v2, Problem 3.11 / I0082"
    metric: "number of three frozen obligations proved for one explicit candidate"
    before: 2/3
    after: 2/3
    unchanged_count: 6
    state: RETIRED_FROZEN
    strongest_package: "R08-I0082-C005/C006; PROVED_ON_PAGE_SELF_CHECKED_AUDIT_PENDING"
  methods_this_run: [2, 18, 24]
  neighbor_reconciliation:
    R09: "latest report is D0012 successor-admission screen; no new theorem package to audit"
  successor_screen:
    D0011:
      source: "Ruodu Wang, Current Open Questions in Complete Mixability, Open Problem 11"
      exact_scope: "necessary and sufficient conditions for an aggregation set to contain a convex-order smallest element"
      ownership: "operations/claims/D0011.md absent immediately before report; no canonical owner recovered in bounded exact-ID search"
      historical_attempt: "D0011-A001 common stop-loss optimizer reduction recovered"
      current_search: "bounded 2026-09-17 search found structural/special-case literature but no general necessary-and-sufficient attainment theorem"
      new_partial_route: "finite-support margins reduce exactly to finitely many threshold LP minima plus common-face feasibility"
      novelty: UNVERIFIED_LIKELY_ELEMENTARY_OR_FOLKLORE
      disposition: SOURCE_RECOVERED_BROAD_NOT_CLOSABLE_FOR_R08
      claim_created: false
  successor_metric: UNMEASURED
  overall: ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
  new_exact_artifact: NONE_GENERAL_PROOF_ON_PAGE_NO_FINITE_INSTANCE
```
