# A birthday bound with explicit degree-ratio dependence

2026-10-11. This is a special case of G0012, not a solution of its full statement. No novelty assertion is made.

**Theorem.** Let G be a finite simple undirected graph with n vertices, minimum degree delta>=3, and maximum degree Delta. Put a=delta-2, b=Delta-2, R=b/a. Fix any directed edge e. If k is a positive integer and k^2>=784 n R^2, then

    P_e(the length-k NBW is simple) <= 800 n R^2/k^2.

Consequently, if R is bounded by a fixed R0, the Alon-Peres conclusion holds with C(epsilon,R0)=sqrt(800/epsilon)R0 for 0<epsilon<1. No connectedness assumption is necessary.

## 1. Plans reproduce the simple-path probability

At each vertex v, independently choose a uniform derangement pi_v of its d(v) neighbors. A derangement is a permutation without fixed points. A plan maps an incoming directed edge (u,v) to (v,pi_v(u)). This is a bijection of the finite directed-edge set: outgoing edges from v are distinct images of all incoming edges to v, and the blocks for distinct v are disjoint. Its iterates starting at e define a non-backtracking trajectory.

Let T be the finite set of all plans and S the subset whose first k edges are simple. The product of uniform local choices is uniform on T even at variable degrees. For any distinct neighbors u,w of v, symmetry by conjugation fixing u shows that the number r'_d of derangements with pi(u)=w is independent of w. If r_d is the number of all derangements, then r_d=(d-1)r'_d, so this prescribed transition has probability 1/(d-1).

A fixed simple path v_0,...,v_k imposes exactly one transition at each of the distinct vertices v_1,...,v_{k-1}. Independence gives probability product_{i=1}^{k-1}1/(d(v_i)-1), exactly its NBW probability. Summing over the disjoint simple-path events proves P_e(simple)=|S|/|T|. This does not identify the laws after self-intersection, nor is that needed.

If k>=n then S is empty, so assume k<n. Necessarily n>=4. The theorem's numerical hypothesis implies k>=56R, hence k>=2. Set

    L=ceil(48 n R/k).

Since nR/k>1, L<=49nR/k and L+1<=50nR/k. Thus k^2>=784nR^2 gives L<=k/(16R). In particular L>=1.

## 2. Raw deviations and disjoint directed-edge packing

For each rho in S with base vertices v_0,...,v_k, a raw deviation is a pair (i,c), where 1<=i<=k-1 and c is a neighbor of v_i different from v_{i-1} and v_{i+1}. Modify pi_{v_i} so it sends v_{i-1} to c; leave all other coordinates fixed. Until the first revisit to v_i, the unused values of the modified permutation cannot matter. A revisit is already a vertex collision. Thus whether the modified trajectory is simple through time i+L is independent of the chosen completion of this modified derangement. Call the raw deviation bad if it is not simple through that time.

The number W(rho) of raw deviations is sum_{i=1}^{k-1}(d(v_i)-2), so W(rho)>=(k-1)a>=ka/2. Let M=sum_{rho in S}W(rho).

Consider deviations that are simple through i+L and do not visit any base-path vertex during these L steps. Their length-L external directed-edge segments follow the original plan after the first edge. For a fixed base plan, distinct such segments cannot share a directed edge. To see this, follow the unique predecessor under the original bijection backwards from a hypothesized shared edge. Either one segment's first edge is reached strictly earlier, forcing the other segment to have visited its departure vertex on the base path, or both first edges are reached at once and the departure edge and vertex coincide. The latter forces the same raw deviation. The former contradicts non-returning. Therefore these segments are directed-edge disjoint, and their number is at most 2m/L, where m=|E|.

Since 2m<=nDelta<=3nb and L>=48nR/k, their number is at most ka/16<=W(rho)/8. This holds per base plan.

Among deviations that first return to the base path within L steps, those first returning at v_k number at most d(v_k)-1<=2b, per base plan. Indeed, each is specified by its directed final arrival edge at v_k. Following original-plan predecessors backwards until first encountering a base vertex uniquely determines its departure and initial changed edge. Simplicity before this first return suffices for this argument. Since k>=32R, 2b<=ka/16<=W(rho)/8.

Returns at v_0 or at/before the departure index are automatically bad. It remains to bound simple middle-returning deviations globally, as follows.

## 3. Excursion reversal: a global involution

It is enough to pair middle-returning raw deviations whose excursion has no repeated interior vertex; excursions with an interior repetition are automatically bad. This restriction makes the reversal's domain and validity explicit.

Take a raw deviation departing at v_i and first returning at v_l, 1<=l<=k-1, with excursion vertices v_i,x_1,...,x_{j-1},v_l and j<=L. The interior vertices are distinct and off the base path. At each interior vertex replace the original local derangement by its inverse, producing a new base plan tilde-rho. No base-path local coordinate changes, so tilde-rho is still in S with the same base trajectory. Now depart from v_l along the reversed final excursion edge, following the reversed excursion back to v_i.

The reversed departure is an allowed raw deviation. If j>1 its outgoing edge is external and cannot equal either adjacent base edge. If j=1 the chord cannot join consecutive base vertices: departure along the next base edge was excluded and departure along the preceding one was forbidden by non-backtracking. At an interior excursion vertex x, the original transition pi_x(previous)=next becomes pi_x^{-1}(next)=previous, giving exactly the reversed path. Applying this operation twice restores every plan coordinate and raw deviation. It is consequently an involution on the global set of middle-returning deviations with simple interiors, over all rho in S.

If l<=i, the original deviation repeats v_l on its already-traversed prefix and is bad. If l>i, the reversed deviation repeats v_i on its prefix and is bad. Hence in each involution pair at most one member is simple through its departure time plus L. The count is global, not per base plan. In particular simple middle-returning deviations number at most half of ALL raw deviations, namely M/2.

Combining the non-returning bound, the final-endpoint bound, and this global bound, the total number of simple raw deviations is at most M/8+M/8+M/2=3M/4. Thus at least M/4 raw deviations are bad.

Discard departure indices i>k-L. At most L indices are discarded per source, with at most b raw choices at each. The discarded total is at most |S|Lb<=|S|ka/16<=M/8. We therefore retain at least M/8>=|S|ka/16 early bad raw deviations. Each yields a target plan in T\S, because its collision happens by i+L<=k.

## 4. Conditional heat bath cancels completion multiplicities

For each retained raw deviation at degree d, give each target completion weight 1/r'_d, uniformly over the derangements satisfying the changed image. The total weight out of that raw deviation is one, so the total outgoing weight from S to T\S is at least |S|ka/16.

Fix a target plan tau in T\S and let j be its first vertex-collision time. Any source that leads to tau by an early bad deviation at i agrees with tau before departure, so i<j. Badness means j<=i+L. Thus j-L<=i<j, giving at most L+1 candidate indices (a deliberately loose bound). These prefixes are simple, and candidate departure vertices are distinct.

Fix such an index i and its incoming label u. The target image c is fixed by tau. Any source local derangement must have its image of u unequal to both u and c, giving d(v_i)-2 possibilities for its used image. Each used image has r'_{d(v_i)} completions. The source agrees with tau everywhere else. Consequently, summing over all possible simple sources at this index gives incoming weight at most

    (d(v_i)-2) r'_{d(v_i)} / r'_{d(v_i)} <= b.

This includes only an upper bound: some of these potential sources may fail to be simple or early bad. No factorial dependence remains. A fixed target receives weight at most (L+1)b. Double counting gives

    |S|ka/16 <= |T\S|(L+1)b.

Divide by |T|ka/16 and use |T\S|<=|T| to get

    |S|/|T| <= 16R(L+1)/k <= 800 n R^2/k^2.

Section 1 identifies this with the required NBW simple-path probability, completing the special-case proof.

## 5. Expected collision-time corollary

Let tau be the first repeated-vertex time, with the first prescribed edge at time 1. Then P(tau>k) is exactly the length-k simplicity probability. Put A=800 n R^2 and B=ceil(sqrt(A)). For k>=B the theorem applies. Using tau<=n and the tail-sum identity,

    E(tau) <= B+1 + A sum_{k=B+1}^infinity 1/k^2
           <= B+1 + A/B
           <= 2 sqrt(800) R sqrt(n)+2.

The series bound follows by comparison with the integral of x^(-2) from B to infinity. Thus graphs with fixed degree ratio also satisfy the expected-time version without the logarithmic loss. No novelty is asserted for this corollary.

## 6. Precise unrestricted gap

R may be as large as n-3 when delta=3; the displayed bound then has no information before the trivial k>=n threshold. The packing proof uses the total directed-edge count and loses a degree ratio when comparing it with deviations along the base path. The incoming and late-departure bounds lose another ratio. No degree-independent replacement for these comparisons was proved. Earlier biregular work can exploit alternating degrees to cancel those ratios, but arbitrary graphs lack that structure. No counterexample to G0012 is obtained here.
