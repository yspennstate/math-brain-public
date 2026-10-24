# P0043 review packet for w443

Exact target and source status: STATEMENT.md and SOURCE_STATUS.json. The corrected scope is infinite connected locally finite quasi-transitive undirected G, independent Bernoulli bond percolation, p_c(G)<1, no infinite cluster at p_c. Theorem 1.1 on page 2 of the 24 September 2026 primary manuscript claims this exact target. This packet neither independently verifies that manuscript nor claims a new full proof. No Lean receipt is asserted.

The prior brain card is `math:probability.core:attempt-p0043-absence-of-infinite-clusters-at-critical-percolation`, explicitly an unverified concept. Its regular-tree fixed point assumes independent isomorphic forward subtrees. Our substantive attempt replaces that step with fresh thinning and an explicit conditional survival criterion; the general bridge remains missing.

Please check the written lemmas in ATTEMPT.md against the exact rows in CLAIMS.jsonl:

- L001: the graph Z has p_c=1 and theta(1)=1; p_c<1 is essential.
- L002: Tonelli and a countable intersection over rational q give the quenched cluster threshold lower bound. Check that the statement covers every component and that no adaptive choice of q is silently treated as independent.
- L003: an injective b-ary tree with uniformly bounded image edge lengths forces exponential volume. Check both injectivity and the uniform length bound.
- L004: connected n-sets have at most Delta^{2(n-1)} canonical traversal codes. Closing the whole boundary gives a/(1-Delta^2 a); require a<1/(Delta^2+1). Different candidate finite clusters are not multiplied as independent events.
- L005: finite binary grafts give growth at least sqrt(2), while the unique infinite ray gives p_c=1. Check the claim that infinitely many finite-component-size patterns exclude quasi-transitivity.
- L006: combine p_c(C)>=p_c(G)/p and p_c(C)<=1-(Delta^2+1)^(-1/h), then check the signs of the logarithms. The almost-sure assertion is for each fixed p, not all uncountably many p at once.

w442 reported KEEP L002-L005 after an independent start. Their own C003, in w442/ATTEMPT.md lines 25-37, proves zero anchored expansion for every infinite subgraph of a bounded-degree subexponential ambient graph. Please check C003 independently. ADVERSARY_RESPONSE.md records its effect: the positive-expansion route is CLOSED for that class. This remains a partial proof packet.

The single hardest remaining gap: a Bernoulli-specific mechanism for zero-anchored-expansion critical clusters that supplies a contradiction or actual survival at one fixed subcritical parameter. No finite-radius continuity, unjustified branch independence, or volume-growth transfer supplies that step.

Proof ingredients use countable product measures, Tonelli, monotonicity, countable intersections, finite traversal coding, a union bound and elementary logarithms. MATH_CHECKS.json records exact finite checks. They are corroboration of those ingredients, not a formal proof of the infinite theorem. If w443 contributes a new result, its independent referee is w446.

Brain handoff: drafts/bundle_001.json contains eight DRAFT entries and five relations. EDGES.jsonl quotes both supporting ends. All original deductions use owner-own-work; refuted candidates are concepts with null proof_text. DRAFT_SCHEMA_CHECK.json records structural validation only. BUNDLE_STATE.json distinguishes preparation/submission/review/ingestion/retrieval. The schema check and hashes, if later supplied by an integrator, do not replace mathematical review.

NEXT: Save a KEEP/FIX/DROP verdict for L002-L006 and C003 with the exact assumption or proof line involved; retain the full-target gap explicitly.
