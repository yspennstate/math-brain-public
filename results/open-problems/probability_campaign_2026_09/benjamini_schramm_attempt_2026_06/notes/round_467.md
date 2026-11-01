# Round 467 exterior components in \(T_d\square K_2\) are two-port cones

Round 467 gives the exact component decomposition needed for the two-layer
product calibration.

Let \(G=T_d\square K_2\), root at \(x=(o,0)\), and put \(q=d-1\).  A vertex
\((v,\epsilon)\), \(\epsilon\in\{0,1\}\), has radius
\[
  d_G(x,(v,\epsilon))=d_T(o,v)+\epsilon.
\]
Fix \(u\ge1\) and consider the exterior
\[
  X_u=V\setminus B_{u-1}(x).
\]
For every tree vertex \(t\) at depth \(u-1\), let \(C_t\) be the subgraph of
\(X_u\) induced by
\[
  \{(w,1): w\text{ descends from }t\}
  \cup
  \{(w,0): w\text{ descends from a child of }t\}.
\]
Then the components of \(X_u\) are exactly the \(C_t\)'s.

Each component \(C_t\) has only two boundary ports in \(S_{u-1}(x)\):
\[
  A_t=(t,0),
  \qquad
  B_t=(\operatorname{par}(t),1),
\]
where \(B_t\) is interpreted only when \(u\ge2\).  The port \(A_t\) is
adjacent to \((t,1)\) and to the layer-\(0\) children of \(t\); the port
\(B_t\) is adjacent only to \((t,1)\).  Different components do not
communicate inside \(X_u\).

Consequently, every exterior return through level \(u\) in
\(T_d\square K_2\) is carried by a single two-port descendant cone.  At the
level of exponential length growth, the annular boundary exponent is
therefore determined by the transfer between \(A_t\) and \(B_t\) inside one
component, up to bounded-degree incidence constants.

This removes the main ambiguity left in Round 466: repeated layer switching
cannot move an exterior return between different tree boundary cones without
passing through \(B_{u-1}(x)\).
