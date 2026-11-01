# Round 138 log

## Goal

Separate the selected anchor tubes from all selected matched endpoints.

## Result

Added `cor:endpoint-separated-tube-obstruction` and
`prop:endpoint-separated-tube-criterion`.

Starting from Round 137, put a conflict edge between distinct indices \(i,k\)
when
\[
  d(z_i,y_k)\le2r_p
  \quad\text{or}\quad
  d(z_k,y_i)\le2r_p .
\]
The same bounded-degree count gives maximum conflict degree at most
\(2\Delta^{2r_p+1}\), so greedy thinning loses at most
\[
  3\Delta^{2r_p+1}.
\]
The resulting obstruction has size
\[
  s=
  \left\lceil
  \frac{\sigma_j^3}{144\Delta^7}\bar\chi_p^{1-16\theta}
  \right\rceil .
\]

The paired distance \(d(z_i,y_i)>2r_p\) follows from
\[
  d(z_i,y_i)\ge d(a_i,y_i)-d(a_i,z_i)>2^j-2r_p
\]
and the strengthened scale condition \(a>4\theta\).

## Interpretation

The current finite obstruction has disjoint gate-to-anchor tubes and satisfies
\[
  d(a_i,y_k)>2r_p,
  \qquad
  d(z_i,y_k)>2r_p
  \qquad(1\le i,k\le s).
\]
Thus each matched endpoint is separated from all gates and from the
\(r_p\)-neighbourhood of every anchor.  The cost is reducing the exponent from
\(1-14\theta\) to \(1-16\theta\).
