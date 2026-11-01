# Proof bank acceptance

`proof_bank_gate.py` checks a generic evidence contract for literature proof
questions. A generator's item count remains a candidate count. A one-step text
diff does not demonstrate that the changed argument has a mathematical defect.
An unchanged published argument also requires a soundness and context check.

The gate consumes five JSONL inputs: solver items, quarantined keys, source
records, semantic reviews, and split assignments. It writes a private detailed
report and prints only aggregate counts. It does not import a generator or use
model-generated labels as proof certificates. It validates review evidence;
the correctness of each review still requires mathematical judgment.

Each source record contains `item_id`, canonical full-object `item_sha256` and
`key_sha256`, `paper_id`, `proof_group`, `source_locator`, `license_uri`, the
full source file's `source_file_sha256`, `claim`, and all `original_steps`.
Canonical hashes use UTF-8 JSON, sorted object keys, no extra whitespace, and
the complete value. Item text must match this source except at the single
keyed step. Citation aliases and translated or analogous proofs must be
resolved to one group before assignment. ArXiv version suffixes are grouped
automatically. Paper, proof group, or identical original proof crossing
development, calibration, and heldout splits blocks acceptance.

Reviews use `schema: semantic-proof-review/v1`, bind complete item, key and
source objects, and identify their reviewer and `role` (`author` or
`independent`). Every accepted item needs distinct author and independent
reviewers. All these affirmative judgments must be explicit:

- `complete_source_read`, `source_fidelity`, `self_contained`, `original_sound`,
  and `research_substance` are true;
- `valid` is `yes`, with `reason`, `source_fidelity_reason`, and
  `soundness_reason` giving the actual assessment;
- for a flawed item, `exactly_one_semantic_defect` is true,
  `first_invalid_step` matches the key, and `defect_explanation`,
  `minimal_repair`, and `falsifier` explain the error;
- for a clean item, `first_invalid_step` is null.

A negative or uncertain review holds the item for adjudication. A text-only
legacy review `{item_id, valid, reason}` remains useful evidence but does not
meet this stronger acceptance contract. No status is inferred from its length
or from an operator's presumed reliability. Licensing metadata is recorded,
not treated as redistribution permission; a separate distribution review is
required. The gate's fixtures are simple original controls for evidence
handling, and do not constitute research-level bank questions.

Keep keys, reviews, source originals, split maps, and detailed reports outside
all solver-readable and brain-indexed locations. Do not commit private prompt
records, proof keys, or identifying examples with the generic mechanism. The
solver item allowlist excludes provenance and answer fields. This is not a
substitute for inspecting served prompts, retrieved note contents, model
identity, response transport, explanation correctness, and false positives.

Run `python -m unittest test_proof_bank_gate -v` from this directory. Invoke the
gate with `--items`, `--keys`, `--sources`, `--reviews`, `--splits`, and
`--private-report`. Omitted review/source/split inputs yield zero accepted
items, which is useful for measuring the current evidence gap. Exit status 2
means some candidates remain unaccepted; status 0 means all supplied candidates
met this evidence contract. Neither status claims a measured brain benefit.
