# P0297 review packet for w521 and claude-4a88bc43

This packet does not solve P0297. Its usable result is a precise obstruction to closing an exact-dimension argument by scalar covariance or thick-point maximization. The independent snowflake route was saved in ATTEMPT.md before w519's proof was read. The completed-square derivation is in INDEPENDENT_DERIVATION.md. Both remain pending independent review.

Referee action: check claims w520.P0297.snowflake.002 and w520.P0297.profile.003. For the snowflake proof, check the cover-mesh conversion and the successive-hitting-time argument for EVERY path on the interval. It intentionally fails the length axiom and is a counterexample only to a reduced scalar inference. For the profile proof, check positive denominators throughout -2<=alpha<=2, the unique equality case alpha=gamma, and exclusion of gamma=2. Do not infer a common almost-sure event over uncountably many alpha or an uncountable-union dimension rule.

Narrow audit of original peer work: KEEP W519-L1 as available in ~/brain_workers/w519/ATTEMPT.md and CLAIMS.jsonl (ATTEMPT.md observed as 1,410 bytes, last-write 2026-10-10 08:11:45). The exact audited statement is: positive a(epsilon),L(epsilon), with log(a)/log(epsilon)->alpha and log(L)/log(epsilon)->0 as epsilon decreases to zero, have log(a*L)/log(epsilon)->alpha. Independent proof: the ratio for the product is the sum of the two ratios. This does not identify alpha, imply any quantitative error rate, or give uniformity in another parameter. No claimed full proof was present in that snapshot.

The single hardest unresolved mathematical piece is an independently evaluated LFPP crossing exponent lambda(xi)=lim log(a_epsilon)/log(epsilon), or an equivalent genuine metric/geodesic estimate. The established relation lambda=1-xi*Q(xi) and xi=gamma/d_gamma only changes parameters. w519's subpower lemma and this packet's profile maximum each leave that input unknown.

Primary references and exact statement locations are in SOURCE_STATUS.json. Current openness remains UNKNOWN: the dated July 2026 survey reports general d_gamma as open, but a targeted check is not an exhaustive owner-work or later-literature certification. No formal theorem receipt or novelty claim is made.

The brain handoff is drafts/bundle_001.json: three DRAFT concepts, four relations with quoted supporting ends, and no theorem promotions. Two relations have endpoints already verified in the read-only store: the P0297 problem and the prior scalar-scaling attempt. reports/context_receipt.json records those exact cards. The prior attempt already recognizes that scalar shifts do not calculate xi; this packet adds a cover-based countermodel and the completed-square profile identity. patches/01_p0297_draft_bundle.diff names the intended live inbox path. drafts/lifecycle.json records prepared/submitted/reviewed/ingested/retrievable separately. Local schema and exact arithmetic checks are recorded in measurements.json; they do not replace your mathematical check. After mathematical review, the coordinator can place the complete JSON in ~/math-brain-inbox/w520/bundle_001.json using a .part file and a final rename. Live integration was not run.

The hook proposal is hooks/proposals/math-w520.jsonl, using the hooks1000 README schema with a fire case and a silent case. It is staged locally because the brief expressly forbids shared writes and mesh sends. The same restriction leaves the progress and peer notices below unsent; they are concrete handoffs, not claims that anybody received them.

Progress handoff: w520 finished the P0297 independent metric/profile obstruction and narrow W519-L1 KEEP; 3 draft brain concepts and 4 relations are ready for w521 review. Evidence: ~/brain_workers/w520/REVIEW_PACKET.md. Row: S1.P0297.w520.

Peer claim handoff: w520 takes the deterministic thick-point completed-square and reduced-covariance snowflake obstruction; no exact LFPP computation or shared artifact is claimed. Evidence: ~/brain_workers/w520/INDEPENDENT_DERIVATION.md.

Peer done handoff: w519's W519-L1 is kept narrowly; w521 should check w520 claims .002 and .003 and then pass the draft bundle to claude-4a88bc43. Evidence: ~/brain_workers/w520/CLAIMS.jsonl.

NEXT: w521 checks the completed-square identity with its positive denominator and the all-path hitting-time snowflake argument, and returns claim-level verdicts for .002 and .003.
