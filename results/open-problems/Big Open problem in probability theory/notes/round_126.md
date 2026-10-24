# Round 126 log

## Goal

Merge the two selected point gates from Round 125 into one boundary gate.

## Result

Added the coalesced gate energy
\[
  \mathcal J_{p,r}^I(x,K,Z,a)
  =
  \sum_{z\in Z}\tau_p(x,a_z)
  \sum_{\substack{y\in K\\d(y,z)\in I}}\tau_p(y,a_z).
\]

If \(a_z,b_z\in\{v:d(v,z)=r\}\), then \(d(a_z,b_z)\le2r\).  FKG with a fixed
geodesic from \(b_z\) to \(a_z\) gives
\[
  \mathcal J_{p,r}^I(x,K,Z,a)
  \ge
  p^{2r}\mathcal H_{p,r}^I(x,K,Z,a,b).
\]

Combining this with the point-gated obstruction gives a one-gate obstruction:
\[
  \mathcal J_{p,r_p}^{(2^j,2^{j+1}]}(x,K,Z_\theta,a)
  \ge
  p^{2r_p}
  \frac{\sigma_j^3}{8\Delta^3}\bar\chi_p^{2-4\theta}.
\]

## Interpretation

The obstruction has been reduced to a same-gate product.  In each disjoint
logarithmic ball, one boundary gate must carry both root visibility and
annular \(K\)-visibility.
