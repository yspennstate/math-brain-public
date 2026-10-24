# P0321 review packet

Primary referee: w545. Independent referee for any new referee result: w548. Current target openness: UNKNOWN. A full hexatic Riesz-gas existence proof is not claimed.

Read INDEPENDENT_OBSTRUCTION.md first. The main new, disjoint result is the exact-density positivity obstruction and its correlated-Gaussian ray proof. Check that bivariate indicator covariance tends to zero, the variance-of-averages argument is valid without independence, the countable-union step excludes finitely many negatives, and the density variance has the coefficient 1/[2pi beta a(4-s)]. A constant Gaussian sequence is the boundary control: covariance does not decay and the almost-sure assertion fails.

ATTEMPT.md retains the independently derived harmonic calculation, saved before any paired proof was opened. Its positive-shear result agrees with w543 and is used as a cross-check, not a separate novelty claim. Audit findings and the explicit missing microscopic premise are in AUDIT.md and AUDIT_VERDICTS.jsonl, bound to audit_snapshots/w543_ATTEMPT.md by AUDIT_SNAPSHOT.json. Do not promote a normalized-rate limit statement to a claim of unequal raw iterated limits.

STATEMENT.md separates the recovered historical wording from a declared stronger working benchmark. SOURCE_STATUS.json and ORIGINAL_RECORD.json hold the target provenance and current-status uncertainty. BRAIN_TARGET_RECEIPT.json records the two exact existing target cards through a read-only query; RELATION_EVIDENCE.jsonl quotes both ends of every proposed relation.

Reproduce auxiliary measurements with:

    python -X utf8 ~/brain_workers/w544/verify_elasticity.py
    python -X utf8 ~/brain_workers/w544/collect_receipts.py

The first command checks 83,100 covariance contractions under a fresh CPU gate. The second checks three exact negative-density tails and nine angular integrals under a separate gate. These are formula checks, not an actual gas simulation, mathematical independent acceptance, or formal proof receipt.

DRAFT_BUNDLE.json contains one definition and two concepts, all labeled draft with pending review. No theorem or lemma is submitted. Validate locally with prepare_bundle.py; --submit writes only the explicitly authorized worker inbox file via a completed .part rename. SUBMISSION_STATUS.json records preparation, submission, review, ingestion, and retrieval separately. The coordinator performs ingestion after validation; the worker never invokes a live-store integrator.

Outbound mesh communication failed (no registered team; first read also saw a lock); a later read received w543's source-only message, so REVIEW_OUTBOX.jsonl retains the narrow claim/review messages and PROGRESS_OUTBOX.jsonl retains the progress row. hooks/proposals/math-w544.jsonl is a staged hook proposal with an exact-identification fire case and fluctuation-law silent case; it was not placed in the global proposal directory under the worker write boundary.

The next mathematical step is to independently check P0321-N01/N02, then state a nonlinear positive microscopic observable or a local good-event comparison with scale-relative correlation error. This packet supplies neither that transfer nor defect weights on an open temperature interval.
