# C0052: annealed single-current overlap bridge

Author w477, 2026-10-10. Author-checked reductions only; referee w479 has not yet returned a verdict. C0052 is not solved. Current openness: UNKNOWN after a bounded check, with the historical source explicitly conjectural.

## Exact intake target and prior attempt

The intake's problems.jsonl row 52 states: prove that the three-dimensional Ising scaling limit is not Gaussian; the renormalised coupling does not vanish. The exact primary source is Duminil-Copin, Lectures on the Ising and Potts models on the hypercubic lattice, arXiv:1707.00520v1, Conjecture 6, printed p.94. Equations (7.1)-(7.2) define g(beta)=sum_{x,y,z} U4(0,x,y,z)/(chi(beta)^2 xi(beta)^3), with chi=sum_x G_beta(0,x) and xi=[lim_n -(1/n) log G_beta(0,n e1)]^{-1}, in the free zero-field subcritical state. The source's g is nonpositive. Its 3D target is g(beta) not tending to zero as beta increases to beta_c. L001-L006 below address the related critical smeared-field formulation. L007 supplies the separate, source-faithful subcritical reduction. No equivalence between the two formulations is assumed.

C0052-A001 (attempts.jsonl row 42, 2026-09-07) proposed a random-current intersection second moment. It did not prove its variance estimate. Its fractal-dimension argument is a heuristic, and the relation between the proposed cluster dimension and the spin exponent is not an established input here. The SOLVER_MAP edge to C0051 omits the current-cluster second-moment hypothesis: a spin two-point improvement alone is not established as sufficient. No C0052 match was found in the named H/I attempt directories in the targeted text search. This is not an exhaustive claim that the owner never solved it.

The primary switching identity used below is Aizenman-Duminil-Copin, arXiv:1912.07973v4, equation (3.11). Equation (3.13) gives an UPPER comparison after adding sourceless currents; reversing it would invalidate a non-triviality proof. The independent clusters in that comparison are not the clusters in equation (3.11).

## Set-up

First work on a finite connected graph with strictly positive ferromagnetic edge couplings and no external field, with free boundary conditions. Let G(x,y)=E[sigma_x sigma_y], including G(x,x)=1. Let a_x>=0 have finite nonempty support. Put M=sum_x a_x sigma_x and V=E[M^2]>0. A current n has weight prod_e J_e^{n_e}/n_e!, conditioned on its odd-degree source set. Repeated source labels cancel modulo two: the source set for x=y is empty.

Draw the ordered pair (X,Y) with probability rho(x,y)=a_x a_y G(x,y)/V, and then draw n from the current law with sources x,y. Make a second, completely independent copy (Z,T,m). All expectations in the next two lemmas include both endpoint draws and currents. Connectivity includes a vertex connected to itself, even in an empty current.

## L002: exact variance-weighted identity

Define D=3-E[(M/sqrt(V))^4]. Then

    D=2 P(X is connected to Z in n+m).

Proof. Expand the fourth cumulant of M as sum_{x,y,z,t} a_x a_y a_z a_t U4(x,y,z,t). The three Wick pairings each sum to V^2, including repeated labels. Insert equation (3.11), divide by V^2, and recognize rho(x,y)rho(z,t). Every term is legitimate because the weights are nonnegative and the sum is finite. The repeated-label cases follow from the same switching lemma with parity cancellation; they must not be omitted. QED.

This is an averaged identity. It does not assert a pointwise scale-uniform lower bound for every separated quadruple.

## L003: single-current overlap criterion

Let W be any finite vertex set. Let C(n,X) be X's positive-edge cluster in the SINGLE current n and C(m,Z) its independent counterpart. Set

    I=|W intersect C(n,X) intersect C(m,Z)|,
    q(v)=P(v in C(n,X)),
    q(v,w)=P(v,w in C(n,X)),
    A=sum_{v in W} q(v)^2,
    B=sum_{v,w in W} q(v,w)^2.

If A>0, then D>=2 A^2/B. In particular, if B/A^2<=K uniformly over scales, then D>=2/K uniformly.

Proof. Independence of the two marked SINGLE currents gives E[I]=A and E[I^2]=B. An intersection of their source clusters supplies an n+m path from X to Z, so {I>0} is a subset of the event in L002. Cauchy-Schwarz applied to I 1_{I>0} gives P(I>0)>=A^2/B. Combine with L002. No independence of two vertex events within the same cluster is assumed. QED.

The sum can be restricted to W=the support box of a, so no infinite local-time expectation is needed. A is positive when W includes the endpoint support. For distinct v,w, the sufficient extra bound q(v,w)<=K0 q(v)q(w) would give B<=A+K0^2 A^2. This occupancy bound is NOT the Lebowitz inequality for spin correlations and is not proved for critical 3D currents here.

## L004: refutation of the first-moment shortcut

For each integer K>=2, take a set of N=K^3 vertices. Independently draw C and C' as follows: with probability 1/K take all N vertices; otherwise take one uniformly chosen vertex. These are identically distributed, independent, nonempty random sets. Put I=|C intersect C'| and b=2/K-1/K^2+(1-1/K)^2/K^3. Then

    P(I>0)=b ->0,
    E I=K+2(1-1/K)/K+(1-1/K)^2/K^3 ->infinity,
    E I^2=K^4+2(1-1/K)/K+(1-1/K)^2/K^3,
    E I^2/(E I)^2 is asymptotic to K^2.

Proof. Both sets are full with probability 1/K^2, giving I=N. Exactly one is full with probability 2(1-1/K)/K, giving I=1. If both are singletons, they agree with probability 1/N and otherwise do not intersect. Sum the three disjoint cases. QED.

This is a counterexample to a probabilistic inference, not a counterexample to Ising non-triviality. Independence between the two entire clusters and a divergent expected intersection count do not supply the relative second-moment bound.

## L005: moment passage is available from switching

For any such zero-field ferromagnetic Ising model and nonnegative weights, E[M^{2k}]<=(2k-1)!! V^k for every integer k>=1. Consequently E exp(t M/sqrt(V))<=exp(t^2/2), E[(M/sqrt(V))^6]<=15, and the fourth-power tail expectation above R is at most 15/R^2.

Proof. For a list x1,...,x_{2k}, let A be its parity source set. If x1 repeats, the connection event to one repeated label is certain. Otherwise x1 belongs to A, and the component of x1 in a current with source set A contains another member of A by parity. Thus the events {x1 connected to xj}, j>=2, cover the whole two-current space with sources A,empty. The switching lemma identifies the probability of each event, multiplied by E[sigma_A], with G(x1,xj) E[prod of the remaining 2k-2 spins]. The union bound and induction give the Wick pairing upper bound, also for repeated labels. Multiply by prod a_x>=0 and sum: each pairing contributes V^k. Spin-flip symmetry removes odd moments. Expanding the finite-volume exponential gives Gaussian domination of the moment generating function. The sixth moment and tail bound follow directly. For finitely supported weights in the free infinite-volume state, pass through finite-volume spin correlations. QED.

Unlike a bare variance bound, this sixth-moment bound supplies the uniform integrability required by L001.

## L006: nonzero distribution-valued subsequences without an exponent assumption

Let sigma be a stationary, centered spin field on Z^3 with nonnegative pair correlations, bounded spins, and positive box-sum variance. Fix smooth f0 with 0<=f0<=1, f0=1 on [-1,1]^3 and support in [-2,2]^3. For integers L>=1 define

    V0,L=Var(sum_x f0(x/L) sigma_x),
    Phi_L=(1/sqrt(V0,L)) sum_x sigma_x delta_{x/L}.

Then {Phi_L} is tight in H^{-2}_loc(R^3). If the Gaussian sixth-moment bound of L005 also holds for the f0 sum, every subsequential limit Phi satisfies E[Phi(f0)^2]=1 and is nonzero.

Proof. Write Sigma_L=Var(sum_{x in [-L,L]^3} sigma_x). Nonnegative correlations imply V0,L>=Sigma_L. A fixed compact K is covered by N_K translated lattice boxes of radius L, with N_K independent of L. Stationarity makes each box-sum variance Sigma_L; Cauchy-Schwarz bounds every cross covariance in absolute value by Sigma_L. Therefore the variance of the sum over the cover is at most N_K^2 Sigma_L. Positivity of pair correlations gives, for any complex coefficients b_x supported in LK,

    E |sum b_x sigma_x|^2 <= (sup |b_x|)^2 N_K^2 Sigma_L.

For a fixed smooth compact cutoff chi and a torus containing its support, every Fourier coefficient of chi Phi_L thus has bounded second moment, uniformly in its frequency and in L. Sum with weights (1+|k|^2)^{-7/4}; this sum is finite in dimension three. Hence E||chi Phi_L||_{H^{-7/4}}^2 is uniformly bounded. Markov's inequality and the compact embedding H^{-7/4}(torus) -> H^{-2}(torus) give tightness on this cutoff. A countable exhaustion by cutoffs, allocating failure probability delta 2^{-j}, and a diagonal compactness argument give tightness in H^{-2}_loc. This is deliberately a coarse regularity exponent.

Evaluation at f0 is continuous on H^{-2}_loc. Its variance is exactly one at each L. The sixth-moment bound gives uniform integrability of its second and fourth powers. Along any convergent subsequence, moment passage gives E[Phi(f0)^2]=1. QED.

No conformal invariance, uniqueness of the limit, or identification with a constructed phi^4_3 field is claimed.

## Auxiliary critical-field conditional consequence

Take the stationary spin-flip symmetric nearest-neighbour critical Ising state on Z^3, weights a_x=f0(x/L), and W_L=[-2L,2L]^3. Use the infinite-volume current identity justified in the primary source for beta<=beta_c; alternatively demand the same overlap bound uniformly over finite free volumes before sending the volume to infinity. L005-L006 provide tight, nonzero distribution-valued subsequences and valid fourth-moment passage. If the annealed SINGLE-current overlaps satisfy sup_L B_L/A_L^2<infinity, L002-L003 and L001 make every such subsequential limit non-Gaussian.

The remaining input for this auxiliary critical result is sup_L B_L/A_L^2<infinity. It is not supplied by spin two-point estimates, Lebowitz, divergent mean overlap, or the 4D independent duplicated-cluster UPPER comparison. No passage from this critical result to the source's g(beta) is proved.

## L007: exact source-coupling bridge with susceptibility-weighted endpoints

Fix 0<beta<beta_c. All currents and correlations below use the free zero-field nearest-neighbour state on Z^3. Write chi=sum_x G_beta(0,x)<infinity and xi=xi(beta)>0. Draw independent X,R from pi_beta(x)=G_beta(0,x)/chi. Draw independent single currents n,m with source sets {0,X} and {0,R}, with repeated labels cancelled modulo two. For y in Z^3 define p_y=P(0 connected to y in n+tau_y m), where tau_y translates the second current by y. The exact identity is

    -g(beta)=(2/xi^3) sum_{y in Z^3} p_y.

Proof. In the sum over U4(0,x,y,z), put z=y+r. The primary switching identity gives -U4(0,x,y,y+r)=2 G_beta(0,x) G_beta(y,y+r) P^{0x,y(y+r)}(0 connected to y). Stationarity gives G_beta(y,y+r)=G_beta(0,r). Sum over x,r, divide by chi^2 xi^3, and recognize pi_beta(x)pi_beta(r). Nonnegative summands justify Tonelli. Subcritical exponential decay and the tree-diagram upper bound make the original sum finite; alternatively the identity holds as an identity of nonnegative extended sums before that fact is used. QED.

Now let H_beta={0,...,ceil(xi)-1}^3, N_beta=|H_beta|>=xi^3, and let Y be uniform on H_beta, independent of the two marked currents. Choose any finite W_beta containing 0; for example [-4 ceil(xi),4 ceil(xi)]^3. Define

    I_beta=|W_beta intersect C(n,0) intersect (Y+C(m,0))|,
    A_beta=E I_beta, B_beta=E I_beta^2, Q_beta=B_beta/A_beta^2.

Then A_beta>0 and

    -g(beta) >= 2 N_beta A_beta^2/(xi^3 B_beta) >= 2/Q_beta.

Proof. At Y=0, both source clusters contain the root, so I_beta>=1 and A_beta>=1/N_beta>0. The overlap event implies the union-current connection event, conditional on every Y. Restrict the exact nonnegative sum to H_beta, average over Y, and apply Cauchy-Schwarz to I_beta. This produces the first inequality; N_beta>=xi^3 gives the second. Currents are independent of each other and of Y, while occupancies within one current need no independence. QED.

For q_beta(v)=P(v in C(n,0)) and q_beta(v,w)=P(v,w in C(n,0)), the exact quantities are

    A_beta=(1/N_beta) sum_{y in H_beta} sum_{v in W_beta} q_beta(v) q_beta(v-y),
    B_beta=(1/N_beta) sum_{y in H_beta} sum_{v,w in W_beta} q_beta(v,w) q_beta(v-y,w-y).

Consequently, a sequence beta_j increasing to beta_c with Q_beta_j<=K<infinity proves that g(beta) does not tend to zero, in the exact primary-source sense. Uniform control for every beta sufficiently close to beta_c is a stronger sufficient condition.

HARDEST GAP FOR THE EXACT SOURCE TARGET: obtain a bounded Q_beta along a sequence beta increasing to beta_c for these susceptibility-weighted single currents and the correlation-length-scale random root Y. The critical block ratio in L003 is a different quantity. No theorem or computation in this packet supplies either ratio bound.
