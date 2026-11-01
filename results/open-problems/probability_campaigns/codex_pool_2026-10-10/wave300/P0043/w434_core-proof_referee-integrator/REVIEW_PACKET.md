# P0043 referee packet — w434, 2026-10-10

## Source and current status

The exact historical Benjamini–Schramm bond conjecture assumes an infinite connected locally finite quasi-transitive graph and `p_c<1`. Hutchcroft's 2016 paper proves the exponential-growth class. The dated P0043 ranking omits `p_c<1`; the line graph gives an immediate counterexample to the unqualified shorthand. A 42-page OpenAI preprint dated 2026-09-24 claims the whole theorem. Current mathematical status in this packet is **UNKNOWN** until that paper receives a stepwise audit. The linked Lean files are comparator statements and contain intentional `sorry`. A distinct 213-line solution Main exists with the matching top-level theorem and no local `sorry` or `axiom`; its imported proof closure and kernel check have not been reproduced.

## Own scoped attempt and independent review request

`ATTEMPT.md` independently rederives the no-strip winding core of Proposition 8.1 and a conditional Proposition 9.3 exploration estimate. It leaves the strip case, fixed-seed parameter transfer, and full fresh-contact transfer unverified. `W437_REVIEW_REQUEST.md` asks the next triad's referee to audit those two new arguments; no second-account verdict has arrived. These checks do not certify the preprint's full theorem.

## Peer verdicts

Detailed per-claim KEEP verdicts and reproductions are in `REVIEW_VERDICTS.jsonl`. I independently rederived w432 L01–L05 and w433 Sections 1–3. Every KEEP is a partial mathematical statement or a corrected source statement. In particular, w432's uniform-integrability condition and w433's robustness input R are each equivalent in strength to P0043; neither is a proof of the parent.

The two routes locate different forms of the same obstacle. W432 needs a uniform bound on finite-radius pivotal mass in a shrinking interval immediately below `p_c`. W433 shows that any hypothetical infinite critical cluster has its own percolation threshold one, so any downward-thinning proof must obtain a new symmetry-dependent contradiction. Their explicit bounded-degree tree and density-one comb examples rule out shortcuts based solely on degree, independence, volume growth or ambient density.

W433's submitted six-concept, five-relation draft received a **KEEP as draft** verdict after independent checks of Sections 2, 5 and 8. Its file SHA-256 and exact verdict are in `W433_BUNDLE_AUDIT.json`. This does not approve theorem promotion or ingestion; G01 and the public full-theorem claim remain unproved in this packet.

W432's revised nine-concept draft received **KEEP on L01–L08, G01 as unproved, and both source corrections; FIX on two relation labels**. The detailed verdict and SHA-256 are in `W432_BUNDLE_AUDIT.json`. The proposed `depends_on` links L03→L02 and G01→L03 should be `semantic_association`: their proofs do not depend on those cited results. The published Cerf abstract is site percolation only, so R02's model-scope correction is supported. Numerical controls were held by a fresh compute gate and are not counted as tests passed.

## Independent source audit underway

The new preprint's Theorem 6.1 asserts the joint gluing inequality `P(o↔A,o↔T) >= P(o↔A) inf_{a∈A}P(a↔T)`. Its finite proof uses a triangular matrix of conditional cluster columns, a deleted-set residual, and alternating cluster resampling. I checked the finite matrix identities and the conditioning map in Lemmas 6.2–6.3 as written; no contradiction has yet been found. Proposition 9.2 applies this inequality after fixing independent interior trial bits and says fresh corridors transfer a hit of a relay set to a target. Its selected contact trials are disjoint and sampled from bits independent of the exterior selection; this part survives the obvious selection-bias check. The later adaptive exploration and the structural quotient reduction remain unverified, so the preprint is a **claim**, not a validated solution in this packet.

## Reproduction and next referee target

Source: `source_2026_claim.pdf` (42 pages, 573471 bytes; SHA-256 `5929ccea200fd7433c5ac519c924316ccdd56fc0208ea0cc65d5a424bb2e425f`), extracted to `source_2026_claim.txt`; public original: https://github.com/openai/math/blob/main/preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/paper.pdf. Comparator statements: https://github.com/openai/math/blob/main/lean/ComparatorChallenges/CriticalPercolation.lean and https://github.com/openai/math/blob/main/lean/ComparatorChallenges/CriticalZ3.lean. Distinct solution entry point: https://github.com/openai/math/blob/main/lean/OAI/Probability/CriticalPercolation/Main.lean. Next: independently audit Proposition 8.1 and the fresh-edge filtration in Proposition 9.3. A referee of any new w434 lemma should be w437.
