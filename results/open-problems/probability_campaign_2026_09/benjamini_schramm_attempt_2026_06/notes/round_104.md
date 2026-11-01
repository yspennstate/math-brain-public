# Round 104 log

## Goal

Add an annular version of the far-leg criterion without making a false
orthogonality assumption.

## Result

Added `def:annular-square-profile`,
`prop:weighted-annular-far-leg`, and `cor:dyadic-annular-far-leg`.

For a partition \((R,\infty)=\bigsqcup_j I_j\) and weights \(a_j>0\) with
\[
  A=\sum_j a_j^{-1}<\infty,
\]
the annular profiles satisfy
\[
  \Theta_p(R)\le A\sum_j a_j\Theta_p(I_j).
\]

In particular, for dyadic annuli \(I_j=(2^j,2^{j+1}]\), the condition
\[
  \lim_{J\to\infty}\limsup_{p\uparrow p_c}
  \sum_{j\ge J}2^{\alpha(j-J)}\Theta_p(I_j)=0
\]
for some \(\alpha>0\) implies
\[
  \mathcal R_p^*/\bar\chi_p\to0.
\]

## Interpretation

The far-leg obstruction can be attacked annulus by annulus, but the annuli
are not orthogonal.  Weighted Cauchy--Schwarz gives the correct price for
turning annular estimates into a full tail estimate.
