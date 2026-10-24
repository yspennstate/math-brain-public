# Pairwise log-odds allocation and a Cauchy family in every dimension

Date: 2026-09-15. Root creative extension of C013's pairwise Fisher allocation. This is not an agent execution. The full Lyons conjecture remains open and worldwide novelty is not established.

## 1. A general pairwise-log theorem

Let 0<K<I on n sites, and suppose its frozen atom weight has no interactions above degree two:

\[
-\log p_S=\text{constant}+\sum_{i\in S}a_i+
\sum_{\{i,j\}\subset S}c_{ij},\qquad c_{ij}\ge0.
\tag{1}
\]

For the marginal law on pair ij write its four probabilities as x,y,z,w (in order 00,10,01,11), and define

\[
T_{ij}={y+z\over2\sqrt{xw}}\ge1,\qquad
m=\min_{i<j}c_{ij},\qquad
F=\sum_{i<j}{c_{ij}-m\over2(1+T_{ij})}.
\]

Let v=Var_K |X|=tr(K-K^2). Then

\[
\boxed{F+mv\le1\ \Longrightarrow\
D^2H(K)[A,A]\le-(1-F-mv)\mathcal I_K(A)-m\|A\|_F^2}
\tag{2}
\]

for every Hermitian direction A. If m>0, this proves negative definiteness of the full Hessian. The theorem is pointwise and does not require that a perturbed kernel continue to satisfy (1).

**Proof.** At the base, the exact entropy Hessian and the DPP inclusion identities give

\[
H''=-I+2\sum_{i<j}c_{ij}\det A_{ij},\qquad I=\mathcal I_K(A).
\tag{3}
\]

Write I_ij for the marginal pair Fisher information. The exact two-site square identity in C013, Section 4, gives

\[
I_{ij}\ge4(1+T_{ij})\det A_{ij}.
\tag{4}
\]

For completeness, set P=adj(K_ij)/sqrt(w), Q=adj(I-K_ij)/sqrt(x), W=P+Q, and V=W^(1/2)A_ij W^(1/2). Then det P=det Q=1 and det W=2+2T_ij. The two extreme atom scores contribute alpha^2+beta^2 with alpha=tr(PA_ij), beta=tr(QA_ij). Subtracting 2 det W det A_ij leaves

\[
{(\alpha-\beta)^2\over2}
{(V_{11}-V_{22})^2+4|V_{12}|^2\over2},
\]

plus the two nonnegative mixed-atom Fisher terms, proving (4) for every Hermitian A_ij, including indefinite ones. Here x,w>0, W>0, and the square root is well-defined.

The full score's conditional expectation is the marginal score, so I-I_ij>=0. Also, for s=tr A, score projection on the particle count gives I-s^2/v>=0. Define f_ij=(c_ij-m)/[2(1+T_ij)]. Since 2 sum_{i<j} det A_ij=s^2-||A||_F^2 in every dimension, there is the exact identity

\[
\begin{aligned}
-H''={}&(1-F-mv)I+mv(I-s^2/v)+m\|A\|_F^2\\
&+\sum_{i<j} f_{ij}\left[(I-I_{ij})+
\{I_{ij}-4(1+T_{ij})\det A_{ij}\}\right].
\end{aligned}
\tag{5}
\]

All bracketed terms are nonnegative. This proves (2).

Since T_ij>=1 and v<=n/4, a simpler sufficient condition, requiring no marginal probabilities, is

\[
F+mv\le {1\over4}\left[
\sum_{i<j}c_{ij}-{n(n-3)\over2}m\right]\le1.
\tag{6}
\]

For n>=3 it is enough that sum c_ij<=4. A strict margin in (6) is a quantitative Fisher surplus. This condition is sufficient, not necessary.

## 2. Cauchy odds realize pairwise log interactions exactly

Take distinct positive numbers x_1,...,x_n and arbitrary positive external scales ell_1,...,ell_n. Set

\[
L_{ij}=\sqrt{\ell_i\ell_j}\,{2\sqrt{x_ix_j}\over x_i+x_j},
\qquad K=L(I+L)^{-1}.
\tag{7}
\]

The matrix (1/(x_i+x_j)) is the Gram matrix of the linearly independent functions exp(-x_i t) in L^2(0,infinity); hence L>0 and K is a strict contraction. The Cauchy determinant identity gives, for every subset S,

\[
\det L_S=\prod_{i\in S}\ell_i
\prod_{\{i,j\}\subset S}\left({x_i-x_j\over x_i+x_j}\right)^2.
\tag{8}
\]

This elementary identity follows by putting the determinant of (1/(u_i+v_j)) over its common denominator: its numerator is alternating separately in the u's and v's, hence has their Vandermonde factors; degree comparison and the one-variable leading coefficient determine the remaining constant. Specializing u=v=x and multiplying the row and column factors in (7) yields (8).

Therefore (1) holds exactly, with

\[
c_{ij}=2\log{x_i+x_j\over|x_i-x_j|}>0.
\tag{9}
\]

The external scales affect only the modular coefficients. Condition (6), and all the conclusions inferred from it, therefore hold for **every positive external scaling**, without a density, conditioning, or spectral-separation restriction.

## 3. An explicit family valid for every n

For n>=3 choose R>=n+1 and x_i=R^i, i=0,...,n-1. Then c_ij depends only on d=|i-j|:

\[
c_d=2\log{R^d+1\over R^d-1}<{4\over R^d-1}.
\]

Using R^d-1>=R^(d-1)(R-1),

\[
\begin{aligned}
\sum_{i<j}c_{ij}
&< {4\over R-1}\sum_{d=1}^{n-1}(n-d)R^{1-d}\\
&< {4(n-1)R\over(R-1)^2}
\le4\left(1-{1\over n^2}\right).
\end{aligned}
\tag{10}
\]

The last inequality follows because R/(R-1)^2 decreases for R>1, and at R=n+1 the expression is (n^2-1)/n^2. Combining (2), (6), and (10) proves the explicit all-dimensional theorem

\[
\boxed{D^2H(K)[A,A]
\le-{1\over n^2}\mathcal I_K(A)-m\|A\|_F^2,
\qquad
m=2\log{R^{n-1}+1\over R^{n-1}-1}>0.}
\tag{11}
\]

This holds for arbitrary ell_i>0 and every Hermitian A. In particular the full Hessian is strictly negative, even for external scales approaching zero or infinity (the assertion is at each finite positive scale; no boundary Hessian is asserted).

For n=2, take R>=3. There is one coefficient m=2log((R+1)/(R-1))<=2log2. Formula (6) gives budget m/2<=log2<1, so the same construction has a strictly negative Hessian by (2), with Fisher surplus at least 1-log2. The singleton case is ordinary Bernoulli entropy.

## Scope and future step

The matrix family is constrained, but its external fields are completely arbitrary and the conclusion controls the entire ambient Hermitian Hessian. Continuity gives open neighborhoods around each such base; convexity of the whole parameterized family is not asserted. C013's sharper three-site excess-budget bound can cover additional n=3 Cauchy shapes beyond the deliberately simple spacing condition here.

The remaining questions include removing the spacing condition for general Cauchy shapes, sharpening the total-pair Fisher allocation in high dimension, and extending the method to nonzero higher log interactions. None is assumed in this proof.
