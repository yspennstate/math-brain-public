# A genuine-product obstruction to strong dyadic hub-target L²

**Status:** proved method counterexample. It does not refute the quadratic density conjecture. It shows that the target-density estimate \(\|T_{s,r}\|_{L^2(dh)}^2\lesssim r\), uniformly in \(s,\beta,\varepsilon\), is false even for a diffuse orthonormal three-frame of genuine independent original inputs. The weak-\(L^2\) endpoint remains viable.

Let \(X_1,\ldots,X_6\) be independent uniform variables on \([-1/2,1/2]\), and define
\[
 L=(X_1+X_2)/\sqrt2,\quad
 V=(X_3+X_4)/\sqrt2,\quad
 P=(X_5+X_6)/\sqrt2.
\]
The vectors defining \(L,V,P\) are orthonormal, every original row has leverage \(1/2\), and \(L,V,P\) are independent. Their common density is
\[
 g(z)=\sqrt2(1-\sqrt2|z|)_+.
\]
For \(\beta=\varepsilon=0\), set
\[
 T_{s,r}(h)=\mathbb E\!\left[
  \mathbf1_{\{r\le|L|\le2r\}}\,
  \delta(2hL+V^2-s)\right].
\]
Equivalently this is the density, in the hub target \(h\), of \(T_s=(s-V^2)/(2L)\) weighted by \(1/(2|L|)\) on the dyadic shell. Fix \(r=1/16\) and \(c=1/64\). For \(s=-\delta\), \(0\le\delta<c\), and \(h=-x\) with
\[
 \delta/r\le x\le c/r,
\]
restrict the integral to \(r\le l\le2r\). Then
\[
 w=2lx-\delta\in[rx,4rx]\subset(0,1/16].
\]
On this range \(g(l)\ge\sqrt2/2\) and \(g(\sqrt w)=g(-\sqrt w)\ge\sqrt2/2\). Integrating the Dirac factor in \(v\) gives
\[
 \begin{aligned}
 T_{-\delta,r}(-x)
 &\ge\int_r^{2r}g(l)
       \frac{g(\sqrt w)+g(-\sqrt w)}{2\sqrt w}\,dl\\
 &\ge \frac{\sqrt r}{4\sqrt x}.             \tag{1}
 \end{aligned}
\]
Consequently, for every \(0<\delta<c\),
\[
 \|T_{-\delta,r}\|_{L^2(dh)}^2
 \ge \frac r{16}\log\frac c\delta
 \longrightarrow\infty\qquad(\delta\downarrow0). \tag{2}
\]
At the nonnegative endpoint \(s=0\), (1) holds for \(0<x\le c/r\), and \(T_{0,r}\notin L^2(dh)\).

The same logarithmic divergence persists along small positive leakage \(\varepsilon=\delta^2\), \(\beta=0\), as \(\delta\downarrow0\). Indeed \(P\) is supported on \([-1/\sqrt2,1/\sqrt2]\). For \(x\in[2\delta/r,c/r]\), \(l\in[r,2r]\), and sufficiently small \(\delta\), the Dirac equation
\[
 V^2=2l(x-\varepsilon P)-\delta
\]
has right side between \(rx\) and \(5rx\le5c<1/8\), uniformly over the support of \(P\). The same triangular-density lower bounds, integrated over \(P\), give \(T_{-\delta,r}(-x)\ge C\sqrt{r/x}\) with an absolute \(C>0\). Its squared integral again grows like \(r\log(c/\delta)\), while \(\varepsilon/\delta=\delta\to0\).

The failure comes from the universal square-root caustic of \(V^2\). Since the output density of \(2HL+V^2+2\varepsilon LP\) can still be bounded after averaging against a cap-one hub density, strong \(L^2\) is an unnecessarily strong intermediate target. A weak-\(L^2\) or Lorentz estimate has the correct scaling.
