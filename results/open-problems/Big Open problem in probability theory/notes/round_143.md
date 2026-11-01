# Round 143 log

## Goal

Recover endpoint-to-anchor two-point mass in the logarithmic scale regime.

## Result

Added `cor:endpoint-anchor-scale-dichotomy`.

For \(L=\log_\Delta\bar\chi_p\) and
\[
  5\theta<a<B<\frac{1-21\theta}{2},
\]
the buffered obstruction satisfies either
\[
  2^j>BL,
\]
or, if \(2^j\le BL\), then each \(y_i\) connects deterministically to \(z_i\)
through \(a_i\) and \(\gamma_i\) using a path of length at most
\[
  2^{j+1}+2r_p\le (2B+2\theta)L.
\]
Thus
\[
  \tau_p(y_i,z_i)\ge\bar\chi_p^{-2B-2\theta}.
\]
Combining this with
\[
  \sigma_j^3\ge
  \left[\frac{\epsilon}{2}(1-2^{-\eta/2})^2\right]^3
  2^{3\eta J}(B L)^{-3\eta}
\]
gives
\[
  \sum_i \tau_p(y_i,z_i)
  \ge
  c_{\epsilon,\eta,J,\Delta,B}
  L^{-3\eta}\bar\chi_p^{1-21\theta-2B}.
\]

## Interpretation

This separates a super-logarithmic annular geometry case from a logarithmic
case where the matched endpoint-anchor pairs carry large total two-point mass.
The exponent is positive when \(B<(1-21\theta)/2\).
