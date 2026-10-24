# Round 137 log

## Goal

Thin the disjoint gate-tube obstruction so every selected gate is separated
from every selected matched endpoint.

## Result

Added `cor:cross-separated-gate-tube-obstruction` and
`prop:cross-separated-gate-tube-criterion`.

On the index set of the disjoint gate-tube obstruction, join distinct indices
\(i,k\) when
\[
  d(a_i,y_k)\le2r_p
  \quad\text{or}\quad
  d(a_k,y_i)\le2r_p .
\]
The conflict graph has degree at most \(2\Delta^{2r_p+1}\), so a greedy
independent set loses only a factor \(3\Delta^{2r_p+1}\).  Since
\[
  \Delta^{2r_p}\le\bar\chi_p^{2\theta},
\]
the resulting obstruction has size
\[
  q=
  \left\lceil
  \frac{\sigma_j^3}{48\Delta^6}\bar\chi_p^{1-14\theta}
  \right\rceil .
\]

The additional condition \(a>3\theta\) ensures the paired distance also
satisfies
\[
  d(a_i,y_i)>2r_p,
\]
because \(d(a_i,y_i)>2^j-r_p\) and \(2^j\ge a\log_\Delta\bar\chi_p\).

## Interpretation

The obstruction now consists of disjoint gate tubes and a matched annular
endpoint family with
\[
  d(a_i,y_k)>2r_p\qquad(1\le i,k\le q).
\]
Thus \(r_p\)-neighbourhoods of all selected gates are disjoint from
\(r_p\)-neighbourhoods of all selected matched endpoints.  The size exponent is
reduced from \(1-12\theta\) to \(1-14\theta\), still a positive power for
\(\theta<1/14\).
