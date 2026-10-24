# A certified diamond controls a full two-dimensional active covariance

Root constructive proof, 2026-09-15, using the fair-middle entropy idea developed with C064. The proof below is self-contained once an unlabeled projection diamond exists. It extends the earlier fixed-support theorem to certified projection backgrounds and permits noncommuting active covariances. Historical priority is unverified; general Lyons concavity remains open.

## 1. Statement

Let W and V be orthogonal isometries with respectively r and two columns in C^n. Write Z for their orthogonal complement. Assume a nonnegative unlabeled diamond coupling exists for the projection flag W ⊂ W+V: its bottom S has law P_W, top T has law P_(W+V), S⊂T and |T\S|=2; the sum of the two middle marginal laws is the sum of the laws P_(W+v_1),P_(W+v_2). This aggregate is independent of the orthonormal basis v_1,v_2 of V.

Put k=min(r,n-r-2). If k≤4, then
\[
\boxed{M\longmapsto H(P_{P_W+VMV^*})\text{ is concave on }0\le M\le I_2.}\tag{1}
\]
For a strict M and a definite Hermitian direction A on the active plane,
\[
\boxed{H''[A,A]\le-C_k\det A,
\qquad C_k=8-2\log2-4\log(k+1)>0.}\tag{2}
\]
The active eigenvectors may change. The theorem is not limited to a commuting spectral square.

Prior rank-one-bottom covering, restated constructively in C033, provides the hypothesis for EVERY flag with k≤1. Hence (1) holds for an arbitrary rank-one projection background in every ambient dimension, and for its complemented cases. Other certified families from C035, C036, C038-C044 also give (1) when k≤4. The theorem does not assume a general six-site diamond, and it does not turn a certified low-rank flag into arbitrary full-rank-base concavity.

## 2. The fair-middle entropy identity

Orient the two elements of T\S fairly, independently conditional on S,T; call them i,j. Let U=S+i and U'=S+j. Both middle laws are
\[
m=\tfrac12(P_{W+v_1}+P_{W+v_2}).
\]
The pair U,U' determines S,T and its fair orientation, so H(U,U')=H(S,T)+log2. The ordinary conditional mutual-information identity gives exactly
\[
\boxed{\beta_*:=2H(m)-H(S)-H(T)
=\log2+H(S\mid T)-2H(S\mid U)+I(i;j\mid S).}\tag{3}
\]
For example, expand I(i;j|S) as H(S,i)+H(S,j)-H(S)-H(S,i,j), then substitute H(S,i)=H(U)+H(S|U) and H(S,i,j)=H(S,T)+log2. No individually prescribed middle labels are required.

Given U, the bottom S is obtained by deleting one of its r+1 elements, so H(S|U)≤log(r+1). Thus
\[
\beta_*\ge\log2-2\log(r+1).\tag{4}
\]
Complementing every set swaps bottom/top and leaves the middle entropy unchanged, giving the same bound with r replaced by n-r-2. Therefore use k in (4). Keeping the exact nonnegative terms in (3) can improve this bound for a particular coupling.

## 3. The exact three-cardinality occupation law

Choose a basis of W, and let a_S=|det W_S|² for |S|=r, b_T=|det[W,V]_T|² for |T|=r+2. These are probability laws. For |U|=r+1, define the two-component row
\[
e_U=(\det[W,v_1]_U,\det[W,v_2]_U).
\]
The exterior-power isometry gives sum_U e_U^*e_U=I_2; in particular m_U=||e_U||²/2 is the fair-middle law in (3).

Set d=det M, d0=det(I-M), and B=M-dI. At 0<M<I, B>0 and det B=dd0. The only possible atom cardinalities have probabilities
\[
p_S=d0\,a_S,\qquad p_U=e_U B e_U^*,\qquad p_T=d\,b_T.\tag{5}
\]
This follows by diagonalizing the active 2x2 covariance and using the fixed-rank projection mixture; the displayed formula is basis independent. Fixed zero atoms are omitted.

Let delta=det A and I=sum(p'_X)^2/p_X. Differentiating (5) along M+tA gives
\[
H''=-I+2\delta\Lambda,
\quad
\Lambda=\sum_U||e_U||²\log p_U-\log(dd0)+H(a)+H(b).
\tag{6}
\]
Let f1=tr B, nu_U=p_U/f1, and T0=f1/(2sqrt(dd0))≥1. Rewriting (6) gives the exact identity
\[
\Lambda=2\log(2T0)-\beta_*-2D(m\Vert\nu).
\tag{7}
\]
Thus, by (4),
\[
\Lambda\le 2\log T0+\log2+2\log(k+1).\tag{8}
\]

## 4. Indefinite directions and the role of the diamond

The frozen table f(X)=-log p_X is supermodular for a strict determinantal law, by the principal-minor inequality. For the present boundary kernel, first regularize the full kernel to (1-2epsilon)K+epsilon I. Apply the diamond inequality to its finite supermodular log table and take epsilon to zero. Every atom receiving positive bottom, top, or middle weight in (5) has a positive probability at strict M, so all terms of this finite expectation have finite limits.

Consequently
\[
E f(S)+E f(T)-E f(U)-E f(U')=\Lambda\ge0.\tag{9}
\]
When delta≤0, equations (6) and (9) give H''≤0. This includes all indefinite and rank-one active directions. An arbitrary choice of middle labels is unnecessary.

## 5. Definite directions need Fisher compensation

When delta>0, reverse A if needed so A>0. The bottom and top cardinalities alone give
\[
I\ge\frac{[\operatorname{tr}(\operatorname{adj}M)A]^2}{d}
+\frac{[\operatorname{tr}(\operatorname{adj}(I-M))A]^2}{d0}
\ge4(1+T0)\delta.\tag{10}
\]
For completeness, put P=adj(M)/sqrt(d), Q=adj(I-M)/sqrt(d0). Both have determinant one. Cauchy-Schwarz followed by (tr CA)^2≥4det(C)det(A) gives
(tr PA)^2+(tr QA)^2≥2det(P+Q)det A; direct 2x2 algebra gives det(P+Q)=2+2T0. This proves (10) independently of the embedding and projection background.

Using (8),
\[
H''\le-4\delta[1+T0-\log T0-\tfrac12\log2-\log(k+1)]
\le-[8-2\log2-4\log(k+1)]\delta,
\]
since 1+T0-log T0≥2. The last constant is positive through k=4 (its smallest such value is 8-2log2-4log5>0). This proves (2) and, together with (9), nonpositivity in every active Hermitian direction. Integration proves (1) for strict active endpoints; regularizing M within its two-dimensional domain and using finite-law entropy continuity proves the full closed domain.

## 6. Strict active gap and scope

If Lambda>0, the count statistic has variance at most 1/2, so I≥2(tr A)^2. Combining this with 2det A=(tr A)^2-||A||F² and (2) yields the same explicit four-dimensional gap argument as ROOT_RANK_TWO_SUPPORT:
\[
-H''\ge\min\left(\Lambda,\frac{2C_k}{C_k+2\Lambda}\right)\|A\|_F^2.
\]
No strictness is asserted when Lambda=0. C040's projection-block substitution preserves the entire Hessian and hence lifts (1) exactly to its encoded families.

This proof does not require projection-entropy submodularity beta=H(P_W+v1)+H(P_W+v2)-H(P_W)-H(P_W+V)≥0. The weaker fair-middle bound (4), together with the extreme Fisher terms, suffices. It also does not assume entropy concavity survives an arbitrary unobserved mixture of projection backgrounds; that remains an additional obligation for general kernels.
