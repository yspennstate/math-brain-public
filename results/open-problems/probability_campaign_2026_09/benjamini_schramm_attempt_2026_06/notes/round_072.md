# Round 072 log

## Goal

Package the tree calibration beyond regular and semiregular examples.

## Finite-quotient universal-cover trees

Added Proposition `finite-quotient-tree-detour`.  Let \(H\) be a finite
connected graph and \(T=\widetilde H\) its universal-cover tree.  If the
directed nonbacktracking matrix \(B\) on \(\vec E(H)\) is irreducible with
Perron radius \(\beta>1\), then
\[
  p_c(T)=\beta^{-1}.
\]
This is the multitype branching threshold for open nonbacktracking descendants.

For the sphere-kernel side, let \(u>0\) be a Perron vector and weight vertices
by
\[
  \phi(x)=u_{\operatorname{type}(\epsilon_x)}\beta^{-d(o,x)/2}.
\]
A Schur-test count over the confluent point of \(x\) and \(y\) gives
\[
  \|S_n\|_{2\to2}\le C_H(n+1)\beta^{n/2},
\]
so \(\rho_{\mathrm{sph},2}(T)\le\sqrt\beta\).

Since a nonbacktracking walk in a tree is forced to be the geodesic between its
endpoints, the detour certificate has \(M=(1)\).  Therefore
\[
  p_c(T)\rho_{\mathrm{sph},2}(T)\le \beta^{-1/2}<1,
\]
which gives \(p_c(T)<p_{2\to2}(T)\).

## Role

This closes the finite-type tree calibration in the raw-count detour framework.
The remaining difficulty for the main conjecture is now isolated more sharply:
cycles create genuine nonbacktracking detours, and those detours must be
controlled by a finite-state transfer bound rather than by the one-state tree
majorization.
