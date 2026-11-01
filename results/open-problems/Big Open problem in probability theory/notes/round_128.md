# Round 128 log

## Goal

Move the high one-gate obstruction from remote-center annuli to annuli around
the selected gate vertices.

## Result

Added `cor:expanded-gate-annulus-obstruction` and
`prop:expanded-gate-annulus-exclusion-criterion`.

For the selected gate \(a_z\) with \(d(a_z,z)=r_p\), define
\[
  I_{j,p}^{\rm gate}=(2^j-r_p,2^{j+1}+r_p].
\]
If \(d(x,z)\in(2^j,2^{j+1}]\), then
\[
  d(x,a_z)\in I_{j,p}^{\rm gate}.
\]
Likewise, every \(y\in K\) counted by \(d(y,z)\in(2^j,2^{j+1}]\) is counted by
\[
  d(y,a_z)\in I_{j,p}^{\rm gate}.
\]

Thus the high one-gate obstruction gives
\[
  \sum_{z\in Z^\sharp}\tau_p(x,a_z)\ge\kappa_j(p)
\]
and, for every \(z\in Z^\sharp\),
\[
  \sum_{\substack{y\in K\\d(y,a_z)\in I_{j,p}^{\rm gate}}}\tau_p(y,a_z)
  \ge\kappa_j(p).
\]

## Interpretation

The remote centers are now only separated anchors.  The probabilistic mass is
measured directly at the selected boundary gates, which should be easier to
compare with annular operator or incidence estimates.
