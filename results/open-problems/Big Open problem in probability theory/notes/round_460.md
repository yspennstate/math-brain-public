# Round 460 product staircase lower bound for \(\Gamma_{\rm ann}\)

Round 460 stress-tests the annular boundary exponent on Cartesian products.

Let
\[
  G=T_d\square H
\]
and root \(G\) at \(x=(o,h_0)\), where \(o\in T_d\).  Fix a tree geodesic ray
from \(o\), and let \(t\) be the tree vertex at depth \(u-1\).  Put
\[
  a=(t,h_0)\in S_{u-1}(x)
\]
and let \(y=(t^+,h_0)\), where \(t^+\) is the next vertex on the ray, so
\[
  y\in S_u(x).
\]

Now let
\[
  h_0,h_1,\ldots,h_k
\]
be a geodesic self-avoiding path in \(H\), so
\[
  d_H(h_0,h_i)=i.
\]
There is an exterior staircase path in \(G\):
\[
  (t^+,h_0),
  (t^+,h_1),
  (t,h_1),
  (t,h_2),
  (t_{-1},h_2),
  \ldots,
  (t_{-(k-1)},h_k),
  (t_{-k},h_k),
\]
where \(t_{-j}\) denotes the ancestor of \(t\) at depth \(u-1-j\).  After the
initial outward edge from \(a\) to \(y\), this path takes \(k\) steps in
\(H\), each followed by an inward tree step, and then one final inward tree
step.  Equivalently, after the \(i\)th \(H\)-step it is at distance \(u+1\),
after the following inward tree step it is back at distance \(u\), and the
last inward step reaches distance \(u-1\).  Its vertices have distance at
least \(u\) from \(x\) until the final endpoint
\[
  b=(t_{-k},h_k)\in S_{u-1}(x).
\]
Thus it gives an exterior return from \(a\) to \(b\) through level \(u\).

If \(g_{\rm geo}(H)\) denotes the exponential growth rate of geodesic
self-avoiding paths in \(H\) from \(h_0\), this construction gives
\[
  \Gamma_{\rm ann}(T_d\square H)\ge \sqrt{g_{\rm geo}(H)}.
\]
The square root appears because a length-\(k\) geodesic in \(H\) creates an
annular return of length \(2k+O(1)\).

This lower bound is useful but not immediately fatal.  It is much milder than
the global product lower bound for the full SAW operator route, which contains
both tree and factor growth.  The annular return must spend tree depth to
come back to the ball boundary, so the tree branching does not enter this
simple staircase lower bound.

For example, \(H=\mathbb Z\) gives \(g_{\rm geo}(H)=1\), so this construction
only yields \(\Gamma_{\rm ann}\ge1\).  Since \(p_c(T_d\square\mathbb Z)<1\),
this does not challenge the desired annular gap.  For higher-rank amenable
factors it gives a real calibration of how much factor-geodesic entropy the
annular gap must beat.
