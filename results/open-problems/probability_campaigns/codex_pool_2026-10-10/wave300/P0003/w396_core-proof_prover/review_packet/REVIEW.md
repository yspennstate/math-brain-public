P0003 draft for w398, 2026-10-10. Full target not proved; no independent KEEP received.

Read ATTEMPT.md and SOURCE_ADDENDUM.md first. Audit L0' (remaining length), L1 (finite optional stopping including terminal prefixes), L2 (TV convention), L3 (closed obstacle and collar-limit hypotheses), and first-entrance counting inequality (U). Check that no ensemble equivalence, conformal exponent, tightness, or open-status assertion is smuggled in.

CLAIMS.jsonl records exact statements, assumptions, proof/counterexample, assigned reviewer and gap. SOURCE_STATUS.json records primary provenance separately. The initial STATEMENT_FOR_ADVERSARY.md is preserved; its initial ensemble identification is corrected explicitly in SOURCE_ADDENDUM.md. w397 received it before the proof (msg-168e5faa4e).

Reproduction: python -B -X utf8 ~/brain_workers/w396/local_checks.py . Current check status: DEFERRED_COMPUTE_GATE; assertions run: 0. A closed gate exits 3 and must never be labeled PASS. No formal proof assistant was run.

Draft: ~\brain_workers\w396\drafts\bundle_001.json . Schema checks validate 7 entries and 7 relations, not mathematics. Source license is owner-own-work; proofs are original campaign writeups of elementary arguments, with no novelty claim. Any integration/retrieval must be separately recorded after mathematical review.

Main attempted gap: H_disk. Additional full-target gaps: H_len, curve tightness and continuum conventions; the related chordal H_5/8 route and any ensemble transfer are unproved.

Submission receipt: ~\math-brain-inbox\w396\bundle_001.json; seven entries and seven relations. Mathematical review requested from w398 as msg-13de88a071. No verdict received; ingestion and retrieval remain unverified.

NEXT: Return a mathematical KEEP/FIX/DROP verdict on L0', L1--L3 and (U); send your own new results to w401 for independent review.

Peer audit received: w397 KEEP on L0/L0prime, L1--L3 under (C), and (U); source ~/brain_workers/w397/REVIEW_w396_proof.md. Citation correction applied in ATTEMPT.md and SOURCE_STATUS.json. One draft proof clarification is ready in patches/02_initial_filtration_expectation.diff: E D_0 replaces D_0 when the abstract F_0 is nontrivial. The local draft includes this clarification; the submitted draft is left for the reviewer to patch before integration. No cross-login admission or assigned-referee verdict is claimed.

NEXT: w398 audit the corrected packet and apply the draft clarification before integration.
