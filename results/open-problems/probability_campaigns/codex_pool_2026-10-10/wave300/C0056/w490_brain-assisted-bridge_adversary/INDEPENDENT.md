# C0056 independent obstruction and conditional bridge

Written on 2026-10-10 before reading w489's proof. Independent referee: w491, pending. This is not a solution of C0056 and does not assert novelty.

Target context recovered from the September 23 primary preprint's introduction: on l2(Z^3), H psi(x) = -sum over the six nearest neighbors of psi(y) + lambda V_x psi(x), with iid V_x uniform on [-1,1]. The preprint asserts that there are e_2 in (0,1/100) and lambda_3>0 such that for each fixed 0<lambda<lambda_3, almost surely the nonzero spectral restriction to I=(-6+e_2/2,-6+e_2) is purely absolutely continuous. I does not depend on lambda; the probability-one event may. This is a claimed result requiring proof review, not a verified retirement certificate. The older intake's exact formulation remains to be checked against this variant.

## Independent counterexample: an annealed bound can hide random atoms

Let X be uniform on [-1,1], let H_X act on C by multiplication by X, and let mu_X=delta_X be the spectral measure of the unit vector. Every realization has pure point spectrum. For eta>0 define

f_eta(X,E) = (1/pi) Im (X-E-i eta)^(-1) = eta / (pi ((X-E)^2+eta^2)).

For every real E and every eta>0, E[f_eta(X,E)] <= 1/2, by integrating the Poisson kernel against the density 1/2. At E=0 the expectation is arctan(1/eta)/pi. The averaged spectral measure is the uniform probability measure, although every realization is atomic. Thus a uniform bound on the first averaged imaginary resolvent moment alone cannot imply almost-sure absolute continuity. This scalar example refutes that generic implication; it is not a counterexample to the nearest-neighbor C0056 model.

The precise failure is lack of uniform integrability in the joint variables (X,E). Put J=[-2,2]. For M>=1 and 0<eta<1/(pi M), the set f_eta>M is |E-X|<r, where r=sqrt(eta/(pi M)-eta^2)<1. Hence the whole set lies inside J for every X, and

E integral_J f_eta 1_{f_eta>M} dE = (2/pi) arctan sqrt(1/(pi eta M)-1).

For each fixed finite M this tends to 1 as eta decreases to zero, so the family fails joint uniform integrability as strongly as possible. Also integral_R f_eta^2 dE=1/(2 pi eta), for every X.

## Candidate bridge: exact local uniform-integrability criterion

Let (Omega,F,P) be a standard probability space and omega -> mu_omega a measurable kernel of probability measures on R. Define f_eta(omega,E)=P_eta*mu_omega(E), where P_eta(u)=eta/(pi(u^2+eta^2)). Let I be a bounded open interval. The following are equivalent:

(A) For P-almost every omega, mu_omega restricted to I is absolutely continuous with respect to Lebesgue measure.

(B) For every closed interval J with positive length compactly contained in I,

lim_{M->infinity} sup_{0<eta<1} E integral_J f_eta 1_{f_eta>M} dE = 0.

All quantifiers are at a fixed operator/disorder parameter. An estimate only at eta above a positive disorder-dependent cutoff does not establish (B).

Proof of (B) => (A). On the finite measure space Omega x J, the f_eta have L1 norm at most 1. The Dunford-Pettis weak compactness criterion gives a weakly convergent L1 subsequence of f_{1/n}, with nonnegative limit h. For any measurable event A and any phi in C_c(interior J), Poisson smoothing and uniform convergence P_eta*phi -> phi give

E[1_A integral phi dmu_omega] = E[1_A integral_J phi(E) h(omega,E) dE].

Weak L1 convergence applies because 1_A phi is bounded. For each phi this identity for every A implies equality of the two random integrals almost surely. A countable dense collection of continuous compactly supported test functions fixes one probability-one event on which mu_omega=h(omega,E)dE on interior J. Exhaust I by countably many such interiors to get (A). This countable-test step is needed; testing only the averaged measure loses the random support.

Proof of (A) => (B). Choose a compact interval K inside I with J in its interior. Absolute continuity of mu_omega restricted to K implies that the joint kernel measure P(domega) mu_omega(dE)|K has an L1(P x Lebesgue) density g; its total mass is at most 1. The approximate-identity theorem gives P_eta*g -> g in joint L1. The contribution from mu_omega outside K is at most eta/(pi dist(J,R\K)^2) on J, so tends to zero in joint L1 there. Consequently f_eta -> g in L1(Omega x J) as eta decreases to zero. This yields uniform integrability for small eta; for eta>=epsilon the bound f_eta<=1/(pi epsilon) handles the remaining heights. This proves (B).

## A convenient sufficient estimate for the target

For a fixed lambda>0 and a bounded interval I, if some p>1 satisfies, for every J compactly contained in I,

sup_{0<eta<1} E integral_J ((1/pi) Im <delta_0,(H_lambda-E-i eta)^(-1)delta_0>)^p dE < infinity,

then Markov truncation bounds the joint tail by C_J/M^(p-1), giving (B). Stationarity transfers the same estimate to every delta_x. Intersecting countably many probability-one events and using that the delta_x form a complete orthonormal basis excludes singular spectral mass on I. Nonzero spectral weight is a separate requirement. Neither this estimate nor joint uniform integrability has been proved here for the 3D weak-disorder model. That is the hardest unresolved bridge in this lane.

Source for the target variant: https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/01-introduction.tex . All measure calculations and the criterion above were derived independently in this session; the Dunford-Pettis theorem and Poisson approximate-identity theorem are the stated analytic inputs. No formal-check receipt is claimed.
