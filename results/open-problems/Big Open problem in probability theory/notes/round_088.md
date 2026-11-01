# Round 088 log

## Goal

Replace the failed sparse restricted-operator route with a finite-set
two-replica target that directly matches the separator square mass.

## Two-replica profile

For finite non-empty \(K\), define
\[
  \mathcal R_p(K)
  =
  \frac{1}{\bar\chi_p|K|}
  \sum_z\left(\sum_{x\in K}\tau_p(x,z)\right)^2
  =
  \frac{\|T_p\mathbf 1_K\|_2^2}{\bar\chi_p|K|},
\]
and let \(\mathcal R_p^*=\sup_K\mathcal R_p(K)\).

Added `prop:two-replica-implies-fe`: if
\[
  \limsup_{p\uparrow p_c}\mathcal R_p^*<\infty
\]
and \(\bar\chi_p\to\infty\), then finite-set escape holds.  The proof is just
Cauchy--Schwarz:
\[
  \frac{\langle \mathbf 1_K,T_p\mathbf 1_K\rangle}{\bar\chi_p|K|}
  \le
  \left(\frac{\mathcal R_p(K)}{\bar\chi_p}\right)^{1/2}.
\]

Added `thm:two-replica-intermediate`: the two-replica bound plus the
mean-field susceptibility input gives \(p_c<p_{2\to2}\).

## Tree-grid use

Added `prop:tree-grid-two-replica`: for finite-fiber projections to
\(\mathbb T\square\mathbb Z^s\), bounded \(\mathcal R_p^*\) implies the local
separator-convolution property.  Averaging over residue vectors gives
\[
  \frac{1}{L^{s+1}}\sum_{\mathbf a}
  \frac{1}{\bar\chi_p|K|}
  \sum_{z\in S_{\mathbf a}}(T_p\mathbf 1_K(z))^2
  \le
  \frac{s+1}{L}\mathcal R_p(K).
\]
Thus the separator square mass is controlled for the actual finite set,
without taking an operator-norm supremum that can be defeated by delta
functions.

## Significance

The new central target is:
\[
  \limsup_{p\uparrow p_c}\mathcal R_p^*<\infty.
\]
It is stronger than finite-set escape but weaker than global \(L^2\)
boundedness.  It is also naturally two-replica, matching the structure of the
Hutchcroft--Pan backscattering mechanism.
