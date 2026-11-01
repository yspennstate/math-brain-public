# Round 499 ordered child packets and shuffle norms

Round 498 leaves one main entropy source: the time order of portal events and
the interleaving of child-cone uses.  The recursive object must be slightly
more precise than a child "subword".

For a root trace word \(\mathcal W\) and a child label \(c\), define the
ordered child packet
\[
  \Pi_c(\mathcal W)
  =
  \bigl((h_i,h_{i+1}):\ell_i=c\bigr),
\]
with the pairs listed in the order in which they occur along the global path.
This packet is not a single continuous path inside the child cone.  It is an
ordered list of boundary-to-boundary pieces that must be realized by
mutually avoiding path segments inside that cone.  The parent root column
connects these pieces in the global path; the child cone only sees the
ordered multi-port boundary condition.

Thus the natural cone partition function is
\[
  E_z(\Pi),
  \qquad
  \Pi=((a_1,b_1),\ldots,(a_k,b_k)),
\]
where \(E_z(\Pi)\) sums \(k\) disjoint cone pieces realizing the ordered
boundary pairs.  The case \(k=1\) is the two-point height kernel from Round
495, while \(k>1\) is the multi-port correction from Round 496.

With this notation, the root transform has the schematic form
\[
  Z_z(\mathcal W)
  \le
  {\bf 1}_{\mathrm{root\ valid}}(\mathcal W)\,
  \mathcal V_z(\mathcal W)
  \prod_{c=1}^q E_z(\Pi_c(\mathcal W)),
\]
where \(\mathcal V_z\) is the hard-core vertical-gap weight from Round 498.
This formula assumes that \(E_z(\Pi)\) includes the two parent-child crossing
edges for each boundary pair; equivalently, one may keep those crossing
weights outside \(E_z\), but they must be assigned consistently.

The shuffle of child packets is real entropy, not an artefact.  If the root
word contains \(k_c\) uses of child \(c\) and \(v\) vertical runs, their
relative time order contributes a multinomial factor
\[
  \binom{k_1+\cdots+k_q+v}{k_1,\ldots,k_q,v}
\]
before imposing the height-gap constraints.  This is the abstract source of
the product-shuffle scale in the earlier tree-line estimates.

The right norm should therefore be exponential-generating in the number of
packet atoms.  Factorials exactly absorb shuffles:
\[
  \frac{1}{K!}
  \binom{K}{k_1,\ldots,k_q,v}
  =
  \frac{1}{k_1!\cdots k_q!v!},
  \qquad K=k_1+\cdots+k_q+v.
\]
Thus a candidate packet norm should have the form
\[
  \mathcal N_z(E;\xi,\Phi)
  =
  \sum_{k\ge0}\frac{\xi^k}{k!}
  \sup_{\Pi:|\Pi|=k}
  \frac{E_z(\Pi)}{\Phi(\Pi)},
\]
with a gap/excess weight \(\Phi\) strong enough to control the ordered portal
heights.  Under this normalization, the \(q\)-fold child interleaving becomes
approximately multiplicative, while the root-column vertical contribution is
the hard-core gap gas from Round 498.

This identifies a concrete fixed-point target:
\[
  \mathcal N_z(\mathcal T E;\xi,\Phi)
  \le
  \mathcal N_z(E;\xi,\Phi)
\]
for some \(\xi\) and \(\Phi\) whenever \(z<M_q^{-1}\).  The remaining
mathematical work is to choose \(\Phi\) so that the annular excess constraint
and adjacent-gap matching dominate the portal-height sums.
