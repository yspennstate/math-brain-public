# Round 508 monotone packet supersolution

Round 507 gives the right span scale.  The next step is to insert the packet
constant and check a genuine supersolution for monotone trace families.

Assume the recursive packet bound has the form
\[
  E_z(\Pi)\le C^{|\Pi|}
  w_*^{E_r(\Pi)}\alpha^{L(\Pi)}
\]
for the moment, suppressing the adjacent-gap gas.  Then every child atom in a
root trace carries the additional packet factor \(C\).  Put
\[
  c_q(z)=qz^2w_*(z)^2,\qquad t=\frac z\alpha,\qquad P(t)=\frac{t}{1-t}.
\]
After dividing by the output span weight \(\alpha^{|a-b|}\), a monotone trace
from height \(a\) to height \(b\) is bounded by the two-state generating
function with child inventory \(Cc_q(z)P(t)\) and vertical inventory \(P(t)\).
Starting from a non-vertical state, the total nonempty trace weight is
\[
  H_{q,z,\alpha}(C)
  =
  \frac{
    P(t)\bigl(1+Cc_q(z)+Cc_q(z)P(t)\bigr)
  }{
    1-Cc_q(z)P(t)(1+P(t))
  },
\]
provided the denominator is positive.

Thus a monotone one-trace supersolution is obtained when
\[
  H_{q,z,\alpha}(C)\le C.
\]
For a \(k\)-packet, ignoring mutual avoidance only makes the bound larger,
and the ordered family is then bounded by \(H_{q,z,\alpha}(C)^k\).  Hence the
same inequality gives the packet supersolution \(C^k\) in the monotone
model.

At the target radius \(z=M_q^{-1}\), the simple uniform choice
\[
  \alpha=0.9,\qquad C=2
\]
works for every integer \(q\ge2\).  The worst cases are:
\[
\begin{array}{c|c|c|c}
q & z & c_q(z) & H_{q,z,0.9}(2)\\
\hline
2 & 0.387584\ldots & 0.136455\ldots & 1.755378\ldots\\
3 & 0.355151\ldots & 0.150540\ldots & 1.444189\ldots\\
4 & 1/3 & 0.16 & 1.265548\ldots
\end{array}
\]
For \(q\ge4\), \(z\le1/3\) and \(c_q(z)\le0.16\), so the \(q=4\) line gives
a uniform upper bound.

This is the first concrete packet-level supersolution in the simplified
model.  It still treats height traces as monotone and suppresses the
adjacent-gap gas, but it shows that the recursive packet factor itself can
be closed with explicit constants at the corrected target scale.
