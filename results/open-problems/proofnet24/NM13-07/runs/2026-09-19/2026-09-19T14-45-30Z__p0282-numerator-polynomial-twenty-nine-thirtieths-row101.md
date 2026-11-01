Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-METRIC MOVEMENT: `N_exact = 100 -> 101`; Section-B methods actually tried: #18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE, and #30 DO ONE PRIME / ONE SCALE / ONE DIRECTION AT A TIME. All three are RECYCLED because all 30 numbered methods have already genuinely been used on P0282; this triple differs from the predecessor's #23/#26/#3.**

# NM13-07 — P0282 numerator-polynomial cancellation, diagonal curvature through order 28, a 29/30 growing-defect window, and exact row 101

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-07` / `proofnet24/NM13-07/`  
Category: **CLOSABLE OUTSIDE**  
Canonical source / claim: `aim_kpz_followup_2025` / `P0282`, `operations/claims/P0282.md`  
Canonical dedup key: `chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis`  
SHA-256: `08312c764bd0e9331fed25b1f255810f3c3b9e0f81134520fa26aca4c9c471a4`  
Selection shard: `6 mod 13`  
Source status: **OPEN**  
Worker status after this run: **PARTIAL**  
Frozen metric: **`N_exact = 100 -> 101`**  
Unchanged-run counter: **`0 -> 0`**  
Stuck-recovery counter: **`0 -> 0`**  
Required audits: **P26 NOT PASSED / NM13-08 NOT PASSED**

## 1. Continuity, ownership, and access truth

This invocation continues the already admitted P0282 assignment. I did **not** reopen admission, create a second claim, hash an alias, or treat the worker's original geometric preference as permission to abandon an active source. The canonical claim still assigns this exact source exclusively to NM13-07, with the same dedup key, SHA-256, and residue-6 shard. A current repository search recovered no P0282 audit PASS, owner-authorized release, competing alias owner, settlement, or posting.

Before new mathematics I freshly read or exact-target-recovered the controlling material required by policy:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0282.md`;
- authoritative predecessor `proofnet24/NM13-07/runs/2026-09-19/2026-09-19T13-48-00Z__p0282-curvature-block-nineteen-twentieths-row100.md`;
- newest visible neighboring NM13-06 report `proofnet24/NM13-06/runs/2026-09-19/2026-09-19T14-36-00Z__post-p0195-admission-delta-screen-29-campbell-q18-released-hard-row100.md`;
- newest visible designated secondary-auditor report `proofnet24/NM13-08/runs/2026-09-19/2026-09-19T14-40-00Z__admission-delta-screen-27-campbell-q18-released-hard-q19-owned-hard-row100.md`;
- the Codex P0282 catalogue entry and `P0282-A001` attempt in `probability_campaign_2026_09/codex_20h_20260906/attempts.jsonl`; and
- exact P0282 / canonical-key / ownership / audit searches.

The newest NM13-08 report explicitly continues to treat P0282 as NM13-07's active residue-6 source and does not claim an audit PASS. Current P26-targeted search likewise recovered no P0282 PASS. Therefore neither designated outside audit is counted as passed.

The append-only `probability_1000_intake_*/problems.jsonl` and probability-attempt corpora are too large for an honest claim that every unchanged historical byte was freshly rendered model-visible in this invocation. I make no such claim. Instead I preserved the already completed canonical reconciliation and ran an exact Git comparison from the predecessor report creation commit `7d94ae4d7ef4eb00ee50c61f9e2b2c2a75f5e0e5` to current `master`. At the comparison point it was `ahead_by=101`, `behind_by=0`, `too_large=null`. The complete material delta contained no mutation of `operations/claims/P0282.md`, no P0282 release/handoff, no root `QUEUE.md`/`POSTED.md`/`RESULTS.md` mutation, no campaign `INDEX.md`/`RANKING.md` mutation, and no screened intake or attempt-ledger mutation affecting P0282. A final race check after the new artifacts found only one unrelated HARD10 artifact after the last NM13-07 artifact commit and no P0282 ownership/status change.

No private-repository history needed for this decision was known to be inaccessible. Public-web literature checking is bounded and is not a proof of worldwide openness, novelty, or priority.

## 2. Exact source and retained state

For

`ell_{n,k} = #{sigma in S_n : LIS(sigma)=k}`,

Chen's conjecture is

`ell_{n,k}^2 >= ell_{n,k-1} ell_{n,k+1}`

for every positive integer `n` and every `1<k<n`.

As in the retained long-first-row analysis, write the defect

`j = n-k`,

and put

`F_j(n)=ell_{n,n-j}`.

The predecessor state retained two exact source-faithful facts that this run uses rather than re-derives:

1. **all-`n` fixed-defect Chen frontier:** the source inequality is proved for every `j<=66` and every admissible `n`;
2. **stable hook factorization:** in the long-first-row regime,

`F_j(n) = (n)_j^2 / j! * A_j(1/n)`,

where under Plancherel measure on partitions `mu` of `j`,

`A_j(t)=E[R_mu(t)^2]`,

`R_mu(t)=prod_{x in contents(mu)} (1-(j+x)t)/(1-(j+x-1)t)`.

The predecessor also proved the finite-degree lemma: if

`G_j(t)=log A_j(t)=sum_{m>=1} D_m(j)t^m`,

then for every fixed `m`, `D_m(j)` is a polynomial in `j` of degree at most `m`. It also established an analytic disk sufficient for the uniform Cauchy estimate

`|D_m(r)| <= 2(6r)^m`

in the regime used below.

The previous growing-defect theorem had exponent `19/20`, obtained by exact positivity of the Chen Taylor curvatures through order 18 in the active sector `j>=67`.

## 3. Method #18 — say it in another language: exact numerator-polynomial cancellation

The run first changed language instead of immediately computing more Taylor coefficients. The idea was recorded before production validation in

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_numerator_polynomial_diagonal_curvature_idea.md`

(commit `274e67b564ace1b6027cf60db0fbdaf27fa22bfe`).

### Lemma 1 — row telescoping

For `mu=(mu_1,mu_2,...)` partitioning `j`, telescope `R_mu(t)` row by row. In row `r`, the contents are `c-r`, `1<=c<=mu_r`, so

`prod_{c=1}^{mu_r} [1-(j+c-r)t]/[1-(j+c-r-1)t]`

is exactly

`[1-(j+mu_r-r)t]/[1-(j-r)t]`.

Extend `mu_r=0` through `r=j`; the extra factors equal one. Define

`Delta_j(t)=prod_{s=1}^{j-1}(1-s t)`

and

`P_j(t)=E_Plancherel(j)[ prod_{r=1}^j (1-(j+mu_r-r)t)^2 ]`.

Then the denominator is shape-independent, and therefore

**(3.1)** `A_j(t)=P_j(t)/Delta_j(t)^2`.

Here `P_j(t)` is a genuine polynomial of degree at most `2j` with rational coefficients.

### Lemma 2 — cancellation in the exact LIS count

Whenever the stable decomposition by shapes `(n-j,mu)` is valid for every `mu` (in particular whenever `n>=2j`),

`(n)_j = n^j Delta_j(1/n)`.

Substituting (3.1) into the retained hook factorization cancels the entire falling-factorial denominator:

**(3.2)** `F_j(n)=n^(2j)/j! * P_j(1/n)`.

Consequently the literal source Chen ratio simplifies to

**(3.3)**

`F_j(n)^2/[F_{j-1}(n)F_{j+1}(n)]`

`= ((j+1)/j) * P_j(1/n)^2/[P_{j-1}(1/n)P_{j+1}(1/n)]`.

This is an exact source-level reformulation, not an asymptotic approximation. The earlier deterministic factor `((n-j+1)/(n-j))^2` in the `A_j` language is precisely canceled by the neighboring `Delta` factors in the `P_j` language.

The production self-check independently verifies `A_j Delta_j^2=P_j` exactly for `1<=j<=10` through the full polynomial degree. That finite check is supplementary; the proof above is the theorem-sized argument.

**Outcome of #18:** success. The source is now expressed through one Plancherel-averaged numerator polynomial, which is a cleaner target for any eventual whole-series curvature or real-stability/Lorentzian attack. This does not close Chen.

## 4. Method #25 — support-pattern counting: what the all-order proof would need

The predecessor's finite-degree lemma comes from grouping identity transposition words by support/equality pattern in Jucys-Murphy products. I tried to strengthen that mechanism into an all-order sign theorem for

`C_m(j)=2D_m(j)-D_m(j-1)-D_m(j+1)`.

A naive term-by-term positivity proof is not available: the logarithm performs cumulant/Mobius subtraction and mixes support patterns with alternating signs. The already exact obstruction `C_11(1)=-1410` shows that no all-`j` positive pattern decomposition can be correct without a compensating threshold or regrouping.

The more plausible statement suggested by the support-size mechanism is a **diagonal threshold** such as

`C_m(j)>0 whenever j>=m`.

I did not obtain an all-order proof of that statement in this invocation, so it is **not** promoted to a theorem. What I did obtain is a substantially larger exact finite block that points directly at this threshold and is sufficient for a new source theorem.

**Outcome of #25:** partial. The route sharpens the structural target to a thresholded support-pattern positivity theorem; it does not yet supply the missing all-order regrouping.

## 5. Method #30 — one Taylor order at a time, then one tail: exact diagonal block through order 28

Production checker:

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_diagonal_curvature28_selfcheck.py`

Archived output:

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_diagonal_curvature28_selfcheck.out`

The checker uses exact rational arithmetic only. For every `m<=28`, it computes exact `D_m(j)` values from partitions/hook dimensions, reconstructs the globally valid polynomial `D_m(j)` using the retained degree bound `deg D_m<=m`, and verifies the interpolation at two extra integer values not used for reconstruction.

It then computes `C_m(j)` and proves the following finite theorem by exact coefficient inspection:

### Lemma 3 — exact diagonal curvature block

For every integer `m` with `2<=m<=28`, every coefficient of

`C_m(m+x)`

is strictly positive. Hence

**(5.1)** `C_m(j)>0` for every `2<=m<=28` and every integer `j>=m`.

The leading coefficient of every checked curvature polynomial is exactly

`2m(m-1)`.

In particular, in the active source sector `j>=67`, all Taylor curvatures through order 28 are positive. For the ten genuinely new orders, the minimum coefficient after shifting by `j=67+x` is:

- `m=19: 684`
- `m=20: 760`
- `m=21: 840`
- `m=22: 924`
- `m=23: 1012`
- `m=24: 1104`
- `m=25: 1200`
- `m=26: 1300`
- `m=27: 1404`
- `m=28: 1512`.

The output ends `ALL_EXACT_CHECKS_PASS`.

This is a finite exact certificate, not a claim that (5.1) holds for all orders.

## 6. New theorem — a 29/30 growing-defect window

Define the truncation remainder after order 28 by

`R_r = sum_{m>=29} D_m(r)n^(-m)`.

For `r in {j-1,j,j+1}`, put

`q=6(j+1)/n`.

If `n>=8(j+1)`, then `q<=3/4`. The retained Cauchy estimate gives

`|R_r| <= 2 sum_{m>=29} q^m <= 8 q^29`.

Therefore the discrete-curvature tail satisfies

`|2R_j-R_{j-1}-R_{j+1}|`

`<= 32 * 6^29 * (j+1)^29 / n^29`.

The exact checker verifies

`32*6^29 = 1179060905177244575465472 < 2^80`.

Now assume `j>=67` and

**(6.1)** `n^29 >= 2^81 (j+1)^30`.

Because `j+1>=68`, (6.1) also implies `n>8(j+1)`, so the analytic estimate above is valid. It further gives

`|tail curvature| < 1/[2(j+1)]`.

The exact source ratio in the retained `A_j` language has logarithm

`log Q_j(n)`

`= log((j+1)/j) + 2 log((n-j+1)/(n-j))`

`  + [2G_j(1/n)-G_{j-1}(1/n)-G_{j+1}(1/n)]`.

The second term is strictly positive. By Lemma 3, every retained Taylor-curvature term through order 28 is nonnegative, and in the active sector the relevant orders are strictly positive. Finally,

`log((j+1)/j) >= 1/(j+1)`.

Thus under (6.1),

`log Q_j(n) > 1/(j+1) - 1/[2(j+1)] > 0`.

We obtain:

### `NM13-07-P0282-TWENTY-NINE-THIRTIETHS-WINDOW-11`

For every integer `j>=67`,

**(6.2)** `n^29 >= 2^81 (j+1)^30`

implies

`F_j(n)^2 > F_{j-1}(n)F_{j+1}(n)`.

A simpler sufficient condition is

**(6.3)** `j+1 <= n^(29/30)/8`,

because `8^30=2^90>2^81`.

For `j<=66`, the retained all-`n` theorem already proves Chen. Hence the source conjecture is now rigorously established throughout the long-LIS boundary window (6.3).

The rigorous growing-defect exponent therefore advances

**`19/20 -> 29/30`.**

This is a source-faithful **PARTIAL** theorem. It still does not reach defects proportional to `n`, and nothing here is called source closure.

**Outcome of #30:** success. A ten-order extension of the exact curvature block, followed by one tail estimate, moves the asymptotic boundary without changing the source metric.

## 7. Frozen metric — exact row 101

The frozen metric is still

`N_exact = largest N for which every interior Chen inequality has an exact certificate for every row n<=N`.

It is not replaced by the growing-defect exponent, the fixed-defect frontier, or the ULC frontier.

For row `n=101`, the retained exact theorem for defects `j<=66` covers all source inequalities with `k>=35`. Therefore only the low-LIS seam

`k=2,...,34`

requires new finite computation.

Production checker:

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_row101_gessel_low.cpp`

Archived output:

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_row101_gessel_low.out`

The checker evaluates the Gessel Toeplitz determinant modulo 18 independently primality-checked moduli, reconstructs the exact counts by CRT, and verifies the result lies in the unique integer range because the CRT modulus has **539 bits** while `101!` has **532 bits** and the modulus exceeds `2*101!`.

Independent internal normalization checks include

`u_2(101)=Catalan_101`

exactly, with

`Catalan_101 = 3533343320884635898708258511468514257188006702535057407320`.

All **33** newly required source inequalities `k=2,...,34` are strictly positive. The weakest new low-seam ratio occurs at `k=34`:

`ell_{101,34}^2/[ell_{101,33} ell_{101,35}]`

`~= 1.08833490030109031 > 1`.

The exact numerator, denominator, and positive margin are archived in the output. The checker ends `ALL_EXACT_CHECKS_PASS`.

Chaining the low seam to the retained exact theorem for `k>=35` certifies every interior source inequality in row 101. Therefore

**`N_exact = 100 -> 101`.**

The predecessor archive certifies all rows through 100, so this is genuine frozen-metric movement rather than a disconnected new row.

## 8. Literature / prior-art refresh — 2026-09-19

Fresh bounded queries included variants of:

- `Chen log-concavity conjecture longest increasing subsequence fixed size permutation 2026`;
- `arXiv Chen log concavity permutation LIS Baslingker Krishnapur Madiman 2412.15116`;
- `Kauers Wang recurrences permutations long increasing subsequences 2026 log concavity`;
- `Rhoades longest increasing subsequence Hilbert series Chen log concavity 2024`;
- `longest increasing subsequence fixed defect polynomial hook formula Plancherel content`;
- `n-j longest increasing subsequence permutations hook formula polynomial`; and
- `Chen log concavity fixed defect longest increasing subsequence polynomial`.

Relevant recovered primary/current sources:

1. **Chen's fixed-size conjecture remains listed as open** by the current MathDB entry for the problem.
2. **Bóna–Lackner–Sagan**, *Longest increasing subsequences and log concavity* (arXiv:1511.08653), restate Chen and prove related/restricted analogues rather than the fixed-size conjecture.
3. **Gao–Xie–Yang**, *Schur positivity and log-concavity related to longest increasing subsequences* (arXiv:1703.06382), prove Schur-positive restricted results and propose an approach, not a full resolution.
4. **Novak–Rhoades**, *Increasing Subsequences and Kronecker Coefficients* (arXiv:2006.13146), formulate a stronger Kronecker-coefficient conjecture implying Chen.
5. **Rhoades**, *Increasing subsequences, matrix loci, and Viennot shadows* (arXiv:2306.08718; 2024 version), gives the Hilbert-series/Viennot-shadow framework, not Chen's full theorem.
6. **Baslingker–Krishnapur–Madiman**, *Log-concavity in one-dimensional Coulomb gases and related ensembles* (arXiv:2412.15116), prove the **Poissonized** Plancherel top-row result and describe it as the first positive result toward Chen, explicitly not the fixed-size resolution.
7. **Clifford–Clifford**, *Exact Sampling of Permutations with a Fixed Longest Increasing Subsequence* (arXiv:2606.02263, 2026-06-01), supplies exact conditional sampling/determinant machinery, not fixed-size log-concavity.
8. **Kauers–Wang**, *Recurrences for permutations with long increasing subsequences* (arXiv:2609.02220, submitted 2026-09-02), prove two bivariate recurrences and D-finiteness in a range, not Chen's fixed-size log-concavity.

No matching published `29/30` boundary theorem, exact `P_j` numerator-polynomial reformulation, or fixed-size resolution surfaced in these bounded searches. That is **negative evidence only**. Novelty and priority of the new statements in this report remain **UNVERIFIED**. The Jucys-Murphy/content machinery and hook telescoping used in the derivation are classical mechanisms; no novelty is claimed for those mechanisms themselves.

## 9. Audit / closure status

Worker result: **PARTIAL**.  
Parent source: **OPEN**.  
New theorem-sized claim: `NM13-07-P0282-TWENTY-NINE-THIRTIETHS-WINDOW-11`, proved on this page with exact finite support for the Taylor block.  
Structural lemma: exact numerator-polynomial cancellation (3.1)–(3.3), proved on this page.  
Finite row-101 claim: exact and archived.  
Novelty: **UNVERIFIED**.  
P26 audit: **NOT PASSED / no source-matching P0282 PASS recovered**.  
NM13-08 audit: **NOT PASSED / newest NM13-08 report contains no P0282 audit PASS**.

The exact checkers are **self-checks/certificates**. They do not count as either independent outside audit. No paper folder is created because the literal source conjecture is not closed.

## 10. Next research step

The strongest next route is now more precise than “compute order 29.” The exact block suggests the candidate threshold

`C_m(j)>0 for j>=m`.

The next primary attack should try to prove that—or a weaker controlled threshold `j>=phi(m)`—directly from support/equality-pattern combinatorics after the cumulant/Mobius cancellations are grouped correctly. A polynomial or linear bound on `phi(m)` would turn the current finite-order exponent lifting into a reusable all-order mechanism and could push the boundary arbitrarily close to linear defect without computing each coefficient separately.

In the new numerator language, an equivalent structural direction is to study

`H_j(t)=log P_j(t)`

and seek a whole-series positive-curvature representation for

`2H_j(t)-H_{j-1}(t)-H_{j+1}(t)`

under a tilted Plancherel law. The exact identity (3.3) removes the falling-factorial nuisance completely. A variance/covariance, stable-polynomial, or injection representation here would be qualitatively stronger than extending the Taylor block to order 38.

Only if those structural routes fail should the next invocation extend the finite block again.

## 11. Runtime/model-control truth

The requested first-line setting was `Model: GPT-6. Reasoning: maximum`. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this worker, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 maximum, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

**The scheduler exposes no model selector and no reasoning selector.** The task-control schema available in this runtime exposes title/prompt, schedule or relative-start fields, timing mode, enabled state, listing, and updates; it has no persistent model-family field, no reasoning-effort field, and no authenticated applied-runtime model/effort receipt. Therefore GPT-6/maximum remains prompt text only in this interface.

Making the request binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists explicit model-family and reasoning-effort routing fields into inference and returns authenticated per-run applied-model/applied-effort telemetry.

The historical P26 `You cannot modify this task` result remains an authorization-context boundary rather than proof of global immutability; repository continuity records later successful P26 updates from another authorized context. If that denial recurs, the compliant workaround is the owning or otherwise authorized account/workspace/API/admin context, an authorized ownership transfer where supported, or platform support for the **same existing task**. It is not task duplication, identity substitution, or permission bypass. This invocation did not create, modify, disable, or duplicate any schedule or permission.

## 12. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: NM13-07
  namespace: proofnet24/NM13-07/
  source_id: aim_kpz_followup_2025
  canonical_problem_id: P0282
  claim_path: operations/claims/P0282.md
  dedup_key: chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis
  source_status: OPEN
  worker_status: PARTIAL
  frozen_metric:
    name: N_exact
    before: 100
    after: 101
    movement: true
  retained_frontiers:
    all_n_fixed_defect_Chen_j_max: 66
    all_n_ULC_shadow_density_j_max: 32
  growing_defect_window:
    before_exponent: 19/20
    after_exponent: 29/30
    theorem_condition: n^29 >= 2^81 * (j+1)^30 for j>=67
    simple_condition: j+1 <= n^(29/30)/8
  new_claim_ids:
    - NM13-07-P0282-TWENTY-NINE-THIRTIETHS-WINDOW-11
    - NM13-07-P0282-NUMERATOR-POLYNOMIAL-11
    - NM13-07-P0282-ROW101-EXACT-11
  methods:
    - number: 18
      name: SAY IT IN ANOTHER LANGUAGE
      recycled: true
      outcome: exact numerator-polynomial cancellation F_j=n^(2j)P_j(1/n)/j! in stable range; source ratio simplified
    - number: 25
      name: COUNT THE SAME THING TWICE
      recycled: true
      outcome: all-order support-pattern sign proof not obtained; thresholded j>=m formulation isolated
    - number: 30
      name: DO ONE PRIME / ONE SCALE / ONE DIRECTION AT A TIME
      recycled: true
      outcome: exact diagonal curvature block m=2..28; one analytic tail gives 29/30 theorem
  exact_artifacts:
    - proofnet24/NM13-07/artifacts/2026-09-19/p0282_numerator_polynomial_diagonal_curvature_idea.md
    - proofnet24/NM13-07/artifacts/2026-09-19/p0282_diagonal_curvature28_selfcheck.py
    - proofnet24/NM13-07/artifacts/2026-09-19/p0282_diagonal_curvature28_selfcheck.out
    - proofnet24/NM13-07/artifacts/2026-09-19/p0282_row101_gessel_low.cpp
    - proofnet24/NM13-07/artifacts/2026-09-19/p0282_row101_gessel_low.out
  exact_checks:
    diagonal_curvature_2_28: PASS
    numerator_polynomial_j1_10: PASS
    row101_low_seam_33_cells: PASS
    row101_Catalan_crosscheck: PASS
  unchanged_runs:
    before: 0
    after: 0
  stuck_recoveries:
    before: 0
    after: 0
  audits:
    P26: NOT_PASSED
    NM13-08: NOT_PASSED
  novelty: UNVERIFIED
  next_step: prove an all-order controlled threshold for Taylor curvature (ideally C_m(j)>0 for j>=m) or a whole-series positive-curvature representation for log P_j
```
