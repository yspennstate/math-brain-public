# A genuine infinite central-density obstruction for a falsely broadened joint-law lemma

**This is not a counterexample to the original-product QFORM conjecture.** It refutes replacing the original-product provenance of three orthogonal linear forms by an arbitrary bounded three-dimensional joint density, even when all *coordinate* one- and two-dimensional marginals are capped and the hub is fully independent.

Fix any target \(s\in(-1,0)\). Let \(L,V\) be independent uniform on \((0,1)\), and let \(E,H\) be independent uniform on \((-1/2,1/2)\), independent also of \((L,V)\). Define
\[
P=\frac{s-V^2}{2L}+E,
\qquad
Q=2HL+V^2+2LP=s+2L(H+E).
\]
The random triple \((L,V,P)\) has a normalized three-dimensional density
\[
g(l,v,p)=\mathbf1_{(0,1)}(l)\mathbf1_{(0,1)}(v)
\mathbf1_{\left|p-(s-v^2)/(2l)\right|<1/2}
\le1.
\]
Its coordinate marginals satisfy
\[
p_L\le1,\quad p_V\le1,\quad p_P\le1,\quad
p_{LV}\le1,\quad p_{LP}\le1,\quad p_{VP}\le1.
\]
Indeed \(p_{LP}(l,p)\) integrates a ≤1 integrand over one unit of \(v\); \(p_{VP}\) integrates over one unit of \(l\). Also \(P=(s-V^2)/(2L)+E\), so convolution with independent cap-one \(E\) ensures \(p_P\le1\). The physical hub \(H\) is independent, cap one. Thus \(U=H+P\) even has conditional density \(p_{U\mid L,V}\le1\), and \(p_{L,U}\le p_L\le1\).

Nevertheless \(T=H+E\) has triangular density \(f_T(t)=(1-|t|)_+\). For \(0<|x|<1/2\), conditioning on \(L=l\) gives
\[
p_Q(s+x)
=\int_0^1\frac{1}{2l}f_T\!\left(\frac{x}{2l}\right)\,dl
\ge\int_{|x|}^{1}\frac{dl}{4l}
=\frac14\log\frac1{|x|}.
\]
Hence \(\|p_Q\|_\infty=\infty\), including essential supremum on every neighborhood of the fixed **negative** target \(s\).

All quantitative assertions above are about coordinate-axis marginals of an arbitrary joint triple. They do **not** assert the boundedness of every oblique orthogonal two-dimensional marginal. The defining nonlinear relation for \(P\) also prevents treating \((L,V,P)\) as an orthonormal linear projection of independent original coordinates. This construction is an explicit mathematical reason that a coarea step based only on joint/marginal caps, or on the physical hub's conditional cap, cannot close the fully overlapping original-product case. The product provenance, or an equally strong additional geometric hypothesis, must be used.
