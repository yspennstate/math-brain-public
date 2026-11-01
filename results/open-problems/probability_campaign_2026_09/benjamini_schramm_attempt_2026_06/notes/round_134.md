# Round 134 log

## Goal

Convert the localized gate-incidence obstruction into a matched finite metric
configuration.

## Result

Added `lem:left-degree-matching-extraction`,
`cor:matched-anchored-incidence-obstruction`, and
`prop:matched-anchored-incidence-criterion`.

The localized obstruction defines a finite bipartite graph with left side the
gate set \(A\), right side \(Y\), and edges
\[
  ay \quad\Longleftrightarrow\quad d(a,y)\in I_{j,p}^{\rm gate}.
\]
It satisfies
\[
  |A|\ge\widehat\kappa_j(p),
  \qquad
  \deg(a)\ge\widehat\kappa_j(p)\quad(a\in A).
\]
With
\[
  m=\left\lceil\widehat\kappa_j(p)\right\rceil,
\]
integer cardinalities give \(|A|\ge m\) and all left degrees at least \(m\).
Hall's theorem then gives a matching of size \(m\).

## Interpretation

The obstruction can now be stated as \(m\) distinct anchored gate-to-vertex
pairs:
\[
  (z_i,a_i,y_i),\qquad 1\le i\le m,
\]
with separated anchors, distinct gates, distinct matched vertices, the improved
scale lower bound \(2^j\ge a\log_\Delta\bar\chi_p\), and all gate and matched
vertices in the prescribed annuli around the root or the gate.

This removes the remaining unmatched incidence cloud from the finite
configuration.  The next useful target is to prove that such a large matched
annular configuration is impossible in nonamenable quasi-transitive graphs, or
to find a structural mechanism that converts it into the desired
finite-set-escape estimate.
