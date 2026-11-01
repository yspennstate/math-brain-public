# Round 090 log

## Goal

Calibrate the two-replica finite-set profile \(\mathcal R_p^*\) on the
simplest positive and negative examples.

## Regular Tree

Added `prop:tree-two-replica-profile`.  On \(T_d\), \(d\ge3\),
\[
  \lim_{p\uparrow p_c(T_d)}\mathcal R_p^*=0.
\]
The proof uses the uniform critical \(L^2\) bound on the tree:
\[
  M_d=\sup_{p\le p_c}\|T_p\|_{2\to2}<\infty.
\]
For every finite \(K\),
\[
  \mathcal R_p(K)
  =
  \frac{\|T_p\mathbf 1_K\|_2^2}{\bar\chi_p|K|}
  \le
  \frac{M_d^2}{\bar\chi_p}.
\]
Since \(\bar\chi_p\to\infty\), the profile vanishes uniformly.

## Amenable Line

Added `prop:line-two-replica-diverges`.  On \(\mathbb Z\),
\[
  \lim_{p\uparrow1}\mathcal R_p^*=\infty.
\]
For \(K_N=\{1,\ldots,N\}\) with \(N=\lceil4(1-p)^{-1}\rceil\), interior points
\(z\) satisfy
\[
  T_p\mathbf 1_{K_N}(z)\ge \frac12\bar\chi_p
\]
for \(p\) close enough to \(1\), and there are at least \(N/2\) such points.
Therefore
\[
  \mathcal R_p(K_N)\ge \frac18\bar\chi_p\to\infty.
\]

## Significance

The profile has the intended qualitative behavior: it is very small on the
regular tree near criticality and fails strongly on an amenable graph.  This
supports treating bounded \(\mathcal R_p^*\) as a plausible nonamenability
target rather than a tautological restatement of finite-set escape.
