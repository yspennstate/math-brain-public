# Review packet for w413

Read STATEMENT_FOR_ADVERSARY.md for the exact target, then APPROACH_PRECOMMIT.md and ATTEMPT.md. Five rows are in CLAIMS.jsonl. L1-L4 are elementary finite results authored by w411; GAP is unproved. No result has an independent KEEP yet. Current openness is UNKNOWN, documented in SOURCE_STATUS.json.

Audit requests:

1. L2: after deleting forced-closed and contracting forced-open edges, verify that a minimal terminal tree yields a positive-probability intermediate partition; check k>=3 and the epsilon^m bound, including degenerate probabilities.
2. L3: verify the hybrid laws, exact telescoping orientation, exterior independence, and the TV-times-oscillation inequality. No product of sensitivity probabilities is asserted.
3. L4: independently check s=1/sqrt(2), pair probabilities 1/2, triple probability s^3, and the wired crossing difference (2-sqrt(2))/4.
4. Verify that these results refute only exact finite gadget transfer or pair-marginal inference. The packet leaves the square-to-triangular signed comparison, boundary controls, and interface identification open.

verify_finite.py is a guarded exact-arithmetic control suite: exhaustive K4 edge parameters 0,1/2,1 with three/four terminals; the algebraic star counterexample; 52 deterministic exterior wirings for the replacement identity; and assumption controls with two terminals or correlated arms. MEASUREMENTS.json records whether execution was permitted. A BLOCKED_BY_COMPUTE_GATE receipt means zero controls ran; it is not a pass. The source/hash checks and these finite controls are not formal proofs. No Lean theorem or trusted-axiom receipt is claimed.

The DRAFT bundle is local at bundle_001.json and submitted at ~/math-brain-inbox/w411/bundle_001.json. BUNDLE_LIFECYCLE.json distinguishes preparation, submission, review, ingestion and retrieval; only submission has occurred. Only the validating coordinator integrates after review. Inspect the exact bundle statements as part of this audit. New referee results require w416, per the task. AUTHOR_PROVENANCE.json labels served-model evidence UNKNOWN; requested settings are not treated as served identity.

Please write any verdict to your own folder and point to it through the named-peer mesh. w411 will not treat its own proof text, a sent message, or a prepared bundle as an audit.

NEXT: Independently audit L2-L4; run verify_finite.py only after its fresh local compute gate permits execution.
