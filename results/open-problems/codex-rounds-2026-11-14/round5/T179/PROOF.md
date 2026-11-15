# A nonanticipating H-valued drift

Let \(H=L^2(\mathbb T;\mathbb R)\), where \(\mathbb T=\mathbb R/\mathbb Z\)
has mass one, and let \(S_t=e^{t\Delta}\). Fix \(T<\infty\) and a
deterministic \(h\in H\). Suppose
\[
0<\beta<1,\qquad |g(z)-g(y)|\le L|z-y|^\beta,
\qquad |g(z)|\ge c>0.                                      \tag{1}
\]
The function \(g\) need not be bounded. Write
\(\mathcal X=C([0,T];H)\), \(X_t(\omega)=\omega_t\), and
\(\mathcal F_t^X=\sigma(X_s:0\le s\le t)\), without completion.
The stopped path is \(\omega^t_s=\omega_{s\wedge t}\).

Assume the following drift-free input:

**(D)** From \(h\), the equation with coefficient \(g\) and zero drift has
a weak mild solution with continuous \(H\) paths and a unique state-path
law \(\mu_0\) on \(\mathcal X\).

The round-3 proof supplies (D) for every \(h\in H\), conditional on
bounded-start uniqueness. That external input is Proposition 8.1 of
Yi Han, *Weak uniqueness for the stochastic heat equation with nondegenerate
diffusion: the full Hölder regime*,
[arXiv:2611.07310v1](https://arxiv.org/html/2611.07310v1).
Han's Proposition 8.5 gives the Girsanov transfer for a pointwise drift.
Here the drift may depend on the past and may act nonlocally in space.
No part of the main bounded-start uniqueness theorem is proved below.

Let \(B:[0,T]\times\mathcal X\to H\) be jointly Borel, with
\[
B(t,\omega)=B(t,\omega^t),\qquad
\|B(t,\omega)\|_2\le K(1+\|\omega_t\|_2)                    \tag{2}
\]
for every \((t,\omega)\), for a finite constant \(K\).
A weak solution is a continuous adapted \(H\)-valued process and a
cylindrical Brownian motion \(W\) on \(H\) such that
\[
U_t=S_th+\int_0^tS_{t-s}B(s,U)\,ds
             +\int_0^tS_{t-s}M_{g(U_s)}\,dW_s.               \tag{3}
\]
Only the history through \(s\) is used in \(B(s,U)\). When \(U\) is
not defined beyond the current time, its stopped continuous extension gives
the same value. The deterministic integral is a Bochner integral. A
predictable version of the stochastic coefficient used below will be
constructed explicitly.

**Theorem.** Under (1), (2), and (D), equation (3) has a weak solution and
a unique state-path law \(\mu_B\). This law is equivalent to \(\mu_0\).
There is a Borel function \(J_B:\mathcal X\to\mathbb R\) such that
\[
\frac{d\mu_B}{d\mu_0}=D_B
 =\exp\{J_B-A_B/2\},\qquad
A_B(\omega)=\int_0^T
 \left\|\frac{B(s,\omega)}{g(\omega_s)}\right\|_2^2ds.        \tag{4}
\]
Both entropies are finite, and
\[
\operatorname{Ent}(\mu_B\mid\mu_0)=\tfrac12E_{\mu_B}A_B,
\qquad
\operatorname{Ent}(\mu_0\mid\mu_B)=\tfrac12E_{\mu_0}A_B.      \tag{5}
\]
One common bound on the quantities in (5) is
\[
c^{-2}K^2T C_T(1+\|h\|_2^2),                               \tag{6}
\]
where, with \(G=|g(0)|+L\), one may take
\[
\begin{split}
a_1&=6(TK^2+G^2),& a_2&=6G^2/\sqrt{8\pi},\\
\lambda&=1+4a_1+16\pi a_2^2,& C_T&=6e^{\lambda T}.
\end{split}                                                \tag{7}
\]
Equivalently, \(\lambda=1+24(TK^2+G^2)+72G^4\): squaring \(a_2\)
gives \(16\pi a_2^2=72G^4\).
Uniqueness here concerns the state path. A Markov property for (3) is not
assumed or asserted.

## 1. A predictable representative on canonical path space

Condition (2) implies that \(s\mapsto B(s,\omega)\) is strongly measurable
and bounded on \([0,T]\), for every fixed continuous path \(\omega\).
Extend this function by zero for negative times and put
\[
B_n(t,\omega)=n\int_{(t-1/n)^+}^t B(s,\omega)\,ds.           \tag{8}
\]
These are Borel \(H\)-valued maps. For example, integrate their scalar
coordinates against a countable orthonormal basis of \(H\); measurable
integration gives Borel coordinates, and those coordinates generate the
Borel sigma field of separable \(H\).

For each fixed \(\omega\), (8) is continuous in \(t\), since it is the
difference of two indefinite Bochner integrals. For fixed \(t\), its value
depends only on \(\omega^t\): for \(s\le t\), nonanticipation gives
\(B(s,\omega)=B(s,\omega^t)\). The map \(\omega\mapsto\omega^t\)
is \(\mathcal F_t^X\)-measurable into \(\mathcal X\), as can be checked
on evaluations at rational times. Thus \(B_n\) is adapted and continuous,
and hence predictable for the raw canonical filtration.

Define \(\widetilde B(t,\omega)\) to be the \(H\)-limit of \(B_n(t,\omega)\)
when that limit exists, and zero otherwise. The Cauchy convergence set is
predictable, so \(\widetilde B\) is predictable and jointly Borel.
Bochner Lebesgue differentiation gives, separately for every path,
\[
\widetilde B(t,\omega)=B(t,\omega)
\quad\text{for Lebesgue-almost every }t.                    \tag{9}
\]
The one-sided differentiation theorem used here follows from the norm
Lebesgue differentiation theorem: approximate an integrable separable
Hilbert-valued function by continuous functions in \(L^1\), apply the
scalar one-sided maximal inequality to the norms of the errors, and let
the approximation errors tend to zero. It therefore applies to each
bounded strongly measurable path function above.

The growth bound is preserved at every point, not just almost everywhere.
Indeed for \(t>0\),
\[
\|B_n(t,\omega)\|_2
 \le K\left(1+\sup_{(t-1/n)^+\le s\le t}\|\omega_s\|_2\right).
\]
Continuity of \(\omega\) makes the right side tend to
\(K(1+\|\omega_t\|_2)\). If the limit exists it satisfies this bound;
otherwise the chosen value zero satisfies it. At \(t=0\) the value is zero.

For any adapted continuous \(U\), the pullback of a canonical predictable
rectangle is predictable in its ambient filtration: its past event at time
\(r\) depends only on \((U_s)_{s\le r}\). Consequently
\(\widetilde B(t,U)\) is predictable. Equation (9) holds for each sample
path, so replacing \(B\) by \(\widetilde B\) changes neither the drift
integral nor \(A_B\). This construction works under all probability laws
at once; it is not a completion chosen for a particular solution law.

In the rest of the proof use \(\widetilde B\), and omit its tilde.

## 2. Spatial representatives and the noise direction

All quotients in (4) are defined on \(L^2\) equivalence classes. An explicit
jointly Borel representative is
\[
R(v,x)=\lim_{n\to\infty}S_{1/n}v(x)
\]
when this limit is finite, and zero otherwise. For each \(v\in H\), heat
approximation at Lebesgue points shows \(R(v,x)=v(x)\) almost everywhere.
The maps before the limit are jointly continuous for each fixed \(n\).
Applying \(R\) to \(B(t,\omega)\) and \(\omega_t\) gives predictable
spatial representatives and defines
\[
\theta(t,\omega)(x)=\frac{B(t,\omega)(x)}{g(\omega_t(x))},
\qquad q(t,\omega)(x)=\frac{B(t,\omega)(x)}{g(\omega_t(x))^2}.
                                                               \tag{10}
\]
They are predictable \(H\)-valued maps: measurable integration gives Borel
coordinates, and ellipticity bounds their norms. In particular
\[
\|\theta(t,\omega)\|_2^2
 \le 2c^{-2}K^2(1+\|\omega_t\|_2^2),\qquad
g(\omega_t)\theta(t,\omega)=B(t,\omega)\quad\text{a.e.}       \tag{11}
\]
The energy \(A_B\) is a finite Borel function on all of \(\mathcal X\),
because each continuous path has bounded \(H\) norm on this horizon.
Measurable integration proves the Borel assertion. Formula (9) shows that
this energy agrees exactly with the one defined from the original \(B\).

Multiplication by \(g(v)\) is used before heat smoothing. It need not be
a bounded operator on \(H\). For \(k\in H\) and \(r>0\),
\[
\|S_r M_k\|_{\rm HS}^2=p_{2r}(0)\|k\|_2^2,
\qquad p_{2r}(0)\le1+(8\pi r)^{-1/2}.                       \tag{12}
\]
The identity follows by integrating the square of the heat kernel in
the output variable. For the bound, use
\(p_{2r}(0)=1+2\sum_{j\ge1}e^{-8\pi^2j^2r}\) and dominate the sum by
the integral of its decreasing Gaussian summand over \([0,\infty)\).

## 3. A moment estimate that tolerates history dependence

Consider any continuous-\(H\) mild solution with drift
\(\kappa_sB(s,U)\), for a predictable scalar process \(0\le\kappa\le1\).
The probability measure and Brownian motion may be arbitrary. We claim
\[
\sup_{t\le T}E(1+\|U_t\|_2^2)
 \le C_T(1+\|h\|_2^2),\qquad
EA_B(U)\le 2c^{-2}K^2TC_T(1+\|h\|_2^2).                    \tag{13}
\]
Since \(|z|^\beta\le1+|z|\),
\[
\|g(v)\|_2^2\le2G^2(1+\|v\|_2^2),\qquad
\|B(s,\omega)\|_2^2\le2K^2(1+\|\omega_s\|_2^2).             \tag{14}
\]
For \(R>\|h\|_2\) stop at \(\sigma_R=\inf\{t:\|U_t\|_2\ge R\}\)
and stop the two integrands in the mild equation:
\[
V_t^R=S_th+\int_0^t1_{s\le\sigma_R}S_{t-s}\kappa_sB(s,U)ds
       +\int_0^t1_{s\le\sigma_R}S_{t-s}M_{g(U_s)}dW_s.       \tag{15}
\]
This equals \(U_t\) for \(t\le\sigma_R\). In particular
\(1_{s\le\sigma_R}(1+\|U_s\|_2^2)\le1+\|V_s^R\|_2^2\).
There is no replacement of the full history \(U\) by \(V^R\) inside
\(B\); only its current-norm bound is used.

Let \(Y_R(t)=1+E\|V_t^R\|_2^2\). Heat contraction, the inequality for
the square of a sum of three vectors, Cauchy--Schwarz in the drift time
integral, stochastic isometry and (12), (14) give
\[
Y_R(t)\le1+3\|h\|_2^2+
 \int_0^t[a_1+a_2(t-s)^{-1/2}]Y_R(s)ds.                     \tag{16}
\]
For each fixed \(R\), the coefficients in (15) have bounded \(H\) norm,
so \(Y_R\) has finite supremum before the following absorption. Set
\(N_R=\sup_{t\le T}e^{-\lambda t}Y_R(t)\). Integrating the discounted
kernel over \((0,\infty)\) gives
\[
N_R\le1+3\|h\|_2^2+
 \left(a_1/\lambda+a_2\sqrt\pi/\sqrt\lambda\right)N_R.
\]
By (7), each kernel term is at most \(1/4\). Hence
\(Y_R(t)\le2e^{\lambda T}(1+3\|h\|_2^2)\).
Every continuous \(H\) path is bounded, so \(\sigma_R>T\) eventually
on each path. Fatou's lemma proves the first assertion in (13); integrating
(11) proves the second.

## 4. Normalizing both changes of measure

For a predictable \(H\)-valued direction \(\theta\) with finite energy,
write
\[
A_t=\int_0^t\|\theta_s\|_2^2ds,\quad
R_t=\exp\{\int_0^t\langle\theta_s,dW_s\rangle-A_t/2\},\quad
\tau_n=\inf\{t:A_t\ge n\}.                                  \tag{17}
\]
The exponential stopped at \(\tau_n\) is a martingale by Novikov, because
its bracket is bounded by \(n\). Put \(dQ_n=R_{T\wedge\tau_n}dP\).
If \(\sup_nE_{Q_n}A_T\le C\), then
\[
1\ge E_PR_T\ge E_P[R_T1_{A_T<n}]
 =Q_n(A_T<n)\ge1-C/n.                                      \tag{18}
\]
The first inequality is the nonnegative local-martingale inequality;
the equality uses agreement of the stopped and full densities on that
event. Thus \(E_PR_T=1\). The supermartingale inequalities then give
constant expectation at every earlier time, and conditional expectation
shows \(R\) is a martingale. Its terminal value is finite and strictly
positive because the energy is finite. Cylindrical Girsanov therefore
applies on the full interval, with equivalent measures.

Start with a drift-free realization \((X,W)\) under \(P\), and use
\(\theta_s=\theta(s,X)\). Under \(Q_n\),
\(W^n=W-\int_0^{\cdot\wedge\tau_n}\theta_sds\) is Brownian, and \(X\)
has drift \(1_{s\le\tau_n}B(s,X)\). This is exactly a drift multiplier
covered by (13), so \(\sup_nE_{Q_n}A_T<\infty\). Equations (17), (18)
give a full density \(R_T\). Under \(dQ=R_TdP\),
\(W^B=W-\int_0^\cdot\theta(s,X)ds\) is Brownian and \(X\) solves (3).

For precision, these substitutions do not presume changed-measure moments.
For smooth spatial tests they follow from the scalar semimartingale
change-of-integrator rule and \(g\theta=B\). At fixed \(t\), the heat
stochastic integrands have finite local square integral by (12), (14)
and the boundedness of the sample path's \(H\) norm. Localize at
\(\sigma_R\); the stopped integrands have bounded \(H\) norm, so finite
Fourier approximation and stochastic isometry give the mild identity.
The finite-variation correction is \(\int_0^tS_{t-s}B(s,X)ds\), which
exists pathwise by (2). Before \(\sigma_R\) the localized identity is the
desired one. Let \(R\to\infty\), first at rational times. The original
continuous state and the continuous deterministic convolution then provide
the continuous version of the new stochastic convolution. This proves the
changed mild equation before applying (13).

Conversely take any solution \((U,W)\) of (3) under \(P\). Use the reverse
exponential
\[
\widehat R_t=\exp\{-\int_0^t\langle\theta(s,U),dW_s\rangle
                           -A_t(U)/2\}.                    \tag{19}
\]
Under its stopped changes of measure the remaining drift is
\(1_{s>\tau_n}B(s,U)\). The same estimate (13) and argument (18) prove
\(E_P\widehat R_T=1\). Under \(d\widehat Q=\widehat R_TdP\),
\[
\widehat W=W+\int_0^\cdot\theta(s,U)ds                       \tag{20}
\]
is Brownian and \(U\) is drift-free. Its state law is \(\mu_0\) by (D).
This proves existence and removal of drift. A state-measurable inverse
density is still needed for uniqueness.

## 5. Constructing the density from the state alone

Under \(\mu_0\), for real smooth periodic \(\varphi\), put
\[
M_t(\varphi)=\langle X_t-h,\varphi\rangle
                 -\int_0^t\langle X_s,\Delta\varphi\rangle ds.
                                                               \tag{21}
\]
These are Borel functions of the path and square-integrable martingales
in the natural filtration. Their identities follow by conditioning those
of any drift-free realization on the state history. Their cross brackets are
\[
[M(\varphi),M(\psi)]_t
 =\int_0^t\!\int_{\mathbb T}g(X_s(x))^2\varphi(x)\psi(x)dxds. \tag{22}
\]
For bounded Borel \(\mathcal F_r^X\)-measurable \(\eta\), define
\[
I(\eta1_{(r,t]}\varphi)=\eta[M_t(\varphi)-M_r(\varphi)]
                                                               \tag{23}
\]
and extend by finite sums. These are Borel path functions. The martingale
isometry says
\[
E_{\mu_0}|I(v)-I(w)|^2
 =E_{\mu_0}\int_0^T\!\int g(X_s)^2|v-w|^2dxds.              \tag{24}
\]
This is a finite-measure \(L^2\) norm: by (13), (14),
\(m(d\omega,ds,dx)=g(X_s(x))^2\mu_0(d\omega)dsdx\) has finite total mass.
Predictable rectangles times spatial Borel sets generate its sigma field
up to the null time-zero set, so their simple functions are dense in
\(L^2(m)\). For any fixed predictable rectangle, integrating \(m\) over
that rectangle induces a finite Borel measure on the compact torus.
Continuous spatial functions are dense for that measure, and smooth
periodic functions are uniformly dense in continuous functions. Thus the
elementary functions in (23) are dense in the required predictable subspace.
No upper bound on \(g\) is used here.

For the predictable \(q\) of (10), its squared weighted norm is
\[
E_{\mu_0}\int g(X_s)^2q(s,X)^2dxds=E_{\mu_0}A_B<\infty.
\]
Choose elementary \(v_j\) converging to \(q\) in this norm. The integrals
\(I(v_j)\) converge in \(L^2(\mu_0)\); take a subsequence converging almost
surely too. Define \(J_B\) by its finite pointwise limit, and zero on the
Borel exceptional set where it does not converge finitely. This defines a
Borel function on all of \(\mathcal X\).

On every drift-free realization \((X,W)\) with this state law, (21), (23)
give
\(I(v_j)(X)=\int\langle g(X_s)v_j(s,X),dW_s\rangle\).
By (24) and stochastic isometry these converge in \(L^2\) to
\(\int\langle\theta(s,X),dW_s\rangle\). The same chosen subsequence
converges almost surely to \(J_B(X)\), because its state law is \(\mu_0\).
Uniqueness of the limit in probability gives
\[
J_B(X)=\int_0^T\langle\theta(s,X),dW_s\rangle.                \tag{25}
\]
Thus the forward density is \(D_B(X)\), and \(\int D_Bd\mu_0=1\).

For an arbitrary drifted solution use (19), (20). Under \(\widehat Q\),
equation (25) applies to \((U,\widehat W)\). Changing the integrator gives
\[
J_B(U)=\int_0^T\langle\theta(s,U),dW_s\rangle+A_B(U),
\qquad \widehat R_T^{-1}=\exp\{J_B(U)-A_B(U)/2\}=D_B(U).      \tag{26}
\]
One may first stop at finite energy in this substitution. Elementary
predictable stochastic integrals converge in probability under either of
two equivalent measures: absolute continuity transfers convergence in
probability in both directions. Their finite-variation correction is the
ordinary integral of \(\|\theta\|_2^2\); Cauchy--Schwarz in time controls
it under approximation. Removing the energy stops proves (26) on the full
horizon. In particular (26) is not an assumption about the joint law of
state and noise.

More explicitly, the elementary approximations above satisfy
\(\int_0^T\|g(U_s)v_j(s,U)-\theta(s,U)\|_2^2ds\to0\) in
probability under \(\widehat Q\), by (24), and hence under \(P\).
The stochastic-integral errors against \(W\) tend to zero in probability
by localization at their quadratic variations. The finite-variation
errors are bounded by
\[
 A_B(U)^{1/2}
 \left(\int_0^T\|g(U_s)v_j(s,U)-\theta(s,U)\|_2^2ds\right)^{1/2},
\]
which also tends to zero in probability. Applying the drifted weak equation
to (23) therefore proves the first identity in (26) directly from the same
state-path subsequence. This also verifies the change-of-integrator step
without requiring its approximations to converge in \(L^2(P)\).

For bounded Borel \(F\) on \(\mathcal X\),
\[
E_PF(U)=E_{\widehat Q}[F(U)\widehat R_T^{-1}]
       =\int F(\omega)D_B(\omega)\mu_0(d\omega).              \tag{27}
\]
Every drifted state-path law is therefore \(D_B\mu_0\). This proves
uniqueness and equivalence, since \(D_B\) is finite and positive almost
surely under \(\mu_0\).

## 6. Entropies

Under the drift-free law, (25) is square integrable and has mean zero.
Under a drifted realization, the stochastic integral in (26) is also
square integrable by (13), and has mean zero. Therefore
\[
E_{\mu_0}[-\log D_B]=\tfrac12E_{\mu_0}A_B,
\qquad E_{\mu_B}\log D_B=\tfrac12E_{\mu_B}A_B.
\]
These logarithms are integrable under their respective measures. The
definition of relative entropy and (27) prove (5); (13) gives (6).

## 7. Examples and checks of the hypotheses

For \(e\in H\), \(\|e\|_2=1\), and \(a\in\mathbb R\), the drift
\[
B(t,\omega)=a(1+\|\omega_t\|_2)
  1_{\{\sup_{0\le r\le t}\langle\omega_r,e\rangle\ge1\}}e   \tag{28}
\]
satisfies (2) with \(K=|a|\). The running supremum is a continuous
function of the stopped path, so the drift is jointly Borel and
nonanticipating. It is spatially nonlocal and remembers whether a
threshold was reached. It is covered even though its switch is
discontinuous. With \(g(z)=1+|z|^\beta\) and
\(h(x)=\operatorname{dist}(x,0)^{-\alpha}\) near zero,
\(0<\alpha<1/2\), it simultaneously permits unbounded diffusion and
an initial state without a spatial bound.

The current-norm bound matters in the stopped estimate. The unrestricted
drift \(B(t,\omega)=\omega_0\) does not satisfy (2) with one fixed \(K\)
on all of \(\mathcal X\): a continuous path can start with arbitrarily
large norm and reach zero later. The proof does not cover arbitrary
linear growth in the running path supremum.

Ordinary left-endpoint sampling cannot replace (8) for a Borel drift.
Take \(B(t,\omega)=1_{\mathbb Q}(t)e\) on \([0,1]\). Its time integral
is zero, and every average in (8) is zero. However, every uniform
rational left-endpoint Riemann sum equals \(e\). This does not contradict
(9), which asserts equality almost everywhere in time, rather than at
every time. It explains the need for time averaging before using canonical
predictable integrals.

As a separate sign check with actual history dependence, take constant
\(g=\sigma\ne0\), \(h=0\), and \(0<s<T\). Write
\(z=\langle X_s,1\rangle/\sigma\), and choose
\[
B(t,\omega)=
\begin{cases}
\sigma a\,1,&t\le s,\\
\sigma k\,1_{\{\langle\omega_s,1\rangle/\sigma>0\}}\,1,&t>s.
\end{cases}                                                \tag{29}
\]
This bounded drift satisfies (2). Under the drift-free law, put
\(z=W_s(1)\), \(y=W_T(1)-W_s(1)\), and \(d=T-s\). The variables
are independent centered normals of variances \(s,d\). Formula (4) is
\[
D_B=\exp\{az-a^2s/2+
             k1_{z>0}y-k^2d1_{z>0}/2\}.                    \tag{30}
\]
Integrating first in \(y\) gives one for its conditional exponential.
The remaining Gaussian tilt in \(z\) is normalized, proving \(ED_B=1\)
directly. Under the tilted law, \(z\) has mean \(as\) and variance
\(s\); conditional on \(z\), \(y\) has mean \(kd1_{z>0}\) and variance
\(d\). Thus, with \(\Phi\) the standard normal distribution function,
\[
\begin{split}
E_{\mu_0}A_B&=a^2s+k^2d/2,\\
E_{\mu_B}A_B&=a^2s+k^2d\,\Phi(a\sqrt{s}),\\
E_{\mu_0}[-\log D_B]&=\tfrac12(a^2s+k^2d/2),\\
E_{\mu_B}\log D_B&=\tfrac12(a^2s+k^2d\,\Phi(a\sqrt{s})).
\end{split}                                                \tag{31}
\]
The last two identities follow independently by inserting the displayed
conditional means into (30). In general the two entropies differ. This
checks that (5) uses energy under the correct law in each direction.

The theorem remains conditional on (D), and hence on the cited bounded-start
input when applied throughout the positive Hölder range. No pathwise
uniqueness conclusion, ellipticity-free conclusion, or endpoint
\(\beta=0\) assertion follows.
