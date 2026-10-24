# Two-light coarea receiver with a shear in the square direction

**Status:** proved scoped addendum, independently checked against the [beta-uniform one-hub proof](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T203100Z-beta-uniform-one-hub-square/REPORT.md). It applies when the leakage linear form lies in the span of the two displayed light variables. It excludes a hub self-quadratic term \(aH^2\) and excludes leakage through an independent third light direction \(P\).

## Lemma

Let \(H\) have a probability density \(0\le f_H\le1\). Let \((L,V)\), independent of \(H\), have an arbitrary joint probability density \(0\le g(l,v)\le M\). No independence between \(L\) and \(V\) is assumed. For \(t\lambda\ne0\) and any real \(\beta,\varepsilon\), put
\[
 Q=2tHL+\beta L^2+2\varepsilon LV+\lambda V^2.             \tag{1}
\]
Then \(Q\) has an essentially bounded density and
\[
 \boxed{\|p_Q\|_\infty
 \le\frac12+\frac{4\sqrt2\,M}{|t|\sqrt{|\lambda|}}.}         \tag{2}
\]
The same holds for deterministic affine terms in the three displayed variables \(H,L,V\), since their nondegenerate \(3\times3\) coefficient matrix permits a deterministic translation of these variables.

## Density formula and proof

Since \(g\) is a planar density, \(\mathbb P(L=0)=0\). Conditioning on \((L,V)=(l,v)\) gives, for almost every \(s\),
\[
 p_Q(s)=\iint_{\mathbb R^2}
  \frac{g(l,v)}{2|tl|}
  f_H\!\left(
   \frac{s-\beta l^2-2\varepsilon lv-\lambda v^2}{2tl}
  \right)\,dl\,dv.                                         \tag{3}
\]
The formula follows first for nonnegative test functions by Tonelli, so the subsequent estimates establish both density existence and its essential bound.

Complete the square by putting
\[
 v'=v+\frac{\varepsilon}{\lambda}l,\qquad
 \beta'=\beta-\frac{\varepsilon^2}{\lambda}.
\]
The sheared density \(g'(l,v')=g(l,v'-\varepsilon l/\lambda)\) still has mass one and cap \(M\), while
\(Q=2tHL+\beta'L^2+\lambda(V')^2\).

On \(|l|>1/|t|\), use \(f_H\le1\) directly in (3). This part contributes at most
\[
 \iint_{|l|>1/|t|}\frac{g'(l,v')}{2|tl|}\,dl\,dv'
 \le\frac12.                                                \tag{4}
\]
For \(|l|\le1/|t|\), use \(g'\le M\) and integrate \(v'\) by the square-map identity. Writing
\(\sigma=\operatorname{sgn}\lambda\) and
\([x]_{+,\sigma}^{-1/2}=\mathbf1_{\{\sigma x>0\}}|x|^{-1/2}\),
this contribution is at most
\[
 \frac{M}{\sqrt{|\lambda|}}
 \int_{|l|\le1/|t|}
 \int_{\mathbb R} f_H(h)\,
 [s-\beta'l^2-2tlh]_{+,\sigma}^{-1/2}\,dh\,dl.              \tag{5}
\]
For each nonzero \(l\), the inner kernel is one-sided and decreases from its singular threshold. Among all \(f_H\le1\) with integral one, filling the nearest permitted interval of length one maximizes its integral. Since the affine slope in \(h\) has magnitude \(2|tl|\),
\[
 \int f_H(h)
 [s-\beta'l^2-2tlh]_{+,\sigma}^{-1/2}\,dh
 \le\int_0^1(2|tl|u)^{-1/2}\,du
 =\sqrt{\frac2{|tl|}}.                                     \tag{6}
\]
The shift \(\beta'l^2\) does not affect this estimate. Finally,
\[
 \frac{M}{\sqrt{|\lambda|}}
 \int_{|l|\le1/|t|}\sqrt{\frac2{|tl|}}\,dl
 =\frac{4\sqrt2\,M}{|t|\sqrt{|\lambda|}}.                    \tag{7}
\]
Equations (4) and (7) prove (2). A standard monotone approximation of the singular square kernel justifies the same inequality at every density point without choosing point values for \(f_H\).

## Exact-rank-three physical-hub corollary

Suppose \(H=X_h\) is one original independent cap-one coordinate and \(L=\ell\cdot X_{-h}\), \(V=v\cdot X_{-h}\), where \(\ell,v\) are orthonormal. Suppose the entire homogeneous quadratic matrix has rank exactly three and is
\[
 A=U\begin{pmatrix}
 0&t&0\\ t&\beta&\varepsilon\\0&\varepsilon&\lambda
 \end{pmatrix}U^\mathsf T,\qquad U=[e_h\ \ell\ v],
\]
with all three nonzero singular values at least one. Then
\[
 |\det A_{\mathrm{essential}}|=|t|^2|\lambda|\ge1,
 \qquad\text{hence}\qquad |t|\sqrt{|\lambda|}\ge1.
\]
If the genuine product projection \((L,V)\) has a known joint density cap \(M\), (2) gives
\[
 \boxed{\|p_{X^\mathsf T A X}\|_\infty\le\tfrac12+4\sqrt2\,M.} \tag{8}
\]
This also allows an affine term in \(\operatorname{range}(A)\) by completing the square through a deterministic translation of the original input coordinates. In particular, any applicable dimension-free two-dimensional projection cap makes (8) a universal bound for this **exact physical-coloop** family.

The unproved near-coloop model has an additional light direction \(P\perp L,V\) and term \(2\varepsilon LP\), with \(P,L,V\) all drawing on the same original inputs. The shear above cannot absorb that term. A hub self-term \(aH^2\) also invalidates the linear-in-\(H\) density formula (3); this addendum makes no claim for it.
