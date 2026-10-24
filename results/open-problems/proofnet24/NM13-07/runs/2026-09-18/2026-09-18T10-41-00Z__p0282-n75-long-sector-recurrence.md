Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-METRIC MOVEMENT: `N_exact = 70 -> 75`. Section-B methods actually tried: #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE; #25 COUNT THE SAME THING TWICE; #28 REPLACE FOR ALL WITH FOR TYPICAL.**

# NM13-07 research invocation — P0282 exact `n<=75` certificate with independent long-LIS recurrence checks

Run date: 2026-09-18 UTC  
Track / namespace: `proofnet24/NM13-07/`  
Category: `CLOSABLE OUTSIDE`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Canonical source / claim: `P0282`, `operations/claims/P0282.md`  
Canonical dedup key: `chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis`  
Selection shard: `6 mod 13`  
Parent source status after this run: **OPEN**  
NM13-07 status after this run: **PARTIAL**  
Frozen metric before / after: **`N_exact = 70 -> 75`**  
Consecutive unchanged runs on P0282: **2 -> 0**  
Stuck recoveries used on P0282: **0 -> 0**  
Required eventual outside auditors: **P26 and NM13-08; neither is counted as passed**

## 1. Runtime and task-control disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this report, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed scheduler/task-control schema still offers title, prompt, schedule or relative-start data, timing mode, enabled state and task identifiers; it exposes **no bindable model-family selector and no bindable reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing persistent model and reasoning controls plus authenticated per-run runtime attestation.

The current repository ledger records that the historical P26 `You cannot modify this task` event was authorization-context-specific and that a later P26 update succeeded from another authorized context. A future denial should therefore be handled in the owning/otherwise-authorized context or through an authorized platform/admin/API/support path for that same task, never by duplication, permission changes or access-control bypass. I did not create, modify, disable, duplicate or probe a schedule in this invocation.

## 2. Authoritative continuity and ownership

This run continues the already admitted exclusive target `P0282`; it does **not** perform a new admission or create a second claim.

Before new mathematics I reread or targeted-recovered current `master` state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized deployment/amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0282.md`;
- exact `P0282`, canonical-key, claim/attempt/handoff/audit and intake/dedup searches;
- newest own report `proofnet24/NM13-07/runs/2026-09-18/2026-09-18T09-41-30Z__p0282-two-thirds-defect-window.md`;
- newest neighboring NM13-06 report `proofnet24/NM13-06/runs/2026-09-18/2026-09-18T09-31-00Z__p0195-barrier-lowtemp-handoff.md`;
- newest neighboring NM13-08 report `proofnet24/NM13-08/runs/2026-09-18/2026-09-18T09-49-00Z__p0093-stuck-recovery-1-vallander-scope-conflict.md`.

The canonical claim still records owner `NM13-07`, SHA256 key `08312c764bd0e9331fed25b1f255810f3c3b9e0f81134520fa26aca4c9c471a4`, and shard residue 6. I recovered no owner-authorized release, competing alias owner, retirement, POSTED/campaign closure or P0282 audit PASS. NM13-08 is currently working on P0093 rather than auditing P0282; P26 has not supplied a P0282 PASS. Ownership therefore remains exclusive to NM13-07 and both required outside audits remain outstanding.

Large JSONL/root surfaces can be connector-bounded when rendered wholesale. Exact canonical identity, dedup evidence, claim ownership, immutable report continuity and targeted attempt/audit searches are the anchors; truncation is not treated as evidence of absence.

A contemporaneous repository-head query during the run showed other workers continuing to commit to `master`; such concurrent activity neither releases P0282 nor changes its frozen metric.

## 3. Exact source statement and bounded literature refresh — 2026-09-18

For a uniform permutation `sigma` of `[n]`, let

`ell_{n,k} = #{sigma in S_n : LIS(sigma)=k}`.

Chen's source conjecture asks whether, for every positive integer `n` and every interior `1<k<n`,

`ell_{n,k}^2 >= ell_{n,k-1} ell_{n,k+1}`.                         (3.1)

The bounded current literature check recovered:

1. Bóna--Lackner--Sagan, *Longest increasing subsequences and log concavity*, arXiv:1511.08653, which states Chen's fixed-size conjecture and proves related restricted results.
2. Gao--Xie--Yang, *Schur positivity and log-concavity related to longest increasing subsequences*, arXiv:1703.06382, which proves Schur-positive analogues/restricted results, not the full fixed-size statement.
3. Novak--Rhoades, *Increasing Subsequences and Kronecker Coefficients*, arXiv:2006.13146, which proposes a stronger representation-theoretic conjecture rather than closing Chen's statement.
4. Baslingker--Krishnapur--Madiman, *Log-concavity in one-dimensional Coulomb gases and related ensembles*, arXiv:2412.15116, which proves the Poissonized Plancherel top-row result and calls it the first positive result toward Chen's fixed-size conjecture.
5. Manuel Kauers and Chen Wang, *Recurrences for permutations with long increasing subsequences*, arXiv:2609.02220, submitted 2026-09-02, which proves two bivariate recurrences in the long-LIS sector and D-finiteness consequences. It does not claim Chen log-concavity.

Fresh searches used the exact Chen/LIS/log-concavity terms, fixed-size versus Poissonized Plancherel, and the exact Kauers--Wang title/arXiv ID. No later primary source explicitly resolving the full fixed-size conjecture surfaced. This is **bounded negative evidence only**, not proof of worldwide openness or publication novelty.

## 4. Frozen metric and prior state

The metric remains exactly

`N_exact = largest N for which NM13-07 has an archived exact-arithmetic certificate verifying every source inequality (3.1) for every 1<=n<=N`.

Before this run: **70**. The archived `n=61..70` hook-length checker output ends `ALL_EXACT_CHECKS_PASS` and chains to the earlier exact `n<=60` Robinson--Schensted/Young-branching certificate.

The preceding run also proved a source-faithful infinite restricted theorem: with defect `j=n-k`, strict Chen log-concavity holds in an explicit `Theta(n^(2/3))` boundary window. That theorem does not itself change the finite metric `N_exact`.

The weakest exact ratios observed for `61<=n<=70` were drifting near `k≈0.61n`, well inside the long-LIS regime `k>=n/2`. That observation motivated a materially different route this run.

## 5. Idea-before-code record

Before writing the new checker I archived

`proofnet24/NM13-07/artifacts/2026-09-18/p0282_long_sector_recurrence_idea.md`

at creation commit

`e87bacf4b236ff2007a5fe4a81aaaf7967d63841`.

It fixes the three methods below, the intended independent identities and the finite goal `N_exact>70`. The checker was written only after that route was recorded.

## 6. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

Kauers--Wang's September 2026 recurrences apply exactly where the finite certificates are empirically weakest. Writing `a_{n,k}=ell_{n,k}`, their two long-LIS relations are

`a_{n+1,k}+n^2 a_{n-1,k}`
`  = a_{n,k+1}+(2n-1)a_{n,k}+a_{n,k-1}`,                            (6.1)

and

`(n+1)^2(a_{n,k}+a_{n,k+1})`
`  = (n-k+1)a_{n+1,k}+(n+k+1)a_{n+1,k+1}`.                         (6.2)

For exact cross-checking I used (6.2) throughout `k>=ceil(n/2)` and (6.1) on the strict shift-stable interior `k>n/2`, so every shifted term in the latter remains within the proved long-LIS sector. The recurrences are used as **independent checks of exact integers**, not as a claimed new theorem.

Outcome: **successful route selection**. The recurrence sector contains the global minimum log-concavity ratio in every newly checked row `n=71,...,75`.

## 7. Method #25 — COUNT THE SAME THING TWICE: exact certificate through `n=75`

For each partition `lambda|-n`, Robinson--Schensted gives

`ell_{n,k} = sum_{lambda|-n, lambda_1=k} (f^lambda)^2`,              (7.1)

with exact hook-length dimension

`f^lambda = n! / prod_{u in lambda} h(u)`.                           (7.2)

The new checker evaluates (7.1)--(7.2) with arbitrary-precision integers for `n=70,...,75` and performs the following independent exact guards:

1. the number of generated partitions equals `p(n)` computed independently by Euler's generalized-pentagonal recurrence;
2. `sum_k ell_{n,k}=n!` at every row;
3. every source margin `ell_{n,k}^2-ell_{n,k-1}ell_{n,k+1}` is nonnegative for every interior `k`;
4. recurrence (6.2) is checked exactly at **184** long-sector positions across `n=70,...,74`;
5. recurrence (6.1) is checked exactly at **146** shift-stable long-sector positions across the consecutive rows.

The new rows certify:

| n | p(n) | exact minimum-ratio k | decimal diagnostic for `ell_k^2/(ell_{k-1}ell_{k+1})` |
|---:|---:|---:|---:|
| 71 | 4,697,205 | 44 | 1.088407093987962 |
| 72 | 5,392,783 | 44 | 1.087075926085345 |
| 73 | 6,185,689 | 45 | 1.085802214907739 |
| 74 | 7,089,500 | 45 | 1.084564324835599 |
| 75 | 8,118,264 | 46 | 1.083351317277728 |

Across the **31,483,441** newly processed partitions for `71<=n<=75`, every exact source margin is nonnegative. The smallest new relative ratio occurs at `(n,k)=(75,46)`. Its exact margin is the positive integer

`33022598359865198353601530384534027559169405060431277771390624119617715472091854352830257276368831950129126997040009128440954408593264568032000`.

The exact ratio itself is archived in the output rather than rounded for certification.

Artifacts:

- checker: `proofnet24/NM13-07/artifacts/2026-09-18/p0282_n71_75_exact_kw.cpp`, creation commit `9799c1b02df148f8d85cf94bc0adbea060515225`, GitHub blob `d055afa41aa5ffc0b1143e4a83225ab13f572e80`, UTF-8 SHA256 `55679f4f1cf6138f90ffb6cd44e1cb8c32eb2a40a4fa838fe35ec9cc450e2eca`;
- executed output: `proofnet24/NM13-07/artifacts/2026-09-18/p0282_n71_75_exact_kw.out`, creation commit `dbbbd25149af053e0917031fac8ad4c708240a3f`, GitHub blob `c8d5bfa940bcea2b5c457144d68bc65bf9ab6c42`.

The output was read back at its creation commit and ends `ALL_EXACT_CHECKS_PASS`.

This is explicitly a **self-check / finite exact certificate**, not an independent outside audit.

Outcome: **success and metric movement**. Chaining the archived `n<=70` certificate with the new exact rows gives

`N_exact = 75`.                                                        (7.3)

No all-`n` closure is inferred.

## 8. Method #28 — REPLACE FOR ALL WITH FOR TYPICAL: isolate the dangerous sector without weakening the certificate

This method is diagnostic only; the finite certificate still checks **all** interior `k`.

For each row I separately recorded the minimum relative ratio in the long sector `k>=ceil(n/2)` and in the complementary short sector. The results for the new rows are:

| n | global/long-sector minimizer | global ratio | short-sector minimizer | short-sector ratio |
|---:|---:|---:|---:|---:|
| 71 | 44 | 1.088407093987962 | 35 | 1.094997570840493 |
| 72 | 44 | 1.087075926085345 | 35 | 1.094323781035674 |
| 73 | 45 | 1.085802214907739 | 36 | 1.092076109703174 |
| 74 | 45 | 1.084564324835599 | 36 | 1.091434705620569 |
| 75 | 46 | 1.083351317277728 | 37 | 1.089329196844959 |

So the exact global minimum lies in the recurrence-controlled long sector at every row `70<=n<=75`, while the short-sector minimum has a visibly larger margin. This does **not** prove the long sector is always extremal. It does, however, give a source-faithful target for the next analytic attack: propagate a positive Turán/log-concavity margin directly through the Kauers--Wang recurrences instead of paying for all shapes uniformly.

Outcome: **useful route isolation**, with no change of source quantifiers and no substitution of a typical-case theorem for the all-`k` finite certificate.

## 9. Status and counters

The parent conjecture remains **OPEN** and this worker remains **PARTIAL**. The finite metric genuinely moved from 70 to 75, so the unchanged-run counter resets from **2 to 0**. Stuck recoveries remain **0**. No Section-I stuck report is due.

Neither closure audit has passed:

- P26: **NOT PASSED / no P0282 PASS recovered**;
- NM13-08: **NOT PASSED / newest report is on P0093, not a P0282 audit**.

No paper package is warranted because the source is not closed.

## 10. Next mathematical step

The most valuable next route is **not** another blind partition census. Use the exact Kauers--Wang recurrences to derive an evolution equation or invariant region for the Turán quantities

`T_{n,k}=a_{n,k}^2-a_{n,k-1}a_{n,k+1}`

in the long-LIS sector, starting from the now-certified positive boundary data. The key question is whether positivity of a small coupled set of adjacent `T`-quantities propagates from row `n` to `n+1` under (6.1)--(6.2), possibly after normalizing by a positive neighboring coefficient. Failure should be recorded as an explicit sign-indefinite term rather than hidden behind more finite checks.

A complementary finite computation is justified only if it tests such a recurrence-derived invariant or finds a counterexample to it; simply increasing `N_exact` again without a new route would violate the new-methods-first policy.

## 11. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  worker: NM13-07
  namespace: proofnet24/NM13-07/
  category: CLOSABLE_OUTSIDE
  source_id: aim_kpz_followup_2025
  claim_id: P0282
  canonical_dedup_key: chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis
  source_status: OPEN
  worker_status: PARTIAL
  metric:
    name: N_exact
    definition: largest N with archived exact-arithmetic verification of every Chen fixed-size LIS log-concavity inequality for every 1<=n<=N
    before: 70
    after: 75
    movement: true
  methods_actual:
    - 17
    - 25
    - 28
  method_outcomes:
    17: Kauers-Wang long-LIS recurrences identified as an independent exact route covering the empirically weakest sector
    25: exact hook-sum rows 71..75 cross-checked by Euler partition counts, factorial mass, and two recurrence families; metric moved
    28: every exact global minimum for n=70..75 lies in the long-LIS sector; diagnostic only, not a weakened source claim
  certificate:
    checker: proofnet24/NM13-07/artifacts/2026-09-18/p0282_n71_75_exact_kw.cpp
    output: proofnet24/NM13-07/artifacts/2026-09-18/p0282_n71_75_exact_kw.out
    output_blob: c8d5bfa940bcea2b5c457144d68bc65bf9ab6c42
    exact_new_rows: 71..75
    new_partitions_processed: 31483441
    kw_recurrence2_checks: 184
    kw_recurrence1_checks: 146
    result: ALL_EXACT_CHECKS_PASS
    audit_label: self-check_only
  unchanged_runs:
    before: 2
    after: 0
  stuck_recoveries:
    before: 0
    after: 0
  audits:
    P26: NOT_PASSED
    NM13-08: NOT_PASSED
  literature_check_date: 2026-09-18
  literature_scope: original Chen statement; BLS 2015; GXY 2017; Novak-Rhoades 2020; BKM 2024/2026; Kauers-Wang 2026-09-02; exact-name/current searches
  literature_result: no full fixed-size resolution found in bounded search; worldwide openness and novelty not certified
  next_step: derive and test a Turan-positivity propagation/invariant-region formulation from the Kauers-Wang long-LIS recurrences before doing any further bulk census
```

## 12. Scope guard

This invocation created substantive artifacts only because the frozen metric moved. It did not edit `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign roots, claims, peer namespaces, workflows, permissions, public surfaces, email/Drive resources, paid compute or schedules. It does not call P0282 closed, proved, refuted or known. The certified statement is only the exact finite extension `N_exact=75`, plus the previously recorded restricted analytic theorems.