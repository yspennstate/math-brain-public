# Round 097 log

## Goal

Turn the far-root square-mass obstruction into an equivalent uniform tightness
criterion.

## Result

Added `prop:far-leg-square-criterion`.

For \(R<\infty\), define
\[
  \Theta_p(R)=
  \sup_K \mathcal R_p^{>R}(K)/\bar\chi_p.
\]
Then
\[
  \mathcal R_p^*/\bar\chi_p\to0
\]
if and only if for every \(\delta>0\) there are \(R<\infty\) and \(p_0<p_c\)
such that
\[
  \Theta_p(R)\le\delta\qquad(p\in[p_0,p_c)).
\]

The proof decomposes
\[
  Q_p1_K=u_{\le R}+u_{>R}.
\]
The far part is exactly \(\mathcal R_p^{>R}(K)/\bar\chi_p\).  The near part
is uniformly negligible for fixed \(R\):
\[
  |K|^{-1}\|u_{\le R}\|_2^2\le V_R^3/\bar\chi_p^2.
\]

## Interpretation

The sublinear two-replica problem is equivalent to uniform tightness of the
two-replica square mass in leg length.  Any future separator or backscattering
argument can target \(\Theta_p(R)\): choose a large but fixed radius \(R\),
then prove that the square mass from legs longer than \(R\) is small uniformly
near criticality.
