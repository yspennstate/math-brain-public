# Optimal deterministic time weights for a capacity estimate

For standard Brownian motion and the normalization in the question,

\[
\xi_3(1,1)\leq 1-\frac{2}{957\log3}
=0.998097723664311729584923218044\ldots<0.9981.
\tag{1}
\]

The decimal is an evaluation of the upper bound. The exact exponent is not
determined. The new ingredient is an exact minimization of the expected
energy of a deterministic weighted occupation measure. Segment radii, layer
spacing and time cutoff are the same as in the earlier T200 argument.

The probabilistic inputs about intersection exponents are existence of the
moment limits in the question and the known identity \(\xi_3(1,2)=1\).
The capacity and layer method follows Sections 2–4 of Runsheng Liu,
*An explicit lower bound for the growth exponent of three-dimensional
loop-erased random walk*, [arXiv:2609.18643v1](https://arxiv.org/html/2609.18643v1).
The earlier T200 proof supplied its conditional exponential-moment form.

## 1. The time-energy problem

For a probability measure \(\rho\) on \([0,1]\), set

\[
\mathcal E(\rho)=\iint_{[0,1]^2}|u-v|^{-1/2}\rho(du)\rho(dv),
\]

allowing infinity, and write
\(B(a,b)=\int_0^1 v^{a-1}(1-v)^{b-1}\,dv\), for \(a,b>0\).
Define the probability measure

\[
\rho_*(du)=\frac{[u(1-u)]^{-1/4}}{B(3/4,3/4)}\,du.
\tag{2}
\]

Then

\[
\min_{\rho\in\mathcal P([0,1])}\mathcal E(\rho)
=\mathcal E(\rho_*)
=J:=\frac{\pi\sqrt2}{B(3/4,3/4)}<\frac{21}{8}.
\tag{3}
\]

### Constant potential, including the endpoints

Put

\[
L(x)=\int_0^x(x-v)^{-1/2}[v(1-v)]^{-1/4}\,dv,
\qquad 0<x<1.
\]

Use the rising factorial \((a)_0=1\),
\((a)_n=a(a+1)\cdots(a+n-1)\). The binomial expansion
\((1-v)^{-a}=\sum_{n\geq0}(a)_n v^n/n!\), with positive terms,
and Tonelli's theorem give

\[
L(x)=\sum_{n\geq0}\frac{(1/4)_n}{n!}
x^{n+1/4}B(n+3/4,1/2).
\tag{4}
\]

The beta recurrence \(B(a+1,b)=aB(a,b)/(a+b)\) follows by integrating
the derivative of \(v^a(1-v)^b\) and using
\(B(a,b)=B(a+1,b)+B(a,b+1)\). Thus

\[
B(n+3/4,1/2)=B(3/4,1/2)\frac{(3/4)_n}{(5/4)_n},
\qquad \frac{(1/4)_n}{(5/4)_n}=\frac1{4n+1}.
\]

Substitute in (4), and integrate the positive binomial series for
\((1-z)^{-3/4}\), to obtain

\[
L(x)=\frac{B(3/4,1/2)}4
\int_0^x[z(1-z)]^{-3/4}\,dz.
\tag{5}
\]

The unnormalized potential at \(x\) is \(L(x)+L(1-x)\), by substituting
\(v\mapsto1-v\) in its right-hand part. The integrand in (5) is symmetric
about \(1/2\). Therefore this sum is independent of \(x\in(0,1)\).

As \(x\downarrow0\), (5) gives \(L(x)\to0\). To compute the other limit,
substitute \(v=xt\) into the defining integral for \(L(x)\):

\[
L(x)=x^{1/4}\int_0^1t^{-1/4}(1-t)^{-1/2}(1-xt)^{-1/4}\,dt.
\]

Monotone convergence as \(x\uparrow1\) gives
\(L(x)\to B(3/4,1/4)\). Direct integration at an endpoint gives the same
beta integral. Consequently the potential is constant on the closed
interval, equal to \(B(1/4,3/4)\).

Here is an elementary evaluation. Substitute \(v=t/(1+t)\), followed by
\(t=z^4\), to get

\[
B(1/4,3/4)=\int_0^\infty\frac{t^{-3/4}}{1+t}\,dt
=4\int_0^\infty\frac{dz}{1+z^4}=\pi\sqrt2.
\tag{6}
\]

For the last integral, let \(I=\int_0^\infty(1+z^4)^{-1}\,dz\).
The substitution \(z=1/w\) gives
\(I=\int_0^\infty z^2/(1+z^4)\,dz\). Hence

\[
2I=\frac12\int_0^\infty\left(
\frac1{z^2+\sqrt2z+1}+\frac1{z^2-\sqrt2z+1}\right)dz.
\]

The two denominators are \((z\pm1/\sqrt2)^2+1/2\).
Their integrals are respectively
\(\sqrt2(\pi/2-\pi/4)\) and
\(\sqrt2(\pi/2+\pi/4)\). Thus \(2I=\pi/\sqrt2\), proving (6).
After division by \(B(3/4,3/4)\), the potential of \(\rho_*\) is \(J\)
everywhere. In particular \(\mathcal E(\rho_*)=J<\infty\).

### Global minimality

The kernel \(|x-y|^{-1/2}\) has nonnegative energy on every finite signed
measure of finite absolute energy. To verify this, for \(a>0\) write

\[
a^{-1/2}=\frac1{\sqrt\pi}\int_0^\infty t^{-1/2}e^{-ta}\,dt.
\tag{7}
\]

The identity follows from \(w=ta\) and
\(\int_0^\infty w^{-1/2}e^{-w}dw=\sqrt\pi\), the Gaussian integral.
For each \(t>0\),

\[
e^{-t|x-y|}=2t\int_{-\infty}^{\min(x,y)}
e^{-t(x-z)}e^{-t(y-z)}\,dz.
\]

Consequently, for a finite signed measure \(\nu\),

\[
\iint e^{-t|x-y|}\nu(dx)\nu(dy)
=2t\int_{\mathbb R}\left(\int_{[z,\infty)}e^{-t(x-z)}\nu(dx)\right)^2dz
\geq0.
\tag{8}
\]

Fubini here is justified by replacing \(\nu\) with \(|\nu|\): the
bounded exponential kernel has integral at most \(|\nu|(\mathbb R)^2\).
For finite absolute Riesz energy, Fubini also permits integration of (8)
against \(t^{-1/2}/\sqrt\pi\); (7) then proves nonnegative Riesz energy.

Take any probability \(\rho\) of finite energy. The mixed energy of
\(\rho\) and \(\rho_*\) is \(J\), because the latter's potential is
constant everywhere. Since \(|\rho-\rho_*|\leq\rho+\rho_*\), the difference
has finite absolute energy. Expanding its nonnegative energy gives

\[
0\leq\mathcal E(\rho-\rho_*)
=\mathcal E(\rho)-2J+J=\mathcal E(\rho)-J.
\]

Infinite-energy probabilities already satisfy this lower bound. This proves
the minimizing assertion in (3), over all probability time measures.

## 2. Rational certification of the energy constant

Symmetry and the positive binomial series on \([0,1/2]\) give

\[
B(3/4,3/4)=2^{1/4}S,
\qquad
S=\sum_{n=0}^\infty\frac{(1/4)_n}{n!\,2^n(n+3/4)}.
\tag{9}
\]

The first eight terms exceed \(178/125\); this is a finite rational
comparison checked in `audit.py weighted`. Also \(\pi<22/7\), since

\[
0<\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx=\frac{22}7-\pi.
\]

Indeed polynomial division gives quotient
\(x^6-4x^5+5x^4-4x^2+4\) and remainder \(-4\); integrate and use
\(\arctan1=\pi/4\). Since \(J^4=2\pi^4/S^4\), the rational comparison

\[
2(22/7)^4<(21/8)^4(178/125)^4
\tag{10}
\]

proves the last assertion in (3). All quantities are positive, so fourth
powers preserve the comparison.

## 3. Brownian energy and the conditional capacity moment

Normalize Newtonian capacity by

\[
\operatorname{cap}(K)=
\left[\inf_{\mu\in\mathcal P(K)}\iint|x-y|^{-1}\mu(dx)\mu(dy)\right]^{-1}.
\]

A radius-\(r\) ball then has capacity \(r\). Let \(W\) start at zero,
\(\sigma_r\) be its first hit of radius \(r\), and put

\[
K(r)=W[\sigma_r,\sigma_{2r}],\quad
C(r)=\operatorname{cap}(K(r))/r,\quad t=r^2/18.
\]

Condition on \(\mathcal F^W_{\sigma_r}\). Its continuation
\(V_u=W_{\sigma_r+u}-W_{\sigma_r}\) is an independent standard Brownian
motion. With \(\Delta=\sigma_{2r}-\sigma_r\), the event \(\Delta<t\)
requires a displacement of at least \(r\) by time \(t\). The convex
function \(\exp(15|V_u|^2/(2r^2))\) is an integrable nonnegative
submartingale up to \(t\). Doob's inequality and the Gaussian square
moment therefore give

\[
\mathbb P(\Delta<t\mid\mathcal F^W_{\sigma_r})
\leq e^{-15/2}(1-15t/r^2)^{-3/2}
=6\sqrt6e^{-15/2}=:p_*<1/120.
\tag{11}
\]

The final bound uses \(\sqrt6<5/2\) and \(e^{15/2}>1800\).
The latter follows by summing its positive Taylor series through degree 30.

Use the unrestricted continuation to define the probability measure

\[
\mu_t=\int_0^1\delta_{W_{\sigma_r+tu}}\rho_*(du),
\qquad I_t=\iint|x-y|^{-1}\mu_t(dx)\mu_t(dy).
\]

For \(u\ne v\), radial Gaussian integration gives

\[
\mathbb E|V_{tu}-V_{tv}|^{-1}
=\frac{4\pi}{(2\pi t|u-v|)^{3/2}}
\int_0^\infty z e^{-z^2/(2t|u-v|)}dz
=\sqrt{2/\pi}\,t^{-1/2}|u-v|^{-1/2}.
\]

The time measure has no atoms, so its product gives zero mass to the
diagonal. Tonelli and (3) imply

\[
\mathbb E[rI_t\mid\mathcal F^W_{\sigma_r}]
=\frac6{\sqrt\pi}J<\frac{63}{4\sqrt\pi}.
\tag{12}
\]

In particular \(I_t\) is finite almost surely. It is positive: its
probability measure has compact support and the kernel is strictly positive.
More generally, replacing \(\rho_*\) by any deterministic probability
time measure gives expected energy \(\sqrt{2/\pi}\,t^{-1/2}\mathcal E(\rho)\),
with infinite values allowed. Atoms give infinite energy on the diagonal.
Thus (2) minimizes expected energy within this full deterministic class.

On \(A=\{\Delta\geq t\}\), the weighted measure lies in \(K(r)\), so
\(C(r)\geq1/(rI_t)\). For \(s,y>0\),

\[
e^{-s/y}\leq y/(es),
\tag{13}
\]

because \(ze^{-z}\leq e^{-1}\) at \(z=s/y\). On \(A^c\), bound
\(e^{-sC(r)}\) by one. Pointwise, therefore,

\[
e^{-sC(r)}\leq\mathbf1_{A^c}+\frac{rI_t}{es}.
\]

No independence of the energy and exit event is used. Taking conditional
expectations gives

\[
\mathbb E[e^{-sC(r)}\mid\mathcal F^W_{\sigma_r}]
\leq p_*+\frac{6J}{es\sqrt\pi}.
\tag{14}
\]

The elementary bounds \(e>65/24\), \(e<68/25\), and
\(\sqrt\pi>177/100\) are certified below. At \(s=29\), (14) yields

\[
\mathbb E[e^{-29C(r)}\mid\mathcal F^W_{\sigma_r}]
<\frac1{120}+\frac{63/4}{29(65/24)(177/100)}
=\frac{324643}{2669160}<\frac{11}{90}.
\tag{15}
\]

The last margin is \(4763/8007480>0\).

## 4. Capacity layers and the exceptional tail

Let \(r_j=3^j\), \(R=3^N\),
\(C_j=C(r_j)\), and \(T_N=\sum_{j=0}^{N-1}C_j\).
Each \(C_j\) is measurable at \(\sigma_{2r_j}\), which precedes
\(\sigma_{r_{j+1}}\). Iterating (15), conditioning from the last layer
backwards, gives

\[
\mathbb E e^{-29T_N}\leq(11/90)^N.
\]

Markov's inequality and \(e<68/25\) give

\[
\mathbb P(T_N<N/29)
\leq e^N\mathbb E e^{-29T_N}
\leq(374/1125)^N=R^{-b},
\quad b=\frac{\log(1125/374)}{\log3}>1.
\tag{16}
\]

The strict comparison follows from \(3\cdot374=1122<1125\).
No independent-layer assertion or integer threshold is required.

## 5. Hitting and avoidance

For compact \(K\subset\overline B(0,2r)\) and \(|x|\leq r\),

\[
\mathbb P_x(H_K<\tau_{3r})\geq\frac2{33r}\operatorname{cap}(K).
\tag{17}
\]

Here \(H_K\) includes a hit at time zero. To check the normalization,
the ball's Dirichlet Green kernel with singularity \(|x-y|^{-1}\) is

\[
g(x,y)=d^{-1}-(d^2+A)^{-1/2},\quad d=|x-y|,
\quad A=\frac{(9r^2-|x|^2)(9r^2-|y|^2)}{9r^2}.
\]

For the indicated radii \(d\leq3r\) and \(A\geq40r^2/9\).
The difference decreases in \(d>0\) and increases in \(A>0\), hence
\(g(x,y)\geq1/(3r)-3/(11r)=2/(33r)\).
At coincident points it is infinite.

For a positive-capacity compact set, its Green equilibrium measure in the
ball has total mass \(\operatorname{cap}_{B(0,3r)}(K)\) and potential
\(\mathbb P_x(H_K<\tau_{3r})\) outside \(K\). Since the Green kernel is
bounded above by the Newtonian kernel, its variational capacity is at least
\(\operatorname{cap}(K)\). Integrating the kernel lower bound proves (17)
outside \(K\). For zero capacity (17) is immediate. If \(x\in K\), the
left side is one and the right side is at most \(4/33\), because
\(\operatorname{cap}(K)\leq2r\). This covers all starting points.

Let \(X\) be an independent Brownian motion starting at \((1,0,0)\), with
first hitting times \(\tau_s\), including \(\tau_1=0\). Define

\[
Q_R(W)=\mathbb P\{X[0,\tau_R]\cap W[0,\sigma_R]=\varnothing
\mid W[0,\sigma_R]\}.
\]

Condition on the whole stopped obstacle path. Each \(K(r_j)\) is part
of it, since \(2r_j<R\). At time \(\tau_{r_j}\), (17) and the strong
Markov property of \(X\) bound the probability of avoiding \(K(r_j)\)
until \(\tau_{r_{j+1}}\) by \(1-(2/33)C_j\), uniformly over the current
position. The earlier local avoidance events are measurable at this time.
Full avoidance implies all local avoidance events, so successive
conditioning gives

\[
Q_R\leq\prod_{j=0}^{N-1}(1-(2/33)C_j)
\leq e^{-(2/33)T_N}.
\tag{18}
\]

All factors are nonnegative since \(0\leq C_j\leq2\). This argument
allows inward returns of \(X\); it requires no annular confinement.
An initial hit only makes the local avoidance probability zero.

On \(T_N\geq N/29\), (18) implies

\[
Q_R\leq R^{-\delta},\qquad \delta=\frac2{957\log3}.
\]

Using \(Q_R^2\leq R^{-\delta}Q_R\) on this event and \(Q_R^2\leq1\)
on its complement, (16) proves

\[
\mathbb E Q_R^2\leq R^{-\delta}\mathbb E Q_R+R^{-b},\qquad b>1.
\tag{19}
\]

## 6. The exponent comparison

Couple all radii with the whole obstacle path. Increasing the radius
enlarges the obstacle trace and lengthens the test trajectory, so \(Q_R\)
and its moments decrease. Bracketing a real log-radius between adjacent
integers transfers the moment limits in the question to all radii,
including \(R=3^N\). The assumed exact second-moment exponent gives

\[
\mathbb E Q_R^2=R^{-1+o(1)},\qquad
\mathbb E Q_R=R^{-\xi_3(1,1)+o(1)}.
\]

For \(0<\varepsilon<b-1\), and all sufficiently large \(N\),
\(\mathbb E Q_R^2\geq R^{-1-\varepsilon}\) and
\(R^{-b}\leq\tfrac12R^{-1-\varepsilon}\). Rearranging (19) gives

\[
\mathbb E Q_R\geq\tfrac12 R^{-1+\delta-\varepsilon}.
\]

Taking the exponent limit yields
\(\xi_3(1,1)\leq1-\delta+\varepsilon\); then let
\(\varepsilon\downarrow0\). This proves the first inequality of (1).
For the simple strict decimal bound, \(\log3<1099/1000\) implies

\[
\delta>\frac{2000}{1051743}>\frac{19}{10000},
\]

since \(20000000>19\cdot1051743=19983117\). Thus
\(\xi_3(1,1)<0.9981\).

## 7. Remaining scalar certificates and numerical checks

The fourth Taylor sum for \(e\) is \(65/24\), strictly below \(e\).
The tail starting with \(1/5!\) has subsequent ratios at most \(1/6\),
so \(e<65/24+(1/120)/(1-1/6)=1631/600<68/25\).
The positive Taylor sum for \(e^{1099/1000}\) through degree six exceeds three,
proving \(\log3<1099/1000\). The analogous sum through degree 30 at \(15/2\)
exceeds 1800, as used in (11).

For \(\sqrt\pi>177/100\), define
\(A_n(x)=\sum_{j=0}^{n-1}(-1)^j x^{2j+1}/(2j+1)\).
Alternating-series bounds give

\[
\pi>16A_8(1/5)-4A_5(1/239)>(177/100)^2.
\]

The first inequality uses Machin's identity
\(\pi=16\arctan(1/5)-4\arctan(1/239)\).
To verify the identity, double-angle formulas give
\(\tan(2\alpha)=5/12\) and \(\tan(4\alpha)=120/119\) for
\(\alpha=\arctan(1/5)\). Subtracting \(\arctan(1/239)\) gives tangent
one and an angle in \((0,\pi/2)\), hence angle \(\pi/4\).
The remaining comparison is rational.

Run `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py weighted`.
Every numerical inequality used for (1) is certified by rational arithmetic.
The script also bounds \(\log3\) using the positive atanh series with its
geometric remainder, evaluates the constants separately with Decimal
arithmetic, computes beta integrals by a second half-interval series, and
checks the final gap against a libm evaluation.

The exact optimum \(J=2.6220575542921198\ldots\) is about 1.67% below
the uniform-time energy \(8/3\). At fixed time cutoff \(r^2/18\), no
deterministic time measure improves this expected-energy constant further.
The exit estimate and the scalar inequality (13) still lose information;
the result makes no optimality claim for the full capacity-moment method.
