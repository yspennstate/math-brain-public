# D0040 — transport route: universal weak two-level coupling

Date: 2026-10-12. This pursues the boundary case of the second approach recorded in SECOND_ATTEMPT.md. No novelty claim is made. A two-level coupling allowing a zero offdiagonal is strictly weaker than the positive-offdiagonal all-level Jacobi/Favard construction required for the full problem.

## Exact theorem

Let μ be a probability measure on R and β>0. Assume

    0<Z=∫∫|u−v|^β μ(du)μ(dv)<∞.

Sample an ordered pair L<U with law obtained by tilting μ⊗μ by |u−v|^β/Z and sorting. Then there exists a coupling with X~μ and L≤X≤U almost surely. Consequently

    M=[[X, sqrt((X−L)(U−X))],
       [sqrt((X−L)(U−X)), L+U−X]]

is a real symmetric tridiagonal two-by-two random matrix whose eigenvalues have exactly the two-point beta-ensemble law, while its leading one-by-one minor has the one-point law μ. The offdiagonal is nonnegative, and strict positivity is NOT asserted.

In particular this applies to μ(dx) proportional to exp(−βx⁴)dx, for every β>0. It gives an arbitrary-weight coupling at sizes one and two, despite the failure of the canonical Dirichlet-weight model. It does not give a common measure for all sizes.

## Interval capacity lemma — complete proof

Let I be any interval, possibly unbounded, and let p=μ(I). If p=0 or p=1, P(L,U∈I)≤p is immediate. Suppose 0<p<1. Define

    C=E[|A−B|^β], A,B independent with law μ conditioned on I;
    H=E[|A−Y|^β], A~μ|I, Y~μ|I^c independently;
    G=E[|Y−Y'|^β], Y,Y' independent with law μ|I^c.

These are finite since their positive coefficients p²,2p(1−p),(1−p)² in Z are nonzero and Z<∞. For a,b∈I and y∉I, the interval property gives

    |a−b|≤max(|a−y|,|b−y|),
    |a−b|^β≤|a−y|^β+|b−y|^β.

After averaging, C≤2H. Thus

    Z=p²C+2p(1−p)H+(1−p)²G≥p²C+p(1−p)C=pC.

The tilted pair lies in I with probability p²C/Z≤p. Sorting does not change this event. This proves the interval lemma for every β>0, without convexity of the power function and without assumptions on μ beyond Z.

## Closed-set capacities

For any closed F⊂R, its open complement is a countable disjoint union of interval components I_j. A connected interval [L,U] avoids F if and only if its two endpoints belong to the same component I_j. These events are disjoint. Therefore the interval lemma gives

    P([L,U]∩F=∅)=Σ_j P(L,U∈I_j)≤Σ_j μ(I_j)=μ(F^c),

or

    μ(F)≤P([L,U]∩F≠∅).

The hit event is Borel. In fact the set of endpoint pairs whose interval meets a fixed closed F is closed: for converging endpoint pairs, a sequence of witnessing points is bounded, has a convergent subsequence, and its limit remains in F and between the limiting endpoints.

This is the Strassen/Artstein selection capacity condition. The next section proves sufficiency in the specific setting directly, so no unverified variant of a selection theorem is needed.

## Sufficiency by finite weighted Hall matching and a tight limit

Write ν for the ordered-pair law. For each positive integer m, partition R into finitely many half-open bounded intervals of diameter at most 1/m covering [−m,m), and two tail intervals. Denote the disjoint Borel cells by A_i. Let a_i=μ(A_i), and define, for each endpoint pair, its hit pattern

    S(L,U)={i : [L,U]∩closure(A_i)≠∅}.

There are finitely many possible patterns S. Set b_S=ν(S(L,U)=S). For any subset T of cell indices,

    Σ_{i∈T}a_i ≤ μ(∪_{i∈T}closure(A_i))
                 ≤ ν([L,U] hits ∪_{i∈T}closure(A_i))
                 =Σ_{S:S∩T≠∅}b_S.

The union of finitely many closed cell closures is closed, including tail closures, so the previously proved capacity inequality applies. No nonatomicity or zero-boundary-mass assumption is needed.

**Finite weighted matching step, with proof.** These inequalities imply there are numbers f_{iS}≥0, zero unless i∈S, with row sums a_i and column sums b_S. Form a finite directed network: source-to-i capacities a_i, i-to-S capacities 2 when i∈S, and S-to-sink capacities b_S. Feasible flows form a nonempty compact subset of a finite Euclidean space; hence a maximum flow exists. If its value is less than one, there can be no residual source-to-sink path, because augmenting by the minimum positive residual capacity along such a finite path would increase its value. Let V be the vertices reachable from the source in the residual graph. The sink is not in V. Let T be the cell vertices in V. Any i∈T has all neighboring S vertices in V: an i-to-S arc of capacity 2 cannot be saturated, since its flow is at most the total source flow, which is at most one. Across the cut (V,V^c), forward arcs are saturated and backward arcs carry zero flow, by residual reachability. Flow conservation therefore makes the flow value equal to the cut capacity. That capacity is at least

    Σ_{i∉T}a_i+Σ_{S:S∩T≠∅}b_S
       ≥1−Σ_{i∈T}a_i+Σ_{i∈T}a_i=1,

a contradiction. Thus a unit flow exists. All source and sink arcs are saturated because their capacities each sum to one. Its middle-arc flows are the required f_{iS}.

Discard zero-mass cells or patterns when taking conditional probabilities. Define a coupling π_m of X and (L,U) by giving component (i,S) weight f_{iS}, and within that component taking independently X~μ conditioned on A_i and (L,U)~ν conditioned on hit pattern S. Its marginal laws are μ and ν by the row and column sums.

If X belongs to a bounded cell, that cell's closure intersects [L,U], so

    d(X,L,U):=max(L−X,X−U,0)≤1/m.

Only target-tail cells can violate this bound. Hence for every ε>0 and all m with 1/m<ε,

    π_m(d>ε)≤μ(R\[−m,m))→0.

The family of π_m is tight: choose compact sets with large μ and ν masses; their Cartesian product misses at most the sum of the two marginal tail probabilities, uniformly in m. By the standard Prokhorov compactness theorem on the Polish space R³, a subsequence converges weakly to a probability law π. Its marginals remain μ and ν, as follows by testing bounded continuous functions of the respective coordinates.

The function d is continuous, so {d>ε} is open. Portmanteau gives

    π(d>ε)≤liminf π_m(d>ε)=0.

Using ε=1/k, k≥1, yields π(d>0)=0. Thus L≤X≤U under π. This proves the required selection coupling. The only infinite-dimensional compactness input is the standard Prokhorov theorem, whose tightness and Polish-space hypotheses have been checked.

## Matrix realization and quartic application

The chosen offdiagonal is real because (X−L)(U−X)≥0. The matrix's trace is L+U and its determinant is

    X(L+U−X)−(X−L)(U−X)=LU.

Thus its characteristic polynomial is (z−L)(z−U), and its eigenvalues are exactly the prescribed ordered pair. Its leading one-by-one minor is X~μ.

For μ(dx)=c_β exp(−βx⁴)dx, normalization is finite and positive and every absolute moment is finite. The inequality |u−v|^β≤2^β(|u|^β+|v|^β) shows Z<∞; positivity follows because μ is not concentrated at one point. The sorted tilted pair has density proportional to (U−L)^β exp(−β(L⁴+U⁴)), exactly the intended two-point quartic law. Therefore the theorem applies for every β>0.

## Referee checks and exact remaining gaps

* The interval distance bound is valid also for 0<β<1; it uses monotonicity, not convexity.
* Closed-set capacity is proved for arbitrary closed sets by their interval complement components, not merely for half-lines or single intervals.
* The finite flow argument uses real capacities and an attained maximum, so it does not assume a terminating integer-capacity augmenting algorithm.
* The approximate couplings have EXACT marginal laws; only the interval-support constraint is approximated before the tight limit.
* The Portmanteau direction is π(open)≤liminf π_m(open), which is the direction needed here.
* The limit may put mass on X=L or X=U. No argument above excludes that. Thus strict positivity of the offdiagonal remains unproved by this method.
* Nothing constructs level three or imposes the positive three-term recurrence across three successive characteristic polynomials. Extending a weak two-level coupling to the source's single infinite Jacobi matrix remains a separate problem.

This is a proved weak two-level special case, not a solution of D0040. For the quartic model the next precise questions are whether an interior selector can be obtained and whether a compatible size-three recurrence coupling exists.
