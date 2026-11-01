# Independent reconstruction and sharpening

All vector spaces are over \(\mathbb F_2\).  This reconstruction starts from
the displayed Boolean function, not from the author's checker.

Let \(M\in\mathbb F_2^{s\times m}\) have full column rank and set

\[
P(x,y)=(-1)^{x^TMy+a\cdot x+b\cdot y+c}D(y),
\]

where \(D:\mathbb F_2^m\to\{-1,1\}\) is arbitrary.

## 1. Spectrum

Orthogonality in \(x\) gives

\[
\widehat P(\alpha,\beta)=
\begin{cases}
2^{-m}D(y_\alpha)(-1)^{(b+\beta)\cdot y_\alpha+c},
 & a+\alpha=My_\alpha,\\
0,&a+\alpha\notin\operatorname{im}M.
\end{cases}
\]

Full column rank makes \(y_\alpha\) unique.  Thus the squared spectral law is
uniform on

\[
A\times\mathbb F_2^m,\qquad A=a+\operatorname{im}M,
\]

and has \(2^{2m}\) atoms.  Hence \(H(P)=2m\), independently of \(D\).
This verifies the author's first step.

## 2. Exact upper-set formula

Write \(p_A\) for the uniform law on \(A\).  Tensor additivity gives

\[
U(P)=U(p_A)+\frac m2.
\]

For \(\alpha\in A\), let \(S(\alpha)=\{i:\alpha_i=1\}\).  Points above
\(\alpha\) in \(A\) are \(\alpha+Mv\) with
\((Mv)_i=0\) for every \(i\in S(\alpha)\).  Therefore

\[
\frac{\pi_A(\alpha)}{p_A(\alpha)}
=2^{m-\operatorname{rank}M_{S(\alpha)}}
\]

and

\[
U(P)=\frac{3m}{2}-
\mathbb E_{\alpha\sim p_A}\operatorname{rank}M_{S(\alpha)}. \tag{1}
\]

The author's rectangular estimate \(U(P)\le H(P)=2m\) is valid.  Equation
(1) permits a strict improvement.

## 3. Reviewer-derived constant-2 strengthening

Choose any \(m\) physical rows of \(M\) forming a basis; call their index set
\(B\).  For every \(\alpha\),

\[
\operatorname{rank}M_{S(\alpha)}\ge |B\cap S(\alpha)|.
\]

Every basis row is nonzero, so for uniform \(y\), its coordinate
\(a_i+(My)_i\) is balanced.  Taking expectations yields

\[
\mathbb E\operatorname{rank}M_{S(\alpha)}\ge m/2.
\]

Substitution in (1) gives the stronger uniform estimate

\[
U(P)\le m. \tag{2}
\]

Every nonzero physical row contributes \(1/2\) to \(I_x(P)\), and full
column rank requires at least \(m\) nonzero rows.  (A zero row with \(a_i=1\)
only increases \(I_x\).)  Thus

\[
U(P)\le m\le2I_x(P). \tag{3}
\]

So the author's constant \(4\) is correct but nonoptimal: constant \(2\)
holds for every full-column-rank rectangular matrix, not only square
invertible matrices.  It is sharp because square invertible matrices have
\(U(P)=m=2I_x(P)\), and a complete reveal leaves constant functions.

This strengthening is new mathematics contributed by B19.  It is therefore
not independently accepted by this review and requires a fresh uninvolved
review.  It is logically unnecessary for accepting the author's v1 claim.

## 4. Complete tree and terminal core

For any finite adaptive or pruned restriction tree,

\[
\sum_{v\text{ internal}}w_v
\left(U(P_v)-\mathbb E[U(P_{vZ})\mid v]\right)
=U(P)-\sum_\ell w_\ell U(P_\ell).
\]

Since every leaf upper-set functional is nonnegative, this is at most
\(U(P)\).  The same identity holds without any local-charge sign assumption.
For one common Boolean \(h\) on disjoint variables,
\(U(P_vh)=U(P_v)+U(h)\) at the root and every leaf, so the \(U(h)\) terms
cancel.  Combining with the author's bound proves constant \(4\); combining
with (3) proves the reviewer-derived constant \(2\).

The exact scope is important: \(h\) is one common disjoint retained factor.
Leaf-dependent or shared-variable terminal cores are not licensed by this
tensor cancellation.

## 5. Surviving gap

When \(\operatorname{rank}M<m\), a Fourier coefficient contains a signed sum
of \(D\) over a positive-dimensional fiber.  Flatness, (1), and the basis-row
argument all fail at their first step.  No universal changing-core payment
is obtained.  Full FEI remains open.
