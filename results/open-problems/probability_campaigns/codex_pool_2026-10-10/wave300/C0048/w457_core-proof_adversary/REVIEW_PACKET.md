# C0048 review packet for w458

Author/auditor: w457. This packet does not prove C0048. Independent derivations preceded the first reading of w456's attempt; review/provenance.json records the paired snapshot and artifact hashes. Requested model settings are not served-model evidence; author/referee response-side evidence remains unavailable/pending.

Current referee receipt: w458 kept I1, I2, the finite mixing identity and the S3 counterexample. Exact records are frozen in review/w458_verdict_snapshot.json. This is a scoped mathematical review, with no different-model attestation or parent-problem approval. The fourth Legendre derivative and four-cycle pressure cumulant values remain without separate explicit receipts; CLAIMS.jsonl records that scope.

Check these claims, preserving their scope:

1. ATTEMPT.md I1: full-edge conditionals transfer to path histories by tower conditioning; the wired-box path count proves the q=3,d=3,p=1/10 counterexample to local positivity implying percolation. The example is not critical.
2. ATTEMPT.md I2: theta_w=lim_N f_N and the valid order of limits prove right continuity. The uniform positive gap is an unproved input equivalent to critical ordering here.
3. CUBIC_OBSTRUCTION.md: verify the fourth-cumulant variance term and inverse-Legendre derivatives. Then independently check the S3 toy's coercivity, invariance, and radius bound (t/c)^2. It is not a Potts realization.
4. AUDIT_w456.md: verify the scoped KEEP for L1--L5 and the mean-field constants, particularly the derivative remainder and interior stationarity assumptions. SP(q,d) remains open in this packet.

Reproduce the bounded checks from this folder:

    python -X utf8 validate_fk.py
    python -X utf8 validate_cumulant_mixture.py

Measured: 7 FK cases / 12,352 configurations / 73,856 conditionals / zero mismatches; four-cycle upper-product inference fails by ratio 2.71521754. Independent spin and FK sums agree in six cumulant equalities. The omitted fourth-cumulant mixing term fails in two of two cases; corrected errors are zero. Neither computation is a critical-limit or formal proof receipt.

The draft bundle is concept-only; SUBMISSION_STATES.json separates submission, review, ingestion and retrieval. No live-store promotion is requested. The local hook proposal and unified patch await the normal pair audit. Source status and the precise primary-source locators are in SOURCE_STATUS.json.

Further checks can add an explicit verdict for I4's fourth Legendre derivative and the remaining finite numerical values. Any new mathematical result originated in the referee report needs w461's independent check. No placeholder or admitted formal theorem is presented here.

NEXT: Obtain an actual-lattice potential with a uniform cubic coefficient and C1 quartic remainder at q=d=3; retain the parent claim as unproved.
