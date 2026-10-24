# Round 009 log

Date: 2026-06-08

## Focus

Stress-tested the global SAW \(L^2\) route on Cartesian products.

## Product lower bound

For connected infinite bounded-degree graphs \(G\) and \(H\),
\[
  \gamma_{\rm SAW,2}(G\square H)
  \ge
  \gamma_{\rm SAW,2}(G)+\gamma_{\rm SAW,2}(H).
\]

The key entrywise inequality is
\[
  C_n^{G\square H}
  \ge
  \binom nk C_k^G\otimes C_{n-k}^H.
\]
It comes from shuffling a length-\(k\) SAW in \(G\) with a length-\(n-k\) SAW
in \(H\).  The resulting path in \(G\square H\) is self-avoiding because both
coordinate paths have distinct coordinate indices, and time is the sum of the
two indices.

Taking operator norms, \(n\)th roots, and optimizing over \(k/n\) yields the
additive lower bound.

## Consequence for \(T_d\square H\)

If \(H\) is connected, transitive, amenable, and bounded degree, then Round
008 gives \(\gamma_{\rm SAW,2}(H)=\mu(H)\), while the tree calculation gives
\[
  \gamma_{\rm SAW,2}(T_d)=\sqrt{d-1}.
\]
Thus
\[
  \gamma_{\rm SAW,2}(T_d\square H)\ge \sqrt{d-1}+\mu(H).
\]

Route A7 can therefore prove the product case only if
\[
  p_c(T_d\square H)<\frac{1}{\sqrt{d-1}+\mu(H)}.
\]

## Interpretation

This does not rule out the SAW operator gap on products.  It identifies a
quantitative barrier: mixed coordinate SAWs add to the \(L^2\) growth exponent.
The next check is to compare the necessary inequality with known estimates for
\(p_c(T_d\times\mathbb Z^r)\).  If it fails in a natural product family, the
global SAW route is too strong there and the boundary-energy or scattering
route becomes necessary.
