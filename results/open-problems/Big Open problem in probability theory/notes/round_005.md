# Round 005 log

Date: 2026-06-08

## Focus

Packaged the killed-growth and boundary-energy reductions into a single
finite-set escape criterion.

## New definitions

The killed connective constant is
\[
  \kappa_{\rm kill}(G)
  =
  \limsup_{n\to\infty}
  \left(\sup_{K\subset V\text{ finite}} A_n(K)\right)^{1/n}.
\]

The normalized boundary energy is
\[
  \mathcal E_p(K)
  =
  p^2|K|^{-1}\langle\mu_{p,K},Q_p\mu_{p,K}\rangle.
\]

## New criterion

If
\[
  \kappa_{\rm kill}(G)<1/p_c(G)
\]
and
\[
  \sup_K\mathcal E_p(K)\to0
  \quad\text{as }p\uparrow p_c,
\]
then finite-set escape follows:
\[
  \sup_K |K|^{-1}\sum_{x,y\in K}Q_p(x,y)\to0.
\]

With Hutchcroft's mean-field susceptibility bound, this implies
\[
  p_c(G)<p_{2\to2}(G)\le p_u(G).
\]

## Why this matters

The problem has been separated into two concrete inputs:

1. a killed path-growth gap;
2. a boundary energy vanishing estimate.

This is stronger than what is known from nonamenability alone, but it is now a
testable theorem-shaped framework.  A publishable intermediate result could
come from verifying these two inputs in a natural nonamenable quasi-transitive
class not already covered by hyperbolicity, nonunimodularity, planar methods,
or product methods.

## Next target

Calibrate \(\kappa_{\rm kill}\) on known examples, starting with regular trees
and products \(T\times H\).  The main question is whether
\(\kappa_{\rm kill}<1/p_c\) is true beyond hyperbolic/tree-like settings or is
too strong to be useful.

