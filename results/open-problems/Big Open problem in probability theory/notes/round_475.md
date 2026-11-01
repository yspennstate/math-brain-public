# Round 475 clique-fiber percolation scale is also linear

Round 475 pairs the \(K_m\) annular lower bound from Round 474 with the
matching percolation scale.

Consider \(T_d\square K_m\), \(q=d-1\), and set
\[
  p=\frac{C}{m}
\]
with \(C>1\) fixed.  Inside each clique bag, the open \(K_m\)-subgraph is an
Erdos-Renyi graph \(G(m,C/m)\).  For \(C>1\), it has a giant component of
asymptotic density \(\theta(C)>0\), where
\[
  \theta(C)=1-e^{-C\theta(C)}.
\]

Use a coarse two-type exploration that keeps only whether the current bag
cluster is giant-sized.  If a parent bag has a connected set of size about
\(\theta m\), and a child bag has a giant component of size about
\(\theta m\), then the two sets overlap in about \(\theta^2m\) fiber
coordinates.  Along those coordinates, the parent-child tree edges are open
with probability \(C/m\), so the chance of at least one open bridge into the
child giant is approximately
\[
  1-\exp(-C\theta(C)^2).
\]
For \(C\) large enough, this probability is close to \(1\).  Since each bag
has \(q\ge2\) forward children, the giant-type exploration is supercritical
for all sufficiently large \(C=C(q)\).  Therefore
\[
  \pc(T_d\square K_m)\le \frac{C(q)+o(1)}{m},
  \qquad
  \frac1{\pc(T_d\square K_m)}\ge c(q)m
\]
along the clique-fiber family.

This scale matches the lesson of Round 474.  The annular transfer exponent
can grow linearly in \(m\), so a uniform comparison with \(q\) is the wrong
target.  But the inverse percolation threshold also grows linearly in \(m\),
and the desired comparison
\[
  \Gamma_{\rm ann}(T_d\square K_m)<1/\pc(T_d\square K_m)
\]
remains a constant-level finite-width problem.

To turn this calibration into a proof, one would need an upper bound on the
finite-state SAW transfer for \(K_m\) with a constant smaller than the
percolation constant from the finite-type matrix \(M_p\).  The scale alone
does not prove the gap.
