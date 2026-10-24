# Round 443 raw Schur bounds are too expensive

Round 443 calibrates the corrected annular SAW transfer against the trivial
bounded-degree estimate.

Let \(\Delta\) be the maximum degree.  For a fixed boundary point
\(a\in S_{u-1}(x)\), the number of self-avoiding exterior-return paths of
length \(\ell\) starting from \(a\) is at most
\[
  \Delta(\Delta-1)^{\ell-1}.
\]
Therefore the row sum of the truncated annular transfer satisfies only
\[
  \sum_b A_{Q,u,\le L}^x(a,b)
  \le
  \sum_{\ell=2}^L \Delta(\Delta-1)^{\ell-1}Q^\ell
  \le
  C_\Delta\sum_{\ell=2}^L (Q(\Delta-1))^\ell .
\]

This is not useful in the intended range.  In the subdivision criterion,
\[
  Q=q^2,\qquad q>\pc(\operatorname{Sub}(G)),
\]
so \(Q>\pc(G)\).  The universal tree-counting lower bound gives
\[
  \pc(G)\ge \frac{1}{\Delta-1},
\]
and hence the relevant \(Q\)'s are not forced below
\((\Delta-1)^{-1}\).  Typically one should expect
\[
  Q(\Delta-1)>1.
\]
The trivial Schur row sum can then grow exponentially in \(L\).

Thus the corrected annular-transfer program cannot be closed by bounding
each return interval independently with ambient degree growth.  A useful
estimate must exploit at least one of the following:

1. exact-sphere averaging in the definition of \(\mathfrak R_{r,d}\);
2. the cut/subset structure from Rounds 441--442;
3. laminar nesting, which prevents arbitrary independent placement of return
   intervals;
4. graph-specific operator geometry, such as tree-like radial \(L^2\) bounds,
   hyperbolic separation, or product backscattering.

This mirrors the earlier obstruction for unrestricted radial tails: the
ambient number of SAWs is too large precisely because the criterion asks for
control at a parameter \(Q\) above \(p_c\).  The new annular language is still
valuable, but only if it extracts structure unavailable to the raw degree
bound.
