# Round 096 log

## Goal

Strengthen the far-root obstruction from a mixed product to an actual
far-root square-mass obstruction.

## Result

Added `cor:far-root-square-mass`.

If \(\eta(Q_{p_n}^2)\ge\epsilon>0\), then the same finite sets \(K_n\) can be
chosen so that, for every fixed \(R\),
\[
  \liminf_{n\to\infty}
  |K_n|^{-1}\sum_z
  \left(
    \sum_{\substack{x\in K_n\\ d(x,z)>R}}Q_{p_n}(x,z)
  \right)^2
  \ge \epsilon^2/16.
\]

Equivalently, with
\[
  \mathcal R_p^{>R}(K)
  =
  \frac1{\bar\chi_p|K|}
  \sum_z
  \left(
    \sum_{\substack{x\in K\\ d(x,z)>R}}\tau_p(x,z)
  \right)^2,
\]
one has
\[
  \liminf_{n\to\infty}
  \mathcal R_{p_n}^{>R}(K_n)/\bar\chi_{p_n}
  \ge \epsilon^2/16.
\]

The proof applies Cauchy--Schwarz to the Round 095 mixed far-leg product and
uses \(\|Q_{p_n}1_{K_n}\|_2^2/|K_n|\le1\).

## Interpretation

Failure of sublinear two-replica escape survives after deleting every bounded
neighborhood of the test set.  This is stronger than an ordinary one-replica
far-tail statement, which is mostly automatic near criticality; it keeps the
two-replica \(L^2\) structure that a separator/backscattering argument must
control.
