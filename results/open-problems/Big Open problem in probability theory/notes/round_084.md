# Round 084 log

## Goal

Translate the Hutchcroft--Pan backscattering mechanism into the language of
the separator-convolution program.

## Observation

For a finite-fiber projection to \(\mathbb T\square\mathbb Z^s\), periodic
tree-grid separators \(S_{\mathbf a}\) already give:

- small buffer mass after averaging over shifts \(\mathbf a\);
- uniformly bounded pieces after removing \(S_{\mathbf a}\).

Thus the remaining obstruction is exactly the square-mass term
\[
  \frac{1}{\bar\chi_p|K|}
  \sum_{z\in S_{\mathbf a}}
    (T_p\mathbf 1_K(z))^2 .
\]
Equivalently, one wants
\[
  \lim_{L\to\infty}\limsup_{p\uparrow p_c}
  \sup_K
  \min_{\mathbf a}
  \frac{1}{\bar\chi_p|K|}
  \sum_{z\in S_{\mathbf a}}
    (T_p\mathbf 1_K(z))^2
  =0.
\]

## Relation to Hutchcroft--Pan

The product backscattering argument is a two-replica argument.  In
\(T\times H\), if the directional exponent were below \(1/2\), two downward
connections in different \(H\)-fibers can be run in parallel often enough to
create a supercritical embedded branching process; after increasing \(p\), this
forces the corresponding fiber clusters to merge.  This is what rules out the
bad exponent below \(p_u\).

The separator square-mass term has the same two-replica shape: it counts two
connections from a separator grid point into the same finite test set.  A
general proof along this route would need a local version of backscattering
that rules out persistent square mass on separating grids without relying on
a global tilted/nonunimodular height.

## Manuscript update

The remark after `prop:finite-fiber-tree-grid-separators` now states the
layer-square estimate explicitly and identifies it as the product-like
backscattering target.
