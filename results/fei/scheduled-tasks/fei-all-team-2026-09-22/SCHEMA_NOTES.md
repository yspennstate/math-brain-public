# FEI memory record checks

`CLAIMS.schema.json` describes the actual canonical claim projection. `DELTAS.schema.json` describes its mandatory source-bound correction feed. `MEMORY_SNAPSHOT.schema.json` describes a worker's compact run memory record; `CORRECTION_INBOX.schema.json` describes critical events awaiting canonical consolidation. `MEMORY_BUNDLE.schema.json` combines those schemas for callers that already use JSON Schema tooling.

The standalone validator uses only Python's standard library. It checks actual source pins, reference resolution, scope and candidate identity, positive-premise dependencies, transitive stale dependencies, conditional assumptions, scope promotion, immutable history, required correction consumption, pending inbox challenges, native-memory receipt fields, and optional manifest byte hashes. It does **not** certify source contents, independently verify mathematical proofs, contact GitHub, or prove that a claimed memory read occurred.

From the canonical FEI directory, run:

```bash
python validate_memory.py --claims CLAIMS.json --deltas DELTAS.json --manifest MANIFEST.json --inbox CORRECTION_INBOX.json
python -m unittest -v test_validate_memory.py
```

Before publishing a worker snapshot, also pass `--snapshot` with its local JSON path and `--observed-head` with the actual fresh branch SHA. The expected parent check is meaningful only when the caller obtains that SHA from a fresh authorized repository read. For manifest hash checks, pass `--directory` with the local directory corresponding to the manifest's relative file paths. For an update, `--previous-claims` and `--previous-deltas` compare immutable identities and event history with the previous committed versions.

Seventeen regression tests mutate the actual rollout data to exercise failure modes seen in this research: reviving the refuted 0.337 candidate, applying a candidate refutation to FEI itself, losing a new correction between consolidated revisions, promoting a read-once result to full FEI, treating a refuted base definition as though it invalidated every repaired candidate, and confusing repository reads with native persistent memory. The fixtures are test-only; they are not claimed worker executions, proofs, or API receipts.

The initial `DELTAS.json` entries are immutable source-summary events from the owner rollout. Their `immutable_event_path` points to `events/owner/FEI-ALL-TEAM-20260922T095941Z/`. Every event contains actual immutable source pins and explicitly records that the state editor did not complete an independent full proof review. The live inbox begins empty because those initial events are already in the canonical feed; future unmerged critical events are placed there without changing the hashed manifest bundle.
