# Round 083 log

## Goal

Separate the geometric part of the regular-tree local separator-convolution
proof from the analytic \(L^2\) estimate used to control the separator term,
and check the same geometry for finite-fiber models over
\(T\times\mathbb Z^s\).

## Setup

Let \(G\) admit a finite-fiber, 1-Lipschitz projection to
\(\mathbb T\square\mathbb Z^s\), where \(\mathbb T\) is a bounded-degree tree:
\[
  \sup_u|\pi^{-1}(u)|<\infty,
  \qquad
  x\sim y\Rightarrow
  d_{\mathbb T\square\mathbb Z^s}(\pi x,\pi y)\le1.
\]
For a residue vector
\(\mathbf a=(a_0,\ldots,a_s)\in\{0,\ldots,L-1\}^{s+1}\), let
\[
  \Sigma_{\mathbf a}=
  \{u:\rho_j(u)\equiv a_j\pmod L
    \text{ for some }0\le j\le s\},
  \qquad
  S_{\mathbf a}=\pi^{-1}(\Sigma_{\mathbf a}),
\]
where \(\rho_0\) is tree distance from the root and
\(\rho_1,\ldots,\rho_s\) are the Euclidean coordinates.

The components of
\((\mathbb T\square\mathbb Z^s)\setminus \Sigma_{\mathbf a}\) have uniformly
bounded size depending only on \(L\), \(s\), and the tree degree.  Finite
fibers imply the same for components of \(G\setminus S_{\mathbf a}\).  Thus
intersections of \(K\setminus S_{\mathbf a}\) with those components have
uniformly bounded diameter.

## Averaging

For \(K_{\mathbf a}=K\cap S_{\mathbf a}\), a fixed vertex lies in
\(S_{\mathbf a}\) for at most an \((s+1)/L\) fraction of residue vectors.
Hence
\[
  \frac{1}{L^{s+1}}\sum_{\mathbf a}
  \frac{2|K_{\mathbf a}|}{|K|}
  \le \frac{2(s+1)}{L}.
\]
Also
\[
  \frac{1}{L^{s+1}}\sum_{\mathbf a}
  \frac{1}{\bar\chi_p|K|}
  \sum_{z\in S_{\mathbf a}}(T_p\mathbf 1_K(z))^2
  \le
  \frac{s+1}{L}
  \frac{\|T_p\|_{2\to2}^2}{\bar\chi_p}.
\]
If
\[
  \limsup_{p\uparrow p_c}
  \frac{\|T_p\|_{2\to2}^2}{\bar\chi_p}<\infty,
\]
then \(L\) can be chosen so that one residue vector simultaneously has small
buffer mass and small separator-convolution mass.

## Result

Added `prop:finite-fiber-tree-grid-separators`: finite-fiber tree-grid
geometry over \(T\times\mathbb Z^s\), plus the displayed square-mass bound,
implies the local
separator-convolution property.

This is not a new route to the main conjecture by itself.  When
\(\bar\chi_p\to\infty\), the same analytic bound already gives finite-set
escape by
\[
  \frac{\langle \mathbf 1_K,T_p\mathbf 1_K\rangle}{\bar\chi_p|K|}
  \le
  \frac{\|T_p\|_{2\to2}}{\bar\chi_p}.
\]
The useful output is diagnostic: the finite-fiber tree/product-grid geometry
is not the hard part; the missing mechanism is layerwise square-mass control
without a conclusion-like global \(L^2\) estimate.
