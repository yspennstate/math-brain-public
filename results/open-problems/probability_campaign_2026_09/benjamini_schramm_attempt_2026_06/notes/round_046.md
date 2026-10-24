# Round 046 log

## Goal

Extract the fiber-summed line-factor proof into a form that no longer assumes a
Cartesian product.

## Quotient-tree criterion

Added Proposition `prop:quotient-tree-fiber`.  Let a graph \(G\) have a vertex
partition
\[
  V(G)=\bigsqcup_{u\in V(T_d)}F_u
\]
indexed by a \(d\)-regular tree.  For \(n\ge0\), define the uniform inter-fiber
mass
\[
  J_n(p)=
  \sup_{\operatorname{dist}_{T_d}(u,v)=n}
  \max\left\{
    \sup_{a\in F_u}\sum_{c\in F_v}\tau_p(a,c),
    \sup_{c\in F_v}\sum_{a\in F_u}\tau_p(a,c)
  \right\}.
\]
If \(J_0(p)<\infty\) and
\[
  \limsup_{n\to\infty}J_n(p)^{1/n}< (d-1)^{-1/2},
\]
then \(T_p\) is bounded on \(\ell^2(V(G))\).

The proof decomposes \(T_p\) by tree distance of the fiber indices.  Each
fiber block has operator norm at most \(J_n(p)\) by Schur's test, while the
tree sphere kernel contributes only \(O(n(d-1)^{n/2})\).  The resulting
operator-norm series converges under the displayed exponent gap.

## Why this is useful

The product criterion from Round 041 is the special case
\[
  F_u=\{u\}\times V(H)
\]
where transitivity identifies \(J_n(p)\) with the fiber-summed mass \(I_n(p)\).
The new statement also applies in principle to graph bundles, tree-indexed
extensions, and lamplighter-type quotients, provided one can prove the needed
uniform row/column decay.

This does not solve the open problem.  It clarifies the next concrete target:
find a non-product, preferably unimodular, tree-indexed quotient where
\[
  J_n(p)\le C\theta^n,\qquad \theta<(d-1)^{-1/2},
\]
holds for some \(p>p_c\), or for all \(p<p_u\).
