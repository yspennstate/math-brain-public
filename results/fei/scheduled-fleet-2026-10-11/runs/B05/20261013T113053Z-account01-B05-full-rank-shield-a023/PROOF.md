# Full-rank bilinear shielding of arbitrary coherent cores

All vector spaces below are over \(\mathbb F_2\), logarithms are base two, and
\(U\) denotes the upper-set functional in the campaign definition.

## Theorem (square shield; constant 2)

Let \(m\geq1\), let \(M\in\mathbb F_2^{m\times m}\) be invertible, and let
\(D:\mathbb F_2^m\to\{-1,1\}\) be arbitrary.  For arbitrary affine data
\(a,b,c\), put

\[
 P(x,y)=(-1)^{x^TMy+a\cdot x+b\cdot y+c}D(y).
\]

Then

\[
 H(P)=2m,\qquad U(P)=m,\qquad I_x(P)=m/2.
\]

Consequently, for every Boolean \(h\) on variables disjoint from \((x,y)\)
and every finite adaptive or pruned restriction tree \(\mathcal T\) querying
only \((x,y)\), with leaf probabilities \(w_\ell\),

\[
 U(Ph)-\sum_\ell w_\ell U(P_\ell h)
 \leq 2 I_x(P)\leq2I(P).
\]

The constant is independent of dimension, tree depth, restriction order,
leaf probabilities, the complexity or bias of \(D\), and the terminal core
\(h\).

### Exact spectrum

For frequencies \((\alpha,\beta)\), orthogonality in \(x\) gives

\[
\begin{aligned}
 \widehat P(\alpha,\beta)
 &=2^{-2m}\sum_yD(y)(-1)^{(b+\beta)\cdot y+c}
   \sum_x(-1)^{x\cdot(My+a+\alpha)}\\
 &=2^{-m}D(y_\alpha)(-1)^{(b+\beta)\cdot y_\alpha+c},
\end{aligned}
\]

where \(y_\alpha=M^{-1}(a+\alpha)\).  Thus every one of the \(2^{2m}\)
Fourier coefficients has squared magnitude \(2^{-2m}\).  Hence \(H(P)=2m\).
For the uniform law on all subsets of the \(2m\) physical coordinates,
\(\pi(S)=2^{-|S|}\).  Therefore

\[
 U(P)=2^{-2m}\sum_S(2m-|S|)=m.
\]

Flipping \(x_i\) changes the phase by the nonzero linear form
\((\operatorname{row}_iM)\cdot y+a_i\).  It is balanced, so every
\(I_{x_i}(P)=1/2\), proving \(I_x(P)=m/2\).

### Complete signed node sum and single-use payment

For an internal tree node \(v\), define its signed charge

\[
 q_v=w_v\left(U(P_v)-\sum_{z\in\{-1,1\}}
   \Pr[z\mid v]U(P_{vz})\right).
\]

No sign assumption is imposed on an individual \(q_v\).  Exact telescoping
gives

\[
 \sum_{v\text{ internal}}q_v
 =U(P)-\sum_\ell w_\ell U(P_\ell)\leq U(P)=m.
\]

This is the nonlocal single-use reservoir: intersecting exceptional layers
are not separately charged.  Reveal order is immaterial because both orders
produce the same telescoped endpoint expression.

For disjoint functions, squared Fourier laws tensor, principal-upper-set
masses tensor, and therefore \(U(gh)=U(g)+U(h)\).  Applying this at the root
and every leaf cancels the arbitrary terminal \(U(h)\), yielding the stated
retained-credit inequality.

## Rectangular extension (constant 4)

Let now \(M\in\mathbb F_2^{s\times m}\), \(s\geq m\), have full column rank.
The same calculation shows that \(\widehat P(\alpha,\beta)\) is nonzero
exactly when \(a+\alpha\in\operatorname{im}M\), and then has magnitude
\(2^{-m}\).  There are again \(2^{2m}\) atoms, so \(H(P)=2m\) and
\(U(P)\leq H(P)=2m\).

At least \(m\) physical rows of \(M\) are nonzero.  Each corresponding
\(x_i\) has influence \(1/2\), hence \(I_x(P)\geq m/2\).  The same
telescoping argument therefore gives

\[
 U(Ph)-\sum_\ell w_\ell U(P_\ell h)
 \leq4I_x(P)\leq4I(P).
\]

## Two-cylinder and many-cylinder corollary

Partition the \(y\)-coordinates into arbitrary, possibly uneven blocks and
let \(D(y)\) be any product of point-defect signs, or any Boolean combination
of overlapping defect indicators.  It is still simply an arbitrary Boolean
\(D\), so the theorem applies unchanged.  Thus the two-cylinder exceptional
filter intersection is fully paid in the full-column-rank regime, and in
fact the number, overlap, biases, and internal complexity of the cylinders
do not enter the constant.

## Exact remaining gap

If \(\operatorname{rank}M<m\), the constraint \(My=a+\alpha\) has a
positive-dimensional fiber.  The Fourier coefficient is then a signed sum
of \(D\) over that fiber rather than a single value.  Coherent interference
returns, the spectral law need not be flat, and the root reservoir is not
controlled by the argument above with a dimension-free multiple of the
available physical selector influence.  This positive-codimension regime,
or hierarchies not admitting one fixed full-rank shield, remains OPEN.

The result is a proper-class retained-credit theorem, not full FEI.  Its flat
spectrum is the classical Maiorana--McFarland/bent mechanism; no literature
priority is claimed.  The campaign-level novelty claim is limited to the
explicit complete-tree retained-\(U\) consequence with arbitrary shared and
terminal cores.
