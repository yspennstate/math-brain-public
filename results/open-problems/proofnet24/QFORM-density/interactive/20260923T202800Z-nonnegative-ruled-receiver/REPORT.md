# Uniform nonnegative-level receiver for a one-hub quadratic and arbitrary light overlap

**Status:** proved analytic theorem. It closes every output level \(s\ge0\) of the canonical one-hub form, uniformly in the \(L^2\) coefficient and the overlapping third-light coefficient. It does **not** settle negative levels or a hub-square perturbation.

## Theorem

Let \(H\) be a real random variable with probability density \(f_H\le1\). Let \(Z=(L,V,P)\) be independent of \(H\) and have a joint density \(g\). Suppose every orthogonal two-dimensional projection of \(Z\) has density bounded by \(K\). For arbitrary \(\beta,\varepsilon\in\mathbb R\), put
\[
 Q=2HL+\beta L^2+V^2+2\varepsilon LP.
\]
Then the restriction of the law of \(Q\) to the nonnegative half-line has a density with
\[
 \operatorname*{ess\,sup}_{s\ge0}p_Q(s)
 \le\frac12+4\sqrt2\,K.                                    \tag{1}
\]
The bound is independent of \(\beta,\varepsilon\), the hub support, and light support or moments.

If \(Z=UX\), where \(UU^T=I_3\) and the original \(X_i\) are independent real variables with probability densities at most one, the product-projection inequality gives \(K\le2\). Thus
\[
 \operatorname*{ess\,sup}_{s\ge0}p_Q(s)
 \le\frac12+8\sqrt2<11.814.                                \tag{2}
\]
This uses actual product provenance only to certify the projection caps. The analytic receiver itself allows an arbitrary dependent light triple satisfying those caps.

## Ruled parametrization for \(\varepsilon\ne0\)

First suppose \(g\) is Gaussian-mollified. Its two-dimensional projection densities remain bounded by \(K\), since orthogonal projection commutes with convolution and convolution with a probability Gaussian preserves an \(L^\infty\) cap. The projected densities are continuous, so their caps hold pointwise. In particular:

* The \((L,V)\) marginal \(m(l,v)=\int g(l,v,p)\,dp\) obeys \(m\le K\).
* For every unit direction \(d\) and every affine line \(z_0+\mathbb R d\), the line integral \(\int_{\mathbb R}g(z_0+u d)\,du\le K\). It is the continuous density of the orthogonal projection onto \(d^\perp\).

Fix \(s\ge0\) and write \(q=\sqrt s\). For \(l\ne0\), use
\[
 v=q+t l,\qquad
 p=-\frac{h+q t+(\beta+t^2)l/2}{\varepsilon}.               \tag{3}
\]
These points satisfy \(2hl+\beta l^2+v^2+2\varepsilon lp=s\). In the density integral, integration of the Dirac mass in \(p\), followed by \(dv=|l|\,dt\), gives the exact Jacobian \(1/(2|\varepsilon|)\):
\[
 p_Q(s)=\frac1{2|\varepsilon|}
 \int_{\mathbb R}f_H(h)\,dh\int_{\mathbb R}dt
 \int_{\mathbb R}dl\,
 g\!\left(l,q+t l,
 -\frac{h+q t+(\beta+t^2)l/2}{\varepsilon}\right).          \tag{4}
\]
The set \(L=0\) has probability zero because \((L,V)\) has a density.

Let \(T>0\). Choose an exceptional set \(E_T\) of slope parameters:

* If \(\beta\ge0\), set \(E_T=[-T,T]\).
* If \(\beta<0\), write \(r_0=\sqrt{-\beta}\) and set
  \(E_T=[r_0-T,r_0+T]\cup[-r_0-T,-r_0+T]\).

Then \(|E_T|\le4T\), and
\[
 \int_{\mathbb R\setminus E_T}\frac{dt}{|t^2+\beta|}
 \le\frac2T.                                                \tag{5}
\]
For \(\beta\ge0\), use \(t^2+\beta\ge t^2\). For \(\beta=-r_0^2<0\), the complement has \(|t-r_0|,|t+r_0|\ge T\), while
\[
 \frac1{|t-r_0||t+r_0|}
 \le\frac12\left(\frac1{(t-r_0)^2}
                 +\frac1{(t+r_0)^2}\right).
\]
Each squared-denominator integral over the complement is at most \(2/T\), proving (5).

On \(t\in E_T\), integrate first in \(h\) in (4). The affine map \(h\mapsto p\) has Jacobian \(1/|\varepsilon|\), and \(f_H\le1\), so this part is at most
\[
 \frac12\int_{E_T}dt\int_{\mathbb R}m(l,q+t l)\,dl.          \tag{6}
\]
For \(|l|\ge1\), change \(t\) to \(v=q+t l\), then use \(1/|l|\le1\) and \(\int m=1\); this costs at most \(1/2\). For \(|l|<1\), use \(m\le K\), \(|E_T|\le4T\), and the \(l\)-interval length two; this costs at most \(4KT\). Thus (6) is at most \(1/2+4KT\).

On \(t\notin E_T\), for each fixed \(h,t,s\), the points in (3) form an affine line as \(l\) varies, with direction
\[
 d_t=\left(1,t,-\frac{\beta+t^2}{2\varepsilon}\right).
\]
The line-X-ray cap gives
\[
 \int_{\mathbb R}
 g\!\left(l,q+t l,
 -\frac{h+q t+(\beta+t^2)l/2}{\varepsilon}\right)\,dl
 \le\frac K{\|d_t\|}
 \le\frac{2|\varepsilon|K}{|\beta+t^2|}.
\]
Formulae (4) and (5), with \(\int f_H=1\), bound this complementary part by \(2K/T\). We have proved
\[
 p_Q(s)\le\frac12+4KT+\frac{2K}{T}
 \quad(s\ge0,\ \varepsilon\ne0).                            \tag{7}
\]
Choose \(T=1/\sqrt2\) to obtain (1).

The initial Gaussian mollification was used only to turn essential projection caps into pointwise caps on every line offset. If \(Z_\delta=Z+G_\delta\), then \(Z_\delta\Rightarrow Z\), and the corresponding quadratic outputs converge in law by the continuous mapping theorem. Their uniform density bound implies \(\Pr(Q\in I)\le C|I|\) for every open interval \(I\subset[0,\infty)\) by the Portmanteau theorem. This yields the essential bound (1) for the original light law.

## The case \(\varepsilon=0\)

Here only the \((L,V)\) joint cap \(m\le K\) is needed. On \(|L|\ge1\), invert the affine map in \(H\) to get a density contribution at most \(1/2\). On \(0<|l|<1\), integrate in \(v\) first using \(m(l,v)\le K\); the two-branch square Jacobian gives
\[
 K\int_{\mathbb R} f_H(h)
   [s-2lh-\beta l^2]_+^{-1/2}\,dh.
\]
For fixed \(l\ne0\), the bracket is affine in \(h\) with slope magnitude \(2|l|\). The bathtub bound for a cap-one probability density yields
\[
 \int f_H(h)[s-2lh-\beta l^2]_+^{-1/2}\,dh
 \le\int_0^1(2|l|u)^{-1/2}\,du
 =\sqrt{\frac2{|l|}}.
\]
Integration over \(-1<l<1\) gives \(4\sqrt2 K\), proving (1) also when \(\varepsilon=0\).

## Exact boundary

The geometry of \(s\ge0\) admits the real ruling (3). At negative output levels its counterpart is a positively curved sheet, and the projection-only fake with an independent hub has unbounded density at \(s=-1\) despite all two-dimensional projection caps. Thus (1) cannot be extended to negative levels using only the stated projection hypotheses.

Adding \(aH^2\) changes the hub-to-\(p\) map in (3) from affine to nonlinear and can destroy the low-slope estimate (6). No small-hub-square claim is made here. The unrestricted three-eigenvalue bounded-density problem remains **OPEN**.
