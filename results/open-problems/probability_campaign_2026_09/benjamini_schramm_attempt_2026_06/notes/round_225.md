# Round 225

Round 225 splits the shifted original radial tail into finite bins plus a far
tail.

The shifted tail is
\[
  \mathfrak L_{Q,\rho}^{G\to H,{\rm rad}}(s,p)
  =
  \sup_m\sum_{\substack{|2r-m|\le2\\d>K_{\rho,p}^H/2-2}}
  Q^d\mathfrak R_{r,d}^{G,{\rm rad,saw,sph}}.
\]
Choose \(\lambda>\rho/2\) and \(\delta>0\).  For defects
\[
  d\le \lambda L_H,
\]
bin by \(i\delta L_H\le d<(i+1)\delta L_H\), defining
\(\mathfrak E_{i,\delta}^{G\to H,{\rm rad}}\).  Since \(Q<1\), the \(i\)th
bin has weight at most \(Q^{i\delta L_H}\).  The number of defect values in a
bin is \(O(L_H)\), which is exponent-negligible.

The remaining far tail is
\[
  \mathfrak Y_{Q,\lambda}^{G\to H,{\rm rad}}(s,p)
  =
  \sup_m\sum_{\substack{|2r-m|\le2\\d>\lambda L_H}}
  Q^d\mathfrak R_{r,d}^{G,{\rm rad,saw,sph}}.
\]

Therefore the shifted tail exponent follows from finitely many bin exponent
checks
\[
  \limsup_{p\uparrow p_c(H)}
  \frac{\log_{D_H}\mathfrak E_{i,\delta}^{G\to H,{\rm rad}}(s,p)}
       {\log_{D_H}\bar\chi_p^H}
  +i\delta\log_{D_H}Q
  <
  -c_s\log_{D_H}p_c(H)-(2+7\alpha_\omega)s
\]
and the same exponent bound for the far tail \(\mathfrak Y\).
