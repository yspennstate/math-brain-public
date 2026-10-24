# Round 167

Date: 2026-06-09

## Aim

Turn the large-scale open buffered tube obstruction into a dichotomy between a
polynomial tube scale and a polynomial number of opened gate tubes.

## Main addition

Added
`cor:volume-sensitive-large-scale-open-tube-dichotomy`.

Under the volume-growth hypothesis
\[
  |B(u,R)|\le C_{\rm vol}\omega^R,\qquad 1\le\omega<\Delta,
\]
and endpoint-anchor parameters
\[
  0<\theta<1/31,\qquad
  5\theta<a<B<\frac{1-21\theta}{2},
\]
the obstruction can be chosen with
\[
  2^j>B\log_\Delta\bar\chi_p.
\]
For every \(b>0\) with
\[
  \rho=1-20\theta-3\eta b>0,
\]
one has either
\[
  2^j>\bar\chi_p^b,
\]
or
\[
  \mathbb P_p\!\left(
    N_{\rm open}\ge c_{\epsilon,\eta,J,\Delta}\bar\chi_p^\rho
  \right)
  \ge
  1-\exp\!\left[
    -\frac{c_{\epsilon,\eta,J,\Delta}}4\bar\chi_p^\rho
  \right],
\]
where
\[
  c_{\epsilon,\eta,J,\Delta}
  =
  \frac{1}{864\Delta^8}
  \left[\frac{\epsilon}{2}(1-2^{-\eta/2})^2\right]^3
  2^{3\eta J}.
\]

## Proof mechanism

Start from the large-scale open buffered tube obstruction.  If
\(2^j>\bar\chi_p^b\), the first alternative holds.  Otherwise
\[
  j\le b\log_2\bar\chi_p,
\]
so
\[
  \sigma_j^3
  \ge
  \left[\frac{\epsilon}{2}(1-2^{-\eta/2})^2\right]^3
  2^{3\eta J}\bar\chi_p^{-3\eta b}.
\]
Substituting this lower bound into
\[
  \lambda_j^{\rm open}(p)
  =
  \frac{\sigma_j^3}{864\Delta^8}\bar\chi_p^{1-20\theta}
\]
gives the polynomial open-tube lower bound.

## Status

This is still an obstruction statement.  It sharpens the remaining task: either
exclude polynomial-scale buffered tubes or compare polynomially many opened
short tubes against annular/operator estimates.
