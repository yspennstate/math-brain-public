# Round 045 log

## Goal

Close the calibration question left in Round 006: does the boundary-energy
condition vanish on regular trees?

## Result

Yes.  For the \(d\)-regular tree \(T_d\),
\[
  \sup_{K\subset V\text{ finite}}\mathcal E_p(K)\to0
  \qquad (p\uparrow p_c(T_d)).
\]

## Proof idea

Let \(q=d-1\).  The same spherical estimate used for killed growth gives a
uniform bound
\[
  \sup_{p\le q^{-1}}\|T_p\|_{2\to2}<\infty.
\]
For finite \(K\), write
\[
  w(a)=\mathbf 1_{\partial_{\rm in}K}(a)\chi_p^K(a).
\]
Since finite-volume connections are dominated by ambient connections,
\[
  0\le w\le T_p\mathbf 1_K,
\]
so \(\|w\|_2\le C\sqrt{|K|}\).  The exterior boundary vector \(\mu_{p,K}\) is
obtained from \(w\) by a bounded-degree incidence map, hence
\[
  \|\mu_{p,K}\|_2^2\le C|K|.
\]
Finally,
\[
  \|Q_p\|_{2\to2}=\|T_p\|_{2\to2}/\bar\chi_p\le C/\bar\chi_p,
\]
and therefore
\[
  \mathcal E_p(K)
  =
  p^2|K|^{-1}\langle\mu_{p,K},Q_p\mu_{p,K}\rangle
  \le C/\bar\chi_p\to0.
\]

## Interpretation

The boundary-energy condition is correctly calibrated on the tree.  However,
the proof uses the already-known \(L^2\)-boundedness of \(T_p\) up to \(p_c\).
Using the same argument in the general conjecture would be circular: the real
task is to prove an analogue of \(\|\mu_{p,K}\|_2^2=O(|K|)\) or
\(\langle\mu,Q_p\mu\rangle=o(|K|)\) without first knowing the desired
\(L^2\)-boundedness.
