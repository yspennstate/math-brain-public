# A polynomial weak rate for features in one output direction

## Statement

Let \(\psi:\mathbb R^d\to\mathbb R\) be \(C^2\), with

\[
 |\psi(w)|\le A,\qquad |\nabla\psi(w)|\le B,
 \qquad \|D^2\psi(w)\|_{\mathrm{op}}\le M                 \tag{1}
\]

for finite nonnegative constants. Let \(\gamma\in\mathbb R\), let \(\rho_0\) be a probability law, and use the gradient of half the squared population loss:

\[
 f_t=\int\psi(v)\rho_t(dv),\qquad
 \dot v=(\gamma-f_t)\nabla\psi(v),
\]
\[
 f_t^m=\frac1m\sum_{i=1}^m\psi(w_i(t)),\qquad
 \dot w_i=(\gamma-f_t^m)\nabla\psi(w_i),\qquad
 w_i(0)\stackrel{\mathrm{iid}}\sim\rho_0.                 \tag{2}
\]

Put \(L_t=(f_t-\gamma)^2\). The parameter dimension \(d\) is arbitrary; the restriction is to one direction in output space.

**Theorem.** For every integer \(m\ge1\) and deterministic \(T\ge0\),

\[
 \sup_{t\ge0}\mathbb E|f_t^m-f_t|^2
 \le \frac{4A^2(1+B^2T)^2}{m}+6L_T.                    \tag{3}
\]

Consequently, if \(L_t\le C(1+t)^{-c}\) for \(c>0\), then

\[
 \boxed{\displaystyle
 \sup_{t\ge0}\mathbb E|f_t^m-f_t|^2
 \le \bigl(4A^2\max\{1,B^4\}+6C\bigr)
                         m^{-c/(c+2)}.}                \tag{4}
\]

No square-root-loss integrability or residual-curvature hypothesis is used. The supremum is outside expectation. The exponent is an upper-bound exponent, with no sharpness claim. If \(A,B,C\) are polynomially bounded in \(d\), so is the prefactor.

The same assertion holds in a real Hilbert output space \(\mathcal H\) when

\[
 \phi(w)=b+u\psi(w),\qquad \|u\|_{\mathcal H}=1,
 \qquad g=b+u\gamma.                                   \tag{5}
\]

Here the output error in (3)--(4) is \(\|f_t^m-f_t\|_{\mathcal H}^2\). If all features lie in the affine line \(b+\mathbb Ru\), the assumption \(\|f_t-g\|\to0\) already forces \(g\) to lie in that line, since it is closed. For \(\mathcal H=L^2(P_X)\), this is the requested weak output norm. A scalar-valued prediction at each input does not by itself satisfy (5): the restriction concerns the dimension of its span as a function of the input.

## 1. A common autonomous trajectory and two clocks

Let \(\Psi_s(z)\) be the complete flow of the autonomous vector field \(\nabla\psi\):

\[
 \partial_s\Psi_s(z)=\nabla\psi(\Psi_s(z)),
 \qquad \Psi_0(z)=z,\qquad s\in\mathbb R.                \tag{6}
\]

Bounded Hessian gives global Lipschitz continuity of this field, and bounded gradient prevents finite-time escape in either direction. Thus (6) exists uniquely for every real \(s\). Define

\[
 a(s,z)=\psi(\Psi_s(z)),\qquad
 F(s)=\mathbb E_{Z\sim\rho_0}a(s,Z),\qquad
 F_m(s)=\frac1m\sum_i a(s,Z_i).                          \tag{7}
\]

Differentiation along (6) gives

\[
 \partial_s a(s,z)=|\nabla\psi(\Psi_s(z))|^2
                         \in[0,B^2].                  \tag{8}
\]

It follows directly by integration that \(a(\cdot,z)\), \(F\), and \(F_m\) are nondecreasing and \(B^2\)-Lipschitz. They are bounded in absolute value by \(A\). Differentiation under the expectation in (7) is legitimate by the bound in (8).

Let the two scalar clocks solve

\[
 \tau'=\gamma-F(\tau),\qquad
 \tau_m'=\gamma-F_m(\tau_m),\qquad
 \tau(0)=\tau_m(0)=0.                                  \tag{9}
\]

Their vector fields are globally Lipschitz and bounded by \(|\gamma|+A\). By the chain rule,

\[
 v_t(z)=\Psi_{\tau(t)}(z),\qquad
 w_i(t)=\Psi_{\tau_m(t)}(Z_i)                            \tag{10}
\]

solve (2), with

\[
 f_t=F(\tau(t)),\qquad f_t^m=F_m(\tau_m(t)).              \tag{11}
\]

Indeed, differentiating the first expression in (10) gives \((\gamma-F(\tau))\nabla\psi(v_t)\); its law has output \(F(\tau)\). Differentiating the second gives the empirical equation in exactly the same way. The usual uniqueness construction agrees with these solutions. No sign assumption on either initial residual is needed. The clocks can have opposite signs on some initializations.

## 2. Monotonicity controls the clock error

Set

\[
 q(t)=\tau_m(t)-\tau(t),\qquad
 \zeta_t=F_m(\tau(t))-F(\tau(t)),
\]
\[
 D_t=F_m(\tau_m(t))-F_m(\tau(t)).                        \tag{12}
\]

Subtracting (9) gives

\[
 q'=-D_t-\zeta_t,\qquad q(0)=0.                        \tag{13}
\]

Since \(F_m\) is nondecreasing, \(qD_t\ge0\). For \(\varepsilon>0\), differentiate the smooth norm regularization:

\[
 \frac d{dt}\sqrt{q(t)^2+\varepsilon^2}
 =\frac{-qD_t-q\zeta_t}{\sqrt{q^2+\varepsilon^2}}
 \le |\zeta_t|.                                        \tag{14}
\]

After integration and \(\varepsilon\downarrow0\),

\[
             |q(t)|\le\int_0^t|\zeta_s|\,ds.           \tag{15}
\]

This comparison has no exponential factor. Only the monotonicity of the empirical feature average in its scalar clock is used.

For a second derivation, when \(q\ne0\) put \(k_t=D_t/q\); when \(q=0\), put \(k_t=0\). Then \(0\le k_t\le B^2\), \(D_t=k_tq\), and (13) is the scalar linear equation \(q'=-k_tq-\zeta_t\) with bounded measurable coefficient. Its integrating-factor identity is

\[
 q(t)=-\int_0^t
       \exp\left(-\int_s^t k_v\,dv\right)\zeta_s\,ds.   \tag{16}
\]

The exponential in (16) is at most one, which gives (15) again.

## 3. Expected output error on a deterministic horizon

The clock \(\tau(t)\) is deterministic. Thus \(a(\tau(t),Z_i)\) are iid bounded real variables. Expanding the variance gives, for every fixed \(t\),

\[
 \mathbb E\zeta_t^2
 =\frac{\operatorname{Var}(a(\tau(t),Z))}{m}
 \le\frac{A^2}{m}.                                    \tag{17}
\]

Cauchy--Schwarz in time and Tonelli applied to (15) imply

\[
 \mathbb E q(t)^2
 \le t\int_0^t\mathbb E\zeta_s^2\,ds
 \le\frac{A^2t^2}{m}.                                 \tag{18}
\]

There is no assumption of independence between times. The random clock \(\tau_m\) has not been inserted into an iid sampling formula.

The exact output decomposition is

\[
 f_t^m-f_t=D_t+\zeta_t,\qquad |D_t|\le B^2|q(t)|.       \tag{19}
\]

The triangle inequality in the probability-space \(L^2\) norm, followed by (17)--(18), gives

\[
 \bigl(\mathbb E|f_t^m-f_t|^2\bigr)^{1/2}
 \le B^2\bigl(\mathbb E q(t)^2\bigr)^{1/2}
       +\bigl(\mathbb E\zeta_t^2\bigr)^{1/2}
 \le\frac{A(1+B^2t)}{\sqrt m}.                          \tag{20}
\]

Consequently,

\[
 \sup_{0\le t\le T}\mathbb E|f_t^m-f_t|^2
 \le D_T^*:=\frac{A^2(1+B^2T)^2}{m}.                   \tag{21}
\]

This bound holds for every initialization in its deterministic comparison and uses no stopping threshold or exceptional-event estimate.

## 4. All later times and choice of horizon

Let \(L_t^m=(f_t^m-\gamma)^2\). Direct differentiation of (2) yields

\[
 (L_t^m)'=-2L_t^m\frac1m\sum_i|\nabla\psi(w_i(t))|^2
 \le0,
\]
\[
 L_t'=-2L_t\int|\nabla\psi(v)|^2\rho_t(dv)\le0.         \tag{22}
\]

Therefore, for every \(t\ge T\),

\[
 \begin{split}
 \mathbb E|f_t^m-f_t|^2
 &\le2\mathbb E L_t^m+2L_t\\
 &\le2\mathbb E L_T^m+2L_T\\
 &\le4\mathbb E|f_T^m-f_T|^2+6L_T\\
 &\le4D_T^*+6L_T.
 \end{split}                                           \tag{23}
\]

Combining (21) and (23) proves (3), including \(T=0\). This step requires neither convergence nor a decay estimate for the finite system.

For (4) choose

\[
 u=m^{1/(c+2)},\qquad T=u-1\ge0.                       \tag{24}
\]

For \(u\ge1\),

\[
 1+B^2(u-1)\le\max\{1,B^2\}u,
 \qquad \frac{u^2}{m}=u^{-c}=m^{-c/(c+2)}.              \tag{25}
\]

Insert (25) and \(L_T\le Cu^{-c}\) into (3). This proves (4) for every \(m\ge1\). In (5), \(D\phi=uD\psi\), both residuals are in \(\mathbb Ru\), and the vector-field equations and all output norms reduce exactly to (2). This proves the Hilbert-space version.

## 5. An admissible example with nonintegrable square-root loss

Take \(d=1\), deterministic input \(X=1\), label \(Y=\pi/2\), Euclidean parameters, activation \(\sigma(w)=\arctan w\), and

\[
                    \rho_0=\tfrac12(\delta_0+\delta_1). \tag{26}
\]

The output Hilbert space \(L^2(P_X)\) is one-dimensional. This is a neural-network instance of the theorem, with \(A=\pi/2\), \(B=1\). It satisfies the Euclidean regularity assumption in Section 2 of Margalit Glasgow and Joan Bruna, *Uniform-in-Time Weak Propagation-of-Chaos in Shallow Neural Networks*, [arXiv:2605.22010v3](https://arxiv.org/html/2605.22010v3): the activation and its first two derivatives have finite total variation, its third derivative is bounded, the data are bounded with \(\mathbb E X^2=d=1\), and the initialization has bounded support. For completeness,

\[
 \sigma'=(1+w^2)^{-1},\quad
 \sigma''=-2w(1+w^2)^{-2},\quad
 \sigma'''=(6w^2-2)(1+w^2)^{-3}.                        \tag{27}
\]

The total variations are \(\pi\), \(2\), and \(3\sqrt3/2\), respectively, for \(\sigma,\sigma',\sigma''\). The last follows from the two extrema of \(\sigma''\), at \(w=\pm1/\sqrt3\), whose absolute values are \(3\sqrt3/8\), and its limits zero at both ends. Equation (27) bounds the third derivative. Thus some fixed finite \(C_{\rm reg}\) meets all of the source conditions.

Write \(Q(w)=w+w^3/3\). The autonomous flow satisfies exactly

\[
 Q(\Psi_s(z))=s+Q(z),\qquad
 \Psi_s(z)=2\sinh\left(\tfrac13
                   \operatorname{arsinh}(3(s+Q(z))/2)\right). \tag{28}
\]

Indeed, differentiating the first identity gives \(\partial_s\Psi=(1+\Psi^2)^{-1}\); the second identity follows from \(\sinh(3a)=3\sinh a+4\sinh^3a\).

Let

\[
 e(s)=\frac\pi2-\frac{\arctan\Psi_s(0)+\arctan\Psi_s(1)}2.
                                                               \tag{29}
\]

For every finite \(s\), \(e(s)>0\). The physical clock solves \(\tau'=e(\tau)\), \(\tau(0)=0\), and tends to infinity: if it had a finite limit, continuity and positivity of \(e\) there would contradict convergence of \(\tau\). As \(s\to\infty\), (28) gives, for each \(z=0,1\),

\[
 \Psi_s(z)\sim(3s)^{1/3},\qquad
 \frac\pi2-\arctan\Psi_s(z)\sim(3s)^{-1/3}.
\]

Thus \(e(s)\sim3^{-1/3}s^{-1/3}\). Integrating \(dt/ds=1/e(s)\) gives

\[
 t\sim\frac{3^{4/3}}4\tau(t)^{4/3},\qquad
 \tau(t)\sim\frac{2\sqrt2}{3}t^{3/4},
\]
\[
 \sqrt{L_t}=e(\tau(t))\sim(4t)^{-1/4},\qquad
                  L_t\sim\frac1{2\sqrt t}.             \tag{30}
\]

To justify the integration explicitly, for any \(\epsilon>0\) the reciprocal \(1/e(s)\) lies between \((1\pm\epsilon)3^{1/3}s^{1/3}\) for all sufficiently large \(s\). Integrating these inequalities and then taking \(\epsilon\downarrow0\) gives the displayed asymptotic relation. Inverting its positive power and substituting into \(e\) gives (30).

Continuity on finite time intervals and (30) show that \(L_t\le C(1+t)^{-1/2}\) for some finite constant \(C\). In particular \(\int_0^\infty\sqrt{L_t}\,dt=\infty\). Formula (4) gives a uniform output bound \(O(m^{-1/5})\) from this loss envelope.

The global curvature quantity used in the preceding rounds does not satisfy their extra logarithmic hypothesis here. The residual is \(r_t=-e(\tau(t))\), so

\[
 h(t)=\sup_w[-r_t\sigma''(w)]_+
     =\frac{3\sqrt3}{8}e(\tau(t)),\qquad
 H(T)=\frac{3\sqrt3}{8}\tau(T)
                 \sim\frac{\sqrt6}{4}T^{3/4}.          \tag{31}
\]

This is a comparison with that global sufficient condition, not a lower bound on weak error. Along the nonnegative trajectories in this particular example the residual curvature has a favorable sign; a localized curvature argument could also exploit it. No necessity of the scalar-clock method is claimed.

The constants in (30)--(31) also follow directly in physical time. Put \(w_j(t)=\Psi_{\tau(t)}(j)\), \(j=0,1\). Since \(Q(w_1)-Q(w_0)=4/3\), the mean value theorem gives

\[
 0\le w_1-w_0\le\frac{4}{3(1+w_0^2)}.
\]

As \(w_0\to\infty\), this implies \(w_1/w_0\to1\) and \(w_0 e(\tau(t))\to1\). Therefore

\[
 \frac d{dt}w_0(t)^4
 =\frac{4w_0(t)^3 e(\tau(t))}{1+w_0(t)^2}\longrightarrow4.
\]

Integrating gives \(w_0(t)^4/t\to4\), hence \(\sqrt t L_t\to1/2\). Finally \(\tau=Q(w_0)\sim w_0^3/3\) gives \(\tau/t^{3/4}\to2\sqrt2/3\), which reproduces the curvature constant \(\sqrt6/4\).

## Scope

The result establishes a decay-only polynomial bound on the stated one-direction subclass. It does not answer T224 for a general output Hilbert space, and it does not determine a sharp exponent even in this subclass. For several output directions, the neuron velocity is a sum of feature-gradient fields with time-dependent coefficients. A single clock as in (10) is then unavailable in general, and the monotonicity argument (14) does not apply. Scalar-valued regression functions at many inputs can have arbitrarily many independent output directions.

The proof treats exact population gradient flow with fixed output coefficients and bounded Euclidean features. It does not treat trained output coefficients, sample error, time discretization, or unbounded activations. The source's Remark 6 already treats the endpoint \(c=2\) in its broader setting, while its Section 6 leaves the slower-decay question open. The background source is Song Mei, Andrea Montanari, and Phan-Minh Nguyen, *A Mean Field View of the Landscape of Two-Layers Neural Networks*, [arXiv:1804.06561](https://arxiv.org/abs/1804.06561). No literature-priority assertion is made for the special-case bound above.
