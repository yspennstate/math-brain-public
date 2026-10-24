# C0041 independent-route review packet, w447

Review request to w449: a scoped KEEP/FIX/DROP for ER, FV, CC and GO, and a separate source-status verdict. No KEEP of the parent implication is requested or justified. Your own new mathematical claims need the assigned independent referee w452; this packet requests no review of another review.

Statement first was delivered to adversary w448 via msg-8b8ec06cdc before the complete packet. It is in [STATEMENT_FOR_ADVERSARY.md](STATEMENT_FOR_ADVERSARY.md). The route was committed before reading any peer proof or the public full claimed solution. Prior method digest and the single remaining gap are in [ATTEMPT.md](ATTEMPT.md).

| Claim | Exact proof artifact | Review boundary |
| --- | --- | --- |
| ER | LEMMA_ESCAPE_RADIUS.md | Quenched conditional tail at actual block times, including stopping-time selected fixed sets; not future-conditioned Markovity. |
| FV | LEMMA_ESCAPE_RADIUS.md | Orthant-simplex volume count and finite-set corollary; no iid trap-cost bound. |
| CC | LEMMA_CLOCK_TO_COUNT.md | Exponential episode moment and non-stopping clock/count equivalence; division by P(B) exactly once. |
| GO | LEMMA_RETURN_OBSTRUCTION.md | No uniform Green bound across planar ballistic laws at fixed kappa; every fixed-law Green mean is finite. |

Main unresolved obligation: for the fixed-radius ball-exit skeleton before a standard directional regeneration horizon tau and no-backtracking event B, prove E[K_tau | B] < infinity from the target hypotheses. None of the saved lemmas establishes it. The standard regeneration-to-velocity link is the earlier source's Remark 3.11; no new renewal theorem or parent solution is claimed.

Validation: VERIFICATION.json and COMPUTE_GATE.json; 15 kernels, 300 statewise tails, 60 return-probability checks, 32 moment constants, 64 anticipative outcomes. Run python -X utf8 ~/brain_workers/w447/verify_exact.py. ARTIFACT_CHECK.json describes 6 entries and 5 relations, with no proves edge to the target.

Brain submission candidate: drafts/bundle_001.json (mirror of the intended ~/math-brain-inbox/w447/bundle_001.json). All entries are DRAFT; four contain complete author lemma proofs, two are concept/status/gap rows. Own-source license is owner-own-work. Do not ingest before the proof and model-review gates. submitted/reviewed/ingested/retrievable states are recorded separately in SUBMISSION_STATE.json. Relations quote both exact supporting ends.

Source correction: patches/01_C0041_source_status.diff, only C0041 at line 41. Original row and proposed row are preserved in sources/. The new primary claim is mapped by sources/DirectionalBallisticity.config.json to OAI.Probability.Ballisticity.Main and OAI.DirectionalTransience.directional_transience_implies_ballisticity. Permitted configuration axioms are propext, Quot.sound, Classical.choice; actual exported axioms are unobserved. The copied 33-line actual entrypoint calls an imported theorem. No formal-check receipt exists. Do not reject the supplied solution merely because its separate comparator template contains sorry.

Served-model evidence: author requested gpt-6.1-sol/max/Fast; actual response-side served identity unavailable. Referee response-side identity/receipt not received. Request text and turn context do not establish served model. This gap prevents representing any review as a satisfied different-model gate. Reviewer may audit mathematics now while recording identity evidence separately.

Routing: mathematical referee w449; review-ready integration contact codex-01a12190. REPORT.md gives application instructions. STORE_STATUS_ANNOTATIONS.json contains 2 conditional source-status annotations for exact legacy node IDs/titles, not mathematical statement changes. Local hook proposals: proposals/math-w447.jsonl. No live store, blind evaluation material, services or other workers' artifacts were changed.

NEXT: Check CC's non-stopping tail argument first, then GO's scope; KEEP only the exact statements justified by those proofs. The remaining research step is the fixed-law conditional exit-count moment, not another open-status search.

Publication confirmed: ~/math-brain-inbox/w447/bundle_001.json, 6 entries. PATCH_CHECK.json records successful git apply --check --unidiff-zero and application to an isolated local fixture: 1 changed row, 0 live edits. The required-referee, ingestion and retrieval receipts remain pending.

Scoped peer review received: w448 KEEP of ER/FV/CC/GO, recorded with each exact scope in PEER_KEEP_RECEIPT.json. No parent keep or source-status keep. Required w449 review, byte-frozen audit binding and actual served-model evidence remain pending; do not treat this as a satisfied integration gate. The mathematical proof texts and published bundle remain unchanged.
