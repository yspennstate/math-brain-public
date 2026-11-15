# A terminal-mass and local-time reduction for T423

Let \(u,v\) be two solutions in the question on the same filtered
probability space, driven by the same space-time white noise \(W\), and
with the same deterministic initial density \(u_0\). Write

\[
m=\int_{\mathbb R}u_0(x)\,dx,\qquad
U_t=\int_{\mathbb R}u_t(x)\,dx,\qquad
V_t=\int_{\mathbb R}v_t(x)\,dx,\qquad D_t=U_t-V_t.
\]

Here and below, equality of fields on an interval means equality for all
times and spatial points outside one null event. Fix a deterministic
\(T>0\). Define

\[
C_t=\int_{\mathbb R}\sqrt{u_t(x)v_t(x)}\,dx,\qquad
A_t=\int_{\mathbb R}(\sqrt{u_t(x)}-\sqrt{v_t(x)})^2\,dx
     =U_t+V_t-2C_t.
\tag{1}
\]

The following are equivalent:

1. The fields \(u,v\) agree on \([0,T]\times\mathbb R\).
2. \(U_T=V_T\) almost surely.
3. \(\mathbb E\int_0^T A_s\,ds=0\).
4. The symmetric local time \(L_T^0(D)\) is zero almost surely.
5. The following limit is zero:

\[
\lim_{\varepsilon\downarrow0}\frac1{2\varepsilon}
 \mathbb E\int_0^T
 \mathbf1_{\{|U_s-V_s|<\varepsilon\}}A_s\,ds.
\tag{2}
\]

The exact identities and bound behind the equivalence are

\[
\mathbb E D_T^2=\mathbb E\int_0^T A_s\,ds,
\qquad
\mathbb E|D_T|=\mathbb E L_T^0(D)
 =\lim_{\varepsilon\downarrow0} Q_\varepsilon(T),
\tag{3}
\]

where \(Q_\varepsilon(T)\) denotes the expression before the limit in
(2), and

\[
0\leq\mathbb E|D_T|-Q_\varepsilon(T)\leq\frac\varepsilon2.
\tag{4}
\]

There is also a quantitative spatial bound:

\[
\mathbb E\int_0^T\|u_s-v_s\|_{L^1(\mathbb R)}\,ds
 \leq 2\sqrt{mT\,\mathbb E D_T^2}.
\tag{5}
\]

These statements reduce pathwise uniqueness to the vanishing of (2) for
every admissible pair and every deterministic \(T\). No vanishing estimate
for (2) is asserted here. To obtain indistinguishability on all finite
times, apply the equivalence for each positive integer \(T\) and intersect
the resulting countably many probability-one events.

The equivalence concerns almost-sure statements for the whole pair.
Equality of terminal masses merely on a positive-probability event does
not imply equality of fields on that event.

## 1. The single-solution input and integration over space

Use the established single-solution identification with finite-measure
super-Brownian motion: each solution separately has continuous total mass
and

\[
\mathbb E U_t=\mathbb E V_t=m,\qquad t\geq0.
\tag{6}
\]

This is an input about each marginal law, not a uniqueness assertion about
the coupling \((u,v,W)\). The weak uniqueness of the density equation is
part of the known setting of T423. Its connection to the usual
super-Brownian martingale problem is discussed in Yu-Ting Chen,
[arXiv:1308.5141](https://arxiv.org/abs/1308.5141), equations (1.1) and
(1.7) and the paragraph following (1.8), and in Jie Xiong,
[arXiv:1203.4873](https://arxiv.org/abs/1203.4873), the introduction to the
super-Brownian martingale problem. Only (6) and mass continuity are used
from that identification. In particular, no strong uniqueness result for
a distribution-function SPDE is used.

The weak formulation of the mild equation, for a compactly supported
smooth test function \(\phi\), is

\[
\langle u_t,\phi\rangle
 =\langle u_0,\phi\rangle
 +\frac12\int_0^t\langle u_s,\phi''\rangle\,ds
 +\int_0^t\int_{\mathbb R}\phi(x)\sqrt{u_s(x)}\,W(ds,dx).
\tag{7}
\]

It follows by testing the mild equation and applying deterministic and
stochastic Fubini; the expected integrated mass on every finite interval
is finite by (6), so the bounded test integrands are square integrable.
The heat semigroup identity
\(P_t\phi-\phi=\frac12\int_0^tP_s\phi''\,ds\) gives the drift in (7).

To justify the test function \(1\), choose \(\chi\in C_c^\infty(\mathbb R)\)
with \(0\leq\chi\leq1\), \(\chi=1\) on \([-1,1]\), and \(\chi=0\) outside
\([-2,2]\). Put \(\chi_R(x)=\chi(x/R)\). The drift in (7) satisfies

\[
\mathbb E\sup_{t\leq T}\left|
 \frac12\int_0^t\langle u_s,\chi_R''\rangle\,ds\right|
 \leq\frac{\|\chi''\|_\infty mT}{2R^2}\longrightarrow0.
\tag{8}
\]

The stochastic integrals converge to the stochastic integral with
integrand \(\sqrt u\), uniformly in time in \(L^2\), because Doob's
inequality and Itô isometry give an upper bound

\[
4\mathbb E\int_0^T\int_{\mathbb R}
 (1-\chi_R(x))^2u_s(x)\,dx\,ds\longrightarrow0.
\tag{9}
\]

Dominated convergence applies: the integrand is bounded by \(u_s(x)\),
whose integral over probability, time, and space is \(mT\). At each
fixed time, \(\langle u_t,\chi_R\rangle\to U_t\) almost surely and in
\(L^1\). Thus (7)--(9), first at rational times and then by continuity of
the mass and stochastic integral, imply the process identity

\[
U_t=m+\int_0^t\int_{\mathbb R}\sqrt{u_s(x)}\,W(ds,dx).
\tag{10}
\]

The same argument gives

\[
V_t=m+\int_0^t\int_{\mathbb R}\sqrt{v_s(x)}\,W(ds,dx).
\tag{11}
\]

In particular, \(U-m\) and \(V-m\) are square-integrable continuous
martingales on every finite interval. Their brackets are

\[
\langle U\rangle_t=\int_0^tU_s\,ds,\quad
\langle V\rangle_t=\int_0^tV_s\,ds,\quad
\langle U,V\rangle_t=\int_0^tC_s\,ds.
\tag{12}
\]

The last identity uses the fact that the white noise in (10) and (11) is
the same. Cauchy--Schwarz gives

\[
0\leq C_s\leq\sqrt{U_sV_s}\leq\tfrac12(U_s+V_s),\qquad
0\leq A_s\leq U_s+V_s.
\tag{13}
\]

Consequently \(\mathbb E\int_0^T A_s\,ds\leq2mT\).

## 2. Terminal mass determines equality on the whole interval

Subtracting (11) from (10) gives

\[
D_t=\int_0^t\int_{\mathbb R}
 (\sqrt{u_s(x)}-\sqrt{v_s(x)})\,W(ds,dx),\qquad
\langle D\rangle_t=\int_0^t A_s\,ds.
\tag{14}
\]

Itô isometry proves the first identity in (3). Thus \(U_T=V_T\) almost
surely if and only if condition 3 holds.

If condition 3 holds, the nonnegative random variable
\(\int_0^T\int(\sqrt u-\sqrt v)^2\,dx\,ds\) is zero almost surely.
On each sample path in this probability-one event for which the fields
are continuous, \(u=v\) for Lebesgue-almost every \((s,x)\). If the fields
differed at any point of \((0,T)\times\mathbb R\), continuity would give
a nonempty open rectangle on which they differ. The integral in (14)
would then be strictly positive, a contradiction. Continuity extends
equality to \(s=T\); equality at \(s=0\) is the common initial condition.
This proves condition 1. Condition 1 immediately implies condition 2.

For a second derivation of the energy identity, (10)--(12) give

\[
\mathbb E U_T^2=\mathbb E V_T^2=m^2+mT,
\qquad
\mathbb E(U_TV_T)=m^2+\mathbb E\int_0^T C_s\,ds.
\]

Expanding \(\mathbb E(U_T-V_T)^2\) therefore yields

\[
\mathbb E D_T^2
 =2mT-2\mathbb E\int_0^TC_s\,ds
 =\mathbb E\int_0^T A_s\,ds,
\tag{15}
\]

in agreement with (14). In particular, every nonidentical admissible
pair on \([0,T]\) must have unequal terminal masses with positive
probability; having unequal profiles while retaining identical mass
paths is impossible.

The marginal coefficient \(mT\) has a separate Laplace-transform check.
For \(\lambda>0\), put
\(q_s=\lambda/(1+(T-s)\lambda/2)\), \(0\leq s\leq T\).
Then \(q_s'=q_s^2/2\). Applying Itô formula to
\(\exp(-q_sU_s)\), with (12), cancels the two drift terms:
\(-q_s^2U_s\exp(-q_sU_s)/2\) from the time derivative and
\(+q_s^2U_s\exp(-q_sU_s)/2\) from the second derivative in \(U_s\).
The resulting stochastic integral has mean zero, since \(q_s\leq\lambda\)
and its expected quadratic variation is at most \(\lambda^2mT\).
Consequently

\[
\mathbb E e^{-\lambda U_T}
 =\exp\left(-\frac{m\lambda}{1+T\lambda/2}\right).
\]

Expansion at zero gives the coefficients \(-m\) and
\((m^2+mT)/2\), hence the first moment \(m\) and second moment
\(m^2+mT\), consistently with the isometry calculation. The second
moment is already known finite from (10), so this differentiation is
justified. The same check applies to \(V_T\).

## 3. An exact occupation identity, including its finite-width error

Normalize symmetric local time by Tanaka's formula

\[
|D_t|=\int_0^t\operatorname{sgn}(D_s)\,dD_s+L_t^0(D),
\qquad \operatorname{sgn}(0)=0.
\tag{16}
\]

The stochastic integral has mean zero because
\(\mathbb E\langle D\rangle_T<\infty\) and the sign function is bounded.
Taking expectations in (16) gives

\[
\mathbb E L_T^0(D)=\mathbb E|D_T|.
\tag{17}
\]

To prove the occupation limit without interchanging an unbounded
approximation with expectation, introduce the convex \(C^1\) function

\[
F_\varepsilon(z)=
\begin{cases}
 z^2/(2\varepsilon),& |z|\leq\varepsilon,\\
 |z|-\varepsilon/2,& |z|\geq\varepsilon.
\end{cases}
\tag{18}
\]

Its derivative is bounded by one, \(F_\varepsilon(0)=0\), and its
second derivative almost everywhere is
\(\varepsilon^{-1}\mathbf1_{\{|z|<\varepsilon\}}\).
The generalized Itô formula, valid for \(C^1\) functions with locally
absolutely continuous derivative, gives

\[
\mathbb E F_\varepsilon(D_T)
 =\frac1{2\varepsilon}\mathbb E\int_0^T
  \mathbf1_{\{|D_s|<\varepsilon\}}A_s\,ds
 =Q_\varepsilon(T).
\tag{19}
\]

The martingale term has mean zero by the same square-integrability
argument as in (16). The values assigned to the second derivative at
\(\pm\varepsilon\) do not matter, since the occupation formula implies
\(\int_0^T\mathbf1_{\{D_s=a\}}\,d\langle D\rangle_s=0\) at each
fixed level \(a\).

For every real \(z\), (18) gives

\[
0\leq |z|-F_\varepsilon(z)\leq\varepsilon/2.
\tag{20}
\]

Indeed, outside the central interval the difference is exactly
\(\varepsilon/2\); inside, its value is
\(|z|-|z|^2/(2\varepsilon)\), which increases from zero to
\(\varepsilon/2\). Equations (19)--(20) prove (4) and the occupation
identity in (3). Equations (17) and (3) establish the equivalence of
conditions 2, 4, and 5, since all the random quantities whose expectations
vanish are nonnegative.

A separate smooth check fixes the factor \(1/2\). Apply ordinary Itô
formula to \(G_\delta(z)=\sqrt{z^2+\delta^2}-\delta\). Then

\[
\mathbb E G_\delta(D_T)
 =\frac12\mathbb E\int_0^T
  \frac{\delta^2}{(D_s^2+\delta^2)^{3/2}}A_s\,ds.
\tag{21}
\]

Since \(0\leq |z|-G_\delta(z)\leq\delta\), the right side converges
to \(\mathbb E|D_T|\). Moreover

\[
\int_{\mathbb R}\frac12
 \frac{\delta^2}{(z^2+\delta^2)^{3/2}}\,dz=1,
\]

as follows by differentiating
\(z/\sqrt{z^2+\delta^2}\). This agrees with the unit integral of the
box kernel \((2\varepsilon)^{-1}\mathbf1_{\{|z|<\varepsilon\}}\).

## 4. Quantitative spatial control

Put \(S_s=U_s+V_s\) and \(B_s=\|u_s-v_s\|_1\). Spatial
Cauchy--Schwarz yields

\[
\begin{aligned}
B_s^2
 &=\left(\int|\sqrt{u_s}-\sqrt{v_s}|
                    (\sqrt{u_s}+\sqrt{v_s})\,dx\right)^2\\
 &\leq A_s\int(\sqrt{u_s}+\sqrt{v_s})^2\,dx\\
 &=A_s(S_s+2C_s)\leq2S_sA_s.
\end{aligned}
\tag{22}
\]

Define \(B_s^2/(2S_s)=0\) when \(S_s=0\), which is legitimate because
nonnegativity then implies that both fields vanish. It follows that

\[
\mathbb E\int_0^T\frac{B_s^2}{2S_s}\,ds
 \leq\mathbb E D_T^2.
\tag{23}
\]

Another Cauchy--Schwarz inequality, now on probability times time, gives

\[
\begin{aligned}
\mathbb E\int_0^TB_s\,ds
 &\leq\left(\mathbb E\int_0^T A_s\,ds\right)^{1/2}
       \left(\mathbb E\int_0^T2S_s\,ds\right)^{1/2}\\
 &=2\sqrt{mT\,\mathbb E D_T^2},
\end{aligned}
\]

which proves (5). The algebraic factor 2 in \(B_s^2\leq2S_sA_s\)
cannot be decreased uniformly over profiles: for a nonnegative smooth
function \(f\) of integral one, profiles \(u=c^2f,v=d^2f\) give

\[
\frac{\|u-v\|_1^2}{(\int u+\int v)\int(\sqrt u-\sqrt v)^2}
 =\frac{(c+d)^2}{c^2+d^2}\longrightarrow2
\]

as \(c/d\to1\) through \(c\neq d\). This is sharpness of the
deterministic inequality; it is not a claim of sharpness over SPDE
solution pairs in (5).

## 5. What the reduction does not supply

A sufficient remaining estimate is, for every admissible pair and \(T\),

\[
\mathbb E\int_0^T
 \mathbf1_{\{|U_s-V_s|<\varepsilon\}}A_s\,ds=o(\varepsilon).
\tag{24}
\]

Equations (2)--(4) show that (24) is also necessary. It is not a
consequence of the elementary inequalities in (13).

The available unconditional bound has exactly linear order. Indeed,
\(|D_T|\leq U_T+V_T\), (6), and (15) imply
\(\mathbb E|D_T|\leq\min\{2m,\sqrt{2mT}\}\). Multiplying (4) by
\(2\varepsilon\) gives

\[
2\varepsilon\mathbb E|D_T|-\varepsilon^2
 \leq\mathbb E\int_0^T
     \mathbf1_{\{|D_s|<\varepsilon\}}A_s\,ds
 \leq2\varepsilon\mathbb E|D_T|
 \leq2\varepsilon\min\{2m,\sqrt{2mT}\}.
\tag{24a}
\]

Thus any nonidentical admissible pair would have a strictly positive
linear coefficient in this occupation integral. The missing step is the
improvement from \(O(\varepsilon)\) to \(o(\varepsilon)\).

For example, let \(f\in C_c^\infty(\mathbb R)\) be nonnegative, supported
in \([-1,1]\), and of integral one; put \(g(x)=f(x-4)\). For profiles
\(a=mf,b=mg\), with \(m>0\), the masses are equal while

\[
\int(\sqrt a-\sqrt b)^2\,dx=2m.
\tag{25}
\]

Even among nearby equal-mass profiles, put
\(b_\theta=m((1-\theta)f+\theta g)\), \(0<\theta<1\). Then

\[
\|a-b_\theta\|_1=2m\theta,\qquad
\int(\sqrt a-\sqrt{b_\theta})^2\,dx
 =2m(1-\sqrt{1-\theta})>0.
\tag{26}
\]

Thus no bound of the form \(A\leq K\omega(|U-V|)\), with
\(\omega(0)=0\), can hold for arbitrary nonnegative smooth profiles,
even when the profiles are close. These profiles are not asserted to
occur as a same-noise solution pair. Their role is to disprove an
algebraic shortcut to (24).

Likewise, projecting the common white noise to each population does not
produce the same scalar Brownian motion. On times when \(U_s,V_s>0\),
the normalized mass martingale increments have instantaneous correlation

\[
\rho_s=\frac{C_s}{\sqrt{U_sV_s}}.
\tag{27}
\]

Equality \(\rho_s=1\) requires equality in spatial Cauchy--Schwarz,
equivalently \(u_s/U_s=v_s/V_s\) almost everywhere. This is additional
information about the pair. Scalar Feller-diffusion pathwise uniqueness
cannot be applied by silently identifying these projected drivers.

Finally, if \(m=0\), (6) and nonnegativity imply that both fields vanish
at all rational times almost surely, and continuity gives equality
everywhere. No division by a possibly zero mass was used in the main
reduction. Infinite random extinction times cannot replace the finite
deterministic \(T\) without a new uniform-integrability argument.
