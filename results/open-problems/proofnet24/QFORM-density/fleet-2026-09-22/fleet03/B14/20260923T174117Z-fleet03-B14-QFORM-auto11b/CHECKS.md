# Checks for fleet03/B14 20260923T174117Z

These checks support `REPORT.md`; they are not Monte Carlo evidence for QFORM.

## Algebraic spectrum

For

\[
A_2=\begin{pmatrix}0&1&-1\\1&0&0\\-1&0&0\end{pmatrix}
\]

the characteristic polynomial is

\[
\det(\lambda I-A_2)=\lambda(\lambda^2-2),
\]

so the spectrum is exactly `{sqrt(2),-sqrt(2),0}`. The negative construction is therefore rank two and is not a counterexample to the owner target.

For the partner-control form

\[
2U_1U_2+\frac12(X+X'-\beta)^2,
\]

the hyperbolic pair block has eigenvalues `+1,-1`; the square block has eigenvalues `+1,0`. Thus its homogeneous spectrum contains exactly `1,-1,1,0` on the four active coordinates and meets the three-large-eigenvalue hypothesis.

## Interval-Frostman constants

Let `N=ceil(1/epsilon)`, `l>=epsilon`, and suppose a test interval in the unscaled `E_N` coordinate meets `m>=2` support components. The report uses

\[
R_{m,N}=\frac{m}{\sqrt{6N(m-1)}}.
\]

Since

\[
\frac{m^2}{N(m-1)}\le\frac{N}{N-1}\le2,
\]

one has `R_{m,N}<=1/sqrt(3)<1`. For a one-component intersection the ratio is at most `1/sqrt(2)`. Hence the constant `K=1` in the interval estimate is rigorous.

## Exact peak values

The exact density value is

\[
p_T(0)=\frac12\log\frac{1+\epsilon}{\epsilon}.
\]

Representative values:

- `epsilon=0.1`: `p_T(0)=1.1989476364`, `N=10`;
- `epsilon=0.01`: `p_T(0)=2.3075602584`, `N=100`;
- `epsilon=0.0001`: `p_T(0)=4.6052201835`, `N=10000`.

The divergence is analytic as `epsilon->0`; the table is only a consistency check.

## Partner-control constant

Fleet04/B14 r7 with `c=d=1`, `alpha=0` gives `theta=1`, hence

\[
4+2\log 8 = 8.15888308335967\ldots.
\]

This constant is independent of `N`, `epsilon`, `beta`, support diameter and fragment separation.
