# Quadratic forms with fragmented hub densities

## Abstract

An interval estimate for a quadratic form with one independent hub extends to countable interval majorants of the hub density. The resulting bound depends on the cube roots of the interval lengths, rather than their number or separation. It applies to some hub densities with infinite total variation and infinite first moment. We also formulate the exact measurable-set estimate needed to cover every bounded hub density. The unrestricted dimension-free quadratic-form density conjecture remains open.

## 1. Setting

Let $H,X_1,\ldots,X_m$ be independent real random variables with probability densities bounded by one. Let $w,v\in\mathbb R^m$ be orthonormal and assume

$$
w_i^2+v_i^2\le\tfrac12\qquad(1\le i\le m).
$$

Write $L=w\cdot X$, $V=v\cdot X$, and consider

$$
Q=2H(L+\beta)+\lambda V^2+2L(q\cdot X)
  +\sum_{i=1}^m(d_iX_i^2+b_iX_i+c_i),\qquad \lambda\ne0.
\tag{1.1}
$$

The coefficients $\beta,q,d_i,b_i,c_i$ are arbitrary. There is no quadratic term in $H$. Set

$$
C_* = \frac32(4\sqrt2\,\pi^2)^{2/3}
     =21.9116163581\ldots.
\tag{1.2}
$$

All measures below are positive. A density bound for a finite measure means an essential bound on its Radon–Nikodym derivative with respect to Lebesgue measure.

## 2. An interval estimate without probability normalization

**Lemma 2.1.** Replace the probability law of $H$ in (1.1) by the finite measure $\mathbf1_J(h)\,dh$, where $J$ is a bounded interval of length $D>0$. Denote the resulting output measure by $\nu_J$. Then

$$
\|p_{\nu_J}\|_\infty\le C_* (D/|\lambda|)^{1/3}.
\tag{2.1}
$$

The total mass of $\nu_J$ is $D$. In particular, the lemma also applies when $D<1$.

**Proof.** We first recall the slice estimate used in the interval argument. For fixed $a\in\mathbb R$, let $\mu_{a,\ell}$ be the unnormalized slice at $L=\ell$ of

$$
Y_a=\lambda V^2+2a(q\cdot X)+\sum_i(d_iX_i^2+b_iX_i+c_i).
$$

Its mass is $\rho_L(\ell)$. For almost every $\ell$, every real $t\ne0$, and every interval $B\subset\mathbb R$,

$$
|\widehat\mu_{a,\ell}(t)|
\le\min\{\rho_L(\ell),4\sqrt\pi\,|t\lambda|^{-1/2}\},
\qquad
\mu_{a,\ell}(B)\le2\pi^2\sqrt{|B|/|\lambda|}.
\tag{2.2}
$$

Here is the Fourier justification, including the role of the product law. For any complex $g_i$ dominated in modulus by the density of $X_i$, sharp Hausdorff–Young gives, for $p\ge2$,

$$
\int_{\mathbb R}|\widehat g_i(t)|^p\,dt
\le 2\pi\sqrt e\,p^{-1/2}<4\pi p^{-1/2}.
$$

The geometric Brascamp–Lieb inequality applied to the orthonormal two-frame $w,v$, with row weights $w_i^2+v_i^2\le1/2$, consequently gives

$$
\int_{\mathbb R^2}\prod_i
 |\widehat g_i(zw_i+uv_i+\theta_i)|\,dz\,du\le(4\pi)^2.
$$

Fresnel linearization of $\lambda V^2$, followed by Fourier inversion in $L$, proves the first inequality in (2.2). A squared-sinc majorant of an interval proves the second. The Fresnel identity can first be damped by a positive Gaussian; the displayed integrable majorant permits removal of the damping. These are applications of the Fourier inequalities in [1,2]. Absolute continuity of $L$ also follows from the projection theorem [3].

To use a slice estimate with $a=L$, partition the $L$-axis into cells of mesh $h$, freeze $a$ at one point in each cell, and then let $h\downarrow0$. There are only countably many frozen parameters at each stage. Moreover,

$$
Y_a-Y_L=2(a-L)(q\cdot X)\longrightarrow0
$$

almost surely, without any moment assumption. This avoids substituting directly into parameter-dependent exceptional slices.

Fix an output center $s$ and a radius $\delta>0$. For $u=\ell+\beta\ne0$, integration over the interval hub produces the window kernel

$$
G(\ell,y)=\frac{|(s-y+[-\delta,\delta])\cap 2uJ|}{2|u|}.
$$

For a frozen slice $\mu=\mu_{a,\ell}$, its integral has the three bounds

$$
\begin{aligned}
\int G\,d\mu&\le\frac\delta{|u|}\rho_L(\ell),\\
\int G\,d\mu&\le\frac\delta{|u|}\,2\pi^2
                  \sqrt{(2|u|D+2\delta)/|\lambda|},\\
\int G\,d\mu&\le2\pi^2D\sqrt{2\delta/|\lambda|}.
\end{aligned}
\tag{2.3}
$$

The first uses the total light-slice mass and the maximum possible window overlap. The second uses the interval supporting the window kernel. For the third, integrate in the hub coordinate first and apply (2.2) to an interval of length $2\delta$.

Use the first estimate on $|u|\ge T$. Since $\int\rho_L=1$, its contribution after division by $2\delta$ is at most $1/(2T)$. On $|u|<\delta$, the third estimate gives a term tending to zero. On $\delta\le|u|<T$, the second estimate and dominated convergence give

$$
\limsup_{\delta\downarrow0}
\frac{\nu_J([s-\delta,s+\delta])}{2\delta}
\le\frac1{2T}+4\sqrt2\,\pi^2\sqrt{DT/|\lambda|}.
\tag{2.4}
$$

The estimate is uniform in $s$. The freezing procedure above justifies the varying slice parameter. The finite-window bounds imply absolute continuity and the corresponding essential density bound. Minimize the right side using

$$
T=(4\sqrt2\,\pi^2)^{-2/3}(D/|\lambda|)^{-1/3}
$$

to obtain (2.1). The normalization used in the far-$u$ estimate was the unit mass of the light law. No unit-mass assumption on $\mathbf1_J(h)\,dh$ was used. \$\square$

## 3. Countable interval majorants

**Theorem 3.1.** Suppose the hub density admits an almost-everywhere majorant

$$
f_H(h)\le\sum_{j=1}^{\infty}a_j\mathbf1_{J_j}(h),
\qquad a_j\ge0,
\qquad
S:=\sum_{j=1}^{\infty}a_j|J_j|^{1/3}<\infty,
\tag{3.1}
$$

where the $J_j$ are bounded intervals. They may overlap and may have arbitrary locations. Then the form (1.1) has a bounded density and

$$
\boxed{\|p_Q\|_\infty\le C_*|\lambda|^{-1/3}S.}
\tag{3.2}
$$

**Proof.** For every bounded Borel set $B$, positivity, Tonelli's theorem, and Lemma 2.1 give

$$
\begin{aligned}
\mathbb P(Q\in B)
&\le\sum_j a_j\nu_{J_j}(B)\\
&\le C_*|\lambda|^{-1/3}|B|
       \sum_j a_j|J_j|^{1/3}.
\end{aligned}
$$

This directly proves absolute continuity and (3.2), including for the infinite sum. No uniform support radius or finite variation bound is required. \$\square$

The infimum of the sum in (3.1) over all such majorants may be used. The theorem also has the following integral version.

**Corollary 3.2.** Suppose there is a measurable interval decomposition, up to null sets,

$$
\{h:f_H(h)>t\}=\bigcup_j J_j(t),\qquad 0<t<1,
$$

with disjoint components, and

$$
\int_0^1\sum_j|J_j(t)|^{1/3}\,dt<\infty.
$$

Then

$$
\|p_Q\|_\infty
\le C_*|\lambda|^{-1/3}
\int_0^1\sum_j|J_j(t)|^{1/3}\,dt.
\tag{3.3}
$$

**Proof.** Apply Lemma 2.1 to every component and use the layer-cake identity $f_H(h)=\int_0^1\mathbf1_{\{f_H>t\}}(h)\,dt$ and Tonelli. \$\square$

If there are at most $k$ components at almost every level, Hölder and Jensen imply

$$
\int_0^1\sum_j|J_j(t)|^{1/3}dt
\le k^{2/3}
\left(\int_0^1\sum_j|J_j(t)|dt\right)^{1/3}
=k^{2/3}.
$$

Thus the explicit bound is $C_*k^{2/3}|\lambda|^{-1/3}$. The finite-component case is also accessible through a bounded-variation estimate. Theorem 3.1 continues to apply when the number of components and total variation are infinite.

## 4. An infinitely fragmented example

For $j\ge1$, set

$$
d_j=7\,8^{-j},\qquad J_j=[10^j,10^j+d_j],
\qquad f_H=\sum_{j\ge1}\mathbf1_{J_j}.
$$

The intervals are disjoint and

$$
\int f_H=\sum_{j\ge1}7\,8^{-j}=1,
\qquad
\sum_{j\ge1}d_j^{1/3}
=7^{1/3}\sum_{j\ge1}2^{-j}=7^{1/3}.
$$

The density has infinite total variation, because its first $N$ components already contribute variation $2N$. It has infinite first moment, since

$$
\mathbb E|H|\ge\sum_{j\ge1}10^j d_j
=7\sum_{j\ge1}(10/8)^j=\infty.
$$

Nevertheless, for every independent cap-one light law and every frame and coefficients satisfying Section 1,

$$
\boxed{\|p_Q\|_\infty
\le C_*7^{1/3}|\lambda|^{-1/3}
<41.916|\lambda|^{-1/3}.}
\tag{4.1}
$$

In particular, let $w,v,p$ be orthonormal, with $w_i^2+v_i^2\le1/2$, and write $P=p\cdot X$. The density bound $41.916$ holds for

$$
Q_\varepsilon=2HL+V^2+2\varepsilon LP
$$

for every real $\varepsilon$, uniformly in the ambient dimension and the light coordinate laws. Its quadratic matrix has nonzero eigenvalues $1,\sqrt{1+\varepsilon^2},-\sqrt{1+\varepsilon^2}$, so this is a normalized three-eigenvalue family.

## 5. The exact measurable-set endpoint

For fixed light laws and coefficients, and for $s\in\mathbb R,\delta>0$, define the nonnegative measurable function

$$
K_{s,\delta}(h)
=\frac{1}{2\delta}\mathbb P_X\bigl(|Q(h,X)-s|\le\delta\bigr).
$$

For every hub density $f$, independence gives the exact identity

$$
\frac{\mathbb P(|Q(H,X)-s|\le\delta)}{2\delta}
=\int_{\mathbb R}f(h)K_{s,\delta}(h)\,dh.
\tag{5.1}
$$

The elementary rearrangement principle for a nonnegative measurable function states

$$
\sup_{0\le f\le1,\,\int f=1}\int fK
=\sup_{|E|=1}\int_E K
=\int_0^1K^*(u)\,du,
\tag{5.2}
$$

where $K^*$ is its decreasing rearrangement. The equality is valid in the extended nonnegative reals; approximation by superlevel sets handles ties and absence of maximizers.

Consequently, a bound for (5.2) uniform in $s,\delta$, the admissible light laws, and the coefficients in the normalized hub family is exactly what is needed to cover every cap-one hub density. This formulation does not require a choice of conditional density versions.

The interval proof bounds the contribution of a union by a sum of cube roots of component lengths. For $N$ separated intervals of equal length $1/N$, that sum is $N^{2/3}$, which is not uniform. Therefore Theorem 3.1 does not settle (5.2).

An estimate of the stronger form

$$
\int_EK_{s,\delta}(h)\,dh\le C|E|^{1/3}
$$

for every measurable finite-measure $E$ would suffice, but the full hub question only requires the measure-one case in (5.2). Neither bound is proved here for arbitrary $E$. A general quadratic term in $H$, and the additional terms arising in arbitrary-matrix reductions, require further estimates.

## References

1. W. Beckner, *Inequalities in Fourier analysis*, Annals of Mathematics **102** (1975), 159–182. [DOI](https://doi.org/10.2307/1970980).
2. F. Barthe, *On a reverse form of the Brascamp–Lieb inequality*, Inventiones Mathematicae **134** (1998), 335–361. [arXiv:math/9705210](https://arxiv.org/abs/math/9705210).
3. G. Livshyts, G. Paouris and P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel Journal of Mathematics **216** (2016), 877–889. [arXiv:1507.07949](https://arxiv.org/abs/1507.07949).
