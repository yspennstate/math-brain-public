# account02/B01 auto14 early mathematical checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Role: Oscillatory replacement. Full conjecture remains OPEN.

Attack: spend the previously proved global sub-half-Riesz currency as an absolute weighted-Fourier moment, then combine it with a source-disjoint two-bank rank-two bicore. No scalar law-uniform quadratic-phase decay is used; the phase-aligned-density refutation is preserved.

## Candidate theorem under proof

For any quadratic packet S=X_D^T C X_D+b^T X_D+c on independent cap-one original coordinates, put

F(C)=sum_{i!=j} C_ij^2.

The same fair-cut dichotomy behind QFORM-GLOBAL-OFFDIAG-SUBHALF-RIESZ-v1 gives, for every 0<beta<1/2,

W_beta(S):=integral_R |t|^(beta-1)|phi_S(t)| dt
 <= K_beta F(C)^(-beta/2),

K_beta=2 exp(beta/2)(4 pi)^beta/[beta(1-2 beta)].

Indeed the diffuse order-one minor branch has |phi(t)|<=min(1,B|t|^-1/2) with B=exp(1/4)(2pi)^(1/2)E_1^-1/4; the heavy-row branch has the same exponent from aggregate random-slope Plancherel. In either case

integral_R |t|^(beta-1) min(1,B|t|^-1/2) dt=2 B^(2beta)/[beta(1-2beta)],

and a fair cut has E_1>=F(C)/4.

If an independent/source-disjoint active bicore has original-coordinate banks I,J and rank-two physical cross matrix K with nonzero singular values kappa_1,kappa_2, Delta=kappa_1 kappa_2, while arbitrary self-curvature remains on both I and J, the two-bank Plancherel envelope is

|phi_bicore(t)|<=min(1,2pi/(sqrt(Delta)|t|)).

For Q=bicore+S, split the Fourier integral at T:

||phi_Q||_1 <=2T +(2pi/sqrt(Delta))T^-beta W_beta(S).

Optimizing T gives

||p_Q||_infinity <= D_beta Delta^(-1/[2(1+beta)]) F(C)^(-beta/[2(1+beta)]),

D_beta=(1+beta)/(pi beta) * [2pi exp(beta/2)(4pi)^beta/(1-2beta)]^(1/(1+beta)).

At beta=1/4, D_beta=22.1034183615 and

||p_Q||_infinity <=22.104 Delta^-2/5 F(C)^-1/10.

Next checks: (i) preserve conditioning on an arbitrary outside bank W, allowing affine leakage but no active I/J-D cross block; (ii) derive the spectral packet corollary F(C)>=(s-delta)^2 when C has one singular value >=s and max|C_ii|<=delta<s; (iii) apply the newest Claude Theorem D and the completed account03/B01 source-disjoint-square theorem to concrete comparison families.
