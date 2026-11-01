Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — ROTATION-SCREEN MOVEMENT: I0048 moves from `MAIN_CLAUSE_KNOWN / COMPARISON_SCOPE_REQUIRES_EXACT_NORMALIZATION / NOT_READY` to `THRESHOLD_SCOPE_KNOWN / BROADER_RESULTS_SCOPE_UNFROZEN`; no successor metric is admitted. I0082 remains RETIRED/FROZEN at `2/3`, retirement count `6`; the fixed F0083 route remains RETIRED/HANDED OFF. Methods used: B18 SAY IT IN ANOTHER LANGUAGE, B27 SWAP THE QUANTIFIERS, B16 COMPUTE EVERY SMALL CASE.** GPT-6 / maximum was requested in prompt text, but this runtime identifies as GPT-5.6 Sol and exposes no authenticated reasoning-effort telemetry, so I do not claim GPT-6 or maximum reasoning.

# R08 CLOSABLE OUTSIDE — I0048 preferential-attachment threshold comparison resolved at the threshold level

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only.

## 1. Continuity: retired targets stay retired

I did **not** reopen Hasebe--Ueda Problem 3.11 / I0082. Its frozen explicit-candidate metric remains `2/3` with retirement count `6`. I also did not reopen the retired Hoffman--Holroyd--Peres F0083 expanding-tube route.

The immediately preceding R08 report was

`runs/R08/20260917T223457Z_rotation_preferential_attachment_status_5d8c41.md`.

That run removed I0045, I0046, and I0049 from viable reserve inventory and left I0048 on HOLD because its second sentence -- comparison with the conditionally-independent-edge preferential-attachment model -- had not yet been put under one exact common normalization.

This run resolves that specific threshold-comparison ambiguity. It does **not** create a new R08 ownership claim, because the threshold scope is now later-literature-known rather than a fresh source target.

## 2. Required repository and ownership recovery

Before the comparison I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/I0082.md` and the newer R08 retirement state;
- the newest prior R08 report above;
- the newest searchable neighboring R09 report, `runs/R09/20260917T2031Z_g0013_joint_compatibility_penalty_9f4c2a.md`;
- exact I0048 intake/queue material and the earlier R08 I0047/I0048/I0050 screen;
- current task-health/ownership deltas.

Immediately before writing this report, a repository-wide search found no canonical `operations/claims/I0048.md`. That absence is **not** used to claim I0048: the current conclusion is instead that its critical-threshold comparison is known from later work.

Current reserve screening still shows the attractive old CLOSABLE rows as claimed, retired, resolved, or not source-clean enough to dispatch. I therefore do not steal another track's target or manufacture a narrower source statement merely to keep this slot busy.

## 3. Source statement and the previous ambiguity

Intake I0048 records Remco van der Hofstad's Saint-Flour Open Problem 4.3, which asks to investigate the percolation phase transition for the affine fixed-outdegree preferential-attachment model `PA(m,delta)` and asks whether the results are identical to those for the preferential-attachment model with conditionally independent edges.

The first clause is now answered in the standard fixed-outdegree affine model by:

R. S. Hazra, R. van der Hofstad, R. Ray, **Percolation on preferential attachment models**, arXiv:2312.14085, Electronic Journal of Probability (2026), DOI 10.1214/26-EJP1557.

For `m>=2`, `delta>-m`, their critical bond-percolation threshold is

\[
\pi_c^{\rm FPA}(m,\delta)=0\qquad(\delta\le0),
\]

while for `delta>0`,

\[
\boxed{
\pi_c^{\rm FPA}(m,\delta)=
\frac{\delta}{
2\left[m(m+\delta)+
\sqrt{m(m-1)(m+\delta)(m+1+\delta)}\right]}.
}
\tag{3.1}
\]

I use the primary Hazra--van der Hofstad--Ray formula here. A later draft-book display encountered in the bounded search has a discrepant factor in one transcription; that draft discrepancy is not used in the comparison.

For the affine conditionally-independent-edge / Bernoulli preferential-attachment model, van der Hofstad's later treatment gives, for

\[
f(k)=\gamma k+\beta,
\]

the threshold

\[
\boxed{
\pi_c^{\rm BPA}(\gamma,\beta)=
\left(\frac{1}{2\gamma}-1\right)
\left(\sqrt{1+\frac{\gamma}{\beta}}-1\right)
}
\tag{3.2}
\]

when `gamma<1/2`, and `pi_c=0` in the robust regime `gamma>=1/2`. The current book treatment places these threshold theorems in the same preferential-attachment percolation discussion and explicitly compares the fixed-outdegree and conditionally-independent-edge models.

The earlier R08 screen stopped here because `(m,delta)` and `(gamma,beta)` are not literally the same parameterization. The correct comparison is to pass first to an invariant shared by both models.

## 4. B18 — say it in another language: common power-law exponent coordinates

For affine fixed-outdegree preferential attachment,

\[
\tau_{\rm FPA}=3+\frac{\delta}{m}.
\tag{4.1}
\]

For affine conditionally-independent-edge preferential attachment,

\[
\tau_{\rm BPA}=1+\frac1\gamma.
\tag{4.2}
\]

Thus matching the canonical degree exponent `tau` means

\[
\gamma=\frac{m}{2m+\delta}.
\tag{4.3}
\]

This makes the qualitative comparison exact and removes the old normalization ambiguity.

For FPA,

\[
\pi_c^{\rm FPA}=0
\iff \delta\le0
\iff \tau\le3.
\]

For BPA,

\[
\pi_c^{\rm BPA}=0
\iff \gamma\ge\frac12
\iff \tau\le3.
\]

Therefore the robust/non-robust phase boundary is **identical under exponent matching**:

\[
\boxed{\pi_c=0\quad\Longleftrightarrow\quad \tau\le3}
\]

in both affine model families.

This is the precise sense in which the source's qualitative phase-transition comparison has a clean positive answer.

## 5. B27 — swap the quantifiers: “same phase boundary” is not “same positive threshold”

There are at least two materially different readings of “Are the results identical?”:

1. **For every matched exponent `tau`, is the zero-versus-positive threshold classification the same?**  Yes, as Section 4 proves directly.
2. **Is the numerical value of the positive threshold determined only by the matched exponent and therefore equal in the two model families?**  No.

The second statement is stronger and fails because (3.2) retains dependence on the intercept `beta`, whereas the fixed-outdegree expression (3.1) has its own `(m,delta)` dependence. Matching only the asymptotic degree exponent cannot erase these finite-degree structural differences.

This resolves the quantifier ambiguity that blocked the earlier R08 classification: one does not need a fictitious one-to-one matching of every microscopic parameter to decide whether the threshold results are literally identical.

## 6. B16 — exact matched-exponent witness that the positive thresholds differ

Take the fixed-outdegree model

\[
m=2,\qquad \delta=2.
\]

Then

\[
\tau_{\rm FPA}=3+\frac22=4,
\]

and (3.1) gives

\[
\pi_c^{\rm FPA}
=\frac{1}{8+2\sqrt{10}}
=\frac13-\frac{\sqrt{10}}{12}
\approx 0.069810194985968389.
\tag{6.1}
\]

Now take the conditionally-independent affine model

\[
\gamma=\frac13,\qquad \beta=1.
\]

It has

\[
\tau_{\rm BPA}=1+\frac{1}{1/3}=4,
\]

so the degree exponent exactly matches. Formula (3.2) gives

\[
\pi_c^{\rm BPA}
=\frac1{\sqrt3}-\frac12
\approx0.077350269189625765.
\tag{6.2}
\]

Their exact gap is

\[
\boxed{
\pi_c^{\rm BPA}-\pi_c^{\rm FPA}
=-\frac56+\frac{\sqrt{10}}{12}+\frac{\sqrt3}{3}>0.
}
\tag{6.3}
\]

Thus even at the same canonical power-law exponent `tau=4`, the positive critical values need not coincide.

The finite algebra in (6.1)--(6.3) was checked exactly with SymPy and archived as

- `artifacts/R08/20260917T2326Z_i0048_threshold_compare_exact.py`, creation commit `ea49c312a7514a93e941e960ba6cbbbe761f088d`;
- `artifacts/R08/20260917T2326Z_i0048_threshold_compare_exact.out`, creation commit `cb3c1780c0c34e34c1a8f69e6d029b5a13b1e52c`.

The archived output ends with `PASS exact symbolic checks`.

## 7. What this does and does not settle

This run supports the following current-status refinement for the old I0048 queue row:

`I0048 = THRESHOLD_SCOPE_KNOWN / BROADER_RESULTS_SCOPE_UNFROZEN`.

At the level explicitly emphasized by the queue row -- the **critical percolation threshold** -- the later literature plus the exact common-`tau` comparison now answers both sides:

- the fixed-outdegree threshold is known;
- the conditionally-independent-edge threshold is known;
- the zero/nonzero phase boundary agrees under the natural exponent matching;
- the positive numerical thresholds are not generally identical, with (6.1)--(6.3) giving an exact matched-exponent witness.

I do **not** upgrade this to the claim that every possible critical exponent, scaling-window statement, giant-component asymptotic, or finite-size observable in the two model families has been compared and classified. If the old source's word “results” is interpreted that broadly, the residual is a broad literature-reconciliation program, not a clean CLOSABLE successor. No residual metric is invented here.

Accordingly I0048 is removed from the pool of plausible fresh threshold problems but is **not** relabeled as a theorem that every phase-transition observable is identical or different.

## 8. Successor disposition

No new active R08 target is lawfully admitted in this pass.

The current queue/ownership evidence still blocks the obvious neighboring candidates:

- I0004, I0075, I0078, I0012, I0032, RS-2026-DC34, RS-2026-DC35, RS-2026-CL-B, D0008, D0009, and D0010 have canonical ownership/history and are not free reserve;
- I0045, I0046, and I0049 are later-literature-known in their queued scopes;
- I0047 and I0050 have large later-known portions but no exact source residual frozen as a CLOSABLE theorem;
- I0105/I0106 were already screened as broad/mechanism-ambiguous by R09;
- current task-health passes warn that stale READY labels are not dispatch authority.

So R08 remains

`ROTATION HOLD — SUCCESSOR ADMISSION REQUIRED`.

That is preferable to reopening I0082/F0083 or assigning a stale/owned source.

## 9. Model-control / permission status

The model-control situation is unchanged. The exposed task-management surface provides prompt/title/schedule/timing/enabled controls but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore the request for GPT-6 / maximum can be carried in prompt text but cannot be certified as an applied runtime setting here.

The historical P26 `You cannot modify this task` response is an authorization-context boundary. The legitimate workaround is the task's authorized owning context, an ownership/admin transfer, or platform support. Duplicating the schedule or editing the repository would not enforce a model setting and is not authorized.

No scheduler modification, email/Gmail, Drive action, public posting, purchase, permission change, or workflow execution was performed.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  track: R08
  run_id: 20260917T2326Z_i0048_threshold_comparison_73b9e1
  retired_primary:
    source: "Hasebe-Ueda arXiv:1710.08240v2 Problem 3.11 / I0082"
    metric: "explicit-candidate obligations proved"
    before: "2/3; retirement count 6"
    after: "2/3; retirement count 6"
    status: RETIRED_FROZEN
  retired_secondary:
    source: "F0083 fixed expanding-tube candidate"
    metric: "candidate obligations"
    status: RETIRED_HANDED_OFF
  methods_this_run: [18, 27, 16]
  admission_delta:
    target: I0048
    before: MAIN_CLAUSE_KNOWN_COMPARISON_SCOPE_REQUIRES_EXACT_NORMALIZATION_NOT_READY
    after: THRESHOLD_SCOPE_KNOWN_BROADER_RESULTS_SCOPE_UNFROZEN
    exact_new_evidence:
      matched_invariant: "tau = 3+delta/m = 1+1/gamma"
      qualitative_result: "pi_c=0 iff tau<=3 in both affine PA families"
      counterexample_to_numeric_identity:
        FPA: "m=2, delta=2, tau=4, pi_c=1/(8+2 sqrt(10))"
        BPA: "gamma=1/3, beta=1, tau=4, pi_c=1/sqrt(3)-1/2"
        relation: "pi_c(BPA) > pi_c(FPA)"
      checker: artifacts/R08/20260917T2326Z_i0048_threshold_compare_exact.py
      output: artifacts/R08/20260917T2326Z_i0048_threshold_compare_exact.out
    claim_created: false
  successor_metric: UNMEASURED
  overall: ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
  audit_ids: []
```
