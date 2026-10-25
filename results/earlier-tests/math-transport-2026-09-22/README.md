# Moving results from the notes into the math store, 22 September 2026

The brain keeps two collections with different readers: the agents' working notes, read by lexical recall, and the
math store, read by the hook that serves theorem cards. A result written only as a note never reached the hook. On
22 September the store held no claim for a read-once FEI theorem proved the day before, although five notes stated it,
and the hook answered a question about it with the open-problem card. A transport job now scans the notes every 15
minutes and writes the results it can recognise into the store as claims.

## The rule

A note is taken automatically when its first words state a result (THEOREM, PROVED, SETTLED, REFUTED) or when it names a
known problem together with a result verb. A campaign's cycle log goes to a review queue. Everything else is skipped,
and so is every note whose subject is not mathematics, even when it carries a theorem. Each claim records in its
evidence that its statement is prose from a note; a typed statement with assumptions is added later as a superseding
claim.

## What was measured

| step | result |
|---|---|
| notes scanned | 16,998: 54 taken, 13 queued, 7 already in the store or dismissed, 16,908 skipped |
| after the first run | 54 claims written, but the hook still served the open problem: its integrity check dropped every transported card, because the node body carried a note excerpt after the statement and the reader binds a claim to its node by exact statement |
| after the repair | body set to the statement, titles and digests recomputed through the store's own model: the hook's reader accepts 54 of 54, and the same question now gets the proved constant first and the open problem second |
| self-test | 14 labelled positives all taken, 13 labelled negatives all skipped (five of them theorems from a non-mathematical domain, refused even when the ingest is forced); an end-to-end run on a stripped copy of the store with the hook's reader as the final check; a second run changes nothing |

The general lesson: a row existing in a store does not make it servable. The check that would have caught the first
run is the consumer's own reader, so the self-test now ends with it.

The note titles, the ledger of ingested notes and the hook transcripts are not included; they name working notes
outside the store. The claims themselves are part of the store's export.
