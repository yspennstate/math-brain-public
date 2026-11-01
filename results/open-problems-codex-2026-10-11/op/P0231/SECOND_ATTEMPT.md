# Second serious attempt at P0231

2026-10-12. Starting gap: the deterministic supremum over finite recolorings need not be attained by the original coloring. The previous attempt proved no uniform conditional lower probability near that supremum.

## Two previously untried approaches

1. **A dual minimum-cut reduction on the genealogical contact graph.** Keep the original seeds opposite, minimize frontier dimension over all other prefix colors, and express this minimum as a maximum-bottleneck path between the seeds in a finite weighted overlap graph. Unlike the prior supremum, this quantity should decrease under refinement. Finite-permutation invariance of its limit could produce a deterministic lower envelope and a concrete connectivity criterion for a full solution. Pursue this first: its finite graph algebra can be proved and tested exactly.

2. **A stochastic homogenization / germ-law route.** Rescale around an interface point and seek a seed-independent stationary local law for the contact graph or tangent coloring. Ergodicity of an actual local limit might then force a local dimension and transfer it to the original frontier. This would need tightness, a Palm or interface-biased selection law, identification of the limit, and an argument connecting tangent laws to Hausdorff dimension. None was established in the first attempt. An ordinary translation-ergodicity theorem on all of R^d cannot be applied directly to a bounded cube with two fixed seeds. This approach is distinct from a local regeneration construction, but currently has substantially more prerequisites than approach 1.

The brain is being queried for the actual conditional-probability/martingale gap and for neighbouring random-partition/branching results. Brain output is only a lead.

## First saved result: a dual deterministic lower envelope

Let K_i^(n) be the descendant cells from ATTEMPT.md Section 2. For each binary assignment a on S_n with a(r)=red and a(b)=blue, let F_(n,a) be the resulting limiting frontier. Define

    m_n = min_{a(r)=red, a(b)=blue} dim_H F_(n,a).

The minimum is over a finite nonempty family. An assignment at time n can be extended to time n+1 by coloring the newly rooted point with its old inherited color. Its future coloring and limiting frontier are unchanged. Therefore m_(n+1)<=m_n. At n=0 there is only one allowed assignment, and m_0=D, the original frontier dimension. Thus m_n decreases to a limit B<=D.

For any finite permutation of arrivals supported on the first k indices, and any n>=k, the spatial root cells at time n are unchanged, up to labels. The two spatial seeds r,b are fixed. The collection of permitted seed-separating assignments is therefore unchanged. Thus m_n is unchanged for every n>=k, and so is B. Each m_n is measurable by the compact-set/dimension arguments checked in ATTEMPT.md Section 2.3. Hewitt–Savage gives a deterministic constant beta(r,b,d) with B=beta almost surely.

Consequently there are deterministic constants

    beta <= D <= c,

where c is the previous finite-recoloring supremum. This proposition does not identify beta with c or with D. In particular, monotonicity points in the opposite direction from an argument that would force all refinements to retain the original frontier dimension.

The following sections supply the graph interpretation, exact finite tests, and the obstruction to the proposed geometric bridge.

## Complete graph reduction

Fix n. Use the complete undirected graph on the spatial roots S_n, with weights

    w_n(i,j) = dim_H(K_i^(n) intersect K_j^(n))   (i!=j),

and assign weight zero when the intersection is empty. This convention is harmless for positive dimension thresholds and agrees with the convention dim_H(empty)=0 used in the first attempt. The graph is a finite algebraic encoding of limiting cells; it is not the finite Voronoi graph, whose faces have dimension d-1 and would discard the needed information.

For a seed-separating cut A (r in A, b outside A), put

    C_n(A)=max_{i in A, j outside A} w_n(i,j).

The exact finite union identity from the first attempt shows that C_n(A) is the dimension of its recolored limiting frontier. Thus m_n=min_A C_n(A).

For a simple path P from r to b define its bottleneck as the minimum edge weight on P, and let W_n be the maximum bottleneck over all simple paths. This maximum exists: there are finitely many simple paths, and the complete graph has the one-edge path. Allowing non-simple paths changes nothing, because deleting a cycle cannot lower a minimum of edge weights.

**Finite theorem: m_n=W_n.** Every r-to-b path crosses every separating cut. The minimum weight on that path is at most the weight of its crossing edge, and hence at most the maximum crossing weight of the cut. Taking maxima over paths and then minima over cuts gives W_n<=m_n.

For the reverse inequality, retain only edges with weight strictly greater than W_n and let A be the vertices reachable from r in this threshold graph. The seed b is outside A: otherwise a path entirely of weights greater than W_n, reduced to a simple path if needed, would contradict the definition of W_n. Every edge from A to its complement has weight <=W_n, since a larger edge would extend reachability. Therefore C_n(A)<=W_n and m_n<=W_n. This proves equality, including tied weights; strict greater-than is essential in the reachability construction.

Equivalently, for any real t>=0,

    m_n>t iff r and b are connected by edges of weight >t.

The implication from a path to a cut uses an edge crossing, not the sum of edge weights. The ordinary maximum-flow/minimum-cut theorem with summed capacities is not the appropriate theorem here.

### Refinement checked at the level of individual weights

Let p:S_(n+1)->S_n be the root map from the first attempt. For two distinct old roots i,j, finite unions distribute over intersection, giving

    K_i^(n) intersect K_j^(n)
      = union_{p(u)=i, p(v)=j} (K_u^(n+1) intersect K_v^(n+1)).

Consequently

    w_n(i,j) = max_{p(u)=i,p(v)=j} w_(n+1)(u,v).

Every coarse cut A lifts to p^(-1)(A), and its crossing maximum is unchanged by this formula. The lifted cut still separates the original seeds, since p(r)=r and p(b)=b. The fine graph permits additional cuts, so m_(n+1)<=m_n. This proves the asserted monotonicity with no assumption that children within one root group have large-weight contacts.

### Full zero-one step for the decreasing limit

Each m_n is a minimum of finitely many measurable compact-set dimensions, hence measurable. Since 0<=m_n<=d and m_n decreases, B=inf_n m_n is measurable and exists. Finite permutations fix m_n for every sufficiently large n by spatial-root invariance, retaining the two terminal seed locations. Taking the infimum of the decreasing sequence, or its limit, therefore gives B(pi X)=B(X). Hewitt–Savage makes every event {B<=q}, q rational, have probability zero or one. Define beta=inf{q rational:P(B<=q)=1}; the set is nonempty because B<=d. Every rational q<beta has probability zero, and every rational q>beta has probability one by monotonicity and the definition of the infimum. Countable rational approximation from both sides gives B=beta almost surely.

The original prefix coloring is an allowed cut for every n. Therefore m_n<=D for every n, and beta<=D. At n=0, m_0=D exactly. Combining with the previously proved upper envelope yields beta<=D<=c. No strict lower bound for beta is asserted in this attempt.

**Useful sufficient criterion for solving P0231.** If beta=c, then D=c almost surely. More explicitly, it would suffice to prove that almost surely, for every rational t<c, the seeds remain connected in the weight->t graph for all n. Countability of these thresholds and times removes any simultaneous-null-set issue. Indeed that would give m_n>t for every n, and hence beta>=t; rational approximation gives beta>=c, and beta<=D<=c gives equality. Conversely, if beta=c then for each t<c, m_n>=beta=c>t for all n, so this connectivity criterion holds. This is an equivalence for beta=c, not an equivalence for the original question: D could be deterministic with beta<c.

## Hostile-referee obstruction search

### Minimal weighted obstruction

Take fine vertices r,u,b forming a path with w(r,u)=a and w(u,b)=h, where 0<a<h, and set w(r,b)=0. Its maximum bottleneck from r to b and its minimum cut maximum are both a. If the coarse r cell is the union of r and u, its only contact with b has weight h. Thus the coarse minimum cut equals h, while the fine minimum equals a. The inherited assignment r,u red and b blue retains the frontier value h; recoloring u blue changes the cut value to a.

For t in (a,h), the coarse roots are connected in the weight->t graph, but the refined seeds are not. All coarse inter-group weights obey the exact maximum-under-collapse formula. Ordinary graph connectedness therefore does not imply the needed threshold connectedness, and coarse threshold connectedness need not survive refinement. The exhaustive/random computations reproduce this obstruction with a=13,h=16.

This is an abstract finite obstruction, not a counterexample to the Poisson model. The next construction checks that the obstruction can also arise from genuine closed partitions of a connected cube, with both positive contact dimensions strictly between d-1 and d.

### An explicit closed-partition realization

Fix d>=2. In [0,1], put a two-branch Cantor set C_L of contraction ratio 1/4 in [.1,.4], and another C_H of contraction ratio 1/3 in [.6,.9]. A middle gap of generation k means one removed at the k-th step of that Cantor construction. Label the complementary open intervals as follows:

- [0,.1) has label r, (.4,.6) has label u, and (.9,1] has label b (relative open intervals).
- In [.1,.4], middle gaps of odd generation have label r and of even generation have label u.
- In [.6,.9], middle gaps of odd generation have label u and of even generation have label b.

Let O_r,O_u,O_b be the unions of the intervals with the corresponding labels, and let L_i be their closures in [0,1]. Every Cantor point is approached by gaps of both parities: a sufficiently fine construction interval containing that point lies in any given neighborhood, and inside it there are gaps removed at each of the next two generations. Thus each point of C_L belongs to L_r and L_u, and each point of C_H belongs to L_u and L_b.

Outside C_L union C_H every point is in the relative interior of a complementary interval of a unique label; an open neighborhood inside that interval is disjoint from all intervals of other labels. Such a point belongs only to the closure for its own label. Also L_r is contained in [0,.4] and L_b in [.6,1]. It follows exactly that

    L_r intersect L_u=C_L,
    L_u intersect L_b=C_H,
    L_r intersect L_b=empty,
    L_r union L_u union L_b=[0,1].

Define K_i=L_i times [0,1]^(d-1). These are compact sets covering Q, with disjoint relative interiors. All three have nonempty interior; the points (.05,.5,...,.5), (.5,.5,...,.5), (.95,.5,...,.5) lie in neighborhoods contained only in K_r,K_u,K_b respectively. Their exact contact sets are C_L times [0,1]^(d-1) and C_H times [0,1]^(d-1), and there is no r-b contact.

For completeness, the dimension calculation used here is proved next rather than inferred from a picture or a simulation.

### Cantor-product dimension proof

For 0<rho<1/2, let C_rho be the two-branch middle-gap Cantor set in an interval [a,a+ell] of length ell>0. Put alpha=log(2)/log(1/rho), so rho^alpha=1/2. At level k there are 2^k disjoint construction intervals of length ell*rho^k. Define the uniform Cantor probability measure as the law of a+ell*(1-rho)*sum_{j>=1} epsilon_j*rho^(j-1), where the epsilon_j are independent fair bits. This convergent series has support C_rho and assigns mass 2^(-k) to each level-k interval, as seen by fixing its first k bits.

For any interval I of length z<ell, choose k>=1 with ell*rho^k<=z<ell*rho^(k-1). Any two consecutive level-k construction intervals are separated by a gap at least ell*(1-2rho)*rho^(k-1). If I meets N such intervals, points of I in consecutive intervals are separated by at least this gap, so (N-1)*ell*(1-2rho)*rho^(k-1)<=z. Hence N<=1+1/(1-2rho). Enlarging this numerical bound to an integer constant A is harmless. Therefore

    mu(I)<=A*2^(-k)=A*(rho^k)^alpha<=A*(z/ell)^alpha.

For z>=ell the same inequality holds after increasing A if needed. Points have zero measure, since the level-k mass at any point is at most 2^(-k), which tends to zero.

Let nu be mu times (d-1)-dimensional Lebesgue probability measure on [0,1]^(d-1). Any nonempty set U of diameter z is contained in a product of d coordinate intervals of lengths at most 2z (choose a point of U and bound each coordinate distance from it by z). Consequently the outer nu-measure of U is at most A*ell^(-alpha)*(2z)^(alpha+d-1), with a larger fixed constant if necessary. For every countable cover of the support, outer-measure subadditivity gives

    1 <= constant * sum diam(U_j)^(alpha+d-1).

Taking infima over covers at every scale proves positive (alpha+d-1)-dimensional Hausdorff measure, hence dimension at least alpha+d-1. This is the mass-distribution argument written explicitly, and uses no unproved formula for arbitrary fractal products.

For the upper bound, at level k cover each Cantor interval times [0,1]^(d-1) by at most A_d*(ell*rho^k)^(-(d-1)) cubes of side at most ell*rho^k, adjusting A_d for the first few k. Their diameters are at most sqrt(d)*ell*rho^k. For any s>alpha+d-1 the total s-cost is at most a fixed constant times

    2^k*(rho^k)^(s-(d-1)) = (2*rho^(s-(d-1)))^k,

which tends to zero because s-(d-1)>alpha. Thus the dimension is at most alpha+d-1, proving equality.

Applying this with rho=1/4 and 1/3 gives exact weights

    a=d-1+1/2,
    h=d-1+log(2)/log(3),

with d-1<a<h<d. The coarse partition (K_r union K_u, K_b) has frontier dimension h. The alternative seed-separating partition (K_r, K_u union K_b) has frontier dimension a. This realizes the strict-drop weighted obstruction in a closed partition of a connected cube with protected seed neighborhoods and strictly fractal contacts.

It is not asserted that these Cantor-product cells are realizable by nearest-neighbor Poisson coloring. In particular, this is not a counterexample to P0231. It refutes a proposed deterministic shortcut based only on connectedness, closure, seed neighborhoods, and strict contact-dimension bounds. A model-specific universality or threshold-connectivity result would still be required.

## Checks and remaining gap

1. Bottleneck identity: the reachable-set proof handles ties and uses strict threshold edges; summing capacities would prove a different statement.
2. Refinement: crossing weights of inherited cuts are unchanged, while new cuts can lower the minimum. No reverse monotonicity is assumed.
3. Zero-one: only the limit of the minimization is permutation invariant. m_0=D can change under early permutations, so the argument does not prove D invariant.
4. Numerical scope: bottleneck_checks.py exhaustively checked 59,808 complete weighted graphs on 2–5 vertices with weights 0,1,2; all min-cut/bottleneck identities passed. It checked 500 random refinements and every inherited terminal cut in each trial, and found the explicit strict-drop example. These are exact integer computations, not estimates of Hausdorff dimensions. Runtime recorded in bottleneck_checks.json was about 54 seconds; memory is far below 1 GB.
5. Geometric scope: the Cantor-product example has full dimension proofs and exact contact sets, but is deliberately not claimed to follow the Poisson genealogy.
6. Formal scope: BottleneckCuts.lean formalizes no-path iff a closed separating cut for an arbitrary relation; this is the reachable-set algebra behind the weighted bottleneck theorem. It uses only Mathlib.Data.Set.Basic, with no sorry or native_decide. The command `lake env lean ~/brain_workers/TRIO_1011/op/P0231/BottleneckCuts.lean`, run from ~/lean_verify, completed with exit code 0 and no compiler diagnostics after acquiring the shared slot. This algebra is kernel-checked; the analytical and Poisson arguments remain handwritten proofs. The record is in second_lean_check.txt.
7. Brain scope: no recalled card supplied the missing local-universality theorem. The bottleneck query returned maximum-flow/minimum-cut and spanning-tree leads, but these do not identify beta and c. One card mislabeled an edge-disjoint-path assertion as Hall's marriage theorem; it was not used. The homogenization query returned Kingman's subadditive theorem, but no stationary subadditive dimension functional has been constructed for this model, so Kingman is not applied.

**Exact remaining gap:** establish original-frontier determinism, or produce two different dimension values with positive probability in the actual Poisson model. The new deterministic bounds beta<=D<=c do not imply that beta=c. The proposed stronger target beta=c is equivalent to persistent seed-to-seed connectivity in all refined graphs above every dimension threshold below c. Neither that property nor a replacement sufficient argument was proved. The explicit closed-partition construction shows why the finite graph and topological facts proved so far cannot supply it alone.

Second-attempt verdict: PARTIAL. New proved content is the deterministic lower envelope and its exact bottleneck/minimum-cut formulation, together with a rigorous obstruction to an overstrong geometric shortcut. No resolution of the original d>=2 zero-one question is claimed.
