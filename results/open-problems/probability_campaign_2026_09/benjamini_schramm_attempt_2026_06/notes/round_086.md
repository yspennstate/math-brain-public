# Round 086 log

## Goal

Make the layer-square target more checkable by reducing it to deterministic
restricted shell operators on a base graph and fibre-summed two-point masses.

## New Proposition

Added `prop:restricted-shell-layer-square`.

Use the setup of the base-sphere fibre criterion: \(V(G)=\bigsqcup_{u\in B}F_u\)
and
\[
  J_n(p)=
  \sup_{d_B(u,v)=n}
  \max\left\{
    \sup_{a\in F_u}\sum_{c\in F_v}\tau_p(a,c),
    \sup_{c\in F_v}\sum_{a\in F_u}\tau_p(a,c)
  \right\}.
\]
For \(\Sigma\subseteq V(B)\), let \(M_\Sigma\) be multiplication by
\(\mathbf 1_\Sigma\) and \(S_\Sigma=\bigcup_{u\in\Sigma}F_u\).  If
\[
  A_\Sigma(p)=\sum_{n\ge0}J_n(p)\|M_\Sigma S_n^B\|_{2\to2}<\infty,
\]
then every finite \(K\subset V(G)\) satisfies
\[
  \sum_{z\in S_\Sigma}(T_p\mathbf 1_K(z))^2
  \le A_\Sigma(p)^2 |K|.
\]
Consequently, a separator family \(\Sigma_a\) has small layer-square mass
whenever
\[
  \chi_p^{-1}\min_a A_{\Sigma_a}(p)^2
\]
is small.

## Proof Idea

Decompose \(T_p=\sum_n L_n\) by base distance.  For
\[
  g(u)=\|\mathbf 1_{K\cap F_u}\|_2,
\]
the block-Schur estimate gives
\[
  \|(L_n\mathbf 1_K)\mathbf 1_{S_\Sigma}\|_2
  \le
  J_n(p)\|M_\Sigma S_n^B g\|_2.
\]
The result follows by summing over \(n\) and using \(\|g\|_2^2=|K|\).

## Significance

This is still conditional, but it separates two tasks:

1. percolation input: control the fibre masses \(J_n(p)\);
2. deterministic geometry: prove useful restricted-shell bounds for
   \(M_\Sigma S_n^B\).

For tree/product-like graphs, this gives a concrete route from
backscattering-style directional decay to the separator-convolution
layer-square estimate.
