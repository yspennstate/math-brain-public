# B16 supplement — finite-difference form of the Brownian/Laplace radial coefficients

**Status:** proved source-side lemmas; full FEI remains OPEN.

This note continues `REPORT.md`.  It gives the explicit finite-difference form of the radial Krawtchouk coefficient `lambda_k` that appears in the exact retained-shell/same-syndrome identities there.

## 1. General symmetric finite-difference formula

Let

\[
F(j)=\phi\!\left((1-2j/N)^2\right),\qquad 0\le j\le N,
\]

and let `J ~ Bin(N-k,1/2)`.  For a fixed truth-table subset `A` of size `k`, conditioning on the `N-k` coordinates outside `A` gives

\[
\lambda_k^\phi
=2^{-k}\,\mathbb E_J
\sum_{\ell=0}^k(-1)^\ell\binom{k}{\ell}F(J+\ell).
\]

With `Delta F(j)=F(j+1)-F(j)`, this is

\[
\boxed{
\lambda_k^\phi
=(-1)^k2^{-k}\,\mathbb E_{J\sim\mathrm{Bin}(N-k,1/2)}
\Delta^kF(J).
}
\tag{1.1}
\]

This is exactly equivalent to the Krawtchouk formula in the main report, but it is better adapted to the ordered q-flip/Hardy side: relation size `k` is literally a `k`th discrete derivative of one scalar radial profile.

For the present squared-correlation features, `F(N-j)=F(j)`, so every odd coefficient vanishes.

For the Laplace/Shannon bank,

\[
F_t(j)=\exp\left[-t(1-2j/N)^2\right],
\]

and therefore

\[
\boxed{
\lambda_k^{\rm Lap}(t)
=(-1)^k2^{-k}\,
\mathbb E\Delta^kF_t(J).
}
\tag{1.2}
\]

No absolute value has been inserted; the alternating finite difference is the source cancellation that must be retained when matching the R16/moment ledger.

## 2. Exact Brownian-threshold boundary derivative

For `0<u<1`, away from the finitely many values `(1-2a/N)^2`, there is a unique

\[
a\in\{0,1,\ldots,N/2-1\}
\]

such that

\[
(1-2(a+1)/N)^2<u<(1-2a/N)^2.
\]

Then

\[
F_u(j)={\bf1}_{\{j\le a\}}+{\bf1}_{\{j\ge N-a\}}.
\]

Let

\[
p_m(j)=2^{-m}\binom mj,
\]

with `p_m(j)=0` outside `0,...,m`, and let

\[
\nabla p(j)=p(j)-p(j-1).
\]

### Theorem 2.1 — `P03-B16-THRESHOLD-BOUNDARY-DIFFERENCE`

For every even `k>=2`, with `m=N-k`,

\[
\boxed{
\lambda_k^{\rm th}(u)
=2^{1-k}\,\nabla^{k-1}p_{N-k}(a).
}
\tag{2.1}
\]

For odd `k`, the coefficient is zero.

### Proof

Apply (1.1) to the left step `L_a(j)=1_{j<=a}`.  The `k`th forward difference is supported only at `j=a-r`, `0<=r<=k-1`, and for even `k`

\[
\Delta^kL_a(a-r)=(-1)^r\binom{k-1}{r}.
\]

Hence

\[
\mathbb E\Delta^kL_a(J)
=\sum_{r=0}^{k-1}(-1)^r\binom{k-1}{r}p_{N-k}(a-r)
=\nabla^{k-1}p_{N-k}(a).
\]

The right step gives the same contribution by the symmetry `p_m(j)=p_m(m-j)` and evenness of `k`.  Multiplication by the factor `2^{-k}` in (1.1) yields (2.1).  Endpoint values of `u` are irrelevant to every `du` integral in the Brownian bank.  \(\square\)

Thus the Brownian source coefficient is not a generic Krawtchouk transform: it is an explicit high discrete derivative of a binomial density at the moving threshold boundary.

## 3. Exact integrated level energy

Put

\[
\mu_k=\int_0^1\lambda_k^{\rm th}(u)^2\,du.
\]

On the interval belonging to boundary index `a`, the `u`-length is exactly

\[
(1-2a/N)^2-(1-2(a+1)/N)^2
=\frac{4(N-2a-1)}{N^2}.
\]

Therefore Theorem 2.1 gives, for every even `k>=2`,

\[
\boxed{
\mu_k
=\frac{4^{\,2-k}}{N^2}
\sum_{a=0}^{N/2-1}
(N-2a-1)
\left[\nabla^{k-1}p_{N-k}(a)\right]^2.
}
\tag{3.1}
\]

This is an exact finite sum, not an asymptotic approximation.

There is also a clean universal envelope.  For `r>=0`, `m>=0`, Parseval for the generating function of the binomial law gives

\[
\sum_{a\in\mathbb Z}
[\nabla^r p_m(a)]^2
=
\frac{4^r}{\pi}
B\!\left(r+\frac12,m+\frac12\right).
\tag{3.2}
\]

Indeed, on the unit circle the Fourier multiplier of `nabla^r` is `(1-e^{-i theta})^r`, while that of `p_m` is `((1+e^{i theta})/2)^m`; the resulting beta integral is immediate.

Since `N-2a-1<=N`, (3.1)--(3.2) imply

\[
\boxed{
\mu_k
\le
\frac{4}{\pi N}
B\!\left(k-\frac12,N-k+\frac12\right),
\qquad k\ge2\ \text{even}.
}
\tag{3.3}
\]

In particular, for every fixed even `k`,

\[
\boxed{
\mu_k=O_k(N^{-k-1/2}).
}
\tag{3.4}
\]

The exact global identity from the main report is still

\[
\sum_k\binom Nk\mu_k=\frac1N.
\]

Thus (3.4) shows a useful structural fact: **the difficult Brownian source cannot live in any fixed collection of relation sizes.  Its remaining mass migrates to relation sizes growing with `N`.**  This matches the live instruction to keep the high-frequency/terminal/moment structure rather than trying to close the compiler with finitely many local relation orders.

## 4. Compiler consequence

Substituting (2.1) into the exact source identity from `REPORT.md` gives

\[
\mathbb E_S\mathcal Q_{\mathsf M}(g_S)
=4\sum_R\int_0^1
\left(
\sum_{\substack{A\in C_0\setminus D_d\\f_A=-1,\ R_A=R}}
2^{1-|A|}\nabla^{|A|-1}p_{N-|A|}(a(u))
\right)^2du.
\tag{4.1}
\]

This is now in the same formal language as a signed Hardy/finite-difference estimate: the unresolved task is a bounded operator inequality for **same-syndrome sums of binomial boundary derivatives**, not a pointwise bound on individual relation coefficients.

The beta estimate (3.3) may safely pay fixed low relation orders, but the main report's one-point obstruction shows that summing individual absolute/diagonal payments over all orders is the wrong operation.  The next useful attack is therefore to Abel-sum or telescope the sequence

\[
2^{1-k}\nabla^{k-1}p_{N-k}(a)
\]
inside each syndrome class before taking a square, and compare that signed transform to the already-proved physical `kappa_i` bank.

Full FEI remains **OPEN / NOT PROVED**.
