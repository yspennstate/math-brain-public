Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `N_exact = 70 -> 70`. Section-B methods actually tried: #5 ADD A PARAMETER AND DIFFERENTIATE; #12 FIND WHAT IS CONSERVED; #21 ASK WHO ELSE HAS THIS SHAPE.**

# NM13-07 research invocation — P0282 conserved hook mass and an `n^(2/3)` defect window

Run date: 2026-09-18 UTC  
Track / namespace: `proofnet24/NM13-07/`  
Category: `CLOSABLE OUTSIDE`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Canonical source / claim: `P0282`, `operations/claims/P0282.md`  
Canonical dedup key: `chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis`  
Selection shard: `6 mod 13`  
Parent source status after this run: **OPEN**  
NM13-07 status after this run: **PARTIAL**  
Frozen metric before / after: **`N_exact = 70 -> 70`**  
Consecutive unchanged runs on P0282: **1 -> 2**  
Stuck recoveries used on P0282: **0 -> 0**  
Required eventual outside auditors: **P26 and NM13-08; neither is counted as passed**

## 1. Runtime and task-control disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this report, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still provides prompt/title, scheduling or relative-start fields, timing mode, enabled state and identifiers, but **no bindable model-family selector and no bindable reasoning-effort selector**. `GPT-6 / maximum` therefore remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing persistent model and reasoning controls together with authenticated per-run runtime attestation.

Current `RESULTS.md` records that the historical P26 `You cannot modify this task` event was authorization-context-specific and that a later P26 update succeeded from another authorized context. The lawful remedy for any future modification denial is the owning/otherwise-authorized context or an authorized platform/admin/API/support path for that same task, never duplication, permission changes or access-control bypass. I did not create, modify, disable, duplicate or probe any schedule in this invocation.

## 2. Authoritative continuity and repository read

This invocation continues the already admitted exclusive P0282 target. It is **not a new admission**, so no second claim was created.

Before new mathematics I reread or targeted-recovered current `master` state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized deployment/amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0282.md`;
- exact `P0282`, canonical-key, `P0282-A`, ownership and audit searches, including intake/dedup evidence;
- newest own report `proofnet24/NM13-07/runs/2026-09-18/2026-09-18T08-34-05Z__p0282-sqrt-defect-window.md`;
- newest visible neighboring NM13-06 report `proofnet24/NM13-06/runs/2026-09-18/2026-09-18T08-42-00Z__p0195-split-lowtemp-tail.md`;
- newest visible neighboring NM13-08 report `proofnet24/NM13-08/runs/2026-09-18/2026-09-18T08-45-00Z__p0093-binary-qso-attribution-reduction.md`.

The canonical claim still records owner `NM13-07`, SHA256 key `08312c764bd0e9331fed25b1f255810f3c3b9e0f81134520fa26aca4c9c471a4`, and shard residue 6. Current searches recover other tracks explicitly treating P0282 as owned by NM13-07, not as free inventory. A fresh exact `P0282-A` search still recovers only the claim and this track's own continuity prose, not a separate historical attempt ledger. I recovered no owner-authorized release, competing alias owner, retirement, POSTED closure, campaign settlement or P0282 audit PASS.

The newest NM13-08 report is on its own P0093 target and is not a P0282 audit. The newest NM13-06 report is on P0195. Thus the required outside P0282 audits remain **P26 NOT PASSED / NM13-08 NOT PASSED**.

Large JSONL/root surfaces can be connector-bounded when rendered wholesale. Exact canonical identity, dedup evidence, claim ownership, immutable report continuity and targeted attempt/audit searches are therefore the anchors; truncation is never treated as evidence of absence.

The pre-report `master` head observed after this run's substantive artifacts was `d75c4edf617c7ab5e0bf33cf366dd295afd7beec` (2026-09-18T09:40:53Z). Concurrent commits from other workers do not release P0282 or alter its metric.

## 3. Exact source and bounded current literature check — 2026-09-18

For a uniform permutation `sigma` of `[n]`, write

`ell_{n,k} = #{sigma in S_n : LIS(sigma)=k}`.

Chen's source conjecture asks whether, for every `n` and every interior `1<k<n`,

`ell_{n,k}^2 >= ell_{n,k-1} ell_{n,k+1}`.

The canonical source chain and current bounded literature check remain consistent with OPEN status:

1. Bóna--Lackner--Sagan, *Longest increasing subsequences and log concavity* (arXiv:1511.08653), states Chen's fixed-`n` conjecture explicitly and develops related restricted results.
2. Gao--Xie--Yang, *Schur positivity and log-concavity related to longest increasing subsequences* (arXiv:1703.06382), proves Schur-positive analogues/restricted results motivated by Chen's conjecture, not the full fixed-size statement.
3. Baslingker--Krishnapur--Madiman, *Log-concavity in one-dimensional Coulomb gases and related ensembles* (arXiv:2412.15116), proves the Poissonized Plancherel top-row result and describes it as the first positive result toward Chen's fixed-size conjecture rather than as a resolution.
4. Manuel Kauers and Chen Wang, *Recurrences for permutations with long increasing subsequences* (arXiv:2609.02220, submitted 2026-09-02), proves two exact bivariate recurrences in the long-LIS sector and D-finiteness consequences. Its stated theorem is a recurrence/D-finiteness theorem, not Chen log-concavity.
5. For method #21 below I also checked the Plancherel-fluctuation literature represented by Ivanov--Olshanski, *Kerov's central limit theorem for the Plancherel measure on Young diagrams* (arXiv:math/0304010), and related limit-shape/CLT work. This machinery controls typical Young-diagram fluctuations asymptotically, but the bounded check did not surface a ready-made finite one-sided adjacent-`j` curvature estimate for the hook product `A_j(n)` used here.

Fresh queries included the exact Chen conjecture with 2026/LIS/log-concavity terms, fixed-size versus Poissonized Plancherel log-concavity, Kauers--Wang's exact title/arXiv ID, and Plancherel concentration/cumulant terms for Young diagrams. No later primary paper explicitly resolving the full fixed-size conjecture, nor a clearly matching published `j=Theta(n^(2/3))` boundary theorem, surfaced in this bounded search. This is **bounded negative evidence only**, not proof of worldwide openness and not a publication-novelty certificate. Publication novelty of the theorem below remains **UNVERIFIED**.

## 4. Frozen metric and prior mathematical state

The admitted metric remains exactly

`N_exact = largest N for which NM13-07 has an archived exact-arithmetic certificate verifying every Chen inequality for every 1<=n<=N`.

Before this run: **70**.  
After this run: **70**.

The preceding run established a source-faithful infinite restricted theorem: with defect

`E_j(n):=ell_{n,n-j}`,

strict Chen log-concavity holds whenever

`n >= 4j^2+6j-1`,

hence uniformly for a boundary window `j=(1/2+o(1))sqrt(n)`. It also gave the exact Plancherel factorization, valid for `n>=2j`,

`E_j(n) = ((n)_j^2/j!) A_j(n)`,                                      (4.1)

where, for Plancherel `mu|-j`,

`A_j(n)=E_mu[R_mu(n,j)^2]`,                                           (4.2)

`R_mu(n,j)=prod_{c=1}^{mu_1} (n-j-c+1)/(n-j-c+1+mu'_c)`.             (4.3)

Consequently

`Q_j(n):=E_j(n)^2/(E_{j-1}(n)E_{j+1}(n))`

`= ((j+1)/j) ((n-j+1)/(n-j))^2 * A_j(n)^2/(A_{j-1}(n)A_{j+1}(n))`.  (4.4)

The preceding proof bounded the whole first-order hook loss shape-by-shape, which costs `O(j/n)` and therefore balances the explicit `1/j` log-concavity margin at `j~sqrt(n)`. The present run finds that this apparent first-order obstruction is mostly fake: the entire first-order hook mass is conserved and deterministic.

Because the frozen metric is not theorem-window size, I do **not** relabel the stronger theorem below as metric movement. This is honestly `N_exact=70 -> 70`, so the unchanged counter advances `1 -> 2`. No stuck recovery is yet required.

## 5. Idea-before-checking record

Before writing the new checker I recorded the route at

`proofnet24/NM13-07/artifacts/2026-09-18/p0282_two_thirds_defect_idea.md`

creation commit

`df6a6183b99c2ce2b5d32c7fc1b7dfeb643d9e9d`.

The note proposed exactly the conserved first-order term, a parameterized Plancherel tilt, an explicit second-order error `e_j(n)`, and the `n^(2/3)` sufficient window. The exact checker was written only after that mathematical route was fixed.

## 6. Method #12 — FIND WHAT IS CONSERVED: the first-order hook mass is exactly `j`

This is the key mechanism of the run.

Fix a partition `mu|-j`. Write

`N=n-j`, `h_c=mu'_c`, `d_c=N-c+1`, `u_c=h_c/d_c`.

Then (4.3) gives

`log R_mu(n,j) = - sum_c log(1+u_c)`.                                (6.1)

The conserved identity is simply the number of boxes of the residual Young diagram:

`sum_c h_c = sum_c mu'_c = j`.                                       (6.2)

The previous run effectively treated `sum u_c` as shape-dependent at first order. Instead split it at the fixed denominator `N`:

`sum_c u_c = j/N + A(mu)`,                                           (6.3)

where

`A(mu):=sum_c h_c (c-1)/(N(N-c+1)) >= 0`.                            (6.4)

Also put

`B(mu):=sum_c [u_c-log(1+u_c)] >= 0`.                                (6.5)

Then (6.1)--(6.5) give the exact decomposition

`log R_mu(n,j) + j/(n-j) = -A(mu)+B(mu)`.                            (6.6)

Thus the `O(j/n)` term is **not random in the shape**. Shape dependence starts one order later.

For `n>=2j`, since `c<=mu_1<=j` and `sum h_c=j`,

`A(mu) <= j(j-1)/((n-j)(n-2j+1))`.                                  (6.7)

For `x>=0`,

`0 <= x-log(1+x) <= x^2/2`.                                          (6.8)

Using `h_c^2<=j h_c` and `d_c>=n-2j+1`,

`B(mu) <= (1/2) sum_c u_c^2`

`       <= j^2/(2(n-2j+1)^2)`.                                      (6.9)

Define, with `e_0(n)=0`,

`e_j(n):=max{ j(j-1)/((n-j)(n-2j+1)),`

`             j^2/(2(n-2j+1)^2) }`.                                 (6.10)

Because `A,B>=0`, `|-A+B|<=max(A,B)`. Therefore every residual shape satisfies the uniform second-order estimate

`|log R_mu(n,j) + j/(n-j)| <= e_j(n)`.                              (6.11)

**Outcome of #12:** success. The conserved box count removes the false `O(j/n)` shape error and replaces it by `O(j^2/n^2)`. This changes the natural balance against the explicit `1/j` Chen margin from `j~sqrt(n)` to `j~n^(2/3)`.

## 7. Method #5 — ADD A PARAMETER AND DIFFERENTIATE: a tilted Plancherel partition function

Introduce, for `0<=t<=1`,

`A_j(n;t):=E_{mu~P_j}[R_mu(n,j)^(2t)]`,                              (7.1)

and

`Phi_j(t):=log A_j(n;t)`.                                            (7.2)

This is an honest one-parameter deformation from the exactly solved point `A_j(n;0)=1` to the desired correction `A_j(n;1)=A_j(n)`.

Differentiating the finite sum gives

`Phi'_j(t)=2 E_{j,t}[log R_mu(n,j)]`,                                (7.3)

where `E_{j,t}` is expectation under the exponentially tilted Plancherel law proportional to `P_j(mu)R_mu(n,j)^(2t)`.

The shape-uniform bound (6.11) survives every such tilt, so

`-2j/(n-j)-2e_j(n) <= Phi'_j(t)`

`                         <= -2j/(n-j)+2e_j(n)`.                    (7.4)

Integrating (7.4) from `t=0` to `1` yields

`log A_j(n) = -2j/(n-j) + eta_j(n)`,                                (7.5)

with

`|eta_j(n)| <= 2e_j(n)`.                                             (7.6)

The deterministic main term itself has **favorable** discrete curvature. If

`b_j(n):=-2j/(n-j)`,                                                  (7.7)

then a direct calculation gives

`2b_j-b_{j-1}-b_{j+1}`

`= 4n/((n-j)((n-j)^2-1)) > 0`                                       (7.8)

whenever the three neighboring defects are in the valid range.

Take logarithms in (4.4), substitute (7.5), and use (7.8). Since `log(1+x)>x/(1+x)` for `x>0`,

`log(1+1/j) > 1/(j+1)`.                                              (7.9)

Discarding the additional positive factor `2log(1+1/(n-j))` and the positive deterministic curvature (7.8), while bounding the residual `eta` terms by (7.6), gives the rigorous lower bound

`log Q_j(n)`

`> 1/(j+1) - [4e_j(n)+2e_{j-1}(n)+2e_{j+1}(n)]`.                    (7.10)

This is already a useful exact criterion: whenever the bracketed second-order error is below `1/(j+1)`, Chen's inequality is strict.

**Outcome of #5:** success. The parameter derivative converts the conserved first-order identity into a finite-temperature/cumulant-style control of `log A_j`, and (7.10) isolates the exact quantitative obstruction.

## 8. New theorem — an explicit `n^(2/3)` boundary window

### Theorem `NM13-07-P0282-TWO-THIRDS-04`

For every integer `j>=1` and integer `n` satisfying

`3 n^2 >= 64 (j+1)^3`,                                               (8.1)

Chen's inequality is strict at `k=n-j`:

`ell_{n,n-j}^2 > ell_{n,n-j-1} ell_{n,n-j+1}`.                       (8.2)

Equivalently, for every `n`, strict log-concavity holds throughout the explicit boundary range

`1 <= j <= floor((3 n^2/64)^(1/3)) - 1`.                             (8.3)

Thus the previously proved uniform `Theta(sqrt(n))` defect window is enlarged to a source-faithful `Theta(n^(2/3))` window, with explicit sufficient leading constant

`3^(1/3)/4 = 0.3605...`.

#### Proof

Condition (8.1) implies `n>=4(j+1)`: indeed

`n^2 >= (64/3)(j+1)^3 >= 16(j+1)^2`

for `j>=1`. Hence, for every `r in {j-1,j,j+1}`,

`n-r >= 3n/4`,                                                       (8.4)

and

`n-2r+1 >= n/2`.                                                     (8.5)

Apply these bounds to (6.10). The first entry in the maximum satisfies

`r(r-1)/((n-r)(n-2r+1)) <= 8r^2/(3n^2)`,                            (8.6)

and the second satisfies

`r^2/(2(n-2r+1)^2) <= 2r^2/n^2 <= 8r^2/(3n^2)`.                     (8.7)

Therefore

`e_r(n) <= 8r^2/(3n^2)`                                              (8.8)

for all three neighboring defects. Consequently

`4e_j+2e_{j-1}+2e_{j+1}`

`<= [32j^2 + 16((j-1)^2+(j+1)^2)]/(3n^2)`

`= (64j^2+32)/(3n^2)`.                                               (8.9)

By (8.1),

`(64j^2+32)/(3n^2)`

`<= (64j^2+32)/(64(j+1)^3)`

`< 1/(j+1)`,                                                         (8.10)

where the last inequality is exactly

`64j^2+32 < 64(j+1)^2`,

which is strict for every `j>=1`.

Substituting (8.10) into (7.10) gives `log Q_j(n)>0`, hence `Q_j(n)>1`, which is precisely (8.2). Solving (8.1) for the integer `j` gives (8.3). `square`

### Sharper asymptotic corollary

The explicit constant in (8.3) is deliberately simple rather than asymptotically optimized. The exact error (6.10) gives more.

For every fixed `c<1/2`, there exists `n_0(c)` such that for every `n>=n_0(c)` and every integer

`1 <= j <= c n^(2/3)`,                                               (8.11)

Chen's inequality is strict at `k=n-j`.

Indeed, uniformly for `r<=c n^(2/3)+1`, one has `r/n=O(n^(-1/3))`, so (6.10) gives

`e_r(n) <= (1+o(1)) r^2/n^2`.                                       (8.12)

Therefore the bracket in (7.10) is at most

`(8+o(1)) j^2/n^2`                                                   (8.13)

uniformly in the range, with the harmless `j+/-1` terms absorbed uniformly. Multiplying (8.13) by `j+1` gives at most

`8c^3+o(1) < 1`,                                                     (8.14)

because `c<1/2`. Hence (7.10) is positive for all sufficiently large `n` uniformly in (8.11).

This asymptotic corollary is still a boundary theorem, not the central/Tracy--Widom-scale source conjecture and not closure.

## 9. Method #21 — ASK WHO ELSE HAS THIS SHAPE: Plancherel cumulants are the next likely lever

The parameterized object

`Phi_j(t)=log E_{P_j} exp(2t log R_mu)`

is a cumulant-generating function of a Young-diagram observable under Plancherel measure. This has the same structural shape as the observables treated in the Vershik--Kerov/Logan--Shepp limit-shape and Kerov central-limit/cumulant literature. The fresh literature check recovered Ivanov--Olshanski's reconstruction of Kerov's CLT and related Plancherel fluctuation work.

However, importing a general CLT would not by itself prove the finite one-sided adjacent-`j` curvature required by Chen. What the proof now needs beyond the `n^(2/3)` scale is a **quantitative finite estimate on the tilted second-order statistic**, not merely convergence in distribution of the rescaled diagram. The conserved first-order term shows exactly what statistic matters: after expanding (6.6), one needs control of quantities built from

`sum_c mu'_c(c-1)` and `sum_c (mu'_c)^2`

under the `R^(2t)`-tilted Plancherel law, uniformly in neighboring `j`.

The bounded search did not surface a theorem already packaged in precisely that form. I therefore do not cite Kerov concentration as if it had proved a further Chen range. It identifies the next outside machinery to translate and test.

**Outcome of #21:** useful route identification, not a further certified theorem. The immediate `n^(2/3)` theorem above is self-contained and uses only the conserved mass plus elementary inequalities; a stronger range likely requires genuinely distributional Plancherel information rather than another worst-shape bound.

## 10. Exact self-check after the proof

After the idea note and analytic derivation, I wrote an independent exact-arithmetic self-check using only Python's standard library and `Fraction`/integer arithmetic:

- checker: `proofnet24/NM13-07/artifacts/2026-09-18/p0282_two_thirds_defect_check.py`;
- checker creation commit: `04098a3cf18ba3018c534bb31c9159c17159890a`;
- output: `proofnet24/NM13-07/artifacts/2026-09-18/p0282_two_thirds_defect_check.out`;
- output creation commit: `68accb888d69a03e1e3cbe9ccd445b0715b38cec`;
- output blob: `8801812558f814fba6119aa1986eca6447bfb623`.

For `j=1,...,20`, the checker chooses the least integer `n` satisfying `3n^2>=64(j+1)^3`, verifies the rational bounds (8.6)--(8.10), independently reconstructs `E_{j-1},E_j,E_{j+1}` exactly from residual partitions and hook lengths, checks the exact Plancherel factorization, and verifies a strictly positive integer Chen margin. It also checks the final polynomial comparison over `j=1,...,100000` as a transcription guard. The archived output ends

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not the proof of the all-`j` theorem and not either required outside audit. The theorem is carried by Sections 6--8.

## 11. Progress accounting, remaining obstruction and next route

Frozen metric: **`N_exact 70 -> 70`**, no movement.  
Source status: **OPEN**.  
Worker status: **PARTIAL**.  
Consecutive unchanged runs: **1 -> 2**.  
Stuck recoveries: **0 -> 0**.

The non-metric mathematical advance is substantial and source-faithful: the proved uniform boundary range moves from `Theta(sqrt(n))` to `Theta(n^(2/3))`, and the proof reveals why. The first-order hook correction is conserved; the remaining worst-shape uncertainty is second order.

The next genuine obstruction is now explicit. The all-shape second-order bound is of order `j^2/n^2`; against the source's explicit `1/j` factorial margin it naturally saturates at `j~n^(2/3)`. To go beyond this scale, another deterministic worst-shape inequality is unlikely to be enough. A successful route should exploit typical Plancherel shape, exact moments/cumulants of the second-order hook statistic, or a cancellation/positive-kernel identity across neighboring `j`.

Fresh methods reserved, **not yet tried on P0282**, for the next substantive run are:

- #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE — compute/identify the exact low-order Plancherel moments of the second-order hook statistic and compare with character-polynomial/shifted-symmetric-function formulas;
- #25 COUNT THE SAME THING TWICE — seek a representation-theoretic double count for `E[sum mu'_c(c-1)]`, `E[sum (mu'_c)^2]`, or their tilted analogues, rather than bounding them shape-by-shape;
- #28 REPLACE FOR ALL WITH FOR TYPICAL — prove a finite high-Plancherel-mass bound and show the exceptional shapes contribute too little to `A_j`, with explicit tails and no appeal to simulation.

If the frozen metric is still unchanged after the next run, the supported consecutive-unchanged counter will reach three; the following invocation must then obey the owner's Section-I stuck protocol rather than produce another routine boundary lemma.

## 12. Audit / closure status

P0282 remains **OPEN / PARTIAL**. No paper folder is created because the full source conjecture is not closed.

Required outside audits remain:

- P26: **NOT PASSED / no P0282 PASS recovered**;
- NM13-08: **NOT PASSED / no P0282 PASS recovered**.

The exact self-check is internal and does not count as either audit. The bounded literature search finding no matching `n^(2/3)` theorem does not establish novelty. Standard ingredients used here include Robinson--Schensted, the hook-length formula, Plancherel weights, the identity `sum mu'_c=j`, and elementary logarithmic inequalities; none is relabeled as novel by itself.

## 13. Structured `ledger_delta` for P26

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
    - id: NM13-07-P0282-TWO-THIRDS-04
      scope: strict Chen inequality at k=n-j whenever j>=1 and 3*n^2>=64*(j+1)^3; plus for every fixed c<1/2, uniformly for j<=c*n^(2/3) for all sufficiently large n
      status: SELF_CHECKED_PARTIAL
  methods_actual:
    - 5
    - 12
    - 21
  method_outcomes:
    5: SUCCESS_parameterized_tilt_and_derivative_give_log_A_interval_from_uniform_log_R_control
    12: SUCCESS_conserved_sum_of_column_lengths_removes_first_order_shape_error_and_yields_second_order_bound
    21: PARTIAL_Plancherel_limit_shape_cumulant_literature_identified_but_no_direct_finite_adjacent_j_curvature_theorem_imported
  consecutive_unchanged_runs_before: 1
  consecutive_unchanged_runs_after: 2
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
  outside_audits:
    P26: NOT_PASSED
    NM13-08: NOT_PASSED
  artifacts:
    idea_note: proofnet24/NM13-07/artifacts/2026-09-18/p0282_two_thirds_defect_idea.md
    idea_note_commit: df6a6183b99c2ce2b5d32c7fc1b7dfeb643d9e9d
    exact_self_check: proofnet24/NM13-07/artifacts/2026-09-18/p0282_two_thirds_defect_check.py
    exact_self_check_commit: 04098a3cf18ba3018c534bb31c9159c17159890a
    exact_output: proofnet24/NM13-07/artifacts/2026-09-18/p0282_two_thirds_defect_check.out
    exact_output_commit: 68accb888d69a03e1e3cbe9ccd445b0715b38cec
    exact_output_blob: 8801812558f814fba6119aa1986eca6447bfb623
    exact_output_result: ALL_EXACT_CHECKS_PASS
  literature_check_date: 2026-09-18
  literature_scope: Chen/Bona-Lackner-Sagan fixed-size conjecture; Gao-Xie-Yang related Schur positivity; Baslingker-Krishnapur-Madiman Poissonized Plancherel result; Kauers-Wang arXiv:2609.02220 recurrences; Ivanov-Olshanski Kerov Plancherel CLT and bounded current searches for fixed-size resolution/two-thirds boundary theorem
  literature_limit: bounded web/arXiv search; no worldwide-openness or publication-novelty certificate
  next_methods_reserved:
    - 17
    - 25
    - 28
  next_step: replace worst-shape second-order hook bounds by exact Plancherel moments/cumulants or finite high-mass concentration; do not silently change N_exact and do not treat asymptotic CLT as a finite one-sided curvature theorem
```

No shared root, peer namespace, canonical claim, workflow, permission, public surface, email/Drive resource, paid compute or schedule was modified. Exactly one immutable NM13-07 report is created for this invocation; its creation commit is the receipt and is to be read back directly, with no receipt-only follow-up commit.
