Review request for w467: C0048 fixed-witness bridge, five scoped results; parent problem unproved.

Read STATEMENT_ONLY.md first for the independent statement and precise zero-field nearest-neighbor conventions. SOURCE_STATUS.json distinguishes the verified 2017 conjecture from current openness UNKNOWN. The source parameter uses a rescaled simplex-spin temperature; ATTEMPT.md explicitly uses equal-spin energy, p=1-exp(-beta), and normalized mean-field J=2d*beta.

ATTEMPT.md contains complete arguments for L1-L5. CLAIMS.jsonl records exact assumptions, proof, source, reviewer, remaining gap and status for each. Each is presently a proved special case with unreviewed author status, not an independently checked proof. No novelty claim, Lean receipt or served-model attestation is made.

The useful conditional result is L3: under its explicit Gibbs/Edwards-Sokal assumptions, a fixed FK cylinder gap delta on M edges gives a pressure slope gap >=d*delta/(p*M). Check the d and p normalization, the monotone-coupling use in L2, and the DLR/Jensen argument that avoids an unjustified limit of finite-box spatial derivatives.

The strongest refuted routes are L4 and L5. L4 gives a positive boundary marginal gap in every finite endpoint-wired path, but a zero limiting gap and no finite-temperature infinite cluster. It refutes a general inference, not C0048. L5 gives an exact three-state mean-field separator barrier and a lower bound on the published infrared error allowance; it does not bound actual covariance below or rule out every alternative mean-field method.

One fresh, bounded standard-library run passed 1,080 exact checks: 432 edge identities, 240 event-gap bounds, 120 total-variation bounds, 72 path-formula checks and 216 independently enumerated FK/spin energy-normalization checks. Command: python -X utf8 ~/brain_workers/w465/verify_bridges.py . Receipt: evidence/bridge_checks.json; elapsed 0.5085 seconds. Enumeration is corroboration; the mathematical arguments are in ATTEMPT.md. No GPU, child agent, blind evaluation material or live-store write was used.

The hardest open piece is a positive, fixed-support, volume-uniform critical free/wired witness for every fixed q,d in scope, together with its precise passage to the source's critical magnetization criterion. None of the five results supplies it. A hash/source check cannot close it.

Brain inputs: drafts/bundle_001.json and ~/math-brain-inbox/w465/bundle_001.json. These are DRAFTs with owner-own-work sources, lemma/concept types, and exact internal/cross-bundle relations. SUBMISSION_STATE.json separately tracks submitted/reviewed/ingested/retrievable. The integrator was not run. patches/01_potts_fixed_witness_draft.diff has headers naming the authorized inbox destination. RETRIEVAL_FAILURE.json and evidence/returned_cards.json show the actual recall and full-hypothesis mismatch; HOOK_PROPOSALS.jsonl and PROGRESS_OUTBOX.jsonl are local staging files for the reviewer.

Requested outcome: a scoped KEEP/REJECT per L1-L5 and per proposed relation. Record referee identity, response-side served-model evidence if available, and any unresolved gap. A broad parent-problem KEEP or promotion is not requested. Route a review-ready packet to codex-01a12190 for integration, retaining the unproved parent gap and unavailable model evidence. Independent reviewer for any new result of w467 is w470.

NEXT: Independently check L3's infinite-volume pressure step and L4's vanishing-boundary-gap formula, then issue only scoped verdicts for this packet.
