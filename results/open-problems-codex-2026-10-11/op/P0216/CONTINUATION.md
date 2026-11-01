# Further attempt — 2026-10-11

The remaining gap is existence and evaluation of lim E C_n/n^(1/3) for same-label independent uniform-square orders. The previous variance bound and grid lower bounds do not resolve it.

## Two approaches not previously tried

1. **Exact collision enumeration through balanced permutations.** Reverse the last two coordinate orders. Equality of the two posets then becomes the requirement that each pair is oriented each way twice among four total orders. Fix the first order by relabelling and recursively insert the largest label. The other three prefix sets must partition the old labels. This gives an exact finite recurrence for collision probabilities and exposes the exponential factor in Aldous–Brightwell Subproblem 4. Pursue exact counts, sharp insertion bounds, and whether these can sharpen the first-moment upper constant. This differs from simulating a lower construction or small optimal coincidence sets.

2. **Poissonized box concatenation toward a Hammersley limit theorem.** Regard the input as a Poisson process in [0,t]^4. Concatenating boxes along all four diagonals gives superadditivity, but the natural t scale corresponds to n^(1/4), whereas the target is n^(1/3). Try a three-direction tiling or a surface variational principle that preserves agreement across boxes. The key obstacle is that unions of locally feasible sets need not agree across boxes unless both pairs of coordinate signs are controlled. A successful theorem must address that obstruction rather than simply invoke subadditivity.

Approach 1 is selected: it has an exact, verifiable recursion and a plausible route to a genuinely sharper upper estimate. Approach 2 remains a lead, with its scaling obstruction explicitly recorded.

Brain query: `Aldous Brightwell common random posets limit constant subadditivity balanced permutations` (math_recall.py, 2026-10-11). Returned cards will be treated as hints only.

## Exact collision reduction and insertion recurrence

Let p_n be the probability that two independent point orders on n labels are identical, and let H_n count triples of total orders for which, together with the increasing first order, every pair is oriented each way exactly twice. Set H_0=1.

For an ordered pair i,j, let a,b,c,d in {0,1} indicate that i precedes j in the four coordinate orders. Identical partial orders require a*b=c*d and (1-a)*(1-b)=(1-c)*(1-d). These two equations hold exactly when a+b+(1-c)+(1-d)=2: if a+b is 0 or 2, c+d must equal it, and if a+b=1, neither direction is comparable and c+d must also be 1. Reversing the last two total orders therefore gives a bijection from equal-order quadruples to balanced quadruples.

Each of the (n!)^4 coordinate-rank quadruples is equally likely. Relabelling to make the first order increasing is a bijection on the remaining triples, and there are n! choices for that first order. Hence

    p_n=H_n/(n!)^3.

To generate all balanced triples on [n], remove n. The remaining triple must be balanced on [n-1]. Insert n in its three orders after prefix sets A,B,C. Since n is last in the fixed first order, each old label already precedes n once. Balance says it must precede n exactly once among the other three orders. Thus A,B,C must partition [n-1]. Conversely any such three prefixes produce a balanced triple. Removal uniquely recovers the parent and the insertion slots; no overcount occurs. This proves the exact enumeration recurrence, without an asymptotic assertion.

The exact values through n=8 are H_n=1,3,15,99,771,6693,62841,627621. They agree with the independently computed collision probabilities for n<=4 in exact_posets.json. The data do not determine the exponential growth rate.

## Neighboring-theorem reduction

For a permutation pi, let P_pi be the order with first-coordinate ranks 1,...,n and second-coordinate ranks pi. Write r(pi) for its number of ordered two-total-order realizers. Counting equal-order quadruples by their first two orders, and relabelling their first order to increasing, gives

    H_n=sum_{pi in S_n} r(pi).

There is also a useful exact graph interpretation. The incomparability graph of P_pi is the inversion graph of pi. A realizer determines a transitive orientation of that graph by its first total order. Conversely, combine any transitive orientation Q of this graph with P_pi. The tournament P_pi union Q has no directed triangle: two consecutive edges of the same one of these two transitive relations would force their third edge to be in that same relation, contrary to the triangle. Every directed triangle has two consecutive edges of one color. A tournament without directed triangles is a total order (a shortest directed cycle would have a chord producing a shorter cycle). The same argument applies to P_pi union Q^op. Their intersection is P_pi. These maps are inverse, so r(pi) equals the number of transitive orientations of its inversion graph.

Use Gallai's transitive-orientation theorem for canonical modular decomposition to encode (pi, Q) by a plane rooted tree. Leaves are singletons. At an increasing quotient node there is one orientation, at a decreasing quotient node of arity d there are d! orientations, and at a prime quotient node there are two. A quotient permutation has at most d! choices. A deliberately loose node-label bound is 4*d! for d>=2. The structural theorem and the interval property are verified in the explicit encoding proof below. In particular no unverified equivalence between arbitrary graph modules and permutation intervals is assumed.

## Rigorous weighted-tree bound (independent of the encoding question)

Let Z_n count all plane rooted trees with n leaves, internal arity d>=2, with 4*d! possible node labels. For formal power series T(x)=sum Z_n x^n, the recursive specification is

    T=x+sum_{d>=2} 4*d!*T^d.

This is a formal identity: each coefficient uses only finitely many terms, so convergence of the factorial series is irrelevant. Lagrange inversion applied to T=x/(1-sum_{j>=1}4*(j+1)! T^j) gives, for n>=2,

    Z_n=sum_{k=1}^{n-1} (n+k-1)!/(n!*k!) * 4^k
          *sum_{j_1+...+j_k=n-1; j_i>=1} prod_i (j_i+1)!.

For positive r,s, (r+1)!(s+1)!<=[2*(r+s)!]. Indeed the ratio (r+1)!(s+1)!/(r+s)! is nonincreasing in r, because its next/current ratio is (r+2)/(r+s+1)<=1; at r=1 it equals 2. Repeatedly merge r,s to r+s-1. This proves prod_i(j_i+1)!<=2^(k-1)*(n-k+1)!. There are binomial(n-2,k-1) compositions.

Set Q(n,k)=(n+k-1)!(n-k+1)!/(n!)^2. For k<=n-1, Q(n+1,k)/Q(n,k)=1-(k-1)^2/(n+1)^2<=1. Thus Q(n,k)<=Q(k+1,k)=2*binomial(2k,k)/(k+1)^2<=4^(k-1) when k>=2, using binomial(2k,k)<=4^k and (k+1)^2>=8. For k=1, Q=1, the same bound holds. Also binomial(n-2,k-1)<=n^(k-1)/(k-1)!.

Combining the inequalities gives

    Z_n/n! <=4*sum_{j>=0} (32n)^j/((j+1)!j!)
             <=4*sum_{j>=0} (32n)^j/(j!)^2
             <=4*exp(2*sqrt(32n)).

For the last inequality, binomial(2j,j)<=4^j gives 1/(j!)^2<=4^j/(2j)!, and the resulting even-power exponential series is cosh(2sqrt(32n))<=exp(2sqrt(32n)). The bound also holds for n=1, where Z_1=1.

The encoding H_n<=Z_n, proved below using the checked Gallai theorem, now establishes

    1 <= (p_n (n!)^2)^(1/n) <= (4 exp(2sqrt(32n)))^(1/n) ->1,

because every pi has at least one realizer, so H_n>=n!. This solves the collision-rate subproblem (Aldous–Brightwell Subproblem 4, beta=1), not P0216 itself. The elementary counting and asymptotic portions are fully proved here; the structural input is the established Gallai theorem, with exact retrieved statements below. No novelty claim is made.

## Consequence for the optimal mean

The preceding bound gives p_k<=4 exp(A sqrt(k))/(k!)^2 with A=2sqrt(32). For every integer k<=n,

    Pr(C_n>=k)<=binomial(n,k)p_k<=4 exp(A sqrt(k)) n^k/(k!)^3.

The first inequality is a union bound over label subsets of size k; each restriction has exactly the independent k-point law. Since k!>=(k/e)^k, for fixed B>e and k>=B n^(1/3), the last expression is at most 4 exp(A sqrt(k)-delta k), where delta=3log(B/e)>0. For all sufficiently large n, A sqrt(k)<=delta k/2 for every such k. Summing the geometric tail proves limsup E C_n/n^(1/3)<=B. Let B decrease to e. This independently establishes the order upper bound, without importing the source's sketched bound.

The binomial-moment refinement improves e to an explicit K. Let x=E C_n and k be an integer. The function f_k(t)=0 for t<=k-1 and f_k(t)=prod_{j=0}^{k-1}(t-j)/k! for t>k-1 is convex: on the second region its second derivative is a sum of products of nonnegative factors; at the junction its right derivative is 1/k>=0 and its left derivative is zero. For integer nonnegative t it equals binomial(t,k). The number of coincident k-subsets equals binomial(C_n,k) only as a LOWER bound: any optimal set supplies all its k-subsets, while other feasible subsets may exist outside that set. Thus, with N_k counting all coincident k-subsets,

    f_k(x)<=E binomial(C_n,k)<=E N_k=binomial(n,k)p_k.

This distinction is essential; equality E N_k=E binomial(C_n,k) would be false. For x>k-1 the inequality implies

    prod_{j=0}^{k-1}(x-j) (k!)^2 <=4 exp(A sqrt(k)) n^k.

Take a subsequence on which x/n^(1/3)->c>0; boundedness was just proved. Set k=floor(b n^(1/3)) for any fixed 0<b<c. The logarithm of the product is a Riemann sum, with all x-j bounded away from zero at this scale. Stirling's formula for k! and division by n^(1/3) give

    c log c -(c-b)log(c-b)+2b log b-3b<=0.

The term A sqrt(k)/n^(1/3) tends to zero; so does log(4)/n^(1/3). Write r=b/c. Dividing by b gives

    3 log c + h(r)-3<=0, where
    h(r)=2log r-((1-r)/r)log(1-r), 0<r<1.

Its derivative is [3r+log(1-r)]/r^2. The numerator starts at zero, increases up to r=2/3 and then decreases strictly to minus infinity. Consequently there is exactly one zero r* in (2/3,1), and h reaches its unique maximum there. The equation is log(1-r*)=-3r*. Therefore

    K=exp(1-h(r*)/3)=exp(r*)/(r*)^(2/3),
    limsup E C_n/n^(1/3)<=K.

Every positive subsequential limit obeys that bound; a zero subsequential limit does so trivially. This is the source's beta=1 first-moment constant; the collision beta=1 proof above now establishes its premise. This still supplies no matching lower constant and no limit-existence argument.

The root is r*=0.9404797907073597 and K=2.668162063280738 (bisection evaluated independently in JavaScript and Python, residual -4.44e-16). The preliminary progress message's 2.66848 decimal was a transcription error; this value replaces it.

## Explicit encoding proof and external-theorem audit

Use the canonical strong-module decomposition of the inversion graph G_pi. A module M has uniform adjacency to every outside vertex; it is strong if it overlaps no other module (overlap means nonempty intersection with neither set containing the other). Taking complements preserves the module family and overlap, hence the strong-module family and its canonical inclusion tree. G_pi and its complement therefore have the same tree.

The exact established structural input is verified in Miriam Münch, Ignaz Rutter, Peter Stumpf, *Partial and Simultaneous Transitive Orientations via Modular Decompositions*, arXiv:2209.13175, retrieved PDF pp.4–5. Page 4 states:

> For every graph G there exists a uniquely defined modular decomposition, that we call the canonical modular decomposition of G, introduced by Gallai [17], such that each quotient graph is either prime, complete or empty and, additionally, no two adjacent nodes are both complete or are both empty

Page 5 defines the represented orientation by directing every edge between two child modules according to their quotient edge, and then states verbatim:

> Let T now be the canonical modular decomposition of G. Then T represents exactly the transitive orientations of G [17].

The same page states:

> If G is a comparability graph, every prime quotient graph G[µ] = (Vµ, Eµ) has exactly two transitive orientations, one the reverse of the other [20]

This is exactly the needed uniform-cross-edge and quotient-orientation representation theorem. G_pi and its complement are finite simple comparability graphs: the inversion and noninversion orientations from natural index order are explicitly transitive, as shown below. Thus the theorem's hypotheses are satisfied. These are established graph-theoretic inputs, not conjectured poset-limit inputs.

An independent retrieved proof of the prime-orientation part is Robert Brignall, Sean Mandrick, Vincent Vatter, *Chains and unique transitive orientations of prime graphs*, arXiv:2609.08057v1, Theorem 1.1, PDF p.2 (proof pp.3–4):

> If a graph is prime, then any two of its edges belong to the same edge class. In particular, a prime graph has at most two transitive orientations, and if there are two, they are reversals of each other.

It identifies the original as T. Gallai, *Transitiv orientierbare Graphen*, Acta Math. Acad. Sci. Hungar. 18 (1967), 25–66, Satz 1.8, Item 5. This neighboring result is not a literature solution of P0216.

The required interval property now follows. Let Q_0 orient inversions from smaller natural index to larger, and P orient noninversions in the same way. Q_0 is transitive because i<j<k and pi_i>pi_j>pi_k imply pi_i>pi_k. P is transitive by the analogous increasing inequalities. For any strong module M and outside vertex v, their lowest common ancestor in the decomposition puts M inside one child and v in another. Uniform quotient orientation therefore gives uniform cross-direction between v and M whenever edges exist. Since M is a module in both complementary graphs, exactly one of P or Q_0 has all the edges from v to M. Thus v is uniformly before or uniformly after M in their union, the increasing total order. Consequently M is an interval of that order: an outside vertex lying between two members would contradict that uniform direction. The same argument for P union Q_0^op, the pi total order, shows M is an interval there too.

Order the children at every tree node by their first-coordinate intervals. Their second-coordinate intervals determine a unique quotient permutation sigma. It specifies the quotient graph. Empty quotient: sigma is increasing, one Q orientation. Complete quotient: sigma is decreasing, at most d! Q orientations. Prime quotient: at most d! choices of sigma and at most two Q orientations each. There are at most 1+d!+2d!<=4d! possible combined node labels.

The encoding is injective: the plane tree, quotient permutations, and child sizes reconstruct pi by repeated inflation of contiguous blocks; quotient Q orientations and recursively encoded child orientations reconstruct all edges of Q. Leaves are already in natural index order, so no additional leaf-labelling n! factor is required. Adding such a factor would destroy the collision conclusion and would be a serious counting error. Actual canonical trees are a subset of the overcounted all-plane-trees family Z_n. This proves H_n<=Z_n and completes both the collision-rate theorem and the upper-mean theorem.

For the later exact generating-series argument, quotient choices also extend independently. This can be checked directly, in addition to the structural theorem: inflate a transitively oriented quotient by transitively oriented child graphs, directing all cross edges uniformly. Consider any directed two-edge path x->y->z. If the three vertices lie in three different children, quotient transitivity supplies x->z. If two consecutive vertices are in one child and the third is outside, uniform cross directions supply x->z. If x,z are in one child and y outside, the two directions to y would conflict with uniform orientation, so that case cannot occur. If all three are in one child, use that child's transitivity. Induction on the tree proves the global orientation is transitive. Thus no unverified independence of orientation choices is needed in the formal-series root partition.

## Remaining gap after this attempt

We have proved the exact collision-rate limit and the numerical limsup bound 2.668162063... for the optimal mean. We have NOT proved convergence of E C_n/n^(1/3), and have NOT determined its limit. The collision-rate limit does not supply either: the first-moment bound does not control dependence among the many candidate subsets. No matching lower bound has been constructed. In particular the source's conjectured optimal c must not be identified with the first-moment upper constant K.

The order upper bound is now established in this attempt, so ATTEMPT.md's variance reduction applies without relying on the draft's outline: C_n/n^(1/3)-E C_n/n^(1/3) tends to zero in L^2, and a mean limit is equivalent to a probability limit. This still leaves the deterministic mean sequence's convergence unproved.

## Hostile-referee audit

* Labels are preserved in the problem. The only relabelling in the collision count simultaneously relabels all four orders to normalize the first order; the missing n! is then explicitly restored before dividing by (n!)^4.
* Both directions of a pair's partial-order relation must agree. Testing only a*b=c*d would miss reverse comparabilities. The two-direction truth table is the Lean target.
* The transitive-orientation/realizer bijection is proved by the absence of directed triangles, not assumed from the fact that a graph is a permutation graph.
* Only canonical strong modules are used. Arbitrary modules need not be intervals in either total order. Their interval property here is derived from the exact all-orientations representation theorem for the canonical tree and its complement.
* The node label bound includes all quotient permutations and all quotient orientations. Leaves are in their already fixed first-coordinate order; no independent leaf-labelling factor remains.
* Factorial ordinary series are handled formally. Lagrange inversion is a coefficient identity; no false positive radius of convergence is invoked.
* The tree overcount is sufficient for an exponential-rate upper bound. It is not asserted to give an asymptotic equivalent for H_n.
* Coincident k-subsets outside a selected optimal set mean E N_k need not equal E binomial(C_n,k). The proved inequality has the correct direction.
* The Jensen function is truncated below k-1; the untruncated falling factorial is not globally convex. The derivative jump and nonnegative second derivative are checked explicitly.
* A tail SUM is used to pass from the first-moment probability bound to the mean bound. A single probability estimate at B n^(1/3) would not suffice for this passage.
* The upper constant K is distinct from any conjectured optimal limit c. No step proves or assumes that the first-moment method is sharp.

## Auxiliary exact formal-series reduction

This identity is not required for the upper bound, but gives an efficient further computation of the collision counts. All series here are formal (their ordinary factorial coefficients do not define convergent analytic functions near zero).

Let F(x)=sum_{n>=1} n! x^n, and let S(x) count simple permutations of size at least four. A quotient permutation in a prime node is simple: a nontrivial common interval would be a nontrivial inversion-graph module. Conversely a simple nonmonotone permutation has prime inversion graph: if the canonical graph tree had a proper nonsingleton child, the proved interval property would give a nontrivial common interval; if all children are singletons, the only nonprime alternatives are a complete or empty graph, corresponding to monotone permutations. Thus prime quotient labels are precisely the simple permutations of size at least four.

The canonical tree decomposes every permutation into a singleton, an increasing root, a decreasing root, or a simple prime root. With unweighted orientations, the increasing-root generating series is F^2/(1+F): its children are non-increasing-root objects I, giving increasing roots I^2/(1-I) and F=I/(1-I). The decreasing-root expression is the same, by symmetry. Therefore

    F=x+2F^2/(1+F)+S(F),
    S(u)=-F_inverse(u)+2u/(1+u)-u.

This agrees with Adin et al., arXiv:1711.06511, Proposition 5.3, PDF p.9, specialized to s=t=1; the displayed formula was independently derived here from the root partition.

Now let H(x)=sum_{n>=1} H_n x^n count (pi,Q). Its increasing roots still contribute P=H^2/(1+H), since their quotient graph is empty and has a unique orientation. Write B for its decreasing-root contribution and J=H-B. A decreasing root with d children has d! quotient orientations, and each child's root is not decreasing, so B=sum_{d>=2}d!J^d. Thus H=F(J), J=F_inverse(H), and B=H-F_inverse(H). Prime roots contribute 2S(H). Consequently

    H=x+H^2/(1+H)+H-F_inverse(H)+2S(H),
    x=3F_inverse(H)+H-3H/(1+H).

Every root partition is canonical, so this is an exact identity rather than an inequality. Composition inverses exist formally because F(0)=H(0)=0 and F'(0)=H'(0)=1. Formal inversion by integer coefficient recursion in JavaScript gives H_9=6606069, and coefficients through H_16 in formal_series_diagnostic.json. The first eight coefficients agree with both independent enumerations. Higher coefficients from this identity are exact computations conditional only on the established canonical decomposition used throughout the proof; they are not data about the optimal C_n limit. No unproved analytic asymptotic is inferred from this factorially divergent series.

## A concrete second-moment obstruction for the remaining gap

Let N_k count all k-subsets whose two induced orders agree. At k=floor((12/5)n^(1/3)), the ratio E N_k^2/(E N_k)^2 grows exponentially in k. This does NOT assert that Pr(C_n>=k) tends to zero; it shows that the direct unweighted Paley–Zygmund lower bound (E N_k)^2/E N_k^2 tends to zero, so that particular lower-bound route fails to approach K.

Fix a first k-subset A and a second k-subset B with |A intersection B|=r. If the two orders agree on their union, they agree on both subsets. Their union has m=2k-r labels, so the joint event has probability at least p_m>=1/(m!)^2. There are binomial(k,r)binomial(n-k,k-r) choices for B for every A. With p_k<=4 exp(A_0 sqrt(k))/(k!)^2, A_0=2sqrt(32), we obtain the rigorous lower bound

    E N_k^2/(E N_k)^2 >=
      [binomial(k,r)binomial(n-k,k-r)/binomial(n,k)]
      *(k!)^4/[16 exp(2A_0 sqrt(k)) ((2k-r)!)^2].

To compute its exponent, take k~a n^(1/3) and r~xk with fixed 0<x<1. For j<=k=o(sqrt(n)),

    log binomial(n,j)=j log n-log(j!)+O(k^2/n).

Indeed log((n)_j/n^j)=sum_{i=0}^{j-1}log(1-i/n), whose absolute value is at most 2sum_i i/n for sufficiently large n, using -log(1-t)<=2t on 0<=t<=1/2. The same estimate with n-k instead of n changes j log(n-k) from j log n by O(k^2/n). Stirling's formula, together with log n=3log k-3log a+o(1), therefore gives, for the logarithm of the displayed lower bound divided by k,

    [log of displayed lower bound]/k = J_a(x)+o(1), where
    J_a(x)=3x log a-x log x-2(1-x)log(1-x)
               -2(2-x)log(2-x)-3x.

The exp(2A_0 sqrt(k)) penalty disappears after division by k. At a=12/5 and x=4/5, direct simplification gives

    J_(12/5)(4/5)=[log(250000)-12]/5 >0.

Here is an exact sign verification without trusting floating logarithms. The exponential series gives e<11/4: for j>=3, j!>=6*3^(j-3), so its tail is at most (1/6)/(1-1/3)=1/4, with strict inequality because the j=4 inequality is strict. Also 11^12=3138428376721 <250000*4^12=4194304000000. Hence e^12<(11/4)^12<250000, proving log(250000)>12. Numerically J=0.08584323936887657, but positivity is proved exactly.

Thus for some eta>0 and all sufficiently large n, E N_k^2/(E N_k)^2>=exp(eta k). A valid choice is any eta less than [log(250000)-12]/5, for example half that value. This establishes the claimed obstruction. Large-overlap clustering cannot be ignored, even though two random k-subsets usually have very small intersection at this scale. A weighted count, a restricted family of candidate subsets, or another spatial method is required to overcome this specific second-moment barrier; none is proved here to do so.

The same obstruction holds for any fixed a>=12/5, since J_a(4/5) is increasing in log a. This includes K: the function exp(r)/r^(2/3) is minimized at r=2/3, and e>8/3 gives K>4^(2/3)>12/5 (the final comparison follows from 16>(12/5)^3). Thus the claim about failing to reach the upper constant does not depend on rounding its decimal.

## Final verification record

* Balanced-prefix enumeration gives all eight counts above; the independent strong-interval/orientation computation agrees through n=8 and additionally gives H_9=6606069, matching formal-series inversion. Individual orientation counts were independently brute-forced through n=5. The counts are stored in balanced_counts.json and substitution_check.json.
* Python and JavaScript integer formal-series inversion agree through n=16, including H_16=359311487783721; formal_series_check.json records the cross-check.
* The weighted-tree bound was checked against exact coefficients through n=100. The factorial merge inequality was checked for 1<=r,s<=79 and the factorial ratio bound for n<=149; their general proofs are above. Numerical evaluation of K agrees in Python and JavaScript.
* overlap_check.json checks the analytic second-moment lower bound for k=100,1000,10000,100000 with r=4k/5. Its normalized log is positive (0.0143434794) at the final k, approaching the proved limit J=0.08584323937 after the subexponential collision penalty is removed. These are O(k) arithmetic checks, not generation of the correspondingly large n point samples.
* The first Lean attempt failed because Boolean conjunction and equality were not parenthesized; Lean parsed a different, false proposition. The failure is preserved in collision_lean_failed.json. The corrected proposition passed ordinary decide and then the explicitly requested decide +kernel. The final command `lake env lean ~/brain_workers/TRIO_1011/op/P0216/CollisionTruth.lean`, from ~/lean_verify, exited 0 with empty diagnostics, one check at a time and a 3600-second timeout. Final SHA256 is 2ed24cc823e4adfc1023a15579c6a221c95dbcccd4c1c8626a6262c01ef6f055. The exact finite truth table alone is formalized; neither the modular-decomposition nor the asymptotic theorem is claimed Lean-checked. There is no sorry or native_decide.

Timing error: the original optional permutation enumeration had a time-budget check only between sizes. Its final n=9 level took 2685.76 seconds on this shared machine, exceeding the requested ten-minute command ceiling. This was a resource-control mistake. The maintained script now checks the 120-second budget within each size and discards incomplete totals. No further exhaustive enumeration was launched. The final Lean run took 1062.96 seconds including shared execution/slot time, within its separately requested one-hour timeout.

Final verdict: PARTIAL. The collision-rate subproblem, exact formal-series reduction, upper-mean bound K, and unweighted second-moment obstruction are proved. The full problem's mean-limit existence and constant remain unresolved. No novelty or solved-in-literature claim is made.
