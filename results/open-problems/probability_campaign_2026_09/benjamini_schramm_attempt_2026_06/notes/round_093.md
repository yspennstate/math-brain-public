# Round 093 log

## Goal

Turn the Round 092 normalization into a reusable kernel statement.

## Result

Added `cor:escape-stable-under-squaring`.

For any positive symmetric kernel \(Q\) with row sums at most one,
\[
  \eta(Q)^2\le \eta(Q^2)\le \sqrt{6\eta(Q)}.
\]
Hence, for any family \(Q_\alpha\),
\[
  \eta(Q_\alpha)\to0
  \quad\Longleftrightarrow\quad
  \eta(Q_\alpha^2)\to0.
\]

For the percolation kernels \(Q_p=T_p/\bar\chi_p\),
\[
  \eta(Q_p^2)=\mathcal R_p^*/\bar\chi_p.
\]

## Interpretation

The two-replica obstruction is exactly ordinary finite-set trapping for the
squared normalized two-point kernel.  This reframes the next target: instead
of controlling \(\|Q_p1_K\|_2\) as a separate analytic quantity, one may try to
prove that the percolation square kernel \(Q_p^2\) also escapes finite sets.
