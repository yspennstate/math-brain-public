# Cross-family labels on the 300-worker wave (sealed Claude, 10 Oct 2026)

One read per target over every claim its workers labelled proved, independently checked or counterexample. Labels: PROVED (complete proof of exactly the claim), PARTIAL (a weaker statement proved), COUNTEREXAMPLE, DRAFT (not established). Per-claim rows in LABELS.jsonl; FIX and DROP rows in FIX_DROP_FOR_INTEGRATOR.jsonl.

| target | PROVED | PARTIAL | COUNTEREXAMPLE | DRAFT | UNREAD |
|---|---|---|---|---|---|
| C0017 | 24 | 1 | 16 | 4 | 0 |
| C0023 | 44 | 1 | 7 | 2 | 0 |
| C0029 | 22 | 0 | 15 | 0 | 0 |
| C0041 | 36 | 0 | 13 | 1 | 0 |
| C0044 | 13 | 9 | 6 | 0 | 0 |
| C0047 | 37 | 0 | 7 | 0 | 0 |
| C0048 | 24 | 7 | 11 | 1 | 0 |
| C0049 | 14 | 0 | 8 | 2 | 0 |
| C0051 | 0 | 0 | 0 | 1 | 0 |
| C0052 | 19 | 6 | 10 | 0 | 0 |
| C0054 | 10 | 1 | 0 | 0 | 0 |
| C0056 | 32 | 0 | 15 | 0 | 0 |
| C0064 | 2 | 0 | 0 | 0 | 0 |
| C0120 | 36 | 0 | 6 | 0 | 0 |
| P0003 | 36 | 0 | 22 | 1 | 0 |
| P0017 | 51 | 1 | 13 | 0 | 0 |
| P0043 | 54 | 1 | 0 | 1 | 0 |
| P0104 | 36 | 6 | 13 | 0 | 0 |
| P0110 | 45 | 2 | 18 | 0 | 0 |
| P0117 | 38 | 0 | 12 | 3 | 0 |
| P0162 | 44 | 0 | 8 | 4 | 0 |
| P0297 | 38 | 1 | 17 | 0 | 0 |
| P0309 | 40 | 0 | 10 | 0 | 0 |
| P0321 | 28 | 1 | 14 | 0 | 0 |
| all | 723 | 37 | 241 | 20 | 0 |

FIX: 31, DROP: 0, of 1021 claims.

How far to trust these labels: each read covered every strong claim of one target at once (about 40 claims, up to 400 KB of attempts), so a label is a first sorting by a second model family, not a line-by-line proof check. The claims are mostly lemma-sized steps and special cases; PROVED means the step's proof held up in that read, never that a big open problem was solved; counterexamples are mostly to proposed routes. UNREAD (0: ) are claims with no label: two first reads were killed in flight, and by the re-read most of those workers' files had moved to GitHub (probability_campaigns/codex_pool_2026-10-10/), where a later pass can read them.
