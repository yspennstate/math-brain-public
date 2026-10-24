# Round 505 corrected scalar child-atom inventory

Round 504 omitted a necessary cost.  A child atom in the root trace uses the
parent-child edge twice, once when entering the child cone and once when
exiting it.  Whether those two edges are included inside \(E_z(\Pi)\) or kept
outside the recursive call, every child atom carries a factor \(z^2\).

Keeping the crossing edges outside for bookkeeping, the crude scalar
row-sum inventory for one child atom is therefore
\[
  A_q(z)
  =
  q z^2 w_*(z)^2\frac{2z}{1-z},
  \qquad
  w_*(z)=\frac{2z}{1+z^2}.
\]
Equivalently,
\[
  A_q(z)
  =
  \frac{8qz^5}{(1-z)(1+z^2)^2}.
\]
This is the corrected version of \(C_{\rm row}\) from Round 504.

At the target radius \(z=M_q^{-1}\), this constant is small for every
integer \(q\ge2\).  If \(q=s^2\ge4\), then \(M_q=s+1\), and
\[
  A_q(M_q^{-1})
  =
  \frac{8s}{((s+1)^2+1)^2}
  \le
  \frac{16}{100}
  =
  0.16.
\]
For the two fresh-column-dominated integer cases,
\[
\begin{array}{c|c}
q & A_q(M_q^{-1})\\
\hline
2 & 0.1727181345\ldots\\
3 & 0.1658202069\ldots
\end{array}
\]
Thus the scalar child-atom proliferation is not the obstruction.  The
crossing-edge cost more than pays for the \(q\) child labels and the row sum
over height jumps.

The closure target should be revised accordingly.  A plausible next estimate
is no longer a contraction failure, but a geometric domination:
\[
  \sum_{\text{child atoms}}
  qz^2w_*^2 z^{|\Delta h|}
  \le A_q(z)<1
\]
for \(z<M_q^{-1}\), with \(\alpha\downarrow z\).  The remaining work is to
combine this small child-atom inventory with the adjacent-gap hard-core gas
and the external packet norm, rather than to seek extra savings against a
large row-sum constant.
