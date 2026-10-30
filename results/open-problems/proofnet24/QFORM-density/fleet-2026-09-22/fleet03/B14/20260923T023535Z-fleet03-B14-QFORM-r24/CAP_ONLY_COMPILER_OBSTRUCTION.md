# r24 addendum — no monotone cap-only quadratic compiler survives conjugate conditioning

This addendum strengthens Theorem 3.1 of `REPORT.md`. It shows that the failure is not an artifact of assigning the common conditional cap to every coordinate: **any** coordinatewise-monotone cap-only bound with the unavoidable common-scale quadratic homogeneity pays an `N^2` tax on the same legal finite-fragment source.

## Setup

Let

\[
E_N=\bigcup_{k=1}^N[4^k,4^k+1/N],\qquad N\ge2,
\]

and let `X,X'` be iid with density `1_{E_N}`. Put

\[
U=X-X',\qquad V=X+X'.
\]

As proved in the main report, if `m_N` is the density of `U`, then

\[
\|f_{V\mid U=u}\|_\infty=M_N(u)=\frac1{2m_N(u)}.
\]

For each off-diagonal ordered pair `j != k`, the difference cluster centered at `d_{jk}=4^j-4^k` has

\[
m_N(d_{jk}+w)=\ell-|w|,\qquad |w|<\ell,\qquad \ell=1/N.
\]

Define the central half of all off-diagonal clusters by

\[
G_N=\bigcup_{j\ne k}\{d_{jk}+w:|w|\le\ell/2\}.
\]

On `G_N`,

\[
\ell/2\le m_N(u)\le\ell,
\]

so

\[
\boxed{N/2\le M_N(u)\le N.}
\]

Moreover its exact `U`-probability is

\[
\begin{aligned}
\Pr\{U\in G_N\}
&=N(N-1)\int_{-\ell/2}^{\ell/2}(\ell-|w|)\,dw\\
&=N(N-1)\frac{3\ell^2}{4}\\
&=\boxed{\frac34\left(1-\frac1N\right)}.
\end{aligned}
\]

In particular this probability is at least `3/8` for every `N>=2`.

## Theorem — QFORM-NO-MONOTONE-CAP-ONLY-CONJUGATE-COMPILER-v1

Fix an integer `r>=1`. Let

\[
F:(0,\infty)^r\to[0,\infty]
\]

be coordinatewise nondecreasing and suppose it has the common-scale homogeneity forced by a quadratic-output density estimate,

\[
F(tM_1,\dots,tM_r)=t^2F(M_1,\dots,M_r),\qquad t>0,
\]

with `F(1,...,1)>0`.

Take `r` independent copies of the above pair construction and condition on the difference vector `U=(U_1,...,U_r)`. Then

\[
\boxed{
\mathbb E\,F(M_N(U_1),\dots,M_N(U_r))
\ge
\left[\frac34\left(1-\frac1N\right)\right]^r
\frac{N^2}{4}F(1,\dots,1).
}
\]

Consequently the averaged cap-only proof constant diverges at least quadratically in `N`.

### Proof

The events `{U_i in G_N}` are independent. On their intersection every `M_N(U_i)>=N/2`. Coordinatewise monotonicity gives

\[
F(M_N(U_1),\dots,M_N(U_r))
\ge F(N/2,\dots,N/2)
=\frac{N^2}{4}F(1,\dots,1).
\]

Multiplying by the probability of the intersection proves the claim. ∎

## Why degree two is intrinsic here

If all active input densities have a common cap `M`, put `Y_i=M X_i`. Then `Y_i` have cap one and for any quadratic form `q_H(x)=x^T Hx`,

\[
q_H(X)=M^{-2}q_H(Y).
\]

A one-dimensional output density therefore scales by `M^2`. Thus any cap-only conditional density certificate that respects the physical scaling of the problem necessarily has common-scale degree two. The fleet04/B14 r6 leakage-core estimate does so exactly: `K_H(M)=M^2K_H(1)`.

Hence no anisotropic repackaging which remembers only the conditional caps and is monotone in those caps can repair the conjugate-conditioning route. The obstruction persists even if one avoids the crude `max_i M_i`: on a fixed positive-probability event all caps are simultaneously of order `N`, forcing the quadratic tax.

## Scope

This is a proof-architecture obstruction, **not** a counterexample to QFORM. The source laws are legal cap-one compact finite-fragment extremes. What fails is the sequence

1. condition on sum/difference fibers;
2. replace each fiber by only its normalized density cap(s);
3. invoke a quadratic-output theorem whose constant is a monotone cap-only function;
4. average the resulting constants.

A successful decoupled proof must retain more than the cap number: in particular the unnormalized overlap mass/geometry must remain coupled to the quadratic phase until after smoothing is extracted.
