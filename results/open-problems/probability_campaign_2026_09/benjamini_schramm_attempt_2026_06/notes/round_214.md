# Round 214

Round 214 makes the bipartite criterion fully one-parameter.

Round 213 replaced the long-excess tail by the exact inward-return tail
\[
  b>K_{\rho,p}/2
\]
because bipartite graphs have \(h=0\) and hence \(k=2b\).  The same identity
also sharpens the finite-excess side: the condition \(0\le k\le K_{\rho,p}\)
is exactly
\[
  0\le b\le K_{\rho,p}/2.
\]

The new finite inward profile is
\[
  \mathfrak F_{q,\rho}^{\rm in,saw}(s,p)
  =
  \sup_n\sup_{0\le b\le K_{\rho,p}/2}
  q^{2b}\mathfrak M_{n,b,0}^{\rm rad,saw,sph}.
\]
Together with the Round 213 tail profile
\[
  \mathfrak L_{q,\rho}^{\rm in,saw}(s,p)
  =
  \sup_n\sum_{b>K_{\rho,p}/2}q^{2b}
  \mathfrak M_{n,b,0}^{\rm rad,saw,sph},
\]
it implies the finite-excess/tail criterion.

The subdivision criterion now asks for these two inward profiles on
\(\operatorname{Sub}(G)\).  This does not solve the open problem, but it
removes the remaining two-coordinate radial bookkeeping from the bipartite
route.
