# Arbitrary physical orientation at nullity two

All vector spaces below are over \(\mathbb F_2\), Boolean values are in
\(\{-1,1\}\), and logarithms are base two.

## The shield class

Let \(M\in\mathbb F_2^{s\times m}\) have rank \(r=m-2\), and let
\[
 P(x,y)=(-1)^{x^TMy+a\cdot x+b\cdot y+c}D(y),
 \qquad x\in\mathbb F_2^s,\ y\in\mathbb F_2^m,                 \tag{1}
\]
where \(D\) is an arbitrary Boolean function.  No change of the physical
\(y\)-coordinates is made.  Put \(K=\ker M\), so \(\dim K=2\), and define
\[
 Z=\{j:Me_j=0\},\qquad k=|Z|.
\]
The vectors \(e_j\), \(j\in Z\), are independent members of \(K\), hence
\(0\le k\le2\).

## Exact entropy decomposition

For a frequency \((\alpha,\beta)\), summing first over \(x\) gives
\[
 \widehat P(\alpha,\beta)
 =2^{-m}(-1)^c
   \sum_{y:My=a+\alpha}D(y)(-1)^{(b+\beta)\cdot y}.           \tag{2}
\]
There are \(2^r\) nonempty fibers \(A_\alpha=y_\alpha+K\).  On each one,
write
\[
 E_\alpha(k)=(-1)^{b\cdot(y_\alpha+k)}D(y_\alpha+k),
 \qquad k\in K.
\]
Each character of \(K\) has \(2^r\) extensions to \(\mathbb F_2^m\), and
(2) assigns each extension squared mass \(2^{-2r}\) times the corresponding
fiber squared Walsh mass.  Consequently
\[
 \boxed{H(P)=2r+2^{-r}\sum_\alpha H(E_\alpha).}               \tag{3}
\]
This calculation is invariant under the choice of coordinates used only to
describe the abstract two-dimensional space \(K\).

## Physical influence ledger

If the \(i\)-th row of \(M\) is nonzero, flipping \(x_i\) changes the phase
on exactly half the \(y\)'s, so \(I_{x_i}(P)=1/2\).  Rank \(r\) supplies at
least \(r\) nonzero rows.  If \(Me_j\ne0\), then after flipping \(y_j\) the
derivative contains the nonconstant character
\((-1)^{x^TMe_j}\); averaging over \(x\) again gives
\(I_{y_j}(P)=1/2\), independently of \(D\).

For \(j\in Z\), the flip by \(e_j\) stays in the same coset of \(K\), and
its physical influence is exactly the average fiber directional influence.
Thus, with
\[
 J=2^{-r}\sum_\alpha\sum_{j\in Z}
       \operatorname{Inf}_{e_j}(E_\alpha),
\]
we have
\[
 \boxed{I(P)\ge {r\over2}+{m-k\over2}+J.}                   \tag{4}
\]

## The two-dimensional directional lemma

For every Boolean \(E\) on a two-dimensional affine cube,
\[
 H(E)\le 2-k+2\sum_{j\in Z}\operatorname{Inf}_{e_j}(E),     \tag{5}
\]
where the \(k\) displayed directions are independent.

Indeed, every two-bit Boolean function is either affine, in which case its
Fourier entropy is zero, or quadratic bent.  In the bent case all four
squared Fourier coefficients are \(1/4\), so \(H(E)=2\), and the derivative
in every nonzero direction is balanced, so each displayed influence is
\(1/2\).  The right side of (5) is therefore exactly 2 in the bent case and
is nonnegative in the affine case.

Average (5) over the cosets and use (3):
\[
 H(P)\le 2r+2-k+2J.                                         \tag{6}
\]
Because \(m=r+2\), doubling (4) gives
\[
 2I(P)\ge r+m-k+2J=2r+2-k+2J.                              \tag{7}
\]
Equations (6)--(7) prove the all-parameter theorem
\[
 \boxed{H(P)\le2I(P),\qquad U(P)\le H(P)\le2I(P).}          \tag{8}
\]
The constant is independent of \(s,m\), bias, affine phase, the two-bit
fibers, and the physical orientation of \(K\).  This strictly removes the
coordinate-alignment hypothesis from the preceding B01 theorem.

## Why this exact mechanism stops at nullity three

The tempting \(t\)-dimensional extension of (5) is
\[
 H(E)\stackrel{?}{\le}t-k+2\sum_{j\in Z}\operatorname{Inf}_{e_j}(E). \tag{9}
\]
It already fails at \((t,k)=(3,2)\).  Let \(E\) be the three-bit one-point
defect.  Its squared Walsh law is \(9/16\) at the empty set and \(1/16\) at
each of the other seven sets, while every coordinate influence is \(1/4\).
Hence
\[
 H(E)={7\over4}+{9\over16}\log_2{16\over9}>2
      =1+2\left({1\over4}+{1\over4}\right).                \tag{10}
\]

This failure is physically realizable inside (1).  Take \(s=1,m=4\),
\[
 M=(1,1,0,0),\qquad
 D(y)=-1\ \Longleftrightarrow\ y_1=y_3=y_4=0.               \tag{11}
\]
There is one point defect on each coset of \(\ker M\).  Directly from
(3)--(4), with equality in the influence ledger,
\[
 I(P)=2,qquad
 H(P)={15\over4}+{9\over16}\log_2{16\over9},               \tag{12}
\]
so
\[
 H(P)-2I(P)=-{1\over4}+{9\over16}\log_2{16\over9}
            \approx0.2169171867>0.                          \tag{13}
\]
Thus nullity two is the exact endpoint of the coefficient-two directional
fiber payment.  The witness is not a counterexample to FEI; it only refutes
the same constant and the direct higher-nullity generalization.

## Scope relative to GU'

The theorem is a direct root FEI/upper-set endpoint.  It is not restriction
closed: restricting shield coordinates can lower the rank and increase the
kernel dimension.  It therefore does not prove
\(G(P)\le aI(P)+bU(P)\), and no control with \(b<1\) of the aggregate
upper-set asymmetry mismatch follows from (8).  Full FEI remains open.

There is also no automatic transfer of the same constant from (8) to GU.
For an exact calibration inside this class, take
\[
 M=\begin{pmatrix}0&1&1&0\\1&1&0&1\end{pmatrix}
\]
and encode \(y=(y_1,y_2,y_3,y_4)\) by
\(y_1+2y_2+4y_3+8y_4\).  Let \(D(y)=+1\) precisely at
\[
 \{1,2,3,4,6,7,8,9,10,14\}
\]
and \(-1\) elsewhere.  Direct exact dyadic upper-set arithmetic gives
\[
 H(P)=6,\qquad U(P)=3,\qquad I(P)=3,\qquad G(P)={277\over32},
\]
and hence
\[
 {G(P)\over I(P)}={277\over96}>2.                         \tag{14}
\]
This is a quadratic-phase calibration already compatible with the earlier
quadratic \(G\le3I\) theorem; it is recorded here to prevent the invalid
inference \(U\le2I\Rightarrow G\le2I\).  The natural enlarged-class
candidate
\[
 \boxed{G(P)\le3I(P)\quad\text{for every rank-}(m-2)\text{ shield (1)}} \tag{15}
\]
survived the bounded checks but remains **OPEN**.  Proving (15), or a GU'
variant with \(b<1\), requires control of the upper-set asymmetry term under
the physical coordinate order; the entropy decomposition (3) alone does
not provide it.
