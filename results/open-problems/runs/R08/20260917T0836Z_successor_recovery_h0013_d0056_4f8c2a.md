Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-run telemetry, so I do not claim otherwise. **NO MOVEMENT in the retired I0082 metric: `2/3 -> 2/3`, retirement count remains `6`; no successor metric was admitted. Methods actually used: B4 PROVE SOMETHING WEAKER COMPLETELY, B20 FIND WHY THE ALGORITHM FAILS, B27 SWAP THE QUANTIFIERS.**

# R08 CLOSABLE OUTSIDE — successor admission: prior-resolution recovery before dispatch

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity: do not reopen I0082 or D0016

I did not reopen Hasebe–Ueda Problem 3.11. The I0082 source package remains retired from this slot after six supported unchanged runs. The strongest preserved source-answer candidate is still C005/C006 (the proposed classification that only Dirac measures are freely strongly unimodal), but the portfolio status remains **PARTIAL / PROVED-ON-PAGE / SELF-CHECKED / AUDIT-PENDING** until the required two independent end-to-end outside audits exist. The frozen explicit-candidate metric therefore stays `2/3`; it is not reset during rotation.

I also did not reopen D0016. The preceding R08 report proved that the particular deterministic-accumulation construction `J_j -> 2` cannot yield a uniform positive lower bound because any nested infinite-zero event would force a zero of the deterministic horizontal slice `s -> B(s,2)`, a planar Brownian motion, at a point; that route was handed off/released. This run returns to successor admission exactly as that report required.

## 2. Repository recovery performed before research

I refreshed the controlling campaign surfaces before touching another problem:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and current `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` and `operations/NEW_METHODS_2026-09-16.md`;
- stale historical `operations/claims/I0082.md`, interpreted only through the later immutable R08 retirement reports;
- newest own R08 report `runs/R08/20260917T0730Z_d0016_fixed_endpoint_polarity_handoff_93c1e7.md`;
- newest neighboring R09 report `runs/R09/20260917T080455Z_g0002_section_neighborhood_reconstruction_4e91c8.md`;
- current task-health successor screen `operations/task_health/runs/2026-09-17T080300Z/queue_screening.md`;
- intake-H source verification and the relevant intake-D/G records.

The current coordinator screen is important: D0044, D0038 and D0047 were just admitted/assigned elsewhere; D0036/D0037 remain broad PENDING targets; D0042 is HARD-leaning; and one CLOSABLE successor-admission gate remains intentionally unfilled. I therefore did not steal an occupied row or treat a stale `admitted=true` flag as dispatch permission.

The newest R09 report introduces no theorem-sized source claim to audit: it explicitly keeps its G0002 metric `UNMEASURED` because Cerf's formulas (51.1)-(52.1) are still missing, and labels its neighborhood reconstruction H2 as **NOT SOURCE VERIFIED**. R08 therefore did not manufacture an audit of a research hypothesis.

## 3. B4 — prove something weaker completely: settle H0013/H0014's *admission* question

A superficially attractive fresh row was H0013/H0014 from Yuichi Shiozawa and Jian Wang, *Essential spectrum for Brox-type diffusion processes*, arXiv:2607.07410, Remark 5.3(ii). The source itself asks, for `delta > 1/alpha`, whether the two random-drift operators `L^{w_1+W}` and `L^{w_2+W}` generate compact Markovian semigroups.

Before doing any new proof, I ran the required whole-repository recovery. That search found a substantial 14 September campaign package that had not been represented by a canonical `operations/claims/H0013.md` file:

`probability_1000_attempts_I_20260914/Probability_H0013_H0014_random_drift_destroys_compactness_for_every_delta_2026-09-14.md`

with exact-supporting scripts

- `probability_1000_attempts_I_20260914/h0013_hardy.py`,
- `probability_1000_attempts_I_20260914/h0013_jumps.py`.

That memo contains a full jump-well proof of the negative answer in the sign-supported regimes: a downward Lévy jump creates a large Hardy/Muckenhoupt product for `w_1+W`, upward jumps give the `w_2+W` analogue, and Borel–Cantelli supplies infinitely many suitably deep quiet wells. It is not merely an intake sketch. The current coordinator/status files independently list **H0013/H0014 as already settled negatively in the campaign** and exclude them from successor dispatch.

This completely settles the only question relevant to R08 here: **H0013/H0014 are not eligible successors.** I do not re-prove their mathematics, reopen them, create a duplicate claim, or count recovery of old work as a new theorem.

A fresh 2026-09-17 primary-source check still finds Shiozawa–Wang's July 8, 2026 paper itself as the relevant source; its abstract records the large-`delta` cases as open in the paper. That is compatible with the repository chronology: the negative package is later campaign work, not something I should rediscover today.

**Outcome B4:** admission/exclusion question closed; mathematical target not reopened.

## 4. B20 — find why the dispatch algorithm fails

The failed naive algorithm is:

> `admitted=true` + no obvious canonical claim file = safe unassigned research target.

H0013/H0014 are an exact counterexample to that algorithm. They have source-verified open rows, but a later campaign proof/memo and current coordinator exclusion live elsewhere in the repository. A worker that reads only `operations/claims/` or the intake row would duplicate settled work.

The same pattern appears in the current reserve:

- I0004 looked READY/unassigned in an older queue snapshot but now has an exclusive P21 claim;
- I0075 likewise later acquired an exclusive PROB20-17 claim;
- I0011 is now owned by P16;
- I0070 is/was owned by R10 and has an author-side proof candidate awaiting audits;
- H0019 is campaign-PROVED, H0020 campaign-refuted, H0024's apparent gap is recorded as an artefact, and H0025 is resolved in its source paper.

So the correct dispatch predicate is conjunctive and current:

`source_exact AND current_open AND later_literature_checked AND prior_attempts_recovered AND exclusive_owner_absent AND lane=CLOSABLE`.

Failing any one of these leaves the row PENDING/HOLD rather than READY.

**Outcome B20:** the admission mechanism itself is sharpened; no false successor was created.

## 5. B27 — swap the quantifiers: an unclaimed row is not an unclaimed READY row

There are many statements of the form

`there exists an admitted intake row with no canonical R08 claim`.

What R08 actually needs is the stronger statement

`there exists a source-exact, current-open, ownership-clear, genuinely CLOSABLE row that R08 may exclusively claim now`.

Those are not interchangeable. The current H intake makes the distinction especially clear. After reading the source-verification table:

- H0002 asks for **natural conditions on all finite graphs** guaranteeing a giant component above `(1+epsilon)/lambda(G)` — a broad classification request, not a frozen closable theorem;
- H0003/H0004/H0006-H0009 are broad threshold-cascade limit/fluctuation programs;
- H0010 is the Bramson/derivative-martingale problem and already has only a restricted prior partial result;
- H0011 is assigned elsewhere;
- H0012-H0014 overlap the recovered random-drift package above;
- H0017, H0018, H0021 and H0022 are genuine but hard asymptotic problems;
- H0023 is being handled in another successor lane;
- H0019/H0020/H0024/H0025 are excluded by current campaign/source status.

Thus the existential statement “there is some apparently unclaimed admitted H-row” is true, while the stronger dispatch statement “there is an evidenced unassigned CLOSABLE H-row for R08” is not established by the present screen.

I also used the same quantifier discipline on intake-D Conjecture D0056 (critical Derrida–Retaux survival). The source asks for the **exact asymptotic**

`P(X_n != 0) ~ [4/(m-1)^2] n^{-2}`.

The known 2021 Chen–Hu–Shi theorem proves only `P(X_n>0)=n^{-2+o(1)}`; that is an exponent-order result, not the source's universal exact constant. A fresh September 2026 search also finds Duquesne–Shi's 10 September 2026 continuous Derrida–Retaux/Brownian-CRT paper, but its continuum representation is not a proof of the discrete exact survival constant. So D0056 remains genuinely open in this bounded check, but it is a HARD asymptotic constant problem rather than an honest CLOSABLE replacement for R08.

**Outcome B27:** no quantifier weakening was used to fake a closure-ready successor.

## 6. Current disposition

The honest R08 state after this screen is

`ROTATION_HOLD — SUCCESSOR_ADMISSION_REQUIRED`.

This is not mathematical stagnation on I0082: I0082 is retired and frozen. It is an admission gate. The useful movement this run is negative but operationally decisive:

1. H0013/H0014 were recovered as **already settled by prior campaign work**, preventing duplicate research;
2. H intake was source-verified against current ownership/exclusion state and yielded no presently evidenced CLOSABLE successor for R08;
3. D0056 was rechecked against current literature and kept in the HARD pool rather than mislabeled CLOSABLE.

No successor claim was created. No new finite claim was made, so no exact-arithmetic checker was manufactured.

## 7. Next methods if the gate remains open

If the next run still lacks a coordinator-admitted target, do not repeat B4/B20/B27. Use a new triple, for example **B23 DO WHAT THE PROPOSER DID NOT EXPECT, B8 DISCRETIZE, B16 COMPUTE EVERY SMALL CASE**, on the next source-exact unclaimed candidate that survives current-status/ownership screening. In particular, prefer a genuinely unattempted admitted intake statement with a finite obstruction/counterexample route over another broad classification problem.

## 8. Model / scheduler-control status

The requested GPT-6/maximum setting is still not enforceable or verifiable in this exposed scheduler surface. The available task controls cover prompt/title/schedule/timing/enabled state, but there is no model-family selector, reasoning-effort selector, or authenticated completed-run telemetry. Actually changing this requires a native product/API model-and-reasoning control in the authorized owning workspace plus runtime metadata confirming what executed.

The historical `You cannot modify this task` response for one P26 scheduler ID is an ownership/context boundary, not a mathematical or prompt-level issue. Repository history records later successful modification from another authorized context. The lawful workaround is therefore the task-owning authorized workspace/account, an admin/ownership transfer if supported, or platform support. Duplicating the task or editing repository text would not change the scheduler runtime and is not a valid workaround.

No scheduler modification was attempted.

## 9. Prohibited-action audit

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler mutation, force-push, shared-root edit, peer-file edit, or paid compute was performed.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  track: R08
  run_id: 20260917T0836Z_successor_recovery_h0013_d0056_4f8c2a
  retired_predecessor:
    id: I0082
    source: "Hasebe-Ueda arXiv:1710.08240v2, Problem 3.11"
    metric: "number of three frozen explicit-candidate obligations proved"
    before: "2/3"
    after: "2/3"
    unchanged_count: 6
    state: RETIRED_FROZEN_PARTIAL_AUDIT_PENDING
  released_candidate:
    id: D0016
    source_status: OPEN
    route_status: FIXED_ENDPOINT_ROUTE_REFUTED
    ownership_disposition: HANDOFF_RELEASED
    metric: "1/2"
    state: NOT_REOPENED
  successor_screen:
    H0013_H0014:
      before: APPARENT_OPEN_INTAKE_CANDIDATE
      after: EXCLUDED_ALREADY_SETTLED_NEGATIVELY_IN_CAMPAIGN
      evidence: "14-Sep full memo + exact scripts + current coordinator exclusion"
      new_claim: NONE
    H_intake_remaining:
      status: NO_EVIDENCED_UNASSIGNED_CLOSABLE_SUCCESSOR_THIS_PASS
    D0056:
      exact_source_target: "P(X_n != 0) ~ 4/(m-1)^2 n^-2"
      best_known_recovered: "n^-2+o(1) survival probability"
      current_2026_followup: "continuous Derrida-Retaux/Brownian CRT representation, not exact discrete constant"
      status: OPEN_CURRENT_BOUNDED_HARD_NOT_CLOSABLE
      new_claim: NONE
  methods_this_run: [4, 20, 27]
  next_methods: [23, 8, 16]
  new_exact_finite_claim: NONE
  new_checker: NONE
  neighboring_R09_audit: NOT_APPLICABLE_NEW_REPORT_HAS_ONLY_NOT_SOURCE_VERIFIED_HYPOTHESIS
  overall: ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
```
