Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — averaged cumulants, a conserved row-energy tensor, and the `1/5` singularity exponent

Date: 2026-09-18 UTC.  
Slot: `R7-07 Hard Problem New Methods`, native ID `6aabe8413f60819197825dd81ca138ae`.  
Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Section 5 immediately after Theorem 5.2.  
Primary undirected input: Jiaoyang Huang, *Invertibility of adjacency matrices for random d-regular graphs*, arXiv:1807.06465.  
Local characteristic-function input: Hoi H. Nguyen and Amanda Pan, *A note on the singularity probability of random directed d-regular graphs*, arXiv:2308.06461 / *European Journal of Combinatorics* (2024). Only their one-row `U_{d,p}` characteristic-function estimates are imported; no directed global independence or directed singularity conclusion is imported.

Frozen metric:

\[
a_3:=\sup\{a\ge0:\Pr(A_{n,3}\text{ singular})\le n^{-a+o(1)}\}.
\]

Cumulative evidenced value before this artifact: **`a_3 >= 1/6`**, from the corrected artifact `2026-09-18T102500Z__F0003_one_sixth_corrected_proof.md`.  
Value after the theorem below: **`a_3 >= 1/5` — MOVEMENT.**

Methods in this iteration: **B5 ADD A PARAMETER AND DIFFERENTIATE / B12 FIND WHAT IS CONSERVED / B24 FIND THE EXTREMAL OBJECT.** The immediately preceding mathematical triple was B14/B6/B29.

The full source target remains `Pr(A_{n,d} singular)=n^{-d+2+o(1)}` for every fixed `d>=3`; in particular the source-predicted cubic endpoint is `a_3=1`. The present theorem is therefore **PARTIAL**, not source closure.

---

## 1. Cumulative interfaces that are reused

This artifact does not restart the proof. It uses four cumulative ingredients whose hypotheses are rechecked here.

### 1.1 Huang's exact undirected finite-field decomposition

For fixed `d>=3` and an odd prime `p` with `p` not dividing `d`, Huang rewrites the expected number of nonzero `F_p` null vectors in the undirected configuration model as a sum over symmetric edge-count matrices. In the equidistributed region write

\[
A_{ij}=\frac{m_{ij}}{dn}-\frac1{p^2},
\qquad r=A\mathbf 1,
\qquad \sum_{i,j}A_{ij}=0.
\]

The quadratic exponent is

\[
Q(A)=\frac{dnp^2}{4}\|A\|_F^2-\frac{(d-1)np}{2}\|r\|_2^2.
\tag{1.1}
\]

Huang's four non-equidistributed classes are also retained class by class. We do **not** invoke his final Proposition 4.2 beyond its stated prime range; the sparse third class has already been replaced by an R7-07 field-independent support theorem.

### 1.2 The R7-07 sparse-support sieve

The preceding R7-07 support theorem proves, uniformly for a prescribed field, that a nonzero kernel vector with support between `3` and `delta_d n` has probability `o(n^{2-d})`, while support two is exactly the nonadjacent-twin mechanism and has probability `O_d(n^{2-d})`. Consequently Huang's sparse third class has event probability

\[
\Pr(E_{sp})=O_d(n^{2-d})
\tag{1.2}
\]

whenever its cutoff `O(p^3 log n)` is `o(n)`. At the `1/5` scale below this condition has a large margin.

### 1.3 The exact isotypic decomposition

Define

\[
B(r):=\frac{r\mathbf1^T+\mathbf1r^T}{p},
\qquad H:=A-B(r).
\]

Then `H1=0`, `H` is Frobenius-orthogonal to `B(r)`, and the corrected preceding artifact proves the exact identities

\[
Q(A)=\frac{dnp^2}{4}\|H\|_F^2+\frac{np}{2}\|r\|_2^2,
\tag{1.3}
\]

and, for the row-deviation matrix

\[
u_{ij}:=pA_{ij}-r_i,
\]

\[
u=pH+\mathbf1 r^T.
\tag{1.4}
\]

Normalize

\[
X:=\sqrt n\,pH,
\qquad Y:=\sqrt{np}\,r,
\qquad Z:=\sqrt n\,u.
\]

Under the centered Gaussian with density proportional to `exp(-Q)`, `X` and `Y` are independent Gaussian vectors on their invariant subspaces and

\[
Q=\frac d4\|X\|_F^2+\frac12\|Y\|_2^2,
\qquad
Z_{ij}=X_{ij}+\frac{Y_j}{\sqrt p}.
\tag{1.5}
\]

All covariance operators in these normalized coordinates are bounded above and below by constants depending only on fixed `d` on their supports.

It is also convenient to normalize the raw type fluctuation

\[
W_{ij}:=\sqrt n\,p A_{ij}
=X_{ij}+\frac{Y_i+Y_j}{\sqrt p}.
\tag{1.6}
\]

### 1.4 Nguyen--Pan's one-row inverse characteristic estimate

For the uniform `U_{d,p}` row walk, Nguyen--Pan prove an inverse theorem of the following form: if the characteristic function has modulus at least `1-c/p^2`, the frequency lies in one of `p` structured neighborhoods of radius `O(1/p)`. Huang's row factors use the **same** `U_{d,p}` walk. Therefore, for an undirected row with sample size `n_i asymp n/p`, frequencies outside those structured neighborhoods contribute

\[
\exp\{-c_d n_i/p^2\}
=
\exp\{-c_d n/p^3\}
\tag{1.7}
\]

relative to the row normalization. This is a row statement and imports no directed global factorization.

Their moment calculation on `1^perp` also gives the already-used local expansion

\[
\log\phi(s)
=-\frac d{2p}\|s\|^2
-i\frac{C_{d,p}}{6p}\sum_j s_j^3
+R(s),
\tag{1.8}
\]

where `C_{d,p}=d+O_d(1/p)` and

\[
|R(s)|\le C_d\left(p^{-2}\|s\|^4+p^{-1}\sum_j s_j^4\right).
\tag{1.9}
\]

---

## 2. A Gaussian cubic lemma used repeatedly

The new argument stops taking suprema of cubic corrections over a ball. Instead it averages them under the exact quadratic Gaussian.

### Lemma 2.1 — cubic chaos with `O(p^2)` variance

Let `G=(G_a)_{a in I}` be a centered Gaussian vector with `|I|=O(p^2)`, covariance operator norm `O_d(1)`, and coordinate variances `O_d(1)`. Then

\[
T(G):=\sum_{a\in I}G_a^3
\]

satisfies

\[
\boxed{\operatorname{Var}T(G)=O_d(p^2).}
\tag{2.1}
\]

#### Proof

Write `C_ab=E(G_aG_b)`. Wick's formula gives

\[
E(G_a^3G_b^3)=9C_{aa}C_{bb}C_{ab}+6C_{ab}^3.
\]

For the first sum, if `v_a=C_aa`,

\[
\sum_{a,b}C_{aa}C_{bb}C_{ab}=v^TCv
\le \|C\|_{op}\|v\|_2^2=O_d(|I|).
\]

For the second,

\[
\sum_{a,b}|C_{ab}|^3
\le \max_{a,b}|C_{ab}|\sum_{a,b}C_{ab}^2
=O_d(\operatorname{tr}C^2)=O_d(|I|).
\]

Since `|I|=O(p^2)`, (2.1) follows. QED.

The lemma applies to both arrays `W` and `Z`, because they are bounded-operator-norm linear images of `(X,Y)`.

### Lemma 2.2 — safe averaging of an odd cubic perturbation

Let `O(G)` be an odd cubic polynomial in `(X,Y)` whose variance is `sigma^2=o(1)` after its `n,p` coefficient is included. Suppose on Huang's broad equidistributed ball

\[
|O(G)|\le \varepsilon_n Q(G),\qquad \varepsilon_n\to0.
\tag{2.2}
\]

Then, for the continuous centered Gaussian truncated to that ball,

\[
\frac{\int e^{-Q+O}}{\int e^{-Q}}
=1+O(\sigma^2)+o(1).
\tag{2.3}
\]

#### Proof

The centered Gaussian and the full symmetric ball are invariant under `G -> -G`, so the linear odd term cancels. Pairing `G` and `-G` gives `cosh O`. Since

\[
0\le\cosh x-1\le \frac{x^2}{2}e^{|x|},
\]

and (2.2) turns `e^{-Q+|O|}` into a Gaussian with precision `(1-o(1))Q`, the second moment of the same fixed-degree chaos remains within a fixed constant of its centered Gaussian second moment. The Gaussian mass outside the broad ball is exponentially negligible. QED.

The same proof works for a sum of finitely many odd cubic terms.

---

# 3. B5 — expand the *global* central weight and average before bounding

The preceding `1/6` proof still bounded several central corrections separately. At `p=n^{1/5-o(1)}`, the right operation is to keep the global Stirling/local-CLT exponent in a one-parameter family and differentiate its Gaussian normalization at the quadratic point.

Formally, if `Psi(A)` is the sum of all nonquadratic central corrections, define

\[
Z(t):=\int e^{-Q(A)+t\Psi(A)}\,dA,
\qquad 0\le t\le1.
\]

Then

\[
\frac d{dt}\log Z(t)=E_t\Psi,
\tag{3.1}
\]

so odd corrections vanish at `t=0` and the first surviving contribution is their covariance scale. The estimates below make this perturbation argument uniform up to `t=1` because every correction is `o(Q)` on Huang's broad ball.

## 3.1 The Stirling entropy cubic is odd and has variance `O(p^4/n)`

Taylor expansion of the matrix-entropy and row-entropy terms around the uniform type has the form

\[
\Psi_{St,3}
=c_{3,d}\,np^4\sum_{i,j}A_{ij}^3
+c'_{3,d}\,np^2\sum_i r_i^3,
\tag{3.2}
\]

with fixed constants depending only on `d`; the exact signs are irrelevant to the estimate. By (1.6),

\[
np^4\sum A_{ij}^3
=\frac p{\sqrt n}\sum W_{ij}^3,
\tag{3.3}
\]

and

\[
np^2\sum r_i^3
=\frac{\sqrt p}{\sqrt n}\sum_iY_i^3.
\tag{3.4}
\]

Lemma 2.1 gives

\[
\operatorname{Var}\Psi_{St,3}
=O_d\left(\frac{p^4}{n}\right).
\tag{3.5}
\]

The broad type ball has `||W||=O(p sqrt(log n))`; hence the cubic/quadratic ratio is at most `O(p^2 sqrt(log n/n))=o(1)` at every scale `p<=n^{1/5}` with logarithmic slack. Lemma 2.2 therefore gives an averaged Stirling-cubic cost

\[
1+O_d(p^4/n)+o(1).
\tag{3.6}
\]

## 3.2 The even Stirling correction is also `O(p^4/n)`

The matrix quartic term has size

\[
O_d\left(np^6\sum A_{ij}^4\right)
=O_d\left(\frac{p^2}{n}\sum W_{ij}^4\right).
\tag{3.7}
\]

Under the quadratic Gaussian, `E sum W_ij^4=O_d(p^2)`, so its mean is

\[
O_d(p^4/n).
\tag{3.8}
\]

The row quartic term is smaller, `O_d(p^2/n)`. On the broad ball every higher Taylor term is bounded by an additional factor `max |p^2A_ij|+max|pr_i|=o(1)` relative to the preceding one. Thus the full entropy correction beyond the cubic has normalized expectation

\[
1+O_d(p^4/n)+o(1).
\tag{3.9}
\]

The square-root Stirling prefactors and the `1/(12m)` remainders are no larger: the total reciprocal-cell error is `O(p^4/n)`, their common linear fluctuation either cancels from `sum A_ij=0` or is an odd centered diagonal statistic, and their quadratic contribution is `O(p^4/n)`.

## 3.3 The local cubic saddle also costs only `O(p^4/n)` after gluing

The preceding symmetric-gluing derivation expresses the leading row cubic correction as

\[
\Psi_{loc,3}
=\lambda_{d,p}T_Z,
\qquad
\lambda_{d,p}=O_d(p/\sqrt n),
\qquad
T_Z=\sum_{i,j}Z_{ij}^3.
\tag{3.10}
\]

Lemma 2.1 gives `Var(T_Z)=O_d(p^2)`, hence

\[
\operatorname{Var}\Psi_{loc,3}=O_d(p^4/n).
\tag{3.11}
\]

Moreover `|Psi_loc,3|=o(Q)` uniformly on the broad equidistributed ball, because the cubic/quadratic ratio is bounded by `O(p^2 sqrt(log n/n))`. Lemma 2.2 therefore replaces the old max-coordinate cubic bound by

\[
E_Q e^{\Psi_{loc,3}}=1+O_d(p^4/n)+o(1).
\tag{3.12}
\]

## 3.4 The fourth-order row remainder is `O(p^4 log n/n)` in normalized mass

For one row, after the quadratic contour shift, the real Gaussian Fourier coordinate has variance `O_d(p^2/n)` in each of `p` directions. Thus (1.9) gives expected fourth-order exponent `O_d(p^3/n)` per row and `O_d(p^4/n)` over all rows.

The target-dependent imaginary shift can be expressed through row energies

\[
S_i:=\sum_jZ_{ij}^2.
\]

The fourth-order target terms are bounded by the cumulative formula

\[
C_d\left[
\frac pn\sum_iS_i^2+
\frac{p^2}{n}\sum_{i,j}Z_{ij}^4
\right].
\tag{3.13}
\]

Under the quadratic Gaussian,

\[
E\sum_iS_i^2=O_d(p^3),
\qquad
E\sum_{i,j}Z_{ij}^4=O_d(p^2),
\tag{3.14}
\]

so both terms in (3.13) have mean `O_d(p^4/n)`.

To justify exponentiation rather than only first moments, split the Gaussian into the core

\[
\|Z\|_F^2\le C_dp^2,
\qquad
\max_{ij}|Z_{ij}|^2\le C_d\log n,
\tag{3.15}
\]

and its complement. On the core, (3.13) is `O_d(p^4 log n/n)=o(1)`. On Huang's full broad ball it is at most `o(1)Q`, because `||Z||^2=O(p^2 log n)` and `p^4 log n/n=o(1)`. Hence the complement remains exponentially dominated by a slightly weakened Gaussian. Therefore the complete fourth-order row remainder changes normalized mass by

\[
1+O_d\left(\frac{p^4\log n}{n}\right)+o(1).
\tag{3.16}
\]

This is the central B5 gain: no `p^6/n` term is intrinsically forced after the perturbation is averaged in the correct Gaussian variables.

---

# 4. B12 — a conserved row-energy mode removes the denominator barrier

The exact one-row quadratic exponent contains

\[
E_2(A)
=\frac d2\sum_iS_i\frac{x_i}{1+x_i},
\qquad
x_i:=pr_i=\sqrt{p/n}\,Y_i.
\tag{4.1}
\]

Expand

\[
\frac{x_i}{1+x_i}=x_i+O(x_i^2).
\]

The leading term is the odd cubic statistic

\[
L:=\frac d2\sqrt{p/n}\,P,
\qquad
P:=\sum_iY_iS_i.
\tag{4.2}
\]

A crude bound treats `S_i` and `Y_i` as if they could all be maximal simultaneously. The exact decomposition has a conservation law that forbids that.

### Lemma 4.1 — conserved common row-energy mode

With `Z_ij=X_ij+Y_j/sqrt(p)` and `X1=0`, put

\[
R_i:=\sum_jX_{ij}^2.
\]

Then

\[
\boxed{
P
=\sum_iY_iR_i
+\frac2{\sqrt p}Y^TXY.
}
\tag{4.3}
\]

In particular the common term `||Y||^2/p` in every `S_i` cancels **exactly** because `sum_iY_i=0`.

#### Proof

Expanding row energy,

\[
S_i=R_i+\frac2{\sqrt p}\sum_jX_{ij}Y_j+\frac1p\|Y\|^2.
\]

Multiply by `Y_i` and sum in `i`. The last term is `(||Y||^2/p)sum_iY_i=0`; the middle term is `(2/sqrt p)Y^TXY`. QED.

### Lemma 4.2 — variance of the conserved denominator tensor

Under the centered quadratic Gaussian,

\[
\boxed{\operatorname{Var}P=O_d(p^2).}
\tag{4.4}
\]

#### Proof

Condition on `X`. Since `Y` is a standard Gaussian on `1^perp`,

\[
E_Y\left(\sum_iY_iR_i\right)^2
=\|P_{1^\perp}R\|_2^2.
\]

Permutation symmetry makes `E R_i` independent of `i`. Each `R_i` is a quadratic form in an `O(p)`-dimensional Gaussian row with bounded covariance operator, so `Var(R_i)=O_d(p)`. Hence

\[
E\|P_{1^\perp}R\|^2
\le\sum_iE(R_i-ER_i)^2=O_d(p^2).
\]

For the second term, the standard Gaussian quadratic-form identity gives

\[
E_Y(Y^TXY)^2
=2\operatorname{tr}(X^2)+(\operatorname{tr}X)^2.
\]

Now `E||X||_F^2=O_d(p^2)` and `E(tr X)^2=O_d(p^2)`, so after multiplication by `4/p` its contribution is `O_d(p)`. The cross term is absorbed by Cauchy--Schwarz. QED.

It follows from (4.2) that

\[
\operatorname{Var}L=O_d(p^3/n).
\tag{4.5}
\]

The quadratic remainder in (4.1) has expectation

\[
O_d\left(\frac pn E\sum_iS_iY_i^2\right)=O_d(p^3/n),
\tag{4.6}
\]

because there are `p^2` bounded-moment `(i,j)` contributions in `S_i`. As in Lemma 2.2, the odd leading term averages out and all denominator perturbations are `o(Q)` on the broad ball. Therefore

\[
\boxed{
\frac{\text{Gaussian mass with exact row denominators}}
{\text{quadratic Gaussian mass}}
=1+O_d(p^3/n)+o(1).
}
\tag{4.7}
\]

This removes the last `p^3/sqrt(n)` pointwise barrier from the `1/6` proof.

A parallel conservation is visible directly in the cubic tensor. Expanding

\[
\sum_{i,j}Z_{ij}^3
\]

in `X` and `Y`, the term `sum_{i,j}X_ijY_j^2` vanishes because every column sum of `X` is zero, and the common row mode cancels against `sum Y=0`. This is the structural reason Lemma 2.1 is the correct scale after symmetric gluing.

---

# 5. B24 — the extremal congruence character has support at least `p-1`

The remaining obstruction is no longer a central cumulant. It is an **outer-frequency / dual-lattice** effect. The exact congruence homomorphism retained from the earlier R7-07 work is

\[
\mathcal L(M)
=
\left(
(\sum_jm_{ij}\bmod d)_i,
(\sum_jj m_{ij}\bmod p)_i
\right),
\tag{5.1}
\]

with one global dependency in the mod-`d` coordinates. Its image has size `d^{p-1}p^p`.

A mod-`p` character is represented by `beta=(beta_0,...,beta_{p-1}) in F_p^p`. On an off-diagonal symmetric count coordinate `m_ij`, `i<j`, its mod-`p` frequency numerator is

\[
\beta_i j+\beta_j i,
\tag{5.2}
\]

while on the diagonal half-coordinate `m_ii=2k_i` it is

\[
2\beta_i i.
\tag{5.3}
\]

### Lemma 5.1 — minimum support of a nontrivial weighted-row character

If `beta !=0`, at least `p-1` independent upper-triangular count coordinates have nonzero mod-`p` numerator in (5.2)--(5.3).

#### Proof

If `beta_0 !=0`, every edge coordinate `(0,j)`, `j=1,...,p-1`, has numerator `beta_0 j !=0`, giving `p-1` coordinates.

Assume `beta_0=0` and let

\[
S=\{i\in\{1,...,p-1\}:\beta_i\ne0\},
\qquad |S|=k\ge1.
\]

For each `i in S`, the diagonal numerator `2 beta_i i` is nonzero because `p` is odd, giving `k` coordinates. Every cross edge with `i in S` and `j in {1,...,p-1}\S` has numerator `beta_i j !=0`, giving `k(p-1-k)` more. Thus the support size is at least

\[
k+k(p-1-k)=k(p-k)\ge p-1.
\]

QED.

Now include an arbitrary mod-`d` row character. Because `gcd(p,d)=1`, a nonzero fraction `a/p` cannot be cancelled modulo integers by adding `b/d`: if `a/p+b/d` were integral then reducing `da+pb` modulo `p` would force `a=0 mod p`. Hence each of the `p-1` coordinates above lies at distance at least `1/(dp)` from the integer dual lattice. Therefore every character with nontrivial mod-`p` part has squared dual distance

\[
\boxed{\operatorname{dist}^2\ge \frac{c_d}{p}.}
\tag{5.4}
\]

A character with trivial mod-`p` part but nontrivial mod-`d` part has an even larger fixed-denominator distance.

## 5.2 Poisson suppression is `exp(-c n/p^3)`, not `exp(-c n/p^4)`

In integer count coordinates `K=dnA`, the precision eigenvalues of the quadratic form are `Theta_d(p^2/n)`. Therefore Poisson summation turns (5.4) into

\[
\boxed{
\left|\frac{S_\chi}{S_1}\right|
\le
\exp\left\{C_dp^2\log n-c_d\frac n{p^3}\right\}
}
\tag{5.5}
\]

for every nontrivial congruence character. The `C p^2 log n` term is a deliberately crude dimension/dual-packing allowance. Since there are only `d^{p-1}p^p=exp(O_d(p log p))` finite characters, the exact congruence theta sum equals its trivial-character Gaussian value up to `1+o(1)` whenever

\[
\boxed{p^5\log n=o(n).}
\tag{5.6}
\]

The same Poisson argument can be differentiated a fixed number of times. Consequently every polynomial moment of total degree at most six under the exact congruence theta measure agrees with the corresponding centered Gaussian moment up to a polynomial factor times the exponentially small right side of (5.5). This justifies the odd-cubic cancellations and even fourth-moment estimates in Sections 3--4 **on the exact lattice**, not merely in the continuum.

## 5.3 The same `1/5` obstruction appears in the row Fourier integral

Nguyen--Pan's inverse characteristic theorem gives the rowwise outer factor (1.7). The number of structured neighborhoods is `p` per row, and the number/type entropy in Huang's symmetric `M` sum is at most `exp(O(p^2 log n))`. Thus the total outer-frequency contribution is negligible under exactly the same sufficient condition

\[
\exp\left\{C_dp^2\log n-c_d n/p^3\right\}=o(1),
\tag{5.7}
\]

again equivalent to (5.6) at the polynomial scale.

This identifies the **first genuine barrier after averaging**: at present, the proof controls the central saddle much farther, but the inverse-characteristic decay is only `1-c/p^2` per one-row step and each row has only `n/p` steps. The competition `n/p^3` versus a `p^2`-dimensional type entropy naturally produces the exponent `1/5`.

---

# 6. Central equidistributed estimate at `p=n^{1/5-o(1)}`

Collect the normalized central errors proved above:

\[
\begin{array}{rcl}
\text{Stirling odd cubic, averaged} &:& O_d(p^4/n),\\
\text{Stirling even quartic+higher} &:& O_d(p^4\log n/n),\\
\text{Stirling reciprocal/prefactor errors} &:& O_d(p^4/n),\\
\text{exact row denominator} &:& O_d(p^3/n),\\
\text{local cubic saddle, averaged} &:& O_d(p^4/n),\\
\text{fourth-order row remainder} &:& O_d(p^4\log n/n),\\
\text{nontrivial congruence characters} &:& \exp\{C_dp^2\log n-c_dn/p^3\},\\
\text{outer row frequencies} &:& \exp\{C_dp^2\log n-c_dn/p^3\}.
\end{array}
\tag{6.1}
\]

All Taylor arguments are uniform on Huang's equidistributed ball because

\[
\max_{ij}|p^2A_{ij}|
\le p^2\|A\|_F
=O\left(p^2\sqrt{\log n/n}\right)=o(1),
\tag{6.2}
\]

and

\[
\max_i|pr_i|
\le p\|r\|_2
=O\left(p^{3/2}\sqrt{\log n/n}\right)=o(1)
\tag{6.3}
\]

at the scale below. Each nonquadratic correction is `o(Q)` on the broad ball, so the Gaussian-tail truncations used in the averaging lemmas are legitimate.

Take

\[
x_n:=\frac{n^{1/5}}{(\log n)^2}.
\tag{6.4}
\]

By Bertrand's postulate choose a prime

\[
p_n\in[x_n,2x_n].
\tag{6.5}
\]

For fixed `d`, eventually `p_n>d`, so `p_n` is odd and `p_n` does not divide `d`. Then

\[
\frac{p_n^5\log n}{n}=O((\log n)^{-9})\to0,
\tag{6.6}
\]

while every polynomial central error in (6.1) also tends to zero. Therefore Huang's equidistributed contribution, with the exact undirected symmetry and exact congruences retained, has bounded expected number of nonzero `F_p` null vectors at this prime scale.

---

# 7. Non-equidistributed classes remain negligible at the `1/5` prime

The support cutoff in the sparse third class is

\[
O(p^3\log n)
=O\left(n^{3/5}(\log n)^{-5}\right)=o(n),
\]

so (1.2) remains valid.

Huang's other near-corner classes have exponentially small displayed bounds in `p^2 log n` once their fixed constants are chosen, and the far class has the form

\[
\exp\{-c n/p^2+O(p^2\log n)\}.
\tag{7.1}
\]

At (6.5), `n/p^2 >> p^2 log n` because `p^4 log n=o(n)`. Thus classes 1, 2, and 4 remain negligible by their class-specific derivations; Proposition 4.2 is not being invoked outside its published aggregate prime hypothesis.

Let `N_ns` be the number of nonzero `F_p` null vectors outside the sparse event. Combining Sections 6--7 in the configuration model gives

\[
E N_{ns}=O_d(1).
\tag{7.2}
\]

For fixed `d`, conditioning on simplicity costs only a fixed positive factor, so (7.2) also holds under the uniform simple `d`-regular law.

---

# 8. The `1/5` theorem

## Theorem 8.1

For every fixed integer `d>=3`, if `A_{n,d}` is the adjacency matrix of a uniformly random simple `d`-regular graph, then

\[
\boxed{
\Pr(A_{n,d}\text{ singular over }\mathbb R)
\le O_d(n^{2-d})+n^{-1/5+o(1)}.
}
\tag{8.1}
\]

In particular,

\[
\boxed{
\Pr(A_{n,3}\text{ singular})\le n^{-1/5+o(1)},
\qquad a_3\ge\frac15.
}
\tag{8.2}
\]

### Proof

Choose `p=p_n` from (6.5). By (1.2), the sparse finite-field kernel event has probability `O_d(n^{2-d})`. Outside that event, Section 7 gives `E N_ns=O_d(1)`.

If `A` is singular over `F_p` outside the sparse event, its kernel contains at least `p-1` nonzero vectors, all counted by `N_ns`. Hence

\[
(p-1)\mathbf1_{\{A\text{ singular over }F_p\}\cap E_{sp}^c}
\le N_{ns}.
\]

Taking expectations,

\[
\Pr(A\text{ singular over }F_p)
\le O_d(n^{2-d})+O_d(p^{-1}).
\tag{8.3}
\]

The adjacency matrix has integer entries. Singularity over `R` means its determinant is the integer zero, hence it is singular modulo every prime. Thus (8.3) also bounds real singularity. Finally

\[
p^{-1}=n^{-1/5+o(1)}.
\]

This proves (8.1) and (8.2). QED.

---

# 9. Noncircularity, failures, and what is *not* proved

The dependency chain is noncircular.

1. Huang supplies the undirected symmetric type formula, the exact quadratic form, the original class decomposition, and the class-specific large-deviation estimates.
2. Earlier R7-07 work supplies the field-independent sparse-support sieve; it does not use the present finite-field local-CLT improvement.
3. Nguyen--Pan is imported only for the one-row `U_{d,p}` characteristic-function inverse theorem and local cumulants. Their directed global row independence and their directed singularity exponent are not used.
4. Earlier R7-07 work supplies the exact `H/r` Gaussian decomposition and the congruence homomorphism.
5. This artifact supplies the new averaged-cumulant argument, the conserved denominator tensor (4.3), and the `p-1` support lower bound for every nontrivial weighted-row dual character.

Three tempting stronger routes fail or remain incomplete:

- **Pointwise Edgeworth control** is the wrong scale: it recreates artificial `1/6` or `1/7` barriers by forcing all rows to be simultaneously extremal.
- **A source-level `a_3=1` conclusion does not follow** from the present finite-field method, because the present outer-frequency/type-entropy comparison stops at `p^5 log n=o(n)`.
- **The exponent `1/5` is not claimed sharp for the method.** It is the first barrier under the current inverse-characteristic input. A stronger row inverse theorem, a reduction of the effective symmetric type entropy, or cancellation among outer structured neighborhoods could move it.

The full source remains OPEN-looking / worldwide status UNVERIFIED, and this result is **PARTIAL**.

---

# 10. Dated source and later-literature check — 2026-09-18

Primary source checked: Van Vu, arXiv:2005.02797, Section 5 after Theorem 5.2.  
Undirected baseline checked: Jiaoyang Huang, arXiv:1807.06465.  
Directed neighboring method checked: Nguyen--Pan, arXiv:2308.06461 / EJC 2024.  
Later fixed-degree spectral work checked in the cumulative record includes Huang--McKenzie--Yau, arXiv:2412.20263, which concerns rigidity/Ramanujan/edge universality rather than the exact zero-eigenvalue singularity exponent.

A bounded fresh search dated 2026-09-18 did not locate a later undirected fixed-degree theorem proving the source endpoint `Pr(A_{n,d} singular)=n^{-d+2+o(1)}`. This is negative evidence only, not a proof of worldwide openness or novelty.

---

# 11. Next mathematical attack

The next run must not repeat B5/B12/B24. The new exact bottleneck is

\[
\boxed{
\text{outer suppression }e^{-c n/p^3}
\quad\text{versus}\quad
\text{symmetric-type complexity }e^{O(p^2\log n)}.
}
\tag{11.1}
\]

Three nonrepeating next methods are:

1. **B1 CHANGE THE CATEGORY:** interpret the symmetric type sum as a high-dimensional theta/transport operator and try to bound its effective entropy by spectral dimension rather than ambient `p^2` dimension;
2. **B15 BREAK THE SYMMETRY ON PURPOSE:** identify whether the worst outer neighborhoods actually coexist with a symmetric admissible type, by forcing one exceptional row/frequency and solving the compatibility equations;
3. **B30 LOCALIZE:** decompose the dual-frequency matrix by support size and prove stronger suppression for large support, leaving only a low-support finite family to treat separately.

The next metric milestone is `a_3>1/5`; no stronger value is claimed here.
