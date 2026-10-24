# Canonical rank three with an independent linear source

**Status:** Proved all-level original-product theorem for a disjoint physical support configuration. It allows complete overlap of the third and square light projections and arbitrary fragmented, infinite-variance laws. It does not prove the canonical case when the linear projection shares original inputs with either of the other two light projections.

## Statement

Let \(H,X_1,\ldots,X_n\) be independent real variables, each with a probability density bounded by one. Let \(\ell,v,p\in\mathbb R^n\) be orthonormal and put \(L=\ell\cdot X\), \(V=v\cdot X\), \(P=p\cdot X\). Assume the physical support of \(\ell\) is disjoint from the union of the physical supports of \(v\) and \(p\). Then, for every \(\beta,\varepsilon\in\mathbb R\),
\[
 Q=2HL+\beta L^2+V^2+2\varepsilon LP
\]
has a density satisfying
\[
 \|p_Q\|_\infty\le\sqrt2\,(7.2+2\log16)<19.
 \tag{1}
\]
No spectral restriction \(|\beta|\le\varepsilon^2\) is needed for this stronger physical-source hypothesis. The bound does not depend on the law, dimension, coefficient \(\beta\), coefficient \(\varepsilon\), or output level.

## Proof

The disjoint support hypothesis makes \(L\) independent of the pair \((P,V)\). The standard one-dimensional original-product projection bound gives \(\|f_L\|_\infty,\|f_V\|_\infty\le\sqrt2\). Conditional on any value \((P,V)=(p_0,v_0)\), the variables \(H,L\) remain independent with their original distributions; in particular \(H+\varepsilon p_0\) has a density bounded by one. Set \(Y=\sqrt2L\), whose density is also bounded by one. The conditional two-input quadratic is
\[
 2(H+\varepsilon p_0)L+\beta L^2
 =\begin{pmatrix}H+\varepsilon p_0&Y\end{pmatrix}
  \begin{pmatrix}0&1/\sqrt2\\1/\sqrt2&\beta/2\end{pmatrix}
  \begin{pmatrix}H+\varepsilon p_0\\Y\end{pmatrix}.
\]
Its matrix is indefinite with determinant \(-1/2\), and its critical value is exactly zero for every \(p_0,\beta,\varepsilon\). The proved uniform hyperbolic envelope for two independent cap-one originals (`geometry.tex`, Theorem `geom:pair`) therefore gives the conditional density bound, for almost every \(u\ne0\),
\[
 p_{2(H+\varepsilon p_0)L+\beta L^2}(u)
 \le\sqrt2\left(5.2+\log_+\frac{16/\sqrt2}{|u|}\right)
 \le\sqrt2\left(5.2+\log_+\frac{16}{|u|}\right).
 \tag{2}
\]
The critical value zero matters: it is independent of the conditioned \(p_0\), so the possible correlation of \(P\) and \(V\) has no effect on the next step.

For any \(s\in\mathbb R\) and \(r>0\), the set \(\{x:|x^2-s|\le r\}\) has Lebesgue length at most \(2\sqrt{2r}\). Since \(\|f_V\|_\infty\le\sqrt2\),
\[
 \Pr(|V^2-s|\le r)\le\min\{1,4\sqrt r\}.
 \tag{3}
\]
Layer cake gives, uniformly in \(s\),
\[
 \begin{split}
 \mathbb E\log_+\frac{16}{|s-V^2|}
 &=\int_0^\infty\Pr\{|s-V^2|<16e^{-t}\}\,dt\\
 &\le\int_0^\infty\min\{1,16e^{-t/2}\}\,dt
 =2\log16+2.
 \end{split}
 \tag{4}
\]
Average (2) over the potentially dependent pair \((P,V)\) with \(u=s-V^2\), and insert (4). This proves (1). Formula (2) can be integrated against an output interval test function before conditioning; Fubini then yields a density bound without any pointwise-version assumption.

## Scope

The result is an exact original-product statement; it does not pretend that \(L,V,P\) are jointly independent. Only \(L\perp(P,V)\) is imposed, by a real partition of original physical coordinates. In particular, \(P\) may be arbitrarily correlated with \(V\) and have unbounded support or variance. If some originals feed both \(L\) and \((P,V)\), conditioning on \((P,V)\) does not preserve the cap on the conditional law of \(L\), and this argument no longer applies.

The hyperbolic envelope and the one-dimensional projection-density bound are in the manuscript at commit d6f59993e85da91da39942ae96d92481abbaf541 (`geometry.tex` and `supplement.tex`).
