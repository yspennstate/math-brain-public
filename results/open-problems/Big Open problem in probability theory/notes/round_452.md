# Round 452 annular boundary SAW exponent

Round 452 isolates the boundary-vector version of the killed SAW operator
condition.

For \(X_u=V\setminus B_{u-1}(x)\), let \(C_\ell^{X_u}\) be the length
\(\ell\) killed SAW kernel in \(X_u\).  Define the annular boundary exponent
\[
  \Gamma_{\rm ann}(G)
  =
  \limsup_{\ell\to\infty}
  \sup_{x,u,U,V}
  \left(
    \frac{\langle\nu_U,C_\ell^{X_u}\nu_V\rangle}
         {\sqrt{|U||V|}}
  \right)^{1/\ell},
\]
where \(U,V\subseteq S_{u-1}(x)\) are nonempty and
\[
  \nu_U(y)=\#\{a\in U:a\sim y,\ d(x,y)=u\}.
\]
Bounded degree constants are harmless in this normalization.

This exponent is no larger than the global SAW \(L^2\) growth exponent, but
it may be strictly smaller because it only tests:

* paths killed outside a ball;
* boundary-to-boundary vectors coming from one sphere; and
* exterior returns, not arbitrary point-to-point SAWs.

If for the \(Q\) appearing in the subdivision criterion one has
\[
  Q\Gamma_{\rm ann}(G)<1,
\]
then for every \(\epsilon>0\) and all large \(\ell\),
\[
  \langle\nu_U,C_\ell^{X_u}\nu_V\rangle
  \le
  C_\epsilon(\Gamma_{\rm ann}+\epsilon)^\ell\sqrt{|U||V|}.
\]
Summing in \(\ell\) gives the annular cut estimate
\[
  A_{Q,u,\le L}^x(U,V)\le C_Q\sqrt{|U||V|}
\]
uniformly in \(x,u,L,U,V\).

Thus \(\Gamma_{\rm ann}(G)<1/Q\) is the precise boundary-vector substitute
for the global killed SAW operator gap.  It is still a major analytic input,
but it is targeted exactly at the spread-return obstruction rather than at
all SAW propagation in the graph.

On a regular tree, \(\Gamma_{\rm ann}=0\): ball exteriors split into disjoint
forward cones, so there are no nontrivial exterior returns between distinct
vertices of \(S_{u-1}(x)\).  This calibration matches the fact that the
annular-return obstruction is purely cyclic.
