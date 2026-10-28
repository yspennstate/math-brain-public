# Protocol-aware PLIT report, 7 September 2026

The first stage of PLIT was served overnight on 6 to 7 September. Its grader reported the pooled all-tier full-credit contrast as the primary result. The frozen protocol and its third amendment name a different primary population: tier A for a solver below the ceiling and tier B for a solver at the tier-A ceiling. The sizing file chose tier A for Haiku and tier B for Opus.

This folder holds a separate report producer. It reads the served results without changing them and recomputes the primary comparison on the populations the protocol names. It requires full coverage of the planned items and arms, strict row identities and an explicit primary tier, and it reports planned and achieved counts side by side. A missing, duplicated, malformed or wrong-arm row stops the report rather than shrinking the population. Pooled counts are still printed, as descriptive figures. The producer does not change answer keys, frozen samples or the original grader.

## Result

| Solver | Primary tier | Correct, brain arm | Correct, no-brain arm | Pairs achieved / planned |
|---|---|---:|---:|---:|
| Haiku | A | 44/82 | 46/82 | 82/120 |
| Opus | B | 37/64 | 38/64 | 64/146 |

Neither comparison shows a benefit, equivalence or general harm, and neither reached its planned number of pairs. A separate SQL aggregation (`check_sqlite.py`) reproduced all four primary arm counts and their exact binomial probabilities over 1,170 response rows. On the protocol's arithmetic, the remaining room to gain is 43.90 percentage points for Haiku and 40.625 for Opus. That is the ceiling on the possible effect, not the statistical power.

The campaign also reviewed calibration material. Twenty new calibration forms from ten proofs in nine source families were reviewed independently, which brings the accepted calibration inventory to 46 forms from 25 proofs in 13 families. Two further forms from one proof are provisional held-out material and are not certified as untouched. `check_inventory_sqlite.py` counted both populations independently and found that no source family crosses the split. Acceptance here means a local review of each adapted proof. It is not a review of the source paper as published.

## Files

- `protocol_report.py` produces the report from a pinned snapshot, and `check_sqlite.py` is the independent counting lane.
- `recover_accepted_inventory.py`, `check_inventory_sqlite.py` and `corpus_inventory.py` rebuild and count the calibration inventory.
- `export_reviewed_calibration.py` exports reviewed forms under random aliases.
- `review_queue.py`, `extend_context.py`, `pin_plit.py`, `capture_source_metadata.py` and `check_population_reflex.py` are helpers.
- `write_finding.py` and `render_dashboard.py` produce the campaign record.
- The tests are run with `python -m unittest test_protocol_report test_reviewed_calibration test_inventory_transport`. All 21 protocol tests, 24 export tests and 4 transport tests passed, and they use synthetic fixtures only.

The snapshots, answer keys, item text and the status file with their hashes are private evaluation material and are not included. Local paths are replaced by `<HOME>` and `<BRAIN>`.
