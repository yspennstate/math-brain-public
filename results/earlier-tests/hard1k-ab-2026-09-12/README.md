# A 1,000-item test, brain on against brain off, 12-13 September 2026

One thousand items, each answered twice by Opus 5 agents at maximum effort: once with nothing (arm A) and once with
the note block the math hook serves for that item (arm B). Arm B ran no live query of the store. It answered from the
served block alone, so the test measures what the hook delivers and nothing else.

## The items

| family | items | what is asked |
|---|---|---|
| op_pagesum | 260 | the sum of the PDF pages on which three named open problems of the store's ledger are posed |
| op_pagediff | 150 | the signed difference of two such pages |
| op_pagemax | 73 | which of four named problems is posed on the highest page (a letter) |
| op_oddsource | 140 | which of four problems is cited to a different source (a letter) |
| saw_triple, saw_spread4, saw_growthdiff | 300 | counts of self-avoiding walks in a strip with forbidden sites, and differences of counts |
| proof_audit | 77 | a proof in numbered steps: valid or flawed, and if flawed the first faulty step |

The ledger items are lookups over one to four of the 214 ledger problems that have a unique name, a parsed page and a
parsed source; every key was derived twice from separate reads, with no mismatch. The proof audits were written by
one agent and kept only when an independent verifier confirmed the key. The grader requires an exact integer, an exact
signed integer or the exact letter; a proof audit counts only when both the verdict and the step are right.

Two families were included as controls rather than as tests. A strong solver can compute the walk counts, and the
odd-source question turns out to be answerable from the wording of the prompt.

## Result

| family | n | without the brain | with the brain | helped | harmed |
|---|---|---|---|---|---|
| op_pagesum | 260 | 0 | 260 | 260 | 0 |
| op_pagediff | 150 | 0 | 150 | 150 | 0 |
| op_pagemax | 73 | 21 (chance is 25%) | 73 | 52 | 0 |
| op_oddsource | 140 | 140 | 140 | 0 | 0 |
| self-avoiding walks | 300 | 300 | 300 | 0 | 0 |
| proof_audit | 77 | 77 | 77 | 0 | 0 |
| all | 1,000 | 538 | 1,000 | 462 | 0 |

All 462 discordant pairs favour the brain (exact McNemar, two-sided, p = 1.7e-139). Where the answer has to be
recalled, the served block moves the solver from zero or chance to every item. Where the solver can derive the
answer, the block changes nothing, and in 538 such items it harmed none. The proof audits stood at 77 of 77 in both
arms: the bank was at its ceiling, because the same model that solves the proofs wrote them, and it could not make
them hard enough.

This is a retrieval test with a mathematical control inside it. It shows that the hook reaches the right rows and
that a solver uses them without inventing values. It does not show any gain in mathematical reasoning.

## Checks made before the score was accepted

- The keys were kept in a separate directory that no solver was pointed to. Every agent transcript was scanned for
  that directory's path inside any tool input. The scanner was first run on writes known to have happened (it
  found all 44) so that a zero would mean something; across sixteen transcripts it found zero touches.
- At the first capture 28 of the 1,000 items received no note. Twenty-three died at the near-tie margin of the
  selector: they name two to four problems by quoted title, and two titles ranked a hair apart. The hook now runs
  one sub-query per quoted title. The other five were walk-difference questions whose two parameter sets sat in one
  clause joined by a bare "and"; the clause splitter now cuts there. After both changes every item received a note,
  and the standing instruments held: the fresh bank's unnamed questions moved from 71 to 72 of 89 served (named
  84 unchanged), absent-target fires from 28 to 27 of 40, value in block was identical, and locate reach stayed 40
  of 40 served with one item dropping from rank 1.
- Each arm ran as four agents, one per group of ten shards, each writing one answer file per shard and skipping
  written shards on resume, so a run cut by a usage limit lost nothing.

## Files

`rows/GRADE_ROWS.json` holds one row per item: its id, kind, family and whether each arm was right.
`python recompute.py` derives the result table and the p-value from the rows and checks them. The questions, keys,
served blocks and answers are not included, so that the bank stays usable.
