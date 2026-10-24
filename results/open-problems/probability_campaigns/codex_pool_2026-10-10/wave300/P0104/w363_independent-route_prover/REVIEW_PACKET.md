P0104 / w363 independent route / referee w365

This packet does not prove P0104. It contains five local lemmas/reductions and one explicit gap. The source asks for strict subdiffusivity, planar chi=1/3, and positive chi in a suitable dimension. It leaves the suitable laws unspecified. The chosen exploratory law is nearest-neighbor Z^2 with weights 1 and 2 and cheap-edge probability 0.01; no generic curvature or universality assertion is made.

Read STATEMENT_FOR_ADVERSARY.md and SOURCE_STATUS.json for exact scope and source limits. The statement reached w364 first, message msg-d12635c55c. APPROACH_BEFORE_PEER_PROOFS.md records the route before any core proposed proof was read. The route claim reached w360, message msg-3f9a0d9597. Mesh lease: clm-fbbad4837e on topic:P0104:w363-spectral-harmonic.

Review ATTEMPT.md and CLAIMS.jsonl. Check C004-C006 first: the forced-edge sandwich and its tie convention, the simple-path union bound at q=0.01 giving n/600<=D_n<=(99/50)n, and the exact size-biased spectral reduction. C003 is a rederivation of established finite resampling mathematics. C001 repeats the historical n/log n obstruction. C008 rejects a typical-scale shortcut; it is not an FPP counterexample.

Hardest remaining gap G1 / C007: E_nu_n[1/K]=n^(-1/3+o(1)). It is conjectural. The proposed noise envelope in ATTEMPT.md is only a sufficient hypothesis. No argument in this packet establishes it, and no qualitative chaos theorem is used to set its scale.

Reproduce the finite controls with:

    python -X utf8 ~/brain_workers/w363/verify_finite.py --gate-seconds 60 --max-configurations 128

MEASUREMENTS.json records PASS: 4 exact variance identities, 15 exact gradient correlations, 544 forcing checks, 4 energy sandwiches, 4 harmonic identities, 2 invalid shortcuts rejected, elapsed 0.174503 seconds. These finite tests are not a formal-check receipt or an asymptotic proof. No admitted theorem, trusted-axiom receipt, or Lean proof is claimed.

BUNDLE_VALIDATION.json identifies the staged math-brain draft and its local structural checks. All five entries are explicitly unreviewed concept cards; no theorem entry or live-store mutation. Four relations use supporting ends in the same file. The source license is owner-own-work for this campaign reconstruction; literature attribution is explicit. Review, ingestion, and retrievability are separate pending states. The coordinator must perform any final integration. The local hook proposal is hooks/math-w363.jsonl, with a fire and silent case grounded in the exact leakage counterexample; it is staged for the collector under the worker's write restriction.

Return a per-claim KEEP/FIX/DROP with the mathematical reason and scope. Any new mathematical claim by referee w365 goes to w368 for independent review. No prior keep, account diversity, or peer acknowledgement is presumed.

NEXT: Estimate F_n(k)=nu_n(K<=k) for k<=n^(1/3), starting with the first-level term pq sum_e(E delta_e T_n)^2 and the weighted harmonic-tail identity.
