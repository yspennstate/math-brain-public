Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — predecessor Tang metric remains retired/frozen at `UNBOUNDED_ABOVE`, unchanged count frozen at `6`; successor metric remains `UNMEASURED`; methods used this run: B22 READ THE FAILURES, NOT THE SUCCESSES; B21 ASK WHO ELSE HAS THIS SHAPE; B4 PROVE SOMETHING WEAKER, COMPLETELY.** GPT-6/maximum remains prompt-only because the exposed scheduler/runtime has no model selector, no reasoning-effort selector, and no authenticated applied-run telemetry.

# R09 CLOSABLE rotation admission — I0006 exact-source repair: top queue row remains HOLD_SOURCE, not READY

Repository / branch: `yspennstate/math-open-problems` / `master`.
Dated source/status check: 2026-09-17 UTC.

## 1. Continuity: Tang remains retired; no seventh Tang attack

I continued from `runs/R09/20260917T013300Z_rotation_admission_i0105_i0106.md`. I did not reopen Pengfei Tang Question 4.11.

Preserved predecessor state:

- periodic-tree clause mathematically REFUTED;
- physical percolation branch verified separately from the algebraic zero branch;
- fixed curvature metric `UNBOUNDED_ABOVE`;
- six-run unchanged count frozen at `6` after retirement;
- two distinct OTHER-track audits present (R08 and P26);
- source-matching package `paper_tang_q411_periodic_tree_counterexample/` exists;
- transitive-graph-only clause remains OPEN.

No Tang theorem, checker, package, claim file, or metric is changed in this run.

## 2. Required repository recovery / admission gate

I reread/recovered the controlling current surfaces before screening a successor:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- newest own R09 report;
- current exact-ID/ownership evidence for the leading queue rows;
- targeted intake/claim history for the candidate screened below.

The large intake JSONL corpus cannot be rendered byte-for-byte through the connector in one response; I used exact-ID/source/ownership searches and do not claim otherwise.

Current queue state still says newly certified READY entries are zero. The leading apparent CLOSABLE row is `I0006`, but it carries `HOLD_SOURCE` and requires recovery of an exact remaining source statement. Repository search finds no canonical `operations/claims/I0006.md`; a previous P21 admission screen likewise recorded it as unclaimed but PENDING until source/current-status/category fit are completed. No claim was created before doing that check.

## 3. B22 — read the gap, not merely the headline: what arXiv:2609.02820 actually proves

Candidate `I0006` points to:

Ahmed Bou-Rabee and Christoforos Panagiotis, **Sharpness and critical scaling of parking**, arXiv:2609.02820v1, submitted 2 September 2026.

Fresh checks this run used the current arXiv abstract/HTML and dated searches for:

- exact arXiv id/title;
- `parking odometer tail d>=5`;
- `critical parking S_t t^{-1} log gap`;
- author/title follow-ups and citing papers.

The current paper explicitly says its main results answer questions of Damron--Gravner--Junge--Lyu--Sivakoff (2019). In particular:

1. Critical expected particle odometer:
   `E U_n(0) asymp n^{(4-d)/4}` for `d<=3`, and `E U_n(0) asymp log n` for `d>=4` (Corollary 1.3).
2. Critical active-particle tail:
   for `d>=4`,
   `c/(t+1) <= S_t <= C log(t+2)/(t+1)`.
   The text notes that the upper bound has an extra logarithm compared with the `t^{-1}` power obtained for the related moving-hole system.
3. Quenched comparison in `d>=5`:
   for bounded-below initial law, `E U_n(0) asymp log n`, `E|U_n(0)-u_n(0)| asymp log n`, and `E U_n(0)/E u_n(0) -> infinity` (Theorem 1.4(iii)).
4. The original 2019 critical-growth and near-critical expectation questions are presented as answered by this paper, not left as a newly numbered conjecture.

This corrects the queue shorthand. The natural residual mathematical gap visible in the source is **the logarithmic gap in the critical survival/active-particle tail `S_t` for `d>=4`**, not an explicit new `d>=5 odometer-tail` open problem. The particle odometer order itself is already determined to be `log n` from dimension four onward.

## 4. Admission consequence: I0006 stays HOLD_SOURCE

The owner policy requires an outside source with a complete source statement before admission. I did **not** locate in arXiv:2609.02820 a numbered open problem, conjecture, or explicit author question asking to remove the logarithm in

`c/t <= S_t <= C log(t)/t`,

nor an explicit new question matching the queue phrase `remaining odometer-tail problem in d>=5`.

Therefore it would be dishonest to turn the visible estimate gap into a source-owned conjecture merely because it is tempting. The paper's actual source-facing claims say that the original Damron et al. questions on critical odometer growth and near-critical divergence are answered.

**Admission verdict for I0006:**

`HOLD_SOURCE / NOT_READY / NO_CLAIM_CREATED`.

Precise reason:

- current source is recovered and current;
- ownership appears unclaimed in the bounded repository search;
- but no exact author-stated residual open problem matching the queue shorthand was recovered;
- the most obvious residual `S_t` log gap is an inferred research direction, not yet an admissible outside-source target under the controlling policy.

If a later source/status page, author remark, talk note, or cited paper explicitly formulates the sharp critical `S_t` asymptotic as open, this candidate can be reconsidered with that exact locator. Until then it is not READY.

## 5. B21 — nearest solved shape and why it does not certify the inferred target

The paper itself contrasts its lattice `S_t` estimate with Bramson--Lebowitz's `t^{-1}` power for a related annihilating system where holes also move. That neighboring model explains why `t^{-1}` is a plausible scale, but it is a different process. Importing its conclusion would violate the source/model-preservation rule.

Likewise, the paper's divisible-sandpile odometer has a different high-dimensional order, `(log n)^{2/d}` under bounded-below scenery, while the particle odometer is `log n`. Thus neither the deterministic comparison process nor the moving-hole model supplies a source-valid closure by substitution.

Outcome: useful method transfer exists, but it does not turn I0006 into a certified outside open problem.

## 6. B4 — the complete result this run is an admission theorem, not a fake mathematical theorem

The fully justified narrower statement is operational/source-theoretic:

> As of the current v1 source and bounded 2026-09-17 literature check, I0006 does not satisfy the campaign's admission rule because the queue's proposed residual is not recovered as an explicit outside-source open statement.

This is stronger than leaving `HOLD_SOURCE` unexplained and weaker than claiming the residual log gap is solved or even formally posed by the authors.

No mathematical checker is warranted: there is no finite mathematical claim to certify in this run.

## 7. Successor disposition

No successor metric is started. `I0006` is not claimed. The higher-ranked apparent alternatives are either already owned/claimed in current repository history or remain PENDING/HARD under recent screens. R09 therefore remains:

**ROTATION HOLD — SUCCESSOR ADMISSION REQUIRED.**

This does not authorize a Tang restart, a HARD-reserve grab, or promotion of a stale intake `admitted=true` field.

## 8. R10 directed-audit gate

No newer self-contained closure-ready R10 package was recovered in the bounded current repository check, so the standing directed-audit trigger does not fire. No audit verdict is invented.

## 9. Model / scheduler / denied-task escalation

The limitation remains real: the exposed automation task schema offers title, prompt, schedule, enablement and timing mode, but no model-family field, no reasoning-effort field, and no authenticated runtime telemetry proving applied GPT-6/maximum.

To make GPT-6/maximum enforceable, the product/API would need explicit model and reasoning fields plus completed-run telemetry, or the task would need to be edited through an owning native workspace/UI that exposes those controls.

Historical `You cannot modify this task` responses are authorization/context boundaries. The lawful workaround is the owning authorized context, explicit ownership/permission transfer, or platform support. Duplicating a schedule or bypassing the boundary is not authorized. No scheduler change is attempted here.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  track: R09
  run_id: 20260917T023356Z_rotation_admission_i0006
  predecessor:
    source: "Pengfei Tang, arXiv:2012.01135, PDF Question 4.11"
    metric: "greatest certified lower bound for theta'' in fixed periodic-tree family"
    before: UNBOUNDED_ABOVE
    after: UNBOUNDED_ABOVE
    unchanged_count_before: 6
    unchanged_count_after: 6
    movement: RETIRED_METRIC_FROZEN
    status: REFUTED_PERIODIC_CLAUSE_RETIRED_TRANSITIVE_OPEN
  methods_this_run: [22, 21, 4]
  successor_screen:
    candidate: I0006
    source: "Bou-Rabee--Panagiotis, Sharpness and critical scaling of parking, arXiv:2609.02820v1"
    source_date: 2026-09-02
    ownership: "no canonical I0006 claim recovered in bounded search"
    queue_state_before: HOLD_SOURCE
    queue_state_after_for_R09: HOLD_SOURCE_NOT_READY
    inferred_residual: "remove the logarithmic gap in critical S_t for d>=4"
    admission_failure: "no explicit author-stated residual open problem/conjecture matching the queue shorthand recovered; odometer order itself is already proved"
    claim_created: false
  successor_metric: UNMEASURED
  overall: ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
  R10_audit: NOT_TRIGGERED
  exact_artifact: NONE_SOURCE_ADMISSION_RUN
```

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, shared-root edit, peer-file edit, force-push, or scheduler modification was performed.