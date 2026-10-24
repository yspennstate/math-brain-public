# Nullity-one bilinear shielding of arbitrary Boolean cores

All vector spaces are over \(\mathbb F_2\), logarithms are base two, and
\(U\) is the campaign upper-set functional in the physical Fourier basis.

## Theorem

Let \(M\in\mathbb F_2^{s\times m}\) have rank \(r=m-1\), let
\(D:\mathbb F_2^m\to\{-1,1\}\) be arbitrary, and set
\[
 P(x,y)=(-1)^{x^TMy+a\cdot x+b\cdot y+c}D(y),
 \qquad x\in\mathbb F_2^s,\ y\in\mathbb F_2^m.
\]
Then the squared Fourier law is uniform on exactly \(2^{2r}\) atoms.  Hence
\[
 H(P)=2r,\qquad U(P)\le2r,\qquad
 I_x(P)\ge r/2,\quad I_y(P)\ge r/2.
\]
Consequently, for every Boolean \(h\) on a disjoint block and every finite
adaptive or pruned physical restriction tree \(\mathcal T\) querying only
the \((x,y)\)-variables, with leaf probabilities \(w_\ell\),
\[
 \boxed{
 U(Ph)-\sum_\ell w_\ell U(P_\ell h)
 \le4I_x(P),\qquad
 U(Ph)-\sum_\ell w_\ell U(P_\ell h)
 \le2I(P).}
\]
The constant is independent of \(s,m\), physical orientation of
\(\ker M\), affine phase, the Boolean core \(D\), tree depth, reveal order,
leaf probabilities and the disjoint terminal core \(h\).

Together with the preceding full-column-rank theorem, this gives the same
constant four whenever \(\operatorname{rank}M\ge m-1\).

## Exact two-point-fiber spectrum

For physical frequencies \((\alpha,\beta)\), orthogonality in \(x\) gives
\[
 \widehat P(\alpha,\beta)
 =2^{-m}(-1)^c
 \sum_{y:\,My=a+\alpha}D(y)(-1)^{(b+\beta)\cdot y}. \tag{1}
\]
If \(a+\alpha\notin\operatorname{im}M\), the coefficient is zero.  Otherwise
the fiber is \(\{y_0,y_0+v\}\), where \(v\ne0\) spans \(\ker M\).  Put
\(\eta(y_0)=D(y_0+v)/D(y_0)\in\{-1,1\}\).  The sum in (1) is
\[
 D(y_0)(-1)^{(b+\beta)\cdot y_0}
 \left[1+\eta(y_0)(-1)^{(b+\beta)\cdot v}\right]. \tag{2}
\]
For each admissible \(\alpha\), exactly one of the two affine parity classes
of \(\beta\cdot v\) makes (2) nonzero.  On that class its magnitude is two.
There are \(2^r\) admissible \(\alpha\)'s and \(2^{m-1}=2^r\) surviving
\(\beta\)'s for each one.  Thus there are \(2^{2r}\) nonzero coefficients,
each of magnitude
\[
 2^{1-m}=2^{-r}.
\]
Their squares are the uniform law on this physical support.  This argument
uses no change of physical basis: a dense kernel vector \(v\) is allowed.
It follows immediately that \(H(P)=2r\).  Since every principal upper mass
is at most one, \(U(P)\le H(P)=2r\).

## Physical selector influence

Flipping \(x_i\) multiplies \(P\) by
\((-1)^{(\operatorname{row}_iM)\cdot y+a_i}\).  If row \(i\) is nonzero,
this linear form is balanced, independently of \(D\), so
\(\operatorname{Inf}_{x_i}(P)=1/2\).  A rank-\(r\) matrix has at least
\(r\) nonzero physical rows.  Therefore
\[
 I_x(P)\ge r/2,
\]
and the root reservoir satisfies \(U(P)\le4I_x(P)\).

There is also a stronger payment by total physical influence.  Flipping
\(y_j\) changes the bilinear phase by
\((-1)^{x\cdot(\operatorname{col}_jM)+b_j}\).  Whenever column \(j\) is
nonzero, averaging over \(x\) makes the derivative balanced regardless of
the core ratio \(D(y+e_j)/D(y)\), so
\(\operatorname{Inf}_{y_j}(P)=1/2\).  Rank \(r\) forces at least \(r\)
nonzero physical columns.  Therefore \(I_y(P)\ge r/2\), whence
\[
 U(P)\le2r\le2(I_x(P)+I_y(P))\le2I(P). \tag{3}
\]

## Complete-tree retained credit

For every finite restriction tree, signed node charges telescope exactly:
\[
 \sum_{v\text{ internal}}w_v
 \left(U(P_v)-\mathbb E[U(P_{v\pm})\mid v]\right)
 =U(P)-\sum_\ell w_\ell U(P_\ell). \tag{4}
\]
No sign is asserted for an individual node.  Since \(U\ge0\), (4) is at
most \(U(P)\), which is at most \(4I_x(P)\) and at most \(2I(P)\).  For a disjoint terminal core,
tensor additivity gives \(U(P_vh)=U(P_v)+U(h)\) at the root and every leaf,
so \(U(h)\) cancels exactly once.  This proves the theorem.

## Why nullity one is special

The proof works because every Boolean function on a two-point fiber has a
one-point Walsh support: it is affine on that fiber.  At nullity two, a
four-point restriction of \(D\) can have several unequal Fourier masses;
the physical spectrum need not be plateaued and the root bound above no
longer follows from selector influence alone.  Thus the theorem removes one
rank of the preceding full-rank hypothesis but does not control arbitrary
positive-dimensional fibers.

## Scope

This is a retained-credit theorem for one fixed bilinear shield, arbitrary
shared Boolean core and arbitrary one-dimensional kernel.  It does not prove
the universal GU inequality, handle nullity at least two with arbitrary
cores, or settle full FEI.  The flat/plateaued spectrum itself is classical;
the campaign claim is the exact rank-hypothesis removal and its nonlocal
complete-tree consequence.
