# Scoped adversarial audit of w561

Author/auditor: w562, 2026-10-10. Referee for the triad: w563. Source: ~/brain_workers/w561/ATTEMPT.md, L01-L05. A frozen copy and SHA-256 receipt are attached by the packet builder. Independent derivation was saved in independent_obstruction.md before this proof was read.

Verdict: KEEP the conditional deductions L01-L05 within their stated assumptions. No proof of C0047 follows from this packet because critical operator boundedness is an explicit extra premise. This is an audit of the original derivation, not an audit of another review.

L01. The tree forward offspring distribution is Binomial(d-1,p); at p=1/(d-1) it is critical and nondegenerate for d>=3. The chosen off-geodesic branches and their attaching edges have pairwise disjoint supports. Independent Borel-Cantelli therefore proves infinitely many isolated infinite clusters for each fixed p in (p_c,1). The argument requires these cut edges; it supplies no corresponding separation in a general Cayley graph.

L02, the important bridge. I separately obtain the derivative bound in each finite induced H. Russo's formula sums the probabilities that an edge is pivotal, without fixing its state. A pivotal edge {u,v} supplies edge-disjoint open connections x-to-u and v-to-y, or x-to-v and u-to-y, in H with that edge deleted. BK bounds each disjoint occurrence by the product of the two marginal connection probabilities. Enlarging back to H increases those marginals. Summing both orientations gives T'_p <= T_p A_H T_p entrywise. This justifies the multiplication; ordinary dependence of overlapping path events is never ignored. A factor 1/(1-p) would belong to a formula using an edge-closed pivotal event; this proof uses unconditional pivotal probabilities, so no such factor is missing.

For the norm step, nonnegative matrices satisfy |Bf|<=C|f| when B<=C entrywise, and hence ||B||<=||C||. With f_H=||T_p^H||, local Lipschitz continuity and the integral norm inequality give f'_H<=a f_H^2 almost everywhere. Since f_H(p0)<=M, integration gives f_H(q)<=M/(1-aM(q-p0)) only when aM(q-p0)<1. Monotone convergence of finite-volume connections for finitely supported nonnegative test functions yields the uniform bilinear-form bound in G. Absolute values handle arbitrary complex test functions. No boundedness at q is assumed in advance.

I checked the entrywise derivative inequality by independent exact configuration enumeration on triangle, cycle-four and diamond graphs at p=1/4,1/2,3/4: 123 ordered-pair inequalities passed (pivotal_measurement.json, 0.0201 s). These are finite controls; the written argument above, not enumeration, supports the infinite-volume implication.

L03. Countability plus almost sure existence and transitivity imply theta>0. FKG then gives tau_p(x,y)>=theta^2 whenever uniqueness holds. An infinite constant lower bound on a column forbids an l2-bounded operator. Downward closure of operator boundedness suffices for p_{2->2}<=p_u; no unsupported uniqueness comparison is needed.

L04-L05. The tree column-square calculation and adjacency Rayleigh quotient have the correct normalization. The all-walk Neumann majorant proves only p_c<1/||A|| => p_c<p_u. With normalized rho, ||A||=d*rho. Our independent normalization finding agrees with these sections; retain one correction row if deduplicating the triad's bundles.

Minimal missing premise for the parent's proof in this packet: ||T_{p_c}||_{2->2}<infinity for the prescribed generating set. A recent September 24, 2026 primary manuscript states exactly this estimate in Theorem 1.1 and every fixed generating set in Corollary 1.2. Its 53-page proof has not been independently certified here. Therefore this audit neither certifies present openness nor certifies a new solution.

NEXT: Referee-check w562's distinct bounded-congestion coupling; the unclosed route step is preservation of separation after extra base edges are opened.
