# Second serious attempt at P0331

2026-10-12. Starting verdict PARTIAL. This file records new work beyond ATTEMPT.md.

## Two approaches not previously attempted

1. **Localize relative entropy using translation symmetry.** The previous global Pinsker estimate loses a factor N and only applies when beta N tends to zero. On a periodic Coulomb box, translation invariance and superadditivity of entropy relative to a product Poisson reference should divide that entropy cost among equal spatial cells. If periodic Onsager stability is uniform in box size, this should prove point-process TV convergence on explicit growing windows even when the Debye length is strictly inside the box. The canonical fixed-N constraint costs only the entropy of conditioning a Poisson(N) count to equal N.

2. **Use a localized electrostatic test function and rare-event lower bounds.** Gauss' law paired with a smooth compactly supported test function gives a lower bound on electric energy in terms of the squared smoothed charge discrepancy, with denominator integral |grad phi|^2. One could combine a conditional Gibbs insertion/deletion comparison with this bound to control moderately rare count deviations. This would address the actual energy-law gap more directly. Obstacles: the source's truncation radii and self-energy corrections must be included; exterior charges affect the field; the tail cost may already cancel the energy exponential, so a Poisson variance alone is insufficient. No quantitative insertion lower bound is currently available here.

Approach 1 is pursued first because each step can be proved without an unknown correlation estimate. It is a periodic-model special case, not a solution for the source's full-space/Neumann ensembles. Target: an explicit local entropy bound in d>=3 with beta N^{2/d} tending to infinity, which the previous very-hot proof could not reach.

Math-store gap queries: `Coulomb localized electric energy lower bound Poisson tails Debye screening Onsager`; `relative entropy superadditivity stationary point processes Poisson Coulomb torus Onsager`. Returned cards are hints only; outcomes will be recorded below.

## Proposed theorem to check

Let d>=3, N an integer, L=N^{1/d}>=8, and T_L=(R/LZ)^d with volume measure dx (total mass N). Let G_L be the mean-zero periodic Coulomb Green function normalized by

\[
 -\Delta G_L=c_d(\delta_0-N^{-1}),\qquad
 c_d=(d-2)|S^{d-1}|.
\]

Let P_N be N independent uniform positions in T_L, F_N=sum_{i<j}G_L(x_i-x_j), and dQ=Z^{-1}exp(-beta F_N)dP_N. The neutral uniform-background terms vanish by the mean-zero normalization. The proposed bound for every cube A of side ell<=L/2, at every location, is

\[
 d_{TV}(\mathcal L_Q(X|_A),\operatorname{PPP}(1_A dx))
 \le \sqrt{2^{d-1}\ell^d\left(C_d\beta+\frac{1+\log N}{N}\right)}.
 \tag{T}
\]

This requires proving F_N>=-C_d N uniformly in L, ordinary relative entropy D(Q||P_N)<=C_d beta N, and a product-Poisson spatial entropy inequality. This was initially a target under verification; its complete proof is now in Section 3. The regime beta ell^d->0 is strictly smaller than the whole sub-Debye range ell<<beta^{-1/2} in d>=3, but it removes the previous requirement beta N->0.

## New simplification during the attempt

Translation symmetry is needed only to make the result uniform in the center. The entropy inequality itself proves an average-over-cells result without symmetry. Therefore the same method can already improve the actual full-space hard-reference ensemble of ATTEMPT.md Section 2, using its proved stability bound, even in a localized temperature regime. It will show Poisson TV approximation for all but a vanishing fraction of equal-volume bulk cells, provided beta times cell volume tends to zero. The periodic Green-function construction is pursued as an additional uniform-center special case, not as a necessary premise of that improvement.

## 1. Proved general spatial entropy lemma

Let D have volume N, P be N independent uniform points in D, and Q be any exchangeable law on those labeled points with D(Q||P)<=B<infinity. Write Xi for the unlabeled counting measure and Pi_D for the unit-intensity Poisson law. Partition D into m disjoint measurable cells D_j, and let Q_j be the restriction laws. Then

\[
 \sum_j D(Q_j\Vert\Pi_{D_j})\le B+h_N,\qquad
 h_N=-\log\Pr(\operatorname{Poisson}(N)=N)\le1+\log N.
 \tag{E1}
\]

Full proof: P induces Pi_D conditioned on total count N. Both exchangeable labeled laws have the same uniform conditional distribution over labelings of a simple configuration. Alternatively, their density ratio is a symmetric function, hence is unchanged on passing to configurations. Consequently the unlabeled relative entropy is D(Q||P). On the event of N points, the density relative to Pi_D equals the density relative to its conditioned law divided by p_N=exp(-N)N^N/N!. Integrating its logarithm gives exactly

\[
 D(\mathcal L_Q(\Xi)\Vert\Pi_D)=D(Q\Vert P)+h_N. \tag{E2}
\]

Collisions and cell boundaries of zero volume have zero probability under P and Q. The restrictions of Pi_D are independent, and the density decomposition gives

\[
 D(Q_{1:m}\Vert\bigotimes_j\Pi_{D_j})
 =D(Q_{1:m}\Vert\bigotimes_jQ_j)+\sum_jD(Q_j\Vert\Pi_{D_j})
 \ge\sum_jD(Q_j\Vert\Pi_{D_j}).
\]

Each marginal divergence is finite by data processing. The joint law is absolutely continuous with respect to its product marginal law: on any coordinate where its marginal reference density is zero, the joint density is zero for almost every other coordinate, by Fubini. The displayed identity follows by taking the logarithm of the joint/product-marginal density times the product marginal/reference density and integrating. Negative parts of relative-entropy integrals are integrable (u log u>=-1/e); the global and marginal divergences are finite. This proves (E1). Finally, monotonicity of log gives

\[
 \log N!\le\int_1^N\log x\,dx+\log N
 =N\log N-N+1+\log N,
\]

by bounding the k-th term, k<N, with the integral over [k,k+1]. Substitution into h_N proves its bound, including N=1.

Let t_j=TV(Q_j,Pi_{D_j}). Pinsker gives

\[
 \frac1m\sum_jt_j^2\le\frac{B+h_N}{2m},\qquad
 \frac{\#\{j:t_j>\epsilon\}}m\le\frac{B+h_N}{2m\epsilon^2}. \tag{E3}
\]

For equal-shaped cells, translate them to a common cube. A uniformly chosen cell has the mixture of these restriction laws; convexity of TV and Cauchy–Schwarz bound its TV by sqrt((B+h_N)/(2m)). For a subset of k cells replace m by k in the averaged bounds, since the subset entropy sum is bounded by the full sum. No independence of Q's cells is assumed.

## 2. Stronger special case in the original full-space hard-reference ensemble

For the d>=3 ensemble of ATTEMPT.md Section 2, its proved stability and Jensen bounds imply D(Q||P)<=K_d beta N for every beta>=0, K_d=1/2+|S^{d-1}|(1/2-1/d). There is no beta N->0 hypothesis on this entropy inequality. Partition the volume-N cube into m=q^d cells, each of volume v=N/m. Then (E3) proves

\[
 \frac1m\sum_jt_j^2
 \le\tfrac12\left(K_d\beta v+\frac{v(1+\log N)}N\right). \tag{H}
\]

If beta v->0 and v log N/N->0, the entire random-cell point process converges in TV to the unit-intensity Poisson process on that growing cell; the fraction of deterministic cells with TV>epsilon tends to zero. Write a_N=K_d beta v+v(1+log N)/N. When a_N->0, the stronger threshold TV>a_N^{1/4} holds for at most sqrt(a_N)/2 of all cells, by (E3).

For q>=8, the cells contained in the concentric half-sized cube number at least (q/4)^d=m/4^d: in each coordinate at least q/2-2>=q/4 intervals are contained. Their averaged squared TV is bounded by 4^d times (H). They all lie at distance at least L/4 from the outer boundary. Thus the same conclusions hold for the bulk cells, up to constants.

Explicit d=3 example: beta_N=N^{-1/3}, L=N^{1/3}, q=floor(N^{1/4}), side s=L/q, volume v=s^3. Then v is order N^{1/4}, beta v is order N^{-1/12}, and v log N/N is order N^{-3/4}log N. Moreover

\[
 \beta_NN^{2/3}=N^{1/3}\to\infty,\qquad
 1\ll s\asymp N^{1/12}\ll\rho_\beta\asymp N^{1/6}\ll L.
\]

For a random bulk cell the entire point-process TV error is O(N^{-1/24}); at all but a vanishing fraction of bulk cells it tends to zero. The source's bulk buffer d0 in (8.3.2) is order max(N^{2/9},N^{1/5})=o(L), so these windows satisfy its distance condition. The cells are below the proved R range of Theorem 8.2; we do not invoke that theorem there. This is a genuine improvement on the previous very-hot regime and unquantified diagonal windows, but no fixed prescribed center or energy-law failure is asserted.

## 3. Uniform-center periodic special case: proof of (T)

### 3.1 Definition and local regular part

The mean-zero Green function on the unit torus can be defined by its heat kernel p_t:

\[
 G_1(x)=c_d\int_0^\infty(p_t(x)-1)\,dt
\]

away from the singularity, or in distributions. The nonconstant Fourier modes have positive coefficients c_d/(4pi^2|k|^2); the constant mode is zero. The integral converges at large t by the spectral gap. Locally its singular part is g(x)=|x|^{2-d}, as follows by splitting the periodized heat kernel into its Euclidean contribution and the other lattice translates at small t. The latter integrals and their derivatives converge uniformly in a neighborhood of zero; thus G_1=g+H_1 with H_1 smooth there and Delta H_1=c_d. Equivalently this local regularity follows by subtracting the fundamental solution and solving a Poisson equation with smooth constant right side. On a fixed ball |x|<=1/4, write M_d=sup|H_1(x)|<infinity.

Scaling gives G_L(x)=L^{2-d}G_1(x/L). On |x|<=2 with L>=8,

\[
 G_L(x)=g(x)+H_L(x),\quad
 H_L(x)=L^{2-d}H_1(x/L),\quad
 \Delta H_L=c_d/N,\quad |H_L|\le M_d.
\]

The last bound uses d>=3 and L>=1. Boundary values of the radius-1/4 ball may be included by choosing a slightly larger smooth neighborhood; there are no other torus singularities nearby.

### 3.2 Corrected shell averaging and uniform stability

Let sigma be normalized radius-one spherical measure, interpreted on the torus. Set a=c_d/(2dN), and f(x)=(|x|^{2-d}-1)_+ on the embedded unit ball, zero outside it. Then

\[
 G_L*\sigma=G_L-f+a. \tag{S1}
\]

Proof: on a radius-one ball without a singularity, subtract the quadratic function (c_d/(2dN))|y-x|^2 from G_L(y); the result is harmonic, so the sphere average differs from G_L(x) by a. If the ball contains a lattice singularity, subtract its Coulomb fundamental solution as well. The regular part has the same average shift, and Newton's shell theorem replaces g(x) by min(g(x),1), precisely subtracting f. Since L>=8 there cannot be two lattice singularities in one such ball. The identity holds off zero and distributionally. Notice the positive a term: ordinary full-space superharmonicity cannot be copied to the torus without this correction.

Since f>=0 and convolution preserves inequalities, (S1) gives

\[
 G_L*\sigma*\sigma\le G_L+2a.
\]

The self-shell interaction I=integral G_L(x-y)d sigma(x)d sigma(y) is bounded above by J_d=1+M_d, because all lifted differences have norm<=2, the fundamental-solution shell self-energy is one, and |H_L|<=M_d. It is finite and nonnegative by the positive nonconstant Fourier coefficients of G_L (subtracting the uniform background from sigma does not change the energy).

For arbitrary distinct points let A=sum_{i!=j}G_L(x_i-x_j), A'=sum_{i!=j}(G_L*sigma*sigma)(x_i-x_j). With nu=sum_i sigma_{x_i}-dx, positivity of the periodic Green quadratic form gives

\[
 S=\tfrac12\iint G_L(x-y)d\nu(x)d\nu(y)
 =\tfrac12(A'+NI)\ge0.
\]

Here the uniform-background terms vanish. To justify positivity without a formal Fourier summation, use the heat representation. For t>0, the heat kernel is positive definite: its absolutely convergent Fourier series has positive coefficients exp(-4pi^2|k|^2 t/L^2)/N. Thus its quadratic integral against nu is nonnegative, and the constant subtraction has zero quadratic integral since nu has total mass zero. Absolute Fubini for the t integral holds. At large t the nonconstant heat kernel decays exponentially by its Fourier series. For 0<t<=1 the periodized Euclidean Gaussian, integrated in t, is bounded by C_L(1+dist(x,y)^{2-d}): the nearest image gives the usual Coulomb singularity by the Gaussian integral, and the other images give a bounded sum with Gaussian-decaying tails. The resulting bound is integrable against |nu| times |nu|. Indeed sphere-sphere g interactions, including identical spheres, are finite by the shell formula; background interactions are finite by bounded density and compactness. Integrating the nonnegative heat quadratic forms gives S>=0. This avoids an unproved exchange of a conditionally convergent Green Fourier series with the measures.

The pair bound A'<=A+2aN(N-1) and self bound I<=J_d imply

\[
 F_N=A/2\ge -NI/2-aN(N-1)
 \ge-N\left(J_d/2+c_d/(2d)\right)=-C_dN. \tag{S2}
\]

The additive background correction is order N, not order N^2, because a is order 1/N. Collisions have infinite positive energy and zero reference measure. This proves uniform stability for all box sizes under consideration.

### 3.3 Entropy, symmetry and arbitrary cubes

Mean-zero G_L and independent uniform points imply E_P F_N=0, so Jensen gives log Z>=0. Stability gives Z<=exp(beta C_dN). At beta>0, F_N's positive part is Q-integrable since t exp(-beta t) is bounded for t>=0. Therefore

\[
 D(Q\Vert P)=-\beta E_QF_N-\log Z\le C_d\beta N.
\]

The beta=0 case is immediate. Partition the torus into q^d equal cubes of side s=L/q and volume v=N/q^d. Translating by grid steps permutes cells, and Q is invariant under every torus translation, since both Haar reference measure and all pair differences are invariant. All spatial marginal divergences are equal. Section 1 consequently gives for each cell

\[
 D(Q_{\rm cell}\Vert\Pi_{\rm cell})
 \le C_d\beta v+v(1+\log N)/N. \tag{E4}
\]

For a cube A of side ell<=L/2 choose q=floor(L/ell)>=2. A translated grid cell of side s=L/q contains A, and ell<=s<=2ell, since floor(L/ell)>=L/(2ell). Translation invariance permits choosing this grid at A's location. Restriction to A is a measurable map and cannot increase TV. Its Poisson restriction has intensity 1_A dx. Pinsker and v=s^d<=2^d ell^d prove (T).

Thus for every center and every sequence ell_N with beta_N ell_N^d->0 and ell_N^d log N/N->0, the whole local point process converges in TV to PPP. This is a homogeneous periodic model only. For d=3, beta=N^{-1/3}, ell=N^{1/12}, (T) gives the same O(N^{-1/24}) rate uniformly at every center, while rho_beta is strictly inside the box. Transfer to the source's Neumann/full-space laws would require a new boundary/comparison argument. The first-attempt estimate did not provide such a transfer, and it remains unproved here.

## 4. Testing the second route on the actual source electric energy

This calculation now uses the actual source energy, not a count surrogate. Equations (7.1.26) and (7.1.36), Lemma 7.8 on PDF page 150, supply radii tilde r_i<=1/4 in full space and

\[
 \int_\Omega|\nabla u_{\tilde r}|^2
 \le4c_d H_\Omega,\qquad
 H_\Omega=F_\Omega+C_0\# I_\Omega\ge0. \tag{L1}
\]

Let phi be a nonzero smooth function supported in (-1/2,1/2)^d. Put phi_R(x)=phi((x-z)/R) and Omega=z+(-R,R)^d with R>=2. Let A=integral |grad phi|^2>0 and M=sup||D^2 phi||_op. Define D_R=sum_i phi_R(x_i)-integral phi_R dmu and n_Omega=#I_Omega. The truncated field satisfies -Delta u_tilder=c_d(sum_i sigma_{x_i}^{tilde r_i}-mu), with uniform spherical charges. Since each sphere has mean displacement zero, Taylor's formula gives

\[
 |\phi_R(x_i)-\int\phi_R\,d\sigma_{x_i}^{\tilde r_i}|
 \le\frac{M}{2R^2}\tilde r_i^2\le\frac{M}{32R^2}.
\]

Only centers in Omega can contribute to this difference or the test integral, because the support has a one-neighborhood in Omega and all radii are <=1/4. Integration by parts, Cauchy–Schwarz and (L1) therefore prove the deterministic bound

\[
 \left(|D_R|-\frac{M n_\Omega}{32R^2}\right)_+^2
 \le \frac{4A}{c_d}R^{d-2}H_\Omega. \tag{L2}
\]

The integration by parts is distributional against a smooth compactly supported function. The truncated field is locally square-integrable by (L1); no boundary term occurs. The exact identity used is integral phi_R(sum sigma-mu)=(1/c_d)integral grad phi_R dot grad u_tilder. Taking absolute values and inserting the Taylor bound proves (L2). This improves the source's general Lipschitz-test error O(n/R) to O(n/R^2) for smooth tests, and handles exterior charges deterministically via the source field.

In d=3, Poisson-like fluctuations give a real but insufficient lower bound for H. Write a_2=integral phi^2>0 and a_4=integral phi^4. Under unit PPP on Omega,

\[
 E D_R^2=R^3a_2,\qquad E D_R^4=R^3a_4+3R^6a_2^2.
\]

These identities follow first for step functions: independence of Poisson counts and the centered Poisson moments E(K-lambda)^2=lambda and E(K-lambda)^4=lambda+3lambda^2 give the formula by expansion. Approximate a bounded smooth compactly supported phi in L2 and L4 by step functions; the same fourth-moment identity makes the centered integrals converge in L4 and passes the identities to the limit.

For Y=D_R^2, Cauchy–Schwarz applied to Y on {Y>=EY/2} proves Paley–Zygmund in this instance: EY<=EY/2+sqrt(EY^2 P(Y>=EY/2)). Consequently, for R>=1,

\[
 \Pr(|D_R|\ge\sqrt{a_2/2}R^{3/2})\ge
 p_0:=\frac{a_2^2}{4(a_4+3a_2^2)}>0.
\]

Since E n_Omega=8R^3, choose K>=16/p_0. Markov's inequality gives Pr(n_Omega>KR^3)<=p_0/2, so the intersection of these two favorable events has probability at least p_0/2. If the local point-process law is within TV<=p_0/4 of PPP, the same event has probability >=p_0/4 under the Coulomb law. On that event the Taylor error is <=MK R/32, and for sufficiently large R it is at most half the discrepancy lower bound. Equation (L2) yields

\[
 \Pr\left(H_\Omega\ge\frac{c_3a_2}{32A}R^2\right)\ge p_0/4. \tag{L3}
\]

This applies to all but a vanishing fraction of the growing bulk cells in Section 2 (take R=half their side). It is a lower bound for the **corrected localized energy in (8.3.3)** in a genuinely sub-Debye, localized d=3 regime. Its proof uses only the proved cell-TV result and the source's deterministic Lemma 7.8, not an assumption about unknown Coulomb moments.

Why this does not prove sharpness: H is forced to be at least order R^2 with positive probability, while the source permits order R^3. If h=c_3a_2 R^2/(32A), beta h/2<=1, and p=p_0/4, nonnegativity gives

\[
 \log E e^{\beta H/2}\ge\log(1+p\beta h/2)\ge p\beta h/4.
\]

The last inequality uses log(1+x)>=x/2 for 0<=x<=1, proved by integrating 1/(1+x)>=1/2. Thus we obtain an order beta R^2 lower bound, not one exceeding C beta R^3. The ratio to the permitted volume scale is order 1/R. This explicitly shows that the natural smooth-discrepancy route cannot supply the needed contradiction from ordinary Poisson-sized fluctuations alone. Larger rare deviations or collective field modes require new information.

## 5. Brain outcomes and hostile-referee checks

The first gap query returned the old linear-response diagnostic and unrelated energy results. It supplies no nonlinear tail theorem. The second query returned the generic relative-entropy/Pinsker card `claim_9a0024c47f80d6e08a113cbde08d41df`, generic PPP definitions, and unrelated stationary-entropy material. No card supplied the proposed localization theorem, so the entropy decomposition and canonical correction were proved directly above. No brain write command was used.

Checks already completed:

* The canonical correction is essential. Exact enumeration of a 12-point, three-cell symmetric toy Gibbs law gives labeled KL=0 at beta=0 but sum of cell KLs=0.11191599>0. Omitting h_N would falsely claim Poisson marginals at finite N. With h_N=2.16833470, entropy superadditivity holds in all four tests.
* The torus is not superharmonic away from zero. Ewald evaluation and 4096-point spherical quadrature verified the **positive** shell shift a=4pi/(6N). At L=8 and radii 0.5, 1.5, 3, errors in (S1) were at most 1.10e-6, well below the shift 0.0040906. This tests the sign and normalization; the analytic proof remains the justification.
* Numerical finite tests also checked Pinsker with the convention TV=sup event difference, the elementary h_N bound, and the explicit localized-regime exponents. `second_checks.py` ran in 1.53 seconds, with chunked arrays far below 1 GB. Results: `second_checks.json`.
* Neither finite enumeration nor periodic quadrature simulates the source gas. No claim of empirical confirmation of full Debye sharpness follows from them.
* The field lower bound includes the source's C0 times particle count, uses its actual truncation radii, and retains the smooth-test Taylor error. It is not a lower bound for an invented count-energy functional.
* Positive-probability event transfer uses TV only for bounded event indicators. We have not transferred fourth moments or exponential moments by TV. The Poisson moments are used to prove a PPP event, and then only that event is transferred to the gas.

Formal check: `SpatialEntropy.lean` imports only Real.Basic, the finite ordered-sum module, and the linarith tactic module. It formalizes summed Pinsker-budget algebra, the periodic smearing stability algebra, and division of the entropy budget by the number of cells. The initial run failed because `local` was used as a binder name (a Lean reserved word); it was renamed to Dloc/Dglob. The corrected run completed with exit code 0, empty stdout/stderr, in 137.9 seconds under a 3600-second timeout. The result is in `second_lean_result.json`; the initial failure is retained in `second_lean_initial_failure.json`. The final file contains no sorry or native_decide; all three algebraic lemmas are kernel checked. The full analytic probability arguments are not formalized.

## 6. Exact remaining gaps after this attempt

The strongest original-model result is explicit growing-window point-process TV convergence for a spatial average and for most bulk cells in d>=3, when beta times window volume tends to zero. It does not cover a prescribed center, nor the full interval beta^{-1/d}<<R<<beta^{-1/2}. Uniformity in the center was obtained only for a periodic homogeneous model, and no transfer to the source's Neumann/full-space setting is proved.

Even in the improved sub-Debye regimes, the proved electric-energy lower bound is order R^2, which is smaller than the allowed volume R^3. A sharpness proof still needs a lower bound on the actual exponential energy observable that exceeds every beta-independent volume-law constant at an appropriate sequence of admissible windows, or a counterexample to the conjecture. Dimension d=2 and its logarithmic correction, d=1 and its correction, and the other temperature regimes remain open within this attempt.

The full P0331 verdict therefore remains PARTIAL. The new statements are stronger special cases and a checked obstruction to a particular proof route; they are not a proof or refutation of the all-case source conjecture.

## 7. A sharper conditional reduction to Debye–Hückel free energy

The entropy method identifies a concrete way to extend the periodic d=3 result to the entire sub-Debye range. This is a proved implication with an **unproved premise**, not a new Coulomb estimate. Let f_N(beta)=log Z_N(beta)/N for the mean-zero periodic model above. Its mean reference energy is zero, so f_N>=0. For beta>0 it is differentiable and convex: differentiability follows from stability and exponential suppression of the positive energy tail, and its second derivative is Var_Q(F_N)/N>=0. Convexity gives

\[
 f_N'(\beta)\le\frac{f_N(2\beta)-f_N(\beta)}\beta,
 \qquad
 \frac{D(Q_\beta\Vert P)}N
 =\beta f_N'(\beta)-f_N(\beta)
 \le f_N(2\beta)-2f_N(\beta)\le f_N(2\beta). \tag{DH1}
\]

If one could prove the uniform finite-volume Debye–Hückel-type bound

\[
 \log Z_N(2\beta)\le C N\beta^{3/2} \tag{DH2}
\]

in the periodic d=3 regime with beta small and L sqrt(beta) large, (DH1) and exactly the proved spatial entropy argument would yield

\[
 TV(Q|_A,\Pi_A)
 \le C'\sqrt{\beta^{3/2}\ell^3+\ell^3(1+\log N)/N}.
\]

Thus every window ell=o(beta^{-1/2}) would be Poisson in TV provided also ell^3 log N/N->0. The first term is exactly (ell sqrt(beta))^{3/2}. This would reach the Debye spatial scale for point-process convergence in this periodic three-dimensional model, rather than merely beta^{-1/3}. The finite-size conditioning condition and transfer to source boundary conditions would still remain, and even this would not prove energy-law sharpness.

No argument here proves (DH2). A Gaussian screened determinant predicts this exponent but cannot be substituted for the nonlinear singular gas. A named math-store query `Brydges Federbush Debye Huckel jellium free energy high temperature` is made to look for a rigorous neighboring free-energy theorem. Any returned theorem must match the background, ensemble, normalization and finite-volume uniformity before use; otherwise it is only a lead.

That named query completed and returned unrelated Potts-spin-glass results and a one-dimensional Riesz analyticity problem. It supplied no matching Debye–Hückel theorem. Consequently (DH2) remains an explicit unproved premise; no literature shortcut is asserted.
