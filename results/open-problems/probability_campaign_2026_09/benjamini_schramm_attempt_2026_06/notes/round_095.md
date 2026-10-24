# Round 095 log

## Goal

Refine the long-range squared-kernel obstruction by locating the common root
in the two-replica expansion.

## Result

Added `prop:square-trapping-far-root-leg`.

If \(\eta(Q_{p_n}^2)\ge\epsilon>0\) along \(p_n\uparrow p_c\), then there are
finite sets \(K_n\) such that for every fixed \(R\),
\[
  \liminf_{n\to\infty}
  |K_n|^{-1}\sum_z
  \left(\sum_{\substack{x\in K_n\\d(x,z)>R}}Q_{p_n}(x,z)\right)
  \left(\sum_{y\in K_n}Q_{p_n}(z,y)\right)
  \ge \epsilon/4.
\]

The proof expands \(Q^2(x,y)=\sum_zQ(x,z)Q(z,y)\).  If \(d(x,y)>2R\), then
for every root \(z\), at least one of \(d(x,z)>R\) or \(d(y,z)>R\) holds.
Thus long-range endpoint-pair mass forces same-root two-replica mass with a
far leg.

## Interpretation

A failure of sublinear two-replica escape cannot consist of many short
connections to a nearby root.  It must contain a persistent same-root
backscatter in which one replica reaches distance beyond every fixed scale.
This is the form most directly comparable to separator and backscattering
arguments.
