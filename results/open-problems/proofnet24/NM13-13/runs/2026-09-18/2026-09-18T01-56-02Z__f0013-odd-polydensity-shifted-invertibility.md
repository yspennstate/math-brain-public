Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `N_exact_irred` stayed `6 -> 6`. Section-B methods actually tried: #6, #17, #26.**

# NM13-13 — F0013 odd-order polynomial-density irreducibility via shifted invertibility

Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-13`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `F0013` / `operations/claims/F0013.md`  
Canonical dedup key: `vu_combinatorial_rmt_2020::conjecture_11.1_(irreducibility)`  
Source status after this run: **OPEN**  
Local status after this run: **PARTIAL**

## 1. Runtime, continuity, ownership, and controls

The requested `GPT-6 / maximum` setting is not a binding runtime setting in the exposed task-control surface. The actual model exposed to this invocation is **GPT-5.6 Sol** and authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. The available task-control schema exposes prompt/title, schedule or relative start, timing mode, and enabled state; it exposes no model-family selector and no reasoning-effort selector. Making `GPT-6 / maximum` binding would require an authorized product/scheduler/API surface that exposes those fields together with runtime attestation.

I did not create, edit, disable, or duplicate any schedule. Repository policy records a historical `You cannot modify this task` result for P26 in one scheduler authorization context and a later successful P26 update from another authorized context. The legitimate response to such a denial is therefore the owning account/workspace or another authorized product/admin surface, not an access-control bypass or a duplicate task.

This run **continues the already-admitted F0013 source**. It does not reopen intake, create a new claim, alter the shard identity, or reinterpret a disabled task as a release. The create-only claim `operations/claims/F0013.md` remains owned exclusively by NM13-13. Its canonical key has SHA-256

`632e1dfff6e45b78875c758adf458c3ee12f39a1ef2867a71e5f178f18821e4d`,

whose integer residue modulo 13 is `12`, matching this worker.

Before new mathematics I reread or targeted-search-recovered the required current control and continuity surfaces:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- `operations/claims/F0013.md`;
- the F-series intake / canonicalization material and historical attempt `F0013-A001`;
- all prior NM13-13 reports, newest first, especially `proofnet24/NM13-13/runs/2026-09-18/2026-09-18T00-58-30Z__f0013-odd-compression-hensel.md`;
- the newest visible neighboring NM13-12 report, `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T00-52-07Z__p0483-span-regeneration-transfer.md`;
- the newest visible designated eventual second-audit-partner NM13-01 report, commit `5294635825d4be576855294022dbcb645dc960d1`, on P0292;
- current searches for F0013 ownership, aliases, handoffs, attempts, posted status, retirement, and source corrections.

No newer release, handoff, retirement, posted closure, competing owner, or completed P26/NM13-01 audit for F0013 was recovered. Search and connector surfaces are bounded; this is source-specific continuity recovery, not a claim of byte-for-byte omniscience over every historical blob.

The historical attempt `F0013-A001` remains controlling continuity for the ERH/Chebotarev bottleneck: modular factorisation statistics across enough primes are much harder than determinant/cokernel information. This run does not refile that obstacle as new work.

### Method history

Previous substantive triples on F0013 were:

- `#2/#14/#16`;
- `#18/#25/#30`;
- `#3/#20/#21`;
- `#4/#11/#24`;
- `#5/#15/#29`.

The preceding report nominated `#6/#17/#26`; those three were still untried on F0013 and are the methods genuinely used here.

## 2. Exact source and bounded literature check — 2026-09-18 UTC

The exact source remains Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Section 11, Conjecture 11.1:

> for an `n x n` matrix `A` with iid Rademacher entries, prove that `det(tI-A)` is irreducible over `Q` with probability `1-o(1)`.

Fresh bounded searches used the exact source/conjecture wording and combinations of

- `Rademacher characteristic polynomial irreducible unconditional 2026`;
- `Van Vu Conjecture 11.1 random matrix irreducibility 2026`;
- `random sign matrix integer eigenvalue shifted singularity`;
- `Jain Sah Sawhney smoothed analysis smallest singular value discrete noise`;
- `Galois groups random integer matrices 2026`.

The directly relevant current literature recovered is:

1. **Sean Eberhard, *The Characteristic Polynomial of a Random Matrix*, Combinatorica 42 (2022), 491–527, DOI 10.1007/s00493-020-4657-0.** For iid `+-1` entries it proves high-probability irreducibility **conditionally on ERH**. Thus it does not close the unconditional source.
2. **Vishesh Jain, Ashwin Sah, Mehtaab Sawhney, *On the smoothed analysis of the smallest singular value with discrete noise*, Bull. London Math. Soc. 54 (2022), 369–388, DOI 10.1112/blms.12561.** For deterministic `D` and iid mean-zero variance-one sub-Gaussian `M`, their first main theorem gives

   `P[s_n(D+M) <= eps] = O(eps sqrt(n)) + 2 exp(-Omega(n))`

   whenever `D` has `Omega(n)` singular values of size `O(sqrt(n))`. This published result is the key imported tool in this run.
3. **Bary-Soroker, Garzoni, Sodin, *Irreducibility of the characteristic polynomials of random tridiagonal matrices*, J. Number Theory 280 (2026), 973–998.** It treats a different tridiagonal ensemble and remains conditional on suitable Riemann hypotheses.
4. **Theresa C. Anderson, Evan M. O'Dorney, *Galois groups of random integer matrices*, published online 12 August 2026, DOI 10.1017/S0305004126102126.** It studies fixed dimension with entry height tending to infinity, not the fixed-entry Rademacher `n -> infinity` regime.

No unconditional source-matching resolution of Vu Conjecture 11.1 was recovered in this bounded search. This is **bounded negative evidence only**, not proof of worldwide openness or publication novelty.

The shifted-smallest-singular-value theorem itself is published prior art. I therefore **do not claim novelty** for the exponentially small probability of an integer eigenvalue derived below; it is a short corollary of published invertibility machinery. Publication novelty of combining that corollary with NM13-13's preceding odd-order `F_2` compression theorem is **UNVERIFIED**.

## 3. Frozen metric — no movement, threshold reached

The frozen metric remains exactly the admission metric:

`N_exact_irred` = largest order `n` for which NM13-13 has completed an exhaustive exact certification covering **all** `2^(n^2)` Rademacher matrices, with exact rational factor-degree distribution and irreducibility probability.

Before this run: **6**.  
After this run: **6**.  
Movement: **none**.

The order-six signed-permutation atlas remains the last exhaustive all-matrix census. The theorem below is asymptotic and analytic; it does not constitute an exhaustive order-seven census and does not justify renaming the metric.

This is the **third consecutive unchanged run** since the order-six movement:

`unchanged_runs_since_metric_movement = 3`,  
`stuck_recoveries_used = 0`.

Therefore, under the owner's Section-I protocol, the **next NM13-13 invocation must be a thinking-only stuck-recovery report with no new mathematical claim**. This run is the ordinary run that reaches the threshold; it does not pre-consume a recovery episode.

---

# 4. The new bridge: integer eigenvalues are exponentially rare

The preceding odd-order theorem reduced all rational reducibility on an exact event `G_n` of probability `Theta(1/n)` to one scalar obstruction: an odd integer eigenvalue. The missing estimate was

`P(G_n and A has an odd integer eigenvalue) = o(P(G_n)).`           (4.1)

The published shifted-invertibility theorem gives substantially more: **having any integer eigenvalue is exponentially rare**.

## Proposition F0013-INTEGER-EIGENVALUE-06

Let `A_n` be an `n x n` iid Rademacher matrix. There exists an absolute constant `c>0` such that, for all sufficiently large `n`,

`P(A_n has an integer eigenvalue) <= exp(-c n).`                    (4.2)

### Proof

We separate the argument into a self-contained norm truncation and the published shifted-singularity input.

### Step 1 — an elementary exponential operator-norm tail

Let `N` be a `1/4`-net of the Euclidean unit sphere in `R^n` with

`|N| <= 9^n`.

For any real matrix `M`, approximating a maximizing left and right unit vector by points of `N` gives the standard deterministic inequality

`||M|| <= 2 max_(x,y in N) |y^T M x|.`                             (4.3)

For fixed unit vectors `x,y`,

`y^T A_n x = sum_(i,j) y_i x_j a_ij`

is a Rademacher sum whose squared coefficients add to

`sum_(i,j) y_i^2 x_j^2 = 1`.

Hoeffding's inequality therefore gives

`P(|y^T A_n x| >= t) <= 2 exp(-t^2/2).`                            (4.4)

Taking `t=4 sqrt(n)` and union-bounding over at most `81^n` net pairs,

`P(||A_n|| > 8 sqrt(n))
 <= 2 * 81^n * exp(-8n)
 = 2 exp(-(8-log 81)n).`                                           (4.5)

Thus the exceptional norm event already has probability `exp(-Omega(n))`.

### Step 2 — every possible integer root becomes a solved shifted-singularity problem

On the event `||A_n|| <= 8 sqrt(n)`, every eigenvalue `lambda` satisfies

`|lambda| <= ||A_n||`,

so every integer eigenvalue `m` lies in

`|m| <= 8 sqrt(n)`.                                                (4.6)

Fix such an integer `m`. Apply the Jain–Sah–Sawhney theorem to

`D = -m I`, `M = A_n`.                                             (4.7)

The random matrix `M` has iid mean-zero variance-one sub-Gaussian entries. Every singular value of `D` equals `|m| <= 8 sqrt(n)`, so in particular `D` has `n = Omega(n)` singular values of size `O(sqrt(n))`, with a fixed implied constant `8`.

At `eps=0`, their theorem yields, uniformly over all integers in (4.6),

`P(det(A_n-mI)=0) <= 2 exp(-c_0 n)`                                (4.8)

for some constant `c_0>0` depending only on the fixed sub-Gaussian law and the fixed `8` bound.

There are at most `16 sqrt(n)+1` integers satisfying (4.6). Hence

`P(A_n has an integer eigenvalue)
 <= P(||A_n||>8 sqrt(n))
    + sum_(|m|<=8 sqrt(n)) P(det(A_n-mI)=0)`

`<= 2 exp(-(8-log81)n)
    + 2(16 sqrt(n)+1) exp(-c_0 n)`

`<= exp(-c n)`                                                     (4.9)

for some `c>0` and all sufficiently large `n`. `QED`

This proposition is deliberately presented as a **published-tool corollary**, not a new stand-alone random-matrix theorem.

---

# 5. Consequence for the odd-order compression event

Recall the preceding run's theorem for odd `n>=3`. Write

`A = J-2B`, `u=(1,...,1)^T`, `H=u^perp over F_2`,

and let

`D_B = pi_H B|_H : H -> H`.

Put `d=n-1`, and define

`G_n := { det(y I_H + D_B) is irreducible over F_2 }`.              (5.1)

The preceding run proved exactly that

`P(G_n)
 = [I_2(d)/2^d] product_(j=1)^(d-1) (1-2^(-j)),`                  (5.2)

where

`I_2(d)=(1/d) sum_(r|d) mu(r) 2^(d/r)`,                            (5.3)

and, on `G_n`,

`chi_A is reducible over Q  <=>  A has an odd integer eigenvalue.` (5.4)

Combining (5.4) with Proposition F0013-INTEGER-EIGENVALUE-06 immediately gives the main result of this run.

## Theorem F0013-ODD-POLYDENSITY-06

For odd `n`, let `A_n` be an iid Rademacher matrix and let `G_n` be the exact compression event above. Then there exists `c>0` such that

`P(G_n and chi_A reducible over Q) <= exp(-c n).`                  (5.5)

Consequently,

`P(chi_A irreducible over Q)
 >= [I_2(n-1)/2^(n-1)] product_(j=1)^(n-2)(1-2^(-j))
    - exp(-c n).`                                                  (5.6)

Moreover,

`P(chi_A irreducible over Q | G_n) = 1-exp(-Omega(n)).`            (5.7)

Finally, because the exact irreducible-polynomial count satisfies

`I_2(d)=2^d/d + O(2^(d/2)/d)`,                                    (5.8)

and the finite Euler product tends to

`C_2 := product_(j>=1)(1-2^(-j)) > 0`,                             (5.9)

we obtain the unconditional odd-order lower bound

`P(chi_A irreducible over Q)
 >= (C_2+o(1))/(n-1).`                                             (5.10)

### Proof

Equation (5.5) follows because on `G_n` reducibility forces an odd integer eigenvalue, while Proposition (4.2) bounds the larger event of **any** integer eigenvalue by `exp(-cn)`.

Subtracting that exceptional probability from the exact value (5.2) proves (5.6).

For (5.7), (5.2), (5.3), and the elementary estimate (5.8) imply `P(G_n)=Theta(1/n)`. Therefore

`P(reducible | G_n)
 <= exp(-cn)/P(G_n)
 <= C n exp(-cn)
 = exp(-Omega(n)).`                                                (5.11)

For completeness, (5.8) follows directly from the Möbius formula (5.3): the `r=1` term is `2^d/d`, while every proper divisor contributes exponent at most `d/2`, and the divisor count is subexponential. Combining with the convergence of the product in (5.9) gives (5.10). `QED`

---

# 6. What the three Section-B methods actually did

## Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

The preceding run's exact event had probability asymptotic to `C_2/(n-1)` but was blocked by one Hensel root being an ordinary integer. Rather than continuing purely 2-adic manipulation, I searched the random-matrix invertibility literature for the probability of singularity under deterministic scalar shifts.

The decisive published statement is Jain–Sah–Sawhney's discrete-noise smoothed-analysis theorem. At `eps=0`, a scalar shift `-mI` with `|m|=O(sqrt(n))` has exponentially small singularity probability. That is exactly the obstruction left by the previous theorem.

**Outcome of #17: success.** A nearby smallest-singular-value theorem supplies the anti-concentration statement missing from the arithmetic compression route.

## Method #6 — DEFORM TO A POINT YOU CAN SOLVE

The remaining obstruction `m is an eigenvalue of A` was rewritten as

`A-mI is singular`.                                                (6.1)

This scalar-shift deformation is materially different from the preceding run's rank-one `2`-adic parameter `sJ-2B`: it stays inside the exact source random matrix plus a deterministic matrix and lands directly in a published theorem whose hypotheses can be checked uniformly after norm truncation.

**Outcome of #6: success.** Every candidate ordinary integer root is transferred to a solved shifted-invertibility problem.

## Method #26 — HUNT THE SPORADIC CASE

The preceding compression theorem had already shown that all possible rational reducibility on `G_n` is a single exceptional linear factor. I treated that factor as the sporadic case and asked how many ordinary integers it could represent.

A simple exponential operator-norm tail reduces the candidates to only `O(sqrt(n))` integers, and the published shifted-singularity theorem kills each candidate with probability `exp(-Omega(n))`. Thus the whole sporadic obstruction is exponentially negligible compared with `P(G_n)=Theta(1/n)`.

**Outcome of #26: success.** The unique ordinary-integer branch is not merely finite-checkable per matrix; probabilistically it disappears exponentially fast.

---

# 7. Source relevance and exact remaining gap

This run moves the **mathematics** substantially even though the frozen exhaustive metric does not move.

The previous odd-order route only said:

`on an event G_n of probability Theta(1/n), reducibility is equivalent to one integer-root obstruction.`

This run upgrades that to:

`on G_n, irreducibility holds with conditional probability 1-exp(-Omega(n)).`

Hence an unconditional `Theta(1/n)` irreducibility lower bound is certified along odd orders.

That is still far from Vu's source target `1-o(1)`. The exact missing phenomenon is no longer the Hensel root inside `G_n`; it is **coverage**. The current mod-2 compression certificate sees only a `Theta(1/n)` slice of all matrices. A source-level proof needs either:

- a family of exact local/modular certificates whose union has probability `1-o(1)`, with overlaps controlled; or
- a different global argument showing irreducibility outside `G_n` without relying on the ERH/Chebotarev route already identified in `F0013-A001`.

I do not relabel the polynomial-density theorem as source closure. F0013 remains **OPEN / NM13-13 PARTIAL**.

No P26 or NM13-01 audit is requested or counted. No self-check is an independent audit. No new finite enumeration claim was made in this run, so no checker artifact was manufactured. The theorem-sized proof is written on the page, and its only non-elementary input is the explicitly cited published shifted-smallest-singular-value theorem.

## 8. Mandatory next-run protocol

Because `N_exact_irred` has now stayed at `6` for three consecutive runs, the **next invocation must be a Section-I thinking-only stuck-recovery report with no new claims**.

That report must state, in the owner's required five-part format:

1. the exact source blocker in one displayed formula;
2. every route tried and its precise failure mode;
3. what a proof would have to contain that no route yet contains;
4. the simplest special case still unproved;
5. the nearest solved problem in the literature and the ingredient it has that F0013 lacks.

It must then choose exactly one permitted recovery action. The next three still-untried Section-B lenses reserved for that thinking run are **#1, #12, #27**. They are **not** counted as tried in this run.

---

## 9. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-13
  category: HARD_OUTSIDE
  source_id: F0013
  claim_path: operations/claims/F0013.md
  canonical_dedup_key: vu_combinatorial_rmt_2020::conjecture_11.1_(irreducibility)
  source_status: OPEN
  track_status: PARTIAL
  metric:
    name: N_exact_irred
    before: 6
    after: 6
    movement: none
  theorem_this_run: F0013-ODD-POLYDENSITY-06
  theorem_scope: >-
    For odd n, on the exact F_2 compression event G_n from the preceding
    run, rational reducibility is exponentially unlikely. A published
    shifted-smallest-singular-value theorem implies that an iid Rademacher
    matrix has any integer eigenvalue with probability exp(-Omega(n));
    hence P(irreducible | G_n)=1-exp(-Omega(n)) and the unconditional
    irreducibility probability is at least (C_2+o(1))/(n-1).
  published_input:
    authors: Jain-Sah-Sawhney
    title: On the smoothed analysis of the smallest singular value with discrete noise
    journal: Bulletin of the London Mathematical Society 54 (2022), 369-388
    doi: 10.1112/blms.12561
  methods_tried:
    - 6
    - 17
    - 26
  method_outcomes:
    6: scalar spectral shift converts an integer eigenvalue into a solved deterministic-shift singularity problem
    17: published smoothed-invertibility theorem supplies the missing anti-concentration estimate
    26: all ordinary-integer root candidates are confined to O(sqrt(n)) values and are exponentially negligible
  unchanged_runs_since_metric_movement: 3
  stuck_recoveries_used: 0
  next_run_required: SECTION_I_THINKING_ONLY_STUCK_RECOVERY
  next_methods_reserved_not_tried:
    - 1
    - 12
    - 27
  audits_counted:
    p26: false
    nm13_01: false
  literature_check_date: 2026-09-18
  literature_outcome: >-
    Fresh bounded search recovered Eberhard's conditional-ERH full-matrix
    theorem, Jain-Sah-Sawhney shifted invertibility, the 2026 conditional
    tridiagonal theorem, and Anderson-O'Dorney's fixed-dimension
    growing-height theorem. No unconditional source-matching resolution of
    Vu Conjecture 11.1 was recovered. The integer-eigenvalue estimate is
    treated as a published-tool corollary; novelty of its combination with
    the NM13-13 compression theorem is unverified.
  next_step: >-
    Mandatory Section-I thinking-only recovery. The central blocker is
    coverage: replace the Theta(1/n) certificate slice by a source-valid
    family or mechanism whose certified irreducible mass tends to one.
```

## 10. Repository-write compliance

This invocation writes exactly this one immutable report in the NM13-13 `runs/` namespace. It does not edit shared root ledgers, claims, peer tracks, schedules, workflows, permissions, email, Drive, or public surfaces. The report is to be read back at the creation commit; no receipt-only follow-up commit is authorized.
