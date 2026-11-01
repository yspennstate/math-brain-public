# Round 514 packet lift from the scalar record-envelope lemma

Round 513 isolates a single-trace scalar lemma.  If that lemma holds, the
packet-level scalar transform closes directly.

Let
\[
  B_q(z)=\frac{H_{q,z,0.99}(2)}{1-D_q(z)}
\]
where \(D_q\) is the neutral bubble inventory from Round 511.  The numeric
values in the residual cases are:
\[
\begin{array}{c|c|c}
q & B_q(M_q^{-1}) & 2-B_q(M_q^{-1})\\
\hline
2 & 1.742953\ldots & 0.257047\ldots\\
3 & 1.411562\ldots & 0.588438\ldots\\
4 & 1.223666\ldots & 0.776334\ldots\\
5 & 0.951638\ldots & 1.048362\ldots\\
6 & 0.788235\ldots & 1.211765\ldots
\end{array}
\]
Thus
\[
  B_q(M_q^{-1})<2=C
\]
for every \(q=2,\ldots,6\).  For \(q\ge7\), Round 509 already supplies a
coarse two-sided scalar supersolution, while the monotone argument covers all
integer \(q\ge2\).

Now consider a packet
\[
  \Pi=((a_1,b_1),\ldots,(a_k,b_k)).
\]
Apply the single-trace record-envelope encoding to each of the \(k\) trace
words in global order.  Since the scalar majorant already includes:

* the \(q\) choices of child label in \(c_q=qz^2w_*^2\);
* the recursive packet factor \(C\) for each child atom;
* the two crossing edges for each child atom;
* the monotone trace inventory \(H\);
* the ordered bubble sequence \(1/(1-D)\);

the total scalar contribution is bounded by
\[
  B_q(z)^k.
\]
Because \(B_q(z)<C\), this is at most \(C^k\), matching the packet
supersolution.

The shared root-column constraints in the actual packet transform can only
reduce the set of valid trace families compared with independently encoding
each trace.  The child packets created by all traces are collected in global
order, and the product of recursive bounds over child labels gives
\[
  \prod_{c=1}^q C^{|\Pi_c|}
  =
  C^{\sum_c|\Pi_c|},
\]
which is exactly the child-atom factor already used in the scalar majorant.

Therefore, modulo the single-trace record-envelope lemma and the previously
specified span/excess weights, the scalar part of the packet transform closes
with \(C=2\), \(\alpha=0.99\), and \(w=w_*(z)\) at \(z=M_q^{-1}\).  The final
remaining issue is to reinsert the ordered gap gas \(G_\eta(A)\) and verify
that virtual cuts of child atoms do not create a gap-weight deficit.
