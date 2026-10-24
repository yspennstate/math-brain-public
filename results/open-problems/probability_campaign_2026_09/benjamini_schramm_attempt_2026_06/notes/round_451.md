# Round 451 killed SAW operator gap would close annular cuts

Round 451 records the clean sufficient condition suggested by Round 450.

Assume that for some \(a<1/Q\) and subexponential \(c_\ell=e^{o(\ell)}\),
every ball exterior \(X_u=V\setminus B_{u-1}(x)\) satisfies
\[
  \|C_\ell^{X_u}\|_{2\to2}\le c_\ell a^\ell
  \qquad(\ell\ge0).
\]
Then for all \(U,V\subseteq S_{u-1}(x)\),
\[
\begin{aligned}
  A_{Q,u,\le L}^x(U,V)
  &\le
  Q^2\sum_{\ell=0}^{L-2}
    Q^\ell
    \langle\nu_U,C_\ell^{X_u}\nu_V\rangle \\
  &\le
  Q^2\Delta^2\sqrt{|U||V|}
    \sum_{\ell=0}^{L-2} c_\ell (Qa)^\ell .
\end{aligned}
\]
Since \(Qa<1\), the sum is bounded uniformly in \(L\), up to a constant
depending on the subexponential sequence.  Hence
\[
  A_{Q,u,\le L}^x(U,V)
  \le
  C_Q\sqrt{|U||V|}.
\]

This gives the desired annular cut \(L^2\)-type estimate.  It would control
arbitrary endpoint weights after a dyadic decomposition, modulo the endpoint
level bookkeeping from Round 441.

However, this condition is close to the global SAW operator-gap route:
\[
  \gamma_{\rm SAW,2}(G)<1/Q.
\]
Since \(Q>\pc(G)\) in the subdivision criterion, proving such a bound for
some admissible \(Q\) would already be a strong form of the desired
\(p_c<p_{2\to2}\) mechanism.  The exterior-domain formulation may still be
weaker than a global bound, because it only tests killed operators outside
balls and boundary vectors arising from spheres, but it should be treated as
a serious analytic input rather than a cheap consequence of nonamenability.

The value of this round is calibration: the annular cut target is exactly a
localized killed-SAW \(L^2\) problem.  Any proof avoiding the global operator
gap must exploit special boundary-vector structure, not merely the norm of
\(C_\ell^{X_u}\).
