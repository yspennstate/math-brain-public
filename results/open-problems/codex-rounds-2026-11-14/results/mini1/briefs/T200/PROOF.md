# An explicit capacity bound for the two-path exponent

**Proposition.** In the definition in the task,

\[
\xi_3(1,1)\leq
1-\frac{9}{40\log 3}\log\frac{16500}{16487}
<\frac{6249}{6250}=0.99984.
\tag{1}
\]

This improves the constant in the displayed theorem of Runsheng Liu,
*An explicit lower bound for the growth exponent of three-dimensional
loop-erased random walk*, [arXiv:2609.18643v1](https://arxiv.org/html/2609.18643v1),
by changing the constants and the layer-count estimate in its capacity argument.
It is weaker than the bound mentioned without proof in that paper's Remark 1.2.
No exact value is obtained, and no claim of a new best bound is made.

The only intersection-exponent inputs are the existence of the limits in the
task and the known identity \(\xi_3(1,2)=1\). The existence result is also stated
in Section 1.1 of Yifan Gao, Xinyi Li, Yifan Li, Runsheng Liu, and Xiangyi Liu,
*A boundary Harnack principle and its application to analyticity of 3D Brownian
intersection exponents*, [arXiv:2411.14921](https://arxiv.org/pdf/2411.14921).
Analyticity and estimates with constant prefactors are not needed.

## 1. A deterministic hitting estimate

Use Newtonian capacity with kernel \(|x-y|^{-1}\): for a compact nonempty set
\(K\subset\mathbb R^3\),

\[
\operatorname{cap}(K)=\left[
\inf_{\mu\in\mathcal P(K)}
\iint\frac{\mu(du)\mu(dv)}{|u-v|}
\right]^{-1}.
\]

The capacity of a ball of radius \(s\) is \(s\). Let
\(D=B(0,3r)\), \(K\subset\overline B(0,2r)\) be compact, and \(|x|\leq r\).
For Brownian motion \(X\) starting at \(x\), write \(H_K\) for its first hit
of \(K\), including time zero, and \(\tau_D\) for its first exit from \(D\).
Then

\[
\mathbb P_x(H_K<\tau_D)
\geq\frac{2\operatorname{cap}(K)}{33r}.
\tag{2}
\]

Here are the potential-theoretic details. Normalize the Dirichlet Green kernel
in the ball to have singularity \(|x-y|^{-1}\). It is

\[
g_D(x,y)=\frac1d-\frac1{\sqrt{d^2+A}},\quad
d=|x-y|,\quad
A=\frac{(9r^2-|x|^2)(9r^2-|y|^2)}{9r^2}.
\]

For \(|x|\leq r\), \(|y|\leq2r\), we have
\(d\leq3r\) and \(A\geq40r^2/9\). The displayed difference decreases with
\(d>0\) and increases with \(A>0\), so

\[
g_D(x,y)\geq\frac1{3r}-\frac3{11r}=\frac2{33r}.
\tag{3}
\]

At \(x=y\) the Green kernel is infinite, and the same lower bound applies.
Define relative capacity by the same energy variational formula with \(g_D\)
in place of the Newtonian kernel. Since \(g_D(u,v)\leq |u-v|^{-1}\),
\(\operatorname{cap}_D(K)\geq\operatorname{cap}(K)\). The Green equilibrium
measure \(e_K^D\) has mass \(\operatorname{cap}_D(K)\), and its potential is
\(\mathbb P_x(H_K<\tau_D)\) for \(x\notin K\). These are the usual
equilibrium-potential identities; with exactly these normalizations they are
also set out in Liu, Section 2. Integrating (3) against \(e_K^D\) proves (2)
when the capacity is positive and \(x\notin K\). Capacity zero gives a trivial
bound. If \(x\in K\), the left side is one and the right side is at most
\(4/33\), since \(\operatorname{cap}(K)\leq2r\). This covers all cases.

## 2. One Brownian segment has sufficient capacity with high probability

Let \(W\) be standard three-dimensional Brownian motion starting at the origin.
Write \(\sigma_s\) for its first hit of \(\partial B(0,s)\), and let

\[
K(r)=W[\sigma_r,\sigma_{2r}],\qquad c=\frac{13}{1000}.
\]

For \(r\geq1\), condition on \(\mathcal F^W_{\sigma_r}\). The process
\(V_u=W_{\sigma_r+u}-W_{\sigma_r}\) is an independent standard Brownian
motion starting at zero. Set \(t=r^2/18\). Exiting \(B(0,2r)\) within time
\(t\) requires \(\sup_{u\leq t}|V_u|\geq r\). The process

\[
Y_u=\exp\left(\frac{15|V_u|^2}{2r^2}\right),\qquad 0\leq u\leq t,
\]

is an integrable nonnegative submartingale: the function of \(V_u\) is convex,
and its Gaussian exponential moment is finite because
\(15t/r^2=5/6<1\). Doob's maximal inequality and the Gaussian moment formula
therefore give

\[
\mathbb P\left(\sigma_{2r}-\sigma_r<t\mid\mathcal F^W_{\sigma_r}\right)
\leq e^{-15/2}(1-15t/r^2)^{-3/2}
=6\sqrt6\,e^{-15/2}.
\tag{4}
\]

Consider the probability measure
\(\mu_t=t^{-1}\int_0^t\delta_{W_{\sigma_r+u}}\,du\), on the unrestricted
continuation of the path. For \(u\ne v\), Gaussian radial integration gives

\[
\begin{aligned}
\mathbb E|V_u-V_v|^{-1}
&=\frac{4\pi}{(2\pi s)^{3/2}}
\int_0^\infty\rho e^{-\rho^2/(2s)}\,d\rho\\
&=\frac{4\pi s}{(2\pi s)^{3/2}}
=\sqrt{2/\pi}\,s^{-1/2},\qquad s=|u-v|.
\end{aligned}
\]

Tonelli's theorem and integration over the two triangles of \([0,t]^2\)
yield

\[
\begin{aligned}
\mathbb E[I(\mu_t)\mid\mathcal F^W_{\sigma_r}]
&=t^{-2}\sqrt{2/\pi}\int_0^t\int_0^t|u-v|^{-1/2}\,du\,dv\\
&=\frac83\sqrt{2/\pi}\,t^{-1/2}
=\frac{16}{r\sqrt\pi}.
\end{aligned}
\tag{5}
\]

The diagonal has two-dimensional Lebesgue measure zero, and the integral is
finite. On \(\{\sigma_{2r}-\sigma_r\geq t\}\), \(\mu_t\) is supported on
\(K(r)\). On that event, \(\operatorname{cap}(K(r))<cr\) forces
\(I(\mu_t)>1/(cr)\), by the variational definition of capacity. A union bound
and Markov's inequality now give the uniform conditional bound

\[
\mathbb P\left(\operatorname{cap}(K(r))<cr\mid\mathcal F^W_{\sigma_r}\right)
\leq6\sqrt6\,e^{-15/2}+\frac{16c}{\sqrt\pi}
<p:=\frac{63}{500}.
\tag{6}
\]

For explicit verification of the last strict inequality, use
\(\sqrt6<5/2\), \(e^{15/2}>1800\), and \(\sqrt\pi>177/100\). They imply

\[
6\sqrt6\,e^{-15/2}+\frac{16c}{\sqrt\pi}
<\frac1{120}+\frac{104}{885}
<\frac{63}{500},
\tag{7}
\]

where the difference in the last inequality is \(9/59000\).
Exact arithmetic certificates for the exponential and pi estimates are
provided in Section 6.

## 3. A conditional Chernoff bound for the layers

Fix \(N\geq1\), let \(r_j=3^j\), \(R=3^N\), and take
\(K_j=K(r_j)\) for \(0\leq j<N\). All these compact sets belong to
\(W[0,\sigma_R]\), since \(2r_j<r_{j+1}\leq R\).
Let

\[
B_j=\mathbf 1\{\operatorname{cap}(K_j)<cr_j\},\quad
S_N=\sum_{j=0}^{N-1}B_j,\quad L_N=N-S_N.
\]

The variable \(B_j\) is measurable at \(\sigma_{2r_j}\), which precedes
\(\sigma_{r_{j+1}}\). By (6), for every \(\theta>0\),

\[
\mathbb E[e^{\theta B_j}\mid\mathcal F^W_{\sigma_{r_j}}]
\leq1-p+pe^\theta.
\]

The earlier \(B_i\), \(i<j\), are measurable in this conditioning sigma-field.
Repeated conditioning, without an independence assumption, gives

\[
\mathbb E e^{\theta S_N}\leq(1-p+pe^\theta)^N.
\tag{8}
\]

Set \(q=9/40\) and \(a=1-q=31/40>p\). Markov's inequality in (8), with
\(e^\theta=a(1-p)/(p(1-a))>1\), proves

\[
\mathbb P(L_N<qN)=\mathbb P(S_N>aN)
\leq e^{-ND},\quad
D=a\log\frac ap+(1-a)\log\frac{1-a}{1-p}.
\tag{9}
\]

There is no integrality restriction on \(qN\) in this inequality. For the
specified rational numbers,

\[
D=\frac{31}{40}\log\frac{775}{126}
 +\frac9{40}\log\frac{225}{874}>\log3.
\tag{10}
\]

The last comparison is equivalent to the integer inequality

\[
775^{31}225^9>3^{40}126^{31}874^9.
\tag{11}
\]

Section 6 gives its reproducible exact check. Consequently, with
\(b=D/\log3>1\), (9) implies \(\mathbb P(L_N<qN)\leq R^{-b}\).

## 4. Conditional avoidance and the second moment

Let \(X\), independent of \(W\), start at \((1,0,0)\). Denote its first
hit of \(\partial B(0,s)\) by \(\tau_s\), with \(\tau_1=0\), and define

\[
Q_R(W)=\mathbb P\bigl(X[0,\tau_R]\cap W[0,\sigma_R]=\varnothing
\mid W[0,\sigma_R]\bigr).
\]

Fix the stopped path \(W[0,\sigma_R]\). Its sets \(K_j\) and good-layer
indicators are now deterministic. If the \(j\)-th layer is good, (2) says
that a test motion starting anywhere on \(\partial B(0,r_j)\) hits \(K_j\)
before exiting \(B(0,r_{j+1})\) with probability at least

\[
h:=\frac{2c}{33}=\frac{13}{16500}.
\]

Let \(A_j\) be the event that \(X[\tau_{r_j},\tau_{r_{j+1}}]\) avoids
\(K_j\). Conditional on \(X\)'s past at \(\tau_{r_j}\), the probability of
\(A_j\) is at most \((1-h)^{1-B_j}\), by its strong Markov property.
All earlier \(A_i\) are measurable at this time. The full avoidance event
implies every \(A_j\); hence repeated conditioning gives

\[
Q_R(W)\leq\mathbb P\left(\bigcap_{j=0}^{N-1}A_j\mid W[0,\sigma_R]\right)
\leq(1-h)^{L_N}.
\tag{12}
\]

This step allows the test motion to return to smaller radii; it does not
assume that its whole trajectory lies in disjoint annuli. Only its successive
first-hitting-time segments are used. It also places no conditioning on the
future of \(X\) when applying the strong Markov property.

Define

\[
\delta=-\frac{q\log(1-h)}{\log3}
=\frac9{40\log3}\log\frac{16500}{16487}.
\]

On \(\{L_N\geq qN\}\), (12) implies \(Q_R^2\leq R^{-\delta}Q_R\).
On the complement use \(Q_R^2\leq1\). With (9), this yields

\[
\mathbb E Q_R^2\leq R^{-\delta}\mathbb E Q_R+R^{-b},\qquad b>1.
\tag{13}
\]

## 5. Passage to the exponent

The existence of the limits and \(\xi_3(1,2)=1\) imply, along \(R=3^N\),

\[
\mathbb E Q_R^2=R^{-1+o(1)},\qquad
\mathbb E Q_R=R^{-\xi_3(1,1)+o(1)}.
\tag{14}
\]

For completeness, the task initially defines limits at integer log-radii.
The conditional avoidance probability, coupled using the whole obstacle path,
is nonincreasing with the radius. Its moments are therefore nonincreasing.
For any real \(s\), bracket its moments by those at \(\lfloor s\rfloor\)
and \(\lceil s\rceil\). Dividing negative logarithms by \(s\) transfers
the integer limit to all log-radii, in particular \(s=N\log3\).

Choose any \(\varepsilon\in(0,b-1)\). For sufficiently large \(N\), (14)
implies \(\mathbb E Q_R^2\geq R^{-1-\varepsilon}\), and
\(R^{-b}\leq\tfrac12 R^{-1-\varepsilon}\). Equation (13) gives

\[
\mathbb E Q_R\geq\tfrac12 R^{-1+\delta-\varepsilon}.
\]

Taking the exponent limit yields
\(\xi_3(1,1)\leq1-\delta+\varepsilon\). Letting \(\varepsilon\downarrow0\)
proves the first inequality in (1).

Finally, \(-\log(1-h)>h\) and \(\log3<11/10\) give

\[
\delta>\frac{qh}{11/10}
=\frac{39}{242000}>\frac1{6250}.
\tag{15}
\]

The second comparison is \(39\cdot6250=243750>242000\).
This proves the strict rational bound in (1).

## 6. Exact numerical certificates and a second derivation

All transcendental comparisons used above can be replaced by rational ones.

* The positive Taylor sum
  \(\sum_{j=0}^{30}(15/2)^j/j!\) is greater than \(1800\), and is strictly
  less than \(e^{15/2}\).
* Write \(A_m(x)=\sum_{j=0}^{m-1}(-1)^j x^{2j+1}/(2j+1)\).
  The alternating-series bounds and Machin's identity give
  \(\pi>16A_8(1/5)-4A_5(1/239)>(177/100)^2\).
  To check the identity, if \(\alpha=\arctan(1/5)\), then
  \(\tan(2\alpha)=5/12\), \(\tan(4\alpha)=120/119\), and
  \(\tan(4\alpha-\arctan(1/239))=1\).
  The angle is between zero and \(\pi/2\), so it equals \(\pi/4\).
* The positive Taylor sum
  \(\sum_{j=0}^{6}(11/10)^j/j!\) is greater than \(3\), proving
  \(e^{11/10}>3\) and thus \(\log3<11/10\).
* (11), (7), and (15) are checked using integers and rational arithmetic in
  `verify_certificate.py`. Its exact comparisons do not depend on the
  exploratory parameter search.

Two independent ways to obtain the Green constant agree. The distance-and-
\(A\) estimate above gives \(2/(33r)\). Alternatively, for fixed
\(s=|x|\leq r\) and \(u=|y|\leq2r\), increasing the angle between \(x,y\)
increases \(d\) and decreases the Green kernel. At opposite directions its
value is

\[
\frac1{s+u}-\frac{3r}{9r^2+su}.
\]

Its derivative in \(s\) is
\(-1/(s+u)^2+3ru/(9r^2+su)^2<0\): indeed
\(\sqrt{3ru}<3r\) and
\(9r^2+su-3r(s+u)=(3r-s)(3r-u)>0\).
The same argument interchanging \(s,u\) gives a negative derivative in \(u\).
Thus its minimum occurs at \(s=r,u=2r\), where it is again \(2/(33r)\).
Zero radii follow by continuity; coincident points do not lower the minimum.

The energy constant has a separate scaling check: Brownian scaling makes
\(\mathbb E I(\mu_t)=t^{-1/2}\mathbb E I(\mu_1)\), while
\(2\int_0^1(1-v)v^{-1/2}\,dv=8/3\). This agrees with the double-integral
calculation in (5). The verifier also evaluates the constants independently
using high-precision logarithm/exponential series and prints the margins.
