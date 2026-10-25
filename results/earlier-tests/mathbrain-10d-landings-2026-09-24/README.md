# Twenty landings of the math hook, 24 to 28 September 2026

Between 24 and 28 September a campaign changed the math hook (`framework/dreaming/math_sense.py` and, in the first
packages, the prefilter, the retrieval and semantic layers of the store and a new expansion module) in small packages.
Each package was built as a full copy of the hook, compared with the live files, measured, and then copied over them.
This folder records the 20 packages that landed: when, what each changed, which files and how many lines, and, where
it was run, the hook's counts on the fixed 218-prompt bank of `hook-path-ablations-2026-09-23` and
`nightly-math-gate-2026-09-11-to-10-25` (89 results asked unnamed and named, 40 the store did not hold).

The landing order is fixed by the files themselves: each package records the hash of the hook it was built on and the
hash it leaves, and a package landed when the next package starts from its hash. The hashes are of the hook as it ran
on our machine; the copy in this repository is a later, cleaned edition and does not match them.

| cand. | landed | change | files (lines + / -) | unnamed served / first / silent | named served / first / silent | unanswerable with a card (target) |
|---|---|---|---|---|---|---|
| 14 | 24 Sep 16:37 | First landing, cut from candidates 11 and 12: long passages of non-mathematical text no longer open the hook. | math_sense.py +345 -1, math_prefilter.py +19 -1, retrieval.py +53 -2, semantic.py +47 -10 | 71 / 56 / 8 | 86 / 83 / 1 | 26 (7) |
| 22 | 24 Sep 19:47 | The silences of candidate 17, document expansion, a time budget for headless runs, and named problems. | math_sense.py +259 -4, math_prefilter.py +28 -3, retrieval.py +51 -2, expansion.py +166 -0 | 71 / 55 / 8 | 86 / 83 / 1 | 26 (7) |
| 28 | 25 Sep 00:55 | An origin tag on cards the store holds only from our own records; signals pooled from a sidecar; function words treated as generic; nine typed cards; a failed-route card for one method. | math_sense.py +77 -3, math_prefilter.py +19 -1, retrieval.py +110 -0 | 71 / 55 / 8 | 86 / 83 / 1 | 27 (8) |
| 33 | 25 Sep 02:46 | Two cards stating the same result count as one result; plurals accepted at the entry gate. | math_sense.py +178 -1 | - | - | - |
| 34 | 25 Sep (between 02:46 and 06:26) | On prompts of 80 words or more, cards titled by a slug follow the same lead-named rule as other cards. | math_sense.py +27 -1 | - | - | - |
| 36 | 25 Sep 06:26 | The house coverage floor on by default (0.25, lead mode); letter exponents accepted at the entry gate. | math_sense.py +84 -7 | - | - | - |
| 40 | 25 Sep 08:46 | A named sub-query split from a long prompt may refill a block the gates emptied. | math_sense.py +24 -4 | 71 / 55 / 9 | 86 / 83 / 1 | 27 (8) |
| 41 | 25 Sep 09:19 | The refill rule judged by the sub-query's source; no refill from a quoted phrase the store does not hold. | math_sense.py +18 -9 | 71 / 55 / 9 | 86 / 83 / 1 | 27 (8) |
| 42 | 25 Sep 12:28 | Named sub-queries merged round-robin over three depths. | math_sense.py +12 -0 | 71 / 55 / 9 | 86 / 83 / 1 | 27 (8) |
| 46 | 25 Sep 14:34 | Pasted research reports are no longer read as proof text. | math_sense.py +72 -9 | 71 / 55 / 9 | 86 / 83 / 1 | 27 (8) |
| 55 | 25 Sep 16:56 | Dash folding in the word-set tests (Cauchy-Schwarz and the like), and a fix to the named sub-query. | math_sense.py +153 -11, retrieval.py +61 -3 | 71 / 55 / 9 | 86 / 83 / 1 | 27 (8) |
| 65 | 25 Sep 19:1x-19:4x | Eighteen dials from candidates 56 to 65, among them accented names merged with their plain twins (Rouché, Grönwall, Picard-Lindelöf, Itô) and Wald's identity served. | math_sense.py +313 -46 | 71 / 55 / 9 | 87 / 84 / 0 | 27 (8) |
| 71 | 26 Sep 09:2x | A named result of a wider kind ("Fredholm alternative") opens the entry gate when the store holds a card about it. | math_sense.py +156 -7 | - | - | - |
| 74 | 27 Sep 21-22 | A vouch route for plainly worded questions. | math_sense.py +69 -1 | 71 / 55 / 9 | 87 / 84 / 0 | 27 (8) |
| 75 | 27-28 Sep | The coverage floor yields to a stronger card. | math_sense.py +42 -4 | 71 / 55 / 9 | 87 / 84 / 0 | 27 (8) |
| 76 | 28 Sep 04-05 | The agreed card is sealed through delivery. (from a scheduled code audit) | math_sense.py +19 -1 | 71 / 55 / 9 | 87 / 84 / 0 | 27 (8) |
| 78 | 28 Sep 06 | Per-prompt state is reset at the start of each prompt. | math_sense.py +4 -0 | - | - | - |
| 79 | 28 Sep 08 | The semantic top-list cache is cleared for each prompt. (from a scheduled code audit) | math_sense.py +1 -0 | - | - | - |
| 80 | 28 Sep 09 | A failed vocabulary read is not cached. (from a scheduled code audit) | math_sense.py +1 -1 | - | - | - |
| 81 | 28 Sep 13 | A failed document-frequency or expansion read is not cached. (from a scheduled code audit) | math_sense.py +26 -23 | - | - | - |

The fixed bank barely moved over the five days: the unnamed form stayed at 71 served, 55 or 56 first, 8 or 9 silent,
and the named form went from 86 to 87 served and 83 to 84 first, with its last silence gone after candidate 65. That is
the intended reading. The bank was the guard, run before each landing so that a change aimed elsewhere did not cost
the hook what it already did; the changes themselves were aimed at long research prompts, named sub-queries, accented
and dashed names and caching faults, and were measured on other banks: questions on our own mathematics, the locate
and pivot banks, and a sample of real past prompts. Their prompts and keys are kept private.
Four of the late packages came out of scheduled audits of the hook's code and fix faults of state carried from one
prompt to the next.

Candidate 71's own summary on the bank reads 63 / 47 / 19 and 77 / 75 / 10. It came from a run on a heavily loaded
machine; the paired re-run of all 218 rows around that landing found no row that differed, so the row is left out of
the table. Between candidate 71 and candidate 74 the live hook changed once outside the campaign's packages (candidate
74 starts from a hook no package left); `python check.py` reports that place and no other.

Built and measured but not landed: 12 (cut down into candidate 14); 17 (folded into candidate 22); 20 (superseded by candidate 22); 25 (superseded by candidate 28); 26 (superseded by candidate 28).

## Files

`landings.json` holds every package, landed or not: the change, the files with the hash before and after (the first 16
hex digits of the sha256) and the lines added and removed, and the bank counts of its last 218-prompt run.
`python check.py` walks the landed packages in order, checks that each starts from the hook the previous one left, and
prints the bank counts.
