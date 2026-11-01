# P0331 — source verification and rigorous partial results

Date: 2026-10-12. This is not a solution of the Debye-scale sharpness conjecture.

The user's requested second serious attempt is fully recorded in [SECOND_ATTEMPT.md](SECOND_ATTEMPT.md). It adds a proved spatial entropy localization theorem, explicit growing Poisson windows for most original-model bulk cells, a uniform-center periodic special case, and an actual corrected local-energy lower bound. The full verdict remains PARTIAL; see that file's Sections 6–7 for the updated gap and conditional Debye–Hückel reduction.

## 1. Exact source and scope

Sylvia Serfaty, *Lectures on Coulomb and Riesz gases*, arXiv:2407.21194, downloaded in `source.raw`; extracted text in `source.txt`. PDF pages 163–164 state

\[
 |\log E_{Q_\beta(U,\mu)}\exp(\beta F_{\square_R}/2)|
 \le C\beta\chi(\beta)R^d,\qquad
 \rho_\beta=C\max(1,\sqrt{\chi(\beta)/\beta}).
\]

Equation (5.2.27), PDF page 108, gives chi=1 for s>0 or beta>=1, and chi=1+beta^{s/(d-s)}|log beta| for s<=0 and beta<=1. Thus in the Coulomb case s=d-2: chi=1 in d>=3, chi=1+|log beta| in d=2 at beta<=1, and chi=1+beta^{-1/2}|log beta| in the one-dimensional Coulomb case. The latter is not the one-dimensional logarithmic gas.

The conjecture, verbatim from PDF page 164:

> We conjecture that this lengthscale is sharp and that (8.0.1) is optimal, in particular that local laws do not hold below ρβ because particle numbers behave in a Poissonian way below that scale.

No topology for Poissonian behavior or joint limiting regime is specified there. It is inappropriate to silently turn this into a claim of exactly Poisson counts at fixed positive temperature.

The rigorous local-law statement is Theorem 8.2, PDF pages 169–170. It assumes d>=1, s=d-2, a bounded nonnegative background density of integer mass N on U, bounded piecewise C1 boundary, and a lower bound mu>=m>0 on Lambda. Additional assumptions (5.2.28), (5.2.29), (5.2.37) are imposed for s<=0 and unbounded U. Cubes must have radius R>=rho_beta and satisfy the explicit bulk-distance condition (8.3.1)–(8.3.2). Its actual estimate (8.3.3) includes the correction C0 times the number of particles in the cube. The localized energy in (7.1.23), PDF page 148, is the truncated electric-field energy, with point self-energy and point-background corrections. It depends on particles outside the cube. A standalone quadratic count statistic cannot be substituted for it.

For a conventional confining-potential gas the text before Theorem 8.2 requires (A1)–(A5) and theta=beta N^{2/d}>theta0. These assumptions matter: the very-hot special case proved below does not meet this condition.

## 2. A proved special case: total-variation Poisson approximation at very high temperature, d>=3

Let d>=3, g(x)=|x|^{2-d}, and let D_N be a cube of Lebesgue volume N. Put mu=1_{D_N} dx, p_N=mu/N, and define the full-space neutral modulated energy

\[
 F_N(X)=\sum_{i<j}g(x_i-x_j)
 -\sum_i\int g(x_i-y)\,d\mu(y)
 +\tfrac12\iint g(x-y)\,d\mu(x)d\mu(y).
\]

This is the full-space Coulomb modulated Gibbs ensemble, with hard support provided by the reference density, not the Neumann-cube energy. Let

\[
 dQ_{N,\beta}=Z^{-1}e^{-\beta F_N}\,dp_N^{\otimes N}.
\]

For any measurable A subset D_N of volume v, the point process restricted to A satisfies

\[
 d_{TV}(\mathcal L_Q(X|_A),\operatorname{PPP}(1_A dx))
 \le \sqrt{\beta K_d N/2}+v^2/N,
 \qquad K_d=\tfrac12+|S^{d-1}|(\tfrac12-1/d).
\tag{P}
\]

TV is sup over measurable events. Consequently beta_N N ->0 and v_N^2/N ->0 suffice for convergence in total variation to the unit-intensity Poisson process on A_N, even for growing A_N. This is a special regime, not the requested scale-sharpness theorem.

### 2.1 Complete stability proof

Let sigma_x be normalized surface measure on the sphere of radius one centered at x. Newton's shell theorem yields

\[
 (g*\sigma_0)(z)=\begin{cases}1&|z|\le1,\\g(z)&|z|\ge1.\end{cases}
\]

For completeness, rotational symmetry and harmonicity off the shell give a radial harmonic function inside and outside. The bounded interior solution is constant; the decaying exterior solution is a multiple of r^{2-d}. Unit mass fixes that multiple to one, and continuity at r=1 fixes the interior constant. Continuity holds because the Coulomb singularity is integrable on the (d-1)-dimensional sphere: locally the integral is bounded by a constant times integral_0^epsilon r^{d-2}r^{2-d} dr. Thus g*sigma_0<=g and its sphere self-energy equals one. Convolving this inequality a second time gives g*sigma_0*sigma_0<=g*sigma_0<=g. Hence smearing cannot increase any distinct pair energy.

Let nu=sum_i sigma_{x_i}-mu. Its Coulomb quadratic energy is nonnegative. Here is a direct justification, including convergence: all point-shell, shell-shell and bounded-density interactions are finite, so integral g d|nu|d|nu| is finite. For alpha=(d-2)/2>0,

\[
 g(z)=\Gamma(\alpha)^{-1}\int_0^\infty t^{\alpha-1}e^{-t|z|^2}\,dt.
\]

Each Gaussian kernel is positive definite: its Fourier transform is a positive Gaussian, so its quadratic integral against any finite real signed measure is nonnegative. This Fourier assertion follows directly by the Gaussian integral and Fubini, since the Fourier Gaussian is integrable and nu has finite total variation. Integrate in t; absolute convergence against |nu| justifies Fubini. This proves the claimed positivity without an assumption on an unknown electric field.

Write A for the ordered distinct point-pair sum, A' for the ordered distinct shell-pair sum, B for the point-background interaction, B' for the shell-background interaction, and C for the background self-interaction. Then

\[
 F_N=A/2-B+C/2,\qquad
 S=\tfrac12\iint g\,d\nu\,d\nu=(A'+N)/2-B'+C/2\ge0.
\]

The point-background loss is bounded separately for each point:

\[
 0\le\int[g(x-y)-(g*\sigma_0)(x-y)]\,d\mu(y)
 \le\int_{B_1}( |z|^{2-d}-1)\,dz
 =|S^{d-1}|(1/2-1/d).
\]

The inequality uses 0<=mu<=1; extending the integral to the whole unit ball only increases it. Combining A>=A', B-B'<=N|S^{d-1}|(1/2-1/d), and S>=0 gives

\[
 F_N\ge-K_dN.
\tag{S}
\]

Collisions, a Lebesgue-null set, have F_N=+infinity and do not invalidate the estimate. The algebraic combination of these inequalities is formalized in `OnsagerAlgebra.lean`. The analytical shell theorem and Gaussian positivity are proved above, not formalized in that file.

### 2.2 Complete entropy and Poisson approximation proof

Put a_N=integral g(x-y) dp_N(x)dp_N(y), a finite positive number. Independence gives E_P A=N(N-1)a_N, E_P B=N^2 a_N, and C=N^2 a_N. Thus E_P F_N=-Na_N/2<=0. Jensen's inequality gives log Z>=-beta E_P F_N>=0. Stability also gives Z<=exp(beta K_d N), so Z is positive and finite.

The relative entropy is

\[
 D(Q\Vert P)=-\beta E_QF_N-\log Z\le\beta K_dN.
\]

For beta>0 this identity has finite terms: F_N is bounded below and t exp(-beta t) is bounded on [0,infinity), making its positive part Q-integrable. For beta=0, Q=P and entropy is zero. Pinsker's inequality gives d_TV(Q,P)<=sqrt(beta K_dN/2). Restriction to A cannot increase TV.

Under P the number of points in A is Binomial(N,v/N). Conditional on that number, their locations are independent with common law dx/v on A (the case v=0 is trivial). A unit-intensity Poisson process on A has the same conditional location laws and a Poisson(v) count. Couple each Bernoulli(p) variable with an independent Poisson(p) variable. Their TV distance is p(1-e^{-p})<=p^2, obtained by comparing their masses at 0, 1, and >=2. Product coupling and the union bound give d_TV(Binomial(N,p),Poisson(Np))<=Np^2=v^2/N. Applying the common conditional-location kernel proves the second term in (P). The triangle inequality completes the proof.

### 2.3 Hostile-referee checks and scope

* The model uses full-space pair energy, not an unproved replacement by Neumann Green functions.
* Shells may extend beyond D_N; this is allowed in full space. The background remains supported on D_N, and the loss bound is uniform even near its boundary.
* Self-shell energy is exactly one; it cannot be omitted from the algebra.
* The entropy argument uses ordinary unnormalized relative entropy. The source's H_N convention has an extra N, so copying its display without conversion would produce an incorrect estimate.
* Total-variation convergence does not imply convergence of the unbounded exponential observable in (8.0.1).
* Under beta_N N ->0, rho_beta/N^{1/d}->infinity for d>=3. Indeed beta_N N^{2/d}=(beta_N N)N^{2/d-1}->0. Thus there is no Debye crossover inside this box. This proof establishes only a very-hot Poisson regime and cannot be sold as a proof of sharpness in the localized regime theta>=theta0.

## 3. A rigorous obstruction to a tempting implication

If K is Poisson(lambda) with lambda>0, then for every t>0,

\[
 E\exp(t(K-\lambda)^2)=\infty.
\tag{Q}
\]

Proof: the kth summand is a_k=e^{-lambda}lambda^k exp(t(k-lambda)^2)/k!, and

\[
 a_{k+1}/a_k=\frac\lambda{k+1}\exp(t(2(k-\lambda)+1))\longrightarrow\infty.
\]

The summands therefore fail to tend to zero, proving divergence. In contrast, conditioned laws K_M=(K | K<=M) are finitely supported and have finite exponential square moments. Their TV distance from K is exactly P(K>M)->0 (compare the two masses on {0,...,M} and its complement). Thus even TV convergence to Poisson does not decide the behavior of quadratic exponential moments. It does not identify the localized electric energy either. Any argument deducing failure of (8.0.1) merely from point-process convergence has two missing steps: an energy/count comparison for the actual F_square, and quantitative control of the relevant rare-event tails uniformly in beta,N,R.

## 4. Remaining gap

No lower bound contradicting (8.0.1) or its rigorous corrected version (8.3.3) has been proved here for admissible bulk cubes with 1<<R<<rho_beta<<N^{1/d}. Nor is there a uniform Poisson approximation on all such growing windows. The temperature and dimension dependence of the sharp crossover, including whether the d=2 logarithmic chi correction is essential, remains unresolved by this attempt. The global entropy proof cannot reach that regime because its error is order sqrt(beta N), and the local energy is influenced by exterior charges.

## 5. A literature-based reduction inside the localized d=2 regime

This section uses Theorem 1 of Padilla-Garza–Peilen–Thoma, arXiv:2507.08198v2, PDF page 3, as an external theorem. It is a special-case consequence, not a literature solution of P0331. Take the planar confining gas of that paper, V(x)=|x|^2/2, z=0, and beta_N=N^{-3/4}. Its (Conf), (Grow), and (Temp) hypotheses hold (the positive infimum of beta_N N is one), and beta_N N=N^{1/4}->infinity. The equilibrium density is a positive constant m=1/pi near zero: apply -Delta to h_mu+V=constant to obtain 2pi mu=Delta V=2 in the droplet, whose radius one follows from unit mass. Thus the theorem gives vague weak convergence Q_{0,N}=>PPP(m dx).

There exists a deterministic sequence of integers R_N->infinity such that

\[
 R_N/\rho_{\beta_N}\to0,\quad R_N/\sqrt N\to0,\qquad
 d_{TV}\big(\mathcal L(Q_{0,N}([-R_N,R_N]^2)),
 \operatorname{Poisson}(4mR_N^2)\big)\to0.
\tag{D}
\]

Complete diagonal proof: For each fixed integer j>=1 the Poisson process places no point on the square boundary almost surely, so the count map is continuous at almost every limiting configuration. The continuous mapping theorem gives convergence of the integer-valued count in [-j,j]^2 to Poisson(4mj^2). This convergence is in TV: for an arbitrary epsilon choose a finite set {0,...,M} carrying at least 1-epsilon of the limiting mass; individual probabilities converge (use the intervals (k-1/2,k+1/2)), and hence the finite sum of absolute differences tends to zero. The remaining total variation is bounded by the two tail probabilities, whose limsup is at most 2epsilon. Let epsilon decrease to zero.

Choose strictly increasing n_j so that for every N>=n_j that TV distance is <=1/j, rho_beta_N>=j^2, and sqrt N>=j^2. Such n_j exist since the fixed-j distance tends to zero and both scales diverge. For N>=n_1 set R_N=max{j:n_j<=N}; set it to one for the finitely many earlier N. The maximum is finite because n_j is strictly increasing, R_N->infinity, the TV distance is <=1/R_N, and both scale ratios are <=1/R_N. This proves (D).

Here rho_beta_N is order N^{3/8} sqrt(log N), which is o(sqrt N), so the crossover is inside the macroscopic droplet. These windows lie deep in the bulk. The source buffer d0 is order at most N^{5/12}(log N)^{1/3} plus N^{1/4}, which is o(sqrt N); hence the bulk-distance obstruction is absent in this example. This calculation follows by substituting rho_beta_N into (8.3.2).

Limitations: the construction supplies no explicit growth rate of R_N and does not handle every sub-Debye window. It controls counts, not point-process TV on growing regions, variance convergence, or electric-energy exponential moments. It inherits the cited theorem, whose full proof has not been independently reproduced here. Its printed Theorem 1 omits beta_N N->infinity even though its proof uses mu_theta->mu_V; the chosen beta_N satisfies that extra condition explicitly. Also, Proposition 3.7 fixes k, so its error cannot be freely used with k growing like R_N^2. These are precisely why this remains a limited reduction.

## 6. Computation and formal checking

`numerical_checks.py` computes exact finite binomial/Poisson mass comparisons through logarithms, midpoint quadrature for the d=3 shell potential, and the logarithm of successive Poisson exponential-square summands. It uses fewer than 100,001 quadrature terms and 10,001 count entries per case. Results are saved in `numerical_checks.json`. These are consistency checks; all propositions above have analytic proofs or explicitly cited theorem dependencies.

`OnsagerAlgebra.lean` formalizes the stability-inequality algebra and the entropy cancellation, importing Mathlib.Data.Real.Basic and Mathlib.Tactic.Linarith. The first run failed because the real-number import was missing. After adding it, `lake env lean` from ~/lean_verify exited 0 with empty stdout/stderr, in 113.3 seconds and with a 3600-second timeout. The final file has no sorry or native_decide; linarith constructs kernel-checked proof terms. The result is saved in `lean_result.json`. This verifies only the two algebraic implications, not the analytic or probabilistic arguments.
