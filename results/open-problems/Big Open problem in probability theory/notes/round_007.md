# Round 007 log

Date: 2026-06-08

## Focus

Added a global self-avoiding-walk operator criterion.

## Definition

Let \(C_n(x,y)\) be the number of length-\(n\) self-avoiding paths from \(x\)
to \(y\).  Define
\[
  \gamma_{\rm SAW,2}(G)
  =
  \limsup_{n\to\infty}\|C_n\|_{2\to2}^{1/n}.
\]

## Criterion

If
\[
  \gamma_{\rm SAW,2}(G)<1/p_c(G),
\]
then
\[
  p_c(G)<p_{2\to2}(G).
\]

The proof is the union bound
\[
  T_p(x,y)\le\sum_{n\ge0}p^n C_n(x,y)
\]
plus the operator estimate
\[
  \|T_p\|_{2\to2}\le\sum_{n\ge0}p^n\|C_n\|_{2\to2}.
\]
The strict gap allows this series to converge for some \(p>p_c\).

If \(\bar\chi_p\to\infty\), the same bound gives finite-set escape because
\[
  |K|^{-1}\sum_{x,y\in K}Q_p(x,y)
  \le \|T_p\|_{2\to2}/\bar\chi_p.
\]

## Interpretation

This is a strong sufficient condition, not a proposed proof of the full
Benjamini-Schramm conjecture.  It separates a possible direct \(L^2\) route
from the boundary-energy route.  The regular-tree calculation fits this
criterion because the self-avoiding sphere is the tree spherical operator and
has \(L^2\) growth \(\sqrt{d-1}<1/p_c(T_d)\).

## Next target

Stress-test \(\gamma_{\rm SAW,2}<1/p_c\) on products \(T_d\times H\) and on
amenable graphs.  The condition must fail in broad amenable settings and may
be too strong for product graphs, but that failure would clarify why the
finite-set boundary-energy route is needed.
