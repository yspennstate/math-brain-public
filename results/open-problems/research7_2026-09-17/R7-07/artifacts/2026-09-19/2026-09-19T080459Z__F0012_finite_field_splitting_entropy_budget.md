Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0012 final-recovery artifact — exact finite-field splitting entropy and the many-prime budget

Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Section 9, Conjecture 9.5.  
R7 owner: `R7-07`, native ID `6aabe8413f60819197825dd81ca138ae`.  
Methods in this run: **B17** (look for the same number/shape elsewhere), **B22** (read the failures/limits of adjacent methods), **B9** (randomize the prime family).  
Frozen source metric:

\[
u_{GI}:=\liminf_{n\to\infty}\frac{-\log_2\Pr(E_n)}{n^2},
\qquad
E_n=\{\operatorname{Spec}(M_n)\subset \mathbf Z[i]\}.
\]

The previously proved source-level refutation gives

\[
0\le u_{GI}\le \frac12.
\]

This artifact does **not** move that interval. Its purpose is to quantify exactly how much information a finite-field complete-splitting test carries in the uniform matrix benchmark, and to convert the STUCK2 prime-sieve idea into a precise source-level target.

## 1. Why finite-field complete splitting is the right local event

For every rational prime `p == 1 (mod 4)`, fix a square root `i_p` of `-1` in `F_p`. Reduction modulo `p` gives a ring homomorphism

\[
\mathbf Z[i]\longrightarrow \mathbf F_p,
\qquad i\mapsto i_p.
\]

If the integer characteristic polynomial `chi_M(x)` of a sign matrix `M` splits completely over `Z[i]`, then reducing its linear factorization modulo `p` shows that `chi_M(x) mod p` splits completely over `F_p`. Thus, for

\[
S_p:=\{\chi_{M_n}(x)\bmod p\text{ splits completely over }\mathbf F_p\},
\]

we have the exact source-level implication

\[
\boxed{E_n\subseteq S_p\quad\text{for every prime }p\equiv1\pmod4.}
\tag{1.1}
\]

Consequently, for every finite set `P` of such primes,

\[
\boxed{\Pr(E_n)\le \Pr\!\left(\bigcap_{p\in P}S_p\right).}
\tag{1.2}
\]

The issue is not the implication; it is the dependence of the events `S_p` when the same `n^2` Rademacher bits generate every modular reduction.

## 2. B17: exact complete-splitting probability for a uniform matrix over `F_q`

The closest clean comparison model is a matrix chosen uniformly from `M_n(F_q)`. This model has an exact fixed-characteristic-polynomial formula due to Reiner.

For a prime power `q`, define

\[
F_q(m):=\prod_{j=1}^{m}(1-q^{-j}),\qquad F_q(0):=1,
\qquad
F_q(\infty):=\prod_{j=1}^{\infty}(1-q^{-j}).
\tag{2.1}
\]

Let `A` be uniform in `M_n(F_q)`, and let

\[
T_{n,q}:=\{\chi_A\text{ splits completely over }\mathbf F_q\}.
\]

### Theorem 2.1 — exact split probability

For every prime power `q` and every `n >= 0`,

\[
\boxed{
\Pr(T_{n,q})
=
q^{-n}F_q(n)
\sum_{\substack{(m_a)_{a\in\mathbf F_q}\in\mathbf Z_{\ge0}^{q}\\
\sum_a m_a=n}}
\prod_{a\in\mathbf F_q}F_q(m_a)^{-1}.
}
\tag{2.2}
\]

Equivalently,

\[
\Pr(T_{n,q})
=
q^{-n}F_q(n)[z^n]
\left(\sum_{m\ge0}\frac{z^m}{F_q(m)}\right)^q.
\tag{2.3}
\]

#### Proof

A monic degree-`n` polynomial splits completely over `F_q` exactly when it has the form

\[
f(x)=\prod_{a\in\mathbf F_q}(x-a)^{m_a},
\qquad m_a\ge0,\quad\sum_a m_a=n.
\tag{2.4}
\]

The multiplicity vector `(m_a)` determines `f` uniquely. Reiner's fixed-characteristic-polynomial formula states that if

\[
f=\prod_{\phi}\phi^{m_\phi}
\]

is the factorization into distinct monic irreducibles, then for uniform `A in M_n(F_q)`,

\[
\Pr(\chi_A=f)
=
q^{-n}F_q(n)
\prod_{\phi}F_{q^{\deg\phi}}(m_\phi)^{-1}.
\tag{2.5}
\]

For the polynomial (2.4), every irreducible factor is linear, so (2.5) becomes

\[
\Pr(\chi_A=f)
=
q^{-n}F_q(n)
\prod_{a\in\mathbf F_q}F_q(m_a)^{-1}.
\tag{2.6}
\]

Summing (2.6) over all weak compositions `(m_a)` of `n` into `q` parts proves (2.2), and the generating-function form (2.3) is the same sum written as a coefficient. QED.

References for (2.5): Irving Reiner, *On the number of matrices with given characteristic polynomial*, Illinois J. Math. 5 (1961), 324–329; Eric Schmutz, *Splitting Fields for Characteristic Polynomials of Matrices with Entries in a Finite Field*, which states the Reiner probability formula explicitly.

## 3. A uniform constant-factor comparison with random monic polynomials

The number of monic degree-`n` polynomials over `F_q` that split completely over `F_q` is exactly the number of multisets of `n` roots drawn from `q` field elements:

\[
N_{\mathrm{split}}(n,q)=\binom{n+q-1}{n}.
\tag{3.1}
\]

Thus a uniformly random monic degree-`n` polynomial splits completely with probability

\[
R_{n,q}:=q^{-n}\binom{n+q-1}{n}.
\tag{3.2}
\]

The following theorem shows that, for this particular extreme factorization event, the characteristic polynomial of a uniform random matrix differs from a uniform random monic polynomial by only an **absolute constant factor**, uniformly in both `n` and `q`.

### Theorem 3.1 — uniform split comparison

Let

\[
c_0:=F_2(\infty)=\prod_{j\ge1}(1-2^{-j})>0.
\]

Then for every prime power `q >= 2` and every `n >= 0`,

\[
\boxed{
c_0 R_{n,q}\le \Pr(T_{n,q})\le e^4R_{n,q}.}
\tag{3.3}
\]

Hence

\[
\boxed{
-\log_2\Pr(T_{n,q})
=
\log_2\!\frac{q^n}{\binom{n+q-1}{n}}+O(1),
}
\tag{3.4}
\]

where the `O(1)` is absolute, independent of `n` and `q`.

#### Proof

For every `m`,

\[
F_q(\infty)\le F_q(m)\le1.
\tag{3.5}
\]

There are exactly `binom(n+q-1,n)` vectors `(m_a)` in (2.2). Therefore each summand in (2.2), including the common numerator `F_q(n)`, satisfies

\[
F_q(\infty)
\le
F_q(n)\prod_aF_q(m_a)^{-1}
\le
F_q(\infty)^{-q}.
\tag{3.6}
\]

The lower endpoint in (3.6) uses `F_q(n) >= F_q(infinity)` and every reciprocal factor at least `1`. The upper endpoint uses `F_q(n)<=1` and `F_q(m_a)>=F_q(infinity)` for all `q` possible roots.

Because `F_q(infinity)` increases with `q`,

\[
F_q(\infty)\ge F_2(\infty)=c_0.
\tag{3.7}
\]

For the upper constant, use `-log(1-x)<=x/(1-x)` for `0<=x<1`:

\[
\begin{aligned}
-\log F_q(\infty)
&=\sum_{j\ge1}-\log(1-q^{-j})\\
&\le\sum_{j\ge1}\frac{q^{-j}}{1-q^{-j}}\\
&\le\frac1{1-q^{-1}}\sum_{j\ge1}q^{-j}
=\frac{q}{(q-1)^2}.
\end{aligned}
\tag{3.8}
\]

Thus

\[
F_q(\infty)^{-q}
\le
\exp\!\left(\frac{q^2}{(q-1)^2}\right)
\le e^4.
\tag{3.9}
\]

Multiplying the bounds (3.6) by `q^{-n}` and by the number of weak compositions proves (3.3). Taking base-two logarithms proves (3.4). QED.

### Novelty warning

The Reiner formula is classical, and Hansen–Schmutz explicitly study the sense in which finite-field random-matrix characteristic polynomials resemble random monic polynomials away from small factors. The simple constant-factor inequality (3.3) is a direct elementary corollary of Reiner's formula. No novelty is asserted for it.

## 4. The exact local entropy budget

Define the complete-splitting surprise in the uniform finite-field matrix model by

\[
I_{n,q}:=-\log_2\Pr(T_{n,q}).
\tag{4.1}
\]

Theorem 3.1 gives

\[
I_{n,q}
=
\log_2\!\frac{q^n}{\binom{n+q-1}{n}}+O(1).
\tag{4.2}
\]

Two regimes are particularly important.

### Corollary 4.1 — fixed field

For fixed `q`,

\[
\boxed{
I_{n,q}
=n\log_2 q-(q-1)\log_2 n+O_q(1).
}
\tag{4.3}
\]

Indeed,

\[
\binom{n+q-1}{n}
=\binom{n+q-1}{q-1}
=\frac{n^{q-1}}{(q-1)!}(1+O_q(n^{-1})).
\]

So one fixed finite field supplies only `Theta(n)` bits of complete-splitting surprise in the uniform matrix benchmark.

### Corollary 4.2 — a universal ceiling in the uniform benchmark

For all `q` and `n`,

\[
\binom{n+q-1}{n}
=
\frac{q(q+1)\cdots(q+n-1)}{n!}
\ge\frac{q^n}{n!}.
\tag{4.4}
\]

Combining (4.4) with the lower bound in (3.3) gives

\[
\Pr(T_{n,q})\ge \frac{c_0}{n!},
\]

and therefore

\[
\boxed{I_{n,q}\le\log_2(n!)-\log_2 c_0.}
\tag{4.5}
\]

Thus even when `q` is allowed to grow arbitrarily, a single complete-splitting test in the **uniform finite-field matrix benchmark** carries at most

\[
\log_2(n!) + O(1)
=
 n\log_2 n-(\log_2 e)n+O(\log n)
\tag{4.6}
\]

bits.

For `q >= n^2`, the product representation in (4.4) also gives

\[
\frac{1}{n!}
\le R_{n,q}
=\frac1{n!}\prod_{j=0}^{n-1}\left(1+\frac jq\right)
\le\frac{e^{1/2}}{n!},
\tag{4.7}
\]

so in that regime

\[
\boxed{I_{n,q}=\log_2(n!)+O(1).}
\tag{4.8}
\]

Again, all constants are absolute.

## 5. B22: what this says about the adjacent finite-field/Galois route

The closest literature found in the dated search is:

1. Hansen–Schmutz, *How random is the characteristic polynomial of a random matrix?* They prove a precise form of the heuristic that, except for small factors, the characteristic polynomial of a uniform finite-field random matrix behaves like a random monic polynomial.
2. Eberhard, *The Characteristic Polynomial of a Random Matrix*, Combinatorica 42 (2022), 491–527. For iid sign/integer-entry matrices, conditionally on ERH, the characteristic polynomial is irreducible and its Galois group contains `A_n` with high probability.
3. Cheong–Lee–Nam–Yu, *Jordan–Landau theorem for matrices over finite fields*, whose proof explicitly uses Reiner's fixed-characteristic-polynomial count and studies the number of irreducible factors.

These are structurally adjacent but do not provide the required `2^{-Theta(n^2)}` complete-splitting tail for Bernoulli matrices.

The entropy calculation above makes the scale mismatch precise in the cleanest comparison model. If one **pretended** that reductions at `k` primes were independent and each reduction behaved exactly like an independent uniform finite-field matrix, then the total complete-splitting surprise would be at most

\[
k(\log_2(n!)+O(1)).
\tag{5.1}
\]

To accumulate `delta n^2` bits for any fixed `delta>0`, even this idealized model requires

\[
\boxed{
k\ge (\delta+o(1))\frac{n}{\log_2 n}.}
\tag{5.2}
\]

For bounded `q`, (4.3) is only `Theta(n)` bits per prime, so an idealized bounded-field product would need `Omega(n)` genuinely independent-equivalent tests.

This is **not** a theorem that Bernoulli reductions obey the uniform benchmark, and it is **not** a theorem that different primes are independent. The Bernoulli matrix modulo `p` is supported only on `{+1,-1}^{n^2}`, and the same sign pattern determines every modulus. Formula (5.2) is therefore an entropy-budget calibration/no-go for a naive finite-prime argument, not a source-level probability bound.

It explains exactly what an Eberhard-style local-to-global strategy would need beyond a qualitative irreducibility theorem: a growing collection, on the order of at least `n/log n` large-prime-equivalent tests (or `n` bounded-prime-equivalent tests), together with quantitative control of their dependence on the common Bernoulli input at the full quadratic information scale.

## 6. B9: randomizing the prime family gives an exact averaged sieve target

The prime family need not be deterministic.

### Lemma 6.1 — randomized prime-family reduction

Let `mu_n` be any probability distribution on finite sets `P` of rational primes congruent to `1 mod 4`. Then

\[
\boxed{
\Pr(E_n)
\le
\mathbf E_{P\sim\mu_n}
\Pr\!\left(\bigcap_{p\in P}S_p\right).
}
\tag{6.1}
\]

#### Proof

For every deterministic `P`, (1.1) gives the pointwise indicator inequality

\[
1_{E_n}(M)\le \prod_{p\in P}1_{S_p}(M).
\]

Taking expectation over the Bernoulli matrix first gives (1.2). Taking expectation over `P~mu_n` preserves the inequality and yields (6.1). QED.

This matters because a large-sieve argument may be much easier in average over a random set of primes than for one adversarially fixed set. In particular, the following would immediately move the frozen source metric.

### Corollary 6.2 — exact source-movement criterion

If there exist distributions `mu_n` and a fixed `delta>0` such that

\[
\mathbf E_{P\sim\mu_n}
\Pr\!\left(\bigcap_{p\in P}S_p\right)
\le
2^{-(\delta+o(1))n^2},
\tag{6.2}
\]

then

\[
\boxed{u_{GI}\ge\delta.}
\tag{6.3}
\]

Together with R7-07's explicit all-`n` shear family, that would give

\[
\delta\le u_{GI}\le\frac12.
\]

The proof is immediate from (6.1), then taking `-log_2`, dividing by `n^2`, and passing to the liminf.

## 7. Ordered-prime chain formulation

For an ordered list `p_1,...,p_k`, define

\[
Q_j:=\Pr\!\left(S_{p_j}\mid \bigcap_{i<j}S_{p_i}\right),
\]

whenever the conditioning event has positive probability. The exact chain rule gives

\[
\Pr\!\left(\bigcap_{j=1}^kS_{p_j}\right)=\prod_{j=1}^kQ_j.
\tag{7.1}
\]

Hence if one can prove, for some ordered prime family,

\[
Q_j\le2^{-\eta_{n,j}},
\]

then

\[
\boxed{
\Pr(E_n)
\le
2^{-\sum_j\eta_{n,j}},
\qquad
u_{GI}\ge
\liminf_n\frac{\sum_j\eta_{n,j}}{n^2}.
}
\tag{7.2}
\]

This is the exact quantitative form of the missing dependence theorem.

If `k` is chosen on the benchmark-critical scale `k asymp n/log n`, then quadratic source movement requires average conditional surprise of order `n log n` bits per prime. That is essentially the **maximum** complete-splitting surprise available per prime in the uniform finite-field benchmark by (4.5). Thus the critical-scale many-prime program has almost no room for dependence loss: at `k~n/log n`, a constant-factor collapse in per-prime information directly reduces the attainable quadratic exponent.

Choosing more primes may be more robust. For example, `k~n` allows only `Theta(n)` average conditional surprise per prime, the same scale as fixed-field complete splitting in (4.3). The price is that one must control dependence across a linearly growing prime family determined by the same Bernoulli input.

## 8. A second obstruction: CRT does not create new entrywise randomness

It is tempting to argue that reductions modulo distinct primes should become independent because of the Chinese remainder theorem. That is false for the present input distribution.

For a fixed sign entry `epsilon in {+1,-1}`, the entire residue vector

\[
(\epsilon\bmod p)_{p\in P}
\]

contains exactly one input bit, regardless of the number or product of the primes. Entrywise CRT therefore does not manufacture independent modular samples. Across the whole matrix there are exactly `n^2` input bits, and all modular splitting events are deterministic functions of those same bits.

This does not rule out a large-sieve theorem: different arithmetic tests can extract different information from the same bits. But it means any proof must establish **conditional anti-concentration of the splitting constraints**, not merely invoke CRT or multiply one-prime probabilities.

## 9. Why repeated-root exceptional families cannot be discarded

A source-valid sieve must include matrices whose characteristic polynomial has repeated roots. R7-07's explicit Gaussian-integral-spectrum family already contains highly nongeneric triangular/block-triangular structures, and the nilpotent subfamilies have characteristic polynomial `x^n`. Therefore a proof that first conditions on nonzero discriminant or simple spectrum and never controls the discarded part would be circular/incomplete for F0012.

This is another difference from typical-Galois arguments, where the repeated-root or reducible set may be negligible for proving a `1-o(1)` statement. Here the entire desired exceptional event itself lives at exponentially small scale, and structured repeated-root strata can contribute at the candidate leading exponent `1/2`.

## 10. What was gained and what remains

### B17 outcome

**Success, but no source-metric movement.** Reiner's theorem gives an exact formula for complete splitting of a uniform finite-field random matrix. It implies the absolute comparison

\[
\Pr(T_{n,q})=\Theta(1)\,q^{-n}\binom{n+q-1}{n}
\]

uniformly in `n,q`, with explicit constants `c_0` and `e^4`. This identifies the local information scale exactly.

### B22 outcome

**Success as a route diagnosis.** The uniform benchmark proves that a bounded number or even `o(n/log n)` independent large-prime-equivalent splitting tests cannot accumulate a quadratic number of bits. Existing qualitative irreducibility/Galois results do not by themselves address this scale. The missing theorem must be a many-prime quantitative dependence estimate, not another one-prime factorization statement.

### B9 outcome

**Success as an exact source-level reduction, no probability estimate yet.** Randomizing the prime family is legitimate and yields (6.1). It suffices to prove an average joint splitting bound (6.2); no deterministic prime set has to be selected in advance. The hard part remains controlling the joint Bernoulli splitting probability.

### Frozen source metric

Before:

\[
0\le u_{GI}\le\frac12.
\]

After:

\[
0\le u_{GI}\le\frac12.
\]

**NO SOURCE-METRIC MOVEMENT.** This is ordinary no-movement run 1 of the final post-STUCK2 recovery cycle.

## 11. Next attack forced by the entropy budget

The next three nonrepeating Section-B methods should be:

- **B30 — one prime, one scale, one direction at a time:** work on primes in one dyadic window, preferably on the scale where the uniform benchmark contributes `Theta(n log n)` bits, and determine an actual Bernoulli conditional split bound rather than mixing prime regimes.
- **B25 — count the same thing twice:** count pairs `(M,P)` where `M` is a sign matrix and all primes in `P` split `chi_M`, once by matrices and once by prime sets/factorization types. This is the natural form for exploiting the randomized reduction (6.1).
- **B3 — prove something stronger:** target a uniform averaged large-sieve inequality for all sign matrices outside an explicitly classified structured family; if the structured family itself has at most `2^{(1-delta)n^2}` elements, the two pieces combine into source movement.

The first quantitative milestone is deliberately weaker than the conjectured corrected exponent `1/2`: prove **any** fixed `delta>0` in (6.2). That would be the first lower-endpoint movement of `u_GI` and would turn the current interval `[0,1/2]` into `[delta,1/2]`.

## 12. Dated literature/source notes

Checked 2026-09-19:

- Van H. Vu, arXiv:2005.02797. The arXiv record still exposes only `v1`, submitted 2020-05-06. R7-07's explicit shear family refutes Conjecture 9.5 as stated, but novelty of that refutation remains **UNVERIFIED** pending a broader prior-art process and independent audits.
- Sean Eberhard, arXiv:2008.01223 / *Combinatorica* 42 (2022), 491–527. The current arXiv version is `v2` (2021-08-13); the theorem is conditional on ERH and gives irreducibility / Galois group containing `A_n` with high probability, not a quadratic rare-event exponent.
- Jennie C. Hansen and Eric Schmutz, *How random is the characteristic polynomial of a random matrix?*, Math. Proc. Cambridge Philos. Soc. 114 (1993), 507–515.
- Irving Reiner, *On the number of matrices with given characteristic polynomial*, Illinois J. Math. 5 (1961), 324–329.
- Gilyoung Cheong, Jungin Lee, Hayan Nam, Myungjun Yu, *Jordan–Landau theorem for matrices over finite fields*, Linear Algebra Appl. 655 (2022), 100–128.

No bounded search hit was treated as proof of novelty or openness. The exact finite-field formula in this artifact is classical/Reiner-derived; the source-level many-prime Bernoulli estimate remains unproved.
