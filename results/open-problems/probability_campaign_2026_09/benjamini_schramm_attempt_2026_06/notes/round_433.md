# Round 433 span-root split and residual tree cost

Round 433 refines the span idea from Round 432 and records its limitation.

Choose one exterior-return interval for each of the \(N\) return levels in a
spread-return witness, and form the laminar forest from Round 428.  For
\(\eta>0\), say that the forest has a large-span chain if some interval
through level \(u\) contains a descendant interval through level \(v\) with
\[
  v-u\ge \eta L_H.
\]

If there is no large-span chain, then every tree rooted at a top-level
interval has all its levels contained in an interval of radial length
\(<\eta L_H\).  Indeed, every node in a root tree is a descendant of the root,
and descendant levels are larger than the root level.  Hence each root tree
contains at most
\[
  \lceil \eta L_H\rceil
\]
selected return levels.  Therefore the number of root intervals is at least
\[
  \left\lceil \frac{N}{\lceil \eta L_H\rceil}\right\rceil.
\]
Root intervals in a laminar forest are pairwise time-disjoint.  Thus
spread-return implies the deterministic alternative:

1. a nested exterior-return pair with radial span at least \(\eta L_H\); or
2. at least \(N/\lceil\eta L_H\rceil\) pairwise disjoint root return
   intervals.

This is true but still not enough for an exponent estimate.  Since
\[
  N\simeq \delta L_H,
\]
the disjoint-root lower bound is only about \(\delta/\eta\) when \(\eta\) is
fixed.  If \(\eta\) is chosen of order \(1/L_H\), the disjoint-root branch
becomes linear, but the large-span branch only asks for fixed radial span.

The residual obstruction is now precise: a spread-return witness may consist
of only \(O(1)\) root excursions, each containing \(O(L_H)\) return levels in
a small radial band.  Controlling such a witness requires an estimate for the
internal cost of a laminar return tree, not just the number of root
excursions or the maximum root-to-descendant span.

The next target should therefore be a tree-cost lemma.  A possible form is:
for a laminar return tree rooted at level \(u\) and containing \(m\) selected
return levels in the band \([u,u+\eta L_H]\), the property-restricted radial
profile pays a cost growing with \(m\) or with a weighted sum of parent-child
level increments.  Proving such a lemma would turn the laminar structure into
an actual density-rate estimate.
