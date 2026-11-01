# Round 207

Round 207 decomposes exact-sphere excess by radial defect.

For a path \(\gamma=(v_0,\ldots,v_m)\) started at \(x\), define
\[
  I_x(\gamma)=\#\{i:d(x,v_i)=d(x,v_{i-1})-1\}
\]
and
\[
  H_x(\gamma)=\#\{i:d(x,v_i)=d(x,v_{i-1})\}.
\]
If \(\gamma\) ends in \(S_n(x)\), then with \(O_x(\gamma)\) the number of
outward steps,
\[
  m=O_x+I_x+H_x,\qquad n=O_x-I_x,
\]
so
\[
  m-n=2I_x+H_x.
\]

The new profile
\[
  \mathfrak M_{n,b,h}^{\rm rad,saw,sph}
\]
counts, in spherical average and with root supremum, self-avoiding paths to
\(S_n(x)\) with \(b\) inward steps and \(h\) same-sphere steps.

The exact-length profile obeys
\[
  \mathfrak N_{n,k}^{\rm saw,sph}
  \le
  \sum_{2b+h=k}
  \mathfrak M_{n,b,h}^{\rm rad,saw,sph}.
\]
Consequently the \(q\)-weighted Round 203 target is implied by the radial
target
\[
  \sup_n\sum_{b,h\ge0}q^{2b+h}
  \mathfrak M_{n,b,h}^{\rm rad,saw,sph}.
\]

This is still conditional, but it separates inward radial backtracking from
same-sphere wandering, which are geometrically different sources of excess.
