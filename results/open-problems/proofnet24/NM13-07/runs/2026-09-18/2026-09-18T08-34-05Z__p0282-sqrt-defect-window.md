Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `N_exact = 70 -> 70`. Section-B methods actually tried: #11 DUALIZE; #20 FIND WHY THE ALGORITHM FAILS; #30 DO ONE SCALE, ONE DIRECTION AT A TIME.**

# NM13-07 research invocation — P0282 growing-defect log-concavity window

Run date: 2026-09-18 UTC  
Track / namespace: `proofnet24/NM13-07`  
Category: `CLOSABLE OUTSIDE`  
Canonical source / claim: `P0282`, `operations/claims/P0282.md`  
Canonical dedup key: `chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis`  
Parent source status after this run: **OPEN**  
NM13-07 status after this run: **PARTIAL**  
Frozen metric before / after: **`N_exact = 70 -> 70`**  
Consecutive unchanged runs on P0282: **0 -> 1**  
Stuck recoveries on P0282: **0 -> 0**  
Designated eventual outside auditors: **P26 and NM13-08; neither is counted as passed**

## 1. Runtime and task-control disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this report, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The task-control schema exposed to this session still offers title/prompt, schedule or relative-start fields, timing mode, and enabled state, but **no bindable model-family selector and no bindable reasoning-effort selector**. `GPT-6 / maximum` therefore remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface that exposes persistent model and reasoning settings together with authenticated per-run runtime attestation.

I did not attempt to modify any scheduler task in this invocation. The repository's current policy/reconciliation records the historical P26 `You cannot modify this task` result as authorization-context-specific and also records that P26 was later updated from another authorized context. The lawful remedy for any future denial is the owning/otherwise-authorized task context or an authorized product/admin/API/support path for that same task, never cloning the job, changing permissions, or bypassing access controls.

## 2. Authoritative continuity and repository read

This invocation continues the already admitted P0282 target; it is **not a new admission** and no new claim was created.

Before new mathematics I reread or targeted-recovered current `master` state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment/deployment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0282.md`;
- exact P0282 / canonical-key / `P0282-A` attempt / audit searches and the intake dedup evidence;
- newest own report `proofnet24/NM13-07/runs/2026-09-18/2026-09-18T07-34-34Z__p0282-n70-top4.md`;
- newest visible neighboring NM13-06 report `...T07-30-30Z__p0195-stuck-recovery-1.md`;
- newest visible neighboring NM13-08 report `...T07-46-00Z__p0093-all-arity-fixed-simplex.md`.

The canonical claim still records owner `NM13-07`, SHA256 key `08312c764bd0e9331fed25b1f255810f3c3b9e0f81134520fa26aca4c9c471a4`, and shard residue 6. I recovered no owner-authorized release, competing alias owner, retirement, POSTED closure, campaign settlement, or P0282 audit pass. The exact-attempt search still recovers no separate `P0282-A...` attempt ledger row beyond the claim/history already incorporated by this track. NM13-06 remains on P0195; NM13-08 remains on P0093 and has not audited P0282.

The pre-report `master` head observed after this run's substantive artifacts was `d77ffdef927f4c64f21ba5a3261de646fdeb0518` (2026-09-18T08:40:17Z). Concurrent commits belong to other workers and do not release P0282.

The preceding P0282 report is authoritative continuity. It established `N_exact=70`, proved strict Chen inequalities at the top four interior positions for every valid `n`, and derived for fixed defect `j` the asymptotic `E_j(n)=n^(2j)/j!+O_j(n^(2j-1))`, where `E_j(n):=ell_{n,n-j}`. It also showed that the checked near-extremizer had moved inward to defect 27 at `n=70`, and it explicitly reserved methods #11/#20/#30 for the present growing-defect run. I do not reuse the preceding #4/#18/#24 triple.

Large JSONL/root surfaces can be connector-bounded when rendered wholesale. Exact canonical identity, claim, dedup index, immutable reports and targeted ownership/attempt/audit searches are therefore the continuity anchors; truncation is never treated as evidence of absence.

## 3. Exact source and bounded current literature check — 2026-09-18

For a uniform permutation `sigma` of `[n]`, write

`ell_{n,k} = #{sigma in S_n : LIS(sigma)=k}`.

Chen's source conjecture is

`ell_{n,k}^2 >= ell_{n,k-1} ell_{n,k+1}`

for every `n` and every interior `1<k<n`.

The bounded 2026-09-18 literature refresh searched the exact Chen conjecture, fixed-size Plancherel log-concavity, growing-defect / square-root-defect variants, and the new long-LIS recurrences. Current evidence remains:

1. Chen's fixed-size conjecture is still listed as open in current secondary indexing and continues to be stated in the Bóna--Lackner--Sagan line of work.
2. Baslingker--Krishnapur--Madiman prove the Poissonized result and fixed-defect eventual positivity, but that is not the all-`n` fixed-size conjecture and does not, in the material recovered here, state the growing `j=Theta(sqrt n)` window proved below.
3. Manuel Kauers and Chen Wang, arXiv:2609.02220, submitted 2026-09-02, prove two exact bivariate recurrences for `a_{n,k}=ell_{n,k}` in the sector `n/2 <= k <= n`:

   `(KW1)  a_{n+1,k} + n^2 a_{n-1,k} = a_{n,k+1} + (2n-1)a_{n,k} + a_{n,k-1}`,

   `(KW2)  (n+1)^2(a_{n,k}+a_{n,k+1}) = (n-k+1)a_{n+1,k} + (n+k+1)a_{n+1,k+1}`.

   The paper's theorem/abstract concerns these recurrences and D-finiteness in the long-LIS sector; it does not claim Chen's log-concavity conjecture. I inspected the paper itself, including its theorem page and the page displaying the neighboring guessed `n/3<k<n/2` recurrence, rather than relying only on an abstract.

No source matching full resolution, nor a clearly matching published square-root boundary theorem, surfaced in this bounded search. That is **bounded negative evidence only**, not proof of worldwide openness and not a novelty certificate. Publication novelty of the theorem below remains **UNVERIFIED**.

## 4. Frozen metric

The admitted metric remains exactly

`N_exact = largest N for which NM13-07 has an archived exact-arithmetic certificate verifying every Chen inequality for every 1<=n<=N`.

Before this run: **70**.  
After this run: **70**.

I deliberately did not spend the run extending the finite table. The new result is an infinite, growing-defect restricted theorem, but the metric is not silently redefined to count boundary layers or theorem strength. Therefore this is honestly **no frozen-metric movement**, and the unchanged-run counter advances `0 -> 1`.

## 5. Idea-before-checking record

Before writing the archival self-check I recorded the new route in

`proofnet24/NM13-07/artifacts/2026-09-18/p0282_sqrt_defect_window_idea.md`

at commit `7742bda3d391af50f42f7b4eca4a721a76d5910a`.

The idea was to factor the residual-partition hook correction as a Plancherel expectation, dualize Chen's inequality to adjacent ratios, and use only one scale (`j` versus `sqrt n`) until the exact obstruction became visible. The exact self-check was written only afterward.

## 6. Method #11 — DUALIZE: isolate the only nontrivial curvature factor

Put

`E_j(n):=ell_{n,n-j}`.

For `n>=2j`, every relevant RSK shape is uniquely `lambda=(n-j,mu)` with `mu |- j`. The preceding report proved the exact hook formula

`f^(n-j,mu) = binom(n,j) f^mu R_mu(n,j)`,

where

`R_mu(n,j) := prod_{c=1}^{mu_1} (n-j-c+1)/(n-j-c+1+mu'_c)`.

Let `P_j(mu)=(f^mu)^2/j!` be Plancherel measure on partitions of `j`, and define

`A_j(n):=E_{mu~P_j}[R_mu(n,j)^2]`.

Robinson--Schensted and `sum_{mu|-j}(f^mu)^2=j!` give the **exact factorization**

`E_j(n) = binom(n,j)^2 j! A_j(n)`

`       = ((n)_j^2/j!) A_j(n)`.                                      (6.1)

The Chen ratio at defect `j` is therefore

`Q_j(n):=E_j(n)^2/[E_{j-1}(n)E_{j+1}(n)]`

`= ((j+1)/j) ((n-j+1)/(n-j))^2 * A_j(n)^2/[A_{j-1}(n)A_{j+1}(n)]`.    (6.2)

The first two factors are explicit and strictly above 1. Thus the source inequality has been reduced to controlling the discrete curvature of a single Plancherel hook-correction sequence `A_j(n)`.

**Outcome of #11:** success. This is a cleaner dual object than the raw counts: factorial/falling-factorial curvature is solved exactly, and all remaining difficulty is localized in `A_j`.

## 7. Method #20 — FIND WHY THE ALGORITHM FAILS: the new bivariate recurrences are not manifestly TP2-preserving

The Kauers--Wang recurrences are directly relevant because the present boundary regime lies inside their proven sector. Substituting `k=n-j` into `(KW1)` and `(KW2)` gives

`E_{j+1}(n+1) + n^2 E_{j-1}(n-1)`

`    = E_{j-1}(n) + (2n-1)E_j(n) + E_{j+1}(n)`,                    (7.1)

and

`(n+1)^2(E_j(n)+E_{j-1}(n))`

`    = (j+1)E_{j+1}(n+1) + (2n-j+1)E_j(n+1)`.                     (7.2)

A naive induction on log-concavity would need a positive/TP2 kernel mapping one same-`n` log-concave row to the next. Equation (7.1) does not present such a kernel: solving for the new term introduces

`- n^2 E_{j-1}(n-1)`.

Equation (7.2) has positive coefficients as written but couples two unknown terms on the new row; solving for either one introduces a subtraction of the other. Dividing by adjacent `E_j` values likewise does not close on the same-row ratio field `E_j/E_{j-1}`.

This is the exact obstruction to the most obvious recurrence-propagation algorithm. It does **not** prove that no positive combination, determinant identity, or higher-dimensional cone built from the two recurrences can work. It does explain why simply citing D-finiteness or iterating either recurrence does not prove Chen log-concavity.

There is a second, independent obstruction visible in the hook-correction route below: the worst-shape loss is of order `j/n`, while the explicit factorial log-concavity margin is only of order `1/j`. They balance at `j~sqrt n`. Thus a shape-uniform correction bound cannot by itself enter `j >> sqrt n`.

**Outcome of #20:** successful failure diagnosis. The next recurrence route must either construct a genuinely TP2 combination of (7.1)--(7.2) or import more information about the distribution of `R_mu` than a worst-shape bound.

## 8. Method #30 — ONE SCALE, ONE DIRECTION: a complete `j=O(sqrt n)` theorem

The residual partition formula already gives enough uniform control for a nontrivial growing window.

### Theorem `NM13-07-P0282-SQRT-DEFECT-03`

For every integer `j>=1` and every integer

`n >= 4j^2 + 6j - 1`,                                                (8.1)

Chen's inequality is **strict** at `k=n-j`:

`ell_{n,n-j}^2 > ell_{n,n-j-1} ell_{n,n-j+1}`.                       (8.2)

Equivalently, for every `n`, strict log-concavity holds simultaneously throughout the boundary window

`1 <= j <= floor((sqrt(4n+13)-3)/4)`.                                (8.3)

In particular the proved defect range grows like `(1/2)sqrt n`, rather than remaining fixed.

### Proof

Condition (8.1) implies `n>=2(j+1)`, so the exact representation (6.1) is valid for `j-1,j,j+1`.

For every `mu|-j`, since `sum_c mu'_c=j` and `c<=mu_1<=j`,

`n-j-c+1 >= n-2j+1`.

Therefore

`log R_mu(n,j)`

`= - sum_c log(1 + mu'_c/(n-j-c+1))`

`>= - sum_c mu'_c/(n-j-c+1)`

`>= - j/(n-2j+1)`,                                                    (8.4)

where `log(1+x)<=x` was used. Hence

`exp(-2j/(n-2j+1)) <= A_j(n) <= 1`.                                  (8.5)

Apply the lower bound only to the numerator correction in (6.2), and the trivial upper bound `A<=1` to both denominator corrections. This yields

`Q_j(n)`

`>= ((j+1)/j) ((n-j+1)/(n-j))^2 exp(-4j/(n-2j+1))`.                  (8.6)

Taking logarithms,

`log Q_j(n)` is bounded below by

`log(1+1/j) + 2 log(1+1/(n-j)) - 4j/(n-2j+1)`.                       (8.7)

For every `j>=1`, the standard strict inequality

`log(1+x) > x/(1+x)` for `x>0`

gives

`log(1+1/j) > 1/(j+1)`.                                               (8.8)

Condition (8.1) is exactly equivalent to

`1/(j+1) >= 4j/(n-2j+1)`.                                             (8.9)

Combining (8.7)--(8.9), and retaining the strictly positive second logarithm in (8.7), gives `log Q_j(n)>0`. Hence `Q_j(n)>1`, which is precisely (8.2).

Finally, solving `4j^2+6j-1<=n` for `j>=0` gives

`j <= (sqrt(4n+13)-3)/4`,

which is (8.3). This proves the theorem. `square`

### What this theorem does and does not do

This is source-faithful infinite restricted progress: it proves a growing boundary class without changing the ensemble or the inequality. It does **not** settle the central/Tracy--Widom-scale region, does not prove full fixed-size log-concavity, and is not being labeled a publication-novel theorem before broader prior-art review and outside audits.

**Outcome of #30:** success. The run moves from fixed defect to an explicit uniform square-root defect window, while keeping the source statement unchanged.

## 9. Exact self-check after the proof

After recording the idea, I wrote an independent exact-arithmetic self-check using only Python's standard library and rational/integer arithmetic:

- checker: `proofnet24/NM13-07/artifacts/2026-09-18/p0282_sqrt_defect_window_check.py`, creation commit `d36c47efe95962441b93e24f9896a8c33b513177`;
- output: `proofnet24/NM13-07/artifacts/2026-09-18/p0282_sqrt_defect_window_check.out`, creation commit `519c01aaf862ddd29bbba76b373ff4ddaf07c38a`, GitHub blob `6702a09a40bc03c59871bafc64f6ce4f830c4f94`.

For `j=1,...,12`, the checker evaluates the threshold point `n_0=4j^2+6j-1`, reconstructs `E_{j-1},E_j,E_{j+1}` exactly from residual partitions and hook lengths, checks the exact factorization (6.2), checks the rational sufficient condition (8.9), and verifies a strictly positive exact Chen margin. The output ends

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not the proof of the theorem and not either required independent audit. The all-`j` proof is the analytic argument in Section 8.

## 10. Progress accounting, obstruction and next route

Frozen metric: **`N_exact 70 -> 70`**, no movement.  
Source status: **OPEN**.  
Worker status: **PARTIAL**.  
Unchanged counter: **0 -> 1**.  
Stuck recoveries: **0 -> 0**.

The non-metric mathematical advance is substantial but is not used to relabel the metric: Chen's source inequality is now proved on an explicit growing boundary window `j <= (sqrt(4n+13)-3)/4`.

The proof also identifies the next genuine obstruction. The worst-shape estimate loses about `4j/n` in log-ratio, whereas the solved factorial factor contributes about `1/j`; this route saturates at the square-root scale. To move farther, the next run should replace worst-case `mu` by Plancherel-distribution information about

`log R_mu(n,j) = -sum_c log(1+mu'_c/(n-j-c+1))`,

or find a positive determinant/TP2 combination of the exact Kauers--Wang recurrences. A mere extension of `N_exact` would not address that obstruction.

Reserved, **not yet tried on P0282**, methods for a next run are:

- #5 ADD A PARAMETER AND DIFFERENTIATE — introduce a parameter multiplying the hook correction and study derivatives/cumulants of `log A_j`;
- #12 FIND WHAT IS CONSERVED — inspect the two Kauers--Wang recurrences for a determinant or Wronskian-like invariant controlling adjacent minors;
- #21 ASK WHO ELSE HAS THIS SHAPE — compare the Plancherel expectation `A_j` with concentration/limit-shape estimates for Young diagrams and with total-positivity recurrences in neighboring arrays.

## 11. Audit / closure status

P0282 remains **OPEN / PARTIAL**. No paper folder is created because the source is not closed.

Required outside audits remain:

- P26: **NOT PASSED / no P0282 audit recovered**;
- NM13-08: **NOT PASSED / no P0282 audit recovered**.

The exact self-check is internal and does not count as either audit. A bounded literature search finding no matching square-root theorem does not establish novelty. Standard ingredients used here include Robinson--Schensted, the hook-length formula, Plancherel weights and elementary logarithmic inequalities; they are not relabeled as new mechanisms.

## 12. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  worker: NM13-07
  namespace: proofnet24/NM13-07
  category: CLOSABLE_OUTSIDE
  source_id: P0282
  claim_id: P0282
  canonical_dedup_key: chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis
  source_status_before: OPEN
  source_status_after: OPEN
  worker_status_before: PARTIAL
  worker_status_after: PARTIAL
  frozen_metric:
    name: N_exact
    definition: largest N with an archived exact-arithmetic certificate for every Chen inequality for every 1<=n<=N
    before: 70
    after: 70
    movement: false
  theorem_claims:
    - id: NM13-07-P0282-SQRT-DEFECT-03
      scope: strict Chen inequality at k=n-j for every j>=1 and n>=4j^2+6j-1; equivalently j<=floor((sqrt(4n+13)-3)/4)
      status: SELF_CHECKED_PARTIAL
  methods_actual:
    - 11
    - 20
    - 30
  method_outcomes:
    11: SUCCESS_exact_Plancherel_hook_correction_factorization_and_adjacent_ratio_reduction
    20: SUCCESS_precise_failure_diagnosis_for_naive_Kauers_Wang_TP2_propagation_and_worst_shape_scale
    30: SUCCESS_complete_uniform_sqrt_defect_theorem
  consecutive_unchanged_runs_before: 0
  consecutive_unchanged_runs_after: 1
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
  outside_audits:
    P26: NOT_PASSED
    NM13-08: NOT_PASSED
  artifacts:
    idea_note_commit: 7742bda3d391af50f42f7b4eca4a721a76d5910a
    exact_self_check_commit: d36c47efe95962441b93e24f9896a8c33b513177
    exact_output_commit: 519c01aaf862ddd29bbba76b373ff4ddaf07c38a
    exact_output_blob: 6702a09a40bc03c59871bafc64f6ce4f830c4f94
    exact_output_result: ALL_EXACT_CHECKS_PASS
  literature_check_date: 2026-09-18
  literature_scope: original Chen/Bona-Lackner-Sagan; Baslingker-Krishnapur-Madiman fixed-size-vs-Poissonized progress; Kauers-Wang arXiv:2609.02220 theorem and recurrence pages; bounded searches for growing/sqrt defect Chen log-concavity
  literature_limit: bounded web/arXiv search; no worldwide-openness or publication-novelty certificate
  next_step: replace worst-shape hook correction by Plancherel concentration/cumulant control, or derive a TP2 determinant invariant from Kauers-Wang; try methods 5,12,21; do not merely extend N_exact
```

No shared root, peer namespace, canonical claim, workflow, permission, public surface, email/Drive resource, paid compute, or schedule was modified. Exactly one immutable NM13-07 report is created for this invocation; the creation commit is its receipt and is to be read back directly, with no receipt-only follow-up commit.
