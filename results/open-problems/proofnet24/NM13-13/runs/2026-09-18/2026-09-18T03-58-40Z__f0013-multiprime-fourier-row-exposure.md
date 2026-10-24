Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `N_exact_irred` stayed `6 -> 6`. Section-B methods actually tried: #7, #19, #27. New PARTIAL route theorem: an exact multi-prime row-exposure/Fourier formula reduces simultaneous fixed-factor divisibility under the common Rademacher signs to one signed walk on a product of finite fields; this removes entry-level cross-prime coupling as the immediate obstruction for fixed factor degrees, while exposing the still-unproved large-degree Fourier-mass estimate.**

# NM13-13 — F0013 multi-prime row exposure after stuck recovery 1

Date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-13`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `F0013` / `operations/claims/F0013.md`  
Canonical dedup key: `vu_combinatorial_rmt_2020::conjecture_11.1_(irreducibility)`  
Canonical SHA-256 / shard: `632e1dfff6e45b78875c758adf458c3ee12f39a1ef2867a71e5f178f18821e4d`, residue `12 mod 13`  
Source status after this run: **OPEN in the bounded current-status check below**  
Local status after this run: **PARTIAL / exact route theorem; source conjecture not solved**

## 1. Runtime, scheduler-control reality, continuity, and ownership

The prompt requests `GPT-6 / maximum`. That is not a binding runtime setting in the task-control surface exposed here. The actual model exposed to this invocation is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**. The exposed scheduler/task schema provides prompt/title, schedule or relative start, timing mode, and enabled state; it provides no model-family selector and no reasoning-effort selector. Making `GPT-6 / maximum` binding would require an owner-authorized product/workspace/API/admin surface exposing those controls together with per-run runtime attestation.

I did not create, edit, disable, or duplicate any schedule. Repository policy records historical `You cannot modify this task` responses in some authorization contexts and later successful edits from another authorized context. The legitimate remedy for a denied edit is the owning/authorized account or product/admin surface, not task cloning or access-control bypass.

This invocation continues the already-admitted F0013 target. It does **not** reopen intake, create a second claim, alter the shard identity, or edit a shared root. `operations/claims/F0013.md` still names NM13-13 as exclusive owner. Repository-wide searches recovered no F0013 release, handoff, retirement, competing owner, POSTED closure, or completed P26/NM13-01 source audit.

Before the mathematics I reread or targeted-search-recovered the required current state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- `operations/claims/F0013.md`;
- the exact intake row for F0013 and historical attempt `F0013-A001`;
- all prior NM13-13 reports, newest first, especially `2026-09-18T02-57-45Z__f0013-stuck-recovery-1.md`;
- newest visible neighboring NM13-12 report, which remains on distinct P0483;
- newest designated eventual audit-partner NM13-01 report, which hands off distinct P0292 and creates no ownership conflict;
- current repository searches for F0013 aliases, ownership, handoffs, attempts, audits, POSTED/settled state, and source corrections.

Connector searches are bounded, so this is authoritative source-specific continuity recovery, not a claim of byte-for-byte visibility over every historical blob.

The previous run was the mandatory first stuck recovery. It chose exactly one action, **PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM**, namely Eberhard's four-prime factor-degree sieve, and reserved methods **#7/#19/#27**. Those are the three methods actually attempted below. I do not re-credit any older method.

## 2. Exact source and fresh bounded literature/status check — 2026-09-18 UTC

The exact source remains Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Section 11, Conjecture 11.1:

> for an `n x n` matrix `A_n` with iid Rademacher entries, the characteristic polynomial `det(tI-A_n)` is irreducible over `Q` with probability `1-o(1)`.

Fresh dated searches included the exact source/conjecture wording and combinations of `Rademacher characteristic polynomial irreducible`, `random matrix Galois group`, `finite fields characteristic polynomial irreducible polynomial`, `normal vector random hyperplane`, and `2025/2026`.

The relevant current/nearby primary literature recovered is:

1. **Sean Eberhard, *The Characteristic Polynomial of a Random Matrix*, Combinatorica 42 (2022), 491–527, DOI `10.1007/s00493-020-4657-0`.** For iid `+-1` (and other fixed finitely supported integer laws), high-probability irreducibility and `Gal >= A_n` are conditional on ERH. The previous F0013 stuck report also recorded Eberhard's unconditional four-prime theorem for a different entry-law hypothesis that gives independent modular reductions; the Rademacher law does not have that CRT-uniformity.

2. **Kyle Luh, Sean Meehan, Hoi H. Nguyen, *Some new results in random matrices over finite fields*, JLMS 103 (2021), 1209–1252, DOI `10.1112/jlms.12405`.** It proves finite-field universality results for rank, normal-vector equidistribution, eigenvalue-freeness, and divisibility of the characteristic polynomial by a given irreducible polynomial. This is single-prime/local input; I did not find in the inspected material a theorem giving the four-prime large-factor partition law needed for F0013.

3. **Jennie Hansen and Eric Schmutz, *How random is the characteristic polynomial of a random matrix?*, Math. Proc. Camb. Phil. Soc. 114 (1993), 507–515.** It shows that for uniform finite-field matrices the characteristic polynomial behaves like a random monic polynomial away from its smallest factors. Eberhard's four-prime route uses this large-factor-partition shape.

4. **Lior Bary-Soroker, Daniele Garzoni, Sasha Sodin, *Irreducibility of the characteristic polynomials of random tridiagonal matrices*, J. Number Theory 280 (2026), 973–998, DOI `10.1016/j.jnt.2025.09.008`.** This is a different tridiagonal ensemble and remains conditional on suitable Riemann hypotheses.

5. **Theresa C. Anderson and Evan M. O'Dorney, *Galois groups of random integer matrices*, Math. Proc. Camb. Phil. Soc., published online 12 August 2026, DOI `10.1017/S0305004126102126`.** This very recent paper concerns the complementary **large-box model**: fixed matrix dimension `n`, entries bounded by `T`, and `T -> infinity`. It proves power-saving/counting results in that regime and explicitly distinguishes it from the restricted-entry model. It does **not** settle Vu's fixed-Rademacher, `n -> infinity` conjecture.

No unconditional source-matching resolution of Vu Conjecture 11.1 was recovered in this bounded search. This is **bounded negative evidence only**, not proof of worldwide openness or publication novelty.

The elementary finite-abelian-group Fourier identity used below is standard/folklore. I do **not** claim that identity as publication novelty. The source-relevant contribution of this run is the exact way it resolves the *common-sign multi-prime row-exposure bookkeeping* and pinpoints the stronger Fourier-mass statement still missing.

## 3. Frozen metric and counters

The frozen metric remains exactly the claim-file metric:

`N_exact_irred` = largest order `n` for which NM13-13 has exhaustively certified **all** `2^(n^2)` Rademacher matrices, including exact rational factor-degree distribution and irreducibility probability.

Before this run: **6**.  
After this run: **6**.  
Movement: **none**.

The order-six signed-permutation atlas remains the last complete finite census. I do not relabel the analytic route theorem below as movement of this metric.

This is the **fifth consecutive unchanged-metric invocation** since the order-six movement. The first formal stuck recovery has already been used and succeeded in changing the attack from 2-adic subfamilies to the multi-prime/global-to-local route:

`unchanged_runs_since_metric_movement = 5`,  
`stuck_recoveries_used = 1`.

Neither P26 nor NM13-01 is counted as an audit.

---

# 4. Method #19 — MAKE IT AN ALGORITHM: exact multi-prime row exposure

The previous stuck report identified a concrete question: the four modular reductions are fed by the **same signs**, so how can one recover enough joint modular randomness to imitate Eberhard's independent-four-prime model?

For **specific modular factors**, there is an exact answer.

Let `p_1,...,p_k` be distinct odd primes. For each `j`, let

- `g_j in F_{p_j}[t]` be monic irreducible of degree `d_j`;
- `K_j = F_{p_j^{d_j}}`;
- `alpha_j in K_j` be a root of `g_j`.

Put the additive product group

`G = K_1 x ... x K_k`.

Let `A` be an `n x n` iid Rademacher matrix. Expose its first `n-1` rows. For each `j`, consider the exposed first `n-1` rows of

`A - alpha_j I`

over `K_j`.

Assume for the moment that those rows have rank exactly `n-1`. Choose a nonzero right normal vector

`u^(j) = (u_1^(j),...,u_n^(j)) in K_j^n`.

The last row of `A` is an independent sign vector

`epsilon = (epsilon_1,...,epsilon_n) in {+-1}^n`.

Because the first `n-1` rows span the hyperplane orthogonal to `u^(j)`, the full shifted matrix is singular iff

`sum_i epsilon_i u_i^(j) = alpha_j u_n^(j)`.                 (4.1)

And because `alpha_j` is a root of the irreducible `g_j`,

`g_j | chi_A mod p_j`

is equivalent to that singularity statement.

Therefore the simultaneous divisibility event for all `j` is exactly **one signed walk** in the product group. Define

`v_i = (u_i^(1),...,u_i^(k)) in G`,

`b = (alpha_1 u_n^(1),...,alpha_k u_n^(k)) in G`.

Then, conditional on the exposed rows and the rank assumptions,

`g_j | chi_A mod p_j for every j`

iff

`sum_i epsilon_i v_i = b in G`.                              (4.2)

This is already the desired algorithmic reduction: solve `k` exact nullspaces over finite fields/extensions, then evaluate one finite-abelian signed-walk distribution.

## Theorem 4.1 — exact product-field Fourier formula

For `a=(a_1,...,a_k) in G`, let

`chi_a(x) = exp(2 pi i sum_j Tr_{K_j/F_{p_j}}(a_j x_j)/p_j)`

be the corresponding additive character. Then under the rank assumptions above,

`P( g_j | chi_A mod p_j for all j | first n-1 rows )`

is exactly

\[
\boxed{
\frac1{|G|}\sum_{a\in G}
\chi_a(-b)\prod_{i=1}^n \operatorname{Re}\chi_a(v_i).
}
\tag{4.3}
\]

Let `P = p_1 ... p_k` and

`rho_P = cos(pi/P) < 1`.

For a nontrivial character `a`, define

`m(a) = #{ i : chi_a(v_i) != 1 }`.

If

`m_* = min_{a != 0} m(a)`,

then

\[
\boxed{
\left|
P(\text{all }g_j\mid\chi_A\bmod p_j\mid\text{exposure})-|G|^{-1}
\right|
< \rho_P^{m_*}.
}
\tag{4.4}
\]

### Proof

Fourier inversion on the finite additive group `G` gives

\[
1_{S=b}=|G|^{-1}\sum_{a\in G}\chi_a(S-b),
\]

where `S=sum_i epsilon_i v_i`. Taking expectation over the independent signs,

\[
E\chi_a(S)
=\prod_i E\chi_a(\epsilon_i v_i)
=\prod_i \frac{\chi_a(v_i)+\chi_a(-v_i)}2
=\prod_i \operatorname{Re}\chi_a(v_i),
\]

which proves (4.3).

Every value of a product character lies among the `P`th roots of unity, because the prime orders are pairwise coprime. Since `P` is odd, for a nontrivial `P`th root `z != 1`,

\[
|\operatorname{Re}z|\le \cos(\pi/P)=\rho_P.
\]

Thus each nontrivial Fourier coefficient in (4.3) has magnitude at most `rho_P^{m(a)}`. Removing the trivial character and summing gives

\[
|\text{error}|
\le |G|^{-1}\sum_{a\ne0}\rho_P^{m(a)}
\le \frac{|G|-1}{|G|}\rho_P^{m_*}
<\rho_P^{m_*}.
\]

This proves (4.4). `QED`

## Primewise support already controls product support

There is a useful exact corollary which is easy to miss. Write the product character as

`chi_a(v_i)=prod_j chi_{j,a_j}(u_i^(j))`,

where each factor has order dividing the distinct prime `p_j`. If this product equals `1`, then **every factor equals `1`**: raise the identity to `P/p_j` to isolate the `j`th factor, and use that `P/p_j` is invertible modulo `p_j`.

Consequently, for any nonzero tuple `a`, if `a_j != 0` then

`#{i: chi_a(v_i)!=1} >= #{i: chi_{j,a_j}(u_i^(j))!=1}`.       (4.5)

So a prime-by-prime normal-vector anti-structure statement is sufficient to force linear support for **every product character**. One does not need independence of the normal vectors across primes for this support implication.

**Outcome of #19.** The common-sign coupling is not an algebraic dead end for fixed specific factors. It becomes a completely explicit finite-group Fourier problem, and the generic-rank branch needs a normal-vector Fourier-mass estimate rather than entry-level CRT independence.

---

# 5. Method #7 — TAKE THE LIMIT: fixed degrees work conditionally, growing degrees reveal the real barrier

Suppose the primes are fixed and the degrees `d_j` are fixed. If a typical exposure satisfies the generic rank assumptions and there is a constant `c>0` such that every nontrivial primewise additive character is active on at least `c n` coordinates, then (4.5) gives `m_* >= c n`. Hence

\[
P(\text{all fixed }g_j\mid\chi_A\bmod p_j\mid\text{exposure})
=|G|^{-1}+O(e^{-\kappa_P c n}),
\]

where

`kappa_P = -log cos(pi/P) > 0`.                               (5.1)

For the four concrete primes `3,5,7,11`, `P=1155` and

`kappa_P approximately 3.6991872607 x 10^(-6)`.

Because `|G|` is constant when all `d_j` are fixed, this is genuine asymptotic equidistribution **provided** the stated normal-vector hypothesis and the rank branch hold with high probability. I have not proved those hypotheses here for extension-field normals, so (5.1) is a conditional route corollary, not an unconditional new source theorem.

The important point is what happens when the factor degrees grow with `n`, which is exactly the regime needed for Eberhard's large-factor partition sieve.

Write the exact relative Fourier error from (4.3) as

\[
\mathcal M(U)
:=
\sum_{a\ne0}
\left|\prod_i \operatorname{Re}\chi_a(v_i)\right|.
\tag{5.2}
\]

Then relative equidistribution follows from the **Fourier-mass condition**

\[
\boxed{\mathcal M(U)=o(1).}
\tag{FM}
\]

A mere pointwise support bound `m(a)>=cn` gives only

\[
\mathcal M(U)\le (|G|-1)e^{-\kappa_P c n}.
\]

When `sum_j d_j log p_j` is of order `n`, `|G|` is itself exponential in `n`; the crude maximum-coefficient estimate is therefore far too weak. For the four-prime product it is especially weak because `kappa_1155` is small.

This is the main mathematical diagnosis of the run:

> **Fixed-factor multi-prime dependence is tractable by row-exposure Fourier analysis; the large-factor source obstruction is an entropy problem over exponentially many product characters, not merely the fact that the same signs feed all primes.**

To reach the source one needs a typical-exposure estimate for the **sum of Fourier weights**, stratified by structured/large-spectrum characters, not another worst-character Littlewood-Offord bound.

**Outcome of #7.** The limiting analysis sharply separates the regime where the port can plausibly work (fixed/low extension degree) from the regime that still blocks F0013 (growing factor degrees). This is why simply importing a single-prime normal-vector theorem is not yet enough.

---

# 6. Method #27 — SWAP THE QUANTIFIERS: fix the four primes first, then ask for one all-degree certificate

Fix four odd primes in advance, for example `3,5,7,11`. For a matrix `A`, let

\[
D_p(A)=\{\deg h:\ h\text{ is a monic divisor of }\chi_A\bmod p\}.
\]

Gauss's lemma gives the deterministic implication

\[
\chi_A\text{ reducible over }\mathbf Q
\Longrightarrow
\exists d\in[1,\lfloor n/2\rfloor]
\text{ with }
 d\in\bigcap_{p\in\{3,5,7,11\}}D_p(A).
\tag{6.1}
\]

Thus the fixed-prime certificate

\[
\bigcap_{p\in\{3,5,7,11\}}D_p(A)
\cap[1,\lfloor n/2\rfloor]=\varnothing
\tag{6.2}
\]

is sufficient for rational irreducibility. This is the quantifier order used by the nearby four-prime method: choose the primes once, then rule out **all** rational factor degrees at once.

Theorem 4.1 now says something precise about the common-sign coupling underneath (6.2): for any **fixed tuple of irreducible modular factors**, the generic last-row constraint is a product-field signed walk, and primewise character support already prevents exact product-character collapse.

But (6.2) is a union over a huge collection of modular factor configurations and, in the source-relevant degree range, over exponentially many Fourier modes. Therefore a proof of (6.2) cannot be assembled by a naive union bound over Theorem 4.1. It needs one of the following genuinely stronger objects:

1. a four-prime joint law for large factor-degree partitions under the common-sign Rademacher coupling;
2. a direct typical-exposure bound `(FM)` strong enough at extension degrees growing with `n`;
3. a coarser invariant of the four modular characteristic polynomials whose compatibility already excludes every common divisor degree but has only subexponential entropy.

**Outcome of #27.** Fixing the primes first is still the right source-level quantifier order, but the run identifies exactly why the fixed-factor Fourier formula is insufficient by itself and what strength the next theorem must have.

---

# 7. What moved mathematically, what did not, and the next source-level target

This run does **not** prove Vu's conjecture, does not improve the frozen exhaustive cutoff beyond `n=6`, and does not claim a new literature theorem about finite-field normal vectors. The new internal result is a complete on-page derivation of the multi-prime last-row reduction and its Fourier bound. Its mechanism is standard Fourier analysis; novelty is **UNVERIFIED**.

What materially changed is the obstruction. The previous report said “joint four-prime factor data under common signs” was the missing bridge. This run decomposes that statement:

- **specific fixed modular factors:** exact product-field signed-walk formula available;
- **cross-prime exact character support:** reduces to primewise support because the prime orders are coprime;
- **growing factor degrees:** still blocked by the total Fourier mass over exponentially many characters;
- **source-level all-degree sieve:** still needs a large-factor partition law or a lower-entropy surrogate.

The next substantive target, if F0013 continues under the hard-source stuck policy, is therefore **not** another finite atlas and not another scalar-eigenvalue estimate. It is:

\[
\boxed{
\text{either prove a nontrivial typical-exposure bound on }\mathcal M(U)
\text{ for a growing degree window, or exhibit a structured Fourier family showing this port cannot scale.}
}
\tag{7.1}
\]

The next previously untried Section-B methods reserved, and **not counted as attempted here**, are:

- **#8 GO THE OTHER WAY AND DISCRETIZE:** stratify product characters by exact discrepancy/level sets and test whether the Fourier mass can be reduced to finitely many structural classes;
- **#12 FIND WHAT IS CONSERVED:** identify an invariant of product-field normal vectors under row exposure that controls the count of large Fourier coefficients;
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT:** actively construct a typical-looking exposure with exponentially many near-trivial product characters; if such exposures have non-negligible probability, abandon the four-prime port rather than forcing it.

Because the frozen metric remains unchanged, `unchanged_runs_since_metric_movement` advances to **5**. The hard-source recovery count remains **1**; this invocation is the substantive run prescribed by recovery 1, not recovery 2. A second formal stuck-recovery episode may be used only under the owner's Section-I rule; a third stuck episode on F0013 requires a preserved handoff and rotation.

## 8. Audit / artifact status

No checker was manufactured merely to certify an unchanged number. The new claim is theorem-sized and its complete proof is written in Sections 4–6. There is no finite computational core requiring a checker in this run.

No audit is presumed. P26: **NOT REQUESTED / NOT PASSED**. NM13-01: **NOT REQUESTED / NOT PASSED**.

No paper package is created because the exact source remains OPEN.

## 9. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-13
  category: HARD OUTSIDE
  source_id: F0013
  claim_path: operations/claims/F0013.md
  owner: NM13-13
  canonical_dedup_key: "vu_combinatorial_rmt_2020::conjecture_11.1_(irreducibility)"
  source_status: OPEN
  local_status: PARTIAL
  metric_name: N_exact_irred
  metric_before: 6
  metric_after: 6
  movement: false
  unchanged_runs_since_metric_movement: 5
  stuck_recoveries_used: 1
  methods_tried: [7, 19, 27]
  method_outcomes:
    7: "Fixed-degree multi-prime row exposure would equidistribute under linear character support, but growing degrees require total Fourier-mass control; worst-character bounds are exponentially too weak."
    19: "Proved exact product-field row-exposure/Fourier formula and support bound for simultaneous divisibility by fixed irreducible factors."
    27: "Fixed four primes give the correct all-degree irreducibility certificate; theorem 4.1 handles fixed factor tuples but not the exponentially large factor-partition union."
  new_internal_claims:
    - NM13-13-F0013-MULTIPRIME-ROW-EXPOSURE-08
  audits:
    P26: NOT_REQUESTED
    NM13-01: NOT_REQUESTED
  next_step: "Attack the growing-degree Fourier mass M(U), or construct a structured near-trivial-character family showing that the four-prime port cannot scale; reserved B8/B12/B23."
  literature_check_date: 2026-09-18
  literature_scope: "Vu source; Eberhard 2022; Luh-Meehan-Nguyen 2021; Hansen-Schmutz 1993; Bary-Soroker-Garzoni-Sodin 2026; Anderson-O'Dorney 2026; exact/current 2025-2026 searches."
  literature_limit: "Bounded web/index search; no worldwide-openness or novelty certificate."
```

## 10. Save/readback obligation

This report is the single immutable run report for the invocation. It is written only in `proofnet24/NM13-13/runs/`. No shared root, peer namespace, claim file, schedule, workflow, permission, email/Drive item, or public surface is modified. Readback must occur at the returned commit, without a receipt-only follow-up commit.
