# Proof bank acceptance gate, 6 September 2026

Literature proof questions are made by taking a published proof and changing one step, or leaving it unchanged. A count of generated items is a count of candidates, not of usable questions. A one-step text change does not show that the argument now has a mathematical defect, and an unchanged argument still needs a check that it is sound in context.

`proof_bank_gate.py` takes five JSONL inputs: solver items, quarantined keys, source records, semantic reviews and split assignments. It accepts an item only when the following hold:

- The item matches its full source except at the keyed step, and every object is bound by a canonical SHA-256 hash.
- Two distinct reviewers, one the author and one independent, have each given every affirmative judgment the contract requires: that the whole source was read, that the item is faithful to it, that the original is sound, and that it has research substance. For a flawed item they also confirm exactly one semantic defect at the keyed step, with an explanation, a minimal repair and a falsifier.
- No paper, proof group or identical original proof crosses the development, calibration and held-out splits. ArXiv version suffixes are grouped automatically.

A negative or uncertain review holds the item for adjudication. The gate prints only aggregate counts and writes its detailed report to a private file. Exit status 2 means some candidates were not accepted, and 0 means every supplied candidate met the contract. Neither status says anything about whether the brain helps. `PROOF_BANK_ACCEPTANCE.md` gives the full contract.

The two patches correct the PLIT proof extractor. One pairs each proof with its own statement when a theorem has several numbered proof parts. The other keeps the full source reference on every note served to a solver. Each patch comes with tests.

The gate's tests run on their own with `python -m unittest test_proof_bank_gate -v`. The two PLIT tests run against the code they patch: `python test_plit_extractor_pairing.py --module path/to/extract_proofs.py`, and `test_plit_note_source_identity` with `PLIT_NOTES_UNDER_TEST` set to the note builder (without it, those cases are skipped). Every fixture is a simple synthetic control and none is a bank question. The bank itself, its keys, the reviews and the split maps are private and are not included.
