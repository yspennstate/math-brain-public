# Round 080 log

## Goal

Audit the Round 079 separator-convolution abstraction for degeneracies before
using it as a future target.

## Issue found

The first version allowed \(W_{ij}\) to contain endpoints.  Then the singleton
partition \(K=\bigsqcup_{x\in K}\{x\}\), with \(W_{xy}=\{x\}\), turns the
separator-convolution condition into the original finite-set escape quantity:
\[
  \sum_{z\in W_{xy}}\tau_p(x,z)\tau_p(z,y)=\tau_p(x,y).
\]
Thus the property was formally correct as a criterion but essentially
tautological.  It was not a useful abstraction of geometric separation.

## Correction

Replaced the separator setup by a buffered partition
\[
  K=K_0\sqcup K_1\sqcup\cdots\sqcup K_m.
\]
The part \(K_0\) is a buffer/interface whose normalized two-point mass must be
small.  For \(i,j\ge1\), the separator \(W_{ij}\) is now required to be proper:
\[
  W_{ij}\cap(K_i\cup K_j)=\varnothing,
\]
and every path from \(K_i\) to \(K_j\) must hit \(W_{ij}\).

The corrected criterion requires three near-critical small quantities:
\[
  \mathcal B_p(K_0;K)=
  \frac{2}{\chi_p|K|}\sum_{x\in K_0,y\in K}\tau_p(x,y),
\]
the same-piece mass over \(K_1,\ldots,K_m\), and the proper
separator-convolution term.  These bounds imply finite-set escape with a
factor \(3\delta\), and \(\delta\) is arbitrary.

## Result

The separator-convolution property is now non-tautological.  It is closer to
the intended hyperbolic/half-space picture: vertices lying in the interface are
paid for through the buffer term, and cross-piece connections must pass through
a genuinely separate weighted separator.
