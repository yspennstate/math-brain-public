# Excluding ground states in the normal sector of the known state

Let \(\mathfrak A\) be the quasi-local algebra of a finite-dimensional spin chain. Write
\[
 D(A)=[H,A],\qquad
 \left.\frac{d}{dt}\alpha_t(A)\right|_{t=0}=iD(A).
\]
For a bounded nearest-neighbor interaction, \(D(A)\) is a finite sum when \(A\) is local, and \(\alpha_t\) denotes the infinite-volume dynamics. An algebraic ground state is a state \(\theta\) satisfying
\[
 \theta(B^*D(B))\geq0\quad\text{for every local }B.                 \tag{1}
\]

Assume a ground state \(\omega\) satisfies, for some \(\gamma>0\),
\[
 \omega(A^*D(A))\geq
 \gamma\{\omega(A^*A)-|\omega(A)|^2\}
 \quad\text{for every local }A.                                  \tag{2}
\]
For the spin-1 Heisenberg application, (2) is an external premise: Hal Tasaki, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, [arXiv:2610.34330v2, Theorem 2.1, equation (2.12)](https://arxiv.org/html/2610.34330v2). Its numerical premises are not verified here. No explicit value of \(\gamma\) is needed below.

Let \((\pi,\mathcal H,\Omega)\) be the GNS representation of \(\omega\). A state \(\rho\) will be called normal in this representation if there is a positive trace-class operator \(T\) on \(\mathcal H\), with \(\operatorname{Tr}T=1\), such that
\[
 \rho(A)=\operatorname{Tr}(T\pi(A)),\qquad A\in\mathfrak A.         \tag{3}
\]
This is the usual normal folium of the representation. The operator \(T\) need not be unique.

**Proposition.** Under (2), every algebraic ground state satisfying (3) equals \(\omega\). In particular, if \(C\) is local and \(q=\omega(C^*C)>0\), then
\[
 \omega_C(A)=q^{-1}\omega(C^*AC)                                  \tag{4}
\]
can be a ground state only when it equals \(\omega\). The same conclusion holds for finite mixtures of states (4), and for limits of these mixtures in the norm of state functionals.

The proposition is a deduction from the local gap premise. It does not assert that an arbitrary Heisenberg ground state satisfies (3). No literature priority is claimed for this general consequence of ground-state spectral theory.

## 1. Ground-state dynamics and its sign convention

The finite-range dynamics has infinitesimal generator \(iD\). The following details justify the use of its ground-state implementer. Suppose each bond term has norm at most \(J\), and \(A\) is supported on an interval of \(\ell\) sites. Each commutator increases the containing interval by at most one site at each end. At the \(k\)-th step at most \(\ell+2k+1\) bonds meet it. Using \(\|[h,X]\|\leq2\|h\|\|X\|\) gives
\[
 \|D^n(A)\|\leq (2J)^n
 \prod_{k=0}^{n-1}(\ell+2k+1)\|A\|
 \leq(4J)^n\frac{(n+\ell)!}{\ell!}\|A\|.                         \tag{5}
\]
Consequently local observables are analytic for this dynamics for \(|t|<1/(4J)\): the norm series \(\sum_n(it)^nD^n(A)/n!\) converges there. This also follows directly from finite-volume dynamics: the bound (5) is uniform in the volume, and each fixed coefficient stabilizes once the interval contains the support of \(D^n(A)\). Its norm limit is \(\alpha_t(A)\).

For any ground state \(\theta\), apply (1) to \(1+zB\), where \(B\) is local and \(z\in\mathbb C\). The resulting expression is
\[
 z\theta(D(B))+|z|^2\theta(B^*D(B)).                              \tag{6}
\]
It must be real and nonnegative for every \(z\). Taking arbitrarily small \(z\) in all complex directions forces \(\theta(D(B))=0\). Since \(D^{n-1}(B)\) is local, this also gives \(\theta(D^n(B))=0\) for every \(n\geq1\). The analytic series and continuity yield \(\theta\circ\alpha_t=\theta\) for \(|t|<1/(4J)\), first on local observables and then on \(\mathfrak A\). The group law extends invariance to every real \(t\).

In the GNS representation of \(\theta\), invariance defines a strongly continuous unitary group by
\[
 V_t\pi_\theta(A)\Omega_\theta
   =\pi_\theta(\alpha_t(A))\Omega_\theta.
\]
It is isometric because \(\theta\) is invariant, is onto because \(\alpha_t\) is invertible, and is strongly continuous by norm continuity of \(\alpha_t(A)\). Write \(V_t=e^{itK_\theta}\). Then
\[
 K_\theta\Omega_\theta=0,\qquad
 K_\theta\pi_\theta(A)\Omega_\theta
   =\pi_\theta(D(A))\Omega_\theta                              \tag{7}
\]
for local \(A\). These local vectors are a dense invariant domain for the restriction of \(K_\theta\), and (5) makes every such vector analytic. The analytic-vector essential-self-adjointness theorem therefore makes this domain a core for \(K_\theta\). Condition (1) says the quadratic form of \(K_\theta\) is nonnegative on that core. Graph-norm approximation extends it to the full operator domain, so the spectral theorem gives \(K_\theta\geq0\).

For \(\theta=\omega\), apply the same core argument to (2). It yields
\[
 K:=K_\omega\geq\gamma(1-P_\Omega),\qquad
 \ker K=\mathbb C\Omega,\qquad
 P_\Omega=|\Omega\rangle\langle\Omega|.                          \tag{8}
\]
Indeed, (2) is exactly this quadratic-form inequality on local vectors; both sides converge under graph-norm approximation. If \(K\psi=0\), the inequality forces \((1-P_\Omega)\psi=0\). The reverse inclusion follows from (7).

## 2. Negative-frequency averages vanish in every ground state

Choose \(F\in C_c^\infty(( -\infty,0))\), and let
\[
 f(t)=\frac1{2\pi}\int_{\mathbb R}F(s)e^{-its}\,ds,
 \qquad F(s)=\int_{\mathbb R}f(t)e^{its}\,dt.
\]
The function \(f\) is Schwartz and hence integrable. For \(A\in\mathfrak A\), define the norm-convergent integral
\[
 A_f=\int_{\mathbb R}f(t)\alpha_t(A)\,dt\in\mathfrak A.           \tag{9}
\]
In the GNS representation of any ground state \(\theta\), covariance and \(V_t\Omega_\theta=\Omega_\theta\) give
\[
 \pi_\theta(A_f)\Omega_\theta
  =\int f(t)e^{itK_\theta}\pi_\theta(A)\Omega_\theta\,dt
  =F(K_\theta)\pi_\theta(A)\Omega_\theta=0.                     \tag{10}
\]
The last equality uses \(K_\theta\geq0\) and the strictly negative support of \(F\). Thus
\[
 \theta(A_f^*A_f)=0.                                            \tag{11}
\]
Although \(A_f\) need not be local, (11) follows from (1) through the implementing group; no commutator involving \(A_f\) is required.

## 3. Normality forces support at zero energy

Let \(\rho\) be a ground state of the form (3). Decompose its trace-class operator as
\[
 T=\sum_j\lambda_j|\psi_j\rangle\langle\psi_j|,
 \qquad\lambda_j>0,\quad\sum_j\lambda_j=1,
\]
where the \(\psi_j\) are unit vectors; zero eigenvalues are omitted. Apply (11) to \(\rho\). Positivity of every summand gives
\[
 0=\sum_j\lambda_j\|\pi(A_f)\psi_j\|^2,
 \qquad \pi(A_f)\psi_j=0\quad\text{for every }j.                 \tag{12}
\]
This holds for every \(A\) and every choice of negative-frequency \(F\).

Take the matrix element of (12) against \(\Omega\). Inner products are linear in their second argument. Since \(K\Omega=0\), covariance gives
\[
 \begin{aligned}
 0&=\langle\Omega,\pi(A_f)\psi_j\rangle\\
  &=\int f(t)\langle\Omega,e^{itK}\pi(A)e^{-itK}\psi_j\rangle\,dt\\
  &=\langle\Omega,\pi(A)F(-K)\psi_j\rangle.
 \end{aligned}                                                   \tag{13}
\]
The vectors \(\pi(A)^*\Omega\), as \(A\) varies, form a dense set by cyclicity of the GNS vector. Equation (13) therefore implies
\[
 F(-K)\psi_j=0.                                                  \tag{14}
\]
To make the spectral conclusion explicit, for each integer \(n\geq2\) choose a nonnegative smooth function \(F_n\) compactly supported in \((-2n,-1/(2n))\), positive on \([-n,-1/n]\). If \(\mu_j\) is the spectral measure of \(K\) in \(\psi_j\), (14) gives
\[
 0=\|F_n(-K)\psi_j\|^2
   =\int|F_n(-E)|^2\,d\mu_j(E).
\]
Hence \(\mu_j([1/n,n])=0\). These intervals cover \((0,\infty)\). Since \(K\geq0\), the measure is supported at zero, so \(\psi_j\in\ker K\). By (8), every \(\psi_j\) is proportional to \(\Omega\). Consequently \(T=P_\Omega\) and \(\rho=\omega\). This proves the main assertion. In fact this part only needs a nonnegative implementer with one-dimensional kernel; the positive gap is a sufficient premise for that property.

## 4. Local filters, mixtures and norm limits

For a local \(C\) with \(q>0\), the vector
\(\psi_C=q^{-1/2}\pi(C)\Omega\) represents (4). Taking
\(T=|\psi_C\rangle\langle\psi_C|\) proves normality. A finite convex mixture is represented by the corresponding finite convex mixture of these positive trace-class operators.

For completeness, normal states in this representation are closed under convergence in the norm of functionals on \(\mathfrak A\). Put \(M=\pi(\mathfrak A)''\). Restriction from the predual \(M_*\) to \(\mathfrak A^*\) is isometric: Kaplansky density approximates the unit ball of \(M\) by the unit ball of \(\pi(\mathfrak A)\) in the strong-* topology, and bounded strong-* convergence implies convergence against every normal functional. Thus both unit balls give the same supremum defining its functional norm. The predual is a Banach space, so its isometric image is norm closed. A norm limit of normal states consequently is the restriction of a normal state on \(M\); positivity and normalization pass to the limit, using the same density. In a concrete representation every positive normal functional is a sum of vector functionals, equivalently has a positive trace-class realization (3). The proposition therefore applies to these limits.

The converse description is useful too. Every state (3) is a norm limit of finite mixtures of local filtered states. Truncate the spectral decomposition of \(T\) and renormalize its positive eigenvalues; the trace-norm error tends to zero. For each retained vector \(\psi_j\), cyclicity and norm density of local observables give local \(C_{j,k}\) with \(\pi(C_{j,k})\Omega\to\psi_j\). Normalize these nonzero vectors. Their vector functionals converge in norm, since for unit vectors \(v,w\),
\[
 \sup_{\|A\|\leq1}
 |\langle v,\pi(A)v\rangle-\langle w,\pi(A)w\rangle|
 \leq2\|v-w\|.
\]
The finite mixtures converge as well. Thus the class excluded is exactly the normal folium, described in terms of local filters and norm limits, whenever the resulting state is a ground state.

## 5. Independent unitary check and a quantitative witness

For a local unitary \(U\), set
\[
 \rho_U(A)=\omega(U^*AU),\qquad E_U=\omega(U^*D(U)).
\]
Testing (2) with \(U\) gives
\[
 E_U\geq\gamma(1-|\omega(U)|^2).                                \tag{15}
\]
The inverse unitary supplies a direct test in \(\rho_U\). By the Leibniz rule, \(D(U^*)U=-U^*D(U)\). Therefore
\[
 \rho_U\bigl((U^*)^*D(U^*)\bigr)
 =\omega(D(U^*)U)=-E_U.                                         \tag{16}
\]
If \(\rho_U\) is a ground state, (16) gives \(E_U\leq0\), whereas (15) gives \(E_U\geq0\). It follows that \(|\omega(U)|=1\). The unit vectors \(\pi(U)\Omega\) and \(\Omega\) are then proportional by equality in Cauchy–Schwarz, so \(\rho_U=\omega\). This argument does not use frequency averages or normal-state decomposition.

There is also a quantitative conclusion. For a finite block \(I\), let
\(d_I=\|(\rho_U)_I-\omega_I\|_1\), with no factor \(1/2\). The difference of the rank-one projections onto \(\pi(U)\Omega\) and \(\Omega\) has trace norm
\(2\sqrt{1-|\omega(U)|^2}\). To verify this number, multiply one vector by a phase so that its overlap with the other is \(q\geq0\); in their two-dimensional span the projection difference has trace zero and eigenvalues \(\pm\sqrt{1-q^2}\). If \(q=1\), the difference is zero. Restriction to a block cannot increase the norm of a functional, and hence
\[
 d_I\leq2\sqrt{1-|\omega(U)|^2},\qquad
 E_U\geq\frac\gamma4 d_I^2.                                    \tag{17}
\]
Equations (16)–(17) give an explicit violation of local stability whenever a unitary defect changes a block marginal. In particular, \(d_I\geq\varepsilon\) implies a local test of norm one with expectation at most \(-\gamma\varepsilon^2/4\).

## 6. Scope and failure of a stronger inference

Normality is essential to the argument at (12). Local, or weak-*, limits of normal states need not be normal. This can be checked without a Hamiltonian. In the GNS representation of the all-zero product state on a two-level chain, let \(U_N\) flip all sites in \([-N,N]\). Each corresponding vector state is a local unitary perturbation and therefore normal. For every fixed local observable these states eventually agree with the all-one product state, so they converge weak-* to that state.

The all-one state is not normal in the all-zero representation. Let \(Q_N\) project onto all-one spins in \([-N,N]\). On every vector with excitations confined to a finite set, \(Q_N\) is eventually zero. Such vectors have dense span in this GNS Hilbert space, and \(\|Q_N\|=1\), so \(\pi(Q_N)\to0\) strongly. For any positive trace-class \(T=\sum_j\lambda_j|\psi_j\rangle\langle\psi_j|\), dominated convergence in the summable series gives \(\operatorname{Tr}(T\pi(Q_N))\to0\). The all-one product state instead assigns value one to every \(Q_N\), proving the assertion.

This example is not a Heisenberg competing ground state. It shows exactly why extending the proposition from norm limits to arbitrary local limits would be invalid. The round 3 density theorem controls fixed-block translates in average, and does not provide normality. The present proposition excludes local filtered defects and their normal closure; unrestricted uniqueness still requires exclusion of ground states outside this folium.
