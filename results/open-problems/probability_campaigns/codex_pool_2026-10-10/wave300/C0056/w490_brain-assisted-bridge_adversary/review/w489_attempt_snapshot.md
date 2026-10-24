# C0056: cavity escape width and spectral absolute continuity

2026-10-10. Native prover w489; adversary w490; referee w491. All results below are draft campaign mathematics pending independent review. No claim that C0056 is solved, no novelty claim, and no live-store promotion.

## Exact problem and scope

The intake's C0056 requests both weak-disorder absolutely continuous spectrum on Z^3 and GOE microscopic statistics for a finite-volume restriction. Bourgade's 2018 primary Section 2.1 uses H=Delta+lambda V, iid centred variance-one real site variables, and periodic boxes. Its discussion is a research question rather than a theorem with a universally quantified single-site class. An explicit specialised model is required before a proof can be evaluated.

This packet takes H=-A+lambda V on l2(Z^3), A the six-neighbour adjacency operator, V_x iid Uniform[-1,1], lambda>0 fixed. This law has variance 1/3; writing W_x=sqrt(3)V_x and alpha=lambda/sqrt(3) gives the primary's variance-one convention. The bipartite unitary reverses the hopping sign. We seek a nonzero absolutely continuous spectral restriction on a deterministic bounded nonempty open interval I at fixed sufficiently small lambda. We do not derive GOE statistics from this condition. The September 23, 2026 primary preprint claims the uniform-law spectral assertion; its complete certificate is not audited here, so current openness is UNKNOWN.

## Prior attempt and retrieved-obstruction digest

C0056-A001 (2026-09-07) explored perturbation and a spanning-tree transfer, without a proof or independent check. It identifies the missing closed lattice recursion and the fixed-coupling infinite-time gap. Deleting lattice edges changes the operator; independent forward branches available on a tree cannot be assumed on the lattice. Targeted searches of the named H/I attempts found no further C0056/Anderson proof; the Lean annotated ranking repeats attempted_un and is not a theorem receipt.

Personal-brain recall was limited to 60 seconds and timed out. The required scar perceptron_proof_open_gaps_fleet_2026_07_12 was read directly after the memory-index search found no relevant entry. Its applicable lesson is to identify the hardest unchecked piece and distinguish successful validation of one part from completion of the entire proof. No conditional probabilities are multiplied here.

## L1: first moments do not exclude atoms

For mu=delta_0 its unnormalised Poisson transform is P_eta(E)=eta/(E^2+eta^2). Direct substitution gives integral_R P_eta=pi and integral_R P_eta^2=pi/(2 eta). Thus a bounded first energy moment is consistent with a purely atomic measure. The second equality exhibits the obstruction at heights tending to zero. This example concerns a scalar spectral measure and is not a counterexample to the lattice conjecture.

## L2: an annealed density can conceal purely atomic sample measures

Let S be Uniform[-1,1], let H_S be multiplication by S on a one-dimensional Hilbert space, and let mu_S=delta_S. Each sample spectral measure is atomic, but E mu_S has density (1/2)1_[-1,1]. For every E and eta>0,

E Im(S-E-i eta)^(-1)=(1/2) integral_[-1,1] eta/((s-E)^2+eta^2) ds <= pi/2.

This follows by extending a nonnegative integral to R. A uniform bound on the expected scalar imaginary part therefore cannot be promoted to samplewise absolute continuity. Conditioning on the other variables does not alter this one-dimensional counterexample.

## L3: a higher Poisson moment is sufficient

Let mu_omega be random positive Borel measures of mass at most one, let I be a bounded open interval, and let p>1. Define P_omega,eta(E)=integral eta/((t-E)^2+eta^2) dmu_omega(t). Assume for a fixed deterministic sequence eta_n decreasing to zero that

sup_n E integral_I P_omega,eta_n(E)^p dE <= C < infinity.

Then almost surely mu_omega restricted to I has an Lp density f_omega, and E integral_I |f_omega|^p <= C/pi^p.

Proof. Put X_n=integral_I P_eta_n^p. Fatou gives E liminf_n X_n<=C, hence liminf X_n is finite almost surely. For such a sample, choose a subsequence along which X_n tends to its finite lower limit. Boundedness in reflexive Lp(I) gives a weakly convergent further subsequence, with limit h. For each phi in C_c(I), extend phi by zero to R. The normalised Poisson convolution of phi converges uniformly to phi. Fubini, and the bound on total measure, therefore give lim integral_I phi P_eta_n=pi integral phi dmu. Weak convergence identifies h dE=pi dmu on I. This proves absolute continuity on the whole open interval, not merely on a prescribed full-Lebesgue-measure subset. Weak lower semicontinuity gives pi^p ||f||_p^p<=liminf X_n. Fatou yields the expected norm bound. The density and its norm are measurable; for example, approximate identities give a jointly measurable representative and the norm bound also follows from a countable dense family of continuous tests. The hypothesis is on a genuine pth moment, not the pth power of an expectation.

## L4: conditional cavity negative moments supply L3

Let H be a bounded self-adjoint lattice Hamiltonian with bounded deterministic hopping, iid real site variables V_x of probability density rho in L-infinity(R), and diagonal lambda V_x with lambda>0 fixed. Bounded support is sufficient for boundedness and is imposed here. Delete site x to obtain the compression H^x. Write b_x for its hopping vector and

M_x(z)=z+<b_x,(H^x-z)^(-1)b_x>,
Gamma_x(E,eta)=Im M_x(E+i eta)>0.

For p=1+q with 0<q<1, the Schur complement and own-site independence give

G_xx(z)=(lambda V_x-M_x(z))^(-1),
E[(Im G_xx(E+i eta))^p | {V_y:y!=x}]
<= (||rho||_infinity/lambda) c_p Gamma_x(E,eta)^(1-p),
c_p=integral_R (1+u^2)^(-p)du=sqrt(pi) Gamma(p-1/2)/Gamma(p).

Proof. Freeze the complement so that M_x=a+i gamma is fixed and gamma>0. Integrate [gamma/((lambda v-a)^2+gamma^2)]^p against rho(v)dv, bound rho by its supremum, extend to all real v, and substitute u=(lambda v-a)/gamma. The result is exactly the displayed upper bound. This proof uses independence of the own-site variable from the full complement, not independence of different neighbours.

Consequently, if for every x and every compact interval J contained in I there is C_x,J<infinity such that

sup_{0<eta<1} E integral_J Gamma_x(E,eta)^(-q)dE <= C_x,J,

then almost surely every basis spectral measure is absolutely continuous on I, locally with L^(1+q) density. To prove it, apply the conditional inequality, Tonelli, and L3 to J's interior along eta_n=1/(n+1). Countably many intervals with rational endpoints exhaust I. Countably many sites give one event on which all site measures are absolutely continuous on I. If B is a null Borel subset of I then <delta_x,chi_B(H)delta_x>=0 for all x, so chi_B(H)delta_x=0 for every basis vector and chi_B(H)=0. This is precisely pure absolute continuity of the spectral restriction. This conclusion by itself permits the projection on I to vanish; nonzero mass must be established separately.

The hypothesis is an unproved sufficient condition for the lattice model, not a theorem asserting that the lattice satisfies it. It is stronger than the qualitative cavity-boundary-positivity route used in recent primary literature. No necessity is asserted.

## L5: the bounded-potential perturbation route stops at positive height

Take the six-neighbour lattice and ||V||_infinity<=1. Let H_lambda^x=H_0^x+lambda V^x. At z=E+i eta the resolvent identity and ||(H_lambda^x-z)^(-1)||<=1/eta give

||R_lambda^x(z)-R_0^x(z)||<=lambda/eta^2,
|Gamma_lambda,x(E,eta)-Gamma_0,x(E,eta)|<=6 lambda/eta^2.

The factor six is ||b_x||^2. If a free lower bound Gamma_0,x>=c>0 holds on an energy set and at the heights under consideration, this proves Gamma_lambda,x>=c/2 only when eta^2>=12 lambda/c. For a fixed positive lambda it leaves a whole interval of arbitrarily small heights uncontrolled. It cannot prove L4's supremum over all heights. The displayed restriction is sufficient, not a claimed necessary bound or a physical transition scale.

## Single hardest remaining mathematical gap

Establish, at a fixed sufficiently small positive lambda, a volume-free and height-free bound sup_eta E integral_J Gamma_x^(-q)<infinity for the actual cyclic Z^3 cavity operator on some interval with nonzero spectral weight. The calculations above reduce one sufficient route to this precise negative-moment estimate; they do not establish it. Positivity or first moments of the disorder average, a tree recursion, and the deterministic positive-height perturbation estimate do not supply it. GOE microscopic statistics need a separate argument even if this gap is closed.

NEXT: Compare the full hypotheses of the returned math-brain cards with L4, measure the mismatches, and package L1--L5 with the unproved gap for independent review.
