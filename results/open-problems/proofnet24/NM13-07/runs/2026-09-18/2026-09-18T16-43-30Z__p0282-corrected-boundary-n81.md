Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-METRIC MOVEMENT: `N_exact = 80 -> 81`. Section-B methods actually tried: #8 GO THE OTHER WAY AND DISCRETIZE, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #26 HUNT THE SPORADIC CASE.**

# NM13-07 — P0282 exact lower-boundary correction and row-81 certificate

Date: 2026-09-18 UTC  
Worker: `NM13-07`  
Namespace: `proofnet24/NM13-07/`  
Category: `CLOSABLE OUTSIDE`  
Canonical source / claim: `P0282`, `operations/claims/P0282.md`  
Canonical dedup key: `chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis`  
SHA256: `08312c764bd0e9331fed25b1f255810f3c3b9e0f81134520fa26aca4c9c471a4`  
Shard: `6 mod 13`  
Parent source status: **OPEN**  
Worker status: **PARTIAL**

## 1. Continuity, ownership, repository state

This run continued the already-admitted P0282 target; it did not reopen admission or create a second claim. The canonical claim still names `NM13-07` as owner and freezes the source statement: for

`ell_{n,k} = #{sigma in S_n : LIS(sigma)=k}`,

ask whether

`ell_{n,k}^2 >= ell_{n,k-1} ell_{n,k+1}`

for every positive integer `n` and every `1<k<n`.

The immediate predecessor is

`proofnet24/NM13-07/runs/2026-09-18/2026-09-18T15-56-00Z__p0282-completed-boundary-n80.md`

created at commit `2782255b8090c4296ea16fffe3a8b4813c4e27d2`, blob `bbf9e3fdd5ecc9a05b11bc6a2fd736c1eb1ee1ce`. It left the frozen metric at `N_exact=80`, source OPEN, worker PARTIAL, `unchanged_runs=0`, `stuck_recoveries=0`, and identified the first completion-invalid boundary `n=2j-2` as the next route.

At run start, an exact Git comparison from that predecessor creation commit to then-current master head `9aa2576e7b9b9b5c4cfe4b4b4f61ed8ab0bb6ef3` gave **55 commits ahead, 0 behind**. The changed-file list contained concurrent reports/artifacts and unrelated new claims, but no edit to `operations/claims/P0282.md`, `QUEUE.md`, `POSTED.md`, `RESULTS.md`, `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, or the screened intake/attempt ledgers. The canonical P0282 claim was read again and still records this worker as exclusive owner. No release, handoff, settlement, POSTED exclusion, or duplicate ownership was recovered.

I reread the controlling/current material required by policy: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; the later NM13 deployment manifest; current `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md` and `RANKING.md`; the newest own report; and the newest visible neighboring NM13-06/NM13-08 run listings. The exact Git delta established that the large intake/attempt ledgers relevant to this source had not changed since the predecessor recovery, so their canonical identity/alias conclusions carry forward without inventing a new screen.

A repository search found no `P26-AUDIT-P0282` record and no P0282 PASS. The newest visible NM13-08 work remains on its own target/successor screening and is not a P0282 audit. Thus both required external audits remain **NOT PASSED**.

## 2. Frozen metric and source notation

The frozen metric is unchanged in definition:

`N_exact` = largest integer `N` for which this worker has an archived exact-arithmetic certificate verifying every Chen inequality for every `1<=n<=N`.

Before this run: **80**.  
After this run: **81**.

For the fixed-defect analysis write

`E_r(n) = ell_{n,n-r}`.

From the predecessor's residual-partition formula, with `N=n-r`, define the polynomial completion

`Etilde_r(n) = P_r(n)/r!`

with

`Etilde_r(n)
 = 1/(r!)^2 * sum_{mu |- r} (f^mu)^2 R_mu(N)^2`,

where, padding `mu` by zeros,

`R_mu(N)=prod_{i=1}^r (N+i-mu_i)`.

The actual source count uses only residual partitions satisfying `mu_1<=N`; `Etilde_r` includes all partitions. Hence completion is useful only when its omitted/extra residual terms are controlled exactly.

The predecessor also established

`Delta_tilde_j(n)
 := Etilde_j(n)^2-Etilde_{j-1}(n)Etilde_{j+1}(n)
 = D_j(n)/((j+1)(j!)^2)`,

where

`D_j(n)=(j+1)P_j(n)^2-jP_{j-1}(n)P_{j+1}(n)`.

## 3. Idea-before-code receipt

Before writing the checker I committed the route note

`proofnet24/NM13-07/artifacts/2026-09-18/p0282_lower_boundary_correction_idea.md`

at creation commit `734dc097226cc51738f5aa9bf34542433fa0bedd`.

The idea was to stop demanding positivity of a surrogate that is already known to fail at `j=4,n=6`, and instead classify and subtract the surrogate's exact completion error at the first invalid boundary.

## 4. Method #8 — GO THE OTHER WAY AND DISCRETIZE: classify every nonzero completion error at `n=2j-2`

Fix `j>=4` and set `n=2j-2`.

### 4.1 The `j-1` count is exact

For `E_{j-1}`, the residual size is `j-1` and the allowed first-row length is

`N=n-(j-1)=j-1`.

Every partition of `j-1` has first part at most `j-1`, so no completion term is spurious:

`Etilde_{j-1}(2j-2)=E_{j-1}(2j-2)`.                 (4.1)

### 4.2 The middle count has exactly one nonzero offender

For `E_j`, the residual allowance is `N=j-2`. The invalid residual partitions are `(j)` and `(j-1,1)`. For `(j-1,1)`, the first residual factor is

`N+1-(j-1)=0`,

so its completed contribution vanishes. For `(j)`, `f^(j)=1` and

`R_(j)(j-2) = - (2j-2)!/(j-1)!`.

Therefore

`Etilde_j(2j-2)=E_j(2j-2)+c_j`,                    (4.2)

with

`c_j = [ (2j-2)! / ((j-1)! j!) ]^2`.              (4.3)

This recovers the predecessor's correction, but now it is only the middle part of the full source-margin correction.

### 4.3 The `j+1` count has exactly four nonzero offenders

For `E_{j+1}`, the residual allowance is

`N=n-(j+1)=j-3`.

Any invalid residual partition with first part exactly `j-2` again has zero first residual factor. The only invalid residual partitions with nonzero completed weight are therefore

`(j+1)`, `(j,1)`, `(j-1,2)`, `(j-1,1,1)`.          (4.4)

Normalize their completed squared weights by `c_j`. Standard hook dimensions and the explicit residual factors give the following amplitude ratios before squaring:

`(j+1):          3(j-1)/(j+1)`,

`(j,1):          2j(j-2)/(j+1)`,

`(j-1,2):        (j-2)(j-3)/2`,

`(j-1,1,1):      (j-1)^2(j-2)/(2(j+1))`.           (4.5)

For completeness, the dimensions used here are

`f^(j+1)=1`,
`f^(j,1)=j`,
`f^(j-1,2)=(j+1)(j-2)/2`,
`f^(j-1,1,1)=j(j-1)/2`.

Squaring and summing (4.5) gives

`rho_j = 9(j-1)^2/(j+1)^2
       + 4j^2(j-2)^2/(j+1)^2
       + (j-2)^2(j-3)^2/4
       + (j-1)^4(j-2)^2/(4(j+1)^2)`

`      = (j^6-8j^5+30j^4-52j^3+47j^2-40j+38)
         /(2(j+1)^2)`.                              (4.6)

Hence the exact `j+1` completion error is

`d_j = c_j rho_j`,                                  (4.7)

and

`Etilde_{j+1}(2j-2)=E_{j+1}(2j-2)+d_j`.            (4.8)

This is a finite classification, not a limiting approximation.

## 5. Method #23 — DO WHAT THE PROPOSER DID NOT EXPECT: correct a false surrogate instead of proving it

Let at `n=2j-2`

`A=Etilde_j`, `B=Etilde_{j-1}`, `C=Etilde_{j+1}`.

By (4.1), (4.2), and (4.8), the source Turan margin is exactly

`M_j
 = E_j^2-E_{j-1}E_{j+1}`

` = (A-c_j)^2 - B(C-d_j)`

` = (A^2-BC) + B d_j - 2c_j A + c_j^2`              (5.1)

` = Delta_tilde_j(2j-2)
   + Etilde_{j-1}(2j-2)d_j
   -2c_j Etilde_j(2j-2)+c_j^2`.                     (5.2)

### Theorem NM13-07-P0282-LOWER-CORRECTION-14

For every integer `j>=4`, equations (4.3), (4.6), (4.7), and (5.2) give the exact difference between the completed residual-partition Turan quantity and the genuine source Turan margin at `n=2j-2`.

### Proof

The only distinction between source and completion is the residual constraint `mu_1<=N`. Sections 4.1--4.3 exhaust all invalid residual partitions with nonzero residual factor for the three neighboring counts. Substituting their exact squared weights into `(A-c_j)^2-B(C-d_j)` gives (5.1)--(5.2). No asymptotic or sign assumption is used. QED.

This is the key conceptual correction to the predecessor route. At `j=4,n=6`, the completed margin is negative, so proving the surrogate positive is impossible there. But the source correction is large enough to restore a positive genuine margin. The failed surrogate is not evidence against Chen's source statement.

## 6. Method #26 — HUNT THE SPORADIC CASE: exact corrected boundary scan

Only after fixing the correction identity did I write and execute the arbitrary-precision checker

`proofnet24/NM13-07/artifacts/2026-09-18/p0282_lower_boundary_j300_n81.cpp`

creation commit `cfce3eae988bc2e73010a84a57ff945f228575d0`, local SHA-256

`197b38e219fd7fad903c258b4320a3cf94caf7eb8edafe324c7db11f8300c3dd`.

Its executed output is archived at

`proofnet24/NM13-07/artifacts/2026-09-18/p0282_lower_boundary_j300_n81.out`

creation commit `49fa2c6b0795b4d2331cf6f5274e18a539c5ceb4`, local SHA-256

`13ab92ed91ddac4a4f236b7b047b61610cbb93b4e5753bd7b6328430574ad62f`.

The checker uses Boost `cpp_int`; every recurrence value, factorial division, correction, hook dimension, partition count, and margin decision is exact integer arithmetic. Floating point is used only to print one diagnostic ratio.

It builds the fixed-defect recurrence table through `j=300` and tests the exact corrected boundary `n=2j-2`. Results:

- **297/297 corrected source margins are strictly positive** for `4<=j<=300`;
- the smallest is `16780` at `j=4`;
- the correction addendum `B d_j-2c_j A+c_j^2` is positive for every tested `j`;
- among the *uncorrected completed* margins, the only nonpositive value in `4<=j<=300` occurs at `j=4`, where it is exactly `-144828`;
- direct independent RSK/hook enumeration at every `j=4,...,10` matches `A-c_j`, `B`, and `C-d_j` exactly and matches the corrected Turan margin.

Thus the sporadic hunt did not find a source counterexample at this boundary through defect 300. It instead isolates the predecessor's `j=4` failure as a surrogate-only phenomenon.

### Restricted theorem NM13-07-P0282-BOUNDARY-DEFECT100-15

For every integer `4<=j<=100` and every integer

`n>=2j-2`,                                               (6.1)

one has the strict source inequality

`ell_{n,n-j}^2 > ell_{n,n-j-1} ell_{n,n-j+1}`.          (6.2)

### Proof

At `n=2j-2`, the exact checker verifies the genuine source margin from the all-`j` correction identity (5.2), with direct RSK cross-checks on the small end. For `n>=2j-1`, the predecessor theorem `NM13-07-P0282-BOUNDARY-DEFECT100-13` already proved strict source positivity for every `4<=j<=100` using the completed residual-partition coefficient cone and the exact source/completion transfer. Combining the new boundary with that theorem proves (6.1)--(6.2). QED.

For `31<=j<=100`, this moves the certified threshold inward by one more row, from `n>=2j-1` to **`n>=2j-2`**. For `j<=30`, older work remains stronger and already covers every source-valid `n>=j+2`.

Separately, the new finite scan certifies the single boundary point `n=2j-2` for every `101<=j<=300`; it does **not** silently promote the predecessor's all-larger-`n` theorem beyond defect 100.

## 7. Frozen metric movement: exact full row 81

The same checker independently enumerated every partition of 81 by recursive integer partition generation and hook-length dimensions.

It processed exactly

`p(81)=18,004,327`

partitions, independently matched Euler's generalized-pentagonal recurrence for `p(81)`, and verified

`sum_k ell_{81,k}=81!`.

It then checked every source Turan margin in the complete row `n=81` with exact integers. All are nonnegative. The weakest ratio occurs at

`k=49`, defect `j=32`,

with presentation-only value

`ell_{81,49}^2/(ell_{81,48}ell_{81,50}) ~= 1.07679353323803387`.

The corresponding exact positive margin is

`629712961774739158766893670254848758637110180627646811434196767623481128739754798724041728373601566821042490793057599113171794894162949998144768795906348353647`.

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

Chained to the archived exact certificate through row 80, this gives the honest frozen-metric movement

**`N_exact: 80 -> 81`.**

Because the metric moved, `unchanged_runs` remains **0** and `stuck_recoveries` remains **0**.

## 8. Literature refresh — 2026-09-18

I ran fresh public web/arXiv searches on 18 September 2026 with terms including:

- `Chen longest increasing subsequences log concavity fixed size conjecture 2026`;
- `Kauers Wang longest increasing subsequences log concavity 2026 recurrence Chen conjecture`;
- `Poissonized Plancherel log concavity Chen conjecture 2026`;
- exact-phrase searches for Chen's longest-increasing-subsequence log-concavity conjecture.

The recovered current-source picture is still:

1. Bóna--Lackner--Sagan, *Longest increasing subsequences and log concavity* (arXiv:1511.08653; Annals of Combinatorics 2017), states Chen's fixed-size conjecture exactly.
2. Gao--Xie--Yang, *Schur positivity and log-concavity related to longest increasing subsequences* (arXiv:1703.06382), gives related Schur-positive results and an approach, not the full source theorem.
3. Novak--Rhoades, *Increasing Subsequences and Kronecker Coefficients* (arXiv:2006.13146), proposes a stronger Kronecker formulation rather than resolving Chen's conjecture.
4. Baslingker--Krishnapur--Madiman, arXiv:2412.15116, proves log-concavity for the **Poissonized Plancherel** top row and describes it as a positive result toward Chen's conjecture, not the fixed-size theorem.
5. Kauers--Wang, arXiv:2609.02220, submitted 2 September 2026, proves two bivariate recurrences for permutations with long increasing subsequences and D-finiteness consequences; its abstract does not claim Chen's fixed-size log-concavity conjecture.
6. A current MathDB entry still labels Chen's fixed-size conjecture open.

No source-matching full fixed-size resolution, and no paper obviously stating the exact lower-boundary correction theorem above, appeared in this bounded search. This is **negative evidence only**, not proof of worldwide openness or novelty. Novelty of the two theorem labels in this report remains **UNVERIFIED**.

## 9. What moved and what the new route learned

This run made three distinct source-relevant advances:

1. the frozen metric moved **`N_exact 80 -> 81`** by a complete exact row-81 certificate;
2. the first invalid completion boundary `n=2j-2` now has an **all-`j` exact correction identity**, with every nonzero offending residual partition classified;
3. for `4<=j<=100`, the strict source theorem moves one row inward to **all `n>=2j-2`**, while an exact boundary-only counterexample hunt through `j=300` finds none.

The main lesson is methodological: the completed residual-partition model need not itself be log-concave. At the first boundary where it fails, its error has finite support and can be corrected exactly. The obstruction is therefore not the negative completed margin at `j=4`; it is controlling the growing finite family of omitted residual shapes as one moves farther inward.

The next mathematically natural boundary is `n=2j-3`. There the residual invalid set grows, so the next useful result is either an exact finite-support correction formula with a positive source margin, or the first genuine source-negative boundary defect. Merely extending `N_exact` another row is secondary to that mechanism.

The recovered P0282 method ledger now leaves only Section-B **#9 RANDOMIZE** and **#22 READ THE FAILURES, NOT THE SUCCESSES** genuinely unused. Twenty-eight of the thirty methods have now actually been used on this source. Therefore a future P0282 run cannot truthfully claim three globally-unused Section-B methods. It should use #9 and #22 plus one explicitly labeled recycled-but-materially-new route if continuation is otherwise authorized, rather than falsely describing a previously used method as untried. The no-consecutive-triple rule can still be respected.

## 10. Audit / closure state

P0282 parent source: **OPEN**.  
This worker: **PARTIAL**.  
`NM13-07-P0282-LOWER-CORRECTION-14`: proved on this page.  
`NM13-07-P0282-BOUNDARY-DEFECT100-15`: proved on this page with exact finite certificate plus predecessor theorem.  
Boundary-only scan `101<=j<=300`: exact self-check, not an all-larger-`n` theorem.  
Row-81 metric certificate: exact and archived.  
Novelty: **UNVERIFIED**.  
P26 audit: **NOT PASSED / no `P26-AUDIT-P0282` recovered**.  
NM13-08 audit: **NOT PASSED / no P0282 audit PASS recovered**.

Nothing is called closed. Closure still requires a source-matching full all-`n`, all-`k` argument or literal source counterexample, appropriate exact finite core, recorded prior-art search, and two independent OTHER-track audits.

## 11. Model/scheduler control reality

The runtime self-identifies as GPT-5.6 Sol; reasoning level is not exposed to this worker, so it is reported **UNVERIFIED**, not maximum.

The exposed scheduler/task update interface still provides prompt/title, schedule or offset, timing mode, enabled state, and related task metadata. It still exposes **no bindable model-family selector and no bindable reasoning-effort selector**. Thus `GPT-6 / maximum` remains a prompt request only; this run does not claim that setting was enforced.

Repository configuration history now records both facts about P26: an earlier authorization context returned `You cannot modify this task`, while a later authorized P/C context successfully updated P26. The lawful workaround for a task that refuses modification is therefore to use the task's owning/authorized account/workspace/context, or an approved platform/admin surface that grants that access. It is not to duplicate the task, bypass permissions, or treat a repository edit as a native scheduler repair. No support escalation was sent by this run.

## 12. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  worker: NM13-07
  namespace: proofnet24/NM13-07/
  category: CLOSABLE_OUTSIDE
  source_id: aim_kpz_followup_2025
  claim_id: P0282
  canonical_dedup_key: chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis
  source_status_before: OPEN
  source_status_after: OPEN
  worker_status_before: PARTIAL
  worker_status_after: PARTIAL
  metric_name: N_exact
  metric_definition: largest N with archived exact-arithmetic certificate verifying every Chen inequality for every 1<=n<=N
  metric_before: 80
  metric_after: 81
  movement: true
  unchanged_runs_before: 0
  unchanged_runs_after: 0
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
  methods_tried: [8, 23, 26]
  method_outcomes:
    8: exact classification of all nonzero residual-partition completion errors at the first invalid boundary n=2j-2
    23: exact correction of the false completed surrogate, yielding the genuine source Turan identity instead of demanding surrogate positivity
    26: exact boundary hunt through j=300; corrected source margins all positive, while the uncorrected completion has its only nonpositive tested case at j=4
  theorem_ids:
    - NM13-07-P0282-LOWER-CORRECTION-14
    - NM13-07-P0282-BOUNDARY-DEFECT100-15
  theorem_scope: exact all-j correction identity at n=2j-2; strict source Chen inequalities for every 4<=j<=100 and n>=2j-2; additional boundary-only exact positivity for 101<=j<=300
  finite_certificate:
    boundary_scan_j: 4..300
    corrected_boundary_checks: 297
    corrected_boundary_all_positive: true
    minimum_corrected_margin: 16780
    minimum_corrected_margin_j: 4
    uncorrected_completed_nonpositive_count: 1
    uncorrected_first_nonpositive_j: 4
    uncorrected_first_nonpositive_value: -144828
    direct_RSK_boundary_crosschecks_j: 4..10
    direct_RSK_crosschecks: PASS
    row81_partitions_exact: 18004327
    row81_euler_partition_count: PASS
    row81_factorial_mass_check: PASS
    row81_all_source_margins: PASS
    row81_weakest_k: 49
    row81_weakest_defect: 32
    row81_ratio_diagnostic: 1.07679353323803387
    output_terminal: ALL_EXACT_CHECKS_PASS
  artifacts:
    - proofnet24/NM13-07/artifacts/2026-09-18/p0282_lower_boundary_correction_idea.md
    - proofnet24/NM13-07/artifacts/2026-09-18/p0282_lower_boundary_j300_n81.cpp
    - proofnet24/NM13-07/artifacts/2026-09-18/p0282_lower_boundary_j300_n81.out
  artifact_commits:
    idea: 734dc097226cc51738f5aa9bf34542433fa0bedd
    checker: cfce3eae988bc2e73010a84a57ff945f228575d0
    output: 49fa2c6b0795b4d2331cf6f5274e18a539c5ceb4
  literature_check_date: 2026-09-18
  literature_result: bounded current search found no source-matching fixed-size resolution; novelty remains UNVERIFIED
  required_auditors:
    P26: NOT_PASSED
    NM13-08: NOT_PASSED
  method_menu_remaining_genuinely_untried: [9, 22]
  next_step: classify the completion error at n=2j-3 and attack the corrected source margin; do not treat the uncorrected completed surrogate as the source and do not prioritize another blind N_exact extension
```

## 13. Safeguards

Writes before this immutable report were limited to the substantive idea note, exact checker, and executed checker output under `proofnet24/NM13-07/artifacts/2026-09-18/`. No shared root, canonical claim, peer namespace, workflow, permission, public surface, email/Gmail, Drive resource, paid-compute resource, or scheduler was modified. This file is the single immutable run report for this invocation. Its creation commit is the receipt and is to be read back directly; no receipt-only follow-up commit is authorized.
