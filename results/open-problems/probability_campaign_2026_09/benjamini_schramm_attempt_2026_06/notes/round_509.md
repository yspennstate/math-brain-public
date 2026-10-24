# Round 509 two-sided tilt fails in low branching

Round 508 closes monotone trace families.  A natural attempt for nonmonotone
height traces is to use an exponential tilt toward the endpoint.  This is
still too crude in the low-branching cases.

Suppose the endpoint lies to the right.  After dividing by
\(\alpha^{h_{\rm end}-h_{\rm start}}\), a positive height increment of length
\(\ell\) has effective length weight \((z/\alpha)^\ell\), while a negative
height increment has effective length weight \((z\alpha)^\ell\).  Thus
\[
  P_+(\alpha)=\frac{z/\alpha}{1-z/\alpha},
  \qquad
  P_-(\alpha)=\frac{z\alpha}{1-z\alpha},
  \qquad
  P(\alpha)=P_+(\alpha)+P_-(\alpha).
\]
Using only the no-consecutive-vertical rule and the packet constant \(C\),
the same one-trace majorant as Round 508 becomes
\[
  H^{\pm}_{q,z,\alpha}(C)
  =
  \frac{P(\alpha)\bigl(1+Cc_q(z)+Cc_q(z)P(\alpha)\bigr)}
       {1-Cc_q(z)P(\alpha)(1+P(\alpha))}.
\]
The tilt is optimized at \(\alpha=1\), where \(P(\alpha)=2z/(1-z)\).

For fixed \(P\) and \(c=c_q(z)\), the scalar supersolution inequality
\[
  H^{\pm}_{q,z,\alpha}(C)\le C
\]
has a solution \(C\) only if
\[
  (1-b)^2-4bP\ge0,
  \qquad b=cP(1+P).
\]
At the target radius \(z=M_q^{-1}\), with the optimal \(\alpha=1\), this
discriminant is negative for
\[
  q=2,3,4,5,6
\]
and becomes positive starting at \(q=7\).  The first values are:
\[
\begin{array}{c|c|c}
q & P=2z/(1-z) & (1-b)^2-4bP\\
\hline
2 & 1.265752\ldots & -1.610869\ldots\\
3 & 1.101500\ldots & -1.110873\ldots\\
4 & 1 & -0.817600\ldots\\
5 & 0.894427\ldots & -0.369915\ldots\\
6 & 0.816497\ldots & -0.080829\ldots\\
7 & 0.755929\ldots & 0.118966\ldots
\end{array}
\]

Thus the nonmonotone problem cannot be solved for the key low-branching
cases by a plain two-sided tilted row-sum majorant.  The missing estimate
must use structure discarded by this tilt:

* global distinctness of portal heights;
* adjacent-gap hard-core constraints for vertical intervals;
* the killed annular-excess walk;
* mutual avoidance among packet traces sharing the root column.

This narrows the remaining obstruction.  Monotone traces and high-branching
nonmonotone traces are compatible with the packet supersolution; the hard
case is low-branching nonmonotone height motion.
