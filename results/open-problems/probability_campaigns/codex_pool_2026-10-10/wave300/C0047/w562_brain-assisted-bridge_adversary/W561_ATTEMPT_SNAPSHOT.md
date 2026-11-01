# C0047 bridge attempt — w561

Current general target (primary verification pending): for every infinite finitely generated nonamenable group and every finite symmetric generating set, independent Bernoulli bond percolation on its Cayley graph satisfies p_c < p_u. The converse for amenable Cayley graphs is a separate known uniqueness implication. No current-openness or novelty claim is made yet.

## L01: regular-tree reference case

Let T_d be the infinite d-regular tree, d >= 3. Edges are independently open with probability p. Let p_c be the infimum of p for which the root has positive probability of belonging to an infinite open cluster; let p_u be the infimum of p for which there is almost surely exactly one infinite open cluster.

The forward cluster, after excluding the edge to its parent, is a Galton-Watson process with Binomial(d-1,p) offspring. Its survival probability is positive exactly when p(d-1)>1 (at equality this nondegenerate critical process dies out). The root has d forward branches, which have the same threshold. Therefore p_c=1/(d-1).

Fix p in (p_c,1) and a bi-infinite geodesic L. For every vertex v of L choose one neighbor u(v) outside L. Let A_v be the event that edge vu(v) is closed and the open forward cluster of u(v) in the component of T_d\L containing u(v) is infinite. The probability of A_v is (1-p) times the positive forward survival probability. The edge sets defining the A_v are pairwise disjoint; Bernoulli independence therefore gives independent events with a common positive probability. Almost surely infinitely many A_v occur, by the elementary independent-event Borel-Cantelli theorem. Their clusters belong to pairwise disjoint components of T_d\L and cannot connect across their closed attaching edges, hence there are infinitely many infinite open clusters. At p=1 the entire tree is connected. Below or at p_c there is no infinite cluster. Thus p_u=1.

This is a reproduced known special case, not a new resolution. Its independence is justified by explicitly disjoint edge sets.

Hardest general gap at this checkpoint: replace deterministic edge-separated infinite branches by an argument valid for every nonamenable Cayley graph, including graphs with no cut edges. Transporting branch events without disjoint supports is invalid.

## L02: quantitative continuation of a bounded two-point operator

Let G be a countable simple graph of uniformly bounded degree, with adjacency operator A on l2(V), a=||A||>0. For independent Bernoulli bond percolation write tau_p(x,y)=P_p(x is connected to y), and T_p for this nonnegative kernel. Suppose T_p0 defines a bounded operator with M=||T_p0||<infinity, for some p0 in [0,1). Then for every q in [p0,1] such that a M (q-p0)<1,

    ||T_q|| <= M / (1-a M (q-p0)).

Proof. Exhaust G by finite induced subgraphs H. For x,y in H Russo's formula gives d tau^H_p(x,y)/dp as a sum of pivotal-edge probabilities. If e={u,v} is pivotal, then after deleting e there are disjoint open paths from x to one endpoint and from the other endpoint to y. The two possible orientations, and the BK inequality applied to these increasing path events in the product law on E(H)\{e}, give

    0 <= (T^H_p)' <= T^H_p A_H T^H_p    (entrywise).

No independence between overlapping path events is assumed. Pivotality is independent of e's own state; probabilities in the graph with e deleted are bounded by the corresponding full-graph probabilities. The matrix inequality therefore has no missing factor 1/(1-p).

For nonnegative matrices entrywise domination implies domination of l2 operator norms: |Bf| <= C|f|. Also ||A_H||<=a, and ||T^H_p0||<=M since its entries are bounded by those of the compression of T_p0. Let f_H(p)=||T^H_p||. The norm is locally Lipschitz, and almost everywhere its upper derivative is at most ||(T^H_p)'|| <= a f_H(p)^2. Integrating the scalar inequality gives f_H(q)<=M/(1-aM(q-p0)) on the displayed interval, uniformly in H.

For finitely supported nonnegative f,g, connectivity inside the exhaustion increases to connectivity in G, so monotone convergence gives <g,T_q f> <= [M/(1-aM(q-p0))] ||f||2 ||g||2. Taking absolute values reduces arbitrary real or complex f,g to the nonnegative case. These uniformly bounded bilinear forms extend to a bounded l2 operator with the asserted kernel and norm. This closes the finite-volume-to-infinite-volume step without assuming boundedness at q in advance.

Corollary: if p0=p_c<1 and M is finite, p_c<p_{2->2}, with every 0<epsilon<min(1-p_c,1/(aM)) giving a bounded T_{p_c+epsilon}. This is a conditional implication; finiteness of M at p_c is not proved for the general target here. It reproduces a standard operator continuation argument, with an explicit quantitative bound for review.

## L03: uniqueness prevents l2 boundedness

Let G additionally be infinite and vertex-transitive. If there is almost surely exactly one infinite cluster at p, then theta=P_p(o lies in an infinite cluster)>0: the infinite cluster is nonempty almost surely, the vertex set is countable, and transitivity makes the vertex probabilities equal. Harris-FKG applied to the increasing events {x belongs to an infinite cluster} and {y belongs to an infinite cluster} gives tau_p(x,y)>=theta^2. The column T_p delta_x therefore has infinite squared l2 norm, contradicting boundedness.

Hence no parameter with bounded T_p has almost-sure uniqueness. Since the bounded-kernel parameter set is downward closed by entrywise domination, p_{2->2}<=p_u. In particular, the L02 corollary implies p_c<p_u for vertex-transitive graphs under the additional critical-operator boundedness assumption.

Single hardest remaining gap: establish ||T_{p_c}||_{2->2}<infinity for EVERY prescribed finite symmetric generating set of EVERY nonamenable finitely generated group, or find another argument establishing the phase gap. Nonamenability, anchored expansion, and pointwise exponential decay do not by themselves prove this missing estimate. Recent claimed general-result artifacts are being checked separately; no solved/open certification follows from their scope document or comparator declarations.

## L04: two exact refutations of insufficient operator arguments

On T_d, writing b=d-1, the unique path gives tau_p(o,x)=p^{dist(o,x)}. Thus tau_p decays exponentially in distance for every p<1. However

    ||T_p delta_o||_2^2 = 1 + d p^2 sum_{n>=0} (b p^2)^n,

which is infinite whenever b p^2>=1. Consequently pointwise exponential decay, without a rate relative to volume growth, does not imply boundedness of the two-point operator. In T_4 with p=3/4, the growth factor is 27/16>1 despite strictly positive exponential-decay rate log(4/3).

The adjacency norm of T_d is a=2 sqrt(b), and the normalized simple-random-walk spectral radius is rho=a/d. For completeness, orient the tree toward one fixed end, so each vertex has one parent and b children. Weighted Young's inequality on each edge, 2|f(parent)f(child)| <= |f(parent)|^2/sqrt(b) + sqrt(b)|f(child)|^2, gives |<f,Af>|<=2 sqrt(b)||f||_2^2. For the reverse bound use f_N(x)=b^{-dist(o,x)/2} up to radius N and zero beyond it. Its squared norm is 1+dN/b and <f_N,Af_N>=2dN/sqrt(b), whose ratio tends to 2 sqrt(b). Hence the asserted adjacency norm and normalized spectral radius follow.

In particular on T_4, p_c=1/3, rho=sqrt(3)/2, and p_c<1/rho is automatic, while p_c<1/(d rho)=1/(2sqrt(3)) is false. More generally any p_c in [0,1] satisfies p_c<1/rho whenever 0<rho<1. Therefore the prior C0047-A001 obstruction p_c>=1/rho, explicitly using normalized simple-random-walk rho, cannot be the missing case. This diagnoses a normalization error; it does NOT refute the Benjamini-Schramm conjecture.

## L05: correctly normalized sufficient spectral criterion

For any graph under L02's assumptions, a union bound over simple paths, enlarged to all walks, gives tau_p(x,y)<=sum_{n>=0}p^n A^n(x,y). If p a<1, this positive Neumann series has l2 norm at most 1/(1-pa); entrywise domination gives ||T_p||<=1/(1-pa). Thus for infinite vertex-transitive G,

    p_c(G)<1/||A||  =>  p_c(G)<p_u(G).

For a d-regular graph ||A||=d rho, so the sufficient criterion is p_c d rho<1. It is sufficient, not necessary: T_4 violates it while L01 establishes p_c<p_u. Replacing normalized rho by d rho repairs the erroneous spectral transfer but cannot prove the general conjecture through this criterion alone.
