# Round 438 profile-compatible annular kernels

Round 438 corrects the annular-kernel target from Rounds 435--437 for the
radial-profile route.

The spread-return profiles are deterministic weighted self-avoiding path
counts:
\[
  \sum_d Q^d \mathfrak R_{r,d}^{G,\mathcal P},
  \qquad d=2I_x(\gamma)+H_x(\gamma).
\]
They are not probabilities of annular connections.  Thus the percolation
existence kernel
\[
  R_{p,u}^x(a,b)=\mathbf P_p(\mathcal A_u^x(a,b))
\]
does not by itself upper bound the profile contribution of return intervals.
It forgets multiplicity.  In fact \(R_{p,u}^x(a,b)\le A_{p,u}^x(a,b)\), where
\(A\) is the corresponding expected number of open annular SAW witnesses, so
an upper bound on \(R\) is too weak for a counting estimate unless a separate
multiplicity bound is proved.

The profile-compatible object is the \(Q\)-weighted exterior-return transfer
kernel
\[
  A_{Q,u}^x(a,b)
  =
  \sum_{\eta:a\to b\ {\rm exterior\ return\ through}\ u}
  Q^{|\eta|},
  \qquad a,b\in S_{u-1}(x),
\]
where the sum is over self-avoiding return subpaths whose first and last
edges enter \(S_u(x)\) and whose interior stays outside \(B_{u-1}(x)\).

This is exactly the right weight.  If
\(\eta=(w_0,\ldots,w_\ell)\) is such a return interval, then
\[
  d(x,w_0)=d(x,w_\ell)=u-1.
\]
Let \(O,I,H\) be the outward, inward, and horizontal step counts of \(\eta\)
relative to \(x\).  Since the endpoints have the same radius, \(O=I\).  Hence
the interval's defect contribution is
\[
  2I+H=O+I+H=\ell.
\]
Therefore the global weight \(Q^{2I_x(\gamma)+H_x(\gamma)}\) factors across a
marked exterior-return interval with factor \(Q^{|\eta|}\).

The boundary-energy analogue of Round 436 should therefore use the SAW
generating kernel in the killed exterior domain, not the percolation two-point
function.  If
\[
  C_Q^{X_u}(y,z)
  =
  \sum_{\eta:y\to z,\ \eta\subset X_u\ {\rm SAW}} Q^{|\eta|}
\]
is finite, then
\[
  A_{Q,u}^x(a,b)
  \le
  Q^2
  \sum_{a':(a,a')\in E_u^+(x)}
  \sum_{b':(b,b')\in E_u^+(x)}
  C_Q^{X_u}(a',b').
\]

In the actual criterion \(Q=q^2\) with \(q>\pc(\operatorname{Sub}(G))\), so
\(Q>\pc(G)\).  The untruncated \(C_Q^{X_u}\) may be infinite or much too
large.  The correct next object is therefore a truncated kernel
\[
  C_{Q,\le L}^{X_u}(y,z)
  =
  \sum_{\substack{\eta:y\to z,\ \eta\subset X_u\ {\rm SAW}\\|\eta|\le L}}
  Q^{|\eta|},
\]
with \(L\) bounded by the available defect budget in the radial profile.

Thus Rounds 435--437 remain useful as a probabilistic analogy, but they are
not yet a proof route for the deterministic spread-return profile.  The live
target is a truncated \(Q\)-weighted annular SAW transfer estimate.
