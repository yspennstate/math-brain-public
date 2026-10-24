# Round 464 two-layer product is the first annular upper-bound test

Round 464 identifies the simplest product graph on which to test an upper
bound for \(\Gamma_{\rm ann}\):
\[
  G=T_d\square K_2.
\]

Root at \(x=(o,0)\).  A vertex \((v,\epsilon)\) has distance
\[
  d_G(x,(v,\epsilon))=d_T(o,v)+\epsilon,
  \qquad \epsilon\in\{0,1\}.
\]
Thus the sphere \(S_{u-1}(x)\) consists of
\[
  \{(v,0):d_T(o,v)=u-1\}
  \cup
  \{(v,1):d_T(o,v)=u-2\}.
\]

The Round 462 lower bound gives
\[
  \Gamma_{\rm ann}(T_d\square K_2)\ge\sqrt{d-1}.
\]
This graph removes all factor-geodesic growth, so any larger value of
\(\Gamma_{\rm ann}\) must come from repeated switching between the two layers
while moving in the tree.

A killed exterior path in this graph can be encoded by:

* a tree-depth process \(r_t=d_T(o,v_t)\);
* a layer bit \(\epsilon_t\in\{0,1\}\);
* the constraint \(r_t+\epsilon_t\ge u\) for all interior vertices;
* tree steps changing \(r_t\) by \(\pm1\), with \(d-1\) choices for outward
  moves away from the root and one forced inward move along a fixed branch;
* layer switches changing \(\epsilon_t\) and hence the radial distance by
  \(\pm1\).

This is a weighted half-plane path problem with a self-avoidance constraint
on tree vertices in each layer.  The out-and-back lower bound corresponds to
one long outward tree run in layer \(0\), one layer switch at the top, and one
long inward tree run in layer \(1\).

The first concrete upper-bound target is therefore:
\[
  \Gamma_{\rm ann}(T_d\square K_2)=\sqrt{d-1}
  \quad\text{or at least}\quad
  \Gamma_{\rm ann}(T_d\square K_2)<d-1.
\]
The weaker strict bound would already match the annular gap threshold coming
from the tree subgraph:
\[
  \frac1{\pc(T_d\square K_2)}\ge d-1.
\]

This is a finite-state transfer problem modulo the self-avoidance bookkeeping
on a tree.  Solving it would give the first non-tree calibration of the
annular boundary exponent.
