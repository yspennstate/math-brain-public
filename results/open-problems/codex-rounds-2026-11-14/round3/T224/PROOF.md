# An output cancellation improves the curvature-dependent weak bound

## Setting and result

Let \(\mathcal H\) be a real separable Hilbert space, \(g\in\mathcal H\), and let \(\phi:\mathbb R^d\to\mathcal H\) be twice continuously differentiable with

\[
 \sup_w\|\phi(w)\|\le A,\qquad
 \sup_w\|D\phi(w)\|_{\rm op}\le B,\qquad
 \|D^2\phi(w)[u,v]\|\le M|u||v|.                         \tag{1}
\]

All constants are finite and nonnegative. The population mean-field flow and the interacting particle flow are

\[
 f_t=\int\phi(v)\rho_t(dv),\qquad r_t=f_t-g,\qquad
 \dot v=-D\phi(v)^*r_t,
\]
\[
 f_t^m=\frac1m\sum_i\phi(w_i(t)),\qquad
 \dot w_i=-D\phi(w_i)^*(f_t^m-g).                         \tag{2}
\]

The initial particles are iid with law \(\rho_0\). These are population-data flows with fixed output coefficients and the half-squared-loss time convention. The bounds in (1) give bounded velocities and globally Lipschitz parameter vector fields for fixed bounded residuals; the usual characteristic construction defines the global flows. The argument below also applies whenever these flows are given. Write \(L_t=\|r_t\|^2\).

Define

\[
 h(t)=\sup_{w\in\mathbb R^d,\ |u|=1}
       [-\langle r_t,D^2\phi(w)[u,u]\rangle]_+,
 \qquad H(t)=\int_0^t h(s)\,ds.                           \tag{3}
\]

Here \([x]_+=\max(x,0)\), so \(0\le h(t)\le M\sqrt{L_t}\).
Continuity permits countable dense sets in the suprema and hence gives measurability. Put

\[
 K_* = 2A^2+4A^2B^2+2M^2A^4.                            \tag{4}
\]

**Theorem.** For every deterministic \(T\ge1\),

\[
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
 \le \frac{4K_*(1+T)^2e^{2H(T)}}m+6L_T.                 \tag{5}
\]

The supremum is outside the expectation. In particular, if

\[
 L_t\le C(1+t)^{-c},\qquad
 H(T)\le h_0+\kappa\log(1+T),                           \tag{6}
\]

where \(c>0\) and \(h_0,\kappa\ge0\), then, for \(m\ge2^{c+2+2\kappa}\),

\[
 \boxed{\displaystyle
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
 \le (4K_*e^{2h_0}+6C)\,m^{-c/(c+2+2\kappa)}.}         \tag{7}
\]

This improves the exponent \(c/(c+4+2\kappa)\) in the preceding report under the same assumptions. The new constant \(K_*\) is polynomial in the feature bounds. No optimality is asserted. The curvature hypothesis in (6) is additional to the loss envelope and is not derived from it when \(0<c<2\).

## Proof

### 1. Coupling and iid fluctuations

Set \(v_i(0)=w_i(0)\), and let each \(v_i(t)\) follow the deterministic mean-field vector field in (2). At each fixed time the \(v_i(t)\) are iid with law \(\rho_t\). Define

\[
 \bar f_t^m=\frac1m\sum_i\phi(v_i(t)),\qquad
 \zeta_t=\bar f_t^m-f_t,\qquad \eta_t=\|\zeta_t\|,
\]
\[
 e_i=w_i-v_i,\qquad y(t)=\frac1m\sum_i|e_i(t)|^2,
 \qquad J_T=\int_0^T\eta_s^2\,ds.                        \tag{8}
\]

Centering the iid Hilbert-valued variables and expanding their squared norm gives

\[
 \mathbb E\eta_t^2
 =\frac1m\left(\mathbb E\|\phi(v_1(t))\|^2-\|f_t\|^2\right)
 \le\frac{A^2}{m},\qquad
 \mathbb E J_T\le\frac{A^2T}{m}.                         \tag{9}
\]

The last assertion follows by Tonelli and requires no independence across time.

### 2. Exact cancellation in the output

At a given time write

\[
 \delta=f_t^m-f_t,\qquad
 \Delta=f_t^m-\bar f_t^m,\qquad \delta=\Delta+\zeta_t,
 \qquad J_WE=\frac1m\sum_iD\phi(w_i)e_i.                 \tag{10}
\]

Subtracting the two particle equations, with the same mean-field residual in the first term, gives exactly

\[
 \frac12y'
 =-\frac1m\sum_i
    \langle r_t,(D\phi(w_i)-D\phi(v_i))e_i\rangle
    -\langle J_WE,\delta\rangle.                        \tag{11}
\]

For each particle the fundamental theorem of calculus gives

\[
 (D\phi(w_i)-D\phi(v_i))e_i
 =\int_0^1D^2\phi(v_i+\theta e_i)[e_i,e_i]\,d\theta.
\]

The first term of (11) is therefore at most \(h(t)y\).
There is also the Taylor remainder identity

\[
 \begin{split}
 R:=J_WE-\Delta
 &=\frac1m\sum_i\int_0^1
     [D\phi(w_i)-D\phi(v_i+\theta e_i)]e_i\,d\theta,\\
 \|R\|&\le\frac M{2m}\sum_i|e_i|^2=\frac M2y.          \tag{12}
 \end{split}
\]

Since \(J_WE=\delta-\zeta_t+R\), the last term in (11) is

\[
 \begin{split}
 -\langle J_WE,\delta\rangle
 &=-\|\delta\|^2+\langle\zeta_t-R,\delta\rangle\\
 &=-\left\|\delta-\frac{\zeta_t-R}{2}\right\|^2
      +\frac14\|\zeta_t-R\|^2\\
 &\le\frac12\eta_t^2+\frac12\|R\|^2
 \le\frac12\eta_t^2+\frac{M^2}{8}y^2.                  \tag{13}
 \end{split}
\]

Combining (11)--(13), and putting \(\alpha=M^2/4\), yields

\[
 \boxed{\quad y'\le2h(t)y+\eta_t^2+\alpha y^2,
       \qquad y(0)=0.\quad}                            \tag{14}
\]

No third derivative is used. The positive term \(\eta_t^2\) has one fewer time integration than the square of \(\int\eta_t\), and the nonlinear remainder is quadratic in \(y\).

### 3. A pathwise Riccati comparison

Fix \(T\ge1\) and define the deterministic number

\[
 S_T=\int_0^T e^{2H(s)}\,ds\le T e^{2H(T)}.              \tag{15}
\]

For \(z(t)=e^{-2H(t)}y(t)\), (14) gives, almost everywhere,

\[
 z'\le e^{-2H(t)}\eta_t^2+\alpha e^{2H(t)}z^2.
\]

Since \(H\ge0\), integration gives, for \(t\le T\),

\[
 z(t)\le J_T+\alpha\int_0^t e^{2H(s)}z(s)^2\,ds.       \tag{16}
\]

If \(J_T>0\), let the right side of (16) be \(Z(t)\). Then \(0\le z\le Z\), \(Z(0)=J_T\), and

\[
 Z'\le\alpha e^{2H(t)}Z^2,
 \qquad
 \frac1{Z(t)}\ge\frac1{J_T}
                  -\alpha\int_0^t e^{2H(s)}ds.          \tag{17}
\]

The second inequality follows by differentiating \(1/Z\) and integrating. In particular, whenever \(\alpha J_TS_T\le1/2\),

\[
 y(s)\le2e^{2H(s)}J_T\le2e^{2H(T)}J_T
 \qquad(0\le s\le T).                                  \tag{18}
\]

When \(J_T=0\), (14) and uniqueness for the scalar comparison with zero forcing give \(y=0\). Equivalently, replace \(J_T\) by \(J_T+\varepsilon\) in (16)--(17) and let \(\varepsilon\) decrease to zero. When \(\alpha=0\), direct integration gives \(y(s)\le e^{2H(s)}J_T\), so (18) holds with no restriction.

Let

\[
 \mathcal G_T=\{\alpha S_T J_T\le1/2\}.
\]

Markov's inequality and (9) give

\[
 \mathbb P(\mathcal G_T^c)
 \le2\alpha S_T\mathbb E J_T
 \le\frac{2\alpha A^2T^2e^{2H(T)}}m.                    \tag{19}
\]

For \(\alpha=0\), the event is the whole probability space and the bound is zero.

### 4. Output error up to the horizon

From (1), (8), and Cauchy--Schwarz over particles,

\[
 \|\Delta\|\le\frac Bm\sum_i|e_i|\le B\sqrt y,
 \qquad \|\delta\|^2\le2B^2y+2\eta_t^2.                 \tag{20}
\]

For every fixed \(s\le T\), (9) and (18) imply

\[
 \mathbb E[\mathbf1_{\mathcal G_T}\|\delta_s\|^2]
 \le\frac{4A^2B^2T e^{2H(T)}+2A^2}{m}.                 \tag{21}
\]

The two outputs have norm at most \(A\), so \(\|\delta_s\|^2\le4A^2\) for every initialization. Thus (19) gives

\[
 \mathbb E[\mathbf1_{\mathcal G_T^c}\|\delta_s\|^2]
 \le\frac{8\alpha A^4T^2e^{2H(T)}}m
 =\frac{2M^2 A^4T^2e^{2H(T)}}m.                          \tag{22}
\]

Combining these estimates proves the slightly finer bound

\[
 \sup_{0\le s\le T}\mathbb E\|f_s^m-f_s\|^2
 \le\frac{2A^2+4A^2B^2T e^{2H(T)}
                 +2M^2A^4T^2e^{2H(T)}}m
 \le D_T:=\frac{K_*(1+T)^2e^{2H(T)}}m.                  \tag{23}
\]

In the last inequality, each of \(1,T,T^2\) is at most \((1+T)^2\), and \(e^{2H(T)}\ge1\).

### 5. Later times

Let \(L_t^m=\|f_t^m-g\|^2\). Differentiation along the population particle flow gives

\[
 (L_t^m)'=-\frac2m\sum_i
       |D\phi(w_i)^*(f_t^m-g)|^2\le0,
\]
\[
 L_t'=-2\int|D\phi(v)^*r_t|^2\rho_t(dv)\le0.           \tag{24}
\]

Consequently, for every deterministic \(t\ge T\),

\[
 \begin{split}
 \mathbb E\|f_t^m-f_t\|^2
 &\le2\mathbb E L_t^m+2L_t\\
 &\le2\mathbb E L_T^m+2L_T\\
 &\le4\mathbb E\|f_T^m-f_T\|^2+6L_T
 \le4D_T+6L_T.                                         \tag{25}
 \end{split}
\]

Together with (23), this proves (5).

Under (6), its right side is at most

\[
 \frac{4K_*e^{2h_0}(1+T)^{2+2\kappa}}m
       +6C(1+T)^{-c}.                                   \tag{26}
\]

Choose \(1+T=m^{1/(c+2+2\kappa)}\). The stated lower bound on \(m\) ensures \(T\ge1\). The exponent of \(m\) in the first term is

\[
 \frac{2+2\kappa}{c+2+2\kappa}-1
 =-\frac c{c+2+2\kappa},
\]

which equals the exponent in the second term. This proves (7).

## What follows from the slow loss envelope alone

For \(0<c<2\), put \(p=1-c/2\), \(D=1+M\sqrt C/p\). Equation (3) and the loss envelope give

\[
 H(T)\le\frac{M\sqrt C}{p}\big((1+T)^p-1\big).
\]

For \(\log m\ge4D\,2^p\), choose \(1+T=(\log m/(4D))^{1/p}\). Then \(T\ge1\) and \(2H(T)\le\frac12\log m\), so (5) gives

\[
 \sup_{t\ge0}\mathbb E\|f_t^m-f_t\|^2
 \le4K_*m^{-1/2}\left(\frac{\log m}{4D}\right)^{2/p}
     +6C\left(\frac{\log m}{4D}\right)^{-c/p}.            \tag{27}
\]

This has the same logarithmic rate \((\log m)^{-2c/(2-c)}\) as the preceding report, with a smaller finite-horizon term. It does not establish a polynomial rate from slow loss decay alone. At \(c=2\), (3) gives \(H(T)\le M\sqrt C\log(1+T)\); (7) then gives exponent \(1/(2+M\sqrt C)\) for this bounded Euclidean setting. Endpoint polynomial coverage was already known from the source, and this observation is only a specialization of (7).

## Scope and references

For neural-network outputs take \(\mathcal H=L^2(P_X)\) and \(\phi(w)(x)=\sigma(w^\top x)\). If \(S_j=\|\sigma^{(j)}\|_\infty\) and \(Q_j=\sup_{|u|=1}(\mathbb E|u^\top X|^j)^{1/j}\), then (1) holds with \(A=S_0\), \(B=S_1Q_2\), and \(M=S_2Q_4^2\). For the last claim,
\(D^2\phi(w)[u,v]=\sigma''(w^\top X)(u^\top X)(v^\top X)\), and Cauchy--Schwarz bounds its squared norm by \(S_2^2(\mathbb E|u^\top X|^4)^{1/2}(\mathbb E|v^\top X|^4)^{1/2}\). Thus directional subgaussian bounds give dimension-independent \(Q_2,Q_4\). If \(A,B,M,C\) are polynomial in \(d\), \(h_0=O(\log d)\), and \(\kappa\) is dimension independent, the prefactor in (7) is polynomial in \(d\).

The setting is a bounded-feature Euclidean subclass of Margalit Glasgow and Joan Bruna, *Uniform-in-Time Weak Propagation-of-Chaos in Shallow Neural Networks*, [arXiv:2605.22010v3](https://arxiv.org/html/2605.22010v3). Their Remark 6 already treats the critical decay exponent, and their Section 6 leaves slower decay open. The new assertion here is (5)--(7), relative to the preceding report; no literature-priority claim is made.

This proof does not cover unbounded activations, sphere-constrained flows, trained output coefficients, finite training data, or time discretization. In particular, boundedness is essential to (22) as written. There is no counterexample, necessity theorem for (6), or sharp exponent for the original question.
