# P0458 — exact finite-`n` factorial moments at the one-missing-choice boundary

Date: 2026-09-19 UTC  
Worker: `R7-03`  
Target: `P0458`  
Purpose: substantive proof-hardening of the already source-solved standardized-degree problem; this note does **not** change the frozen metric `R_unresolved=0` and is not an independent audit.

## 1. Setup

Work in the bilateral preference graph `LK(n,k)` with iid continuous edge weights, using iid `Uniform(0,1)` weights without loss of generality. This note treats the exact dense boundary

\[
k=n-2.
\]

Thus each vertex prefers all but its unique largest incident edge. Fix a root `0`, let `D_n` be its degree, and put

\[
H_n:=k-D_n=n-2-D_n.
\]

The previously proved fixed-complement theorem corresponds here to `r=n-1-k=1` and gives only the limiting mixed-Poisson description plus first-two-moment convergence. The goal here is stronger in this special case: compute **every finite-`n` falling-factorial moment exactly**.

Write

\[
x^{\underline m}:=x(x-1)\cdots(x-m+1).
\]

## 2. B18 — say the model in the language of maximal-edge arrows

When `k=n-2`, every vertex rejects exactly its largest incident edge. For a neighbor `i` of the root, define `I_i=1` exactly when

1. `(0,i)` is **not** the largest edge at the root, so the root proposes it; and
2. `(0,i)` **is** the largest edge at `i`, so `i` rejects it.

Then

\[
H_n=\sum_{i=1}^{n-1} I_i.
\]

Thus `H_n` counts a simple maximal-edge arrow pattern: neighbors whose unique maximal incident edge points to the root, excluding the unique edge that is maximal at the root itself.

This reformulation makes an exact joint-event integral possible.

## 3. B3 — exact theorem for all finite falling-factorial moments

### Theorem

For every `n>=3` and every integer `1<=m<=n-1`,

\[
\boxed{
\mathbb E\!\left[H_n^{\underline m}\right]
=
\frac{(n-1)^{\underline{m+1}}}
{(m+1)\displaystyle\prod_{j=1}^{m+1}
\left(n-\frac{j+1}{2}\right)}.
}
\tag{3.1}
\]

Equivalently,

\[
\boxed{
\mathbb E\!\left[H_n^{\underline m}\right]
=
\frac1{m+1}
\prod_{j=1}^{m+1}
\frac{n-j}{n-(j+1)/2}.
}
\tag{3.2}
\]

In particular, for every fixed `m`,

\[
\mathbb E\!\left[H_n^{\underline m}\right]
=
\frac1{m+1}-\frac{m}{4n}+O_m(n^{-2}),
\tag{3.3}
\]

so the full factorial-moment sequence converges to `1/(m+1)`.

### Proof

Fix an ordered `m`-tuple of distinct neighbors `i_1,...,i_m`. Let

\[
u_a:=U_{0i_a},\qquad 1\le a\le m,
\]

and put `M=max_a u_a`.

Conditional on these `m` root-edge weights, all the events `I_{i_a}=1` occur if and only if the following three independent edge-set conditions hold.

First, none of the chosen root edges may be the root's unique maximum. Among the `n-1-m` remaining root edges, at least one must exceed `M`. This has conditional probability

\[
1-M^{n-1-m}.
\tag{3.4}
\]

Second, for each chosen neighbor `i_a`, every edge from `i_a` to a non-root, non-chosen vertex must lie below `u_a`. There are `n-m-1` such edges for each `a`, producing

\[
\prod_{a=1}^m u_a^{\,n-m-1}.
\tag{3.5}
\]

Third, for every pair `a<b`, the shared edge `(i_a,i_b)` must be below both root-edge thresholds, hence below `min(u_a,u_b)`. These shared edges are mutually distinct, producing

\[
\prod_{1\le a<b\le m}\min(u_a,u_b).
\tag{3.6}
\]

Therefore

\[
\mathbb P(I_{i_1}=\cdots=I_{i_m}=1)
=
\int_{[0,1]^m}
(1-M^{n-1-m})
\prod_{a=1}^m u_a^{n-m-1}
\prod_{a<b}\min(u_a,u_b)
\,du.
\tag{3.7}
\]

The integrand is symmetric. Restrict to the ordered simplex

\[
0<u_1<\cdots<u_m<1
\]

and multiply by `m!`. On this simplex, `M=u_m` and

\[
\prod_{a<b}\min(u_a,u_b)
=
\prod_{a=1}^m u_a^{m-a}.
\]

Thus the exponent of `u_a` becomes

\[
(n-m-1)+(m-a)=n-a-1.
\]

Define

\[
\alpha_a:=n-a,
\qquad
S_j:=\sum_{a=1}^j\alpha_a
=jn-\frac{j(j+1)}2
=j\left(n-\frac{j+1}{2}\right).
\tag{3.8}
\]

Successively integrating `u_1,...,u_{m-1}` leaves

\[
\frac1{\prod_{j=1}^{m-1}S_j}
\int_0^1
u_m^{S_m-1}
\left(1-u_m^{n-1-m}\right)
\,du_m.
\]

The final integral equals

\[
\frac1{S_m}-\frac1{S_m+n-1-m}.
\tag{3.9}
\]

But

\[
S_m+n-1-m
=(m+1)\left(n-\frac{m+2}{2}\right)
=S_{m+1}.
\]

Hence the ordered-simplex integral is

\[
\frac{n-m-1}{\prod_{j=1}^{m+1}S_j}.
\tag{3.10}
\]

There are `(n-1)^{\underline m}` ordered `m`-tuples of distinct neighbors, so by the standard falling-factorial expansion

\[
\mathbb E[H_n^{\underline m}]
=(n-1)^{\underline m}m!
\frac{n-m-1}{\prod_{j=1}^{m+1}S_j}.
\tag{3.11}
\]

Using

\[
(n-1)^{\underline m}(n-m-1)
=(n-1)^{\underline{m+1}}
\]

and

\[
\prod_{j=1}^{m+1}S_j
=(m+1)!\prod_{j=1}^{m+1}
\left(n-\frac{j+1}{2}\right),
\]

(3.11) becomes (3.1). Formula (3.2) is the same identity after factoring each numerator term. Expanding its logarithm at fixed `m` gives

\[
\sum_{j=1}^{m+1}
\left[
\log\left(1-\frac jn\right)
-
\log\left(1-\frac{j+1}{2n}\right)
\right]
=-\frac{m(m+1)}{4n}+O_m(n^{-2}),
\]

which proves (3.3).  `\square`

The endpoint `m=n-1` is included: both sides vanish because `H_n<=n-2` and `(n-1)^{\underline n}=0`.

## 4. Exact mean and variance at finite `n`

Taking `m=1` in (3.1) gives

\[
\boxed{
\mathbb E H_n=\frac{n-2}{2n-3}.
}
\tag{4.1}
\]

Taking `m=2` gives

\[
\boxed{
\mathbb E[H_n(H_n-1)]
=\frac{2(n-3)}{3(2n-3)}.
}
\tag{4.2}
\]

Therefore

\[
\boxed{
\operatorname{Var}(H_n)
=
\frac{7n^2-27n+24}{3(2n-3)^2}.
}
\tag{4.3}
\]

Since `D_n=n-2-H_n`, the same variance is `Var(D_n)`. Expanding,

\[
\mathbb E H_n
=\frac12-\frac1{4n}-\frac3{8n^2}+O(n^{-3}),
\tag{4.4}
\]

\[
\operatorname{Var}(D_n)
=\frac7{12}-\frac1{2n}-\frac{13}{16n^2}+O(n^{-3}).
\tag{4.5}
\]

This gives explicit finite-size corrections to the previously proved `r=1` limiting constants `mu_1=1/2` and `nu_1=7/12`.

## 5. The limiting law becomes a uniform mixed Poisson law

The previous fixed-complement theorem says that for fixed `r`,

\[
H_n\Longrightarrow H_r,
\qquad
H_r\mid A_r=a\sim\operatorname{Poisson}(\Lambda_r(a)),
\]

where `A_r~Gamma(r,1)` and

\[
\Lambda_r(a)
=e^{-a}\sum_{\ell=0}^{r-1}(r-\ell)\frac{a^\ell}{\ell!}.
\]

For `r=1`, `A_1~Exp(1)` and

\[
\Lambda_1(A_1)=e^{-A_1}.
\]

If `U=e^{-A_1}`, then `U~Uniform(0,1)`. Hence

\[
\boxed{
H_1\mid U\sim\operatorname{Poisson}(U),
\qquad U\sim\operatorname{Uniform}(0,1).
}
\tag{5.1}
\]

Consequently, for every integer `j>=0`,

\[
\boxed{
\mathbb P(H_1=j)
=\frac1{j!}\int_0^1e^{-u}u^j\,du
=1-e^{-1}\sum_{\ell=0}^j\frac1{\ell!}.
}
\tag{5.2}
\]

The falling-factorial moments are

\[
\boxed{
\mathbb E[H_1^{\underline m}]
=\mathbb E[U^m]
=\frac1{m+1}.
}
\tag{5.3}
\]

Thus the exact finite formula (3.1) converges term-by-term to the complete factorial-moment sequence of the limiting mixed-Poisson law, not merely its first two moments.

The standardized `r=1` boundary law can therefore be written explicitly as

\[
L_1=\frac{1/2-H_1}{\sqrt{7/12}},
\qquad
H_1\sim\operatorname{Poisson}(U),\ U\sim\operatorname{Unif}(0,1).
\tag{5.4}
\]

## 6. General fixed-complement limit: all factorial moments

The same mixed-Poisson representation gives a useful exact strengthening for every fixed `r`, although this section claims a formula for the **limit variable** `H_r`, not a finite-`n` all-moment theorem.

For every integer `m>=1`, conditional Poisson factorial moments give

\[
\mathbb E[H_r^{\underline m}]
=\mathbb E[\Lambda_r(A_r)^m].
\]

Expanding the finite polynomial in `Lambda_r` and integrating against the `Gamma(r,1)` density yields

\[
\boxed{
\mathbb E[H_r^{\underline m}]
=
\frac1{(r-1)!}
\sum_{\ell_1,\ldots,\ell_m=0}^{r-1}
\frac{\prod_{a=1}^m(r-\ell_a)}{\prod_{a=1}^m\ell_a!}
\frac{(r+\ell_1+\cdots+\ell_m-1)!}
{(m+1)^{r+\ell_1+\cdots+\ell_m}}.
}
\tag{6.1}
\]

For `m=1`, this recovers the exact `mu_r` formula. For `m=2`, it recovers the existing second-factorial-moment term underlying the finite-sum variance formula. For `r=1`, the sum has one term and reduces to `1/(m+1)`.

## 7. B16 — exact finite arithmetic check

The companion exact-arithmetic script

`research7_2026-09-17/R7-03/artifacts/2026-09-19/2026-09-19T093100Z__P0458_r1_factorial_check.py`

checks the ordered-simplex formula against the closed form (3.1) with Python `Fraction` arithmetic for all `3<=n<=30` and every `1<=m<=n-1` (434 exact `(n,m)` pairs), checks (4.1)–(4.3), and checks the first seven `r=1` limiting factorial moments from (6.1). Its archived output ends in

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not P26, not an OTHER-track audit, and not a substitute for the written proof above.

## 8. What this changes and what it does not

The source-level P0458 endpoint was already mathematically proved in the preceding R7-03 runs. Therefore the frozen metric remains

`R_unresolved: 0 -> 0 (NO MOVEMENT)`.

This artifact does materially strengthen the proof package: the most delicate dense boundary now contains an exact finite-`n` theorem for every factorial moment and an explicit closed-form limiting pmf. It also independently matches the previously obtained `mu_1` and `nu_1`.

Protocol closure is unchanged: the package still requires an actual P26 full-proof PASS and one distinct OTHER-track full-proof PASS. Negative literature searches remain negative evidence only.