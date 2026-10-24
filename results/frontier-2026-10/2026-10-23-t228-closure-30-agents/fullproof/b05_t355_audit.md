# T355: a quantitative slow-manifold theorem and independent audit

Date: 2026-10-24. Author: B05, with the exponential exit argument supplied by the root worker and independently checked here.

**Status.** The theorem below has a complete proof for its explicit class. It gives a raw-observable weak error of order \(\sqrt\eta\), uniformly over \(T/\eta^2\) updates, when initialized on the minimizer manifold. It also gives a projected-observable bound from an attracting tube and the necessary raw-observable boundary layer. **This is not a new closure of the original row:** positive quantitative slow-SDE rates already appear in Gu–Lyu–Huang–Arora (ICLR 2023). The displayed exponent improves their displayed \(\widetilde O(\eta^{1/4})\) bound on the overlap of the hypotheses; publication novelty of this improvement is not certified.

## 1. Primary-source audit

| Primary source | Checked conclusion and boundary |
|---|---|
| [Li–Wang–Arora, 2110.06914v4](https://arxiv.org/html/2110.06914v4), Assumptions 3.1–3.2, Theorem 4.6, Lemma B.1 | Establishes the slow manifold diffusion limit on the update scale \(\eta^{-2}\). Its main theorem gives convergence in distribution, not an explicit positive-power weak error. |
| [Gu–Lyu–Huang–Arora, 2303.01215v2](https://arxiv.org/html/2303.01215v2), Assumptions 3.1–3.3, Theorem 3.2, Appendix F Theorem F.1 | Uses smooth loss and covariance square root, bounded stochastic gradients, and a compact smooth constant-rank minimizer manifold. F.1 directly gives a projected SGD weak error \(\widetilde O(\eta^{1/4})\) at every update through \(T/\eta^2\), after setting its scaling factor to one. The paper explicitly identifies the single-worker specialization as a quantitative SGD result. |
| [Shalova–Schlichting–Peletier, JMLR 27(146), 2026](https://www.jmlr.org/papers/volume27/24-0571/24-0571.pdf), Theorems 23 and 29 | Gives broad singular-limit convergence results. Its “rate” terminology often describes time rescaling, not an approximation-error exponent. No matching explicit weak-error rate was found in the checked main statements. |
| [Gess–Kassing–Rana, 2402.03467v2](https://arxiv.org/html/2402.03467v2), Theorems 1.1–1.2 and 5.1 | Gives quantitative approximation for an algorithm already constrained to a manifold, on its ordinary \(T/\eta\) update horizon. This is not directly the ambient SGD slow-normal-relaxation theorem below. |

The Gu et al. normal-distance estimates provide the usual bridge from projected to raw observables for starts already near the manifold. They must not be omitted when comparing theorem statements. A logarithmically modified positive-power bound already answers the row's basic positive-exponent request on a stated smooth compact class; the explicit constants and sharper exponent below are a refinement.

## 2. Precisely stated class

Let \(M\subset\mathbb R^d\) be a compact embedded \(C^6\) manifold without boundary. Write

\[
U_s=\{x:\operatorname{dist}(x,M)<s\},\qquad
V(x)=\operatorname{dist}(x,M)^2.
\]

Choose \(r>0\) such that \(V\) is smooth enough to have a bounded Hessian on \(U_{3r}\). Assume:

1. \(L\) is smooth on \(U_{3r}\), \(g=\nabla L\) vanishes on \(M\), and there is \(\lambda>0\) with
   \[
   \nabla V(x)\cdot g(x)\ge2\lambda V(x)\quad(x\in U_{2r}).
   \tag{A1}
   \]
2. The gradient-flow limit map \(\Phi:U_{3r}\to M\) is \(C^6\), \(\Phi|_M=\mathrm{id}\), and
   \[
   D\Phi(x)g(x)=0.
   \tag{A2}
   \]
3. SGD is well defined in \(\mathbb R^d\) and has updates
   \[
   \theta_{n+1}=\theta_n-\eta\bigl(g(\theta_n)+\xi_{n+1}\bigr).
   \tag{A3}
   \]
   With respect to its past filtration, whenever \(\theta_n\in U_{2r}\),
   \[
   \mathbb E_n\xi_{n+1}=0,\quad
   \mathbb E_n[\xi_{n+1}\xi_{n+1}^{\top}]=\Sigma(\theta_n),\quad
   \|\xi_{n+1}\|\le B.
   \tag{A4}
   \]
   A finite-column factor \(\sigma\in C^4(U_{3r};\mathbb R^{d\times q})\) is specified with \(\Sigma=\sigma\sigma^\top\). No differentiability of the conditional noise law beyond this covariance assumption is used.

The \(C^6\) requirement on \(\Phi\) and a smooth factor \(\sigma\), rather than covariance regularity alone, explicitly supplies the regularity needed below. The preliminary proposal with only \(\Phi\in C^4\) and \(\Sigma\in C^3\) did not by itself justify the required \(C^4\) semigroup bound in a possibly degenerate diffusion.

These are geometric and local noise conditions, not a nonexit assumption. Nonexit is proved quantitatively. They include a substantial explicit class: any compact smooth embedded \(M\), the local loss \(L=\tfrac12\operatorname{dist}(\cdot,M)^2\), its nearest-point retraction \(\Phi\), and any noise satisfying (A4) with a smooth factor. More general normally attracting losses satisfy the same conditions when their asymptotic-phase map has the stated regularity.

To connect (A1) to the usual Hessian condition, suppose \(H(p)=\nabla^2L(p)\) has kernel \(T_pM\), its normal eigenvalues are at least \(\mu>0\), and \(\|D H\|\le L_3\) in the tube. With \(p\) the nearest point and \(n=x-p\),

\[
g(x)=H(p)n+R(x),\quad\|R(x)\|\le\tfrac12L_3\|n\|^2,
\]
\[
\nabla V(x)\cdot g(x)
\ge2\mu V(x)-L_3 V(x)^{3/2}.
\]

Shrinking the tube gives (A1), for example with \(\lambda=\mu/2\). It also proves convergence of the gradient flow: \(V\) decays exponentially and \(\|g(x)\|\le G_1\sqrt{V(x)}\), so its remaining path length is integrable. Condition (A2)'s higher differentiability is an explicit additional structural hypothesis; no unsupported high-order phase regularity theorem is silently invoked.

## 3. Extensions, norms, and constants

Choose a smooth cutoff equal to one on \(U_{3r/2}\) and supported in \(U_{2r}\). It gives global bounded-derivative extensions \(\bar\Phi\in C_b^6\) and \(\bar\sigma\in C_b^4\), agreeing with the original maps on \(U_{3r/2}\); \(\bar\Phi\) can be constant outside \(U_{2r}\). It need not be a retraction there. Put \(\bar\Sigma=\bar\sigma\bar\sigma^\top\).

All tensor norms below are Euclidean Hilbert–Schmidt norms; using them makes tensor contractions and compositions bounded by products of norms. Define

\[
\begin{gathered}
G=\sup_{U_{2r}}\|g\|,\quad D_0=G+B,\quad
H_V=\sup_{U_{2r}}\|D^2V\|,\quad C_V=\tfrac12H_VD_0^2,\\
G_1=\sup_{U_{2r}}\|Dg\|,\quad
P=\max\bigl(1,\max_{1\le j\le4}\|D^j\bar\Phi\|_\infty\bigr),\\
C_d=1+P,\quad C_\Phi=15P^4,\quad
S_0=\|\bar\Sigma\|_\infty,\quad S_1=\|D\bar\Sigma\|_\infty,\\
C_N=\frac{C_\Phi}{2}\bigl((S_0+S_1)C_d+G_1^2r\bigr),\qquad
C_R=\frac{C_\Phi D_0^3}{6}.
\end{gathered}
\tag{6}
\]

Define globally extended SDE coefficients

\[
a(x)=D\bar\Phi(x)\bar\sigma(x),\qquad
b(x)=\tfrac12D^2\bar\Phi(x):\bar\Sigma(x),
\tag{7}
\]

and

\[
K=\max\left(1,\max_{0\le j\le4}\|D^jb\|_\infty,
\max_{0\le j\le4}\sup_x\left(\sum_{\ell=1}^q\|D^ja_\ell(x)\|^2\right)^{1/2}\right).
\]
\[
\mathcal M(T)=15(1+d^4)\exp\bigl(26000(1+K)^2T\bigr).
\tag{8}
\]

These constants are deliberately loose but explicit in fixed local geometric and noise norms and the chosen cutoff. Set

\[
\eta_0=\min\left(1,\frac1{2\lambda},\frac r{2D_0}\right),
\tag{9}
\]

with the last term interpreted as infinity if \(D_0=0\). Take \(0<\eta\le\eta_0\), deterministic \(x_0=\theta_0\in U_r\), and let \(V_0=V(x_0)\).

## 4. The theorem

Let \(X\) solve

\[
dX_s=b(X_s)\,ds+a(X_s)\,dW_s,\qquad X_0=\Phi(x_0).
\tag{10}
\]

This solution is global, unique, and stays on \(M\). For \(f\in C_b^4(\mathbb R^d)\), use

\[
\|f\|_{C_b^4}=\max_{0\le j\le4}\|D^jf\|_\infty.
\]

Let

\[
\begin{gathered}
\alpha=\frac{\lambda}{2\max(1,B^2)},\qquad
C_E=\alpha C_V\exp\left(\frac{2\alpha C_V}{\lambda}+\alpha C_V\right),\\
D_\eta=\sqrt{\frac{C_V\eta}{2\lambda}},\qquad
p_\eta(T)=\exp\left(-\frac{\alpha r^2}{\eta}\right)
\left[\exp\left(\frac{\alpha V_0}{\eta}\right)+\frac{C_ET}{\eta}\right],\\
\mathcal R_\eta(T,V_0)=\mathcal M(T)\|f\|_{C_b^4}
\left[C_N\left(\frac{\eta\sqrt{V_0}}\lambda+TD_\eta\right)
+C_RT\eta+4K^4T\eta^2\right].
\end{gathered}
\tag{11}
\]

For every integer \(0\le N\le T/\eta^2\),

\[
\left|\mathbb Ef(\bar\Phi(\theta_N))-\mathbb Ef(X_{N\eta^2})\right|
\le\mathcal R_\eta(T,V_0)+2\|f\|_\infty p_\eta(T),
\tag{12}
\]

and

\[
\begin{aligned}
\left|\mathbb Ef(\theta_N)-\mathbb Ef(X_{N\eta^2})\right|
\le{}&\mathcal R_\eta(T,V_0)
+C_d\|Df\|_\infty\left((1-2\lambda\eta)^{N/2}\sqrt{V_0}+D_\eta\right)\\
&+2\|f\|_\infty p_\eta(T).
\end{aligned}
\tag{13}
\]

The choice of \(\bar\Phi\) outside the tube only changes the projected quantity on a rare exit event. Formula (13) is a raw-observable statement for the original SGD process, not a replaced or projected algorithm.

In particular, if \(\theta_0\in M\), then

\[
\boxed{\quad
\sup_{0\le N\le T/\eta^2}
\left|\mathbb Ef(\theta_N)-\mathbb Ef(X_{N\eta^2})\right|
\le C(T)\|f\|_{C_b^4}\sqrt\eta.
\quad}
\tag{14}
\]

One completely explicit choice, writing \(c=\alpha r^2\), is

\[
\begin{aligned}
C(T)={}&\mathcal M(T)T
\left[C_N\sqrt{\frac{C_V}{2\lambda}}+C_R+4K^4\right]
+C_d\sqrt{\frac{C_V}{2\lambda}}\\
&+2\left[(2ec)^{-1/2}
+C_ET\left(\frac3{2ec}\right)^{3/2}\right].
\end{aligned}
\tag{15}
\]

For a fixed off-manifold start, (12) is still \(O(\sqrt\eta)\). The raw bound includes a decaying initial layer. Uniform raw convergence down to \(N=0\) is impossible when \(f(x_0)\ne f(\Phi(x_0))\). If \(V_0>\eta\), the layer is at most \(\sqrt\eta\) once

\[
N\ge\frac{\log(V_0/\eta)}{2\lambda\eta}.
\tag{16}
\]

## 5. Proof: confinement and normal moments

Let \(\tau=\inf\{n:\theta_n\notin U_r\}\). The step restriction ensures that a step started before \(\tau\), including the exit step, lies inside \(U_{3r/2}\). Taylor's theorem, (A1), and \(\|\nabla V\|^2=4V\) give, before exit,

\[
V(\theta_{n+1})
\le V(\theta_n)-2\lambda\eta V(\theta_n)
-\eta\nabla V(\theta_n)\cdot\xi_{n+1}+C_V\eta^2.
\tag{17}
\]

The scalar noise in (17) is centered and bounded by \(B\|\nabla V\|\). The elementary bounded-variable exponential estimate gives

\[
\mathbb E_n\exp\left(\frac{\alpha V(\theta_{n+1})}{\eta}\right)
\le\exp\left(\frac{\alpha V(\theta_n)}\eta\right)
\exp\left(-\alpha\lambda V(\theta_n)+\alpha C_V\eta\right).
\tag{18}
\]

Indeed its noise factor is at most \(\exp(2\alpha^2B^2V)\), and \(2\alpha^2B^2\le\alpha\lambda\). If \(V\ge2C_V\eta/\lambda\), the last factor is at most one. Otherwise the expected additive increase of the exponential is at most \(C_E\eta\). Freezing at \(\tau\), iteration therefore yields

\[
\mathbb E\exp\left(\frac{\alpha V(\theta_{N\wedge\tau})}{\eta}\right)
\le e^{\alpha V_0/\eta}+C_EN\eta.
\]

On \(\{\tau\le N\}\), \(V(\theta_\tau)\ge r^2\). Consequently

\[
\Pr(\tau\le N)\le p_\eta(T).
\tag{19}
\]

For the ordinary moment use the **killed**, not frozen, process. Write

\[
v_n=\mathbb E[V(\theta_n)\mathbf1_{\{\tau>n\}}].
\]

Nonnegativity of \(V\) and conditional centering in (17) imply

\[
v_{n+1}\le(1-2\lambda\eta)v_n+C_V\eta^2,
\qquad
v_n\le(1-2\lambda\eta)^nV_0+\frac{C_V\eta}{2\lambda}.
\tag{20}
\]

Thus

\[
\mathbb E[\operatorname{dist}(\theta_n,M)\mathbf1_{\{\tau>n\}}]
\le(1-2\lambda\eta)^{n/2}\sqrt{V_0}+D_\eta,
\tag{21}
\]

and, using \(1-\sqrt{1-2\lambda\eta}\ge\lambda\eta\),

\[
\eta^2\sum_{n<N}\mathbb E[\operatorname{dist}(\theta_n,M)\mathbf1_{\{\tau>n\}}]
\le\frac{\eta\sqrt{V_0}}\lambda+TD_\eta.
\tag{22}
\]

The distinction between frozen exponential control and killed ordinary moments is essential: an exited, frozen point does not continue to contract.

## 6. Proof: limiting SDE and semigroup regularity

At \(y\in M\), \(D\Phi(y)\) is the tangent projection. The tangent identity follows from \(\Phi|_M=\mathrm{id}\); its action on normal directions vanishes by differentiating (A2) at \(y\) and using the nondegenerate normal Hessian. More generally the same conclusion may be included in the phase-map structure of (A2).

Differentiate \(\Phi\circ\Phi=\Phi\) twice. With \(P_y=D\Phi(y)\),

\[
(I-P_y)D^2\Phi(y)[u,v]=D^2\Phi(y)[P_yu,P_yv].
\tag{23}
\]

It follows that the diffusion fields \(a_\ell\) are tangent and the Stratonovich drift

\[
b-\tfrac12\sum_\ell Da_\ell\,a_\ell
\]

is tangent as well. A local-coordinate construction of the Stratonovich equation on \(M\) therefore agrees, by uniqueness, with (10). Compactness prevents explosion. This proves invariance. The global extensions separately guarantee existence and uniqueness for every ambient starting point.

Let \(P_tf(x)=\mathbb E[f(X_t^x)]\) for this extended SDE. We now prove

\[
\|P_tf\|_{C_b^4}\le\mathcal M(T)\|f\|_{C_b^4},\qquad0\le t\le T.
\tag{24}
\]

Let \(J_n=D_x^nX_t^x\), \(1\le n\le4\). Differentiating the integral SDE gives a sum over partitions \(\pi\) of \(\{1,\ldots,n\}\): its drift terms are

\[
D^{|\pi|}b(X_t)[J_{|B_1|},\ldots,J_{|B_{|\pi|}|}],
\]

with identical expressions for each diffusion coefficient. There are at most \(15\) partitions. Put

\[
Z=1+\sum_{n=1}^4\|J_n\|^{8/n}.
\]

For a partition of \(n\), the block orders sum to \(n\). Weighted arithmetic–geometric mean therefore bounds each drift contribution

\[
\|J_n\|^{8/n-1}\prod_{B\in\pi}\|J_{|B|}\|
\]

by \(Z\); it also bounds each quadratic-variation contribution, whose total weighted order is again eight, by \(Z\). The radial Hessian bound for \(\|z\|^p\), \(p\ge2\), supplies a coefficient at most \(p(p-1)\). Itô's formula, Cauchy–Schwarz over at most 15 partitions, and \(p\le8\) give

\[
\mathcal G Z\le(480K+25200K^2)Z
\le26000(1+K)^2Z.
\]

Here \(\mathcal G\) denotes the generator of the augmented flow-and-jet process. Localization, Grönwall, and Fatou give

\[
\mathbb EZ\le(1+d^4)e^{26000(1+K)^2t},
\]

because \(J_1(0)=I_d\) and the higher jets start at zero. Differentiating \(f(X_t^x)\) by the same partition formula and using weighted arithmetic–geometric mean once more gives (24). The moment bounds justify differentiating under expectation. This argument does not require ellipticity.

## 7. Proof: the one-step weak expansion

The limiting generator is

\[
Au=b\cdot Du+\tfrac12aa^\top:D^2u.
\]

At \(y\in M\), the chain rule gives

\[
Au(y)=\tfrac12D^2(u\circ\bar\Phi)(y):\Sigma(y).
\tag{25}
\]

Fix \(x\in U_r\), set \(y=\Phi(x)\), and write \(F=u\circ\bar\Phi\). The partition formula gives \(\|D^jF\|_\infty\le C_\Phi\|u\|_{C_b^4}\) for \(j\le4\). Conditional Taylor expansion, with (A2), yields

\[
\mathbb E_n F(\theta_{n+1})
=F(x)+\frac{\eta^2}{2}D^2F(x):[g(x)g(x)^\top+\Sigma(x)]+R,
\quad |R|\le C_R\|u\|_{C_b^4}\eta^3.
\tag{26}
\]

If \(p\) is the nearest point on \(M\), then

\[
\|x-y\|\le\|x-p\|+\|\Phi(p)-\Phi(x)\|
\le C_d\operatorname{dist}(x,M),\quad
\|g(x)\|\le G_1\operatorname{dist}(x,M).
\]

The globally extended maps allow Lipschitz comparisons along arbitrary straight segments. Equations (25)–(26) imply

\[
\left|\mathbb E_n u(\bar\Phi(\theta_{n+1}))-u(y)-\eta^2Au(y)\right|
\le\|u\|_{C_b^4}\left[C_N\eta^2\operatorname{dist}(x,M)+C_R\eta^3\right].
\tag{27}
\]

Finally, direct differentiation of \(A\) gives

\[
\|A^2u\|_\infty\le8K^4\|u\|_{C_b^4}.
\]

For example, \(\|D(Au)\|\le(2K+\tfrac32K^2)\|u\|_{C_b^4}\) and \(\|D^2(Au)\|\le(4K+\tfrac92K^2)\|u\|_{C_b^4}\). Applying Dynkin's identity twice gives

\[
\|P_hu-u-hAu\|_\infty\le4K^4h^2\|u\|_{C_b^4}.
\tag{28}
\]

With \(h=\eta^2\), combine (27) and (28).

## 8. Proof: telescoping and the final rate

Fix the terminal integer \(N\), put \(u_j=P_{(N-j)\eta^2}f\), and use the time-dependent stopped quantity

\[
u_{N\wedge\tau}\bigl(\Phi(\theta_{N\wedge\tau})\bigr).
\]

The exit point remains in the outer tube. The backward relation \(u_j=P_{\eta^2}u_{j+1}\), (24), (27), and (28) bound the expected telescoping increments by

\[
\mathcal M(T)\|f\|_{C_b^4}
\sum_{j<N}\left[
C_N\eta^2\mathbb E[\operatorname{dist}(\theta_j,M)\mathbf1_{\{\tau>j\}}]
+C_R\eta^3+4K^4\eta^4\right].
\]

Equation (22) bounds this sum by \(\mathcal R_\eta(T,V_0)\). On an exited path the difference between the desired terminal observable and the stopped backward observable is at most \(2\|f\|_\infty\). On a nonexited path the projected terminal observable agrees exactly; the raw terminal observable differs by at most \(C_d\|Df\|_\infty\operatorname{dist}(\theta_N,M)\). Equations (19) and (21) prove (12)–(13).

For \(V_0=0\), all nonexit terms in (13) are at most their coefficients times \(\sqrt\eta\), since \(\eta\le1\). The elementary inequalities

\[
e^{-c/\eta}\le(2ec)^{-1/2}\sqrt\eta,
\qquad
\eta^{-1}e^{-c/\eta}\le\left(\frac3{2ec}\right)^{3/2}\sqrt\eta
\]

follow by maximizing \(u^{1/2}e^{-u}\) and \(u^{3/2}e^{-u}\). They give (15), completing the proof.

## 9. Audit conclusion and remaining scope

The proof survives the main independent checks: correct slow clock; cancellation of the order-\(\eta\) tangential drift; retention of the normal-state error; a noncircular exit estimate; killed normal moments; a uniform backward-semigroup norm; the raw-observable boundary layer; and the same finite SGD horizon throughout.

No claim is made for singular or stratified minimizers, unbounded heavy-tailed noise, nonsmooth phase maps, noncompact manifolds without quantitative replacement conditions, all-time invariant laws, or uniformity as the normal spectral gap vanishes. None is needed for the stated theorem. The prior 2023 positive-rate result prevents classifying this as a newly solved original T355 problem. The appropriate label is **self-contained quantitative refinement on a stated smooth, normally attracting, compact class; novelty unverified**.
