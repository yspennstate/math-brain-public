# Round 470 finite-fiber tree products reduce to bounded-width transfers

Round 470 records the next calibration target suggested by the exact
\(T_d\square K_2\) computation.

Let \(F\) be a finite connected graph, fix \(f_0\in F\), and set
\[
  G=T_d\square F,\qquad x=(o,f_0),\qquad q=d-1.
\]
Write
\[
  h(f)=d_F(f_0,f),\qquad R=\max_{f\in F} h(f).
\]
Then
\[
  d_G(x,(v,f))=d_T(o,v)+h(f).
\]
For large \(u\), the exterior \(X_u=V\setminus B_{u-1}(x)\) has no vertices
whose tree coordinate has depth less than \(u-R\).  Hence every component is
contained in the descendant cone of a unique tree vertex \(a\) at depth
\(u-R\); the component over \(a\) consists of the decorated descendant cone
\[
  \{(w,f): w\text{ descends from }a,\,
          d_T(a,w)+h(f)\ge R\}.
\]
Its boundary ports in \(S_{u-1}(x)\) have bounded relative depth.  There are
two types:

1. descendant-side ports \((w,f)\), where \(w\) descends from \(a\),
   \(d_T(a,w)+h(f)=R-1\), and \((w,f)\) has an edge into the decorated cone;
2. parent-side ports \((\operatorname{par}(a),f)\) with \(h(f)=R\), adjacent
   to \((a,f)\).

For \(F=K_2\), these are exactly the ports
\((a,0)\) and \((\operatorname{par}(a),1)\).  In general, the number of ports
is bounded by a constant depending only on \(F\) and \(d\), not on \(u\).

Thus every annular exterior return in \(T_d\square F\) is carried by one
bounded-width decorated tree cone, with uniformly bounded port incidence
between cones and the boundary sphere.  The annular exponent is therefore the
exponential growth rate of a finite-state boundary-to-boundary SAW transfer
on this rooted cone.  The finite state must remember enough of the current
bounded bag to enforce self-avoidance; no global tree-history memory is
needed beyond the stack of cone entries.

For \(F=K_2\), this finite-state transfer collapses to the one-recursion
calculation of Rounds 466--469 and gives
\[
  \Gamma_{\rm ann}(T_d\square K_2)=\sqrt q.
\]
For general finite \(F\), the next concrete target is a finite matrix or
pushdown transfer \(\mathcal T_F(z)\) whose smallest positive singularity
gives a number \(\rho_F(q)\) satisfying
\[
  \Gamma_{\rm ann}(T_d\square F)=\rho_F(q).
\]
Since \(T_d\square F\) contains \(T_d\), the stronger inequality
\(\rho_F(q)<q\) would already imply the desired annular gap.  That is a
useful low-width test, but it is stronger than necessary for high-entropy
finite fibers.  The actual finite-fiber target is
\[
  \rho_F(q)<1/\pc(T_d\square F).
\]

This is not yet a proof of the finite-fiber case.  It is a precise reduction
target: replace crude radial-excess counting by a bounded-width
self-avoiding transfer, then compare the resulting spectral radius with the
percolation threshold of the same finite-width product.
