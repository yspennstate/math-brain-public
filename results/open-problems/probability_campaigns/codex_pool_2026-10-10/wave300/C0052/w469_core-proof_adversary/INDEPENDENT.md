# C0052 independent adversary checkpoint

Author: w469. Date: 2026-10-10. Paired prover w468's proof has NOT been read at this checkpoint. Mathematical review by w470 is pending. No parent-problem solution or novelty claim.

The hardest missing input is a scale-independent lower bound on an appropriately normalized random-current connection probability. Divergence of an expected intersection count does not provide that input.

## Source definition and scope

Hugo Duminil-Copin, *Lectures on the Ising and Potts models on the hypercubic lattice*, https://www.ihes.fr/~duminil/publi/2017PIMS.pdf, printed pp. 94-95, equations (7.1)-(7.2), Conjecture 6 and Exercise 61, defines triviality by g(beta) tending to zero as beta increases to beta_c. Here G_beta(x,y)=mu_beta^f[sigma_x sigma_y] for the zero-field nearest-neighbor ferromagnetic Ising model on Z^3, chi(beta)=sum_x G_beta(0,x), xi(beta) is the exponential correlation length in direction e_1, and

g(beta) = [sum_{x2,x3,x4} U4_beta(0,x2,x3,x4)] / [chi(beta)^2 xi(beta)^3],

where U4 is the fourth moment minus the three products of two-point functions. With this sign convention g<=0. The source asks for the three-dimensional part of Conjecture 6. The intake-to-source mapping is still being checked.

The literal source criterion is g(beta) not tending to zero. It requires a sequence beta_n increasing to beta_c and epsilon>0 with -g(beta_n)>=epsilon; it does not by itself require liminf_{beta -> beta_c}(-g)>0. A statement about every critical spin-field subsequential limit is a stronger formulation and requires its own normalization and limit argument. Do not silently substitute the two formulations.

## Independently derived counterexample: expectation is insufficient

Let N>=2 and L=N^2. Take four distinct endpoints a,b,c,d, and mutually disjoint corridors V_j={v_{j,1},...,v_{j,L}}, j=1,...,N. Add edges along each corridor and attach a,c to its first vertex and b,d to its last vertex. Let J and K be independent uniform labels on {1,...,N}. A is the connected a-b path using corridor J; B is the connected c-d path using corridor K. Their endpoints do not belong to the other path.

I=|V(A) intersect V(B)|=L*1{J=K}. Consequently

P(I>0)=1/N,
E I=L/N=N,
E I^2=L^2/N=N^3,
(E I)^2/E I^2=1/N.

The two random paths are independent, each is connected and has the prescribed two endpoints. Every corridor vertex has marginal hit probability 1/N for either path, so multiplying the two independent one-point hit probabilities correctly gives E I; it still gives no scale-independent lower bound on P(I>0).

An optional bounded-degree version replaces each endpoint's N incident edges by a separate binary fan with N leaves. The four fans are mutually disjoint; each leaf attaches to its designated corridor end. The maximum degree is three; paths still have I=L*1{J=K}. Endpoint degrees therefore do not cause the failure.

This is a counterexample to the stated generic probabilistic inference. These uniformly chosen paths are NOT asserted to be Ising random currents. A theorem using additional Ising structure is not refuted by this example; it must identify and prove that structure.

## Independently derived weak-limit lemma

Let X_n be centered real variables with E X_n^2=1 and E X_n^4<=3-delta for a fixed delta>0. If X_n converges in distribution to X, then X is centered, has variance one, and E X^4<=3-delta. Hence X is not Gaussian.

Proof. The fourth moment bound gives uniform integrability of X_n^2, since E[X_n^2; |X_n|>M] <= (3-delta)/M^2. It also gives uniform integrability of X_n. Weak convergence and truncation then give E X=0 and E X^2=1. For each R, the function min(x^4,R) is bounded continuous, so E min(X^4,R)=lim_n E min(X_n^4,R)<=3-delta. Let R increase to infinity. A centered Gaussian of variance one has fourth moment three, yielding a contradiction.

Only second-moment uniform integrability is needed here; fourth-moment equality under the limit is unnecessary. The moment bound makes the scalar laws tight by Chebyshev. It does not prove tightness of the entire random distribution in a field topology.

## Finite-volume Ising reduction

For a finite graph with ferromagnetic couplings, zero field and free boundary, let f_x>=0 be finitely supported and not identically zero. Put S=sum_x f_x sigma_x, V=E S^2>0 and X=S/sqrt(V). The sourced-current switching identity in Exercise 61 and Aizenman, https://arxiv.org/html/2112.04248v2, section 5.2, implies

-U4(x1,x2,x3,x4)=2 G12 G34 p(x1,x2,x3,x4),

where p is the probability that x1 and x3 connect in the union of independent currents with parity source sets {x1,x2} and {x3,x4}. Repeated endpoints must be handled with source sets interpreted modulo two and connectivity including the zero-length path.

Define the probability weight Q_f(x1,x2,x3,x4)=f1 f2 f3 f4 G12 G34/V^2. Its weights sum to one. Then

r_f=E_{Q_f} p,
E X^4=3-2r_f.

Thus r_f>=epsilon uniformly along a sequence, together with a weak scalar subsequential limit, proves that limit non-Gaussian by the preceding lemma. The algebra and weak-limit implication are elementary reductions. Proving the required r_f bound for the actual 3D currents at growing scale is the missing Ising theorem.

This scalar reduction does not identify the source g(beta) with r_f. Moving from a smeared finite-volume variable to the near-critical infinite-volume coupling requires a separate cutoff and normalization argument.

## What a usable intersection lemma must supply

For a nonnegative overlap variable I under the EXACT current law needed in the switching identity, Cauchy-Schwarz gives P(I>0)>=(E I)^2/E I^2. A bound E I^2<=C(E I)^2 with C independent of the scale would therefore suffice, provided I>0 implies the desired connection event. A comparable conditional-cluster-size estimate could also suffice. These are still-unproved inputs for the proposed 3D route.

Check the current law carefully: the exact single-site identity G(x,u)G(u,y)/G(x,y) refers to the source component of one sourced current PLUS an independent sourceless current. It does not automatically describe a bare sourced current or the joint two-site hit probabilities. Adding sourceless currents increases connectivity; a lower bound for the enlarged intersection event does not establish a lower bound for the original two-current event.

NEXT: Verify the intake source mapping, freeze this independent checkpoint, then audit w468's main lower-bound step against these exact laws and quantifiers.
