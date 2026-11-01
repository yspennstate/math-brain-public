# A hard computation bank, six arms, and the calculator inside the brain arm (5 October 2026)

The bank hard1k_v3 holds 1,000 generated problems in 25 families over algebra, combinatorics, games, geometry,
graphs, linear algebra, number theory and probability, each at three difficulty tiers, with exact answers. The
first 300 in id order were served to every arm. Claude Sonnet solved, ten minutes a problem. Every stream was
scanned for leak markers and none was flagged. The problems and keys are not published.

## Arms

| arm | what the solver had |
|---|---|
| nothing | the model alone, no tools |
| documents | the memory folder and a store snapshot, with read, grep and glob |
| documents and recall | documents and the recall command |
| math brain v4n | documents, the math brain's hooks and served notes, its audit prompts and recall, and a Lean command (90 s) |
| documents and Lean | documents and the brain arm's own Lean command, nothing else of the math brain |
| documents and Lean, one line | the same, plus one sentence from the brain arm's audit prompt: write the statement on a single line, since some agent shells refuse a quoted command that spans lines |

The last two arms were added during the run, each preregistered before any of its answers existed. On the first
192 problems the brain arm led the documents arm 158 to 105, and a Lean call had compiled on 79 of those problems,
76 of them right. 218 of its first 240 Lean calls carried an `#eval`. A compiled Lean call prints what it
evaluates, which makes it a calculator the other arms did not have.

## Results, 300 problems

| arm | right | tier 1 (85) | tier 2 (105) | tier 3 (110) | median seconds | cost (dollars) |
|---|---|---|---|---|---|---|
| nothing | 175 | 56 | 59 | 60 | 29 | 27.76 |
| documents | 168 | 54 | 56 | 58 | 37 | 28.99 |
| documents and recall | 149 | 52 | 50 | 47 | 48 | 21.65 |
| math brain v4n | 246 | 69 | 88 | 89 | 70 | 32.14 |
| documents and Lean | 179 | 59 | 56 | 64 | 36 | 18.77 |
| documents and Lean, one line | 265 | 78 | 94 | 93 | 90 | 15.41 |

Paired, exact McNemar (wins of the first arm against the second):

| comparison | first only | second only | p |
|---|---|---|---|
| math brain against nothing | 89 | 18 | 2e-12 |
| math brain against documents | 94 | 16 | 1e-14 |
| math brain against documents and Lean | 86 | 19 | 2e-11 |
| math brain against documents and Lean, one line | 28 | 47 | 0.037 |
| documents and Lean, one line, against documents and Lean | 102 | 16 | 2e-16 |
| documents and Lean, one line, against documents | 114 | 17 | 8e-19 |
| documents against nothing | 28 | 35 | 0.45 |
| documents and recall against documents | 25 | 44 | 0.030 |

The first Lean arm barely moved, because the permission layer refused a quoted statement that breaks onto a new
line beginning with `#`, as an `#eval` does: 70 of its first 207 Lean calls (34 per cent), and every attempt on
56 of the 95 problems where it tried. The brain arm was refused on 30 of 344 calls (9 per cent), because its audit
prompt carried the single-line sentence. With that one sentence and nothing else of the math brain, the documents
arm overtook the brain arm, 47 problems to 28. On linear algebra (18 determinant problems) every arm without a
working Lean call scored 0, the brain arm 11 and the one-line arm 16.

The brain arm's lead was the calculator. Setting aside the 117 problems where one of its Lean calls compiled (114
of them right), it stood level with documents (23 to 15, p = 0.26) and with nothing (22 to 16, p = 0.42). Its
served notes did not account for the lead either: it led documents by about the same margin where the hook served
a block (36 to 6 on 124 problems) and where it served nothing (58 to 10 on 176). Documents with recall lost to
documents alone, and gave no answer on 122 problems against 77.

The run led to the equal-tools design that followed (`equal-tools-five-arms-2026-10-05`): every arm gets the same
Python and Lean, named in the same words, so that the arms differ only in what they can read and recall.
