# Round 222

Round 222 turns the subdivision count comparison into a weighted finite/tail
criterion on the original graph.

Define the collapsed original radial profile
\[
  \mathfrak R_{n,d}^{G,{\rm rad,saw,sph}}
  =
  \sum_{2i+j=d}\mathfrak M_{n,i,j}^{G,{\rm rad,saw,sph}}.
\]
With \(H=\operatorname{Sub}(G)\), \(Q=q^2\), and
\[
  C_\star
  =
  \max\left\{1,\frac{\Delta}{h(G)},\Delta\right\}(1+2C_H),
\]
the weighted count comparison is
\[
  q^{2B}\mathfrak M_{m,B,0}^{H,{\rm rad,saw,sph}}
  \le
  C_\star
  \sum_{|2r-m|\le2}\sum_{a=0}^2
  Q^{B-a}\mathfrak R_{r,B-a}^{G,{\rm rad,saw,sph}}.
\]

This gives shifted original finite and tail profiles
\[
  \mathfrak F_{Q,\rho}^{G\to H,{\rm rad}},\qquad
  \mathfrak L_{Q,\rho}^{G\to H,{\rm rad}},
\]
over the half-radius window \(|2r-m|\le2\).  They control the bipartite
inward profiles on \(H\) by
\[
  \mathfrak F_{q,\rho}^{H,{\rm in,saw}}
  \le 9C_\star\mathfrak F_{Q,\rho}^{G\to H,{\rm rad}},
  \qquad
  \mathfrak L_{q,\rho}^{H,{\rm in,saw}}
  \le 3C_\star\mathfrak L_{Q,\rho}^{G\to H,{\rm rad}}.
\]
Thus the subdivision route can now be stated directly as original-graph
radial finite/tail estimates, with only bounded radius and defect shifts.
