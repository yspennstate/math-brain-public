Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `N_exact_irred` stayed `6 -> 6`. Section-B methods actually tried: #9 RANDOMIZE, #10 DERANDOMIZE, #13 FIND WHAT ONLY INCREASES. This is the third stuck episode after the two permitted HARD recoveries, so F0013 is handed off and NM13-13 rotates to `ADMISSION_PENDING`.**

# NM13-13 — F0013 aggregate divisor-degree reduction and mandatory hard-source handoff

Date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-13`  
Category: `HARD OUTSIDE`  
Canonical source / historical claim: `F0013` / `operations/claims/F0013.md`  
Canonical dedup key: `vu_combinatorial_rmt_2020::conjecture_11.1_(irreducibility)`  
Canonical SHA-256 / shard: `632e1dfff6e45b78875c758adf458c3ee12f39a1ef2867a71e5f178f18821e4d`, residue `12 mod 13`  
Source status after this run: **OPEN in the bounded current-status check below**  
Local disposition after this run: **PARTIAL / mandatory handoff; NM13-13 must not execute another F0013 research invocation without explicit fresh reassignment**

## 1. Runtime, controls, continuity, ownership, and required reads

The prompt requests `GPT-6 / maximum`. That is not an authenticated runtime setting exposed here. The actual model available to this invocation is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**. The exposed task-control surface provides ordinary scheduling fields such as title/prompt, schedule or relative start, timing mode, and enabled state; it provides no binding model-family selector and no reasoning-effort selector. Making `GPT-6 / maximum` binding would require an owner-authorized product/workspace/API/admin surface exposing those settings plus authenticated per-run runtime attestation.

Repository policy records a historical P26 scheduler-context response `You cannot modify this task` and later successful modification from another authorized context. The legitimate workaround is the owning/otherwise-authorized scheduler surface or platform/admin support, not cloning an inaccessible task or bypassing access controls. This invocation did not create, edit, disable, or duplicate any schedule.

Before the mathematics I reread or targeted-search-recovered the owner-required state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- `operations/claims/F0013.md`;
- the F-series intake, canonical identities and attempt history, including `F0013-A001`;
- all prior NM13-13 reports, newest first, especially `2026-09-18T04-56-00Z__f0013-stuck-recovery-2.md`;
- newest neighboring NM13-12 handoff report and newest designated eventual audit-partner NM13-01 report;
- current searches for F0013 aliases, claims, handoffs, attempts, audit records, POSTED/settled state and later source corrections.

The current F0013 claim still names NM13-13 as the historical exclusive owner. No competing F0013 owner, explicit source release, POSTED closure, retirement, P26 source audit pass, or NM13-01 source audit pass was recovered. A disabled or inaccessible task was not treated as release. Connector/search access is bounded, so this is authoritative source-specific continuity recovery, not a claim of byte-for-byte visibility over every historical repository object.

The method history is preserved rather than restarted. Before this invocation the actually used triples were:

1. `#2/#14/#16` — admission and exact small cases;
2. `#18/#25/#30` — exact order 5;
3. `#3/#20/#21` — exact order 6;
4. `#4/#11/#24` — even-order Krylov/Eisenstein family;
5. `#5/#15/#29` — odd compression/Hensel route;
6. `#6/#17/#26` — odd polynomial-density/shifted-invertibility route;
7. stuck recovery 1: `#1/#22/#28`;
8. post-recovery multi-prime row exposure: `#7/#19/#27`;
9. stuck recovery 2: `#8/#12/#23`, which proved the one-row growing-degree pointwise-uniformity surrogate impossible by an exact entropy/support barrier.

That second recovery explicitly reserved the only three still-untried methods `#9/#10/#13`. Those are the three methods genuinely attempted below. No earlier method is re-credited.

## 2. Exact source and fresh bounded literature/status check — 2026-09-18 UTC

The source remains Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Section 11, Conjecture 11.1:

> for an `n x n` matrix `A_n` with iid Rademacher entries, the characteristic polynomial `det(tI-A_n)` is irreducible over `Q` with probability `1-o(1)`.

Fresh dated searches used the exact source/conjecture wording together with `Rademacher characteristic polynomial irreducible`, `random matrix Galois group`, `2026`, and the names of the closest authors. The current comparison points remain:

1. **Sean Eberhard, *The Characteristic Polynomial of a Random Matrix*, Combinatorica 42 (2022), 491–527, DOI `10.1007/s00493-020-4657-0`.** The abstract states that for iid `+-1` entries (and more generally fixed nontrivial finitely supported integer laws), high-probability irreducibility and `Gal >= A_n` are proved **conditionally on ERH**. This does not give the unconditional source statement.
2. **Lior Bary-Soroker, Daniele Garzoni, Sasha Sodin, *Irreducibility of the characteristic polynomials of random tridiagonal matrices*, J. Number Theory 280 (2026), 973–998, DOI `10.1016/j.jnt.2025.09.008`.** This treats a different tridiagonal ensemble and is conditional on Riemann hypotheses for suitable Dedekind zeta functions.
3. **Theresa C. Anderson and Evan M. O'Dorney, *Galois groups of random integer matrices*, Mathematical Proceedings of the Cambridge Philosophical Society, published online 12 August 2026, DOI `10.1017/S0305004126102126`.** This is a large-box regime with fixed matrix dimension and entry height tending to infinity, not fixed Rademacher entries with `n -> infinity`.
4. The previously recovered finite-field comparison remains Hansen–Schmutz and the later Luh–Meehan–Nguyen one-prime universality/normal-vector results. Those provide local factor information, not the source-matching common-sign multi-prime law required here.

No unconditional source-matching resolution of Vu Conjecture 11.1 was recovered in this bounded search. This is **bounded negative evidence only**, not proof of worldwide openness or publication novelty.

## 3. Frozen metric and exact handoff trigger

The frozen claim-file metric remains

`N_exact_irred` = the largest order `n` for which NM13-13 has exhaustively certified **all** `2^(n^2)` Rademacher matrices, including exact rational factor-degree distribution and irreducibility probability.

Before this run: **6**.  
After this run: **6**.  
Movement: **none**.

The exact order-six signed-permutation atlas remains the last complete finite census. Its executed certificate records 3,081,888 signed-permutation classes, total weight `68,719,476,736 = 2^36`, exact factor-degree census, and irreducible probability `22084965/134217728`, ending `ALL_EXACT_CHECKS_PASS`.

The preceding recovery was the sixth consecutive unchanged-metric invocation and consumed the second permitted hard-source recovery. This invocation is therefore the **third stuck episode**:

`unchanged_runs_since_metric_movement: 6 -> 7`,  
`stuck_recoveries_used: 2 -> 2`.

There is no recovery number 3. Under the controlling HARD rule, this run must preserve a handoff and rotate away from F0013 even though the route theorem below is useful PARTIAL progress. Neither P26 nor NM13-01 is counted as an audit.

---

# 4. Method #9 — RANDOMIZE: random factor identities reveal an exact first-moment trap

The second recovery said to aggregate factor identities before uniformizing. Start with the most literal randomized version.

For a monic polynomial `F in F_q[t]` of degree `n`, let

`D_d(F) = #{ monic H in F_q[t] : deg H = d and H | F }`.

Let `F` be uniform over the `q^n` monic degree-`n` polynomials, and independently choose a uniform monic degree-`d` polynomial `H`, where `0 <= d <= n`.

### Lemma 4.1 — exact randomized divisor identity

For every fixed monic `H` of degree `d`,

`P(H | F) = q^{-d}`,

and consequently

`E D_d(F) = 1`.

### Proof

A monic degree-`n` polynomial is divisible by fixed monic `H` iff it is `H Q` for a monic degree-`n-d` polynomial `Q`. There are exactly `q^(n-d)` such `Q` among `q^n` monic degree-`n` polynomials. Thus `P(H|F)=q^{-d}`. Summing this probability over the `q^d` monic degree-`d` choices of `H` gives `E D_d(F)=1`. `QED`

For independent uniform-polynomial models `F_j in F_{p_j}[t]` at distinct primes,

`E prod_j D_d(F_j) = prod_j E D_d(F_j) = 1`.                 (4.1)

**Outcome of #9.** Randomizing a specific modular factor tuple and averaging its compatibility does remove the impossible pointwise-uniformity demand, but the obvious first moment is exactly critical: it is **one**, even in the ideal independent-uniform finite-field model. Therefore a union/first-moment argument over factor identities cannot yield the `o(1)` rational-reducibility bound. This is an exact route obstruction, not a heuristic failure.

---

# 5. Method #10 — DERANDOMIZE: tuple averaging is exactly the wrong deterministic count

For the actual integer matrix `A`, prime `p`, and degree `d`, define

`D_{p,d}(A) = D_d( chi_A mod p )`.

Then

`prod_{p in P} D_{p,d}(A)`

is **exactly** the number of tuples `(H_p)_{p in P}` of monic degree-`d` polynomials such that

`H_p | chi_A mod p`

for every `p in P`. This follows simply by expanding the product of the divisor-indicator sums. Hence the random-factor-tuple experiment derandomizes with no loss to the deterministic tuple count.

But (4.1) shows why this deterministic statistic is the wrong one: in the ideal model of independent uniform monic characteristic polynomials, its expectation is still exactly one for every degree `d`. Summing over `d <= n/2` is then of order `n`, not `o(1)`.

So the failed route is now sharply identified:

> **factor identities carry a built-in multiplicity that exactly cancels their individual rarity.**

The right quotient must forget identities and retain only whether a degree is reachable at all.

**Outcome of #10.** The naive randomized factor-tuple route is completely derandomized and refuted at first moment even in the ideal comparison model. Any successful four-prime argument must work with factor-degree partitions / reachable degrees, or use genuinely higher-order information, rather than the raw number of divisor identities.

---

# 6. Method #13 — FIND WHAT ONLY INCREASES: the divisor-degree reachability support

For a monic polynomial `f` over any field define the **divisor-degree support**

`S(f) = { d >= 0 : f has a monic divisor of degree d }`.

Equivalently, if

`f = prod_i g_i^{m_i}`

is the irreducible factorization with `r_i = deg g_i`, then

`S(f) = { sum_i a_i r_i : 0 <= a_i <= m_i }`.               (6.1)

Thus `S(f)` depends only on the factor-degree partition with multiplicities, not on factor identities. It is the support of

`prod_i (1 + z^{r_i} + ... + z^{m_i r_i})`.

### Lemma 6.1 — monovariance under multiplication

If monic `f | F`, then

`S(f) subseteq S(F)`.

### Proof

Every monic divisor of `f` is also a monic divisor of `F`. `QED`

Consequently, as irreducible factors are processed one at a time, the Boolean bitset of reachable degrees **only gains entries**. Formula (6.1) gives an exact subset-sum dynamic program for this support. This is the requested monovariant: unlike the raw divisor count, multiplicities of factor identities cannot inflate it without adding a genuinely new reachable degree.

For an integer matrix `A`, prime `p`, write

`R_{p,d}(A) = 1_{ d in S(chi_A mod p) }`.

For any finite nonempty set `P` of primes define the common-degree count

`C_P(A) = sum_{d=1}^{floor(n/2)} prod_{p in P} R_{p,d}(A)`.   (6.2)

### Theorem 6.2 — exact aggregate multi-prime reducibility certificate

For every integer `n x n` matrix `A` and every finite nonempty prime set `P`,

`1_{ chi_A reducible over Q } <= 1_{ C_P(A) >= 1 } <= C_P(A)`.       (6.3)

Therefore for any random integer matrix ensemble,

`P( chi_A reducible over Q )
 <= E C_P(A)
 = sum_{d=1}^{floor(n/2)} P( d in intersection_{p in P} S(chi_A mod p) ).`  (6.4)

### Proof

If the monic integer polynomial `chi_A` is reducible over `Q`, Gauss's lemma gives a factorization into monic integer polynomials. Choose the smaller nonconstant factor, of degree `d` with `1 <= d <= floor(n/2)`. Reducing that monic factorization modulo **any** prime preserves the factor's degree and shows that `chi_A mod p` has a monic divisor of degree exactly `d`. Hence `R_{p,d}(A)=1` for every `p in P`, so `C_P(A)>=1`. The second inequality in (6.3) is immediate because `C_P(A)` is a nonnegative integer. Taking expectations proves (6.4). `QED`

This theorem is elementary, and the finite-field subset-sum mechanism is standard; I do **not** claim publication novelty for it. Its value here is route-level: it is the exact source-faithful quotient requested by the prior recovery. It sums factor identities *before* taking probabilities, erases the one-row target-by-target entropy obstruction, and reduces unconditional irreducibility to a common factor-**degree** problem.

For squarefree reductions, `S(f)` is literally the set of subset sums of irreducible factor degrees, making the connection to cycle-length subset sums in random permutations explicit. With repeated factors it is the bounded-multiplicity version (6.1). This is exactly the partition-level observable that the finite-field characteristic-polynomial literature is naturally organized around.

**Outcome of #13.** The correct monotone quotient is `S(chi_A mod p)`, not the number of modular factor identities. It yields the exact aggregate obstruction (6.4), but the required joint multi-prime estimate is still missing.

---

# 7. Section-I final handoff: exact blocker, failures, missing ingredient, simplest case, nearest solved comparison

## (a) Exact statement that blocks

A source-closing four-prime route would follow, for example, from proving for a fixed prime set such as `P={3,5,7,11}` that

`boxed{ sum_{d=1}^{floor(n/2)} P( d in intersection_{p in P} S(chi_A mod p) ) = o(1). }`       (7.1)

Theorem 6.2 would then give `P(chi_A reducible)=o(1)` unconditionally.

## (b) Every route tried and why it stopped

The complete method history is the nine prior triples listed in Section 1 plus this run's `#9/#10/#13`. The decisive stops are:

- finite exact enumeration moved the metric through `n=6` but is not asymptotic;
- 2-adic/even-order Eisenstein and odd Hensel/compression families certify genuine subfamilies but leave a positive-density/global gap;
- shifted-invertibility / polynomial-density reductions do not control all rational factor degrees;
- the first stuck recovery identified Eberhard's four-prime factor-partition method as the nearest solved template but Rademacher entries lack entrywise CRT-uniformity;
- one-row multi-prime exposure converts fixed specific factors to one signed walk, but the second recovery proved pointwise growing-degree uniformity impossible when the product target group carries more entropy than the `2^n` remaining sign vectors;
- this run proves that averaging **factor identities** first is also insufficient at first moment: even independent uniform finite-field polynomials have expected degree-`d` divisor count exactly one;
- the remaining viable quotient is the common divisor-degree support (6.4), whose joint Rademacher multi-prime law is not currently controlled.

## (c) What a proof needs that no route currently contains

It needs a genuinely **partition-level multi-prime decorrelation theorem** for Rademacher characteristic polynomials: enough control of the joint reachable-degree sets `S(chi_A mod p)` to make the expectation in (7.1) vanish. Crucially, this need not and cannot come from pointwise uniformity over exponentially many specific factor tuples after one-row exposure. It must aggregate identities before the entropy bottleneck—through a block exposure, a partition process, a higher moment/collision argument, or a different global-to-local mechanism.

## (d) Simplest special case still unproved

Even the single middle degree

`d_n = floor(n/3)`

is not controlled at the strength suggested by the four-prime sieve. A clean first target for a future reassignment is

`P( d_n in intersection_{p in {3,5,7,11}} S(chi_A mod p) ) = o(1/n)`.    (7.2)

Proving (7.2) alone would not settle the source, but it would demonstrate the missing partition-level decorrelation on a genuinely growing degree without demanding impossible factor-identity uniformity.

## (e) Nearest solved problem and missing ingredient

Eberhard's theorem is the nearest source-matching template. For Rademacher entries it gives high-probability irreducibility conditional on ERH. His unconditional modular route applies under stronger entry-law hypotheses that provide the needed joint modular randomness across several primes. The present Rademacher model lacks that input. Single-prime finite-field universality results provide local information but not the joint common-degree law (7.1).

### Mandatory Section-I choice

Because this is the third stuck episode after two hard-source recoveries, the only policy-compliant choice is **MOVE TO THE NEXT PROBLEM AND RECORD THE SWITCH**. F0013 is therefore handed off. The historical claim file is left untouched; a handoff is not permission for NM13-13 to silently restart it later, nor is an idle/disabled schedule a release for another worker. Any future reassignment must first repeat current literature, ownership, and route-clearance checks and bring a genuinely new partition-level mechanism.

# 8. Post-handoff residue-12 admission screen

After freezing the F0013 handoff, I resumed canonical intake screening rather than inventing a successor. I hashed the exact stored `dedup_key` strings, not display titles or aliases, through F0065. In the post-F0013 range F0014–F0065, the residue-12 identities encountered are exactly:

1. **F0021** — `zygouras_polymers_review_2024::question_5`, SHA-256 `37c323a028bce20b4442fd9cbb06a2833c23aa0b929e7596694128bacf8dbf69`, residue 12. The live source clause asks for limiting behaviours in the unresolved heavy-tailed directed-polymer phase diagram and asks whether Airy/KPZ asymptotics extend at fixed temperature. It is a large asymptotic universality target, already attempted in intake, with no honest finite certificate / exact construction / certified finite bound matching this HARD worker's admission rule. **Rejected at source-shape gate; not selected.**
2. **F0035** — `brownian_web_net_2015::conjecture_8.2_(bubble_complexity)`, SHA-256 `e576cbd02f829b8631d9b3f6b87c4144c593287e078c8e678301312bce2c6376`, residue 12. It is conditional on the preceding Brownian-net bubble hypothesis and concerns density/local finiteness of continuum orbit classes. It is already attempted and offers no source-valid finite deciding milestone of the required kind. **Rejected at source-shape/dependency gate; not selected.**
3. **F0039** — `brownian_web_net_2015::section_8.3_q8`, SHA-256 `b652fcfbd8ed8506ff86a0c6be6e317a7ee8caed203b00238ca1eb1272ae79b8`, residue 12. The source asks for the scaling limit of critical/near-critical 1+1-dimensional oriented percolation and explicitly notes the absence of conjectured critical scaling limits/exponent existence. It is already attempted and is neither a finite existence target nor a realistic explicit quantitative milestone for this worker. **Rejected at source-shape gate; not selected.**

No other canonical identity in F0014–F0065 hashes to residue 12. The rows F0040 onward encountered in that interval that are literature-resolved remain excluded regardless of shard. I did not create a claim for any rejected screening row, did not relabel an asymptotic continuum/KPZ problem as finite, and did not count screening as mathematical progress.

**Successor state: `ADMISSION_PENDING`. Durable cursor: F0066 in `probability_1000_intake_F_20260908/problems.jsonl`, then later intake families, with canonical-key hashing and the full source/literature/attempt/ownership gate before any create-only claim.**

The initial-method triple `#2/#14/#16` belongs to a newly admitted successor only; there is currently no successor, so no new-target methods are credited by this screening.

# 9. Handoff package preserved

A future explicitly reassigned F0013 worker must recover, at minimum:

- the canonical source statement and claim `operations/claims/F0013.md`;
- exact complete censuses through `n=6`, including the order-six certificate ending `ALL_EXACT_CHECKS_PASS`;
- the exact factor-pattern counts and irreducibility probability at order six;
- the even-order Krylov/Eisenstein and odd compression/Hensel restricted-family results;
- the polynomial-density/shifted-invertibility route and why it does not cover all factor degrees;
- stuck recovery 1 and its Eberhard four-prime comparison;
- the exact multi-prime one-row signed-walk/Fourier formula;
- stuck recovery 2's entropy/support/granularity obstruction to growing-degree pointwise uniformity;
- this run's exact first-moment identity `E D_d(F)=1` and the aggregate divisor-degree support reduction (6.4);
- `unchanged_runs_since_metric_movement = 7` and `stuck_recoveries_used = 2` at handoff;
- audit state `0/2` for source closure: neither P26 nor NM13-01 is presumed to pass.

No result in this handoff closes Vu's conjecture. The local status is **PARTIAL**; source status is **OPEN in the bounded 2026-09-18 check**.

# 10. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  worker: NM13-13
  category: HARD_OUTSIDE
  source_id: F0013
  historical_claim_path: operations/claims/F0013.md
  canonical_dedup_key: vu_combinatorial_rmt_2020::conjecture_11.1_(irreducibility)
  shard_mod_13: 12
  source_status: OPEN_BOUNDED_CHECK
  local_status: PARTIAL_HANDOFF
  metric_name: N_exact_irred
  metric_before: 6
  metric_after: 6
  metric_movement: false
  unchanged_runs_before: 6
  unchanged_runs_after: 7
  stuck_recoveries_before: 2
  stuck_recoveries_after: 2
  stuck_episode: 3
  hard_rotation_required: true
  methods_actual: [9, 10, 13]
  method_outcomes:
    9: "For uniform monic F over F_q, every fixed degree-d monic H divides F with probability q^-d and E[D_d(F)]=1 exactly; factor-identity averaging is first-moment critical even in the ideal model."
    10: "The randomized factor-tuple test derandomizes exactly to product_p D_{p,d}(A); its ideal-model expectation is still 1, so raw factor-identity counting cannot yield o(1)."
    13: "Defined divisor-degree support S(f), monotone under multiplication and determined solely by the factor-degree partition; proved P_Q(reducible) <= sum_d P(d lies in every modular support)."
  new_route_theorem: F0013-DEGREE-SUPPORT-10
  exact_blocker: "For a fixed prime set such as {3,5,7,11}, prove sum_{d<=n/2} P(d in intersection_p S(chi_A mod p)) = o(1)."
  simplest_unproved_special_case: "For d=floor(n/3), prove four-prime common degree reachability probability o(1/n)."
  audits:
    P26: NOT_REQUESTED
    NM13-01: NOT_REQUESTED
  disposition: "F0013 handed off after third stuck episode; NM13-13 must not resume without explicit fresh reassignment and new route clearance."
  successor_state: ADMISSION_PENDING
  screening_progress:
    F_intake_post_F0013: COMPLETE_F0014_THROUGH_F0065
    residue12_rejected:
      F0021: HARD_ASYMPTOTIC_KPZ_NO_FINITE_MILESTONE
      F0035: CONDITIONAL_CONTINUUM_NO_FINITE_MILESTONE
      F0039: CRITICAL_OP_SCALING_LIMIT_NO_FINITE_MILESTONE
  screening_cursor: F0066
  successor_metric_before: UNMEASURED
  successor_metric_after: UNMEASURED
  literature_check_date: 2026-09-18
  literature_scope: "Vu source; Eberhard 2022; Bary-Soroker-Garzoni-Sodin 2026; Anderson-O'Dorney 2026; current exact-title/author/source searches."
  literature_limit: "Bounded search only; no worldwide-openness or publication-novelty certificate."
```

No shared root, canonical claim file, peer namespace, workflow, permission, public surface, email/Drive item, paid-compute resource, or schedule was modified in this invocation. This file is the single immutable run report.
