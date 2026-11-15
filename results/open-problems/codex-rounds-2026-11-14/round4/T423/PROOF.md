# The exact coefficient of extinction disagreement

Let u,v be a fixed pair of solutions in T423 on the same filtered
probability space and driven by the same space-time white noise. All
spatial integrals below are over the real line. Put

\[
m=\int u_0(x)\,dx,\qquad U_t=\int u_t(x)\,dx,\qquad
V_t=\int v_t(x)\,dx,\qquad D_t=U_t-V_t,
\]
\[
C_t=\int\sqrt{u_t(x)v_t(x)}\,dx,\qquad
A_t=\int(\sqrt{u_t(x)}-\sqrt{v_t(x)})^2\,dx
=U_t+V_t-2C_t.
\tag{1}
\]

Write

\[
\delta_T=\mathbb P\big(\{U_T=0<V_T\}\cup\{V_T=0<U_T\}\big).
\tag{2}
\]

Normalize symmetric local time L at zero of D by

\[
|D_t|=\int_0^t\operatorname{sgn}(D_s)\,dD_s+L_t,
\qquad \operatorname{sgn}(0)=0.
\tag{3}
\]

**Theorem.** The finite number

\[
\ell:=\mathbb E L_\infty
=\lim_{t\to\infty}\mathbb E|U_t-V_t|\in[0,2m]
\tag{4}
\]

is well defined, and

\[
\boxed{\displaystyle\lim_{T\to\infty}T\delta_T=2\ell.}
\tag{5}
\]

For every fixed \(\lambda>0\), one also has

\[
\lim_{T\to\infty}
T\mathbb E\big|e^{-\lambda U_T/T}-e^{-\lambda V_T/T}\big|
=\frac{2\lambda}{\lambda+2}\ell,
\tag{6}
\]

and, for every T>0,

\[
\left|T\delta_T-
T\mathbb E\big|e^{-\lambda U_T/T}-e^{-\lambda V_T/T}\big|\right|
\leq\frac{8m}{\lambda+2}.
\tag{7}
\]

Consequently the pair is indistinguishable for all times if and only
if the limit in (5) is zero. The theorem identifies the coefficient;
it does not prove that the coefficient vanishes.

## 1. Mass martingales and the earlier reductions

The single-solution input, as in the preceding reductions, is the
finite-measure super-Brownian marginal law: U and V have continuous
paths and \(\mathbb E U_t=\mathbb E V_t=m\). This is an input about
each marginal, not a Markov assertion in the joint filtration. All
joint martingale identities used below follow from the given white noise.

Here is a justification for testing the mild equation against one.
Let \(\chi_R\) be smooth compactly supported functions taking values
in [0,1] and tending pointwise to one. For fixed a>0, testing the mild
equation gives

\[
\langle u_a,\chi_R\rangle
=\langle u_0,P_a\chi_R\rangle
+\int_0^a\int P_{a-s}\chi_R(x)\sqrt{u_s(x)}\,W(ds,dx),
\tag{8}
\]

where P is the heat semigroup with generator one half of the Laplacian.
Stochastic Fubini is legitimate: the square of the integral of
\(|\chi_R(y)|\) times the L2 norm of the stochastic convolution at y
is bounded, by Cauchy--Schwarz and Tonelli, by

\[
\|\chi_R\|_2^2\int_0^a\frac{m}{2\sqrt{\pi(a-s)}}\,ds<\infty.
\]

This uses \(\int p_r(y-x)^2dy=1/(2\sqrt{\pi r})\).
Since \(0\leq P_{a-s}\chi_R\leq1\) and it tends to one for s<a,
dominated convergence and Ito isometry imply convergence of the
stochastic term in (8) in L2 to the integral with integrand sqrt(u).
The domination is \(\mathbb E\int_0^a U_sds=ma\).
The left side tends almost surely to U_a by finite mass, and the
initial term tends to m. Apply this at all rational a and use mass
continuity to obtain the process identities

\[
U_t=m+\int_0^t\int\sqrt{u_s(x)}\,W(ds,dx),\qquad
V_t=m+\int_0^t\int\sqrt{v_s(x)}\,W(ds,dx).
\tag{9}
\]

They are square-integrable martingales on each finite interval, with

\[
d\langle U\rangle_s=U_sds,\quad
d\langle V\rangle_s=V_sds,\quad
d\langle U,V\rangle_s=C_sds,\quad
d\langle D\rangle_s=A_sds.
\tag{10}
\]

The inequalities
\(0\leq C_s\leq\sqrt{U_sV_s}\leq(U_s+V_s)/2\) imply
\(0\leq A_s\leq U_s+V_s\). In particular,

\[
\mathbb E D_t^2=\mathbb E\int_0^t A_sds\leq2mt.
\tag{11}
\]

Independently, (9)--(10) give
\(\mathbb E U_t^2=\mathbb E V_t^2=m^2+mt\) and
\(\mathbb E U_tV_t=m^2+\mathbb E\int_0^t C_sds\).
Expanding the square of the difference recovers (11), including its
normalization.

Thus U_t=V_t almost surely at a deterministic t>0 is equivalent to
field equality on [0,t]. Indeed, zero in (11) makes the nonnegative
space-time integral defining its right side zero almost surely.
Joint continuity forces equality at all interior points and then at
the endpoints. A nonzero continuous difference at an interior point
would give a neighborhood of positive integral, a contradiction.

For later use derive the conditional Laplace transform directly in
the joint filtration. Fix T>0 and theta>0 and put

\[
b_s=\frac{\theta}{1+(T-s)\theta/2},\qquad 0\leq s\leq T.
\tag{12}
\]

Then \(b'_s=b_s^2/2\). Ito's formula and (10) show that
\(e^{-b_sU_s}\) has differential
\(-b_se^{-b_sU_s}dU_s\): its two drift terms cancel.
The stochastic integral is square integrable since b<=theta and
its expected bracket is at most \(\theta^2mT\). Therefore

\[
\mathbb E[e^{-\theta U_T}\mid\mathcal F_t]
=\exp\left(-\frac{\theta U_t}{1+(T-t)\theta/2}\right).
\tag{13}
\]

The same formula holds for V. In particular,

\[
\mathbb E e^{-\theta U_T}
=\exp\left(-\frac{m\theta}{1+T\theta/2}\right),\qquad
\mathbb P(U_T=0)=\mathbb P(V_T=0)=e^{-2m/T}.
\tag{14}
\]

The extinction formula follows by bounded monotone convergence as
theta increases to infinity. For t<T the same conditional limit gives
\(\mathbb P(U_T=0\mid\mathcal F_t)=e^{-2U_t/(T-t)}\).
Equality almost surely of the two terminal extinction indicators
therefore forces U_t=V_t at each earlier rational t, by strict
monotonicity of this exponential. Mass continuity and (11) give field
equality on [0,T]. This verifies the preceding binary criterion in
the actual joint filtration.

Taking expectations in (3) is justified by (11). It gives
\(\mathbb E L_t=\mathbb E|D_t|\leq2m\). Since L is continuous and
nondecreasing, monotone convergence proves (4). In particular L_infinity
is finite almost surely. This does not assert uniform integrability
of D over unbounded times.

## 2. An absolute Laplace-difference identity

Set \(M_t=\min(U_t,V_t)\) and \(J_t=\max(U_t,V_t)\).
The occupation formula implies

\[
\int_0^t\mathbf1_{\{D_s=0\}}\,d\langle D\rangle_s=0.
\tag{15}
\]

Indeed, applying that formula to the indicator of the singleton zero
gives an integral over a set of Lebesgue measure zero in the local-time
variable. Consequently the stochastic integral
\(\int_0^t\mathbf1_{\{D_s=0\}}dD_s\) has zero bracket and is zero.
Tanaka's formula for \((U+V-|D|)/2\) and its counterpart with a plus
sign therefore give

\[
\begin{aligned}
dM_s&=\mathbf1_{\{U_s\leq V_s\}}dU_s
      +\mathbf1_{\{U_s>V_s\}}dV_s-\tfrac12dL_s,\\
dJ_s&=\mathbf1_{\{U_s>V_s\}}dU_s
      +\mathbf1_{\{U_s\leq V_s\}}dV_s+\tfrac12dL_s.
\end{aligned}
\tag{16}
\]

The choice of which martingale to use at a tie makes no difference
by (15). The two indicator sets in each line are disjoint. Thus their
martingale parts have brackets

\[
d\langle M\rangle_s=M_sds,\qquad
d\langle J\rangle_s=J_sds.
\tag{17}
\]

Local time at zero is carried by \(\{s:D_s=0\}\). On this set,
\(M_s=J_s=U_s=V_s\).

Use b from (12) and apply Ito's formula to
\(f(s,x)=e^{-b_sx}\), first at M and then at J. Since
\(f_s+(x/2)f_{xx}=0\), (17) cancels both ordinary drifts. The finite
variation terms in (16) contribute, respectively,

\[
\tfrac12b_se^{-b_sM_s}dL_s
\quad\hbox{and}\quad
-\tfrac12b_se^{-b_sJ_s}dL_s.
\]

Subtract the second formula from the first. The difference of the
functions is
\(e^{-b_sM_s}-e^{-b_sJ_s}=|e^{-b_sU_s}-e^{-b_sV_s}|\).
It starts at zero because the initial masses agree. The martingale
terms have zero expectation: their derivatives are bounded by theta,
and \(\mathbb E\int_0^T(M_s+J_s)ds=2mT\).
The finite variation terms are integrable since their absolute values
sum to at most \(\theta L_T\). On the support of dL the two half terms
sum to \(b_se^{-b_sU_s}dL_s\). This proves the exact identity

\[
\boxed{\displaystyle
\mathbb E|e^{-\theta U_T}-e^{-\theta V_T}|
=\mathbb E\int_0^T b_se^{-b_sU_s}\,dL_s.}
\tag{18}
\]

## 3. Large-time limit with a finite Laplace parameter

Fix lambda>0 and set theta=lambda/T in (18). For clarity write

\[
b_s^{T,\lambda}
=\frac{\lambda}{T+(T-s)\lambda/2},\qquad 0\leq s\leq T.
\tag{19}
\]

For all such s, \(0\leq T b_s^{T,\lambda}\leq\lambda\).
For each fixed finite s and each path with finite U_s,

\[
T b_s^{T,\lambda}e^{-b_s^{T,\lambda}U_s}
\longrightarrow\frac{2\lambda}{\lambda+2}.
\tag{20}
\]

Define the measure nu on probability times [0,infinity) by integration
against \(dL_s\) and then expectation. Its total mass is ell, at most
2m. Extend the integrand in (20) to be zero for s>T. It is bounded
by lambda on this entire measure space and converges pointwise at
every finite s outside a null set where the mass paths fail to be
finite and continuous. Dominated convergence against nu in (18)
now proves (6). This argument handles the full real limit T to
infinity, or equivalently every sequence of positive T tending to
infinity. There is no exchange with a singular extinction kernel.

## 4. Uniform approximation of extinction indicators

Put \(X_T=\mathbf1_{\{U_T=0\}}\) and
\(Y_T=\mathbf1_{\{V_T=0\}}\). For any theta>0,
\(e^{-\theta U_T}\geq X_T\). The reverse triangle inequality gives

\[
\left|\mathbb E|X_T-Y_T|
-\mathbb E|e^{-\theta U_T}-e^{-\theta V_T}|\right|
\leq2\left(\mathbb E e^{-\theta U_T}-e^{-2m/T}\right).
\tag{21}
\]

The equality of the marginal laws was used only on the right.
Since \(\mathbb E|X_T-Y_T|=\delta_T\), set theta=lambda/T and use
(14) to write the right side as

\[
2\left(\exp\left[-\frac{2m}{T}\frac{\lambda}{\lambda+2}\right]
-\exp\left[-\frac{2m}{T}\right]\right).
\]

For \(0\leq a\leq b\),
\(0\leq e^{-a}-e^{-b}=\int_a^be^{-r}dr\leq b-a\).
Applying this with
\(a=(2m/T)\lambda/(\lambda+2)\), \(b=2m/T\), and multiplying
by T proves (7).

To finish, apply (6)--(7) at a fixed lambda. They imply

\[
\limsup_{T\to\infty}|T\delta_T-2\ell|
\leq\frac{8m+4\ell}{\lambda+2}
\leq\frac{16m}{\lambda+2}.
\tag{22}
\]

Let lambda tend to infinity. The right side tends to zero, which
proves (5). The two limits are taken in the stated order.

If ell=0, (4) implies \(D_t=0\) almost surely for every deterministic
t. Equation (11) gives field equality on every integer horizon.
Their countable intersection is indistinguishability for all times.
Conversely, indistinguishability gives D=0 and ell=0. This proves
the final assertion of the theorem, also when m=0.

## 5. Independent checks and scope

There is a separate derivation of the lower half of (5). Conditional
Jensen and (13) at the infinite parameter give, for 0<t<T,

\[
\delta_T\geq
\mathbb E\left|e^{-2U_t/(T-t)}-e^{-2V_t/(T-t)}\right|.
\tag{23}
\]

After multiplication by T the integrand tends to \(2|D_t|\).
For T>=2t it is bounded by \(4|D_t|\), by the mean value theorem
and \(|(e^{-qx})'|\leq q\). Thus dominated convergence gives
\(\liminf T\delta_T\geq2\mathbb E|D_t|\).
Letting t increase to infinity proves the lower bound 2ell in (5)
without the min/max calculation. It improves the earlier lower bound
that retained only the event where exactly one earlier mass is zero.

The normalization in (18) also follows by an independent local-time
change of variables. For finite theta, let
\(N_s=e^{-b_sU_s}-e^{-b_sV_s}\). It is a continuous martingale.
Write N=-HD, where
\(H_s=b_s\int_0^1e^{-b_s(V_s+rD_s)}dr>0\).
This is a smooth function of s,U_s,V_s and hence a continuous
semimartingale. Apply the product formula to H|D| and use (3).
Its terms other than H dL agree with the signed terms in Tanaka's
formula for HD: use D*sgn(D)=|D| and
\(d[H,|D|]_s=\operatorname{sgn}(D_s)d[H,D]_s\).
It follows that \(dL_s^0(N)=H_s dL_s\).
On the support of dL, H equals \(b_se^{-b_sU_s}\).
Taking expectations in Tanaka for N now gives (18). This verifies
the factor independently of (16)--(17).

Three scalar coupling examples check the coefficient independently.
They concern mass martingales, not constructed density-SPDE pairs.

* If U=V, both sides of (5) vanish.
* If U,V are independent critical Feller diffusions, each starting at
  m, their extinction disagreement is
  \(2e^{-2m/T}(1-e^{-2m/T})\), so its scaled limit is 4m. Independence
  gives \(\mathbb E\min(U_t,V_t)\leq
  \mathbb E[U_t\mathbf1_{\{V_t>0\}}]=m(1-e^{-2m/t})\to0\).
  Hence \(\mathbb E|D_t|=2m-2\mathbb E\min(U_t,V_t)\to2m\),
  agreeing with (5).
* Let X,Y,Z be independent critical Feller diffusions with initial
  masses a,b,b, and put U=X+Y, V=X+Z. The two marginal initial masses
  are m=a+b. Their extinction disagreement is
  \(2e^{-2(a+b)/T}(1-e^{-2b/T})\), whose scaled limit is 4b.
  Here D=Y-Z, so the preceding independent calculation gives ell=2b.
  This checks intermediate coefficients, including b=0 and a=0.

The marginal Laplace parameter in (19) is essential. In the formal
infinite-parameter version of (18), multiplication by T gives the
kernel \(2T/(T-s)\exp[-2U_s/(T-s)]\). It is not bounded uniformly
over s<T. Finiteness of \(\mathbb E L_\infty\) alone does not justify
dominated convergence for this kernel. Equations (19)--(21) supply a
bounded kernel first and a uniform error afterwards.

Although both masses become zero eventually almost surely, this does
not force ell=0: even the independent Feller example has ell=2m.
No unbounded-time optional stopping or uniform integrability of D is
used. No rate of convergence in (5) is asserted. For actual spatial
pairs, proving ell=0 remains exactly the unresolved step.
