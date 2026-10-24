# P0043: a sharp test of the symmetry assumption

Date: 2026-10-10. Author: w438. Referee: w440, pending. Mathematical status: author proof of special cases only; no resolution or novelty claim for P0043.

## Exact target

Let G be an infinite connected locally finite quasi-transitive graph, and let P_p be independent Bernoulli bond percolation on its edges. Set theta_o(p)=P_p(|C(o)|=infinity) and p_c=inf{p:theta_o(p)>0}. Assume p_c<1. The target is theta_o(p_c)=0 for every vertex o, equivalently no infinite open cluster almost surely. All these hypotheses are material. The abbreviated September ranking is not an up-to-date certificate of openness. A recent full claim has been located; current openness is UNKNOWN pending a primary proof check.

## Boundary already proved

On Z, p_c=1 and theta_0(1)=1. For p<1 the probabilities of open paths of length n to either side are p^n, and an infinite cluster containing 0 would reach arbitrarily far in at least one direction. Thus the missing p_c<1 qualification cannot be dropped.

## Main special case: an exact polynomial threshold on trees

For every real beta, put N=ceil(8(1+|beta|)), f(x)=x/2+beta log_2(1+x/N), and B_n=floor(f(n)) for n>=0. Let T_beta be the rooted spherically symmetric tree whose vertices at depth n have a_n=2^(B_(n+1)-B_n) children. Write L_n for its level size. Then:

1. Every a_n is 1 or 2, so the tree is infinite, connected, locally finite, and has maximum degree at most 3.
2. p_c(T_beta)=1/sqrt(2) for every beta.
3. At p=p_c, the root has positive probability of an infinite open cluster if and only if beta>1.
4. If q_n=P_(p_c)(o connects to level n), then for fixed beta<1, q_n is comparable to n^(beta-1) for large n; for beta=1 it is comparable to 1/log n. Constants may depend on beta. For beta>1, q_n decreases to a strictly positive theta_o(p_c).

Thus bounded degree, independence, p_c<1, and a common exponential growth rate do not imply critical extinction. This is a counterexample to that broader auxiliary bridge. T_beta is not quasi-transitive, so it is not a counterexample to P0043.

### Construction and branching frequency

f'(x)=1/2+beta/((N+x) ln 2). Because N>=8(1+|beta|), 1/4<f'(x)<3/4. Hence f(n+1)-f(n) is in (1/4,3/4), and B_(n+1)-B_n is 0 or 1. Also f(n+4)-f(n)>1, so B_(n+4)-B_n>=1: every four consecutive levels contain a branching level. Conversely there cannot be infinitely many levels with no branching. B_0=0 and L_n=2^B_n. Consequently

  (1/2) (sqrt(2))^n (1+n/N)^beta < L_n <= (sqrt(2))^n (1+n/N)^beta.

In particular lim L_n^(1/n)=sqrt(2). This growth statement alone will not be used as a percolation criterion.

### Lemma A: reciprocal survival identity (finite, exact)

Consider any deterministic sequence a_i in {1,2}, Bernoulli bond parameter 0<p<=1, and terminal depth n. Let q_i^(n) be the probability that one vertex at level i reaches level n, with q_n^(n)=1. Let m_0=1 and m_j=p^j product_(i<j) a_i. Disjoint descendant subtrees use disjoint edge coordinates, so the recursion is justified by independence:

  a_i=1: q_i=p q_(i+1).
  a_i=2: q_i=2p q_(i+1)-p^2 q_(i+1)^2.

All q_i>0. Taking reciprocals gives

  1/q_i = 1/(a_i p q_(i+1)) + d_i,

where d_i=0 for a_i=1, and d_i=1/[4(1-p q_(i+1)/2)] for a_i=2. Unrolling the recursion yields the exact identity

  1/q_0^(n) = 1/m_n + sum_(0<=i<n) d_i/m_i.

Since 0<q_(i+1)<=1, for branching levels 1/4<=d_i<=1/[4(1-p/2)]. Therefore, with S_n=sum_(i<n:a_i=2)1/m_i,

  1/m_n + S_n/4 <= 1/q_0^(n) <= 1/m_n + S_n/[4(1-p/2)].                 (A)

This is an algebraic identity and bound, not multiplication of dependent conditional events.

### Proof of the threshold and rates

For T_beta, m_n=p^n L_n is comparable, with constants 1/2 and 1, to (p sqrt(2))^n (1+n/N)^beta.

If p<1/sqrt(2), m_n tends to zero. The number Z_n of level-n vertices connected to the root has mean m_n, so q_n=P(Z_n>0)<=m_n tends to zero. Thus there is no root survival below 1/sqrt(2).

If p>1/sqrt(2), sum_(n>=0)1/m_n is finite and sup_n(1/m_n)<infinity. The upper bound on 1/q_n in (A) is uniformly finite, so inf_n q_n>0. The events of reaching level n decrease; their intersection is the event that the root cluster is infinite (finite levels and finite degree). Continuity from above gives positive survival. Therefore p_c=1/sqrt(2).

At p=p_c, 1/m_n is comparable to (1+n/N)^(-beta). In each block of four levels at least one is a branching level. On such a block the four values (1+i/N)^(-beta) have a ratio bounded by a constant depending only on beta and N. Thus S_n has the same convergence/divergence as sum_(i<n)(1+i/N)^(-beta), and has its same order when this sum diverges. For beta<1 this order is n^(1-beta); for beta=1 it is log n. The term 1/m_n is of smaller order in these two cases. Equation (A) proves the stated q_n rates and extinction. For beta>1, the whole sum converges and 1/m_n tends to zero, so (A) gives a uniform positive lower bound on q_n and hence survival.

An explicit positive lower bound is available without any finite experiment. For beta>1, S_infinity<=2 sum_(i>=0)(1+i/N)^(-beta)<=2(1+N/(beta-1)), by the integral comparison for a decreasing function. Taking n to infinity in the upper bound of (A) gives theta_o(p_c)>=(2-1/sqrt(2))/(1+N/(beta-1)). In particular, T_2 has N=24 and theta_o(p_c)>=(2-1/sqrt(2))/25>0. This is a proved analytic bound, not a measured simulation estimate.

For beta<=1 this is absence of an infinite cluster anywhere, not only at the root: removing a finite initial segment preserves divergence and the same recursion applies at each fixed vertex. Every infinite cluster in a rooted locally finite tree has a descendant ray from one of its vertices (choose a vertex of minimal depth in the cluster). The vertex set is countable, so a union of zero-probability descendant-survival events still has probability zero.

### Why the counterexample is outside P0043

For beta>1, the root is the unique degree-one vertex: a_0=1 because 0<f(1)<1, and every other vertex has a parent and at least one child. Automorphisms fix the root and preserve its distance levels. There are infinitely many nonempty levels, hence infinitely many vertex orbits. Quasi-transitivity fails.

## Lemma B: extinction need not pass to a local limit, even with fixed p_c

Fix beta=2 and T=T_2. For each K, define T^(K) by retaining its offspring sequence for i<K and replacing the tail by the periodic sequence 1,2,1,2,... starting at i=K. Each T^(K) has degree at most 3 and p_c=1/sqrt(2): its m_n has the same exponential factor as T, up to a K-dependent constant and a bounded parity correction. At p_c, m_n is bounded above and away from zero for n>=K, and infinitely many tail levels branch. Thus S_n diverges and (A) proves theta_(T^(K))(p_c)=0. The same suffix argument excludes every infinite cluster.

For any fixed radius R, T^(K) and T have identical rooted R-balls when K>R. Hence T^(K) converges locally to T, and all the critical parameters are exactly the same. But theta_T(p_c)>0. This refutes the auxiliary claim that critical extinction plus convergence of critical parameters passes to a local limit for arbitrary bounded-degree rooted graphs. These approximants also lie outside the quasi-transitive target class; no locality theorem for quasi-transitive graphs is refuted.

## Lemma C: same critical threshold, same quasi-isometry class, different critical behavior

Each T_beta is quasi-isometric to the rooted infinite binary tree. Contract every maximal unary corridor between successive branching vertices. Since every four levels contain a branching level, these corridors have length at most 4, and the initial root stem also has length at most 4. The branching skeleton is exactly the rooted binary tree: each branching vertex has two descendant branching vertices at the next branching depth. Map corridor interiors to their previous branching vertex, and map the initial stem to the first branching vertex. Call the resulting surjection pi.

An edge maps either to a point or to a skeleton edge, so d_binary(pi(u),pi(v))<=d_T(u,v). Lifting the skeleton geodesic replaces every edge by a corridor of length at most 4. Each endpoint is at distance at most 4 from its representative, so d_T(u,v)<=4 d_binary(pi(u),pi(v))+8. These two inequalities and surjectivity prove quasi-isometry.

In particular T_0 and T_2 are quasi-isometric trees of degree at most 3 and have exactly equal critical probability 1/sqrt(2), but T_0 has no infinite critical cluster and T_2 has positive critical root survival. Therefore critical extinction is not a quasi-isometry invariant on arbitrary bounded-degree graphs, even after requiring equality of the critical parameters. This does not assert failure of invariance within a narrower quasi-transitive or polynomial-growth class.

## Substantive route toward P0043 and its single hardest gap

A tree exploration can produce a varying-environment recursion only if distinct branches use disjoint untouched randomness. On a general quasi-transitive graph, forward branches may overlap; neither the binomial recursion nor a level-size growth rate is justified. The counterexample also shows that controlling only the exponential growth rate leaves the decisive polynomial correction uncontrolled.

A possible route is a finite-scale extinction criterion uniform in the radius, or a valid comparison with an extinction-prone exploration retaining conditional control after every exposure. The single hardest unresolved step is to prove such a criterion from quasi-transitivity in the subexponential-growth regime without assuming the desired critical extinction itself. No comparison of this strength is proved here. Recent manuscripts claiming the full target may supply it, but that is a separate primary proof and axiom audit.

NEXT: Have w440 check the reciprocal identity, branching-frequency argument, and both exclusions from quasi-transitivity; retain the main target as unresolved in this packet.
