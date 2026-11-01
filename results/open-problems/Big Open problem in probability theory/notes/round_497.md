# Round 497 root-column trace words

Round 497 makes the multi-port cone object from Round 496 more precise.

For a self-avoiding path segment inside a rooted cone with root column
\(\{r\}\times\mathbb Z\), record the ordered list of visits to the root
column:
\[
  h_0,h_1,\ldots,h_m.
\]
Self-avoidance implies that these heights are all distinct.  For each
consecutive pair \((h_i,h_{i+1})\), exactly one of the following occurs:

1. **Vertical interval:** the path moves in the root column from \(h_i\) to
   \(h_{i+1}\), using every intermediate height.  These vertical intervals
   must be pairwise disjoint except for their endpoints in the trace.
2. **Child-cone piece:** the path leaves the root column from height \(h_i\)
   into one of the \(q\) child cones and returns to the root column at
   height \(h_{i+1}\).  The chosen child label is recorded.

Thus the boundary data for a cone is not merely a finite height set.  It is a
trace word
\[
  \mathcal W=(h_0,\ell_0,h_1,\ell_1,\ldots,\ell_{m-1},h_m),
\]
where each label \(\ell_i\) is either \(V\) for a vertical interval or a child
index \(c\in\{1,\ldots,q\}\).

For a fixed child label \(c\), the subword consisting of all pairs
\[
  (h_i,h_{i+1})\quad\text{with }\ell_i=c
\]
is the multi-port boundary condition passed recursively to that child cone.
The key point is that these pairs are ordered by the global path time, not by
height order.  Arbitrary pairings of a height set are therefore the wrong
primitive; the primitive is a time-ordered trace word.

The recursive partition function should sum over trace words subject to:

* distinct root-column heights \(h_i\);
* disjointness of vertical intervals;
* for each child \(c\), recursive feasibility of the subword with label \(c\);
* the annular excess constraint along every vertical interval and at every
  child-cone entry/exit.

This trace-word formulation has two advantages.

1. It keeps the support memory missing from the free signed-run model:
   repeated use of a child cone appears as repeated occurrences of the same
   child label in the trace word.
2. It preserves the single-path nature of the object.  A child cone receives
   a subword induced by the order in which the global path visits that cone,
   not an independent family of paths.

The next upper-bound target is a trace-word norm.  For a rooted cone, define
\[
  Z_z(\mathcal W)
\]
as the partition function of paths realizing trace word \(\mathcal W\).  One
needs a bound of the form
\[
  \sum_{\mathcal W:h_0=h,\ h_m=h'}
  Z_z(\mathcal W)
  \le
  \Psi_z(h,h')
\]
where \(\Psi_z\) has subcritical annular cut norm for \(z<M_q^{-1}\).  This is
the concrete version of the interval-renewal transform from Round 495.
