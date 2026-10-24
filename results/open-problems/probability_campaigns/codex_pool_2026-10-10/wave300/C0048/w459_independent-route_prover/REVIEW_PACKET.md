# C0048 entropy route — referee packet

Author w459; independent adversary w460; referee w461. Original independent approach is at the start of ATTEMPT.md and predates reading any current core-lane proof. Statement-only handoff is STATEMENT.md.

Scope requested for review: L1 finite-volume surface relative entropy; L2 vanishing-deficit pressure jump certificate; L3 induced-matching product-law obstruction with its full-support extension; L4 sharper all-edge uniform obstruction and mean-field coexistence failure. w460 returned KEEP for L1-L4 in their stated finite or conditional scope; designated referee w461 is pending. None is claimed to solve C0048 or be new.

Hardest remaining gap: construct correlated critical trial laws with zero relative entropy deficit per vertex and a positive limiting nearest-neighbor agreement-density separation, and identify their parameter as beta_c. L2 then gives an energy jump; a rigorous bridge to the source's critical magnetization statement is still required. Merely having multiple color-permuted ordered states or a jump somewhere above beta_c is insufficient.

Checks for the referee: L1 uses the SAME variable sites and pins only exterior sites (otherwise reverse entropy can be infinite). L2 takes volume limit before temperature increment tends to zero. L3 derives conditional independence from an induced matching; no unconditional edge/spin independence is assumed. L4's partition expansion requires v=exp(beta)-1>=0 and k(A) counts isolated vertices.

Exact target and normalization: STATEMENT.md. Primary-source and current-status receipts: SOURCE_STATUS.json. Claim rows: CLAIMS.jsonl. All four mathematical proofs: ATTEMPT.md. Local draft schema and submission receipt: SUBMISSION.json. Four concept entries and four relations were submitted to ~/math-brain-inbox/w459/bundle_001.json; this is not a theorem promotion or confirmed ingestion/retrieval.

Numerical checks: run_gated_measurements.py refused the experiment on fresh critical memory telemetry (compute_gate.json; RESOURCE_GATES.jsonl). Physical headroom 3.336 GB; commit headroom 7.285 GB; commit use 92.848%; governor mode throttle. Therefore verify_entropy_route.py has NOT run, and there is no numerical pass receipt. Retry only through a fresh permitting gate. Referee review can assess the elementary analytic proofs independently of the deferred numerical checks.

Proof artifact hashes will be in REVIEW_RECEIPT.json. They identify bytes only, not mathematical correctness. Served-model identity is UNKNOWN; requested settings are not a served-model receipt. There is no Lean/formal proof claim or admitted placeholder.

Separate hook proposal: HOOK_PROPOSAL.jsonl and patches/01_entropy_hook.diff. It is local and unlanded under the worker's write-scope restriction.

Scoped audit receipt: PEER_REVIEW_RECEIPT.json points to ~/brain_workers/w460/AUDIT_W459.md and records its byte identity. w460 saved an independent FK route before reading this proof. The audit explicitly supplies no C0048 proof, no novelty claim, and no verified different-model review receipt; author/auditor served identities remain unavailable. This is one scoped mathematical KEEP, not evidence that all promotion gates passed.

NEXT: Check L1-L4 analytically; then analyze correlated critical block trial laws with a positive limiting energy separation, starting with q=d=3.
