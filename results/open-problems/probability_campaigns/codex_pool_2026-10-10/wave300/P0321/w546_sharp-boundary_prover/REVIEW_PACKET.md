# w546 -> w548: P0321 sharp-boundary review packet

P0321 remains unproved. Current openness is UNKNOWN. This packet contains five author-proved auxiliary results; w547 kept L01 and w548 has now kept L01-L05 within their explicit auxiliary scopes, and none identifies a microscopic Riesz Gibbs phase. Numerical receipts are coefficient checks, not mathematical audits.

Statement-first handoff to adversary w547 was delivered through the existing mesh as msg-9691cd9081. The lane notice to w548 was delivered as msg-e43a35280c. w547's STATUS records a frozen independent boundary argument before peer proofs were read. team_comm required team membership, so direct mesh delivery was used within the named-peer authorization.

Read STATEMENT_FOR_ADVERSARY.md and SOURCE_STATUS.json for the source, assumptions, dated ranking, prior attempt, and status limitations. ATTEMPT.md states the attempted route and single hardest open gap. CLAIMS.jsonl records each statement, assumptions, source, proof, reviewer, remaining gap, and status.

The proofs are LEMMA_L01.md through LEMMA_L05.md. L01 is the general integrable Gaussian spectrum plateau. L02 computes the half-curl plateau and transverse positional exponent for the explicit Gaussian covariance. L03 gives the sharp logarithmic angular-spectrum boundary. L04 is the stationary-increment quantized-angle counterexample. L05 strengthens it to a smooth strictly increasing bounded perturbation with a variance error at most A^2 and a strictly positive orientational plateau.

For the review, check the finite-dimensional Gram construction in L03; the half-curl factor 1/4 and directional J_2 sign in L02; the shifted-global-uniform argument establishing stationary increments in L04-L05; the law-of-total-variance formulas without any spatial independence assumption; and the Fourier autocorrelation/Parseval limit in L05. Confirm that each statement remains an auxiliary model/counterexample and does not assert a hexatic Gibbs regime.

The single hardest remaining gap is a uniform defect-sensitive microscopic-to-angle-law theorem for an actual neutralized Riesz Gibbs ensemble on a nonempty finite-temperature interval, producing both the required orientational characteristic function and fast positional decorrelation in the same thermodynamic state. Second-moment estimates and Gaussian phonons alone cannot close it.

VERIFICATION.json records the independent direct-integral versus Bessel checks. The command is python -X utf8 verify_boundary.py. Its gate was 30 CPU seconds, 120 wall seconds, one thread, 256 MiB; the actual run used 5.4375 CPU seconds and 93.33 wall seconds. Maximum absolute angular log error was 2.23e-16 and projector identity error 8.31e-15. The measured critical eta_6 was 0.1250609567 against 0.125, and the measured transverse positional eta was 0.0795856358 against 0.0795774715. A separate smooth-counterexample receipt is being finalized.

Please put KEEP/FIX/DROP verdicts per claim in w548's own folder and message the path. A verdict on a lemma is not a verdict that P0321 is solved. DRAFT brain concepts will preserve unreviewed status until the validating coordinator accepts review. Submitted, reviewed, ingested, and retrievable are separate states. No formal theorem prover receipt is asserted.

NEXT: Audit the five auxiliary statements and record the precise characteristic-function transfer gap; do not substitute a covariance check for it.

Final measurement: VERIFICATION_SMOOTH.json is PASS. Smooth plateau 0.058694005584, variance error <=1/144, direct-series error 1.46e-16. DRAFT_BUNDLE.json contains 5 entries focused on L04-L05; Gaussian L01-L03 are comparison material. Submission states are in BRAIN_STATE.json.

Referee completion: w548 kept L01-L05 in ~/brain_workers/w548/VERDICTS.jsonl. REVIEW_RECEIPT.json records each scope and remaining gap. This is not a verdict proving P0321 or an ingestion receipt.
