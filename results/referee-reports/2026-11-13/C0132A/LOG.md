# C0132 working log

Task received: 2026-11-13, approximately 03:24 Asia/Tbilisi (the supplied prompt has no receipt timestamp; this is the first shell observation).

## 2026-11-13 03:24–03:27 +04 — literature audit

- Read the startup memory, recalled the brain, and read the agent-mesh protocol. Global mesh registration, claim/assert, and checklist updates fail because their stores are outside the sandbox's writable roots. A read-only query of the real mesh found no live claims overlapping this workspace and no C0132/balanced-excited-walk task. No global coordination state was changed. All deliverables stay in this isolated workspace; no subagents are used.
- Compute governor at startup: status `ok`, mode `owner_away_open`. Any simulation will use one low-priority process and bounded memory.
- Verified Benjamini–Kozma–Schapira (2011): transience of M(2,2).
- Located Peres–Popov–Sousi (2013), Theorem 1.2. Its phrase “d-dimensional measures” means each covariance is invertible; it does not apply to the singular step laws here.
- Located Peres–Schapira–Sousi (2016), arXiv:1403.1571: transience of M(1,2).
- Located Angel–Holmes–Ramírez (2021 preprint, published 2023), arXiv:2110.15889: planar range and recurrent-set results, requiring inspection of theorem statements.
- Located Qin (September 2026), arXiv:2609.30045. Its M(2,1,2) uses horizontal first departures and planar subsequent departures; it is not M(1,1). The introduction expressly leaves recurrence of M(2,1,1), i.e. the requested M(1,1), conjectural.
- An accidentally opened, unrelated arXiv identifier 1504.07944 was discarded; it supplies no evidence for this report.

NEXT: finish exact source statements and the M(2,1) search before simulations.

## 2026-11-13 03:27–03:34 +04 — source verification and simulations

- Camarena–Panizo–Ramírez, arXiv:2002.05750v2, introduction, explicitly says M(2,1) is open; the chapter appeared in 2021. Peres–Schapira–Sousi, Section 4, explains why their M(1,2) proof does not apply to M(2,1). Searches through November 2026 found no later settlement. Qin's September 2026 introduction still identifies only the M(1,2) transience result and explicitly leaves M(1,1) recurrence conjectural.
- Downloaded the primary PDFs/HTML and recorded URLs in `sources/manifest.json`. Author preprint of Angel–Holmes–Ramírez supplies exact Theorems 1.1 and 1.5; publisher metadata verifies Annals of Probability 51(4), 1421–1448 (2023). The final publisher PDF and full IMS issue were blocked by an HTML security page; the latter is retained as `sources/aop_51_4.failed.html`, not used as a PDF.
- Built `code/simulate.cpp` with clang++ and independently replayed 120,000 transitions using departure counts in `code/verify.py`. The model uses two separately seeded SplitMix64 streams and an exact packed-coordinate hash set; coordinate overflow and table overload terminate the run. Range/clock identity is asserted at every checkpoint.
- Initial attempt to lower priority with `os.nice(10)` failed because the inherited process already has nice 20. The runner now checks that priority is at least 10. macOS sandbox also rejects RLIMIT_AS changes; the table is deterministically 128 MiB and measured peak child RSS is 135,544,832 bytes. No worker pools or background services were created.
- Completed 128 seeds per open case, each to 10^7 steps: 2.56 billion transitions in total. Each run used one process/thread; cases ran sequentially. Raw checkpoints are in `data/m11.csv` and `data/m21.csv`; timing/RSS in `data/resources.json`.
- At 10^7 steps the mean ranges are 589,396 (M(1,1)) and 6,073,117 (M(2,1)); late-window origin hits occurred for 4/128 and 0/128 seeds respectively. Finite-horizon estimates do not prove either classification.
- Corrected the previous note's geometry: a column's visited/consumed set need not be an interval. `code/verify.py` checks a legal ten-step path leaving sites 0 and 2 visited in column zero but site 1 unvisited. The exact conditional return probability can therefore be zero despite repeated returns of the first projection.
- A separate Python/MT19937 implementation is checking 16 seeds per case to 10^6 steps, independently of the C++ RNG and hash table.

NEXT: prove a range-clock bound for M(2,1), write the exact conditional recurrence criterion with proof, and generate numerical summaries with uncertainty.
