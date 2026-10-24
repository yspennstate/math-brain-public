# Round 437 killed-\(L^2\) annular contraction criterion

Round 437 extracts a simple sufficient condition from the annular
boundary-energy formula of Round 436.

Assume \(G\) has maximum degree \(\Delta\).  For the boundary multiplicity
\[
  \nu_u(y)=\#\{a\in S_{u-1}(x):a\sim y\},\qquad y\in S_u(x),
\]
we have
\[
  \|\nu_u\|_2^2
  \le
  \Delta\sum_{y\in S_u(x)}\nu_u(y)
  \le
  \Delta^2 |S_{u-1}(x)|.
\]
Therefore, if the killed exterior operator satisfies
\[
  \|T_p^{X_u}\|_{2\to2}\le C_{\rm kill}
\]
uniformly in \(x,u\), then
\[
  \frac{1}{|S_{u-1}(x)|}
  \sum_{a,b\in S_{u-1}(x)}R_{p,u}^x(a,b)
  \le
  p^2\Delta^2 C_{\rm kill}.
\]
Thus an averaged annular-return contraction follows whenever
\[
  p^2\Delta^2 C_{\rm kill}<1.
\]

This is a useful calibration but not yet a solution.  A uniform killed
\(L^2\) bound strong enough near \(p_c\) is close in spirit to the desired
\(p_c<p_{2\to2}\) conclusion, and the crude \(\Delta^2\) factor is likely far
too expensive in low-degree cases.  Still, the criterion identifies exactly
where an improvement could enter:

1. replace \(\Delta^2\) by the actual boundary multiplicity ratio
   \(\|\nu_u\|_2^2/|S_{u-1}(x)|\);
2. exploit killed exterior geometry to get a better bound than the ambient
   \(\|T_p\|_{2\to2}\);
3. prove a weaker density-rate estimate instead of one-step contraction
   \(<1\).

The next technical target is to estimate
\[
  \langle \nu_u,T_p^{X_u}\nu_u\rangle
\]
directly for balls, rather than through the full killed \(L^2\) norm.  This
may be easier because \(\nu_u\) is a boundary vector and \(X_u\) is an
exterior domain.
