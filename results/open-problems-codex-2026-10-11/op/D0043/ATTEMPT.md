# Final outcome: counterexample to D0043

The conjecture as posed is false for k=1,beta=2. The full proof follows. No matching literature solution was certified; this is a counterexample derived from published local-kernel convergence and a Gaussian form bound. No mathematical gap remains in this argument. The correct replacement operator is not identified.

# D0043: tail obstruction to the proposed exotic edge operator

Research date: 2026-10-12. This is an original implication of cited theorems, not a claim that a cited paper states a solution of Virag's question. Final source/hypothesis and formal checks are recorded in STATUS.md and LITERATURE.md.

## Statement being refuted

Virag's Conjecture 5 (arXiv:1804.06953, PDF p.14) proposes, for an analytic beta-ensemble with equilibrium density vanishing as (E-x)^(2k+1/2), a scaled tridiagonal limit

 S_beta,k = -d^2/dt^2 + t^(1/(2k+1)) + (2/sqrt(beta))t^(-k/(2k+1))B'(t).

The precise refinement is Krishnapur-Rider-Virag, arXiv:1306.4832, Conjecture 45, PDF p.57: half-line Dirichlet boundary, H_n,k=gamma n^(2/(4k+3))(E I-T_n), and joint convergence of ordered eigenvalues and eigenvectors in law. The counterexample is k=1, beta=2. The proof works for every fixed positive scaling constant gamma, not just the particular gamma proposed there.

## Source-compatible ensemble

In CIK's convention let

 W(x)=x^4/20-4x^3/15+x^2/5+8x/5,

and take the unitary ensemble with density proportional to exp(-n tr W(M)). Its eigenvalue density is proportional to exp(-n sum W(lambda_i)) product_{i<j}|lambda_i-lambda_j|^2.

Thus in the KRV convention beta=2 and V=W/2. Its random Jacobi matrix T_n is obtained from these eigenvalues and independent Dirichlet(1,...,1) spectral weights, exactly as KRV specifies. Its eigenvalues equal those of M. CIK Example 1.2, equations (1.4)-(1.5), PDF p.2 gives equilibrium support [-2,2] and density

 rho(x)=(1/(10pi))(x+2)^(1/2)(2-x)^(5/2) 1_{[-2,2]}.

The top edge E=2 therefore has k=1. In particular it is not a uniformly convex regular-edge example.

For completeness, the equilibrium formula can be verified independently. Let R(z)=sqrt(z^2-4), analytic off [-2,2] and R(z)~z at infinity, and set

 G(z)=(1/2)[W'(z)-(1/5)(z-2)^2 R(z)].

Expansion at infinity gives G(z)=1/z+O(1/z^2). Its upper/lower boundary values have difference -2pi i rho(x), and their sum equals W'(x). Thus G is the Stieltjes transform of the positive probability density rho; uniqueness follows by the usual jump and infinity argument (subtract the integral transform; the endpoint square roots give removable bounded singularities). Its effective potential W(x)-2 integral log|x-y|rho(y)dy is constant on [-2,2]. Off this interval its derivative is (1/5)(x-2)^2 R(x), positive for x>2 and negative for x<-2, so the variational inequality is strict off support. These are the equilibrium Euler-Lagrange conditions, sufficient for the unique logarithmic-energy minimizer. There are no interior zeros of rho, the left edge is regular, and the right edge has precisely order 5/2.

An affine change x=2y gives W(2y)=2V_*(y), where V_*(y)=2y^4/5-16y^3/15+2y^2/5+8y/5 is the September witness. The identity is also in TailAlgebra.lean; its checked status is reported separately.

## Two rigorously incompatible spectral tails

### 1. Every nontrivial additive Gaussian potential has at least a Gaussian tail in this direction

Use the Dirichlet realization of S_2,1 constructed in ATTEMPT.md. Choose a deterministic real smooth f supported in (1,2), ||f||_2=1. Its form value is

 q(f)=A+Z,
 A=integral (|f'|^2+t^(1/3)f^2)dt,
 Z=sqrt(2) integral t^(-1/3)f(t)^2 dB(t).

Z is a centered real normal random variable with strictly positive finite variance sigma^2=2 integral t^(-2/3)f^4 dt. This does not involve a stochastic integral of an adapted random eigenfunction: f is fixed and deterministic. The distributional noise pairing agrees with this stochastic integral by integration by parts. Rayleigh-Ritz gives lambda_0<=q(f). Thus for all large r,

 P(lambda_0<-r) >= P(Z<-r-A) >= exp(-C r^2). (A)

The final elementary inequality follows by integrating the standard normal density over [z,z+1/z] with z=(r+A)/sigma, as proved in ATTEMPT.md. Constants are deterministic and finite. This holds regardless of the singular endpoint because the trial function is supported away from it. The stronger optimized bound exp(-C r^(7/6)) is proved in ATTEMPT.md, but is unnecessary for this contradiction.

### 2. Local beta=2 kernel convergence forces a much smaller tail for any proposed lowest eigenvalue limit

Claeys-Vanlessen, arXiv:math-ph/0607043, Theorem 1.7, PDF pp.6-7 proves that for a type-III 5/2 edge, with zero deformation parameters, there is c0>0 such that

 Ktilde_n(u,v)=(1/(c0 n^(2/7))) K_n(E+u/(c0 n^(2/7)),E+v/(c0 n^(2/7)))
   -> K_crit(u,v)

uniformly on compact subsets of R^2. The critical quartic is EXACTLY CV Example 1.2, PDF p.5, equation (1.28), with V0=W, V1(x)=x and V2(x)=x^3-6x. Take deformation parameters s=t=0 for every n. Thus it satisfies their Assumptions 1.1. Independently: the uniformly confining quartic leading term proves (i); h0(x)=(x-2)^2/5 has h0(2)=h0'(2)=0, h0''(2)=2/5>0 and h0(-2)=16/5>0, giving (ii) together with the equilibrium verification above. For (iii), under u=2cos(theta), the critical integral of sqrt((u+2)/(2-u)) V2'(u) du becomes integral_0^pi (2+2cos(theta))(12cos(theta)^2-6)dtheta=0 (odd cosine moments vanish and integral cos^2=pi/2). All three requirements are checked.

The associated critical kernel has

 0 <= K_crit(u,u) <= C0 exp(-c1 u^(7/2)) for u sufficiently large. (B)

Here is a direct proof in CV's own normalization. Their equations (3.41)-(3.42), PDF pp.20-21, identify the Phi-vector on the upper side of the positive axis with the first column of the RH matrix Psi and give its asymptotic expansion. The jump on the positive axis, equation (3.39), is upper triangular with unit diagonal, so its multiplication fixes the first column; the first-column asymptotic has the same boundary value there. At s=t=0, equation (1.21), PDF p.4, gives theta(u)=u^(7/2)/105. Hence ||Phi(u)||<=C u^(1/4) exp(-u^(7/2)/105) for u>=u0. Equations (1.15)-(1.17), PDF p.4, give Phi'(u)=U(u)Phi(u), with U a polynomial matrix of degree at most 3 and finite coefficients (the distinguished solution has no real poles). Thus ||Phi'(u)||<=C' u^(13/4) exp(-u^(7/2)/105). Taking the diagonal limit in the integrable-kernel formula (1.34), PDF p.7, yields

 |K_crit(u,u)| <= (1/(2pi))||Phi(u)|| ||Phi'(u)||
   <= C'' u^(7/2) exp(-2u^(7/2)/105)
   <= C''' exp(-u^(7/2)/105)

after enlarging u0. This proves (B) with positive exponent constant. Nonnegativity follows as the local uniform limit of the nonnegative diagonal finite-n correlation kernels. No differentiation of an uncontrolled asymptotic error has been used. CIK equation (1.23), PDF p.5, explicitly records the same positive-axis exponential scale in its normalization and independently confirms the direction of the bound. No equality between the CV and CIK normalization constants is needed.

Now suppose the conjectured ordered-eigenvalue convergence holds for any gamma>0. Write L_n=gamma n^(2/7)(E-lambda_max(M_n)); it is the lowest eigenvalue of H_n. By the conjecture L_n converges in law to lambda_0 of S_2,1. Put d=c0/gamma>0. For fixed R>r sufficiently large, the event L_n in (-R,-r) implies that the scaled matrix point process has a point in (dr,dR). Markov's inequality for the nonnegative integer count gives

 P(L_n in (-R,-r)) <= E[number of points in (dr,dR)]
   = integral_dr^dR Ktilde_n(u,u)du.

Uniform convergence on this fixed compact interval implies convergence of the right side to integral_dr^dR K_crit(u,u)du. The Portmanteau theorem for the open interval (-R,-r) gives

 P(lambda_0 in (-R,-r)) <= liminf P(L_n in (-R,-r))
   <= integral_dr^dR K_crit(u,u)du.

Let R increase to infinity. Since lambda_0 is finite almost surely, continuity from below yields

 P(lambda_0<-r) <= integral_dr^infinity K_crit(u,u)du
   <= C2 exp(-c2 r^(7/2)). (C)

For the final estimate, split exp(-c1 u^(7/2)) into two equal exponent factors; one factor is at most exp(-(c1/2)(dr)^(7/2)), and the other is integrable on [0,infinity). Thus C2 is finite and c2>0. This reasoning uses only locally uniform kernel convergence and the proposed lowest-eigenvalue convergence. It does NOT assume that CIK's displayed largest-eigenvalue convergence equation (1.15) has been proved, nor does it require a uniform finite-n tail estimate or interchange the n and r limits.

### Contradiction

Combining (A) and (C) would give

 exp(-C r^2) <= C2 exp(-c2 r^(7/2))

for every sufficiently large r. Taking logarithms gives c2 r^(7/2)-C r^2<=log C2, impossible since r^(7/2)/r^2=r^(3/2)->infinity. In particular the conjectured ordered-eigenvalue limit is impossible for this source-compatible k=1,beta=2 ensemble. Any fixed positive affine shift or rescaling leaves this power mismatch intact. Consequently the operator-convergence claim with its explicitly stated eigenvalue consequence is false as posed.

## Hostile-referee checklist

- Actual beta-ensemble: exp(-beta n sum V) with beta=2,V=W/2, and the exact Dirichlet spectral-weight tridiagonalization. Eigenvalue identity is exact, not approximate.
- Equilibrium exponent: explicitly 5/2, with positive quartic leading coefficient and strict off-support inequality.
- General-beta quantifier: one admissible beta=2 example suffices to refute a conjecture covering every fixed beta>0.
- Gaussian form event: a single deterministic test function; no independence assumptions about eigenvalues or stochastic eigenfunctions.
- Endpoint: support of the test function avoids zero; any fixed local boundary convention admitting compactly supported interior functions has the same lower bound.
- Source details: KRV Conjecture 45 explicitly requires Dirichlet boundary and convergence of ordered bottom eigenvalues; this is the source-faithful refinement.
- Scaling constants: arbitrary gamma>0, and c0>0 from the local-kernel theorem, so differing phase conventions cannot remove the contradiction.
- Limits: n tends to infinity for fixed r,R; then R tends to infinity; only finally r tends to infinity. No unproved largest-eigenvalue distribution theorem is invoked.
- Positive-axis tail rather than gap tail: large negative operator eigenvalue corresponds to a matrix point ABOVE its top edge, so it is the kernel's positive u asymptotic, not the negative-s large-gap asymptotic.
- Dependence on prior work: no September Hessian/Gaussian-approximation claim is used. The proof uses equilibrium data from primary literature, a local determinantal theorem, and a Gaussian trial-function bound.
- Formalization: TailAlgebra.lean checks only potential rescaling and elementary exponent algebra, conditional on a successful kernel check. It does not formalize stochastic analysis or the literature theorems.
- Primary-source audit completed: CV Assumptions 1.1 and exact Example 1.2 on PDF p.5; Theorem 1.7 on pp.6-7; positive-axis RH equations (3.39)-(3.42) on pp.20-21; Lax equations (1.15)-(1.17) and phase (1.21) on p.4. The proof is complete subject to these cited published theorems, with no remaining mathematical gap. Formal algebra checking is an additional check, reported separately.


# Auxiliary operator results

## A partial theorem: construction and leading spectral growth

Fix an integer k >= 0 and beta > 0. Put a=1/(2k+1), p=k/(2k+1), c=2/sqrt(beta). For standard Brownian motion B define W(t)=integral_0^t s^(-p) dB(s). Since 2p<1, W has a continuous version on [0,infinity), W(0)=0. Use the Dirichlet boundary condition at zero. With probability one the form

 q(f)=integral (|f'|^2+t^a|f|^2)dt + c <W',|f|^2>

on D={f in H_0^1(0,infinity): integral t^a |f|^2 dt < infinity} has a rigorous closed, lower-bounded realization. Its associated self-adjoint operator has compact resolvent. If N(lambda) counts eigenvalues strictly below lambda, with multiplicity, then

 N(lambda) ~ C_a lambda^(1/a+1/2),
 C_a=(1/pi) integral_0^1 sqrt(1-s^a) ds.

This fixes one boundary condition; no source boundary condition has yet been verified.

### Proof of the pathwise noise estimate

For each integer j>=0 define d_j=W(j+1)-W(j), let L be the piecewise affine interpolation of W at the integers, and put R=W-L. Then R vanishes at integer endpoints. Write M_j=sup_{[j,j+1]} |R|. The integrated noise on interval j>=1 has variance at most j^(-2p). Its increments have the law of Brownian motion with deterministic clock of length at most j^(-2p). The reflection bound gives

 P(sup_{[j,j+1]}|W(t)-W(j)| > u j^(-p)) <= 4 exp(-u^2/2).

Consequently, by Borel-Cantelli (take u=sqrt(6 log(j+2))), almost surely, for all sufficiently large j,

 |d_j| <= sqrt(6 log(j+2)) j^(-p),
 M_j <= 2 sqrt(6 log(j+2)) j^(-p).

M_0 is finite by continuity; there is no use of the singular derivative of s^(-p) at zero. Thus M_j^2/(1+j^a) -> 0 and |d_j|/(1+j^a) -> 0, including p=0 because log(j)/j^a -> 0.

Define the noise pairing, first for smooth compactly supported Dirichlet functions, by

 I(f)=sum_j d_j integral_j^(j+1)|f|^2 dt - 2 Re integral_0^infinity R(t) conjugate(f(t)) f'(t) dt.

This equals -integral W (|f|^2)' by integration by parts with L, since endpoint terms vanish; R vanishes at the internal integer endpoints. For every eta>0 there is a finite random K_eta such that

 |c I(f)| <= eta integral (|f'|^2+t^a|f|^2) dt + K_eta ||f||_2^2. (1)

Indeed, choose epsilon=eta/2 in Young's inequality to bound 2c M_j |f f'| by epsilon |f'|^2 + c^2 M_j^2/epsilon |f|^2. The coefficient c|d_j|+c^2 M_j^2/epsilon, divided by t^a on [j,j+1], tends to zero. Outside a finite interval it is at most eta t^a/2. On the remaining intervals it has a finite maximum, absorbed in K_eta. This proves (1).

The series for the first term and the integral for the second are absolutely convergent on D: |d_j| and M_j^2 are bounded by a constant times 1+t^a, and Cauchy-Schwarz applies to M_j f and f'. The same estimates and polarization give a continuous symmetric sesquilinear noise form on D. Compactly supported smooth Dirichlet functions are dense in D: cut off at infinity with uniformly bounded cutoff derivatives, use dominated convergence, then use the usual H_0^1 density on a bounded interval where t^a is bounded. Thus the extension agrees with the distributional expression.

### Closedness, lower bound, compactness

The deterministic form q0(f)=integral (|f'|^2+t^a|f|^2) on D is closed: its form norm is the intersection norm of H_0^1 and the weighted L2 space, both complete, and their limits coincide in L2. Taking eta=1/2 in (1) shows q is lower bounded and that q+(K_1/2+1)||f||^2 has norm equivalent to q0+||f||^2. Hence it is closed. The representation theorem for closed semibounded forms gives the stated self-adjoint operator.

The embedding of D with the deterministic form norm into L2 is compact. On [0,A] use Rellich compactness. On [A,infinity), integral |f|^2 <= A^(-a) integral t^a|f|^2, uniformly on bounded form-norm sets. A diagonal subsequence on bounded intervals and this tail estimate give an L2-convergent subsequence. Equivalent form norms give compact resolvent for the random operator.

### Deterministic Weyl law and transfer to the random operator

Let H0=-d^2/dt^2+t^a with Dirichlet boundary. At energy lambda>0 set T=lambda^(1/a). Partition [0,T] into m equal intervals. Dirichlet insertion increases eigenvalues, so the sum of counts for constant potentials lambda((i+1)/m)^a with Dirichlet endpoints is a lower bound for N0(lambda). Neumann splitting decreases eigenvalues; constant potentials lambda(i/m)^a with Neumann endpoints give an upper bound. The tail [T,infinity) has potential >=lambda and nonnegative derivative energy, so contributes no eigenvalues strictly below lambda. Each finite-interval constant-potential count differs by at most 1 from

 (T/m)(sqrt(lambda)/pi) sqrt(1-(i/m)^a)

or its right-endpoint analogue. Therefore lower and upper bounds, divided by lambda^(1/a+1/2), converge for fixed m to the right and left Riemann sums of (1/pi)sqrt(1-s^a). Let m tend to infinity. This proves the asserted asymptotic for H0, without a differentiability assumption on the potential.

For every 0<eta<1, (1) gives the form inequalities

 (1-eta)H0-K_eta <= H <= (1+eta)H0+K_eta.

The min-max principle yields

 N0((lambda-K_eta)/(1+eta)) <= N(lambda) <= N0((lambda+K_eta)/(1-eta)).

The Weyl law for H0 bounds the normalized lower/upper limits by C_a(1+eta)^(-1/a-1/2) and C_a(1-eta)^(-1/a-1/2). Let eta decrease to zero. This completes the partial theorem.

## Hostile-referee checks and limitations

1. Endpoint singularity: square integrability requires 2p<1, which holds with margin 1/(2k+1). A derivative of the weight would be singular and was never used.
2. k=0: increment bounds grow like sqrt(log j), rather than decaying. The estimate uses their square divided by j^a, so this case is included.
3. Constants depend on the Brownian sample and eta; no uniform statement in beta, k, or sample is asserted.
4. Boundary condition: Dirichlet was imposed explicitly. Other source choices must be checked before any comparison to the conjecture.
5. The leading counting exponent is 2k+3/2, consistent with integrating a density vanishing to order 2k+1/2. This consistency does not prove a limiting point process or scaling constants.
6. The probabilistic and analytic proof above is not Lean-checked. It uses the reflection bound, Borel-Cantelli, Rellich compactness, closed-form representation, and min-max; these applications have been spelled out.
7. The displayed source conjecture and analytic critical-edge context are verified. Its referenced refinement, normalization, matrix law, topology and boundary data still require inspection, and whether later work proves the full claim remains unverified. Neither the generic Airy case nor a constructed discretization would solve those missing matrix statements.


## A new tail obstruction, proved on the operator side

For the same candidate operator, there are deterministic positive constants C and r0, depending on k,beta and a fixed trial function, such that

 P(lambda_min(H)<-r) >= exp(-C r^(3/2-p)), r>=r0, p=k/(2k+1). (2)

Proof. Choose a real smooth normalized f compactly supported in (1,2). Set A=integral |f'|^2, D=integral x^a f(x)^2 dx, J=integral x^(-2p) f(x)^4 dx>0. For h>0 let f_h(t)=h^(-1/2)f(t/h). Its deterministic form energy is A h^(-2)+D h^a. Its noise form equals c integral t^(-p)f_h(t)^2 dB(t), a centered Gaussian of variance c^2 J h^(-1-2p). The distributional pairing agrees with this stochastic integral for this fixed deterministic smooth trial function.

Set h=r^(-1/2). The event that this Gaussian is less than -[(1+A)r+D r^(-a/2)] makes q(f_h)<-r, and the variational principle gives lambda_min<-r. The Gaussian threshold in standard-deviation units is

 z_r=[(1+A)r+D r^(-a/2)]/(c sqrt(J) r^((1+2p)/4)).

For r>=1 it is positive and at most C1 r^((3-2p)/4), and tends to infinity. For z>=1,

 P(Z<-z) >= (1/(sqrt(2pi) z)) exp(-(z+1/z)^2/2),

by integrating the standard normal density from z to z+1/z. Its logarithm is bounded below by -C2 z^2 for all z>=1. Substitute z=z_r and enlarge constants. This proves (2) in full. The trial functions have support away from zero for each r, so no endpoint stochastic integration subtlety is involved. They satisfy any fixed Dirichlet or local homogeneous endpoint condition.


Final referee result (2026-10-12): all source hypotheses, the actual beta=2 eigenvalue density, positive-axis kernel decay, Gaussian trial-function law, and the order n -> infinity then R -> infinity then r -> infinity were checked analytically. The proof avoids the expected/unproved largest-eigenvalue limit in CIK. Exact rational checks passed. The single restarted lake env lean attempt timed out after its full 3600-second allowance. TailAlgebra.lean remains UNVERIFIED; no declaration is counted Lean-checked. Its potential-rescaling and exponent arithmetic were separately checked exactly in Python. The formalization/checking gap is computational only: there is no missing mathematical step in the written analytic counterexample. The stochastic and Riemann-Hilbert arguments remain analytic, not Lean-formalized. No mathematical gap remains in the counterexample; the correct replacement operator and worldwide novelty are not established.
