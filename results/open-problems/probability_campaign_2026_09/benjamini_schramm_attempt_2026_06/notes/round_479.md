# Round 479 symmetric portal-staircase lower bound

Round 479 strengthens the portal-staircase lower bound from Round 478 by
using large boundary sets on both sides of the annular cut norm.

Let \(q=d-1\), root at \((o,0)\), and fix two disjoint principal branches of
the tree from \(o\).  For large \(u\), let \(U\subset S_{u-1}((o,0))\) be the
vertices \((p,0)\) with \(p\) at tree depth \(u-1\) in the first branch, and
let \(V\) be the analogous set in the second branch.  Then
\[
  |U|\asymp |V|\asymp q^u.
\]

For each \(p\in U\), choose a child \(v\) of \(p\), so \((v,0)\in X_u\).  For
each \(r\in V\), choose a child \(w\) of \(r\).  There are \(q^2|U||V|\)
such endpoint choices, up to constants.

For each pair \((v,w)\), use the same Catalan portal path as in Round 478:

1. move from \((v,0)\) to \((o,u)\) by interleaving \(u\) inward tree steps
   with \(u\) upward line steps, keeping every prefix outside the ball;
2. move from \((o,u)\) to \((w,0)\) by interleaving \(u\) outward tree steps
   with \(u\) downward line steps.

Each leg has \(C_u\asymp4^u u^{-3/2}\) admissible interleavings.  The two
tree branches are disjoint, so the resulting path is self-avoiding except
for the intended join at \((o,u)\).  The length is \(4u\).

Therefore the normalized annular cut contribution is at least
\[
  \frac{C_u^2 q^2 |U||V|}{\sqrt{|U||V|}}
  \asymp
  \frac{16^u q^u}{\operatorname{poly}(u)}.
\]
Taking \(4u\)-th roots gives
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)
  \ge
  2q^{1/4}.
\]

Together with the tree out-and-back lower bound,
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)
  \ge
  \max\{\sqrt q,\ 2q^{1/4}\}.
\]

This supersedes the singleton-start \(2q^{1/8}\) bound in Round 478.  It
still does not attain the global product-shuffle value \(\sqrt q+1\) for
large \(q\), but it shows that the annular cut normalization can harvest
tree entropy from both endpoint sides of the high-\(\mathbb Z\) portal.
