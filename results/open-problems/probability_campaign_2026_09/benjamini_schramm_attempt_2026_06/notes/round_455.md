# Round 455 endpoint congestion is not automatically finite-set two-replica

Round 455 compares the endpoint \(L^2\) obstruction from Round 454 with the
earlier finite-set two-replica profile.

The earlier profile is percolative:
\[
  \mathcal R_p(K)
  =
  \frac{1}{\bar\chi_p|K|}
  \sum_z\left(\sum_{x\in K}\tau_p(x,z)\right)^2.
\]
It is a two-replica quantity for the normalized near-critical two-point
kernel.

The new endpoint \(L^2\) term has the same algebraic form,
\[
  \sum_{a\in S_{u-1}(x)} f(a)^2,
\]
but \(f(a)\) is a \(Q\)-weighted count of deterministic skeleton prefixes
created by deleting annular return intervals.  The parameter \(Q\) is chosen
above \(\pc(G)\) in the subdivision criterion, and the skeletons are not
percolation clusters.

Therefore endpoint congestion is not automatically controlled by the
existing finite-set two-replica theorem.  A bridge is needed.  There are two
possible routes:

1. compare the relevant \(Q\)-weighted skeleton prefix counts to near-critical
   percolation two-point mass, with enough loss control to invoke finite-set
   two-replica escape;
2. introduce a deterministic endpoint two-replica profile for the radial
   skeleton families and prove an independent exponent estimate.

This distinction matters.  Treating the deterministic endpoint \(L^2\) term
as if it were already covered by \(\mathcal R_p\) would hide the same
counting-to-probability gap that forced the correction from \(R_{p,u}\) to
\(A_{Q,u}\) in Round 438.
