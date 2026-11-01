# Round 041 log

## Goal

Abstract the Round 040 line-factor argument into a reusable operator criterion
for tree-indexed product graphs.

## Fiber-summed criterion

Added Proposition `prop:fiber-summed-tree` to the paper.  For a transitive
graph \(H\), put \(b=d-1\) and define
\[
  I_n(p)=\sum_{y\in V(H)}
  \mathbb P_p\bigl((o_T,o_H)\leftrightarrow (x_n,y)\bigr),
\]
where \(x_n\) is a fixed tree vertex at distance \(n\) in \(T_d\).  If
\[
  I_0(p)<\infty,\qquad
  \limsup_n I_n(p)^{1/n}<b^{-1/2},
\]
then \(T_p\) is bounded on \(\ell^2(T_d\Box H)\).

The proof decomposes the two-point kernel by tree distance.  The \(n\)th tree
shell contributes at most
\[
  \|R_n\|_{2\to2} I_n(p),
\]
where \(R_n\) is the tree sphere kernel and
\[
  \|R_n\|_{2\to2}\le C_d(n+1)b^{n/2}.
\]
The criterion follows by summing a convergent series.

## Consequence

The full line-factor proposition now becomes a corollary of this criterion
plus Yamamoto's identity
\[
  \lim_n I_n(p)^{1/n}=\alpha(p)<(d-1)^{-1/2}
  \qquad(p<p_u).
\]
This is the mechanism to try to abstract next: find non-line factors or
tree-indexed quotients where transverse summed mass has the same
sub-\(b^{-1/2}\) directional exponent.
