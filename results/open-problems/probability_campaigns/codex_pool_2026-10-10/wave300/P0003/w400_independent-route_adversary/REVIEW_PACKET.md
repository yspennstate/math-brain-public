# w400 P0003 review packet

Reviewer: w401. Author proofs and counterexamples await an independent mathematical check. No formal checker was run, no admitted theorem is offered, and no complete SAW scaling-limit proof or novelty claim is made.

The exact target is Grimmett, arXiv:2205.07318, Question 2.2, printed page 3: the uniform n-step honeycomb SAW rooted at the origin, with a free endpoint, suitably rescaled. The source leaves the precise rescaling, parametrization and SLE variant unspecified. SOURCE_STATUS.json records that uncertainty and distinguishes the related critical chordal law from Duminil-Copin--Smirnov Conjecture 1. Current openness is UNKNOWN.

Read ATTEMPT.md for the derivations; CLAIMS.jsonl gives exact assumptions, proof or counterexample, status, remaining gap and reviewer for each row. The initial restriction/continuity derivation, its explicit slit example, and the rare-length example were saved before reading the paired proof. After discovering that the store already holds the finite-prefix identity and peers hold buffered avoidance, the distinct deliverable became prescribed-length conditioning and exponent-normalized error control. The finite identities and slit example are background and are not counted as new fleet results.

Please check these three points independently:

1. P0003-w400-005: both rare-length joint laws are within total variation 1/n of the same zero-feature discrete law, which converges to (0,U). Conditioning at L=1/2 instead gives opposite deterministic features. Identical marginal length scaling and a weak joint limit cannot supply the required conditional local limit.
2. P0003-w400-006: use deterministic W=0 and alpha_n=1/n on a fixed small stopped interval. Bounded log h-prime gives uniform convergence of each derivative-power probe to 1. At the three specified initial slits, the raw drifts are alpha_n times (9/8,9/8,33/32). Variance remains zero. This refutes use of raw drift error after a vanishing exponent normalization, not w399's fixed-positive-alpha theorem.
3. P0003-w400-007 and -002: division proves the relative local-limit transfer criterion. The general conditional-limit lemma uses a continuity event, vanishing event mismatch, and a strictly positive limiting conditioning probability. These are sufficient hypotheses; other direct or buffered continuity arguments may also work.

The hand audit of w399's actual derivation found the Taylor/Itô drift, initial determinant 9/32, displayed inverse and upper bounds correct under the stated assumptions. AUDIT_VERDICTS.jsonl preserves that conditional verdict, the unproved exponent passage, and the exact-target scope limit. A fixed initial invertible matrix does not supply global probe coverage, and a chordal fugacity result does not supply the fixed-length/free-endpoint transfer.

The single hardest remaining input for this independent route is a conditional local shape limit at a selected length with relative error, together with endpoint and domain transfer. The related chordal curve/driver convergence and positive common exponent are themselves unproved in the paired packet. None is replaced by finite enumeration or a source/hash check.

Four concept-only drafts are staged in drafts/bundle_001.json. The validating coordinator may ingest after review. Submitted, reviewed, ingested and retrievable are distinct fields in BRAIN_HANDOFF.json. No live mathematical store or recall control was changed. A source license tag is not a proof receipt.

check_obstructions.py contains bounded exact diagnostics, with at most ten vertices and no models, GPU, training or network. COMPUTE_GATE.json records whether a fresh governor reading permits execution. If the gate denies execution, the examples remain analytical derivations and the prepared script is not reported as a test pass. REVIEW_PACKET.md and REPORT.md must be read with that gate receipt.

NEXT: w401 checks the original rare-length and exponent counterexamples and the conditional transfer proofs; the validating coordinator decides whether to integrate the concept drafts.
