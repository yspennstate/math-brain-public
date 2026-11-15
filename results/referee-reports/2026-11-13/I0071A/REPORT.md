PARTIAL

# I0071: triangular reaction–diffusion systems with transport noise

Task: “Open problem I0071”, received 13 November 2026 at approximately 18:56 Asia/Tbilisi.

This report proves the periodic, globally Lipschitz-noise case of Problem 7, in every spatial dimension and for every finite polynomial reaction order allowed by the local theory. The transport coefficients may differ between species, need not be divergence free, need not be small, and need only have the Hölder regularity used in that theory. The indispensable assumption is uniform stochastic parabolicity. A polynomial energy with mixed monomials handles the triangular reaction inequalities and the mixed transport Itô terms simultaneously.

The status is PARTIAL because the theorem below is restricted to the torus. This report does not establish a full-space theorem in an explicitly specified initial-data space, nor a theorem for arbitrary additional boundary conditions, nor the question's further extension to superlinear noise. No printed result located in the literature search settles the general transport problem. The closest 2026 triangular result, Milesis–Salins, has no transport noise.

## 1. Source statement and the meaning of the question

Page numbers for the survey below are the publisher's “Page ... of 150”, not the arXiv pagination. Problem 7 is on published p. 131, or arXiv v5 PDF p. 93. Equation (8.14) is on published p. 96, or v5 PDF p. 69. The HTML conversion renumbers some equations; PDF numbering is used here.

### Equation (8.14)

For an integer \(\ell\geq1\), \(i=1,\dots,\ell\),

\[
 \begin{cases}
 du_i-\nu_i\Delta u_i\,dt
  =f_i(\cdot,u)\,dt+
    \displaystyle\sum_{n\geq1}
       [(b_{n,i}\cdot\nabla)u_i+g_{n,i}(\cdot,u)]\,dW^n,
       &\text{on }\mathbb T^d,\\
 u_i(0)=u_{0,i},&\text{on }\mathbb T^d.
 \end{cases} \tag{8.14}
\]

Here \(u:[0,\infty)\times\Omega\times\mathbb T^d\to\mathbb R^\ell\), \(W^n\) are independent standard real Brownian motions on a fixed filtered probability space, and \((b_{n,i}\cdot\nabla)u_i=\sum_{j=1}^d b^j_{n,i}\partial_j u_i\). The stochastic integrals are Itô integrals. Diffusion and transport are diagonal in the species index; the reactions and the zero-order noise may couple species. The same Brownian motions may drive both types of noise. A Stratonovich formulation would require its correction to be included in the drift, as discussed in Remark 8.12; it is not interchangeable with this displayed Itô equation.

### The six conditions in Problem 7

The problem asks about \(\mathcal O=\mathbb T^d\) or \(\mathbb R^d\), \(\ell\geq2\), \((b^j_{n,i})_{n\geq1}\in C^\gamma(\mathcal O;\ell^2)\) for some \(\gamma>0\) (equivalently the vector-field-valued version, with the finite spatial coordinate understood), and “possibly additional boundary conditions” off the torus. For a fixed \(h>1\), its conditions are:

1. \(u_0\in[0,\infty)^\ell\).
2. \(g_i:\mathbb R^\ell\to\ell^2\) is globally Lipschitz, and \(g_i(y)=0\) whenever \(y\in[0,\infty)^\ell\) and \(y_i=0\).
3. \(f_i(y)\geq0\) whenever \(y\in[0,\infty)^\ell\) and \(y_i=0\).
4. For all \(y,y'\in[0,\infty)^\ell\),
   \[
   |f_i(y)-f_i(y')|\lesssim
   (1+|y|^{h-1}+|y'|^{h-1})|y-y'|.
   \]
5. Mass control:
   \[
   \sum_{j=1}^\ell f_j(y)\leq K_0+K_1\sum_{j=1}^\ell y_j
   \quad(y\geq0).
   \]
   The printed quantifier says “\(\exists K_1,K_2\geq0\)” but the displayed inequality uses \(K_0,K_1\). This is a naming inconsistency. The intended condition has two nonnegative constants. The source calls this “mass conservation”; an upper affine bound is mass control, not an equality asserting conservation.
6. There are a vector \(r\in\mathbb R^\ell\) and an invertible lower triangular matrix \(R\in\mathbb R^{\ell\times\ell}\), all of whose entries are nonnegative, such that
   \[
       Rf(y)\leq \left[1+\sum_{i=1}^\ell y_i\right]r
       \quad\text{componentwise for every }y\geq0. \tag{T}
   \]

**The last expression is multiplication by the vector \(r\), not exponentiation.** There is no scalar triangular-growth exponent to restrict. This is explicit in v5 and in the publisher's text: \(r\in\mathbb R^\ell\). A plain-text extraction can lose the superscript \(\ell\). In particular, the source does not state the condition \(Rf\leq(1+\sum y_i)^r\) with arbitrary scalar \(r\).

The functions in these six conditions have no displayed spatial variable. They are the spatially homogeneous specialization of (8.14). The proof below also works for measurable spatial dependence when all inequalities and Lipschitz constants are uniform in \(x\).

The follow-up sentences ask whether \(g\) can grow superlinearly, up to the scale of Assumption 8.4(3), where the local Lipschitz growth exponent for \(g\) is \((h-1)/2\), corresponding to growth of order \((h+1)/2\). These are additional questions, not assumptions in (1)–(6).

### Hypotheses required for the survey's actual solution framework

Problem 7 does not itself specify an initial-data function space or a definition of solution. Its pointwise condition on \(u_0\) only specifies positivity. It also does not repeat stochastic parabolicity. These omissions cannot be filled by declaring that an arbitrary nonnegative function is admissible.

Section 8.2 gives the following precise periodic framework (published pp. 96–100). Put

\[
 X_0=H^{-\delta,q}(\mathbb T^d;\mathbb R^\ell),\qquad
 X_1=H^{2-\delta,q}(\mathbb T^d;\mathbb R^\ell),\qquad w_\kappa(t)=t^\kappa.
\]

Assumption 8.4 has integers \(d\geq2\), \(\ell\geq1\), \(p,q\in[2,\infty)\), \(h>1\), \(\delta\in[1,2)\), and:

- Some \(\alpha>\delta-1\) satisfies \((b^j_{n,i})_n\in C^\alpha(\mathbb T^d;\ell^2)\) for every spatial coordinate and species.
- Uniform stochastic parabolicity is required. In the constant-diffusivity notation of (8.14), its mathematically operative form is
  \[
    2\nu_i|\xi|^2-\sum_n|b_{n,i}(x)\cdot\xi|^2\geq\mu|\xi|^2,
    \qquad \mu>0. \tag{P}
  \]
  Thus \(\nu_i>0\). Both survey PDF versions print the opposite inequality,
  \(\sum_{j,k,n}b^j_{n,i}b^k_{n,i}\xi_j\xi_k\geq(2\nu_i-\mu)|\xi|^2\).
  That line cannot supply parabolicity. The cited local paper's Assumption 2.1(3), PDF p. 7, states correctly that \(a_i-\frac12\sum_n b_{n,i}\otimes b_{n,i}\) is uniformly positive. All applications below use (P), explicitly, rather than the reversed printed sign.
- The measurable maps \(f_i\) and \(g_i=(g_{n,i})_n\) have bounded values at zero, and uniformly in \(x\),
  \[
  |f_i(x,y)-f_i(x,y')|\lesssim(1+|y|^{h-1}+|y'|^{h-1})|y-y'|,
  \]
  \[
  \|g_i(x,y)-g_i(x,y')\|_{\ell^2}
   \lesssim(1+|y|^{(h-1)/2}+|y'|^{(h-1)/2})|y-y'|.
  \]
  Their domains are vector valued in \(y\); occurrences of scalar \(\mathbb R\) in parts of the printed assumption are understood in the surrounding system notation.
- Either
  \[
  p>2,\quad \delta\in[1,(h+1)/h),\quad
  \frac{1+\kappa}{p}+\frac12\left(\delta+\frac dq\right)=\frac h{h-1},
  \quad \frac d{d-\delta}<q<\frac{d(h-1)}{h+1-\delta(h-1)}, \tag{A}
  \]
  with \(\kappa\in[0,p/2-1)\), or \(p=q=2,\ \kappa=0,\ \delta=1,\ h\leq1+4/d\), with the additional strict restriction \(h<3\) if \(d=2\).

The local theorem is Theorem 8.6, published p. 98. Its initial space is

\[
 u_0\in L^0_{\mathscr F_0}\bigl(\Omega;
 B^{d/q-2/(h-1)}_{q,p}(\mathbb T^d;\mathbb R^\ell)\bigr). \tag{I}
\]

There is no moment assumption in \(L^0\). For the Hilbert endpoint the trace space is \(L^2\), as follows from the actual interpolation trace \(B^{2-\delta-2(1+\kappa)/p}_{q,p}\); it equals the displayed critical exponent in (I) in case (A), but not when \(h<1+4/d\) in the Hilbert case. In the latter case the critical exponent in (I) is negative: that blanket display would enlarge the initial space beyond the \(L^2\) trace actually furnished by this Hilbert setting. The report does not use such an enlargement.

For clarity, the theorem below uses case (A), where there is no trace ambiguity. If necessary the polynomial upper bound can be increased from \(h\) to a larger \(\widetilde h\). This enlarges the range of available local parameters but changes the declared critical initial space. It does not change the equation. For example, for \(d\geq2\), \(\widetilde h>1+4/d\), one can choose \(q=d(\widetilde h-1)/2>2\), \(\delta>1\) sufficiently close to 1 with \(\delta-1<\gamma\), \(p\) sufficiently large, and \(\kappa=p(1-\delta/2)-1\). This includes nonnegative data in the critical Lebesgue space \(L^{d(\widetilde h-1)/2}\) when \(p\geq q\). Bounded nonnegative data are included. For \(d=1\), the survey uses a dummy periodic spatial variable, or the separate one-dimensional theory in the local paper, Section 6.

A \((p,\kappa,q,\delta)\)-solution means the \(L^p_\kappa\)-local strong solution of Definitions 4.5–4.6, published p. 42, with
\((Au)_i=-\nu_i\Delta u_i\), \((Bu)_i=((b_{n,i}\cdot\nabla)u_i)_n\), and \(F_i=f_i\), \(G_i=g_i\). It is progressively measurable, solves the integral equation in \(X_0\) with the given Brownian motions, and up to an exhausting sequence of stopping times has

\[
 u\in L^p(0,\tau,t^\kappa dt;X_1)\cap
 C([0,\tau];B^{d/q-2/(h-1)}_{q,p}).
\]

“Strong” here includes a strong integral identity and adaptation on the prescribed stochastic basis; it does not assert classical twice differentiable spatial sample paths. Uniqueness is pathwise in this local class; Proposition 8.8 identifies solutions constructed with different admissible parameters. Global means its maximal lifetime \(\sigma\) equals \(\infty\) almost surely, with these properties on every finite time interval. The local theory also gives, for every finite \(a>2\) and \(\theta\in(0,1)\),

\[
 u\in L^a_{\rm loc}((0,\sigma);H^{1,a})\cap
 C^{\theta/2,\theta}_{\rm loc}((0,\sigma)\times\mathbb T^d;\mathbb R^\ell).
 \tag{Reg}
\]

Nonnegativity at negative Besov smoothness is interpreted distributionally; for positive time it is pointwise by (Reg) and Proposition 8.10. One can avoid this interpretation by starting with nonnegative functions in one of the included Lebesgue spaces.

The torus imposes periodic boundary conditions. \(\mathbb R^d\) has no spatial boundary and would require a specified whole-space function-space realization. The phrase about additional boundary conditions in Problem 7 does not name Dirichlet, Neumann, mixed, or compatibility conditions. Section 8.2, p. 96, expressly restricts its detailed theory to periodic boundaries because stochastic maximal regularity with transport at a boundary is a separate issue. No arbitrary-boundary theorem is implicit in Theorem 8.6.

## 2. A periodic theorem

**Theorem.** Let \(d\geq2\), \(\ell\geq2\). Suppose (8.14) on \(\mathbb T^d\) has (P), bounded Hölder transport coefficients as above, and conditions (1)–(6), with (6) understood as the vector product (T). For any parameters in case (A), and any nonnegative initial datum (I), the unique maximal solution supplied by the local theory is global. It retains its local-theory regularity on every finite interval. There is no upper restriction on \(d\) or on the finite polynomial growth order \(h\), beyond selecting an admissible local setting. The same continuation argument applies to any already constructed positive Hilbert-endpoint local solution with (Reg). For \(d=1\) it applies after adding a dummy periodic variable, in the corresponding initial-data class.

For nonnegative smooth initial data, the estimates proved below are uniform in the data except through their specified energy. They imply the global continuous-dependence conclusion of Agresti–Veraar, global paper Theorem 5.2, PDF p. 35, when \(p\geq q\geq q_*:=\max\{d(h-1)/2,2\}\) and there exists an integer \(m\geq q_*\) with \(2-\delta-d/q>-d/m\). One then takes \(\zeta_0=m\) in that theorem. For example this includes the critical settings with \(h>3\), \(q=d(h-1)/2\), and \(\delta\) sufficiently close to 1. The proof of global existence and uniqueness itself does not require these extra continuity parameters.

### 2.1 Constructing an energy compatible with the triangular cone

Fix an integer \(m\geq2\). It is an energy exponent, unrelated to the temporal exponent \(p\). Write multi-indices \(\alpha\in\mathbb N_0^\ell\), \(|\alpha|=\sum_i\alpha_i\), \(y^\alpha=\prod_i y_i^{\alpha_i}\), \(\binom m\alpha=m!/\prod_i\alpha_i!\). All diagonal entries \(R_{ii}\) are strictly positive.

Let \(\vartheta>1\), to be chosen large enough below. Choose positive numbers \(t_i\) backwards:

\[
 t_\ell=1,\qquad
 t_i=\vartheta^{2(m-1)}
       \left(1+\sum_{j>i}\frac{R_{ji}}{R_{jj}}t_j\right),
 \quad i=\ell-1,\ldots,1.
 \tag{1}
\]

Set

\[
 c_\alpha=\vartheta^{\sum_i\alpha_i^2}\prod_i t_i^{\alpha_i},\qquad
 \Phi_m(y)=\sum_{|\alpha|=m}\binom m\alpha c_\alpha y^\alpha.
 \tag{2}
\]

On the nonnegative cone all coefficients are positive, and

\[
 a_m\left(\sum_i y_i\right)^m\leq\Phi_m(y)
 \leq A_m\left(\sum_i y_i\right)^m
 \tag{3}
\]

for some finite \(0<a_m\leq A_m\). Constants may grow very rapidly with \(m\); no limit \(m\to\infty\) will be taken.

For \(|\beta|=m-1\), put \(v_i=c_{\beta+e_i}\). Factoring out the common positive factor gives

\[
 v_i=\vartheta^{\sum_k\beta_k^2+1}t^\beta\,t_i\vartheta^{2\beta_i}.
\]

Since \(0\leq\beta_i\leq m-1\), (1) implies
\(v_i\geq\sum_{j>i}(R_{ji}/R_{jj})v_j\).
Solve \(R^T\eta=v\) backwards. If \(\eta_j\geq0\) for \(j>i\), then \(\eta_j\leq v_j/R_{jj}\), and consequently

\[
 \eta_i=\frac{v_i-\sum_{j>i}R_{ji}\eta_j}{R_{ii}}\geq0.
\]

This proves \(R^{-T}v\geq0\) for every such \(\beta\). Differentiating (2),

\[
 \nabla\Phi_m(y)=m\sum_{|\beta|=m-1}
       \binom{m-1}\beta y^\beta v_\beta
       =R^T\lambda(y),\qquad \lambda(y)\geq0.
 \tag{4}
\]

Therefore (T) gives

\[
 \nabla\Phi_m(y)\cdot f(y)
 \leq(1+\textstyle\sum_i y_i)\lambda(y)\cdot r
 \leq C_m(1+\Phi_m(y)),\qquad y\geq0.
 \tag{5}
\]

In the second inequality one can replace \(r\) by its positive part. Each component of \(\lambda\) is a fixed nonnegative homogeneous polynomial of degree \(m-1\), so (3) and \(s^{m-1}(1+s)\leq C(1+s^m)\) prove the bound. No sign of an individual \(f_i\) away from its boundary face is assumed. Mass condition (5) of the question is not separately needed by this argument; (T) is sufficient for the reaction estimate.

### 2.2 The Hessian and the leading transport correction

Put \(H(y)=D^2\Phi_m(y)\). For \(|\beta|=m-2\), define the symmetric matrix

\[
 (C_\beta)_{ij}=c_{\beta+e_i+e_j},\quad
 d_{\beta,i}=\sqrt{c_{\beta+2e_i}},\quad
 \rho=\vartheta^{-2}.
\]

A direct exponent calculation gives, whenever \(i\ne j\),

\[
 c_{\beta+e_i+e_j}
   =\rho\sqrt{c_{\beta+2e_i}c_{\beta+2e_j}}. \tag{6}
\]

Indeed the exponent \(\sum_k\alpha_k^2\) at the midpoint is two less than the average at the two endpoints; the powers of \(t\) cancel exactly. Thus

\[
 C_\beta=\operatorname{diag}(d_\beta)
     [(1-\rho)I+\rho\mathbf1\mathbf1^T]
     \operatorname{diag}(d_\beta),\qquad
 H(y)=m(m-1)\sum_{|\beta|=m-2}\binom{m-2}\beta y^\beta C_\beta.
 \tag{7}
\]

In particular \(H\) is positive semidefinite on the cone and has nonnegative entries. For every real vector \(z\),

\[
 (1-\rho)\sum_i H_{ii}z_i^2
 \leq z^T H z
 \leq[1+(\ell-1)\rho]\sum_i H_{ii}z_i^2. \tag{8}
\]

Let \(V=\max_i\nu_i\), \(B=\max_i\sup_x(\sum_n|b_{n,i}(x)|^2)^{1/2}\), and \(K=V+B^2/2\). These are finite. Choose \(\vartheta\) so large that

\[
 \rho K(\ell-1)\leq\mu/4. \tag{9}
\]

This chooses the energy after the coefficients, without any smallness assumption on the noise. For vectors \(z_i\in\mathbb R^d\), consider

\[
 Q_y(z)=\sum_{i,j}H_{ij}(y)
 \left[\frac{\nu_i+\nu_j}{2}z_i\cdot z_j
 -\frac12\sum_n(b_{n,i}\cdot z_i)(b_{n,j}\cdot z_j)\right].
 \tag{10}
\]

For each matrix \(C_\beta\) in (7), set \(a_i=d_{\beta,i}|z_i|\). By (P) the diagonal contribution to (10) is at least \((\mu/2)\sum_i a_i^2\). The absolute value of the off-diagonal contribution is at most
\(\rho K\sum_{i\ne j}a_i a_j\leq\rho K(\ell-1)\sum_i a_i^2\).
Multiply by the nonnegative weights in (7) and sum. It follows that

\[
 Q_y(z)\geq\frac\mu4\sum_i H_{ii}(y)|z_i|^2. \tag{11}
\]

This is the mixed-species estimate that cannot be obtained by merely citing componentwise parabolicity for an arbitrary Hessian. The Hessian in (2) was constructed for precisely this purpose. No derivative of \(b\) appears.

### 2.3 Zero-order noise and the full Itô formula

From global Lipschitz continuity and vanishing on the \(i\)-th face,

\[
 \|g_i(y)\|_{\ell^2}
 =\|g_i(y)-g_i(y_1,\ldots,0,\ldots,y_\ell)\|_{\ell^2}
 \leq L_i y_i \quad(y\geq0). \tag{12}
\]

Euler's identities, together with nonnegative Hessian coefficients, give

\[
 \sum_i H_{ii}(y)y_i^2\leq y^T H(y)y=m(m-1)\Phi_m(y). \tag{13}
\]

For \(\mathcal B_i=(b_{n,i}\cdot z_i)_n\), inequalities (8), (12), (13) yield

\[
 \sum_{i,j}H_{ij}\langle g_i,g_j\rangle\leq C_m\Phi_m(y),
\]
\[
 \left|\sum_{i,j}H_{ij}\langle\mathcal B_i,g_j\rangle\right|
 \leq C_m\left(\sum_i H_{ii}|z_i|^2\right)^{1/2}\Phi_m(y)^{1/2}.
 \tag{14}
\]

For the second line, use Cauchy–Schwarz for the positive semidefinite form \(H\), followed by (8); it is valid also for \(\ell^2\)-valued vectors by summing the scalar identity. Young's inequality absorbs this into \((\mu/8)\sum_i H_{ii}|z_i|^2+C_m\Phi_m\).

Fix a deterministic \(s>0\), on \(\{s<\sigma\}\), and work before a localizing stopping time. Set

\[
 E_m(t)=\int_{\mathbb T^d}\Phi_m(u(t,x))\,dx,\qquad
 D_m(t)=\int_{\mathbb T^d}\sum_i H_{ii}(u)|\nabla u_i|^2\,dx.
\]

Itô's formula, including the complete covariance between the two kinds of noise, reads

\[
 dE_m=\left[-\int Q_u(\nabla u)
       +\int\nabla\Phi_m(u)\cdot f(u)
       +\int\sum_{i,j}H_{ij}(u)\langle\mathcal B_i,g_j(u)\rangle
       +\frac12\int\sum_{i,j}H_{ij}(u)\langle g_i(u),g_j(u)\rangle\right]dt+dM_m,
 \tag{15}
\]

where every spatial integral is over the torus and

\[
 M_m(t)=\sum_n\int_s^t\int\sum_i\partial_i\Phi_m(u)
       [(b_{n,i}\cdot\nabla)u_i+g_{n,i}(u)]\,dx\,dW^n.
\]

By (5), (11), (14),

\[
 dE_m+cD_m\,dt\leq C_m(1+E_m)\,dt+dM_m,\qquad c=\mu/8>0.
 \tag{16}
\]

Here the finite volume of the torus is absorbed in \(C_m\).

There is no unproved classical-smoothness assumption in (15). On a compact subinterval of \((0,\sigma)\), (Reg) gives continuity and \(L^a(H^{1,a})\) regularity. Stop when the spatial supremum and the \(L^2(H^{1,2})\) integral exceed finite levels. Then \(f(u)\) and all polynomial derivatives on the range are bounded, and the noise is in \(L^2(\ell^2;L^2)\). Apply the variational Itô formula to a smooth function agreeing with \(\Phi_m\) on this range, or first apply spatial convolution to the variational equation. In the latter argument, \(J_\varepsilon(b\nabla u)\to b\nabla u\) in \(L^2\), without commuting \(J_\varepsilon\) through \(b\); the drift integration-by-parts terms converge in \(H^1\). Boundedness of the cut-off derivatives and strong \(H^1\)/noise convergence justify every term of (15). The extra stopping times exhaust the original lifetime by (Reg). Thus rough \(C^\gamma\) coefficients cause no derivative loss in this energy calculation.

### 2.4 A tail bound without an unjustified martingale absorption

Discarding the dissipation term in (16), \(e^{-C_m(t-s)}(1+E_m(t))\) is a nonnegative local supermartingale on each stopped interval. For \(\Gamma\in\mathscr F_s\), \(\Gamma\subseteq\{s<\sigma\}\), with \(E_m(s)\) bounded on \(\Gamma\), optional stopping at the first energy level \(A\), before any exhausting stopping time and before \(T\), gives

\[
 \mathbb P\left(\Gamma\cap
 \left\{\sup_{s\leq t<\sigma\wedge T} E_m(t)\geq A\right\}\right)
 \leq\frac{e^{C_m(T-s)}}{1+A}
       \mathbb E[\mathbf1_\Gamma(1+E_m(s))]. \tag{17}
\]

One can use a strict threshold or its limit to remove any distinction between an attained supremum and a supremum on a half-open interval. Pass through the exhausting stopping times first. Then let \(A\to\infty\). Finally take the union over \(\Gamma=\{s<\sigma,\ E_m(s)\leq k\}\), \(k\in\mathbb N\). Since (Reg) makes \(E_m(s)\) finite,

\[
 \sup_{s\leq t<\sigma\wedge T}\|u(t)\|_{L^m}<\infty
 \quad\text{almost surely on }\{s<\sigma\}. \tag{18}
\]

This avoids assuming an \(L^1\) bound on the time supremum, or incorrectly absorbing a BDG term with two incompatible small constants. It also avoids any moment assumption on \(u_0\).

Keeping \(D_m\) in (16), taking expectations at stopped times and applying Gronwall gives an expectation bound for its time integral in terms of \(1+\mathbb E E_m(s)\). Since \(H_{ii}(y)\geq c_m y_i^{m-2}\), this also controls \(\int\sum_i u_i^{m-2}|\nabla u_i|^2\). These are genuine energy estimates, not just formal bounds on reactions.

### 2.5 Closing the blow-up criterion and stability

Choose \(h_0>\max\{h,1+4/d\}\), \(q_0=d(h_0-1)/2\). Choose \(\delta_0>1\) sufficiently close to 1 that \(\delta_0-1<\gamma\), \(\delta_0<(h_0+1)/h_0\), and the strict \(q_0\) inequalities in (A) hold. This is possible because \(q_0>2\); at \(\delta_0=1\), \(d/(d-1)\leq2<q_0\), and the upper bound becomes \(d(h_0-1)/2=q_0\), which strictly increases when \(\delta_0\) increases. Take \(p_0\) large enough that
\(\kappa_0=p_0(1-\delta_0/2)-1\in[0,p_0/2-1)\).
The Lipschitz bound for \(g\) satisfies every larger polynomial upper-growth assumption.

Pick a finite integer \(m>q_0\). Theorem 8.9(1), published p. 100, states exactly

\[
 \mathbb P\left(s<\sigma<T,\
   \sup_{s\leq t<\sigma}\|u(t)\|_{L^m}<\infty\right)=0.
\]

Combining it with (18) gives \(\mathbb P(s<\sigma<T)=0\). A countable sequence \(s\downarrow0\), and then integer \(T\to\infty\), proves \(\sigma=\infty\) almost surely. Positivity and uniqueness are inherited from the local theory. This establishes the theorem.

For the stated continuous-dependence assertion, write \(q_*=\max\{d(h-1)/2,2\}\) and choose an integer \(m\geq q_*\) satisfying \(2-\delta-d/q>-d/m\), as required by the global paper's Assumption 5.1. Apply (16) to both \(\Phi_2\) and \(\Phi_m\). Their sum controls \(\|u\|_{L^{q_*}}^{q_*}\) on the finite-volume domain and, since \(y^{q_*-2}\leq1+y^{m-2}\), the corresponding \(q_*\)-gradient integral. Equations (17) and the expectation dissipation bound verify that Assumption 5.1 with \(\zeta_0=m\), uniformly for nonnegative smooth initial data. Its Theorem 5.2 then supplies convergence in probability in \(C([0,T];B^{d/q-2/(h-1)}_{q,p})\) under the parameter restrictions stated above. This use of the published stability theorem does not assume diagonal coercivity of the reactions.

## 3. Verification

- Independently re-fetched all four supplied source URLs. Each PDF SHA-256 matches its supplied header exactly, including both the publisher survey and arXiv v5. Results are in `data/supplied_source_verification.json`. PDFs were held in memory only.
- Saved page-marked plain text for both Milesis–Salins versions, both Agresti–Veraar transport papers, the delayed-blow-up paper, and the additional comparison papers. `data/retrievals.jsonl` records URLs and fingerprints. The first pypdf extraction was replaced with `pdftotext -layout` for readable formulas; the later fingerprint entries record the retained extraction.
- Re-derived the polynomial first and second derivatives directly from multinomial coefficients, and separately from the Hessian decomposition (7). The two-species quadratic case provides a simple independent sign check: for \(R=\left(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\right)\), \(\Phi=A u_1^2+2B u_1u_2+C u_2^2\), with \(A\geq B\geq C>0\),
  \[
  \nabla\Phi\cdot f=2[(A-B)u_1+(B-C)u_2]f_1
             +2[Bu_1+Cu_2](f_1+f_2).
  \]
  Taking \(B/\sqrt{AC}\) small controls unequal leading coefficients. Formula (2) realizes the same mechanism in every degree and number of species.
- `python3 code/check_energy.py` passed 417 exact rational checks in four cases \((\ell,m)=(2,2),(2,5),(3,4),(4,6)\): cone membership, the squared identity (6), direct Hessian coefficients, both Euler identities, boundary values, and evaluations of the complete leading Itô form with unequal transport coefficients. Results are in `data/energy_checks.json`. These finite checks detect algebra mistakes; the arbitrary-parameter proof is the displayed argument, not the computation.
- Audited separately the covariance cross term, the optional-stopping tail bound, the countable passage from positive time to time zero, and the strict exponent \(m>q_0\) in Theorem 8.9(1). No \(m\to\infty\) estimate, unproved stochastic duality lemma, or small-noise assumption is used.
- No simulations, subagents, publication, or pushes were used. Extraction/checking was single-process or at most three concurrent small retrieval processes, with inherited nice 20. The entire working directory is a few megabytes. No PDF, image, or scan was retained in it.

## 4. Literature comparison

The search and reading preceded the proof draft. References were checked by title and mathematical statement: the published survey's numerical citations near Problem 7 are shifted in several places. For example its [213] is Pisier, whereas v5 correctly cites Pierre; its [200,201] should refer to Morgan's 1989/1990 papers, whereas published [201] is Neelima–Šiška. The matching bibliography entries are [199,200] for Morgan and [212] for Pierre. These numerical slips do not change (T).

### 4.1 The transport-noise results cited by the survey

| Source | Exact result and location in the saved version | Scope relative to Problem 7 |
|---|---|---|
| [Agresti–Veraar, local theory](https://arxiv.org/pdf/2209.14759v2) | Assumption 2.1, p. 7; Definition 2.3, p. 8; Theorem 2.7, p. 10; Theorem 2.10, pp. 11–12; Theorem 2.13, p. 13 | Periodic transport SPDEs; critical Besov local existence, blow-up criteria, positivity. No general triangular global theorem. The survey refers to some of these with earlier theorem numbers. |
| [Agresti–Veraar, global theory](https://arxiv.org/pdf/2301.06897v4) | Assumption 3.1 and Theorem 3.2, p. 10 | All dimensions with an additional \(L^\zeta\)-coercivity inequality, \(\zeta\geq\max\{d(h-1)/2,2\}\). |
| Same | Assumption 4.4, pp. 23–24; Theorem 4.5, p. 24 | Predator–prey: \(d\leq4\), \(h=2\), nonnegative \(L^2\) data, transport allowed, special noise bounds. |
| Same | Assumption 4.8, pp. 26–27; Theorem 4.9, p. 27 | Brusselator: \(d=1,2\), cubic reactions, specified coefficient/noise bounds, \(L^q\) data for its stated \(q>2\). |
| Same | Assumption 4.10 and Theorem 4.11, pp. 29–30 | Brusselator: \(d=3\), cubic reactions, nonnegative \(L^3\) data, additional noise bounds. |
| Same | Example 4.12, p. 34 | Gray–Scott is a special case of those Brusselator results. |

These give maximal-regularity strong solutions, rather than only martingale solutions. None covers arbitrary triangular reactions. Their Section 1.4, p. 6, explicitly identifies that gap. In the survey, the corresponding coercive theorem is 8.15, p. 102. Theorem 8.18, p. 104, treats its displayed predator–prey model in \(d\leq4\) with \(L^2\) data; transport is omitted in that particular presentation.

Here are the additional algebraic assumptions, to make the comparison explicit. In the global paper write \(\lambda_i>0\) for its ellipticity margin (called \(\nu_i\) there), choose \(0<\varepsilon<\min_i\lambda_i\), and set
\[
 \mathcal A_i(y)=\tfrac12\|g_i(y)\|_{\ell^2}^2+
 \frac{(\sum_n|b_{n,i}|\,|g_{n,i}(y)|)^2}{4(\lambda_i-\varepsilon)}.
\]
For predator–prey,
\[
 f_1=\lambda_1' y_1-\chi_{11}y_1^2-\chi_{12}y_1y_2,
 \qquad f_2=\lambda_2' y_2-\chi_{22}y_2^2+\chi_{21}y_1y_2,
\]
with bounded coefficients, \(\chi_{ij}\geq0\), and Assumption 4.4 requires \(\mathcal A_i\leq N_i\), where
\[
 N_1=M(1+y_1^2)+\chi_{11}y_1^3+\chi_{12}y_1^2y_2,
\quad
 N_2=M[1+(1+y_1)y_2^2+y_1^2y_2+y_1^3]+\chi_{22}y_2^3.
\]
For Brusselator, (4.18) has
\[
 f_1=-y_1y_2^2+\alpha_1y_1+\alpha_2y_2+\alpha_0,
\qquad f_2=y_1y_2^2+\beta_1y_1+\beta_2y_2+\beta_0.
\]
In \(d\leq2\) its noise bounds are
\[
 N_1=M(1+y_1^2)+(1-\varepsilon)y_1^2y_2^2,
\qquad N_2=M[1+(1+y_1^2)y_2^2+|y_1||y_2|^3+y_1^4];
\]
in \(d=3\) replace the coefficient \(1-\varepsilon\) by \(1/5\). In three dimensions positivity also requires \(\alpha_2,\alpha_0,\beta_1,\beta_0\geq0\). Theorem 4.11 uses \(\delta\in(1,4/3]\), \(p\geq\max\{3,2/(2-\delta)\}\), \(q=3\), \(\kappa_0=p(1-\delta/2)-1\). Theorem 4.9 uses \(\delta\in(1,2)\), \(2<q<2/(2-\delta)\), \(p\geq2/(2-\delta)\), with the same \(\kappa_0\).

Some displayed face-vanishing identities in Section 4 interchange the two coordinate faces (also in the survey's Assumption 8.17). The face condition needed for positivity is exactly \(g_1(0,y_2)=g_2(y_1,0)=0\), as correctly stated in the global paper's introductory Theorem 1.2 and in Problem 7 itself. The new proof uses Problem 7's unambiguous condition. These special-model results allow selected superlinear \(g\) under the displayed bounds; they do not permit every noise with the local-theory growth order.

The relevant mass-control result is [Agresti, delayed blow-up](https://arxiv.org/pdf/2207.08293), Theorems 3.5 and 3.6, PDF pp. 12–13. For prescribed \(T,N,\varepsilon\), Theorem 3.5 **chooses** a transport spectrum and intensity giving \(\mathbb P(\tau\geq T)>1-\varepsilon\). Theorem 3.6 adds exponentially decreasing mass and gives \(\mathbb P(\tau=\infty)>1-\varepsilon\), again for a selected noise. These quantifiers do not give almost sure global existence for every fixed admissible transport coefficient. Its noise is a special divergence-free Stratonovich transport construction. The published article is SPDE: Analysis and Computations 12 (2024), 1907–1981; the page locators here refer to the saved arXiv PDF.

### 4.2 Milesis–Salins, both versions

The [arXiv version history](https://arxiv.org/abs/2604.06645) lists exactly two versions as checked on 13 November 2026. Both were obtained and their assumptions, auxiliary estimates and main proofs inspected.

| Version | Two species | General finite number of species | Assumptions |
|---|---|---|---|
| [v1, 8 April 2026](https://arxiv.org/pdf/2604.06645v1), 37 pages | Theorem 5.1, p. 23; proof pp. 23–30 | Theorem 6.1, p. 31; proof pp. 31–33 | Assumptions 0–11, pp. 8–11; general triangular matrix in Remark 1, p. 9 |
| [v2, 26 May 2026](https://arxiv.org/pdf/2604.06645v2), 38 pages | Theorem 5.1, p. 29; proof pp. 29–31 | Theorem 5.2, p. 31; proof pp. 31–34 | Assumptions 0–11, pp. 9–12; Remark 1, p. 10 |

Their equation is
\[
 \partial_t u_i-d_i\Delta u_i
 =f_i(u)+\sum_{k=1}^{N}\sigma_{ik}(u)\dot W_k,
 \quad d_i>0,
\]
on a smooth bounded \(D\subset\mathbb R^d\), with homogeneous Dirichlet or Neumann conditions. There is no \(b\cdot\nabla u\) term.

| Hypothesis | Problem 7 | Milesis–Salins |
|---|---|---|
| Initial data | Positivity; precise periodic trace space supplied by Section 8.2 | Nonnegative \(L^\infty(D)\) data |
| Reaction | Polynomial Lipschitz bound of order \(h\) | Local Lipschitz; \(|f_i(a)|\leq C(1+\sum_j a_j^\mu)\), any finite \(\mu>0\) |
| Triangular control | \(Rf\leq(1+\sum a_i)r\) | Same linear control: partial sums in Assumption 3, general \(R\) in Remark 1 |
| Zero-order noise | \(g_i:\mathbb R^\ell\to\ell^2\), globally Lipschitz, vanishes on its face | \(\sigma_{ik}\) locally Lipschitz, face vanishing, \(|\sigma_{ik}(a)|\leq C(1+\sum a_j)\) |
| Spatial covariance | Pointwise square-summable coefficients; also derivative noise | Gaussian white-in-time fields with kernels \(L_k\); no derivative noise |
| Dimension | No bound in the question | Any \(d\), subject to the kernel conditions below; white noise in space allowed in \(d=1\) |
| Solution | Prescribed-basis maximal-regularity local strong solution | Unique global heat-kernel mild solution; nonexplosion of the supremum-norm truncation lifetime |

For every \(i,k\), their noise assumptions require \(L_k\) symmetric positive definite and pointwise nonnegative, together with
\[
 \sup_{x,y}G_i(t,x,y)\leq Ct^{-d/2},\qquad
 \sup_x\iint G_i(t,x,y_1)G_i(t,x,y_2)L_k(y_1,y_2)\,dy_1dy_2
 \leq Ct^{-\eta},\quad 0<\eta<1,
\]
\[
 \sup_{y_1}\int_D L_k(y_1,y_2)\,dy_2<\infty.
\]
These allow suitably coloured non-trace-class noise. Space-time white noise has \(\eta=d/2\), explaining the one-dimensional restriction for that case. Likewise a Riesz kernel \(|y_1-y_2|^{-\beta}\) requires \(\beta<2\) as well as \(\beta<d\); their example's displayed \(\beta<d\) does not remove Assumption 10.

The asserted estimate is \(\sup_n\mathbb E\sup_{t\leq T,x,i}|u_{i,n}(t,x)|^p<\infty\). Their proof subtracts the stochastic convolution, uses Pierre's deterministic duality estimate on the remainder, absorbs its \(L^p\) norm on a short interval, and obtains global mild nonexplosion. The v2 organization separates Lemmas 5–6 before Theorem 5.1; no transport operator is added. Thus this is a substantial partial answer in a different noise/domain/data regime, not RESOLVED_IN_LITERATURE for Problem 7.

### 4.3 Other 2025–2026 candidates

[Agresti–Germ–Veraar, arXiv:2606.07417v3](https://arxiv.org/pdf/2606.07417v3), re-fetched and matched to the supplied text, has Theorem 2.9 (local existence), p. 13; Theorem 2.12 (regularization), p. 15; Theorem 2.20 and Corollary 2.21 (blow-up), p. 17; Theorem 2.24 (positivity), p. 19. Its general forcing is multiplicative Nemytskii coloured noise, not transport noise. Example 3.4, p. 22, explicitly cites Milesis–Salins for triangular global results; it does not prove a new global triangular theorem. Corollary 3.14, p. 26, is a separate scalar, one-dimensional white-noise result with \(|f(y)|=O(|y|\log|y|)\), \(g(y)=o(|y|(\log|y|)^{1/4})\), not the polynomial triangular system. The supplied `reaction_2026.txt` is v2, not v1; both supplied versions were checked, with v3 used for the current theorem numbering.

[Blessing–Seitz–Sonner–Tang, arXiv:2502.01209](https://arxiv.org/pdf/2502.01209), Theorem 4.10, PDF p. 24, concerns a scalar dissipative equation, with additive coloured noise, on a bounded Dirichlet domain. Conditions (F1)–(F2), pp. 18–19, include dissipativity and a dimension-dependent subcritical reaction order. It is not a triangular transport theorem.

[Földes–Stacy, arXiv:2601.19145](https://arxiv.org/pdf/2601.19145), Theorem 6.31, PDF pp. 47–48, gives global positive mild solutions under its SPDE Assumptions 1–3. Assumption 2, p. 40, bounds the positive parts of the component reactions by linear expressions. Assumption 3, pp. 40–41, has Nemytskii noise with bounded derivative and a spectral colouring condition. It neither includes a transport derivative nor replaces those componentwise positive-part bounds by arbitrary triangular cancellation.

Searches through 13 November 2026 combined the survey title/identifier, “Problem 7”, “triangular”, “mass control”, “transport noise”, and the names Pierre, Morgan, Fellner–Morgan–Tang and Souplet; polynomial-Lyapunov variants were also searched. The relevant stochastic matches above were read from primary-source full texts. No exact resolution was found. This is a dated search result, not a claim that an indexed search proves nonexistence of a paper.

### 4.4 Deterministic comparison and an access limitation

[Fellner–Morgan–Tang](https://imsc.uni-graz.at/fellnerk/preprints/Classical.pdf), Theorem 1.1, author PDF p. 2, proves global classical solutions on smooth bounded domains in arbitrary dimension under quasi-positivity, mass control and growth \(|f|\leq C(1+|u|^{2+\varepsilon})\), for sufficiently small \(\varepsilon>0\). The initial data are bounded and nonnegative, with homogeneous Neumann conditions (Dirichlet in Remark 1.1(ii)). The published article is Ann. IHP C 37 (2020), 281–307. This theorem is deterministic and has a different growth restriction; triangular control is not its assumption.

[Souplet, arXiv:1804.05193](https://arxiv.org/pdf/1804.05193), the main **Theorem** on PDF p. 3 (called Theorem 1 later in its text), covers a smooth bounded Neumann domain or \(\mathbb R^d\), in any dimension. It assumes bounded nonnegative data, mass dissipation, entropy dissipation \(\sum_i f_i(u)\log u_i\leq0\), and \(|\nabla f_i(u)|\leq C(1+|u|)\); see (2)–(9), pp. 1–2. It is deterministic and uses entropy absent from Problem 7.

The deterministic triangular antecedents are [Morgan 1989](https://doi.org/10.1137/0520075), 1128–1144, [Morgan 1990](https://doi.org/10.1137/0521064), 1172–1189, and [Pierre's survey](https://doi.org/10.1007/s00032-010-0133-4), 417–455, Theorem 3.5. Pierre's duality estimate is reproduced as Milesis–Salins v1 Lemma 3, PDF p. 20, and v2 Lemma 4, PDF p. 20, with its complete inequality and boundary hypotheses. Those reproductions were read. The original Pierre author link now returns 404, the publisher supplies only its landing page, and the HAL/ISTEX and CiteSeer links did not yield the PDF. The original Morgan full texts were not obtained either. Accordingly, this report does **not** invent original theorem-page locators for these older papers or claim to have audited their full proofs. Their role here is contextual; neither the new proof nor the stochastic literature classification depends on an unchecked theorem from them. This is the remaining limitation of the requested original-source literature audit.

## 5. Limits of the result

On \(\mathbb R^d\), a spatially homogeneous nonzero \(f(0)\) need not preserve an unweighted finite-\(L^q\) space even for a constant forcing and zero initial data. A whole-space statement must specify its data and behavior at infinity. This is not a blow-up counterexample. If \(f(0)=0\), the same algebra gives \(\nabla\Phi_m\cdot f\leq C\Phi_m\), by local Lipschitz continuity near zero and (T) for large \(y\); the formal infinite-volume energy estimate is then integrable for finite-\(L^m\) solutions. That observation alone is not a completed whole-space local/continuation theorem, and none is claimed here.

For superlinear \(g\), estimate (12) fails. The Hessian trace then has growth exceeding \(m\), and (16) no longer closes from triangular control alone. Special dissipative examples in the literature permit superlinear noise; that does not establish the general follow-up question.

At a physical boundary, the energy calculation requires valid boundary cancellations and a positive local solution theory for the corresponding transport operator. These are additional analytic hypotheses, not consequences of the six pointwise reaction/noise conditions.
