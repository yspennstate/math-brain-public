# C0056 referee attempt, 2026-10-10

## Precise scope

Bourgade's 2018 Section 2.1 considers an iid centered variance-one lattice potential in the discrete Anderson operator and separately discusses finite periodic boxes and GOE microscopic bulk statistics. The 2026-09-07 intake combines absolutely continuous spectrum in d=3 with GOE. A 2026-09-23 author preprint claims a nonzero purely absolutely continuous interval for the narrower iid uniform [-1,1] law in every fixed d>=3. I located its theorem but did not verify its long proof. The present a.c. status is UNKNOWN. The preprint's theorem does not assert GOE.

## Brain-assisted bridge and exact mismatch

`python -X utf8 probe_brain.py` made three bounded, read-only `rg -m 3` queries against the exported math-brain nodes; the recorded run is `retrieval_measure.json`. The target query took 21.188 s and returned two dated C0056 records plus one irrelevant card. The bridge query took 3.098 s and returned an approximate-identity card and Weyl's lemma; **0/2** supplies a fixed-positive-disorder, eta-to-zero estimate. The measure-theory query took 8.777 s and returned three general cards. The approximate-identity card requires an L1-normalized family, uniform L1 norms and vanishing tails; the Poisson kernel has these properties. Applying it to a spectral measure gives weak convergence to that measure, which may be singular. The Lebesgue-decomposition card assumes sigma-finite measures and decomposes absolute-continuous and singular parts; it does not show that the singular part vanishes. The missing input is control of samplewise concentration as eta decreases to zero.

## Independently checked sufficient route

For a random finite positive spectral measure mu_omega, define f_eta(omega,E)=eta/pi times the integral of ((t-E)^2+eta^2)^(-1) against mu_omega. A uniform joint Lp bound, p>1, on compact J inside I implies local uniform integrability. Weak compactness in L1(P x J), event-weighted continuous tests and the Poisson approximate identity then imply mu_omega|I is absolutely continuous almost surely. The event weights are essential: an averaged spectral measure can have a density while each sample is an atom.

The cavity route in w489's packet gives a concrete sufficient input. With iid bounded-density site variables of density rho, a fixed lambda>0 and x removed, set M_x(z)=z+<b_x,(H^x-z)^(-1)b_x> and Gamma_x=Im M_x>0. The Schur complement gives G_xx(z)=1/(lambda V_x-M_x(z)). Conditioning on all variables except V_x and integrating the own-site variable yields, for p=1+q>1,

E[(Im G_xx)^p | complement] <= ||rho||_infinity c_p Gamma_x^(-q)/lambda,

where c_p=integral_R(1+u^2)^(-p)du. Thus a fixed-lambda bound on E integral_J Gamma_x^(-q) uniformly for 0<eta<1 would imply local Lp densities of all basis spectral measures, and hence pure a.c. spectral type on I. It would **not** imply nonzero spectral weight or GOE statistics. This negative-moment bound for the cyclic Z^3 cavity operator is the single hardest unsupplied input in this sufficient route. The recent preprint may use a different certificate; this packet does not assert its proof needs this exact bound.

w490's `UI_SEPARATION.md` demonstrates that the p>1 route is stronger than absolute continuity. The probability density g(E)=1/[E(log(1/E))^2] on (0,e^-1) has L1 mass one but belongs to no Lp for p>1. Its Poisson transforms converge in L1 and are uniformly integrable, yet Fatou makes every local pth Poisson moment unbounded. I independently checked the substitution u=log(1/E). The lack of a cavity negative-moment bound would not refute C0056.

## Independently derived warning for the GOE branch

The free nearest-neighbor Laplacian on Z^3 has purely a.c. spectrum: Fourier transform makes it multiplication by -2 sum_j cos k_j, and for each fixed (k_2,k_3), the pushforward in k_1 has an a.c. arcsine density. Fubini gives null preimages for every Lebesgue-null energy set, for every scalar spectral measure. Yet on a periodic L^3 torus, the eigenvalues indexed by k and -k coincide; at most 8 momentum indices are fixed by negation. Among the L^3 ordered eigenvalues there are at least (L^3-8)/2 zero adjacent gaps, so the empirical zero-gap proportion is at least 1/2-O(L^-3). This free, deterministic example shows that a.c. spectral type alone cannot force GOE finite-volume gaps. It is outside the positive-disorder iid target. This new w491 lemma needs independent w494 review before theorem-node promotion.

NEXT: Obtain an independently audited, fixed-positive-disorder estimate or certificate reaching eta=0 for the actual Z^3 model; treat GOE as a separate obligation.
