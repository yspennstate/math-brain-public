# Round 221

Round 221 packages the subdivision count comparisons into restricted profiles.

For \(H=\operatorname{Sub}(G)\), define old-root and midpoint-root restricted
profiles
\[
  \mathfrak M_{\ell,B}^{H,{\rm old}},
  \qquad
  \mathfrak M_{\ell,B}^{H,{\rm mid}}.
\]
Since \(H\) is bipartite,
\[
  \mathfrak M_{\ell,B,0}^{H,{\rm rad,saw,sph}}
  =
  \max\{\mathfrak M_{\ell,B}^{H,{\rm old}},
        \mathfrak M_{\ell,B}^{H,{\rm mid}}\}.
\]

The old-root bounds are now:
\[
  \mathfrak M_{2n,B}^{H,{\rm old}}
  \le
  \sum_{2i+h=B}\mathfrak M_{n,i,h}^{G,{\rm rad,saw,sph}},
\]
and
\[
  \mathfrak M_{2n+1,B}^{H,{\rm old}}
  \le
  \frac{\Delta}{h(G)}
  \sum_{2i+h=B}\mathfrak M_{n,i,h}^{G,{\rm rad,saw,sph}}
  +
  \Delta
  \sum_{2i+h=B-1}\mathfrak M_{n+1,i,h}^{G,{\rm rad,saw,sph}}.
\]

The midpoint-root bound is
\[
  \mathfrak M_{m,B}^{H,{\rm mid}}
  \le
  2C_H\left(
    \mathfrak M_{m-1,B}^{H,{\rm old}}
    +
    \mathfrak M_{m+1,B-1}^{H,{\rm old}}
  \right),
  \qquad
  C_H=D_H^4/h(H).
\]
This makes the subdivision comparison count-level and non-circular: midpoint
roots reduce to old-root profiles, and old-root profiles reduce to original
two-coordinate radial profiles.
