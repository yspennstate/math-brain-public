# I0022 — serious second attempt, 2026-10-11

## The gap being attacked

The first pass established positive long-dendron limits only under complete condensation and excluded nontrivial compact GH scaling limits in a regularly varying class. It did not determine whether arbitrary weights with ν<1 can have a full-sequence nontrivial limit even in the weaker sampling-distance topology. Incomplete condensation alone is not a proof of failure of a limit.

## Two approaches not tried in the first pass

1. **Explicit sparse zero-radius weights with competing skeletons.** Force a one-hub star at sizes n=k+1 and a two-hub double star at n=2k+1, with k growing through a sparse support. Prove dominance using the full number of ordered trees, not just the maximum weight. The two limiting pair-distance laws have different shapes; a scalar cannot match a point mass and a two-atom law. This targets a universal full-sequence sampling-limit assertion directly and needs no asymptotic branching theorem.
2. **A finite-hub reduction to metric-measure skeletons.** Assume finitely many large-degree vertices with converging inter-hub distances and empirical attached-forest size/height distributions. Show by a truncation/collision argument that uniform sampled vertices fall in different small attached components; the distance array then comes from the skeleton plus independent arms. This would extend the complete-condensation theorem to a multiple-condensation special case, but does not ensure convergence of the skeleton for arbitrary weights.

Approach 1 is selected because its entire dominance estimate is explicit and can produce a counterexample to the full-sequence conjecture. Approach 2 is useful if the counterexample fails, or as a description of its subsequential limits.

## Brain consulted for the gap

- math_recall.py query: `Janson incomplete condensation large degree skeleton dendron tree limits Example 19.37`.
- brain.py recall query: `incomplete condensation sampling limit dendron mistakes`.

The math store suggests sparse cubic spikes and two-condensate constructions in earlier Janson problems. The memory recall warns that a past zero-radius maximum-weight argument omitted an order-n mixing entropy. No stored dendron result was found. Here the proposed proof will explicitly bound the contribution of **all** non-target ordered trees by 4^(n−1) times their maximum weight, so the entropy is retained. Brain results are hints, not proof inputs.

## Initial construction to audit

Set w_0=w_1=1, w_{3^j}=2^((3^j)^3) for j≥1, and all other weights zero. The base 2 permits exact integer computations. Then ρ=ν=0, and the unary path has positive weight for every n. For k=3^j the next support degree is 3k, unavailable at either n=k+1 or n=2k+1. Every smaller positive degree is ≤k/3. The degree budget is Σ_v d^+(v)=n−1. Expected outcome: stars at the first sequence and double stars at the second. This is not yet marked proved pending the full counting and scaling audit below.

## Theorem C: explicit incompatible condensation subsequences

For these fixed weights, every size n is admissible, ν=0<1, and, for k=3^j,

- T_{k+1} is a rooted star with k leaves with probability tending to one.
- T_{2k+1}, considered as an unrooted graph, is the double star consisting of two adjacent hubs with k−1 leaves at one hub and k leaves at the other, with probability tending to one.

More precisely, for q∈{1,2}, the probability of failure is at most

    4^(qk) 2^(−8k³/9).

This theorem and its proof are independent of the recalled brain claims.

### Proof

The path with n vertices has only degrees 0 and 1 and weight one, so the partition function Z_n is positive for every n. It is finite because there are finitely many ordered trees of size n and each relevant weight is finite. Along d=3^j,

    w_d^(1/d)=2^(d²)→∞.

Thus Φ has radius of convergence ρ=0, and Janson's convention gives ν=0. The hypotheses w_0>0 and w_d>0 for a d≥2 hold.

Fix q∈{1,2}, n=qk+1, and a tree of positive weight. Counting edges by their parent gives Σ_v d^+(v)=n−1=qk. No degree can exceed this budget, so the next supported degree 3k is unavailable. Let H be the number of vertices of degree k. Then H≤q. Every other positive supported degree d is ≤k/3. Define its binary log-weight E=log_2 W(t). Vertices of degrees 0 and 1 contribute zero, and every other vertex contributes d³. Since 0≤d≤k/3 implies d³≤(k²/9)d, we obtain

    E ≤ H k³ + (k²/9)(qk−Hk)
      = H k³ + (q−H)k³/9.

If H<q, the right side is at most qk³−8k³/9. This calculation retains the budget of **all** non-maximal degrees, including the unary vertices; no multiplicity or entropy is omitted.

If H=q, those q vertices use the entire degree budget. Every other vertex must be a leaf. For q=1 the root must be the hub, and the only tree is the k-leaf star. For q=2 the root is one hub; any other non-root hub must be adjacent to it, because there are no other non-leaves to lie on the connecting path. The first hub has the second hub as one of its k ordered children and k−1 leaf children; the second has k leaf children. There are exactly k rooted ordered target trees, one for each position of the internal child. They all have the same graph metric. Their weights are respectively 2^(k³) and 2^(2k³).

The number of rooted ordered trees on n vertices is at most 4^(n−1). Here is an injection proving this bound: traverse the tree from the root in child order, write 1 when going down an edge and 0 when returning along it, and recover the tree by the usual stack reconstruction. Each edge contributes two symbols, so the injective code has length 2(n−1), giving at most 2^(2n−2) possibilities.

Consequently the total weight of all non-target trees is at most

    4^(qk) 2^(qk³−8k³/9).

The partition function is at least the weight 2^(qk³) of a single target tree, so division gives the stated probability bound. Since q is fixed and 8k³/9−2qk→∞, the bound tends to zero. This proves all assertions. □

## Theorem D: no nontrivial full-sequence metric sampling limit, even with random scalar scales

Give T_n graph distance d_n and uniform probability measure on its vertices. Let A_n be any finite nonnegative random scalar determined by T_n and possibly auxiliary randomness, but chosen before sampling the vertices. Conditional on T_n and A_n, let V_{n,1},V_{n,2},… be independent uniform vertices. Define

    D^{(n)}_{ij}=A_n d_n(V_{n,i},V_{n,j}).

If for every fixed r the r×r distance arrays converge in distribution along the full size sequence to finite-valued arrays, then all off-diagonal distances in the limit equal zero almost surely. In particular **no deterministic scalar rescaling, and no tree-dependent random scalar rescaling, has a nontrivial full-sequence sampling-distance limit** for these weights.

“Nontrivial” here means P(D_12>0)>0. This is a necessary notion of nontriviality for the measured CRT, stable trees and long dendrons when viewed by iid sampled distances. The theorem allows joint random-tree limits, rather than requiring a deterministic limiting distance law.

### Proof by three sampled vertices

It suffices initially to consider the three off-diagonal entries (x,y,z)=(D_12,D_13,D_23). On [0,∞)^3 define the bounded continuous function

    g(x,y,z)=(max{x,y,z}−min{x,y,z})/(1+max{x,y,z}).

This function takes values in [0,1]. It vanishes precisely on equilateral triples.

On the star subsequence n=k+1, conditional on the target event and on any scalar A_n, the probability that the three iid vertices are distinct leaves is

    k(k−1)(k−2)/(k+1)³→1.

On that event the distance triple is (2A_n,2A_n,2A_n), so g=0. Thus, regardless of how A_n varies or depends on the tree,

    E g(D^{(k+1)}_12,D^{(k+1)}_13,D^{(k+1)}_23)→0.

If the full-sequence triple laws converge to a finite-valued probability law Λ, bounded-continuous convergence gives ∫g dΛ=0. In particular the expectations of g also tend to zero on the double-star subsequence n=2k+1.

On a target double star let L=k−1 and R=k be its two leaf-group sizes. The conditional probability that the three samples are distinct leaves and use both groups is

    p_k=[(L+R)(L+R−1)(L+R−2)
          −L(L−1)(L−2)−R(R−1)(R−2)]/(2k+1)³
       =3LR(L+R−2)/(2k+1)³→3/4.

These samples have unscaled distance triple (2,3,3) in some order. Therefore g=A_n/(1+3A_n) on this event. Since the samples are uniform conditional on the tree and its scale, and the leaf-group counts are identical for every ordered target tree, p_k does not depend on A_n. Writing G_n for the double-star target event, we get the rigorous lower bound

    E g(D^{(n)}_12,D^{(n)}_13,D^{(n)}_23)
      ≥p_k E[1_{G_n} A_n/(1+3A_n)],   n=2k+1.

The left side tends to zero and p_k→3/4. For each ε>0, the function a/(1+3a) is increasing on [0,∞) and at least ε/(1+3ε) when a≥ε. Hence

    P(G_n and A_n≥ε)
      ≤(1+3ε)/ε · E[1_{G_n} A_n/(1+3A_n)]→0.

As P(G_n^c)→0 by Theorem C, A_{2k+1}→0 in probability. On G_n every unscaled graph distance is at most 3, so for any r and ε>0,

    P(max_{i,j≤r}D^{(2k+1)}_{ij}>ε)
      ≤P(G_n^c)+P(A_{2k+1}>ε/3)→0.

Thus every finite array tends to the zero array along this subsequence. Any full-sequence limit must have that same law. This proves the theorem. □

The scalar is allowed to be random and depend arbitrarily on the ordered tree, but not to be chosen after seeing the sampled vertices. This restriction is intrinsic to sampling a rescaled metric space: one metric must be fixed before taking iid samples. Finite-valued weak limits are required, as for the CRT, stable trees and long dendrons; a putative “limit at infinite distance” is outside this claim.

## An elementary deterministic-scaling check

Along the star sequence the unscaled pair distance converges to the point mass δ_2. Along the double-star sequence it converges to (δ_2+δ_3)/2. For deterministic a_n, a full-sequence positive finite pair limit would have to be δ_r for some r>0 along stars. Tightness along double stars supplies a convergent subsequence of their scale factors, b_j→b≥0. Its pair limit is (δ_{2b}+δ_{3b})/2. Equality to δ_r would force 2b=3b=r, hence r=0, a contradiction. This corroborates the three-point proof. The three-point argument is stronger because random scales can disguise the two-point marginals.

## Subsequence objects: approach 2 applied to this example

At unit edge scale, the star sequence converges in the sampling-distance sense to the unit-arm long dendron: all off-diagonal distances are 2. The double-star sequence converges to a long dendron with base interval [0,1] and probability measure assigning mass 1/2 to each of (0,1) and (1,1) in base×arm coordinates. Its samples have an iid Bernoulli endpoint label B_i and arm length 1, giving

    D_ii=0;   D_ij=2+|B_i−B_j| for i≠j.

To prove the full finite-array statement, fix r. The probability any sampled vertex is a hub is at most 2r/(2k+1). The probability that any pair coincides is at most r(r−1)/(2(2k+1)). Both vanish. Conditional on being leaves, the samples are iid labels with probabilities (k−1)/(2k−1) and k/(2k−1), which tend to 1/2. On distinct-leaf events the above distance formula is exact. Coupling the labels to iid fair labels and taking a union bound proves convergence for every r. The analogous star proof uses the same hub/collision bounds with one hub.

Thus the obstruction is not absence of any subsequential object: it is incompatible skeletons along different sizes. This gives a fully proved two-hub special case of the second approach, without claiming a general finite-hub theorem.

## Current checked scope

Theorems C and D are complete proofs of a counterexample to an unrestricted **full-sequence nontrivial metric sampling-limit assertion** for all ν<1 weights. They do not claim that no topology-unspecified “some kind” of limiting object can ever be defined. They also do not settle the separate problem restricted to 0<ν<1, because the construction has ν=0, explicitly allowed in Janson's question.

## Corollary E: the compact metric-space interpretation also has only a trivial full-sequence limit

For the same weights and any tree-dependent random scalar A_n≥0, if A_n T_n converges in distribution along all n in compact GH topology, its limit is the one-point space. A zero scalar is interpreted as the one-point metric quotient.

Proof. Weak convergence in the Polish GH space implies tightness. Fix ε>0 and a compact family K. By the uniform covering property proved in ATTEMPT.md, all members of K have an ε/2-ball covering number bounded by some C(K,ε/2). On the k-leaf star event and A_{k+1}≥ε, its k leaves are at pairwise distance at least 2ε, so each ε/2-ball covers at most one leaf. For k>C(K,ε/2) this event excludes membership in K. For any δ>0 choose a tightness compact K carrying probability at least 1−δ for every star-subsequence index. Then

    limsup_j P(A_{3^j+1}≥ε) ≤δ,

because the non-star event tends to zero. Let δ↓0. Thus A_{k+1}→0 in probability. On the target event the star has diameter 2A_{k+1}, so its GH distance to the singleton tends to zero; the non-target event has vanishing probability. The star subsequence converges to the singleton. A full-sequence weak limit must have that same law. □

This corollary does not depend on convergence of the uniform vertex measure, and applies also to geometric realizations with unit-length edges: diameters and separated leaves are unchanged.

## Hostile-referee checklist and verification

1. **One fixed sequence of weights, not n-dependent weights:** w_d is defined once for every degree. Both size subsequences use it unchanged; k+1 and 2k+1 are disjoint when k runs through powers of 3.
2. **Admissibility and source hypotheses:** w_0=w_1=1 gives all n positive partition functions and span one. The weights have zero radius, so ν=0<1 under the exact source convention. No equivalent subcritical Galton–Watson law is asserted.
3. **Missing entropy:** all non-target trees, not just one maximum-weight competitor, are counted by the injective length-2(n−1) traversal code. The error bound has exponent 2qk−8k³/9, which tends to −∞.
4. **Degrees versus undirected graph valences:** each hub has outdegree k; the lower hub has undirected degree k+1 because it also has a parent. The leaf counts are k−1 and k, not k and k. The root cannot be a unary vertex in a target tree since the hubs consume the entire degree budget.
5. **Scaling scope:** random tree-dependent scalars are allowed. The bounded continuous statistic g avoids an invalid discontinuous “equilateral indicator” argument at zero. The conditional independence of subsequent vertex sampling is explicitly used to factor the mixed-leaf probability p_k. All finite limits are required to have finite distances.
6. **What collapse means:** Theorem D proves only sampling collapse, which may ignore zero-mass geometry. Corollary E separately rules out a nontrivial compact GH full-sequence limit, without making a metric-measure assumption.
7. **Exact numerical checks:** sparse_exact_checks.py checks the partition coefficient formula against an independently implemented ordered-tree recursion for n=1,…,13. It computes exact partition functions at n=4,7,10,19,28,55 and exhausts every feasible nonzero-degree count pattern at those sizes. The bad-event bounds pass in exact rational arithmetic. Floating-point displays at n=28,55 underflow to zero; the output explicitly records that the exact probabilities are positive and records numerator/denominator bit lengths. No zero-probability conclusion is drawn from underflow.
8. **Independent graph and tree enumeration:** sparse_graph_checks.py enumerates all 5, 132 and 4,862 ordered trees of sizes 4,7,10, checks exact target counts 1,3,1 and weighted partition functions, and independently constructs the double-star graphs. BFS pair-distance counts and enumeration of every ordered distinct-leaf triple at k=3,9,27 agree with the formulas. Each numerical job ran in under a second of measured Python computation and used tiny memory.
9. **Lean:** SparseChecks.lean proves lower_degree_cube, energy_gap, mixed_triple_count and scaling_cannot_match. `lake env lean ~/brain_workers/TRIO_1011/op/I0022/SparseChecks.lean`, run from ~/lean_verify, passed with exit_code=0 in 49.80 seconds. Only narrow Real, Linarith and Ring imports are used; no sorry or native_decide. These algebraic steps are kernel-checked; the probabilistic weak-convergence argument remains the written proof above.
10. **Prior art and novelty:** sparse spikes and multiple condensation are already present in Janson and the brain's neighbouring-problem notes. No novelty claim is made for the idea. The results recorded here are the explicit weighted-tree counting proof and the random-scalar sampling obstruction; no memory claim is used as an axiom.

## Final assessment and precise remaining gap

The first pass's gap concerning a possible universal full-sequence scalar metric limit is now answered negatively: the above admissible ν=0 example admits only trivial full-sequence sampling limits, even under random scalar scales. Thus the statement “every ν<1 weight sequence has a nontrivial metric sampling limit after suitable scalar scaling” is false, and the standard compact GH interpretation is false as well.

The original Problem 20.11 literally asks for “some kind” of object without specifying topology, admissible changes of representation, or whether subsequential limits suffice. The counterexample does not forbid a size-dependent family of limits, a subsequential theory, nonscalar/decorated representations, or positive-radius classifications. The surviving mathematical questions are to describe incomplete-condensation skeleton limits for **0<ν<1**, and to give an appropriate general subsequential or representation-dependent limit theory. Those are not proved here.

For the original topology-unspecified question, retain the conservative **VERDICT: PARTIAL**, with the precise universal scalar metric formulation now rigorously refuted. This is substantially stronger than the first pass and is not an assertion that Janson's general question is solved in every interpretation.
