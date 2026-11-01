# P0043: thinning and the missing growth bridge

Exact target: on every infinite connected locally finite quasi-transitive graph G with p_c(G)<1, independent Bernoulli bond percolation at p_c has no infinite open cluster. The 2026-09-07 catalog is historical evidence, not a current openness certificate. A primary manuscript dated 24 September 2026, `sources/criticality_2026_09_24.pdf`, claims precisely this in Theorem 1.1 (page 2). Its whole proof and trusted formal axioms have not been checked here. Current openness is UNKNOWN; this packet makes no novelty claim.

## Saved deduction L002: quenched thinning obstruction

Let G be any countable graph and let p_c(G)=inf{r:P_r(some infinite open cluster exists)>0}. Take a Bernoulli-p edge configuration omega, p>0. For almost every omega, every infinite component C of the open-edge graph has its own Bernoulli bond threshold p_c(C)>=min{1,p_c(G)/p}. In particular, any putative infinite critical cluster has p_c(C)=1.

Proof: for each rational q in (0,1) with pq<p_c(G), take a fresh family eta of independent Bernoulli-q bits, independent of all omega bits. The products omega_e eta_e are mutually independent Bernoulli-pq bits. They have no infinite component almost surely. By Tonelli, their conditional probability of an infinite component given omega is zero for almost every omega. On the open edges of each C, eta is precisely independent bond percolation on C. For this fixed rational q there are at most countably many components, so all have zero q-percolation probability. Intersect the probability-one sets for countably many rational q. Monotonicity then gives the threshold bound for every component, including parameters arbitrarily close to min{1,p_c(G)/p}. At p=p_c>0 the bound is one. On a bounded-degree infinite graph p_c>0 by the self-avoiding-path union bound. A connected locally finite quasi-transitive graph has bounded degree and is countable, so this applies to the target.

This is an elementary deduction, with no novelty claim and no independent review yet. Conditional independence is used only after introducing fresh eta; selected clusters are not declared independent of omega.

## Saved deduction L003: bounded corridors cannot supply independent branching in subexponential growth

Suppose the rooted b-ary tree, b>=2, admits an injective vertex map f into a locally finite graph G, and every parent-child image pair has G-distance at most a fixed L>=1. Then |B_G(f(root),Ln)|>=b^n, hence liminf_{r->infinity}|B_G(f(root),r)|^(1/r)>=b^(1/L)>1. Thus no graph of subexponential volume growth can support such an embedding.

Proof: the b^n vertices at tree-depth n are distinct images and each is within distance Ln of the root image. For arbitrary r use n=floor(r/L). This gives the liminf bound. The conclusion needs injectivity and a uniform length bound. It makes no assertion about variable-length corridors, repeated vertices, or dependent block processes.

This rules out a tempting thinning bridge that tries to find a uniformly bounded independent branching network inside every critical cluster on a subexponential graph. Such a network would already contradict ambient growth, whether or not percolation is critical.

## Saved deduction L004: positive anchored expansion survives thinning

Let C be an infinite connected graph of maximum degree Delta>=2 and o a vertex. Define h(C,o) as the infimum of |boundary_E K|/|K| over finite connected vertex sets K containing o. If h=h(C,o)>0, set a=(1-q)^h. For any q<1 with a<1/(Delta^2+1),

P_q^C(o belongs to an infinite cluster) >= 1 - a/(1-Delta^2 a) > 0.

Proof: impose fixed orders on the countable vertex and neighbor sets. A canonical spanning tree of a connected n-vertex set K containing o has a depth-first walk of length 2(n-1). A walk determines its visited set, so at most Delta^{2(n-1)} such K exist. If the q-open root cluster equals K, all edges of boundary_E K are closed. Independence of the fresh thinning bits bounds this event by (1-q)^{|boundary_E K|}<=a^n. Sum over all finite root clusters: P_q^C(root cluster finite)<=sum_{n>=1}Delta^{2(n-1)}a^n=a/(1-Delta^2 a). The stated restriction makes this strictly below one. No independence between different possible K is assumed; this is a union bound over mutually exclusive exact-cluster events.

Corollary L004b: for any bounded-degree countable ambient graph with p_c>0, almost surely every infinite Bernoulli-p_c cluster has h(C,o)=0 for every vertex o in that cluster. Otherwise L004 supplies some rational q<1 with positive conditional survival, contradicting the simultaneous rational-q statement in L002. This is a necessary property; zero anchored expansion does not imply finiteness.

## Saved counterexample L005: exponential growth without quasi-transitivity can be fragile

Let H consist of a spine ray s_0,s_1,..., with a full finite binary tree of depth n attached to s_n by one edge for each n>=0. Maximum degree is at most 3. The ball B_H(s_0,2n+1) contains the 2^n leaves of the nth graft, so liminf_r |B_H(s_0,r)|^{1/r}>=sqrt(2)>1. Every infinite simple path from s_0 must follow the entire spine, since each graft is finite. For q<1 its first m spine edges are open with probability q^m, tending to zero. The same holds from any vertex, so p_c(H)=1. At q=1 it is one infinite cluster.

This is an exact counterexample to `infinite + bounded degree + exponential volume growth implies p_c<1`. It does not refute Hutchcroft's theorem: H is not quasi-transitive. The spine vertices have different sizes of finite components attached to them; the finite-component-size data after removal distinguish infinitely many vertex types. A random critical cluster also need not inherit quasi-transitivity from its ambient graph. Thus that theorem cannot be transferred to a cluster by checking growth alone.


## Saved deduction L006: a quantitative bound near criticality

Fix a bounded-degree countable graph G with maximum degree Delta>=2 and 0<p_c(G)<1. For each fixed p in (p_c,1], almost surely every infinite Bernoulli-p component C and every o in C satisfy

h(C,o) <= log(Delta^2+1) / log(p/(p-p_c)).

At p=p_c the corresponding bound is h(C,o)=0. This is a statement for each fixed p; simultaneity for an uncountable collection of p is not claimed.

Proof: L002 gives p_c(C)>=p_c(G)/p. If h(C,o)>0, L004 gives survival for every q>1-(Delta^2+1)^(-1/h), hence p_c(C)<=1-(Delta^2+1)^(-1/h). Combining gives (Delta^2+1)^(-1/h)<=(p-p_c)/p. Taking logarithms and rearranging yields the displayed bound. If h=0 the inequality holds directly. At p=p_c, L002 and L004 contradict any h>0. Countable vertices ensure the statement holds for every root. This is an original derivation in this packet, with no novelty or independent-review claim.

## Brain-assisted prior-attempt digest

The bounded read-only store query returned `math:probability.core:attempt-p0043-absence-of-infinite-clusters-at-critical-percolation`, explicitly marked unverified concept/author-checked only. Its saved regular-tree proof uses x=1-(1-px)^b at p=1/b with b>=2. This equation requires b independent isomorphic forward subtrees. A general quasi-transitive ambient graph supplies neither those forward components nor their independence after cluster exploration; a random critical cluster supplies even less symmetry. The old record itself names loop dependence as its obstruction. This packet avoids redoing that computation: fresh thinning on a fixed sampled configuration gives the valid L002 product law, then L004 supplies a genuine survival bridge under a stated additional condition. L006 quantifies why the needed anchored expansion cannot persist near criticality.


## The single hardest remaining gap

Prove a mechanism specific to independent Bernoulli critical clusters that makes any putative infinite cluster survive some independent q-thinning with q<1, or supply a different critical finite-connection contradiction. L002 shows that the first mechanism would settle the target. L004 proves it under positive anchored expansion, but also shows that this property is impossible for a putative critical cluster. L003 rules out a uniformly bounded injective branching construction in subexponential growth. L005 shows that even exponential intrinsic volume growth without quasi-transitivity does not repair the route.

Independent adversary closure: w442/ATTEMPT.md, lines 25-37, proves that every infinite subgraph of bounded-degree subexponential G has zero asymptotic anchored expansion. In particular h(C,o)=0. Therefore L004 cannot cover any subexponential ambient graph, even above criticality. This route is CLOSED. The valid L006 bound is retained as a necessary condition on general bounded-degree clusters; it is not a proof of critical absence. See ADVERSARY_RESPONSE.md.

NEXT: w443 checks L002-L006 and w442 C003; a future proof step must handle zero anchored expansion directly, with one fixed thinning parameter and justified conditional probabilities.
