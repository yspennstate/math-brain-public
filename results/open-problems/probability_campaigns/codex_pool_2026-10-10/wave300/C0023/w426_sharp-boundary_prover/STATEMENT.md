# C0023: statement-only handoff for w427

Fix an integer d with 3 <= d <= 10. On the undirected graph with vertex set Z^d and an edge {x,y} exactly when ||x-y||_1=1, let edge states be independent Bernoulli(p). Let C(0) be the open cluster of the origin, theta_d(p)=P_p(|C(0)|=infinity), and p_c(d)=inf{p in [0,1]:theta_d(p)>0}. The assigned target is theta_d(p_c(d))=0 for every such d. This packet treats BOND percolation; site and long-range versions are separate statements. Current openness: UNKNOWN, not a novelty claim.

Primary mathematical route: Kozma-Nitzan, arXiv:2401.12397v1, Conjectures 1-3 and Theorem 6. Conjecture 3 asks for delta(epsilon)>0 independent of the graph and the number of relays: P(o connects to A)>1-delta and P(a connects to b)>1-delta for every a in A imply P(o connects to b)>1-epsilon. Theorem 6 proves that this uniform gluing assertion would imply the lattice target.

Disjoint lane for adversarial review: finite forests, deterministic separator witnesses, and conditioning on a selected relay. No general finite-graph gluing proof is claimed.

L1. Let G be a finite undirected graph, o,b vertices, A a nonempty vertex set, v a vertex, and a_star in A. Suppose every o-to-A path contains v and every a_star-to-b path contains v. Then for EVERY probability law on edge configurations, {o connects to A} intersect {a_star connects to b} is a subset of {o connects to b} intersect {o connects to A}. Under independent edge states with arbitrary probabilities in [0,1], P(o connects to b) >= P(o connects to A) min_{a in A}P(a connects to b).

L2. Under independent bond percolation on ANY finite forest with arbitrary edge probabilities in [0,1], the product inequality in L1 holds for every o,b and nonempty A, regardless of |A|. In fact a deterministic a_star in A witnesses the stronger event inclusion in L1. The coefficient 1 in the product inequality is sharp.

B1 to stress-test. Given an arbitrary ordering of A, let I be its first member in the open cluster of o, undefined if o misses A. A tempting stronger bridge says either P(a connects to b | I=a)>=P(a connects to b) for each selection with positive probability, or its averaged version P(o connects to b)>=sum_{a in A}P(I=a)P(a connects to b). Check both on the path o--a2--a1--b, with independent edge probabilities r,s,t in (0,1), and relay order (a1,a2). This is an auxiliary bridge; a failure would not refute Conjecture 1 or C0023. Any assertion requiring ordering by nondecreasing P(a connects to b) is a different assertion.

Please start from these statements, not my proofs. w428 will receive the complete proof and calculation packet later. Independent review pending.
