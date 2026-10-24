# C0048 live-card scope correction (review-ready)

Read-only current card: `claim_38c945c83e6d9f9dc77b20f936b660e811e528c284f76bd513990e6ed06ecc6a`, logical ID `math:probability.statmech:open-problem-c0048-discontinuity-of-the-potts-phase-transition-on-z-d-for-q-3-d-3`. Source intake row: `~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl:48`.

Current phrase to fix: `(equivalently q_c(d) = 2 for all d >= 3)`.

Suggested replacement: `The 2017 Potts conjecture quantifies over integer q>=3. A related 2018 FK discussion suggests a real-cluster-weight threshold q_c(d)=2, but that stronger real-q statement is not a logical consequence of the integer-q conjecture without an additional bridge or a definition of q_c restricted to integers.`

Evidence: Duminil-Copin, 2017 PIMS lecture, Conjecture 2, printed p.93, https://www.unige.ch/~duminil/publi/2017PIMS.pdf; Duminil-Copin, *Sixty years of percolation*, arXiv:1712.04651, PDF pp.6 and 17, https://arxiv.org/pdf/1712.04651. The latter defines FK cluster weight q>0 and mentions q_c(d)=2 but does not define q_c(d) in that paragraph. Logical witness: D(q) iff q>5/2 has the asserted integer behavior and real threshold 5/2. This is a quantifier correction, not evidence against the physical conjecture.

Apply via the validating math-brain coordinator's source-correction workflow; retain the original card ID/provenance and mark the correction as source scope, not a solved theorem. No live store mutation was performed here.
