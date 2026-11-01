Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0012 terminal research artifact — Fourier collision identity, Krylov row reconstruction, and a structured-fiber criterion

Date: 2026-09-19 UTC  
Slot: `R7-07`  
Native identity: `6aabe8413f60819197825dd81ca138ae`  
Repository: `yspennstate/math-open-problems`, branch `master`  
Run-start master snapshot: `13b623132250e526bf18294cef8b502ea145d30f`  
Fresh pre-write master snapshot: `e9fa850251b63f6c2ebbabf5651c50d0289da194`  
Canonical target: `F0012`  
Canonical claim: `operations/claims/F0012.md`  
Previous report: `research7_2026-09-17/R7-07/runs/2026-09-19/2026-09-19T091500Z__report.md` @ `678669d41572634d6671dcef6a4fab1da6cb1f79`.

## 0. Exact source and fixed metric

Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797v1 (2020), published in *Probability Surveys* 18 (2021), Section 9, Conjecture 9.5, defines `M_n` to have iid Rademacher entries and conjectures

`P(E_n) = 2^{-(1+o(1)) n^2}`,

where

`E_n = { Spec(M_n) subset Z[i] }`.

The admission-frozen metric is

`u_GI = liminf_n (-log_2 P(E_n))/n^2`.

Earlier R7-07 work proved for every `n>=1`

`P(E_n) >= 3^{floor(n/2)} 2^{-floor(n^2/2)}`,

so the source conjecture is already **REFUTED mathematically**, and the fixed interval is

`0 <= u_GI <= 1/2`.

The present run is the third and final ordinary run after STUCK2. Its prescribed methods are B11 / B21 / B28. The goal was to force a positive lower endpoint for `u_GI`, preferably `1/2`. The lower endpoint does **not** move in this artifact.

---

# 1. B11 — exact Fourier/Parseval dualization of characteristic-polynomial collisions

Fix an odd prime `p`. For a sign matrix `M`, write over `F_p`

`chi_M(t) = t^n + c_1(M)t^{n-1} + ... + c_n(M)`

and set

`c(M)=(c_1(M),...,c_n(M)) in F_p^n`.

Let

`nu_{n,p}(y)=P(c(M_n)=y)`

and

`C_{n,p}=sum_y nu_{n,p}(y)^2
         =P(c(M_n)=c(M_n'))`,

with `M_n'` independent.

## Theorem 1.1 — exact Parseval formula

With `e_p(x)=exp(2 pi i x/p)` and

`Phi_xi = E_M e_p(<xi,c(M)>)`,

one has

`C_{n,p} = p^{-n} sum_{xi in F_p^n} |Phi_xi|^2`.                 (1.1)

### Proof

For `nu=nu_{n,p}`, define its unnormalized Fourier transform

`hat nu(xi)=sum_y nu(y)e_p(<xi,y>)`.

Since `nu` is the pushforward of the uniform measure on the sign cube,

`hat nu(xi)=E_M e_p(<xi,c(M)>)=Phi_xi`.

Finite-group Parseval on `F_p^n` gives

`sum_y |nu(y)|^2 = p^{-n} sum_xi |hat nu(xi)|^2`,

which is (1.1). QED.

This identity says that the desired near-maximal order-2 entropy

`C_{n,p_n} <= 2^{-n^2+o(n^2)}`

is equivalent to showing that the total nonzero Fourier mass of the nonlinear coefficient map `M -> c(M)` is essentially minimal at quadratic scale.

## Theorem 1.2 — one-row conditional product formula

Fix a row index `i` and condition on every entry of `M` outside row `i`. For every `xi in F_p^n`, there exist coefficients

`b=b(xi,M_{-i}) in F_p`,  `a_1,...,a_n in F_p`

such that, if the random row is `x=(x_1,...,x_n) in {+1,-1}^n`,

`<xi,c(M)> = b + sum_{j=1}^n a_j x_j`.                         (1.2)

Consequently

`| E_{row i} e_p(<xi,c(M)>) |
 = product_{j=1}^n | cos(2 pi a_j/p) |`.                       (1.3)

### Proof

The coefficient `c_k(M)` is, up to sign, the sum of all `k x k` principal minors of `M`. A principal minor not using index `i` is constant under variation of row `i`. A principal minor using `i` is a determinant and therefore linear in row `i`. Hence each `c_k` is affine-linear in that row, and so is every linear combination `<xi,c(M)>`, proving (1.2).

Conditional independence of the Rademacher coordinates gives

`E_x e_p(b+sum_j a_j x_j)
 = e_p(b) product_j [ (e_p(a_j)+e_p(-a_j))/2 ]
 = e_p(b) product_j cos(2 pi a_j/p)`.

Taking absolute values yields (1.3). QED.

### What this gains and what it does not

Equation (1.3) is the exact point at which inverse Littlewood--Offord technology would have to enter. If many `a_j` stay quantitatively away from `0 mod p`, one row gives genuine Fourier contraction. But a quadratic-rate estimate would have to accumulate such contraction across `Theta(n)` rows for almost all relevant Fourier frequencies.

The obstruction is not a missing trigonometric inequality. After integrating one row, the remaining object is no longer simply a single affine phase of the next row. Repeated contraction requires a robust multistage inverse theorem controlling how the cofactor coefficient vectors reorganize under previous averaging. No such theorem is proved here.

---

# 2. B11/B21 bridge — exact Schur--Krylov reconstruction for one row/column pair

The row-affine formula has a sharper algebraic form.

Write an `n x n` matrix over a field `K` in block form

`M = [[a, r^T], [c, B]]`,

where `B` is `(n-1)x(n-1)`, `r,c in K^{n-1}`.

## Theorem 2.1 — Schur--adjugate identity

For every indeterminate `t`,

`chi_M(t) = (t-a) chi_B(t) - r^T adj(tI-B)c`.                  (2.1)

This is the determinant identity for the first row/column block of `tI-M` and holds as a polynomial identity, without assuming `tI-B` invertible.

Define the linear map

`L_{B,r}: K^{n-1} -> K[t]_{<=n-2}`,

`L_{B,r}(c)=r^T adj(tI-B)c`.

## Theorem 2.2 — rank equals Krylov dimension

`rank L_{B,r}
 = dim span{ r, B^T r, ..., (B^T)^{n-2} r }`.                 (2.2)

In particular, if `r` is cyclic for `B^T`, then `L_{B,r}` is injective. Therefore, once `B,r,a` and `chi_M` are known, the missing column `c` is uniquely determined.

### Proof

Put `m=n-1`. The adjugate has an expansion

`adj(tI-B)=sum_{k=0}^{m-1} t^{m-1-k} Q_k(B)`,

where each `Q_k(X)` is a monic polynomial of degree `k` plus lower-degree terms. This follows by multiplying by `tI-B` and matching coefficients against `chi_B(t)I`; equivalently it is the standard Faddeev--LeVerrier triangular expansion.

Hence the coefficient row-vectors of the polynomial `r^T adj(tI-B)` are

`r^T Q_0(B), ..., r^T Q_{m-1}(B)`.

Because `Q_k(B)=B^k + span{I,B,...,B^{k-1}}`, the change of basis from

`r^T, r^T B, ..., r^T B^{m-1}`

to

`r^T Q_0(B), ..., r^T Q_{m-1}(B)`

is unit triangular. The two families therefore have the same span and the same rank. Transposing identifies this rank with the right-hand side of (2.2). QED.

## The exact noncircularity failure

The theorem is strong only for an **enriched invariant**. The source event supplies `chi_M`, but not the principal submatrix `B`, not `chi_B`, and not the row `r`. If one simply sums over all choices of `B,r,a`, the count is of order

`2^{(n-1)^2+(n-1)+1}=2^{n^2-n+1}`,

which saves only `Theta(n)` bits from the full sign cube and is useless for `u_GI>0`.

Thus it would be circular to claim that cyclicity of `r` for `B^T` makes the characteristic polynomial nearly injective on sign matrices. It makes `c` reconstructible **after** exponentially much extra information has been revealed. A successful argument must compress or eliminate that extra information.

---

# 3. B21 — the imported problem is itself a fingerprint/cospectral-fiber problem

The most important outcome of the analogous-field search is that the remaining obstacle is not merely similar to a known open problem: Vu's same survey states a closely related one explicitly.

In Section 11, Conjecture 11.2 (“Finger Print”), Vu asks for the qualitative statement that almost all sign matrices are determined by their spectrum, modulo the source's “trivial permutations” convention.

The collision target needed for the corrected F0012 exponent is much stronger in the rare-tail direction. A statement that a `1-o(1)` fraction of sign matrices has only trivial cospectral mates permits an exceptional set of cardinality `o(2^{n^2})`, which may still be as large as `2^{(1-o(1))n^2}`. F0012 at exponent `1/2` requires controlling the Gaussian-integral-spectrum portion down to `2^{n^2/2+o(n^2)}` matrices.

So a proof of the desired collision estimate by “generic spectral uniqueness” would require a **quadratic-rate quantitative fingerprint theorem**, far stronger than the qualitative almost-all statement in Vu's Conjecture 11.2.

## Closest external analogues checked on 2026-09-19

1. Sean Eberhard, *The Characteristic Polynomial of a Random Matrix*, *Combinatorica* 42 (2022), 491--527, arXiv:2008.01223. Under ERH, iid sign/integer-entry matrices have irreducible characteristic polynomial and Galois group containing `A_n` with high probability. This is qualitative `1-o(1)`, not a `2^{-Theta(n^2)}` fiber/collision estimate.
2. Jennie Hansen and Eric Schmutz, *How random is the characteristic polynomial of a random matrix?*, *Math. Proc. Camb. Phil. Soc.* 114 (1993), 507--515. This supplies finite-field random-matrix characteristic-polynomial comparison, not the Bernoulli-to-growing-field transfer needed here.
3. Illya Koval and Matthew Kwan, *Exponentially Many Graphs Are Determined By Their Spectrum*, *Q. J. Math.* 75 (2024), 869--899. This advances the graph analogue but explicitly leaves the “almost all graphs” spectral-determination conjecture open.
4. Wei Wang and Da Zhao, arXiv:2509.05781 (2025), prove that almost all Erdos--Renyi graphs have no cospectral mate of each fixed level. This is again qualitative/fixed-level and does not supply a quadratic-rate matrix-fiber estimate.

A bounded current search found no theorem giving the Bernoulli characteristic-polynomial collision exponent needed here. This is negative evidence only; novelty remains **UNVERIFIED**.

---

# 4. B28 — exact unavoidable switching fibers

Before trying to prove near-injectivity, one must remove a universal source of cospectrality.

For `epsilon=(epsilon_1,...,epsilon_n) in {+1,-1}^n`, put

`D_epsilon=diag(epsilon_1,...,epsilon_n)`.

Then

`M -> D_epsilon M D_epsilon`

maps sign matrices to sign matrices and preserves the characteristic polynomial by similarity.

## Theorem 4.1 — every diagonal-switching orbit has exactly `2^{n-1}` elements

For every sign matrix `M`,

`|{D M D : D diagonal with +/-1 entries}|=2^{n-1}`.            (4.1)

### Proof

`D` and `-D` induce the same conjugation, so the orbit has size at most `2^{n-1}`.

Conversely, suppose `DMD=D'MD'`. Put `E=D'D`, again diagonal with entries `e_i in {+1,-1}`. Then `EME=M`, so for every `i,j`,

`e_i e_j M_{ij}=M_{ij}`.

Every entry `M_{ij}` is nonzero, hence `e_i e_j=1` for all `i,j`. Therefore all `e_i` are equal, so `E=I` or `E=-I`, i.e. `D'=D` or `D'=-D`. These are exactly the two representatives of the same conjugation. QED.

## Corollary 4.2 — exact collision lower bound

For every odd prime `p`,

`C_{n,p} >= 2^{-n^2+n-1}`.                                   (4.2)

### Proof

Partition the `N=2^{n^2}` sign matrices into fibers of `c(M) mod p`, with sizes `m_f`. Every nonempty fiber is a union of diagonal-switching orbits, so `m_f>=d=2^{n-1}`. Therefore

`C_{n,p}=N^{-2} sum_f m_f^2
        >=N^{-2} d sum_f m_f
        =d/N
        =2^{-n^2+n-1}`.

QED.

This improves the information-theoretic lower bound `2^{-n^2}` by the exact universal switching factor, while leaving the normalized quadratic collision exponent equal to `1`. Therefore the target

`C_{n,p_n}=2^{-n^2+o(n^2)}`

is still the strongest possible at `n^2` scale, but any fine theorem must quotient or tolerate at least these `2^{n-1}` mates.

Simultaneous coordinate permutations and transposition supply further familiar cospectral symmetries, but they are also only `2^{o(n^2)}` and do not alter the quadratic exponent. No generic stabilizer statement is needed for the present conclusion.

---

# 5. B28 — a structured-exception / small-fiber theorem that would suffice

The previous run proved the archimedean fact that if `E_n` occurs then every Gaussian-integer eigenvalue lies in

`D_n={z in Z[i]: |z|<=n}`,

and hence the number `B_n` of possible Gaussian-integral spectral multisets is

`B_n <= binom(n+(2n+1)^2-1,n)=2^{O(n log n)}`.                (5.1)

Let `A_n` be the corresponding set of admissible characteristic polynomials.

## Theorem 5.1 — structured-exception criterion

Suppose there are sets of sign matrices `S_n` and constants `sigma,tau in [0,1]` such that

`|S_n| <= 2^{(sigma+o(1))n^2}`,                               (5.2)

and, uniformly for every `f in A_n`,

`#{M notin S_n : chi_M=f} <= 2^{(tau+o(1))n^2}`.              (5.3)

Then

`u_GI >= 1-max(sigma,tau)`.                                   (5.4)

In particular, if both `sigma<=1/2` and `tau<=1/2`, then the previous explicit lower construction and (5.4) force

`u_GI=1/2`.                                                    (5.5)

### Proof

Every exceptional matrix either lies in `S_n` or belongs to one of the admissible fibers. Thus by (5.1)--(5.3),

`#E_n <= |S_n| + |A_n| max_{f in A_n} #{M notin S_n: chi_M=f}`

`     <= 2^{(sigma+o(1))n^2} + 2^{O(n log n)}2^{(tau+o(1))n^2}`

`     = 2^{(max(sigma,tau)+o(1))n^2}`.

Dividing by the ambient `2^{n^2}` sign matrices gives

`P(E_n) <= 2^{-(1-max(sigma,tau)+o(1))n^2}`,

which implies (5.4). The earlier R7-07 construction gives `u_GI<=1/2`; hence (5.5). QED.

## Why this criterion is preferable to demanding a global collision theorem

The global collision estimate from the previous run asks for near-maximal order-2 entropy across **all** characteristic polynomials. Theorem 5.1 needs small fibers only for the `2^{o(n^2)}` Gaussian-integral admissible polynomials, after isolating one structured exceptional set. Thus it is strictly more tailored to F0012.

It also gives a genuine route to **any** lower-endpoint movement: if one could prove `max(sigma,tau)<1`, then `u_GI>0` immediately.

## Sharp stress test from the refuting family

The explicit R7-07 signed-shear family contains

`3^{floor(n/2)} 2^{ceil(n^2/2)}`

distinct sign matrices with Gaussian-integral spectrum. Therefore any proposed structured set designed to absorb the whole explicit obstruction necessarily has quadratic cardinality exponent at least `1/2`.

So the threshold `sigma=1/2` in Theorem 5.1 is not an artifact: it is already saturated by the known source-refuting family up to `2^{O(n)}` factors.

---

# 6. Method outcomes

## B11 — DUALIZE

**Success:** exact Parseval identity (1.1), exact one-row Rademacher product formula (1.3), and exact Schur--Krylov reconstruction theorem (2.2).

**Failure relative to the fixed metric:** no theorem was obtained that accumulates one-row Fourier contraction across `Theta(n)` dependent stages. Revealing enough data to invoke Krylov injectivity destroys the quadratic entropy gain.

## B21 — IMPORT AN ANALOGOUS-FIELD TECHNIQUE

**Success:** the route was identified with spectral fingerprint / cospectral-fiber theory; Vu's own Conjecture 11.2 shows the qualitative version is itself open in essentially the same sign-matrix setting. The graph analogue remains difficult even for almost-all uniqueness.

**Failure relative to the fixed metric:** known qualitative irreducibility, Galois-group, controllability, and graph spectral-determination results do not provide an exceptional-set estimate of order `2^{n^2/2+o(n^2)}` or a Bernoulli characteristic-polynomial collision exponent `1`.

## B28 — STUDY THE TYPICAL CASE, THEN CLASSIFY EXCEPTIONS

**Success:** exact universal diagonal-switching fiber size `2^{n-1}`, collision lower bound (4.2), and the sufficient structured-exception theorem (5.1).

**Failure relative to the fixed metric:** no source-valid classification was proved with `max(sigma,tau)<1`; in particular, no positive lower endpoint for `u_GI` follows.

---

# 7. Fixed metric and terminal blocker

Metric before:

`u_GI in [0,1/2]`.

Metric after:

`u_GI in [0,1/2]`.

Movement: **NO MOVEMENT**.

Post-STUCK2 ordinary no-movement count:

`2 -> 3`.

HARD stuck recoveries already consumed:

`2/2`.

The exact final blocker can now be stated in either of two equivalent-strength forms at the needed scale:

1. **Fourier/collision form:** prove near-maximal order-2 entropy for the characteristic-polynomial map at one suitable growing split prime, modulo `2^{o(n^2)}` symmetries;
2. **structured-fiber form:** find `S_n` satisfying Theorem 5.1 with `max(sigma,tau)<1` for movement, and `<=1/2` for the conjectural corrected exponent.

The strongest algebraic local fact available, Schur--Krylov injectivity, becomes useful only after revealing an `(n-1)x(n-1)` block and therefore does not itself compress a characteristic-polynomial fiber.

Because this is the third ordinary unchanged run after the second and final HARD stuck recovery, the owner protocol forbids a STUCK3 cycle. F0012 must be handed off/retired from this slot and R7-07 must rotate only after a fresh shard-6 source/ownership admission.

---

# 8. Source-status distinction

- Vu Conjecture 9.5: **REFUTED mathematically** by the already-proved all-`n` signed-shear family.
- Corrected exponent `u_GI=1/2`: **OPEN / UNPROVED**.
- Novelty/prior-art status of the explicit refutation: **UNVERIFIED** despite bounded current searches; search misses are not novelty proof.
- Closure protocol: **INCOMPLETE** because independent P26 and distinct OTHER-track audits remain absent. The existing exact checks are self-checks, not independent audits.
- This artifact proves no new source closure beyond the existing refutation and does not alter shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md`.