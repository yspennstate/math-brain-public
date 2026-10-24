# Round 068 log

## Goal

Move the finite-state bridge route closer to the full quasi-transitive
bounded-degree setting, rather than only \(D\)-regular graphs.

## Bounded-degree certificate

Added Corollary `bounded-degree-detour-certificate`.  Let \(G\) be connected,
locally finite, and bounded degree.  If \(q\ge p_c(G)\) and
\[
  \sup_{\operatorname{dist}(x,y)=n}
  \sum_{k\ge0}q^kN_{n+k}(x,y)
  \le a^TM^nb
\]
for all \(n\ge0\), then \(\delta_c^{\mathrm{NB,end}}\le\rho(M)\).  Therefore
\[
  q\rho(M)\rho_{\mathrm{sph},2}(G)<1
  \quad\Longrightarrow\quad
  p_c(G)<p_{2\to2}(G).
\]

## Interpretation

The regular bridge-probability certificate is a normalized version of this
criterion.  The bounded-degree version uses raw nonbacktracking counts, so it
does not require regularity, but the graph-specific computation must estimate
the full \(q\)-weighted detour series directly.
