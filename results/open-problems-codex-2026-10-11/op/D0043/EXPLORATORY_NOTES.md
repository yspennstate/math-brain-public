# Archived exploratory notes, superseded by ATTEMPT.md

These notes preserve the earlier stage of the 2026-10-12 attempt. Their statements that the matrix conjecture remained unproved/unrefuted were superseded by the complete counterexample subsequently written in ATTEMPT.md and COUNTEREXAMPLE.md. They are retained as history, not as the final verdict.

# D0043 — research attempt, 2026-10-12

## Scope and source status

The requested matrix convergence conjecture has not been proved or disproved here. Conjecture 5 and its immediate analytic-potential context have been verified on source PDF page 14; it does not itself enumerate scaling, topology or boundary data, instead referring to [38]. Later literature retrieval remains incomplete. The theorem below concerns the candidate differential expression only; it does not establish convergence of any matrix ensemble. No claim of a solution in the literature is made. Prior repository paths show that related operator-construction work was already recorded in September; no novelty is claimed for this partial theorem.

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

## Precise remaining gap

Even after the candidate operator is constructed, one must prove that the particular tridiagonal random matrices from the source, under its critical-edge assumptions and appropriate scaling, converge to this operator (including the correct boundary condition and constants). This requires actual coefficient asymptotics, joint fluctuation control, and tightness/confinement estimates for that ensemble. No such estimate has been obtained here.

## A new tail obstruction, proved on the operator side

For the same candidate operator, there are deterministic positive constants C and r0, depending on k,beta and a fixed trial function, such that

 P(lambda_min(H)<-r) >= exp(-C r^(3/2-p)), r>=r0, p=k/(2k+1). (2)

Proof. Choose a real smooth normalized f compactly supported in (1,2). Set A=integral |f'|^2, D=integral x^a f(x)^2 dx, J=integral x^(-2p) f(x)^4 dx>0. For h>0 let f_h(t)=h^(-1/2)f(t/h). Its deterministic form energy is A h^(-2)+D h^a. Its noise form equals c integral t^(-p)f_h(t)^2 dB(t), a centered Gaussian of variance c^2 J h^(-1-2p). The distributional pairing agrees with this stochastic integral for this fixed deterministic smooth trial function.

Set h=r^(-1/2). The event that this Gaussian is less than -[(1+A)r+D r^(-a/2)] makes q(f_h)<-r, and the variational principle gives lambda_min<-r. The Gaussian threshold in standard-deviation units is

 z_r=[(1+A)r+D r^(-a/2)]/(c sqrt(J) r^((1+2p)/4)).

For r>=1 it is positive and at most C1 r^((3-2p)/4), and tends to infinity. For z>=1,

 P(Z<-z) >= (1/(sqrt(2pi) z)) exp(-(z+1/z)^2/2),

by integrating the standard normal density from z to z+1/z. Its logarithm is bounded below by -C2 z^2 for all z>=1. Substitute z=z_r and enlarge constants. This proves (2) in full. The trial functions have support away from zero for each r, so no endpoint stochastic integration subtlety is involved. They satisfy any fixed Dirichlet or local homogeneous endpoint condition.

For k=1, exponent 3/2-p=7/6. The beta=2 critical-edge point process is expected to have upper-edge tail bounded above by exp(-c r^(7/2)). These exponents are incompatible under any fixed positive affine rescaling. HOWEVER, the random-matrix upper bound, its matching ensemble hypotheses, and the precise spectral convergence implication have not yet been verified from the downloaded papers. Thus this is presently a proved operator-side bound and a conjectural counterexample route, not a certified refutation of Conjecture 5.
