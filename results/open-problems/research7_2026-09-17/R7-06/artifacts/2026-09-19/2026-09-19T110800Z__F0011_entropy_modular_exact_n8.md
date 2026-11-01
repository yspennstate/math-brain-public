# F0011 / Vu integral-spectrum conjecture — spectrum-entropy reduction, modular splitting certificates, and exact n=8 classification

Date: 2026-09-19 UTC  
Slot: `R7-06`  
Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4 (Integral spectrum).  
Status: **PARTIAL**. The source asymptotic conjecture is not proved here.

Let `M=M_n^sym` be a symmetric `n x n` matrix with entries in `{+1,-1}`. Under the random model, the upper-triangular entries are independent Rademacher signs. The source asks whether

`P(Spec(M_n^sym) subset Z) = 2^{-(1/2+o(1)) n^2}`.

From the preceding R7-06 run we use two proved facts only:

1. diagonal sign switching `M -> D M D` is free modulo `+/- I` and gives a unique representative with first-row off-diagonal entries all `+1`;
2. if the spectrum is integral, then all eigenvalues are even for even `n`, while for odd `n` exactly one eigenvalue is odd.

Write `I_n` for the number of switching-normalized integral-spectrum representatives. Then Vu's conjecture is equivalent to `I_n=2^{o(n^2)}`.

## B25 — count the same thing twice: the spectrum itself has only linear entropy

For an integral spectrum `lambda=(lambda_1,...,lambda_n)`, counted as an unordered multiset, we have

`sum_i lambda_i^2 = tr(M^2)=n^2`.

Let `S_n` be the set of all integral multisets that can possibly occur. We do not need to know which members of `S_n` are realizable.

### Theorem 1 (only exponentially many candidate integral spectra)

`|S_n| <= 2^n p(n^2) <= exp(C n)`

for an absolute constant `C`, where `p(N)` is the integer partition function.

#### Proof

Forget the signs of the nonzero eigenvalues. The multiset of squares `lambda_i^2`, with zeros omitted, is a partition of `n^2` into square parts, hence certainly one of the `p(n^2)` unrestricted partitions of `n^2`.

Fix the multiplicities `m_a` of each positive absolute value `a`. There are exactly `m_a+1` ways to choose how many of the `m_a` copies receive the positive sign. Therefore the number of sign refinements is at most

`prod_a (m_a+1) <= prod_a 2^{m_a} <= 2^n`.

It remains to give a self-contained exponential-in-`n` bound on `p(n^2)`. For `N>=1`, put `x=exp(-1/sqrt(N))`. Euler's generating function gives

`p(N) x^N <= prod_{k>=1} (1-x^k)^{-1}`.

Taking logarithms,

`log prod_{k>=1}(1-x^k)^{-1}
 = sum_{m>=1} (1/m) x^m/(1-x^m)
 = sum_{m>=1} 1/[m(e^{m/sqrt(N)}-1)]`.

Since `e^y-1 >= y`, this is at most

`sqrt(N) sum_{m>=1} 1/m^2 = (pi^2/6) sqrt(N)`.

Also `x^{-N}=exp(sqrt(N))`. Hence

`p(N) <= exp((1+pi^2/6)sqrt(N))`.

Taking `N=n^2` proves the theorem. ∎

For a candidate integral spectrum `lambda`, let `F_n(lambda)` be the number of switching-normalized sign matrices with exactly that spectrum. Then

`I_n = sum_{lambda in S_n} F_n(lambda)`.

### Corollary 1.1 (single-fiber reformulation)

Vu Conjecture 9.4 is equivalent to

`max_lambda F_n(lambda) = 2^{o(n^2)}`.

Indeed `max F_n <= I_n`, while Theorem 1 gives

`I_n <= exp(C n) max_lambda F_n(lambda)`.

Thus **all possible quadratic entropy is inside one cospectral switching fiber; choosing the integer spectrum itself costs only `O(n)` bits**. This is stronger localization than the earlier reduction `I_n=2^{o(n^2)}`.

A related deterministic observation is that an integral spectrum has only `O(n^{2/3})` distinct eigenvalues: among `r` distinct integers, the sum of their squares is `Omega(r^3)`, while the full spectrum has square sum exactly `n^2`. This alone is not enough, because a single repeated-eigenvalue fiber can still be large.

## B30 — one prime at a time: exact splitting criterion and the CRT obstruction

The previous run observed that integrality forces the characteristic polynomial to split over every finite field. The following form avoids polynomial factorization entirely.

### Theorem 2 (matrix criterion for complete splitting mod p)

Let `A` be any `n x n` matrix over `F_p`. Then its characteristic polynomial splits completely into linear factors over `F_p` if and only if

`(A^p-A)^n = 0` in `M_n(F_p)`.

#### Proof

Work over an algebraic closure. If `lambda` is an eigenvalue of `A`, then `lambda^p-lambda` is an eigenvalue of `A^p-A`. Thus if `A^p-A` is nilpotent, every eigenvalue satisfies `lambda^p=lambda`, so every eigenvalue lies in `F_p`; the characteristic polynomial splits over `F_p`.

Conversely, suppose the characteristic polynomial splits over `F_p`. In Jordan form every block is `J=lambda I+N` with `lambda in F_p` and nilpotent `N`. The polynomial `f(x)=x^p-x` vanishes at `lambda`; hence `f(J)` is a polynomial in `N` with zero constant term, so it is nilpotent. Therefore `A^p-A` is nilpotent. Every nilpotent `n x n` matrix has nth power zero. ∎

This gives an exact arithmetic rejection certificate: if `(M^p-M)^n != 0 mod p` for one prime, then `M` cannot have integral spectrum.

### Why a fixed number of primes does not automatically give the n^2 exponent

There are only

`binom(n+p-1,p-1)`

monic degree-`n` polynomials that split completely over a fixed `F_p`, because such a polynomial is a multiset of `n` roots chosen from `p` field elements. For fixed `p` this is polynomial in `n`, whereas there are `p^n` monic degree-`n` polynomials over `F_p`. Thus even in an idealized uniform-polynomial benchmark, one fixed prime supplies only `Theta(n)` bits of rarity, not `Theta(n^2)`.

More importantly, the reductions of one `{+/-1}` matrix modulo different odd primes are not independent random matrices: they are deterministic images of the same sign pattern. Hence multiplying fixed-prime splitting probabilities is unjustified. This is the precise CRT-gluing obstruction that a multi-prime proof must overcome.

The 2023 Ferber-Jain-Sah-Sawhney theorem gives sharp rank information over `F_p` for a wide range of primes and, conditionally on ERH, high-probability irreducibility of the characteristic polynomial. That technology is highly relevant to finite-field root counts, but it does not provide the cross-prime independence or cospectral-fiber entropy bound needed for Vu's `n^2/2` exponent.

## B28 — replace “for all” by “for typical”: exact n=8 quotient and modular anatomy

A direct `n=8` switching-normalized enumeration has `2^29=536,870,912` matrices. A second exact quotient makes it small enough to classify without floating-point eigenvalues.

After switching normalization, the off-diagonal signs among coordinates `2,...,n` form a `{+/-1}` symmetric zero-diagonal pattern. Interpret `+1` as an edge and `-1` as a nonedge of a graph on `n-1` vertices. Permuting coordinates `2,...,n` preserves the spectrum. Thus, for `n<=8`, we may enumerate the complete graph atlas of unlabeled graphs on at most seven vertices.

For an unlabeled graph `G`, the number of labeled residual sign patterns in its orbit is exactly

`(n-1)! / |Aut(G)|`.

For every `G` we enumerate all `2^n` diagonal sign patterns. The checker independently asserts that the sum of these orbit weights is exactly

`2^{n + binom(n-1,2)}`,

the complete switching-normalized sample space.

For each matrix, candidate integral spectra are generated from the necessary conditions

- `|lambda_i|<=n`,
- `sum lambda_i^2=n^2`,
- the exact mod-2 parity theorem,
- the trace constraint.

The checker computes the integer traces `tr(M^k)` for `1<=k<=n`. Newton identities imply that equality of those power sums with a candidate spectrum is equality of the complete characteristic polynomial. No floating eigensolver is used.

### Theorem 3 (exact classification through n=8)

The switching-normalized integral counts are

| n | normalized total | integral `I_n` | realized integral spectra | exact probability |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 1 |
| 2 | 4 | 2 | 2 | 1/2 |
| 3 | 16 | 10 | 6 | 5/8 |
| 4 | 128 | 10 | 5 | 5/64 |
| 5 | 2,048 | 154 | 14 | 77/1024 |
| 6 | 65,536 | 274 | 14 | 137/32768 |
| 7 | 4,194,304 | 15,446 | 44 | 7723/2097152 |
| 8 | 536,870,912 | **111,290** | **33** | **55645/268435456** |

Thus among all `2^36=68,719,476,736` symmetric `8 x 8` sign matrices, exactly

`111,290 * 2^7 = 14,245,120`

have integral spectrum.

At `n=8`, the largest switching-normalized cospectral fiber has size **24,360**. By number `r` of distinct eigenvalues, the exact integral count is

| r | normalized integral matrices | realized spectra | largest fiber |
|---:|---:|---:|---:|
| 2 | 4 | 4 | 1 |
| 3 | 2,366 | 11 | 630 |
| 4 | 5,740 | 6 | 2,520 |
| 5 | 103,180 | 12 | 24,360 |

Hence about 92.7% of the integral normalized `n=8` matrices have **five** distinct eigenvalues. The finite exceptional set is not dominated by the rank-one family or by two-eigenvalue sporadics.

### Theorem 4 (small-prime splitting certificates through n=8)

For `n<=7`, simultaneous complete splitting modulo `3,5,7` is **exactly equivalent** to integral spectrum within the complete switching-normalized census. The counts are

| n | split mod 3 | split mod 5 | split mod 7 | split mod 3&5 | split mod 3&5&7 = `I_n` |
|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 2 | 2 |
| 2 | 2 | 2 | 4 | 2 | 2 |
| 3 | 10 | 10 | 10 | 10 | 10 |
| 4 | 50 | 34 | 24 | 10 | 10 |
| 5 | 274 | 308 | 314 | 154 | 154 |
| 6 | 6,226 | 4,126 | 5,346 | 1,666 | 274 |
| 7 | 166,198 | 69,192 | 115,642 | 16,566 | 15,446 |

At `n=8` the triple `{3,5,7}` is no longer sufficient: it leaves **190,250** matrices, versus `I_8=111,290`. This is the first failure in the exact census.

Testing the prime set `{3,5,7,11,13}` gives a sharper fact. No two-prime subset of this set characterizes integrality at `n=8`, but each of

`{3,5,13}`, `{3,7,13}`, `{5,7,13}`, `{5,11,13}`

leaves **exactly 111,290** matrices. Since every integral-spectrum matrix necessarily survives every prime splitting test, equality of the exact counts proves equality of the sets. For comparison, `{7,11,13}` leaves `111,306`, exactly sixteen false positives.

This finite behavior suggests a potentially useful asymptotic direction — grow a carefully chosen set of primes while controlling the common matrix fibers — but it does **not** justify independence or an asymptotic product estimate.

## Literature positioning checked 2026-09-19

- Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / Probability Surveys 18 (2021), Conjecture 9.4.
- K. Costello and P. Williams, *On the number of integral graphs*, Linear Algebra Appl. 493 (2016), 447–454, DOI 10.1016/j.laa.2015.11.027: upper proportion `2^{-c n^{3/2}}`; the authors explicitly describe the likely correct exponent as proportional to `n^2`.
- A. Ferber, V. Jain, A. Sah, M. Sawhney, *Random symmetric matrices: rank distribution and irreducibility of the characteristic polynomial*, Math. Proc. Cambridge Philos. Soc. 174 (2023), 233–246, DOI 10.1017/S0305004122000226: finite-field rank distribution and ERH-conditional high-probability irreducibility.
- Yi Han, *On the rank of a random symmetric matrix in the large-deviation regime*, J. London Math. Soc. 113 (2026), e70581, first published 2026-05-30, DOI 10.1112/jlms.70581: `exp(-c'kn)` corank large deviations for `k<=c sqrt(n)`.

A bounded current search on 2026-09-19 did not locate a later source claiming Vu's `2^{-(1/2+o(1))n^2}` asymptotic. This is negative evidence only, not a proof of openness or novelty.

## What is genuinely moved and what remains open

The frozen finite metric moves from `N_exact=7` to **`N_exact=8`**.

The source-level gap is still the upper bound `I_n=2^{o(n^2)}`. The strongest conceptual reduction from this run is the equivalent single-fiber statement

`max_lambda F_n(lambda)=2^{o(n^2)}`.

The modular experiments expose a useful exact finite phenomenon and a precise failure mode for naive prime multiplication, but they do not yet control those cospectral fibers asymptotically. No P26 audit, distinct OTHER-track audit, or source-closure package is claimed.