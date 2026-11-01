# Round 224

Round 224 cleans up the shifted original radial criterion and bins its finite
profile.

First, the collapsed defect profile now has an explicit convention for
negative defects:
\[
  \mathfrak R_{n,d}^{G,{\rm rad,saw,sph}}=0\qquad(d<0),
\]
and every term with \(B-a<0\) in the weighted subdivision comparison is
interpreted as zero.

Second, the finite shifted profile
\[
  \mathfrak F_{Q,\rho}^{G\to H,{\rm rad}}(s,p)
\]
can be replaced by finitely many bins.  For \(\delta>0\), set
\[
  m_{\rho,\delta}^{G\to H}
  =
  \left\lfloor\frac{\rho}{2\delta}\right\rfloor+1
\]
and define \(\mathfrak D_{i,\delta}^{G\to H,{\rm rad}}\) by restricting
\(\mathfrak R_{r,d}^{G,{\rm rad,saw,sph}}\) to
\[
  i\delta L_H\le d<(i+1)\delta L_H
\]
inside the shifted half-radius window \(|2r-m|\le2\).  Since \(Q<1\), the
\(i\)th bin contributes weight at most \(Q^{i\delta L_H}\).  Hence the finite
profile exponent follows from the finite list
\[
  \limsup_{p\uparrow p_c(H)}
  \frac{\log_{D_H}\mathfrak D_{i,\delta}^{G\to H,{\rm rad}}(s,p)}
       {\log_{D_H}\bar\chi_p^H}
  +i\delta\log_{D_H}Q
  <
  -c_s\log_{D_H}p_c(H)-(2+7\alpha_\omega)s.
\]
