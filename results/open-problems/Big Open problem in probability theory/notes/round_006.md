# Round 006 log

Date: 2026-06-08

## Focus

Calibrated the killed connective constant on the regular tree.

## Result

For the \(d\)-regular tree \(T_d\), \(d\ge3\),
\[
  \kappa_{\rm kill}(T_d)=\sqrt{d-1}.
\]
Since
\[
  p_c(T_d)=\frac1{d-1},
\]
this verifies the killed-growth input
\[
  \kappa_{\rm kill}(T_d)<1/p_c(T_d).
\]

## Proof idea

Let \(q=d-1\).  The spherical operator
\[
  R_nf(x)=\sum_{y:d(x,y)=n}f(y)
\]
on \(T_d\) satisfies the tree Chebyshev/Haagerup-type estimate
\[
  \|R_n\|_{2\to2}\le C_d(n+1)q^{n/2}.
\]
For every finite \(K\), killed self-avoiding paths in \(K\) are bounded by
pairs of vertices of \(K\) at ambient distance \(n\), so
\[
  A_n(K)\le C_d(n+1)q^{n/2}.
\]
Conversely, in the ball \(B_m\), pairs of vertices at depth \(m\) in different
principal branches give killed paths of length \(2m\), yielding
\[
  A_{2m}(B_m)\gtrsim q^m.
\]

## Interpretation

The killed-growth exponent is an \(L^2\)-spherical exponent rather than the
pointwise connective constant.  This is encouraging for the conditional
finite-set escape criterion because it shows that finite-volume boundary
pressure lowers the exponent from \(d-1\) to \(\sqrt{d-1}\) on the most basic
nonamenable graph.

## Direct finite-set escape on \(T_d\)

The same spherical estimate proves the full finite-set escape condition on
regular trees.  Since
\[
  \tau_p(x,y)=p^{d(x,y)}
\]
and
\[
  \bar\chi_p=1+d\sum_{n\ge1}(d-1)^{n-1}p^n,
\]
we have uniformly over finite \(K\)
\[
  |K|^{-1}\sum_{x,y\in K}Q_p(x,y)
  \le
  \frac{C_d}{\bar\chi_p}
  \sum_{n\ge0}(n+1)(p\sqrt{d-1})^n.
\]
At \(p_c=1/(d-1)\), the series stays bounded and \(\bar\chi_p\to\infty\), so
the right-hand side tends to zero.

## Remaining gap

The boundary-energy input
\[
  \sup_K\mathcal E_p(K)\to0
  \quad(p\uparrow p_c)
\]
is still not proved in this framework.  On \(T_d\), it may be unnecessary
because finite-set escape is already obtained directly.  The next useful task
is to decide whether boundary energy also vanishes on \(T_d\), or whether the
boundary-energy condition is stronger than finite-set escape even in this
model case.
