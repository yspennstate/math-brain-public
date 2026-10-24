# Round 081 log

## Goal

Remove the remaining tautology from the separator-convolution abstraction.
After Round 080, endpoint separators were disallowed, but the property could
still be satisfied vacuously by taking a single non-buffer piece \(K_1=K\), in
which case the same-piece term is the original finite-set escape quantity.

## Local separator-convolution property

Added a local version.  For every \(\delta>0\), near \(p_c\), every finite set
\(K\) should admit a buffered partition
\[
  K=K_0\sqcup K_1\sqcup\cdots\sqcup K_m
\]
with
\[
  \operatorname{diam}(K_i)\le R
  \qquad (i\ge1),
\]
for a fixed \(R=R(\delta)\), and with both the buffer mass
\[
  \mathcal B_p(K_0;K)
\]
and the proper separator-convolution mass
\[
  \mathcal C_p(K_1,\ldots,K_m;W)
\]
at most \(\delta\).

## Criterion

The bounded-diameter condition makes the same-piece term automatic.  If the
maximum degree is \(\Delta\), every piece has size at most
\[
  V_R=1+\Delta\sum_{\ell=0}^{R-1}(\Delta-1)^\ell.
\]
Thus
\[
  \sum_i\sum_{x,y\in K_i}\tau_p(x,y)
  \le V_R |K|.
\]
Since \(\chi_p\to\infty\) as \(p\uparrow p_c\), the normalized same-piece mass
is \(o(1)\).  The buffer and separator-convolution assumptions then imply
finite-set escape.

## Result

Added `def:local-separator-convolution`,
`prop:local-separator-convolution`, and
`thm:local-separator-intermediate`.

The new conditional theorem is:
\[
  \text{local separator-convolution property}+\text{MF}
  \Longrightarrow
  p_c(G)<p_{2\to2}(G).
\]

This is now a non-tautological target: the local pieces handle trapped internal
mass, while the hard part is controlling the buffer and proper separator
convolution.
