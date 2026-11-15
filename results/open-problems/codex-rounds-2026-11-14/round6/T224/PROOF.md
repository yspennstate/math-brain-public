# Commuting feature gradients give polynomial uniform output rates

## Statement

Let \(\psi:\mathbb R^d\to\mathbb R^k\) be \(C^2\), where \(k<\infty\), and suppose

\[
 \sup_w|\psi(w)|\le A,\qquad
 \sup_w\|D\psi(w)\|_{\rm op}\le B,\qquad
 |D^2\psi(w)[u,v]|\le M|u||v|.                         \tag{1}
\]

All constants are finite and nonnegative. Write \(X_j=\nabla\psi_j\). Assume the feature-gradient fields commute everywhere:

\[
 DX_j(w)X_i(w)=DX_i(w)X_j(w)
 \quad(1\le i,j\le k,\ w\in\mathbb R^d).               \tag{2}
\]

For a target \(\gamma\in\mathbb R^k\), consider exact Euclidean population gradient flow, using half the squared loss:

\[
 f_t=\int\psi(v)\rho_t(dv),\qquad
 \dot v=D\psi(v)^\top(\gamma-f_t),
\]
\[
 f_t^m=\frac1m\sum_{i=1}^m\psi(w_i(t)),\qquad
 \dot w_i=D\psi(w_i)^\top(\gamma-f_t^m),\qquad
 w_i(0)=Z_i\stackrel{\rm iid}\sim\rho_0.               \tag{3}
\]

Set \(L_t=|f_t-\gamma|^2\).

**Theorem.** Under (1)--(3), for every deterministic \(T\ge0\) and integer \(m\ge1\),

\[
 \boxed{\displaystyle
 \sup_{t\ge0}\mathbb E|f_t^m-f_t|^2
 \le \frac{4A^2(1+B^2T)^2}{m}+6L_T.}                  \tag{4}
\]

Consequently, if \(L_t\le C(1+t)^{-c}\) for \(c>0\), then

\[
 \boxed{\displaystyle
 \sup_{t\ge0}\mathbb E|f_t^m-f_t|^2
 \le \bigl(4A^2\max\{1,B^4\}+6C\bigr)
                         m^{-c/(c+2)}.}               \tag{5}
\]

This extends the preceding one-output-direction theorem. The extra structural assumption is (2). It is automatic for \(k=1\), but is not a consequence of bounded smoothness or slow loss decay. No square-root-loss integrability is imposed. The supremum is outside expectation, and no sharpness is claimed.

There is a Hilbert-space version. Let \(\mathcal H\) be a real Hilbert space, let \(U:\mathbb R^k\to\mathcal H\) be an isometry, and let

\[
 \phi(w)=b+U\psi(w),\qquad g=b+U\gamma.                \tag{6}
\]

Then (4)--(5) hold for \(\|f_t^m-f_t\|_{\mathcal H}^2\). If all features lie in the affine subspace \(b+U\mathbb R^k\), the hypothesis \(\|f_t-g\|\to0\) forces \(g\) into that subspace, since it is closed. Thus (6) does not impose an additional target assumption in the loss-decay setting. For \(\mathcal H=L^2(P_X)\), these are weak output bounds.

## 1. The joint autonomous flow

By (1), every \(X_j\) is globally Lipschitz with constant at most \(M\) and bounded in norm by \(B\). Its autonomous flow \(\Phi_j^s\) exists for all \(s\in\mathbb R\), is \(C^1\) in the initial condition, and satisfies

\[
 \partial_s\Phi_j^s(z)=X_j(\Phi_j^s(z)),\qquad
 \Phi_j^0(z)=z.                                       \tag{7}
\]

Global Lipschitz continuity gives uniqueness and local existence, and the bound \(|\Phi_j^s(z)-z|\le B|s|\) prevents finite-time escape in either direction.

Fix \(i,j,z\). The vector
\(V(s)=D_z\Phi_i^s(z)X_j(z)\) solves the variational equation

\[
 V'(s)=DX_i(\Phi_i^s(z))V(s),\qquad V(0)=X_j(z).
\]

On the other hand, \(W(s)=X_j(\Phi_i^s(z))\) satisfies, by (2),

\[
 W'(s)=DX_j(\Phi_i^s(z))X_i(\Phi_i^s(z))
       =DX_i(\Phi_i^s(z))W(s),\qquad W(0)=X_j(z).
\]

Uniqueness for this linear equation gives

\[
 D_z\Phi_i^s(z)X_j(z)=X_j(\Phi_i^s(z)).                \tag{8}
\]

For fixed \(s\), differentiate \(t\mapsto\Phi_i^s(\Phi_j^t(z))\). Equation (8) says that it is an integral curve of \(X_j\), starting at \(\Phi_i^s(z)\). Hence

\[
 \Phi_i^s\circ\Phi_j^t=\Phi_j^t\circ\Phi_i^s.         \tag{9}
\]

Define, for \(s=(s_1,\ldots,s_k)\in\mathbb R^k\),

\[
 \Psi_s(z)=\Phi_k^{s_k}\circ\cdots\circ\Phi_1^{s_1}(z).
                                                               \tag{10}
\]

It is defined globally, and (9) makes its order immaterial. Move the \(j\)-th factor to the outside before differentiating; this gives

\[
 \partial_{s_j}\Psi_s(z)=X_j(\Psi_s(z)),\qquad
 D_s\Psi_s(z)=D\psi(\Psi_s(z))^\top.                  \tag{11}
\]

In particular \(\Psi_0(z)=z\) and \(\Psi_{s+r}=\Psi_s\circ\Psi_r\).

## 2. The feature-average map has a Gram Jacobian

Define

\[
 a(s,z)=\psi(\Psi_s(z)),\qquad
 F(s)=\mathbb E a(s,Z),\qquad
 F_m(s)=\frac1m\sum_i a(s,Z_i).                        \tag{12}
\]

The chain rule and (11) give the exact identity

\[
 D_s a(s,z)=D\psi(\Psi_s(z))D\psi(\Psi_s(z))^\top.
                                                               \tag{13}
\]

This matrix is symmetric positive semidefinite, and its operator norm is at most \(B^2\). The bounded derivative justifies differentiation under expectation in (12), for example by applying dominated convergence to difference quotients written as integrals along segments. Continuity of the averaged derivative follows by the same domination. Therefore

\[
 0\preceq DF(s),DF_m(s)\preceq B^2I_k,
 \qquad |F(s)|,|F_m(s)|\le A.                         \tag{14}
\]

For \(s,r\in\mathbb R^k\), integrating the Jacobian along their segment gives

\[
 F_m(s)-F_m(r)=K_m(s,r)(s-r),
 \quad K_m(s,r)=\int_0^1DF_m(r+\theta(s-r))\,d\theta,
\]
\[
 0\preceq K_m(s,r)\preceq B^2I_k.                    \tag{15}
\]

In particular \(F_m\) is monotone in the vector sense,
\(\langle s-r,F_m(s)-F_m(r)\rangle\ge0\), and is \(B^2\)-Lipschitz. The same statements hold for \(F\). Equation (13) proves the proposed missing lemma for any finite number of commuting feature-gradient fields.

## 3. Vector clocks represent both interacting systems

Let

\[
 \tau'=\gamma-F(\tau),\qquad
 \tau_m'=\gamma-F_m(\tau_m),\qquad
 \tau(0)=\tau_m(0)=0\in\mathbb R^k.                   \tag{16}
\]

Both vector fields are globally Lipschitz and bounded by \(|\gamma|+A\), so these clocks exist uniquely for all nonnegative physical times. Define

\[
 v_t(z)=\Psi_{\tau(t)}(z),\qquad
 w_i(t)=\Psi_{\tau_m(t)}(Z_i).                         \tag{17}
\]

Differentiating (17) using (11) and (16) gives (3), and taking averages gives

\[
 f_t=F(\tau(t)),\qquad f_t^m=F_m(\tau_m(t)).           \tag{18}
\]

Thus (17) constructs global solutions. These are the usual unique population flows. Indeed, for two population characteristic families \(v_t(z),\widetilde v_t(z)\) starting from the same law and coupled identically at time zero, bounded outputs imply residual norms at most \(|\gamma|+A\). Subtracting their velocities gives

\[
 |\dot v_t(z)-\dot{\widetilde v}_t(z)|
 \le M(|\gamma|+A)|v_t(z)-\widetilde v_t(z)|
             +B|f_t-\widetilde f_t|.
\]

Also \(|f_t-\widetilde f_t|\le B\mathbb E|v_t(Z)-\widetilde v_t(Z)|\). Integrating in time, averaging, and applying the scalar Gronwall inequality shows that this expected paired distance is zero. The distance is integrable on bounded intervals because both velocities are bounded and their initial difference is zero; no moment condition on \(\rho_0\) is needed. The finite system is unique by the same argument with empirical averages.

## 4. Contractive clock comparison

Set

\[
 q(t)=\tau_m(t)-\tau(t),\qquad
 \zeta_t=F_m(\tau(t))-F(\tau(t)),\qquad
 D_t=F_m(\tau_m(t))-F_m(\tau(t)).                       \tag{19}
\]

Subtracting (16) gives

\[
 q'=-D_t-\zeta_t=-K_tq-\zeta_t,\qquad q(0)=0,
 \quad K_t=K_m(\tau_m(t),\tau(t)),
 \quad 0\preceq K_t\preceq B^2I_k.                    \tag{20}
\]

For \(\varepsilon>0\),

\[
 \frac d{dt}\sqrt{|q|^2+\varepsilon^2}
 =\frac{-\langle q,K_tq\rangle-\langle q,\zeta_t\rangle}
             {\sqrt{|q|^2+\varepsilon^2}}
 \le |\zeta_t|.
\]

Integration and \(\varepsilon\downarrow0\) yield

\[
                    |q(t)|\le\int_0^t|\zeta_s|\,ds.  \tag{21}
\]

A second derivation checks the matrix issue in (20). For each realized sample, let \(R(t,s)\) be the evolution matrix solving \(\partial_tR(t,s)=-K_tR(t,s)\), \(R(s,s)=I_k\). Every homogeneous solution \(z\) satisfies
\((|z|^2)'=-2\langle z,K_tz\rangle\le0\), so \(\|R(t,s)\|_{\rm op}\le1\) for \(t\ge s\). Variation of constants gives

\[
 q(t)=-\int_0^t R(t,s)\zeta_s\,ds,
\]

which proves (21) again. No commutation between the matrices \(K_t\) at different times is needed; only positive semidefiniteness at each time is used.

The clock \(\tau(t)\) is deterministic. The random vectors \(a(\tau(t),Z_i)\) are iid, and (1) gives

\[
 \mathbb E|\zeta_t|^2
 =\frac{\mathbb E|a(\tau(t),Z)|^2-|F(\tau(t))|^2}{m}
 \le\frac{A^2}{m}.                                   \tag{22}
\]

Cauchy--Schwarz in time and Tonelli give

\[
 \mathbb E|q(t)|^2
 \le t\int_0^t\mathbb E|\zeta_s|^2\,ds
 \le\frac{A^2t^2}{m}.                                \tag{23}
\]

No temporal independence or iid assertion at the empirical clock is used. Since \(f_t^m-f_t=D_t+\zeta_t\), (15), Minkowski in probability-space \(L^2\), and (22)--(23) imply

\[
 \bigl(\mathbb E|f_t^m-f_t|^2\bigr)^{1/2}
 \le B^2\bigl(\mathbb E|q(t)|^2\bigr)^{1/2}
                +\bigl(\mathbb E|\zeta_t|^2\bigr)^{1/2}
 \le\frac{A(1+B^2t)}{\sqrt m}.                        \tag{24}
\]

## 5. All times and the exponent

Let \(L_t^m=|f_t^m-\gamma|^2\). Direct differentiation of (3) gives

\[
 (L_t^m)'=-\frac2m\sum_i
       |D\psi(w_i)^\top(f_t^m-\gamma)|^2\le0,
\]
\[
 L_t'=-2\int|D\psi(v)^\top(f_t-\gamma)|^2\rho_t(dv)
       \le0.                                        \tag{25}
\]

For \(t\ge T\), two squared triangle inequalities give

\[
 \begin{split}
 \mathbb E|f_t^m-f_t|^2
 &\le2\mathbb E L_t^m+2L_t
 \le2\mathbb E L_T^m+2L_T\\
 &\le4\mathbb E|f_T^m-f_T|^2+6L_T.
 \end{split}                                        \tag{26}
\]

Combining (24) on \([0,T]\) with (26) proves (4), including \(T=0\). For (5), put \(u=m^{1/(c+2)}\) and \(T=u-1\). Then \(u\ge1\),

\[
 1+B^2(u-1)\le\max\{1,B^2\}u,\qquad
 \frac{u^2}{m}=u^{-c}=m^{-c/(c+2)}.                    \tag{27}
\]

Insert (27) and \(L_T\le Cu^{-c}\) into (4). In the Hilbert formulation (6), \(D\phi=UD\psi\), and isometry reduces the velocities, losses, and errors exactly to (3). This proves that version too. The prefactor has no additional dependence on \(k\); it is polynomial in \(d\) whenever the aggregate bounds \(A,B,C\) are polynomial in \(d\).

## 6. A two-input neural-network instance with slow loss

Let \(d=2\), and let the input take the values \(\sqrt2 e_1,\sqrt2 e_2\) with equal probabilities. Let \(Y=\pi/2\), \(\sigma=\arctan\), and \(\rho_0\) be uniform on

\[
 \left\{(0,0),(0,1/\sqrt2),(1/\sqrt2,0),
                     (1/\sqrt2,1/\sqrt2)\right\}.    \tag{28}
\]

The orthonormal basis of \(L^2(P_X)\) is \(u_j(x)=\sqrt2\,1_{\{x=\sqrt2 e_j\}}\). In these coordinates,

\[
 \psi_j(w)=\frac1{\sqrt2}\arctan(\sqrt2 w_j),\qquad
 \gamma_j=\frac\pi{2\sqrt2},\qquad j=1,2.             \tag{29}
\]

The two gradients act on separate parameter coordinates and commute. Valid aggregate bounds are \(A=\pi/2\) and \(B=1\); \(M<\infty\). The output image has a two-dimensional affine span. Thus this is outside the preceding affine-line theorem.

The activation satisfies the Euclidean regularity assumption of Margalit Glasgow and Joan Bruna, *Uniform-in-Time Weak Propagation-of-Chaos in Shallow Neural Networks*, [arXiv:2605.22010v3](https://arxiv.org/html/2605.22010v3), Section 2: \(\arctan\), its first derivative, and its second derivative have total variations \(\pi,2,3\sqrt3/2\), respectively; its third derivative is \((6w^2-2)/(1+w^2)^3\), which is bounded. The data and initialization here are bounded, \(\mathbb E|X|^2=2=d\), and the label has finite second moment. Hence one fixed finite regularity constant suffices.

Write \(a_j=\sqrt2 w_j\), and let \(h_j(t)=\mathbb E\arctan a_j(t)\). The physical neuron equation from (29) is

\[
 \dot w_j=\frac{\pi/2-h_j(t)}{\sqrt2(1+2w_j^2)},
 \qquad
 \dot a_j=\frac{\pi/2-h_j(t)}{1+a_j^2}.                \tag{30}
\]

Each marginal is therefore exactly the previous scalar arctangent system initialized uniformly on \(\{0,1\}\), with no time rescaling. For clarity, its asymptotic constant can be derived directly. For the two marginal particles \(a_0,a_1\), put \(e(t)=\pi/2-(\arctan a_0+\arctan a_1)/2>0\) and \(Q(a)=a+a^3/3\). Then

\[
 (Q(a_i))'=e(t),\qquad Q(a_1)-Q(a_0)=4/3.             \tag{31}
\]

The common clock \(s(t)=\int_0^t e(v)\,dv\) tends to infinity: a finite limit would leave \(a_i\) finite and \(e\) bounded below by a positive constant. Consequently \(a_0\to\infty\). The mean value theorem gives
\(0\le a_1-a_0\le4/[3(1+a_0^2)]\), so \(a_1/a_0\to1\) and \(a_0e(t)\to1\). Hence

\[
 \frac d{dt}a_0^4=\frac{4a_0^3e(t)}{1+a_0^2}\to4,
 \qquad e(t)^2\sim\frac1{2\sqrt t}.                  \tag{32}
\]

The two marginals are identical, and the population output norm uses the input probabilities \(1/2\), so

\[
 L_t=\frac12 e(t)^2+\frac12 e(t)^2
                  \sim\frac1{2\sqrt t}.              \tag{33}
\]

Continuity on compact intervals and (33) give \(L_t\le C(1+t)^{-1/2}\) for some finite \(C\), while \(\int_0^\infty\sqrt{L_t}\,dt=\infty\). The new theorem gives a uniform \(O(m^{-1/5})\) weak output bound for this two-input instance. This is an upper-bound application, not a lower bound or sharpness example. Empirical coordinate samples can be correlated; independence within each neuron is not used by the theorem.

## 7. Why noncommuting fields obstruct this clock argument

The Gram identity (13) relies on (11), not just on positivity of a Gram matrix in parameter space. The following source-admissible feature map shows that an ordered composition of noncommuting gradient flows need not produce a monotone feature map.

Let \(d=1\), \(\alpha=\sqrt{2/5}\), and let the input take \(\alpha,2\alpha\) with equal probabilities. Then \(\mathbb E X^2=1=d\). With \(\sigma=\arctan\), the orthonormal output coordinates are

\[
 \psi_1(w)=\frac{\arctan(\alpha w)}{\sqrt2},\qquad
 \psi_2(w)=\frac{\arctan(2\alpha w)}{\sqrt2}.          \tag{34}
\]

All features and derivatives are bounded, and the same activation regularity applies. Put \(u=\alpha w\). The fields are

\[
 X_1(w)=\frac\alpha{\sqrt2(1+u^2)},\qquad
 X_2(w)=\frac{\sqrt2\alpha}{1+4u^2}.
\]

Direct differentiation gives their bracket, in the convention of (2),

\[
 DX_2(w)X_1(w)-DX_1(w)X_2(w)
   =-\frac{6\alpha^3u}{(1+u^2)^2(1+4u^2)^2},         \tag{35}
\]

which is nonzero for \(u\ne0\).

Let \(\Phi_j\) be these autonomous flows and define the ordered map

\[
 \Theta(s_1,s_2)=\Phi_2^{s_2}(\Phi_1^{s_1}(0)),
 \qquad G(s)=\psi(\Theta(s)).                         \tag{36}
\]

At \(s_*=(0,35/(6\sqrt2))\), one has \(\Theta(s_*)=1/\alpha\). Indeed, along \(X_2\),
\(du/ds_2=\sqrt2\alpha^2/(1+4u^2)\), so travel from \(u=0\) to \(u=1\) takes \((1+4/3)/(\sqrt2\alpha^2)=35/(6\sqrt2)\).

For a positive scalar vector field \(X_2\), separation of variables gives
\(D_z\Phi_2^s(z)=X_2(\Phi_2^s(z))/X_2(z)\). Since
\(X_1(0)/X_2(0)=1/2\), the two parameter derivatives at \(s_*\) are

\[
 \partial_1\Theta(s_*)=\frac\alpha{5\sqrt2},\qquad
 \partial_2\Theta(s_*)=\frac{2\alpha}{5\sqrt2}.
\]

At the terminal point the two feature derivatives are \(\alpha/(2\sqrt2)\) and \(2\alpha/(5\sqrt2)\). Taking their outer product gives exactly

\[
 DG(s_*)=
 \begin{pmatrix}
 1/50&1/25\\
 2/125&4/125
 \end{pmatrix}.                                     \tag{37}
\]

For \(h=(1,-1)\),

\[
 h^\top DG(s_*)h=-\frac1{250}<0,
 \qquad
 \det\frac{DG(s_*)+DG(s_*)^\top}{2}
                     =-\frac9{62500}.                \tag{38}
\]

Thus \(G\) is not monotone: differentiability implies
\(\langle\varepsilon h,G(s_*+\varepsilon h)-G(s_*)\rangle
=-\varepsilon^2/250+o(\varepsilon^2)<0\) for sufficiently small nonzero \(\varepsilon\).

There is also no local two-clock action with \(\partial_j\Psi_s=X_j(\Psi_s)\) near a point where (35) is nonzero. If such an action existed, its mixed partial derivatives, computed using the \(C^1\) fields, would imply
\(DX_2X_1=DX_1X_2\). This contradicts (35). In particular, applying the clocks (16) to the ordered map (36) does not generally represent the physical dynamics (3).

Equations (35)--(38) are an obstruction to extending this proof by dropping (2). They do not give a weak-error counterexample: no slow-loss trajectory or amplification of iid sampling error is asserted for (34).

The precise defect in a general two-field ordered flow can also be written down. Let \(z_1=\Phi_1^{s_1}(z)\), let \(y(u)=\Phi_2^u(z_1)\), and put

\[
 \mathcal C(w)=DX_2(w)X_1(w)-DX_1(w)X_2(w),
 \quad E(u)=D\Phi_2^u(z_1)X_1(z_1)-X_1(y(u)).
\]

The variational equation and the chain rule give

\[
 E'(u)=DX_2(y(u))E(u)+\mathcal C(y(u)),\qquad E(0)=0.
\]

Variation of constants yields, with oriented integration also when \(s_2<0\),

\[
 E(s_2)=\int_0^{s_2}
    D\Phi_2^{s_2-u}(y(u))\mathcal C(y(u))\,du.         \tag{39}
\]

For \(\Theta(s,z)=\Phi_2^{s_2}(\Phi_1^{s_1}(z))\), the two derivatives are therefore \(\partial_1\Theta=X_1(\Theta)+E(s_2)\) and \(\partial_2\Theta=X_2(\Theta)\). Consequently

\[
 D_s[\psi(\Theta(s,z))]
 =D\psi(\Theta)D\psi(\Theta)^\top
       +(D\psi(\Theta)E(s_2))e_1^\top.                \tag{40}
\]

Under \(\|DX_2\|\le M\), \(|\mathcal C|\le K\), and (1), (39) gives

\[
 |E(s_2)|\le K|s_2|e^{M|s_2|},
\]

so the symmetric part of the last term in (40) has operator norm at most \(BK|s_2|e^{M|s_2|}\). This crude estimate reintroduces an exponential in clock length. Moreover, an ordered-clock curve has velocity

\[
 \frac d{dt}\Theta(\tau(t),z)
 =\tau_1'X_1(\Theta)+\tau_2'X_2(\Theta)
                      +\tau_1'E(\tau_2(t)).          \tag{41}
\]

Thus a quantitative extension must control both the Jacobian defect (40) and the physical-velocity defect (41). A bound on the ordered-map Jacobian alone does not restore the representation used in Section 3. For commuting fields, \(\mathcal C=E=0\), recovering the theorem exactly.

## Scope and remaining question

The result proves the finite-rank commuting-gradient extension suggested by the preceding report. It includes a two-input neural-network example with genuinely nonintegrable square-root loss. Exact commutation is a sufficient structural stability hypothesis here. No necessity is asserted, and no implication from loss decay to commutation is claimed.

The full slow-decay question for general noncommuting features remains unresolved. There is no sharp exponent and no output-error counterexample to T224 in this proof. Sphere constraints, unbounded features, trained output coefficients, finite training data and time discretization are outside the theorem. The source's Remark 6 already covers the critical exponent \(c=2\); its Section 6 still asks about slower convergence. The background paper opened for the literature check is Song Mei, Andrea Montanari, and Phan-Minh Nguyen, *A Mean Field View of the Landscape of Two-Layers Neural Networks*, [arXiv:1804.06561](https://arxiv.org/abs/1804.06561). No literature-priority claim is made.
