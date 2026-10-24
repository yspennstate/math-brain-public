# Uniform-in-time logistic GD for Gaussian tanh random features

Author: B02. Date: 2026-10-24. This is new work under `fullproof/`; no frozen file is modified.

**Status.** The coercivity, curvature, MLE, and uniform-in-time delocalization results below are proved directly. They apply when the fixed sample-to-width ratio is sufficiently large and the fixed positive step is sufficiently small. With B04's independently audited total-variation transfer theorem, they give a calibration floor simultaneously at every positive training time, including the MLE and arbitrary data-dependent positive stopping times. A deterministic calibration curve additionally needs the finite-time deterministic overlaps. Section 9 states exactly how such overlaps, once proved, extend uniformly to all times. This note does not silently assume that separate state-evolution theorem.

## 1. Model, constants, and theorem

Let
\[
X_i\stackrel{\mathrm{iid}}\sim N(0,I_d),\qquad
Y_i\mid X_i\sim\operatorname{Bernoulli}(\sigma(\beta\theta^\top X_i)),
\quad \|\theta\|=1,
\]
with conditionally independent labels, fixed finite \(\beta\geq0\), and \(\sigma(u)=(1+e^{-u})^{-1}\). Independently, the rows of \(F\in\mathbb R^{m\times d}\) are \(W_j\sim N(0,I_d/d)\). Put
\[
h(x)=\tanh(Fx),\quad H_{ij}=h_j(X_i),\quad
\mathcal L_n(b)=\frac1n\sum_{i=1}^n
 \big\{\log(1+e^{h(X_i)^\top b})-Y_i h(X_i)^\top b\big\}.
\tag{1.1}
\]
Assume \(n/d\to\alpha>0\), \(m/d\to\gamma>0\). The raw score is \(b^\top h(x)\); in the alternative network notation \(b=a/\sqrt m\). The GD update in the other notes is exactly
\[
b^0=0,\qquad b^{t+1}=b^t-\eta_d\nabla\mathcal L_n(b^t),
\qquad \eta_d=\frac{cd}{m}.
\tag{1.2}
\]

Here are explicit, deliberately conservative constants. For \(G\sim N(0,1)\), define
\[
a_1=\mathbb E[G\tanh G],\quad v=\mathbb E\tanh^2G,
\quad \nu=v-a_1^2>0.
\]
Choose any deterministic \(L\) for which \(\|F\|_{\mathrm{op}}\leq L\) with probability tending to one. The elementary Gaussian net bound permits, for example,
\[
L=8\sqrt{1+\gamma}.
\]
Set
\[
s=\nu/2,\qquad \kappa=\sqrt{s/2},\qquad
p_0=\frac{s^2}{20L^4},\qquad
B=\sqrt{2\log(4/p_0)},
\]
\[
q_\beta=\sigma(-\beta B),\quad
p_1=q_\beta p_0/2,\quad
\mathfrak a=\kappa p_1/4,\quad
C_*=\max\left\{1,\left(\frac{32L}{\kappa p_1}\right)^2\right\}.
\tag{1.3}
\]
The ratio and step assumptions for this note are
\[
\boxed{\quad\alpha/\gamma>C_*,\qquad
0<c<\frac{\gamma}{2\Lambda},\quad
\Lambda=16L^2.\quad}
\tag{1.4}
\]
These define a nonempty proportional regime for each fixed \(\beta,\gamma\). No assertion that these thresholds are sharp is made.

Further set
\[
R_0=\frac{\log2}{\mathfrak a},\quad R=2R_0,
\quad C_H=64L^2,\quad \delta=p_0/4,
\quad M=R\sqrt{C_H/\delta},
\]
\[
\chi=\frac{\kappa^2p_0}{16},\qquad
\mu=\chi\sigma'(M)>0,\qquad
\eta_-=\frac{c}{2\gamma},\qquad q=1-\eta_-\mu\in(0,1).
\tag{1.5}
\]
All these constants are independent of \(d\), although some are very small or very large.

**Theorem 1 (whole GD trajectory).** Under (1.4), with probability tending to one:

1. \(\mathcal L_n(b)\geq\mathfrak a\|b\|\) for every \(b\in\mathbb R^m\). There is a unique finite unregularized MLE \(b^*\), with \(\|b^*\|\leq R_0\).
2. Every GD iterate and every feature-deleted GD iterate defined in Section 6 lies in \(\{\|b\|\leq R_0\}\). On the larger ball \(\{\|b\|\leq R\}\),
   \[
   \mu I\preceq\nabla^2\mathcal L_n(b)\preceq\Lambda I.
   \tag{1.6}
   \]
3. For every integer \(t\geq0\), simultaneously,
   \[
   \|b^t-b^*\|\leq R_0q^t.
   \tag{1.7}
   \]
4. The MLE and the whole trajectory are delocalized:
   \[
   \|b^*\|_\infty+\sup_{t\geq0}\|b^t\|_\infty
      =O_P\!\left(\sqrt{\frac{\log d}{d}}\right).
   \tag{1.8}
   \]
5. For a deterministic \(r_*>0\),
   \[
   \inf_{t\geq1}\|b^t\|\geq r_*,\qquad \|b^*\|\geq r_*
   \tag{1.9}
   \]
   with probability tending to one. One permissible choice is
   \[
   r_* =\frac c4\sqrt{\frac{v\rho_\beta}{\alpha\gamma}},
   \qquad \rho_\beta=\mathbb E\sigma'(\beta G)>0.
   \tag{1.10}
   \]

The label mechanism is not independent of the feature vector after conditioning on \(F\). The proof below does not make that assumption.

## 2. The good feature event

Write \(\Sigma_F=\mathbb E_X h(X)h(X)^\top\) and
\(g_F=\mathbb E_X[(\theta^\top X)h(X)]\). There is an event \(\mathcal F_d\), depending only on \(F\), on which
\[
\|F\|_{\mathrm{op}}\leq L,\qquad
\Sigma_F\succeq sI,\qquad
\Sigma_F-g_Fg_F^\top\succeq sI,
\tag{2.1}
\]
with \(\mathbb P(\mathcal F_d^c)=O(d^{-1})+O(de^{-c_Fd})\) for some fixed \(c_F>0\). Constants in probability estimates may depend on fixed model parameters.

For completeness, the covariance claim follows directly from Hermite expansion. Put \(q_j=\|W_j\|^2\),
\(A(q)=\mathbb E\tanh'(\sqrt qG)\), and \(D_A=\operatorname{diag}(A(q_j))\). Oddness gives only odd Hermite coefficients, and Gaussian integration by parts identifies the linear coefficient. Thus
\[
\Sigma_F=D_AFF^\top D_A+D_\nu+E,
\quad (D_\nu)_{jj}=\mathbb E\tanh^2(\sqrt{q_j}G)-q_jA(q_j)^2,
\tag{2.2}
\]
where \(E_{jj}=0\) and, for \(j\ne k\),
\[
|E_{jk}|\leq |\rho_{jk}|^3,\qquad
\rho_{jk}=\frac{W_j^\top W_k}{\|W_j\|\|W_k\|}.
\tag{2.3}
\]
Indeed, Cauchy--Schwarz on the Hermite coefficients of degree at least three bounds their sum by \(|\rho_{jk}|^3\), since tanh has second moment at most one. Independent Gaussian directions give
\[
\mathbb E\|E\|_F^2\leq
\frac{15m(m-1)}{d(d+2)(d+4)}=O(d^{-1}).
\tag{2.4}
\]
Uniform concentration of \(q_j\) around one and continuity give \(\min_j(D_\nu)_{jj}\geq3\nu/4\) except on an exponentially unlikely event. Markov's inequality gives \(\|E\|_{\mathrm{op}}\leq\nu/4\) with failure \(O(d^{-1})\). Also
\[
g_F=D_AF\theta,
\quad
\Sigma_F-g_Fg_F^\top
=D_AF(I-\theta\theta^\top)F^\top D_A+D_\nu+E\succeq sI.
\tag{2.5}
\]
The operator norm bound follows by a Gaussian sphere-net argument. These observations prove (2.1).

Conditional on \(F\in\mathcal F_d\), for every unit \(u\in\mathbb R^m\), the function \(x\mapsto u^\top h(x)\) is odd and \(L\)-Lipschitz. In particular,
\[
\mathbb E e^{t u^\top h(X)}\leq e^{t^2L^2/2},\qquad
s\leq\mathbb E(u^\top h(X))^2\leq L^2,
\quad
\mathbb E(u^\top h(X))^4\leq5L^4.
\tag{2.6}
\]
The fourth-moment bound follows from Gaussian Poincare applied first to the centered function and then to its square:
\(\mathbb E f^4\leq(\mathbb E f^2)^2+4L^2\mathbb E f^2\leq5L^4\).

## 3. Uniform small-ball events and noisy-label coercivity

Everything in this section is conditional on a fixed \(F\in\mathcal F_d\). The pairs \((X_i,Y_i)\) are iid under this conditioning. For each unit \(u\), Paley--Zygmund, or Cauchy--Schwarz applied above the threshold, gives
\[
\mathbb P(|u^\top h(X)|\geq\kappa)\geq p_0.
\tag{3.1}
\]
Let \(Z=\theta^\top X\) and \(T=2Y-1\). The chosen \(B\) has \(\mathbb P(|Z|>B)\leq p_0/2\). On \(|Z|\leq B\), either label has conditional probability at least \(q_\beta\). Therefore
\[
\mathbb P(-T u^\top h(X)\geq\kappa)
\geq q_\beta\mathbb P(|u^\top h(X)|\geq\kappa,|Z|\leq B)
\geq p_1.
\tag{3.2}
\]
This is a conditional-label calculation at each \(X\); it never separates the dependent events involving \(h(X)\) and \(Z\).

Define the bounded cutoff
\[
\psi(x)=
\begin{cases}
0,&x\leq\kappa/2,\\
2x/\kappa-1,&\kappa/2<x<\kappa,\\
1,&x\geq\kappa.
\end{cases}
\tag{3.3}
\]
It is \(2/\kappa\)-Lipschitz and vanishes at zero. For either class
\[
f_u(X,Y)=\psi(-T u^\top h(X)),\qquad
\widetilde f_u(X)=\psi(|u^\top h(X)|),\quad \|u\|=1,
\]
symmetrization and Rademacher contraction give
\[
\mathbb E\sup_{\|u\|=1}|(P_n-P)f_u|
\leq\frac{8}{\kappa}
 \mathbb E\left\|\frac1n\sum_i\epsilon_iT_i h(X_i)\right\|
\leq\frac{8L}{\kappa}\sqrt{\frac mn}.
\tag{3.4}
\]
The same bound holds for \(\widetilde f_u\), with \(T_i\) omitted. The numerical factor eight safely includes the absolute-value form of contraction. The last inequality uses \(T_i^2=1\) and the independent Rademacher signs, not independence of \(T_i\) and \(h(X_i)\).

Since changing one sample changes each supremum by at most \(1/n\), bounded differences imply an upper-tail bound \(e^{-2nz^2}\) above its expectation. If \(n/m\geq C_*\), (3.4) is at most \(p_1/4\). Using \(z=p_1/4\) for the signed class and \(z=p_0/4\) for the unsigned class proves, simultaneously, except with probability
\[
e^{-np_1^2/8}+e^{-np_0^2/8},
\tag{3.5}
\]
that for every unit \(u\),
\[
\frac1n\sum_i\psi(-T_i u^\top h_i)\geq p_1/2,
\qquad
\frac1n\#\{i:|u^\top h_i|>\kappa/2\}\geq p_0/2.
\tag{3.6}
\]
Measurability of the suprema is unproblematic: the cutoff classes are continuous in \(u\), so a countable dense subset of the sphere suffices.

The logistic loss obeys \(\log(1+e^{-Tz})\geq(-Tz)_+\). Also \(x_+\geq(\kappa/2)\psi(x)\). Consequently, for every \(b\ne0\), using \(u=b/\|b\|\),
\[
\mathcal L_n(b)
\geq\|b\|\frac1n\sum_i(-T_i u^\top h_i)_+
\geq\frac{\kappa p_1}{4}\|b\|
=\mathfrak a\|b\|.
\tag{3.7}
\]
The inequality at \(b=0\) is immediate. Thus the entire initial sublevel set \(\{\mathcal L_n\leq\log2\}\) is contained in the deterministic radius-\(R_0\) ball.

## 4. Robust covariance and curvature on the whole ball

The unsigned event in (3.6) gives an arbitrary-deletion bound: for **every** subset \(I\subseteq\{1,\ldots,n\}\) with \(|I^c|\leq\delta n\),
\[
\frac1n\sum_{i\in I}h_i h_i^\top\succeq\chi I_m.
\tag{4.1}
\]
Indeed, for each unit \(u\), at least \(p_0n/2\) rows have \(|u^\top h_i|>\kappa/2\); after arbitrary deletion of at most \(p_0n/4\) rows, at least \(p_0n/4\) remain, contributing at least \(\kappa^2p_0/16\). This proof does not union-bound over subsets and does not assume deleted rows are independent of the data.

We also have, with conditional failure at most \(2e^{-3n}\) when \(n\geq m\),
\[
\|H\|_{\mathrm{op}}\leq8L\sqrt n,
\qquad \frac1nH^\top H\preceq C_H I_m.
\tag{4.2}
\]
For a direct proof, take \(1/4\)-nets of the two unit spheres, of cardinalities at most \(9^n,9^m\). Each bilinear form \(u^\top Hv\) is centered \(L\)-subGaussian by independence of the rows and (2.6). The bound at \(4L\sqrt n\), a union bound, and the factor-two net inequality give failure
\(2\exp\{(n+m)\log9-8n\}\leq2e^{-3n}\). This uses no within-row independence.

For any \(\|b\|\leq R\), let \(I_b=\{i:|h_i^\top b|\leq M\}\). Equation (4.2) gives
\[
\frac{|I_b^c|}{n}\leq\frac{b^\top H^\top Hb}{nM^2}
\leq\frac{C_HR^2}{M^2}=\delta.
\]
The logistic Hessian is therefore bounded simultaneously on the ball by
\[
\nabla^2\mathcal L_n(b)
=\frac1n\sum_i\sigma'(h_i^\top b)h_ih_i^\top
\succeq\sigma'(M)\frac1n\sum_{i\in I_b}h_ih_i^\top
\succeq\mu I_m.
\tag{4.3}
\]
Globally, \(\nabla^2\mathcal L_n(b)\preceq C_HI/4=\Lambda I\). Thus the desired curvature is simultaneous for all points in the ball, not merely at a prespecified iterate.

Let \(\mathcal G_d\) be the feature event together with (3.6) and (4.2). For large \(d\), (1.4) gives \(n/m\geq C_*\), and
\[
\mathbb P(\mathcal G_d^c)
\leq\mathbb P(\mathcal F_d^c)
 +e^{-np_1^2/8}+e^{-np_0^2/8}+2e^{-3n}=o(1).
\tag{4.4}
\]

## 5. MLE existence and uniform contraction

On \(\mathcal G_d\), coercivity and continuity give a finite global minimizer. Its loss is at most \(\mathcal L_n(0)=\log2\), so its norm is at most \(R_0\). Strict convexity on the containing ball proves uniqueness; call the minimizer \(b^*\). Its full gradient is zero.

For probabilistic expressions involving the MLE, assign \(b^*=0\) on any exceptional realization without a unique finite MLE. This arbitrary extension has vanishing probability and does not change any conclusion.

For large \(d\), the step assumption implies
\[
\eta_-\leq\eta_d\leq2c/\gamma<1/\Lambda.
\tag{5.1}
\]
The global smoothness inequality gives
\[
\mathcal L_n(b-\eta_d\nabla\mathcal L_n(b))
\leq\mathcal L_n(b)-\frac{\eta_d}{2}\|\nabla\mathcal L_n(b)\|^2.
\tag{5.2}
\]
Thus all iterates remain in the initial sublevel set, and hence in the radius-\(R_0\) ball.

For \(x,y\) in this ball, integrate the Hessian along their line segment. It yields a symmetric matrix \(A_{x,y}\) with spectrum in \([\mu,\Lambda]\) such that
\[
[x-\eta_d\nabla\mathcal L_n(x)]-[y-\eta_d\nabla\mathcal L_n(y)]
=(I-\eta_dA_{x,y})(x-y).
\]
Consequently the GD map contracts by
\[
q_d=1-\eta_d\mu\leq q<1.
\tag{5.3}
\]
Applying this with \(y=b^*\) proves (1.7), uniformly for every integer time. No dimension-dependent burn-in is hidden in the contraction factor.

## 6. Leave-one-feature definitions and concentration

Let \(P_j\) set coordinate \(j\) to zero. Define restricted GD for every data realization, including outside \(\mathcal G_d\), by
\[
b^{-j,0}=0,\qquad
b^{-j,t+1}=b^{-j,t}-\eta_d P_j\nabla\mathcal L_n(b^{-j,t}).
\tag{6.1}
\]
The coordinate \(j\) stays zero, so this update uses only \(X,Y,F_{-j}\). On \(\mathcal G_d\), the same descent inequality applied on the coordinate subspace shows that every restricted iterate has loss at most \(\log2\) and norm at most \(R_0\). Therefore the same full Hessian bounds apply simultaneously along the full and all restricted trajectories.

Also define \(\bar b^{-j}\), for every data realization, to minimize \(\mathcal L_n\) over the deterministic compact set
\[
\{b:b_j=0,\ \|b\|\leq R\}.
\tag{6.2}
\]
If needed, select the unique minimum-norm minimizer. This is a measurable selector: it is the limit as \(\epsilon\downarrow0\) of the unique minimizers after adding \(\epsilon\|b\|^2\). The definition uses only \(X,Y,F_{-j}\). On \(\mathcal G_d\), its loss is at most \(\log2\), so \(\|\bar b^{-j}\|\leq R_0<R\). It is then an unconstrained minimizer in its coordinate subspace, and
\[
\nabla\mathcal L_n(\bar b^{-j})=g_j^*e_j.
\tag{6.3}
\]
The larger compact ball in the definition is essential: it keeps the object well defined and independent of \(W_j\) even on exceptional samples, while still giving interior stationarity on the good event.

For any of these restricted coefficient vectors \(b\), put
\[
g_j(b)=\frac1n\sum_i
 [\sigma(h_{i,-j}^\top b_{-j})-Y_i]\tanh(W_j^\top X_i).
\tag{6.4}
\]
Conditional on \(X,Y,F_{-j}\), the bracketed residual vector is fixed, has norm at most \(\sqrt n\), and is independent of \(W_j=G_j/\sqrt d\). As a function of standard Gaussian \(G_j\), (6.4) is odd, has mean zero, and has Lipschitz constant at most
\[
\frac{\|X\|_{\mathrm{op}}}{\sqrt{nd}}.
\tag{6.5}
\]
Hence
\[
\mathbb P(|g_j(b)|>u\mid X,Y,F_{-j})
\leq2\exp\!\left(-\frac{ndu^2}{2\|X\|_{\mathrm{op}}^2}\right).
\tag{6.6}
\]
This conditioning is valid for the compact restricted minimizer and for every deterministic restricted-GD time. Conditioning instead on a good event involving \(W_j\) before applying concentration would not be valid; we do not do so.

Choose a deterministic \(B_X\) with \(\mathbb P(\|X\|_{\mathrm{op}}>B_X\sqrt d)\leq e^{-c_Xd}\) for large \(d\); the same net proof permits \(B_X=8\sqrt{1+\alpha}\). For \(d\geq3\), define
\[
T_d=1+\left\lceil\frac{\max\{0,\log(R_0d)\}}{-\log q}\right\rceil,
\qquad
\tau_d=B_X\sqrt{\frac{8\log d}{n}}.
\tag{6.7}
\]
In particular \(T_d=O(\log d)\) with a dimension-independent implied constant. Applying (6.6) and a union bound over \(j\leq m\), \(0\leq t<T_d\), and the restricted minimizers gives
\[
\max_{j,t<T_d}|g_j(b^{-j,t})|\leq\tau_d,
\qquad \max_j|g_j^*|\leq\tau_d
\tag{6.8}
\]
except with probability at most
\[
e^{-c_Xd}+2m(T_d+1)d^{-4}=o(1).
\tag{6.9}
\]
No independence between different leave-one-feature problems or different times is asserted or required.

## 7. Uniform coefficient delocalization

First compare the full and restricted MLEs on the intersection of \(\mathcal G_d\) and (6.8). Strong monotonicity along their segment gives
\[
\mu\|\bar b^{-j}-b^*\|^2
\leq\langle\nabla\mathcal L_n(\bar b^{-j})-
 \nabla\mathcal L_n(b^*),\bar b^{-j}-b^*\rangle
=-g_j^*b_j^*.
\]
Cauchy--Schwarz implies
\[
|b_j^*|\leq\|\bar b^{-j}-b^*\|\leq|g_j^*|/\mu,
\quad\text{hence}\quad \|b^*\|_\infty\leq\tau_d/\mu.
\tag{7.1}
\]

For the trajectories, let \(G_d(b)=b-\eta_d\nabla\mathcal L_n(b)\). Equation (6.1) says
\[
b^{-j,t+1}=G_d(b^{-j,t})+\eta_dg_j(b^{-j,t})e_j.
\]
The contraction established on the common ball gives
\[
\|b^{t+1}-b^{-j,t+1}\|
\leq q_d\|b^t-b^{-j,t}\|+\eta_d|g_j(b^{-j,t})|.
\tag{7.2}
\]
Starting from zero and using \(1-q_d=\eta_d\mu\), (6.8) implies
\[
\max_{j,\ 0\leq t\leq T_d}\|b^t-b^{-j,t}\|
\leq\frac{\eta_d\tau_d}{1-q_d}=\frac{\tau_d}{\mu}.
\tag{7.3}
\]
Since the restricted coordinate is zero, this bounds every \(|b_j^t|\) through time \(T_d\). For every \(t\geq T_d\), (1.7) and the definition of \(T_d\) give
\[
\|b^t\|_\infty\leq\|b^*\|_\infty+R_0q^{T_d}
\leq\tau_d/\mu+d^{-1}.
\tag{7.4}
\]
Thus on this single event,
\[
\boxed{\quad\sup_{t\geq0}\|b^t\|_\infty
\leq\tau_d/\mu+d^{-1},\qquad \|b^*\|_\infty\leq\tau_d/\mu.\quad}
\tag{7.5}
\]
Together with (4.4) and (6.9), this proves (1.8) with an explicit failure bound. The proof handles infinitely many GD times by deterministic contraction after a logarithmic horizon; it does not union-bound infinitely many concentration events.

## 8. Positive norms and simultaneous calibration floor

The lower-norm result is the argument in B03 Proposition 3; it is included here to make its use explicit. Put \(K=HH^\top/m\), \(\lambda_d=cd/n\), and \(R_Y=Y-1/2\). Then
\[
\|b^1\|^2=\frac{\lambda_d^2}{m}R_Y^\top K R_Y.
\tag{8.1}
\]
Conditional on \(X,F\), decompose \(R_Y=\bar r+\epsilon\), with independent centered bounded \(\epsilon_i\), and
\(D_{ii}=\mathbb E(\epsilon_i^2\mid X,F)=\sigma'(\beta Z_i)\). A quadratic-form expansion gives
\[
\operatorname{Var}(R_Y^\top KR_Y\mid X,F)
\leq C\{\operatorname{tr}K^2+\|K\bar r\|^2\}
\leq Cn\|K\|_{\mathrm{op}}^2.
\tag{8.2}
\]
The norm \(\|K\|\) is bounded in probability, so the normalization in (8.1) makes its centered fluctuation \(o_P(1)\). The contribution \(\bar r^\top K\bar r\) is nonnegative. Conditional on \(F\), the bounded iid row variables \(D_{ii}K_{ii}\) have expectation tending to \(v\rho_\beta\): uniformly over features, \(\|W_j\|^2\to1\) and \(\theta^\top W_j\to0\), and the relevant bounded bivariate Gaussian expectation is continuous. Hence
\[
\frac1n\operatorname{tr}(KD)\to v\rho_\beta,
\qquad
\|b^1\|^2\geq\frac{c^2v\rho_\beta}{\alpha\gamma}+o_P(1).
\tag{8.3}
\]

Let \(g_0=\nabla\mathcal L_n(0)\). Descent and convexity respectively give, for every \(t\geq1\),
\[
\mathcal L_n(b^t)\leq\log2-\frac{\eta_d}{2}\|g_0\|^2,
\qquad
\mathcal L_n(b^t)\geq\log2+g_0^\top b^t.
\]
Therefore \(\|b^t\|\geq\eta_d\|g_0\|/2=\|b^1\|/2\), simultaneously at all positive times. Letting \(t\to\infty\) gives the same bound for \(b^*\). Equation (8.3) proves (1.9)--(1.10).

For a fresh test pair, condition on the complete training environment \(\mathcal E_d=(F,X_{1:n},Y_{1:n})\). Let \(S_{t,d}=h(X)^\top b^t\) and
\[
A_{t,d}=\mathbb E_X[ZS_{t,d}\mid\mathcal E_d]=g_F^\top b^t,
\qquad
Q_{t,d}=\mathbb E_X[S_{t,d}^2\mid\mathcal E_d]=(b^t)^\top\Sigma_Fb^t.
\tag{8.4}
\]
Use \(t=\infty\) for \(b^*\). Equations (2.1), (1.9), and Poincare yield, simultaneously for all \(t\in\{1,2,\ldots,\infty\}\),
\[
Q_{t,d}-A_{t,d}^2\geq s r_*^2=:\Delta_*>0,
\qquad Q_{t,d}\leq L^2R_0^2=:Q_*.
\tag{8.5}
\]
The readout derivative bounds are uniform in time:
\[
\|\nabla S_t\|\leq LR_0,\quad
\|\nabla^2S_t\|_{\mathrm{HS}}\leq2L^2R_0,\quad
\|\nabla^2S_t\|_{\mathrm{op}}
\leq2L^2\sup_u\|b^u\|_\infty=o_P(1).
\tag{8.6}
\]
The proof of B04 Theorem 2.1 is sequentially uniform over classes with fixed bounds in (8.5)--(8.6). Otherwise a deterministic sequence violating uniformity would contradict that theorem. Consequently its random-environment argument gives
\[
\sup_{t\in\{1,2,\ldots,\infty\}}
\left\|\mathcal L((Z,S_{t,d})\mid\mathcal E_d)
-N\!\left(0,\begin{pmatrix}1&A_{t,d}\\A_{t,d}&Q_{t,d}\end{pmatrix}\right)
\right\|_{\mathrm{TV}}\longrightarrow0
\quad\text{in probability}.
\tag{8.7}
\]
This argument does not require deterministic overlap limits or a union bound over time.

For \(Q>A^2\), define the explicit Gaussian calibration functional
\[
\mathcal C_\beta(A,Q)
=\mathbb E_{U}\left|
\mathbb E_V\sigma\!\left(\beta\frac{A}{\sqrt Q}U
+\beta\sqrt{1-\frac{A^2}{Q}}V\right)
-\sigma(\sqrt Q U)\right|,
\qquad U,V\stackrel{\mathrm{iid}}\sim N(0,1).
\tag{8.8}
\]
Let \(\mathrm{CE}_{t,d}\) be exact, unbinned population calibration error of the predictor \(\sigma(S_{t,d})\), conditional on \(\mathcal E_d\). Since sigmoid is injective, conditioning on its probability is equivalent to conditioning on the score. B04's signed-measure argument makes this calibration error TV-Lipschitz. Applying the common label kernel \(Y\mid Z\) and (8.7),
\[
\sup_{t\in\{1,2,\ldots,\infty\}}
|\mathrm{CE}_{t,d}-\mathcal C_\beta(A_{t,d},Q_{t,d})|
\longrightarrow0
\quad\text{in probability}.
\tag{8.9}
\]

For clarity, strict positivity of (8.8) holds for every \(Q-A^2>0\). If \(\beta=0\), the true curve is the constant \(1/2\) and the nonconstant prediction has positive error. If \(\beta>0,A\leq0\), the Gaussian conditional probability is nonincreasing while sigmoid is strictly increasing. If \(\beta>0,A>0\), write its conditional curve as
\(g(s)=\mathbb E\sigma(ks+\tau V)\), with
\(k=\beta A/Q>0\) and \(\tau=\beta\sqrt{1-A^2/Q}>0\). Dominated convergence gives
\[
\lim_{s\to\infty}e^{ks}(1-g(s))=e^{\tau^2/2}.
\]
Equality with \(\sigma(s)\) for every \(s\) would force first \(k=1\) and then \(e^{\tau^2/2}=1\), a contradiction. Equality almost everywhere would imply equality everywhere by continuity. Thus the error is strictly positive.

The parameter set
\[
\mathcal K=\{(A,Q): Q\leq Q_*,\ Q-A^2\geq\Delta_*\}
\tag{8.10}
\]
is compact. Formula (8.8) is continuous on it by dominated convergence. Therefore
\[
\varepsilon_*:=\min_{(A,Q)\in\mathcal K}\mathcal C_\beta(A,Q)>0.
\tag{8.11}
\]
Equations (8.5) and (8.9) prove the simultaneous statement
\[
\mathbb P\!\left(
\inf_{t\in\{1,2,\ldots,\infty\}}\mathrm{CE}_{t,d}
\geq\varepsilon_*/2\right)\longrightarrow1.
\tag{8.12}
\]
In particular, **no training-measurable stopping rule taking a positive integer time, even one diverging with dimension, attains asymptotic calibration in this fixed-step regime.** The same holds if the rule may output the MLE. At time zero the constant predictor \(1/2\) is calibrated, since the symmetric teacher has marginal class probability \(1/2\). The theorem does not cover steps \(c=c_d\to0\), which alter the stated regime.

Positive absolute calibration error does not alone assert that every confidence level is overconfident. The full curve in (8.8), or its conditional form \(g(s)\), determines the direction. Early positive iterates can be underconfident while still having strictly positive exact calibration error.

## 9. Promotion of deterministic finite-time overlaps to all times

This section is a conditional consequence with a clearly identified remaining input. Suppose a separate finite-time state-evolution theorem proves, for every fixed integer \(t\geq1\), deterministic limits
\[
A_{t,d}\xrightarrow{P}A_t(\alpha,\gamma,c,\beta),\qquad
Q_{t,d}\xrightarrow{P}Q_t(\alpha,\gamma,c,\beta).
\tag{9.1}
\]
Then these limits extend to \(t=\infty\), and convergence is uniform over all positive integer times and the MLE:
\[
\sup_{t\in\{1,2,\ldots,\infty\}}
\big\{|A_{t,d}-A_t|+|Q_{t,d}-Q_t|\big\}\xrightarrow{P}0.
\tag{9.2}
\]

Here is the proof, including the exchange of limits. The population norm bounds are \(\|g_F\|\leq L\) and \(\|\Sigma_F\|\leq L^2\). From (1.7), for every \(t\geq T\), including infinity,
\[
\|b^t-b^T\|\leq2R_0q^T,
\]
\[
|A_{t,d}-A_{T,d}|\leq2LR_0q^T,
\qquad
|Q_{t,d}-Q_{T,d}|\leq4L^2R_0^2q^T.
\tag{9.3}
\]
For each fixed \(t,T\), take probability limits in these deterministic inequalities on events of probability tending to one. This gives the same bound between \((A_t,Q_t)\) and \((A_T,Q_T)\). Therefore the deterministic sequence is exponentially Cauchy and has a limit \((A_\infty,Q_\infty)\). For arbitrary fixed \(T\), split the supremum in (9.2) into the finite times below \(T\) and the common exponential tail. Equation (9.1) controls the finite part, while (9.3) controls both tails. Let \(d\to\infty\), then \(T\to\infty\). This proves (9.2) without interchanging unproved limits.

Combining uniform continuity on (8.10), (8.9), and (9.2) gives the deterministic whole-trajectory theorem
\[
\boxed{\quad
\sup_{t\in\{1,2,\ldots,\infty\}}
\left|\mathrm{CE}_{t,d}
-\mathcal C_\beta\big(A_t(\alpha,\gamma,c,\beta),
Q_t(\alpha,\gamma,c,\beta)\big)\right|
\xrightarrow{P}0.\quad}
\tag{9.4}
\]
For a data-dependent positive stopping rule \(\tau_d\), the same uniform estimate holds after substituting \(t=\tau_d\). If \(\tau_d\to\infty\) in probability, then \(\mathrm{CE}_{\tau_d,d}\to\mathcal C_\beta(A_\infty,Q_\infty)>0\) in probability. If the stopping time has no limiting value, the deterministic curve still approximates its realized index and the common positive floor still applies.

The imported input (9.1) is what makes (9.4) a calibration function of the aspect ratios and training time. Equations (8.7)--(8.12) themselves do not require that input and are already unconditional consequences of the proofs above and B04's analytic transfer theorem.

## 10. Scope and dependencies

- The general proportional regime of this note is an explicit open set: arbitrary fixed finite \(\beta\), arbitrary fixed width ratio \(\gamma>0\), sufficiently large fixed \(\alpha/\gamma\), and sufficiently small fixed positive \(c\). The proof neither covers separable small-sample regimes nor claims a sharp sample-to-width threshold.
- The feature covariance and empirical coercivity/curvature arguments are proved here. They account for teacher-feature dependence and adaptive row deletion.
- Leave-one-feature objects are defined independently of the omitted feature even on exceptional samples. The common curvature event holds for both full and restricted trajectories because both stay in the same initial sublevel ball.
- The time-uniform probabilistic claim uses concentration only through a deterministic \(O(\log d)\) horizon and a dimension-independent geometric tail afterward.
- The only analytic calibration input is `fullproof/b04_calibration_transfer.md`, Theorem 2.1 and its signed-measure CE continuity argument, independently audited in `fullproof/b02_gaussian_calibration_audit.md`.
- A deterministic state-evolution theorem is an explicit additional hypothesis only in Section 9. This note supplies the rigorous uniform-time extension once that theorem is certified.
