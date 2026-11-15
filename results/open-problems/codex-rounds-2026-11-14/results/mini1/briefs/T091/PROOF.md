# Spatially constant additive noise: an exact reduction

Let \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\), with normalized Haar measure \(dx\), so that \(\int 1\,dx=1\). Fix \(\nu>0\), a deterministic divergence-free \(u_0\in L^2\), and constant vectors \(\sigma_1,\ldots,\sigma_r\in\mathbb R^3\). The covariance \(K=\sum_j\sigma_j\otimes\sigma_j\) may have any rank, including rank three. Consider

\[
 du+\bigl[-\nu\Delta u+P\operatorname{div}(u\otimes u)\bigr]dt
       =\sum_{j=1}^r\sigma_j\,d\beta_j(t),\qquad u(0)=u_0.                 \tag{1}
\]

Here \(P\) is the periodic Leray projection, acting as the identity on constants, and \(\beta\) is an \(r\)-dimensional standard Brownian motion on the solution's filtered probability space. No deterministic body force is present. Write \(\bar f=\int f\,dx\), and set \(v_0=u_0-\bar u_0\).

The phase space in this statement includes constant vector fields. If both velocity and noise are required to be mean zero, nonzero noise of the form (1) is excluded. The theorem concerns a degenerate class of smooth additive noises and does not address nonconstant mean-zero noise.

## Solution class and statement

A Leray–Hopf martingale solution here is an adapted distributional solution of (1) with paths in

\[
 C_w([0,\infty);L^2)\cap L^2_{\mathrm{loc}}([0,\infty);H^1),
\]

locally bounded in \(L^2\), satisfying the pathwise energy inequality

\[
 \frac12\|u(t)\|_2^2+\nu\int_s^t\|\nabla u(a)\|_2^2\,da
 \leq \frac12\|u(s)\|_2^2
 +\sum_j\int_s^t\langle u(a),\sigma_j\rangle\,d\beta_j(a)
 +\frac12\sum_j|\sigma_j|^2(t-s).                                  \tag{2}
\]

Almost surely, this holds for every \(t\geq s\), for \(s=0\) and almost every other \(s\). Equivalent localized integrability conventions for the stochastic integrals may be used. The deterministic Leray–Hopf class has the same path regularity and initial value, with (2) replaced by the unforced deterministic energy inequality. A definition imposing only an expected energy inequality, without (2), is not being identified with this class.

**Theorem.** For the noise in (1), define

\[
 m(t)=\bar u_0+\sum_j\sigma_j\beta_j(t),\qquad
 X(t)=\int_0^t m(a)\,da.                                         \tag{3}
\]

Every Leray–Hopf martingale solution satisfies \(\bar u(t)=m(t)\). Almost surely,

\[
 v(t,x)=u(t,x+X(t))-m(t)                                         \tag{4}
\]

is a deterministic unforced Leray–Hopf solution with initial value \(v_0\), in the sense that each sample path solves that deterministic problem. Its choice among deterministic solutions can still be random.

Conversely, every fixed deterministic Leray–Hopf solution \(v\) with initial value \(v_0\) gives a Leray–Hopf martingale solution on any Brownian probability space by

\[
 u(t,x)=v(t,x-X(t))+m(t).                                        \tag{5}
\]

Consequently:

1. There is at most one velocity law for (1) in the stated martingale class if and only if there is at most one deterministic Leray–Hopf trajectory starting at \(v_0\). No uniqueness assumption about the joint law with unused Brownian coordinates is needed.
2. For smooth \(u_0\), a global deterministic strong solution starting at \(v_0\) exists if and only if (1) has a global strong solution almost surely. Existence of a global strong stochastic trajectory on even a positive-probability event already implies the deterministic assertion.
3. For maximal local strong solutions, the maximal lifetime equals the deterministic maximal lifetime, almost surely. Thus, for this noise, increasing its intensity cannot change a finite strong-solution lifetime into an infinite one.

In assertions 2–3, “strong” includes spatial regularity, for example \(C([0,T];H^s)\cap L^2(0,T;H^{s+1})\) for every finite interval in the lifetime and an integer \(s\geq3\). Probabilistically strong by itself does not imply this regularity.

## Proof

### 1. Recovering the mean and removing the stochastic differential

Test (1) against the three constant coordinate vectors. The Laplacian and periodic divergence integrate to zero. Therefore, simultaneously for every time,

\[
 \bar u(t)=\bar u_0+\sum_j\sigma_j\beta_j(t)=m(t).                 \tag{6}
\]

This uses continuity of the weak pairings to extend the identity from rational times. In particular, \(m\) is continuous and \(X\) is continuously differentiable with \(X'=m\). Although \(m\) is Brownian, \(X\) has finite variation on every finite time interval.

Set \(y=u-m\). Subtracting the equation for \(m\) from (1) gives, path by path,

\[
 \partial_t y-\nu\Delta y+P\operatorname{div}(y\otimes y)
                 +(m\cdot\nabla)y=0,\qquad \bar y=0.            \tag{7}
\]

For completeness, the expansion of the nonlinear term has only one nonzero cross term. With \((\operatorname{div}(a\otimes b))_i=\sum_k\partial_k(a_i b_k)\),

\[
 \operatorname{div}(y\otimes m)=(m\cdot\nabla)y,\qquad
 \operatorname{div}(m\otimes y)=m\,\operatorname{div}y=0,\qquad
 \operatorname{div}(m\otimes m)=0.
\]

The surviving cross term is divergence free and is unchanged by \(P\).

All these identities hold on one event of probability one. One way to obtain such an event is to write the integrated weak equations first for a countable dense family of smooth solenoidal tests and rational times, and then extend by continuity and the energy bounds. The drift belongs to \(L^1(0,T;H^{-4})\): indeed

\[
 |\langle P\operatorname{div}(y\otimes y),\phi\rangle|
 \leq \|y\|_2^2\,\|\nabla P\phi\|_\infty
 \leq C\|y\|_2^2\,\|\phi\|_{H^4},
\]

and the Laplacian and advection terms obey the corresponding bounds. Here the last inequality follows from boundedness of \(P\) on \(H^4\) and the Sobolev embedding \(H^4\subset W^{1,\infty}\) in three dimensions. Thus \(y\) has an absolutely continuous representative in \(H^{-4}\), consistent with its weakly continuous \(L^2\) representative.

### 2. The change of variables at Leray–Hopf regularity

For \(a\in\mathbb R^3\), let \(T_a f(x)=f(x+a)\). Spatial translation commutes with \(\Delta\), \(P\), and spatial convolution. Let \(\rho_\epsilon\) be a smooth periodic approximate identity, and put \(y_\epsilon=\rho_\epsilon*y\). Its equation is

\[
 \partial_t y_\epsilon-\nu\Delta y_\epsilon
  +P\operatorname{div}\bigl(\rho_\epsilon*(y\otimes y)\bigr)
  +(m\cdot\nabla)y_\epsilon=0.                                  \tag{8}
\]

For fixed \(\epsilon\), \(y_\epsilon\) is absolutely continuous in time with values in every fixed spatial \(C^k\) space. This follows by applying the bounded smoothing map from \(H^{-4}\) to \(C^k\) to the preceding absolutely continuous equation. The ordinary chain rule is therefore applicable to \(v_\epsilon=T_X y_\epsilon\). Since \(X'=m\), it gives

\[
 \partial_t v_\epsilon
 =T_X\bigl(\partial_t y_\epsilon+(m\cdot\nabla)y_\epsilon\bigr)
 =\nu\Delta v_\epsilon
  -P\operatorname{div}\bigl(T_X[\rho_\epsilon*(y\otimes y)]\bigr). \tag{9}
\]

There is no Itô correction: the translating path is \(X\), not \(m\).

On every finite time interval, \(y_\epsilon\to y\) in \(L^2_{t,x}\), and \(\rho_\epsilon*(y\otimes y)\to y\otimes y\) in \(L^1_{t,x}\). Translation is an isometry in these norms at every time. Thus (9) converges in distributions to

\[
 \partial_t v-\nu\Delta v+P\operatorname{div}(v\otimes v)=0,
 \qquad \operatorname{div}v=0,\quad \bar v=0,\quad v(0)=v_0.     \tag{10}
\]

Here \(T_X(y\otimes y)=(T_X y)\otimes(T_X y)=v\otimes v\).

Translation preserves the \(L^2\) and gradient norms of \(y\), so \(v\) is locally bounded in \(L^2\) and locally square integrable in \(H^1\). It is weakly continuous in \(L^2\): for \(t_n\to t\) and \(\phi\in L^2\),

\[
 \langle v(t_n),\phi\rangle
 =\langle y(t_n),T_{-X(t_n)}\phi\rangle
 \longrightarrow\langle y(t),T_{-X(t)}\phi\rangle.
\]

To justify the limit, subtract the test at time \(t\). The difference tends to zero strongly in \(L^2\) by continuity of translations and of \(X\), while \(y(t_n)\) is bounded in \(L^2\). The remaining pairing converges by weak continuity of \(y\). This also verifies the initial value in (10).

### 3. Exact preservation of the energy defect

Orthogonality of constants and mean-zero fields gives, at every time,

\[
 \|u(t)\|_2^2=\|v(t)\|_2^2+|m(t)|^2,\qquad
 \|\nabla u(t)\|_2^2=\|\nabla v(t)\|_2^2.                       \tag{11}
\]

The stochastic work has no contribution from the centered field:

\[
 \langle u(t),\sigma_j\rangle=m(t)\cdot\sigma_j.
\]

Itô's formula in \(\mathbb R^3\) yields

\[
 \frac12|m(t)|^2-\frac12|m(s)|^2
 =\sum_j\int_s^t m(a)\cdot\sigma_j\,d\beta_j(a)
   +\frac12\operatorname{tr}K\,(t-s),\qquad
 \operatorname{tr}K=\sum_j|\sigma_j|^2.                         \tag{12}
\]

This identity has a continuous version valid simultaneously for all \(s,t\). Substitute (11)–(12) into (2) and cancel exactly. The result is

\[
 \frac12\|v(t)\|_2^2+\nu\int_s^t\|\nabla v(a)\|_2^2\,da
 \leq\frac12\|v(s)\|_2^2.                                      \tag{13}
\]

The exceptional starting times are exactly those in (2). In particular \(s=0\) is retained. More precisely, the left side minus the right side of (13) equals the left side minus the entire right side of (2). Thus the transformation preserves the energy defect, not just its sign. This proves the first direction of the theorem.

### 4. Lifting a deterministic trajectory

Let \(v\) be a fixed deterministic solution of (10), with the deterministic Leray–Hopf energy inequality, and define \(u\) by (5). It is adapted: at time \(t\) the formula uses only \(v(t)\), \(\beta(t)\), and \(\beta\) before \(t\). It has all the required spatial integrability and weak continuity.

The same spatial-mollification argument, now with the translating path \(-X\), gives

\[
 \partial_t[T_{-X}v]
 =\nu\Delta[T_{-X}v]
  -P\operatorname{div}\bigl((T_{-X}v)\otimes(T_{-X}v)\bigr)
  -(m\cdot\nabla)[T_{-X}v].                                   \tag{14}
\]

Adding \(dm=\sum_j\sigma_j\,d\beta_j\) and using the nonlinear expansion from Step 1 proves (1). Adding (12) to (13), with (11), proves (2). Any usual finite-time energy moment requirements follow as well: the centered trajectory has deterministic energy bounds and the only added terms are finite-dimensional Brownian maxima, which have finite moments of every order on finite intervals. Thus (5) is an admissible martingale solution.

Equations (4) and (5) are inverse transformations for each fixed mean path. A random deterministic-PDE trajectory obtained from an arbitrary martingale solution need not be independent of that mean path; no such independence is used below.

### 5. Recovering the deterministic trajectory from the velocity law

Velocity laws may be regarded as probability measures on

\[
 \mathcal E=C([0,\infty);H^{-4}),
\]

with the topology of uniform convergence on compact time intervals. Every trajectory under consideration belongs to this space by Step 1 and continuity of \(m\).

The following map uses only a velocity path \(f\), not a separately recorded Brownian motion:

\[
 m_f(t)=\bar f(t),\qquad X_f(t)=\int_0^t\bar f(a)\,da,\qquad
 \Psi(f)(t)=T_{X_f(t)}\bigl(f(t)-\bar f(t)\bigr).                \tag{15}
\]

It is Borel measurable; in fact it is continuous on \(\mathcal E\). To see this, the mean is a continuous linear functional on \(H^{-4}\), integration is continuous for uniform convergence on compact time intervals, and translation is an isometry that is strongly continuous on \(H^{-4}\). This last continuity is uniform on a compact subset of \(H^{-4}\): approximate that subset by finitely many balls, use strong continuity at their centers, and bound the error by the isometry. The image of a continuous path over \([0,T]\) is compact. These observations prove uniform convergence on \([0,T]\) of the translated paths whenever \(f_n\to f\) there.

Suppose first that the deterministic Leray–Hopf trajectory \(v_*\) starting at \(v_0\) is unique. For any martingale solution, Step 2 and Step 3 give

\[
 \Psi(u)=v_*\quad\hbox{almost surely},\qquad
 u(t)=T_{-X(t)}v_*(t)+m(t).                                    \tag{16}
\]

The law of \(m\) is fixed by \(\bar u_0\) and \(K\). Formula (16) fixes the velocity law. Extra randomness in the filtration cannot change it.

Conversely, suppose \(v_1\ne v_2\) are two deterministic Leray–Hopf trajectories with initial value \(v_0\). Lift each by (5), using the same Brownian space if desired, and denote the resulting velocity laws by \(\mu_1,\mu_2\). Then

\[
 \Psi_\#\mu_1=\delta_{v_1},\qquad
 \Psi_\#\mu_2=\delta_{v_2}.                                   \tag{17}
\]

These point masses are distinct, so \(\mu_1\ne\mu_2\). Distinct weakly continuous trajectories are distinct in \(\mathcal E\); equality as distributions would give equality at every time. This proves assertion 1. It also proves the corresponding equivalence for pathwise uniqueness on a common Brownian space.

### 6. Strong regularity and lifetime

For every \(a\), translation is an isometry on every Sobolev space, and the centered fields satisfy

\[
 \|u(t)-m(t)\|_{H^q}=\|v(t)\|_{H^q}.                           \tag{18}
\]

On compact time intervals \(m\) is bounded, and \(X\) is continuous. Equations (4)–(5) therefore preserve \(C_tH^s\cap L^2_tH^{s+1}\). For continuity in \(H^s\), use strong continuity of translations and the compact-image argument from Step 5. The distributional equations already proved then give precisely the deterministic or stochastic strong equation as appropriate.

If a deterministic global strong \(v\) exists, (5) constructs an adapted global strong \(u\) for almost every Brownian path. If a stochastic solution is spatially strong for all time on an event of positive probability, choose a sample path in that event on which the weak equations also hold. Formula (4) produces one deterministic global strong trajectory from \(v_0\). This argument does not infer a deterministic solution from the zero-probability Brownian path \(\beta=0\). It proves assertion 2.

To check assertion 3, strong deterministic solutions are unique on their common intervals. Indeed, if \(a,b\) are such solutions and \(w=a-b\), then

\[
 \partial_t w-\nu\Delta w+P[(a\cdot\nabla)w+(w\cdot\nabla)b]=0.
\]

Pair with \(w\). Periodicity and \(\operatorname{div}a=0\) remove the first transport term. Hence

\[
 \frac12\frac{d}{dt}\|w\|_2^2+\nu\|\nabla w\|_2^2
 \leq\|\nabla b\|_\infty\|w\|_2^2.
\]

For \(s\geq3\), \(H^s\subset W^{1,\infty}\), and \(b\in C_tH^s\) makes the coefficient integrable on every compact subinterval. Gronwall's inequality gives \(w=0\) for the same initial value. The pairing is justified directly by strong regularity, or by smooth approximation. The usual local strong solution therefore has a well-defined maximal interval, obtained by joining its mutually agreeing local extensions.

Let its endpoint be \(T_*\). Formula (5) lifts it on every compact subinterval of \([0,T_*)\), for every continuous Brownian path. Thus the stochastic maximal lifetime cannot be smaller. Conversely, (4) converts any strong stochastic extension beyond \(T_*\) into a deterministic strong extension of the same local trajectory, by the uniqueness just proved. Such an extension contradicts maximality. Taking one event on which the weak identities hold on all integer time intervals proves equality of the lifetimes almost surely. The only background existence fact used in this lifetime formulation is standard local strong existence for smooth deterministic data; the transformation and assertion 2 do not require a global existence theorem. This proves assertion 3. \(\square\)

## Scope

This reduction leaves deterministic three-dimensional regularity and deterministic Leray–Hopf uniqueness unresolved. It also leaves the stated problem for nonconstant mean-zero additive noise unresolved. Its content is that nonzero spatially constant additive Gaussian noise cannot improve either question: its effect on the centered field is exactly a translation. The argument is elementary and no novelty is claimed.
