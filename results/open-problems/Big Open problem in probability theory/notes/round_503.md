# Round 503 packet-level root transform

The root trace transform must be stated at packet level, not just for a
single cone excursion.

For a cone packet
\[
  \Pi=((a_1,b_1),\ldots,(a_k,b_k)),
\]
the partition function \(E_z(\Pi)\) sums \(k\) mutually avoiding path pieces
inside the cone.  The \(j\)-th piece enters through the parent edge at height
\(a_j\) and exits through the parent edge at height \(b_j\).  These pieces
are ordered by global path time, but they are not connected to each other
inside the cone; the global path connects them through the parent side.

Therefore, at the cone root column, one must choose an ordered family
\[
  \mathfrak W=(\mathcal W^{(1)},\ldots,\mathcal W^{(k)})
\]
of compressed root trace words, where \(\mathcal W^{(j)}\) starts at \(a_j\)
and ends at \(b_j\).  The separators between the \(\mathcal W^{(j)}\)'s are
outside the cone and do not use the root column.

The self-avoidance constraints are global across the whole family:

* all root-column portal heights appearing in all \(\mathcal W^{(j)}\)'s are
  distinct;
* all vertical labels, across all pieces, form a hard-core matching of
  adjacent gaps in the increasing order of the union of portal heights;
* no vertical interval in one piece may contain a portal height belonging to
  another piece;
* for each child label \(c\), the ordered packet \(\Pi_c(\mathfrak W)\) is
  obtained by collecting all \(c\)-labeled pairs from all pieces in global
  order.

Thus the recursive transform has the schematic packet form
\[
  (\mathcal T E)_z(\Pi)
  =
  \sum_{\mathfrak W:\partial\mathfrak W=\Pi}
  {\bf 1}_{\mathrm{valid}}(\mathfrak W)\,
  \mathcal V_z(\mathfrak W)
  \prod_{c=1}^q E_z(\Pi_c(\mathfrak W)).
\]
Here \(\partial\mathfrak W=\Pi\) means that the \(j\)-th root trace starts at
\(a_j\) and ends at \(b_j\).  The case \(k=1\) is the single trace word from
Rounds 497--499.

This formulation keeps the previous norm proposals intact: the factorial
still counts packet atoms, \(E_r(\Pi)\) still measures boundary-port excess,
and \(G_\eta(A)\) should be applied to the union of all portal heights created
by the trace family.  It also makes clear that the closure proof is a
polymer estimate for a family of trace words sharing one root column, not an
ordinary one-path renewal equation.
