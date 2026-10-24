# C0023 boundary audit

The deliverable is a proof audit guard for passing from finite-width graphs to their increasing union. I proved the exact missing quantifier: the connection-radius estimate must hold uniformly over all approximating graphs. A Bernoulli counterexample has no infinite cluster in any fixed strip, but its union has origin percolation probability at least 0.9999955119566373. This refutes the unrestricted auxiliary bridge; it does not refute C0023 or a bridge with extra threshold-convergence hypotheses.

ATTEMPT.md gives the proofs. CLAIMS.jsonl records their assumptions and pending independent review. PAIRED_AUDIT.jsonl contains scoped KEEP verdicts on w426's separator, finite-forest, and selected-relay statements. The four-cycle in PAIRED_AUDIT.md shows why the deterministic forest witness does not extend automatically to cyclic graphs.

Measured with `python -X utf8 ~/brain_workers/w427/verify_boundary.py`: 4,436 exact configurations, 20 correct cut bounds passed, and two wrong-width negative controls failed as intended; computation took 0.057 seconds. For example, at width three and p=1/10 the actual radius-one probability is 0.22048759, exceeding the deliberately incorrect width-one bound 0.2; the correct bound is 0.542. This is an adversarial control, not an assertion that a live store contained that wrong formula.

Measured with `python -X utf8 ~/brain_workers/w427/verify_pair.py`: 24 configurations checked the selected-relay excess 1/16 and the four-cycle's correct product-inequality margin 1/64. Computation took 0.001 seconds. Finite checks support the constants; the general arguments are the written proofs.

The four-entry bundle is concept-only draft material with owner-own-work tags and four exact relations. `python -X utf8 ~/brain_workers/w427/prepare_draft.py` checked its shape, sources, relation endpoints and card-text privacy. Local validation is not integrator acceptance. This proposes a card-level self-checking improvement; live recall benefit has not been measured. Source status remains UNKNOWN because a recent public preprint claims a broader solution and its full proof is unchecked. A by-sorry comparator is not a formal proof receipt and does not refute the separate preprint.

Submission, mathematical review, ingestion and retrieval are recorded separately in SOURCE_STATUS.json and SUBMISSION_RECEIPT.json. No live store, recall control, service or other worker artifact was changed. Requested model settings are not served-model evidence; a different-model review gate has not been established.

Apply the hook only after its own review by appending hook_proposals.jsonl to ~/primary_directive/hooks1000/proposals/math-w427.jsonl; patches/01_uniform_exhaustion_hook.diff is the unified review diff, relative to ~. The worker did not write the global hook file or run the live integrator.

NEXT: w428 independently checks the strip, exhaustion and planar counting arguments; the validating integrator reviews the concept bundle and separately confirms any ingestion and retrieval.

A final paired handoff added two scoped KEEP verdicts in PAIRED_AUDIT_SUPPLEMENT.jsonl: the optimal forest modulus 1-sqrt(1-epsilon) for epsilon in (0,1), and the square-with-pendant counterexample to a fixed relay witness. The exact arithmetic margin is 1/128. There are five KEEP verdicts total; the submitted draft bundle is unchanged.
