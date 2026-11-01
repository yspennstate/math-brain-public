Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-METRIC MOVEMENT: `N_exact = 79 -> 80`; Section-B methods actually tried: #18 SAY IT IN ANOTHER LANGUAGE, #20 FIND WHY THE ALGORITHM FAILS, #24 FIND THE EXTREMAL OBJECT.**

# NM13-07 — P0282 completed residual boundary transfer, exact obstruction, and row 80

Run date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Track / namespace: `proofnet24/NM13-07/`  
Category: **CLOSABLE OUTSIDE**  
Canonical source / claim: `P0282`, `operations/claims/P0282.md`  
Source id: `aim_kpz_followup_2025`  
Canonical dedup key: `chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis`  
SHA256: `08312c764bd0e9331fed25b1f255810f3c3b9e0f81134520fa26aca4c9c471a4`  
Shard: `6 mod 13`  
Parent source before / after: **OPEN -> OPEN**  
Worker status before / after: **PARTIAL -> PARTIAL**  
Frozen metric before / after: **`N_exact: 79 -> 80`**  
Unchanged runs: **0 -> 0**  
Stuck recoveries: **0 -> 0**

## 1. Runtime truth and scheduler-control disclosure

The task text requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still provides title/prompt, schedule or relative-start information, timing mode, enabled state, and list/update operations. It exposes **no bindable model-family selector and no bindable reasoning-effort selector**. Therefore `GPT-6 / maximum` remains prompt text only. Making it enforceable would require an owner-authorized product/workspace/API/admin scheduling surface exposing persistent model-family and reasoning-effort controls plus authenticated per-run runtime attestation.

Repository policy records the historical P26 `You cannot modify this task` response as an authorization-context boundary and separately records a later successful P26 update from another authorized context. The lawful workaround for any such denial is the owning/otherwise-authorized scheduler context or an authorized platform/admin/API/support path for that same task, never duplication, permission changes, or access-control bypass. I did not create, modify, disable, duplicate, or probe any schedule in this invocation.

## 2. Authoritative continuity, ownership, and required reads

This invocation continues the already-admitted exclusive P0282 target; it is **not** a new admission and no second claim is created.

The immediate predecessor is

`proofnet24/NM13-07/runs/2026-09-18/2026-09-18T14-52-00Z__p0282-forced-factor-j100-n79.md`,

creation commit `64d7e5e8b4fd3f719130bc119d71e8a69f22095f`, blob `7077d0504e8316930476c134476cff92d6a043f4`. It moved `N_exact: 78 -> 79`, proved the all-`j` forced factor `(n)_floor((j+1)/2) | D_j(n)`, certified the stable source inequality for defects through 100 in the range `n>=2j+1`, and reserved methods #18/#20/#24 for this run.

Before new mathematics I reread or exact-target-recovered current state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0282.md` and exact canonical-key / ownership / audit searches;
- the predecessor report above;
- newest neighboring NM13-06 report `2026-09-18T15-34-30Z__post-p0195-admission-delta-screen-6.md`;
- newest neighboring / designated audit-partner NM13-08 report `2026-09-18T15-42-00Z__post-static-admission-delta-screen-4.md`;
- newest visible P26 report `2026-09-18_18-00-51__run-report.md`;
- the source/attempt/intake continuity already reconciled by this track, together with the exact predecessor-to-current-head Git delta.

The append-only source and attempt corpora are too large for useful byte-for-byte connector rendering every invocation. I therefore do **not** claim a fresh visual reread of every roughly 780-row ledger. The exact canonical P0282 identity and ownership are already recovered; the exact Git comparison determines whether any source/attempt/claim/queue/posting/campaign/policy surface changed. Connector truncation or a search miss is never treated as evidence of openness, novelty, or release.

The pre-report head observed after this run's three substantive artifacts was `924633fbbf3c73aaca56240a3f25903475bfc6e0`. Relative to predecessor creation commit `64d7e5e8b4fd3f719130bc119d71e8a69f22095f`, master was **65 commits ahead and 0 behind**. The complete changed-file list contains concurrent mathematics, artifacts, reports and task-health material, including this run's three P0282 artifacts, but **no change** to root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, any previously screened `probability_1000_intake_*/problems.jsonl`, any canonical `operations/claims/*.md`, or the controlling owner/NM13 policy files. Thus no owner-authorized release, competing claim, alias correction, retirement, posting, or campaign settlement changes P0282 ownership.

NM13-06's newest report explicitly records NM13-07 as still exclusively on P0282. NM13-08's newest report is a residue-7 successor admission screen and is not a P0282 audit. P26's newest visible report audits a different P04/I0101 claim. I recovered no P0282 PASS from either required auditor.

## 3. Source, frozen metric, and fixed-defect notation

For a uniform permutation `sigma` of `[n]`, let

`ell_{n,k} = #{sigma in S_n : LIS(sigma)=k}`.

Chen's source conjecture is

`ell_{n,k}^2 >= ell_{n,k-1} ell_{n,k+1}`

for every positive integer `n` and every `1<k<n`.

The frozen worker metric remains exactly

`N_exact = largest N for which this worker has an archived exact-arithmetic certificate verifying every Chen inequality for every 1<=n<=N`.

It is **79** on entry and **80** after this run. The all-`n` source statement remains open; `N_exact` is restricted finite progress only.

Write defect `j=n-k` and

`E_j(n)=ell_{n,n-j}`.

Retain the exact Kauers-Wang fixed-defect polynomial normalization from the predecessor:

`P_0(n)=1`, `P_1(n)=(n-1)^2`,

`P_{j+1}(n)=n^2(P_j(n-1)+jP_{j-1}(n-1))-(2n-j-1)P_j(n)`.

Define

`D_j(n)=(j+1)P_j(n)^2-jP_{j-1}(n)P_{j+1}(n)`.

The predecessor proved

`(n)_q | D_j(n)`, where `q=floor((j+1)/2)`,

and set

`H_j(n)=D_j(n)/(n)_q`.

## 4. Idea-before-checking record

Before the archived checker I wrote

`proofnet24/NM13-07/artifacts/2026-09-18/p0282_completed_plancherel_boundary_idea.md`

at creation commit `044e2c89a5b91f4919842bb758b69fc846f34a2f`.

The note fixed three routes before the archival validation: translate the fixed-defect polynomial into a completed positive residual-partition count (#18), force that language one step below its stable boundary to find the exact failure (#20), and identify the extremal excluded residual shape producing the failure (#24).

## 5. Method #18 — SAY IT IN ANOTHER LANGUAGE: completed residual partitions

The key is to stop treating `P_j(n)` merely as a formal polynomial and interpret it as a **completed** RSK count.

For a partition `mu |- j`, pad `mu` by zeros and write

`R_mu(N)=prod_{i=1}^j (N+i-mu_i)`.

The fixed-defect identity already proved on this track is

`P_j(n)=(1/j!) sum_{mu|-j} (f^mu)^2 R_mu(n-j)^2`.             (5.1)

For completeness, when `N=n-j` and `mu_1<=N`, the Young diagram `lambda=(N,mu)` is a partition of `n`. The hook lengths below its first row are exactly those of `mu`; the first-row hook product cancels against `(N+j)!` to give the standard residual factorization

`f^(N,mu) = f^mu R_mu(N)/j!`.                                 (5.2)

Squaring (5.2) and summing over the source-valid residual shapes `mu_1<=N` gives `E_j(n)`.

Define the completed count

`Etilde_j(n):=P_j(n)/j!`

so by (5.1)

`Etilde_j(n)=(1/(j!)^2) sum_{mu|-j}(f^mu)^2 R_mu(n-j)^2`.      (5.3)

Every summand in (5.3) is a square. Therefore, for every source-valid `(n,j)`,

`Etilde_j(n) >= E_j(n)`.                                      (5.4)

If `n>=2j`, then `N=n-j>=j` and every partition `mu|-j` satisfies `mu_1<=N`, so equality holds. The useful new boundary is one step lower.

### Theorem NM13-07-P0282-COMPLETED-BOUNDARY-12

For every `j>=1`,

`Etilde_j(n)=E_j(n)` for all `n>=2j-1`.                        (5.5)

### Proof

Only `n=2j-1` is new. Then `N=j-1`. Every `mu|-j` except `mu=(j)` satisfies `mu_1<=j-1` and is a valid source residual. The sole invalid residual `mu=(j)` has

`R_(j)(j-1)` containing the first factor

`(j-1)+1-j=0`,

so its completed squared contribution is zero. Thus completing the residual sum adds no mass and (5.5) follows. QED.

The completed Turan difference is exactly

`Etilde_j(n)^2-Etilde_{j-1}(n)Etilde_{j+1}(n)`

`= D_j(n)/((j+1)(j!)^2)`.                                     (5.6)

At `n>=2j-1`, theorem (5.5) gives

`Etilde_{j-1}=E_{j-1}`, `Etilde_j=E_j`,

while (5.4) gives `Etilde_{j+1}>=E_{j+1}`. Hence

`D_j(n)>0`

implies

`E_j(n)^2 > E_{j-1}(n)E_{j+1}(n)`.                            (5.7)

This is the transfer that the previous stable-range argument was missing.

## 6. Exact boundary certificate and improved restricted theorem

After the route was fixed I built and executed the exact arbitrary-precision checker

`proofnet24/NM13-07/artifacts/2026-09-18/p0282_completed_boundary_j100_n80.cpp`

(created at commit `0fd00e20469490eddd406b8f7e934079b7c89eaa`) and archived its executed output at

`proofnet24/NM13-07/artifacts/2026-09-18/p0282_completed_boundary_j100_n80.out`

(created at commit `da2867d4a2146ea733a79613f37dd491d54f82cf`).

The checker uses Boost `cpp_int`; every equality and sign decision is exact integer arithmetic. It regenerated `P_0,...,P_101`, divided the forced factors exactly, and verified that every coefficient of

`H_j(m+2j-1)`

is strictly positive for every `4<=j<=100`: **17,727 exact positive coefficients**, with global minimum coefficient `1`. Therefore, for every integer `m>=0`, `H_j(m+2j-1)>0`; since `(n)_q>0` at `n=m+2j-1`, also `D_j(n)>0`.

Combining this certificate with the analytical transfer (5.7) proves:

### Restricted theorem NM13-07-P0282-BOUNDARY-DEFECT100-13

For every integer `4<=j<=100` and every `n>=2j-1`,

`ell_{n,n-j}^2 > ell_{n,n-j-1} ell_{n,n-j+1}`.                (6.1)

### Proof

Write `n=m+2j-1` with `m>=0`. Exact coefficient positivity gives `H_j(n)>0`; the forced-factor identity gives `D_j(n)=(n)_q H_j(n)>0`. Equation (5.7) transfers completed positivity to the source counts. QED.

For defects `31<=j<=100`, this improves the preceding certified threshold from `n>=2j+1` to **`n>=2j-1`**. For `j<=30`, the older finite bridge remains stronger and already covers every source-valid `n>=j+2`. Nothing here is called a proof of the all-defect source conjecture.

## 7. Method #20 — FIND WHY THE ALGORITHM FAILS: the next boundary really breaks

I then forced the same quotient cone one step farther, to

`H_j(m+2j-2)`.

The exact checker finds its first nonpositive coefficient immediately at

`j=4`, coefficient index `0`, value

`-13903488`.                                                   (7.1)

This is not a numerical accident. At the corresponding source point `j=4,n=6`, exact RSK enumeration gives

`(E_3,E_4,E_5)=(381,131,1)`,

so the source Turan margin is

`131^2-381*1 = 16780 > 0`.                                    (7.2)

But the completed polynomial counts are

`(Etilde_3,Etilde_4,Etilde_5)=(381,156,444)`,

whose Turan margin is

`156^2-381*444 = -144828 < 0`.                                (7.3)

Thus the source inequality is still true at this example while the completed-count certificate becomes false. The current algorithm cannot be pushed from `2j-1` to `2j-2` merely by extending the same positive-coefficient cone. This is an exact failure mechanism, not a lack of compute.

## 8. Method #24 — FIND THE EXTREMAL OBJECT: the first omitted residual is explicit

At the new successful boundary `n=2j-1`, the only invalid residual is `(j)` and its completed weight is zero. One step lower, `n=2j-2`, the first-row length is `N=j-2`. The only residual partitions with `mu_1>N` are `(j)` and `(j-1,1)`.

For `mu=(j-1,1)`, the first factor is

`N+1-(j-1)=0`,

so this invalid shape still contributes zero. For the unique nonzero offender `mu=(j)`, `f^(j)=1` and

`R_(j)(j-2) = - prod_{t=j}^{2j-2} t`

`            = -(2j-2)!/(j-1)!`.

Therefore the **exact spurious middle-count mass** introduced by completion is

`c_j = [ (2j-2)! / ((j-1)! j!) ]^2.                           (8.1)`

For `j=4`, (8.1) gives `c_4=25`, exactly the observed discrepancy

`Etilde_4(6)-E_4(6)=156-131=25`.

So the extremal residual shape `(j)` precisely explains where the completion method first stops matching the source. The next route is not another blind coefficient extension: it is to subtract or dominate the explicitly classified omitted residual mass, beginning at `n=2j-2`, and determine whether the corrected Turan expression has a positive basis or recurrence.

## 9. Frozen metric movement: exact full row 80

The same independent checker exactly enumerated all **15,796,476 partitions of 80**, matching Euler's partition number. It independently checked

`sum_k ell_{80,k}=80!`

and every source Turan margin in row 80 with exact integers. All margins are nonnegative. The weakest ratio is at

`k=49`, defect `j=31`,

with diagnostic value

`ell_{80,49}^2/(ell_{80,48}ell_{80,50}) ~= 1.07780547126494278`.

The exact positive minimum margin is

`16455894041929236344520989486267007546052304592897642135746780115757620751325831155495505950032682070639569882087869679165908419339158435949143641854775445`.

The archived output ends `ALL_EXACT_CHECKS_PASS`. Chained to the archived exact certificates through row 79, this gives the honest frozen-metric movement

`N_exact: 79 -> 80`.

Because the metric moved, `unchanged_runs` remains **0** and `stuck_recoveries` remains **0**.

## 10. Literature refresh — 2026-09-18

Fresh same-day public searches used exact terms for Chen's fixed-size LIS log-concavity conjecture, the recent Kauers-Wang recurrence paper, and Poissonized Plancherel log-concavity.

The current primary/current-source picture recovered is unchanged in the relevant scope:

1. Bóna-Lackner-Sagan, *Longest increasing subsequences and log concavity* (arXiv:1511.08653 / Annals of Combinatorics), states Chen's fixed-`n` conjecture explicitly.
2. Baslingker-Krishnapur-Madiman, arXiv:2412.15116, proves the **Poissonized Plancherel** top-row result and describes it as the first positive result toward Chen's conjecture, rather than the fixed-size theorem.
3. Kauers-Wang, arXiv:2609.02220, submitted 2026-09-02, proves two bivariate recurrences for permutations with long increasing subsequences and D-finiteness consequences. Its stated theorem is recurrence machinery, not a resolution of Chen's fixed-size log-concavity conjecture.
4. A current 2026 search surface for work on increasing subsequences still describes the fixed-size statement as Chen's conjecture.

I found no source-matching full fixed-size resolution and no paper obviously stating the boundary-transfer theorem above in this bounded search. This is **negative evidence only**, not proof of worldwide openness or publication novelty. Novelty of `NM13-07-P0282-COMPLETED-BOUNDARY-12` and `NM13-07-P0282-BOUNDARY-DEFECT100-13` remains **UNVERIFIED**.

## 11. What moved, what failed, and next route

Real mathematical movement occurred in three distinct ways:

1. frozen metric `N_exact: 79 -> 80` by a complete exact row-80 certificate;
2. for certified defects through 100, the source-valid boundary moved two rows inward from `n>=2j+1` to **`n>=2j-1`**;
3. the exact first obstruction below that boundary was identified: the completed middle count first acquires the nonzero residual `(j)` correction (8.1), and the uncorrected completed Turan cone already fails at `j=4,n=6` even though the source margin is positive.

The next research target is therefore the **corrected lower-boundary expression at `n=2j-2`**. A useful theorem would classify the omitted residual mass for `E_{j+1}` as well as the exact `c_j` correction for `E_j`, then prove positivity after correction in a positive basis or recurrence. A useful failure would locate the first genuine source obstruction after exact correction. Merely extending `N_exact` to another row without attacking this mechanism is not the preferred route.

## 12. Audit / closure state

P0282 parent source: **OPEN**.  
This worker: **PARTIAL**.  
`NM13-07-P0282-COMPLETED-BOUNDARY-12`: proved on this page.  
`NM13-07-P0282-BOUNDARY-DEFECT100-13`: proved on this page with exact finite certificate.  
Row-80 metric certificate: exact and archived.  
Novelty: **UNVERIFIED**.  
P26 audit: **NOT PASSED / no P0282 PASS recovered**.  
NM13-08 audit: **NOT PASSED / newest NM13-08 report is not a P0282 audit**.

Nothing is called closed. Closure still requires a source-matching full argument, exact finite core where applicable, recorded prior-art search, and two independent OTHER-track audits.

## 13. Structured `ledger_delta` for P26

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
  metric_definition: largest N with archived exact certificate verifying every Chen inequality for every 1<=n<=N
  metric_before: 79
  metric_after: 80
  movement: true
  unchanged_runs_before: 0
  unchanged_runs_after: 0
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
  methods_tried: [18, 20, 24]
  method_outcomes:
    18: completed residual-partition count majorizes the source count and equals it through boundary n=2j-1, transferring D_j positivity to the source
    20: exact one-step-lower test fails first at j=4 with H_4(6)=-13903488; source margin at n=6 remains +16780 while completed margin is -144828
    24: unique nonzero middle-count completion error at n=2j-2 is residual mu=(j), with exact correction [(2j-2)!/((j-1)!j!)]^2
  theorem_ids:
    - NM13-07-P0282-COMPLETED-BOUNDARY-12
    - NM13-07-P0282-BOUNDARY-DEFECT100-13
  theorem_scope: strict source Chen inequalities for every 4<=j<=100 and n>=2j-1; prior stronger all-source-valid-n coverage retained for j<=30
  finite_certificate:
    boundary_quotient_defect_range: 4..100
    boundary_quotient_positive_coefficients: 17727
    lower_shift_first_failure_j: 4
    lower_shift_first_failure_coefficient: 0
    lower_shift_first_failure_value: -13903488
    exact_n6_source_margin: 16780
    exact_n6_completed_margin: -144828
    row80_partitions_exact: 15796476
    row80_euler_partition_count: PASS
    row80_factorial_mass_check: PASS
    row80_all_source_margins: PASS
    output_terminal: ALL_EXACT_CHECKS_PASS
  artifacts:
    - proofnet24/NM13-07/artifacts/2026-09-18/p0282_completed_plancherel_boundary_idea.md
    - proofnet24/NM13-07/artifacts/2026-09-18/p0282_completed_boundary_j100_n80.cpp
    - proofnet24/NM13-07/artifacts/2026-09-18/p0282_completed_boundary_j100_n80.out
  literature_check_date: 2026-09-18
  literature_result: bounded current search found no source-matching fixed-size resolution; novelty remains UNVERIFIED
  required_auditors:
    P26: NOT_PASSED
    NM13-08: NOT_PASSED
  next_step: classify and correct omitted residual-partition mass at n=2j-2, then test/prove the corrected Turan expression rather than extending the uncorrected cone
```

## 14. Safeguards

Writes before this immutable report were limited to the substantive idea note, checker, and executed output under `proofnet24/NM13-07/artifacts/2026-09-18/`. No shared root, canonical claim, peer namespace, workflow, permission, public surface, email/Gmail, Drive resource, paid compute, or scheduler was modified. This file is the single immutable run report for this invocation.