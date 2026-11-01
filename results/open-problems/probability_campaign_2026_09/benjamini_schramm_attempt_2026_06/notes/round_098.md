# Round 098 log

## Goal

Package the far-leg square criterion as a direct route to the desired
\(L^2\)-gap theorem.

## Result

Added `cor:far-leg-tightness-l2-gap`.

Under the mean-field susceptibility bound and \(\bar\chi_p\to\infty\), if for
every \(\delta>0\) there are \(R<\infty\) and \(p_0<p_c\) such that
\[
  \Theta_p(R)
  =
  \sup_K \mathcal R_p^{>R}(K)/\bar\chi_p
  \le \delta
  \qquad(p\in[p_0,p_c)),
\]
then
\[
  p_c(G)<p_{2\to2}(G).
\]

The proof is just the established implication chain:
far-leg tightness gives \(\mathcal R_p^*/\bar\chi_p\to0\), sublinear
two-replica escape gives finite-set escape, and Hutchcroft's criterion gives
the \(L^2\) gap.

## Interpretation

The manuscript now has a single citable target for the remaining work.  A
successful separator/backscattering argument only has to prove uniform
tightness of \(\Theta_p(R)\) near criticality.
