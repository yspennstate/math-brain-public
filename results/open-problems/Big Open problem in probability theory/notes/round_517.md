# Round 517 scalar span-only bootstrap obstruction

Round 516 leaves open a bootstrap from a stronger span scale to a weaker one.
The scalar span-only bootstrap fails in the low-branching residual cases.

First solve the monotone recursive scalar fixed point exactly.  Let
\[
  b_q(z)=qz^2w_*^2,\qquad V(x)=\frac{zx}{1-zx}.
\]
If \(F(x)\) is the monotone trace generating function by endpoint span, the
no-consecutive-vertical skeleton gives
\[
  F=V+b_q(1+V)F+b_q(1+V)F^2.
\]
The singularity occurs when
\[
  \bigl(1-b_q(1+V)\bigr)^2
  =
  4b_q(1+V)V.
\]
At \(z=M_q^{-1}\), the corresponding monotone span bases are:
\[
\begin{array}{c|ccccc}
q&2&3&4&5&6\\
\hline
\beta_q
&0.974664&0.948207&0.925926&0.829994&0.753661
\end{array}
\]
Thus monotone control is only available in \(\mathcal B_\theta\) for
\(\theta>\beta_q\).

Trying to start a two-scale step just above \(\beta_q\) leaves too little
room before scale \(1\).  For example, with
\[
  \theta=\beta_q+0.005,\qquad \alpha=0.999,
\]
and using the exact monotone input norm \(C_{\rm in}=F(1/\theta)\), the
denominator of the two-scale monotone transform is already negative for
\(q=2,3,4,5\).  The values are:
\[
\begin{array}{c|c|c|c|c}
q & \theta & C_{\rm in} & \text{denominator} & D\\
\hline
2&0.979664&1.513746&-16.099313&111.610481\\
3&0.953207&1.400357&-5.808671&23.171847\\
4&0.930926&1.332122&-3.374274&11.123932\\
5&0.834994&1.378449&-0.544124&2.071761\\
6&0.758661&1.426486&0.084944&0.946516
\end{array}
\]
Here \(D\) is the neutral bubble inventory at that input scale.

Therefore a span-only Banach-scale bootstrap cannot close the low-branching
cases.  The scalar calculations from Rounds 507--516 remain useful
calibrations, but the missing estimate must use structure that reduces
reversal entropy before the span scale approaches \(1\).  The available
sources are:

* the annular excess process, especially the fact that downward reversal
  depth must be funded by previously accumulated excess;
* the adjacent-gap hard-core gas on actual root-column vertical intervals;
* shared root-column self-avoidance between packet traces;
* stronger information about child packets than endpoint span alone.

The next viable norm should therefore be excess-sensitive, not merely
span-sensitive.  It should retain the current height excess \(e\) or a
record-height reserve, so that reversal bubbles are charged against a finite
budget rather than summed as unconstrained neutral loops.
