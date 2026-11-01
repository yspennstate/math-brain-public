# Early calculation — critical selector packet plus one physical square

Run: `20260923T205229Z-fleet01-B03-QFORM-r33`.

Assume the dependence-safe weighted-selector estimate already proved in fleet01/B03 r32 from the completed fleet02/B03 whole-selector Plancherel theorem:

\[
 |\phi_Q(t)|^2\le K^2 |t|^{-2} H(t),\qquad
 H(t)=\mathbb E|G_{h(W)}(t)|^2\le1,
\]
with
\[
K=\pi\sqrt{\frac{M_ZM_C}{|\det B|}},\qquad
G_a(t)=\mathbb E_X e^{itd(X-a)^2},\qquad D=|d|.
\]
The shift-uniform square-energy lemma from r32 is
\[
\int_T^{2T}H(t)\,dt\le D^{-1}L(DT),\qquad
L(x)=8+8\pi\log(1+\sqrt{x}/2),\quad DT\ge1.
\]

For any `y>=1`, put `T0=y/D`, `kappa=KD`, and `T_j=2^jT0`. On each tail block Cauchy--Schwarz gives
\[
\int_{T_j}^{2T_j}|\phi_Q(t)|\,dt
\le K\Big(\int_{T_j}^{2T_j}t^{-2}dt\Big)^{1/2}
       \Big(\int_{T_j}^{2T_j}H(t)dt\Big)^{1/2}
\le \frac{K}{\sqrt{2DT_0}}2^{-j/2}\sqrt{L(2^jy)}.
\]
Hence, with
\[
S(y)=\sum_{j\ge0}2^{-j/2}\sqrt{L(2^jy)},
\]
we get the exact one-parameter bound
\[
\boxed{
\|p_Q\|_\infty
\le \frac1{\pi D}\left[y+\frac{\kappa}{\sqrt{2y}}S(y)\right]
}\tag{E1}
\]
provided the full theorem hypotheses needed for the weighted-selector estimate hold.  This already improves the previous forced choice `T0=max(K,D^-1)`: the tail estimate is valid even when `T0<K` because `|phi|^2<=K^2t^-2H` itself is valid there.

For `y>=1`,
\[
L(2^jy)\le L_0+4\pi\log y+4\pi j\log2,
\qquad L_0=8+8\pi\log(3/2).
\]
With `r=2^{-1/2}`,
\[
\sum r^j=2+\sqrt2,
\qquad
\sum_{j\ge1}\sqrt j\,r^j
\le\frac12\left(\frac r{(1-r)^2}+\frac r{1-r}\right)
=\frac{5+4\sqrt2}{2}.
\]
Therefore
\[
S(y)\le C_*\sqrt{1+\log y},
\]
where
\[
C_*=(2+\sqrt2)\sqrt{8+8\pi\log(3/2)}
+\frac{5+4\sqrt2}{2}\sqrt{4\pi\log2}
=30.2876536044\ldots<30.3.
\]
Choosing `y=1` for `kappa<=1` and
\[
y=\kappa^{2/3}(1+\log\kappa)^{1/3}
\]
for `kappa>=1` gives
\[
\boxed{
\|p_Q\|_\infty
\le A D^{-1}\max\left\{1,\kappa^{2/3}(1+\log_+\kappa)^{1/3}\right\},
\quad
A=\frac1\pi+\frac{C_*}{\pi\sqrt2}=7.1354270657\ldots<7.14.
}\tag{E2}
\]
The completed report will verify the hypotheses, continuity, whole-copy collision integral, a target-valid stress test, and the exact fleet02/B03 theorem used at the selector inequality.
