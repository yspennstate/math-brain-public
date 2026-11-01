# An independent two-packet gluing estimate

**Scope.** This is a proved sufficient case for quadratic forms on disjoint independent coordinate packets. It does not establish a uniform density bound for general matrices with four, or even three, large eigenvalues: cross-packet quadratic interactions destroy the convolution used below.

## Two-coordinate \(L^2\) estimate

Let \(U,V\) be independent real variables with probability-density caps \(M,N>0\). For every invertible real symmetric \(2\times2\) matrix \(B\), every affine term, and
\[
 T=(U,V)B(U,V)^{\mathsf T}+\ell_1U+\ell_2V+c,\qquad D=|\det B|>0,
\]
the output density satisfies
\[
 \|p_T\|_2^2<\frac{171MN}{\sqrt D}. \tag{1}
\]

**Proof.** Put \(U'=MU,V'=NV\). Both transformed densities have cap one; the transformed quadratic matrix has determinant modulus \(D'=D/(M^2N^2)\). Since \(B\) is invertible, translation removes the affine term while preserving the two independent density caps. For a definite matrix the ellipsoid coarea estimate \(\|p_T\|_\infty\le\pi/\sqrt{D'}\), together with \(\|p_T\|_1=1\), proves the stronger bound \(\|p_T\|_2^2\le\pi/\sqrt{D'}\).

For an indefinite matrix, use the orientation-uniform physical-pair estimate in the assembled manuscript, geometry.tex, in the form
\[
 p_T(t)\le\frac{1}{\sqrt{D'}}\left(5.2+\log_+\frac{16\sqrt{D'}}{|t-\kappa|}\right).
\]
Set \(q(x)=\sqrt{D'}\,p_T(\kappa+\sqrt{D'}x)\), a probability density. Write \(a=5.2+\log16\). On \(|x|>1\), \(q(x)\le a\), so \(\int_{|x|>1}q^2\le a\). On \(|x|\le1\), \(q(x)\le a+\log(1/|x|)\), so
\[
 \int_{|x|\le1}q(x)^2\,dx\le
 2\int_0^1(a+\log(1/x))^2\,dx
 =2(a^2+2a+2).
\]
The sum \(2(a^2+2a+2)+a=170.9872855\ldots<171\). Scaling back gives (1). \(\square\)

## Two disjoint packets

Let the coordinate groups underlying \(T_1,T_2,Z\) be mutually independent. Suppose \(T_i\) satisfies the preceding hypotheses with caps \(M_i,N_i\) and determinant modulus \(D_i\). The remainder \(Z\) can have any probability law. Then \(Q=T_1+T_2+Z\) has a density in \(C_0(\mathbb R)\), with
\[
 \|p_Q\|_\infty
 \le \|p_{T_1}\|_2\|p_{T_2}\|_2
 <171\,\frac{\sqrt{M_1N_1M_2N_2}}{(D_1D_2)^{1/4}}. \tag{2}
\]
Indeed, the \(L^2*L^2\) convolution is bounded and continuous by translation continuity in \(L^2\), and convolution with the independent probability law of \(Z\) preserves its \(C_0\) property and supremum bound.

In particular, take two independent physical hubs \(H_1,H_2\), each of density cap one, and two independent light banks with unit linear statistics \(L_1,L_2\), each of density cap at most \(\sqrt2\) by the product-marginal theorem. Any pairwise affine quadratics \(T_i=(H_i,L_i)B_i(H_i,L_i)^{\mathsf T}+\text{affine}\), with \(|\det B_i|>0\), obey
\[
 \|p_{T_1+T_2+Z}\|_\infty
 <\frac{171\sqrt2}{(|\det B_1\det B_2|)^{1/4}}
\]
for an independent remainder \(Z\). For exact bilinear star packets \(B_i=\left(\begin{smallmatrix}0&\lambda_i\\\lambda_i&0\end{smallmatrix}\right)\), this is \(171\sqrt2/\sqrt{|\lambda_1\lambda_2|}\); existing more specialized pure-bilinear bounds may give smaller constants.

**Dependencies:** the orientation-uniform indefinite two-coordinate density envelope in proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/geometry.tex, and the linear product-marginal estimate of Livshyts–Paouris–Pivovarov (2016). The only new step here is the explicit \(L^2\) integration and independent-packet convolution. All interactions between the two packets are excluded; this qualification is essential. Full \(s_3(A)\ge1\) remains open.
