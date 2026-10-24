# Aligned nullity-two fiber payment and the arbitrary-nullity hardness boundary

All vector spaces are over \(\mathbb F_2\), and logarithms are base two.

## Theorem 1: arbitrary changing two-bit fibers

Let \(M_0\in\mathbb F_2^{s\times r}\) have full column rank.  For
\(x\in\mathbb F_2^s\), \(u\in\mathbb F_2^r\), \(z\in\mathbb F_2^2\), let
\[
P(x,u,z)=(-1)^{x^TM_0u+a\cdot x+b\cdot u+c\cdot z+d}D(u,z),
\]
where \(D\) is an arbitrary Boolean function.  Then
\[
\boxed{H(P)\le2I(P),\qquad U(P)\le2I(P).}
\]
The constant is independent of \(s,r\), the orientation of the full-rank
shield \(M_0\), affine phase, core bias, and variation of the two-bit core
with \(u\).

Equivalently, this covers every bilinear matrix of rank \(m-2\) whose
two-dimensional kernel is spanned by two physical input coordinates, after
permuting those physical coordinates.

### Exact Fourier decomposition

Absorb the \(z\)-linear phase into
\[
E_u(z)=(-1)^{c\cdot z}D(u,z).
\]
For frequency \((\alpha,\beta,\gamma)\), orthogonality in \(x\) forces
\(M_0u=a+\alpha\).  Full column rank gives either no solution or one
solution \(u=u_\alpha\), and then
\[
|\widehat P(\alpha,\beta,\gamma)|
=2^{-r}|\widehat E_{u_\alpha}(\gamma)|.
\]
There are \(2^r\) admissible \(\alpha\)'s and, for each of them, \(2^r\)
choices of \(\beta\) with the same squared magnitude.  Therefore
\[
\boxed{H(P)=2r+2^{-r}\sum_u H(E_u).}                 \tag{1}
\]

### Exact physical influence payment

Every nonzero physical row of \(M_0\) contributes \(1/2\) to the
\(x\)-influence, regardless of \(D\); rank \(r\) supplies at least \(r\)
such rows.  Every \(u\)-column is nonzero, so each \(u_j\) also has
influence \(1/2\).  Finally, the shield does not depend on \(z\), hence
\[
I_z(P)=2^{-r}\sum_u I(E_u).
\]
Thus
\[
\boxed{I(P)\ge r+2^{-r}\sum_u I(E_u).}              \tag{2}
\]

Every Boolean function on two bits has algebraic normal form
\(e+pz_1+qz_2+tz_1z_2\).  If \(t=0\), it is affine and has Fourier entropy
zero.  If \(t=1\), it is quadratic bent: its four squared Fourier
coefficients are all \(1/4\), so \(H=2\), while both coordinate influences
are \(1/2\), so \(I=1\).  Consequently
\[
H(E_u)\le2I(E_u)
\]
for every fiber.  Equations (1)--(2) prove \(H(P)\le2I(P)\), and
\(U(P)\le H(P)\) gives the upper-set endpoint.

## Theorem 2: general aligned fibers and the exact hardness boundary

The same calculation works with \(z\in\mathbb F_2^t\):
\[
H(P)=2r+\mathbb E_u H(E_u),\qquad
I(P)\ge r+\mathbb E_u I(E_u).                        \tag{3}
\]
Hence if every fiber belongs to a class with \(H\le C I\), then
\[
H(P)\le\max\{2,C\}I(P).                              \tag{4}
\]
This is useful for a uniformly controlled fiber class, but it cannot remove
the arbitrary-nullity parameter without solving FEI itself.

Indeed, take \(s=r\), \(M_0=I_r\), and let \(D(u,z)=g(z)\) be independent
of \(u\).  Then, up to affine signs,
\[
P=q_r\,g,qquad q_r(x,u)=(-1)^{x\cdot u},
\]
on disjoint blocks.  For every Boolean \(g\),
\[
\begin{aligned}
H(q_rg)&=2r+H(g),& I(q_rg)&=r+I(g),\\
U(q_rg)&=r+U(g),& G(q_rg)&=2r+G(g).
\end{aligned}                                        \tag{5}
\]
Here \(G(f)=\sum_i[U(f)-\mathbb E U(f|x_i)]\).  The last identity follows
from disjoint tensor additivity of \(U\), coordinatewise.

Apply (5) to \(q_r g^{\otimes N}\) and divide by \(N\).  Letting
\(N\to\infty\) gives three precise reductions:

1. a uniform \(H\le C I\) theorem for arbitrary aligned fibers implies
   full FEI with the same \(C\);
2. a uniform \(U\le K I\) theorem implies the universal \(U\)-endpoint;
3. a uniform
   \(G\le aI+bU\) theorem implies the universal GU' inequality with the
   same \((a,b)\).

Thus arbitrary-nullity aligned fibers are not a proper intermediate target:
they contain an arbitrary Boolean tensor factor with only fixed shield
overhead.  A productive next step must either control a genuine restricted
fiber class, exploit interaction between changing fibers, or prove the
universal inequality itself.

## Restriction-closure warning

The nullity-two endpoint is not restriction closed.  Restricting a shield
coordinate \(x_i\) leaves its paired \(u_i\) unshielded and increases the
physical kernel dimension.  Iterating this operation reaches the
arbitrary-nullity hardness family above.  Therefore (1)--(2) are a direct
FEI class theorem, not a GU-induction proof and not a proof of full FEI.
