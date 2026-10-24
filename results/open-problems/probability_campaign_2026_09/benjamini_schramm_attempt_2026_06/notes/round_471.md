# Round 471 explicit finite-state transfer for \(T_d\square F\)

Round 471 makes the finite-fiber transfer target from Round 470 explicit.

Fix a finite connected graph \(F\).  A descendant cone in
\(T_d\square F\) is a rooted tree of finite bags, one copy of \(F\) over
each tree vertex, with vertical edges given by \(F\) and child edges joining
equal fiber coordinates.  Since \(|F|<\infty\), self-avoiding
boundary-to-boundary paths in such a cone can be counted by a finite
tree-decomposition transfer.

For a root bag \(B=\{r\}\times F\), a transfer state records:

1. the subset of bag vertices already used by the partial path;
2. the degree \(0,1,2\) of each used bag vertex within the partial path;
3. the pairing/connectivity data of open path ends created by processed
   child cones;
4. the distinguished external terminals, when the state is used for a
   boundary-port transfer.

The transition at a bag is finite.  One chooses a simple subgraph of the
fiber copy \(F\), attaches zero or more child-cone transfers at matching
fiber coordinates, and then checks the usual self-avoiding path constraints:
no vertex has degree \(>2\), no completed cycle is formed before the final
terminal closure, and the final object has one path component connecting the
two prescribed ports.

Because the rooted tree has exactly \(q=d-1\) forward children, attaching
children contributes finite polynomial operations in \(q\) and in the
generating functions of the child states.  Thus the vector
\[
  \mathbf G(z)=\bigl(G_\sigma(z)\bigr)_{\sigma\in\Sigma_F}
\]
for the finite state set \(\Sigma_F\) satisfies a finite recursive system
\[
  \mathbf G(z)=\Phi_F(z,\mathbf G(z);q)
\]
with nonnegative coefficients.  The boundary-to-boundary annular transfer
functions are selected coordinates or finite linear combinations of
\(\mathbf G(z)\).

This gives a concrete version of the finite-fiber reduction:
\[
  \Gamma_{\rm ann}(T_d\square F)
  =
  \rho_F(q),
\]
where \(\rho_F(q)\) is the inverse of the smallest positive singularity
reached by the relevant solution branch of the finite system.  For
\(F=K_2\), the state set collapses to the single branch-switch recursion
\[
  S(z)=z+qz^2S(z).
\]

The remaining finite-fiber problem is now spectral/algebraic rather than
combinatorial: compare the selected singularity exponent with the
percolation threshold of the same finite-width product,
\[
  \rho_F(q)<1/\pc(T_d\square F).
\]
The stronger estimate \(\rho_F(q)<q\) is sufficient because
\(T_d\square F\) contains \(T_d\), but it is only a low-width calibration
target and should not be treated as the natural inequality for arbitrary
finite fibers.
