P0043 independent route: quenched thinning and path-intersection energy

Exact target and source status are in STATEMENT.md. The independent approach was saved in APPROACH_BEFORE_PEER_PROOFS.md before reading current peer proofs. The following are complete author proofs of auxiliary statements, awaiting w437; they do not prove P0043 and carry no novelty claim.

Prior-attempt digest. The 2026-09-07 ranking names P0043, while the same intake's exact companion statement is C0084, problems.jsonl line 84, sourced to Heydenreich--van der Hofstad, Open Problem 15.11. C0084-A001, attempts.jsonl line 72, uses a growth-class split and the exponential-growth connectivity argument. It supplies no complete proof. Its description of polynomial growth as essentially reducing to Z^d is not a justified transfer theorem; the attempt itself notes critical behavior is not generally a quasi-isometry invariant. Its speculation that the exponential-growth argument makes susceptibility finite at criticality is false in general: see L5 below. The primary proof instead uses finite susceptibility strictly BELOW p_c, then left continuity of a minimum-connectivity exponential rate. Ten named intake ledgers yielded one cross reference: H0016, a not-attempted site-percolation lattice conjecture tagged duplicate_of G0001/P0043. Cerf's primary abstract, arXiv:2608.23661, confirms a site partial result and supplies neither general critical extinction nor a site-to-bond transfer. The targeted H/I attempt search returned no target proof. The Lean directory's hits concerned other percolation problems, not this target. These are bounded negative searches, not completeness or current-openness certificates. Team O lists the same statement under C0084 for w344. This route reserves thinning and ray-energy boundaries rather than repeating the growth split.

Primary sources actually opened: Benjamini--Schramm (1996), Conjecture 4, printed page 75, calls the graphs 'almost transitive' and discusses site percolation; Hutchcroft, arXiv:1605.05301v1, Introduction, states the precise bond version with connectedness and local finiteness. Benjamini--Pemantle--Peres, arXiv:math/9701227v1, Section 2, equations (5)--(7), already contains the normalized open-prefix second-moment method used in L2. It is a classical rederivation. The public full-target scope claim links to a formal COMPARATOR with `sorry`; that comparator only specifies the target. No actual solution-module verification or trusted-axiom report was obtained here. Current openness stays UNKNOWN.

L1. Critical components are maximally fragile under independent thinning.

Let G be any countable connected locally finite graph, with bond threshold p_c>0. Sample iid Bernoulli(p_c) edge states omega. Almost surely, every infinite component C of omega has p_c(C)=1, where p_c(C) is the threshold for iid bond percolation on the fixed graph C.

Proof. For a fixed rational r in (0,1), independently retain every omega-open edge with probability r. Unconditionally the resulting graph is iid Bernoulli(p_c r) on G and has no infinite component, since p_c r<p_c. Thus the nonnegative conditional probability, given omega, of any infinite component after thinning equals zero for almost every omega, by integration. Intersect these probability-one sets over rational r. For every omega in that intersection, no fixed component C percolates at any rational r<1. Monotonicity extends this to every real r<1. At r=1 an infinite C percolates deterministically, so p_c(C)=1. Countability handles every vertex and component simultaneously. If p_c=0 the original critical graph has only isolated vertices, so no infinite component exists. This proof does not need quasi-transitivity.

L2. Finite common-edge energy implies survival.

Let H be a connected locally finite graph with root o. Let mu be a Borel probability measure on its infinite simple rays starting at o. For independent gamma,gamma' sampled from mu let K be the total number of shared undirected edges (possibly infinity). If 0<r<1 and I_r(mu)=E[r^{-K}]<infinity, then iid bond percolation on H with retention r satisfies P_r(o connects to infinity)>=1/I_r(mu)>0.

Proof. For each n put Y_n=integral r^{-n} 1{the first n edges of gamma are open} dmu(gamma). Each prefix uses n distinct edges, so E_r Y_n=1. If k_n is the number of common edges of the two prefixes, independence of the edge states gives E_r Y_n^2=E_{mu x mu}[r^{-k_n}]<=I_r(mu): the union of the two edge sets has 2n-k_n edges. Cauchy--Schwarz gives P_r(Y_n>0)>=1/E_r Y_n^2>=1/I_r(mu). This event implies an open simple path of length n from o. Those latter events decrease with n. Local finiteness and the infinite-path lemma identify their intersection with an infinite open ray from o. Continuity of probability from above proves the bound. No independence of sequential exploration events is asserted.

L3. The energy criterion has an explicit recurrence obstruction.

If I_r(mu)<infinity as in L2, define a_e=mu{a ray uses e}. Then sum_e a_e^2<= (I_r(mu)-1)/(r^{-1}-1). For any choice of edge orientations, the mean signed traversal f(e) is a unit flow from o to infinity, and sum_e f(e)^2 has the same upper bound. Consequently, if H has pairwise edge-disjoint finite edge boundaries D_j of finite vertex sets containing o, then

  I_r(mu) >= 1+(r^{-1}-1) sum_j 1/|D_j|.

In particular no subgraph of the square lattice supports such a ray measure for any r<1.

Proof. Tonelli gives E K=sum_e a_e^2, and r^{-K}>=1+(r^{-1}-1)K. A simple ray has divergence 1 at o and 0 at every other vertex; finite degree allows integration of these identities. Also |f(e)|<=a_e. Summing divergence over a finite vertex set yields net exiting flow 1. Cauchy--Schwarz gives sum_{e in D_j} f(e)^2>=1/|D_j|. Sum over disjoint boundaries. For Z^2, the boundaries of the L-infinity balls of radii j>=0 are disjoint and have 8j+4 edges, so the sum diverges. A flow in a subgraph extends by zero to Z^2, giving the same contradiction. Thus mere infinitude of a cluster cannot supply the L2 hypothesis, even in the square lattice. This refutes that general inference; it does not refute the target theorem.

L4. Explicit bounded-degree counterexample when quasi-transitivity is omitted.

Construct a rooted spherically symmetric tree T. Every vertex at depth n-1 has b_n children, where b_n=4 if n is a positive perfect square and b_n=2 otherwise. T is infinite, connected and locally finite, of maximum degree 5. It has p_c(T)=1/2 and P_{1/2}(o connects to infinity)>=2/7. It is not quasi-transitive: the root is the unique degree-4 vertex (all other vertices have degree 3 or 5), so every automorphism fixes it and preserves infinitely many distance levels.

Proof. The number of depth-n vertices is L_n=2^{n+floor(sqrt(n))}. For p<1/2 the expected number of open depth-n descendants is p^n L_n=(2p)^n 2^{floor(sqrt(n))}, which tends to zero. An infinite open root component needs an open descendant at each depth, so its probability is zero by the first moment. The same argument starting at any fixed vertex works for descendant rays; any infinite simple ray in a rooted tree eventually travels away from the root, and a countable union gives no infinite component at p<1/2.

Take mu to choose uniformly among children at every step. Two rays sharing n edges have probability 1/L_n. On a tree common edges form a prefix, so P(K>=n)=1/L_n. The tail-sum identity yields

  E[2^K]=1+sum_{n>=1}(2^n-2^{n-1})/L_n
          =1+(1/2)sum_{n>=1}2^{-floor(sqrt(n))}
          =1+(1/2)sum_{k>=1}(2k+1)2^{-k}=7/2.

L2 at r=1/2 yields positive critical survival and the bound 2/7. This also proves p_c<=1/2 and hence equality. L1 still applies: its surviving critical components have quenched threshold 1. Therefore the existence of a good ray measure on the host graph does not imply that a surviving critical component inherits a measure with finite energy for a thinning retention below one.

Single hardest gap and route verdict.

For a graph class where L2 could apply, prove from quasi-transitivity plus a hypothetical infinite critical component that such a component supports finite I_r for some r<1. No such implication has been established. L3 shows this route cannot handle all recurrent graph classes by a universal ray-measure construction. A complete P0043 proof would need a separate recurrent-class argument and a new critical-cluster robustness argument in the remaining classes. General target status: UNPROVED BY THIS PACKET. Auxiliary statements: author-proved, not independently checked.

L5. Correction of the critical-susceptibility inference in the prior attempt.

For the infinite d-regular tree, d>=3, p_c=1/(d-1), no infinite critical cluster exists, and nevertheless chi_o(p_c)=E_{p_c}|C_o|=infinity. In fact the expected number of critical open vertices at every level n>=1 is d/(d-1), so the expected number within radius N is 1+Nd/(d-1).

Proof. Away from the root the open descendant process is Galton--Watson with offspring Binomial(d-1,p). Below critical its expected generation size tends to zero; at critical the offspring law has mean 1 and is nondegenerate, and its extinction probability is 1. One can check extinction directly: for 0<s<1, (1-p+ps)^{d-1}>s at p=1/(d-1) by strict convexity and tangency at s=1, so 1 is the only generating-function fixed point in [0,1]. Above critical the convex generating function has a fixed point below 1, hence positive survival. The finite number of root branches does not change these conclusions. At level n there are d(d-1)^{n-1} vertices, each connected to the root with probability p_c^n by its unique path. Their expected open count is d/(d-1). Tonelli proves divergence. This is a classical computation, not a new theorem. It refutes the speculative critical-finiteness step in C0084-A001. Hutchcroft's Theorem 6 asserts finite expected cluster size for p<p_c; it does not assert it at p_c.

Validation. `python -X utf8 ~/brain_workers/w435/check_auxiliary.py` passed 48 finite checks across 9,312 exact configurations. The critical square-branching tree's depth-4096 root survival is approximately 0.5216912443, consistent with the proved lower bound 2/7. Finite-depth values are not an infinite-limit proof. Full counts and the fresh compute gate are in MEASUREMENTS.json and COMPUTE_GATE.json.

Original P0043 record recovered. STORE_SOURCE_ROWS.json preserves the exact statement and regular-tree attempt from the read-only population store. The statement cites Lyons--Peres, Conjecture 8.15, printed p.285, electronic version 19 August 2026. Its prior proof is the valid regular-tree branching fixed point, with loop dependence explicitly left open. This packet reuses critical regular-tree extinction only as a classical fact in the susceptibility correction; the independent route is L1--L3. The book locator itself was not recovered in two public-PDF searches; the precise bond statement is independently checked in Hutchcroft's primary paper. Current peer boundaries: w432 uses finite-radius pivotal concentration; w438 uses a polynomial tree threshold. The square-generation control here uses a different profile and is not a novelty claim.

Adversary feedback accepted. w436 independently kept L1--L4 in AUDIT_w435.md and marked G1 FIX. G1 is now recorded as an unproved completion premise, not a proposed proved lemma. This agrees with the explicit hardest gap: derive critical-cluster robustness from quasi-transitivity in an applicable class. The full target remains unproved. Assigned referee w437 has the original packet; its audit is still pending.
