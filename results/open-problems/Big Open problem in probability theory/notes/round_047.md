# Round 047 log

## Goal

Generalize the quotient-tree operator endpoint to arbitrary base graphs.

## Base-sphere criterion

Added Proposition `prop:base-sphere-fiber`.  Let \(B\) be a connected graph and
let
\[
  V(G)=\bigsqcup_{u\in V(B)}F_u
\]
be a partition of \(G\)'s vertices into fibers indexed by \(B\).  Let
\[
  S_n^B(u,v)=\mathbf 1\{\operatorname{dist}_B(u,v)=n\}
\]
be the distance-\(n\) sphere kernel on \(B\), and define the uniform inter-fiber
two-point mass
\[
  J_n(p)=
  \sup_{\operatorname{dist}_B(u,v)=n}
  \max\left\{
    \sup_{a\in F_u}\sum_{c\in F_v}\tau_p(a,c),
    \sup_{c\in F_v}\sum_{a\in F_u}\tau_p(a,c)
  \right\}.
\]
If
\[
  \sum_{n\ge0}J_n(p)\|S_n^B\|_{2\to2}<\infty,
\]
then \(T_p\) is bounded on \(\ell^2(V(G))\).

The proof is the same Schur/block argument as in the tree case.  The only
change is that the tree spherical bound is replaced by the actual \(L^2\)
operator norm of the base sphere kernel.

## Exponential test

The proposition gives the following clean sufficient condition.  If
\[
  \limsup_n\|S_n^B\|_{2\to2}^{1/n}\le\rho
\]
and
\[
  \limsup_n J_n(p)^{1/n}<\rho^{-1},
\]
then \(T_p\) is \(L^2\)-bounded.  The quotient-tree criterion is the special
case \(B=T_d\), where \(\rho=\sqrt{d-1}\).

## Consequence

The project now has a more flexible endpoint for possible intermediate
theorems.  One can search for quotients whose base has known sphere-operator
growth and then try to prove matching inter-fiber decay.  This may be more
useful than focusing only on regular-tree quotients, because the base can now
be a hyperbolic graph, a product-like graph, or any graph with Haagerup-type
radial bounds.
