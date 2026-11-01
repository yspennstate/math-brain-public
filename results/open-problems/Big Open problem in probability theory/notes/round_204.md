# Round 204

Round 204 splits the \(q\)-weighted exact-sphere excess-length target from
Round 203 into a finite-excess maximum and a long-excess tail.

For \(L=\log_\Delta\bar\chi_p\), set
\[
  K_{\rho,p}=\lfloor\rho L\rfloor.
\]
The finite-excess profile is
\[
  \mathfrak A_{q,\rho}^{\rm saw}(s,p)
  =
  \sup q^k\mathfrak N_{n,k}^{\rm saw,sph},
\]
where the supremum is over the half-to-full window for \(n\) and
\(0\le k\le K_{\rho,p}\).  The long-excess tail is
\[
  \mathfrak T_{q,\rho}^{\rm saw}(s,p)
  =
  \sup_n\sum_{k>K_{\rho,p}}q^k
  \mathfrak N_{n,k}^{\rm saw,sph}.
\]

Since the finite part has only \(K_{\rho,p}+1=O(L)\) terms, its polynomial
factor is invisible after division by \(L\).  Thus it is enough to prove the
same Round 203 exponent margin separately for
\(\mathfrak A_{q,\rho}^{\rm saw}\) and
\(\mathfrak T_{q,\rho}^{\rm saw}\).

This turns the remaining obstruction into two cleaner tasks: control the
weighted excess spectrum up to linear excess, and prove a true tail estimate
for paths with excess larger than \(\rho L\).
