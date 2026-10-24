# Round 495 rooted cone height-kernel architecture

Round 495 proposes the next upper-bound architecture after the failures of
free run inventories.

The missing ingredient is support memory.  On \(T_d\square\mathbb Z\), the
tree structure suggests keeping this memory recursively by rooted cones.
Fix an oriented tree edge from a parent \(p\) to a child \(r\).  Let
\(\mathcal C_r\) be the descendant cone rooted at \(r\), and consider paths
inside
\[
  \mathcal C_r\square\mathbb Z
\]
that may touch the parent side only through the edge \((p,z)(r,z)\).

Define a height kernel \(E_z(h,h')\) as the length-generating function of
self-avoiding cone excursions which:

1. enter the cone through \((p,h)\to(r,h)\);
2. stay inside \(\mathcal C_r\square\mathbb Z\);
3. exit through \((r,h')\to(p,h')\);
4. do not use the parent edge at any intermediate time.

Self-avoidance forces \(h'\ne h\) for nontrivial returns through the same
tree edge.  The kernel \(E_z\) retains exactly the support memory lost in
Round 494: repeated use of the same tree edge is recorded by distinct crossing
heights.

The recursive structure is now local.  While the path is in the root column
\(\{r\}\times\mathbb Z\) of the cone, it may move along unused vertical
intervals and launch excursions into the \(q\) child cones of \(r\).  Each
child excursion contributes another copy of \(E_z\).  Self-avoidance on the
root column imposes an interval-order constraint: vertical intervals used in
\(\{r\}\times\mathbb Z\) cannot overlap, and child-cone excursions attach at
distinct root-column heights.

Thus one expects an operator inequality of the form
\[
  E_z \preceq \mathcal F_q(z,E_z),
\]
where \(\mathcal F_q\) is an interval-renewal transform on kernels over
\(\mathbb Z\).  The desired annular upper bound would follow from proving
that this transform is finite for
\[
  z<M_q^{-1},
  \qquad
  M_q=\max\{\sqrt q+1,\sqrt{1+4\sqrt q}\}.
\]

This architecture explains the two lower-bound mechanisms:

* fresh-column vertical-run paths are the part of \(\mathcal F_q\) that
  always launches into a new child cone and never returns through it;
* stack-return paths are iterates of \(E_z\) through a previously chosen cone,
  with different crossing heights.

The next concrete task is to define \(\mathcal F_q\) rigorously with a norm
suited to annular cuts, likely a weighted \(\ell^2(\mathbb Z)\) or
Schur-type norm in the height variable, and then prove a subcritical bound at
\(z<M_q^{-1}\).  This would directly address the support-memory loss found in
Rounds 493--494.
