# Review packet for w368; independent adversary w367

Read STATEMENT.md first for the exact questions and auxiliary statements. The complete proof is LEMMAS.md; ATTEMPT.md identifies the remaining global gap. SOURCE_STATUS.json carries the primary locators and exact canonical P0104 source/attempt cards. CLAIMS.jsonl records each result separately.

Please audit the following mathematical points without treating the numerical checks as proof:

1. C1's four paths have disjoint undirected edges for every n>=1; their lengths are n,n+2,n+2,n+8. Independence applies to these deterministic edge sets only. Check both tail inequalities and the r-th moment integration, including divergent equality cases.
2. C2 distinguishes finite mean from finite variance at alpha=1/2. No model with infinite variance is used to refute the suitably hypothesized original target.
3. C3 includes n epsilon=2 for the passage-time identity. Positive-probability dogleg sharpness uses n epsilon>2, with delta=min(epsilon/4,(n epsilon-2)/(4n+4)).
4. C4 changes the law with n deliberately to refute a statement uniform over laws. It does not refute an asymptotic exponent for a fixed law.
5. C5 uses strict n epsilon<2 for unique geodesics. Verify exact covariance under independent refresh and the full-refresh overlap n.

MEASUREMENTS.json is reproduced by `python -X utf8 verify_boundaries.py`. Its fresh COMPUTE_GATE.json limits work to 4 CPU seconds, 30 wall seconds, 4,000 configurations and n<=64, with no GPU or background processes. The run passes 3,504 configurations, 384 disjointness checks and exact variance ratios 2,4,8. Finite graphs corroborate the proofs; the proofs cover the entire infinite lattice.

bundle_001.json contains DRAFT concepts with owner-own-work sources, so pending results cannot be mistaken for independently checked theorems. The identical draft was submitted atomically to ~/math-brain-inbox/w366/bundle_001.json under exclusive claim clm-97b2877004. BUNDLE_VALIDATION.json records local structural checks only; BRAIN_DELIVERY.json records submission separately from review, ingestion and retrieval. The validating coordinator performs integration after mathematical review; no integrator is run by w366. The patches name exact live destinations and preserve all other agents' work.

The single hardest gap is a fixed-law lattice geodesic estimate beyond its crossover that yields the matching 2/3 variance exponent. No claim in this packet supplies it. The original target is not solved here; present openness is UNKNOWN and novelty is not claimed.

Return KEEP/FIX/DROP per C1-C5, with the exact audited assumptions. A referee's new mathematical result needs the assigned independent w371 review; no review of a review is requested.

NEXT: Audit C3-C5 boundary and quantifier steps, then integrate only the correctly labeled draft concepts and their supporting relations.

Independent audit update: w367 KEEP on C1-C4 is saved in PEER_AUDIT_RECEIPT.json with exact source lines and scope. This is not two-other-login admission. C5 and final w368 review remain pending. The submitted bundle stays immutable DRAFT concepts. Merge w367's overlapping support/variance proof as evidence, avoiding duplicate nodes.
