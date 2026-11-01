# C0052: Lee–Yang route

Author-derived lemmas, not independently checked. The parent problem remains unproved. ROUTE_PRECOMMIT.md records this choice before any peer proof was read. Exact target and model are in STATEMENT_PACKET.md.

## Hardest remaining gap

For beta increasing to beta_c in the nearest-neighbor Ising model on Z^3, prove that the first Lee–Yang zero of the block selected below stays at bounded distance after multiplication by the block's standard deviation. Even a bounded subsequence suffices for the source's non-vanishing target. This bound is presently UNPROVED. No finite computation establishes it.

## L1. Exact zero/cumulant identity and quantitative Gaussian criterion

Assume S is a bounded, symmetric, real random variable of variance V>0, and F(z)=E exp(zS) has only imaginary zeros. Write its positive imaginary zeros as i y_j, with multiplicities; y_1 is the smallest. Then

F(z)=product_j(1+z^2/y_j^2),
V=2 sum_j y_j^(-2),
kappa_4(S)=-12 sum_j y_j^(-4).

For X=S/sqrt(V), r_j=sqrt(V)y_j, and B=3-E X^4=-kappa_4(S)/V^2,

sum_j r_j^(-2)=1/2,
B=12 sum_j r_j^(-4),
12/r_1^4 <= B <= 6/r_1^2.

Proof: F is even and entire of exponential type because S is bounded. H(w)=F(sqrt(w)), defined by the even power series, is entire of order at most 1/2; its zeros are -y_j^2. Hadamard factorization for order below 1 gives the genus-zero product with constant H(0)=1 and sum_j y_j^(-2)<infinity. No exponential quadratic factor is permitted at this order. Differentiating log F at zero gives the displayed cumulants. With a_j=r_j^(-2), sum a_j=1/2 and max a_j=r_1^(-2); therefore a_1^2 <= sum a_j^2 <= a_1/2, proving both constants. A nonconstant H has a zero, since a zero-free entire function of order below 1 would be constant by the same factorization.

Also E exp(tX)<=exp(t^2/2) for every real t: use log(1+t^2/r_j^2)<=t^2/r_j^2 in the product. Chernoff gives P(|X|>u)<=2 exp(-u^2/2), uniformly over all such X. Thus the fourth powers in any sequence are uniformly integrable. For a sequence satisfying these hypotheses, X_n converges in law to N(0,1) if and only if r_1,n tends to infinity. Gaussian convergence implies B_n->0 by uniform integrability, hence r_1,n->infinity by the lower bound. Conversely, for |z|<r_1,n,

|log E exp(zX_n)-z^2/2| <= |z|^4/[4 r_1,n^2(1-|z|^2/r_1,n^2)].

This follows from the power series for log(1+w), the bound sum a_j^2<=1/(2r_1,n^2), and termwise absolute convergence. If r_1,n->infinity, the generating functions converge locally uniformly to exp(z^2/2), implying Gaussian weak convergence. If r_1,n<=C along a subsequence, every weak limit on that subsequence has variance 1 and fourth moment at most 3-12/C^4, and is non-Gaussian. Tightness follows from variance 1 and moment convergence from the uniform tail bound.

Application hypotheses: zero-field finite ferromagnetic pair-interaction Ising graphs satisfy spin-flip symmetry and the multivariate Lee–Yang theorem. For S=sum f_x sigma_x with f_x>=0, first take every f_x>0 so the fugacities lie strictly inside or outside the unit circle when Re(z) is nonzero. For weights equal to zero, take a positive-weight approximation and apply Hurwitz on each open half-plane; the limit cannot be identically zero since F(t)>0 on the real axis. The same argument applies to a fixed finite-support observable in a spin-flip symmetric infinite-volume free-state limit: its finitely many marginal probabilities converge, so its generating functions converge locally uniformly. These are actual Gibbs marginals, not independent spins in the block.

## L2. One-sided bridge to the source's global coupling

Fix 0<beta<beta_c in Z^3. Assume the translation-invariant symmetric free state, G>=0, chi<infinity, 0<xi<infinity, U4<=0, and summability of -U4. These are the precise hypotheses used, including repeated indices in U4. Let K=-U4 and A=sum_{x2,x3,x4} K(0,x2,x3,x4)=g_+ chi^2 xi^3.

Let ell be the smallest positive integer for which sum_{|z|_infinity<=ell}G(z)>=chi/2. It exists by susceptibility summability. Put R=max(1,ceil(xi),ell), Lambda={x:|x|_infinity<=2R}, N=(4R+1)^3, S=sum_{x in Lambda}sigma_x, V=E S^2, and r=sqrt(V)y_1, where y_1 is the first zero of E_beta exp(hS) in the dimensionless field h applied only to Lambda.

Then

g_+(beta) >= (N/xi^3)(V/(N chi))^2 B >= B/4 >= 3/r^4.

Proof: -kappa_4(S)=sum_{x1,x2,x3,x4 in Lambda}K(x1,x2,x3,x4)<=N A by positivity and translation invariance. Hence g_+>=B V^2/(N chi^2 xi^3). For each x in the inner cube |x|_infinity<=R, its entire R-neighborhood lies in Lambda and contributes at least chi/2 to sum_{y in Lambda}G(y-x). The inner cube contains (2R+1)^3>=N/8 vertices. Therefore V>=N chi/16. Also N/xi^3>=64 since R>=xi. Substitute these bounds to obtain g_+>=B/4 and apply L1. Every summation is over the actual joint Gibbs law. No independence or product of conditional estimates is used.

Consequently, r bounded along beta_n increasing to beta_c implies limsup g_+>0. A uniform eventual bound r<=C implies liminf g_+>=3/C^4. Conversely g_+->0 forces r->infinity for these selected blocks. The converse assertion r->infinity implies g_+->0 is NOT established: L2 is only a lower bound on g_+.

The block R need not be comparable above to xi: ell is a susceptibility quantile, and only R>=xi is used. This choice proves the variance-capture bound without presuming a correlation-length scaling law. The missing bound on r must apply to this precisely selected block, not to a free-boundary finite-volume partition function or a different block size without comparison.

## Failed closure and control example

The Lee–Yang theorem locates the zeros on an axis but gives no uniform upper bound on r. For N independent fair Ising spins, F(h)=cosh(h)^N, V=N, y_1=pi/2, r=pi sqrt(N)/2, and B=2/N. All L1 hypotheses hold, while r diverges and the normalized sum converges to a Gaussian. Absolute zeros approaching zero at a critical thermodynamic limit also give no bound on sqrt(V)y_1 when V diverges. Thus a thermodynamic first-zero theorem cannot close the gap without a quantitative rate and the correct block-field comparison. The example checks the proposed implication's scope; it is not a counterexample to 3D critical Ising.

## Prior-attempt digest (initial targeted recovery)

The C0052-A001 intake record dated 2026-09-07 uses random-current intersection probabilities, conjectural fractal dimension heuristics, and a second-moment route. It explicitly leaves the variance of the intersection count open, involving higher correlations. None of its numerical exponents or claimed equivalences are used as lemmas here. A solver-map edge to C0051 is conditional on a variance estimate and is not an unconditional reduction. The Lee–Yang route avoids that recorded computation. Targeted searches of the named H/I and Lean intake records found no exact C0052 match; further relevant Ising records are being checked. No peer proof has been read.

## Review obligations

Check (1) the order-1/2 factorization and multiplicity constants, (2) Hurwitz with zero block weights and infinite-volume marginals, (3) the sign and summability of U4, including repeated indices, (4) all powers of N, chi, xi, and the factors 16 and 64 in L2, (5) that the unresolved bound is stated for the selected Gibbs marginal. Finite checks are diagnostic, not independent mathematical review or a formal proof receipt.
