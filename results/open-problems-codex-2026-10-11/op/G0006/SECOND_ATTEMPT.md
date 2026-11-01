# G0006 — second serious attempt (2026-10-11)

Final outcome: PARTIAL. The original all-dimensional gap remains unproved. Theorem 8 gives a complete finite-certificate characterization in d=2; no critical-rate certificate is established.

The previous remaining gap is an upper bound on infected spatial connectivity at a rate strictly above lambda_c. No such bound follows from marginal density or stationary pairs.

Two approaches not pursued in the first attempt:

A. Finite-volume stationary laws with permanently infected exterior, and block annulus crossing events. Dominate the infinite-volume law locally by these finite-state laws, color enlarged blocks using a fixed number of colors, and derive a computable renormalization certificate from a finite stationary crossing probability. Unlike the earlier singleton exit criterion, the independence penalty is fixed as the block size grows. Pursue this first: it preserves actual spatial connectivity and permits a concrete finite-state calculation.

B. A cluster-weight stationarity identity. Replace the one-site observable by the reciprocal finite occupied-cluster size, or a truncated cluster generating function. A birth can merge finite components or attach them to an infinite one, while a death can split a component. A mass-transport rewrite might control the density of infinite components directly and avoid averaging infinite vertices together with isolated sites. The obstacle to check is that truncation errors and pivotal split/merge terms depend on multi-point connectivity, not only density. This is a distinct dynamic reduction, not a product comparison.

Chosen approach: A. It gives a finite and explicitly testable certificate and does not presuppose near-critical mixing. No success is claimed yet.


## Progress saved: buffered block certificate

A buffer is needed if the wired finite-volume calculation is to approximate an infinite-volume crossing law. For block side L define C_z=Lz+[0,L-1]^d, M_z=Lz+[-L,2L-1]^d, and D_z=Lz+[-2L,3L-1]^d. Run the finite contact process on D_z with all exterior vertices permanently infected. Let b_L(lambda) be its stationary probability of an occupied path, entirely in M_z, from C_z to the inner vertex boundary of M_z.

Candidate theorem now being checked: b_L(lambda)<(2d-1)^(-5^d) implies nonpercolation of nu_lambda. Disjoint D_z boxes are independent after coloring z by its coordinate residues modulo 5; this number of colors does not grow with L. Continuity of this finite stationary probability implies that a strict certificate at lambda_c would imply a gap.

A further reduction looks possible in dimension two: the original gap should be equivalent to existence of such a finite certificate at lambda_c. For necessity, choose a rate strictly between lambda_c and a supercritical nonpercolating rate, apply van den Berg's exponential cluster-size theorem, and control the buffered wired-law discrepancy by finite propagation plus exponential temporal convergence. This implication must be written fully before it is called proved.

The earlier 3-by-3 calculation in compute_wired.py is the UNBUFFERED diagnostic, not the 5-by-5 L=1 buffered law. It gives crossing probability 0.204892335 at lambda=1/4 and 0.393353517 at lambda=0.4; these are floating-point results only. They fail the unbuffered certificate. No stationary buffered probability has yet been certified.


## Theorem 6: finite stationary block certificate (all d >= 2)

Definitions. L is a positive integer, k=2d, and C_z, M_z, D_z are the cubes defined above. The inner vertex boundary of M_z consists of the vertices of M_z having a nearest neighbor outside M_z. Let pi_D,lambda be the unique stationary law of the contact process on D with its exterior permanently infected. Inside D, a healthy vertex x is infected at rate lambda times its occupied neighbors inside D plus lambda times the number of its neighbors outside D. It recovers at rate 1. Let b_L(lambda) be the pi_D,lambda probability of an occupied nearest-neighbor path from C to the inner boundary of M, entirely inside M. Put

    tau_d = (2d-1)^(-5^d).

Claim. If b_L(lambda)<tau_d for any L, then nu_lambda has no infinite occupied component. b_L is continuous and nondecreasing in lambda. Thus if b_L(lambda_c)<tau_d for some L, then lambda_c<lambda_p. It also suffices to certify b_L(u)<tau_d at any rigorous upper bound u>=lambda_c, since continuity permits a slightly larger rate.

Proof of existence and coupling of the finite stationary laws. Use recovery clocks at vertices of D and infection-arrow clocks whose TARGET lies in D. Arrows with sources outside D treat their sources as permanently infected. Starting at any two configurations and using these clocks preserves their order. In a unit interval with no arrow having target in D and with a recovery at every vertex, every initial state becomes empty. This event has positive probability exp(-k*lambda*|D|)*(1-exp(-1))^|D|. On independent successive intervals the probability that this has never occurred decays geometrically. Consequently all initial states coalesce, there is a unique stationary law, and it is determined by the clocks arbitrarily far in the past. One may equally use the eventually constant pullback states from the all-infected initial state.

Use the same global graphical clocks to define the stationary infinite-volume upper law nu_lambda and each pi_Dz,lambda. The wired finite process dominates the infinite process on its own domain because its exterior is always occupied. Taking the coupled pullback limit preserves this domination. For disjoint D domains, the input families of clocks are disjoint: each arrow is assigned by its target. In particular an arrow crossing between domains is used only by the domain containing its target. Its source occupation is a fixed 1 there, not the random occupation in the other domain. Thus the wired finite fields are independent on disjoint domains. They are not independent on overlapping domains.

Proof of the block estimate. Color coarse sites z by their d coordinate residues modulo 5, using m=5^d colors. Distinct same-colored D_z cubes have disjoint vertex sets: their centers differ in some coordinate by at least 5L, equal to the side length of D_z. Therefore the corresponding crossing indicators are independent and identically distributed with parameter b_L.

If an infinite occupied component of nu_lambda meets a coarse block C_z, it has an occupied path from a vertex of C_z to the boundary of M_z. The path up to its first boundary visit lies in M_z, so the wired crossing indicator at z is 1. The set of coarse blocks visited by the component is infinite and connected in the nearest-neighbor coarse lattice: a nearest-neighbor site step either stays in one C block or moves to a nearest-neighbor C block. Thus that component gives an infinite connected set of good coarse sites.

There are at most k*(k-1)^(n-1) self-avoiding n-edge coarse paths from a fixed z. In each such deterministic path, one color appears at least ceil((n+1)/m) times. The probability that every site of the path is good is at most b_L^ceil((n+1)/m), by restricting to that color. The union bound gives

    P(z begins a good n-edge self-avoiding path)
      <= k*(k-1)^(n-1)*b_L^((n+1)/m).

For b_L<tau_d this tends to zero. Hence no coarse site belongs to an infinite good component, almost surely, using countability. No infinite component of nu_lambda is possible. The case b_L=0 is immediate and needs no interpretation of a fractional power.

Continuity and monotonicity. This finite chain has a generator whose entries are affine polynomials in lambda. Replace one equation in the transposed stationary system by normalization. The resulting finite linear system is invertible as follows: for lambda>0 the connected finite chain is irreducible (recover to empty, infect successively from its boundary to fill the domain, then recover unwanted sites). Its stationary nullspace is one-dimensional. At lambda=0 the generator is triangular when ordered by occupancy count, with eigenvalues minus the counts and exactly one zero, again giving an invertible normalized system. Cramer's rule makes every stationary probability a rational function of lambda with no denominator zero on lambda>=0. In particular b_L is continuous, even at zero, where the unique stationary law is empty. Monotonicity follows by adding infection arrows and taking ordered pullback limits. If b_L(lambda_c)<tau_d, continuity gives some epsilon>0 with b_L(lambda_c+epsilon)<tau_d. Nonpercolation at that rate yields lambda_p>=lambda_c+epsilon. The upper-bound-u assertion is identical with u in place of lambda_c. QED.

Unlike Proposition 5's singleton-exit method, the exponent penalty here is 5^d, independent of L. The previous prescribed-path obstruction with an exponent growing as L^d therefore does not rule out this certificate. This statement concerns the two particular criteria; it does not assert that b_L is small.

## Lemma 7: a quantitative buffered comparison at a fixed supercritical rate

This lemma is asserted here for d=2, using an explicitly verified literature input. Let lambda>lambda_c. Van den Berg (2011), Theorem 2.1, arXiv:0907.2843v2 PDF p. 5, gives constants C3,C4>0 such that the all-infected process at time T satisfies

    d_TV(mu_T restricted to F, nu_lambda restricted to F)
      <= |F|*C3*exp(-C4*T)

for every finite F and T>0. In particular its single-site density differs from nu_lambda's by at most C3*exp(-C4*T). Constants can depend on the chosen rate; no uniform near-critical assertion is used.

Claim. In the common monotone graphical coupling, for the buffered D and M above, for every T>0,

    P(pi_D,lambda and nu_lambda differ anywhere on M)
      <= |M| * [C3*exp(-C4*T) + sum_{n>=L} (k*lambda*T)^n/n!].

Proof. Start both the wired D process and the full-lattice process all infected at time -T. Their time-zero values dominate their respective stationary pullback values. Moreover wired stationary values dominate nu_lambda. If the wired stationary field and nu_lambda disagree at x, the all-infected wired field and nu_lambda also disagree there. Such a disagreement is included in the union of a disagreement between the two all-infected time-T fields and a disagreement between the full-lattice all-infected field and nu_lambda.

The second single-site probability is at most C3*exp(-C4*T), by the density bound and monotonicity. For the first disagreement, the differing boundary condition must have affected x during [-T,0]. Following its graphical infection ancestry backwards gives a directed chronological arrow path from outside D to x. Since x is in M, it contains at least L arrows. Recoveries can be ignored for an upper bound.

For a fixed n-step directed spatial walk ending at x, the expected number of chronological tuples of its arrows in an interval of length T is lambda^n*T^n/n!: this is the Poisson factorial-moment identity, integrated over the ordered time simplex. It remains true if an edge is repeated, because distinct event times use the corresponding Poisson factorial moments. There are at most k^n such spatial walks. Markov's inequality followed by a union bound over all lengths n>=L gives the indicated series bound. Sum the single-site discrepancy probabilities over x in M. QED.

For T=a*L, choose a=1/(4*e*k*lambda). Since n! >= (n/e)^n and n>=L, each series term is at most (1/4)^n. Thus

    discrepancy <= |M| * [C3*exp(-C4*a*L) + (4/3)*4^(-L)].

The factorial estimate follows by summing log j >= integral_1^n log x dx = n*log n-n+1, and also holds at n=1. This supplies a fully explicit finite-propagation bound; the only uncomputed constants are the cited fixed-rate temporal-convergence constants.

## Theorem 8: a finite-certificate characterization of the gap in d=2

For the nearest-neighbor contact process on Z^2 in the same per-edge convention, the following are equivalent:

(i) lambda_c < lambda_p.
(ii) There exists a positive integer L with b_L(lambda_c) < 3^(-25).

This is a proved reduction using two known theorems, not a proof that either condition holds. No assertion of novelty is made.

Proof. (ii) implies (i) by Theorem 6. Conversely assume (i). Choose rates lambda_c < lambda_b < lambda_a < lambda_p. The upper invariant law at lambda_a does not percolate, by monotonicity and the definition of lambda_p. Van den Berg's Theorem 1.1, same paper PDF p. 4, gives constants C1,C2>0 such that

    nu_lambda_b(|cluster of x| >= n) <= C1*exp(-C2*n)

for all n>=1 and x. This is exactly the published theorem: it starts from nonpercolation at lambda_a and gives exponential decay at smaller rates. Here that starting rate exists only because the gap is being assumed in this direction of the equivalence.

An occupied path from C to the boundary of M has length at least L, so at least one of the L^2 vertices x of C has occupied-cluster size at least L. Therefore its probability under nu_lambda_b is at most L^2*C1*exp(-C2*L). Apply Lemma 7 at the fixed rate lambda_b and |M|=9L^2 to obtain

    b_L(lambda_b)
      <= L^2*C1*exp(-C2*L)
         + 9L^2*[C3*exp(-C4*a*L) + (4/3)*4^(-L)].

Every term tends to zero. For sufficiently large finite L, b_L(lambda_b)<3^(-25). By monotonicity, b_L(lambda_c)<=b_L(lambda_b), proving (ii). QED.

The buffer is essential to this necessity proof: the crossing event only uses M, separated by distance of order L from the infected exterior of D. Local convergence of wired laws on fixed sets, without this quantitative comparison, would not control the growing crossing event.

No version of Theorem 8 is claimed for all d: the explicit sharpness and temporal-convergence inputs were verified here only in the fetched d=2 paper. The sufficient certificate Theorem 6 is dimension independent.

## Exact small-case obstruction and numerical exploration

At L=1 in d=2, D={-2,-1,0,1,2}^2, C={0}, and M={-1,0,1}^2. Restrict the wired process to the three sites 2e1,e1,0. Retain only a boundary immigration arrow from 3e1 to 2e1 at rate lambda, the directed arrows 2e1 to e1 and e1 to 0 at rate lambda, and all three recovery clocks. Suppress all other births. The restricted stationary process is dominated by the wired one, by graphical attractiveness. If e1 and 0 are simultaneously occupied in it, the wired crossing event occurs.

Its generator on the eight occupancy states is specified and solved symbolically in compute_directed_chain.py. Recovery of each occupied site has rate 1. Site 0 of this chain (the physical site 2e1) has immigration rate lambda, and the other two sites are born at rate lambda if their predecessor is occupied. A positive-probability emptying interval ensures a unique stationary law, and at lambda>0 this chain is irreducible. The exact joint occupancy of its last two sites gives a rigorous lower bound on b_1(lambda). The numerical code computes its rational stationary law at lambda=1/4 and checks all eight stationary equations. The lower bound, together with attractiveness in lambda and lambda_c>=1/4 proved in the first attempt, rules out the buffered L=1 certificate throughout the survival regime once the exact comparison to 3^(-25) is checked below.

compute_wired.py is a separate unbuffered 3-by-3 diagnostic with 512 states. It constructs the exact finite generator but solves it in floating point. Numerical residuals are below 3e-16; this is numerical evidence, not an exact certificate. The stationary crossing probabilities at lambda=1/4 and 0.4 are approximately 0.20489 and 0.39335, respectively.

simulate_buffered.py samples the actual buffered family at L=1,2,4,8 and lambda=0.35,0.4,0.43. It uses exact CTMC uniformization: choose R=|D|*(1+4lambda), draw N~Poisson(R*T), and make N iid update proposals. A proposal chooses a uniform site, recovers it with probability 1/(1+4lambda), otherwise chooses a uniform neighbor and infects the site if that neighbor is occupied or outside D. Null updates remain. This discrete kernel satisfies Q=R*(P-I), so mixing over the Poisson count gives exp(TQ). Thus there is no Euler time-discretization error. It uses NumPy/Numba pseudorandom generators, so the outputs remain numerical experiments.

Each of the 40 replicas starts all infected and is sampled at T=100; no stationary error bound at these parameters is computed. Its distribution stochastically dominates the stationary wired law. At L=8 all 40 samples had no crossing at each of the three rates. This does NOT certify the threshold: even zero out of 40 independent Bernoulli observations gives a one-sided 95-percent upper bound 1-0.05^(1/40), approximately 0.07216, whereas the required probability is 3^(-25), approximately 1.18e-12. About 2.54e12 zero-hit trials would be needed to reach that threshold by this method. No survival claim is made for the sampled rates. In particular no approximate remembered value of lambda_c is used as a rigorous bracket.

A sparse 5-by-5 full-state generator would have 2^25 states and of order 25*2^25 transition entries, exceeding the prescribed 1-GB limit. No such job was launched. Simulated arrays had at most 1600 sites; the largest directly solved generator had 512 states. The simulations completed in seconds after compilation and do not replace the missing probability bound.

## Hostile-referee audit and remaining gap

1. Finite boundary forcing gives an UPPER law, not a lower law. The three-site restricted immigration process is used only for an exact LOWER bound ruling out L=1.
2. Arrow-label independence uses TARGETS for the wired process. The earlier singleton-exit construction used SOURCES instead. Switching the convention without fixing which exterior occupations are deterministic would invalidate the proof.
3. Good coarse sites need not themselves percolate under the actual law; the argument uses only the implication from an actual infinite component to an infinite good-site component.
4. There are 5^d color classes, not a number growing with L. Buffers leave M at distance at least L from the exterior of D.
5. Theorem 8's necessity assumes the gap and uses it to choose lambda_a. It must not be used circularly as an unconditional proof of exponential cluster decay above lambda_c.
6. Temporal-convergence constants are used at one fixed strictly supercritical lambda_b. No uniform limiting estimate as lambda decreases to lambda_c is asserted.
7. The increasing event used in b_L is an instantaneous occupied spatial path, not a space-time infection trajectory.
8. Small Monte Carlo crossing frequencies cannot prove an event probability below 3^(-25). Neither burn-in nor a critical-rate bracket has been certified.
9. The first symbolic residual check compared unsimplified Sympy expressions structurally and failed. It was replaced by factoring every exact rational residual; no zero residual is claimed without that successful check. This is a computational assertion-format correction, not evidence about the original problem.

Precisely remaining: prove, for every d>=2, a finite L and a rate u>=lambda_c(d) with b_L(u)<(2d-1)^(-5^d), or obtain a different sufficient spatial-connectivity estimate. Even in d=2 no such certificate has been established. Theorem 8 identifies the critical buffered crossing condition exactly in that dimension, but leaves its existence undecided. Larger-scale analytic control of these wired spatial crossings is the missing step; small density or a zero-hit sample does not supply it.


## Lemma 9: the certificate is nonvacuous below the branching threshold

If 0<lambda<1/k, put a=k*lambda<1. Then

    b_L(lambda) <= L^d * a^(2L+1)/(1-a).

In particular it passes Theorem 6 for all sufficiently large L. At d=2, lambda=1/8 and L=25, the bound is 625/4^25 < 1/3^25, so this is an explicit rigorously passing subcritical certificate. It is a sanity-check special case, not the target gap.

Proof. For a vertex x in D let r_x be its stationary occupied probability, and let e_x be its number of outside neighbors. Stationarity gives

    r_x = lambda*E[(1-eta_x)*(sum_{y in D,y~x}eta_y+e_x)]
        <= lambda*sum_{y in D,y~x} r_y + lambda*e_x.

Let A be the nonnegative internal adjacency matrix. Its maximum row sum is at most k. Iterating the componentwise inequality yields

    r <= sum_{j=0}^{n-1}(lambda*A)^j*lambda*e + (lambda*A)^n*r.

Since r<=1 and k*lambda<1, the last term is bounded by a^n and vanishes. Each term in the series counts walks that stay inside D until their final exit, weighted by lambda to the walk length. For x in C any exit walk has length at least 2L+1. There are at most k^n length-n walks, so r_x <= sum_{n>=2L+1} a^n = a^(2L+1)/(1-a). The crossing event requires at least one occupied vertex of C. Union over its L^d vertices proves the bound. Since a<1, polynomial L^d times a^(2L+1) tends to zero, establishing eventual passage. At lambda=0 the crossing probability is zero directly. QED.

This estimate ceases to give a finite bound when k*lambda>=1. It supplies no control at the actual survival critical rate and therefore does not complete Theorem 8's condition.

## Exact three-site result saved

At lambda=1/4 the eight stationary probabilities, ordered by binary occupancy states 0 through 7, are

    (394304/507375, 9824/56375, 8464/507375, 2252/101475,
     1696/507375, 76/56375, 1436/507375, 223/101475).

They are positive, sum to one, and satisfy all eight rational generator balance equations. States 6 and 7 have the last two sites occupied, with total probability 2551/507375. This is strictly greater than 1/847288609443 = 3^(-25). Graphical monotonicity extends the lower bound to every lambda>=1/4. Since lambda_c(Z^2)>=1/4, no L=1 buffered certificate can pass at or above lambda_c. This is a proof about L=1 only; it leaves every larger scale undecided.

SecondChecks.lean checks normalization, positivity, all eight generator balance equations, the exact joint probability and its strict threshold comparison, using decide +kernel. The generated equations are checked against the independently constructed Fraction generator in generate_second_lean.py. See second_lean_check.txt for the actual Lean result. This does not formalize the infinite-volume coupling, the sharpness theorem, or the block proof.


## Approach B: an exact split-and-merge stationarity identity

Proposition 10. For a finite vertex set F, let K_F(eta) be the number of occupied connected components in its induced graph. For a healthy x in F, let a_x be the number of distinct occupied components of F containing a neighbor of x inside F. For an occupied x in F, let s_x be the number of distinct components of eta restricted to F with x deleted that contain a neighbor of x. Let N_x be the number of occupied neighbors of x in the FULL lattice, including those outside F. Then any stationary contact-process law satisfies

    sum_{x in F} E[lambda*(1-eta_x)*N_x*(1-a_x)
                      + eta_x*(s_x-1)] = 0.

Proof. A birth at x merges its a_x neighboring components and the new vertex into a single component, so its change to K_F is 1-a_x. A death at x removes the old component containing x and replaces it by exactly s_x components. Indeed each surviving component of the old component contains a neighbor of x: follow an old occupied path from a vertex of that component to x, stopping at the vertex before x. All components not containing x are unchanged. Thus the death change is s_x-1, including the isolated case s_x=0. The generator changes K_F only at the finitely many sites x in F, with birth rate lambda*(1-eta_x)*N_x and death rate eta_x. K_F is a bounded cylinder function and its generator is bounded. Stationarity sets its expected generator to zero, proving the formula. QED.

This confirms the dynamic route's obstacle precisely: a_x and s_x are connectivity and articulation quantities, not functions of density or adjacent pair probabilities. Dividing by |F| and sending F to the full lattice requires controlling components that connect around the finite box boundary. No sign inequality on these split-and-merge terms has been proved that would exclude an infinite occupied component near lambda_c. The identity is valid but does not close the gap.


Final verification: SecondChecks.lean passed all five theorems, Lean 4.33.1 exit 0 in 169.162 seconds. The human probabilistic proofs are not Lean formalizations. Exact rational, finite-generator numerical and Monte Carlo results have distinct statuses in CLAIMS.jsonl.
