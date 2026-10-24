# P0017 review packet

Target and provenance: SOURCE_STATUS.json, ORIGINAL_SOURCE_REPORT.json, HISTORICAL_SOURCE_EXCERPT_REPORT.json. The historical route was Gaussian Hermite expansion; w352's method is disintegration with moving conditional supports. Current openness UNKNOWN; no novelty claim.

Independent derivation, saved before any w351 proof was read: ATTEMPT.md. Independently check convexity of x>=|y|^p, the Exp/Gamma representation, exact isotropic covariance, conditional gradient energy D_p, and its limit D_p/p=1/3. The conditional mean variance shrinks; this is not a KLS counterexample.

Peer proof audit: PEER_AUDIT.md. KEEP w351-L0 and L1 with their hypotheses. Independently check the distinct ball witness: radius sqrt(n+2), n=2d, A=|U|^2, B=|V|^2, Cov(A,B)=-d^2/(d+2), P f+Q f=(1+d/(d+2))f for f=A-B. The exact witness ratio is (n+4)/4 for every balanced orthogonal split. No optimal constant for every function or conclusion about unbalanced splits is claimed.

Claims and reviewer assignments: CLAIMS.jsonl. Own new mathematical claims w352-S1.3 and S1.6 remain sketch/draft pending w353. w356 independently checks any new result originated by w353. The w351 simplex claims were not certified by this packet.

Prepared check command: python -B -X utf8 verify_obstruction.py. It compares the epigraph Gamma formula with direct y-coordinate quadrature and checks the disk by independent radial/angular integrals. Current MEASUREMENTS.json records a denied fresh gate and ZERO experiments. Do not treat its resource receipt as numerical mathematical evidence or relax the gate. Resume only in an admitted window.

Draft submission: ~/math-brain-inbox/w352/bundle_001.json. DRAFT_BUNDLE.json is the local copy; both entries are concepts with null proof_text and an explicit pending-review label. SUBMISSION_STATES.json separates submitted, reviewed, ingested and retrievable. RELATIONS_REPORT.json quotes the exact ends of the only relation. No unreviewed theorem was promoted.

Optional hook: HOOK_PROPOSAL.jsonl and patches/01_conditional_averaging_hook.diff. No live hook was changed and its fire/silent controls have not been run. PROGRESS_EVENT.json and CLAIM_BOUNDARY.md are local handoffs, because this worker's brief forbids global progress writes and mesh send commands.

Decision needed: accept the analytic draft for proof-only independent review now, or provide a healthy admitted local window for the prepared numerical cross-check. The worker cannot change services, resources or processes to create that window.

NEXT: Independently verify the two exact derivations; return a concrete KEEP/FIX with the checked statement and assumptions, and run the prepared numerical check only under an admitted gate.
