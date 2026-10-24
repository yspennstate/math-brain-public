# Team O, w344: ten checked partial-result packets

Date: 2026-10-10. All independent verdicts are pending w346. "Proof" below means a written argument checked by this worker; it is not an auditor KEEP or a novelty claim. No full open problem is reported solved. Cached status is historical: absence of a local resolution is not a current worldwide openness certificate. The prior-attempt extracts and exact source paths are in packet_sources.json; source_excerpts.json and source_followup.json contain bounded primary-source context reads. No test bank was read or written.

## P0341: a fixed-width boundary deletion still fails

The source is Aldous-Janson, Critical Beta-splitting Random Tree II, arXiv:2303.02529v3 (17 April 2025), Section 3.1, equation (2), and Open Problem 8/Ansatz 20, PDF pp.39-40. The earlier campaign already refuted both clauses by sparse powers-of-two weights. We retain that attribution and extend its failed-repair analysis.

Let H_k=sum_(r=1)^k 1/r. The discrete tagged descent chain jumps n to j<n with probability 1/((n-j)H_(n-1)); a(n,j) is its visiting probability. Fix an integer L>=0, and truncate the occupation sum at j<=n-L-1. Set g(j)=j 1_{j=2^r,r>=1}. Along N=2^K and n=N+L+1, a(n,N)>=1/((L+1)H_(N+L)), since the first jump alone is a visit. Thus the retained sum is at least N/((L+1)H_(N+L)). The comparison coefficients are a(j)=6H_(j-1)/(pi^2(j-1)). For large K, n<2N and the comparison sum, whether stopped at n or n-L-1, has exactly K nonzero terms. Since H_(2^r-1) is of order r, that sum is of order K^2. For fixed L, H_(N+L) is of order K, and the ratio is bounded below by c_L 2^K/K^3 -> infinity. This proves that removing the root, or any fixed number of states just below it, does not repair the divergent-series clause.

This proof does not cover a growing trimming width, regular test classes, or the general quantitative occupation-bound problem. The first-jump bound needs no recurrence solution. Nineteen exact rational transition-normalization checks, three complete small descent computations, and sixteen finite lower-bound checks are saved in p0341_measurements.json. At K=18 the ratio lower bound is 126.182 for L=1 and 3.88245 for L=64.

A positive repair criterion is available without inventing a rate: for nonnegative b_n(j) supported on j<=n with b_n(j)->b(j) for each fixed j, and f(j)>=0 with S=sum b(j)f(j)<infinity, sum b_n(j)f(j)->S if and only if lim_(M->infinity) limsup_(n->infinity) sum_(j>M) b_n(j)f(j)=0. For fixed M, the finite prefix converges. Tail control gives the forward implication by splitting the sum into prefix and tail; conversely, convergence of total and prefix gives limsup tail=S-sum_(j<=M)b(j)f(j), which tends to zero. This is a criterion requiring weighted tail control, not a proof that the tagged chain satisfies it for any new test class.

## C0039: execute the deferred S3 experiment and a finite rank-one case

Lyons, Determinantal Probability: Basic Properties and Conjectures, arXiv:1406.2707v1 (10 June 2014), Theorem 5.6 and the following paragraph, PDF p.23, explicitly leaves the noncommuting linear bound open. The cached intake's S3 transport experiment was specified but not run. No later local resolution was found in the named attempts.

experiment_c0039.py constructs real symmetric right-convolution kernels on S3, rescales their spectra into [0.1,0.9], and verifies that they commute with every left translation. For a strictly positive contraction Q, the exact-set DPP formula is P_Q(S)=det(I-Q)det((Q(I-Q)^-1)_S). All 64 configuration probabilities and six one-site marginals are checked. Coupling distance is the 4096-variable transportation LP with cost |S symmetric_difference T|/6. Averaging any finite-group coupling over simultaneous left translations preserves the marginals and cost, so this unrestricted LP equals the invariant coupling optimum. The normalized Schatten norm is trace|Q-Q'|/6, which is the equivariant trace on the transitive six-point set. Primal constraints, dual feasibility and objective gap are checked; the .3I/.7I control gives equality.

Twelve noncommuting pairs, seed 344, gave no violation. The largest ratio was 0.6934876897518668; the largest marginal residual was 1.124100812432971e-15 and dual gap 5.551115123125783e-17. These are finite numerical observations, not proof for all finite or infinite kernels, complex kernels, projections, or spectra near the boundary.

A proved finite special case: for unit vectors v,w in C^n and rank-one projections P=vv*, Q=ww*, their DPPs select one site with probabilities |v_i|^2 and |w_i|^2. The minimum expected normalized Hamming cost is (1/n) sum_i ||v_i|^2-|w_i|^2|. Multiply w by a phase so <v,w>=r>=0. The real-part identity for squared magnitudes and Cauchy-Schwarz give sum_i ||v_i|^2-|w_i|^2| <= ||v-w||_2 ||v+w||_2=2 sqrt(1-r^2). The two nonzero eigenvalues of P-Q are plus and minus sqrt(1-r^2), as follows by restricting to span(v,w), checking trace zero and trace of its square. Hence the cost is <=trace|P-Q|/n. This proves the finite rank-one inequality; it does not give an approximation argument for the general equivariant problem.

## P0023: symmetric starting pairs admit an efficient reflection coupling

Burdzy's cached official open-problems page, Problem 4, asks about arbitrary distinct starting points in any acute triangle. The prior attempt gives only a spectral lower bound, with the correct generator convention. For a bounded reflection-symmetric triangle D, let R be reflection through a symmetry axis and start at x and Rx, with x off the axis. Run Neumann reflected Brownian motion X with generator Delta/2, set Y=RX until the first hitting time T of the axis, and set Y=X thereafter. Reflection invariance of the domain and the strong Markov property make both marginals reflected Brownian motion. At T, X=RX, so the construction is coalescent.

Before T, X lives in one half-triangle with Neumann condition on its exterior sides and absorbing condition on the axis. Its survival exponent is the first mixed-boundary eigenvalue lambda_mix of -Delta/2. Odd extension across the axis sends every admissible half-domain test function to a mean-zero H^1 function on D, preserving its Rayleigh quotient. Thus lambda_mix>=lambda_1, where lambda_1 is the first positive full-domain Neumann generator eigenvalue. The bounded-domain killed heat semigroup therefore gives, for each gamma<lambda_1, P_x(T>t)<=C_(x,gamma) exp(-gamma t). This is an affirmative special case for mirror-image starting points in reflection-symmetric acute triangles. It does not construct a coupling for arbitrary pairs or scalene triangles.

Checks: require a global domain symmetry, not just a reflected noise formula; identify absorbing/reflecting boundary pieces; require coalescence after meeting; use -Delta/2 rather than -Delta. A one-dimensional reflection control on [0,1], starting at 1/4 and 3/4, has generator exponent pi^2/2. Its exact mixed-boundary survival expansion has scaled limit (4/pi)cos(pi/4); three values are saved in special_case_measurements.jsonl. That control checks the convention and stopping mechanism, not the full triangular spectral theory.

## P0177: global-mode estimates under finite variance and seventh moment

The earlier campaign already derived the classical expansion under an exponential quadratic moment. The following worker proof addresses the free global mode and retains no claim of priority or full-problem acceptance.

Label: proof (worker checked), independent audit pending w346. No novelty or full-problem solution certificate. The mode here means the global maximizer of the canonical continuous density.

Let X have mean m and finite variance sigma^2, and let mu_t be its law freely convolved with a semicircle law of variance t. If sigma=0, mu_t is a semicircle centered at m and the assertions below hold directly. Assume sigma>0. Put

    B=(sqrt(2)+2)sigma,
    A=B^2+sigma^2=(7+4sqrt(2))sigma^2,
    T=1024 A.

For every t>=T, mu_t has a unique global mode. That mode tends to m as t tends to infinity. If E|X-m|^3<infinity, putting M3=E|X-m|^3 and K=A(B+sigma)+4(B^3+M3), its location M(t) satisfies the explicit estimate |M(t)-m|<=36 K/t for t>=T. If E|X-m|^7<infinity, then

    M(t)=m-3mu_3/t+(5mu_5-22mu_2mu_3)/t^2+O_mu(t^-3),

where mu_k=E[(X-m)^k]. The threshold is a proved sufficient bound, with no optimal transition location claimed. An exponential quadratic moment, as in the original classical question, implies the required seventh moment.

Use the general Biane parametrization from Hasebe-Ueda, ALEA 15 (2018), equations (2.10), (2.13), (2.14). With w_t(u)=v_t(u)^2>0, it reads E[1/((u-X)^2+w_t(u))]=1/t, the density at psi_t(u) is sqrt(w_t(u))/(pi t), and psi_t is a homeomorphism. Hence global density maxima correspond exactly to global maxima of w_t. The function v_t is continuous and tends to zero at both infinities: for any a>0, E[1/((u-X)^2+a)] tends to zero as |u| tends to infinity by dominated convergence, forcing w_t(u)<a eventually. Thus a positive global maximum is attained.

Jensen's inequality gives w_t(m)>=t-sigma^2 when t>sigma^2. Indeed, at w=t-sigma^2 the reciprocal expectation is at least 1/t, and the expectation is strictly decreasing in positive w. Every positive solution also has w_t(u)<=t. Let u_* be any global maximizer and w_*=w_t(u_*). Then w_*>=t-sigma^2 and

    E[(u_*-X)^2/(w_*+(u_*-X)^2)]=1-w_*/t<=sigma^2/t.

Chebyshev gives P(|X-m|<=sqrt(2)sigma)>=1/2. If r=|u_*-m|-sqrt(2)sigma>0, the last expectation is at least (1/2)r^2/(t+r^2). For t>=4sigma^2 this implies r^2<=2sigma^2 t/(t-2sigma^2)<=4sigma^2. Consequently every global maximizer lies in I=[m-B,m+B].

For every u in I and t>=T, Jensen similarly yields t-A<=w_t(u)<=t. Set epsilon=1/t, r_t(u)=w_t(u)/t, d=r_t(u)+epsilon(u-X)^2, and

    C2=E[d^-2], J=E[(u-X)d^-2].

The positive implicit solution is smooth in u and r_t'(u)=-2epsilon J/C2. Its stationary points have J=0. Differentiating J along this solution gives

    J'=C2-4epsilon E[(u-X)^2 d^-3]-2r_t'(u)E[(u-X)d^-3].

Uniformly on I, E[(u-X)^2]<=A, r_t>=1-epsilon A>=1/2, C2>=(1+epsilon A)^-2>=1-2epsilon A, and |J|<=4E|u-X|. For epsilon A<=1/2, |r_t'|<=18epsilon E|u-X|, so the magnitude of the final term is at most 288epsilon A; the middle term is at most 32epsilon A. Thus J'>=1-322epsilon A>0 for t>=1024A. At least one global maximizer exists inside I, is a positive interior stationary point of w_t, and therefore has J=0. Strict increase of J permits only one such point. This proves eventual uniqueness of the global density maximizer without a compact-support or unimodality assumption.

As t tends to infinity, r_t->1 uniformly on I. The functions J(u) tend uniformly to u-m: split the integral at a bounded |X-m|, use uniform convergence on the bounded part, and dominate the tail by a constant times |X-m|+B. Its unique zero u_t therefore tends to m. The same truncation argument gives E[(u_t-X)/d]->u_t-m, so psi_t(u_t)=u_t+E[(u_t-X)/d]->m.

If M3 is finite, |d^-2-1|<=16|d-1| and |d^-1-1|<=4|d-1| because d>=1/2. With E|u-X|<=B+sigma and E|u-X|^3<=4(B^3+M3), the equation J=0 yields |u_t-m|<=16epsilon K. The spatial map then yields |psi_t(u_t)-m|<=2(16epsilon K)+4epsilon K=36K/t. All constants and hypotheses are explicit.

For the second-order expansion, translate m to zero and work with F(epsilon,u,r)=E[1/(r+epsilon(u-X)^2)]-1 and J(epsilon,u,r)=E[(u-X)/(r+epsilon(u-X)^2)^2]. Finite seventh absolute moment makes these functions C^3 up to epsilon=0 from epsilon>=0, for u near zero and r near one. Every derivative of total order at most three is dominated by a constant times 1+|X|^7 when r>=1/2. To use the ordinary C^3 implicit-function theorem, extend to epsilon<0 using the degree-three Taylor polynomial in epsilon at zero, with its smooth u,r-dependent coefficients; this matches all partial derivatives through order three at zero. No reciprocal expectation at negative epsilon is used. The Jacobian with respect to (u,r) at (epsilon,u,r)=(0,0,1) is [[0,-1],[1,0]], hence invertible. The resulting C^3 branch has a Taylor expansion with O(epsilon^3) remainder and is the unique global-maximizer branch already identified above.

Writing r=1+c1 epsilon+c2 epsilon^2+O(epsilon^3) and u=a1 epsilon+a2 epsilon^2+O(epsilon^3), direct expansion gives c1=-mu2, c2=mu4-mu2^2, a1=-2mu3, a2=3mu5-14mu2mu3. Inserting into psi=u+E[(u-X)/(r+epsilon(u-X)^2)] gives -3mu3 epsilon+(5mu5-22mu2mu3)epsilon^2+O(epsilon^3). Translation back yields the displayed formula.

Checks requiring the auditor's attention: global existence of a maximum for an unbounded initial law; the Chebyshev interval; the uniform derivative constants; the sign of r_t'; positivity of w on the entire interval; the one-sided C^3 extension rather than an unjustified analytic continuation; variance normalization; and the distinction between a unique global maximizer and the number of local density peaks.

Numerical evidence: special_case_measurements.jsonl contains five compact-law comparisons with the classical expansion; mode_boundary_measurements.json contains twelve point-mass, symmetry, three-atom and zero-third-moment controls. unbounded_mode_measurements.json tests the geometric law with an explicit truncation and seventh-moment tail bound. These computations check coefficients and physical equations; the written argument supplies the noncompact global-maximizer step.

## C0004: correct the target and the normalization claim

Biskup, arXiv:1712.09972v4 (17 August 2019), Theorem 12.19, equation (12.86), and Problem 16.4, request the joint density rho^D(x,t) of the rescaled maximizer location and centered maximum height. The intake instead states a marginal location-density problem. The source's measure at height t is

    A -> e^(-alpha t) E[Z^D(A) exp(-alpha^-1 e^(-alpha t) Z^D(D))].

Its density in x, combined with dt, is the joint law. Integrating in t yields E[Z^D(A)/Z^D(D)], assuming 0<Z^D(D)<infinity almost surely. Indeed, conditional on Z, substitute s=alpha^-1 e^(-alpha t); the integral becomes Z(A) int_0^infinity exp(-s Z(D)) ds=Z(A)/Z(D). This explains the related marginal question without replacing the actual joint-density target. The cached paper supplies no explicit general answer; no current-status certificate is claimed.

The intake's C0004-A002 also falsely says equality of normalized averages requires independence. For a general random finite measure Z with T=Z(D)>0 and 0<E T<infinity, write U_A=Z(A)/T. Then

    E[Z(A)]/E[T] - E[U_A] = Cov(T,U_A)/E[T].

Equality for every measurable A is exactly zero covariance for every such U_A. Independence is sufficient but unnecessary. On two sites, take three equally likely outcomes with T=(1,2,3), U_{first}=(1,0,1), and Z=T(U_{first},1-U_{first}). Both averaging procedures give (2/3,1/3), but P(T=2,U_{first}=1)=0 whereas P(T=2)P(U_{first}=1)=2/9. This is an exact counterexample to the necessity direction in A002. It does not establish equality or inequality for the actual DGFF extremal measure; integrability must be checked before using normalized intensity.

Fraction arithmetic verifies the example. C0004Counterexample.lean formalizes only its denominator-cleared arithmetic. lean_check_receipt.json records SETUP_UNVERIFIED: Compute status is distressed or unknown. It is not Lean-checked, and no admission setting was changed.

## C0063: an exact tree special case and a failed inference

The cached Heydenreich-van der Hofstad source's Open Problem 9.1 asks for a positive limit of theta(p)/(p-p_c) for high-dimensional lattice percolation, beyond bounded ratios. The intake route writes beta=gamma-Delta while substituting gamma=1 and Delta=2; that displayed subtraction cannot produce beta=1. We do not accept the claimed equivalence or differentiation of a singular limit as proved.

For bond percolation on the infinite d-regular tree, d>=3, p_c=1/(d-1) and

    theta(p) = [2d(d-1)/(d-2)] (p-p_c)+O((p-p_c)^2).

Let k=d-1 and u be the probability that a vertex with its parent edge removed has an infinite descendant cluster. It solves 1-u=(1-pu)^k. For p>1/k it is the positive branching-process survival solution. Dividing by u and expanding gives kp-1=binom(k,2)p^2 u+O(u^2). The divided equation has nonzero u derivative at (u,p)=(0,1/k), so its positive branch is analytic. With epsilon=p-1/k, u=2k^2 epsilon/(k-1)+O(epsilon^2), and theta=1-(1-pu)^d gives the claimed coefficient. This is a tree analogue, not a proof on Z^d. Nine small numerical checks for d=3,4,8 approach the predicted slopes.

Bounded-ratio exponent information and monotonicity alone are insufficient: F(epsilon)=epsilon(2+sin(log epsilon)), epsilon>0 small, lies between epsilon and 3epsilon and is strictly increasing because F'=2+sin(log epsilon)+cos(log epsilon)>=2-sqrt(2)>0. Nevertheless F(epsilon)/epsilon has no limit, while log F/log epsilon ->1. A lattice-percolation proof therefore needs an additional mechanism ruling out oscillation; this example is not a percolation counterexample.

## C0087: exact transfer of intrinsic-diameter lower bounds

Open Problem 16.3 in the same cached source asks for MST diameter of order V^(1/3) on high-dimensional tori and the hypercube. The prior proposed reduction lacked complete geometric hypotheses. We prove only its deterministic lower-bound step.

Let G be a finite connected graph with distinct edge weights, T its MST, and G_p the graph of edges with weight <=p. Kruskal's algorithm has, by level p, selected a spanning tree inside every component C of G_p. These selected edges remain in T. Hence the unique T path between any u,v in C lies inside C, and its length is at least their shortest-path distance in C. Consequently max_C diam_intrinsic(C)<=diam(T). Any probabilistic lower bound for the left side transfers directly to the MST diameter without a universality assumption.

The reverse inequality fails: on K_n give the edges of a Hamilton path the n-1 smallest weights and every other edge larger distinct weights. Kruskal selects exactly that path, so diam(T)=n-1. At a threshold including every edge, G_p=K_n has intrinsic diameter 1. Thus intrinsic cluster-diameter control at one level gives no MST upper bound. This does not refute high-dimensional scaling. The script checks all 38 connected labeled four-vertex graphs at every selected threshold and exact K_4,K_8,K_16 path examples. Full torus/hypercube bounds remain unresolved in this packet.

## C0139: the positive-Cheeger regime with an explicit threshold bound

The cached Pete problem asks whether bounded-degree isoperimetric dimension >1 ensures p_c<1. The intake credits the dimension >4/Cayley results and leaves the non-Cayley intermediate regime unresolved. We give a self-contained stronger-hypothesis special case, not a new general resolution.

For an infinite connected graph of maximum degree D<infinity with edge-Cheeger constant h=inf_(finite nonempty S) |boundary_E S|/|S|>0, independent bond percolation satisfies

    1/(D-1) <= p_c <= 1/(1+h) < 1.

The lower bound is the union bound over at most D(D-1)^(r-1) simple paths of length r from a fixed vertex, for p(D-1)<1. To prove the upper bound, explore a cluster by testing only unrevealed edges from discovered vertices to undiscovered vertices. After s successful discoveries and f failures, the discovered set has s+1 vertices, and at least h(s+1)-f boundary edges remain untested. Thus the exploration cannot finish while Z=h+hs-f>0. The tests are an independent Bernoulli(p) sequence: each success adds h to Z and each failure subtracts 1. If p>1/(1+h), its drift is positive. For sufficiently small lambda>0, p exp(-lambda h)+(1-p) exp(lambda)<1. Then exp(-lambda Z), stopped at the first Z<=0, is a nonnegative supermartingale, and the probability ever reaching Z<=0 is at most exp(-lambda h)<1. With positive probability exploration never terminates, proving the upper bound. Critical equality itself is not decided by this drift argument. For the d-regular tree h=d-2, the upper bound matches its exact critical probability.

IP_(1+epsilon) does not supply a positive uniform h: the square lattice has a two-dimensional isoperimetric inequality but its square boxes have boundary/volume tending to zero. This explains the remaining gap rather than incorrectly applying the proved bound to the whole question.

## P0018: a valid one-edge shape; exclude the diagonal example

Randomstrasse101, arXiv:2603.29571, Definition 14.2 and Conjecture 31, PDF p.14, define the cited restricted graph matrices using a partition into left and right vertex sets. Overlapping index vertices and unindexed internal vertices are not supplied by that displayed definition. The diagonal signed-degree experiment in special_case_measurements.jsonl therefore belongs to a broader convention and is explicitly excluded as a special case of this literal problem. Its finite calculations are retained only as a scope warning.

A valid shape has two distinct vertices u,v, one edge uv, U={u} and V={v}. Injective labeling gives an n by n symmetric Rademacher matrix A with zero diagonal. It satisfies E||A||=Theta(sqrt(n)), so f=1/2 and g=0 for this shape. The lower bound is deterministic: ||A||>=||A||_F/sqrt(n)=sqrt(n-1). For a fixed unit real x, x^T A x=sum_(i<j)2x_i x_j epsilon_ij. Its moment-generating function is at most exp(s^2), since cosh z<=exp(z^2/2) and sum_(i<j)x_i^2 x_j^2<=1/2. Hence P(|x^T A x|>=r)<=2 exp(-r^2/4). A 1/4 net of the unit sphere has at most 9^n points and ||A||<=2 max_net |x^T A x|; a union bound and integration of this tail give E||A||<=C sqrt(n). This proves the shape exponents, without resolving the all-shapes existence conjecture.

valid_shape_measurements.json uses 12 samples each at n=64,128,256 and verifies the shape's n(n-1) nonzero entries. The mean norm divided by sqrt(n) is 1.926,1.955,1.974. At n=256 the old Frobenius upper bound is 255.500 and the mean norm is 31.5894, a factor 8.088 numerical gap. The experiment illustrates the bound's loss; the proved improvement is the order n to order sqrt(n) for this one shape.

## P0047: the finite/infinite component dichotomy is deterministic

Lyons-Peres, Probability on Trees and Networks, electronic edition 19 August 2026, Theorem 10.18 and Question 10.28, prove tail triviality but leave determinism of the FUSF component count on arbitrary networks open. The earlier attempt correctly warns that finite component counts can change under one edge modification.

For any spanning subgraph on a countable graph, adding or removing one edge changes a finite component count by at most one; finitely many modifications cannot change an infinite count to a finite one or conversely. For every finite edge set K, the event {infinitely many components} is therefore identical to the same event computed after setting all edges in K absent. It is measurable using only edges outside K, hence is a tail event. Under any tail-trivial forest law, in particular FUSF on an infinite connected locally finite network, its probability is 0 or 1. Thus either there are infinitely many components almost surely, or the number is finite almost surely. The latter alternative does not force the finite number to be constant.

This tail argument does not prove the full Question 10.28. On the infinite path, removing one edge changes the deterministic spanning subgraph from one component to two, so a generic finite count is not a tail statistic. Three finite path checks confirm this elementary obstruction; they are not samples from an allegedly random FUSF count. On a network that is itself a tree, every finite connected exhaustion has a unique spanning tree, and its free limit contains every edge, giving the trivial connected special case.
