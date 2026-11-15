# Local time after the first small-mass entrance

Let u,v be a fixed pair in T423, with the same white noise and initial
density. All spatial integrals are over the real line. Write

\[
m=\int u_0,\quad U_t=\int u_t,\quad V_t=\int v_t,\quad
D_t=U_t-V_t,\quad M_t=\min(U_t,V_t),
\]
\[
C_t=\int\sqrt{u_tv_t},\qquad
A_t=\int(\sqrt{u_t}-\sqrt{v_t})^2=U_t+V_t-2C_t.
\tag{1}
\]

Let L be symmetric local time at zero of D, normalized by

\[
|D_t|=\int_0^t\operatorname{sgn}(D_s)\,dD_s+L_t,
\qquad \operatorname{sgn}(0)=0.
\tag{2}
\]

For a>0 define

\[
\tau_a=\inf\{t\geq0:M_t\leq a\},\qquad b=\min(m,a).
\tag{3}
\]

**Theorem.** The time \(\tau_a\) is finite almost surely, and

\[
\mathbb E(L_\infty-L_{\tau_a})\leq2b.
\tag{4}
\]

For every deterministic finite T, with \(\sigma=T\wedge\tau_a\), the
more precise identity is

\[
\mathbb E(L_T-L_\sigma)
=2b\,\mathbb P(\tau_a\leq T)
 -2\mathbb E[M_T\mathbf1_{\{\tau_a\leq T\}}].
\tag{5}
\]

For every \(\varepsilon>0\) and \(0<T\leq\infty\),

\[
\boxed{\displaystyle
\mathbb E\int_0^T
 \mathbf1_{\{|D_s|<\varepsilon,\ M_s\leq a\}}A_s\,ds
\leq4b\varepsilon+\varepsilon^2.}
\tag{6}
\]

In particular, taking \(a=\varepsilon\) bounds this integral by
\(5\varepsilon^2\), uniformly over the entire lifetime. Thus total masses
on the scale of the occupation window cannot account for a positive
linear occupation coefficient.

There is also the local-time bound

\[
\mathbb E\int_0^\infty\mathbf1_{\{M_s\leq a\}}\,dL_s
\leq2b.
\tag{7}
\]

The bounds do not prove pathwise uniqueness. They localize its remaining
occupation estimate to positive total masses.

## 1. Mass identities and integrability

The marginal input is the usual finite-measure super-Brownian law for
each solution separately: U,V have continuous paths and
\(\mathbb E U_t=\mathbb E V_t=m\). This is the same input used in the
earlier reports. No Markov property in the joint filtration is inferred
from a marginal law.

For completeness, take smooth compactly supported \(\chi_R\), between
zero and one, tending pointwise to one. Testing the mild equation at
fixed t with \(\chi_R\) gives a stochastic integrand
\(P_{t-s}\chi_R(x)\sqrt{u_s(x)}\). Here P has generator
\(\tfrac12\partial_{xx}\). Stochastic Fubini is justified by
Cauchy--Schwarz and

\[
\|\chi_R\|_2^2\int_0^t
 \frac{m}{2\sqrt{\pi(t-s)}}\,ds<\infty,
\]

which bounds the square of the spatial integral of the L2 norm of the
tested stochastic convolution. Since \(0\leq P_{t-s}\chi_R\leq1\),
Ito isometry and domination by
\(\mathbb E\int_0^tU_sds=mt\) let R tend to infinity. The left side
converges almost surely by finite mass, and the deterministic initial
term converges to m. First doing this at rational times and then using
continuity gives

\[
U_t=m+\int_0^t\int\sqrt{u_s(x)}\,W(ds,dx),\qquad
V_t=m+\int_0^t\int\sqrt{v_s(x)}\,W(ds,dx).
\tag{8}
\]

They are square-integrable martingales on every finite interval in the
actual common filtration, with

\[
d\langle U\rangle_s=U_sds,\quad
d\langle V\rangle_s=V_sds,\quad
d\langle U,V\rangle_s=C_sds,\quad
d\langle D\rangle_s=A_sds.
\tag{9}
\]

Since \(0\leq C_s\leq\sqrt{U_sV_s}\leq(U_s+V_s)/2\),
one has \(0\leq A_s\leq U_s+V_s\). Consequently

\[
\mathbb E D_T^2=\mathbb E\int_0^T A_sds\leq2mT,\qquad
\mathbb E L_T=\mathbb E|D_T|\leq2m.
\tag{10}
\]

The stochastic term in (2) has mean zero because its expected bracket
is finite. Monotone convergence in L gives
\(\ell:=\mathbb E L_\infty\leq2m\), and \(L_\infty<\infty\)
almost surely.

Each mass is absorbed at zero. This follows from nonnegativity and the
martingale property, first after bounded stopping times and then by
localization, using rational future times and continuity.
They reach zero in finite time almost surely. To check this last
assertion without a common scalar driver, fix t and \(\theta>0\).
Ito applied to
\(\exp[-q_sU_s]\), where
\(q_s=\theta/[1+(t-s)\theta/2]\), cancels the drift since
\(q_s'=q_s^2/2\). The martingale term is square integrable, bounded in
expected bracket by \(\theta^2mt\). Thus

\[
\mathbb E e^{-\theta U_t}
=\exp\!\left(-\frac{m\theta}{1+t\theta/2}\right),\qquad
\mathbb P(U_t=0)=e^{-2m/t}.
\tag{11}
\]

The second identity follows as \(\theta\) increases to infinity.
Absorption makes the events of extinction by integer time increasing;
their probabilities tend to one. The same applies to V. Therefore
\(\tau_a<\infty\) almost surely. If \(a<m\), continuity gives
\(M_{\tau_a}=a\); if \(a\geq m\), then \(\tau_a=0\) and
\(M_{\tau_a}=m\). In both cases \(M_{\tau_a}=b\).

The square identity in (10) also gives the earlier reduction:
\(\mathbb E L_T=0\) if and only if \(D_T=0\) almost surely, which
is equivalent to \(\mathbb E\int_0^TA_sds=0\). The latter forces
u=v on the full interval by joint continuity. Countably many integer
intervals give indistinguishability for all time.

## 2. The minimum and bounded optional sampling

The occupation formula gives
\(\int_0^T\mathbf1_{\{D_s=0\}}d\langle D\rangle_s=0\).
Thus the martingale \(\int\mathbf1_{\{D=0\}}dD\) has zero bracket.
The choice of U or V in a stochastic integral at a tie is immaterial.
Using \(M=(U+V-|D|)/2\) in (2) gives

\[
M_t=m+N_t-\tfrac12L_t,\qquad
N_t=\int_0^t\mathbf1_{\{U_s\leq V_s\}}dU_s
    +\int_0^t\mathbf1_{\{U_s>V_s\}}dV_s.
\tag{12}
\]

The two sets in N are disjoint, so
\(d\langle N\rangle_s=M_sds\).
In particular
\(\mathbb E\langle N\rangle_T\leq mT\), and N is a true
square-integrable martingale on every finite interval.

Fix deterministic T and set
\(\sigma=T\wedge\tau_a\), \(B=\{\tau_a\leq T\}\).
The event B belongs to \(\mathcal F_\sigma\): for \(t<T\),
\(B\cap\{\sigma\leq t\}=\{\tau_a\leq t\}\), and for \(t\geq T\)
it belongs to \(\mathcal F_T\).
Bounded optional sampling for N gives

\[
\mathbb E[\mathbf1_B(N_T-N_\sigma)]=0.
\]

All terms are integrable. Indeed, \(M_t\leq U_t+V_t\) has finite
second moments at bounded stopping times, and (12) then also bounds
L at those times in L2.
Subtract (12) at \(\sigma\) from its value at T and multiply by
\(\mathbf1_B\). On B, \(M_\sigma=b\). On its complement,
\(\sigma=T\), so every increment is zero. Taking expectations yields

\[
\mathbb E(L_T-L_\sigma)
=2\mathbb E[\mathbf1_B(M_\sigma-M_T)],
\]

which is exactly (5). Its right side is at most \(2b\mathbb P(B)\).
Its left side is nonnegative.

As T increases, \(L_T-L_{T\wedge\tau_a}\) increases to
\(L_\infty-L_{\tau_a}\). Monotone convergence proves (4).
No optional sampling at an unbounded time, and no uniform integrability
at infinity, have been used.

Before \(\tau_a\), \(M>a\), so any contribution to the integral in
(7) is after \(\tau_a\). L is continuous and hence has no atom at
\(\tau_a\). Equation (4) therefore proves (7).

## 3. The occupation estimate at finite width

For \(\varepsilon>0\), define the convex C1 function

\[
F_\varepsilon(z)=
\begin{cases}
z^2/(2\varepsilon),& |z|\leq\varepsilon,\\
|z|-\varepsilon/2,& |z|\geq\varepsilon .
\end{cases}
\qquad
0\leq |z|-F_\varepsilon(z)\leq\varepsilon/2.
\tag{13}
\]

Its derivative is bounded by one and is locally absolutely continuous.
For every stopping time \(\rho\leq T\), generalized Ito and (9) give

\[
Q_\varepsilon(\rho):=\frac1{2\varepsilon}
 \int_0^\rho\mathbf1_{\{|D_s|<\varepsilon\}}A_sds,\qquad
\mathbb E Q_\varepsilon(\rho)
=\mathbb E F_\varepsilon(D_\rho)
=\mathbb E L_\rho-e_\rho,
\tag{14}
\]

where \(e_\rho=\mathbb E(|D_\rho|-F_\varepsilon(D_\rho))\)
satisfies \(0\leq e_\rho\leq\varepsilon/2\).
The stochastic integrals have mean zero by (10) and bounded optional
sampling. Values of the second derivative at the two boundary levels
do not matter by the occupation formula.

Because \(M_s>a\) for \(s<\tau_a\), the low-mass integral satisfies
the pathwise inequality

\[
\frac1{2\varepsilon}\int_0^T
 \mathbf1_{\{|D_s|<\varepsilon,\ M_s\leq a\}}A_sds
\leq Q_\varepsilon(T)-Q_\varepsilon(T\wedge\tau_a).
\tag{15}
\]

Changing a time-integral endpoint has no effect.
Subtract (14) at T and at \(T\wedge\tau_a\), then use (5):

\[
\begin{aligned}
\mathbb E[Q_\varepsilon(T)-Q_\varepsilon(T\wedge\tau_a)]
&=\mathbb E(L_T-L_{T\wedge\tau_a})
       -e_T+e_{T\wedge\tau_a}\\
&\leq2b+\varepsilon/2.
\end{aligned}
\tag{16}
\]

Multiplying (15)--(16) by \(2\varepsilon\) proves (6) for finite T.
The integrands are nonnegative, so monotone convergence proves it for
\(T=\infty\) with the same constant.
There is no limiting argument for an occupation integral carrying a
discontinuous random weight.

## 4. The remaining criterion at a positive mass floor

Fix finite T. Equation (14) gives the exact stopped limit

\[
\lim_{\varepsilon\downarrow0}
\frac1{2\varepsilon}\mathbb E\int_0^{T\wedge\tau_a}
 \mathbf1_{\{|D_s|<\varepsilon\}}A_sds
=\mathbb E L_{T\wedge\tau_a},
\qquad
0\leq \mathbb E L_T-\mathbb E L_{T\wedge\tau_a}\leq2b.
\tag{17}
\]

For comparison, write \(Q_\varepsilon^{>a}(T)\) for the normalized
integral on \(\{|D_s|<\varepsilon,M_s>a\}\). Splitting the full
integral and using (6), (14) yields

\[
\max(0,\mathbb E L_T-2b)
\leq\liminf_{\varepsilon\downarrow0}
       \mathbb E Q_\varepsilon^{>a}(T)
\leq\limsup_{\varepsilon\downarrow0}
       \mathbb E Q_\varepsilon^{>a}(T)
\leq\mathbb E L_T.
\tag{18}
\]

Consequently, for any positive deterministic sequence \(a_n\downarrow0\),
field equality through T is equivalent to

\[
\mathbb E\int_0^T
 \mathbf1_{\{|D_s|<\varepsilon,\ M_s>a_n\}}A_sds
=o(\varepsilon)
\quad\hbox{for every }n.
\tag{19}
\]

Indeed, equality makes the full occupation limit zero. Conversely,
(18) and (19) imply \(\mathbb E L_T\leq2a_n\) for every n,
and hence \(\mathbb E L_T=0\).
The same equivalence follows from the stopped condition in (17).

Let \(\delta_T=\mathbb P(U_T=0<V_T\ \text{or}\ V_T=0<U_T)\).
Combining (4) with the round 4 coefficient, checked in LOG.md, gives
the useful approximation

\[
0\leq
\lim_{T\to\infty}T\delta_T-2\mathbb E L_{\tau_a}
=2\mathbb E(L_\infty-L_{\tau_a})\leq4b.
\tag{20}
\]

Thus all but \(4a\) of that coefficient is determined before either
mass first falls to a.

## 5. Independent check and limitations

There is a second proof of the factor in (7) that does not use
\(\tau_a\). For \(\eta>0\), take the increasing concave C1 function

\[
f_{a,\eta}(x)=
\begin{cases}
x,&0\leq x\leq a,\\
a+(x-a)-(x-a)^2/(2\eta),&a<x<a+\eta,\\
a+\eta/2,&x\geq a+\eta .
\end{cases}
\tag{21}
\]

Its derivative is one on \([0,a]\), tapers linearly to zero,
and then vanishes. Extend it linearly to negative x if needed for
Ito's formula. From (12),

\[
\mathbb E f_{a,\eta}(M_T)
=f_{a,\eta}(m)
 -\frac1{2\eta}\mathbb E\int_0^T
        \mathbf1_{\{a<M_s<a+\eta\}}M_sds
 -\frac12\mathbb E\int_0^T f'_{a,\eta}(M_s)dL_s.
\tag{22}
\]

The stochastic integral has mean zero since \(|f'|\leq1\).
Both drift terms are nonpositive, and \(f\geq0\) on the range of M.
Since \(f'=1\) on \([0,a]\) and
\(f(m)\leq\min(m,a+\eta/2)\), (22) implies

\[
\mathbb E\int_0^T\mathbf1_{\{M_s\leq a\}}dL_s
\leq2\min(m,a+\eta/2).
\]

Letting \(\eta\) decrease to zero, then T increase to infinity,
recovers (7), including its endpoint convention.
This separately checks the half-local-time drift and the coefficient
2 in the budget. The error \(\varepsilon^2\) in (6) is checked
independently by averaging \(|z-r|-|r|\) over
\(r\in[-\varepsilon,\varepsilon]\); that average is precisely
\(F_\varepsilon(z)\) and its difference from \(|z|\) is between
zero and \(\varepsilon/2\).

When m=0, the first-moment input and nonnegativity give identically
zero fields, so every claim holds. For \(a\geq m\), \(\tau_a=0\)
and (5) reduces to
\(\mathbb E L_T=2m-2\mathbb E M_T\), as also follows directly
from \(|D_T|=U_T+V_T-2M_T\). After the first extinction,
M remains zero; its martingale bracket in (12) vanishes and L is
constant. In particular extinction itself creates no jump of L.

Finite-width occupation can nevertheless continue after the first
extinction. This checks the otherwise easy-to-miss error term in (6).
For a scalar Feller mass X started at c>0, paired with an identically
zero mass, define the bounded nonnegative C1 function
\[
g_\varepsilon(x)=
\begin{cases}
2\varepsilon x-x^2,&0\leq x\leq\varepsilon,\\
\varepsilon^2,&x\geq\varepsilon.
\end{cases}
\]
Its generator is
\((x/2)g_\varepsilon''(x)=-x\mathbf1_{\{0<x<\varepsilon\}}\).
Ito on a finite interval and then bounded convergence, since
X eventually vanishes, give
\[
\mathbb E\int_0^\infty
 \mathbf1_{\{0<X_s<\varepsilon\}}X_sds
=g_\varepsilon(c)
=2\varepsilon(c-F_\varepsilon(c)).
\]
This equals \(\varepsilon^2\) when \(c\geq\varepsilon\), although
the local time of the nonnegative mass difference at zero is zero.
It is a scalar check, not an admissible pair with the prescribed common
SPDE initial value. It explains why a finite-width remainder must be
retained even when the subsequent local-time increment vanishes.

It would be invalid to send T to infinity in the last term of (5)
using only almost-sure extinction. The variables
\(M_T\mathbf1_{\{\tau_a\leq T\}}\) need not be uniformly integrable.
For the identical coupling \(U=V\), L is zero, but this expectation
equals \(b\mathbb P(\tau_a\leq T)\) and tends to b. Thus equality
in (4) is not asserted.

The factor 2 is also checked by independent scalar Feller diffusions
started at a. Then \(\tau_a=0\), and independence gives
\[
\mathbb E\min(U_t,V_t)
\leq\mathbb E[U_t\mathbf1_{\{V_t>0\}}]
=a(1-e^{-2a/t})\longrightarrow0.
\]
Hence \(\mathbb E L_\infty=2a\), attaining (4) in the broader class
of coupled Feller mass martingales. The identical coupling instead
gives zero. These examples do not construct spatial solution pairs.
The constant 2 is not claimed optimal over actual spatial pairs.
The bound \(5\varepsilon^2\) follows solely from
\(4\min(m,\varepsilon)\varepsilon+\varepsilon^2\);
it is not an asymptotic formula.
None of (4)--(20) controls local time at equal positive masses.
There the two spatial profiles can still differ and their signed
differences can cancel in the total mass. Proving (19), or its
stopped version, for arbitrary actual solution pairs remains open.
