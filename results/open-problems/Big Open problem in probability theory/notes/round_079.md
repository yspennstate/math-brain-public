# Round 079 log

Update: Round 080 corrected this abstraction by adding a buffer part and
requiring proper separators disjoint from the pieces being separated.  The
unbuffered formulation below records the idea, but the manuscript now uses the
Round 080 version.

## Goal

Move from finite-cycle diagnostics back to the main finite-set escape route by
adding a separator abstraction that actually uses percolation structure.

## Separator convolution

Let \(K=K_1\cup\cdots\cup K_m\) be a partition, and let \(W_{ij}\) be a path
separator between \(K_i\) and \(K_j\).  Define
\[
  U_i^p(z)=\sum_{x\in K_i}\tau_p(x,z).
\]
If \(x\in K_i\), \(y\in K_j\), and \(i\ne j\), every open self-avoiding path
from \(x\) to \(y\) hits \(W_{ij}\).  Splitting at the first hit and applying
BK gives
\[
  \tau_p(x,y)
  \le
  \sum_{z\in W_{ij}}\tau_p(x,z)\tau_p(z,y).
\]
After summing,
\[
  \sum_{x\in K_i,y\in K_j}\tau_p(x,y)
  \le
  \sum_{z\in W_{ij}}U_i^p(z)U_j^p(z).
\]

## Criterion

Added `lem:separator-convolution` and
`prop:separator-convolution-criterion` to the manuscript.  The criterion says
that finite-set escape follows if, uniformly near \(p_c\), every finite \(K\)
has a partition with
\[
  \sum_i\sum_{x,y\in K_i}\tau_p(x,y)=o(\chi_p |K|)
\]
and
\[
  \sum_{i\ne j}\sum_{z\in W_{ij}}U_i^p(z)U_j^p(z)=o(\chi_p |K|).
\]

Also added a uniform critical separator-convolution property and the conditional
intermediate theorem:
\[
  \text{separator-convolution property}+\text{MF}
  \Longrightarrow
  p_c(G)<p_{2\to2}(G).
\]

## Significance

This does not solve the conjecture, but it is a better target than raw
scattering.  The separator term is weighted by the two-point function, so a
future proof can try to use hyperbolic half-spaces, tilted mass transport, or a
new nonamenability mechanism to bound exactly the quantity that appears after
BK.
