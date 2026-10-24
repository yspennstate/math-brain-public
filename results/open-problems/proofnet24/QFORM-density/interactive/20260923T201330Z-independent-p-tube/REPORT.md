# Dyadic quadratic tube bounds when \(P\) is independent of \((L,V)\)

**Scope.** This note proves a curved tube estimate for an independent-\(P\) subclass of the QFORM high-leverage model. It applies when \((L,V)\) have any joint density bounded by \(M\), \(P\) is independent of that pair, and \(P\) has density at most one. It permits arbitrary dependence between \(L\) and \(V\). It does **not** settle the general two-bank product-source case, where \(P\) may correlate with \(L,V\).

Let
\[
F(l,v)=-c-dl-\frac{\gamma+v^2}{2l},
\qquad R_r=\{l:r\leq |l|\leq2r\},
\]
where \(r,a>0\), \(c,d\in\mathbb R\), and \(|\gamma|\geq1\). Let \(E_{r,a}=\{L\in R_r,\ |P-F(L,V)|\leq a\}\). Restricting \(V\) to any additional interval can only reduce this event.

## Results

**Theorem 1 (both signs, fractional gain).** For each \(q>2\) there is a constant \(C_q\), independent of \(r,a,c,d,\gamma,M\), such that
\[
\mathbb P(E_{r,a})\leq C_q M\,a\,r^{\,2-1/q}.
\]
Thus this independent-\(P\) subclass satisfies the proposed \(C_\alpha M a r^{1+\alpha}\) estimate for every \(1/2<\alpha<1\), with \(\alpha=1-1/q\). The estimate remains true with no restriction on \(V\).

**Theorem 2 (elliptic sign).** If \(\gamma>0\), then the stronger endpoint estimate holds:
\[
\mathbb P(E_{r,a})\leq 160M\,a\,r^2/\sqrt{\gamma}.
\]
The constant \(160\) is only a convenient explicit choice. The estimates are uniform under the affine shear \(dL\) and translation \(c\).

The independent-\(P\) hypothesis is compatible with the two-bank Gram condition: each bank may contain separate physical coordinates for the \(L,V,P\) directions, each with half the frame energy. The argument does not extend to a correlated \(P\) merely from two-bank nondegeneracy.

## Reduction to a Lebesgue pushforward

Let \(m\) be the (possibly infinite at isolated critical values) density of the pushforward of two-dimensional Lebesgue measure \(\mathbf1_{R_r}(l)\,dl\,dv\) under \(F\). The measure is locally finite, and the arguments below show \(m\in L^q(\mathbb R)\) for every \(q>2\). For any interval \(J\), the corresponding pushforward \(m_J\) with \(v\in J\) satisfies \(0\leq m_J\leq m\).

If \(f_{L,V}\leq M\), \(P\) is independent of \((L,V)\), and \(f_P\leq1\), then
\[
\begin{aligned}
\mathbb P(E_{r,a})
&\leq M\int_{\mathbb R}f_P(p)
       \int_{p-a}^{p+a}m(u)\,du\,dp\\
&\leq 2Ma\,\|f_P\|_{q'}\|m\|_q
 \leq 2Ma\,\|m\|_q,\qquad q'=\frac q{q-1}.
\end{aligned}
\]
The second line applies Hölder to each translated copy of \(m\); the last uses \(f_P\leq1\) and \(\int f_P=1\). For Theorem 2 one may instead use \(2Ma\|m\|_\infty\).

## Proof of Theorem 1

We prove the quantitative analytic lemma
\[
\|m\|_q\leq C_q r^{\,2-1/q}
\quad\text{for every }q>2,\quad |\gamma|\geq1. \tag{1}
\]
To justify Fourier transforms despite unrestricted \(v\), first insert the Gaussian cutoff \(e^{-\varepsilon v^2}\), \(\varepsilon>0\), and call the resulting finite pushforward density \(m_\varepsilon\). With the convention \(\widehat m(t)=\int e^{-itp}m(p)\,dp\), the elementary complex Gaussian integral gives
\[
\widehat m_\varepsilon(t)
=\sqrt\pi\int_{R_r}
  e^{\,it(c+dl+\gamma/(2l))}
  \bigl(\varepsilon-it/(2l)\bigr)^{-1/2}\,dl. \tag{2}
\]
The square root is chosen continuously from positive real \(\varepsilon\). All subsequent bounds concern its modulus, so the sign convention does not matter.

Set \(A_{\varepsilon,t}(l)=\sqrt\pi(\varepsilon-it/(2l))^{-1/2}\). For \(t\neq0\) and \(l\in R_r\),
\[
|A_{\varepsilon,t}(l)|\leq C\sqrt{\frac{|l|}{|t|}},
\qquad
|A'_{\varepsilon,t}(l)|
 \leq \frac{C}{|l|}\sqrt{\frac{|l|}{|t|}},
\]
uniformly in \(\varepsilon\). Integrating the first inequality directly on the two components of \(R_r\) yields
\[
|\widehat m_\varepsilon(t)|
 \leq C r^{3/2}|t|^{-1/2}. \tag{3}
\]

On either component of \(R_r\), the real phase
\(\phi(l)=t(c+dl+\gamma/(2l))\) has
\[
|\phi''(l)|=\frac{|t\gamma|}{|l|^3}
 \geq \frac{|t\gamma|}{8r^3}.
\]
The weighted second-derivative van der Corput estimate, together with
\[
\sup_{R_r}|A_{\varepsilon,t}|
 +\int_{R_r}|A'_{\varepsilon,t}(l)|\,dl
 \leq C\sqrt{r/|t|},
\]
therefore gives the second bound
\[
|\widehat m_\varepsilon(t)|
 \leq C\frac{r^2}{|t|\sqrt{|\gamma|}}
 \leq C r^2|t|^{-1}. \tag{4}
\]
The two intervals making up \(R_r\) are handled separately. Crucially, the affine coefficients \(c,d\) disappear from the second derivative.

For \(q>2\), put \(q'=q/(q-1)\in(1,2)\). Integrate (3) over \(|t|\leq r\) and (4) over \(|t|\geq r\):
\[
\begin{aligned}
\|\widehat m_\varepsilon\|_{q'}^{q'}
&\leq C_{q'}
 \left[r^{3q'/2}\int_0^r t^{-q'/2}\,dt
       +r^{2q'}\int_r^\infty t^{-q'}\,dt\right]\\
&\leq C_{q'}r^{q'+1}.
\end{aligned}
\]
Both integrals converge precisely because \(1<q'<2\). The inverse Hausdorff–Young inequality consequently gives
\(\|m_\varepsilon\|_q\leq C_q r^{1+1/q'}=C_q r^{2-1/q}\), uniformly in \(\varepsilon\). Finally \(m_\varepsilon\uparrow m\) as \(\varepsilon\downarrow0\); Fatou proves (1), and the reduction above proves Theorem 1.

## Proof of Theorem 2: explicit quadratic-root lemma

We use the following one-dimensional lemma.

**Lemma.** If \(G>0\) and \(Q(t)=-G+At+Bt^2\) with arbitrary real \(A,B\), then
\[
\int_1^2 \frac{\mathbf1_{\{Q(t)>0\}}}{\sqrt{Q(t)}}\,dt
 \leq \frac{10}{\sqrt G}. \tag{5}
\]

Here is a complete root-case proof. If \(B>0\), \(Q(0)<0\) forces real roots \(-u<0<t_+\). On its positive part of \([1,2]\),
\[
Q(t)=G(t/t_+-1)(1+t/u)\geq G(t/t_+-1).
\]
If \(t_+\geq2\) the integral is zero; otherwise integration gives at most
\[
\frac{2}{\sqrt G}\sqrt{t_+(2-\max\{1,t_+\})}
 \leq \frac2{\sqrt G}.
\]
If \(B=0\), only \(A>0\) can contribute, and the same computation with the single positive root \(t_+=G/A\) applies.

If \(B<0\), positivity on \([1,2]\) requires two positive roots \(0<t_1<t_2\), with \(t_1<2\) and \(t_2>1\). Then
\[
Q(t)=G(t/t_1-1)(1-t/t_2)
     =\frac{G}{t_1t_2}(t-t_1)(t_2-t).
\]
There are four cases.

- If \(t_1\geq1/2\) and \(t_2\leq4\), integration over the entire positive-root interval is \(\pi\sqrt{t_1t_2/G}\leq\pi\sqrt8/\sqrt G<9/\sqrt G\).
- If \(t_1<1/2\) and \(t_2\leq4\), the first displayed factor is at least one for \(t\in[1,2]\). Integration of the remaining inverse square root is at most \(2t_2/\sqrt G\leq8/\sqrt G\).
- If \(t_1\geq1/2\) and \(t_2>4\), the second displayed factor is at least \(1/2\) on \([1,2]\); the same positive-root integral as in the convex case gives at most \(2\sqrt2/\sqrt G\).
- If \(t_1<1/2\) and \(t_2>4\), both factors are at least \(1\) and \(1/2\), respectively, so the integral is at most \(\sqrt2/\sqrt G\).

If a concave \(Q\) has no positive interval intersecting \([1,2]\), the integral is zero. This covers double roots and roots outside the integration interval, establishing (5).

For each \(p\), solving \(p=F(l,v)\) gives
\[
v^2=D_p(l):=-\gamma-2(c+p)l-2dl^2.
\]
The two roots \(v=\pm\sqrt{D_p(l)}\) contribute the Jacobian \(2|l|/\sqrt{D_p(l)}\). For either sign of \(l\), write \(l=\pm rt\), \(1\leq t\leq2\). Then \(D_p(\pm rt)\) is a quadratic in \(t\) whose constant term is \(-\gamma\). When \(\gamma>0\), applying (5), using \(t\leq2\), and summing both signs yields
\[
m(p)
 =\sum_{\pm}2r^2\int_1^2
   \frac{t\,\mathbf1_{\{D_p(\pm rt)>0\}}}
        {\sqrt{D_p(\pm rt)}}\,dt
 \leq 80r^2/\sqrt\gamma .
\]
The \(L^\infty\) reduction gives
\(\mathbb P(E_{r,a})\leq2Ma\|m\|_\infty
 \leq160Ma r^2/\sqrt\gamma\), as claimed.

## Remaining gap

The proof of Theorem 1 extracts curvature through a signed Fresnel integral and obtains a uniform \(L^q\) bound for the geometric pushforward \(m\). The final Hölder step uses \(P\) independent of \((L,V)\). For a general product projection of original coordinates, \(P\) can depend strongly on \(L,V\), even when the frame splits into two nondegenerate independent banks. No bound of the required form has been established here for that correlated case.


## Affine-regression extension

The independence hypothesis permits an affine dependence of \(P\) on \((L,V)\). Suppose
\[
P=\alpha L+\beta V+Z,
\]
where \(Z\) is independent of \((L,V)\), has density at most \(K\), and the joint density of \((L,V)\) is at most \(M\). Put \(V'=V+\beta L\). The shear \((l,v)\mapsto(l,v+\beta l)\) has Jacobian one, so the joint density of \((L,V')\) is still at most \(M\), while \(Z\) remains independent of that pair. Also
\[
P+c+dL+\frac{\gamma+V^2}{2L}
=Z+c+\left(d+\alpha-\frac{\beta^2}{2}\right)L
  +\frac{\gamma+(V')^2}{2L}.
\]
Hence Theorems 1 and 2 apply with an extra factor \(K\): the both-sign bound is \(C_qMK a r^{2-1/q}\), and the \(\gamma>0\) bound is \(160MK a r^2/\sqrt\gamma\).

This includes all jointly Gaussian \((L,V,P)\) whose covariance matrix is bounded below by \(\sigma_0^2 I_3\). Gaussian regression provides such a residual \(Z\), with variance
\(\inf_{\alpha,\beta}\operatorname{Var}(P-\alpha L-\beta V)\geq\sigma_0^2\), so \(K\leq(2\pi\sigma_0^2)^{-1/2}\); the \((L,V)\) density is at most \((2\pi\sigma_0^2)^{-1}\). For orthonormal-frame projections of independent Gaussian originals each having density at most one, their original variances are at least \(1/(2\pi)\), and hence \(\sigma_0^2\geq1/(2\pi)\). This remains a Gaussian or independent-residual subclass, rather than a solution for arbitrary fragmented product laws.


## Endpoint logarithmic estimate for either sign

The proof of Theorem 1 also gives a uniform logarithmic bound:
\[
\boxed{\ \mathbb P(E_{r,a})
 \leq C M a r^2\bigl(1+\log_+(1/r)\bigr),
 \qquad |\gamma|\geq1.\ } \tag{6}
\]
For an affine-regression residual \(Z\) of density at most \(K\), multiply the right side by \(K\).

To see the constant dependence, retain the denominators when integrating (3) and (4). For \(q\geq3\), \(q'=q/(q-1)\), the inverse Hausdorff–Young constants are bounded uniformly over \(q'\in(1,3/2]\), while
\[
\|\widehat m_\varepsilon\|_{q'}
 \leq C r^{2-1/q}
 \left(\frac1{1-q'/2}+\frac1{q'-1}\right)^{1/q'}
 \leq Cq\,r^{2-1/q}.
\]
The first denominator stays bounded and \(q'-1=1/(q-1)\). Fatou again yields
\(\|m\|_q\leq Cq\,r^{2-1/q}\). The Hölder reduction then bounds the tube probability by \(CMa q r^{2-1/q}\).

For \(0<r\leq e^{-3}\), choose \(q=\log(1/r)\), so \(q\geq3\) and \(r^{-1/q}=e\). For \(r\geq e^{-3}\), take \(q=3\) and use \(r^{5/3}\leq e r^2\) on \([e^{-3},1]\) and \(r^{5/3}\leq r^2\) on \([1,\infty)\). These cases prove (6). The elliptic sign \(\gamma>0\) has the stronger log-free Theorem 2.


## Sharpness of the logarithm on the hyperbolic side

The logarithm in (6) is necessary when \(\gamma<0\), even for mutually independent cap-one \(L,V,P\) and an affine shear chosen with \(r\). Here is an explicit example. Let \(0<r<1/32\), \(\gamma=-1\), \(l_0=3r/2\),
\[
d=-\frac{1}{2l_0^2},\qquad c=\frac1{l_0}.
\]
Then the surface function simplifies exactly to
\[
F(l,v)=\frac{(l-l_0)^2/l_0^2-v^2}{2l}.
\]
Take \(L\) uniform with density one on
\([r,2r]\cup[2,3-r]\), whose total length is one, and take \(V,P\) independent uniform on \([-1/2,1/2]\). For \(l=l_0(1+x)\), set \(u=x+v\), \(w=x-v\). Then
\[
F(l,v)=\frac{uw}{2l},\qquad
dl\,dv=\frac{l_0}{2}\,du\,dw.
\]
For \(|u|,|w|\leq h:=1/8\), the resulting \(l\) lies in \([r,2r]\) and \(|v|\leq1/2\). If also \(|uw|\leq r/2\), then \(l\geq r\) gives \(|F(l,v)|\leq1/4\). For any \(0<a\leq1/4\), the conditional probability over \(P\) of \(|P-F(l,v)|\leq a\) is exactly \(2a\). The \((u,w)\)-area of this region is
\[
4\left[\int_0^{r/(2h)}h\,du
      +\int_{r/(2h)}^h\frac{r}{2u}\,du\right]
=2r\left[1+\log\left(\frac{2h^2}{r}\right)\right].
\]
Consequently
\[
\mathbb P(E_{r,a})
 \geq 2a\cdot\frac{l_0}{2}\cdot
 2r\left[1+\log\left(\frac{2h^2}{r}\right)\right]
 =3a r^2\left[1+\log\left(\frac1{32r}\right)\right].
\]
For small \(r\) this is a constant multiple of \(a r^2\log(1/r)\), proving that the endpoint logarithm cannot be removed under the independent-\(P\) hypotheses when \(\gamma<0\). The construction is a test of that scoped tube theorem, not a counterexample to the QFORM density conjecture.
