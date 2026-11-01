# Independent audit of w441's P0043 bridge

Input: ~/brain_workers/w441/ATTEMPT.md, read after independent C001-C003 were saved. Reviewer: w442; referee for w442's own new claims: w443. This is an audit of the proof, not another audit.

L002 (quenched thinning obstruction): KEEP as an elementary conditional deduction. For each fixed rational q with pq<p_c(G), fresh independent thinning makes the marginal configuration Bernoulli-pq. Tonelli gives a probability-one set of configurations on which conditional survival is zero. Intersecting over countably many rationals is legitimate, and countability handles all components. At p=p_c>0 it gives p_c(C)=1. The division by p requires p>0; the target has p_c>0 because quasi-transitivity and local finiteness imply a uniform finite degree bound. No selected cluster is treated as independent of the original configuration.

L003 (uniform bounded corridors): KEEP. Depth n has b^n distinct embedded vertices within ambient radius Ln. For arbitrary radii use floor(r/L), rather than just a subsequence. Both injectivity and uniform L are essential; variable-length or overlapping routes are outside the claim.

L004 (positive rooted expansion survives thinning): KEEP under its stated assumptions. A canonical depth-first spanning-tree walk gives an injective encoding of each rooted n-vertex connected set by a walk of length 2(n-1), bounding the number by Delta^{2(n-1)}. Closing its edge boundary has probability (1-q)^{|boundary K|}; the root-cluster event is a subset of this event. The sum is a union bound, not a product of conditionally dependent cluster events. With a=(1-q)^h<1/(Delta^2+1), a/(1-Delta^2 a)<1. Fresh independent bits are indispensable. The definition used is an infimum over ALL rooted finite connected sets; the usual asymptotic anchored constant is a different definition, though positive asymptotic anchored expansion also implies a positive all-size infimum here because small rooted sets have size bounded and nonempty edge boundary.

L004b: KEEP as a necessary-property conclusion. Countably many rationals and vertices make the simultaneous conditional contradiction sound. It shows that every putative infinite critical cluster has zero rooted expansion; it does not exclude such a cluster.

L005 (decorated-ray witness): KEEP. For all sufficiently large radii use n=floor((r-1)/2), yielding the liminf growth lower bound sqrt(2). Each infinite path must ultimately follow the spine, whose q-open tail has probability zero for q<1. The missing quasi-transitivity is real: deleting a spine vertex s_n exposes finite components of sizes 2^{n+1}-2 and 2^{n+1}-1 (omit the empty prefix for n=0), distinguishing infinitely many rooted vertex types.

The attempted general bridge remains OPEN. L002 says hypothetical infinite critical clusters must be fragile under every q<1 thinning. L004 contradicts fragility only with positive rooted expansion. Independent C003 proves that this sufficient premise is impossible for every infinite connected subgraph of every bounded-degree subexponential ambient graph. Thus anchored expansion cannot settle the subexponential target by supplying that premise. A new percolation-specific mechanism, not density plus anchored expansion, is required.

No full proof of P0043 is certified. These KEEP verdicts are one independent worker's mathematical audit; they are not two-login admission receipts or formal-check receipts.

NEXT: w443 checks C003 independently; use a finite gluing mechanism whose hypotheses hold on subexponential graphs instead of positive anchored expansion.
