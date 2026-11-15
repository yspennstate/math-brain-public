MINOR

Independent referee report on I0071, survey Problem 7. Reviewed 13 November 2026.

The periodic global-existence claim survives this audit. In particular, estimate (11) is valid for the report's specially constructed polynomial, with species-dependent transport under uniform stochastic parabolicity. A counterexample for an arbitrary mixed Hessian exists, but does not apply to that polynomial. The positive-time energy estimate, optional-stopping argument, positivity theorem and flexible blow-up criterion establish almost-sure nonexplosion in the stated local-theory classes. No restriction on the finite reaction order beyond applicability of the local theory is introduced by this argument.

I request minor revisions for attribution and the extra continuous-dependence assertion. I found no fatal error in the proof of global existence and pathwise uniqueness. Relative to the primary literature independently checked here, the extension to arbitrary fixed, species-dependent Hölder transports appears new. The underlying deterministic polynomial-energy method is established prior work. This is a partial answer to Problem 7: the torus with globally Lipschitz zero-order noise and the specified positive local solutions. It does not settle the whole-space, general-boundary, or superlinear-noise questions.

The errors, omissions and requested fixes are:

1. **Missing close deterministic predecessor.** Location: submitted REPORT §2.1–2.2 and §4.4, especially lines 138–262 and 480–486. The literature discussion omits Fitzgibbon–Morgan–Tang–Yin, *Reaction-Diffusion-Advection Systems with Discontinuous Diffusion and Mass Control*, [arXiv:2103.16863](https://arxiv.org/abs/2103.16863). Its equations (2.9)–(2.10), PDF p. 13, already use mixed multinomial energies with coefficients \(\prod_i\theta_i^{\alpha_i^2}\); Lemma 2.4, p. 14, arranges reaction compatibility, and pp. 15–16 arrange coercivity of the mixed diffusion form. The report's common quadratic exponent, extra linear weights and stochastic covariance estimate provide a particularly explicit variant and extension. Fix: cite and compare this work, distinguishing the deterministic construction from the stochastic transport conclusion. This omission affects attribution, not validity. The deterministic paper has no stochastic derivative term.

2. **The stability citation has a small initial-data quantifier gap.** Location: submitted REPORT line 136 and §2.5, line 365. AV global Assumption 5.1, PDF pp. 34–35, quantifies over nonnegative \(\mathscr F_{s_0}\)-measurable \(C^\theta\) initial data with an \(L^m(\Omega\times\mathbb T^d)\) moment, for some \(\theta>0\). The report explicitly verifies its estimates only for smooth data, then invokes Theorem 5.2. Smooth data alone do not literally verify that assumption. Fix: add the initial-time stopped variational-energy argument for bounded Hölder data, or a localized approximation argument, and retain the stated restrictions \(p\ge q\ge q_*\) and \(2-\delta-d/q>-d/m\). The bounds already proved have exactly the required strength; details of this repair are below. Alternatively, omit the extra stability assertion. The nonexplosion theorem starts at deterministic \(s>0\) and is unaffected.

3. **Incomplete scope description of Fellner–Morgan–Tang.** Location: submitted REPORT §4.4, line 482. The stated bounded-domain subcase is correct, but its Theorem 1.1 also covers \(\mathbb R^d\): Assumption (A1), PDF p. 1, explicitly allows the whole space. Fix: include this when comparing domains. Its growth, mass and deterministic-noise distinctions remain as reported. This is a literature-description omission, not a missing whole-space proof for the submitted theorem.

4. **Missing current transport-noise comparison.** Location: submitted REPORT §4.3, lines 470–478. Add Agresti–Kniely–Tang, [arXiv:2608.13332](https://arxiv.org/abs/2608.13332), Theorem 3.4, PDF p. 15. It obtains high-probability global classical solutions for suitably selected transport noise and complex-balanced networks under further hypotheses. Its quantifiers do not settle the submitted arbitrary-fixed-transport theorem. This is a literature-completeness revision, not prior resolution of the claim.

There are no further mathematical errors established by this audit. Access limitations for the older Morgan and Pierre originals are recorded below, rather than presented as verified original-source proof audits.

**Independent sources and exact source statements.**

All retained source texts were fetched from primary URLs independently of `claim_files/sources`. PDFs were downloaded into memory and piped to `pdftotext -layout`; none was saved. The arXiv texts include the survey v5, AV local v2, AV global v4, both Milesis–Salins versions, Fellner–Morgan–Tang, Morgan–Tang, Fitzgibbon–Morgan–Tang–Yin, and every additional modern paper named in the submission. `data/retrievals.jsonl` records URLs, timestamps, PDF hashes and text hashes. `data/citation_locations.json` records statement locations in these new texts.

The Springer PDF endpoint returned HTML in this audit. I obtained the published edition from the [Delft institutional repository](https://pure.tudelft.nl/ws/portalfiles/portal/257214795/s00030-025-01090-2.pdf). It has one repository cover page: its physical PDF page is the publisher's printed page plus one. In the following, “published p.” means the printed “Page ... of 150”; other page numbers refer to the indicated arXiv PDF. The relevant published material and arXiv v5 agree, including the reversed parabolicity sign and the triangular vector product.

Problem 7 is at [survey v5](https://arxiv.org/abs/2501.18561v5), PDF p. 93, and published p. 131. Its complete mathematical question is as follows. For \(\mathcal O=\mathbb T^d\) or \(\mathbb R^d\), \(\ell\ge2\), transport coefficients \((b_{n,i})_n\in C^\gamma(\mathcal O;\ell^2)\), \(\gamma>0\), and possibly additional boundary conditions when \(\mathcal O\ne\mathbb T^d\), does (8.14) have global well-posedness under these conditions, for a fixed \(h>1\) and each species \(i\)?

- The initial datum is nonnegative.
- \(g_i:\mathbb R^\ell\to\ell^2\) is globally Lipschitz and \(g_i(y)=0\) on the nonnegative face \(y_i=0\).
- \(f_i(y)\ge0\) on that face.
- For nonnegative \(y,z\), \(|f_i(y)-f_i(z)|\le C(1+|y|^{h-1}+|z|^{h-1})|y-z|\).
- For nonnegative \(y\), \(\sum_i f_i(y)\le K_0+K_1\sum_i y_i\), with two nonnegative constants. The printed quantifier names \(K_1,K_2\), whereas the inequality uses \(K_0,K_1\).
- There exist \(r\in\mathbb R^\ell\) and an invertible lower triangular matrix \(R\) with nonnegative entries such that
  \[
  Rf(y)\le\left(1+\sum_i y_i\right)r,\qquad y\in[0,\infty)^\ell,
  \]
  componentwise.

The follow-up asks for superlinear \(g_i\), possibly with the growth permitted by Assumption 8.4(3). The final factor \(r\) in the triangular condition is a vector multiplier, not a scalar exponent. The source calls the upper affine mass inequality conservation; “mass control” is the precise description. The submitted report gets these points right.

Equation (8.14), v5 PDF p. 69 / published p. 96, is the Itô system

\[
du_i-\nu_i\Delta u_i\,dt
=f_i(x,u)\,dt+\sum_{n\ge1}\bigl[(b_{n,i}(x)\cdot\nabla)u_i+g_{n,i}(x,u)\bigr],dW^n,
\qquad u_i(0)=u_{0,i},\quad x\in\mathbb T^d.
\]

Here \(i=1,\ldots,\ell\), the \(W^n\) are independent standard Brownian motions on the prescribed stochastic basis, and \((b_{n,i}\cdot\nabla)u_i=\sum_{j=1}^d b_{n,i}^j\partial_j u_i\). There is no cross-species leading operator; different species can have different transports driven by the same Brownian motions. Problem 7 specializes the displayed nonlinearities to functions of \(u\). The submission restates the equation and its Itô convention correctly.

Assumption 8.4, v5 PDF p. 69 / published p. 97, has integers \(d\ge2\), \(\ell\ge1\), \(p,q\in[2,\infty)\), \(h>1\), \(\delta\in[1,2)\), and the following requirements, with the parabolicity sign corrected as justified below:

- For some \(\alpha>\delta-1\), every coordinate \((b_{n,i}^j)_n\) belongs to \(C^\alpha(\mathbb T^d;\ell^2)\).
- For a common \(\mu>0\), all \(x,\xi,i\) satisfy
  \[
  2\nu_i|\xi|^2-\sum_n|b_{n,i}(x)\cdot\xi|^2\ge\mu|\xi|^2.
  \tag{P}
  \]
- The nonlinearities are measurable, bounded at zero uniformly in \(x\), and satisfy the drift Lipschitz bound above and
  \[
  \|g_i(x,y)-g_i(x,z)\|_{\ell^2}
  \le C(1+|y|^{(h-1)/2}+|z|^{(h-1)/2})|y-z|.
  \]
  The arguments are vectors in the system formulation, despite scalar-domain typography in the displayed assumption.
- Either \(p>2\), \(\delta\in[1,(h+1)/h)\), \(\kappa\in[0,p/2-1)\), and
  \[
  \frac{1+\kappa}{p}+\frac12\left(\delta+\frac dq\right)=\frac h{h-1},
  \qquad
  \frac d{d-\delta}<q<\frac{d(h-1)}{h+1-\delta(h-1)},
  \tag{A}
  \]
  or \(p=q=2\), \(\kappa=0\), \(\delta=1\), \(h\le1+4/d\), with \(h<3\) if \(d=2\).

Both independently obtained survey editions actually print
\(\sum_n|b_{n,i}\cdot\xi|^2\ge(2\nu_i-\mu)|\xi|^2\). That direction is wrong for stochastic parabolicity. The correct inequality is \(\le\), equivalently (P). [AV local](https://arxiv.org/abs/2209.14759v2), Assumption 2.1(3), p. 7, states
\[
\sum_{j,k}\left(a_i^{jk}-\tfrac12\sum_n b_{n,i}^j b_{n,i}^k\right)\xi_j\xi_k\ge\lambda_i|\xi|^2,
\qquad\lambda_i>0.
\]
For \(a_i=\nu_i I\), take \(\lambda_i=\mu/2\). A scalar Fourier mode also verifies the sign: its effective dissipative coefficient is \(2\nu_i|k|^2-\sum_n|b_{n,i}\cdot k|^2\). The submission explicitly corrects the source and assumes (P), so this is not a defect in its claim.

The precise local framework is
\[
X_0=H^{-\delta,q}(\mathbb T^d;\mathbb R^\ell),\qquad
X_1=H^{2-\delta,q}(\mathbb T^d;\mathbb R^\ell).
\]
In case (A), Theorem 8.6, v5 p. 70 / published p. 98, supplies the unique maximal adapted local strong solution for
\[
u_0\in L^0_{\mathscr F_0}
\left(\Omega;B^{d/q-2/(h-1)}_{q,p}(\mathbb T^d;\mathbb R^\ell)\right).
\]
Its lifetime is strictly positive almost surely. On its lifetime it belongs locally to
\[
L^p([0,\sigma),t^\kappa dt;H^{2-\delta,q})
\cap C([0,\sigma);B^{d/q-2/(h-1)}_{q,p}),
\]
and for every finite \(a>2\), \(\theta\in(0,1)\), it instantaneously has
\[
u\in L^a_{\rm loc}((0,\sigma);H^{1,a})
\cap C^{\theta/2,\theta}_{\rm loc}((0,\sigma)\times\mathbb T^d).
\tag{Reg}
\]
Here \(L^0\) assumes measurability, not an initial moment. The paper's version is AV local Theorem 2.7, p. 10, with its coefficient and parameter assumptions. Its Sobolev coefficient assumption admits the survey's Hölder specialization by taking a slightly smaller smoothness exponent and a sufficiently large finite spatial integrability exponent.

The Hilbert endpoint has the actual trace \(L^2=B^0_{2,2}\), not the negative critical smoothness displayed by the survey when \(h<1+4/d\). AV local Proposition 7.1, p. 34, explicitly starts in \(L^2\); Proposition 7.2 supplies (Reg) under the additional coefficient regularity. The report identifies this discrepancy and makes its main theorem in case (A), with a separate conditional continuation statement for already constructed positive Hilbert solutions with (Reg). That is a sound restriction.

The exact blow-up criterion used is Theorem 8.9(1), v5 p. 71 / published p. 100. Given the original local solution, take admissible auxiliary parameters with \(h_0\ge h\), \(h_0\ge1+4/d\), \(p_0>2\), \(\delta_0>1\), and
\(q_0=d(h_0-1)/2\). For every \(m>q_0\) and \(0<s<T<\infty\),
\[
\mathbb P\left(s<\sigma<T,\quad
\sup_{s\le t<\sigma}\|u(t)\|_{L^m}<\infty\right)=0.
\tag{BU}
\]
The auxiliary parameters need not equal those of the original solution. The direct antecedent is AV local **Corollary 2.11(1)**, p. 12, following its more general Theorem 2.10. The report uses the strict inequality \(m>q_0\), and quotes (BU) correctly. The criterion does not require the rough original initial datum to belong to the auxiliary trace space.

Positivity is **Proposition 8.10**, v5 p. 71 / published p. 100, and AV local Theorem 2.13, p. 13. The exact hypotheses needed here are nonnegative initial data, face quasi-positivity of \(f_i\), and face vanishing of every \(g_{n,i}\). In the local paper there is also a face condition for a conservative nonlinear drift \(\operatorname{div}F_i\); it is automatic since \(F_i=0\) here. Positivity of rough initial data is interpreted distributionally. Positive-time values are pointwise by (Reg). Species-independent or divergence-free \(b\) is not an extra hypothesis. The submission uses this proposition correctly.

**Line-by-line mathematical audit.**

The energy exponent \(m\) is fixed and finite throughout. The tuning parameter \(\vartheta\) can be chosen independently of \(m\); the remaining weights and energy-equivalence constants may depend very strongly on \(m\). No passage to \(m=\infty\) occurs.

For submitted equations (1)–(3), every diagonal entry of \(R\) is positive because it is triangular, invertible and entrywise nonnegative. The backward recursion for the \(t_i\) therefore defines finite positive constants. The coefficient bounds
\[
\min_{|\alpha|=m}c_\alpha\left(\sum_i y_i\right)^m
\le\Phi_m(y)\le
\max_{|\alpha|=m}c_\alpha\left(\sum_i y_i\right)^m
\]
follow directly from the multinomial theorem on \(y\ge0\). Thus the energy is positive away from zero on the cone and controls every component's \(L^m\)-norm. It need not be positive on all of \(\mathbb R^\ell\); the proof only evaluates it on nonnegative solutions.

For (4)–(5), differentiate the original multinomial sum, including its combinatorial factor. At degree \(m-1\), the coefficient vector is
\[
v_{\beta,i}=c_{\beta+e_i}
=F_\beta\,t_i\vartheta^{2\beta_i},\qquad
F_\beta=\vartheta^{\sum_k\beta_k^2+1}t^\beta>0.
\]
Since \(0\le\beta_i\le m-1\), the displayed recursion ensures
\(v_i\ge\sum_{j>i}(R_{ji}/R_{jj})v_j\). In the backward solution \(R^T\eta=v\), induction gives both \(\eta_j\ge0\) and \(\eta_j\le v_j/R_{jj}\). Hence every \(\eta_i\ge0\). Summing the vectors with nonnegative monomial weights gives \(\nabla\Phi_m=R^T\lambda\), \(\lambda\ge0\). Consequently
\[
\nabla\Phi_m\cdot f=\lambda\cdot Rf
\le(1+\textstyle\sum_i y_i)\lambda\cdot r^+
\le C_m(1+\Phi_m).
\]
The last step uses that \(\lambda\) is a fixed polynomial of degree \(m-1\). Its constants depend on the equation, \(R,r,m,\vartheta\), not the solution. The separate mass-control assumption is indeed unused. None of these inequalities asks for an upper bound on an individual positive reaction away from its face.

Here is a hand check for two species, without relying on the submitted code. Write
\[
R=\begin{pmatrix}a&0\\ b&c\end{pmatrix},\qquad a,c>0,
\quad b\ge0,
\quad L=\vartheta^{2(m-1)},\quad
t_2=1,\quad t_1=L(1+b/c).
\]
For \(\beta=(k,m-1-k)\),
\[
\frac{v_1}{v_2}
=t_1\vartheta^{2(2k-m+1)}\ge1+b/c.
\]
Thus \(\eta_2=v_2/c\) and \(\eta_1=(v_1-bv_2/c)/a\) are nonnegative. In degree two the energy is explicitly
\[
\Phi_2=\vartheta^4t_1^2 y_1^2
+2\vartheta^2t_1y_1y_2+\vartheta^4y_2^2.
\]
Its mixed coefficient divided by the geometric mean of its pure quadratic coefficients is \(\vartheta^{-2}\), while both required cone inequalities hold. For \(R=\left(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\right)\), writing the quadratic as \(Ay_1^2+2By_1y_2+Cy_2^2\) gives exactly the submitted identity in §3 with \(A\ge B\ge C\).

For three species, write
\[
R=\begin{pmatrix}a&0&0\\ b&c&0\\ d&e&f\end{pmatrix},
\quad a,c,f>0,\quad b,d,e\ge0.
\]
The proposed weights are
\[
t_3=1,\quad t_2=L(1+e/f),\quad
t_1=L\bigl(1+(b/c)t_2+d/f\bigr).
\]
For every degree-\(m-1\) multi-index they ensure
\(v_2\ge(e/f)v_3\) and
\(v_1\ge(b/c)v_2+(d/f)v_3\). Direct inversion gives
\[
\eta_3=v_3/f,\quad
\eta_2=(v_2-ev_3/f)/c,\quad
\eta_1=(v_1-b\eta_2-dv_3/f)/a\ge0.
\]
In particular, no false assertion that \(R^{-1}\) is entrywise nonnegative is being used. For \(m=2\),
\[
\Phi_2=\vartheta^4\sum_i t_i^2y_i^2
+2\vartheta^2\sum_{i<j}t_it_jy_iy_j.
\]
For every higher degree the same coefficient calculation applies, including \(\beta=(m-1,0,0),(0,m-1,0),(0,0,m-1)\), where the extreme ratios must be controlled. The common factor \(L\) is sufficient for all of them.

For submitted (6)–(8), the exponent difference is exactly
\[
\sum_k(\beta+e_i+e_j)_k^2
-\tfrac12\sum_k\bigl[(\beta+2e_i)_k^2+(\beta+2e_j)_k^2\bigr]=-2
\quad(i\ne j).
\]
The powers of \(t\) cancel. Hence every coefficient matrix has normalized off-diagonal entries \(\rho=\vartheta^{-2}\), and is a positive diagonal congruence of
\((1-\rho)I+\rho\mathbf1\mathbf1^T\). Its eigenvalues in these normalized coordinates are \(1-\rho\) and \(1+(\ell-1)\rho\). Summing with the nonnegative monomial weights proves (7)–(8), including on the boundary of the cone. For \(m>2\) the Hessian vanishes at the origin, which does not harm the estimate.

The dangerous transport step can fail for a different Hessian. Take \(d=2\), \(\nu_1=\nu_2=1\), one Brownian motion, \(b_{1,1}=e_1\), \(b_{1,2}=-e_1\), and \(\Phi(y)=\tfrac12(y_1+y_2)^2\). These constant fields satisfy (P) with \(\mu=1\). With \(z_1=e_1,z_2=-e_1\), the mixed diffusion contribution is zero and the Itô correction is two. Thus
\[
Q_y(z)=-2.
\]
This is an actual counterexample to applying componentwise parabolicity to an arbitrary convex mixed energy. It explains why positivity of the Hessian alone is insufficient.

It is **not** a counterexample to submitted (11). An independent way to check the report's argument is to apply Cauchy–Schwarz to its coefficient-matrix decomposition, obtaining
\[
0\le H_{ij}(y)\le\rho\sqrt{H_{ii}(y)H_{jj}(y)}\quad(i\ne j).
\]
Let \(D=\sum_iH_{ii}|z_i|^2\), \(a_i=\sqrt{H_{ii}}|z_i|\). The diagonal part of \(Q\) is at least \((\mu/2)D\). The absolute off-diagonal part is at most
\[
\rho\left(V+\tfrac12B^2\right)\sum_{i\ne j}a_ia_j
\le\rho K(\ell-1)D.
\]
Here \(|\sum_n(b_{n,i}\cdot z_i)(b_{n,j}\cdot z_j)|\le B^2|z_i||z_j|\) for any inter-species covariance. The report chooses \(\rho K(\ell-1)\le\mu/4\), so
\[
Q_y(z)\ge\frac\mu4D.
\]
All factors and signs agree with (10)–(11). This proof is uniform in \(m\) for the relative Hessian estimate and coercivity margin. Energy-equivalence and lower-order constants are not uniform in \(m\), nor do they need to be. The transport need not be common, divergence free, or small; \(\vartheta\) is chosen after its bounded coefficients. In the counterexample above, replacing the normalized Hessian's off-diagonal one by \(\rho=1/9\) gives a smallest quadratic-form eigenvalue \(1/2-3/(2\cdot9)=1/3>1/4\).

For (12)–(14), global Lipschitz continuity and the correct face condition yield the stronger componentwise bound
\(\|g_i(y)\|_{\ell^2}\le L_i y_i\) on the cone. Because the Hessian has nonnegative entries,
\[
\sum_iH_{ii}y_i^2\le y^THy=m(m-1)\Phi_m(y).
\]
It follows, even for correlated zero-order noises, that
\[
\operatorname{tr}(g^THg)\le C_m\Phi_m,
\qquad
|\operatorname{tr}(\mathcal B^THg)|
\le C_mD^{1/2}\Phi_m^{1/2}.
\]
One can prove the cross bound by Cauchy–Schwarz in the nonnegative Hessian form and (8), followed by Young's inequality. It consumes \(\mu D/8\); it imposes no smallness on \(g\). The trace estimate is correct, including on a face where a component is zero.

For (15)–(16), integration by parts in the diffusion gives
\(-\sum_{ij}\nu_iH_{ij}\nabla u_i\cdot\nabla u_j\); symmetry of \(H\) permits the factor \((\nu_i+\nu_j)/2\). The quadratic variation of \(\mathcal B+g\) gives
\(\tfrac12H[\mathcal B,\mathcal B]+H[\mathcal B,g]+\tfrac12H[g,g]\). Thus the cross term in (15) has coefficient one, as displayed. Combining the preceding estimates leaves the claimed positive dissipation margin \(c=\mu/8\).

The regularity justification is adequate; it does not require differentiating a Hölder field \(b\). More explicitly, fix \(s>0\), localize the starting energy, and stop before an original local-solution stopping time, a spatial supremum cutoff, and a cutoff of \(\int_s^t\|u\|_{H^{1,2}}^2\). On such an interval, \(f(u)\) is bounded, and
\(\sum_n\|b_{n,i}\cdot\nabla u_i+g_{n,i}(u)\|_2^2\)
is time-integrable with a deterministic bound depending on the cutoffs. A smooth cutoff of \(\Phi_m\) has bounded first and second derivatives on the relevant range. Spatial convolution converges strongly in \(L^2(H^1)\), and the convolved noise converges strongly in \(L^2(\ell^2;L^2)\). This proves the integrated Itô identity by passage to the limit. There is no commutator estimate involving a derivative of \(b\).

The stochastic integral is a genuine square-integrable stopped martingale. In fact, with \(G_n=b_n\cdot\nabla u+g_n(u)\), its bracket satisfies
\[
\langle M_m\rangle_{T\wedge\tau}
\le |\mathbb T^d|\int_s^{T\wedge\tau}
\int\sum_n\left|\sum_i\partial_i\Phi_m(u)G_{n,i}\right|^2dxdt
\le C_N(T+N)
\]
under these cutoffs. The localization exhausts \([s,\sigma)\) by (Reg). This supplies the needed expectation-zero assertion, without a global moment assumption.

For (17)–(18), on an \(\mathscr F_s\)-event \(\Gamma\subset\{s<\sigma\}\) with bounded initial energy,
\(\mathbf1_\Gamma e^{-C_m(t-s)}(1+E_m(t))\) is a nonnegative stopped local supermartingale. At the first energy crossing of \(A\), before \(T\), its value is at least \(e^{-C_m(T-s)}(1+A)\). Optional stopping and then passage through the exhausting cutoffs therefore give exactly
\[
\mathbb P\left(\Gamma\cap\left\{\sup_{s\le t<\sigma\wedge T}E_m(t)\ge A\right\}\right)
\le\frac{e^{C_m(T-s)}}{1+A}
\mathbb E[\mathbf1_\Gamma(1+E_m(s))].
\]
Strict thresholds followed by a limit remove any half-open-interval issue. Let \(A\to\infty\), then exhaust \(\{s<\sigma\}\) by the events \(E_m(s)\le k\). This gives almost-sure boundedness of the time supremum in \(L^m\) before \(\sigma\wedge T\). It does not claim integrability of that supremum. Keeping the nonnegative dissipation and taking stopped expectations also gives the stated expectation bound for its time integral. Both arguments are valid. There is no unjustified BDG absorption.

For §2.5, choose \(h_0>\max\{h,1+4/d\}\) and \(q_0=d(h_0-1)/2>2\). An explicit admissible small choice of \(\delta_0-1>0\) can satisfy all of
\[
\delta_0-1<\gamma,\qquad
\delta_0<(h_0+1)/h_0,\qquad
\delta_0<d-2/(h_0-1).
\]
The last upper bound exceeds one: for \(d=2\) this follows from \(h_0>3\), and for \(d>2\) from the chosen lower bound on \(h_0\). These inequalities give the lower \(q_0\) constraint. The upper \(q_0\) constraint is strict when \(\delta_0>1\), with positive denominator. Taking \(p_0\) sufficiently large and
\(\kappa_0=p_0(1-\delta_0/2)-1\) gives \(\kappa_0\in[0,p_0/2-1)\) and the equality in (A). Larger \(h_0\) still bounds the given reaction and Lipschitz noise.

Now fix one integer \(m>q_0\). The energy bound and (BU) yield \(\mathbb P(s<\sigma<T)=0\). Countably many \(s\downarrow0\) and \(T\uparrow\infty\), together with \(\sigma>0\) almost surely, prove \(\mathbb P(\sigma=\infty)=1\). This works for every original admissible \((p,q,\delta,\kappa)\) in case (A), not just the auxiliary critical Lebesgue setting. It does not silently increase the growth exponent at time zero and replace the original data class. The Hilbert continuation statement can instead be connected to AV local Propositions 7.1–7.3 and positive-time compatibility. For \(d=1\), the dummy-variable argument applies to the corresponding embedded two-dimensional data classes; a claim about every separate one-dimensional trace space would require checking the paper's Section 6 and is not asserted by the submitted theorem's qualification.

For the additional stability assertion, put \(q_*=\max\{d(h-1)/2,2\}\). The submitted estimates for \(\Phi_2+\Phi_m\), \(m\ge q_*\), imply
\[
\|u\|_{q_*}^{q_*}\le C(E_2+E_m),\qquad
\sum_i\int u_i^{q_*-2}|\nabla u_i|^2
\le C(D_2+D_m).
\]
They give both probability bounds in AV global Assumption 5.1, with tails tending to zero and right side \(C(1+\mathbb E\|u(s_0)\|_m^m)\). For full applicability one must also establish them starting at Hölder, rather than only smooth, initial data. A standard repair is to localize the initial \(C^\theta\) norm, truncate the nonlinearities outside a bounded range, and use the resulting variational solution with an \(L^2\) initial trace to apply the same cutoff Itô identity from \(s_0\). This agrees with the given local solution by uniqueness. Exhausting the range and initial-data cutoffs gives the displayed estimates with constants depending only on the equation, the energy degree and the time interval; no Hölder norm remains in their right sides. One may equivalently use localized smooth approximation. With that addition, Assumption 5.1 and Theorem 5.2 apply under precisely the extra restrictions stated in the submission. No change to the main theorem is needed.

**Literature result and citation audit.**

The following comparison checks every substantive named citation in the submitted REPORT. Page locators were checked against the independent text files; the complete locator list is retained in `data/citation_locations.json`.

| Citation in the submitted report | Independently checked result | Assessment |
|---|---|---|
| Survey equation (8.14), Assumption 8.4, Theorem 8.6, Propositions 8.8/8.10, Theorem 8.9 | v5 pp. 69–71; published pp. 96–100; Problem 7 at v5 p. 93 / published p. 131 | Restatement correct, with the explicitly discussed source sign and trace corrections. |
| Survey Definitions 4.5–4.6 and Theorem 4.7 | Local adapted integral formulation and maximal-regularity trace | The definition used in the report is appropriate; “strong” does not claim spatially classical paths. |
| AV local, arXiv:2209.14759v2 | Assumption 2.1 p. 7; Definition 2.3 p. 8; Theorem 2.7 p. 10; Theorem 2.10 pp. 11–12; Corollary 2.11 p. 12; Theorem 2.13 p. 13; Hilbert propositions pp. 34–35 | Supplies the needed local theory, flexible continuation and positivity. The direct Lebesgue blow-up statement is Corollary 2.11(1). |
| AV global, arXiv:2301.06897v4, Assumption 3.1 / Theorem 3.2 | p. 10; global existence under an additional weighted sum of component \(L^\zeta\) coercivity inequalities, \(\zeta\ge q_*\) | Does not establish the arbitrary triangular case. Its leading transports may differ by species. |
| Same, Assumption 4.4 / Theorem 4.5 | pp. 23–24; predator–prey, \(d\le4\), quadratic reactions, nonnegative \(L^2\) data, model-specific noise inequalities | Scope and the displayed \(N_1,N_2\) in the submission agree with the source. |
| Same, Assumption 4.8 / Theorem 4.9 | pp. 26–27; Brusselator in dimensions one and two, cubic reaction, stated \(\delta,q,p\) restrictions | The submission's restrictions and noise bounds agree. This theorem also has signed-data cases; the positivity specialization is enough for the comparison. |
| Same, Assumption 4.10 / Theorem 4.11 | pp. 29–30; three-dimensional Brusselator, nonnegative \(L^3\) data, \(q=3\), \(\delta\in(1,4/3]\), \(p\ge3\vee2/(2-\delta)\) | The special \(1/5\) coefficient in \(N_1\) and the other displayed bounds agree. |
| Same, Example 4.12 | p. 34; Gray–Scott obtained within the Brusselator treatment | Correct. |
| Same, Assumption 5.1 / Theorem 5.2 | pp. 34–35; energy-based transfer to global continuous dependence in the critical Besov trace, with \(p\ge q\ge q_*\) and the embedding condition | Correct citation, subject to numbered issue 2. This theorem does not itself produce triangular energy estimates. |
| Survey Theorems 8.15 / 8.18 | published pp. 102 / 104 | Coercive systems / the displayed predator–prey model; no general triangular theorem. |
| Agresti, delayed blow-up, arXiv:2207.08293 | Theorems 3.5–3.6, pp. 12–13 | Chooses noise intensity and spectrum for prescribed high-probability delayed/global existence; the global result assumes exponentially decreasing mass. The source quantifiers are correctly distinguished from almost-sure globality for every fixed admissible transport. |
| Milesis–Salins v1, arXiv:2604.06645v1 | Assumptions 0–11 pp. 8–11; general triangular matrix in Remark 1 p. 9; Theorem 5.1 p. 23; Theorem 6.1 p. 31; Lemma 3 p. 20 | Correct version and theorem numbering; no transport derivative. |
| Milesis–Salins v2, arXiv:2604.06645v2 | Assumptions 0–11 pp. 9–12; Remark 1 p. 10; Theorem 5.1 p. 29; Theorem 5.2 p. 31; Lemma 4 p. 20 | Correct. ArXiv history independently lists exactly v1 and v2 at the audit date. |
| Agresti–Germ–Veraar, arXiv:2606.07417v3 | Theorem 2.9 p. 13; Theorem 2.12 p. 15; Theorem 2.20 / Corollary 2.21 p. 17; Theorem 2.24 p. 19; Example 3.4 p. 22; Corollary 3.14 p. 26 | All stated locators and distinctions verified. Its noise is multiplicative coloured zero-order noise, not transport. The scalar logarithmic-growth corollary is not a triangular-system resolution. Both v2 and v3 were independently fetched. |
| Blessing–Seitz–Sonner–Tang, arXiv:2502.01209 | (F1)–(F2) pp. 18–19; Theorem 4.10 p. 24 | Scalar, dissipative, additive-noise result with dimension-dependent growth restrictions, as reported. |
| Földes–Stacy, arXiv:2601.19145 | SPDE Assumptions 2–3 pp. 40–41; Theorem 6.31 pp. 47–48 | Positive-part bounds are componentwise linear in the stated variables; noise is Nemytskii with bounded derivative and spectral colouring. It does not cover general triangular cancellations with transport. |
| Fellner–Morgan–Tang, independently fetched as arXiv:1808.01315 | (A1)–(A5) pp. 1–2; Theorem 1.1 p. 2; Remark 1.1(ii) pp. 2–3 | The growth and boundary comparison is correct; add its whole-space scope as in numbered issue 3. |
| Souplet, arXiv:1804.05193 | (2)–(9) pp. 1–2; main Theorem p. 3 | Correct: bounded nonnegative data, mass and entropy dissipation, at most quadratic derivative growth; bounded Neumann domain or whole space. |
| Morgan 1989 / 1990 and Pierre 2010 | Bibliographic entries and their role in the survey; duality statement reproduced in Milesis–Salins Lemma 3 / Lemma 4 | Original full texts were not accessible in this audit. No original-proof verification is claimed. |

For the detailed AV model comparisons, I also checked the actual algebraic noise inequalities, not only theorem headings. With \(\lambda_i\) denoting the positive parabolicity residual, the source quantity is
\[
\mathcal A_i=\tfrac12\|g_i\|_{\ell^2}^2+
\frac{(\sum_n|b_{n,i}|\,|g_{n,i}|)^2}{4(\lambda_i-\varepsilon)}.
\]
The submitted predator–prey \(N_1,N_2\), two-dimensional Brusselator \(N_1,N_2\), and the three-dimensional replacement of the mixed coefficient by \(1/5\) match the independent AV text. The report also correctly flags the interchanged face identities printed in some of these special-model assumptions: the positivity condition actually needed is \(g_1(0,y_2)=g_2(y_1,0)=0\), which Problem 7 states unambiguously. These source typographical issues do not enter the new proof.

The printed survey's bibliography shift is real. The independently obtained published bibliography has Morgan at [199,200], Pierre at [212], Neelima–Šiška at [201], and Pisier at [213], whereas the prose by Problem 7 refers to [200,201] and [213]. The report's corrections agree with the titles, and the arXiv version uses author-year keys.

The mathematical distinctions from the closest results are consequential. [AV global](https://arxiv.org/abs/2301.06897v4), §1.4, p. 6, explicitly leaves general triangular systems open. Its results allow species-dependent transport, so exclusion of such transport is **not** the reason they fail to settle Problem 7. They require stronger component energy/coercivity bounds or special predator–prey/Brusselator structure. Entropy or mass control by itself is not their general global strong-solution theorem.

[Milesis–Salins](https://arxiv.org/abs/2604.06645v2) treats
\(\partial_tu_i-d_i\Delta u_i=f_i(u)+\sum_k\sigma_{ik}(u)\dot W_k\)
on bounded smooth domains with homogeneous Dirichlet or Neumann conditions and bounded nonnegative initial data. It has no \(b\cdot\nabla u\). Its coefficients are locally Lipschitz with linear total-state growth, and it permits certain non-trace-class spatial covariances. Besides the heat kernel bound, the kernels must be pointwise nonnegative, symmetric positive definite, integrable in one variable uniformly in the other, and satisfy the heat-kernel convolution bound \(Ct^{-\eta}\), \(0<\eta<1\). This agrees with the submission, including the warning that a Riesz exponent must also obey \(\beta<2\). Their proof uses a stochastic convolution and deterministic duality; it is not a transport-noise extension of the claimed theorem.

The independent search also found [Agresti–Kniely–Tang, arXiv:2608.13332](https://arxiv.org/abs/2608.13332), absent from the submitted comparison. Its Theorem 3.4, PDF p. 15, selects finite-spectrum transport for complex-balanced reaction networks without boundary equilibria, obtaining \(\mathbb P(\tau=\infty)>1-\varepsilon\). The selected noise depends on the prescribed tolerances and data bounds. It neither treats every triangular system nor proves probability-one globality for every admissible fixed transport. It should be added for completeness, but does not remove the present result's apparent novelty.

The closest deterministic method is [Fitzgibbon–Morgan–Tang–Yin](https://arxiv.org/abs/2103.16863): mixed polynomial energies adapted to intermediate-sum conditions and nonsmooth, unequal diffusion. Its Theorem 1.1, p. 5, includes linear triangular control as intermediate-sum order one and arbitrary polynomial individual reactions. This explains why the polynomial idea itself should not be presented without attribution. Its absence of stochastic terms leaves the covariance estimate and the probabilistic localization/continuation as a new extension in the submitted argument.

I cannot know why the survey's authors did not use this route. The obstacle they describe is failure of their deterministic duality route under transport noise. The submitted proof uses an alternative deterministic energy tradition, tunes its normalized mixed Hessian before applying Itô's formula, and uses only one sufficiently large finite energy with an already available flexible blow-up criterion. Those are concrete reasons a short proof can avoid the particular obstacle described in the survey. The existence of a posed problem is not a counterargument to the verified calculation.

The old-source access limitation is explicit. Morgan's DOI metadata and bibliography are consistent with the submission, but the original PDF endpoints returned 403. Pierre's legacy primary archive returned 404 after a certificate-chain failure was separately diagnosed; publisher access did not supply an original text. Milesis–Salins v1 Lemma 3 and v2 Lemma 4 reproduce Pierre's **Lemma 3.4**, the duality estimate; the triangular global result is cited separately as Pierre's Theorem 3.5. The submission does not confuse those two. The old papers are contextual, and no step of the submitted energy proof is accepted on the authority of their inaccessible proofs.

Search queries and screened sources are recorded in `data/search_queries.txt`. The public AIM problem-741 catalogue formulation was inspected read-only; it also distinguishes Milesis–Salins and the August 2026 result from the arbitrary fixed-transport question. It is a problem catalogue, not an independent resolution. The literature conclusion is dated 13 November 2026 and concerns the checked sources; it is not a proof that no unindexed or unpublished prior theorem exists.

**Verification record and precise accepted scope.**

I independently differentiated the energy and re-derived the reaction-cone and covariance estimates by hand as above. `code/check_algebra.py` imports no submitted code. It checked \((\ell,m)=(2,2),(2,3),(2,5),(3,2),(3,3),(3,4)\) with non-unit dense triangular matrices; it directly differentiates the multinomial polynomial and compares the Hessian decomposition, checks Euler identities, cone inversion and boundary values, and evaluates the complete diffusion-minus-Itô form with opposite species transports, unequal diffusivities, two spatial directions and up to two Brownian modes. It passed **24,063 counted exact rational checks**, of which 23,814 are quadratic-form evaluations. It also verifies the generic-Hessian counterexample and the positive margin after tuning. These computations are finite evidence; the arbitrary-degree and arbitrary-coefficient proof is the algebra above. Results are in `data/independent_algebra.json`.

The source texts are plain text only. Retrieval and checking ran with inherited nice 20, one compute thread, and memory far below the 4 GB limit; downloads were small and sequential. No subagents, publication, pushes, or changes to the submitted claim files were made. Input fingerprints are retained in `data/claim_input_hashes.json`.

What is proved is the following. On \(\mathbb T^d\), \(d\ge2\), assume bounded Hölder species transports, (P), the six Problem-7 hypotheses, and nonnegative data in an admissible case-(A) local trace space. Then the maximal prescribed-basis local strong solution is global almost surely and retains its local-theory regularity; pathwise uniqueness and positivity persist. Any finite polynomial reaction order can be handled once a suitable local theory is available. The same estimate continues positive Hilbert solutions with (Reg), and the dummy-variable reduction gives the stated corresponding one-dimensional cases. The extra global continuity assertion is justified after the minor initial-data extension described above and only under its specified parameters.

No claim is accepted here for arbitrary nonnegative data outside a specified local class, for every independent one-dimensional trace realization, for \(\mathbb R^d\), for general physical boundaries, or for superlinear \(g\). The report's whole-space observation about nonzero \(f(0)\) is valid: a spatially constant forcing need not preserve a finite unweighted \(L^q(\mathbb R^d)\) space. Its superlinear-noise limitation is also valid: the face-Lipschitz bound \(\|g_i(y)\|\le L_iy_i\) then fails, and the Hessian trace need not have degree at most \(m\). Neither limitation refutes the accepted torus theorem.

Task: “You are an independent referee … Break it if it is wrong.” Received 13 November 2026, approximately 19:56 Asia/Tbilisi (workspace run marker; exact message time unavailable).
