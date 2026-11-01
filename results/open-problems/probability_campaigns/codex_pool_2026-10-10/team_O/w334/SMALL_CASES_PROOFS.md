Checked special cases and failed routes for the remaining assignments
All proof claims below await the independent auditor w346. No general open problem is declared solved. Current literature status remains unverified unless the cited cached primary text supplies an answer.

C0113: one dimension and a failed limit argument

For a locally finite subset of R unbounded in both directions, with its points in increasing order, the free Euclidean minimal spanning forest consists exactly of edges between consecutive points. An edge skipping an intermediate point is uniquely longest in a triangle and is excluded by the cycle rule. For consecutive points x<y, every path from x to y crosses the cut between them, and every other crossing edge is strictly longer than y-x. Thus there is no alternative path using only shorter edges, and the consecutive edge is retained. These edges form one bi-infinite tree. A homogeneous Poisson process almost surely satisfies these hypotheses. This proves the d=1 special case and does not address d>=3.

Finite connected minimum spanning trees need not have a connected edgewise limit. On a half-infinite ladder with vertices a_i,b_i, i>=1, give each horizontal edge weight 1/2 and rung i weight 1+1/i. In the finite first N columns, every MST consists of all horizontal edges and the unique lightest rung, rung N. Every rung i is eventually absent as N increases. The limit has two disjoint rays. Equivalently rung i is excluded in the infinite forest by the finite cycle through rung i+1, whose other edges are all lighter. Horizontal edges are retained: any bypass uses a rung of weight >1. This is a counterexample to a generic finite-MST connectivity argument, not a Poisson or stationary-iid-weight counterexample. The old intake's purported Lyons-Peres-Schramm connectivity transfer remains unverified; no such theorem is imported here.

P0039: quantitative extension of the subexponential case

Let G have degree at most D and |B_G(x,r)|<=A exp(C r^alpha), with A,C>0 and 0<alpha<1. Let H be any connected subgraph containing x. Assume the classical Carne-Varopoulos bound for simple random walk on H:
P_x(X_n=y)<=2 sqrt(deg_H(y)/deg_H(x)) exp(-d_H(x,y)^2/(2n)).
For every K>(2C)^(1/(2-alpha)), almost surely eventually
d_H(x,X_n)<K n^(1/(2-alpha)).
Consequently ambient distance satisfies the same bound. This strengthens the already-recorded zero-speed special case to an explicit sublinear distance scale. The source P0039 compares the base Cayley walk with the walk on its infinite percolation clusters. Applying the bound to H=G and to every cluster proves both intrinsic speeds are zero in this growth regime.

Proof: intrinsic balls in H lie inside ambient balls in G, and degree prefactors are bounded by 2 sqrt(D). Sum the heat-kernel bound over intrinsic distance shells k from r=ceil(K n^(1/(2-alpha))) to n. Each shell has at most A exp(C k^alpha) vertices. For k>=K n^(1/(2-alpha)), put eta=1/2-C/K^(2-alpha)>0; then C k^alpha-k^2/(2n)<=-eta k^2/n. Hence the tail is at most 2A sqrt(D)n exp(-eta K^2 n^(alpha/(2-alpha))), summable in n. Borel-Cantelli proves the claim (using the threshold r). The isolated vertex case is constant. The base-versus-cluster positive-speed equivalence for exponential-growth Cayley graphs remains unresolved here. The inequality d_G<=d_H compares two metrics on the same cluster walk and is not itself the source's conjecture.

P0245: prescribe the stationary law in the two-state optimum

Let a two-state discrete-time irreducible chain have stationary law (p,q), p,q>0, p+q=1. The initial state counts as visited at time zero. Write a=P(0,1), b=P(1,0), and kappa=pa=qb, with 0<kappa<=min(p,q). The expected cover time from stationarity is
E_pi C=p/a+q/b=(p^2+q^2)/kappa.
For the prescribed stationary law its exact minimum is (p^2+q^2)/min(p,q), attained uniquely at kappa=min(p,q). This prescribes the optimal holding probability rather than merely repeating the unrestricted two-state minimum. Optimizing over p gives the known unrestricted value 1, attained only by p=q=1/2 and deterministic alternation. Proof: conditional cover times are geometric with means 1/a and 1/b; the displayed expression decreases strictly in feasible kappa. It is at least 1 since each conditional mean is at least 1, with equality only when both a and b equal 1. This does not prove the many-state conjecture.

C0108: rank-one squares and coefficient cancellation

For independent uniform signs epsilon_i in {-1,1} and nonzero real a_i, put Q=(sum_(i=1)^n a_i epsilon_i)^2. Then for every real z,
P(Q=z)<=2 binom(n,floor(n/2))/2^n,
and at z=0 the factor 2 can be omitted. Negative z has probability zero. Proof: after absorbing signs of a_i into the independent signs, the coefficients are positive. Subsets yielding a fixed linear sum form an antichain. For an antichain F, a uniform random permutation's increasing subset chain meets F at most once, so sum_(S in F)1/binom(n,|S|)<=1. Since each binomial coefficient is at most binom(n,floor(n/2)), |F| is at most that maximum. A positive quadratic level has at most two linear preimages, +/-sqrt(z); the zero level has one. With all a_i=1 and even n, P(Q=0)=binom(n,n/2)/2^n, which is of order n^(-1/2) by Stirling. Thus the proposed exponent is sharp and holds without logarithms for this rank-one family; no general quadratic result is proved.

Raw nonzero matrix entries alone do not enforce nondegeneracy for uniform signs. Let c_ii=1, c_ij=1 for i<j, and c_ij=-1 for i>j. Every entry is nonzero, but sum_(i,j)c_ij epsilon_i epsilon_j=n deterministically. Thus an anti-concentration statement stated with an arbitrary nonsymmetric matrix and only this raw-entry condition is false. The polynomial uses c_ij+c_ji for i<j, so the relevant hypothesis is on the effective off-diagonal coefficients (or an explicitly symmetric nonzero off-diagonal matrix). This corrects the literal intake wording; it does not claim the original survey intended nonsymmetric coefficients. The sign convention is explicit: this counterexample does not apply as written to 0/1 Bernoulli variables.

C0155: failure of every increasing bijection does not preclude a quasi-isometry

Two independent homogeneous Poisson processes on R almost surely admit no increasing bijection satisfying a coarse Lipschitz upper bound |f(x)-f(x')|<=A|x-x'|+B with fixed finite A,B. Enumerate their positive points increasingly as x_i,y_i. Every increasing bijection between their two-sided enumerations is an index shift k in Z. For each fixed k, far enough out on the positive half-line, pairs of corresponding gaps (X_i=x_(i+1)-x_i,Y_(i+k)=y_(i+k+1)-y_(i+k)) are independent across i and are independent exponential variables. For fixed positive integers A,B, the event X_i<=1 and Y_(i+k)>A+B has a fixed positive probability. Independent Borel-Cantelli gives infinitely many such indices, violating the displayed upper bound. A countable union over shifts and integer upper bounds rules out all increasing bijections almost surely, even with realization-dependent finite constants. Decreasing bijections are also ruled out by the same argument after reflection. The one gap straddling the origin is irrelevant; use tails away from it.

This is stronger than failure of the zero-shift index map, but not failure of all increasing quasi-isometries: a quasi-isometry may skip target points or identify nearby source points, so it need not be a bijection. The old attempt's claim that any quasi-isometry must be a non-monotone matching is not established by failure of index bijections. General C0155 remains unresolved here.

P0026: quadratic spread can increase at rebirth

For N Brownian particles in a domain, define S=sum_(i<j)|x_i-x_j|^2. At a rebirth, translate the dead position to zero and denote the N-1 surviving displacement vectors by y_1,...,y_(N-1). Replacing the dead particle by a uniformly chosen survivor gives
E(Delta S | survivors)=sum_j |y_j|^2 - [2/(N-1)]|sum_j y_j|^2.
Proof: S=N sum_i |x_i|^2-|sum_i x_i|^2. Cloning j changes it by (N-1)|y_j|^2-2 y_j dot sum_i y_i; average over j.

This expectation can be strictly positive even on D=(0,1). For N=4, dead position 0, and survivors 3/4,1/100,1/100, it equals
9/16+2/10000-(2/3)(77/100)^2=5023/30000>0.
The boundary position is the limiting position at the rebirth time; the survivors are strictly inside the interval. Positivity persists for nearby distinct survivor positions by continuity, so the obstruction is not restricted to an exact coincidence. Thus quadratic spread does not contract in conditional mean at every rebirth. This blocks that uniform-contraction route to non-explosion; it is not an exploding example. For N=3 at a one-dimensional endpoint, the formula is -2y_1 y_2<=0, so simply transferring the favorable two- or three-particle sign to larger N is invalid.

Also V=-sum_i log dist(x_i,{0,1}) has unbounded positive Brownian-generator drift even away from the medial point: for every x_i<1/2, (1/2)Delta V=(1/2)sum_i x_i^(-2). With one x_i=epsilon and the others fixed at 1/4, this divided by 1+V tends to infinity as epsilon decreases to zero. Therefore the usual LV<=C(1+V) estimate cannot hold uniformly for this V even in an interval. Clone jumps need a separate argument; generator failure alone proves no explosion claim.
