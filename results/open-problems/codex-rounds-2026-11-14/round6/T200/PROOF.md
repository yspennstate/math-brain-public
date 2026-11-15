# A variable-geometry capacity estimate

For standard Brownian motion with generator \(\Delta/2\),

\[
\boxed{\displaystyle
\xi_3(1,1)\leq
1-\frac{9000}{2361557\log(17/5)}
=0.996885829783172489660892941172\ldots<0.9969.}
\tag{1}
\]

The decimal evaluates the upper bound. No exact intersection exponent is
identified. The exponent inputs are existence of the moment limits in the
question and the known identity \(\xi_3(1,2)=1\).

The capacity method follows Sections 2–4 of Runsheng Liu,
*An explicit lower bound for the growth exponent of three-dimensional
loop-erased random walk*, [arXiv:2609.18643v1](https://arxiv.org/html/2609.18643v1),
and the preceding T200 proofs. The extension is a radial exit bound valid
for every segment radius ratio \(a>1\), coupled to a layer spacing \(b>a\).
The deterministic occupation weight and energy estimate are retained.

## 1. Radial exit and one-dimensional upper exit

Let \(W\) be three-dimensional Brownian motion starting at a point of
radius one, and let \(\tau_a\) be its first exit from \(B(0,a)\), where
\(a>1\). Independently, let \(Y\) be one-dimensional standard Brownian
motion starting at one, write \(H_j\) for its first hit of \(j\), and put
\(T=H_0\wedge H_a\). Then, as measures on finite nonnegative times,

\[
\mathbb P(\tau_a\in dt)
=a\,\mathbb P_1(T\in dt,\ Y_T=a).
\tag{2}
\]

Here is a verification including normalization. For \(q>0\), put
\(z=\sqrt{2q}\). The radial function

\[
f_q(x)=\frac{a\sinh(z|x|)}{|x|\sinh(za)},\qquad
f_q(0)=\frac{az}{\sinh(za)}
\]

is smooth at zero by the power series of \(\sinh(z|x|)/|x|\).
The radial Laplacian gives \(\Delta f_q/2=qf_q\), with boundary value
one at radius \(a\). The martingale \(|W_t|^2-3t\), stopped at
\(t\wedge\tau_a\), gives

\[
\mathbb E(t\wedge\tau_a)
=\frac{\mathbb E|W_{t\wedge\tau_a}|^2-1}{3}
\leq\frac{a^2-1}{3}.
\]

Thus \(\tau_a<\infty\) almost surely. Stopped Itô's formula for
\(e^{-q(t\wedge\tau_a)}f_q(W_{t\wedge\tau_a})\) and bounded convergence
give

\[
\mathbb E e^{-q\tau_a}=\frac{a\sinh z}{\sinh(az)}.
\tag{3}
\]

All stochastic integrands are bounded on the stopped compact domain for
each fixed \(q\); the finite-time stopped stochastic integrals have mean
zero.

For the one-dimensional motion, \(Y_{t\wedge T}^2-(t\wedge T)\)
has mean one and \(|Y_{t\wedge T}|\leq a\), so
\(\mathbb E(t\wedge T)\leq a^2-1\), and \(T\) is finite almost surely.
Stopping the bounded martingale \(Y_{t\wedge T}\) yields
\(\mathbb P_1(Y_T=a)=1/a\). Consequently the right side of (2) has
total mass one.

The function \(h_q(y)=\sinh(zy)/\sinh(za)\) on \([0,a]\) solves
\(h_q''/2=qh_q\), with boundary values zero and one. Its stopped
Itô formula gives

\[
\mathbb E_1[e^{-qT};Y_T=a]=\frac{\sinh z}{\sinh(az)}.
\tag{4}
\]

Equations (3)–(4) identify the Laplace transforms of the two probability
measures in (2). For completeness, equality at positive integer \(q\)
gives equal moments after pushing the measures forward by \(t\mapsto e^{-t}\).
Their zeroth moments are also equal. Polynomial approximation on \([0,1]\)
therefore identifies the pushforward measures; neither has mass at zero
because the times are finite. Applying \(-\log\) proves (2).

Write \(\overline\Phi(x)=(2\pi)^{-1/2}\int_x^\infty e^{-y^2/2}dy\).
By (2), removing the lower-barrier restriction and then applying reflection,
for \(u>0\),

\[
\begin{aligned}
\mathbb P(\tau_a\leq u)
&=a\mathbb P_1(H_a\leq u,H_a<H_0)\\
&\leq a\mathbb P_1(H_a\leq u)
=2a\overline\Phi((a-1)/\sqrt u).
\end{aligned}
\tag{5}
\]

Let now \(W\) start at zero and let \(\sigma_r\) be its first hit of
radius \(r\). The strong Markov property, scaling and rotational invariance
give, with \(\Delta_a(r)=\sigma_{ar}-\sigma_r\),

\[
\mathbb P(\Delta_a(r)<ur^2\mid\mathcal F_{\sigma_r})
\leq 2a\overline\Phi((a-1)/\sqrt u).
\tag{6}
\]

Every finite radius is reached almost surely; the same squared-distance
martingale establishes this. At \(a=2\), (3) simplifies to
\(\operatorname{sech}(\sqrt{2q})\), recovering the round 5 exit identity.

## 2. A bound for arbitrary geometry

Normalize Newtonian capacity by

\[
\operatorname{cap}(K)=\left[
\inf_{\mu\in\mathcal P(K)}\iint |x-y|^{-1}\mu(dx)\mu(dy)
\right]^{-1},\qquad 1/\infty=0.
\tag{7}
\]

A radius-\(r\) closed ball has capacity \(r\). Fix \(1<a<b\), and set

\[
K_a(r)=W[\sigma_r,\sigma_{ar}],\qquad
C_a(r)=\operatorname{cap}(K_a(r))/r.
\]

In particular \(0\leq C_a(r)\leq a\).

For any compact \(K\subset\overline B(0,ar)\) and \(|x|\leq r\),

\[
\mathbb P_x(H_K<\tau_{br})
\geq \frac{g(a,b)}r\operatorname{cap}(K),\qquad
g(a,b)=\frac1{1+a}-\frac b{b^2+a}
=\frac{(b-1)(b-a)}{(1+a)(b^2+a)}>0.
\tag{8}
\]

Here \(H_K\) includes time zero and \(\tau_{br}\) is the first exit
from \(B(0,br)\). To prove the kernel bound underlying (8), use the
Dirichlet Green kernel normalized to have singularity \(|x-y|^{-1}\):

\[
G(x,y)=\frac1d-\frac1{\sqrt{d^2+D}},\qquad d=|x-y|,\qquad
D=\frac{(b^2r^2-|x|^2)(b^2r^2-|y|^2)}{b^2r^2}.
\tag{9}
\]

For the indicated points,
\(d\leq(1+a)r\) and
\(D\geq (b^2-1)(b^2-a^2)r^2/b^2\). The difference in (9) decreases
with \(d>0\) and increases with \(D>0\). Also

\[
(1+a)^2+\frac{(b^2-1)(b^2-a^2)}{b^2}
=\frac{(b^2+a)^2}{b^2}.
\]

It follows that \(G(x,y)\geq g(a,b)/r\). Equality occurs at opposite
radial endpoints of radii \(r\) and \(ar\). Coincident points have
infinite kernel.

For \(x\notin K\) and positive capacity, the Green equilibrium measure
in the ball has potential \(\mathbb P_x(H_K<\tau_{br})\) and total mass
\(\operatorname{cap}_{B(0,br)}(K)\). These are the equilibrium-potential
identities also used in Liu, Section 2. The variational definition and
\(G(u,v)\leq|u-v|^{-1}\) imply that this mass is at least
\(\operatorname{cap}(K)\). Integrating the lower kernel bound proves (8).
At zero capacity the conclusion is immediate. If \(x\in K\), the
left side is one and the right side is at most
\(ag(a,b)<a/(1+a)<1\), so (8) holds there too.

Retain the deterministic probability time measure

\[
\rho(du)=\frac{[u(1-u)]^{-1/4}}{B(3/4,3/4)}du,\qquad
B(c,d)=\int_0^1u^{c-1}(1-u)^{d-1}du.
\]

Its time energy, derived in Section 5 below, is

\[
\iint |u-v|^{-1/2}\rho(du)\rho(dv)
=J=\frac{\pi\sqrt2}{B(3/4,3/4)}<\frac{21}{8}.
\tag{10}
\]

For a deterministic dimensionless cutoff \(u>0\), put \(t=ur^2\) and
use the unrestricted continuation of the obstacle path to form

\[
\mu_t=\int_0^1\delta_{W_{\sigma_r+tv}}\rho(dv),\qquad
I_t=\iint |x-y|^{-1}\mu_t(dx)\mu_t(dy).
\]

Conditionally on \(\mathcal F_{\sigma_r}\), a Brownian increment between
distinct times \(tv,tw\) has covariance \(t|v-w|I_3\). Radial Gaussian
integration gives

\[
\mathbb E|W_{\sigma_r+tv}-W_{\sigma_r+tw}|^{-1}
=\frac{4\pi}{(2\pi t|v-w|)^{3/2}}
\int_0^\infty y e^{-y^2/(2t|v-w|)}dy
=\sqrt{\frac2{\pi t}}|v-w|^{-1/2}.
\]

The time measure has no atoms; its product gives no mass to the diagonal.
Tonelli therefore gives

\[
\mathbb E[rI_t\mid\mathcal F_{\sigma_r}]
=J\sqrt{\frac2{\pi u}}=:A(u).
\tag{11}
\]

This expectation is finite, so the energy is finite almost surely. It is
positive because its probability measure has compact support and the
kernel is positive.

On \(\{\Delta_a(r)\geq t\}\), the occupation measure is supported on
\(K_a(r)\), hence \(C_a(r)\geq1/(rI_t)\). For \(s,y>0\),
\(e^{-s/y}\leq y/(es)\), since \((s/y)e^{-s/y}\leq e^{-1}\).
On \(\{\Delta_a(r)<t\}\), use \(e^{-sC_a(r)}\leq1\). Thus pointwise

\[
e^{-sC_a(r)}\leq
\mathbf1_{\{\Delta_a(r)<t\}}+\frac{rI_t}{es}.
\]

Taking conditional expectations in this inequality and using (6), (11),

\[
\mathbb E[e^{-sC_a(r)}\mid\mathcal F_{\sigma_r}]
\leq 2a\overline\Phi((a-1)/\sqrt u)+\frac{A(u)}{es}.
\tag{12}
\]

No independence between the exit time and the occupation energy is used.
The occupation measure can continue beyond the segment on the short-time
event, where no capacity comparison is made.

Suppose the right side of (12) is bounded above by a deterministic \(m\),
and choose \(c>0\) such that

\[
\beta=e^{sc}m<1/b.
\tag{13}
\]

Then

\[
\xi_3(1,1)\leq1-\frac{g(a,b)c}{\log b}.
\tag{14}
\]

To prove this implication, set \(r_j=b^j\), \(R=b^N\),
\(C_j=C_a(r_j)\) and \(S_N=\sum_{j=0}^{N-1}C_j\). Because
\(a<b\), every \(C_j\) is measurable at \(\sigma_{ar_j}\), before
\(\sigma_{r_{j+1}}\). Iterating (12) backwards through the layers gives
\(\mathbb E e^{-sS_N}\leq m^N\). Markov's inequality at the real
threshold \(cN\) gives

\[
\mathbb P(S_N<cN)\leq\beta^N=R^{-\gamma},\qquad
\gamma=-\log\beta/\log b>1.
\tag{15}
\]

Let \(X\) be an independent Brownian motion starting at \((1,0,0)\),
with first hitting times \(\tau_r\), including \(\tau_1=0\), and define

\[
Q_R=\mathbb P\{X[0,\tau_R]\cap W[0,\sigma_R]=\varnothing
\mid W[0,\sigma_R]\}.
\]

Condition on the stopped obstacle path. Each compact set \(K_a(r_j)\)
is now fixed and contained in that path, because \(ar_j<r_{j+1}\leq R\).
At \(\tau_{r_j}\), (8) bounds the probability of avoiding this set
until \(\tau_{r_{j+1}}\) by \(1-g(a,b)C_j\), uniformly over the
test path's current position. Earlier local avoidance events are measurable
at that time. Full avoidance implies all these local events. Successive
applications of the strong Markov property of \(X\) therefore yield

\[
Q_R\leq\prod_{j=0}^{N-1}(1-g(a,b)C_j)
\leq e^{-g(a,b)S_N}.
\tag{16}
\]

All factors lie in \([0,1]\), since \(0\leq C_j\leq a\) and
\(ag(a,b)<1\). This argument permits inward returns and initial hits;
it does not confine either path to an annulus or condition on future
avoidance.

On \(\{S_N\geq cN\}\), (16) gives \(Q_R\leq R^{-\delta}\), where
\(\delta=g(a,b)c/\log b\). On this event,
\(Q_R^2\leq R^{-\delta}Q_R\), and elsewhere \(Q_R^2\leq1\). Hence

\[
\mathbb E Q_R^2\leq R^{-\delta}\mathbb E Q_R+R^{-\gamma}.
\tag{17}
\]

Couple different radii with the same whole obstacle path and whole test
path. The conditional avoidance probability is nonincreasing in \(R\),
as both stopped traces increase. The conditional probability given the
whole obstacle equals the function \(Q_R\) of its stopped trace. Monotonic
bracketing of real log-radii between successive integers thus extends the
moment limits in the question to \(R=b^N\). They imply

\[
\mathbb E Q_R^2=R^{-1+o(1)},\qquad
\mathbb E Q_R=R^{-\xi_3(1,1)+o(1)}.
\]

Fix \(0<\varepsilon<\gamma-1\). For sufficiently large \(N\),
\(\mathbb E Q_R^2\geq R^{-1-\varepsilon}\) and
\(R^{-\gamma}\leq\tfrac12R^{-1-\varepsilon}\).
Rearranging (17) gives
\(\mathbb E Q_R\geq\tfrac12R^{-1+\delta-\varepsilon}\).
The exponent limit implies
\(\xi_3(1,1)\leq1-\delta+\varepsilon\); letting
\(\varepsilon\downarrow0\) proves (14).

## 3. One certified choice

Take

\[
a=\frac{19}{10},\quad b=\frac{17}{5},\quad
u=\frac{81}{730},\quad s=\frac{43}{2},\quad c=\frac5{121}.
\tag{18}
\]

Then \((a-1)^2/u=v=73/10\), and \(sc=215/242\). The scalar bounds
proved in Section 4 are

\[
2a\overline\Phi(\sqrt v)<p:=\frac{1311}{100000},\qquad
A(u)<A_0:=\frac{629}{100},\qquad e>\frac{1359}{500}.
\tag{19}
\]

Consequently (12) gives

\[
\mathbb E[e^{-(43/2)C_a(r)}\mid\mathcal F_{\sigma_r}]
<p+\frac{A_0}{(43/2)(1359/500)}
=\frac{705610907}{5843700000}
<m:=\frac{151}{1250}.
\tag{20}
\]

Also \(e^{215/242}<304/125\), so the lower-tail base in (15) is bounded
by

\[
\beta_0=\frac{151}{1250}\frac{304}{125}
=\frac{22952}{78125},\qquad
b\beta_0=\frac{390184}{390625}<1.
\tag{21}
\]

Thus (13) holds. Direct arithmetic gives

\[
g(a,b)=\frac{1800}{19517},\qquad
g(a,b)c=\frac{9000}{2361557}.
\tag{22}
\]

Substituting (22) into (14) proves the non-strict inequality in (1).
For the rounded bound, \(\log(17/5)<49/40\) gives

\[
\delta=\frac{9000}{2361557\log(17/5)}
>\frac{360000}{115716293}>\frac{31}{10000}.
\tag{23}
\]

The last comparison is
\(3600000000>31\cdot115716293=3587205083\).
Therefore \(\xi_3(1,1)<0.9969\).

## 4. Finite scalar certificates

The following bounds use rational arithmetic only. Define

\[
E_n(x)=\sum_{j=0}^{n}\frac{x^j}{j!},\qquad
U_n(x)=E_n(x)+\frac{x^{n+1}/(n+1)!}{1-x/(n+2)}.
\]

For \(0<x<n+2\), the positive Taylor series and a geometric bound on its
tail give \(E_n(x)<e^x<U_n(x)\).

For \(A_n(x)=\sum_{j=0}^{n-1}(-1)^jx^{2j+1}/(2j+1)\), Machin's
identity and alternating-series bounds give

\[
\pi>16A_8(1/5)-4A_5(1/239)>
\pi_0:=\frac{314159}{100000}.
\tag{24}
\]

To check the identity, put \(\alpha=\arctan(1/5)\). Double-angle
formulas give \(\tan(2\alpha)=5/12\), \(\tan(4\alpha)=120/119\),
and \(\tan(4\alpha-\arctan(1/239))=1\). This last angle belongs to
\((0,\pi/2)\), so it equals \(\pi/4\).

For the Gaussian estimate, set

\[
R(x)=e^{x^2/2}\int_x^\infty e^{-y^2/2}dy,\quad
P(x)=x^4+9x^2+8,\quad Q(x)=x^5+10x^3+15x.
\]

Differentiation gives \(R'=xR-1\), and direct multiplication gives

\[
P'Q-PQ'-xPQ+Q^2=-120.
\]

Therefore \(V=P/Q\) satisfies \(V'-xV+1=-120/Q^2\). For \(x>0\),
\(R(x)\leq1/x\), by bounding the Gaussian tail integral by
\(x^{-1}\int_x^\infty y e^{-y^2/2}dy\). Since \(V(x)\sim1/x\),
integration of the differential identity from \(x\) to infinity yields

\[
V(x)-R(x)=120e^{x^2/2}\int_x^\infty\frac{e^{-y^2/2}}{Q(y)^2}dy>0.
\tag{25}
\]

In particular, for \(v=73/10\),

\[
H=\frac{v^2+9v+8}{v^2+10v+15}=\frac{12699}{14129},\qquad
2a\overline\Phi(\sqrt v)
<a\sqrt{\frac2{\pi v}}e^{-v/2}H.
\tag{26}
\]

The finite comparisons

\[
E_{32}(73/20)>h_0:=\frac{3847}{100},\qquad
p^2\pi_0 v h_0^2>2a^2H^2
\tag{27}
\]

certify the first inequality in (19) by squaring positive quantities.
For the energy, (10), (11) and

\[
A_0^2\pi_0>\frac{2(21/8)^2}{81/730}
\tag{28}
\]

give its second inequality. The remaining finite comparisons are

\[
E_7(1)>1359/500,\qquad
U_{16}(215/242)<304/125,\qquad
E_{10}(49/40)>17/5.
\tag{29}
\]

Together with the exact rational comparisons in (20)–(23), these certify
all numerical bounds used for (1).

## 5. The retained time-energy identity

For completeness, its calculation requires no minimizing assertion.
For \(0<x<1\), define

\[
L(x)=\int_0^x(x-v)^{-1/2}[v(1-v)]^{-1/4}dv.
\]

The positive binomial series and the beta recurrence yield

\[
\begin{aligned}
L(x)
&=\sum_{n\geq0}\frac{(1/4)_n}{n!}x^{n+1/4}B(n+3/4,1/2)\\
&=B(3/4,1/2)\sum_{n\geq0}
\frac{(3/4)_n x^{n+1/4}}{n!(4n+1)}\\
&=\frac{B(3/4,1/2)}4\int_0^x[z(1-z)]^{-3/4}dz.
\end{aligned}
\tag{30}
\]

Here \((c)_0=1\), \((c)_n=c(c+1)\cdots(c+n-1)\);
\(B(n+3/4,1/2)=B(3/4,1/2)(3/4)_n/(5/4)_n\), and
\((1/4)_n/(5/4)_n=1/(4n+1)\). The beta recurrence follows by integrating
the derivative of \(v^c(1-v)^d\). All series terms in this calculation are
nonnegative, so Tonelli justifies the exchanges.

The unnormalized potential is \(L(x)+L(1-x)\); by the symmetry in the
last integral in (30), this is constant. As \(x\downarrow0\),
\(L(x)\to0\). Substitution \(v=xz\) in its original definition gives

\[
L(x)=x^{1/4}\int_0^1z^{-1/4}(1-z)^{-1/2}(1-xz)^{-1/4}dz.
\]

Monotone convergence as \(x\uparrow1\) gives
\(L(x)\to B(3/4,1/4)\). Direct endpoint integration gives the same
potential there. Substituting \(v=w/(1+w)\), then \(w=z^4\), gives

\[
B(1/4,3/4)=4\int_0^\infty\frac{dz}{1+z^4}=\pi\sqrt2.
\]

For the last equality, substitution \(z\mapsto1/z\) shows that the
integral \(I\) is also \(\int_0^\infty z^2/(1+z^4)dz\). Factoring the
denominator then gives

\[
2I=\frac12\int_0^\infty\left(
\frac1{z^2+\sqrt2z+1}+\frac1{z^2-\sqrt2z+1}\right)dz
=\frac\pi{\sqrt2},
\]

by completing the squares. Dividing the constant potential by
\(B(3/4,3/4)\) and integrating against \(\rho\) proves (10)'s identity.

For its upper bound, the positive binomial series on \([0,1/2]\) gives

\[
B(3/4,3/4)=2^{1/4}S,\quad
S=\sum_{n\geq0}\frac{(1/4)_n}{n!2^n(n+3/4)},\quad
S_8=\frac{112206509213551}{78752847495168}>\frac{178}{125}.
\]

The elementary identity
\(22/7-\pi=\int_0^1 x^4(1-x)^4/(1+x^2)dx>0\)
follows by polynomial division and integration. Since
\(J^4=2\pi^4/S^4\), the rational comparison

\[
2(22/7)^4<(21/8)^4(178/125)^4
\]

proves \(J<21/8\). All quantities are positive.

## 6. Independent checks

Run, from this folder,

```
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py baseline
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py geometry
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py diagnostics
```

The baseline independently certifies round 5. The geometry mode checks the
finite rational comparisons above and separately bounds the Gaussian tail
by integrating its Taylor series. Specifically, put

\[
S_- =\sum_{j=0}^{79}\frac{(-v/2)^j}{(2j+1)j!}.
\]

Taylor's remainder gives
\(S_-<\int_0^1e^{-vz^2/2}dz\), while Gaussian symmetry gives

\[
2a\overline\Phi(\sqrt v)
=a-2a\sqrt{v/(2\pi)}\int_0^1e^{-vz^2/2}dz.
\]

The script checks \(S_->0\) and
\(2a^2vS_-^2>\pi_+(a-p)^2\), with a rational Machin upper bound
\(\pi_+\) on \(\pi\). Thus it certifies the first inequality of (19)
independently of the Mills approximation.

The final gap has rational logarithm enclosures using

\[
\log x=2\sum_{j=0}^{n-1}\frac{z^{2j+1}}{2j+1}+E,
\quad z=\frac{x-1}{x+1},\quad
0<E<\frac{2z^{2n+1}}{(2n+1)(1-z^2)},\quad x>1.
\]

Decimal logarithms and libm supply separate numerical checks.
The diagnostics mode compares two radial exit CDF expansions. Multiplying
the radial survival function by its radius reduces its heat equation to
the one-dimensional heat equation on \((0,a)\) with zero boundary values
and initial function \(r\). Its sine expansion at radius one gives

\[
\mathbb P(\tau_a>t)=\frac{2a}{\pi}
\sum_{n\geq1}\frac{(-1)^{n+1}}n
\sin(n\pi/a)e^{-n^2\pi^2t/(2a^2)}.
\tag{31}
\]

Independently, expanding (3) into exponentials gives

\[
\mathbb P(\tau_a\leq t)=a\sum_{j\geq0}\left[
\operatorname{erfc}\!\left(\frac{(2j+1)a-1}{\sqrt{2t}}\right)
-\operatorname{erfc}\!\left(\frac{(2j+1)a+1}{\sqrt{2t}}\right)
\right].
\tag{32}
\]

Here \(\operatorname{erfc}(x)=2\overline\Phi(\sqrt2x)\).
To justify (32), the bracketed differences of first-passage CDFs are
nonnegative. Their Laplace transforms in \(t\), by the first-passage
transform, are the corresponding differences of exponentials divided by
\(q\). Tonelli sums them to \(a\sinh(\sqrt{2q})/[q\sinh(a\sqrt{2q})]\),
which is the Laplace transform of the radial exit CDF by (3).
Uniqueness identifies the CDFs almost everywhere, and continuity upgrades
this to equality everywhere. Both series converge absolutely for \(t>0\),
locally uniformly there; (32)'s convergence follows from Gaussian tails.
Formula (31), rather than the transform calculation, is the independent
diagnostic of (2). These floating-point comparisons and the finite Green
grid are not needed for the proof of (1).

The exact-value problem remains unresolved. This parameter choice improves
the preceding bound but is not asserted to optimize the method.
