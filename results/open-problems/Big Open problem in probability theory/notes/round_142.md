# Round 142 log

## Goal

Convert the open-tube lower-tail estimate into a scale dichotomy.

## Result

Added `cor:open-tube-scale-dichotomy`.

For any \(b>0\) with
\[
  \rho=1-20\theta-3\eta b>0,
\]
the obstruction satisfies one of two alternatives.

Either the annular scale is polynomially remote:
\[
  2^j>\bar\chi_p^b,
\]
or the open-tube parameter is a positive power:
\[
  \lambda_j^{\rm open}(p)
  \ge
  c_{\epsilon,\eta,J,\Delta}\bar\chi_p^\rho.
\]
In the second case,
\[
  \mathbf P_p\left(
    N_{\rm open}\ge c_{\epsilon,\eta,J,\Delta}\bar\chi_p^\rho
  \right)
  \ge
  1-\exp[-c_{\epsilon,\eta,J,\Delta}\bar\chi_p^\rho/4].
\]

## Interpretation

The obstruction now splits into two concrete regimes: a polynomially remote
scale \(2^j>\bar\chi_p^b\), or many independently opened short tubes at a
positive-power rate.  A future proof can attack these two regimes separately.
