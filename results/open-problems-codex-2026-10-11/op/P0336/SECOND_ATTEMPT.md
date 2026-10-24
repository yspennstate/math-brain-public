# Second serious attempt, 2026-10-12

## Gap being attacked
Identify the horizontal conditional kernel selected by the actual iid empirical Euclidean assignment. Weak vertical concentration and the common-slope local energy do not select it.

## Two approaches not pursued in the previous attempt

A. Use the geometry of noncrossing optimal straight segments across the empty horizontal gap. A single segment with appreciable slope sweeps out a vertical interval that other nearly horizontal edges cannot cross. Uniform empirical occupancy should then force a quantitative maximum-displacement bound, stronger than the existing average bound. Use this to rigorously replace the Euclidean excess by the perspective quadratic action h^2/(2d), with a vanishing error on the actual optimizer, and derive the corresponding Hamilton–Jacobi dual constraint. This targets a new reduction of the original finite optimization, not an assumed local expansion.

B. Test a sampling/entropy universality hypothesis through the Gibbs law on permutations. For fixed sample size, inverse temperature tending to infinity selects the empirical optimizer. Taking sample size to infinity first at fixed temperature instead leads to an entropy-penalized population coupling. In the low-temperature horizontal-ray geometry, A formal Gaussian tube calculation suggests a reference weight proportional to sqrt(d); identifying the constrained limiting kernel and proving that it describes sampling would be additional steps. Analyze whether the two limits commute and compare the resulting bistochastic horizontal kernel with fresh assignment data. Neither commutation nor equality of empirical and entropy selection is known; concentration of the Gibbs law at a unique finite optimizer is not a justification for interchanging limits.

Choice: pursue A. Its first steps follow from deterministic optimality and empirical occupancy, and can be verified without a universality assumption. B remains a separate untried route; entropic selection theorems from the first literature check concern the other order of limits.

## Brain recall
2026-10-12: math_recall.py queried "Euclidean empirical transport horizontal kernel selection noncrossing transport rays microscopic matching". Returned the existing vertical-support attempt and mostly irrelevant cards, no selection theorem. A second query uses the named neighboring concepts Hamilton–Jacobi, Burgers, Benamou–Brenier and perspective quadratic cost. All brain material is a hint only.
## New deterministic reduction: the swept-interval estimate

### Proposition 8: optimal edges do not cross transversely in the empty strip
For finite source points (a_i,s_i) with a_i∈[0,1], and target points (b_j,t_j) with b_j∈[2,3], take a coupling minimizing either Euclidean distance or q(d,h)=h^2/(2d). Assume no three distinct sample points are collinear and no two sample points coincide. Then two edges in the support of an optimal coupling cannot intersect at horizontal coordinate x∈(1,2).

Proof for Euclidean distance: suppose segments X_iY_j and X_kY_l meet at P in the strip. Their source and target indices are distinct: edges sharing a source/target cannot meet again unless their supporting lines are identical, forbidden by general position. Triangle inequalities give |X_i-Y_l|≤|X_i-P|+|P-Y_l| and |X_k-Y_j|≤|X_k-P|+|P-Y_j|. The sum of their right sides equals the original total edge lengths. Since the two intersecting lines are distinct, at least one (indeed both) inequalities is strict. Reduce the mass on each old edge by a common δ>0 and increase each swapped edge by δ. Marginals are unchanged and total cost strictly decreases, a contradiction. This argument covers fractional plans as well as permutations.

Proof for q: if d_1,d_2>0, then
 q(d_1,h_1)+q(d_2,h_2)-q(d_1+d_2,h_1+h_2)
 =(d_2 h_1-d_1 h_2)^2/[2 d_1 d_2(d_1+d_2)] ≥0,
with strict inequality unless h_1/d_1=h_2/d_2. Splitting an old straight edge at P preserves its q-cost exactly, because both pieces have the same slope. Recombining a source-to-P piece with the other P-to-target piece yields the swapped straight edge with strictly smaller q-cost when the lines are distinct. All these horizontal increments are positive since P is in (1,2). The same mass swap contradicts optimality.

For the iid continuous samples, the general-position assumption holds almost surely simultaneously for all n: condition on any two distinct points and the third has probability zero of lying on their line; the supports have densities. A countable union over triples and pairs completes this justification. No assertion about a unique optimal permutation is required.

### Proposition 9: uniform displacement control from source occupancy
For any finite coupling with no transverse crossings in (1,2), let D_n=sup_{z∈[0,1]}|F^s_n(z)-z| for the source vertical empirical cdf, and M=integral h^2 d pi. For every supported edge with displacement h and d=b-a, put w=|h|/d. Then
 M ≥ (w^2/16) (w/2-2 D_n)_+,
and consequently the maximum supported displacement H satisfies
 H ≤ max(24 D_n, 12 M^(1/3)).

Proof: the edge height at horizontal x is z(x)=s+h(x-a)/d. Its heights at x=1 and x=2 differ in absolute value by w. Both heights belong to [0,1] because these x-values lie between the endpoints. Let z_lo,z_hi be their min/max. The open interval J=(z_lo+w/4,z_hi-w/4) has length w/2 when w>0. Consider any source point with source height s'∈J and any supported edge from it. If that edge has |h'|≤w/4, then its heights at x=1 and x=2 differ from s' by at most |h'|, since the linear interpolation fraction lies in [0,1]. Both heights thus lie strictly between z_lo and z_hi. At the two ends of the strip its ordering with the original edge is reversed, so their continuous affine heights agree at an interior x∈(1,2). The lines have different slopes, because the original edge changes by w while the competing edge's strip change is at most |h'|≤w/4. Hence this is a forbidden transverse crossing. The original edge's own source height is not in J: it is at or below z_lo for positive slope and at or above z_hi for negative slope. Therefore every edge from every source height in J has |h'|>w/4.

The empirical source mass of J is F^s_n(right-)-F^s_n(left), at least length(J)-2 D_n. The cdf bound also holds for its left limits, by taking limits from below against the continuous uniform cdf. It remains valid when J's endpoints depend on the sample. For each source in J all its transported mass has h'^2>w^2/16. Hence M≥(w^2/16)(w/2-2D_n)_+. This proves the first assertion for fractional or integral plans.

If w≥8 D_n, then w/2-2D_n≥w/4 and M≥w^3/64, giving w≤4M^(1/3). Otherwise w<8D_n. Thus every edge has w≤max(8D_n,4M^(1/3)); multiplying by d≤3 proves the H bound. The w=0 case is immediate. No assumed independence of an optimal edge and the empirical cdf was used.

### Corollary 10: every empirical optimizer stays uniformly near equal heights
For the original Euclidean optimizer, M_e≤C S_n/2 from the first attempt. For a q-optimizer, q≥h^2/6 and the rank competitor has q≤S_n/2, so M_q≤3 S_n. Therefore both optimizers satisfy H→0 almost surely, and H=O_P(n^(-1/3)). Proof: D_n→0 a.s. by Glivenko–Cantelli and S_n→0 a.s. as already proved. For the rate, D_n=O_P(n^(-1/2)) by the Dvoretzky–Kiefer–Wolfowitz inequality, and S_n=O_P(1/n) by its exact expectation and Markov's inequality. Substitute these into Proposition 9. The exceptional general-position event has probability zero for all n.

### Corollary 11: the two optimal objective values agree through leading fluctuation order
Let Q_n be the minimum of the empirical q-cost, and E_n the minimum Euclidean excess. Then
 0≤Q_n-E_n≤H_e^2 M_e/8=O_P(n^(-5/3)),
so n(Q_n-E_n)→0 in probability.

Proof: e≤q pointwise implies E_n≤Q_n. Evaluating q at the Euclidean optimizer gives Q_n≤q(pi_e). The exact quartic bound from Proposition 6 yields q(pi_e)-E_n≤integral h^4/8 d pi_e≤H_e^2 M_e/8. Corollary 10 and M_e=O_P(1/n) give the displayed order. In addition, pi_e is an O_P(n^(-5/3))-approximate minimizer for q, and a q-optimizer is an O_P(n^(-5/3))-approximate minimizer for Euclidean excess, since E_n≤e(pi_q)≤Q_n. This proves objective equivalence, not convergence of their plans to the same selected kernel.
## Further pursuit: exact Hamilton–Jacobi / Hopf–Lax representation

### Proposition 12: the perspective action admits an exact dynamic-programming reduction
Take any finite quadratic-cost dual optimum f_i, beta_j satisfying f_i+beta_j≤q(b_j-a_i,t_j-s_i), with equality on every supported edge. Such a dual exists by finite linear-programming duality. For x<2 define
 phi(x,z)=min_j [(t_j-z)^2/(2(b_j-x))-beta_j].
Then f_i=phi(a_i,s_i) for every positive-mass source atom: feasibility gives f_i≤phi, and an equality edge gives the opposite inequality. A supported match i→j is a minimizing branch at (a_i,s_i).

For x<x'<2, the following exact semigroup identity holds:
 phi(x,z)=inf_{v∈R} [(v-z)^2/(2(x'-x))+phi(x',v)].
Proof: put A=x'-x>0 and B=b_j-x'>0. The algebraic identity in Proposition 8 gives, for each j,
 (v-z)^2/(2A)+(t_j-v)^2/(2B)
 ≥(t_j-z)^2/(2(A+B)),
with equality at v=(B z+A t_j)/(A+B). Therefore the infimum over v of the jth branch equals its direct action. Infimum over v and a finite minimum over j commute: both equal the infimum over all pairs (v,j). Subtract beta_j to obtain the displayed identity. No limiting stochastic argument is hidden in it.

Where a single branch is minimizing, phi is differentiable and
 phi_x=(t_j-z)^2/[2(b_j-x)^2],
 phi_z=-(t_j-z)/(b_j-x),
so phi_x=(phi_z)^2/2. If multiple branches minimize, differentiability and uniqueness of their slopes are not asserted. The exact semigroup identity is sufficient; no unverified viscosity-solution regularity theorem is used. Thus the new q-problem can be viewed as a backward Hamilton–Jacobi envelope with random terminal points at different horizontal times and sample-dependent dual offsets beta_j.

What this does and does not give: the assignment is encoded by which terminal branch minimizes at each source point. The offsets are determined by the target marginal constraints of the finite assignment problem. A limiting PDE for a scalar macroscopic slope cannot alone identify the horizontal destinations: when phi_z→0, every same-height target has the same limiting slope. A selection theorem requires control of branch competitions and the offsets at the microscopic scale, or a quantitative stability theorem that makes these competitions irrelevant for the weak plan. Neither follows from the semigroup identity or the o(1/n) objective comparison.

## Checks made while developing the reduction
second_experiment.py, seed 3336, ran 20 fresh pairs: 10 at n=200, 6 at n=1000, 4 at n=3000; 40 assignment problems because both costs were solved. It checked ordering of all optimal segments at x=1 and x=2, the swept-interval lower bound for every edge, the derived maximum bound, and the optimal-value remainder inequality. All passed. The run took 20.95 seconds and used at most three 3000×3000 matrices, below 1 GB. Results were saved after every repetition in second_numerics.json.

All 20 cases gave the same permutation for q and Euclidean excess. This is numerical evidence of closeness for these instances, not a theorem. To challenge it, second_counterexample_search.py generated 100,000 two-point configurations (seed 4336) and found opposite signs of the two assignment differences in its first batch. rationalize_second.py seeks a rational version and proves the signs by exact Fraction arithmetic and integer square-root enclosures. The rational certificate, once found, is second_exact_counterexample.json. Thus a blanket claim that the two finite assignment problems have identical optimizers is being explicitly tested, not assumed.
## The exact rational Euclidean-versus-q counterexample

The two source points are (859/1000,67/500) and (1871/2000,293/2000); the two target points are (2737/1000,187/1250) and (4719/2000,611/1000). All coordinates lie in the interiors of the correct sampling rectangles. Let diagonal mean i→i and off-diagonal mean i→3-i. The unnormalized q-cost difference, diagonal minus off-diagonal, is
 2807182184843/963861381667200000 >0.
Hence q strictly chooses off-diagonal.

The squared Euclidean distances, in order (11,22,12,21), are
 11022273/3125000, 1794829/800000,
 9916117/4000000, 162270593/50000000.
Exact square-root enclosures with scale 10^9 are respectively
 (1878064791,1878064792)/10^9,
 (1497843867,1497843868)/10^9,
 (1574493331,1574493332)/10^9,
 (1801502667,1801502668)/10^9.
Each lower square is below the exact rational squared distance and each upper square above it, verified by integer arithmetic. The diagonal cost is less than 3.375908660 and the off-diagonal cost greater than 3.375995998. Thus Euclidean distance strictly chooses diagonal. The horizontal baseline is the same for the two assignments, so subtracting it does not change this preference. Both strict preferences persist on an open neighborhood, giving positive probability under the actual n=2 iid sampling model. This counterexample does not refute equality of asymptotic weak limits; it rules out exact finite optimizer identification.

## Pursuing the neighboring dynamic formulation

### Proposition 13: exact one-dimensional kinetic-action problem with births and deaths
For each permutation sigma, let z_i be an absolutely continuous vertical trajectory on horizontal-time interval [a_i,b_sigma(i)], with z_i(a_i)=s_i, z_i(b_sigma(i))=t_sigma(i). Assign infinite action if its derivative is not square-integrable. Then
 Q_n=min_sigma inf_{z_i} (1/(2n)) sum_i integral_[a_i,b_sigma(i)] |z_i'(x)|^2 dx.

Proof: by the fundamental theorem for absolutely continuous functions and Cauchy–Schwarz,
 (t_sigma(i)-s_i)^2 = (integral z_i')^2
 ≤(b_sigma(i)-a_i) integral |z_i'|^2.
Thus the action of each path is at least q(d_i,h_i)/n. Equality holds for the affine path of constant slope h_i/d_i. Minimizing over all permutations gives the finite assignment minimum; fractional plans give the same value by Birkhoff's theorem. This proves the exact reduction. The optimal paths are affine, and Proposition 8 shows they cannot cross transversely in the gap.

For an optimal permutation define the occupation measure tau_n on [0,3]×[0,1] by
 integral psi d tau_n = (1/n) sum_i integral_[a_i,b_sigma(i)] psi(x,z_i(x)) dx,
and the signed flux J_n by replacing psi with z_i'(x)psi in that expression. For C^1 test functions, direct integration along each path yields
 integral (psi_x d tau_n + psi_z d J_n)
 =(1/n)sum_j psi(b_j,t_j)-(1/n)sum_i psi(a_i,s_i).
Equivalently, in distributions, partial_x tau_n + partial_z J_n equals the birth measure minus the death measure. On x∈(1,2), all n particles are alive. This exact identity is a direct finite calculation; no superposition theorem for arbitrary measure-valued flows is being assumed.

### Proposition 14: the macroscopic dynamic limit discards the selected endpoint kernel
For either optimal permutation (Euclidean or q), almost surely
 tau_n converges weakly to r(x) dx dz,
 J_n converges to zero in total variation,
where r(x)=x for 0≤x≤1, r(x)=1 for 1≤x≤2, and r(x)=3-x for 2≤x≤3. These limits do not require a limit of the endpoint plan and are identical for every possible horizontal population kernel.

Proof: write H_n for maximum endpoint height displacement and M_n for its mean square. We proved H_n→0 and M_n→0 almost surely. Along an affine path, |z_i(x)-s_i|≤H_n and |z_i(x)-t_sigma(i)|≤H_n. For a continuous test psi, uniformly continuous on the compact rectangle, split its path integral into [a_i,1], [1,2], and [2,b_sigma(i)]. Replace the vertical coordinate by s_i on the first two intervals, and by t_sigma(i) on the last. The sum of the replacement errors, divided by n, is at most 3 omega_psi(H_n), tending to zero, since every path length d_i≤3.

After this replacement the first piece is an average of the continuous function (a,s)↦integral_a^1 psi(x,s)dx under the source empirical measure; the middle piece is the source vertical empirical average of integral_1^2 psi(x,s)dx; the last piece is an average of the continuous function (b,t)↦integral_2^b psi(x,t)dx under the target empirical measure. Empirical weak convergence gives their limits. Fubini's theorem gives the first limit as integral_0^1 integral_0^1 x psi(x,z) dz dx, the middle as integral_1^2 integral_0^1 psi(x,z) dz dx, and the last as integral_2^3 integral_0^1 (3-x)psi(x,z) dz dx. Applying the argument first to a countable dense family and then using bounded total mass proves simultaneous weak convergence.

The flux total variation is at most (1/n)sum_i integral |z_i'| dx = (1/n)sum_i |h_i| ≤sqrt(M_n), by Cauchy–Schwarz; it tends to zero. Finally, for any population optimizer all paths have constant height. The same three-way decomposition uses only the fixed marginal laws, yielding exactly r(x)dx dz and zero flux for every K_z. Thus even a uniquely identified macroscopic occupation/flux limit cannot distinguish the endpoint coupling. This identifies precisely why an unscaled hydrodynamic or Hamilton–Jacobi limit would still fail to close P0336.

The potentially useful remaining part of this route is microscopic branch competition, including the random dual offsets beta_j, or a quantitative stability estimate for endpoint labels. A scalar limiting velocity or the universal occupation measure is insufficient. No such microscopic theorem is proved in this attempt.
## Hostile-referee audit of the second attempt

1. Crossing is excluded by a cost-reducing two-edge swap, not by an assumed Monge ordering in source heights. A source's horizontal birth time can vary; height sorting is not used.
2. The crossing point must be inside the EMPTY horizontal strip. This ensures both sources precede it and both targets follow it, so the positive-horizontal-increment splitting identity applies to q. No q triangle inequality with negative time increments is claimed.
3. The swept interval uses the edge's strip displacement w=|h|/d, not its total displacement |h|. Source-to-strip interpolation changes height by at most |h'| because 1 and 2 lie between every pair of horizontal endpoints.
4. The candidate competing source cannot be the source of the swept edge; its own source height lies outside J. Two different supported edges sharing an endpoint cannot cross transversely under general position.
5. For fractional couplings, every edge leaving a source in J must have large displacement, so its FULL source mass contributes to the lower bound. No assumption that pi is a permutation is needed in Propositions 8–11. The later path description explicitly selects an optimal permutation, which exists by Birkhoff's theorem.
6. Uniform empirical-cdf control applies to left limits and sample-dependent interval endpoints. Conditioning the optimizer to make the interval deterministic would be invalid and is not done.
7. Only O_P(n^(-1/3)) is proved for maximum displacement; faster rates observed numerically are not promoted to theorems. The bound also proves a.s. vanishing without asserting an a.s. n^(-1/3) rate.
8. The quartic error is evaluated at the ACTUAL Euclidean optimizer. The comparison Q_n≤q(pi_e) is essential; a rank-competitor remainder alone would not compare the two optimal values to o(1/n).
9. Objective closeness does not imply plan closeness. The exact rational n=2 counterexample confirms that identification of finite optimizers is false; it does not determine their asymptotic weak limits.
10. The Hamilton–Jacobi derivative identity is asserted only on a single minimizing branch. Differentiability at ties and an asymptotic law for beta_j are not assumed. The semigroup statement is proved directly, including interchange of a finite minimum and an infimum.
11. The kinetic continuity identity is verified along finite paths. Equivalence to every feasible measure-valued Eulerian flow, a superposition theorem with creation/destruction, and uniqueness of Eulerian minimizers are not claimed.
12. The occupation-limit proof uses only marginal laws after a three-way decomposition of time. It explicitly proves that every possible horizontal kernel has the same limit, preventing a false inference of endpoint selection from the universal density r(x).

## Formal and computational verification
P0336SecondChecks.lean passed with exit code 0, elapsed 89.52 seconds. It proves the perspective splitting identity, the cubic consequence of the occupancy inequality, and strict opposite preferences of Euclidean and q costs in the rational counterexample. The printed axiom lists for these theorems are only propext, Classical.choice, Quot.sound; no sorry, custom axiom, or native_decide is used. The geometric, probabilistic, semigroup and weak-convergence arguments are written proofs, not advertised as Lean formalizations.

The first 20 fresh sample pairs gave identical e/q assignments; a 100,000-instance two-point search falsified a universal finite equality. Every value in the rationalized counterexample is checked with exact Fraction arithmetic, and all four square-root signs and the final choice inequality are also kernel checked. second_numerics.json contains the displacement/ordering/error checks and second_exact_counterexample.json contains the rational certificate.

## Honest outcome and remaining gap
VERDICT: PARTIAL. The new original-model results are uniform support concentration, quantitative O_P(n^(-1/3)) maximum vertical displacement, and O_P(n^(-5/3)) closeness of optimal Euclidean excess and perspective quadratic values. The latter gives a controlled route to a simpler kinetic/Hamilton–Jacobi assignment problem, but is not yet a reduction of the SELECTED PLAN unless microscopic stability is established. The macroscopic kinetic limit has been identified and proved incapable of discriminating horizontal kernels. Exact finite equivalence of the two optimizers is false.

P0336 remains unresolved: no existence, deterministic identification, random identification, or nonconvergence theorem for pi_n has been proved. The precise remaining task in approach A is to control microscopic target-branch competition in the dual envelope (the beta_j offsets and near ties), or to prove a stability estimate transferring weak endpoint plans under the O_P(n^(-5/3)) perturbation, and then identify the selected kernel for the q-problem. The entropy/Gibbs approach B remains unpursued and cannot currently justify interchanging the sample-size and zero-temperature limits.

The additional small-case check second_referee_check.py exhaustively inspected 5,912 permutations across n=2,...,7 for both costs, checked gap ordering of both computed optimizers, and verified the two-leg action minimum at its explicit stationary point. All passed; these numerical checks supplement, rather than replace, the written proofs and Lean certificates.
