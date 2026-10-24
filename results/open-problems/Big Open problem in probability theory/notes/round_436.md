# Round 436 annular kernels are exterior boundary energies

Round 436 connects the annular-return kernel from Round 435 to the earlier
finite-set boundary-energy program.

Fix a root \(x\) and level \(u\ge1\).  Let
\[
  E_u^+(x)=\{(a,a'): d(x,a)=u-1,\ d(x,a')=u,\ a\sim a'\}
\]
be the oriented edge boundary from \(B_{u-1}(x)\) into its exterior, and let
\[
  X_u=V\setminus B_{u-1}(x).
\]
Write \(\tau_p^{X_u}(y,z)\) for the two-point function restricted to the
induced subgraph on \(X_u\).

For \(a,b\in S_{u-1}(x)\), the annular-return event from Round 435 satisfies
\[
  R_{p,u}^x(a,b)
  \le
  p^2
  \sum_{\substack{a':(a,a')\in E_u^+(x)}}
  \sum_{\substack{b':(b,b')\in E_u^+(x)}}
  \tau_p^{X_u}(a',b').
\]
Indeed, expose the first edge from \(a\) to \(a'\in S_u(x)\), the last edge
from \(b'\in S_u(x)\) to \(b\), and the exterior connection between \(a'\)
and \(b'\) inside \(X_u\).  The displayed bound is a union bound over the
boundary-edge choices, with BK giving the same product structure when the
pieces are required disjointly.

After summing over \(a,b\in S_{u-1}(x)\), this becomes
\[
  \sum_{a,b\in S_{u-1}(x)}R_{p,u}^x(a,b)
  \le
  p^2\langle \nu_u, T_p^{X_u}\nu_u\rangle,
\]
where
\[
  \nu_u(y)=\#\{a\in S_{u-1}(x):a\sim y\},
  \qquad y\in S_u(x),
\]
and \(T_p^{X_u}\) is the killed exterior two-point operator.

Thus an averaged annular-return contraction follows from
\[
  p^2\langle \nu_u,T_p^{X_u}\nu_u\rangle
  \le
  \rho_{\rm ann}|S_{u-1}(x)|
\]
with \(\rho_{\rm ann}<1\), uniformly over the relevant roots and levels.

This is the same analytic shape as the finite-set boundary-energy term from
the last-exit decomposition, but specialized to balls and exterior killed
kernels.  The spread-return problem has therefore looped back to the core
operator target: prove that boundary mass pushed through a killed exterior
kernel has a uniform contraction coming from nonamenability.

The next obstruction is that nonamenability alone gives large boundary, not
small exterior boundary energy.  A proof needs either an \(L^2\)-type bound
on \(T_p^{X_u}\), a ball-boundary escape estimate, or an argument that many
annular returns force repeated use of disjoint boundary energies whose
product beats the entropy cost.
