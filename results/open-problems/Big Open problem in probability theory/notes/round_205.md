# Round 205

Round 205 refines the finite-excess part of Round 204 by binning the excess
length \(k\) at linear scale \(L=\log_\Delta\bar\chi_p\).

For \(\delta>0\), set
\[
  m_{\rho,\delta}=\lfloor\rho/\delta\rfloor+1.
\]
For \(0\le i<m_{\rho,\delta}\), let
\[
  \mathfrak B_{i,\delta}^{\rm saw}(s,p)
\]
be the supremum of \(\mathfrak N_{n,k}^{\rm saw,sph}\) over the half-to-full
window in \(n\) and the excess bin
\[
  i\delta L\le k<(i+1)\delta L.
\]

Because \(q<1\), every term in the \(i\)th bin satisfies
\[
  q^k\mathfrak N_{n,k}^{\rm saw,sph}
  \le
  q^{i\delta L}\mathfrak B_{i,\delta}^{\rm saw}(s,p).
\]
The number of bins is fixed as \(p\uparrow p_c\), so the finite-excess
weighted maximum is controlled by finitely many unweighted binned count
exponents shifted by \(i\delta\log_\Delta q\).

The live target is now:

1. prove each binned finite-excess exponent is below the Round 203 margin
   after the \(q\)-weight shift, and
2. prove the Round 204 long-excess tail bound.
