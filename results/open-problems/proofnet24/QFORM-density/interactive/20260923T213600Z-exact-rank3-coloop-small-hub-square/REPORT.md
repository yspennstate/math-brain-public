# Exact rank-three physical coloop with a small hub diagonal

**Status:** Proved all-level theorem for the specified exact-rank-three case. In particular, this closes the physical spectral-coloop branch for every \(|A_{hh}|\le1/4\), including both signs of that diagonal and arbitrary cross coupling between the two light projections. It does not address a third overlapping light projection or the general high-dimensional conjecture.

## Theorem

Let the original real variables \(X_i\) be independent with densities at most one. Suppose a real symmetric \(A\) has **exact rank three**, \(s_3(A)\ge1\), and a physical coordinate \(h\) satisfies \(e_h\in\operatorname{range}(A)\) and \(|a|:=|A_{hh}|\le1/4\). Then \(X^\top A X\) has a bounded probability density, with a universal all-target bound. The same estimate holds for \(X^\top A X+b^\top X+c\) if \(b\in\operatorname{range}(A)\); arbitrary affine components along the nullspace are outside the proved claim.

The proof actually allows **any** joint planar density \(g(L,V)\le K\) for the light pair below, with an independent cap-one hub. The orthonormal light projection of independent cap-one originals has \(K\le2\).

## Spectral and density normalization

As the physical hub lies in the three-dimensional spectral range, write \(H=X_h\) and choose orthonormal light coordinates \(L,V\), with \(L\) along \(A_{-h,h}\). This off-diagonal column is nonzero: otherwise \(e_h\) would be a nonzero eigenvector with eigenvalue \(a\), which either puts it in the nullspace or contradicts \(s_3(A)\ge1\) since \(|a|<1\). The nonzero matrix is
\[
 B=\begin{pmatrix}a&\tau&0\\\tau&b_0&c_0\\0&c_0&\lambda\end{pmatrix},\qquad \tau>0.
\]
Set \(B_*\) by changing only \(a,\lambda\) to zero. Its first and third rows are both supported on the middle column, so \(\operatorname{rank}B_*\le2\). Hence
\[
 1\le s_3(B)\le\|B-B_*\|_{\rm op}=\max(|a|,|\lambda|),
\]
and \(|\lambda|\ge1\). Complete the light square with \(W=V+(c_0/\lambda)L\), \(\mu=b_0-c_0^2/\lambda\). The \((h,L)\) Schur complement of the \(\lambda\) block is \(C_0=\begin{pmatrix}a&\tau\\\tau&\mu\end{pmatrix}\), so the principal \((h,L)\) block of \(B^{-1}\) is \(C_0^{-1}\). Therefore \(\|C_0^{-1}\|_{\rm op}\le\|B^{-1}\|_{\rm op}\le1\). Its \((h,h)\) entry gives
\[
 \frac{|\mu|}{|a\mu-\tau^2|}\le1,
 \qquad
 (1-|a|)|\mu|\le\tau^2.
\]
Set \(l=\tau L\), \(v=\sqrt{|\lambda|}W\), \(\beta=\mu/\tau^2\), \(\sigma=\operatorname{sgn}\lambda\). Then
\[
 Q=aH^2+2Hl+\beta l^2+\sigma v^2,
 \quad |a|\le\tfrac14,
 \quad |\beta|\le\tfrac43.
 \tag{1}
\]
Since \(s_2(C_0)\ge1\), \(|\det C_0|\ge1\); and \(|\det C_0|=\tau^2|a\beta-1|\le(4/3)\tau^2\). Thus \(\tau\ge\sqrt3/2\). The shear has determinant one, and rescaling changes the planar density cap to
\[
 g(l,v)\le K':=\frac{K}{\tau\sqrt{|\lambda|}}\le\frac{2K}{\sqrt3}.
 \tag{2}
\]
The pair remains independent of \(H\), even though \(l,v\) need not be independent of each other. Moreover the two-variable Hessian \(C=\begin{pmatrix}a&1\\1&\beta\end{pmatrix}\) has \(|\det C|=|1-a\beta|\ge2/3\) and Frobenius norm less than two. Hence \(s_2(C)>1/3\).

## Small \(|l|\): a two-variable product half-Riesz bound

For any target \(s\), on \(|l|<1\), discard the joint density in favor of \(K'\) and integrate the \(v\) square. The density contribution is at most
\[
 K'\int_{-1}^{1}\int_{\mathbb R}f_H(h)
  [\sigma(s-a h^2-2hl-\beta l^2)]_+^{-1/2}\,dh\,dl.
 \tag{3}
\]
The integrand is bounded by the absolute half-Riesz kernel. Regard \(l\) as twice the probability law of a uniform variable on \([-1,1]\), independent of \(H\); its density is \(1/2\le1\). The proved **two-variable product half-Riesz theorem** states that independent cap-one variables \((H,U)\) and any symmetric \(2\times2\) Hessian with least singular value at least a fixed constant have \(\sup_s\mathbb E|s-(H,U)^\top C(H,U)|^{-1/2}\le C_1\). It applies here because \(s_2(C)>1/3\). Thus (3) is at most \(2C_1K'\), uniformly in \(s,a,\beta\) and all fragmented hub laws.

## Large \(|l|\): two derivative sectors

On \(|l|\ge1\), split into \(E_{\rm good}=\{|a h+l|\ge|l|/2\}\) and \(E_{\rm bad}=\{|a h+l|<|l|/2\}\).

On the good set, \(|\partial_h Q|=2|a h+l|\ge|l|\). For each fixed \((l,v)\), the quadratic map in \(h\) has at most two inverse branches, each with the displayed derivative lower bound. Since \(f_H\le1\), its conditional output density on this set is at most \(2/|l|\). Averaging the probability density \(g(l,v)\) gives a contribution at most \(2\).

On the bad set, \(a h\) and \(l\) have opposite signs and the allowed \(l\) for each fixed \(h\) lies in one interval \(I_h\) of length at most \((4/3)|a h|\), with \((2/3)|a h|<|l|<2|a h|\). In particular \(h\ne0\). The derivative of \(a h^2+2hl+\beta l^2\) in \(l\) has fixed sign there and satisfies
\[
 |2h+2\beta l|\ge2|h|-2(4/3)(2|a h|)
 \ge(2/3)|h|.
 \tag{4}
\]
Discard \(g\le K'\) and integrate in \(v\), just as in (3). For each fixed \(h\), the image of restricted Lebesgue measure \(\boldsymbol1_{I_h}(l)dl\) under \(l\mapsto\sigma(s-a h^2-2hl-\beta l^2)\) has a density at most \(3/(2|h|)\) and total mass at most \((4/3)|a h|\). Rearranging this image density under its cap and total mass gives
\[
 \int_{I_h}[\sigma(s-a h^2-2hl-\beta l^2)]_+^{-1/2}dl
 \le2\sqrt{\frac{3}{2|h|}\cdot\frac43|a h|}
 =2\sqrt{2|a|}.
 \tag{5}
\]
Integrate against the probability density \(f_H(h)\), multiply by \(K'\), and use \(|a|\le1/4\). The bad set contributes at most \(\sqrt2K'\). Combining with the small-region and good-region estimates proves the universal all-level bound \(\|p_Q\|_\infty\le2+(2C_1+\sqrt2)2K/\sqrt3\); with \(K\le2\), this is an absolute constant.

## Affine range terms and remaining gap

An affine term in the three-dimensional range can be removed by translating \((H,L,V)\) by \(\tfrac12 B^{-1}b_{\rm range}\). This translates \(H\) and the planar pair separately, preserving independence and both density caps. The quadratic Hessian and the estimate above are unchanged. If \(b\) has a component in the nullspace, this translation cannot remove it; conditioning on a null projection need not preserve the planar cap.

An **approximate** spectral coloop has a third overlapping light projection \(P\), producing \(2\varepsilon LP\). The proof above integrates one transverse square against a **two-dimensional** light density cap. Dropping a three-dimensional light density in the same fashion is invalid; the negative-target hyperbolic fake demonstrates why. That exact product-source overlapping case remains open.
