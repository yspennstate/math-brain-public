# Round 496 multi-port cone kernels are necessary

Round 496 corrects the rooted cone architecture from Round 495.

The two-height kernel
\[
  E_z(h,h')
\]
counts a single excursion that enters a child cone at height \(h\) and exits
at height \(h'\).  This is not enough for an upper bound, because a global
self-avoiding path can use the same child cone more than once at different
heights.

At a root column \(\{r\}\times\mathbb Z\), delete the root-column vertices
from a self-avoiding path.  The remaining pieces inside one child cone of
\(r\) can form several disjoint subpaths with endpoints in distinct boundary
heights of the root column.  Thus a child cone is not described by one pair
\((h,h')\), but by an ordered finite boundary set
\[
  A=\{h_1,\ldots,h_m\}\subset\mathbb Z
\]
together with a pairing or path-ordering of those boundary heights induced by
the global path.

The correct recursive object is therefore a multi-port cone kernel
\[
  E_z(\mathcal P;A),
\]
where \(A\) is a finite ordered set of boundary heights and \(\mathcal P\) is
the connectivity pattern by which the path segments inside the cone connect
the heights in \(A\).  Since the global object is a single path, \(\mathcal P\)
is not arbitrary: it is compatible with a linear order of visits along the
path.  But it can have more than one pair.

The two-point kernel is the special case \(|A|=2\).  Rounds 493--495
effectively assumed that every child cone is used at most once.  That
assumption is false.

This changes the architecture:

1. Root-column self-avoidance gives a finite ordered list of visited heights.
2. The gaps between successive root-column visits are filled either by
   vertical intervals or by child-cone multi-port configurations.
3. Each of the \(q\) child cones receives its own ordered boundary subset and
   multi-port kernel.

The norm suited to annular cuts should therefore be a partition-function norm
over finite height sets, not just an operator norm on \(\ell^2(\mathbb Z)\).
A plausible target is a polymer-type estimate: for every finite ordered
height set \(A\),
\[
  \sum_{\mathcal P} E_z(\mathcal P;A)
  \le
  C(z)^{|A|}\,\Phi_z(A),
\]
where \(\Phi_z(A)\) penalizes the span and gaps of \(A\).  Subcriticality at
\[
  z<M_q^{-1}
\]
would then follow from a cluster-expansion or renewal bound on these
height-set polymers.

This is a substantial refinement.  It avoids the false simplification that a
child cone contributes only a single two-point excursion, and it is the next
real combinatorial object needed for an upper proof.
