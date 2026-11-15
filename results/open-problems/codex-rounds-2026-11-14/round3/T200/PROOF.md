# A capacity exponential moment and an explicit intersection-exponent bound

**Theorem.** With the starting points and normalization in the task,
\[
\xi_3(1,1)\leq 1-\frac{1}{495\log 3}
=0.998161132875501338598759110776\ldots
<0.99817.
\tag{1}
\]
The decimal evaluates the upper bound, not the exponent.

The new estimate is the conditional capacity exponential moment (10) below.
The hitting estimate and occupation-energy calculation are the ingredients
of the earlier T200 proof, based on Sections 2–4 of Runsheng Liu,
*An explicit lower bound for the growth exponent of three-dimensional
loop-erased random walk*, [arXiv:2609.18643v1](https://arxiv.org/html/2609.18643v1).
The required exponent inputs are existence of the moment limits and
\(\xi_3(1,2)=1\), as in the task. Existence is also recalled in Section 1.1 of
Yifan Gao, Xinyi Li, Yifan Li, Runsheng Liu, and Xiangyi Liu,
*A boundary Harnack principle and its application to analyticity of 3D Brownian
intersection exponents*, [arXiv:2411.14921](https://arxiv.org/abs/2411.14921).

## 1. A hitting estimate

Normalize Newtonian capacity by
\[
\operatorname{cap}(K)=\left[\inf_{\mu\in\mathcal P(K)}
\iint\frac{\mu(du)\mu(dv)}{|u-v|}\right]^{-1},
\]
with \(1/\infty=0\). Thus a closed ball of radius \(s\) has capacity \(s\).
For any compact \(K\subset\overline B(0,2r)\), and any \(|x|\leq r\),
\[
\mathbb P_x(H_K<\tau_{3r})\geq
\frac{2}{33r}\operatorname{cap}(K),
\tag{2}
\]
where \(H_K\) includes a hit at time zero and \(\tau_{3r}\) is the exit time
from \(B(0,3r)\).

Here is the potential calculation with this normalization. The Dirichlet
Green kernel in \(D=B(0,3r)\), with singularity \(|x-y|^{-1}\), is
\[
g_D(x,y)=\frac1d-\frac1{\sqrt{d^2+A}},\qquad
d=|x-y|,\quad
A=\frac{(9r^2-|x|^2)(9r^2-|y|^2)}{9r^2}.
\]
For \(|x|\leq r\), \(|y|\leq2r\), we have \(d\leq3r\) and
\(A\geq40r^2/9\). The displayed difference decreases in \(d>0\) and
increases in \(A>0\). Consequently
\[
g_D(x,y)\geq\frac1{3r}-\frac3{11r}=\frac2{33r}.
\tag{3}
\]
At coincident points the kernel is infinite.

For a positive-capacity compact set, its Green equilibrium measure has total
mass \(\operatorname{cap}_D(K)\) and Green potential
\(\mathbb P_x(H_K<\tau_{3r})\) outside \(K\). The variational definition of
relative capacity and \(g_D(u,v)\leq|u-v|^{-1}\) give
\(\operatorname{cap}_D(K)\geq\operatorname{cap}(K)\). Integration of (3)
against this measure proves (2) for \(x\notin K\). If the capacity is zero,
(2) is immediate. If \(x\in K\), its left side is one, whereas its right
side is at most \(4/33\), by capacity monotonicity and
\(\operatorname{cap}(\overline B(0,2r))=2r\). This covers all starting points.

## 2. The conditional capacity exponential moment

Let \(W\) be standard Brownian motion in \(\mathbb R^3\), started at zero,
with filtration \(\mathcal F^W\), and let \(\sigma_s\) be its first hit of
\(\partial B(0,s)\). Define
\[
K(r)=W[\sigma_r,\sigma_{2r}],\qquad
C(r)=\frac{\operatorname{cap}(K(r))}{r},\qquad t=\frac{r^2}{18}.
\]
These sets are compact almost surely, and \(0\leq C(r)\leq2\).
Condition on \(\mathcal F^W_{\sigma_r}\). The process
\(V_u=W_{\sigma_r+u}-W_{\sigma_r}\) is an independent standard Brownian
motion started at zero. Write \(\Delta=\sigma_{2r}-\sigma_r\).

On \(\{\Delta<t\}\), the displacement of \(W\) from its position at
\(\sigma_r\) reaches at least \(r\) by time \(t\). For \(0\leq u\leq t\),
\[
Y_u=\exp\left(\frac{15|V_u|^2}{2r^2}\right)
\]
is a nonnegative submartingale, by convexity. It is integrable through time
\(t\), since \(15t/r^2=5/6<1\). Doob's maximal inequality and the Gaussian
exponential-moment formula yield
\[
\mathbb P(\Delta<t\mid\mathcal F^W_{\sigma_r})
\leq e^{-15/2}\mathbb E Y_t
=6\sqrt6\,e^{-15/2}=:p_*.
\tag{4}
\]

Use the unrestricted continuation of \(W\) to form the probability measure
\[
\mu_t=\frac1t\int_0^t\delta_{W_{\sigma_r+u}}\,du,
\qquad I_t=\iint\frac{\mu_t(dx)\mu_t(dy)}{|x-y|}.
\]
For \(u\ne v\), Gaussian radial integration, with \(s=|u-v|\), gives
\[
\mathbb E|V_u-V_v|^{-1}
=\frac{4\pi}{(2\pi s)^{3/2}}
\int_0^\infty \rho e^{-\rho^2/(2s)}\,d\rho
=\sqrt{2/\pi}\,s^{-1/2}.
\]
The diagonal of \([0,t]^2\) has Lebesgue measure zero. Tonelli's theorem gives
\[
\begin{aligned}
\mathbb E[I_t\mid\mathcal F^W_{\sigma_r}]
&=\frac{2\sqrt{2/\pi}}{t^2}
\int_0^t(t-v)v^{-1/2}\,dv\\
&=\frac83\sqrt{2/\pi}\,t^{-1/2}
=\frac{16}{r\sqrt\pi}.
\end{aligned}
\tag{5}
\]
Thus \(I_t\) is finite almost surely. It is positive, since the occupation
measure is a probability measure supported on a compact set and the kernel
is strictly positive.

For every \(s>0\), \(y>0\),
\[
e^{-s/y}\leq\frac{y}{es}.
\tag{6}
\]
Indeed, putting \(z=s/y\), this is \(ze^{-z}\leq e^{-1}\), whose left side
has its maximum at \(z=1\).

On \(A=\{\Delta\geq t\}\), the measure \(\mu_t\) is supported on \(K(r)\).
The variational definition therefore gives
\(C(r)\geq1/(rI_t)\). On \(A^c\) use \(e^{-sC(r)}\leq1\).
Combining these pointwise bounds with (6),
\[
e^{-sC(r)}\leq \mathbf1_{A^c}+\frac{rI_t}{es}.
\tag{7}
\]
There is no conditioning on \(A\) in (5) and no independence assertion about
\(A\) and \(I_t\). Taking conditional expectations in (7) proves the
general estimate
\[
\mathbb E[e^{-sC(r)}\mid\mathcal F^W_{\sigma_r}]
\leq p_*+\frac{16}{es\sqrt\pi}.
\tag{8}
\]

For a simple explicit certificate, use
\[
\sqrt6<\frac52,\quad e^{15/2}>1800,\quad
\sqrt\pi>\frac{177}{100},\quad e>\frac{27}{10}.
\]
Section 6 verifies all transcendental comparisons. At \(s=30\), they give
\[
p_*+\frac{16}{30e\sqrt\pi}
<\frac1{120}+\frac{1600}{14337}
=\frac{68779}{573480}
<\frac3{25}.
\tag{9}
\]
The margin in the last comparison is \(193/2867400\). In particular,
uniformly in the starting position at \(\sigma_r\),
\[
\boxed{\mathbb E[e^{-30C(r)}\mid\mathcal F^W_{\sigma_r}]<\frac3{25}.}
\tag{10}
\]

## 3. A lower tail for the sum of capacities

Fix \(N\geq1\), set \(r_j=3^j\) for \(0\leq j<N\), and \(R=3^N\).
Let \(K_j=K(r_j)\), \(C_j=C(r_j)\), and
\(T_N=\sum_{j=0}^{N-1}C_j\). Each \(K_j\) is part of
\(W[0,\sigma_R]\), since \(2r_j<3r_j\leq R\). Moreover \(C_j\) is
measurable at \(\sigma_{2r_j}\), which precedes \(\sigma_{r_{j+1}}\).
Earlier \(C_i\) are thus measurable when conditioning on
\(\mathcal F^W_{\sigma_{r_j}}\). Iterating (10) gives
\[
\mathbb E e^{-30T_N}\leq(3/25)^N.
\tag{11}
\]
This iteration uses conditional bounds, not independence of the layers.

By Markov's inequality and \(e<11/4\),
\[
\mathbb P(T_N<N/30)
\leq e^N\mathbb E e^{-30T_N}
\leq(3e/25)^N\leq(33/100)^N=R^{-b},
\quad b=\frac{\log(100/33)}{\log3}>1.
\tag{12}
\]
The last strict inequality is the integer comparison \(100>99\).
The threshold \(N/30\) need not be an integer.

## 4. Avoidance given the obstacle path

Let \(X\) be an independent standard Brownian motion started at \((1,0,0)\),
and let \(\tau_s\) be its first hit of \(\partial B(0,s)\), with
\(\tau_1=0\). Define
\[
Q_R(W)=\mathbb P\bigl(X[0,\tau_R]\cap W[0,\sigma_R]=\varnothing
\mid W[0,\sigma_R]\bigr).
\]
Fix the stopped obstacle path, so that the \(K_j\) and \(C_j\) are now
deterministic. At \(\tau_{r_j}\), (2) and the strong Markov property of \(X\)
give a conditional probability at least \((2/33)C_j\) to hit \(K_j\)
before \(\tau_{r_{j+1}}\), for every possible position on
\(\partial B(0,r_j)\).

Let \(A_j\) be the event that
\(X[\tau_{r_j},\tau_{r_{j+1}}]\) avoids \(K_j\). Every earlier \(A_i\) is
measurable at \(\tau_{r_j}\). Full avoidance implies all the \(A_j\), so
iterating the preceding conditional probability bound gives
\[
Q_R(W)\leq\prod_{j=0}^{N-1}(1-(2/33)C_j)
\leq\exp\left(-\frac2{33}T_N\right).
\tag{13}
\]
All factors are nonnegative since \(C_j\leq2\). The first-hitting-time
segments can return inward; no confinement in annuli is assumed. The bound
also covers a test position already in \(K_j\), when local avoidance has
probability zero.

On \(G_N=\{T_N\geq N/30\}\), (13) implies
\[
Q_R\leq e^{-N/495}=R^{-\delta},\qquad
\delta=\frac1{495\log3}.
\]
Using \(Q_R^2\leq R^{-\delta}Q_R\) on \(G_N\), and \(Q_R^2\leq1\)
elsewhere, (12) gives
\[
\mathbb E Q_R^2\leq R^{-\delta}\mathbb E Q_R+R^{-b},\qquad b>1.
\tag{14}
\]

## 5. Passage to intersection exponents

Couple all radii using the same whole obstacle path. The conditional
avoidance probability decreases as the radius increases: the obstacle trace
grows and the test path must avoid it for longer. Its moments therefore
decrease as well. Bracketing any real log-radius between neighboring integers
extends the exponent limits in the task to arbitrary radii, in particular
\(R=3^N\). Thus
\[
\mathbb E Q_R^2=R^{-1+o(1)},\qquad
\mathbb E Q_R=R^{-\xi_3(1,1)+o(1)}.
\tag{15}
\]
Fix \(0<\varepsilon<b-1\). For all sufficiently large \(N\),
\(\mathbb E Q_R^2\geq R^{-1-\varepsilon}\) and
\(R^{-b}\leq\tfrac12R^{-1-\varepsilon}\). Rearranging (14) gives
\[
\mathbb E Q_R\geq\tfrac12R^{-1+\delta-\varepsilon}.
\]
Taking logarithms, dividing by \(-\log R\), and passing to the exponent
limit yields \(\xi_3(1,1)\leq1-\delta+\varepsilon\). Letting
\(\varepsilon\downarrow0\) proves the first inequality of (1).

Finally, \(\log3<11/10\), so
\[
\delta>\frac2{1089}>\frac{183}{100000}.
\]
The last comparison follows from \(200000>183\cdot1089=199287\).
Therefore \(\xi_3(1,1)<99817/100000=0.99817\), proving (1).

## 6. Exact certificates and independent numerical checks

The command
```
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py moment
```
checks the rational inequalities above and independently evaluates the
constants. The certificates are as follows.

First, the positive Taylor sum through degree 30 at \(15/2\) is greater than
1800, and the sum through degree 6 at \(11/10\) is greater than 3. These prove
the two exponential comparisons. For \(e\), its fourth Taylor sum is
\(65/24>27/10\). Bounding the tail starting at \(1/5!\) by a geometric series
of ratio \(1/6\) gives
\[
e<\frac{65}{24}+\frac{1/120}{1-1/6}
=\frac{1631}{600}<\frac{11}{4}.
\]

For the pi estimate, half the perimeter of an inscribed regular 48-gon in the
unit circle gives
\[
\pi>48\sin(\pi/48)
=24\sqrt{2-\sqrt{2+\sqrt{2+\sqrt3}}}.
\]
The strict inequality follows from \(\sin x<x\) for \(x>0\). Set
\[
a=1.73206,\quad b=1.931855,\quad c=1.982891,\quad d=0.1308.
\]
Exact squaring gives
\(a^2>3\), \(b^2>2+a\), \(c^2>2+b\), and \(d^2<2-c\).
Consequently the last displayed nested radical exceeds \(24d=1962/625\),
which exceeds \((177/100)^2\). This proves \(\sqrt\pi>177/100\).

Rational bounds for \(\log3\) use
\[
\log x=2\sum_{j=0}^{n-1}\frac{z^{2j+1}}{2j+1}+E_n,\quad
z=\frac{x-1}{x+1},\quad
0<E_n\leq\frac{2z^{2n+1}}{(2n+1)(1-z^2)},\quad x>1.
\]
At \(x=3\), \(n=100\), this certifies
\[
0.0018388671244986614012408892237093070719447193075862863529824284107
<\delta<
0.0018388671244986614012408892237093070719447193075862863529824284176,
\]
where the displayed endpoints are rounded decimal presentations of the
rational interval; the script compares the exact rational endpoints.
Decimal logarithms with pi calculated through Machin's identity, and a
separate double-precision evaluation, provide independent numerical checks.
The decimal presentations are not needed for the proof.

The conditional exponential moment (10), its layer iteration, and (14) use
no assertion about the typical value of capacity or an independent-layer
model. The only discarded event has the explicit exponent \(b>1\).
