# P0043 referee attempt

Date: 2026-10-10. I audited source quantifiers and the two assigned peers. The original Benjamini–Schramm Conjecture 4 concerns site percolation on connected locally finite almost-transitive graphs and explicitly assumes p_c<1. It says the nonplanar questions extend to bond percolation. Hutchcroft (2016) restates the bond conjecture and proves the exponential-growth case. See SOURCE_STATUS.json for primary URLs and short quotes.

I independently derived the tree reciprocal identity, the beta=1 survival boundary and one-arm rates in w438-C02/C03, the periodic-tail and quasi-isometry constructions in w438-C04/C05, and the exact subdivision formulas and constants in w439 claims 002/003. Reproductions and scoped KEEP verdicts are in REVIEW_PACKET.md. These results give boundary tests and counterexamples to stronger auxiliary bridges, not a solution of the parent conjecture. I found no unsupported multiplication of conditional probabilities inside either tree proof; it would become invalid if copied to a graph exploration with overlapping branches.

## New sharp special case: a quasi-transitive graph with cycles

For integer m>=2, begin with the infinite 3-regular tree. Replace every original edge {x,y} by m internally vertex-disjoint paths x-z_j-y of length two, with fresh internal vertices z_j. Call the resulting simple graph D_m. It is infinite, connected, locally finite, and quasi-transitive: the original vertices form one orbit and all inserted vertices form a second orbit. Original vertices have degree 3m; inserted vertices have degree 2. Every replaced edge is a finite cyclic block (for m>=2).

In Bernoulli bond percolation at edge parameter p, declare an original edge usable when at least one of its m two-edge paths is fully open. These blocks have disjoint edge sets, so usable indicators are independent with exact retention

    r_m(p)=1-(1-p^2)^m.

An infinite open cluster in D_m exists iff an infinite cluster of usable original edges exists in the 3-regular tree. For the forward binary tree, the offspring law is Bin(2,r); survival is zero for r<=1/2 and positive for r>1/2. Hence the exact threshold is

    p_c(D_m)=sqrt(1-2^(-1/m))<1,

and at p_c there is almost surely no infinite open cluster. The equivalence uses that every block is finite: an infinite graph cluster must contain infinitely many original vertices. It does not multiply branch events after overlapping exposures; independence holds because the blocks use disjoint edge coordinates.

There is also an exact sharp critical one-arm constant. Let u_0=1 and u_(k+1)=1-(1-u_k/2)^2=u_k-u_k^2/4 be the probability that a forward usable-edge branch reaches k original levels at criticality. Then u_k decreases to zero, and

    1/u_(k+1)-1/u_k=1/[4(1-u_k/4)] -> 1/4,

so k u_k ->4. The original root has three usable branches, so its probability q_(2k) of reaching graph distance 2k is 1-(1-u_(k-1)/2)^3, and k q_(2k)->6. In D_m inserted vertices have odd root distance and original vertices have even root distance, so the sphere of radius 2k consists exactly of original vertices at tree depth k. Consequently

    lim_(k->infinity) (2k) P_(p_c)(o connects to graph distance 2k)=12.

This extends the peer subdivision calculation to a cyclic block graph; it is a special case already implied qualitatively by Hutchcroft's exponential-growth theorem, not a new solution of P0043. The proof is author-only until w443 checks the block equivalence and exact constant. Its value is an exact stress test showing which cyclic dependence can be integrated into independent coarse edges.

The hardest unresolved mathematical step in this packet is a conditional finite-scale extinction mechanism for all subexponential-growth quasi-transitive graphs at p_c<1, especially when graph loops prevent disjoint-branch recursions. A recent pinned OpenAI release claims a full bond proof. Its comparator has a `sorry` placeholder, while the separate solution module states the matching theorem and calls deep imported lemmas. I did not rebuild the import graph or check trusted axioms, so full-proof status is UNKNOWN and the site form is not certified by that bond module. The next referee step is a narrow audit of the top-level imported classification lemma and an actual clean axiom/build receipt, not another open-status search.

NEXT: Have w443 audit the cyclic-block reduction and the 12/r critical one-arm constant; keep this author-only result out of theorem ingestion until that review.
