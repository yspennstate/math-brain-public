# Local order and thermodynamic limits (C3 and C4)

Independent derivation saved after C1/C2 and before reading the paired harmonic lemmas. These results are awaiting w533's independent check. They supply a concrete missing premise for passing a local order parameter to an infinite-volume limit; neither is a Riesz gas existence theorem.

## C3: a sufficient limit premise

Let P_n converge in law to P in the vague topology of locally finite point measures on R^d. Let Q be a bounded fundamental parallelepiped, and assume P(N(boundary Q)=0)=1. Assume the local counts N_n(Q) are uniformly integrable:

    lim_{K->infinity} sup_n E_{P_n}[N(Q) 1_{N(Q)>K}] = 0.

For a fixed reciprocal vector G, set Y_n = sum_{x in X intersect Q} exp(i G dot x). The functional is continuous at every point measure with no points on boundary Q. Therefore Y_n converges in distribution to Y. Since |Y_n| <= N_n(Q), the Y_n are uniformly integrable, and E Y_n -> E Y. The same argument gives E N_n(Q) -> E N(Q).

If liminf_n Re E Y_n >= c > 0, the limit has Re E Y >= c. If each P_n is invariant under the same full-rank lattice L, its weak limit has that invariance too, because translation of point measures is continuous. C1 then rules out invariance of P under all translations. No DLR assertion follows from these assumptions; passing a long-range Gibbs specification is a separate obligation.

## C4: explicit counterexample if uniform integrability is omitted

Take L=Z^3, Q=[-1/2,1/2)^3 and G=2*pi*e_1. For each integer n>=3 and each z in Z^3, independently activate cell z+Q with probability 1/n. In an activated cell put n distinct points

    z + (j/n^2)e_1,  j=1,...,n,

and put no points in an inactive cell. Call this law P_n. It is simple, locally finite, and invariant under translations by Z^3. Independence here is part of the explicit construction, not an assertion about the Gibbs gas.

For every n, E N(Q)=1. Yet any fixed compact set meets only finitely many cells; the probability one of those cells is activated is at most their number divided by n. Hence P_n converges locally in probability, and weakly in the vague topology, to the empty point process P_0.

Its local Fourier coefficient is

    m_n = (1/n) sum_{j=1}^n exp(2*pi*i*j/n^2) -> 1,

whereas m(P_0)=0. Its directional moment is

    D_n = 4*pi^2*(n+1)*(2*n+1)/(6*n^4) -> 0.

Thus C1 certifies nonstationarity for every sufficiently large n with a strict order margin, and that margin is lost in the limit despite E N(Q)=1 for all n. The exact missing premise is visible:

    E[N(Q) 1_{N(Q)>K}] = 1  whenever n>K,

so the counts are not uniformly integrable. These P_n are *not* claimed to be Riesz Gibbs measures. They refute only the inference that bounded first moments plus weak convergence preserve a local Fourier expectation. Uniform higher local moments would rule this construction out.

## Relation to the paired route

w531's ROUTE_BEFORE_PEERS.md uses Gaussian acoustic covariance and soft pinning. This packet uses full-specification finite-energy bounds and a point-process limit counterexample; it does not repeat its covariance computations. The transfer from a labelled Gaussian crystal to the unrestricted Riesz law remains the decisive missing estimate.

NEXT: Inspect the paired harmonic lemmas for a valid order of the pinning and volume limits and for an explicit full-Gibbs comparison premise.
