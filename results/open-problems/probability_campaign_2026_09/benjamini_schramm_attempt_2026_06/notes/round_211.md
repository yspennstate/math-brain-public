# Round 211

Round 211 adds the subdivision reduction to bipartite graphs.

Let \(\operatorname{Sub}(G)\) be obtained by replacing every edge of \(G\) by
a path of length two.  Then
\[
  p_c(\operatorname{Sub}(G))=\sqrt{p_c(G)}
\]
and
\[
  p_{2\to2}(\operatorname{Sub}(G))=\sqrt{p_{2\to2}(G)}.
\]

For \(p_c\), percolation on the old vertices of \(\operatorname{Sub}(G)\)
is exactly percolation on \(G\) with parameter \(p^2\).

For \(p_{2\to2}\), the old-old block of the two-point operator is exactly
\[
  T_G(p^2).
\]
The old-midpoint and midpoint-midpoint blocks are bounded using the incidence
operator between vertices and edges of \(G\).  Hence \(T_{\operatorname{Sub}(G)}(p)\)
is \(L^2\)-bounded exactly when \(T_G(p^2)\) is \(L^2\)-bounded.

Therefore
\[
  p_c(G)<p_{2\to2}(G)
  \quad\Longleftrightarrow\quad
  p_c(\operatorname{Sub}(G))<p_{2\to2}(\operatorname{Sub}(G)).
\]

This makes the bipartite radial program relevant to the full target: a proof
for all bipartite subdivisions of nonamenable quasi-transitive graphs would
transfer back to all nonamenable quasi-transitive graphs.
