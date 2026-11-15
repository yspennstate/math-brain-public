# A radial exit estimate for the Brownian capacity argument

For standard Brownian motion with generator \(\tfrac12\Delta\), and the
intersection-exponent normalization in the question,

\[
\boxed{\displaystyle
\xi_3(1,1)\leq 1-\frac{2}{627\log3}
=0.997096525592896850419093332804\ldots<0.9971.}
\tag{1}
\]

The decimal evaluates an upper bound, not the exponent. The exponent inputs
are existence of the moment limits in the question and
\(\xi_3(1,2)=1\). The capacity argument follows Sections 2–4 of Runsheng
Liu, *An explicit lower bound for the growth exponent of three-dimensional
loop-erased random walk*, [arXiv:2609.18643v1](https://arxiv.org/html/2609.18643v1),
and the preceding T200 proofs. The extension here is the radial exit-time
estimate and its use with the weighted occupation measure of round 4.
The exact exponent and the general moment family are not determined.

## 1. An exit-time identity

Let \(W\) be a three-dimensional Brownian motion starting at a point of
radius 1, and let \(\tau\) be its first exit from \(B(0,2)\). Let
\(\eta\) be the first exit from \((-1,1)\) of a one-dimensional standard
Brownian motion starting at zero. Then

\[
\tau\ \stackrel{\mathrm{law}}=\ \eta.
\tag{2}
\]

Here is a direct verification. For \(q>0\), put \(a=\sqrt{2q}\) and
define, for \(0<|x|\leq2\),

\[
f_q(x)=\frac{2\sinh(a|x|)}{|x|\sinh(2a)},
\qquad f_q(0)=\frac{2a}{\sinh(2a)}.
\]

The series for \(\sinh(a|x|)/|x|\) is a convergent power series in
\(|x|^2\), so the apparent singularity at zero is removable and the
function is smooth there. The radial Laplacian
\(f''(s)+2f'(s)/s\) shows that
\(\tfrac12\Delta f_q=qf_q\), including at zero by continuity.
Its boundary value on radius 2 is 1.

The process \(e^{-q(t\wedge\tau)}f_q(W_{t\wedge\tau})\) has constant
expectation by Itô's formula. All coefficients are bounded on the closed
ball for each fixed q; thus the stopped stochastic integral has mean zero.
Also \(\tau<\infty\) almost surely. Indeed the martingale
\(|W_t|^2-3t\), stopped at \(t\wedge\tau\), gives

\[
\mathbb E(t\wedge\tau)
=\frac{\mathbb E|W_{t\wedge\tau}|^2-1}{3}\leq1.
\]

Monotone convergence gives \(\mathbb E\tau\leq1\). Bounded convergence
in the stopped formula therefore gives

\[
\mathbb E e^{-q\tau}=f_q(W_0)
=\frac{2\sinh a}{\sinh(2a)}=\frac1{\cosh a}.
\tag{3}
\]

For the one-dimensional motion, \(h_q(y)=\cosh(ay)/\cosh a\) satisfies
\(h_q''/2=qh_q\) on \((-1,1)\) and has boundary value 1.
The same stopped Itô formula gives
\(\mathbb E e^{-q\eta}=h_q(0)=1/\cosh a\).
Its exit time is finite by stopping the martingale \(B_t^2-t\).

Equality of these transforms implies equality of laws. To see the
uniqueness explicitly, apply the equality at positive integer q to
the random variables \(e^{-\tau},e^{-\eta}\in[0,1]\). They have all the
same positive integer moments, and their zeroth moments are both one.
Polynomial approximation of continuous functions on \([0,1]\) implies
that their distributions coincide. Neither variable has mass at zero,
since the exit times are finite; applying \(-\log\) proves (2).

For a motion starting at zero, write \(\sigma_r\) for its first hit of
radius r and \(\Delta_r=\sigma_{2r}-\sigma_r\). The strong Markov
property, Brownian scaling and rotational invariance now imply that,
conditionally on \(\mathcal F_{\sigma_r}\),

\[
\Delta_r/r^2\ \stackrel{\mathrm{law}}=\ \eta.
\tag{4}
\]

## 2. A certified short-time bound

Write \(\overline\Phi(x)=(2\pi)^{-1/2}\int_x^\infty e^{-z^2/2}\,dz\).
Reflection for the upper and lower one-dimensional barriers, followed by
a union bound, gives for every \(u>0\)

\[
\mathbb P(\eta\leq u)
\leq\mathbb P(\sup_{s\leq u}B_s\geq1)
 +\mathbb P(\inf_{s\leq u}B_s\leq-1)
=4\overline\Phi(1/\sqrt u).
\tag{5}
\]

A rational upper bound for this Gaussian tail is convenient. For \(x>0\),
set

\[
R(x)=e^{x^2/2}\int_x^\infty e^{-z^2/2}\,dz,
\quad P(x)=x^4+9x^2+8,
\quad Q(x)=x^5+10x^3+15x,
\quad U(x)=P(x)/Q(x).
\]

Differentiation gives \(R'=xR-1\). Direct polynomial multiplication gives

\[
P'Q-PQ'-xPQ+Q^2=-120,
\qquad U'-xU+1=-120/Q^2.
\tag{6}
\]

The simple estimate
\(\int_x^\infty e^{-z^2/2}dz\leq
x^{-1}\int_x^\infty z e^{-z^2/2}dz\)
gives \(R(x)\leq1/x\). Since \(U(x)\sim1/x\),
\(e^{-x^2/2}(U(x)-R(x))\to0\) as \(x\to\infty\).
Subtract the differential equations and integrate from x to infinity:

\[
U(x)-R(x)
=120e^{x^2/2}\int_x^\infty\frac{e^{-z^2/2}}{Q(z)^2}\,dz>0.
\tag{7}
\]

At \(x=\sqrt7\),
\(U(x)=120/(134\sqrt7)=60/(67\sqrt7)\). Therefore (4)–(7) give

\[
\begin{aligned}
\mathbb P(\Delta_r<r^2/7\mid\mathcal F_{\sigma_r})
&\leq4\overline\Phi(\sqrt7)\\
&<\frac{240e^{-7/2}}{67\sqrt{14\pi}}
<p:=\frac{16311}{1000000}.
\end{aligned}
\tag{8}
\]

The last comparison has a finite rational certificate in Section 6.
The reflection bound is about 0.0163019431870; the rational Mills bound
before rounding is about 0.0163104821074. The union bound in (5) need not
be an equality.

## 3. Weighted occupation energy

Use Newtonian capacity with kernel \(|x-y|^{-1}\):

\[
\operatorname{cap}(K)=\left[
\inf_{\mu\in\mathcal P(K)}\iint |x-y|^{-1}\mu(dx)\mu(dy)
\right]^{-1},\qquad 1/\infty=0.
\tag{9}
\]

A radius-r ball has capacity r. Let

\[
K(r)=W[\sigma_r,\sigma_{2r}],\quad
C(r)=\operatorname{cap}(K(r))/r,\quad
t=r^2/7.
\]

Let \(B(a,b)=\int_0^1v^{a-1}(1-v)^{b-1}\,dv\), and use the
deterministic probability time measure

\[
\rho(du)=\frac{[u(1-u)]^{-1/4}}{B(3/4,3/4)}\,du.
\tag{10}
\]

Its time energy is

\[
\iint |u-v|^{-1/2}\rho(du)\rho(dv)
=J:=\frac{\pi\sqrt2}{B(3/4,3/4)}<\frac{21}{8}.
\tag{11}
\]

For completeness, this is the time-energy identity from round 4. Define
\(L(x)=\int_0^x(x-v)^{-1/2}[v(1-v)]^{-1/4}dv\) for \(0<x<1\).
The positive binomial series and the beta recurrence give

\[
\begin{aligned}
L(x)
&=\sum_{n\geq0}\frac{(1/4)_n}{n!}
x^{n+1/4} B(n+3/4,1/2)\\
&=B(3/4,1/2)\sum_{n\geq0}
\frac{(3/4)_n x^{n+1/4}}{n!(4n+1)}\\
&=\frac{B(3/4,1/2)}4
\int_0^x[z(1-z)]^{-3/4}dz.
\end{aligned}
\tag{12}
\]

Here \((a)_0=1\), \((a)_n=a(a+1)\cdots(a+n-1)\).
The beta recurrence follows by integrating the derivative of
\(v^a(1-v)^b\); it gives
\(B(n+3/4,1/2)=B(3/4,1/2)(3/4)_n/(5/4)_n\), while
\((1/4)_n/(5/4)_n=1/(4n+1)\).
All series terms and integrands in (12) are nonnegative, so Tonelli
justifies the integrations. The unnormalized potential is
\(L(x)+L(1-x)\), hence is constant by symmetry of the final integrand.
As \(x\downarrow0\), \(L(x)\to0\). Substituting \(v=xz\) in the
definition of L and taking \(x\uparrow1\) by monotone convergence gives
\(L(x)\to B(3/4,1/4)\). Direct endpoint integration gives this same
potential value at 0 and 1.

The substitutions \(v=w/(1+w)\), \(w=z^4\) give

\[
B(1/4,3/4)=4\int_0^\infty\frac{dz}{1+z^4}=\pi\sqrt2.
\]

To evaluate the last integral, its value I is unchanged when its integrand
is replaced by \(z^2/(1+z^4)\), by \(z\mapsto1/z\). Hence

\[
2I=\frac12\int_0^\infty\left[
\frac1{z^2+\sqrt2z+1}+\frac1{z^2-\sqrt2z+1}
\right]dz=\frac\pi{\sqrt2},
\]

where completing the squares evaluates the two terms as
\(\sqrt2(\pi/2-\pi/4)\) and \(\sqrt2(\pi/2+\pi/4)\).
Dividing the constant potential by \(B(3/4,3/4)\) proves the identity
in (11), then integrating against \(\rho\) proves its energy value.

For its rational upper bound, expand on \([0,1/2]\) and use symmetry:

\[
B(3/4,3/4)=2^{1/4}S,\qquad
S=\sum_{n\geq0}\frac{(1/4)_n}{n!\,2^n(n+3/4)}.
\]

Its first eight terms have sum
\(112206509213551/78752847495168>178/125\).
The identity
\(22/7-\pi=\int_0^1 x^4(1-x)^4/(1+x^2)\,dx>0\)
gives \(\pi<22/7\). For example, polynomial division of the integrand
has quotient \(x^6-4x^5+5x^4-4x^2+4\) and remainder \(-4\).
Finally the rational inequality

\[
2(22/7)^4<(21/8)^4(178/125)^4
\]

and \(J^4=2\pi^4/S^4\) prove \(J<21/8\).
All quantities are positive, so taking fourth powers preserves order.

Condition on \(\mathcal F_{\sigma_r}\) and use the unrestricted
Brownian continuation to form

\[
\mu_t=\int_0^1\delta_{W_{\sigma_r+tu}}\rho(du),
\qquad I_t=\iint |x-y|^{-1}\mu_t(dx)\mu_t(dy).
\]

The time measure has no atoms. For \(u\ne v\), the Brownian increment
has covariance \(t|u-v|I_3\), so radial Gaussian integration gives

\[
\mathbb E|W_{\sigma_r+tu}-W_{\sigma_r+tv}|^{-1}
=\frac{4\pi}{(2\pi t|u-v|)^{3/2}}
\int_0^\infty z e^{-z^2/(2t|u-v|)}dz
=\sqrt{2/\pi}\,t^{-1/2}|u-v|^{-1/2}.
\]

The diagonal in time has zero product measure. Tonelli and (11) give

\[
\mathbb E[rI_t\mid\mathcal F_{\sigma_r}]
=\sqrt{14/\pi}\,J
<A:=\frac{27707}{5000}.
\tag{13}
\]

The finite expectation shows that \(I_t\) is finite almost surely.
It is strictly positive, since its probability measure has compact
support and the kernel is strictly positive. Section 6 certifies the last
bound using \(J<21/8\).

On \(\{\Delta_r\geq t\}\), \(\mu_t\) is supported on \(K(r)\), and
(9) gives \(C(r)\geq1/(rI_t)\). For \(y,s>0\),

\[
e^{-s/y}\leq \frac{y}{es},
\]

since \((s/y)e^{-s/y}\leq1/e\). On \(\{\Delta_r<t\}\), use only
\(e^{-sC(r)}\leq1\). Combining the two events pointwise gives

\[
e^{-sC(r)}\leq\mathbf1_{\{\Delta_r<t\}}+\frac{rI_t}{es}.
\]

Thus no independence of the energy and exit event is needed, and (8),
(13) imply

\[
\mathbb E[e^{-sC(r)}\mid\mathcal F_{\sigma_r}]
\leq p+\frac{A}{es}.
\tag{14}
\]

At \(s=17\), using \(e>67957/25000\) yields the particular bound

\[
\mathbb E[e^{-17C(r)}\mid\mathcal F_{\sigma_r}]
<\frac{157378592659}{1155269000000}
<m:=\frac{13623}{100000}.
\tag{15}
\]

## 4. Layers and hitting probabilities

Let \(r_j=3^j\), \(R=3^N\),
\(C_j=C(r_j)\), and \(T_N=\sum_{j=0}^{N-1}C_j\).
Each \(C_j\) is measurable at \(\sigma_{2r_j}\), preceding
\(\sigma_{r_{j+1}}\). Conditioning from the last layer backwards in
(15) gives

\[
\mathbb E e^{-17T_N}\leq m^N.
\]

This uses conditional bounds, not independent layers. Markov's inequality,
at the real threshold \(N/19\), gives

\[
\begin{aligned}
\mathbb P(T_N<N/19)
&\leq(e^{17/19}m)^N\leq\beta^N=R^{-b},\\
\beta&:=\frac{24467}{10000}\frac{13623}{100000}
=\frac{333313941}{1000000000}<\frac13,\qquad
b=-\frac{\log\beta}{\log3}>1.
\end{aligned}
\tag{16}
\]

The bound \(e^{17/19}<24467/10000\) is certified in Section 6.
The strict tail comparison follows from the integer inequality
\(3\cdot333313941=999941823<1000000000\).

For the hitting step, for every compact
\(K\subset\overline B(0,2r)\) and \(|x|\leq r\),

\[
\mathbb P_x(H_K<\tau_{3r})\geq
\frac{2\operatorname{cap}(K)}{33r}.
\tag{17}
\]

Here \(H_K\) allows a hit at time zero. To check the constant, the
Dirichlet Green kernel in \(B(0,3r)\), normalized to have singularity
\(|x-y|^{-1}\), is

\[
g(x,y)=\frac1d-\frac1{\sqrt{d^2+D}},\quad d=|x-y|,\quad
D=\frac{(9r^2-|x|^2)(9r^2-|y|^2)}{9r^2}.
\]

For the indicated radii, \(d\leq3r\) and \(D\geq40r^2/9\).
The displayed kernel decreases with d and increases with D. Its minimum
is therefore at least \(1/(3r)-3/(11r)=2/(33r)\).
Coincident points have infinite kernel and cause no exception.

For positive capacity and \(x\notin K\), the usual Green equilibrium
measure has potential \(\mathbb P_x(H_K<\tau_{3r})\) and total mass
\(\operatorname{cap}_{B(0,3r)}(K)\). These identities with this
normalization are also given in Liu, Section 2. The variational definition
and \(g(x,y)\leq |x-y|^{-1}\) imply that this relative capacity is at
least \(\operatorname{cap}(K)\). Integrating the kernel lower bound proves
(17). At zero capacity the bound is trivial. If \(x\in K\), its left
side is one and the right side is at most \(4/33\), since
\(\operatorname{cap}(K)\leq2r\). Thus (17) holds in all cases.

Let X be an independent Brownian motion starting at \((1,0,0)\), with
first hitting times \(\tau_s\) of radius s, including \(\tau_1=0\).
Condition on the entire stopped obstacle path and write

\[
Q_R=\mathbb P\{X[0,\tau_R]\cap W[0,\sigma_R]=\varnothing
\mid W[0,\sigma_R]\}.
\]

The compact sets \(K(r_j)\) are now fixed, and each is contained in
\(W[0,\sigma_R]\), since \(2r_j<r_{j+1}\leq R\).
At \(\tau_{r_j}\), (17) bounds the probability of avoiding \(K(r_j)\)
until \(\tau_{r_{j+1}}\) by \(1-(2/33)C_j\), for every position on
radius \(r_j\). The earlier such local avoidance events are measurable
at \(\tau_{r_j}\). Full avoidance implies all the local events, so the
strong Markov property of X, successively applied, gives

\[
Q_R\leq\prod_{j=0}^{N-1}(1-(2/33)C_j)
\leq\exp\bigl(-(2/33)T_N\bigr).
\tag{18}
\]

All factors are nonnegative because \(0\leq C_j\leq2\).
This first-hitting-time argument allows inward returns and initial hits;
it puts no annular confinement on X and no conditioning on its future.

## 5. Comparison of the first and second moments

On \(\{T_N\geq N/19\}\), (18) gives
\(Q_R\leq R^{-\delta}\), where

\[
\delta=\frac{2}{33\cdot19\log3}=\frac{2}{627\log3}.
\]

On this event \(Q_R^2\leq R^{-\delta}Q_R\), and on its complement
\(Q_R^2\leq1\). Thus (16) gives

\[
\mathbb E Q_R^2\leq R^{-\delta}\mathbb E Q_R+R^{-b},\qquad b>1.
\tag{19}
\]

When all radii are coupled using the same whole obstacle path, \(Q_R\)
is nonincreasing with R: the obstacle trace and the test path both grow.
Bracketing real log-radii between adjacent integers transfers the moment
limits in the question to all radii, including \(R=3^N\). Therefore

\[
\mathbb E Q_R^2=R^{-1+o(1)},\qquad
\mathbb E Q_R=R^{-\xi_3(1,1)+o(1)}.
\]

Fix \(0<\varepsilon<b-1\). For sufficiently large N the second-moment
asymptotic gives \(\mathbb E Q_R^2\geq R^{-1-\varepsilon}\),
and \(R^{-b}\leq\tfrac12 R^{-1-\varepsilon}\). Rearranging (19) yields

\[
\mathbb E Q_R\geq\tfrac12 R^{-1+\delta-\varepsilon}.
\]

The exponent limit implies
\(\xi_3(1,1)\leq1-\delta+\varepsilon\). Letting
\(\varepsilon\downarrow0\) proves (1)'s non-strict bound.
For its rounded strict form, \(\log3<1099/1000\) implies

\[
\delta>\frac{2000}{689073}>\frac{29}{10000},
\]

since \(20000000>29\cdot689073=19983117\). Thus
\(\xi_3(1,1)<0.9971\).

## 6. Finite certificates and independent checks

Define rational sums

\[
E_n(x)=\sum_{j=0}^n\frac{x^j}{j!},\qquad
A_n(x)=\sum_{j=0}^{n-1}\frac{(-1)^j x^{2j+1}}{2j+1}.
\]

Positive Taylor terms give \(e^x>E_n(x)\), for x positive. If
\(x<n+2\), the omitted successive ratios are at most \(x/(n+2)\), so

\[
e^x<E_n(x)+\frac{x^{n+1}/(n+1)!}{1-x/(n+2)}.
\tag{20}
\]

Machin's identity and alternating-series bounds give

\[
\pi>16A_8(1/5)-4A_5(1/239)>\pi_0:=\frac{314159}{100000}.
\tag{21}
\]

For the identity, if \(\alpha=\arctan(1/5)\), double-angle formulas
give \(\tan(2\alpha)=5/12\), \(\tan(4\alpha)=120/119\), and
\(\tan(4\alpha-\arctan(1/239))=1\). The angle is in \((0,\pi/2)\),
hence it is \(\pi/4\).

The finite rational comparisons used in (8), (13), (15), (16) are

\[
\begin{gathered}
E_{24}(7/2)>h:=662309/20000,\\
p^2\,67^2\,14\pi_0 h^2>240^2,\qquad
(27707/5000)^2\pi_0>14(21/8)^2,\\
E_{10}(1)>67957/25000,\\
E_{16}(17/19)+
\frac{(17/19)^{17}/17!}{1-(17/19)/18}<24467/10000,\\
p+\frac{27707/5000}{17(67957/25000)}
=\frac{157378592659}{1155269000000}<13623/100000.
\end{gathered}
\tag{22}
\]

Squaring the first capacity-related comparisons is valid since every
quantity is positive. For the display in (1), \(E_6(1099/1000)>3\)
certifies the stated upper bound on \(\log3\).
The beta partial sum and its fourth-power comparison in Section 3 are
also exact fractions. The command

```
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py radial
```

checks (6), (21), (22), the tail integer comparison, and the exponent gap
with rational arithmetic. The baseline command independently checks the
round 4 energy and exponent bound before the extension.

There is a second rational certificate for the Gaussian tail, without
the Mills bound. Let

\[
S_-:=\sum_{j=0}^{59}\frac{(-7/2)^j}{(2j+1)j!},\qquad
S_+:=S_-+\frac{(7/2)^{60}}{121\cdot60!}.
\]

Taylor integration of \(e^{-z^2/2}\) from zero to \(\sqrt7\) gives

\[
4\overline\Phi(\sqrt7)=
2-4\sqrt{\frac7{2\pi}}S,\qquad S_-<S<S_+.
\]

The alternating terms decrease from index 2 onwards, which suffices for
these truncation bounds. The script bounds \(\pi\) above by
\(\pi_+=16A_{33}(1/5)-4A_{16}(1/239)\) and checks
\(S_->0\) and \(56S_-^2>\pi_+(2-p)^2\).
These imply \(4\overline\Phi(\sqrt7)<p\) independently of (6)–(8).

As a diagnostic of (2), a radial heat-equation calculation supplies an
independent expression. If
\(v(t,s)=s\mathbb P_s(\tau>t)\), then \(v_t=v_{ss}/2\) on \((0,2)\),
with zero boundary values and initial function \(v(0,s)=s\).
The sine coefficient of this initial function is
\(\int_0^2 s\sin(n\pi s/2)ds=4(-1)^{n+1}/(n\pi)\).
At \(s=1\), the even terms vanish, yielding for \(t>0\)

\[
\mathbb P_1(\tau>t)=\frac4\pi
\sum_{j\geq0}\frac{(-1)^j}{2j+1}
e^{-(2j+1)^2\pi^2t/8}.
\tag{23}
\]

The series converges absolutely at positive t. The diagnostic compares it
with the one-dimensional reflection expansion
\(\mathbb P(\eta\leq t)=2\sum_{j\geq0}(-1)^j
\operatorname{erfc}((2j+1)/\sqrt{2t})\) at four times. It also evaluates
the energy and gap with Decimal arithmetic and checks the gap separately
with libm. These floating-point diagnostics are not needed for (1).

The certified exponent gap is \(29/19\) times the round 4 gap.
Neither the exit-time identity nor the Gaussian rational approximation is
claimed to be new; their use supplies a checkable improvement of the
preceding T200 capacity estimate. No optimality claim is made for the full
argument.
