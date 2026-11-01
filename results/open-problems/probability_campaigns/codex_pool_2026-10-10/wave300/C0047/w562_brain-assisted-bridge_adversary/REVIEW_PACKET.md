# w562 / C0047 review packet

Review-ready deliverables: source correction, exact route counterexample, a candidate coupling, scoped adversarial audit, and one measured retrieval repair. Assigned independent referee: w563. If the referee originates a new mathematical result, its independent referee is w566.

The candidate coupling requires the same countable vertex set, simple fixed paths, uniform route length L, uniform edge congestion M, and iid Bernoulli bond laws. Its conclusion is an existence coupling and a p_c upper bound. It supplies no p_u lower bound or cluster-merger control. Read bridge_derivation.md for the countable-product argument, endpoints p=0,1 and the critical-point limit. The independent_obstruction.md record was saved before the paired proof was read.

| Item | Evidence | Review scope / unresolved premise |
| --- | --- | --- |
| S1.w562.002 | CLAIMS.jsonl, target_cards.json, ATTEMPT.md | Correct normalized-rho criterion; source-backed correction, deduplicate with w561 |
| S1.w562.003 | independent_obstruction.md, overlap_measurement.json | Complete two-route counterexample; no parent refutation |
| S1.w562.004 | bridge_derivation.md, overlap_measurement.json | Candidate slot coupling; independent mathematical check required |
| S1.w562.005 | math_recall_measurement.json, fallback_measurement.json | 0/2 target cards in top six to 2/2 by exact key; one-target evidence |
| w561 L01-L05 | AUDIT_W561.md, W561_ATTEMPT_SNAPSHOT.md, PAIRED_PROOF_RECEIPT.json, pivotal_measurement.json | Conditional KEEP; critical operator boundedness not supplied |

The original primary source is [Benjamini-Schramm 1996](https://emis.de/ft/41630), Conjecture 6 and Theorem 4. The intake's exact group formulation is [Duminil-Copin, Conjecture 2, page 4](https://arxiv.org/pdf/1712.04651). A [September 2026 manuscript](https://github.com/openai/math/blob/main/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf) asserts the critical operator bound in Theorem 1.1 and the fixed-generating-set statement in Corollary 1.2. SOURCE_STATUS.json separates statement verification from proof verification. No claimed formal receipt or admitted comparator establishes a theorem here.

The deployed recall's only generic spectral-radius hit defines the spectral radius of a bounded operator. RETURNED_SPECTRAL_CARD.json records its full body and metadata. It supplies no percolation hypotheses, graph normalization, supercriticality, or nonuniqueness conclusion. The comparison needed for the proof is in BRAIN_COMPARISON.md. The optional fallback exposes full target cards as unverified material; it does not turn them into theorem evidence.

The four concept entries and five precisely supported relations are in draft_bundle_001.json and EDGE_AUDIT.jsonl. Submitted DRAFT: ~/math-brain-inbox/w562/bundle_001.json. SHA-256: b1f06b78783a796ffc7cd588d6e8439510c81d8549905c64dc694eef8041cf24. BUNDLE_RECEIPT.json records submission only; reviewed/ingested/retrievable remain false until evidence arrives. All relation ends are quoted; the refutes edge targets only the degree-free route in the stored attempt.

Patch: patches/01_candidate_target_fallback.diff. Validation: check_candidate_fallback.py, check_overlap.py, check_pivotal_bound.py, verify_packet.py. Measurements: 2/2 exact-key target cards in 0.227 s, four invalid IDs rejected, one absent-candidate control, three overlap/disjoint cases, 48 slot inclusion assignments, 123 pivotal inequalities. No broad performance or parent-solution conclusion follows.

MODEL_PROVENANCE.json records served model UNKNOWN; requested model/reasoning/tier are not served identity evidence. ARTIFACT_HASHES.json fingerprints review inputs, without store seals or integration manifests. REPORT.md contains the apply line and limitations. HOOK_PROPOSALS.jsonl is a staged narrow hook with one fire and one silent case, not a live hook change.

NEXT: Referee-check S1.w562.004; integrate only approved draft concepts/corrections and optional read-only lookup, leaving the merger and current-status boundaries explicit.
