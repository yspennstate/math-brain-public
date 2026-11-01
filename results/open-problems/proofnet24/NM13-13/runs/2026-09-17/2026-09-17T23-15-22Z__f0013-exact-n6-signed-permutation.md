Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Movement: `N_exact_irred` 5 -> 6. Section-B methods actually tried: #3, #20, #21.**

# NM13-13 — F0013 exact order-6 atlas by signed-permutation quotient

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **F0013 source OPEN / NM13-13 PARTIAL.** This invocation continues the already-admitted exclusive F0013 target under `operations/claims/F0013.md`; it does not reopen intake, create a second claim, or change the frozen metric.

## 1. Continuity, ownership, and controls

Before new mathematics I recovered/read the current `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, `QUEUE.md`, root `POSTED.md` and `RESULTS.md`, `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the canonical F0013 claim, F-series intake/dedup/attempt material including `F0013-A001`, the newest own report

`proofnet24/NM13-13/runs/2026-09-17/2026-09-17T21-55-54Z__f0013-exact-n5-modular-certificate.md`,

and current neighboring work including R03's `runs/R03/20260917T2108Z_43_fractional_cavity_energy.md` and the designated eventual second-audit partner NM13-01's `proofnet24/NM13-01/runs/2026-09-17/2026-09-17T22-03-00Z__p0292-frozen-endpoint-barrier.md`. No prior theorem, failed route, metric, or stuck counter was reset.

The exact source remains Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Section 11, Conjecture 11.1: for an `n x n` matrix with iid Rademacher entries, `det(tI-A)` should be irreducible over `Q` with probability `1-o(1)`.

Canonical dedup key remains

`vu_combinatorial_rmt_2020::conjecture_11.1_(irreducibility)`

with SHA256 `632e1dfff6e45b78875c758adf458c3ee12f39a1ef2867a71e5f178f18821e4d`, residue `12 mod 13`. Ownership remains NM13-13. Historical attempt `F0013-A001` remains controlling continuity for the ERH/modular-factorisation bottleneck and is not relabeled as new work.

## 2. Current source/literature check — 2026-09-17 UTC

Fresh bounded public searches used the exact source title and the queries `Rademacher characteristic polynomial irreducible unconditional random matrix 2026`, `Eberhard characteristic polynomial random matrix irreducible Rademacher ERH 2026`, `Luh Meehan Nguyen random matrices finite fields characteristic polynomial irreducible factor Rademacher`, and `Galois groups of random integer matrices Anderson O'Dorney 2026`.

Recovered relevant primary/current literature:

1. Sean Eberhard, *The Characteristic Polynomial of a Random Matrix*, *Combinatorica* 42 (2022), 491–527, DOI `10.1007/s00493-020-4657-0`: for iid `+-1` entries (and more generally fixed nontrivial finitely supported integer laws), high-probability irreducibility and `Gal >= A_n` are proved **conditionally on ERH**. This remains conditional and does not close Vu's unconditional statement.

2. Lior Bary-Soroker, Daniele Garzoni, Sasha Sodin, *Irreducibility of the characteristic polynomials of random tridiagonal matrices*, *Journal of Number Theory* 280 (2026), 973–998, DOI `10.1016/j.jnt.2025.09.008`: a different tridiagonal ensemble, conditional on suitable Riemann hypotheses. It does not resolve F0013.

3. Theresa C. Anderson and Evan M. O'Dorney, *Galois groups of random integer matrices*, published online 12 August 2026, DOI `10.1017/S0305004126102126`: fixed matrix dimension with the entry-height box growing. This is not the restricted-entry `n -> infinity` regime of F0013.

4. Kyle Luh, Sean Meehan, Hoi H. Nguyen, *Some new results in random matrices over finite fields*, *J. London Math. Soc.* 103 (2021), 1209–1252, DOI `10.1112/jlms.12405`: among other results, they prove universality for the probability that the characteristic polynomial of a random finite-field matrix is divisible by a fixed irreducible polynomial, extending the uniform finite-field model. This is directly relevant to method #21 below, but it controls fixed local factor events rather than unconditional rational irreducibility of the integer characteristic polynomial.

No unconditional source-matching resolution was recovered in this bounded search. This is dated negative-search evidence only, not proof of worldwide openness or novelty.

## 3. Frozen metric and movement

The metric remains exactly the admission metric:

`N_exact_irred` = largest order `n` for which NM13-13 has an exhaustive exact certification covering **all** `2^(n^2)` Rademacher matrices, with the exact `Q`-factor-degree distribution and irreducibility probability.

Before this run: **5**.

After this run: **6**.

Coverage at `n=6` is by a proved exact symmetry quotient with exact orbit weights, not by sampling. Thus this is genuine movement of the frozen metric, not a changed normalization.

Unchanged-run count on F0013 remains **0**. Hard stuck-recovery count remains **0**.

## 4. New finite theorem: the complete exact order-6 factor census

### Theorem F0013-SMALL-N-03

Among all

`2^36 = 68,719,476,736`

Rademacher `6 x 6` matrices, there are exactly **131,641 distinct characteristic polynomials**. Their complete factor-degree census over `Q` is:

| factor degrees over Q | distinct polynomials | matrices |
|---|---:|---:|
| `(1,1,1,1,1,1)` | 57 | 1,305,864,192 |
| `(1,1,1,1,2)` | 727 | 5,265,497,600 |
| `(1,1,1,3)` | 3,146 | 9,283,180,800 |
| `(1,1,2,2)` | 1,041 | 2,567,805,440 |
| `(1,1,4)` | 13,666 | 15,419,444,736 |
| `(1,2,3)` | 3,544 | 3,132,318,720 |
| `(1,5)` | 41,004 | 18,573,396,480 |
| `(2,2,2)` | 310 | 100,307,712 |
| `(2,4)` | 4,577 | 1,343,056,896 |
| `(3,3)` | 1,155 | 421,102,080 |
| `(6)` | 62,414 | **11,307,502,080** |

Therefore

`P(chi_A irreducible over Q) = 11,307,502,080 / 68,719,476,736 = 22,084,965 / 134,217,728`.

Exactly **1,864,466,688** reducible matrices have **no rational eigenvalue**, namely factor types `(2,2,2)`, `(2,4)`, or `(3,3)`. Their exact probability is

`7,283,073 / 268,435,456`.

So the warning from orders four and five strengthens again: controlling rational eigenvalues alone misses a positive, explicitly counted part of reducibility even at order six.

The finite sequence now begins

`P_irred(n=1,...,6) = 1, 1/2, 3/16, 141/1024, 17475/131072, 22084965/134217728`.

No monotonicity or asymptotic conclusion is inferred from these six values.

## 5. Exact signed-permutation quotient

The raw `n=6` space has `2^36` matrices, so this run first proved and exploited a larger exact symmetry than the diagonal-switching quotient used at `n=5`.

Let

`G_n = ({+-1}^n / {+-I}) semidirect S_n`,

acting by signed permutation similarity. Its order is

`|G_n| = 2^(n-1) n!`,

and every element preserves the characteristic polynomial.

### 5.1 Rooted normal form

Fix a root vertex `r`. There is a unique diagonal switching modulo global sign that makes every outgoing entry `a_{r v}` for `v != r` equal to `+1`. After this switching, each nonroot vertex has a two-color invariant determined by the incoming root entry, equivalently by the original switching-invariant product

`a_{v r} a_{r v} in {+-1}`.

If `k` vertices have the negative color, order the negative color class first and the positive class second. The remaining `(n-1) x (n-1)` block `B` is then defined up to the residual group

`S_k x S_(n-1-k)`.

For `n<=6`, the checker exactly precomputes the canonical representative and stabilizer size of every possible `B` under every such residual group. A rooted key consists of the canonical `B`, `k`, and the diagonal sign `a_rr`.

The unrooted key is the minimum rooted key over all choices of `r`.

This is a complete invariant for the signed-permutation action: signed-permutation equivalence clearly preserves the multiset of rooted normal forms, while equality of rooted canonical forms explicitly reconstructs a switching plus color-preserving permutation carrying one rooted matrix to the other. Taking the minimum over roots removes the chosen root.

### 5.2 Exact orbit weights

For a canonical unrooted matrix, let `m` be the number of roots attaining its minimum rooted key and let `s` be the rooted residual stabilizer size of that key. The full signed-permutation stabilizer has size `m s`: its orbit on the possible roots has size `m`, and the stabilizer of one such root has size `s`. Hence the matrix class has exact raw multiplicity

`2^(n-1) n! / (m s)`.

No floating-point arithmetic enters this computation.

### 5.3 Canonical augmentation, rather than `2^36` raw enumeration

The checker first enumerates all `2^16` order-four matrices directly and obtains **436** signed-permutation classes.

To extend an order-`p` parent by one new vertex, there are `2p+1` new signs. The new vertex's independent diagonal switch is used to fix one outgoing old-to-new sign to `+1`, leaving exactly `2p` free extension bits. Every child orbit is covered: delete one vertex, move the remaining parent to its canonical signed-permutation representative, and use the deleted vertex's switch to impose the fixed extension sign.

Canonical augmentation gives:

- `n=4`: 436 classes, orbit-weight sum `65,536 = 2^16`;
- `n=5`: **19,216** classes, orbit-weight sum `33,554,432 = 2^25`;
- `n=6`: **3,081,888** classes, orbit-weight sum `68,719,476,736 = 2^36`.

Thus the order-six computation replaces 68.7 billion raw matrices by 3,081,888 exact classes while retaining an exact proof that the orbit weights cover the complete raw space.

## 6. Exact characteristic-polynomial and factor verification

For a rooted canonical order-six representative write

`A = [[a, 1^T], [c, B]]`,

where `B` is `5 x 5`. With `C=xI_5-B`, the exact block determinant identity is

`det(xI_6-A) = (x-a) det(C) - 1^T adj(C) c`.

The checker computes `det(xI_5-B)` by integer Newton identities from the traces of powers of `B`, expands the adjugate by Cayley-Hamilton, and thereby obtains the full sextic using integer arithmetic only.

Independently, for **every one of the 3,081,888 canonical order-six classes**, it recomputes the characteristic polynomial from `tr(A^j)`, `1<=j<=6`, via the full `6 x 6` Faddeev-LeVerrier/Newton identities. The mismatch count is exactly **zero**.

The resulting weighted table contains exactly 131,641 distinct monic integer sextics and has total weight `2^36`. A second exact script factors each distinct polynomial over `ZZ` with SymPy 1.14.0's dense integer factorization backend; for every row it multiplies all returned factors back coefficient-by-coefficient and asserts exact reconstruction of the original sextic and total degree six. The final factor-weight sum is again exactly `2^36` and the output ends `ALL_EXACT_CHECKS_PASS`.

This is a self-check, not an independent external audit.

## 7. Section-B methods actually tried

### #3 — PROVE SOMETHING STRONGER

Instead of merely deciding whether each order-six characteristic polynomial is reducible, I targeted the **complete factor-degree distribution with exact raw multiplicities**, together with the full signed-permutation class atlas. The stronger target forced an exact orbit formula and retained enough information to identify the nonlinear reducibility mass.

Outcome: **success**. It moved the frozen metric `N_exact_irred: 5 -> 6` and produced Theorem F0013-SMALL-N-03.

### #20 — FIND WHY THE ALGORITHM FAILS

The order-five run found that every irreducible quintic in its atlas had an irreducible reduction modulo some prime at most 41. There is a structural reason this certificate idea is unusually well behaved in prime degree: a transitive degree-five Galois group has order divisible by five, hence contains a 5-cycle, so irreducible Frobenius classes are group-theoretically available.

That implication fails already in degree six. A transitive degree-six group need not contain a 6-cycle; the degree-six action of `A_5`, for example, is transitive while `A_5` has no element of order six. Thus rational irreducibility of a sextic does **not** by itself force the existence of a prime at which its reduction is irreducible. The previous small-prime-union strategy therefore cannot be promoted to a general exact certificate scheme in composite degree without extra Galois-group information.

I also started a brute finite-prime scan of the order-six irreducibles, but it did not complete and is not used as evidence or archived as a result. The conceptual group-theoretic obstruction is the useful outcome.

Outcome: **successful failure diagnosis**. It prevents a false extrapolation from the order-five certificate mechanism and redirects the modular route toward factor-cycle statistics rather than “one irreducible prime per polynomial.”

### #21 — ASK WHO ELSE HAS THIS SHAPE

The finite-field literature does have the local statistic needed for a more principled route. Luh-Meehan-Nguyen prove universality for divisibility of a characteristic polynomial by a fixed irreducible polynomial for broad iid finite-field entry laws, extending the uniform-matrix results of Stong and Neumann-Praeger. Hansen-Schmutz and the finite-field cycle-index literature likewise study how random-matrix characteristic polynomials mimic random polynomial factor statistics.

This clarifies the exact remaining gap: local divisibility/factor statistics modulo one fixed prime or one fixed irreducible factor are substantially understood, but F0013 requires enough **simultaneous global information across possible rational factors and primes** to force rational irreducibility. Eberhard's conditional theorem crosses that arithmetic bridge using ERH-dependent effective prime/Frobenius control; the old F0013-A001 warning was therefore aimed at the right bottleneck.

Outcome: **useful literature transfer but no source closure**. The next source-scale route should combine finite-field factor-degree statistics with an arithmetic argument that avoids assuming a single irreducible modular reduction is available.

## 8. Artifacts and exact receipts

Substantive exact checker:

`proofnet24/NM13-13/artifacts/2026-09-17/2026-09-17T23-13-14Z__f0013_exact_n6.cpp`

creation commit `4689341abe9197724cd65a1af4fa115b7a50378b`, read-back blob `96ecf0c516d038f18c3b8d22cc578634293cba5b`.

Exact integer-factor script:

`proofnet24/NM13-13/artifacts/2026-09-17/2026-09-17T23-13-14Z__f0013_factor_n6.py`

creation commit `825928723fe07e7ddf28f250849e2f0cfbc4f762`, read-back blob `5368be7c74ec50003f1102e0dab2acec8f7a29e3`.

Archived exact output:

`proofnet24/NM13-13/artifacts/2026-09-17/2026-09-17T23-13-14Z__f0013_exact_n6.out`

creation commit `2baecb45bbd5a77c63b6cb3156dba38c07d25bd9`, read-back blob `1870a003ac5f35865742c261bd97a7a976c6daf8`.

The deterministic 131,642-line intermediate polynomial/weight table was not committed because it is reproducible from the checker; its recorded SHA256 is `58d0520fa792f4a22297d0f023143da964744db43525968cded6b0c5fbe3be41`. Source SHA256 values are also archived in the output. The final output ends `ALL_EXACT_CHECKS_PASS`.

Only authorized local compute and inspected local code were used. No workflow, external script, paid compute, email, Drive, public posting, or permission change was used.

## 9. What moved and what remains

**PROVED finite claim:** complete exact order-six factor-degree census under a proved signed-permutation quotient.

**Metric:** `N_exact_irred: 5 -> 6`.

**Source status:** **OPEN / PARTIAL** in the bounded current-status check.

**Not claimed:** any asymptotic irreducibility rate, any monotonicity of finite probabilities, a uniform bound on modular certificate primes, existence of an irreducible-mod-p witness for every irreducible sextic, novelty of the finite atlas, or closure of Vu's conjecture.

No P26 or NM13-01 audit is counted. The finite theorem is self-checked only.

## 10. Next mathematical attack

Blind canonical augmentation to `n=7` would start from 3,081,888 order-six classes and `2^12=4096` normalized extensions per class, so repeating the present algorithm unchanged is not a sensible next route.

Next Section-B triple, not yet credited: **#4, #11, #24**.

- **#4 PROVE SOMETHING WEAKER, COMPLETELY:** isolate a source-relevant theorem for one rational factor-degree regime, beginning with fixed small factor degree, using finite-field universality rather than an all-polynomial prime search.
- **#11 DUALIZE:** express “`phi` divides the characteristic polynomial mod `p`” as existence of a structured invariant subspace/module and seek a dual moment or cycle-index estimate that can be summed over factors without losing uniformity.
- **#24 FIND THE EXTREMAL OBJECT:** use the exact `n<=6` atlases to identify which factor-degree/orbit structures dominate reducibility and target the genuinely dominant obstruction rather than treating every factor pattern equally.

The frozen metric remains `N_exact_irred`; auxiliary theorems are not allowed to replace it. If these methods cannot produce source-relevant quantitative leverage, the run should say no movement rather than manufacture another checker.

## 11. Model and scheduler-control reality

Actual runtime here is **GPT-5.6 Sol**; reasoning effort is **UNVERIFIED**. The task-control schema exposed in this environment permits prompt/title/schedule/timing/enablement operations but has **no model-family field and no reasoning-effort field**. Therefore `GPT-6 / maximum` remains prompt text only; it was not a binding selector and I do not claim otherwise.

Repository `RESULTS.md` records that the historical P26 `You cannot modify this task` response was context-dependent: a later authorized P/C context succeeded in updating P26, while other task/context edits have been denied. I did not probe or modify any schedule in this research invocation. If a specific task again returns that denial, the lawful remedy is an owning account/workspace or authorized product/admin interface with modification rights; do not clone the job, bypass permissions, or pretend a GitHub edit changes native scheduler ownership. Changing model/reasoning requires the platform to expose those fields in an authorized task-control surface.

## 12. Audit state

F0013 remains OPEN, so no source-closure audit is requested or presumed. Designated eventual source-level auditors remain P26 and NM13-01; neither is counted in advance.

## 13. `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-13
  allocation: HARD_OUTSIDE
  source_id: F0013
  canonical_dedup_key: vu_combinatorial_rmt_2020::conjecture_11.1_(irreducibility)
  claim_path: operations/claims/F0013.md
  source_status: OPEN
  track_status: PARTIAL
  metric: N_exact_irred
  before: 5
  after: 6
  movement: true
  theorem_id: F0013-SMALL-N-03
  exact_n6_classes: 3081888
  exact_n6_raw_weight: 68719476736
  distinct_characteristic_polynomials_n6: 131641
  irreducible_matrices_n6: 11307502080
  irreducible_probability_n6: 22084965/134217728
  reducible_without_linear_factor_n6: 1864466688
  methods_tried: [3, 20, 21]
  method_outcomes:
    3: complete exact n=6 factor census; metric moved
    20: composite-degree obstruction found for naive irreducible-mod-p certificate route
    21: finite-field divisibility universality recovered; arithmetic simultaneity remains bottleneck
  unchanged_run_count: 0
  hard_stuck_recovery_count: 0
  audit_p26: NOT_REQUESTED
  audit_nm13_01: NOT_REQUESTED
  next_methods: [4, 11, 24]
  next_step: finite-field factor-degree/invariant-subspace route; do not blind-enumerate n=7
  artifact_checker: proofnet24/NM13-13/artifacts/2026-09-17/2026-09-17T23-13-14Z__f0013_exact_n6.cpp
  artifact_factor: proofnet24/NM13-13/artifacts/2026-09-17/2026-09-17T23-13-14Z__f0013_factor_n6.py
  artifact_output: proofnet24/NM13-13/artifacts/2026-09-17/2026-09-17T23-13-14Z__f0013_exact_n6.out
  bounded_literature_check_utc: 2026-09-17
  runtime_model: GPT-5.6 Sol
  runtime_reasoning: UNVERIFIED
```

END NM13-13 RUN REPORT
