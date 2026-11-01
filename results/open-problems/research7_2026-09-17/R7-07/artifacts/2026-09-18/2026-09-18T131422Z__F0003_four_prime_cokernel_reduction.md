Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — exact periodic-center obstruction and a four-prime cokernel reduction

Date: 2026-09-18 UTC.  
Slot: `R7-07 Hard Problem New Methods`, native ID `6aabe8413f60819197825dd81ca138ae`.  
Outside target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Section 5 immediately after Theorem 5.2.  
Frozen metric:

\[
a_3:=\sup\{a\ge0:\Pr(A_{n,3}\text{ singular})\le n^{-a+o(1)}\}.
\]

Cumulative evidenced value before this artifact: **`a_3 >= 1/4`**.  
Value after the results below: **`a_3 >= 1/4` — NO MOVEMENT.**

Methods in this iteration: **B14 FIND THE GROUP ACTING / B21 ASK WHO ELSE HAS THIS SHAPE / B27 SWAP THE QUANTIFIERS.** The immediately preceding mathematical triple was B1/B15/B30.

The point of this run is not another local-CLT checker. It first proves that one tempting symmetry route cannot improve the quarter exponent, and then changes the object being estimated from one growing-prime kernel to a joint multi-prime/cokernel moment. The latter gives an exact endpoint criterion: a suitable four-prime mixed moment at the already-reached quarter scale would imply the conjectured cubic exponent `a_3=1`.

---

## 1. Cumulative interface and the current `1/4` barrier

The preceding R7-07 theorem established, for every fixed `d>=3`,

\[
\Pr(A_{n,d}\text{ singular over }\mathbb R)
\le O_d(n^{2-d})+n^{-1/4+o(1)}.
\tag{1.1}
\]

Its proof uses Huang's undirected symmetric edge-count representation, a field-independent sparse-support sieve, rowwise Cramér tilting, and localized congruence theta sums. At a prime

\[
p\asymp n^{1/4}/(\log n)^K,
\]

the remaining central saddle corrections have size `O_d(p^4 log n/n)`. Thus simply taking a single prime appreciably larger than `n^{1/4}` requires genuinely new information; the old global type-count entropy was already removed.

The new question is therefore whether the source exponent can be reached **without asking one finite field to carry all of the arithmetic information**.

---

# 2. B14 — the `p` structured row saddles are an exact periodic symmetry, not reducible entropy

The previous report proposed exploiting the simultaneous `S_p` symmetry of the structured Fourier neighborhoods. Before attempting an orbit count, one must check whether those neighborhoods are genuinely different configurations or merely exact periods of the same Fourier coefficient. They are exact periods.

## 2.1 The row walk and its character symmetry

Use the cumulative `U_{d,p}` row-walk convention. A support vector

\[
X=(X_0,\ldots,X_{p-1})\in\mathbb Z_{\ge0}^p
\]

records the occupancies of residues in a `d`-tuple

\[
(a_1,\ldots,a_d)\in\mathbb F_p^d,
\qquad a_1+\cdots+a_d=0,
\]

so

\[
\sum_{j=0}^{p-1}X_j=d,
\qquad
\sum_{j=0}^{p-1}jX_j\equiv0\pmod p.
\tag{2.1}
\]

Let

\[
\phi(s)=\mathbb E\,e^{i\langle s,X\rangle}.
\]

For `k in F_p`, define

\[
c_k:=\left(\frac{2\pi k j}{p}\right)_{j=0}^{p-1}.
\tag{2.2}
\]

Then every support vector satisfies

\[
\langle c_k,X\rangle
=\frac{2\pi k}{p}\sum_jjX_j\in2\pi\mathbb Z.
\]

Hence, **exactly**,

\[
\boxed{\phi(s+c_k)=\phi(s)}.
\tag{2.3}
\]

These are precisely the `p` congruence-related structured centers appearing in the one-row inverse characteristic-function analysis.

## 2.2 Feasible coefficient targets have the same exact period

Let `m` be a target with

\[
\Pr(X_1+\cdots+X_N=m)>0.
\]

By summing (2.1),

\[
\sum_jjm_j\equiv0\pmod p,
\]

and consequently

\[
e^{-i\langle c_k,m\rangle}=1.
\tag{2.4}
\]

The complete Fourier coefficient integrand

\[
I_m(s):=\phi(s)^N e^{-i\langle s,m\rangle}
\]

therefore obeys

\[
\boxed{I_m(s+c_k)=I_m(s)}
\tag{2.5}
\]

for every `k`.

Thus the `p` local saddle contributions are not merely approximately equal: they are exact phase-coherent translates for every feasible target.

## 2.3 Consequence for the undirected symmetric type sum

For a fixed undirected symmetric type `M=(m_ij)`, Huang's row factors have feasible row targets `m_i`. Applying (2.5) separately to each row shows that every center tuple

\[
(k_0,\ldots,k_{p-1})\in\mathbb F_p^p
\]

produces the same product of row-local Fourier contributions. The symmetry constraint

\[
m_{ij}=m_{ji}
\]

couples the **targets**, but it does not identify or constrain these row-period labels after the target is fixed.

### Proposition 2.1 — periodic-center no-go theorem

Any improvement that tries only to quotient the `p^p` structured row neighborhoods by simultaneous row-label symmetry cannot improve the current exponent: those neighborhoods are exact periods of the row Fourier coefficient, and every feasible row target carries the same periodicity.

This does **not** say that a genuinely joint Fourier representation cannot help. It says the hoped-for gain cannot come from declaring most of the existing row saddles spurious. A successful collective argument has to introduce information that is absent from the product of the separate row coefficient formulas.

This is the useful B14 failure: it removes a false route before code or a large orbit enumeration is built.

---

# 3. B21 — change category from one finite-field kernel to the integer cokernel

The one-prime method pays for an increasingly high-dimensional local CLT. The same singularity event can instead be seen through the integer cokernel, where information from several moderate primes can be combined exactly.

Let `A` be an integer `n x n` matrix and write

\[
C_A:=\mathbb Z^n/A\mathbb Z^n.
\]

For an integer `q>=2`, define

\[
H_q(A):=|\operatorname{Hom}(C_A,\mathbb Z/q\mathbb Z)|.
\tag{3.1}
\]

A homomorphism `Z^n -> Z/qZ` is represented by a row vector `y in (Z/qZ)^n`, and it descends to `C_A` exactly when `yA=0`. Therefore

\[
\boxed{H_q(A)=|\ker(A^T\bmod q)|.}
\tag{3.2}
\]

For an adjacency matrix, `A=A^T`, so this is the usual modular kernel size.

## 3.1 Deterministic singularity inequality

If `det A=0` over `Q`, Smith normal form gives

\[
C_A\cong\mathbb Z^r\oplus T
\]

with `r>=1`. Hence

\[
H_q(A)\ge q.
\]

For every integer matrix, `H_q(A)>=1`. Consequently

\[
\boxed{
\mathbf1_{\{\det A=0\}}
\le \frac{H_q(A)-1}{q-1}.
}
\tag{3.3}
\]

Taking expectation yields the exact reduction

\[
\boxed{
\Pr(\det A=0)
\le \frac{\mathbb EH_q(A)-1}{q-1}.
}
\tag{3.4}
\]

No finite-field approximation, local CLT, or independence assumption is used in (3.3)-(3.4).

## 3.2 Exact divisor decomposition into surjection moments

Because `Z/qZ` has a unique subgroup of each order `r|q`, every homomorphism `C_A -> Z/qZ` has an image of exactly one such order. Identifying that subgroup with `Z/rZ` gives a surjection. Thus

\[
\boxed{
H_q(A)=\sum_{r\mid q}
|\operatorname{Sur}(C_A,\mathbb Z/r\mathbb Z)|.
}
\tag{3.5}
\]

This identity is exact for every integer `q`.

Now take a squarefree modulus

\[
q=p_1p_2p_3p_4
\tag{3.6}
\]

with four distinct odd primes. Then (3.5) has only `16` terms.

### Theorem 3.1 — four-prime endpoint reduction

For cubic random regular adjacency matrices, choose four distinct primes

\[
p_i\in[P,2P],
\qquad
P=\frac{n^{1/4}}{L(n)},
\qquad L(n)=n^{o(1)},
\tag{3.7}
\]

so that

\[
q=p_1p_2p_3p_4=n^{1-o(1)}.
\]

If one proves the uniform growing-group moment bound

\[
\boxed{
\max_{r\mid q}
\mathbb E\,|\operatorname{Sur}(C_{A_{n,3}},\mathbb Z/r\mathbb Z)|
\le n^{o(1)},
}
\tag{3.8}
\]

then

\[
\Pr(A_{n,3}\text{ singular})\le n^{-1+o(1)},
\]

and hence `a_3=1`, the cubic source endpoint.

### Proof

By (3.5) and the sixteen divisors of squarefree `q`, (3.8) implies

\[
\mathbb EH_q(A_{n,3})\le16n^{o(1)}=n^{o(1)}.
\]

Substitute this into (3.4) and use `q=n^{1-o(1)}`. QED.

This is a qualitatively different target from enlarging one prime. Every individual prime in (3.7) already lies inside the quarter-power range reached by the cumulative R7-07 analysis.

## 3.3 Why the known fixed-cokernel literature is not enough

Nguyen--Wood and Mészáros provide exactly the neighboring machinery one would want: moments and mixing statements for cokernels/sandpile-type groups of random regular graph matrices when the finite target group, or the relevant finite set of primes, is fixed. That is evidence that (3.8) is the right mathematical category.

It is **not** a proof of (3.8). The asymptotic errors in fixed-finite-group statements may depend on the group size `|V|`, while here divisors `r` grow as large as `n^{1-o(1)}`. Replacing a fixed `V` by `V=Z/r(n)Z` without a quantitative uniform theorem would be invalid.

There is a second transfer issue: some cokernel results are proved first in a configuration/sum-of-matchings model. For an unbounded observable such as `H_q`, bare contiguity or conditioning on simplicity does not by itself preserve the required moment estimate. Any later use must keep the exact graph model and the size dependence explicit.

So Theorem 3.1 is an **endpoint reduction with a named missing estimate**, not a claimed solution.

---

# 4. B27 — swap the prime quantifier and target only the top mixed nullity moment

The full bound (3.8) may be stronger than necessary. One can isolate the exact joint modular statistic forced by a real singularity.

For a prime `p`, define

\[
L_p(A):=\frac{H_p(A)-1}{p-1}.
\tag{4.1}
\]

If `nu_p(A)=dim_{F_p} ker(A mod p)`, then

\[
H_p(A)=p^{\nu_p(A)}
\]

and

\[
L_p(A)=
\begin{cases}
0,&\nu_p=0,\\
1+p+\cdots+p^{\nu_p-1},&\nu_p\ge1.
\end{cases}
\tag{4.2}
\]

In particular `L_p>=0`.

If `det A=0` over `Q`, choose a primitive integer null vector `x`. For every prime `p`, primitiveness implies `x mod p` is nonzero, so `nu_p(A)>=1` and therefore `L_p(A)>=1`. Hence for **any** distinct primes `p_1,...,p_k`,

\[
\boxed{
\mathbf1_{\{\det A=0\}}
\le \prod_{i=1}^kL_{p_i}(A).
}
\tag{4.3}
\]

Taking expectation,

\[
\boxed{
\Pr(\det A=0)
\le \mathbb E\prod_{i=1}^kL_{p_i}(A).
}
\tag{4.4}
\]

This is the desired quantifier swap: instead of choosing one prime large enough that `1/p` itself reaches the source exponent, use several primes each inside the analytically accessible range and ask how strongly their kernel events correlate.

### Corollary 4.1 — exact four-prime mixed-moment criterion

For four primes satisfying (3.7), it is enough to prove

\[
\boxed{
\mathbb E\prod_{i=1}^4L_{p_i}(A_{n,3})
\le n^{-1+o(1)}.
}
\tag{4.5}
\]

Then `a_3=1`.

This criterion is weaker than controlling all sixteen divisor moments in (3.8). Indeed Chinese remaindering gives

\[
H_q(A)=\prod_{i=1}^4H_{p_i}(A)
=\prod_{i=1}^4\left[1+(p_i-1)L_{p_i}(A)\right].
\tag{4.6}
\]

All terms are nonnegative, so

\[
\left(\prod_i(p_i-1)\right)
\mathbb E\prod_iL_{p_i}(A)
\le\mathbb EH_q(A).
\tag{4.7}
\]

Thus a uniform `n^{o(1)}` bound on `EH_q` proves (4.5), but one may instead attack (4.5) directly and ignore all lower-order divisor moments.

## 4.1 Sharp calibration against the source lower-bound mechanism

The source's local lower-bound mechanism is rank deficiency caused by twin vertices. On a typical corank-one twin event, every prime has `nu_p>=1`, and generically the corresponding `L_p` contribution is of order one. Hence that event contributes on the order of its real probability, `n^{-1+o(1)}` in the cubic case, to the mixed moment in (4.5).

So the target scale in (4.5) is not artificially strong. It is exactly calibrated to the obstruction that is conjectured to dominate real singularity.

The remaining danger consists of matrices that are nonsingular over `Q` but whose determinant is divisible by all four quarter-scale primes, or matrices with unusually large modular nullities. Those are precisely the multi-prime correlations that a cokernel/surjection argument must suppress.

---

# 5. What moved mathematically and what did not

The source-matching frozen exponent did **not** move:

\[
\boxed{a_3\ge1/4\quad\longrightarrow\quad a_3\ge1/4.}
\]

This is therefore an ordinary unchanged research run, not a source solution.

What did change is the shape of the remaining problem:

1. **B14 proves a no-go:** the `p` structured row saddles are exact congruence periods, so orbit-counting those saddles cannot manufacture the missing exponent.
2. **B21 gives an exact endpoint reduction:** a uniform four-prime cyclic-cokernel surjection-moment estimate at quarter-scale primes implies `a_3=1`.
3. **B27 weakens that requirement further:** it is enough to control one four-prime mixed nullity statistic (4.5), which is exactly calibrated to the twin lower-bound scale.

The central `p^4/n` one-prime barrier is therefore not necessarily a barrier to the source theorem. It is a barrier only to the strategy “make one prime do everything.”

---

# 6. Dated literature check — 2026-09-18

The source remains Van Vu's sharp-exponent question for the undirected fixed-degree random regular adjacency matrix. The bounded search performed for this run did not locate a later theorem proving the source-predicted exponent `d-2`; this is negative evidence only, so worldwide openness and publication novelty remain **UNVERIFIED**.

Relevant current neighboring results checked:

- Hoi H. Nguyen and Amanda Pan, *A note on the singularity probability of random directed d-regular graphs*, arXiv:2308.06461 / *European Journal of Combinatorics* (2024), prove an `n^{-1/3+o(1)}` bound for the **directed** model and develop the one-row structured Fourier analysis used cumulatively here. Their global directed theorem is not transferred to the undirected target.
- Jiaoyang Huang, Theo McKenzie and Horng-Tzer Yau prove optimal-scale spectral rigidity/edge universality for fixed-degree random regular graphs. These results are powerful spectral input but do not by themselves determine the atom at the exact eigenvalue zero.
- Hoi H. Nguyen and Melanie Matchett Wood, *Cokernels of adjacency matrices of random r-regular graphs*, arXiv:1806.10068, and Andras Meszaros, *The distribution of sandpile groups of random regular graphs*, arXiv:1806.03736, supply fixed-finite-group/fixed-prime cokernel and mixing machinery. The size-uniform estimate needed in (3.8) is not asserted here to follow from those fixed-group theorems.

No claim of novelty is based on a failed search.

---

# 7. Exact remaining gap and next nonrepeating attack

The cleanest blocking statement is now:

> For four distinct primes `p_i ~ n^{1/4}/L(n)`, prove the source-scale joint estimate
> \[
> \mathbb E\prod_{i=1}^4L_{p_i}(A_{n,3})\le n^{-1+o(1)}.
> \]
> Equivalently, a stronger sufficient route is to make fixed-group cokernel/surjection moment estimates quantitatively uniform for squarefree cyclic groups of size `n^{1-o(1)}`.

No existing fixed-group result has been silently promoted to this growing-group statement.

The next method triple, avoiding B14/B21/B27, is:

- **B5 — ADD A PARAMETER AND DIFFERENTIATE:** introduce the modulus size or prime-factor count as a deformation parameter and extract explicit dependence of the regular-graph mixing/surjection error on `|V|`.
- **B12 — FIND WHAT IS CONSERVED:** identify the exact symmetric-pairing invariants governing adjacency cokernels and determine whether cyclic targets collapse the state space enough to keep constants polynomial in `|V|`.
- **B25 — COUNT THE SAME THING TWICE:** double-count surjections jointly with the pairing constraints, seeking an exact cancellation that avoids a `q`-dimensional occupancy local CLT.

Those routes attack the new bottleneck rather than extending the saturated one-prime saddle expansion.
