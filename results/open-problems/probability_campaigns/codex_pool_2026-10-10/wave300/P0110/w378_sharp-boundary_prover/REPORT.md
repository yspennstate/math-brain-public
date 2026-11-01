# P0110 handoff

The target is primary Question 22 of Auffinger-Damron-Hanson: exhibit an iid FPP passage-time law satisfying the KPZ exponent identity. This packet does not solve it; current external openness and novelty are UNKNOWN.

The useful result is a sharp support-width boundary. If n(b-a)<2a, positive [a,b] weights force the axial geodesic and iid passage-time variance is exactly n Var(tau). For fixed Uniform[1,1+epsilon] weights, almost-sure axial uniqueness holds exactly when n epsilon<=2. This yields a counterexample to a strict variance contraction starting at one common threshold for every bounded continuous nondegenerate iid law. A threshold depending on the law survives.

Verification: `python -X utf8 verify_boundary.py` passed 8704 exact configurations in 0.084586 seconds. Below threshold 128/128 axial routes were unique; at equality 2/128 had ties; above threshold 2/128 had cheaper detours. At n=2,4 for equiprobable {1,5/4} weights, variances were 1/32 and 1/16, giving V(4)/(2V(2))=1. Exact Uniform moments give 1/96 and 1/48, also ratio 1. The graphs are finite sanity checks; the infinite-lattice argument is in BOUNDARY_LEMMA.md. There is no formal certificate or measured recall improvement.

The review packet, statement, prior-attempt digest, assumptions, claims and hardest gap are saved. The three lemma cards use owner-own-work and remain DRAFT with independent review pending; local JSON and relation checks are run by `python -X utf8 prepare_bundle.py`. BRAIN_SUBMISSION.json records prepared/submitted/reviewed/ingested/retrievable separately.

Apply: after mathematical review, the validating coordinator can integrate the named inbox DRAFT; patches/02_draft_brain_bundle.diff is an equivalent new-file draft. Apply patches/01_math_w378_hook.diff to add the staged hook proposal, then conduct its ordinary hook audit. PROGRESS_EVENT.json is a staged progress row for the reviewer to post. These staged global hook/progress changes respect the worker-folder restriction; the brief separately authorizes the own-agent brain inbox.

What could go wrong: equality differs for atomic and continuous laws; the positive lower support endpoint and nearest-neighbor model are essential; varying epsilon with n cannot prove an exponent for a fixed law. A PASS banner and a source match do not close the gap. The narrow hook passed one fire and one silent control, with no live deployment claimed.

NEXT: Review L1/L2/L3, then seek a fixed-law large-scale exponent bound with a law-dependent threshold; do not repeat the law-uniform bootstrap.

Submission confirmed: ~/math-brain-inbox/w378/bundle_001.json (3 DRAFT lemmas, 2 relations). Full referee request delivered to w380 as msg-f97b6dacae; mathematical acceptance is pending. Final artifact check: python -X utf8 finalize.py, 18 required artifacts present and inbox bytes match the local draft.

Partial review: w379 independently kept L1 and L2; exact receipts saved in PEER_REVIEW_RECEIPTS.json. L3 and official referee w380 remain pending. Temporary inbox claim released.
