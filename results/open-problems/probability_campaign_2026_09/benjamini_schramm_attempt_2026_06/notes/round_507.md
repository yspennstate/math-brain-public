# Round 507 span-resolved trace skeleton

Round 506 proves a row-summed skeleton is subcritical, but a packet norm also
needs uniform control after dividing by the endpoint span weight.  A pure
row-sum bound does not see the following issue: a long monotone height change
can be subdivided into many portal jumps, and if the norm uses exactly the
same span weight as each atom, those subdivisions create an exponential
factor in the endpoint span.

The corrected way to state the scalar skeleton is span-resolved.  Let
\[
  c_q(z)=qz^2w_*(z)^2,
  \qquad
  w_*(z)=\frac{2z}{1+z^2}.
\]
Here \(c_q(z)\) is the child-atom cost before summing over the height length
of that atom.  For a monotone positive height increment, an atom of length
\(\ell\ge1\) contributes:

* \(c_q(z)z^\ell\) if it is a child atom;
* \(z^\ell\) if it is a vertical atom.

Vertical atoms are not allowed to be consecutive.  Put
\[
  P(x)=\frac{x}{1-x}.
\]
The length-generating transfer matrix for monotone subdivisions is
\[
  R_c(x)=
  \begin{pmatrix}
    cP(x)&P(x)\\
    cP(x)&0
  \end{pmatrix}.
\]
The critical equation is
\[
  cP(1+P)=1.
\]
Equivalently, if \(\lambda(c)\) is the exponential growth factor per unit
height span, then
\[
  \lambda(c)
  =
  \frac{2+c+\sqrt{c^2+4c}}{2},
  \qquad
  (\lambda(c)-1)^2=c\lambda(c).
\]
Thus monotone trace subdivisions of total span \(n\) are controlled by
\[
  \bigl(z\lambda(c_q(z))\bigr)^n
\]
up to subexponential or constant factors.

At the target radius \(z=M_q^{-1}\), this span base is \(<1\) for all integer
\(q\ge2\).  Numerically:
\[
\begin{array}{c|c|c|c}
q & z & c_q(z) & z\lambda(c_q(z))\\
\hline
2 & 0.387584\ldots & 0.136455\ldots & 0.559622\ldots\\
3 & 0.355151\ldots & 0.150540\ldots & 0.522249\ldots\\
4 & 1/3 & 0.16 & 0.495974\ldots
\end{array}
\]
For \(q\ge4\), \(z\le1/3\) and \(c_q(z)\le0.16\), so the span base is at most
the \(q=4\) value.

Consequently the packet span parameter should not be taken as
\(\alpha\downarrow z\).  It should be chosen with slack:
\[
  z\lambda(c_q(z))<\alpha<1.
\]
This absorbs monotone portal subdivisions uniformly in the endpoint height
difference.  Nonmonotone height traces have larger total variation than net
span and should be controlled by the same slack together with the killed
excess constraint.

The next packet norm should therefore use this span-resolved \(\alpha\), the
excess multiplier \(w_*(z)\), and the adjacent-gap gas.  The scalar
ingredients are now all below one at \(z<M_q^{-1}\); what remains is the
formal packet-family inequality.
