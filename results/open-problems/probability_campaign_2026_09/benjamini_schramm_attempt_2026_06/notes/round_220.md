# Round 220

Round 220 removes two conditional subdivision-geometry assumptions using
nonamenability.

For old-root odd spheres, the midpoint sphere
\[
  S_{2n+1}^{\operatorname{Sub}(G)}(x)
\]
contains the edge boundary of the original ball \(B_n^G(x)\).  Since the
paper's Cheeger convention gives
\[
  |\partial_E B_n^G(x)|\ge h(G)\sum_{z\in B_n^G(x)}\deg(z)
  \ge h(G)|S_n^G(x)|,
\]
the denominator comparison needed in Round 217 follows from \(h(G)>0\).  The
old-root odd bound becomes
\[
  \frac{\Delta}{h(G)}
  \sum_{2i+h=B}\mathfrak M_{n,i,h}^G
  +
  \Delta
  \sum_{2i+h=B-1}\mathfrak M_{n+1,i,h}^G.
\]

For midpoint roots, a general Cheeger sphere comparison now gives, in any
bounded-degree nonamenable graph \(X\),
\[
  |S_{m-1}^X(a)|,\ |S_{m+1}^X(a)|
  \le \frac{D^4}{h(X)}|S_m^X(b)|
  \qquad(a\sim b).
\]
Thus the shifted-sphere hypothesis from Round 218 holds automatically in the
subdivision \(H\), with \(C=D_H^4/h(H)\).
