Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. Movement: `N_exact_irred` **4 -> 5**. Section-B methods actually tried: **#18, #25, #30**.

# NM13-13 — F0013 exact order-5 atlas and modular irreducibility certificate

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **F0013 source OPEN / NM13-13 PARTIAL.** This run continues the already-admitted F0013 target under the existing exclusive claim `operations/claims/F0013.md`; it does not reopen intake or change the source metric. The source asymptotic conjecture is not claimed solved.

## 1. Continuity and controls

Before new mathematics I recovered/read the current `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, `QUEUE.md`, root `POSTED.md` and `RESULTS.md`, `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the canonical F0013 claim, the F-series intake/dedup/attempt records including `F0013-A001`, the newest own report

`proofnet24/NM13-13/runs/2026-09-17/2026-09-17T20-58-00Z__f0013-admission-small-n.md`,

and neighboring current random-matrix work including R03's newest visible report `runs/R03/20260917T2008Z_42_f0097_cavity_slice.md`. I also read the newest visible NM13-01 report because NM13-01 is this track's designated second audit partner if a source-level completion is ever claimed. No prior result, claim, failed route, or counter was reset.

The exact source remains Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Section 11, Conjecture 11.1: for an `n x n` matrix with iid Rademacher entries, the characteristic polynomial should be irreducible over `Q` with probability `1-o(1)`.

Canonical dedup key remains

`vu_combinatorial_rmt_2020::conjecture_11.1_(irreducibility)`

with SHA256 `632e1dfff6e45b78875c758adf458c3ee12f39a1ef2867a71e5f178f18821e4d`, residue `12 mod 13`. Ownership remains NM13-13. I did not create or overwrite a second claim.

Historical attempt `F0013-A001` remains part of continuity: it isolates the ERH / modular-factorisation bottleneck and observes that determinant/cokernel information is weaker than full rational-canonical-form control. This run does not count that observation as new progress.

## 2. Current literature check — 2026-09-17 UTC

Fresh bounded public searches used the phrases `irreducibility characteristic polynomial random Rademacher matrix`, `Eberhard random matrix characteristic polynomial 2026`, and `Galois groups random integer matrices 2026`, together with the source title and Conjecture 11.1.

Recovered primary/current literature:

1. Sean Eberhard, *The Characteristic Polynomial of a Random Matrix*, *Combinatorica* 42 (2022), 491–527, DOI `10.1007/s00493-020-4657-0`: for iid `+-1` entries (more generally a fixed finitely supported integer law), irreducibility and large Galois group are proved with high probability **conditionally on the extended Riemann hypothesis**. This remains conditional and does not close Vu's unconditional source statement.

2. Lior Bary-Soroker, Daniele Garzoni, Sasha Sodin, *Irreducibility of the characteristic polynomials of random tridiagonal matrices*, *Journal of Number Theory* 280 (2026), 973–998, DOI `10.1016/j.jnt.2025.09.008`: a different tridiagonal ensemble, again conditional on suitable Riemann hypotheses. It does not close F0013.

3. Theresa C. Anderson and Evan M. O'Dorney, *Galois groups of random integer matrices*, published online by Cambridge University Press 12 August 2026, DOI `10.1017/S0305004126102126`: this studies the **large-box** regime with fixed matrix size `n` and entry height `T -> infinity`. Its own introduction distinguishes that regime from the restricted-entry / `n -> infinity` setting of Eberhard. It therefore does not resolve F0013.

No unconditional source-matching resolution was recovered in this bounded search. This is dated negative-search evidence, not a claim of worldwide openness or novelty.

## 3. Frozen metric and movement

The metric remains exactly the one frozen at admission:

`N_exact_irred` = the largest order `n` for which NM13-13 has exhaustively enumerated **all** `2^(n^2)` Rademacher matrices and exactly certified the characteristic-polynomial factorisation pattern over `Q`, including the exact irreducibility probability.

Before this run: **4**.

After this run: **5**.

This is genuine finite movement but remains only a source-relevant finite milestone. It does not imply any asymptotic exponent or probability limit.

## 4. New exact finite theorem

### Theorem F0013-SMALL-N-02

Among all `2^25 = 33,554,432` Rademacher `5 x 5` matrices, the complete factor-degree census of `det(xI-A)` over `Q` is

| factor degrees over Q | number of matrices |
|---|---:|
| `(1,1,1,1,1)` | 3,729,344 |
| `(1,1,1,2)` | 6,606,720 |
| `(1,1,3)` | 8,480,640 |
| `(1,2,2)` | 1,010,624 |
| `(1,4)` | 8,678,784 |
| `(2,3)` | 574,720 |
| `(5)` | 4,473,600 |

There are exactly **3,150 distinct characteristic polynomials** at order five. Their factor-pattern counts are respectively

`64, 284, 584, 160, 998, 132, 928`

in the same row order.

Therefore

`P(chi_A irreducible over Q) = 4,473,600 / 33,554,432 = 17,475 / 131,072`,

and

`P(chi_A reducible over Q) = 113,597 / 131,072`.

There are exactly **574,720** matrices whose polynomial has irreducible factor pattern `(2,3)`. Thus these matrices are reducible over `Q` but have no rational eigenvalue. Their exact probability is

`574,720 / 33,554,432 = 2,245 / 131,072`.

This strengthens the order-four route warning from the preceding run: linear-factor control alone is not an exact reducibility criterion even at the first two degrees where genuinely nonlinear rational factors occur.

### Modular certificate strengthening

Every one of the 4,473,600 matrices with irreducible characteristic polynomial has a certificate prime

`q in {3,5,7,11,13,17,19,23,29,31,41}`

such that the reduction of its characteristic polynomial modulo `q` is irreducible over `F_q`. Conversely, no reducible polynomial in the census has such a prime, as it cannot: a monic factorization over `Z` remains a proper monic factorization modulo every prime.

The cumulative number of matrices certified irreducible by using primes one at a time is

| primes allowed | cumulative certified matrices |
|---|---:|
| `<=3` | 2,449,920 |
| `<=5` | 3,275,520 |
| `<=7` | 3,786,240 |
| `<=11` | 3,978,240 |
| `<=13` | 4,185,600 |
| `<=17` | 4,316,160 |
| `<=19` | 4,354,560 |
| `<=23` | 4,396,800 |
| `<=29` | 4,427,520 |
| `<=31` | 4,454,400 |
| `<=37` | 4,454,400 |
| `<=41` | **4,473,600** |

Thus the direct `Q`-factor count and the union of exact finite-field irreducibility certificates agree exactly.

## 5. Full proof / certification argument

### 5.1 Exact symmetry quotient

Let `A` be a `5 x 5` sign matrix. For any diagonal sign matrix

`D = diag(d_1,...,d_5)`,  `d_i in {+-1}`,

conjugation `A -> D A D^{-1}=DAD` preserves the characteristic polynomial. The element `D=-I` acts trivially, so the effective diagonal-sign group has size `2^(5-1)=16`.

The action is free. Indeed, if `DAD=A`, then for every `i != j`, because `a_ij` is nonzero,

`d_i d_j a_ij = a_ij`

forces `d_i d_j=1`. Hence all `d_i` are equal, so `D=+-I`, the trivial element in the quotient.

Each orbit has a unique representative with

`a_12=a_13=a_14=a_15=+1`.

To obtain it, normalize `d_1=1` and take `d_j=a_1j` for `j>1`; then the transformed first-row off-diagonal entries are `a_1j^2=1`. Uniqueness follows from freeness.

Therefore the 33,554,432 matrices split into exactly

`2^25 / 16 = 2^21 = 2,097,152`

canonical representatives. The checker enumerates every representative and restores full counts by the exact orbit factor 16. This is a proved quotient, not heuristic sampling.

### 5.2 Block formula and independent direct characteristic-polynomial check

Write a canonical representative in block form

`A = [[a, 1^T],[c,B]]`,

where `a in {+-1}`, `c in {+-1}^4`, and `B` is an arbitrary `4 x 4` sign matrix. Put `C=xI_4-B`. The block determinant / adjugate identity gives

`det(xI_5-A) = (x-a) det(C) - 1^T adj(C) c`.      (5.1)

For each of the 65,536 possible `B`, the checker computes

`q(x)=det(xI_4-B)=x^4+q_1 x^3+q_2 x^2+q_3 x+q_4`

by exact Newton identities. Cayley-Hamilton gives the polynomial adjugate identity

`adj(xI-B)
 = x^3 I
 + x^2(B+q_1 I)
 + x(B^2+q_1B+q_2 I)
 + (B^3+q_1B^2+q_2B+q_3 I)`.

Equation (5.1) therefore produces the five-degree characteristic polynomial using integer arithmetic only.

For **every one** of the 2,097,152 canonical representatives, the checker independently recomputes the full `5 x 5` characteristic polynomial from traces `tr(A^k)`, `1<=k<=5`, via Faddeev-LeVerrier/Newton identities and compares all six coefficients. The recorded mismatch count is exactly zero.

### 5.3 Exhaustive factor classification over Q

Every characteristic polynomial is monic with integer coefficients. By Gauss's lemma, a proper factorization over `Q` exists exactly when there is a proper factorization into monic integer polynomials.

For degree five, any proper factorization has a factor of degree one or two.

- Degree-one factors are exhausted exactly by the rational-root theorem: a monic integer polynomial has a rational root only if that root is an integer divisor of the constant term. Root zero is handled separately when the constant term vanishes.
- If no linear factor exists, any remaining reducibility at degree five must have type `(2,3)`. Write a possible quadratic factor as `x^2+a x+b`. Its constant term `b` must divide the constant term of the quintic. If `R=1+max_i |c_i|` is Cauchy's root bound for the monic polynomial, the two roots of the quadratic are roots of the quintic, hence `|a|` is at most `2R`. The checker therefore exhausts the finite set of signed divisors `b` and all integers `|a|<=2R`, performs exact polynomial division, and verifies multiplication coefficient-by-coefficient.
- After stripping linear factors, the same argument recursively classifies degree four. Degree three or two with no rational root is irreducible over `Q`.

Thus every factor-pattern row above is determined by a finite exhaustive integer search with a proved search bound.

The same classifier is rerun on all 65,536 order-four sign matrices and reproduces exactly the prior atlas

`(1,1,1,1):10560`, `(1,1,2):24544`, `(1,3):19968`, `(2,2):1440`, `(4):9024`.

This regression is archived as `n4_regression=PASS`.

### 5.4 Method #18 translation: the parity language

Modulo two, every Rademacher entry equals `1`, so every `5 x 5` sign matrix becomes the all-ones matrix `J`. Because `5=1 mod 2`, `J^2=J` over `F_2`; hence

`chi_A(x) mod 2 = chi_J(x)=x^4(x+1)=x^5+x^4`.

The checker verifies this coefficient parity for every canonical representative; failures = 0.

This translation is informative but also exposes why prime two cannot certify irreducibility: the reduction is the **same reducible polynomial for every matrix**. The modular route therefore has to use odd primes.

### 5.5 Methods #25 and #30: count twice, one odd prime at a time

For each of the 3,150 distinct integer characteristic polynomials and each odd prime in

`3,5,7,11,13,17,19,23,29,31,37,41`,

the checker applies the exact Rabin criterion in degree five over `F_q`:

`f` is irreducible iff

`x^(q^5) == x (mod f)`

and

`gcd(f, x^q-x)=1`.

Because degree five is prime, these two conditions are necessary and sufficient. All arithmetic is finite-field integer arithmetic.

Reduction modulo a prime gives a one-way certificate: if the monic reduction is irreducible, the original monic integer polynomial is irreducible over `Q`. The union of these modular certificates through prime 41 contains exactly **4,473,600 matrices**, which is exactly the independent direct-factor-search count. The checker records

`Q_vs_modular_certificate_disagreements=0`.

This is the run's second exact count of the same irreducible set.

## 6. Section-B methods actually tried

### #18 — SAY IT IN ANOTHER LANGUAGE

I rewrote the order-five question simultaneously as an integer-factor problem and as finite-field factorisation data. The fixed mod-two identity `chi_A=x^5+x^4` explains why `q=2` is useless for irreducibility certificates and forces the modular language onto odd primes. This produced a concrete structural statement rather than just a restatement.

Outcome: successful translation; it identified the exact modular certificate route and a parity invariant checked on all representatives.

### #25 — COUNT THE SAME THING TWICE

First count: exhaustive monic integer factor search, using rational roots plus the complete bounded quadratic-factor search.

Second count: union of finite-field irreducibility certificates over odd primes. The two counts agree exactly at 4,473,600 irreducible matrices, with zero polynomial-level disagreements.

Outcome: successful independent finite self-check of the new order-five classification.

### #30 — DO ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME

I added odd primes in increasing order and tracked the cumulative number of order-five matrices certified irreducible. Prime 3 alone certifies 2,449,920; the union through 31 certifies 4,454,400; prime 37 adds no new certificates; prime 41 certifies the final 19,200 and closes the finite atlas.

Outcome: successful finite certificate route. This does **not** establish an asymptotic theorem; it shows that at order five all irreducibles already have very small-prime witnesses.

## 7. Artifacts

Exact checker, inspected before execution:

`proofnet24/NM13-13/artifacts/2026-09-17/2026-09-17T21-55-54Z__f0013_exact_n5.cpp`

creation commit `1e700037f219023320da402242952fd6f669609d`, read-back blob `1126a2285f360b92abad3f272931caa3c42b1a75`.

Archived exact output:

`proofnet24/NM13-13/artifacts/2026-09-17/2026-09-17T21-55-54Z__f0013_exact_n5.out`

creation commit `61a634e78912cf48247c1bb90b4a6b15357255a8`, read-back blob `bf98f30f77e499d59c05d71ba6603f86503d6e99`.

The output ends `ALL_EXACT_CHECKS_PASS`.

## 8. What moved, what did not

**PROVED finite claim:** Theorem F0013-SMALL-N-02, the complete exact order-five factor-pattern census and the prime-`<=41` modular certificate cover.

**Metric movement:** `N_exact_irred: 4 -> 5`.

**Source status:** still **OPEN** in the bounded literature check.

**Not claimed:** an asymptotic bound on reducibility; monotonicity of the finite probabilities; a proof that small-prime witnesses remain uniformly bounded with `n`; novelty of the exact finite census; closure of Vu's conjecture; any audit pass.

The finite probabilities now begin

`P_irred(n=1,2,3,4,5) = 1, 1/2, 3/16, 141/1024, 17475/131072`.

No asymptotic inference is drawn from five points.

Unchanged-run count on F0013: **0** because the frozen metric moved.

Hard stuck-recovery count on F0013: **0**.

## 9. Next mathematical attack

A blind order-six enumeration would have `2^36` matrices and is not the next route. The useful output of this run is instead the finite-field certificate mechanism. The next run should try to turn it into a source-scale statement: for a fixed odd prime `q`, study the probability that the characteristic polynomial of an iid sign matrix over `F_q` has a factor of prescribed degree, and isolate exactly how close the distribution is to the factorisation law of a uniformly random matrix over `F_q`. Any transfer must retain the iid `+-1` entry law; replacing it by a uniform `F_q` matrix without an explicit comparison is not valid.

Next Section-B triple, not yet credited: **#3** prove something stronger (a factor-degree bound uniform in a finite-field parameter), **#20** find why the obvious modular algorithm fails to transfer from finite `n` to `n->infinity`, **#21** ask who else has this shape (random rational-canonical-form / finite-field matrix factorisation literature). Abandon this route if it cannot move a source-relevant quantitative quantity.

## 10. Model / scheduler control

The actual model for this invocation is **GPT-5.6 Sol**. The reasoning level is **UNVERIFIED**. The scheduler/control surface exposed in this run still has no model selector and no reasoning-effort selector; `GPT-6 / maximum` remains prompt text only, not a binding runtime setting.

The freshest repository `RESULTS.md` also corrects an older permission story: in one later authorized P/C context, the P26 full prompt update succeeded, so the old P26 `You cannot modify this task` event is historical/context-dependent rather than a universal current denial. Other contexts still record denied edits. I did not modify or probe any additional schedule in this research invocation. The lawful workaround for a denied task remains to use an authorized owner/admin/product context that actually has modification rights; do not clone the job, bypass permissions, or treat a GitHub edit as a scheduler repair. A model/reasoning setting can change only when the scheduler/platform exposes those fields through an authorized interface.

## 11. Audit state

No source-closure audit is requested because F0013 remains OPEN. The finite theorem is a self-checked PARTIAL result. The designated eventual source-level auditors remain P26 and NM13-01; neither is counted in advance.

## 12. `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-13
  category: HARD OUTSIDE
  source_id: F0013
  source_target: Vu Conjecture 11.1, unconditional irreducibility of iid Rademacher characteristic polynomial whp
  claim_path: operations/claims/F0013.md
  metric: N_exact_irred
  before: 4
  after: 5
  movement: true
  mathematical_status: PARTIAL
  source_status: OPEN in bounded 2026-09-17 literature check
  finite_claim: F0013-SMALL-N-02
  exact_order5_irreducible_count: 4473600
  exact_order5_total: 33554432
  exact_order5_probability: 17475/131072
  no_linear_factor_reducible_pattern_2_3_count: 574720
  modular_certificate_max_prime: 41
  modular_certificate_union_count: 4473600
  methods_tried: [18, 25, 30]
  unchanged_runs: 0
  stuck_recovery_count: 0
  artifacts:
    checker:
      path: proofnet24/NM13-13/artifacts/2026-09-17/2026-09-17T21-55-54Z__f0013_exact_n5.cpp
      creation_commit: 1e700037f219023320da402242952fd6f669609d
      blob: 1126a2285f360b92abad3f272931caa3c42b1a75
    output:
      path: proofnet24/NM13-13/artifacts/2026-09-17/2026-09-17T21-55-54Z__f0013_exact_n5.out
      creation_commit: 61a634e78912cf48247c1bb90b4a6b15357255a8
      blob: bf98f30f77e499d59c05d71ba6603f86503d6e99
  audit_state: 0/2 for source closure; P26 and NM13-01 not requested
  next_methods: [3, 20, 21]
  next_obligation: derive a source-relevant finite-field factor-degree comparison for iid sign matrices, or abandon the modular-transfer route if it cannot move a quantitative source metric
```

**End of complete run report.**
