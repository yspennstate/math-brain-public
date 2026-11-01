# C0056 independent route, saved before reading w483 or w484 proofs

Date: 2026-10-10. The Bourgade 2018 source separates infinite-volume a.c. spectrum from finite-volume GOE statistics. The September 2026 OpenAI preprint claims the a.c. branch for uniform site potentials, with mathematical verification pending; it leaves GOE aside. I will assess peer proofs with this split.

## Time-domain route to the a.c. branch

Let H be any bounded self-adjoint operator, e a unit vector, and mu_e its spectral measure. Choose a real nonnegative smooth cutoff phi with compact support inside an energy interval I. Put nu(dE)=phi(E)mu_e(dE) and A_phi(t)=<e,e^{-itH}phi(H)e>=int exp(-itE)nu(dE). A sufficient condition for nu to have an L2 density almost surely is

    E[int_R |A_phi(t)|^2 dt] < infinity.                         (TD)

Indeed Fubini makes A_phi an L2 function of t almost surely. Plancherel for finite measures then makes nu an L2(E) density. If phi is strictly positive on J subset I, mu_e restricted to J is a.c. This is a conditional deterministic/annealed criterion, not an assertion that (TD) holds for the Anderson model. For the operator-level pure a.c. statement, it must hold simultaneously for every delta_x (a countable family) and cutoffs covering J. Positive spectral weight is a separate obligation. The GOE branch requires a separate argument.

The equivalent Poisson-smoothed identity, with P_eta(E)=eta/[pi(E^2+eta^2)], is

    int_R |P_eta*nu(E)|^2 dE = (1/2pi) int_R exp(-2eta|t|)|A_phi(t)|^2 dt.

It follows directly from the Fourier transform of P_eta and Plancherel. Thus (TD) needs an all-time estimate at fixed lambda. A kinetic-scale estimate uniform only for |t|<=T(lambda) does not establish it.

## Concrete finite-time obstruction

Let H_0 be nearest-neighbor adjacency on Z^3 and H_L the same adjacency on a finite torus of side L. For all k<L, the moments <delta_0,H_L^k delta_0> and <delta_0,H_0^k delta_0> agree: a walk of fewer than L steps cannot wrap around the torus. Expand exp(-itH) into a degree-(L-1) Taylor polynomial. Since both operator norms are <=6, for each fixed T,

    sup_{|t|<=T} |<delta_0,e^{-itH_L}delta_0>-<delta_0,e^{-itH_0}delta_0>|
        <= 2 sum_{k>=L} (6T)^k/k! -> 0.

Every H_L has pure-point spectrum. H_0 has a.c. local spectral measure (push-forward of uniform measure on the 3-torus by 2 sum_j cos theta_j; convolution of three arcsine laws). So arbitrarily accurate finite-time return amplitudes do not determine infinite-time spectral type. This is a proved special-case obstruction to a proposed inference, not a result about random disorder.

## Hardest missing step and next work

Prove (TD) at fixed small lambda, uniformly enough to cover an energy interval, or find a weaker time-domain criterion that retains singular-spectrum exclusion. The present kinetic-regime literature and 2018 local attempt do not provide this. Any GOE conclusion needs microscopic eigenvalue correlations and cannot follow merely from a.c. spectrum. Audit the September 2026 preprint before treating its a.c. claim as established.

## Disjoint GOE obstruction

The free adjacency operator H_0 on Z^3 has purely a.c. local spectral measures, with density f_1*f_1*f_1. Periodic-box restrictions H_{0,L} are deterministic matrices. For any fixed energy E where the free density is positive (for example E=0), their unfolded local eigenvalue point processes are deterministic. Any distributional limit of deterministic point processes is a Dirac law, while the GOE bulk point-process law is nondegenerate. Thus a.c. spectrum alone cannot imply GOE statistics. This is a proved zero-disorder special case, not a statement about iid disorder at fixed lambda>0.
