# Round 218

Round 218 isolates the midpoint-root subdivision comparison.

Let \(r\) be a midpoint in \(H=\operatorname{Sub}(G)\), adjacent to old
vertices \(u_0,u_1\).  A SAW from \(r\) first chooses one of these old
vertices.  Deleting that first half-edge gives a SAW from \(u_j\).  If the
endpoint is in \(S_m^H(r)\), then its distance from \(u_j\) is \(m-1\) or
\(m+1\).

Since \(H\) is bipartite,
\[
  I_r(\gamma)=\frac{|\gamma|-m}{2},
  \qquad
  I_{u_j}(\gamma')=\frac{|\gamma|-1-d_H(u_j,a)}{2}.
\]
Thus deleting the first half-edge preserves the inward count in the
\(m-1\) case and lowers it by one in the \(m+1\) case.

The resulting midpoint-root average is controlled by adjacent old-root
profiles if the shifted sphere comparison
\[
  |S_{m-1}^H(u_j)|,\ |S_{m+1}^H(u_j)|
  \le C|S_m^H(r)|
\]
holds.  This identifies the remaining geometric input needed to turn the
old-root subdivision comparisons into full subdivision inward-profile
control.
