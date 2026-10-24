# Further serious attempt, 2026-10-12

The remaining gap in ATTEMPT.md is determining c=lim D_k^(1/k) for **unrestricted interleaving** under the uniform product law. A finite cost upper bound does not prove an asymptotic lower base. Existing checked bounds are about 0.17840234 <= sigma <= 0.26185951.

## Two approaches not previously tried in this folder

1. **Optimize the lower-bound test function by transport duality.** Replace the linear sum of queried signs in the O'Donnell–Servedio argument by an arbitrary coordinate-Lipschitz function h. Its posterior under adaptive queries is a martingale with bounded increments. Optimize E[f h] over all such h, equivalently a finite Wasserstein-type dual problem between the two output-conditioned measures. If nonlinear h makes this covariance grow faster than (3/2)^k, its square would improve the exponential cost lower bound. Test finite instances by linear programming; prove the general bound or a precise obstruction. This route targets the missing lower bound directly and admits an exact mathematical analysis, so it is the primary route.

2. **Transfer a continuous-control policy as an explicit discrete construction.** Jacka–Warren–Windridge prove a run-the-middle rule for three diffusions. It was read earlier but no discrete posterior-median policy was tested. At a majority node, compute the three exact posterior probabilities of its children's outputs; recursively query the child whose posterior is the median, with explicit tie-breaking. This is a legal discrete algorithm whether or not the diffusion theorem transfers. Compute its exact cost at small depths and compare it to D_k; a sufficiently good fixed-depth cost would improve the algorithmic endpoint after composition. The theorem alone supplies no discrete optimality assertion.

Plan: pursue route 1 to its limit, with an independent finite LP check. Test route 2 as a bounded secondary check if practical. Brain recall requested using the gap words uniform expected query complexity / interleaving / lower bound / recursive majority / Bellman dual potential.

## Primary route: exact obstruction to optimizing a bounded-increment test function

This route yields a proved limitation, not a better value of sigma. It identifies a large class of potential lower-bound arguments that cannot beat the existing influence bound.

### The martingale lower-bound scheme

Work on the uniform sign cube and let f be nonconstant and monotone, with values ±1. Take any function h on the finite cube and subtract its mean. Suppose that for **every partial assignment on which f is still undetermined**, and for every possible next queried bit, the two conditional means of h differ by at most 2 in absolute value. This condition is weaker than a pointwise coordinate-Lipschitz condition: nothing is required for a residual subcube on which f is already constant.

For an exact algorithm that stops when f first becomes determined, M_t=E[h|the queried transcript and independent coins] is a martingale. Use a bounded horizon n and keep it constant after stopping. At an actual query its increment is X_i b_t, where b_t is half the difference of the two conditional means of h before that query. Hence |b_t|≤1 by the hypothesis. Distinct chronological increments are orthogonal: if s<t, the s-th increment is measurable before the t-th query and the conditional mean of the latter is zero. Thus E[M_T²]=Σ_t E[(M_t−M_(t−1))²]≤Σ_t P(T≥t)=E[T]. The output f is terminal-transcript measurable, so Cov(f,h)=E[(f−E f)M_T]. Cauchy–Schwarz gives

    E[T] >= Cov(f,h)^2 / Var(f).

Algorithms with redundant queries after determination can be shortened, so the same cost lower bound holds for all exact algorithms. All conditional distributions used here are uniform on the unqueried bits: adaptivity and independent coins do not change this fact.

### Optimizing the scheme gives exactly the influence bound

**Theorem.** Under the above condition, |Cov(f,h)|≤I(f). Equality is attainable with h(x)=Σ_i x_i. Therefore the strongest lower bound furnished by this scheme is exactly I(f)^2/Var(f).

Proof. Reveal all coordinates in a fixed deterministic order, regardless of when f becomes determined. Let F_i=E[f|X_1,...,X_i] and H_i=E[h|X_1,...,X_i]. The increments have the forms

    F_i−F_(i−1)=X_i a_i,   H_i−H_(i−1)=X_i b_i,

where a_i,b_i depend only on the first i−1 bits. Monotonicity gives a_i≥0. If f is already determined on that prefix, then a_i=0. Otherwise the assumed conditional-mean condition gives |b_i|≤1. Thus |a_i b_i|≤a_i on every prefix, including already-determined ones. Expanding the covariance of the two terminal martingales, all cross-time terms vanish by conditional mean zero, leaving

    Cov(f,h)=Σ_i E[a_i b_i],   |Cov(f,h)|≤Σ_i E[a_i].

Condition on all coordinates other than i. The half-difference of f between the + and − settings of coordinate i is exactly the pivotal indicator, since f is monotone and ±1-valued. The coefficient a_i is its average over future coordinates, conditional on the past. Averaging again gives E[a_i]=Inf_i(f). Hence Σ_i E[a_i]=I(f). Finally, h=Σ_i x_i has b_i=1 on every prefix and Cov(f,h)=Σ_i E[f X_i]=I(f), proving attainment and the theorem. No optimal-transport duality theorem or stochastic-domination theorem is needed for this proof.

For f_k, Var(f_k)=1 and I(f_k)=(3/2)^k. Thus this optimized scheme gives only D_k≥(9/4)^k. Nonlinear h, arbitrary high-degree polynomials h, and the relaxation that removes all constraints after determination cannot change that exponential base. This does **not** rule out potentials with nonuniform increment budgets, a history-dependent cost charging argument, or nonlinear Bellman subsolutions. Those remain possible approaches to the original gap.

### Vector-valued and fixed-weight extensions: still no stronger bound

The same obstruction holds for any finite collection of test functions combined into a Euclidean-vector-valued h, if its conditional half-difference vector at every undetermined cell has norm at most one. For an algorithm, vector martingale increments are orthogonal in expected inner product, so E[||M_T||²]≤E[T]. If z=E[(f−E f)M_T], then ||z||²≤Var(f)E[||M_T||²]: apply scalar Cauchy–Schwarz to the unit vector z/||z|| when z is nonzero. Thus E[T]≥||Cov(f,h)||²/Var(f). In the fixed full-reveal proof, the f coefficient remains the nonnegative scalar a_i, while the h coefficient is a vector b_i. The triangle inequality gives

    ||Cov(f,h)||=||Σ_i E[a_i b_i]||≤Σ_i E[a_i ||b_i||]≤I(f).

On determined prefixes a_i=0 as before. A single linear scalar test embedded in the vector space attains I(f), so the optimal vector scheme is again the old bound. Merely combining many Fourier polynomials or test functions does not bypass the obstruction.

More generally, fix nonnegative coordinate budgets w_i and require the conditional increment norm for querying i to be at most w_i on every undetermined cell. The same proof gives ||Cov(f,h)||≤Σ_i w_i Inf_i(f), with equality attainable by the scalar h=Σ_i w_i x_i. For an algorithm the squared martingale norm has expectation at most Σ_i w_i² P(i queried). Hence

    Var(f) Σ_i w_i² P(i queried) ≥ ||Cov(f,h)||².

Using only the maximum revealment δ_A gives a lower bound optimized over these tests and weights of

    δ_A ≥ (Σ_i Inf_i(f)²)/Var(f),

because Cauchy–Schwarz bounds (Σ_i w_i Inf_i)²/(Σ_i w_i²) by Σ_i Inf_i², with equality for w_i proportional to Inf_i. For f_k all influences are equal, giving exactly (3/4)^k. If instead only expected total cost is used, Σ_i w_i² P(i queried)≤(max_i w_i²)E[T]; optimizing the covariance ratio cannot exceed I(f)², since Σ_i w_i Inf_i≤(max_i w_i)I(f). Thus **fixed** coordinate weights do not help either. Residual-state-dependent budgets and other cost-sensitive potentials are still outside this theorem and remain untried.

### Equivalent transport result with an explicit all-depth bijection

Use 0/1 bits and Hamming distance. Let Ω_k^−={f_k=0} and Ω_k^+={f_k=1}, each with uniform conditional measure. The optimum mean Hamming cost of transporting one conditional measure to the other is exactly (3/2)^k. More strongly, there is an explicit coordinatewise increasing bijection T_k:Ω_k^−→Ω_k^+ achieving that mean cost.

The construction at depth one maps the four minority patterns as follows (patterns are the integers encoding the three bits):

    000 -> 111,  001 -> 101,  010 -> 011,  100 -> 110.

The four images are precisely the four majority-one patterns, each pair is coordinatewise increasing, and their Hamming distances are 3,1,1,1, with average 3/2. At depth zero, T_0 maps the single zero bit to one.

For depth k+1, let b be the three child-output bits of an input in Ω_(k+1)^−. Apply the displayed pattern bijection to obtain c≥b. For each child with b_i=c_i retain its entire input. For each changed child (necessarily 0→1), apply T_k to that child's input. This is well defined and produces root output one. It is coordinatewise increasing by induction. It is a bijection: from the output input read its child-output vector c, recover the unique b by the inverse pattern map, retain unchanged children and apply T_k inverse to changed children. This reconstructs the unique original input.

Under the uniform law conditioned on root zero, b is uniform over the four majority-zero patterns. Given b, its child inputs are independent uniforms on their corresponding output classes, because the three original input sets are independent and equally large output classes each have probability 1/2. Consequently the expected Hamming cost of the construction obeys

    A_0=1,   A_(k+1)=(3/2) A_k,

since an average of 3/2 child bits change and each such child input is uniform in Ω_k^−. Therefore A_k=(3/2)^k.

Optimality follows without a transport theorem. Let w(x) be the number of one bits. For any coupling (X,Y) of the two conditional measures, d_H(X,Y)≥w(Y)−w(X). Since f_k is balanced,

    E[w(Y)]−E[w(X)]
      = (E[Σ_i X_i | f_k=+1]−E[Σ_i X_i | f_k=−1])/2
      = E[f_k Σ_i X_i]
      = I(f_k) = (3/2)^k,

where the X_i in this display are signs. Thus every coupling has expected cost at least (3/2)^k, and the constructed bijection attains it. This makes the transport obstruction concrete at every depth, including arbitrary interleaving depths; it does not imply a cost-optimal query algorithm.

### Hostile-referee issues checked analytically

Before listing the checks, I extended the primary route beyond the first transport metric.

### Higher-order and bottleneck transport: exact auxiliary growth rates

Write W_p(k)=inf (E[d_H(X,Y)^p])^(1/p), where the infimum is over couplings of the two uniform output-conditioned measures, for a fixed real p≥1. Let W_infinity(k) be the minimum possible essential maximum displacement. These are auxiliary transport quantities, not query costs.

A second base-pattern bijection is

    000 -> 011,  001 -> 101,  010 -> 110,  100 -> 111.

It is coordinatewise increasing, bijective between the four classes, and has distances 2,1,1,2. Recursively retain unchanged children and use this second bijection on each changed child, exactly as in the first construction. The inverse and conditional-uniform-marginal arguments are identical, since the base map is again bijective and changes only 0→1 child outputs. Let Z_k be its Hamming displacement on a uniform negative input. At the top, the number K of changed child outputs is one or two with equal probability. Conditional on the child-output vector, changed child inputs are independent uniforms in their negative classes. Their displacements therefore have independent copies of Z_k, with distributions independent of K. Consequently

    Z_0=1,
    Z_(k+1) has the law of Z_k when K=1,
    and the law of Z_k+Z'_k when K=2,

where Z'_k is an independent copy. This is also the generation-size law of a Galton–Watson process with offspring 1 or 2 equiprobably. This assertion is derived from the conditional product structure, not imported from the book's different pivotal or spectral branching laws.

Put μ=3/2. The mean is μ^k. The second moment S_k obeys S_0=1 and S_(k+1)=μ S_k+μ^(2k): in the K=2 case expand the square and use independence to get 2S_k+2μ^(2k). Direct induction yields

    S_k=(4/3)μ^(2k)−(1/3)μ^k.

Indeed, substituting the displayed expression into μS_k+μ^(2k) gives the formula at k+1, using (4/3)(μ²−μ)=1. The base k=0 is 1. Thus

    μ^k <= W_2(k) <= sqrt((4/3)μ^(2k)−(1/3)μ^k).

The lower bound uses Jensen and the already-proved minimum mean distance; the upper bound uses this explicit coupling. In particular the quadratic transport quantity has exponential base μ, and its square has base 9/4, irrespective of its exact finite values.

In fact, every **fixed finite** p≥1 gives the same base. Here is a full moment proof. For integer r≥1 let u_(r,k)=E[Z_k^r]. We have u_(1,k)=μ^k. For r≥2 the binomial expansion and independence give

    u_(r,k+1)=μ u_(r,k)
      +(1/2) Σ_(j=1 to r−1) binom(r,j) u_(j,k) u_(r−j,k).

Induct on r. Suppose u_(j,k)≤C_j μ^(jk) for all j<r. The sum is at most B_r μ^(rk), with B_r=(1/2)Σ binom(r,j)C_j C_(r−j), a finite constant independent of k. Normalize v_k=u_(r,k)/μ^(rk). The recurrence gives

    v_(k+1)≤μ^(1−r)v_k+B_r μ^(−r).

Since a=μ^(1−r)<1 and v_0=1, iterating gives v_k≤1+B_r μ^(−r)/(1−a). This defines a finite C_r and proves the induction. For real p choose an integer r≥p. Jensen/Lyapunov gives (E Z_k^p)^(1/p)≤(E Z_k^r)^(1/r)≤C_r^(1/r)μ^k. Every coupling has (E d^p)^(1/p)≥E d≥μ^k. Combining the bounds proves

    lim_(k→infinity) W_p(k)^(1/k)=3/2    for every fixed finite p≥1.

The bottleneck value is different and exact: W_infinity(k)=2^k. The second bijection changes at most two child outputs per level, so induction gives displacement at most 2^k on every input. For the reverse bound, any positive-output depth-k input contains at least 2^k ones: at depth zero it needs one; at each majority root at least two positive children are needed, so their minimum one counts double. This bound is attained by choosing two minimum-one positive children and an all-zero third child, proving the minimum exactly. A uniform negative input equals the all-zero vector with positive probability. Conditional on that event, every coupled positive input has Hamming distance at least 2^k. Thus every coupling's essential maximum is at least 2^k, proving optimality of the second bijection for the bottleneck value as well as for the mean.

transport_moments.py checks this second bijection exhaustively at k=0,1,2, including its mean, maximum and second-moment formula. The assertions concern transport only. No inequality comparing D_k directly to W_p(k)^2 for p>1 is asserted here, and these auxiliary exponents do not determine sigma. This extension shows that merely replacing mean transport by a fixed higher-order transport norm cannot increase the transport growth base.

### A finite quadratic-transport identity fails at depth two

The depth-one value W_2(1)^2 happens to equal D_1=5/2. I tested whether this suggests an exact query-cost reduction. It does not: exact quadratic transport between the conditional output classes at depth two is

    W_2(2)^2=337/64,

whereas D_2=393/64; the difference is 7/8. This refutes the literal identity D_k=W_2(k)^2. It does not refute any lower-bound inequality between them or exclude equality of exponential growth rates.

Here is the complete finite-certification method. Enumerate each uniform output class as x_1,...,x_N and y_1,...,y_N, with N=4 at depth one and N=256 at depth two. For integer costs c_ij=d_H(x_i,y_j)^2, compute a candidate permutation π and integer row and column potentials u_i,v_j satisfying

    u_i+v_j≤c_ij for every i,j,
    Σ_i c_(i,π(i))=Σ_i u_i+Σ_j v_j.

These two verified facts prove optimality without any integrality theorem or trust in an optimizer. The uniform permutation coupling has expected cost (Σ_i c_(i,π(i)))/N. Every coupling has masses p_ij with row and column sums 1/N, so its expected cost is at least Σ_ij p_ij(u_i+v_j)=(Σ_i u_i+Σ_j v_j)/N. The verified equality makes this lower bound exactly the candidate coupling's cost. Thus the optimum over **all** couplings, including fractional ones, is certified.

quadratic_transport.py uses SciPy's assignment solver only to propose π. It reconstructs an exact integer dual by difference constraints: writing a_i=c_(i,π(i)), complementary equality requires u_i=a_i−v_(π(i)), and feasibility is equivalent to v_j≤v_(π(i))+c_ij−a_i. Starting all v_j at zero, repeatedly relax all these inequalities with integer arithmetic until fixed; then define u_i. The program checks all inequalities and equality of the total sums. A nonoptimal candidate could fail to yield such a fixed feasible dual; no solver result is accepted without those exact checks.

The saved certificates quadratic_transport_certificate_1.json and _2.json list both complete output classes, π and all integer potentials. Their costs are 10/4=5/2 and 1348/256=337/64. The separate verify_quadratic_transport.py uses direct group-majority truth tests and binary-string Hamming counts, with no solver or NumPy. It checks all 16 and 65,536 pointwise dual inequalities, completeness of both classes, permutation marginals and equality of exact primal and dual costs. Its results are recorded in quadratic_transport_verification.json after the check finishes. Thus this is a computationally proved finite transport result and a finite counterexample to that prospective reduction, not floating-point evidence alone.

### Referee issues

* Centering h is essential for the martingale second-moment argument; h was explicitly centered, which does not alter conditional differences or covariance.
* Full deterministic revelation in the upper-bound proof may continue after f is determined. No bound on its h increment is required there, because the corresponding f increment is zero.
* The coefficient a_i is not a random pivotal indicator at the actual unqueried input. It is a conditional average of that indicator; the tower property is the justification for E[a_i]=Inf_i(f).
* The transport bijection changes entire child inputs only when the child output changes 0→1. Conditional independence and uniformity of those inputs, not unconditional independence of changed-child events, justify the expected-distance recurrence.
* A coupling minimum is not a query-cost minimum. Squaring this transport value gives the old influence bound, not a proof that c=9/4.

Independent LP, exhaustive small-depth bijection and Lean finite-base results are recorded below once available.

## Independent numerical and exhaustive checks of the primary route

transport_checks.py checked the explicit bijection exhaustively at k=0,1,2: respectively 1,4,256 inputs in the zero-output class. Every image has output one, is coordinatewise above its input, and is distinct. Exact mean Hamming distances were 1, 3/2, 9/4. The proof above, rather than extrapolation from these finite values, establishes the all-depth assertion.

The same script optimized E[f h] subject to all coordinate edge differences lying in [−2,2], with one h value fixed to remove additive constants. HiGHS linear programs had (8 variables,24 constraints) and (512 variables,4608 constraints). The optima were exactly 1.5 and 2.25 in floating point, with zero reported edge violation. These LPs are independent checks, not rigorous numerical certificates replacing the proof.

relaxed_transport_lp.py removed all constraints for determined residual subcubes. At k=1 it tested all 13 undetermined partial assignments, giving 42 conditional-increment inequalities. At k=2 it tested all 13,117 undetermined partial assignments, giving 92,142 inequalities and 2,166,336 sparse matrix entries. Coefficients for a cell with m unknown bits are ±2^(−m), representing half the conditional-mean difference. LP optima were 1.5 and 2.2500000000000737; the second maximum reported constraint violation was 8.53e−12. These agree with, but do not prove, the general theorem. Construction/solve time was about 31 seconds and memory stayed within the job budget.

## Secondary route: a stronger restricted-class counterexample

The naive fixed-tie recursive posterior-median policy has exact costs 5/2, 199/32, and 524880675/33554432 at depths 1,2,3. Its attempted depth-four enumeration hit the bounded type cap and yielded no depth-four result. It gives no better exponent bound.

Arbitrary tie-breaking is a genuine issue: a fixed tie rule can lose even if another tie rule attains optimal cost. I therefore optimized over **all recursively posterior-median rules**, including arbitrary choices among tied posteriors, adaptive choices at later transcripts, and independent randomization. The restriction is exact: at every ancestor of the chosen leaf, the chosen child must have posterior output probability equal to the median of the three child probabilities on the current transcript. This is a multilevel discrete restriction; it is not the three-diffusion theorem and does not cover arbitrary within-child strategies in a root-only median rule.

### Complete constrained Bellman proof

Use the same residual simplifications as ATTEMPT.md. They preserve this class. Two equal constant children make the parent determined, so it stops. With one 0 and one 1 child, the third child's probability is strictly between 0 and 1 if the node is undetermined; it is the unique median child. Collapsing that node merely removes an ancestor at which the child choice was forced. Sorting is a permutation of equivalent child positions. Distinct occurrences continue to use distinct unknown bits.

Let Q(s) be the exact posterior probability of a residual type's output being one. Constants have Q=0,1; an unknown bit has Q=1/2; and for three independent child residuals with probabilities a,b,c,

    Q(parent)=ab+ac+bc−2abc.

For a nonconstant node, define its allowed next-query set recursively: select any child whose Q is the median of the three Q values and then select any query allowed in that child. For an unknown leaf the allowed outcomes are (0,1). Lift these outcomes back to the parent and simplify. Take the union over all tied median children, removing duplicates only after canonicalization. This is exactly the set of permissible next leaf queries by the class definition, because a permissible leaf path must select a median child at each of its ancestors. Conversely every path generated recursively satisfies that definition. The median child is always nonconstant at an undetermined node, so the set is nonempty.

With m(s) unknown bits and successors a,b, the exact integer Bellman recurrence for the constrained optimum is

    B(s)=0 for constants;
    B(s)=min_allowed(a,b) [2^m(s)+2^(m(s)−1−m(a))B(a)
                                  +2^(m(s)−1−m(b))B(b)].

Induction on m(s) proves optimality. Any allowed decision tree must take an enumerated first leaf query; conditional on its fair outcome, its remaining cost is at least the corresponding constrained continuation value. Choosing a minimizing first query and optimal continuations attains the minimum. Randomizing cannot lower this minimum, since the average of first-action costs is at least their minimum and the induction applies to randomized continuations as well. Therefore B(full_k)/2^(3^k) is the optimum among the entire stated class, not just one tie rule.

The exact computations are

    M_1=5/2,
    M_2=393/64=D_2,
    M_3=257554309/16777216=15.351433098316193… .

Consequently

    M_3−D_3=4817493/16777216>0.

This is a finite counterexample to optimality of the naive recursive posterior-median construction, **even with optimal adaptive tie-breaking**. It is not a counterexample to the original open problem, to the continuous theorem, or to every conceivable index policy.

It also has a direct revealment formulation. The recursively median-eligible class is preserved by every rooted-tree automorphism: automorphisms merely permute the children and their posterior probabilities, preserving the median condition at each ancestor. The symmetrization proof in ATTEMPT.md therefore applies within this class as well, giving minimum class revealment M_k/3^k. At k=3 this is 257554309/452984832, strictly above the unrestricted value 15796051/28311552; the exact revealment gap is 535277/50331648. This is a finite-class statement. A finite gap alone does not exclude asymptotic optimality at arbitrarily large depths or determine an exponent for this class.

### Independent structural certificate and referee check

median_optimal_ties.py exports median_ties_certificate.json. verify_median.py expands types as actual residual expression trees. It independently computes child probabilities as Fractions, enumerates actual leaf paths satisfying the median condition, substitutes both bit values, normalizes structurally, and compares the full allowed successor set to the certificate. It checks every constrained Bellman equality and strict decrease in unknown-leaf count. The verifier passed all 2,207 states and 2,625 successor pairs with zero errors, in about 0.4 seconds. The unrestricted D_3 used in the comparison was independently certified in the first attempt. Files median_optimal_ties.json and median_verification.json contain the exact results.

The main possible logical failure was omitting permissible tied actions. The verifier enumerates **every** eligible actual leaf path, including tied children with different residual functions; this specifically tests that issue. Collapsing opposite constants is justified above, rather than being assumed to preserve a restricted policy. The exact recurrence uses integer arithmetic; there are no floating-point ordering decisions in this constrained optimization.

### Explicit optimal-policy reachable witness: failure already after three queries

median_witness.py additionally traversed the previously certified unrestricted depth-three Bellman table along actions attaining its optimal value. It found a failure after three queries, all with outcome zero (a trace of probability 1/8 for an exact policy making those optimal choices). Let U be a fresh bit, M=Maj(U,U,U), and A=Maj(0,U,U), with every occurrence using separate unknown bits. The residual root is

    Maj( Maj(M,M,M),  Maj(M,M,A),  Maj(M,A,A) ).

There are 24 unknown leaves. The root's three child posterior probabilities are 1/2,3/8,1/4. Its exact unrestricted continuation value, from the independently checked table, is 3028131/262144. The best next query among **all recursively median-eligible leaf paths**, even if unrestricted optimal continuation is allowed after that one query, costs 3031947/262144. Thus every such next query has regret at least

    477/32768 > 0.

One unrestricted optimal leaf path selects the middle root child Maj(M,M,A), whose posterior 3/8 is indeed the root median. Inside that child it selects A, whose posterior 1/4 is **not** the median of 1/2,1/2,1/4. It then queries an unknown bit in A. Hence the failure is a concrete cross-level effect: the other root children affect the best strategy inside an unfinished child. It is not merely a bad root-level tie choice.

median_witness.json records the state, the three exact Bellman-optimal predecessor transitions, the selected leaf path, all posterior comparisons along that path, the exact value and penalty. Each predecessor action was additionally checked to be median-eligible, so the three-query prefix itself can obey the recursive median rule while remaining unrestricted-cost-optimal. The witness search checks all median-eligible pairs against the unrestricted successor set and compares every eligible one-step cost to its certified unrestricted Bellman value. Only seven reachable states were inspected before finding this witness. This gives a concrete obstruction along an optimal policy; it does **not** by itself prove that every optimal policy encounters this state. The separate full constrained-DP proof establishes M_3>D_3 for the whole class. This distinction is necessary for the quantifiers.

## Brain use and remaining gap after this attempt

Two read-only math-store calls were made specifically for the gap and new route:

* "uniform expected query complexity interleaving lower bound recursive majority Bellman dual potential". The relevant warning card was claim_baea3babc8c8e718c778c89c62b1bf3793c9c3b3a7e39ff98a401521056419b1: average query cost alone need not bound each revealment. This does not invalidate the earlier exact reduction, which uses transitive automorphism symmetrization explicitly. Most retrieved cards were off topic; none supplies a matching lower base.
* "Kantorovich Rubinstein Strassen monotone coupling". The store returned the real-valued Strassen coupling theorem (claim_d4ceae7714f94e59a9363adaaf91efab), Strassen's source (source_875c9cf98717b8c1b29752e022bea64e49a32bf2815b0362f25f4f5535e4b289), and a transportation-information-method card. The real-valued theorem does not directly establish a coordinatewise cube coupling. Our explicit bijection and direct martingale proof avoid this hypothesis mismatch. The complete second recall is saved in brain_transport_recall.txt.

The original gap is still determining c=inf_k D_k^(1/k) for unrestricted interleaving algorithms. The bounded-increment/transport route is now proved incapable of improving the old lower base, including its relaxed version. The naive recursive continuous-policy translation is now refuted at depth three. A genuinely different cost-sensitive, nonuniform-increment or history-dependent lower-bound invariant is still needed; no such invariant is established here. The previously checked interval [0.1784023402720471…,0.2618595071429149…] is unchanged. No novelty or literature-resolution claim is made for these auxiliary results.

Formal finite checks and final verdict are appended when collected.

## Formal checks and final verdict

TransportFinite.lean compiled with exit code 0 using `lake env lean ~/brain_workers/TRIO_1011/op/C0021/TransportFinite.lean` from ~/lean_verify. One shared-slot invocation was used. The file was extended while queued; the output includes the final theorem median_revealment_gap, confirming that the extended revision was checked. Source SHA256: 91b4d03f8964da2bd3c3cc54198b6f64b163953d5d457b88e246e7843f31ebd1.

The eight finite-map theorems (the original coupling facts and the alternate map's output, monotonicity, displacement bound, injectivity and two moments) use `decide +kernel`, not native_decide. Six rational facts use norm_num, including the depth-three strict gap, positive local regret, and revealment-gap normalization. Only Mathlib.Data.Fintype.Basic and Mathlib.Tactic.NormNum are imported. There is no sorry or native_decide. Output and scope are recorded in lean_second_check.txt. The complete martingale theorem, all-depth recursive bijections and transport-moment asymptotics remain full handwritten proofs, not Lean formalizations. MedianGap.lean is a standalone copy of five rational statements; it was not run separately, and its counterparts in TransportFinite.lean are the checked ones.

**Final verdict: PARTIAL.** Two previously untried approaches were developed and checked. The primary approach has a complete obstruction theorem and explicit optimal monotone transport bijections, fixed-order transport growth rates and a finite counterexample to a quadratic-transport query-cost identity. The secondary approach has a certified counterexample to finite-depth optimality of the recursive posterior-median class, including arbitrary adaptive tie-breaking, and an explicit three-query witness. These narrow the viable methods; they do not tighten the existing exponent interval or determine sigma. The remaining gap is still a matching exponential lower bound on unrestricted uniform expected query cost. A concrete next direction is a residual-state-dependent quadratic-variation/cost potential that cannot be reduced to bounded test functions or fixed coordinate weights.
