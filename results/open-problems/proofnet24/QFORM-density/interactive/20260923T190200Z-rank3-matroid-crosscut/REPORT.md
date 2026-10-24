# Exact rank-three no-pivot matrices with no rank-three physical cross cut

Status: PROVED STRUCTURAL CLASSIFICATION; FULL QFORM-DENSITY OPEN. All cuts, rows, and hubs below refer to original physical coordinates. The result is exact rank three; it does not classify an arbitrary-spectrum matrix with only \(s_3(A)\ge1\).

## The theorem

Set \(c=1/64\). Let \(A\) be a real symmetric matrix of exact rank three with \(s_3(A)\ge1\). Assume that for every original coordinate \(i\) and distinct \(i,j\),
\[
 |a_{ii}|<c,\qquad
 |a_{ii}a_{jj}-a_{ij}^2|<c.                              \tag{1}
\]
Thus \(A\) has no physical \(c\)-pivot in the manuscript's sense. Exactly one of the following occurs:

1. There is an original-coordinate partition \([n]=I\sqcup J\) with \(\operatorname{rank} A[I,J]=3\).
2. There is a unique original coordinate \(h\) such that \(\operatorname{rank} A[[n]\setminus\{h\},[n]\setminus\{h\}]\le2\). Writing
   \[
   A=\begin{pmatrix}a&w^{\mathsf T}\\w&B\end{pmatrix}
   \]
   with \(h\) first, let \(t=\|w\|_2\). Then
   \[
   |a|<c,\qquad t\ge\sqrt{1-c^2}>0.9998779.             \tag{2}
   \]
   There are orthonormal vectors \(e,v\) on the light coordinates, \(\lambda\in\mathbb R\) with \(|\lambda|\ge1\), and real \(\beta,u_v\), such that \(w=te\) and
   \[
   B=\beta ee^{\mathsf T}
       +u_v(ev^{\mathsf T}+ve^{\mathsf T})
       +\lambda vv^{\mathsf T}.                          \tag{3}
   \]
   In particular the exact quadratic form has the physical-product-provenance normal form
   \[
   Q=aX_h^2+2tX_hL+
       \lambda(V+(u_v/\lambda)L)^2+
       (\beta-u_v^2/\lambda)L^2,
   \quad L=e^{\mathsf T}X',\quad V=v^{\mathsf T}X'.       \tag{4}
   \]
   The physical hub \(X_h\) is independent of the original-coordinate product light vector \(X'\). No independence of \(L,V\) is asserted.

If \(a=0\), the manuscript's independent-hub transverse-square theorem gives
\[
 \|p_Q\|_\infty
 \le 2\sqrt2+\sqrt2\log(1/3+4\sqrt2)<5.361.            \tag{5}
\]
For \(a\ne0\), (4) reduces the rank-three/no-cross-three survivor to a small physical hub diagonal with two light projections; a uniform density theorem for this precise family has not been proved here.

## Proof: two disjoint row bases

Write \(A=U\Lambda U^{\mathsf T}\) with \(U\) having three orthonormal columns and \(\Lambda\) invertible symmetric \(3\times3\). Give the row indices the rank-three real-representable matroid \(r(F)=\operatorname{rank}U_F\). For disjoint physical sets \(I,J\),
\[
 \operatorname{rank}A[I,J]=3
 \quad\Longleftrightarrow\quad r(I)=r(J)=3,             \tag{6}
\]
because a full-column-rank \(U_I\) followed by invertible \(\Lambda\) and a full-row-rank \(U_J^{\mathsf T}\) has rank three. Consequently a rank-three physical cut exists if and only if the row matroid has two disjoint bases.

We use Edmonds' matroid partition theorem, applied to the dual matroid: two disjoint bases exist if and only if
\[
 |E\setminus F|\ge2(3-r(F))\quad\hbox{for every }F\subset E,
 \qquad E=[n].                                          \tag{7}
\]
For completeness, dual rank is \(r^*(S)=|S|-3+r(E\setminus S)\). Edmonds' theorem says that \(E\) can be partitioned into two dual-independent sets exactly when \(|S|\le2r^*(S)\) for every \(S\subset E\); writing \(F=E\setminus S\) gives (7). Such a dual partition is equivalent to two disjoint primal bases: extend each dual-independent set to a dual base, then complement the two dual bases. This invokes the standard theorem in Jack Edmonds, "Minimum Partition of a Matroid Into Independent Subsets," Journal of Research of the National Bureau of Standards B 69B (1965), 67–72, https://nvlpubs.nist.gov/nistpubs/jres/69B/jresv69Bn1-2p67_A1b.pdf .

Suppose there is no rank-three physical cut. Some \(F\) violates (7). Its rank \(r(F)\le2\), and the integer cardinality bound gives:
\[
\begin{array}{c|c}
 r(F)& |E\setminus F|\\\hline
 0&\le5\\
 1&\le3\\
 2&\le1.
\end{array}                                             \tag{8}
\]
We eliminate the first two possibilities using the exact no-pivot hypothesis. From (1),
\[
 |a_{ij}|<d:=\sqrt{c+c^2}\quad(i\ne j).                \tag{9}
\]
If \(r(F)=0\), every row of \(U_F\) is zero, so \(A\) is supported on at most five active physical coordinates. Gershgorin or the maximum row-sum bound gives
\[
 \|A\|_{\rm op}<c+4d
 =0.5195161092\ldots<1,                               \tag{10}
\]
contrary to \(s_3(A)\ge1\).

If \(r(F)=1\), set \(H=E\setminus F\), so \(|H|\le3\). All light frame rows lie in one line, and therefore \(A[F,F]\) has rank at most one while \(A[H,F]\) has rank at most one and shares the same light row direction. Hence
\[
 A-\operatorname{diag}(A[H,H],0_F)
\]
has rank at most two: its image lies in the span of one vector supported on \(H\) and one supported on \(F\). The physical hub block obeys
\[
 \|A[H,H]\|_{\rm op}<c+2d
 =0.2675705546\ldots<1.                               \tag{11}
\]
The rank-two approximation inequality gives \(s_3(A)<1\), a contradiction.

Thus \(r(F)=2\) and \(|E\setminus F|\le1\). The complement cannot be empty because \(r(E)=3\), so \(E\setminus F=\{h\}\). The light row span is two-dimensional, and hence \(\operatorname{rank} B\le2\). If two different coordinates both had rank-two-complement row spans, deleting both would leave rank at most one; all but at most two rows would then lie in a rank-one flat, which was just excluded. Thus \(h\) is unique.

## Proof: exact light form and parameter floors

Since \(U_F\) has rank two and \(U_E\) rank three, a vector in the nullspace of \(U_F\) has nonzero \(U_h\)-evaluation. Therefore the physical coordinate vector \(e_h\) belongs to \(\operatorname{range}U=\operatorname{range}A\). On this range all three singular values of \(A\) are at least one, so
\[
 1\le\|Ae_h\|_2^2=a^2+\|w\|_2^2.
\]
This proves (2), and in particular \(w\ne0\).

Let \(A_0=A-ae_he_h^{\mathsf T}\). Because \(e_h\in\operatorname{range}U\), the range of \(A_0\) remains inside \(\operatorname{range}U\), so \(\operatorname{rank}A_0\le3\). Singular-value perturbation gives
\(s_3(A_0)\ge s_3(A)-|a|>1-c>0\); hence \(\operatorname{rank}A_0=3\).

Set \(e=w/t\), \(P=I-ee^{\mathsf T}\) on the light coordinates, \(\beta=e^{\mathsf T}Be\), and \(u=PBe\). The exact zero-hub Schur identity from the companion one-hub compression report gives
\[
 \operatorname{rank}A_0=2+\operatorname{rank}(PBP|_{e^\perp}).
\]
Thus \(C=PBP|_{e^\perp}\) has rank one: \(C=\lambda vv^{\mathsf T}\), with \(v\perp e\), \(|v|=1\). The same companion rank-two approximation gives
\[
 s_3(A)\le\max\{|a|,\|C\|_{\rm op}\}.
\]
Since \(s_3(A)\ge1>|a|\), this yields \(|\lambda|\ge1\).

Decompose \(u=u_vv+u_\perp\), with \(u_\perp\perp e,v\). If \(u_\perp\ne0\), the compression of \(B\) to the orthonormal frame \(e,v,u_\perp/\|u_\perp\|\) is
\[
 \begin{pmatrix}
 \beta&u_v&\|u_\perp\|\\
 u_v&\lambda&0\\
 \|u_\perp\|&0&0
 \end{pmatrix},
\]
whose determinant is \(-\lambda\|u_\perp\|^2\ne0\). This contradicts \(\operatorname{rank}B\le2\). Therefore \(u_\perp=0\), and expanding \(B\) in the orthonormal frame \(e,v\) proves (3)-(4).

When \(a=0\), (2) gives \(t\ge1\). Thus \(tX_h\) is an independent cap-one hub and the manuscript's "A transverse square with an independent hub" theorem applies to (4), proving (5).

## A quantitative spectral gap in the remaining hub-square endpoint

In the surviving normal form (3)-(4), set \(\beta'=\beta-u_v^2/\lambda\). On the orthonormal three-dimensional span of \(e_h,e,v\), the exact nonzero part of \(A\) is
\[
 M=\begin{pmatrix}a&t&0\\t&\beta&u_v\\0&u_v&\lambda\end{pmatrix}.
\]
Every singular value of \(M\) is at least one. Taking the Schur complement of the \(\lambda\)-entry gives
\[
 H=\begin{pmatrix}a&t\\t&\beta'\end{pmatrix}.
\]
The upper-left principal \(2\times2\) block of \(M^{-1}\) equals \(H^{-1}\). Since \(\|M^{-1}\|_{\mathrm{op}}\le1\), one has \(\|H^{-1}\|_{\mathrm{op}}\le1\). Thus the two eigenvalues of \(H\) both have modulus at least one. As \(|a|<1\), they cannot have the same sign; their positive and negative eigenvalues lie in \([1,\infty)\) and \((-\infty,-1]\), respectively. The inequalities
\(\det(H-I)\le0\) and \(\det(H+I)\le0\) yield
\[
 \boxed{\ t^2\ge
   \max\{(a-1)(\beta'-1),(a+1)(\beta'+1)\}
   =1+a\beta'+|\beta'+a|.\ }                            \tag{12}
\]
This refines \(t^2\ge1-a^2\) and may be useful for a receiver that controls the small hub-square term. It does not itself bound the output density.

## Scope and next receiver

This is an exhaustive exact-rank-three classification only for the branch in which every original-coordinate cross cut has rank at most two. It does not give a quantitative lower bound on the third crossing singular value in the complementary branch. It does not handle arbitrary additional spectrum. Even in the classified branch, the nonzero hub-square term \(aX_h^2\), with \(|a|<1/64\), remains to be handled uniformly for rough independent coordinates with unbounded fragmented supports; simply deleting that small coefficient is invalid.

The companion proof is https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T185357Z-one-hub-transverse-compression/REPORT.md . The current manuscript and latest B13/B18/B20 fleet reports checked did not explicitly state this matroid classification.