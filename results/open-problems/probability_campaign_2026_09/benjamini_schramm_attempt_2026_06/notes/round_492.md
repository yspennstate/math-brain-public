# Round 492 support-tree and edge-height representation

Round 492 separates the tree branching factor from the remaining
height-order entropy.

Let \(\gamma\) be a self-avoiding path in \(T_d\square\mathbb Z\), and let
\(\pi_T\gamma\) be its projection to the tree.  Let \(S(\gamma)\) be the
minimal tree subtree containing all tree vertices visited by \(\pi_T\gamma\).
For each tree edge \(e\in E(S(\gamma))\), let
\[
  H_e=\{z\in\mathbb Z:\gamma\text{ crosses }e\text{ at height }z\}.
\]
Self-avoidance implies that no height appears twice in \(H_e\): crossing the
same tree edge at the same height would require revisiting at least one of
the two endpoint vertices in \(T_d\square\mathbb Z\).

Let
\[
  a=\#\{\text{tree-coordinate steps of }\gamma\},\qquad
  D=d_T(\pi_T\gamma(0),\pi_T\gamma(n)).
\]
If \(K=|E(S(\gamma))|\), then
\[
  K\le \frac{a+D}{2}.
\]
Indeed, every edge of \(S(\gamma)\) must be crossed at least once, while the
edges on the geodesic between the tree endpoints are crossed an odd number
of times and all other support edges are crossed an even number of times.

Therefore the number of branch choices for a fixed abstract support tree is
at most \(q^K\).  In the annular \(L^2\) cut norm, endpoint averaging supplies
the usual tree Haagerup factor \(q^{D/2}\).  Thus the net tree branching cost
is bounded by
\[
  q^{K-D/2}
  \le
  q^{a/2}.
\]

This proves that the desired \(q^{a/2}\) factor does not require a mysterious
local cancellation.  It follows from:

1. counting branch choices by the number of distinct support-tree edges,
   rather than by the number of tree steps;
2. using endpoint \(L^2\) normalization to pay for the tree endpoint
   displacement.

The entire remaining difficulty is now the labeled traversal problem:

> Count possible abstract support-tree traversals, edge crossing heights
> \(H_e\), and vertical moves, subject to self-avoidance and the annular
> excess constraint, after the branch factor has already been reduced to
> \(q^{a/2}\).

The fresh-column vertical-run obstruction from Round 490 is exactly the case
where \(K=a\), so there are no repeated edge crossings; all entropy sits in
vertical runs across fresh support edges.  Stack-return families have
\(K<a\), and their extra crossings must use distinct heights in the same
support edges.  The corrected master upper target from Round 491 is now a
statement about this height-labeled traversal entropy, not about tree
branching itself.
