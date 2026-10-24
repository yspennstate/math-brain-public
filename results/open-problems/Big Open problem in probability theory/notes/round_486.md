# Round 486 column-cluster percolation comparison for \(T_d\square\mathbb Z\)

Round 486 adds a simple percolation comparison for the one-ended product
calibration.

Let \(q=d-1\) and orient the tree away from a root.  In Bernoulli bond
percolation on \(T_d\square\mathbb Z\), explore only through forward tree
children.  When a tree column is reached at height \(h\), reveal the open
vertical cluster in that column containing \(h\).  Its size is
\[
  N=1+L+R,
\]
where \(L,R\) are independent geometric random variables with
\(\mathbb P(L=k)=(1-p)p^k\).  Thus
\[
  \mathbb E[a^N]
  =
  a\left(\frac{1-p}{1-ap}\right)^2.
\]

For a given forward child column, the probability that at least one horizontal
edge from this vertical cluster into the child column is open is
\[
  1-(1-p)^N.
\]
Therefore the forward-column exploration dominates a Galton-Watson process
with mean
\[
  m_q(p)
  =
  q\,\mathbb E\!\left[1-(1-p)^N\right]
  =
  q\left(
    1-\frac{(1-p)^3}{(1-p+p^2)^2}
  \right).
\]
If \(m_q(p)>1\), then the open cluster survives with positive probability, so
\[
  \pc(T_d\square\mathbb Z)
  \le
  p_{\rm col}(q),
  \qquad
  m_q(p_{\rm col}(q))=1.
\]

This bound is especially useful for the low-branching case \(q=2\).  It gives
\[
  p_{\rm col}(2)=0.3276217564\ldots,
  \qquad
  1/p_{\rm col}(2)=3.0523003446\ldots.
\]
The current annular lower calibration at \(q=2\) is
\[
  \Lambda_2=2\cdot2^{1/4}=2.3784142300\ldots,
\]
so even the low-branching calibration remains below this elementary
inverse-\(\pc\) benchmark.

For every integer \(q\ge3\), the embedded tree already gives
\[
  1/\pc(T_d\square\mathbb Z)\ge q,
\]
and the explicit formula from Round 485 gives \(\Lambda_q<q\).  Thus the
known lower-bound constructions for \(\Gamma_{\rm ann}(T_d\square\mathbb Z)\)
do not threaten the target inequality
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)<1/\pc(T_d\square\mathbb Z).
\]

The remaining problem is upper control of the annular transfer, not a lower
bound obstruction from the portal constructions currently identified.
