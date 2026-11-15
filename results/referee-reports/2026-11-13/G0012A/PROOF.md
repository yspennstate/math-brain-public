# A bounded-degree-ratio extension

This is a partial result toward Dozier's Conjecture 1.5. It adapts his plans and excursion reversal, with weighted departures and randomized replacement of a local derangement. It does not establish a constant uniform over all degree ratios.

**Theorem A.** Let G be a finite simple undirected graph with n vertices, minimum degree m >= 3, and maximum degree M. Put Q=M/(m-1). For every directed starting edge delta and integer k>=1,

\[
 p_k(\delta):=\Pr(\text{the length-}k\text{ NBW from }\delta\text{ is vertex-simple})
 \leq \min\{1,256Q(1+Q)n/k^2\}.
\]

The NBW chooses uniformly among all neighbors other than the preceding vertex. Length counts edges and includes delta. If k>=n, the probability is zero.

Consequently, for 0<epsilon<1:

* If M/m<=D, one may take C(epsilon,D)=32D/sqrt(epsilon).
* If m>=3 and M<=Delta, one may take C(epsilon,Delta)=8 sqrt(Delta(Delta+2)/epsilon).

These constants are not optimized. In particular the first result is uniform over the absolute degree, including regular graphs of degree growing with n.

## 1. Product measure on plans

At each vertex v, independently choose a uniformly random derangement pi_v of its neighbor set N(v). An incoming edge (u,v) is followed by (v,pi_v(u)). The resulting map phi on directed edges is a permutation: at each v its incoming edges map bijectively onto its outgoing edges. Write mu for the product measure on plans with fixed start delta, and S for those whose first k edges form a vertex-simple path x_0,...,x_k.

Let R_d be the number of derangements of d objects. For distinct a,b in N(v), exactly R_d/(d-1) derangements send a to b. This follows by conjugating by permutations fixing a, which acts transitively on the possible b. Thus every specified simple path has mu-probability

\[
 \prod_{i=1}^{k-1}\frac1{d(x_i)-1}.
\]

The constraints concern distinct vertices and so are independent. This is also exactly its NBW probability. Summing over the simple paths proves mu(S)=p_k(delta). We do not identify the plan walk with the NBW after its first repeated vertex; that identification would be false in general.

## 2. Departures and certificates

For a plan rho in S, a departure is a pair (i,beta) where 1<=i<=k-1 and beta=(x_i,z) is an outgoing edge other than (x_i,x_{i-1}) and (x_i,x_{i+1}). Assign this departure weight

\[
 w_i=1/(d(x_i)-1).
\]

Its total weight, for a fixed rho, is

\[
 T(rho)=\sum_{i=1}^{k-1}\frac{d(x_i)-2}{d(x_i)-1}\geq(k-1)/2.
\]

Take an integer L>=1. Follow beta and thereafter the original plan, stopping at the first return to P={x_0,...,x_k}, or after L edges after departure, whichever comes first. At vertices outside P this trajectory uses only the original local derangements. Thus it is independent of how the local derangement at x_i is replaced, provided the replacement sends x_{i-1} to z.

A departure is **certified bad** if the original prefix x_0,...,x_i followed by this stopped trajectory repeats a vertex. This includes an internal repeat along the excursion, a return to x_i, and a return to any earlier vertex of the prefix. The certificate occurs by time i+L and holds for every such replacement of the departure derangement. Departures that return to a later point of P without a repeat before that return are not certified, even if a repeat could occur subsequently.

We bound the average weight of certified bad departures.

### Non-returning departures

Consider departures that do not return to P in their first L edges and have no certificate. Their L-edge pieces use distinct directed edges. Pieces from distinct departures have disjoint directed-edge sets. Indeed, if two pieces met at a directed edge, apply the inverse permutation phi backwards along both pieces. The two backwards sequences agree until one reaches its first edge. If the other has not reached its first edge, it must have passed through the tail of that first edge, a vertex of P, contradicting non-return. If both reach their first edges together, the departure location and outgoing edge coincide, so these are the same departure.

There are at most sum_v d(v)<=nM directed edges. Hence there are at most nM/L such departures, and their total weight U(rho) is at most

\[
 U(rho)\leq\frac{nM}{(m-1)L}=Qn/L. \tag{1}
\]

### Returns to the terminal vertex

At most d(x_k) departures can first return to P at x_k. To see this, associate a returning departure to its last directed edge into x_k. Given that edge, trace the original permutation backwards outside P. It determines uniquely the excursion back to its departure tail on P. Thus distinct departures have distinct final incoming edges. Their total weight E(rho) is bounded by

\[
 E(rho)\leq M/(m-1)=Q. \tag{2}
\]

This bound counts all such returns, including those already certified bad. Their exclusion only weakens the estimate.

### Returns to the initial or an interior vertex

A first return to x_0 is always certified bad. For a first return to x_l with 1<=l<=k-1, reverse the excursion as follows. Invert pi_v at every vertex of the excursion outside P; leave all local permutations on P and off the excursion unchanged. Call the resulting base plan rho_tilde. It has the same main simple path P, so still belongs to S. The reversed departure is at x_l, along the reverse of the last edge of the original excursion.

This is an allowed departure. Its first outgoing edge cannot be the reverse of the preceding main-path edge, or the next main-path edge: otherwise the last edge of the original excursion comes from a main-path neighbor of x_l, so it would have hit P before its final step. In the one-edge excursion case these two exceptions would respectively force the original departure to follow the main path or to backtrack, both excluded.

At every exterior vertex, inverting pi_v reverses the transitions: if pi_v(a)=b, then pi_v^{-1}(b)=a. This remains true if the excursion visits an exterior vertex more than once. A returning excursion cannot repeat a directed edge before returning, because outside P the routing is deterministic and such a repetition would trap it in a cycle forever. Therefore the construction follows the entire excursion backwards and first returns to P at x_i, in the same number of edges, at most L. Applying the construction twice restores rho and the original departure. It is an involution on interior-returning triples (rho,i,beta).

At least one member of every involution pair is certified bad. If the excursion itself repeats a vertex, both are certified. Otherwise, when l<=i the original departure hits its visited prefix, while when l>i the reversed departure hits its visited prefix.

The two triples have the same mu-mass on their base plans: mu is uniform on all plans, and inversion preserves the local derangement spaces. Their departure weights have ratio

\[
 \frac{w_i}{w_l}=\frac{d(x_l)-1}{d(x_i)-1}\in[1/Q,Q], \tag{3}
\]

where the actual maximal ratio (M-1)/(m-1) is even smaller. Fixed points of the involution are necessarily certified bad. Thus the weighted mass of non-certified interior returns is at most Q times the weighted mass of certified interior returns. This assertion holds after summing over all rho in S, rather than separately for each rho. No invariance of the departure weights is assumed.

Let B be the mean certified-bad weight, averaged over rho conditioned on S. If S is empty the theorem already holds. Partition all departures into certified bad, non-certified non-returns, terminal returns, and non-certified interior returns. Initial returns are certified bad. Equations (1)-(3) give

\[
 (1+Q) B\geq\frac{k-1}{2}-\frac{Qn}{L}-Q. \tag{4}
\]

## 3. A resampling flow and its congestion

Keep only certified bad departures at indices i<=k-L. Deleting the other indices removes at most L in departure weight for every rho, since the weight of all departures at any one index is less than 1. Write B_0 for the remaining conditional mean weight. Thus B_0>=B-L.

From a retained triple (rho,i,beta=(x_i,z)), choose uniformly a replacement derangement sigma at x_i satisfying sigma(x_{i-1})=z. Leave all other local derangements unchanged to produce a plan psi. Every resulting psi has a repeated vertex by time i+L<=k, by its certificate.

Send mass mu(rho) w_i, distributed uniformly over these replacements. If d=d(x_i), there are R'_d=R_d/(d-1) possible replacements. For each resulting ordered pair (rho,psi), the flow mass is

\[
 \frac{\mu(rho)}{(d-1)R'_d}=\frac{\mu(rho)}{R_d}. \tag{5}
\]

Fix an output plan psi and let j be the first edge index at which its walk repeats a vertex. An incoming source that deviates at i agrees with psi through edge i, so i<j. The certificate gives j<=i+L. Hence

\[
 j-L\leq i\leq j-1,
\]

at most L possible indices. For a specified such i, the departure vertex and incoming edge are known from psi's prefix. Its outgoing beta is also known. The source plan can differ from psi only in its local derangement at this vertex, with at most R_d choices. All these sources have mu(rho)=mu(psi), since the whole plan space carries uniform measure (the number of local choices may depend on v but is fixed for that vertex). By (5), their total contribution is at most mu(psi). Restricting to simple sources and certified departures reduces it. Thus the total incoming mass at psi is at most L mu(psi).

Summing gives

\[
 p_k(delta) B_0\leq L\mu(S^c)\leq L. \tag{6}
\]

This resampling is why no factor R_M appears. A deterministic choice of a distinguished replacement, followed by unweighted preimage counting, loses this cancellation.

## 4. Constants, including integer endpoints

It suffices to consider 1<=k<n and k^2>=256Q(1+Q)n; otherwise the claimed upper bound is 1. Set A=1+Q and

\[
 L=\left\lceil16Qn/k\right\rceil.
\]

The assumption gives 16Qn/k<=k/(16A). Also n>k implies k>256QA, and hence k>=16A. Consequently

\[
 L\leq16Qn/k+1\leq k/(8A).
\]

In particular L<k. By (4), Qn/L<=k/16 and Q<=k/16. Since k>=4,

\[
 B\geq\frac{(k-1)/2-k/16-k/16}{A}\geq k/(4A).
\]

It follows that B_0>=k/(8A). Equation (6) then implies

\[
 p_k(delta)\leq\frac{8AL}{k}
 \leq\frac{128AQn}{k^2}+\frac{8A}{k}
 \leq\frac{136AQn}{k^2}
 \leq\frac{256AQn}{k^2},
\]

using k<n and Q>=1 in the penultimate inequality. This proves Theorem A.

If M/m<=D, then Q<=3D/2, so 256Q(1+Q)<=960D^2<1024D^2. The first stated C follows. If M<=Delta and m>=3, Q<=Delta/2, so 256Q(1+Q)<=64Delta(Delta+2), proving the second. For epsilon>=1 one can use the constant for epsilon=1/2.

## 5. Expected first collision

Let tau be the first edge index at which the ordinary NBW repeats a vertex, including its initial vertex among visited vertices. Then P(tau>k)=p_k for k>=1 and P(tau>0)=1. With B_*=256Q(1+Q)n and a=ceil(sqrt(B_*)), Theorem A gives

\[
 E\tau=\sum_{k\geq0}P(\tau>k)
 \leq a+1+B_*\sum_{k=a+1}^\infty k^{-2}
 \leq a+1+B_*/a
 \leq 32\sqrt{Q(1+Q)n}+2.
\]

Thus E tau=O_D(sqrt(n)) for bounded degree ratio and O_Delta(sqrt(n)) for bounded maximum degree, uniformly over the starting edge. This also holds for a random first edge from a specified initial vertex, by averaging. This is about the first collision time, not the expected number of collision pairs.

## 6. The unresolved step

Without a bound on degree ratio, the packing bound Qn/L, the terminal-return bound Q, and the weight distortion in (3) are not uniformly controlled by this proof. Double stochasticity survives, but does not bound these terms. No assertion here proves the unrestricted conjecture or supplies a simple-graph counterexample.

## 7. Why the simple-graph convention matters

The multigraph variant is false. This is a version of the example after Question 4 of Bencs et al., PDF p.3, with multiplicities doubled so the minimum degree is at least three. On vertices 1,...,N, put b_j=2^{j^2+1} parallel edges between j and j+1, for 1<=j<N. There are no other edges. The first vertex has degree 4 and every vertex has degree at least 4. Start with any fixed directed edge from 1 to 2. Here non-backtracking excludes just the reverse of the previously used edge, as usual for edge-based NBW on a multigraph.

Conditional on progressing monotonically through vertex j, the probability of going next to j+1 is

\[
 \frac{b_j}{b_j+b_{j-1}-1}
 \geq\frac1{1+2^{-(2j-1)}}\qquad(2\leq j<N).
\]

Thus the probability of a vertex-simple walk of length N-1 is at least

\[
 \prod_{j=2}^{N-1}(1+2^{-(2j-1)})^{-1}
 \geq\exp\left(-\sum_{j=2}^{\infty}2^{-(2j-1)}\right)
 =e^{-1/6}.
\]

The inequality uses log(1+x)<=x. These lengths grow linearly in N, disproving the multigraph variant even for a specified starting edge. This is not a counterexample to Dozier's conjecture, which excludes parallel edges.
