# Second serious attempt, 2026-10-12

## Gap read from the first attempt

ATTEMPT.md Section 6 leaves matching positive L^p bounds, critical/intermediate switching rates in the exact spiral example, and the general higher-dimensional regularity classification unresolved. In particular, only necessary L^p conditions were proved; the cited positive result was C^k under stronger rates.

## Two approaches not previously tried

1. **Critical-rate resolvent plus local positivity.** At the source equilibrium 0, use the stationary last-entry density formula
   `rho_0(x)=lambda_1 integral_0^infinity exp((2-lambda_0)t) rho_1(exp(-At)x) dt`.
   If rho_1 has a uniform positive lower bound near 0, this gives logarithmic blow-up at lambda_0=2. The untried step is to prove local positivity from a finite switching-word construction, rather than assume pointwise density values or use the mass-persistence bound. This would address a single previously open critical case.

2. **L^p transfer decomposition at a fixed observation time.** Because both affine modes have the *same* matrix A, every switching path acts on its initial position by an affine map with linear part exp(AT). Separate paths with enough nondegenerate switch-time derivatives into a smoothing kernel Q and a remainder Delta. On the vector L^p space, the pathwise Jacobian gives the exact growth factor exp(-tr(A)(1-1/p)T). Paths with too few switches have probability decaying at rate min(lambda_0,lambda_1), up to a polynomial factor. Smoothly discard an arbitrarily small additional mass of degenerate switching times. If the probability-weighted remainder norm is less than one, a Neumann series gives a positive L^p result. Combined with a nested-flow-shell obstruction, this may give an exact integrability classification, even for nonconformal stable matrices in any dimension.

**Selected approach: 2.** It directly addresses the missing upper bounds and has a plausible dimension-independent necessary-and-sufficient rate condition. Approach 1 will be reconsidered only after the transfer argument has survived a full referee check.

## Research brain

Asked the math store about the gap with the exact query “PDMP invariant density critical switching rate resolvent positive density equilibrium Benaim Tough”. Raw result is saved in `gap_math_recall.txt`. Further transfer-operator and Neumann-series recalls, if used, will be logged here. Every retrieved card is treated as a hint rather than evidence.

## Initial candidate (subsequently proved as Theorem A)

For the stable common-matrix affine switched system F_0(x)=Ax, F_1(x)=A(x-a), with constant positive rates and full controllability, put D=-tr(A)>0. Candidate: for each finite p>1, the invariant density belongs to L^p(R^d x {0,1}) if and only if min(lambda_0,lambda_1)>D(1-1/p). Necessary equality cases must be included. The global L-infinity boundary requires a separate argument and is not part of this candidate yet.

The second brain query was “Feller Markov kernel Q Delta Neumann series Lp invariant densities Benaim Tough spectral radius”, saved as `gap_transfer_recall.txt`. It returned the standard Neumann-series lemma (card `claim_d42919cf2ac24118a84a6be3f315f5c9`), which is relevant to the proposed reduction. The other leading cards were off topic. The proof below writes out the series argument rather than relying on this card.

## Theorem A: exact finite-p classification for the common-matrix affine family

Let d>=1, let A be a real d-by-d Hurwitz matrix, and suppose the columns a,Aa,...,A^(d-1)a span R^d. Consider the two-mode PDMP

    X'=AX-Aa I,   I=0 or 1,
    0 -> 1 at constant rate lambda_0>0,
    1 -> 0 at constant rate lambda_1>0.

Write D=-tr(A)>0 and m=min(lambda_0,lambda_1). There is a unique invariant probability mu; both mode measures are absolutely continuous. For every finite p>1,

    rho in L^p(R^d x {0,1})  <=>  m>D(1-1/p).          (A.1)

Here rho denotes the two unnormalised mode densities; the same equivalence holds for the spatial marginal rho_0+rho_1. Failure of the condition implies failure of local L^p at the equilibrium of at least one offending mode, including equality. Moreover m>D implies a bounded continuous version of both mode densities on R^d. The theorem does not claim a necessary-and-sufficient L-infinity condition at m=D for arbitrary A.

### A.1 Existence, uniqueness, and compact support

Since A is Hurwitz, there are C,gamma>0 with ||exp(At)||<=C exp(-gamma t), t>=0. This follows, for example, by putting A into complex Jordan form: each Jordan block contributes a polynomial times the exponential of an eigenvalue, and the polynomial is absorbed by a slightly slower exponential. Set b=Aa. For a stationary two-sided two-state chain I, define

    X_t=-integral_0^infinity exp(Au)b I_{t-u} du.

The integrand's norm is at most C|b| exp(-gamma u), so the integral converges absolutely and |X_t|<=C|b|/gamma. Splitting it at a time increment proves the variation-of-constants identity. The joint law is stationary and follows the stated PDMP dynamics: conditional future paths of I depend only on its current state, even though X depends on its past. The mode probabilities are pi_0=lambda_1/(lambda_0+lambda_1) and pi_1=lambda_0/(lambda_0+lambda_1).

For uniqueness, use the common Poisson resampling coupling from ATTEMPT.md Section 2. Both chains coalesce at a finite time S almost surely; after S the positional difference is exp(A(t-S))(X_S-Y_S), tending to zero. For two invariant starting laws, differences of bounded Lipschitz test-function expectations tend to zero by bounded convergence and are constant by stationarity. Hence the invariant laws coincide. No moment hypothesis on arbitrary candidate invariant laws is needed. In particular the unique invariant law is the compactly supported construction above.

### A.2 The fixed-time switch map and its rank

Fix T>0 and initial mode i. Conditional on exactly n switches, their times lie in the open simplex

    S_n={0<s_1<...<s_n<T}.

Their unnormalised probability density is

    w_{i,n}(s)=(product_{j=0}^{n-1} lambda_{i+j mod 2})
                exp(-sum_{j=0}^n lambda_{i+j mod 2}(s_{j+1}-s_j)),

where s_0=0 and s_{n+1}=T. It is smooth and strictly positive. Summing its integral over n, and including the no-switch probability for n=0, gives 1. The final mode is i+n mod 2. The positional endpoint is

    X_T=M_T x+g_{i,n}(s),  M_T=exp(AT),
    g_{i,n}(s)=-integral_0^T exp(A(T-u))b I_u du.

The dependence on x is always the same affine map. If Delta_j=+1 or -1 is the jump of I at s_j, then

    partial_{s_j}g_{i,n}(s)=Delta_j exp(A(T-s_j))b.     (A.2)

This is obtained by differentiating the two integrals adjacent to the moving boundary s_j; all other integral terms are unchanged.

For n>=d, the determinant of the first d columns of (A.2) is a nonzero analytic function of s_1,...,s_d, apart from a constant sign and the invertible common factor M_T. To verify that it is not identically zero, observe that the vectors exp(-As)b, with s in any open interval, span R^d. Otherwise a nonzero linear functional ell would annihilate all of them. Differentiating the identically zero analytic function ell(exp(-As)b) at any interior s gives ell(exp(-As)(-A)^k b)=0 for k=0,...,d-1. But b,Ab,...,A^(d-1)b span R^d, since they are A applied to the independent columns a,Aa,...,A^(d-1)a and A is invertible. This contradicts ell nonzero. Thus one can choose d distinct times in any interval for which these columns are independent; sorting the times changes only the determinant sign. Choose the interval before T/2 when n>d and put the remaining times afterward, to stay inside S_n.

For completeness, a nonzero real-analytic function on a connected open set has a Lebesgue-null zero set. Here is the standard elementary proof. An analytic function vanishing on a nonempty open set vanishes on the whole connected domain: the set where every derivative is zero is closed by continuity and open by the local Taylor series, hence is the whole domain if nonempty. On a product box, expand in the first coordinate at an interior fixed coordinate value. At least one coefficient function in the other coordinates is nonzero as an analytic function; otherwise the function would vanish on the box. By induction on dimension, the zero set of that coefficient has measure zero. For every remaining choice of the other coordinates, the function of the first coordinate is a nonzero one-dimensional analytic function, whose zeros are isolated. Fubini proves that the full zero set on the box is null. The one-dimensional assertion follows directly from the first nonzero Taylor coefficient at any zero. A countable box covering finishes the proof. Applying this to the determinant gives full switch-map rank for almost every s in S_n, n>=d.

### A.3 A smooth cutoff kernel with arbitrarily small extra loss

For any epsilon>0, choose a finite N so that the probability of more than N switches is below epsilon/2 from either starting mode. For each d<=n<=N and each starting mode, take a smooth cutoff 0<=chi_{i,n}<=1, compactly supported inside S_n where the determinant in A.2 is nonzero, so that the discarded w_{i,n}-mass summed over this finite range is below epsilon/2. Such cutoffs exist: the regular locus is open, its complement has probability zero, finite measures are inner regular, and a compact subset of an open set admits a smooth bump function equal to 1 on it.

Define Q by the switch paths in this finite range, weighted by chi; define Delta=P_T-Q. Both are nonnegative sub-Markov kernels, because the weights lie in [0,1]. Their probabilities depend only on the starting mode, not on x. Write r_i=Delta((x,i),R^d x {0,1}) and r=max(r_0,r_1). Then

    r<=max_i P_i(number of switches in [0,T]<d)+epsilon.  (A.3)

The pushforward of chi_{i,n} w_{i,n}(s) ds under g_{i,n} has a smooth compactly supported density q_{i,n}. To check this claim without hiding regularity at a boundary, cover the compact support of chi by finitely many submersion coordinate charts and use a smooth partition of unity. In each chart the map s -> (g(s),s_{d+1},...,s_n) is a diffeomorphism. The transformed integration density is smooth with compact support strictly inside its chart. Integrating over the remaining n-d coordinates produces a smooth compactly supported function of g. Extend each contribution by zero and sum; there are no chart-boundary singularities because every contribution is compactly supported there. For n=d this is simply the inverse-function change of variables.

Consequently Q has kernels q_{ij}(y-M_T x), where q_{ij} is a finite sum of such smooth compactly supported functions. For any finite measure nu, its Q-image has density

    f_j(y)=sum_i integral q_{ij}(y-M_T x) nu_i(dx).

All derivatives exist and are continuous by dominated convergence, using the globally bounded derivatives of q. For 1<=p<=infinity, Minkowski's integral inequality gives

    ||f_j||_p<=sum_i nu_i(R^d)||q_{ij}||_p,

so nu Q has an L^p density for every p. For a compactly supported nu, the density is also compactly supported. In particular this applies to the invariant mu constructed in A.1.

### A.4 The correct L^p operator norm of the remainder

Use the vector norm ||f||_{p,1}=||f_0||_p+||f_1||_p. For any affine path x -> M_T x+z, its density pushforward is

    y -> |det M_T|^{-1} f(M_T^{-1}(y-z)).

Changing variables gives its L^p norm exactly

    |det M_T|^{-(1-1/p)}||f||_p
       =exp(D(1-1/p)T)||f||_p.                       (A.4)

For p=infinity use 1/p=0; the same formula holds. Integrate over the discarded path law and apply Minkowski. Summing output modes before bounding, one obtains

    ||f Delta||_{p,1}<=exp(beta T) sum_i r_i||f_i||_p
                     <=exp(beta T)r ||f||_{p,1},    (A.5)
    beta=D(1-1/p).

The sum over modes is essential: an estimate only of spatial contraction without the discarded probability would not imply this result. On finite signed measures, the total-variation norm of Delta is at most r. These statements also hold for signed densities by replacing f with its absolute value in the inequalities.

### A.5 Making the remainder a strict contraction

Let m=min(lambda_0,lambda_1). The switch count stochastically dominates a Poisson count of rate m. A direct construction uses a state-independent rate-m Poisson clock, at every event of which the state flips, and extra proposed events at rate max(lambda_0,lambda_1)-m, accepted in state i with probability (lambda_i-m)/(max(lambda_0,lambda_1)-m). If the denominator is zero no extra clock is used. This has precisely the required rates and its switch count is at least the base-clock count. Thus

    max_i P_i(number of switches<d)
       <= exp(-mT) sum_{k=0}^{d-1}(mT)^k/k!.          (A.6)

If m>beta, choose T sufficiently large that

    exp(beta T)exp(-mT) sum_{k=0}^{d-1}(mT)^k/k!<1/2.

This is possible because exponential decay with exponent m-beta dominates the fixed-degree polynomial. In A.3 choose epsilon<exp(-beta T)/2. Then c=exp(beta T)r<1. Notice the order: T is chosen first, and the finite switch cutoffs are chosen afterward. No uniform cutoff estimate in T is assumed.

Write mu=mu P_T=mu Q+mu Delta and iterate:

    mu=sum_{k=0}^{n-1} mu Q Delta^k+mu Delta^n.

The residual total mass is at most r^n and tends to zero. If g is the density of mu Q, A.5 gives ||g Delta^k||_{p,1}<=c^k||g||_{p,1}. The nonnegative densities therefore have a sum with L^p norm at most ||g||_{p,1}/(1-c), by finite Minkowski sums and Fatou (or the monotone essential-supremum estimate when p=infinity). The measure sum is mu since the residual vanishes in total variation. This proves absolute continuity and L^p sufficiency without assuming that the unknown invariant density was already in L^p. Taking p=1, beta=0 and m>0 proves absolute continuity for every positive pair of rates.

When m>D, the same construction works on the vector space C_0(R^d) with its sum of sup norms. Each affine inverse path preserves C_0, the path translations are bounded for fixed T, and dominated convergence shows that Delta preserves continuity and vanishing at infinity. Its norm is at most exp(DT)r<1. Since mu Q has a smooth compactly supported density, its series converges uniformly to a C_0 version of the density of mu. Thus the positive L-infinity result also supplies continuity.

### A.6 Necessity, including the exact threshold, for nonconformal A

Fix a mode i and its equilibrium c_i (0 or a). We need disjoint shrinking sets with their exact volumes; Euclidean annuli are not preserved when A is anisotropic. Define

    P=integral_0^infinity exp(A^T t)exp(At) dt.

The integral converges by A.1, P is symmetric positive definite (its quadratic form integrates |exp(At)v|^2), and differentiation gives A^T P+PA=-Id. Hence the P-norm decreases strictly along exp(At)v for every v nonzero. Choose a P-ball B centered at c_i containing the compact invariant spatial support. Its forward images under this mode are nested and shrink to c_i.

Absolute continuity and the positive mode mass pi_i imply that, for some sufficiently large T, E=B\phi^i_T(B) has mode mass M>0; indeed the measure of the inner ball tends to zero while mu_i(B)=pi_i. Choose B open and larger than the support to avoid a boundary convention. Its images are open; E remains Borel. Put E_n=phi^i_{nT}(E). They are pairwise disjoint because they are consecutive differences of the nested sets phi^i_{nT}(B), and they eventually lie in every neighborhood of c_i. Their volumes are

    vol(E_n)=exp(tr(A)nT)vol(E)=exp(-DnT)V, V>0.

The no-switch persistence inequality, valid for this mode's constant rate, gives mu_i(E_n)>=exp(-lambda_i nT)M. For finite p>1, Holder therefore gives

    integral_{E_n} rho_i^p
      >= M^p V^{1-p} exp((D(p-1)-lambda_i p)nT).

If lambda_i<=D(1-1/p), the exponent is nonnegative, and summing over the disjoint E_n diverges, including at equality. This proves the necessary direction of A.1 and its local assertion. If lambda_i<D, the ratio of mass to volume tends to infinity, proving local essential unboundedness. For lambda_i=D this argument deliberately makes no conclusion about boundedness. Nonnegativity makes every obstruction also apply to the spatial marginal. Conversely, summing the two L^p component densities preserves L^p. **Theorem A is proved.**

## What has improved already

For the exact source example D=2. For any finite p>1 we now have the full equivalence

    rho in L^p  <=>  min(lambda_0,lambda_1)>2(1-1/p).

For instance at rates (1/2,3), rho belongs to every L^p with 1<=p<4/3 and to none with p>=4/3. The previous attempt had only the negative half. This is a complete classification of finite-p integrability in an important family, not a full solution of the source's general smoothness question. The paper's global C^k question and general nonlinear/state-dependent systems remain separate.

## Theorem B: the critical rate and exact boundedness/continuity classification in the source spiral

For the exact source Example 4.7, the invariant density has a bounded version if and only if min(lambda_0,lambda_1)>2. The same strict inequality characterizes the existence of a continuous version on all of R^2. At min(lambda_0,lambda_1)=2, both components and their spatial marginal belong to every finite L^p, but at least one component is locally essentially unbounded. At lambda_0=2 there are c,delta>0 such that

    rho_0(x)>=c log(delta/|x|) for almost every 0<|x|<delta. (B.1)

The assertion at a with lambda_1=2 is its reflected counterpart. These are lower bounds, not asserted exact logarithmic asymptotics.

### B.1 A concrete support construction: 0 is an interior point for both modes

Write a=(1,0), A=-Id+J, b=Aa=(-1,1), and

    w(t)=-exp(At)b=exp(-t)R_t(1,-1).

In the stationary convolution, X_0=integral_0^infinity w(t) I_{-t}dt. Fix L>0, and choose t_1=L, t_2=L+2pi/3, t_3=L+4pi/3. Put k_j=exp(t_j)>0. Then

    sum_{j=1}^3 k_j w(t_j)=0,

because three equally spaced 120-degree rotations of any vector sum to zero. The first two w(t_j) are independent: their determinant is 2 exp(-(t_1+t_2))sin(2pi/3), which is positive.

Define, for h near 0 in R^3, the smooth map

    F(h)=sum_{j=1}^3 integral_{t_j}^{t_j+h_j} w(t)dt.

Negative h values are used only to extend the map smoothly for the implicit-function theorem. At h=0 its first two derivative columns are the independent w(t_1),w(t_2). Set h_3(epsilon)=epsilon k_3. The implicit-function theorem produces smooth h_1(epsilon),h_2(epsilon), with h_1(0)=h_2(0)=0 and F(h_1(epsilon),h_2(epsilon),epsilon k_3)=0. Differentiating at epsilon=0 gives

    w(t_1)h_1'(0)+w(t_2)h_2'(0)+w(t_3)k_3=0.

The positive linear relation above and independence imply h_1'(0)=k_1>0 and h_2'(0)=k_2>0. Hence for every sufficiently small positive epsilon all three h_j are positive and less than pi/3. The three pulse intervals [t_j,t_j+h_j] are then disjoint. Their integral is exactly 0. Also, by continuity, the first two derivative columns w(t_1+h_1),w(t_2+h_2) remain independent. With h_3 fixed at this small positive value, varying the two positive lengths h_1,h_2 in an open neighborhood therefore maps onto an open neighborhood of 0 in R^2.

Every such three-pulse integral belongs to the support of mu_0. To verify this, for an arbitrary accuracy eta>0 choose H after the last pulse so that sqrt(2)exp(-H)<eta/3. Prescribe I_{-t}=1 on the three pulse intervals and 0 elsewhere in [0,H]. The stationary two-state chain is reversible, since pi_0 lambda_0=pi_1 lambda_1, so in reverse time it has the same positive jump rates. Starting with I_0=0, the event of exactly these six switches, each within a sufficiently small window about the six prescribed endpoints and with no additional switches up to H, has strictly positive probability. Small enough windows change the integral on [0,H] by less than eta/3, because w is bounded and the total symmetric difference of the pulse intervals is small. The unprescribed tail has norm at most sqrt(2)exp(-H)<eta/3. Thus mu_0 assigns positive mass to the eta-ball about the prescribed pulse integral. This is precisely support membership. The open range just constructed proves that 0 is an interior point of supp(mu_0).

The two mode supports coincide. Indeed the last-entry identity

    mu_1(D)=lambda_0 integral_0^infinity exp(-lambda_1 t)
                            mu_0((phi^1_t)^{-1}(D))dt

shows supp(mu_0) is contained in supp(mu_1): given x in the first support and an open neighborhood U of x, continuity of (t,y)->phi^1_t(y) gives t_0>0 and a neighborhood V of x with phi^1_t(V) contained in U for 0<t<t_0. Then mu_1(U)>=lambda_0 mu_0(V)integral_0^{t_0}exp(-lambda_1 t)dt>0. The analogous identity for mu_0 gives the reverse containment. Thus 0 is an interior support point for both modes. This argument uses neither a guessed picture of the support nor a quoted positivity theorem.

### B.2 A uniform density lower bound near 0

Choose a small T>0, T<1, and start in mode 1 with exactly two switches at s_1=T/3 and s_2=2T/3; the final mode is again 1. In the notation of A.2 the endpoint is exp(AT)x+g(s_1,s_2). Both switch-time derivative columns are independent, since their determinant is a nonzero multiple of sin(s_1-s_2) and 0<s_2-s_1<1. Set

    x_*=-exp(-AT)g(s_1,s_2).

We have |g|<=sqrt(2)T, and ||exp(-AT)||=exp(T). Consequently |x_*|<=sqrt(2)T exp(T), so T can be chosen small enough that x_* lies in the interior support neighborhood of mu_1 obtained in B.1. The selected path then ends exactly at 0.

Take a nonnegative smooth cutoff of the two switch times, equal to 1 near this pair and supported in a small neighborhood on which g is a diffeomorphism. The smooth switch-time density is strictly positive there. Its pushforward density q is smooth and satisfies q(g(s_1,s_2))>0 by the inverse-function change of variables. Continuity therefore provides a neighborhood U of 0, a neighborhood V of x_*, and a constant c_0>0 such that

    q(y-exp(AT)x)>=c_0 for every y in U and x in V.

Since x_* is in supp(mu_1), mu_1(V)>0. Stationarity and positivity of all other path contributions imply the measure inequality

    mu_1(dy)>=integral_V q(y-exp(AT)x)mu_1(dx)dy
             >=c_0 mu_1(V) 1_U(y)dy.

Absolute continuity was proved in Theorem A, so rho_1>=c_0 mu_1(V)>0 almost everywhere on U. Shrink U to a ball B(0,delta). This proves the required uniform lower bound without assigning a value to rho_1 at 0. The proof works for every positive pair of rates.

### B.3 The critical resolvent lower bound and conclusion

The reverse last-entry identity is

    mu_0=lambda_1 integral_0^infinity exp(-lambda_0 t)(phi^0_t)_*mu_1 dt.

It follows by looking back to the most recent 1-to-0 switch, with a no-switch remainder of total mass pi_0 exp(-lambda_0 H) that vanishes as H tends to infinity, exactly as in ATTEMPT.md Section 4. Since phi^0_t(x)=exp(At)x has determinant exp(-2t), Tonelli and change of variables give the density formula, almost everywhere,

    rho_0(x)=lambda_1 integral_0^infinity
                   exp((2-lambda_0)t)rho_1(exp(-At)x)dt. (B.2)

The lower bound in B.2 of this document for rho_1 holds almost everywhere; for each t its inverse-affine pullback also holds almost everywhere. Fubini then permits its use for almost every x and almost every t simultaneously. For 0<|x|<delta, ||exp(-At)x||=exp(t)|x|<delta when 0<t<log(delta/|x|). At lambda_0=2, restricting B.2 to this interval proves

    rho_0(x)>=lambda_1 c_0 mu_1(V) log(delta/|x|)

for almost every such x. This is B.1 and implies essential unboundedness in every neighborhood of 0. Reflecting x -> a-x and exchanging mode labels proves the assertion at a when lambda_1=2.

If some rate is below 2, the earlier persistence lemma already gives essential unboundedness at its equilibrium. If both rates exceed 2, Theorem A gives a bounded continuous version. These statements cover all positive rate pairs and establish the claimed necessary-and-sufficient boundedness and continuity condition. A continuous version would be bounded on any sufficiently small closed ball about an equilibrium, so it cannot exist in the critical or subcritical cases. At m=2, Theorem A puts both densities in every finite L^p because 2>2(1-1/p) for every finite p>1. **Theorem B is proved.**

### Why the critical statement is specific to the spiral

For the one-dimensional model A=-1, a=1, rates (lambda_0,lambda_1)=(1,2), the invariant densities are rho_0(x)=2(1-x)^2 and rho_1(x)=2x(1-x) on (0,1), and zero elsewhere. Their total density is 2(1-x) on (0,1). They are bounded even though m=D=1. Thus Theorem A's strict rate condition for L-infinity is sufficient but cannot be claimed necessary at equality for arbitrary A. The spiral proof uses the extra, explicitly established interior support and positivity at its equilibrium.

## Corollary C: the same decomposition gives a complete proof of the known C^k sufficient condition

Let Lambda_min be the smallest real part of an eigenvalue of A. Under Theorem A's assumptions, for every integer k>=0,

    min(lambda_0,lambda_1)>D-k Lambda_min
          implies a C^k density on all of R^d.       (C.1)

This is the sufficient condition already found in Benaim--Bichard, Theorem 2.2. We record a proof by the fixed-observation-time method, not a claim of novelty or a necessary condition.

**Proof.** Let C_0^k be the space of functions whose derivatives of orders 0,...,k are continuous and vanish at infinity, with norm sum_{j=0}^k ||D^j f||_infinity, using the Euclidean operator norm on derivative tensors. Give the two-mode space the sum of these norms. This is a Banach space: uniform convergence of derivatives preserves derivative identities by the fundamental theorem of calculus on line segments, and uniform limits preserve vanishing at infinity.

For a fixed affine path at time T, its density pushforward has j-th derivative norm at most exp(DT)||exp(-AT)||^j times the original j-th derivative norm, by the chain rule. Repeating the mode sum in A.4 gives

    ||f Delta||_{C^k,1}<=W_k(T) r ||f||_{C^k,1},
    W_k(T)=exp(DT) max_{0<=j<=k} ||exp(-AT)||^j.     (C.2)

The path translations are uniformly bounded for fixed T. Thus differentiating under the discarded path integral is justified by the bounded derivatives, and each derivative remains continuous and vanishes at infinity. Delta preserves C_0^k.

By Jordan-form estimates, for any eta>0 there is C_eta with ||exp(-AT)||<=C_eta exp((-Lambda_min+eta)T) for T>=0. If k>=1 and (C.1) holds, choose eta>0 sufficiently small that m>D+k(-Lambda_min+eta). If k=0 simply use m>D. Then

    W_k(T) exp(-mT) sum_{j=0}^{d-1}(mT)^j/j! -> 0.

Choose T so this is below 1/2 and then choose the smoothing cutoffs so their extra loss epsilon is below 1/(2W_k(T)). The resulting C^k operator norm of Delta is less than 1. The density of mu Q is smooth and compactly supported by A.1 and A.3, hence belongs to C_0^k. The series sum_{n>=0} mu Q Delta^n converges in C_0^k. Its measure equals mu, since the positive remainder mu Delta^n tends to zero in total variation as in A.5. This proves (C.1). QED.

For the source spiral Lambda_min=-1 and D=2, so this proves C^k whenever both rates exceed k+2, including k=0 already used in Theorem B. This method does not prove that failure of (C.1) implies failure of C^k for general k.

## Referee audit of the follow-up

- The norm on the two-mode density space is the sum of the component L^p norms. Summing path output modes gives the discarded probability r_i, not an unnoticed extra factor of 2.
- Cutoffs depend only on switching times and the initial mode. They do not depend on x, which is necessary for the affine pushforward norm estimate.
- Q is constructed from smooth compact cutoffs strictly inside the full-rank locus. The uncut transition kernel is not assumed to have a smooth density.
- The switching count bound is a Poisson domination from a concrete base-clock construction, not an unjustified comparison of state-dependent holding times with independent ones.
- The Neumann-series argument first controls the residual in total variation; it does not insert the unknown density into an L^p space circularly.
- Nonconformal necessity uses consecutive differences of nested ellipsoids. Rotating Euclidean annuli would not suffice for a general matrix.
- The finite-p equality case is excluded by disjoint-shell summation. The infinity equality case is deliberately separated, and the one-dimensional bounded critical example checks this distinction.
- In the support construction, positive pulse lengths are obtained by an implicit-function argument from a strictly positive linear dependence. Numerical cancellation is only a diagnostic.
- Positivity near 0 is a measure lower bound derived from a fixed-time smooth subkernel. Mere membership in the support is not used as a substitute for a positive density lower bound.
- Logarithmic divergence is proved only as a lower bound, for an almost-everywhere density version. No exact asymptotic or arbitrary pointwise value is asserted.

## Remaining gap after this second attempt

The follow-up closes the first attempt's missing positive finite-L^p bounds and the critical-rate boundedness question for the source spiral. It also establishes an exact finite-p integrability theorem for every stable controllable common-matrix two-mode affine system. It does not classify higher differentiability in all source parameter regimes, describe every propagated singularity, prove smoothness away from all such singularities, or settle arbitrary nonlinear switched flows and position-dependent continuous rates. The honest overall E0019 verdict therefore remains PARTIAL.
