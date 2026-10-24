# Round 178

Round 178 calibrates the capped gate-annular operator criterion against the
trivial global Schur bound.

For every annulus \(I\),
\[
  \|T_p^I\|_{2\to2}\le \bar\chi_p.
\]
Therefore the capped operator lower bound from Round 176 cannot occur whenever
\[
  \beta(\theta,U,\omega)>1.
\]
Indeed, the Round 176 lower bound would be
\[
  \|T_p^{I_{j,p}^{\rm gate}}\|_{2\to2}
  \ge
  C_{\epsilon,\eta,J,U,C_{\rm vol}}
  (\log_\Delta\bar\chi_p)^{-6\eta}
  \bar\chi_p^{\beta(\theta,U,\omega)},
\]
which is larger than \(\bar\chi_p\) near criticality if \(\beta>1\).

Consequently, in the \(\beta>1\) parameter regime, any volume-sensitive
counterexample must carry the full expanded gate-annulus obstruction data at
scale
\[
  2^j>U\log_\Delta\bar\chi_p.
\]
The capped-operator branch is only a live analytic target in the regime
\(\beta\le1\).  This prevents a false route: one should not try to prove a
separate capped operator upper bound below a superlinear power of
\(\bar\chi_p\), since Schur already supplies that upper bound.
