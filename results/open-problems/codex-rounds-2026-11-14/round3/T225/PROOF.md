# A polynomial spectral gap after removing the sine parameter symmetry

## 1. Model and statement

Let \(X\sim N(0,1)\), let the activation and teacher be respectively

\[
 \sigma(z)=\sin z,\qquad y(X)=\sin X,
\]

and use the half squared risk and fixed parameter prior

\[
 f_\rho(x)=\int a\sin(wx)\,d\rho(a,w),\qquad
 R(\rho)=\tfrac12\mathbb E[(f_\rho(X)-\sin X)^2],\qquad
 \pi=N(0,I_2).
\]

Write \(\gamma=N(0,1)\). At \(\rho=\pi\), the first variation of the risk is
\(-a g(w)\), where

\[
 g(w)=\mathbb E[\sin X\sin(wX)]
 =\frac{e^{-(w-1)^2/2}-e^{-(w+1)^2/2}}2
 =e^{-(1+w^2)/2}\sinh w.
 \tag{1}
\]

The frozen proximal law is therefore

\[
 p_\lambda(da,dw)=Z_\lambda^{-1}e^{a g(w)/\lambda}\pi(da,dw),
 \qquad \lambda>0.
 \tag{2}
\]

Let \(c>0\) solve \(c\tanh c=1\), and put

\[
 M=g(c),\qquad L=\sup_w|g'(w)|\leq1,\qquad
 K=\max\left\{1,\frac{c^2e^{c^2/2}}2,\frac4{c^2}\right\}.
 \tag{3}
\]

The constants in (3) do not depend on \(\lambda\). In particular
\(1<c<2\), so \(K\leq2e^2\).

Let \(S(a,w)=(-a,-w)\). Define the restricted Poincare constant by

\[
 \beta_S(p_\lambda)=
 \inf_{\substack{h\circ S=h\\0<\operatorname{Var}_{p_\lambda}(h)<\infty}}
 \frac{\int |\nabla h|^2\,dp_\lambda}
      {\operatorname{Var}_{p_\lambda}(h)}.
 \tag{4}
\]

The infimum is taken over the weighted Sobolev space; equivalently it can
be taken over smooth invariant functions by approximation. This is the
spectral gap on the invariant subspace, with the Euclidean Dirichlet form.

**Theorem.** For every \(\lambda>0\),

\[
 \boxed{\quad
 \beta_S(p_\lambda)\geq\frac1{K(1+L/\lambda)^2}.
 \quad}
 \tag{5}
\]

In particular, for \(0<\lambda\leq1\),

\[
 \beta_S(p_\lambda)\geq\frac{\lambda^2}{8e^2}.
 \tag{6}
\]

The unrestricted Poincare constant has the exponentially small scale proved
in the earlier work. Thus that scale disappears from the Poincare estimate
when testing only functions invariant under the feature-preserving symmetry.
The theorem concerns (2), with its drift frozen at \(\rho=\pi\).

## 2. Kernel geometry and exact Gaussian elimination

The identity for the Gaussian characteristic function, applied to
\(2\sin X\sin(wX)=\cos((1-w)X)-\cos((1+w)X)\), proves (1).
The function \(g\) is odd and positive on \((0,\infty)\). Its derivative there is

\[
 g'(w)=e^{-(1+w^2)/2}(\cosh w-w\sinh w).
 \tag{7}
\]

The function \(w\tanh w\) strictly increases from zero to infinity, because
its derivative is \(\tanh w+w\operatorname{sech}^2w>0\). Thus \(g\)
strictly increases on \([0,c]\), strictly decreases on \([c,\infty)\), and
tends to zero at infinity. The same monotonicities hold for \(g^2\).
At \(w=1\) the product \(w\tanh w<1\), whereas \(2\tanh2>1\): the latter
is equivalent to \(e^4>3\), which follows from \(e^4>1+4\).
Consequently \(1<c<2\). Also, differentiating the expectation in (1) gives

\[
 |g'(w)|=|\mathbb E[X\sin X\cos(wX)]|
 \leq(\mathbb E X^2)^{1/2}(\mathbb E\sin^2X)^{1/2}\leq1.
 \tag{8}
\]

Completing the square in (2) gives

\[
 -\frac{a^2+w^2}2+\frac{ag(w)}\lambda
 =-\frac{(a-g(w)/\lambda)^2}2-\frac{w^2}2
    +\frac{g(w)^2}{2\lambda^2}.
 \tag{9}
\]

It follows that

\[
 \begin{split}
 Z_\lambda&=\int e^{g(w)^2/(2\lambda^2)}\,\gamma(dw),\\
 \nu_\lambda(dw)&=Z_\lambda^{-1}e^{g(w)^2/(2\lambda^2)}\gamma(dw),\\
 a\mid w&\sim N(g(w)/\lambda,1).
 \end{split}
 \tag{10}
\]

The normalizing integral is finite because \(|g|\leq M\). The law
\(\nu_\lambda\) is even, and \(p_\lambda\) is invariant under \(S\).

Let \(\nu_\lambda^+\) be the law of \(|w|\) under \(\nu_\lambda\). Its
Lebesgue density \(q_\lambda\) on \([0,\infty)\) satisfies

\[
 q_\lambda(r)\ \propto
 \exp\left(-\frac{r^2}2+\frac{g(r)^2}{2\lambda^2}\right).
 \tag{11}
\]

The normalization in (11) will cancel from all the density ratios below.

## 3. An anchored inequality for the folded marginal

We prove, uniformly in \(\lambda>0\),

\[
 \operatorname{Var}_{\nu_\lambda^+}(u)
 \leq C\int_0^\infty |u'(r)|^2q_\lambda(r)\,dr,
 \qquad
 C=\max\left\{\frac{c^2e^{c^2/2}}2,\frac4{c^2}\right\}.
 \tag{12}
\]

It suffices to control the squared distance from the value at \(c\), since
the mean minimizes the squared distance from a constant. The estimates first
apply to continuously differentiable functions, and then to locally
absolutely continuous functions of finite energy by truncation and limits.

For \(0\leq r\leq s\leq c\), monotonicity of \(g^2\) gives

\[
 \frac{q_\lambda(r)}{q_\lambda(s)}
 =\exp\left(\frac{s^2-r^2}2+
        \frac{g(r)^2-g(s)^2}{2\lambda^2}\right)
 \leq e^{c^2/2}.
 \tag{13}
\]

Cauchy--Schwarz on \([r,c]\), followed by Tonelli, yields

\[
 \begin{split}
 \int_0^c|u(r)-u(c)|^2q_\lambda(r)\,dr
 &\leq\int_0^c(c-r)q_\lambda(r)\int_r^c|u'(s)|^2\,ds\,dr\\
 &=\int_0^c|u'(s)|^2\int_0^s(c-r)q_\lambda(r)\,dr\,ds\\
 &\leq e^{c^2/2}\int_0^c|u'(s)|^2q_\lambda(s)
                       (cs-s^2/2)\,ds\\
 &\leq\frac{c^2e^{c^2/2}}2
             \int_0^c|u'(s)|^2q_\lambda(s)\,ds.
 \end{split}
 \tag{14}
\]

For \(r\geq s\geq c\), the other monotonicity of \(g^2\) gives

\[
 \frac{q_\lambda(r)}{q_\lambda(s)}
 \leq e^{-(r^2-s^2)/2}\leq e^{-c(r-s)}.
 \tag{15}
\]

Fix \(0<\eta<c\). Weighted Cauchy--Schwarz gives

\[
 \begin{split}
 |u(r)-u(c)|^2
 &=\left|\int_c^r
      e^{-\eta(r-s)/2}e^{\eta(r-s)/2}u'(s)\,ds\right|^2\\
 &\leq\left(\int_c^r e^{-\eta(r-s)}\,ds\right)
        \int_c^r e^{\eta(r-s)}|u'(s)|^2\,ds\\
 &\leq\eta^{-1}\int_c^r e^{\eta(r-s)}|u'(s)|^2\,ds.
 \end{split}
 \tag{16}
\]

Integrating in \(r\), using Tonelli and then (15), gives

\[
 \begin{split}
 \int_c^\infty |u(r)-u(c)|^2q_\lambda(r)\,dr
 &\leq\eta^{-1}\int_c^\infty |u'(s)|^2
       \int_s^\infty e^{\eta(r-s)}q_\lambda(r)\,dr\,ds\\
 &\leq\frac1{\eta(c-\eta)}
       \int_c^\infty |u'(s)|^2q_\lambda(s)\,ds.
 \end{split}
 \tag{17}
\]

Taking \(\eta=c/2\) gives the constant \(4/c^2\). Adding (14) and (17),
and bounding each coefficient by \(C\), proves (12). No convexity of
\(-\log q_\lambda\) is needed. In particular, the argument does not assume
that the maximum of \(q_\lambda\) itself is at \(c\).

## 4. Product inequality, shear, and symmetry

The standard Gaussian Poincare inequality is

\[
 \operatorname{Var}_\gamma(v)\leq\int |v'|^2\,d\gamma.
 \tag{18}
\]

For completeness, its semigroup proof uses
\(P_t v(x)=\mathbb E[v(e^{-t}x+\sqrt{1-e^{-2t}}G)]\).
Gaussian integration by parts gives
\(-d\int(P_tv)^2d\gamma/dt=2\int|(P_tv)'|^2d\gamma\), and
\((P_tv)'=e^{-t}P_tv'\). Jensen and invariance give
\(\int|(P_tv)'|^2d\gamma\leq e^{-2t}\int|v'|^2d\gamma\).
Integration from zero to infinity proves (18) for bounded smooth \(v\),
then approximation proves it for finite-energy functions.

For \(\mu_\lambda^+=\gamma(db)\otimes\nu_\lambda^+(dr)\), variance
decomposition, (18), (12), and Jensen give

\[
 \begin{split}
 \operatorname{Var}_{\mu_\lambda^+}(H)
 &=\int\operatorname{Var}_\gamma(H(\cdot,r))\,d\nu_\lambda^+(r)
    +\operatorname{Var}_{\nu_\lambda^+}\left(\int H(b,\cdot)\,d\gamma(b)\right)\\
 &\leq\int |H_b|^2\,d\mu_\lambda^+
      +C\int\left|\int H_r(b,r)\,d\gamma(b)\right|^2d\nu_\lambda^+(r)\\
 &\leq K\int(|H_b|^2+|H_r|^2)\,d\mu_\lambda^+.
 \end{split}
 \tag{19}
\]

Let \(p_\lambda^+\) be \(p_\lambda\) conditioned on \(w>0\). By (9), it
is the pushforward of \(\mu_\lambda^+\) by the shear

\[
 T_\lambda(b,r)=(b+g(r)/\lambda,r).
 \tag{20}
\]

For \(H=h\circ T_\lambda\), the chain rule gives

\[
 H_b=h_a\circ T_\lambda,\qquad
 H_r=(h_w+(g'(r)/\lambda)h_a)\circ T_\lambda.
 \tag{21}
\]

The matrix in (21) is the identity plus a matrix with operator norm at most
\(L/\lambda\); hence

\[
 \operatorname{Var}_{p_\lambda^+}(h)
 \leq K(1+L/\lambda)^2\int |\nabla h|^2\,dp_\lambda^+.
 \tag{22}
\]

If \(h\circ S=h\), then \(h,h^2\), and \(|\nabla h|^2\) are invariant
under \(S\). Indeed differentiating the invariance gives
\(\nabla h(S\theta)=-\nabla h(\theta)\). Since \(p_\lambda\) is invariant,
and the two half-planes each have mass \(1/2\),

\[
 \operatorname{Var}_{p_\lambda}(h)=
 \operatorname{Var}_{p_\lambda^+}(h),\qquad
 \int|\nabla h|^2\,dp_\lambda=
 \int|\nabla h|^2\,dp_\lambda^+.
 \tag{23}
\]

Thus (22) proves (5). There is no boundary-condition claim here: (22)
holds for every half-plane Sobolev function, a class larger than the
restrictions of globally invariant functions.

Since \(c<2\), \(c^2e^{c^2/2}/2\leq2e^2\); since \(c>1\),
\(4/c^2<4<2e^2\). Thus \(K\leq2e^2\). For \(\lambda\leq1\), (8) gives
\((1+L/\lambda)^2\leq4/\lambda^2\), proving (6).

All inequalities extend to the Sobolev classes used in (4): the densities
are smooth and strictly positive, and the shear is globally bi-Lipschitz
for each fixed \(\lambda\). Local smooth approximation followed by cutoffs
gives the extension. To preserve global invariance, average an approximation
with its composition with the orthogonal map \(S\).

## 5. Consequence for the frozen linear diffusion

Consider only the linear diffusion with the drift frozen at initialization:

\[
 \begin{split}
 dA_t&=(g(W_t)-\lambda A_t)\,dt+\sqrt{2\lambda}\,dB_t^{(1)},\\
 dW_t&=(A_tg'(W_t)-\lambda W_t)\,dt+\sqrt{2\lambda}\,dB_t^{(2)}.
 \end{split}
 \tag{24}
\]

Its generator is

\[
 \mathcal L_\lambda=\lambda\Delta+
     (g(w)-\lambda a)\partial_a+(ag'(w)-\lambda w)\partial_w
 =\lambda p_\lambda^{-1}\operatorname{div}(p_\lambda\nabla).
 \tag{25}
\]

The drift is locally Lipschitz and of at most linear growth, by (8) and
boundedness of \(g\), so there is no finite-time explosion. Integration by
parts on compactly supported smooth tests gives the symmetric Dirichlet
form \(-\int u\mathcal L_\lambda v\,dp_\lambda
=\lambda\int\nabla u\cdot\nabla v\,dp_\lambda\). It also gives invariance
of \(p_\lambda\). The drift satisfies \(b(S\theta)=S b(\theta)\), so the
semigroup preserves invariant functions and laws.

Let \(\rho_t\) be its law with \(\rho_0=\pi\), and write
\(q_t=d\rho_t/dp_\lambda\). Reversibility gives
\(\partial_tq_t=\mathcal L_\lambda q_t\). The initial density and its
second moment are exactly

\[
 q_0=Z_\lambda e^{-ag(w)/\lambda},\qquad
 \int q_0^2\,dp_\lambda
 =Z_\lambda\int e^{-ag(w)/\lambda}\,d\pi
 =Z_\lambda^2.
 \tag{26}
\]

The last equality follows from the Gaussian moment generating function in
\(a\). Both \(q_0\) and \(q_t\) are invariant under \(S\). The energy
identity and (5) therefore imply

\[
 \begin{split}
 \frac d{dt}\chi^2(\rho_t\Vert p_\lambda)
 &=-2\lambda\int |\nabla q_t|^2\,dp_\lambda\\
 &\leq-\frac{2\lambda}{K(1+L/\lambda)^2}
           \chi^2(\rho_t\Vert p_\lambda),
 \end{split}
 \tag{27}
\]

and hence

\[
 \chi^2(\rho_t\Vert p_\lambda)
 \leq (Z_\lambda^2-1)
       \exp\left(-\frac{2\lambda t}{K(1+L/\lambda)^2}\right).
 \tag{28}
\]

One can justify (27) first for bounded smooth invariant initial densities,
then by approximation in \(L^2(p_\lambda)\). Equation (26) supplies the
required finite initial norm. Equivalently the self-adjoint semigroup
energy identity gives (27) for positive times and its integrated version
at time zero.

Since \(Z_\lambda\leq e^{M^2/(2\lambda^2)}\), (6) yields the explicit bound
for \(0<\lambda\leq1\):

\[
 \chi^2(\rho_t\Vert p_\lambda)
 \leq\exp\left(\frac{M^2}{\lambda^2}
                   -\frac{\lambda^3t}{4e^2}\right).
 \tag{29}
\]

Furthermore (10) gives
\(\int a^2dp_\lambda=1+\lambda^{-2}\int g(w)^2d\nu_\lambda
\leq1+M^2/\lambda^2\). Pointwise Cauchy--Schwarz and \(|\sin|\leq1\) give

\[
 \begin{split}
 \|f_{\rho_t}-f_{p_\lambda}\|_{L^2(N(0,1))}^2
 &\leq\left(\int a^2dp_\lambda\right)
             \int(q_t-1)^2dp_\lambda\\
 &\leq(1+M^2/\lambda^2)
     \exp\left(\frac{M^2}{\lambda^2}
                   -\frac{\lambda^3t}{4e^2}\right).
 \end{split}
 \tag{30}
\]

Thus an input \(L^2\) predictor distance at most \(\delta\in(0,1)\) from
the frozen equilibrium is reached by time

\[
 t=\frac{4e^2}{\lambda^3}
 \left[\frac{M^2}{\lambda^2}
       +\log\left(\frac{1+M^2/\lambda^2}{\delta^2}\right)\right].
 \tag{31}
\]

This is polynomial in inverse temperature, despite the exponentially small
unrestricted spectral gap. It is not a time to small teacher risk.

## 6. The frozen equilibrium does not solve the regression task

In fact its teacher risk diverges as the temperature decreases. We give
the asymptotic to make the distinction in Section 5 quantitative.

The only maximizers of \(g^2\) are \(\{-c,c\}\). If \(U\) is any open
neighborhood of these points, continuity, decay at infinity and uniqueness
of the maxima give \(s=\sup_{U^c}g^2<M^2\). Choose \(s<v<M^2\).
There is a bounded interval \(I\subset U\) of positive Gaussian mass on
which \(g^2\geq v\). Equation (10) then gives

\[
 \nu_\lambda(U^c)\leq\gamma(I)^{-1}
                    e^{-(v-s)/(2\lambda^2)}\longrightarrow0.
 \tag{32}
\]

Evenness supplies equal masses at the two limiting points, so
\(\nu_\lambda\) converges weakly to
\((\delta_c+\delta_{-c})/2\). Conditioning in (10) gives

\[
 \lambda f_{p_\lambda}(x)
 =\int g(w)\sin(wx)\,d\nu_\lambda(w)
 \longrightarrow M\sin(cx).
 \tag{33}
\]

For each \(x\) the integrand is bounded and continuous; also the left
side of (33) is bounded by \(M\). Dominated convergence in the Gaussian
input law therefore proves convergence in input \(L^2\). Consequently

\[
 \boxed{\quad
 \lim_{\lambda\downarrow0}\lambda^2R(p_\lambda)
 =\frac{M^2}{4}(1-e^{-2c^2})>0.
 \quad}
 \tag{34}
\]

Here \(\mathbb E\sin^2(cX)=(1-e^{-2c^2})/2\), and the teacher term
\(\lambda\sin X\) vanishes in the scaled squared loss.

In the nonlinear MFLD, the function in the drift is instead

\[
 g_t(w)=\mathbb E[(\sin X-f_{\rho_t}(X))\sin(wX)].
 \tag{35}
\]

The symmetry still preserves predictions, and a symmetric initialization
is preserved whenever the nonlinear equation has a unique solution.
However, (35) need not have the single-peak geometry used in (13) and
(15). No uniform-in-time quotient gap or nonlinear risk dissipation bound
has been proved here. Equations (5)--(31) cannot be transferred to (35)
without an additional argument.

## 7. Exact symmetry reduction for the nonlinear equation

Although the gap bound is frozen, removal of the odd component is exact
for the nonlinear equation as well. The following statement does not assume
the single-peak property of \(g\).

Let \(\lambda(t)>0\) be a prescribed temperature schedule. Consider a
solution \(\rho_t\) of MFLD for which the following weak equation is defined
(finite second parameter moments suffice for its displayed integrals):

\[
 \frac d{dt}\int\psi\,d\rho_t
 =\int\mathcal L_{\rho_t,t}\psi\,d\rho_t,
 \tag{36}
\]

where, for smooth compactly supported \(\psi\),

\[
 \mathcal L_{\rho,t}\psi
 =\lambda(t)\Delta\psi+
   (g_\rho(w)-\lambda(t)a)\psi_a+
   (ag_\rho'(w)-\lambda(t)w)\psi_w,
 \quad
 g_\rho(w)=\mathbb E[(\sin X-f_\rho(X))\sin(wX)].
 \tag{37}
\]

Define \(\rho^+=(\rho+S_\#\rho)/2\). Then

\[
 f_{\rho^+}=f_\rho,\qquad g_{\rho^+}=g_\rho.
 \tag{38}
\]

Indeed the feature \(\phi_x(a,w)=a\sin(wx)\) satisfies
\(\phi_x\circ S=\phi_x\), so integration against the average leaves it
unchanged. Also \(g_\rho\) is odd in \(w\) and \(g_\rho'\) is even.
The derivative exists by differentiation under the input expectation:
the residual is in input \(L^2\), so its product with \(|X|\) is integrable.
Thus the drift in (37) obeys \(b_{\rho,t}(S\theta)=S b_{\rho,t}(\theta)\).
The orthogonality of \(S\) gives

\[
 \mathcal L_{\rho,t}(\psi\circ S)
 =(\mathcal L_{\rho,t}\psi)\circ S.
 \tag{39}
\]

Average (36) with the same equation tested against \(\psi\circ S\).
Using (39) and then (38) gives

\[
 \frac d{dt}\int\psi\,d\rho_t^+
 =\int\mathcal L_{\rho_t,t}\psi\,d\rho_t^+
 =\int\mathcal L_{\rho_t^+,t}\psi\,d\rho_t^+.
 \tag{40}
\]

Therefore the symmetrized law itself solves the same nonlinear MFLD,
with the same temperature schedule and its symmetrized initial law.
In any solution class where this equation is unique, two initial laws
with the same symmetrization have identical prediction and risk trajectories.
No general well-posedness theorem is asserted here; (40) is a direct identity
for solutions satisfying (36).

In particular, take the earlier odd cutoff \(h_r(w)\), the invariant law
\(p_{\lambda_0}\) for some \(\lambda_0>0\), and

\[
 \rho_{\eta,0}=(1+\eta h_r(w))p_{\lambda_0},\qquad |\eta|<1.
 \tag{41}
\]

The cutoff has zero mean and changes sign under \(S\); hence these are
probability laws and every one has symmetrization \(p_{\lambda_0}\).
For unique nonlinear evolutions, their risk trajectories coincide for
all times, including under a common annealing schedule. Thus the odd
bottleneck cannot affect prediction through later nonlinear feedback.
Controlling the even component with the changing residual remains open.
