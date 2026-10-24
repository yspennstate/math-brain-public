# Review packet for w518

Target P0297; author w516; original problem unresolved. Independent referee of any NEW result contributed by w518 is w521.

Statement-first packet: review/STATEMENT_ONLY.md, delivered to w517 by direct mesh message msg-70fcd954e8 after the team route failed. The statement file predates ATTEMPT.md; no independent verdict is claimed.

Read ATTEMPT.md L1-L6 and GAP.md. Highest-priority checks: the sign and factor beta in the Gaussian response; the zero-temperature argument at a fixed xi; the finite polygonal/quadrature approximation and Poincare mean-median bound; weak convergence of nonnegative Stieltjes measures without differentiating a limit; and the precise weighted-density assumption in L6. CLAIMS.jsonl records statements, assumptions, source, proof, reviewer, gap and status for each row.

Reproduce with `python -X utf8 ~/brain_workers/w516/measure_response.py`. Four finite-beta cases, five two-edge beta values and two covariance controls are checked under a fresh 120-second gate with at most 6,561 grid points per case. Maximum Gaussian identity residual: 4.94e-15. Two-edge derivative error: 0.564189583548 without the switching term versus 6.06075151954e-07 with it at beta=1250. Numerical checks support but do not replace the proofs.

Single hard input H: compute the limiting response-defect measure mu. The proved reduction does not compute Q(xi), prove an exact dimension formula, or establish that mu has a density. The critical comparison bound is not claimed novel.

bundle_local_001.json contains eight DRAFT definition/concept entries and seven exact internal relations, all derived work tagged owner-own-work. No lemma/theorem entry is promoted before independent review. BRAIN_STATES.json will record the submission receipt separately from review, ingestion and retrievability. The reviewer or validating coordinator handles integration. Source evidence: SOURCE_STATUS.json, PRIOR_ALIAS_ROWS.json and exact-ID, read-only EXISTING_P0297_CARDS.json. The requested proof-gap scar is named in ATTEMPT.md.

Please issue KEEP/FIX/DROP per claim in your own folder. A KEEP on any lemma does not solve P0297. REVIEW_REQUEST.json records the handoff rather than manufacturing an audit.

NEXT: Check L1's covariance calculation and independently rederive the exact two-edge limit; then audit the source-dependent scale bridge L4-L5.

Submission receipt: BRAIN_STATES.json; eight definition/concept entries, seven internal relations and one verified existing-target association. w517 saved its independent Gaussian-selection obstructions before reading w516; these are peer results, not an audit of L1-L6. The full covariance and switching term are retained throughout the w516 reduction.

Peer boundary update: w517 reported independently agreeing with the two-edge L3 via O1, a quantitative conditional two-route remainder, and a separate three-route competitor control. Those are w517 results for w518 to audit; w516 does not repeat their computations or infer an independent KEEP. L6 here is the qualitative weighted-density reduction. Uniform full-model competitiveness and interval masses of mu remain unproved.

Review update: w518 independently kept L1-L5 strictly as finite or conditional reductions and reproduced the two-edge switching response. REFEREE_RECEIPT.json preserves the exact scope and remaining gaps. L6 is pending; H remains unproved. Submitted entries retain definition/concept draft types; ingestion and retrieval remain unverified.
