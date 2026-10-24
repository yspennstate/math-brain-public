Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0012 final recovery 2 — archimedean restriction turns the many-prime split sieve into a one-prime collision-entropy target

Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.5. For the iid nonsymmetric Rademacher matrix `M_n`, let

\[
E_n=\{\operatorname{Spec}(M_n)\subset \mathbf Z[i]\}.
\]

The source conjectures `P(E_n)=2^{-(1+o(1))n^2}`. R7-07 has already refuted that exponent by an explicit all-`n` family and proved

\[
\Pr(E_n)\ge 3^{\lfloor n/2\rfloor}2^{-\lfloor n^2/2\rfloor},
\]

so the frozen source metric

\[
u_{GI}:=\liminf_{n\to\infty}\frac{-\log_2\Pr(E_n)}{n^2}
\]

currently satisfies `0 <= u_GI <= 1/2`.

This note does **not** move that interval. It develops the post-STUCK2 source-level recovery with methods **B30 / B25 / B3** and isolates a sharp single-prime theorem which would prove the corrected exponent `u_GI=1/2`.

## 1. B30 — one prime, one scale: use the archimedean spectral restriction before reducing mod p

The preceding run used only the implication

\[
E_n\Longrightarrow \chi_{M_n}\text{ splits completely over }\mathbf F_p
\]

for every `p=1 (mod 4)`. That discards a large amount of information: a Gaussian-integral eigenvalue of a sign matrix is not an arbitrary element of `F_p`; it has small complex modulus.

### Lemma 1.1 — spectral energy bound

For every real or complex `n x n` matrix `M` with eigenvalues `lambda_1,...,lambda_n`,

\[
\sum_{j=1}^n |\lambda_j|^2\le \|M\|_F^2.
\]

In particular, if `M` is a sign matrix, then

\[
\sum_{j=1}^n |\lambda_j|^2\le n^2,
\qquad |\lambda_j|\le n.
\tag{1.1}
\]

#### Proof

Take a complex Schur decomposition `M=UTU^*`, with `U` unitary and `T` upper triangular. The diagonal of `T` is the eigenvalue multiset. Frobenius norm is unitarily invariant, hence

\[
\|M\|_F^2=\|T\|_F^2
=\sum_j|\lambda_j|^2+\sum_{a<b}|T_{ab}|^2
\ge \sum_j|\lambda_j|^2.
\]

For a sign matrix there are `n^2` entries of modulus one, so `||M||_F^2=n^2`. QED.

Define the Gaussian lattice disk

\[
D_n:=\{z\in\mathbf Z[i]:|z|\le n\},
\qquad L_n:=|D_n|.
\]

Trivially

\[
L_n\le (2n+1)^2=O(n^2).
\tag{1.2}
\]

### Lemma 1.2 — one large split prime sees every admissible Gaussian root distinctly

Let `p=1 (mod 4)` and choose `r in F_p` with `r^2=-1`. Let

\[
\rho_{p,r}:\mathbf Z[i]\to\mathbf F_p,
\qquad a+bi\mapsto a+br.
\]

If `p>4n^2`, then `rho_{p,r}` is injective on `D_n`.

#### Proof

The kernel is the Gaussian prime ideal `mathfrak p=(p,i-r)` of norm `p`. If distinct `z,w in D_n` had the same image, then `0 != z-w in mathfrak p`, so `p` divides the integer norm `N(z-w)=|z-w|^2`. But

\[
0<|z-w|^2\le (|z|+|w|)^2\le4n^2<p,
\]

a contradiction. QED.

Let

\[
A_{n,p}:=\rho_{p,r}(D_n)\subset\mathbf F_p.
\]

For `p>4n^2`, `|A_{n,p}|=L_n=O(n^2)`.

### Corollary 1.3 — archimedean-strengthened modular necessary condition

For every sign matrix `M` and every `p=1 (mod 4)` with `p>4n^2`,

\[
E_n\Longrightarrow
\chi_M(x)\bmod p
=\prod_{j=1}^n(x-a_j)
\quad\text{with every }a_j\in A_{n,p}.
\tag{1.3}
\]

Thus the relevant modular event is not generic complete splitting over all `p` residues. It is complete splitting over only `O(n^2)` allowed residues.

### Uniform finite-field benchmark for a restricted root set

Let `q` be a prime power, let `A subset F_q` have size `m`, and let `X` be uniform in `M_n(F_q)`. Write

\[
T_{n,q}(A)=\{\chi_X\text{ has all its roots in }A\}.
\]

Set

\[
F_q(k)=\prod_{j=1}^k(1-q^{-j}),\qquad F_q(0)=1,
\qquad c_0:=\prod_{j\ge1}(1-2^{-j})>0.
\]

The Reiner fixed-characteristic-polynomial formula used in the preceding run gives exactly

\[
\Pr(T_{n,q}(A))
=q^{-n}F_q(n)
\sum_{\substack{(m_a)_{a\in A}\\\sum_a m_a=n}}
\prod_{a\in A}F_q(m_a)^{-1}.
\tag{1.4}
\]

Since the number of weak `m`-part compositions of `n` is `binom(n+m-1,n)`, and because `m<=q`, the same argument as in the preceding run yields the absolute comparison

\[
\boxed{
 c_0 q^{-n}\binom{n+m-1}{n}
 \le
 \Pr(T_{n,q}(A))
 \le
 e^4 q^{-n}\binom{n+m-1}{n}.
}
\tag{1.5}
\]

The important change is `m=O(n^2)` instead of `m=q`.

If `p_n=1 (mod 4)` satisfies

\[
\log_2 p_n=\alpha n+o(n),\qquad \alpha>0,
\]

then with `A=A_{n,p_n}`,

\[
\log_2\binom{n+L_n-1}{n}=O(n\log n),
\]

and therefore the **uniform finite-field** benchmark is

\[
\boxed{
-\log_2\Pr(T_{n,p_n}(A_{n,p_n}))
=\alpha n^2+O(n\log n)+o(n^2).
}
\tag{1.6}
\]

So once the archimedean restriction is retained, a *single* exponentially large split prime already has a quadratic information budget in the uniform finite-field model. The previous conclusion that one needs about `n/log n` large-prime complete-splitting tests was a statement about the deliberately weaker event “splits somewhere in all of `F_p`”; it is not a barrier for the source event.

This is the main B30 correction.

## 2. B25 — count the source event through characteristic-polynomial atoms and collisions

Let `G_n` denote the set of multisets of `n` Gaussian integers all lying in `D_n`. The energy bound (1.1) cuts this set down further, but the crude disk bound is already enough:

\[
|G_n|\le B_n:=\binom{n+L_n-1}{n}
=2^{O(n\log n)}.
\tag{2.1}
\]

For a prime `p=1 (mod 4)`, define the characteristic-polynomial distribution

\[
\nu_{n,p}(f)
:=\Pr(\chi_{M_n}\equiv f\pmod p),
\]

over monic degree-`n` polynomials in `F_p[x]`. Let

\[
H_{n,p}:=\max_f\nu_{n,p}(f)
\tag{2.2}
\]

and let the collision probability be

\[
C_{n,p}
:=\sum_f\nu_{n,p}(f)^2
=\Pr(\chi_{M_n}\equiv\chi_{M_n'}\pmod p),
\tag{2.3}
\]

where `M_n,M_n'` are independent Rademacher matrices.

### Theorem 2.1 — exact one-prime atom/collision reduction

For every `p=1 (mod 4)` with `p>4n^2`,

\[
\boxed{
\Pr(E_n)\le B_n H_{n,p}
}
\tag{2.4}
\]

and

\[
\boxed{
\Pr(E_n)\le \sqrt{B_n C_{n,p}}.
}
\tag{2.5}
\]

#### Proof

By Corollary 1.3, the reduction of the characteristic polynomial of any matrix in `E_n` belongs to the set `S_{n,p}` of reductions of polynomials whose `n` roots form a multiset in `D_n`. Hence

\[
|S_{n,p}|\le |G_n|\le B_n.
\]

Therefore

\[
\Pr(E_n)
\le\sum_{f\in S_{n,p}}\nu_{n,p}(f)
\le B_nH_{n,p},
\]

which is (2.4). Cauchy-Schwarz gives

\[
\left(\sum_{f\in S_{n,p}}\nu_{n,p}(f)\right)^2
\le |S_{n,p}|\sum_f\nu_{n,p}(f)^2
\le B_n C_{n,p},
\]

proving (2.5). QED.

### Corollary 2.2 — two direct source-metric milestones

Because `log_2 B_n=O(n log n)=o(n^2)`, either of the following would move the frozen source metric:

1. If for some prime sequence `p_n=1 (mod 4)`, `p_n>4n^2`,
   \[
   H_{n,p_n}\le2^{-(\delta+o(1))n^2},
   \]
   then `u_GI>=delta`.

2. If
   \[
   C_{n,p_n}\le2^{-(2\delta+o(1))n^2},
   \]
   then `u_GI>=delta`.

In particular the sharp collision target

\[
\boxed{
C_{n,p_n}\le2^{-n^2+o(n^2)}
}
\tag{2.6}
\]

would imply

\[
u_{GI}\ge\frac12,
\]

and the already-proved R7-07 construction would then give the corrected exponent

\[
\boxed{u_{GI}=\frac12.}
\tag{2.7}
\]

The target (2.6) is information-theoretically sharp. The map `M -> chi_M mod p` starts from only `2^{n^2}` equally likely sign matrices, so every image distribution satisfies

\[
C_{n,p}\ge2^{-n^2}.
\tag{2.8}
\]

Thus (2.6) asks for asymptotically maximal order-2 entropy of the characteristic polynomial, not an artificially stronger exponent.

The explicit R7-07 exceptional family is also compatible with this sharpness: from `P(E_n)>=2^{-n^2/2+O(n)}` and `|S_{n,p}|<=2^{O(n log n)}`, Cauchy-Schwarz in the reverse direction gives

\[
C_{n,p}\ge \frac{\Pr(E_n)^2}{B_n}
=2^{-n^2-O(n\log n)}.
\tag{2.9}
\]

So the candidate collision exponent `1` is simultaneously the information-theoretic floor and the scale forced by the known half-entropy exceptional construction.

This is the main B25 reduction.

## 3. B3 — prove the stronger collision-entropy statement; exact uniform-matrix benchmark

The strongest clean formulation suggested by Section 2 is no longer “control many modular splitting events.” It is:

> **Single-prime collision theorem sought.** Find split primes `p_n>4n^2` for which the Rademacher characteristic polynomial has collision entropy
> \[
> H_2(\chi_{M_n}\bmod p_n)
> :=-\log_2 C_{n,p_n}
> =n^2-o(n^2).
> \]

This theorem is stronger than what is needed for a positive lower endpoint and exactly strong enough for the corrected `1/2` exponent.

The corresponding theorem is elementary for a **uniform finite-field matrix**, which provides a sharp benchmark and isolates the only missing transfer.

### Proposition 3.1 — uniform finite-field characteristic polynomials have almost maximal collision entropy when `q >> n`

Let `X` be uniform in `M_n(F_q)` and let `nu^unif_{n,q}` be the distribution of `chi_X`. If `q>=2`, then for every monic degree-`n` polynomial `f`,

\[
\nu^{\rm unif}_{n,q}(f)
\le
q^{-n}\exp\!\left(\frac{4n}{q-1}\right).
\tag{3.1}
\]

Consequently

\[
\boxed{
q^{-n}
\le
\sum_f \nu^{\rm unif}_{n,q}(f)^2
\le
q^{-n}\exp\!\left(\frac{4n}{q-1}\right).
}
\tag{3.2}
\]

In particular, if `log_2 q=n+o(n)` then

\[
-\log_2\sum_f \nu^{\rm unif}_{n,q}(f)^2
=n^2+o(n^2).
\tag{3.3}
\]

#### Proof

Write

\[
f=\prod_\phi \phi^{m_\phi}
\]

as a product over distinct monic irreducibles, with `d_phi=deg phi`. Reiner's formula gives

\[
\nu^{\rm unif}_{n,q}(f)
=q^{-n}F_q(n)
\prod_\phi F_{q^{d_\phi}}(m_\phi)^{-1}.
\]

Discard `F_q(n)<=1`. For `x in (0,1)`, `-log(1-x)<=x/(1-x)`. Hence

\[
-\log F_{q^d}(m)
\le
\sum_{j\ge1}\frac{q^{-dj}}{1-q^{-dj}}
\le
\frac{q^{-d}}{(1-q^{-d})^2}
\le4q^{-d}.
\]

There are at most `n/d` distinct degree-`d` irreducibles occurring in `f`, because their total degree is `n`. Therefore

\[
\log\prod_\phi F_{q^{d_\phi}}(m_\phi)^{-1}
\le
4n\sum_{d\ge1}\frac{q^{-d}}d
=4n[-\log(1-q^{-1})]
\le\frac{4n}{q-1}.
\]

This proves (3.1). Since there are exactly `q^n` monic degree-`n` polynomials, Cauchy-Schwarz gives the lower collision bound `q^{-n}`. The upper collision bound follows from

\[
\sum_f\nu(f)^2\le(\max_f\nu(f))\sum_f\nu(f)=\max_f\nu(f).
\]

QED.

### What is genuinely missing

For `q` exponentially large in `n`, Proposition 3.1 says the uniform matrix benchmark has precisely the collision exponent required in (2.6). But a Rademacher matrix modulo such a prime is **not** entrywise close to uniform: each entry still has only the two residues `+1,-1`.

Existing finite-field universality results, including Luh–Meehan–Nguyen for rank/eigenvalue-free/fixed-irreducible-divisibility statistics, operate in regimes and observables far weaker than exponential-prime, full-characteristic-polynomial collision entropy. Eberhard's theorem for iid sign matrices gives conditional high-probability irreducibility and large Galois group, but again does not provide a `2^{-Theta(n^2)}` collision tail.

So the missing theorem is now sharply stated:

\[
\boxed{
\Pr\big(\chi_{M_n}\equiv\chi_{M_n'}\pmod {p_n}\big)
\le2^{-n^2+o(n^2)}
}
\tag{3.4}
\]

for some split prime sequence `p_n>4n^2` (an exponential scale is the natural uniform benchmark, but (2.5) itself only needs `p_n>4n^2`).

A naive CRT argument on the matrix entries cannot establish (3.4): for every odd prime, reduction of the **entry vector** `{+1,-1}^{n^2}` is already injective. Any entropy gain must therefore be proved after the nonlinear map `M -> chi_M`, not by pretending that different prime reductions create independent entry randomness.

## 4. Outcomes of the three required methods

- **B30 — one prime, one scale, one direction:** SUCCESSFUL REFORMULATION. Retaining the archimedean eigenvalue bound strengthens “splits over F_p” to “all roots lie in an O(n^2)-point residue set.” A single exponential split prime has quadratic information in the uniform benchmark.
- **B25 — count the same thing twice:** SUCCESSFUL REDUCTION. The source event is bounded by both a max characteristic-polynomial atom and the square root of characteristic-polynomial collision probability. The sharp collision target is exactly `2^{-n^2+o(n^2)}`.
- **B3 — prove something stronger:** PARTIAL. For uniform finite-field matrices, the full characteristic-polynomial collision entropy is `n log_2 q+o(1)` when `q>>n`, and equals `n^2+o(n^2)` at exponential `q`. The missing transfer to Rademacher entries remains open.

## 5. Metric and next attack

Frozen source metric before:

\[
0\le u_{GI}\le\frac12.
\]

Frozen source metric after:

\[
0\le u_{GI}\le\frac12.
\]

**NO SOURCE-METRIC MOVEMENT.** This is the second ordinary no-movement run after STUCK2.

The next nonrepeating methods are **B11 / B21 / B28**:

1. **B11 dualize:** express the characteristic-polynomial collision probability by Fourier/Parseval on the coefficient vector in `F_p^n`, looking for a factorization or rank statistic that converts coefficient collision into anti-concentration of multilinear forms.
2. **B21 import an analogous technique:** treat `M -> chi_M` as a nonlinear hash/coding map and import inverse Littlewood–Offord / leftover-hash / additive-energy machinery to separate structured high-collision fibers from generic ones.
3. **B28 typical rather than all:** prove near-maximal characteristic-polynomial entropy outside an explicitly countable structured family; then bound the structured family directly. The explicit shear family is a mandatory stress test, not an exception to ignore.

No claim of source closure, corrected-exponent proof, or novelty is made here.