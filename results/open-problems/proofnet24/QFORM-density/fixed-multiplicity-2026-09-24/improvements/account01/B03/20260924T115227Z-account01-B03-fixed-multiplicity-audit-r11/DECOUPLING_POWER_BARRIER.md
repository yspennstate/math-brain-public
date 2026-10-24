# B03 improvement attempt: the leverage-free independent-copy power barrier

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T115227Z-account01-B03-fixed-multiplicity-audit-r11`  
Baseline source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **new exact method theorem / obstruction; no multiplicity reduction claimed.**

The baseline theorem uses a fourth-power independent-copy/BL estimate. The natural question for lowering 17 is whether a different power of the same decoupling can make order-four crossing volume integrable and hence yield a 13-eigenvalue theorem. The answer is negative for the entire leverage-free version of this mechanism: `q=2` is already the best allowable power under only cap-one coordinate densities and uniform scalar Fourier inputs.

## 1. General `q`-power determinant theorem

Let

`Z=F(X_I)+2 X_I^T M X_J+G(X_J)`

with `I,J` disjoint original-coordinate blocks, all coordinate densities bounded by one, and arbitrary measurable real `F,G`. Let `q>=2`. Then for every real `t`,

\[
\boxed{
 |\phi_Z(t)|
 \le
 \det\!\left(I+\frac{q t^2}{2\pi^2e^2}M^TM\right)^{-1/(4q)}.
}
\tag{1}
\]

For `q=2`, this is exactly the manuscript determinant theorem.

### Proof

The manuscript's two-copy step gives

\[
 |\phi_Z(t)|^2\le \mathbb E_D B(D),
 \qquad
 B(D)=\prod_{i\in I}|\widehat f_i(2t(MD)_i)|,
\]

where the coordinates of `D=X_J-X'_J` are independent and have densities `g_j<=1`. Since `q>=1`, Jensen gives

\[
 |\phi_Z(t)|^{2q}
 \le (\mathbb E B)^q
 \le \mathbb E B^q
 =\mathbb E_D\prod_i|\widehat f_i(2t(MD)_i)|^q.
\tag{2}
\]

Put `a=2t`, choose a regularizer `alpha>0`, and define

\[
 H=\alpha I+a^2M^TM,
\]

\[
 c_j=\alpha e_j^TH^{-1}e_j,
 \qquad
 d_i=a^2m_i^TH^{-1}m_i,
 \qquad
 \theta=\sum_i d_i=\sum_j(1-c_j),
\]

where `m_i` is the transpose of row `i` of `M`. As in the baseline proof, the vectors

\[
 \sqrt\alpha H^{-1/2}e_j,
 \qquad aH^{-1/2}m_i
\]

form a geometric rank-one frame. After `x=H^{-1/2}z`, geometric Brascamp--Lieb bounds the right side of (2) by

\[
 \det(H)^{-1/2}
 \prod_j\left[\alpha^{c_j/2}c_j^{-c_j/2}\|g_j\|_{1/c_j}\right]
 \prod_i\left[d_i^{-d_i/2}\|h_i\|_{1/d_i}\right],
\tag{3}
\]

where `h_i(u)=|fhat_i(u)|^q`. Since `g_j<=1` and has mass one,

\[
 \|g_j\|_{1/c_j}\le1.
\]

For a row with `d_i>0`, the scalar Fourier exponent is `p=q/d_i>=q>=2`; hence the manuscript scalar Fourier-power lemma gives

\[
\begin{aligned}
 \|h_i\|_{1/d_i}
 &=\left(\int|\widehat f_i(u)|^{q/d_i}\,du\right)^{d_i}\\
 &\le\left(2\pi\sqrt{\frac{2e d_i}{q}}\right)^{d_i}.
\end{aligned}
\tag{4}
\]

Thus the factors `d_i^{d_i/2}` cancel the scale factors in (3). Also

\[
 \prod_jc_j^{-c_j/2}\le e^{\theta/2}.
\]

Factoring `alpha` from the determinant, the total non-determinant multiplier in (3) is

\[
 \left(
 \frac{2\pi e\sqrt{2/q}}{\sqrt\alpha}
 \right)^\theta.
\]

Choose

\[
 \alpha=(2\pi e)^2\frac{2}{q}=\frac{8\pi^2e^2}{q}.
\tag{5}
\]

The multiplier is then exactly one, while

\[
 \frac{a^2}{\alpha}
 =\frac{q t^2}{2\pi^2e^2}.
\]

Therefore (2)--(5) give

\[
 |\phi_Z(t)|^{2q}
 \le
 \det\!\left(I+\frac{q t^2}{2\pi^2e^2}M^TM\right)^{-1/2}.
\]

Taking the `2q`th root proves (1). QED.

## 2. Consequence for crossing-volume exponents

Let `Z_k(M)` be the order-`k` crossing volume from the manuscript. Retaining only the `k`th coefficient in the determinant expansion in (1) gives

\[
 |\phi_Z(t)|
 \le
 C_{k,q}\,Z_k(M)^{-1/(4q)}|t|^{-k/(2q)}
 \quad(t\ne0),
\tag{6}
\]

with the explicit coefficient

\[
 C_{k,q}=\left(\frac{2\pi^2e^2}{q}\right)^{k/(4q)}.
\]

Hence absolute Fourier inversion from this envelope requires

\[
 \frac{k}{2q}>1,
 \qquad\text{i.e.}\qquad k>2q.
\tag{7}
\]

Because the leverage-free scalar input (4) requires `q>=2`, the best exponent in this family occurs at `q=2`:

\[
 \frac{k}{2q}\le\frac{k}{4}.
\tag{8}
\]

For `k=4`, the best possible tail supplied by this entire family is therefore exactly `|t|^{-1}`. Higher Jensen powers only make the decay exponent worse. Thus **changing from the fourth power to a higher independent-copy/Jensen power cannot turn the order-four crossing-volume branch into an `L^1` characteristic-function bound.**

This is a method theorem, not a theorem that a 13-eigenvalue result is impossible.

## 3. Why taking `q<2` is not a leverage-free repair

The formal computation above would be more favorable for `1<=q<2`, but then a BL row with leverage `d_i` close to one asks for a uniform scalar estimate of

\[
 \int|\widehat f(u)|^{p}\,du,
 \qquad p=q/d_i<2.
\]

Such a uniform estimate is false under only `0<=f<=1`, `int f=1`. Here is a self-contained witness.

Fix `1<=p<2`. For integer `N>=2`, define

\[
 f_N(x)=\sum_{j=1}^N\mathbf 1_{[3^j,\,3^j+1/N]}(x).
\tag{9}
\]

The intervals are disjoint, `0<=f_N<=1`, and `int f_N=1`. Write

\[
 \widehat f_N(t)=A_N(t)S_N(t),
\]

\[
 A_N(t)=\int_0^{1/N}e^{itu}\,du,
 \qquad
 S_N(t)=\sum_{j=1}^Ne^{i3^jt}.
\tag{10}
\]

For `0<=t<=N`, using `sin y >=2y/pi` for `0<=y<=1/2`,

\[
 |A_N(t)|=\frac{2|\sin(t/(2N))|}{t}\ge\frac{2}{\pi N}.
\tag{11}
\]

On one period with normalized Lebesgue measure, orthogonality gives

\[
 \mathbb E|S_N|^2=N.
\]

Moreover

\[
 \mathbb E|S_N|^4=2N^2-N\le2N^2.
\tag{12}
\]

Indeed, `3^a+3^b=3^c+3^d` has only the trivial unordered-pair solutions: uniqueness of base-three expansion distinguishes the case `a=b` (one digit equal to two) from `a!=b` (two digits equal to one).

Apply Paley--Zygmund to `Y=|S_N|^2`:

\[
 \mathbb P\{|S_N|^2\ge N/2\}
 \ge\frac{(1-1/2)^2(\mathbb EY)^2}{\mathbb EY^2}
 \ge\frac18.
\tag{13}
\]

Therefore each full `2pi` period contains a set of fixed positive measure on which

\[
 |S_N(t)|\ge\sqrt{N/2}.
\]

The interval `[0,N]` contains order `N` full periods. Combining this fact with (11), for all sufficiently large `N`,

\[
 \int_0^N|\widehat f_N(t)|^p\,dt
 \ge c_p N\,N^{-p}\,N^{p/2}
 =c_p N^{1-p/2}\longrightarrow\infty.
\tag{14}
\]

Thus

\[
\boxed{
 \sup_{0\le f\le1,\ \int f=1}
 \int_{\mathbb R}|\widehat f(t)|^pdt=\infty
 \quad\text{for every }1\le p<2.
}
\tag{15}
\]

Finally, BL row leverage can approach one in the actual determinant construction: for a rank-one crossing matrix with a single active row,

\[
 d(t)=\frac{a^2|m|^2}{\alpha+a^2|m|^2}\to1
 \qquad(|t|\to\infty).
\]

Hence for any fixed `q<2`, `q/d(t)<2` at sufficiently large `|t|`. The scalar step required by the same leverage-free BL mechanism then enters exactly the forbidden range (15).

So `q<2` cannot be justified by merely extending the manuscript's uniform scalar Fourier-power input. A different analytic mechanism that exploits more joint structure would be necessary.

## 4. Threshold consequence

The baseline interpolation proposition converts order `k` crossing volume into `4k-3` spectral directions. The first order that the present leverage-free absolute-Fourier receiver can integrate is `k=5`, hence `4*5-3=17`. Order `k=4` would correspond algebraically to `13` directions, but the best leverage-free copy/BL envelope in the family above is the endpoint `|t|^{-1}`.

Therefore this run establishes:

1. the manuscript's choice of the fourth power (`q=2`) is analytically optimal within this independent-copy/Jensen + geometric-BL + uniform scalar-Fourier-power scheme;
2. increasing the copy/Jensen power cannot lower 17;
3. decreasing it below `q=2` encounters a genuine failure of the required uniform scalar `L^p` Fourier input;
4. a valid `17 -> 13` improvement must use a new order-four endpoint argument, cancellation beyond absolute Fourier inversion, or a structural reduction not captured by this leverage-free determinant receiver.

No lower-multiplicity theorem is claimed in this artifact.
