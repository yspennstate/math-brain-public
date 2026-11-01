# Attempt C0059 -- 2026-10-12

## Target and result

For every weight sequence q of type a in [2,5/2) in Curien's preliminary notes, prove or disprove almost-sure transience of simple random walk on m-dagger under P_infinity^(1). At a=2 the source restricts q to (5.12); this restriction is retained. Parallel edges have their usual multiplicity, loops do not aid escape, and electrical edges have unit conductance.

**Not solved.** What is proved below is almost-sure nonexplosion of exponential first-passage percolation on these duals, the asymptotic expectation of the peeling clock, an exact boundary-case calculation, and a deterministic resistance reduction. None proves recurrence or transience of SRW in the requested family. The nonexplosion result is a consequence of the source's scaling and peeling-clock theorems, rather than a claim of a new published theorem.

## 1. Source inputs used

Write P_n for the half-perimeter of the active hole in uniform filled-in peeling, starting at P_0=1. The source gives:

1. P_n has the law of S_n^up, the positive h-transform of the nu random walk (Section 4.2).
2. n^(-1/(a-1)) P_n converges in distribution to Y=Upsilon_a^up(p_q), with 0<Y<infinity almost surely (Proposition 26, PDF pp. 60-61).
3. Conditional on the entire perimeter/volume process, the uniform FPP clock has law T_n=sum_{i=0}^{n-1} E_i/(2P_i), where E_i are independent rate-one exponential variables (Proposition 33 and proof of Proposition 34, PDF pp. 82-84). This conditional representation is essential; no independence of P_n over time is assumed.
4. Corollary 27 gives exhaustion of the map. The clock is the filled FPP exploration clock; a finite accumulation time corresponds to finite FPP distance to infinity, as used in Proposition 36.
5. Lemma 35 gives E[1/P_n]=2 sum_{k>n} P_1(S_k=0)/k. The local limit theorem (5.15) gives P_1(S_k=0)~C_0 k^(-1/(a-1)), C_0>0.

These are cited source theorems, not independently proved Boltzmann scaling limits. All deductions from them are supplied below.

## 2. Almost-sure nonexplosion throughout [2,5/2)

### Lemma 2.1 (dependence-free divergence)

If X_n>=0 and X_n converges in distribution to a finite random variable X>0 almost surely, then sum_{n>=1} X_n/n=infinity almost surely. No temporal independence is needed.

Proof. If the series is finite on a positive-probability event, then for some finite M the event A={sum X_n/n<=M} has probability epsilon>0. Choose a continuity point delta>0 of the law of X such that P(X<delta)<epsilon/4; such delta exist because P(X<=0)=0 and a distribution has at most countably many atoms. Distributional convergence gives P(X_n<delta)<epsilon/2 for all large n. Therefore

E[1_A X_n]>=delta P(A intersect {X_n>=delta})>=delta(epsilon-P(X_n<delta))>=delta epsilon/2.

For each N, Tonelli and the defining bound on A give sum_{n=1}^N E[1_A X_n]/n=E[1_A sum_{n=1}^N X_n/n]<=M P(A)<=M. The lower bound makes these partial sums diverge harmonically, contradiction. QED.

### Lemma 2.2 (weighted exponential series)

For deterministic 0<w_n<=1/2 and independent Exp(1) variables E_n, sum w_n E_n is finite almost surely exactly when sum w_n is finite.

Proof. When sum w_n<infinity, Tonelli gives finite expected series and hence almost-sure finiteness. Otherwise, for Z_N=sum_{n=0}^{N-1}w_n E_n, independence and the exponential Laplace transform give E[exp(-Z_N)]=product_{n<N}(1+w_n)^(-1). Since log(1+w)>=w/(1+w)>=2w/3 on [0,1/2], the product tends to zero. By bounded convergence, with exp(-infinity)=0, E[exp(-Z_infinity)]=0. A nonnegative random variable with expectation zero is zero almost surely, hence Z_infinity=infinity almost surely. QED.

### Proposition 2.3

Under P_infinity^(1)(dm) Q_m^fpp, for all source types a in [2,5/2), T_infinity=infinity almost surely. Consequently no infinite path from the dual root has finite total exponential FPP length, almost surely.

Proof. Put X_n=(n^(1/(a-1))/P_n)^(a-1)=n/P_n^(a-1). Input 2 and the continuous mapping theorem give X_n => Y^(-(a-1)), a strictly positive finite limit. Lemma 2.1 gives sum_n P_n^(-(a-1))=infinity almost surely. Since P_n>=1 and a-1>=1, P_n^(-1)>=P_n^(-(a-1)), so sum_n 1/(2P_n)=infinity. Conditional on every perimeter sequence in this probability-one event, Lemma 2.2 and input 3 give T_infinity=infinity. Integrating the conditional probability proves the assertion.

For the path interpretation, use the source's FPP-clock identification in inputs 3-4. Equivalently, any finite-length infinite path supplies infinitely many discovered faces before that length; filling finite holes cannot swallow its entire tail in a finite step. This would force infinitely many peeling steps before a finite clock time. This contradicts T_infinity=infinity. Every vertex has finite degree and each filled region is finite, so no hidden infinite discovery occurs in a single step. QED.

This proof explicitly covers the source's special a=2 sequence. The mean-clock argument alone would not suffice: infinite expectation is compatible with almost-sure finiteness. Lemmas 2.1-2.2 close that possible failure.

## 3. Annealed clock asymptotics

Let beta=1/(a-1). From input 5 and the integral test,

E[1/P_n] ~ (2C_0/beta) n^(-beta).

Indeed for each epsilon>0, for all sufficiently large k the return probability lies between (C_0-epsilon)k^(-beta) and (C_0+epsilon)k^(-beta). The bounds on the tail sum sum_{k>n} k^(-beta-1) are asymptotic to n^(-beta)/beta. Let epsilon tend to zero.

Taking expectations in the conditional clock representation gives E[T_N]=(1/2)sum_{n=0}^{N-1}E[1/P_n]. Thus

- a=2: E[T_N]~C_0 log N.
- 2<a<5/2: E[T_N]~[C_0/(1-beta)beta] N^(1-beta) = C_0 (a-1)^2/(a-2) N^((a-2)/(a-1)).

Both statements follow by the same epsilon sandwich and integral comparison, treating finitely many initial terms as a constant. This proves an annealed growth estimate, not concentration, a quenched rate or electrical recurrence.

## 4. Exact a=2 step law and its return constant

At the boundary, nu(0)=0 and nu(k)=1/(4k^2-1) for all nonzero integers k. For positive k,

1/(4k^2-1) = (1/2)[1/(2k-1)-1/(2k+1)].

Telescoping gives sum_{k=1}^N nu(k)=N/(2N+1). The infinite positive mass is 1/2; symmetry makes total mass 1. The displayed finite identity is the Lean verification target in Type2Check.lean; its final outcome is recorded in lean_check.log and the final checks below.

The characteristic function is

phi(t)=1-(pi/2)|sin(t/2)|, for -pi<=t<=pi.

Proof. The even continuous 2pi-periodic function g(t)=|sin(t/2)| has constant Fourier coefficient 2/pi. For k>=1 its cosine coefficient is

(2/pi) integral_0^pi sin(t/2)cos(kt) dt = -4/[pi(4k^2-1)],

by the product-to-sum formula and elementary integration. These coefficients are absolutely summable. Their Fourier series converges uniformly and equals g (uniqueness of Fourier coefficients for continuous functions, or the standard Dirichlet convergence theorem applied to this piecewise smooth function). Multiplying by -pi/2 and adding 1 gives 2 sum_{k>=1}cos(kt)/(4k^2-1), which is exactly the characteristic function of nu.

Fourier inversion for the walk starting at 1 yields p_n=P_1(S_n=0)=(1/pi) integral_0^pi cos(t)phi(t)^n dt. Let c=pi/4. At zero phi(t)=1-ct+O(t^3). Choose delta>0 small enough that on [0,delta], phi(t)>=0 and phi(t)<=exp(-c t/2). On [delta,pi], the absolute value of phi is bounded by a number rho<1: phi decreases from 1 to 1-pi/2, whose absolute value is <1. Therefore the contribution outside [0,delta] is O(rho^n). On the remaining interval substitute u=nt. For each fixed u, cos(u/n)phi(u/n)^n tends to exp(-cu), and its absolute value is bounded by exp(-cu/2) after extending it as zero beyond n delta. Dominated convergence gives

n p_n -> (1/pi) integral_0^infinity exp(-cu) du = 4/pi^2.

So the boundary constant is exactly C_0=4/pi^2, and E[T_N]~(4/pi^2)log N. This agrees with the broader Cauchy-map clock results in the literature. Numerical integration tests this calculation, not SRW on the random maps.

## 5. Why nonexplosion does not answer C0059

Even the ordinary rooted binary tree is transient but has nonexplosive exponential FPP. Its degree is at most 3. There are 2^n paths of length n from the root, each with Gamma(n,1) FPP length. The Gamma density gives P(Gamma(n,1)<=t)<=t^n/n!, so a union bound gives P(exists depth-n path of length<=t)<=2^n t^n/n! -> 0. A finite-length infinite path would give such a depth-n path for every n. Hence no such infinite path exists at any fixed t, almost surely; take a countable union over integer t. Nevertheless, split a unit current equally at each branch. On level n>=1 there are 2^n edges of current 2^(-n); the energy is sum_{n>=1}2^n 2^(-2n)=1. The standard finite-energy-flow criterion proves transience.

Thus Proposition 2.3 rules out the literal finite-FPP-length method of Corollary 38 but cannot rule out a different finite-energy flow. Polynomial volume exponents and recurrence at excluded a=5/2 also do not answer the question; the earlier w342 record gives explicit volume-growth counterexamples.

## 6. A precise remaining resistance reduction

Here is a deterministic sufficient condition that isolates the missing routing control. Let G be an infinite connected locally finite graph and let A_0 subset A_1 subset ... be finite connected vertex sets exhausting G, with A_0={o}. Consider each edge crossing from A_j to its complement as an individual port. Let mu_j be a nonnegative probability distribution on those ports. Suppose we can route mu_j to mu_{j+1} through the finite intervening layer with conserved current at every interior vertex, and route the unit source at o to mu_0. Use split boundary edges (half-resistance on each side) to allocate edges to disjoint layers. Suppose the sum of the energies of these layer flows, including the initial layer, is finite.

Then G is transient. Proof: glue the currents on matching port half-edges, where the assigned mu_j agrees. Current is conserved at every non-root vertex: its incident edges are all present in finitely many layers, and all artificial interface divergences cancel. The root has divergence 1. Every original edge has the same current on its two halves; their energies add to its unit-resistance energy. The total flow therefore has finite energy equal to the sum of the layer energies. The finite-energy-flow criterion applies. QED. Edges spanning more than one layer can be subdivided at the interfaces with total resistance preserved. For a ball exhaustion they span at most one layer; only finitely many ports occur on any fixed interface.

This cannot be replaced by summability of inverse boundary sizes: uniform current on each new boundary need not agree with the currents produced by the preceding layer. Wiring an entire boundary together would permit free lateral transfer and reduce resistance, so a finite resistance of the wired comparison gives a lower bound and cannot prove transience of the original graph.

For C0059 one could take dual graph-distance balls (or a finite-hull exhaustion and its ports). The unresolved step is to construct compatible mu_j and layer flows under the actual Boltzmann law, almost surely, with summable energy. No bound on those routing energies has been proved here. In particular P_n's scaling only controls the number of frontier ports; it does not control how current reaches or leaves them. The tempting heuristic sum_n P_n^(-2)<infinity is not an upper bound on electrical energy, because it ignores routing and current conservation.

### An alternative precise path-overlap target

Let Q_m be a probability law on infinite simple paths from the dual root, with all extra randomness conditional on a fixed map m. If Gamma and Gamma' are **independent under Q_m**, then

E_{Q_m x Q_m}[number of unoriented edges common to Gamma and Gamma'] = sum_e Q_m(e in Gamma)^2,

by Tonelli and independence. If this sum is finite, the map is transient. Proof: fix an orientation on each edge and put theta(e)=Q_m(path uses e forward)-Q_m(path uses e backward). Simplicity of the paths gives divergence 1 at the root and 0 at every other vertex for each sampled path. Taking expectations preserves this identity because each vertex has finite degree. Moreover |theta(e)|<=Q_m(e in Gamma), so its energy sum_e theta(e)^2 is at most the finite overlap expectation. Thus it is a finite-energy unit flow and the standard criterion applies. All sums count parallel edges individually. QED.

The missing probabilistic estimate could therefore be stated as: construct Q_m for which this overlap expectation is finite for almost every m under P_infinity^(1), for every source type in the question. No such estimate is established here.

The recent Kammerer paper arXiv:2412.02666v3 supplies a scaling limit of finite-map FPP geodesic trees (Theorem 1.5), and infinite-map one-path length estimates (Theorem 1.1). It is a relevant lead for studying routing. However, paths to different endpoints in one shared FPP metric are dependent even conditional on the map. Their coalescence probabilities are not Q_m(e in Gamma)^2, which requires independently resampling the path randomness. Also a finite-map scaling limit by itself provides neither infinite simple-path laws nor a uniform integrable bound on shared edges. The one-path length estimates supply no overlap control. Those are additional unresolved requirements, not consequences claimed from that paper.

## 7. Referee audit

- Exact source model and type-2 restriction: verified from PDF, not inherited from brain summary.
- Endpoint inference: rejected; a=5/2 is outside the quantifier.
- Primal/dual recurrence confusion: primal exponential root-degree tail is not a uniform degree bound and says nothing automatic about the dual tail.
- Dependence in perimeter sequence: Lemma 2.1 uses only marginal convergence, no false independent-event argument.
- Infinite mean versus almost-sure divergence: handled separately by the dependence-free lemma and the conditional Laplace product.
- Conditional independence of clock increments: cited precisely from the source's clock representation.
- Fourier aperiodicity: phi has |phi|<1 away from zero, including at pi; negative phi on part of the interval is exponentially negligible, not silently discarded.
- Flow direction and bounds: a resistance lower bound, collapsed boundary or volume exponent cannot supply an upper bound for the original map.
- Boundary computation is about the perimeter walk, not simulation of dual SRW. No finite-map recurrence experiment is claimed to decide transience.
- Formalization scope: the finite rational normalization identity only; not the infinite probability or electrical arguments.

## 8. Checks completed

- `check_type2.py` (Python 3.14, NumPy/SciPy) completed successfully; output is `numerical_checks.json`. Exact rational partial-mass checks were made at N=0,1,2,10,100,1000. Seven characteristic-function checks used 10,000 Fourier terms and the explicit remainder bound 1/(20001), allowing 1e-12 floating-point roundoff. Nine return-integral calculations used u=nt to resolve the peak, explicit omitted-tail bounds, and numerical quadrature tolerances 1e-11. At n=3000, n p_n=0.40514963003189974, compared with 4/pi^2=0.4052847345693511. Numerical quadrature error estimates are not interval certificates; the analytical proof supplies the result.
- `Type2Check.lean` proves the finite partial-mass identity for every natural N over the rationals. Run from `~/lean_verify` using `lake env lean ~/brain_workers/TRIO_1011/op/C0059/Type2Check.lean`, with a 3600-second timeout. Final exit code 0; transcript in `lean_check.log`. No sorry, native_decide or extra axioms were used. Initial encoding/BOM failures were corrected before the successful check. Only narrow Mathlib modules were imported. This verifies only the finite algebraic identity.
- No random-map simulator was used: simulation of an unrelated finite graph would not provide evidence for the required infinite Boltzmann law.

## Remaining gap

For every source type a in [2,5/2), establish almost-sure finite effective resistance from the dual root to infinity (or find an admissible sequence for which it is infinite). None of the results above settles even the source's explicit a=2 case. The current stopping verdict is PARTIAL, not SOLVED.


## Second attempt: two new approaches (2026-10-12)

A. Exact star-mesh elimination of dual face centers after edge subdivision. This turns the unbounded-degree dual into a bounded-total-conductance long-range network on primal edge midpoints. Pursue exact energy-preserving flow lifting and compare its face cliques with a recurrent medial graph. A possible neighbouring theorem is transience of long-range percolation on Z^2; applying it would require a genuine stochastic domination or multiscale conductance estimate. This approach has not been attempted above.

B. Transfer primal planarity/conformal recurrence through a face filling with controlled resistance distortion: triangulate each large face using a bounded-degree disk and use circle-packing or planar-limit recurrence theorems to seek a counterexample. The key issue is the cost of replacing a high-degree star; compute whether bounded-degree fillings can retain its terminal resistances uniformly. This could rule out a naive transfer or identify a restricted recurrent family. This approach has not been attempted above.

Choice: pursue A, which has an exact network identity and a constructive current lift. Approach B needs a uniform face-filling comparison that is suspect for large degrees. All auxiliary-network results will be distinguished from facts about the Boltzmann law.

### Results of the second attempt

Complete proofs and the new remaining gap are in [SECOND_ATTEMPT.md](SECOND_ATTEMPT.md). The exact trace has vertex set given by primal edge midpoints and conductance C(e,e')=sum_f 2m_fe m_fe'/d_f for distinct e,e'. It preserves recurrence/transience and admits explicit energy-nonincreasing current lifting; its total conductance at any vertex is at most four. The planar medial graph beneath it is recurrent by the source's finite local limit and Benjamini-Schramm. However, clique-to-face-cycle energy distortion is sharply 1/[2sin^2(pi/d)], growing as d^2. Berger's independent long-range transience and iid-conductance recurrence theorems do not apply to these dependent face cliques. This attempt does not establish even one requested value of a. The verdict remains PARTIAL.

Further source-law progress in the second attempt: conditional on every finite active perimeter, the newly discovered degree D has E[D^p|past]<infinity exactly for 0<p<a-3/2; in particular its conditional first moment is infinite for every requested a. Arbitrarily large degrees occur infinitely often almost surely, by a conditional avoidance bound. Neither fact is asserted to decide transience. The general finite star-mesh identity passed Lean kernel verification (StarMeshCheck.lean; star_mesh_lean.log). New full proofs and the exact transformed-network gap are in SECOND_ATTEMPT.md, Sections 1-7.
