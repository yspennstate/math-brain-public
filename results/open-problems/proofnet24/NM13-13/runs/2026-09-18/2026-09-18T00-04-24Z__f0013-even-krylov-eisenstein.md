Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `N_exact_irred` stayed `6 -> 6`. Section-B methods actually tried: #4, #11, #24.**

# NM13-13 — F0013 even-order 2-adic Krylov/Eisenstein irreducible family

Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-13`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `F0013` / `operations/claims/F0013.md`  
Source status after this run: **OPEN**  
Local status after this run: **PARTIAL**

## 1. Runtime, continuity, ownership, and controls

The requested `GPT-6 / maximum` setting is not a binding runtime setting in the exposed task-control surface. The actual model exposed to this invocation is **GPT-5.6 Sol** and authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. The available scheduler control schema exposes title/prompt, schedule or relative start, timing mode, and enabled state; it exposes no model-family or reasoning-effort selector. Changing that would require an authorized scheduler/product interface that actually exposes those fields. I did not create or modify any schedule. A historical `You cannot modify this task` result for a P26 scheduler context is not a license to bypass ownership or duplicate the task; current repository history also records a later successful P26 update from another authorized context, so such a denial is context-specific and must be handled through the owning account/workspace or another authorized product/admin surface.

This run **continues the already-admitted F0013 source**. It does not reopen intake, create a new claim, or alter the shard identity. The canonical dedup key remains

`vu_combinatorial_rmt_2020::conjecture_11.1_(irreducibility)`,

whose SHA-256 integer has residue `12 mod 13`, matching NM13-13. `operations/claims/F0013.md` remains exclusively owned by NM13-13.

Before doing new mathematics I reread/recovered the current controlling and continuity surfaces required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- the later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- `operations/claims/F0013.md`;
- the F-series intake / canonicalization / attempt material, including the historical `F0013-A001` ERH/modular-factorisation bottleneck;
- the newest own report, `proofnet24/NM13-13/runs/2026-09-17/2026-09-17T23-15-22Z__f0013-exact-n6-signed-permutation.md`, and its exact order-six checker/output;
- the newest neighboring NM13-12 report and the newest report of the designated eventual second-audit partner NM13-01;
- current repository searches for F0013 ownership, handoffs, aliases, retirement, posting, and competing assignments.

No newer conflicting owner, release, handoff, retirement, posted resolution, or source closure was recovered. Historical attempt `F0013-A001` remains controlling continuity for the ERH/Chebotarev obstruction and is not relabeled as new work.

## 2. Exact source and bounded literature check — 2026-09-18 UTC

The exact source remains Van H. Vu, *Recent progress in combinatorial random matrix theory*, Probability Surveys 18 (2021), Section 11, Conjecture 11.1: for an `n x n` matrix `A` with iid Rademacher entries, prove that

`P(det(tI-A) is irreducible over Q) = 1-o(1)`.

Fresh bounded searches used the source title and combinations of

- `Rademacher random matrix characteristic polynomial irreducible unconditional 2026`,
- `Van Vu Conjecture 11.1 characteristic polynomial irreducible 2026`,
- `Eisenstein characteristic polynomial random sign matrix Rademacher 2-adic`,
- `2-adic characteristic polynomial Bernoulli random matrix irreducible`,
- `Krylov Eisenstein characteristic polynomial random matrix mod 2`.

The controlling nearby literature recovered is still:

1. **Sean Eberhard, *The Characteristic Polynomial of a Random Matrix*, Combinatorica 42 (2022), 491–527, DOI 10.1007/s00493-020-4657-0.** For iid `+-1` entries it proves high-probability irreducibility and `Gal >= A_n` **conditionally on ERH**. It does not close the unconditional source.
2. **Lior Bary-Soroker, Daniele Garzoni, Sasha Sodin, *Irreducibility of the characteristic polynomials of random tridiagonal matrices*, Journal of Number Theory 280 (2026), 973–998, DOI 10.1016/j.jnt.2025.09.008.** This is a different tridiagonal ensemble and is conditional on suitable Riemann hypotheses.
3. **Theresa C. Anderson, Evan M. O'Dorney, *Galois groups of random integer matrices*, published online 12 August 2026, DOI 10.1017/S0305004126102126.** This studies fixed dimension with entry height tending to infinity, not the restricted-entry `n -> infinity` regime of F0013.
4. **Hansen–Schmutz and finite-field characteristic-polynomial work**, together with the Luh–Meehan–Nguyen finite-field universality line recovered in the preceding run, remain relevant to modular factor statistics but do not by themselves cross the arithmetic bridge to unconditional rational irreducibility of the Rademacher characteristic polynomial.

No unconditional source-matching resolution, and no prior source explicitly matching the 2-adic Krylov/Eisenstein family below, was recovered in this bounded search. That is **bounded negative evidence only**. It is not proof of worldwide openness or publication novelty. The determinant lemma, Eisenstein criterion, Krylov sequences, and finite-field linear algebra used below are classical/folklore ingredients; novelty of this particular synthesis/application is **UNVERIFIED**.

## 3. Frozen metric — no movement

The metric remains exactly the admission metric:

`N_exact_irred` = largest order `n` for which NM13-13 has an exhaustive exact certification covering **all** `2^(n^2)` Rademacher matrices, with exact `Q`-factor-degree distribution and irreducibility probability.

Before this run: **6**.  
After this run: **6**.  
Movement: **none**.

The preceding order-six atlas already exhausts all `2^36` matrices by an exact signed-permutation quotient. This run proves an **all-even-n analytic subfamily theorem**, not a complete order-seven census, so I do not rename the new probability as the frozen metric.

This is the **first unchanged run** since the previous metric movement. Thus `unchanged_runs = 1`; hard stuck-recovery episodes used remain `0`.

---

# 4. New route: rank-one parity transfer to a 2-adic irreducibility certificate

Let `n` be even, let `A` be any `n x n` Rademacher matrix, let `J=11^T` be the all-ones matrix, and write uniquely

`A = J - 2B`,

with `B in {0,1}^{n x n}`. For a uniform Rademacher matrix, `B` is a uniform binary matrix.

Put `u=(1,...,1)^T` and define

`f_B(y) = det(yI+B)`,

`g_B(y) = u^T adj(yI+B) u`,

`F_B(y) = 2 f_B(y) - g_B(y)`.

The rank-one determinant identity gives the exact polynomial relation

`chi_A(2y) = det(2(yI+B)-uu^T) = 2^(n-1) F_B(y)`.       (4.1)

The new observation is that the very strong parity event

`g_B(y) = 1  (mod 2)`                                             (4.2)

forces irreducibility over `Q`, and (4.2) has an exact closed-form probability that can be counted by a Krylov-basis argument.

## 5. Theorem F0013-EVEN-2ADIC-04

### Theorem

For every even `n>=2`, let `A` be an iid Rademacher `n x n` matrix and let `B=(J-A)/2`. Define the event

`E_n := { u, Bu, ..., B^(n-2)u is a basis of H=u^perp over F_2,
          and B^(n-1)u notin H }`.

Then every `A` in `E_n` has irreducible characteristic polynomial over `Q`. Moreover

`P(E_n)
 = 2^(-(n-1)) product_{r=1}^{n-2} (1-2^(-r))`,                  (5.1)

so in particular

`P(chi_A irreducible over Q)
 >= 2^(-(n-1)) product_{r=1}^{n-2} (1-2^(-r))`                  (5.2)

for every even `n`.

Equivalently, the exact number of Rademacher matrices in this certified family is

`N_n = 2^(2n-1) product_{j=1}^{n-2} (2^(n-1)-2^j)`.             (5.3)

The probability in (5.1) is asymptotic along even `n` to

`C_2 2^(-(n-1))`, where `C_2 = product_{r>=1}(1-2^(-r)) > 0`.

This is an unconditional explicit irreducible family of exponentially small density. It does **not** imply Vu's `1-o(1)` conjecture.

### Proof, Step 1 — Eisenstein from the rank-one numerator

Reduce (4.1) modulo `2`. Since `2 f_B` vanishes modulo two,

`F_B(y) = g_B(y)  (mod 2)`

(the minus sign is immaterial in characteristic two). Thus on (4.2),

`F_B(y) = 1  (mod 2)`.

The leading coefficient of `F_B` is exactly `2`, because `f_B` is monic of degree `n` and `g_B` has degree at most `n-1`. Hence, if

`F_B(y)=2y^n+a_1 y^(n-1)+...+a_n`,

then (4.2) says

`2 | a_1,...,a_(n-1)` and `2 does not divide a_n`.

Consider the reciprocal polynomial

`R_B(z)=z^n F_B(1/z)=2+a_1 z+...+a_n z^n`.

Every nonleading coefficient of `R_B` is divisible by `2`, its constant coefficient is `2` and therefore not divisible by `4`, and its leading coefficient `a_n` is odd. By Eisenstein at `2`, `R_B` is irreducible over `Q`. Reciprocity preserves reducibility, so `F_B` is irreducible over `Q`. Equation (4.1), followed by the invertible linear change of variable `x=2y`, implies that `chi_A(x)` is irreducible over `Q`.

### Proof, Step 2 — turn (4.2) into a Krylov moment condition

Work over `F_2`. Since

`g_B(y)/f_B(y) = u^T (yI+B)^(-1) u`,

the formal Laurent expansion at infinity is

`g_B(y)/f_B(y) = sum_{k>=0} m_k y^(-k-1)`,

where

`m_k = u^T B^k u in F_2`.

(The alternating signs in the geometric series disappear in characteristic two.) Because `f_B` is monic of degree `n` and `deg g_B <= n-1`, comparison at infinity gives the exact equivalence

`g_B(y)=1`

if and only if

`m_0=m_1=...=m_(n-2)=0,  m_(n-1)=1`.                            (5.4)

Indeed `1/f_B(y)=y^(-n)+O(y^(-n-1))`; if the first `n` Laurent coefficients agree with this pattern, then `(g_B-1)/f_B=O(y^(-n-1))`, impossible for a nonzero numerator of degree at most `n-1`.

For even `n`, `m_0=u^T u=n=0` in `F_2`, as required.

### Proof, Step 3 — the moment condition is exactly first exit from the hyperplane after a Krylov basis

Let

`v_k=B^k u`, `H=u^perp={v:u^T v=0}`.

Since `n` is even, `u=v_0` belongs to `H`, and `dim H=n-1`. Condition (5.4) says

`v_0,...,v_(n-2) in H`, while `v_(n-1) notin H`.                (5.5)

I claim the first `n-1` vectors in (5.5) are automatically linearly independent. Otherwise let `r<=n-2` be the first index such that

`v_r in span(v_0,...,v_(r-1))`.

Then `W=span(v_0,...,v_(r-1))` is `B`-invariant: `Bv_i=v_(i+1)` for `i<r-1`, and `Bv_(r-1)=v_r in W`. Hence every later Krylov vector remains in `W subset H`, contradicting `v_(n-1) notin H`. Therefore

`v_0,...,v_(n-2)`

is a basis of `H`. Conversely, if these vectors form a basis of `H` and `v_(n-1)` lies outside `H`, then (5.4) holds immediately. This proves the exact equivalence between (4.2) and the event `E_n` stated in the theorem.

### Proof, Step 4 — exact count

Count linear maps `B:F_2^n -> F_2^n` satisfying `E_n`.

The first basis vector of `H` is fixed as `v_0=u`. The number of ordered ways to complete it to the Krylov basis

`v_0,v_1,...,v_(n-2)`

of the `(n-1)`-dimensional hyperplane `H` is

`product_{j=1}^{n-2} (2^(n-1)-2^j)`.

There are exactly `2^(n-1)` choices for `v_(n-1)` outside `H`.

Once these vectors are chosen, the values

`B v_i = v_(i+1)`, `0<=i<=n-2`,

completely specify `B` on the basis of `H`. Choose any one fixed complement vector to `H`; its image under `B` is arbitrary, giving another `2^n` choices. Each resulting linear map is counted exactly once, since its Krylov sequence from `u` recovers the chosen vectors.

Hence the number of binary matrices is exactly

`N_n = 2^(n-1) * 2^n * product_{j=1}^{n-2}(2^(n-1)-2^j)`,

which is (5.3). Dividing by all `2^(n^2)` binary matrices and extracting the powers of two gives (5.1). `QED`

## 6. Direct coefficient form and the 2-adic extremal interpretation

Write

`chi_A(x)=x^n+c_1 x^(n-1)+...+c_n`.

From (4.1), the coefficient of `y^(n-k)` in `F_B(y)` is

`c_k / 2^(k-1)`.

Thus the same certificate can be checked without constructing `B`:

> For even `n`, if `2^k | c_k` for every `1<=k<=n-1` and `v_2(c_n)=n-1`, then `chi_A` is irreducible over `Q`.

The final condition is extremal in the familiar determinant divisibility sense: every `n x n` `+-1` determinant is divisible by `2^(n-1)` (subtract the first row from each other row and factor two from those `n-1` rows), so `v_2(det A)=n-1` is the smallest possible valuation. The new family is the portion of this minimal-determinant layer whose **entire transformed characteristic polynomial** has the one-segment reciprocal-Eisenstein parity profile.

This interpretation is useful but should not be overstated: minimal determinant valuation alone is weaker than the full certificate.

There is also a sharp parity warning for the next run. Since every sign matrix satisfies `A=J (mod 2)`, one has

`chi_A(x) = x^(n-1)(x-n)  (mod 2)`.

For even `n` this is `x^n`, which permits the totally ramified Eisenstein pattern above. For odd `n` it is `x^(n-1)(x+1)` with coprime factors. Thus **irreducibility over `Q_2` cannot be the odd-order certificate**, even though rational irreducibility may still hold; the odd-order route must deliberately break this parity symmetry rather than blindly copy the even-order proof.

## 7. Exact finite checks and comparison with the prior census

A new exact-integer checker was written only after the analytic route produced the theorem:

`proofnet24/NM13-13/artifacts/2026-09-18/2026-09-18T00-03-02Z__f0013_krylov_eisenstein_check.py`

Creation commit: `82c934422f6b5f1c998ad162030d7ed828012a6b`.

Archived executed output:

`proofnet24/NM13-13/artifacts/2026-09-18/2026-09-18T00-03-02Z__f0013_krylov_eisenstein_check.out`

Creation commit: `4f7c1673fb642550a60b60f26eea431dc547a2c0`.

The checker uses Python standard-library exact integers only. It exhausts **all** binary matrices at `n=2` and `n=4`, independently computes characteristic polynomials from traces/Newton identities, and verifies matrix-by-matrix that the Krylov moment event is exactly the reciprocal-Eisenstein coefficient event. It also verifies the closed count formula and compares it to the already archived exact irreducible counts. Output:

- `n=2`: `8` certificates out of `16`, probability `1/2`; this equals all `8` irreducibles.
- `n=4`: `3072` certificates out of `65536`, probability `3/64`; the prior atlas has `9024` irreducibles, so this family certifies exactly `16/47` of them.
- `n=6`: formula gives `660,602,880` certified matrices, probability `315/32768`; the prior exact atlas has `11,307,502,080` irreducibles, so the family accounts for exactly `4096/70111` of the order-six irreducibles.

The archived output terminates `ALL_EXACT_CHECKS_PASS`. This is a self-check, not an independent audit.

## 8. Section-B methods actually tried

### #4 — PROVE SOMETHING WEAKER, COMPLETELY

I did **not** try to force the full `1-o(1)` asymptotic. I asked for a completely explicit all-`n` irreducible subfamily with an exact probability. The even-order 2-adic family above gives precisely that:

`P(certified irreducible) = 2^(-(n-1)) product_{r=1}^{n-2}(1-2^(-r))`.

Outcome: **success as a complete restricted theorem; no frozen-metric movement and no source closure.**

### #11 — DUALIZE

I moved from the characteristic polynomial itself to the rank-one dual quantity

`u^T adj(yI+B)u / det(yI+B)`,

then to its projected Krylov moment sequence `u^T B^k u` over `F_2`. The condition that the adjugate numerator collapse to the constant `1` becomes an exact hyperplane-basis/first-exit statement, which is countable in closed form.

Outcome: **success; this is the mechanism of Theorem F0013-EVEN-2ADIC-04.**

### #24 — FIND THE EXTREMAL OBJECT

Within the 2-adic transform, I targeted the extremal reciprocal-Eisenstein profile: the numerator `g_B mod 2` has the smallest possible nonzero degree, namely the constant `1`, and the determinant lies on the minimum possible valuation layer `v_2(det A)=n-1`. The extremal objects are exactly binary maps whose Krylov orbit of `u` forms a basis of `u^perp` and exits on the next step. This classification makes the family exactly enumerable rather than heuristic.

Outcome: **success structurally**, but the exact density is only `Theta(2^(-n))`, so this extremal family is far too sparse to settle the source asymptotic and does not move `N_exact_irred`.

## 9. What this run changes and what it does not

What is genuinely new in the track:

- an unconditional all-even-order irreducibility certificate for a concrete Rademacher subfamily;
- an exact formula for the size/probability of that family;
- an exact bridge from a 2-adic coefficient profile to a finite-field Krylov-basis condition;
- a clear parity obstruction showing why a literal odd-order copy cannot use `Q_2` irreducibility.

What is **not** claimed:

- not a proof of `P(irreducible)->1`;
- not a movement of the frozen exhaustive-order metric `N_exact_irred`;
- not a publication-novelty certificate;
- not an independent audit;
- not a replacement for the historical ERH/modular-factorisation bottleneck.

P26 has not audited this claim. NM13-01 has not audited it. Neither is counted in advance.

## 10. Next route

The next run should **not** repeat #4/#11/#24. Planned methods are **#5, #15, #30**:

- **#5 ADD A PARAMETER:** thicken the exact parity condition to successive `2`-adic layers of the rank-one transfer numerator and determine which Newton-polygon profiles still force a large irreducible factor or full irreducibility;
- **#15 BREAK THE SYMMETRY ON PURPOSE:** treat odd `n`, where `chi_A mod 2 = x^(n-1)(x+1)`, by separating the distinguished simple `2`-adic root from the `(n-1)`-dimensional block rather than pretending the even argument survives;
- **#30 ONE PRIME / ONE SCALE AT A TIME:** classify the first few `2`-adic valuation layers exactly and ask whether their union has probability large enough to become source-relevant before returning to multi-prime arithmetic.

The route should be abandoned if these layers remain exponentially sparse without yielding a transferable arithmetic statement; in that case the next section-B triple must change rather than filing more certificates for the same rare family.

## 11. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-13
  category: HARD_OUTSIDE
  source_id: F0013
  claim_path: operations/claims/F0013.md
  source_status: OPEN
  local_status: PARTIAL
  metric:
    name: N_exact_irred
    before: 6
    after: 6
    movement: false
  new_claims:
    - id: F0013-EVEN-2ADIC-04
      scope: "For every even n, an explicit Krylov/Eisenstein subfamily of Rademacher matrices has irreducible characteristic polynomial over Q, with exact probability 2^{-(n-1)} prod_{r=1}^{n-2}(1-2^{-r})."
      novelty: UNVERIFIED
      audit_status: SELF_CHECK_ONLY
  section_B_methods:
    attempted: [4, 11, 24]
    outcomes:
      4: "SUCCESS complete all-even-n restricted theorem; source remains open"
      11: "SUCCESS rank-one adjugate/Krylov dualization"
      24: "SUCCESS exact extremal 2-adic/Krylov family; density Theta(2^-n), insufficient for source"
    next: [5, 15, 30]
  exact_artifacts:
    checker: proofnet24/NM13-13/artifacts/2026-09-18/2026-09-18T00-03-02Z__f0013_krylov_eisenstein_check.py
    checker_commit: 82c934422f6b5f1c998ad162030d7ed828012a6b
    output: proofnet24/NM13-13/artifacts/2026-09-18/2026-09-18T00-03-02Z__f0013_krylov_eisenstein_check.out
    output_commit: 4f7c1673fb642550a60b60f26eea431dc547a2c0
    terminal_status: ALL_EXACT_CHECKS_PASS
  unchanged_runs: 1
  stuck_recoveries_used: 0
  audit_status:
    P26: NOT_REQUESTED_NOT_PASSED
    NM13-01: NOT_REQUESTED_NOT_PASSED
  literature_check:
    date_utc: 2026-09-18
    result: "No unconditional source-matching resolution recovered in bounded search; novelty of new synthesis UNVERIFIED"
    access_limits: "bounded public web/source-title/current-primary search, not worldwide proof of openness"
  next_step: "2-adic layer thickening, odd-n symmetry break, then one valuation layer at a time; abandon if density stays exponentially sparse without transfer"
  shared_root_edits: none
```

No email/Gmail, Drive, public posting, paid compute, permission change, workflow execution, peer-track edit, shared-root edit, or schedule creation/modification was performed.

**End of complete run report.**
