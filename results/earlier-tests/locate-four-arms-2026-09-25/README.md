# The locate banks in four arms, 25 September 2026

The 130 questions of the locate banks (`locate-and-proof-banks-2026-09-11`: 40 strip walk counts and 20 campaign
constants in L1, 40 problem-ledger pages in L2, 30 differences of two stored walk counts in L3) were put to Sonnet 5
in four arms. Each question asks for a value the math store holds and nothing else does, so the arms differ only in
how the solver may reach the store.

- **both:** the block the hook served for the question (captured once from the frozen hook, candidate 65 of
  `mathbrain-10d-landings-2026-09-24`), plus file tools over the memory folder and a clone of the store's repository,
  with recall by hand.
- **files:** the same file tools and recall, with no hook and no served block.
- **connected:** the served block alone, no tools.
- **sterile:** the question alone, no tools.

One headless run per item per arm, the banks' own instructions, the keys held outside every solver's reach and read
only by the grading script. Before anything was served, a reach probe confirmed that the tool arms could read the
memory folder, run recall and open the repository, and could not read the keys, the test folder or anything through
the shell, and that neither the files nor the sterile arm received an instruction file or a served block.

| arm | correct | unknown | wrong | error | input tokens (median) | turns (median) | seconds (median) | USD, whole bank |
|---|---|---|---|---|---|---|---|---|
| both | 130 | 0 | 0 | 0 | 8,716 | 1 | 12.6 | 2.43 |
| files | 100 | 29 | 0 | 1 | 53,701 | 7 | 54.0 | 7.10 |
| connected | 129 | 1 | 0 | 0 | 5,295 | 1 | 23.6 | 1.82 |
| sterile | 3 | 124 | 1 | 2 | 4,337 | 1 | 20.6 | 2.20 |

By family, correct (both / files / connected / sterile): campaign constants 20 / 20 / 19 / 2, walk counts
40 / 26 / 40 / 0, ledger pages 40 / 40 / 40 / 0, differences of two counts 30 / 14 / 30 / 1.

Paired on the same items, with exact McNemar tests: both right where files is not on 30 items and the reverse on
none (p = 1.9e-9); connected against files 30 to 1 (p = 3.0e-8); files against sterile 97 to 0. Both against
connected is 1 to 0, which says nothing either way: with connected at 129 the bank left one item for the file tools
to add. The served block held the value on 127 of the 130 questions and both brain arms answered all 127.
The only wrong value in the whole test is one sterile guess at a walk count. The cost is in dollars at API prices.

Every value the files arm missed was in the repository it could read. On its misses it stopped after a few turns,
having searched the memory folder, where recall looks, while the computed results live in the store's export. Two
follow-ups on the files arm measured this directly. With one added sentence saying where the math brain keeps its
computed results, the files arm answered 26 of its 30 misses, at the same cost per item. With no added sentence,
after a memory saying the same thing had been filed in the memory folder, it answered 22 of the 30 misses and 17 of
20 control items it had answered before. The served block does that routing without being asked: the both arm
needed one turn and a third of the files arm's dollars to reach every value.

Limits: the questions quote the stored parameters, so a text search over the export finds them once the solver
looks in the right place; one run per item and arm; Sonnet 5 only.

## Files

`rows.json` holds one row per question under an opaque id: bank, family, whether the served block held the value,
and for each arm the grade, turns, seconds, cost and tokens. Questions, keys and answers are not included.
`python recompute.py` rebuilds the table, the family counts and the paired tests from it.
