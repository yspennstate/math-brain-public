# Round 434 corridor model blocks a purely radial tree-cost lemma

Round 434 stress-tests the tree-cost target from Round 433 and shows that no
purely radial laminar-tree cost can be enough.

Consider an abstract annular corridor with two radial rails and one top
connector.  The path starts at radius \(u-1\) on the left rail, moves outward
through radii
\[
  u,u+1,\ldots,u+m,
\]
crosses once at radius \(u+m\), and then moves inward on the right rail back
through radii
\[
  u+m-1,\ldots,u-1.
\]
This path is self-avoiding in the corridor graph.

For every level
\[
  w\in\{u,u+1,\ldots,u+m\},
\]
the subpath from the first visit to radius \(w-1\) on the left rail to the
last visit to radius \(w-1\) on the right rail is an exterior return through
level \(w\).  These returns form one completely nested laminar chain with
\(m+1\) selected levels.

The radial cost is only the obvious one:
\[
  I=m+1,\qquad H=1,\qquad 2I+H=2m+3.
\]
Thus the nested laminar tree pays no hidden deterministic penalty beyond the
inward steps and the single top horizontal connector.  In particular, a
laminar return tree with linearly many selected levels can be realized by a
single corridor excursion whose defect is only linear in the number of
levels.

This does not refute a graph-dependent or percolation-dependent estimate, but
it refutes the hope that laminarity alone gives a tree-cost lemma strong
enough to beat the entropy barrier.  Any successful proof must use more than
the radial distance word.  It must control the availability of annular
corridors, or replace deterministic SAW counting by a percolative
factorization estimate for exterior returns.

The revised target is therefore:

1. define an annular exterior-return kernel measuring connections in
   \(V\setminus B_{u-1}(x)\) between boundary vertices at level \(u-1\);
2. prove decay or summability for many nested or disjoint uses of these
   annular kernels;
3. use BK/Reimer or operator bounds to turn time-disjoint exterior-return
   intervals into products of annular return costs.
