Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-METRIC MOVEMENT: `N_exact = 99 -> 100`; Section-B methods actually tried: #23 DO WHAT THE PROPOSER DID NOT EXPECT, #26 HUNT THE SPORADIC CASE, and #3 PROVE SOMETHING STRONGER, all explicitly RECYCLED because all 30 numbered methods had already genuinely been used on P0282.**

# NM13-07 — Taylor-curvature obstruction/block theorem, 19/20 boundary window, exact row 100

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-07` / `proofnet24/NM13-07/`  
Category: **CLOSABLE OUTSIDE**  
Source / canonical claim: `aim_kpz_followup_2025` / `P0282`  
Canonical dedup key: `chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis`  
SHA-256: `08312c764bd0e9331fed25b1f255810f3c3b9e0f81134520fa26aca4c9c471a4`  
Shard: `6 mod 13`  
Source status after this run: **OPEN**  
Worker status after this run: **PARTIAL**  
Required outside audits: **P26 NOT PASSED / NM13-08 NOT PASSED**

## 1. Executive result

This invocation continued the already admitted exclusive P0282 assignment. Admission was not reopened and no duplicate claim was created.

Two mathematically distinct things moved.

1. The source-faithful growing-defect theorem improves from exponent `10/11` to **`19/20`**. The route first refutes the tempting stronger assertion that every Taylor coefficient has favorable Chen curvature for every defect: the first adverse coefficient occurs at order `11`, defect `j=1`, with curvature exactly `-1410`. The bad point is entirely inside the retained all-`n` fixed-defect theorem. In the genuinely active sector `j>=67`, exact arithmetic proves favorable curvature simultaneously for every Taylor order `10,...,18`. Truncating after order 18 and bounding the whole remaining analytic tail yields the new theorem

   `n^19 >= 2^56 (j+1)^20  =>  ell_{n,n-j}^2 > ell_{n,n-j-1} ell_{n,n-j+1}`

   for `j>=67`. In particular,

   `j+1 <= n^(19/20)/8`

   is a simple sufficient growing-defect window after chaining the retained all-`n` theorem for `j<=66`.

2. The frozen finite metric moved independently. An exact Gessel/Toeplitz/CRT certificate verifies the previously uncovered row-100 cells `k=2,...,33`; the retained all-`n` theorem for defects `j<=66` covers `k>=34`. Hence every interior source inequality in row 100 is certified and

   **`N_exact: 99 -> 100`.**

`unchanged_runs: 0 -> 0`.  
`stuck_recoveries: 0 -> 0`.

This is not closure: the central regime `j=Theta(n)` remains uncontrolled and neither required outside audit has passed.

## 2. Required continuity, ownership, and access disclosure

Before research I reread or exact-target-recovered the controlling state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- predecessor NM13-07 report `proofnet24/NM13-07/runs/2026-09-19/2026-09-19T12-30-35Z__p0282-ten-elevenths-row99.md`, creation commit `d24c2cf4f57c0a1eae18a33704dbc2725f8878b9`;
- current canonical claim `operations/claims/P0282.md`;
- newest neighboring NM13-06 report and newest designated-secondary-auditor NM13-08 report;
- repository-wide canonical-key / source-id searches for P0282; and
- bounded fresh public-literature checks described in section 9.

The append-only intake/source/attempt JSONL corpora are too large for an honest claim that every unchanged historical byte was freshly rendered model-visible in this connector invocation. I make no such claim. Exact Git comparisons from the predecessor report creation commit through frozen pre-write head `563c1780049cd84a49894b59eb3cee6e1286cec5` cover the complete intervening changed-file sets (`too_large=null`) and show no mutation of `operations/claims/`, root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md` / `RANKING.md`, screened `probability_1000_intake_*/problems.jsonl`, or probability attempt ledgers. Candidate-specific claim and neighboring continuity were freshly reopened.

Current `operations/claims/P0282.md` still names NM13-07 as owner, with the exact canonical key above and residue 6. The newest NM13-08 report still treats P0282 as NM13-07's active off-shard source and records no audit PASS. No release, conflicting owner, settlement, or source-resolution event was recovered.

## 3. Exact source and frozen quantity

For a uniform permutation `sigma` of `[n]`, let

`ell_{n,k} = #{sigma in S_n : LIS(sigma)=k}`.

Chen's source conjecture is

`ell_{n,k}^2 >= ell_{n,k-1} ell_{n,k+1}`

for every positive integer `n` and every `1<k<n`.

The frozen metric remains exactly the admission metric:

`N_exact = largest N for which this worker has archived exact-arithmetic certificates for every source inequality in every row 1<=n<=N`.

Entering value: `99`.  
Leaving value: `100`.

The retained theorem from earlier runs proves the source inequality for every `n` whenever the defect `j=n-k` satisfies `j<=66`. The retained stronger binomial-normalized ULC/shadow-density frontier remains `j<=32`. Neither frontier is substituted for the frozen metric.

## 4. Methods actually tried — research first

Idea-before-production-validation note:

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_curvature_block_row100_idea.md`

creation commit `8cfca3011ebb16daf6675f315d88d1020936e12e`.

All three methods are explicitly **RECYCLED** because all 30 Section-B methods had already been genuinely used on this source. The triple differs from the preceding run's `#1/#20/#8`.

### #23 DO WHAT THE PROPOSER DID NOT EXPECT — attack coefficientwise positivity itself

The predecessor suggested proving favorable Chen curvature for every Taylor coefficient of the Plancherel correction. I assumed the opposite and searched exact coefficients for the first failure.

Result: the stronger all-defect coefficientwise-positive pattern is **false**. If

`G_j(t)=log A_j(t)=sum_{m>=1} D_m(j)t^m`

and

`C_m(j)=2D_m(j)-D_m(j-1)-D_m(j+1)`, 

then exact arithmetic gives

`C_11(1) = -1410`.

Orders `m=2,...,10` are positive for every integer `j>=1`, so this is the first adverse Taylor order/defect in the exact search. This is an obstruction to a naive whole-series proof, not a refutation of Chen.

### #26 HUNT THE SPORADIC CASE — localize the adverse coefficient

The adverse point is tiny-defect. Exact interpolation shows `C_11(j)` is coefficientwise positive after writing `j=2+x`, so order 11 is already favorable for every `j>=2`.

More importantly for the actually open sector, exact arithmetic shows that for every order

`m=10,11,...,18`,

`C_m(67+x)` has strictly positive coefficients as a polynomial in `x`. Therefore

`C_m(j)>0` for every integer `j>=67` and every `10<=m<=18`.

The smallest shifted coefficient at each new order is respectively

`180,220,264,312,364,420,480,544,612`.

Thus the sporadic low-defect obstruction is wholly absorbed by the already retained all-`n` theorem `j<=66`.

### #3 PROVE SOMETHING STRONGER — certify a block, not one next coefficient

Rather than derive only `D_10`, the finite-degree lemma from the predecessor is used to certify the whole block `m=10,...,18` simultaneously. This turns one additional Taylor step into a nine-order structural advance and permits a single analytic-tail estimate after order 18.

Outcome: **successful**, yielding the `19/20` window theorem in section 6.

## 5. Exact finite core for the Taylor-curvature block

Production checker:

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_curvature_block_selfcheck.py`

Archived output:

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_curvature_block_selfcheck.out`

Local executed SHA-256 before archival:

- script: `2dac39bef2de0e4dafe58834abe9275865e0c92a12d812cc0c68a6a363cf5bde`;
- output: `16bd08ca06bde1729e93a0146330c8b92082d9b94aaebf3e1676ed642f50ed48`.

The checker is exact rational arithmetic. It enumerates partitions and hook dimensions for `j=0,...,20`, computes `G_j(t)` through order 18 directly from the hook product, and for every order `m` reconstructs `D_m(j)` from exact values.

The key retained lemma from the predecessor is that `D_m(j)` is a polynomial in `j` of degree at most `m`. Its proof groups the Jucys--Murphy/content expansion by equality/support patterns of identity transposition words: an identity word of total transposition length `L` has no vertex occurring only once, so a fixed support pattern uses at most `L` vertices and contributes a falling-factorial polynomial of bounded degree; the logarithm recurrence preserves the degree bound.

Therefore `m+1` exact values determine `D_m` globally. The new checker also verifies each reconstructed polynomial at two additional exact values `j=m+1,m+2`, so the finite recovery is overdetermined.

The checker then verifies:

- `C_m(1+x)` coefficientwise positive for every `2<=m<=10`;
- `C_11(1)=-1410` exactly;
- `C_11(2+x)` coefficientwise positive;
- `C_m(67+x)` coefficientwise positive for every `10<=m<=18`;
- the analytic-tail numerical constant `32*6^19 < 2^55`;
- the simple-window constant comparison.

The archived output terminates `ALL_EXACT_CHECKS_PASS`.

This is explicitly a **self-check**, not an independent P26 or NM13-08 audit.

## 6. Theorem: a rigorous 19/20 growing-defect window

### Statement

Let `j=n-k` and `F_j(n)=ell_{n,n-j}`. For every integer `j>=67`,

**if**

`n^19 >= 2^56 (j+1)^20`,

**then**

`F_j(n)^2 > F_{j-1}(n) F_{j+1}(n)`.

Consequently, after chaining the retained all-`n` theorem for `j<=66`, Chen's source inequality holds throughout the simple sufficient region

`j+1 <= n^(19/20)/8`.

Claim label for this report: `NM13-07-P0282-NINETEEN-TWENTIETHS-WINDOW-10`.

### Proof

The retained exact hook factorization is

`F_j(n) = (n)_j^2/j! * A_j(n)`.

Hence the exact source ratio is

`Q_j(n) := F_j(n)^2/(F_{j-1}(n)F_{j+1}(n))`

`= ((j+1)/j) * ((n-j+1)/(n-j))^2 * A_j(n)^2/(A_{j-1}(n)A_{j+1}(n))`.

Put `t=1/n` and

`G_r(t)=log A_r(t)=sum_{m>=1}D_m(r)t^m`.

The retained analytic-disk lemma gives

`|G_r(t)|<2` for `|t|<=1/(6r)`,

hence Cauchy's estimate gives

`|D_m(r)| <= 2(6r)^m`.

Also `D_1(r)=-2r`, whose discrete Chen curvature is zero. Earlier exact reports established positive curvature `C_m(j)>0` for `m=2,...,9`; section 5 establishes it for `m=10,...,18` whenever `j>=67`. Therefore the Taylor polynomial through order 18 contributes nonnegatively to

`2G_j(t)-G_{j-1}(t)-G_{j+1}(t)`.

It remains to bound the tail. The stated hypothesis implies `n>=8(j+1)`: after dividing by `(j+1)^19`,

`(n/(j+1))^19 >= 2^56(j+1) >= 2^57 = 8^19`.

Thus, for each `r in {j-1,j,j+1}`,

`q_r:=6r/n <= 6(j+1)/n <= 3/4`.

Let

`R_r = sum_{m>=19} D_m(r)n^{-m}`.

Then

`|R_r| <= 2 sum_{m>=19} q_r^m`

`<= 2 q_r^19/(1-q_r)`

`<= 8 (6(j+1)/n)^19`.

Therefore the tail in the discrete curvature satisfies

`|2R_j-R_{j-1}-R_{j+1}|`

`<= 32*6^19 * (j+1)^19/n^19`

`< 2^55 * (j+1)^19/n^19`

`<= 1/(2(j+1))`.

Taking logarithms of the exact ratio and discarding the positive factor `2 log((n-j+1)/(n-j))`,

`log Q_j(n)`

`>= log((j+1)/j) - 1/(2(j+1))`.

Using `log(1+1/j) >= 1/(j+1)`,

`log Q_j(n) > 1/(2(j+1)) > 0`.

Hence `Q_j(n)>1`, proving strict Chen log-concavity in this sector.

Finally, if

`j+1 <= n^(19/20)/8`,

then raising to the twentieth power gives

`n^19 >= 8^20 (j+1)^20 = 2^60 (j+1)^20`,

which is stronger than the theorem hypothesis. This proves the simple `19/20` window. QED.

### What this does and does not establish

The rigorous growing-defect exponent therefore moves

`10/11 -> 19/20`.

This is a restricted theorem. It does not reach defects proportional to `n`; the literal all-`n` source remains OPEN.

The negative `C_11(1)` is also useful: a proof that every coefficient curvature is globally nonnegative is impossible in that form. Any whole-series argument must either exploit compensation between orders or restrict to the active large-defect sector before summing.

## 7. Frozen metric: exact row 100

The finite metric was moved independently from the asymptotic theorem.

For `n=100`, the retained all-`n` fixed-defect theorem `j<=66` covers every `k>=34`. Therefore the only new source cells required for a complete row-100 certificate are

`k=2,...,33`,

32 inequalities, with `ell_{100,34}` reconstructed as the right neighbor.

Production checker:

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_row100_gessel_low.cpp`

Archived output:

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_row100_gessel_low.out`

Local executed SHA-256 before archival:

- source: `987b2007e2c3450854f591591dbe31b31c34a5c8c6cde16d19a20c343a0bf014`;
- output: `7bb137a7a8537ef5dac3eb9581040ff663347bcd2ddbe7949cc48e1ab1eff52f`.

The checker uses Gessel's Bessel/Toeplitz determinant modulo 18 independently primality-checked moduli, followed by CRT. The final modulus has **539 bits**, while `100!` has **525 bits**, so the modulus exceeds `2*100!` and the combinatorial reconstruction is unique. The exact Catalan identity for the `LIS<=2` cumulative count passes.

All 32 new source inequalities are strictly positive. The weakest newly computed low-seam ratio occurs at `k=33`:

`ell_{100,33}^2/(ell_{100,32} ell_{100,34}) ~= 1.09143755021483645 > 1`.

The exact numerator, denominator, and positive margin are archived in the output. It terminates `ALL_EXACT_CHECKS_PASS`.

Chaining the low seam with the retained `j<=66` theorem covers every source inequality `2<=k<=99` in row 100. Therefore

**`N_exact: 99 -> 100`.**

## 8. Artifacts and commits in this invocation

Idea-before-validation note:

- `proofnet24/NM13-07/artifacts/2026-09-19/p0282_curvature_block_row100_idea.md`
- creation commit `8cfca3011ebb16daf6675f315d88d1020936e12e`.

Exact Taylor-curvature block self-check:

- script creation commit `eb2e04aea9511929f283b0f71684a778d5412e5b`;
- output creation commit `db06667f83fba28a6d2d9b972b9b7e1ce780ed62`.

Exact row-100 certificate:

- checker creation commit `a6d8d2eb61d18160790a29bbddbc030c58aae154`;
- output creation commit `ecc903c8b377c6376e3d047ad996ef57e26a000f`.

No shared root, canonical claim, peer namespace, workflow, permission, public surface, email/Gmail resource, Drive resource, paid compute, or scheduler was modified.

## 9. Literature / prior-art refresh — 2026-09-19

Fresh bounded searches included:

- `"Chen" longest increasing subsequence log-concavity conjecture fixed size 2026`;
- `"Poissonized Plancherel" log-concavity Chen conjecture`;
- `"Increasing Subsequences, Matrix Loci, and Viennot Shadows" Chen conjecture`;
- `"Kauers" Wang permutations long increasing subsequences 2026`;
- `"Chen's conjecture" log-concavity longest increasing subsequence`.

Scope checked: the original fixed-size conjecture, later representation-theoretic / Schur-positive approaches, Rhoades's Viennot-shadow model, the Poissonized Plancherel result, and the newest directly relevant September-2026 long-LIS recurrence paper.

Current bounded evidence:

- Chen 2008 (`arXiv:0806.3392`) is the original source.
- Bóna--Lackner--Sagan explicitly restate the fixed-size conjecture and prove related restricted analogues.
- Gao--Xie--Yang prove Schur-positive restricted analogues, not the full source statement.
- Novak--Rhoades formulate a stronger Kronecker-coefficient conjecture implying Chen.
- Rhoades, *Forum of Mathematics, Sigma* 12 (2024), e97, realizes the LIS distribution as a Hilbert series / Viennot-shadow quotient and still states Chen's conjecture; its stronger equivariant injection Conjecture 4.4 is reported computationally checked only through `n<=15`.
- Baslingker--Krishnapur--Madiman (`arXiv:2412.15116`) prove the **Poissonized** Plancherel top-row result and explicitly describe it as the first known positive result toward Chen, not the fixed-size resolution.
- Kauers--Wang, `arXiv:2609.02220`, submitted **2026-09-02**, prove recurrences and D-finiteness for permutations with long increasing subsequences; the abstract does not claim fixed-size log-concavity.

No source-matching all-`n` fixed-size resolution and no matching `19/20` boundary theorem surfaced in these bounded searches. This is **negative evidence only**, not proof of worldwide openness or novelty. Novelty and priority remain **UNVERIFIED**.

The RSK, hook-length, Gessel determinant, Jucys--Murphy/content, regular-representation trace, and Cauchy-estimate mechanisms used here are classical machinery and are not claimed as novel.

## 10. Structured ledger delta for P26

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
  metric_name: N_exact
  metric_before: 99
  metric_after: 100
  metric_movement: true
  retained_all_n_chen_defect_frontier: 66
  retained_all_n_ulc_shadow_density_frontier: 32
  growing_defect_exponent_before: 10/11
  growing_defect_exponent_after: 19/20
  new_claims:
    - NM13-07-P0282-TAYLOR-CURVATURE-OBSTRUCTION-01
    - NM13-07-P0282-NINETEEN-TWENTIETHS-WINDOW-10
  methods_actual:
    - "#23 DO WHAT THE PROPOSER DID NOT EXPECT — counterexample search against all-order/all-defect Taylor-curvature positivity; first failure C_11(1)=-1410"
    - "#26 HUNT THE SPORADIC CASE — localize the failure to retained low defect and certify active-sector positivity"
    - "#3 PROVE SOMETHING STRONGER — certify the entire order-10..18 curvature block and sum the remaining analytic tail"
  methods_recycled: true
  exact_finite_checks:
    taylor_block_selfcheck: PASS
    taylor_orders_newly_certified_active_sector: 10..18
    first_adverse_global_coefficient: "m=11,j=1,C=-1410"
    row100_source_cells: "32/32 strict"
    row100_crt_modulus_bits: 539
    row100_factorial_bits: 525
  audits:
    P26: NOT_PASSED
    NM13-08: NOT_PASSED
  unchanged_runs_before: 0
  unchanged_runs_after: 0
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
  closure: false
```

## 11. Next step

The order-11 low-defect failure rules out the cleanest all-coefficient global positivity conjecture, but the active sector shows a much stronger block phenomenon than one-order-at-a-time lifting suggested.

The next primary route is therefore **not** a routine row census and not automatically `D_19`. The useful question is whether support-pattern combinatorics proves an eventual-in-`j` sign theorem uniform in Taylor order, for example a bound of the form

`C_m(j)>=0 whenever j >= c m` or j >= c m^alpha`.

Such a theorem, combined with the analytic disk, could push the exponent arbitrarily close to 1 with one argument and clarify exactly why the low-defect adverse coefficients do not matter. A second route is to seek cancellation of the negative low-defect Taylor pieces against neighboring positive orders in the full series, rather than demanding coefficientwise positivity.

A finite next-order computation is fallback only if those structural routes fail.

## 12. Model / scheduler-control truth

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 maximum, a binding reasoning setting, an hour-long execution, or a support escalation.

The exposed scheduled-task control schema offers title/prompt, schedule or relative-start fields, timing mode, enabled state, listing, and updates. It exposes **no bindable model-family selector and no bindable reasoning-effort selector**. GPT-6/maximum therefore remains prompt text only.

Making the request binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists explicit model-family and reasoning-effort routing fields and returns authenticated applied-runtime telemetry.

The historical P26 `You cannot modify this task` response is an authorization-context boundary, not permission to duplicate or bypass the task. Repository continuity records later successful P26 updates from another authorized context. The compliant workaround is the owning/authorized account/workspace/API/admin context, an authorized ownership transfer where supported, or platform permission/support repair for the same existing task.

No schedule or permission was modified in this invocation.
