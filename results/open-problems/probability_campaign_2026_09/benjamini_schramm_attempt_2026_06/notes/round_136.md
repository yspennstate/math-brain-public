# Round 136 log

## Goal

Make the local gate-to-anchor paths explicit in the separated matched
obstruction.

## Result

Added `cor:disjoint-gate-tube-obstruction` and
`prop:disjoint-gate-tube-criterion`.

For every separated matched triple \((z_i,a_i,y_i)\), choose a geodesic
\(\gamma_i\) from \(a_i\) to \(z_i\).  Since
\[
  d(a_i,z_i)=r_p,
\]
the path has length \(r_p\) and lies in \(B(z_i,r_p)\).  The anchor separation
\[
  d(z_i,z_k)>4r_p
\]
implies that the paths \(\gamma_i\) are pairwise vertex-disjoint.

## Interpretation

The current obstruction can now be phrased as a separated matched annular
configuration with \(n\) disjoint short gate tubes, where
\[
  n=
  \left\lceil
  \frac{\sigma_j^3}{16\Delta^5}\bar\chi_p^{1-12\theta}
  \right\rceil .
\]
This is useful because, after fixing the deterministic configuration, the
events that all edges of the gate tubes are open are independent and have
probability \(p^{nr_p}\).  The proof still needs a way to use those independent
local tubes against the global two-replica obstruction.
