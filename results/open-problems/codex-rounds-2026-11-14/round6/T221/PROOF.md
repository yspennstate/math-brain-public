# Compatibility constraints on the seven-word table

Write
\[
W=(w_0,\ldots,w_6)=(1,a,b,aa,ab,ba,bb).
\]
Word evaluation is on the right: if the generator permutations are
\(A,B\), then \(T_{uv}=T_v\circ T_u\). A collision type is the
canonical class-label tuple \(\pi=(\pi_0,\ldots,\pi_6)\).
Put \(I_{ij}(\pi)=1_{\{\pi_i=\pi_j\}}\).

The results below strengthen a finite relaxation of type frequencies.
They do not establish an instance of RBS beyond those already known.
All logarithms are natural.

## 1. The existing relaxation

A type is admissible precisely when the two prescriptions
\[
a:(0,1),(1,3),(2,5),\qquad b:(0,2),(1,4),(2,6)
\tag{1}
\]
define injective partial maps on its classes. Equivalently, for any two
edges \((i,j),(k,l)\) in either list,
\(\pi_i=\pi_k\) if and only if \(\pi_j=\pi_l\).
Necessity follows from bijectivity of the generator permutations.
For sufficiency, extend each partial injection to a permutation by
matching its unused sources and targets. Starting at class \(\pi_0\)
gives exactly the prescribed seven images. There are 103 admissible
types among the 877 partitions of seven positions. Denote this set by
\(\mathcal T\).

Let
\[
K_0=(0,1,2),\quad K_a=(1,3,4),\quad K_b=(2,5,6),
\qquad \Sigma=\{000,001,010,011,012\}.
\]
Write \(s_g(\pi)\) for the canonical restriction to \(K_g\), and set
\[
D_{g,\sigma}(\pi)=1_{\{s_0(\pi)=\sigma\}}
                     -1_{\{s_g(\pi)=\sigma\}}.
\tag{2}
\]
Every finite permutation model has frequencies \(x_\pi\) satisfying
\[
x_\pi\geq0,\quad \sum_\pi x_\pi=1,\quad
\sum_\pi x_\pi D_{g,\sigma}(\pi)=0.
\tag{3}
\]
Indeed the child triple at a root is the root triple at its image under
the corresponding generator, which permutes the uniform roots.

The four rows
\[
D_{a,000},D_{a,001},D_{b,000},D_{b,010}
\]
vanish identically. For example, if the first and second positions of
the a-child triple coincide, injectivity of A implies that the root is
fixed by A. The entire child triple then equals the root triple. This
proves both a-identities; the b-identities follow by the same argument
with the first and third positions. The five rows for each generator
also sum to zero. The remaining row space has basis
\[
d_1=D_{a,010},\quad d_2=D_{a,011},\quad
d_3=D_{b,001},\quad d_4=D_{b,011}.
\tag{4}
\]
Independence is certified by the first four rows and columns of the
minor in (8) below.

For completeness, the earlier fair-AND entropy certificate was checked
exactly on this table. Give the classes independent fair bits \(X_q\)
and put
\[
R=X_{\pi_0},\quad E=\prod_{j\in K_0}X_{\pi_j},\quad
N=\left(\prod_{j\in K_g}X_{\pi_j}\right)_{g=0,a,b},
\qquad C_\pi=H(E)+H(R\mid N).
\]
Its certificate is
\[
C_\pi\geq\log2+\alpha d_2(\pi)+\beta d_3(\pi),
\tag{5}
\]
where
\[
\alpha=\tfrac12\log2-\tfrac34\log3-\tfrac7{16}\log7
                      +\tfrac{11}{16}\log11,
\qquad
\beta=-\log2-\tfrac58\log5+\tfrac78\log7.
\]
The 103 costs match their earlier exact logarithm forms. Expanding every
rational entropy as \(-\sum q\log q\), clearing the rational
exponents and comparing integer products proves (5) for all 103 types;
exactly three slacks vanish. This check uses no numerical optimization.

## 2. All single word-equality conjugacy tests

Define
\[
J(\pi)=I_{04}(\pi)-I_{05}(\pi).
\tag{6}
\]
Every finite permutation model satisfies \(\sum x_\pi J(\pi)=0\):
\(T_{ab}=BA\) and \(T_{ba}=AB\) are conjugate, since
\(A(BA)A^{-1}=AB\), so their fixed-point counts agree.
The same identity holds for limits of finite-model frequency vectors.

More generally, the event \(T_u(v)=T_z(v)\) is equivalent to
\(T_{uz^{-1}}(v)=v\). Fixed-point counts agree for conjugate words
and inverse words. Consider all constraints obtained by equating two
such event probabilities when the difference words are conjugate up to
inversion in the free group on a,b. The following list is complete for
the 21 unordered pairs of distinct positions in W.

| Conjugacy class, up to inversion | Word pairs |
|---|---|
| \(a\) | \((1,a),(a,aa),(b,ab),(b,ba)\) |
| \(b\) | \((1,b),(a,ab),(a,ba),(b,bb)\) |
| \(a^2\) | \((1,aa)\) |
| \(b^2\) | \((1,bb)\) |
| \(ab\) | \((1,ab),(1,ba)\) |
| \(ab^{-1}\) | \((a,b),(aa,ab),(aa,ba),(ab,bb),(ba,bb)\) |
| \(ab^{-2}\) | \((a,bb)\) |
| \(a^2b^{-1}\) | \((b,aa)\) |
| \(a^2b^{-2}\) | \((aa,bb)\) |
| \(aba^{-1}b^{-1}\) | \((ab,ba)\) |

To verify completeness, freely reduce each \(uz^{-1}\), cancel inverse
first and last letters until it is cyclically reduced, and list its
cyclic rotations and those of its inverse. Cyclically reduced words in
a free group are conjugate exactly when they differ by a cyclic
rotation. These ten classes are distinct under this test and contain
all \(4+4+1+1+2+5+1+1+1+1=21\) pairs. The finite lists can also
be checked directly; no word problem for a presented group occurs.

Within each row, subtract each event indicator from the first one. The
nonzero differences on admissible types are exactly
\[
\begin{array}{ll}
 I_{01}-I_{25}=d_3,& I_{02}-I_{14}=d_1,\\
 I_{12}-I_{34}=d_2,& I_{12}-I_{56}=d_4,\\
 I_{04}-I_{05}=J.&
\end{array}
\tag{7}
\]
All six other differences vanish pointwise. For example,
\(I_{01}=I_{13}=I_{24}\) by cancellation of the terminal generator;
\(I_{02}=I_{15}=I_{26}\); and
\(I_{12}=I_{35}=I_{46}\). The first two nonzero differences in (7)
are root-minus-child frequencies of a fixed generator, and the next
two are root-minus-child frequencies of equality of a and b. In each
case (2) gives the claimed d-row because its possible all-equal
contribution vanishes identically. This proves (7) without elimination.

Consequently adding J to (3) imposes every constraint of this specified
single-event conjugacy form. Its homogeneous row rank is exactly five.
For a lower bound, use rows \((d_1,d_2,d_3,d_4,J)\) and columns
\[
\begin{split}
&(0,0,1,0,1,2,0),\quad(0,0,1,0,1,2,2),\\
&(0,1,0,0,2,1,0),\quad(0,1,0,2,2,1,0),\\
&(0,1,2,3,0,4,5).
\end{split}
\]
Their minor is
\[
\begin{pmatrix}
0&0&1&1&0\\
0&0&0&-1&0\\
1&1&0&0&0\\
0&-1&0&0&0\\
0&0&0&0&1
\end{pmatrix},\qquad \det=1.
\tag{8}
\]
The upper-left four-by-four determinant is one, as follows by its
single nonzero Leibniz term, and expansion down the last column gives
the displayed determinant. Normalization raises the rank to six,
because all five homogeneous rows vanish on the all-equal type while
the normalization row is one there.

The last column is the earlier stationary-but-impossible singleton.
It has J=1 and is now excluded. This rank statement is only about the
explicit single-event constraints above; it makes no completeness claim
for joint events or for all necessary linear identities.

## 3. A further obstruction on the same window

The singleton distribution on
\[
\widehat\pi=(0,1,2,0,3,4,1)
\tag{9}
\]
satisfies (3) and J=0, hence all the single-event conjugacy constraints.
Indeed all three triple restrictions are 012, and neither ab nor ba
fixes the root. Its prescriptions are injective. An explicit completion
on five points, in image-list notation, is
\[
A=(1,0,4,2,3),\qquad B=(2,3,1,0,4).
\tag{10}
\]
At root zero the images are \((0,1,2,0,3,4,1)\), exactly (9).

Nevertheless (9) cannot hold at every root of a finite model: its
equality \(a=bb\) would give \(A=B^2\) everywhere, implying
\(BA=AB\), whereas its distinct ab and ba classes assert
noncommutation everywhere. The next lemma makes this obstruction
quantitative and rules out limits as well.

**Boundary lemma.** For permutations A,B of a nonempty finite set V,
let
\[
E=\{v:A(v)=B^2(v)\},\qquad
F=\{v:B(A(v))\ne A(B(v))\}.
\]
Then
\[
|E\cap F|\leq |E^c\cap F|.
\tag{11}
\]
Both sides can be positive and equal. In particular
\[
d_H(BA,AB)\leq2d_H(A,B^2),
\tag{12}
\]
and the constant two is optimal.
Here \(d_H(P,Q)=|\{v:P(v)\ne Q(v)\}|/|V|\).

**Proof.** For v in E one has
\(B(A(v))=B^3(v)\). Thus v is in F exactly when
\(A(B(v))\ne B^2(B(v))\), or equivalently B(v) is outside E.
Consequently
\[
E\cap F=E\cap B^{-1}(E^c).
\]
If v is outside E and B(v) is in E, then
\(A(B(v))=B^3(v)\), while
\(B(A(v))\ne B^3(v)\), since B is injective and
\(A(v)\ne B^2(v)\). Therefore
\[
E^c\cap B^{-1}(E)\subseteq E^c\cap F.
\]
Since B is a bijection, the number of points exiting E equals the
number entering it:
\[
|E\cap B^{-1}(E^c)|
=|E|-|E\cap B^{-1}(E)|
=|E^c\cap B^{-1}(E)|.
\]
The last three statements prove (11). Summing the two portions of F
then gives
\(|F|\leq2|E^c\cap F|\leq2|E^c|\), which is (12).

For sharpness take
\[
A=(0,3,2,1),\qquad B=(1,2,3,0)
\tag{13}
\]
on four points. Then \(E=\{1,3\}\), and F consists of all four
points. Thus both sides of (11) equal two, while the two distances in
(12) are one and one-half. Any smaller coefficient on the right of
(11), or any smaller constant in (12), fails for this model. ∎

This proof uses only preservation of uniform measure and the indicated
injectivity. Replacing normalized cardinality by probability gives the
same conclusion for invertible measure-preserving maps. Interchanging
A and B gives the corresponding inequality for \(B=A^2\).

To express (11) in the collision table, define
\[
K(\pi)=\bigl(2I_{16}(\pi)-1\bigr)
                    \bigl(1-I_{45}(\pi)\bigr).
\tag{14}
\]
Every finite-model frequency vector, and every limit of such vectors,
satisfies
\[
\boxed{\quad \sum_{\pi\in\mathcal T}x_\pi K(\pi)\leq0.\quad}
\tag{15}
\]
This is linear in x, even though its column value uses a joint event.
For (9) its left side is one, whereas all the equations in Section 2
hold. Thus (15) strictly strengthens the relaxation after adding every
single-event conjugacy constraint. Since K takes values in
\(\{-1,0,1\}\) and \(K(\widehat\pi)=1\), (15) also gives
\[
x_{\widehat\pi}\leq\tfrac12.
\tag{16}
\]
Indeed the remaining mass contributes at least
\(-(1-x_{\widehat\pi})\). In particular every actual frequency
vector has total variation distance at least one-half from the
singleton in (9). No assertion is made that (16) is the optimal bound
for this particular type.

There is an independent derivation of (12). Normalized Hamming
distance on permutations is bi-invariant and satisfies the triangle
inequality. Insert \(B^3\) between BA and AB:
\[
d_H(BA,AB)\leq d_H(BA,B^3)+d_H(B^3,AB)
             =2d_H(A,B^2).
\]
This rederives the numerical constant, while the boundary proof supplies
the stronger joint-event inequality (11).

## 4. Entropy does not already exclude the new singleton

For (9), write the five independent fair class bits as R,U,V,S,T.
The three outputs are
\[
(RUV,RUS,UVT).
\]
Conditioning on U produces the following nonzero counts for
\((R,N)\), out of 32 assignments:
\[
\begin{array}{c|rrrrrrr}
N&000&001&010&100&101&110&111\\\hline
R=0&14&2&0&0&0&0&0\\
R=1&10&0&2&1&1&1&1
\end{array}
\tag{17}
\]
To check the table, U=0 contributes eight assignments to each root
value at name 000. For U=1 and R=0, the first two outputs vanish,
and VT is zero for six choices of V,S,T and one for two choices.
For U=1 and R=1, V=0 gives names 000 and 010 twice each, while
V=1 gives each of 100,101,110,111 once. The counts sum to 32.

The output E has one-probability 1/8. Using (17) and its marginal
counts \((24,2,2,1,1,1,1)\) gives
\[
C_{\widehat\pi}
=\tfrac92\log2+\tfrac34\log3-\tfrac5{16}\log5
                         -\tfrac{21}{16}\log7
=0.8861651107500812\ldots>\log2.
\tag{18}
\]
For an exact sign check, multiply the difference from log 2 by sixteen
and exponentiate: the required integer comparison is
\(2^{56}3^{12}>5^5 7^{21}\). Thus the singleton satisfies the
fair-AND information lower bound. The new compatibility inequality
excludes something that this entropy inequality does not exclude.

The fair-AND extrema remain log 2 and \((3/2)\log2\) after both
refinements. The lower bound (5) still applies; the upper bound follows
from
\[
H(E)+H(R\mid N)\leq H(E)+H(R\mid E)
                 =H(R)+H(E\mid R)\leq\tfrac32\log2.
\]
Here E is a component of N, E=0 when R=0, and on R=1 its entropy
is at most log 2. The one-point model attains the lower bound, while
the two-point model with A=B the transposition attains the upper
bound. Actual finite models satisfy all the new constraints, so these
attainments remain feasible. Likewise the two- and three-point
attainments of the earlier cap
\(h(p)+p\max\{h(p),h(p^2)\}\) survive for every p.

## 5. Finite checks and limits

`compatibility_audit.py` reconstructs the 103 types, recomputes the
previous exact entropy certificate, lists all 21 pair events and their
ten conjugacy classes, checks every row identity in (7), and certifies
the determinant in (8). It verifies the five-point completion (10),
the exact cost (18), the sharp four-point model (13), and the new
inequality for all permutation pairs on one through five points.
The model and root counts are independently
\[
\sum_{n=1}^5(n!)^2=15017,\qquad
\sum_{n=1}^5 n(n!)^2=74421.
\]
These checks supplement the boundary proof, which covers every finite
size. They are not an asymptotic approximation argument.

The refinement supplies necessary compatibility constraints on rooted
frequencies, but no sufficient realization theorem. No genuine
positive-gap group/code is constructed, and no conclusion for
arbitrary-group RBS follows. Priority of these elementary finite-table
refinements has not been determined. The local conditional-entropy
approach is prior work; see Lewis Bowen and Michael Chapman,
*Surjunctivity does not characterize cosoficity of invariant random
subgroups*, [arXiv:2511.06586](https://arxiv.org/abs/2511.06586).
For RBS and its conditional universal theorem see Brandon Seward,
*Krieger's finite generator theorem for actions of countable groups II*,
[arXiv:1501.03367v4](https://arxiv.org/abs/1501.03367v4).
