# Exact rank-three physical coloop with zero hub diagonal

**Status:** Proved special case. This does not resolve the conjecture for a nonzero hub diagonal, an additional spectral direction, or the small-leakage canonical model with a third light projection.

## Statement

Let \(X_1,\ldots,X_n\) be independent real variables with probability densities at most one. Let \(A\) be real symmetric of **exact rank three**, with \(s_3(A)\ge1\). Suppose some original physical coordinate \(h\) satisfies \(e_h\in\operatorname{range}(A)\) and \(A_{hh}=0\). Then \(Q=X^\top A X+c\) has a probability density satisfying
\[
 \|p_Q\|_\infty\le\frac12+8\sqrt2.\tag{1}
\]
The same bound allows an affine term \(b^\top X\) when \(b\in\operatorname{range}(A)\). The original full conjecture concerns the pure quadratic.

## Exact spectral normalization

Write \(H=X_h\) and let \(D=A_{-h,-h}\), \(w=A_{-h,h}\). Since \(e_h\) is in the rank-three range, \(w\ne0\): if \(w=0\), \(A_{hh}=0\) would imply \(Ae_h=0\), contrary to the range being perpendicular to the nullspace. Put \(\tau=\|w\|_2>0\), \(\ell=w/\tau\), and choose a unit \(v\) perpendicular to \(\ell\) spanning the remaining direction of the rank-three range outside \(e_h\). The leaf projections \(L=\ell^\top X_{-h}\) and \(V=v^\top X_{-h}\) are a genuine two-dimensional orthonormal projection of **original independent** leaf variables. They need not be independent of each other, while \(H\) is independent of the pair.

On \(\operatorname{span}\{e_h,\ell,v\}\), the matrix of \(A\) is
\[
 B=\begin{pmatrix}0&\tau&0\\\tau&b_0&c_0\\0&c_0&\lambda\end{pmatrix}.
\]
Its determinant is \(-\tau^2\lambda\), so \(\lambda\ne0\). Direct cofactors show \((B^{-1})_{h,\ell}=1/\tau\) and \((B^{-1})_{v,v}=1/\lambda\). Since \(s_3(A)\ge1\), all three nonzero singular values of \(B\) are at least one, hence \(\|B^{-1}\|_{\rm op}\le1\). Thus
\[
 \tau\ge1,\qquad |\lambda|\ge1.\tag{2}
\]
Complete the leaf square without touching the independent hub:
\[
 W=V+(c_0/\lambda)L,\quad
 \mu=b_0-c_0^2/\lambda,\quad
 Q=2\tau HL+\mu L^2+\lambda W^2.
\]
Set \(l=\tau L\), \(v'=\sqrt{|\lambda|}W\), \(\beta=\mu/\tau^2\), and \(\sigma=\operatorname{sgn}(\lambda)\). Then \(Q=2Hl+\beta l^2+\sigma(v')^2\). The affine shear \((L,V)\mapsto(L,W)\) has determinant one. If the orthonormal projection \((L,V)\) has planar density bounded by \(K\), the density \(g(l,v')\) is bounded by \(K/(\tau\sqrt{|\lambda|})\le K\). The standard two-dimensional projection-density bound for independent cap-one originals gives \(K\le2\).

## A uniform square-root-kernel lemma

Let \(H\) be independent of a pair \((l,v)\), with \(f_H\le1\) and a joint planar density \(g(l,v)\le K\). For any measurable real \(r(l)\), \(\sigma\in\{-1,1\}\), and \(q=2Hl+r(l)+\sigma v^2\), one has
\[
 \|p_q\|_\infty\le\frac12+4\sqrt2K.\tag{3}
\]
Indeed, \(l=0\) has probability zero. Integrate over \(h\) on the region \(|l|\ge1\): the map \(h\mapsto2hl+r(l)+\sigma v^2\) gives a density at most \(1/(2|l|)\), hence this region contributes at most \(1/2\).

On \(0<|l|<1\), first discard \(g(l,v)\) in favor of \(K\), then integrate in \(v\). At every target \(s\), the contribution is at most
\[
 K\int_{|l|<1}\int_{\mathbb R} f_H(h)
      [\sigma(s-2hl-r(l))]_+^{-1/2}\,dh\,dl.\tag{4}
\]
For fixed nonzero \(l\), the affine variable \(u=\sigma(s-2hl-r(l))\) has a probability density at most \(1/(2|l|)\). Rearranging that density under its cap and total mass one yields
\[
 \int_{\mathbb R}f_H(h)[\sigma(s-2hl-r(l))]_+^{-1/2}\,dh
 \le\frac1{2|l|}\int_0^{2|l|}u^{-1/2}\,du
 =\sqrt{2/|l|}.\tag{5}
\]
Integrating \(\sqrt{2/|l|}\) over \(-1<l<1\) gives \(4\sqrt2\), proving (3). Approximate Dirac kernels justify the calculation for arbitrary measurable densities, or use the standard pushforward density formula off the measure-zero set \(l=0\).

Apply (3) with \(K\le2\) and (2) to obtain (1) for the zero-affine quadratic.

## Affine terms and exact scope

When \(b\in\operatorname{range}(A)\), its affine term is \(b_hH+b_L L+b_VV\). After the shear \(W=V+(c_0/\lambda)L\), complete \(\lambda W^2+b_VW\) by translating \(W\). Translate the scaled \(l=\tau L\) by \(b_h/2\), so the hub terms are precisely \(2Hl\); the residual leaf terms are a real quadratic-plus-affine function \(r(l)\). These two translations preserve the planar density cap, and the lemma already allows arbitrary \(r(l)\). Constant shifts have no effect on the bound. Affine components outside \(\operatorname{range}(A)\) are not covered by this argument, since conditioning on a null projection of the original product variables can increase the conditional planar light density.

The bound relies on a **two-dimensional** light pair after isolating the hub. With a third overlapping light projection \(P\), the term \(2\varepsilon LP\) cannot be sheared into the one square \(V^2\) without changing the relevant joint-dimensional cap. That case is the main unresolved exact-rank-three canonical model when the physical hub is not an exact spectral coloop.
