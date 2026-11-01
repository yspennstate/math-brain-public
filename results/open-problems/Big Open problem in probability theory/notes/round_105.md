# Round 105 log

## Goal

Turn the annular far-leg criterion into an operator-norm target.

## Result

Added `def:annular-two-point-operator`, `lem:annular-operator-control`, and
`cor:dyadic-annular-operator`.

For
\[
  T_p^I(x,y)=\tau_p(x,y)\mathbf 1\{d(x,y)\in I\},
\]
we have
\[
  \Theta_p(I)\le
  \left(\frac{\|T_p^I\|_{2\to2}}{\bar\chi_p}\right)^2 .
\]

Thus, for dyadic annuli \(I_j=(2^j,2^{j+1}]\), the estimate
\[
  \lim_{J\to\infty}\limsup_{p\uparrow p_c}
  \sum_{j\ge J}2^{\alpha(j-J)}
  \left(\frac{\|T_p^{I_j}\|_{2\to2}}{\bar\chi_p}\right)^2=0
\]
implies \(\mathcal R_p^*/\bar\chi_p\to0\), and with mean-field susceptibility
gives \(p_c<p_{2\to2}\).

## Interpretation

This criterion is weaker than demanding an \(\ell^1\) tail of exact-shell
operator norms.  It allows dyadic grouping and square summability with a
controlled Cauchy--Schwarz price.
