# P0017 sharp boundary review packet, w354

Assigned referee: w356. Independent adversary: w355. w356 returned KEEP for claims 001-004; w355 independently kept the complete proof. Verdicts are recorded in REFEREE_VERDICTS.json and the peer's W354_AUDIT.md. Claim 005 records the general Section 5 formula already checked by w355; an explicit additional w356 general-family row is requested.

The exact target and its assumptions are in STATEMENT.md. Primary-source recovery, October proof claims and the Gaussian prior-attempt digest are in SOURCE_STATUS.json and SOURCE_RECOVERY.json. The modern primary literature claims a full solution; no current-openness or novelty claim is made here.

SIMPLEX_PROOF.md is the complete author proof. CLAIMS.jsonl rows 001-004 are the precise review units. The main result is the exact orthogonal conditional-fiber obstruction for the isotropic uniform simplex, including positive-probability neighborhoods, the sharp directional conditional constant and a smooth polynomial witness in dimension two. It refutes specified auxiliary steps, not the full-gradient KLS target.

Critical checks: (1) whitening covariance and unit normalization; (2) ker(PA)=span(e1), so orthogonal conditioning really fixes the other raw coordinates; (3) essential extrema, not just the edge at S=0; (4) finite full energy of each localized sine test; (5) full gradient of the polynomial includes the orthogonal term. The single hardest gap in this worker's route is a bound on the correlation of fiber constants and localized directional energy using orthogonal energy.

Reproduce the measurements with `python -X utf8 ~/brain_workers/w354/measure_boundary.py` and `python -X utf8 ~/brain_workers/w354/check_polynomial.py`. Fresh bounded gates and receipts are saved. The latter independently expands polynomials in raw triangle coordinates rather than reusing the beta conditional formula. No proof-assistant result or formal certificate is claimed.

w355 received the independent statement first, message msg-d2d8a72760. w356 received the complete proof packet, request msg-c9a16f7774; delivery receipt REVIEW_HANDOFF.json distinguishes sending from review. A direct send initially found the recipient unregistered; the existing team_comm mailbox fallback then succeeded after a transient database lock. No new agent process was started.

Draft brain concepts and allowed relations are in drafts/bundle_001.json. All author results are explicitly unreviewed concept material. BRAIN_DELIVERY.json records prepared, submitted, reviewed, ingested and retrievable separately. The validating coordinator performs ingestion after review; this worker does not change the live store. Patches 01-02 name the exact live draft and hook-proposal paths. The hook remains staged locally because the worker's write permission does not include the global proposals folder.

Recorded referee output: KEEP claims 001-004. Claim 005 now states the general Section 5 family as a separate review unit; its formulas were already independently checked by w355, and a scoped w356 KEEP/FIX is requested. Review source chronology separately from mathematical validity. Any full KLS claim would need a different complete proof and independent audit.

The final draft is deduplicated to two distinct concepts: the localized admissible Neumann witness method and the exact full/directional polynomial energy family. Six shared base/status/proposal cards are mapped to peer drafts in DEDUP_MAP.json. Current submission and admission state is BRAIN_DELIVERY.json, not the historical pre-dedup archive.
