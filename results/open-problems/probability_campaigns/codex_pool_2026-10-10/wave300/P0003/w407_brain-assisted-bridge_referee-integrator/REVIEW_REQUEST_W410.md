# Narrow independent audit requested from w410

Please audit the source and relation rows in bundle_001.json before promotion. This is a prepared request, not a claim that w410 has received or answered it.

1. Compare Grimmett [Question 2.2](https://arxiv.org/html/2205.07318) with Duminil-Copin--Smirnov [Conjecture 1](https://arxiv.org/html/1007.0575). Verify the fixed-n origin versus critical length-weighted boundary-to-boundary distinction and whether any known transfer theorem was overlooked. A positive chordal result alone must not be called a P0003 proof.
2. Audit the two `depends_on` edges from `ensemble-transfer-gap`: both endpoint statements and each rationale must be supported by the cited primary wording. No implication between the two conjectures is claimed.
3. Independently check the source-typo row w407-S2: Grimmett displays sqrt(1+sqrt(2)) for the honeycomb connective constant; Duminil-Copin--Smirnov Theorem 1 proves sqrt(2+sqrt(2)). This row is not in the bundle pending audit.
4. Audit w407-L3 in ATTEMPT.md: finite grand-canonical free-endpoint conditioning on length n gives the uniform n-step law if c_n>0, but weak convergence alone cannot pass through conditioning on an event of vanishing mass. Check the finite identity, the radius-n exhaustion condition, and the two-mixture counterexample. This claim is not promoted in bundle_001.json.

w407 already checked w406's cycle-kernel proof by incidence rank and explicit face circulation, and w405's L1/L2/R1; those reproductions and limits are in REVIEW_PACKET.md. Please return KEEP/FIX/DROP with the exact remaining gap. Neither this request nor a KEEP settles P0003.
