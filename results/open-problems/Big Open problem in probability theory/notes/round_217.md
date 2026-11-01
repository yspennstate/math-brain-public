# Round 217

Round 217 adds the old-root odd-sphere subdivision comparison under an
explicit local no-dead-end hypothesis.

For an old root \(x\), the odd sphere \(S_{2n+1}^{\operatorname{Sub}(G)}(x)\)
consists of midpoints of original edges whose nearer endpoint is in
\(S_n^G(x)\).  If every vertex of \(S_n^G(x)\) has a neighbour in
\(S_{n+1}^G(x)\), then this midpoint sphere has size at least both
\(|S_n^G(x)|\) and \(|S_{n+1}^G(x)|\).

A subdivision SAW ending at such a midpoint projects, after deleting the
final half-edge, to an original SAW ending either in \(S_n^G(x)\) or in
\(S_{n+1}^G(x)\).  The final half-edge contributes respectively \(0\) or
\(1\) inward steps, so the old-root odd profile at inward count \(B\) is
bounded by
\[
  \Delta\sum_{2i+h=B}\mathfrak M_{n,i,h}^{G,{\rm rad,saw,sph}}
  +
  \Delta\sum_{2i+h=B-1}\mathfrak M_{n+1,i,h}^{G,{\rm rad,saw,sph}}.
\]

This completes the old-root even/odd subdivision bookkeeping subject to the
local no-dead-end condition.  The remaining missing comparison is for
midpoint roots, and for graphs with dead ends one needs either bounded-depth
shifts or a boundary-weighted spherical profile.
