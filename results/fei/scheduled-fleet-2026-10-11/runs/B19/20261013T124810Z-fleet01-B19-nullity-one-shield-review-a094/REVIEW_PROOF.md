# Independent reconstruction of the nullity-one shield

All vector spaces are over \(\mathbb F_2\).  This reconstruction uses the
physical \((x,y)\)-coordinates throughout.

Let
\[
P(x,y)=(-1)^{x^TMy+a\cdot x+b\cdot y+c}D(y),
\qquad \operatorname{rank}M=m-1=:r,
\]
where \(D\) is an arbitrary Boolean function.

## Fourier law

For physical frequency \((\alpha,\beta)\), summing first over \(x\) gives
\[
\widehat P(\alpha,\beta)
=2^{-m}(-1)^c
\sum_{y:My=a+\alpha}D(y)(-1)^{(b+\beta)\cdot y}.
\]
There are \(2^r\) admissible values of \(\alpha\).  Fix a nonzero physical
kernel vector \(v\), so every nonempty fiber is \(\{y_0,y_0+v\}\).  Its
sum is
\[
D(y_0)(-1)^{(b+\beta)\cdot y_0}
\left(1+\frac{D(y_0+v)}{D(y_0)}
(-1)^{(b+\beta)\cdot v}\right).
\]
Exactly one parity class of \(\beta\cdot v\) survives.  It contains
\(2^{m-1}=2^r\) physical frequencies, and the surviving numerator has
absolute value two.  Consequently there are exactly \(2^{2r}\) nonzero
Fourier coefficients, each of magnitude \(2^{1-m}=2^{-r}\).  Hence
\[
H(P)=2r,\qquad U(P)\le H(P)=2r.
\]
This proves the flatness claim for every physical kernel orientation and
every affine phase without changing coordinates.

## Physical influence

If row \(i\) of \(M\) is nonzero, the ratio after flipping \(x_i\) is a
nonconstant affine character of \(y\), hence is negative on exactly half of
the cube.  Thus \(\operatorname{Inf}_{x_i}(P)=1/2\).  At least \(r\) rows
are nonzero, so \(I_x(P)\ge r/2\).

If column \(j\) is nonzero, then for each fixed \(y\) the ratio after
flipping \(y_j\) is the product of the fixed sign
\((-1)^{b_j}D(y+e_j)/D(y)\) and the nonconstant character
\((-1)^{x\cdot\operatorname{col}_jM}\).  Averaging over physical \(x\)
makes it negative with probability \(1/2\).  Thus every nonzero column also
has influence \(1/2\).  At least \(r\) columns are nonzero, so
\(I_y(P)\ge r/2\).  Therefore
\[
U(P)\le4I_x(P),\qquad U(P)\le2(I_x(P)+I_y(P))\le2I(P).
\]
The edge case \(r=0,m=1\) is included: \(P\) is a character, so \(U=0\).

## Adaptive/pruned trees and a disjoint common core

For any finite adaptive or pruned tree querying only physical \((x,y)\)
coordinates, conditional expectation makes the signed internal-node sum
telescope exactly to
\[
U(P)-\sum_\ell w_\ell U(P_\ell).
\]
Since \(U\ge0\), this is at most the root reservoir \(U(P)\), yielding both
bounds above.  No individual node charge is asserted to be positive, and no
physical event is assigned to more than one node.

If \(h\) is one common Boolean function on a disjoint block, Fourier
products give \(U(P_vh)=U(P_v)+U(h)\) at the root and every leaf.  Since
\(\sum_\ell w_\ell=1\), the \(U(h)\) term cancels.

## Exact scope

This is a root-reservoir/endpoint-telescoping theorem.  It does not prove a
nonnegative nodewise payment, permit a changing or leaf-dependent core, or
control the sum of all root coordinate charges in the universal GU target.
For nullity at least two, a fiber can have several unequal Walsh masses, so
the flat-spectrum step fails and a new payment for conditional fiber entropy
is required.
