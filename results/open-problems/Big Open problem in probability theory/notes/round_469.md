# Round 469 exact annular exponent for \(T_d\square K_2\)

Round 469 converts the two-port computation into the annular boundary
exponent.

By Round 467, \(X_u=V\setminus B_{u-1}(x)\) decomposes into components
\(C_t\) indexed by tree vertices \(t\) at depth \(u-1\).  By Round 468, the
length-\(n\) transfer across one component has coefficient
\[
  O((d-1)^{n/2}).
\]
The boundary incidence between ports is uniformly bounded in \(n\): each
component has two ports, each \(A_t\) belongs to one component, and each
\(B_t\) is shared by only \(d-1\) child components.  Such bounded-degree
incidence changes operator and cut norms only by constants independent of
\(n\).

Hence
\[
  \Gamma_{\rm ann}(T_d\square K_2)
  =
  \sqrt{d-1}.
\]
The lower bound is Round 462; the upper bound is the component decomposition
and two-port transfer formula.

This gives the first non-tree calibration of the annular boundary exponent.
It also verifies the desired annular gap in this example:
\[
  \Gamma_{\rm ann}(T_d\square K_2)
  =
  \sqrt{d-1}
  <
  d-1
  \le
  \frac1{\pc(T_d\square K_2)}
  \qquad(d\ge3),
\]
where the final inequality uses the embedded copy of \(T_d\).

The calculation is useful conceptually.  The full global SAW operator route
is sensitive to unrestricted forward propagation in both layers.  The annular
boundary exponent instead sees only return transfers across exterior
components, and those transfers force tree branching to be paid in
out-and-back pairs.
