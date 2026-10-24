# Round 493 fixed-height run decomposition is too crude

Round 493 tests the most direct upper-counting scheme after the support-tree
reduction.

Decompose a self-avoiding path in \(T_d\square\mathbb Z\) into alternating
maximal runs:

1. fixed-height tree runs, where the path moves only in the tree at a single
   \(\mathbb Z\)-height;
2. vertical runs, where the path moves monotonically in one tree column.

Every fixed-height tree run is a simple path in \(T_d\).  The tree Haagerup
bound gives an \(L^2\) cost
\[
  \sum_{m\ge1}(\sqrt q\,z)^m
  =
  \frac{\sqrt q\,z}{1-\sqrt q\,z}
\]
for a nonempty tree run.  A crude vertical-run inventory is
\[
  \sum_{\ell\ge1}2z^\ell
  =
  \frac{2z}{1-z}.
\]
If these two run types could be alternated freely, the singularity would be
given by
\[
  \frac{\sqrt q\,z}{1-\sqrt q\,z}
  \cdot
  \frac{2z}{1-z}
  =
  1.
\]
Equivalently,
\[
  q_{\rm run}(z):=
  q^{1/2}z^2+(\sqrt q+1)z-1=0,
\]
and the corresponding exponential rate is
\[
  R_{\rm run}(q)
  =
  \frac{\sqrt q+1+\sqrt{q+6\sqrt q+1}}{2}.
\]

This upper envelope is too large.  For example,
\[
  R_{\rm run}(3)=3.262\ldots>3,
\]
so even the embedded-tree inverse threshold would not prove an annular gap in
the \(q=3\) case.  The estimate also misses the corrected target
\[
  M_q=\max\{\sqrt q+1,\sqrt{1+4\sqrt q}\}.
\]

The loss comes from treating the signs and depth changes of tree runs as
free.  A tree run can move inward, outward, or turn once in the rooted tree,
and the vertical run can move up or down, but the annular excess
\[
  e=d_T(o,v)+|z|-u
\]
must remain nonnegative and return to zero at the boundary.  The fresh-column
model in Round 490 keeps this excursion information and gets the sharper
\(\sqrt{1+4\sqrt q}\) scale.  The stack-return model must likewise retain
the excess change of each tree run, not merely its length.

Thus the next upper model needs a signed tree-run inventory, tracking
\[
  \Delta=d_T(o,v_{\rm after})-d_T(o,v_{\rm before}),
\]
together with vertical-run sign.  The crude length-only run decomposition is
not enough.
