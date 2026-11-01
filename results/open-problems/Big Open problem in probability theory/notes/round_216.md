# Round 216

Round 216 records the exact even-sphere projection identity for subdivisions.

Let \(H=\operatorname{Sub}(G)\), start from an old vertex \(x\), and lift a
self-avoiding path \(\pi\) in \(G\) canonically to \(H\).  If \(I_x^G\) and
\(H_x^G\) are the original inward and horizontal radial-step counts, then
\[
  I_x^H(\widehat\pi)=2I_x^G(\pi)+H_x^G(\pi).
\]
The reason is local: an outward original step gives two outward half-steps in
the subdivision, a horizontal original step gives one outward and one inward
half-step, and an inward original step gives two inward half-steps.

For even subdivision spheres,
\[
  S_{2n}^H(x)=S_n^G(x)
\]
as old vertices, and old-to-old subdivision SAWs are in bijection with
original SAWs.  Therefore the old-root even-sphere subdivision profile at
inward count \(B\) is controlled by
\[
  \sum_{2i+h=B}\mathfrak M_{n,i,h}^{G,{\rm rad,saw,sph}}.
\]

This is not yet the full subdivision inward criterion, because odd spheres
and midpoint roots still need bounded-shift comparisons.
