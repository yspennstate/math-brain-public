# One-hub transverse compression: exact rank and inertia

Status: PROVED STRUCTURAL LEMMA; FULL QFORM-DENSITY OPEN. This note supplies an algebraic reduction only. It does not claim a product-law density bound for an arbitrary transverse leakage term.

## Setup

Let \(A\) be any real symmetric \(n\times n\) matrix. Select an original physical coordinate \(h\), write
\[
 A=\begin{pmatrix}a&w^{\mathsf T}\\w&B\end{pmatrix},
\]
and assume \(w\ne0\). On the remaining original-coordinate space let \(e=w/\|w\|_2\), \(P=I-ee^{\mathsf T}\), \(C=PBP|_{e^\perp}\), \(t=\|w\|_2\), \(\beta=e^{\mathsf T}Be\), and \(u=PBe\). The projection is used only in matrix algebra; no probabilistic independence is asserted after rotation.

## Theorem 1: sharp rank-two approximation

The matrix
\[
 R=A-\operatorname{diag}(a,PBP)
   =\begin{pmatrix}0&w^{\mathsf T}\\
                    w&B-PBP\end{pmatrix}
\]
has rank at most two. Consequently
\[
 s_3(A)\le \max\{|a|,\|C\|_{\mathrm{op}}\}.                 \tag{1}
\]
In particular, if \(s_3(A)\ge1\) and \(|a|<1\), then
\[
 \boxed{\ \|C\|_{\mathrm{op}}\ge1.\ }                       \tag{2}
\]
The threshold in (2) is exactly one; no loss of \(|a|\) is necessary.

Proof. Put \(e_0=(1,0)\) and \(e_1=(0,e)\) in the full ambient space. Since
\[
 B-PBP=\beta ee^{\mathsf T}+eu^{\mathsf T}+ue^{\mathsf T},
\]
the vector \(z=t e_0+\frac{\beta}{2}e_1+(0,u)\) satisfies
\(R=e_1z^{\mathsf T}+ze_1^{\mathsf T}\). Hence \(\operatorname{rank}R\le2\). The error \(A-R=\operatorname{diag}(a,PBP)\) is block diagonal and has operator norm \(\max\{|a|,\|C\|_{\mathrm{op}}\}\). The Eckart--Young singular-value inequality gives (1), and (2) follows. If \(w=0\), the analogous elementary conclusion follows directly from the block diagonal matrix \(\operatorname{diag}(a,B)\).

No bound on \(\|B\|\), \(\|w\|\), other eigenvalues, dimension, or original-coordinate laws enters this proof.

## Theorem 2: exact null-hub rank and inertia

If \(a=0\), then
\[
 \operatorname{rank}A=2+\operatorname{rank}C,\qquad
 n_+(A)=1+n_+(C),\qquad n_-(A)=1+n_-(C),             \tag{3}
\]
and \(n_0(A)=n_0(C)\).

Proof. In the orthogonal coordinate decomposition \(e_0\oplus e\oplus e^\perp\),
\[
 A=\begin{pmatrix}
 0&t&0\\
 t&\beta&u^{\mathsf T}\\
 0&u&C
 \end{pmatrix}.                                             \tag{4}
\]
The leading \(2\times2\) block \(H=\left(\begin{smallmatrix}0&t\\t&\beta\end{smallmatrix}\right)\) is nonsingular with determinant \(-t^2\), hence inertia \((1,1,0)\). The bottom-right entry of \(H^{-1}\) is zero. The Schur complement of \(H\) in (4) is therefore exactly \(C\), regardless of the size and direction of \(u\). Sylvester's law of inertia proves (3).

## Exact-rank-three normal form and the unpaid analytic edge

If \(a=0\), \(\operatorname{rank}A=3\), and \(s_3(A)\ge1\), equation (3) forces \(C=\lambda vv^{\mathsf T}\) on \(e^\perp\) for a unit vector \(v\) and \(|\lambda|\ge1\) by (1). With \(L=e^{\mathsf T}X'\), \(V=v^{\mathsf T}X'\), the exact form is
\[
 X^{\mathsf T}AX
 =2tX_hL+\beta L^2+2L\langle u,X'\rangle+\lambda V^2.   \tag{5}
\]
Split \(u=u_vv+u_\perp\), \(u_\perp\perp e,v\). Completing the square gives
\[
 X^{\mathsf T}AX
 =2tX_hL+\lambda(V+(u_v/\lambda)L)^2
  +(\beta-u_v^2/\lambda)L^2+2L\langle u_\perp,X'\rangle.  \tag{6}
\]
## Corollary: the leakage-free exact-rank-three branch is paid

In the exact-rank-three setting above, assume \(u_\perp=0\). Then \(e_h\) is perpendicular to \(\ker A\): the invertible three-dimensional block on \(\operatorname{span}(e_h,e,v)\) contains the whole range, and the kernel lies in its orthogonal complement. Consequently \(e_h\in\operatorname{range}A\), and
\[
 t=\|Ae_h\|_2\ge s_3(A)\|e_h\|_2\ge1.                     \tag{7}
\]
The coordinate \(Y=tX_h\) is independent of the light product vector and has density at most \(1/t\le1\). Equation (6) now reads
\[
 Q=2Y L+\lambda(V-v_c(L))^2+F_c(L),\qquad
 v_c(\ell)=-u_v\ell/\lambda,\quad
 F_c(\ell)=(\beta-u_v^2/\lambda)\ell^2.                  \tag{8}
\]
The manuscript's theorem "A transverse square with an independent hub" (manuscript/hubs.tex, Theorem hub-pure) applies with the orthonormal light directions \(e,v\), independent physical hub \(Y\), and \(\mu=|\lambda|\ge1\). Its two displayed branches are decreasing for \(\mu\ge1\), and their maximum is attained at \(\mu=1\). Thus
\[
 \boxed{\ \|p_Q\|_\infty
 \le 2\sqrt2+\sqrt2\log(1/3+4\sqrt2)
 =5.360042964\ldots<5.361.\ }                             \tag{9}
\]
This is a complete density payment for the stated exact-rank-three, zero-hub-diagonal, zero-transverse-leakage branch, with no spread, moment, or support condition. The step uses the original independent hub and the two-dimensional projection of the original light product vector; \(L,V\) themselves are not asserted independent.

## Theorem 3: exact-rank-three shear reserve

In the exact-rank-three null-hub setting of (5)-(6), put
\(\beta'=\beta-u_v^2/\lambda\) and
\(m^2=t^2+\|u_\perp\|_2^2\). Then
\[
 s_3(A)\le
 \frac{\sqrt{(\beta')^2+4m^2}-|\beta'|}{2}.             \tag{10}
\]
Consequently \(s_3(A)\ge1\) forces
\[
 \boxed{\ t^2+\|u_\perp\|_2^2\ge1+|\beta'|.\ }           \tag{11}
\]

Proof. Regard \(e,v,u_\perp\) as vectors in the full space, supported only on the light coordinates. Completing a rank-one square at the matrix level gives
\[
 A=\lambda\bigl(v+(u_v/\lambda)e\bigr)
            \bigl(v+(u_v/\lambda)e\bigr)^{\mathsf T}
       +R',
\]
where
\[
 R'=e z'^{\mathsf T}+z'e^{\mathsf T},
 \qquad
 z'=t e_h+(\beta'/2)e+u_\perp.
\]
The first summand has rank one. On the two-dimensional span of \(e\) and \(t e_h+u_\perp\), the nonzero block of \(R'\) is
\(\left(\begin{smallmatrix}\beta'&m\\m&0\end{smallmatrix}\right)\).
Its smaller singular value is the right side of (10). The rank-one singular-value interlacing inequality \(s_3(R'+T)\le s_2(R')\) proves (10). Solving the inequality \(s_2(R')\ge1\) yields (11).

The bound is a necessary spectral reserve, not a probability estimate. In particular, \(t\) may be arbitrarily small if the dependent light-coordinate shear \(u_\perp\) has norm near one or larger.

## Corollary: disjoint physical banks pay nonzero leakage uniformly

Retain the exact-rank-three null-hub hypotheses and let \(u_\perp\) be supported on a set \(T\) of original light coordinates disjoint from the supports of \(e\) and \(v\). Then \(P_0=\langle u_\perp,X'\rangle\) is independent of the pair \((L,V)\). Set \(Y=tX_h+P_0\), also independent of \((L,V)\). The cap-one physical hub gives \(\|p_{tX_h}\|_\infty\le1/t\). When \(u_\perp\ne0\), the one-dimensional product-projection theorem gives \(\|p_{P_0}\|_\infty\le\sqrt2/\|u_\perp\|_2\). Convolution does not increase a density supremum, so
\[
 \|p_Y\|_\infty
 \le\min\{1/t,\sqrt2/\|u_\perp\|_2\}\le2,               \tag{12}
\]
where the last inequality follows from \(t^2+\|u_\perp\|^2\ge1\), proved in (11). For \(u_\perp=0\), the earlier sharper leakage-free corollary applies.

Let \(S\) contain the original-coordinate supports of \(e,v\). View \(X_S\) alone as the light product vector: \(L,V\) depend only on \(X_S\), while \(Z=2Y\) depends only on the independent coordinates \(X_h,X_T\). Hence \(Z\) is independent of the entire light vector \(X_S\), has density at most one, and
\[
 2Q=2ZL+2\lambda(V+(u_v/\lambda)L)^2+2\beta'L^2.
\]
The existing independent-hub transverse-square theorem applies at coefficient \(\mu=2|\lambda|\ge2\). Since its bound is decreasing for \(\mu\ge2\), output scaling gives the leakage-uniform estimate
\[
 \boxed{\ \|p_Q\|_\infty
 \le2\!\left[2\sqrt2+\sqrt2\log(1/3+2\sqrt2)\right]
 =8.912738679\ldots<8.913.\ }                           \tag{13}
\]
Only the specified disjointness of original-coordinate supports supplies the independence. The general overlapping-support leakage remains open.

Equation (6) identifies the transverse leakage \(2L\langle u_\perp,X'\rangle\). The first two quadratic directions remain spectrally large even if \(\|u_\perp\|\) is arbitrarily small. The existing pure-hub receiver controls a suitable leakage-free case, while the available nonzero-leakage bounds deteriorate as \(\|u_\perp\|\downarrow0\). Equation (2) is spectral algebra and does not provide an independent physical-coordinate square or a uniform density bound. General matrices with additional spectrum require further analysis as well.

This identity is consistent with the manuscript's one-hub normal form and the fleet04/B18 tiny-edge survivor. It does not resolve the moving-ridge obstruction or the global no-pivot coverage problem. We checked the manuscript's structure and hubs sections and the latest fleet04/B13, B18, B20 and fleet01/B06 reports before recording this scoped lemma.