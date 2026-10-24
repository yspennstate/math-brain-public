# P0297 peer bundle review, 2026-10-10

## w519 submitted bundle_001.json: KEEP mathematical content, FIX one stale review state

Six entries and seven relations were inspected in `~/math-brain-inbox/w519/bundle_001.json`. `local-mass` is a correct definition. `log-potential`, `clock-conversion`, and `gmc-potential` match the independently checked W519-L2/L4/L5 claims, with the Euclidean and conditional scopes explicit. `route-gap` is correctly a concept, not a theorem. `identity-correction` correctly diagnoses D0049-A001, and its source patch passed `verify_peer_patch.py` (`PATCH_CHECK_OK source_line=43 changed_fields=2 untouched_fields=9`). The correction card still says "Independent source-row review is pending"; w521 has now checked the source row and patch. Replace that sentence with "Independently checked by w521; historical source patch not yet applied" before integration. The source revision label `draft-unreviewed` can likewise be updated. No live store ingestion is claimed.

Internal depends_on/specializes/cites links have supported endpoints. The link from the correction card to the existing P0297 problem is a topical association; `semantic_association` is a more exact relation than `cites` if the integrator interprets `cites` as an explicit bibliographic citation. This is a relation-type FIX suggestion, not a mathematical error in the correction.

## w520 staged bundle: two KEEP concepts, one overlapping gap concept held

`~/brain_workers/w520/drafts/bundle_001.json` has three concepts and four relations. The snowflake and thick-point completed-square statements were independently checked in `VERDICTS.jsonl` against the primary LQG length axiom and Gwynne--Pfeffer Theorem 1.5. Their "awaiting w521 review" wording is now stale. The gap concept's LFPP median formula is correct by Ding--Dubedat--Gwynne, equations (2.3)-(2.5), but it overlaps this worker's primary-source problem card and w519's submitted route-gap concept. To avoid that duplicate, `w521/bundle_002.json` carries the two distinct concepts with w520 attribution and three supported semantic links. It is a DRAFT, not an ingested theorem.

## Remaining gate

These are first referee checks. A separate pair audit and normal coordinator integration are still required for live store changes. No peer lemma computes the general d_gamma.
