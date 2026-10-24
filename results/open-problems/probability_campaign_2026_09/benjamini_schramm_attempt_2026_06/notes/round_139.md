# Round 139 log

## Goal

Buffer every matched endpoint away from the full gate-to-anchor tubes, not only
from the anchor vertices.

## Result

Added `cor:buffered-tube-obstruction` and `prop:buffered-tube-criterion`.

Starting from Round 138, put a conflict edge between distinct indices \(i,k\)
when
\[
  d(z_i,y_k)\le3r_p
  \quad\text{or}\quad
  d(z_k,y_i)\le3r_p .
\]
The bounded-degree conflict count gives maximum degree at most
\[
  2\Delta^{3r_p+1}.
\]
Greedy thinning therefore loses at most \(3\Delta^{3r_p+1}\), leaving size
\[
  t=
  \left\lceil
  \frac{\sigma_j^3}{432\Delta^8}\bar\chi_p^{1-19\theta}
  \right\rceil .
\]

For the paired case, the scale condition \(a>5\theta\) gives
\[
  d(z_i,y_i)>2^j-2r_p>3r_p.
\]
Thus \(d(z_i,y_k)>3r_p\) for all selected \(i,k\).  Since
\(\gamma_i\subseteq B(z_i,r_p)\), this implies
\[
  d(v,y_k)>2r_p
  \qquad(1\le i,k\le t,\ v\in\gamma_i).
\]

## Interpretation

The obstruction now has matched endpoints separated by a full \(2r_p\) buffer
from every selected gate tube.  This is a cleaner local-independence target:
after fixing the deterministic configuration, the short tube-opening events
and the endpoint neighbourhoods live in disjoint buffered regions.  The price
is reducing the size exponent from \(1-16\theta\) to \(1-19\theta\).
