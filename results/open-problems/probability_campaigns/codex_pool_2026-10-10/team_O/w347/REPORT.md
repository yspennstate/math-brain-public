P0033 blind audit. The earlier source row needs a locator fix: the annotated ledger has a candidate entry at line 22 and a separate settled claim at line 636; the newer card remains unverified. I kept the proof row after checking the AND/OR disagreement contraction, the same-colour flow, stationarity, and non-ergodicity against the book definition.

Measurement: python -B -X utf8 checks/p0033_exact.py passed 101 exact disagreement cases and 80 selected-child configurations with zero rational error; depth 20 was 0.014436068111854463, below the proved bound 0.060788327295284675.

Risk: prior art is unchecked and the store card truth status remains unverified; the KEEP is proof validity only. No Lean check or edge claim was in this row. The audit verdicts are in udits/w331.jsonl; no live files were changed.

NEXT: w331 should correct the source quote/locator; the mathematical proof can be retained while novelty remains unverified.
