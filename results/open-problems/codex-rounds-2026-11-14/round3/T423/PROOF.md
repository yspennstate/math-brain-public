# A terminal extinction criterion for the density SPDE

Let u and v be a fixed pair of solutions in T423, on the same filtered
probability space, with the same white noise and deterministic initial
density. Set

\[
m=\int u_0(x)\,dx,\quad U_t=\int u_t(x)\,dx,\quad
V_t=\int v_t(x)\,dx,\quad D_t=U_t-V_t,
\]
\[
S_t=U_t+V_t,\quad C_t=\int\sqrt{u_t(x)v_t(x)}\,dx,\quad
A_t=\int(\sqrt{u_t(x)}-\sqrt{v_t(x)})^2\,dx=S_t-2C_t.
\tag{1}
\]
All spatial integrals are over the real line. Equality of fields on an
interval means equality at every time and spatial point outside one null
event. The input about each marginal solution is the usual finite-measure
super-Brownian law: the total mass is continuous and has expectation m at
every time. No Markov property in the joint filtration is assumed.

For T>0 let

\[
E_T=\{U_T=0<V_T\}\mathbin{\cup}\{V_T=0<U_T\},\qquad
\delta_T=\mathbb P(E_T).
\tag{2}
\]

**Proposition.** For each deterministic T>0 the following are equivalent:

1. The fields agree on [0,T].
2. Their terminal extinction indicators agree almost surely:
   \(\mathbf1_{\{U_T=0\}}=\mathbf1_{\{V_T=0\}}\).
3. \(\delta_T=0\).

There is an exact energy identity. For 0<=s<T put

\[
q_s=\frac{2}{T-s},\qquad p_s^u=e^{-q_s U_s},\qquad
p_s^v=e^{-q_s V_s}.
\]
Then

\[
\boxed{\displaystyle
\delta_T=\mathbb E\int_0^T q_s^2
 \int\big(p_s^u\sqrt{u_s(x)}-p_s^v\sqrt{v_s(x)}\big)^2\,dx\,ds.}
\tag{3}
\]
The integral in (3) is defined as the increasing limit of the integrals
up to r<T; its expectation is finite.

There is also a quantitative version before a mass cap. For 0<t<T,
K>m, and

\[
\tau_K=\inf\{s\geq0:U_s\vee V_s\geq K\},\qquad
\sigma=t\wedge\tau_K,
\]
with infimum of the empty set equal to infinity, one has

\[
\boxed{\displaystyle
\mathbb E\int_0^\sigma A_s\,ds
\leq\frac{T^2}{4}\exp\!\left(\frac{4K}{T-t}\right)\delta_T.}
\tag{4}
\]

**Corollary.** The fixed pair is indistinguishable for all times if and
only if

\[
\liminf_{T\longrightarrow\infty}T\delta_T=0.
\tag{5}
\]
Every pair satisfies

\[
0\leq\delta_T\leq
2\min\{e^{-2m/T},\,1-e^{-2m/T}\}\leq\frac{4m}{T}.
\tag{6}
\]
For every fixed t>0,

\[
\liminf_{T\longrightarrow\infty}T\delta_T
\geq 2\mathbb E\big[S_t\mathbf1_{E_t}\big].
\tag{7}
\]
If the fields fail to agree on [0,t], then \(\delta_t>0\), so the right
side of (7) is strictly positive.

The proposition and corollary are reductions. Neither terminal extinction
synchrony nor (5) is established for arbitrary same-noise pairs.

## 1. Independent verification of the mass reduction

The mass identities can be obtained directly from the mild equation.
Write \(P_r\) for the heat semigroup with generator
\(\tfrac12\partial_{xx}\). Choose smooth compactly supported functions
\(\chi_R\) with values in [0,1] and \(\chi_R(x)\to1\) for every x.
For example use \(\chi_R(x)=\chi(x/R)\), where \(\chi=1\) near zero.
Testing the mild equation at a fixed time a gives

\[
\langle u_a,\chi_R\rangle
=\langle u_0,P_a\chi_R\rangle
+\int_0^a\int P_{a-s}\chi_R(y)\sqrt{u_s(y)}\,W(ds,dy).
\tag{8}
\]
Stochastic Fubini in (8) is justified, for fixed R, by

\[
\int |\chi_R(x)|
\left(\mathbb E\int_0^a\int
 p_{a-s}(x-y)^2u_s(y)\,dy\,ds\right)^{1/2}dx<\infty.
\]
Indeed, Cauchy--Schwarz on the support of \(\chi_R\), followed by
Tonelli, bounds the square of the left side by

\[
\|\chi_R\|_2^2\int_0^a
\frac{m}{2\sqrt{\pi(a-s)}}\,ds<\infty,
\]
since the heat kernel satisfies
\(\int p_r(x-y)^2dx=1/(2\sqrt{\pi r})\). This argument also gives the
needed square-integrable stochastic convolution after spatial testing.

Now \(0\leq P_{a-s}\chi_R\leq1\), and these functions converge to one
for s<a and every y. Therefore Itô isometry and dominated convergence give

\[
\mathbb E\int_0^a\int
 |P_{a-s}\chi_R(y)-1|^2u_s(y)\,dy\,ds\longrightarrow0,
\]
using \(\mathbb E\int_0^a U_sds=ma\). The initial term in (8) tends to
m, while its left side tends almost surely to \(U_a\), by finite mass.
Thus

\[
U_a=m+\int_0^a\int\sqrt{u_s(x)}\,W(ds,dx).
\tag{9}
\]
First take (9) simultaneously at all nonnegative rational times.
Continuity of the mass and of the square-integrable stochastic integral
then gives it as a process identity. The same proof applies to v.

In the actual joint filtration, U-m and V-m are consequently continuous
square-integrable martingales on finite intervals, with

\[
d\langle U\rangle_s=U_sds,\quad
d\langle V\rangle_s=V_sds,\quad
d\langle U,V\rangle_s=C_sds.
\tag{10}
\]
Nonnegativity and Cauchy--Schwarz imply
\(0\leq C_s\leq\sqrt{U_sV_s}\leq S_s/2\), so
\(0\leq A_s\leq S_s\) and \(\mathbb E\int_0^a A_sds\leq2ma\).
Subtracting the two identities (9) gives

\[
D_a=\int_0^a\int(\sqrt{u_s}-\sqrt{v_s})\,W(ds,dx),\qquad
\mathbb E D_a^2=\mathbb E\int_0^a A_s\,ds.
\tag{11}
\]
Thus equality of terminal masses almost surely is equivalent to equality
of fields on the whole preceding interval: a zero expectation on the
right forces its nonnegative space-time integrand to vanish almost
everywhere on almost every path. Joint continuity then forces equality
at every point in the interior. Continuity extends it to the terminal
time, and the initial fields already agree.

For an independent coefficient check, (9)--(10) imply

\[
\mathbb E U_a^2=\mathbb E V_a^2=m^2+ma,\qquad
\mathbb E U_aV_a=m^2+\mathbb E\int_0^a C_sds.
\]
Expansion of \(\mathbb E(U_a-V_a)^2\) gives
\(2ma-2\mathbb E\int_0^a C_sds\), agreeing with (11).

The preceding occupation calculation has an independent verification.
Normalize local time by
\(|D_a-b|=|b|+\int_0^a\operatorname{sgn}(D_s-b)dD_s+L_a^b\).
The stochastic integral has mean zero by (11). Average expectations
over \(b\in[-\varepsilon,\varepsilon]\), and apply the occupation
formula and Tonelli. This gives

\[
\frac1{2\varepsilon}\mathbb E\int_0^a
 \mathbf1_{\{|D_s|<\varepsilon\}}A_sds
=\mathbb E\left[\frac1{2\varepsilon}
 \int_{-\varepsilon}^{\varepsilon}
 (|D_a-b|-|b|)db\right]=\mathbb E F_\varepsilon(D_a),
\]
where direct integration gives

\[
F_\varepsilon(z)=
\begin{cases}
z^2/(2\varepsilon),&|z|\leq\varepsilon,\\
|z|-\varepsilon/2,&|z|\geq\varepsilon.
\end{cases}
\]
For every z, \(0\leq |z|-F_\varepsilon(z)\leq\varepsilon/2\).
Thus the preceding local-time normalization and finite-width error hold.

## 2. Conditional extinction in the joint filtration

Fix T>0 and \(\lambda>0\). For 0<=s<=T define

\[
b_s=\frac{\lambda}{1+(T-s)\lambda/2}.
\]
Then \(b_s'=b_s^2/2\). By (9)--(10), Itô's formula gives

\[
d(e^{-b_sU_s})=-b_s e^{-b_sU_s}\,dU_s.
\tag{12}
\]
The drift vanishes: the time derivative contributes
\(-b_s^2U_se^{-b_sU_s}/2\), and the second derivative contributes its
negative. The stochastic integral is a true square-integrable martingale
on [0,T], since

\[
\mathbb E\int_0^T b_s^2 e^{-2b_sU_s}U_sds\leq\lambda^2mT.
\]
Consequently, for every t<T,

\[
\mathbb E[e^{-\lambda U_T}\mid\mathcal F_t]
=\exp\!\left(-\frac{\lambda U_t}{1+(T-t)\lambda/2}\right).
\tag{13}
\]
This proves a conditional identity in the joint filtration, directly
from the stochastic equation. It is stronger than merely invoking the
one-dimensional marginal distribution of U.

Let \(\lambda\uparrow\infty\) through the integers. Bounded conditional
monotone convergence in (13) yields

\[
\mathbb P(U_T=0\mid\mathcal F_t)
=e^{-2U_t/(T-t)}=p_t^u.
\tag{14}
\]
The same argument gives \(p_t^v\) for V. In particular, at time zero,

\[
\mathbb P(U_T=0)=\mathbb P(V_T=0)=e^{-2m/T}.
\tag{15}
\]
The initial sigma field need not be trivial: deterministic initial mass
m suffices for (15).

If the two terminal extinction indicators agree almost surely, their
conditional expectations agree at every fixed t<T. Since
\(a\mapsto e^{-2a/(T-t)}\) is strictly decreasing on [0,infinity),
\(U_t=V_t\) almost surely at each such t. Apply this at all rational
t<T and use mass continuity to obtain equality of mass paths on [0,T],
including T. Equation (11) then gives equality of the fields on [0,T].
The reverse implication is immediate. This proves the equivalences in
the proposition without a terminal-limit argument.

## 3. The exact binary energy identity

Let \(X_T=\mathbf1_{\{U_T=0\}}\),
\(Y_T=\mathbf1_{\{V_T=0\}}\), and
\(N_s=p_s^u-p_s^v\) for s<T. Equation (14) says that
\(N_s=\mathbb E[X_T-Y_T\mid\mathcal F_s]\), and N_0=0.
On any interval [0,r] with r<T, differentiate as in (12), now with
\(q_s=2/(T-s)\). Again \(q_s'=q_s^2/2\), so

\[
dN_s=-q_s\int
(p_s^u\sqrt{u_s(x)}-p_s^v\sqrt{v_s(x)})\,W(ds,dx).
\tag{16}
\]
For fixed r<T, the expected bracket is finite, since q is bounded on
[0,r], both p's are at most one, and

\[
G_s:=\int(p_s^u\sqrt{u_s}-p_s^v\sqrt{v_s})^2dx
=(p_s^u)^2U_s+(p_s^v)^2V_s-2p_s^up_s^vC_s\leq S_s.
\tag{17}
\]
Isometry gives

\[
\mathbb E N_r^2=\mathbb E\int_0^r q_s^2G_sds.
\tag{18}
\]

To pass to T, note that mass continuity makes \(U_T,V_T\), and hence
\(X_T-Y_T\), measurable with respect to
\(\mathcal F_{T-}=\sigma(\bigcup_{s<T}\mathcal F_s)\).
Conditional-expectation martingale convergence gives
\(N_r\to X_T-Y_T\) in L2 as r increases to T. Equivalently, this follows
by convergence of orthogonal projections onto the increasing L2 spaces
of \(\mathcal F_r\)-measurable variables. This step does not assume the
absence of an atom at extinction time T, or interchange a singular
coefficient with a stochastic integral.

Taking limits in (18), by L2 convergence on the left and monotone
convergence on the right, proves (3), since
\((X_T-Y_T)^2=\mathbf1_{E_T}\).

An independent derivation checks the cross-term and normalization.
Apply the product formula to \(p_s^up_s^v\) up to r<T. Its expected
increment is

\[
\mathbb E[p_r^up_r^v]-e^{-4m/T}
=\mathbb E\int_0^r q_s^2p_s^up_s^vC_sds.
\]
The square formula for each individual martingale gives

\[
\mathbb E[(p_r^u)^2]-e^{-4m/T}
=\mathbb E\int_0^r q_s^2(p_s^u)^2U_sds,
\]
and the corresponding identity for v. Subtract twice the product
formula from the two square formulas and pass to T. The terminal
quantity is
\(\mathbb E X_T+\mathbb E Y_T-2\mathbb E X_TY_T=\delta_T\),
and the integrand is exactly (17) multiplied by \(q_s^2\).
All three limiting expectations are finite, since the martingales take
values in [0,1].

## 4. Quantitative control up to a mass cap

For deterministic \(a,b\in[0,K]\) and q>0, the mean value theorem gives

\[
|e^{-qa}-e^{-qb}|\geq q e^{-qK}|a-b|.
\tag{19}
\]
At \(\sigma=t\wedge\tau_K\), continuity and K>m give
\(U_\sigma,V_\sigma\leq K\), while

\[
\frac2T\leq q_\sigma\leq\frac2{T-t}.
\]
Hence (19) implies

\[
|N_\sigma|\geq\frac2T e^{-2K/(T-t)}|D_\sigma|.
\tag{20}
\]
The bounded martingale N is closed by \(X_T-Y_T\), so optional sampling
or conditional Jensen gives
\(\mathbb E N_\sigma^2\leq\mathbb E(X_T-Y_T)^2=\delta_T\).
The stopped version of (11) gives
\(\mathbb E D_\sigma^2=\mathbb E\int_0^\sigma A_sds\).
Square (20), rearrange, and take expectations to obtain (4).

There is a second check on the factor in (4). For fixed q, the inverse
map of \(a\mapsto e^{-qa}\), restricted to [0,K], has derivative in
absolute value at most \(e^{qK}/q\). For
\(q\in[2/T,2/(T-t)]\), this is at most
\((T/2)e^{2K/(T-t)}\). Squaring gives the coefficient in (4).
This estimate is intentionally not claimed sharp. Its growth with K
prevents an unconditional estimate obtained merely by sending K to
infinity when \(\delta_T>0\).

## 5. Absorption and the large-time disagreement criterion

The nonnegative martingale U has zero as an absorbing state. For fixed
0<=t<T,

\[
\mathbb E[\mathbf1_{\{U_t=0\}}U_T]
=\mathbb E[\mathbf1_{\{U_t=0\}}U_t]=0.
\]
Thus \(U_T=0\) almost surely on \(\{U_t=0\}\). The same holds for V.
For the fixed-time argument below this is enough; absorption at all
subsequent times also follows by using rational times and continuity.

On E_t, exactly one mass is positive, and the zero mass remains zero at
T. Equation (14) therefore gives

\[
\mathbb P(E_T\cap E_t)
=\mathbb E\left[\mathbf1_{E_t}
 \left(1-e^{-2S_t/(T-t)}\right)\right].
\tag{21}
\]
In particular, \(\delta_T\) is at least the right side. For each finite
S>=0 and fixed t,

\[
T(1-e^{-2S/(T-t)})\longrightarrow2S.
\]
For T>=2t this quantity lies between zero and 4S, by
\(1-e^{-z}\leq z\). Since \(\mathbb E S_t=2m\), dominated convergence
in (21) proves (7).

To check this factor a second way, use the exact expression

\[
T(1-e^{-2S/(T-t)})
=\frac{2TS}{T-t}\int_0^1e^{-2\theta S/(T-t)}d\theta.
\]
Its limit is 2S, with the same integrable upper bound 4S when T>=2t.

For the upper bound, X_T and Y_T have the same Bernoulli mean
\(p=e^{-2m/T}\), by (15). Their disagreement implies either that at
least one equals one, or that at least one equals zero. The two union
bounds give \(\delta_T\leq2p\) and \(\delta_T\leq2(1-p)\).
The elementary exponential bound gives \(2(1-p)\leq4m/T\). This proves
(6). Independently, expanding
\(\delta_T=\mathbb E(X_T-Y_T)^2=2p-2\mathbb E(X_TY_T)\)
and using \(\max(0,2p-1)\leq\mathbb E(X_TY_T)\) gives the same
Bernoulli bounds.

If the fields agree for all times, then \(\delta_T=0\) for every T, so
(5) holds. Conversely, if they are not indistinguishable, some finite
integer n has a positive probability of field disagreement on [0,n].
The proposition gives \(\delta_n>0\). On E_n the variable S_n is
strictly positive; it is integrable, so
\(0<\mathbb E[S_n\mathbf1_{E_n}]\leq2m\). Equation (7) now contradicts
(5). This proves the corollary. Countably many integer horizons and
joint continuity justify the indistinguishability statement.

## 6. Limits of the criterion

The new missing estimate is extinction synchrony at a deterministic
horizon, or equivalently the global condition (5). The automatic bound
is \(\delta_T=O(T^{-1})\); no little-o improvement is proved. No common
scalar Brownian driver for U and V is presumed.

The integrand in (3) cannot be replaced by a positive deterministic
multiple of A for arbitrary profiles. Let f be a smooth nonnegative
profile of integral one, set u=f and v=4f, and choose
\(q=(\log 2)/3\). The masses are 1 and 4, and

\[
e^{-q}\sqrt u=e^{-4q}\sqrt v,
\qquad
\int(\sqrt u-\sqrt v)^2dx=1.
\]
Indeed, \(e^{3q}=2\), so the two weighted square roots coincide.
Thus the weighted energy density can vanish although A is positive.
These are deterministic test profiles, not a constructed SPDE pair.
The proof of the criterion uses the conditional martingales and the
injective map on masses, not pointwise coercivity of this integrand.

The equal-mass disjoint-profile obstruction from the preceding report
also persists: if both masses equal a, then the weighted discrepancy in
(17) is \(e^{-2qa}A\), which need not vanish. Equality of extinction
probabilities at one instant alone says nothing about equality of the
profiles at that instant. The proposition assumes equality almost
surely of the *terminal events*, and then uses their conditional
expectations at every earlier time.

If m=0, nonnegativity and the first moment imply that both masses and
fields vanish, using rational times and continuity. All displayed
identities remain valid. No division by a possibly vanishing mass is
used. No optional stopping at an unbounded extinction time is used.
Immigration would invalidate the absorbing-zero argument in section 5
and the conditional law (14) for the critical branching mass.
