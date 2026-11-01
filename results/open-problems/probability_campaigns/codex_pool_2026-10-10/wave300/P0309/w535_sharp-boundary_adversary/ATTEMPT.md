# P0309: finite-temperature support boundary

The exact intake and source locators are in SOURCE_STATUS.json. Current openness is UNKNOWN. The review supplies predicted regimes and a phase-law definition, rather than a proved universal transition threshold. The working lane is the ordinary short-range s>3 grand-canonical model.

The independent deliverable is INDEPENDENT.md: with finite activity z and nonnegative interaction, the empty configuration has local weight one and the partition sum is at most exp(z|B|). Therefore P(empty B | outside)>=exp(-z|B|). A tower-property induction over disjoint regions gives P(all m regions occupied)<=(1-exp(-zV))^m. Passing over countable tails and integer radii forces arbitrarily large holes. A full-rank lattice has a finite covering radius, so no configuration with such holes can admit a globally bounded displacement bijection from any full-rank lattice, even one selected from the configuration.

For zV=log(2), the analytic bound for ten disjoint regions is 1/1024. This is an exact consequence of the proof, not a measured probability for a simulated Riesz gas. Equality in the universal bound is attained by the zero-potential Poisson specification.

This defeats only a stronger auxiliary bridge requiring global lattice localization. It leaves periodic probability laws and finite local displacement moments possible. No result is extended to a renormalized long-range or fixed-count specification.

Read order: independent proof saved before paired statement and proof. The paired proof is now directly audited in AUDIT_W534.md: KEEP its s>3 alternating-plane and finite-support instability lemmas. Neither special case solves P0309. w536 is the assigned independent reviewer and has returned KEEP; see REFEREE_W536.md for the independent reproduction.

The single hardest open piece is construction of an unpinned non-translation-invariant Gibbs law through a uniform nonlinear free-energy/order bound that handles defects and competing phases for a stable candidate.

The fresh compute gate reported distress/process_critical. No numerical experiment was launched. Static bundle validation and serialization below belong to completing this checkpoint; they are not mathematical proof certification.

NEXT: coordinator checks the independently reviewed ordinary-DLR scope in the active DRAFT, integrates the lemma, and verifies retrieval.
