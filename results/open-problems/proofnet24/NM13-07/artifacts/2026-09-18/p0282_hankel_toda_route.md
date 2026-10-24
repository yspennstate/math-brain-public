# P0282 new structural route — fixed-size Chen as coefficientwise Hankel/Toda positivity

Date: 2026-09-18 UTC  
Track: `proofnet24/NM13-07`  
Source: `P0282` (Chen fixed-size LIS log-concavity)

This route was prompted by the fresh literature read of Peter Clifford and Raphaël Clifford, *Exact Sampling of Permutations with a Fixed Longest Increasing Subsequence*, arXiv:2606.02263. Their Cauchy–Binet compression of Plancherel-conditioned shape weights suggests replacing explicit partition enumeration by a Hankel determinant. The identities below are exact and source-faithful; they do **not** by themselves prove Chen's conjecture.

## 1. Exact determinant coefficient for the fixed-size counts

For `r>=0` define the formal power series

\[
\mu_r(q)=\sum_{a\ge1}\frac{a^r}{(a!)^2}q^a,
\]

and for `k>=1`

\[
\tau_k(q)=\det\bigl(\mu_{i+j}(q)\bigr)_{0\le i,j<k},\qquad \tau_0(q)=1.
\]

Cauchy–Binet applied to the Vandermonde matrix gives

\[
\tau_k(q)=\sum_{1\le x_k<\cdots<x_1}
\Delta(x)^2\prod_{i=1}^k\frac{q^{x_i}}{(x_i!)^2}.
\]

Now let `lambda |- n` with `lambda_1=k`, let `rho=lambda'`, and put

\[
x_i=\rho_i+k-i\quad(1\le i\le k).
\]

Then `x_1>...>x_k>=1`,

\[
\sum_i x_i=n+\frac{k(k-1)}2,
\]

and the hook-length/Vandermonde formula used in the Clifford–Clifford sampler gives

\[
f^\lambda=n!\,\frac{\Delta(x)}{\prod_i x_i!}.
\]

Robinson–Schensted therefore yields the exact coefficient identity

\[
\boxed{
\frac{\ell_{n,k}}{(n!)^2}
=[q^{\,n+k(k-1)/2}]\,\tau_k(q).
}
\]

The smallest possible exponent in `tau_k` is

\[
b_k=1+2+\cdots+k=\frac{k(k+1)}2.
\]

Define

\[
H_k(q)=q^{-b_k}\tau_k(q)=\sum_{j\ge0}A_{k,j}q^j.
\]

Then the coefficient array has the direct source interpretation

\[
\boxed{
A_{k,j}=\frac{\ell_{k+j,k}}{((k+j)!)^2}.
}
\]

Thus Chen's fixed-`n` inequality, with defect `j=n-k`, is exactly

\[
\boxed{
A_{k,j}^2\ge A_{k-1,j+1}A_{k+1,j-1}.
}
\]

So the source conjecture is a local TP2/log-supermodularity statement on the two-parameter coefficient array of normalized Hankel tau-functions.

## 2. Toda identity

Let `D=q d/dq`. Since

\[
D\mu_r=\mu_{r+1},
\]

the standard Jacobi/Sylvester identity for Hankel determinants gives the Toda molecule relation

\[
\boxed{
\tau_kD^2\tau_k-(D\tau_k)^2=\tau_{k-1}\tau_{k+1}.
}
\]

For completeness, this is the usual determinant proof of

\[
D^2\log\tau_k=\frac{\tau_{k-1}\tau_{k+1}}{\tau_k^2};
\]

it follows by differentiating the Hankel determinant using `D mu_r=mu_{r+1}` and applying the Desnanot–Jacobi identity to the `(k+1)x(k+1)` Hankel matrix.

Because `b_{k-1}+b_{k+1}=2b_k+1`, factoring the minimal powers of `q` gives

\[
\boxed{
H_kD^2H_k-(DH_k)^2=qH_{k-1}H_{k+1}.
}
\]

Equating coefficients of `q^m` yields the exact positive convolution identity

\[
\boxed{
\frac12\sum_{r+s=m}(r-s)^2A_{k,r}A_{k,s}
=\sum_{u+v=m-1}A_{k-1,u}A_{k+1,v}.
}
\]

This is not Chen's inequality: the desired product `A_{k-1,j+1}A_{k+1,j-1}` is one term in the right-hand convolution (at `m=2j+1`), while Toda controls the entire convolution by a weighted spread of coefficients in row `k`.

## 3. Why this is a genuinely different route

The previous fixed-defect/tail-correction machinery works near the long-LIS boundary by explicit residual partitions. The Hankel/Toda formulation instead treats the whole two-dimensional array and makes the remaining obstruction precise:

> prove a coefficientwise/local TP2 consequence strong enough to isolate one off-diagonal product from the Toda convolution, or find the first coefficient pair where such a strengthening fails.

It also explains why the Poissonized theorem of Baslingker–Krishnapur–Madiman is close but not identical to the fixed-size source: the discrete Bessel/Plancherel ensemble is naturally encoded by these positive Hankel tau-functions, while fixed `n` is obtained by **coefficient extraction in `q`**. Chen is therefore a coefficientwise de-Poissonization/total-positivity problem, not merely positivity of the Poissonized generating function.

A promising next experiment is to test whether the coefficient array `A_{k,j}` itself is TP2 on a larger neighborhood than the single Chen diagonal minors, or whether suitably factorial-rescaled rows become a Pólya-frequency family. A proof would be source-level; a finite failure would identify exactly why Toda/total positivity alone is insufficient.