# P0017 review handoff

w356 independently rederived the whitened-simplex conditional law before reading w355's barycentric derivation. KEEP w354's uniform-interval scale result and w355's two mathematical simplex/weighted-energy claims; exact verdicts are in ../PEER_REVIEWS.jsonl. Source-status rows are not re-reviewed as mathematical proofs.

The main obstruction is exact: ambient isotropy does not bound the almost-everywhere conditional Poincare constant uniformly in dimension. Averaging the constants does not fix it because the fiber energy can correlate with fiber size. At n=100 the conditional essential supremum divided by its mean is 1717; the explicit cosine weighted-energy family has quotient/mean=50.5 at k=10.

w359: independently audit w356 C02 and C03 in ../SIMPLEX_FIBERS.md, particularly the linear disintegration, the positive-mass essential supremum, and the Lipschitz extension of f_k at T=0. Reproduce with `python -B -X utf8 ../reproduce_simplex.py` from this directory (or run it directly in w356). Return KEEP/FIX/DROP with the exact unresolved gap. C01 is a trivial scale boundary and may be checked with the packet; it is not the main contribution. Do not count w356's own computations or agreement with w355 as the independent review of w356.

The eight-entry, nine-relation draft is ../drafts/bundle_001.json. All parent proof announcements are concepts with validity explicitly unaudited. Own special-case lemmas are drafts pending w359. Six peer mathematical claims have KEEP verdicts, including the exact optimal conditional directional coefficient and a smooth triangle polynomial with full gradient energy 13/27. Relations quote their two supporting ends in RELATION_EVIDENCE.jsonl. ENTRY_REVIEW_STATES.json records the separate review states. The destination is the task-named w356 draft inbox; the validating coordinator alone handles ingestion and checks retrieval.

The original target is Randomstrasse101 2603.29571v1, Entry 13, Conjecture 30. The current primary proof claims are 2610.05474v1, 2610.01447v2, and 2610.07728v2. The September source status is historical. Current openness in this audit is UNKNOWN; no parent solution or novelty is claimed. The prior stored attempt was only the standard-Gaussian Hermite proof.

No formal kernel check is claimed: the receipt covers exact arithmetic and deterministic quadrature, not theorem verification. The quadrature check initially failed from midpoint endpoint error and passed after switching to Simpson with the same tolerance; see ../VERIFICATION_NOTES.md. Recall ran with a write guard, so its attachment warnings are not evidence of a defective live corpus.

NEXT: w359 audits C02/C03; coordinator deduplicates the overlapping simplex cards, integrates kept drafts and verifies targeted retrieval.
