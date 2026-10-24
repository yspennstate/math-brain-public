# HARD8-04 literature/status gate — 2026-09-16

## Parent source

- Afonso S. Bandeira, Anastasia Kireeva, Antoine Maillard, Almut Rödder, *Randomstrasse101: Open Problems of 2024*, arXiv:2504.20539, Conjecture 14: Hadamard existence conjecture.
- Fresh arXiv query on 2026-09-16 recovered the same source and no universal all-orders solution.

## Maintained construction table

- Matteo Cati and Dmitrii V. Pasechnik, *A database of constructions of Hadamard matrices*, arXiv:2411.18897v2 (2025-08-30), Table 4.
- The machine-diffed transcription in `JD-Jones-ASES/Hadamard-T`, `data/cp-table4-v2.json`, records consecutive entries `515(3)` and `523(3)`, so in that dated table H(2060) and H(2092) were not recorded known.

## Order 2060 gate corrected

The current `JD-Jones-ASES/Hadamard-T` main branch, commit
`1699c317e6c6515962ba48c4b5e35ab2ea225bab` (2026-08-31), states in its README, note and certificate documentation that:

1. Schneider publicly posted an H(2060) artifact on 2026-08-23 at gist `b866a2ff2fcd93934f0db54cfa4069d0`;
2. the artifact was checked exactly and decoded to an explicit four-sequence length-515 supplementary seed;
3. the repository's section 6.5 therefore classifies 2060 as closed by the public record and states that the next unresolved order of the form `4 * odd`, under the audited Cati-Pasechnik Table-4 status, is `2092 = 4 * 523`.

This run independently checked the published decoded seed rather than executing the external repository automation. The task-local checker constructs a 2060-by-2060 Goethals-Seidel matrix, verifies every entry is +/-1, and checks all 2,120,770 distinct row pairs exactly. Therefore 2060 is **KNOWN / INELIGIBLE FOR METRIC CREDIT** in HARD8-04.

The historical Miyamoto (1991) Section-7 route is a separate issue. The newer formal/audit repositories argue that Miyamoto's printed mechanism does not support the 2060 entry, but this does not reopen 2060 because Schneider's independent 2026 artifact closes the order.

## Admission of 2092

`Hadamard-T` section 6.5 explicitly states, with label `REPORTED-FROM-AUDITED-TABLE`, that after the 2026-08-23 closure of 2060, the next unresolved order of the form `4 * odd` in the machine-diffed Table-4 frontier is

`2092 = 4 * 523`, with 523 prime.

A fresh bounded 2026-09-16 web search used the exact queries:

- `"Hadamard matrix of order 2092"`
- `"2092" Hadamard Schneider`
- `"523" Hadamard matrix 2026`
- `"H(2092)" Hadamard`

and found no relevant status-changing primary construction. This negative search is **not** itself treated as proof of openness. The admission relies on the dated audited-table statement in the current Hadamard-T source, not on absence of search hits. Any later primary construction supersedes this admission immediately.

## Nearby current literature checked

- Cati-Pasechnik database source above.
- Hadamard-T / Hadamard-formal public certificate repositories through 2026-08-31.
- Bennett-Bright-Colinot-Nayak, *Quaternionic Perfect Sequences and Hadamard Matrices*, arXiv:2601.22337: exhaustive circulant Williamson-type work through small block orders; it does not supply H(2092).

## Access gaps / caution

- No claim is made that Cati-Pasechnik Table 4 is a nonexistence theorem; it is a dated knowledge table.
- The direct Schneider H(2060) gist payload itself was not re-downloaded byte-for-byte into this task's repository. Instead the explicit length-515 seed published in Hadamard-T and credited to that artifact was independently rebuilt and verified here.
- No current primary construction of H(2092) was found in the bounded search, but future/public-posting activity in this area is rapid; status must be rechecked every run.
