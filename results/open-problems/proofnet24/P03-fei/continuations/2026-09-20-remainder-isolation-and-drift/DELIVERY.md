# Recovery, executed checks, and repository delivery

20 September 2026. This record supersedes the predecessor's pending-delivery and unconfirmed-execution statements, not its mathematical scope. Full FEI remains unproved.

## What was actually recovered

The source was the mounted conversation archive `FEI_Remainder_Isolation_2026-09-20.zip`. Its original execution record reports a failed run: Python refused to stringify a fraction with more than 4,300 digits, and the checker status was `NOT_CONFIRMED`. That record and the original manifest are preserved under `recovered/`; they must not be cited as an earlier successful run. The archive did not contain the final verification output or the two generated certificate files.

The report has one typesetting repair in equation (2.4): a form-feed character was replaced by the intended LaTeX `\frac12`. The checker's only modification is its `str_interval` display routine, now rounding outward to a 96-bit dyadic grid before serialization. Its mathematical assertions, input families, and certificate generator were not weakened or changed. `restore_original_sources.py` reconstructs the exact original report and original checker under `recovered/`, verifies their original SHA-256 hashes, and refuses to overwrite a different historical version. This restoration was executed and its hashes matched.

The complete report, failed-route worklog, original handoff, proposed index addition, generator, and repaired checker are native repository files. The generated recursive-gate inputs and full two-band witness are now also present. Redundant ZIP/patch packaging wrappers remain in the conversation backup; no recovery of unavailable temporary files from an older session is claimed.

## Actual successful execution in this continuation

The repaired checker completed and generated a `PASS` result. A separate-directory replay reproduced all three generated files byte-for-byte:

| File | SHA-256 |
| --- | --- |
| `verify_remainder.py` | `a75acde78bb2dd22aba039ccfbcff1cc8cff75f06e60a3712726cac9c6e522da` |
| full `verification.json` | `c57ddc359c19b3cd1534db47a632276753c20ce06e8e8801be0eaa4d5aae3a5a` |
| `recursive_gate_certificates.json` | `c3aeaf2d85c2901107b6ffb2cf6fecfddd42a71fc879753542e00be6f98fa7ab` |
| `two_band_witness.json` | `e0308f176c0f3f97d650679c2709478f10b821656363e40e448fe09eb04da614` |

The evidence includes 33 isolation cases (24 actual full Walsh transforms, largest direct dimension 15), the six-variable transitive calibration at all six coordinates, seven all-coordinate symbolic parameter cases, 36 bounded-depth branch certificates, 31 actual inputs for a 1,024-variable recursive gate, and the actual nine-variable two-band witness. Large symbolic dimensions are not full truth-table enumerations. This is reproducibility, not independent mathematical review or a proof-assistant formalization.

The large output is stored as `verification.compact.json`: seven giant rational strings are represented by their exact factored formula; all other output data are unchanged. `python expand_verification.py` restores the full original executed JSON and checks its SHA-256 before writing it. Expansion was executed and returned byte-identical output. Running `verify_remainder.py` writes the full JSON directly. The compact archive is a lossless encoding, not a substituted approximate result.

## Confirmed commits and content identities

Report: commit `84e9590e61a598d9d276dc51a4e70b4630808f80`, blob `4ec0bd34e8a188b430f3bd5b028f83d4c2e4fb39`.

Repaired checker: commit `5af785a84e9efe16644827ff19e04772d6a86f58`, blob `96a218b267ba80acab28c16515fc0de6294be12b`.

Lossless output archive: commit `3354b21c173102593e685492bbc8a5aeaa996820`, blob `8adb50d8577c578d1e8c5691d5d4d5f273980567`.

Gate certificates: commit `cb64b57396ea58785064617417ac5c4eec0593d1`, blob `e1cc85a6e74775269864faf6802362b4cb28c902`.

Two-band witness: commit `4747cd83b7c9adb6d4939df957abb092c9358ff0`, blob `e69f95c2f7e16f3effdf658e9e3b104231565271`.

Each listed remote content hash was read back and matched the actual local bytes. No future worker's reading or use is implied by successful delivery.

## Substantive new continuation

The [growing-depth stopping proof](../2026-09-20-growing-remainder-stopping/REPORT.md) handles the predecessor's transitive obstruction with a dimension-growing tree. For that family, it proves a remainder payment at most five times consumed influence, maximum depth `O(log n)`, and expected query count `O(log n/log log n)`. The prior fixed-depth impossibility remains valid. The coefficient five is NOT a universal FEI or remainder bound.

New proof commit `31e92f8e7ed45dec82253a6c1bbf9ca5ea102379`, checker `25289a865623751a9fd10374c4a270e7787b6809`, output `e1b328e06a7df59cebc69171537762f129b6cc74`. The new checker separately replayed with byte-identical output. Its own manifest records exact scope and hashes.

No schedules, ownership, permissions, visibility, or native atlas metrics were changed. Mathematical novelty and unrestricted FEI are not established by this delivery.
