# Dense nullity-two bilinear shielding in the physical basis

All vector spaces are over \(\mathbb F_2\), and all logarithms are base two.
For a Boolean function \(f\), write \(H(f)\), \(U(f)\), and \(I(f)\) for
Fourier entropy, the campaign upper-set functional, and total physical
influence.

## Theorem

Let \(M\in\mathbb F_2^{s\times m}\) have rank \(r=m-2\), let
\(D:\mathbb F_2^m\to\{-1,1\}\) be arbitrary, and put

\[
 P(x,y)=(-1)^{x^TMy+a\cdot x+b\cdot y+c}D(y).
 \tag{1}
\]

No coordinate alignment of \(\ker M\) is assumed. Then

\[
 \boxed{H(P)\le 2I(P),\qquad U(P)\le2I(P).}           \tag{2}
\]

Consequently, if \(h\) is any Boolean function on a disjoint physical block
and \(\mathcal T\) is any finite adaptive/pruned restriction tree querying
only variables of \(P\), then

\[
 \boxed{
 U(Ph)-\sum_{\ell}w_\ell U(P_\ell h)\le2I(P).}
 \tag{3}
\]

The constant two is independent of \(s,m\), the physical orientation of the
two-dimensional kernel, the core \(D\), tree depth, reveal order, leaf
probabilities, and the common disjoint terminal core. It is sharp already at
\(r=0\), for a nonaffine two-bit Boolean function.

## 1. Exact physical-basis fiber entropy

Let \(K=\ker M\), so \(\dim K=2\). Orthogonality in \(x\) gives, for physical
frequencies \((\alpha,\beta)\),

\[
 \widehat P(\alpha,\beta)
 =2^{-m}(-1)^c
 \sum_{y:\,My=a+\alpha}D(y)(-1)^{(b+\beta)\cdot y}.
 \tag{4}
\]

For each admissible \(\alpha\), the summation set is one affine coset
\(C=y_0+K\). Normalize its four-point Walsh transform by

\[
 \widehat D_C(\chi)=\frac14\sum_{k\in K}D(y_0+k)(-1)^{\chi(k)}.
\]

Each character \(\chi\) of \(K\) has exactly \(2^r\) physical extensions
\(\beta\). Hence (4) says that the squared Fourier law is the exact mixture:
choose one of the \(2^r\) cosets uniformly, choose one of the \(2^r\)
extensions uniformly, and then sample \(\chi\) from
\(\widehat D_C(\chi)^2\). Therefore

\[
 \boxed{H(P)=2r+\mathbb E_C H(D_C).}                  \tag{5}
\]

This derivation stays in the original physical basis. The affine phases only
permute/sign the relevant Fourier coefficients and do not affect (5).

## 2. The orientation-sensitive two-bit lemma

Let

\[
 Z=\{j:\operatorname{col}_j(M)=0\},\qquad z=|Z|.
\]

The standard vectors \(e_j\), \(j\in Z\), lie in the two-dimensional space
\(K\), so \(z\in\{0,1,2\}\). Put

\[
 A=\sum_{j\in Z}\operatorname{Inf}_j(D).
\]

For every Boolean function on a two-dimensional affine cube:

\[
 H(D_C)\le
 \begin{cases}
 2, &z=0,\\
 1+2\operatorname{Inf}_{e_j}(D_C), &Z=\{j\},\\
 2\sum_{j\in Z}\operatorname{Inf}_{e_j}(D_C), &z=2.
 \end{cases}                                           \tag{6}
\]

For \(z=0\), this is simply entropy at most the logarithm of the four-point
support. For \(z=1,2\), choose the aligned standard vector(s) as part or all
of a basis of \(K\). A two-bit Boolean function is either affine, in which
case its Fourier entropy is zero, or nonaffine, in which case all four
Fourier squares are \(1/4\) and both basis-direction influences are \(1/2\).
This proves (6) without a numerical maximization.

The cosets partition the cube, so averaging a fiber influence in a standard
kernel direction gives the corresponding global physical influence of
\(D\). Thus (6) implies the unified bound

\[
 \mathbb E_C H(D_C)\le 2-z+2A.                        \tag{7}
\]

## 3. Physical influence pays the fiber entropy

Every nonzero physical row of \(M\) gives an \(x\)-coordinate of influence
\(1/2\), independently of \(D\), and rank \(r\) forces at least \(r\)
nonzero rows. Hence

\[
 I_x(P)\ge r/2.                                       \tag{8}
\]

For \(j\notin Z\), flipping \(y_j\) changes the bilinear phase by a nonzero
linear form in \(x\); averaging over \(x\) makes the derivative balanced,
so \(\operatorname{Inf}_{y_j}(P)=1/2\). For \(j\in Z\), the bilinear phase
does not change and
\(\operatorname{Inf}_{y_j}(P)=\operatorname{Inf}_j(D)\). Consequently

\[
 I_y(P)=\frac{m-z}{2}+A.                              \tag{9}
\]

Since \(m=r+2\), (8)--(9) give

\[
 2I(P)\ge 2r+2-z+2A.                                 \tag{10}
\]

Combining (5), (7), and (10) proves \(H(P)\le2I(P)\).
Also \(0\le U(P)\le H(P)\), proving (2).

The accounting explains why no dense-orientation penalty occurs. Every
physical kernel axis removes one forced half-influence, but the corresponding
two-bit fiber lemma removes exactly one unit of unpaid entropy (and retains
twice its true physical influence). With no aligned axis, all \(m\)
\(y\)-coordinates are already forced to influence \(1/2\).

## 4. Complete signed restriction-tree payment

For any finite tree, the complete signed node sum telescopes:

\[
 \sum_{v\in\mathcal T^\circ}w_v
 \left(U(P_vh)-\frac{U(P_{v,0}h)+U(P_{v,1}h)}2\right)
 =U(Ph)-\sum_\ell w_\ell U(P_\ell h).                \tag{11}
\]

Disjoint tensor additivity gives \(U(P_vh)=U(P_v)+U(h)\), so the common
terminal-core term cancels exactly. Nonnegativity of leaf \(U\), followed by
(2), yields

\[
 U(Ph)-\sum_\ell w_\ell U(P_\ell h)
 \le U(P)\le2I(P).
\]

No sign is assigned to individual node charges, and no closure claim about
the restricted descendants is needed. In particular, rare dyadic leaves and
changing coherent descendants cannot spend the root reservoir more than
once.

## 5. Boundary at nullity three

The same orientation bookkeeping for kernel dimension \(t\) leaves the
entropy of a Boolean \(t\)-bit fiber after subtracting the forced
half-influences of nonkernel physical columns. At \(t=2\), classification of
two-bit Boolean functions closes this packet with constant two. At
\(t\ge3\), a nonaffine fiber need not be flat and no analogue of (7) with an
absolute constant independent of \(t\) is known. In the fully aligned case,
such an all-\(t\) bound is full-FEI-hard by the previously proved rank-one
tensor embedding. Thus (2) removes the orientation gap at width two but does
not settle the universal fiber payment or full FEI.

