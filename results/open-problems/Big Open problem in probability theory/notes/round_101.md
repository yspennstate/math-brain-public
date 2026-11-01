# Round 101 log

## Goal

Record a simple spectral sufficient condition for far-leg tightness.

## Result

Added `cor:operator-tail-l2-gap`.

For
\[
  T_p^{>R}(x,y)=\tau_p(x,y)\mathbf 1\{d(x,y)>R\},
\]
we have
\[
  \Theta_p(R)
  \le
  \left(\frac{\|T_p^{>R}\|_{2\to2}}{\bar\chi_p}\right)^2 .
\]
Therefore, under the mean-field susceptibility bound and
\(\bar\chi_p\to\infty\), the spectral tail condition
\[
  \lim_{R\to\infty}\limsup_{p\uparrow p_c}
  \frac{\|T_p^{>R}\|_{2\to2}}{\bar\chi_p}=0
\]
implies \(p_c(G)<p_{2\to2}(G)\).

## Interpretation

This is stronger than the exact \(\Theta_p(R)\) criterion, but it is a clean
operator-norm target.  It may be useful for geometries where long-distance
two-point kernels can be decomposed into shells or separator layers.
