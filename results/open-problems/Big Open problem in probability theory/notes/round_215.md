# Round 215

Round 215 bins the finite inward profile from Round 214.

The one-parameter finite inward profile
\[
  \mathfrak F_{q,\rho}^{\rm in,saw}(s,p)
  =
  \sup_n\sup_{0\le b\le K_{\rho,p}/2}
  q^{2b}\mathfrak M_{n,b,0}^{\rm rad,saw,sph}
\]
still ranges over \(O(L)\) possible inward counts.  Fixing \(\delta>0\),
define
\[
  m_{\rho,\delta}^{\rm in}
  =
  \left\lfloor\frac{\rho}{2\delta}\right\rfloor+1
\]
and bin \(b\) by \(i\delta L\le b<(i+1)\delta L\).  In the \(i\)th bin,
\[
  q^{2b}\le q^{2i\delta L}.
\]

Thus it is enough to prove, for finitely many \(i\),
\[
  \limsup_{p\uparrow p_c}
  \frac{\log_\Delta\mathfrak C_{i,\delta}^{\rm in,saw}(s,p)}
       {\log_\Delta\bar\chi_p}
  +2i\delta\log_\Delta q
  <
  -c_s\log_\Delta p_c-(2+7\alpha_\omega)s.
\]
This is the bipartite inward analogue of the earlier finite-excess binning.
