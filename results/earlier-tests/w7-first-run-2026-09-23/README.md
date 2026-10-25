# The first run of the W7 bank, 23 September 2026

Eighty questions: 50 about results held in the math store, 10 about open conjectures the store carries, and 20
questions of ordinary mathematics that need no store. Two Opus 5.5 agents at their highest thinking setting answered
all of them, one with the brain (the cards the math hook serves and the recall tool) and one without it, allowed
only to read the questions and write its answers. Both still received the instruction files every session loads, and
a question whose answer sits in those files was dropped from both arms before scoring; that removed one store
question and leaves 79. A blind grader marked each answer 0, 0.5 or 1 against the keys and flagged any confident
false claim. The same bank was used again on 4 October for the five-arm test in
`../three-arm-w7-2026-10-04`.

| questions | n | full credit, brain | full credit, no brain | helped / harmed | exact McNemar p |
|---|---|---|---|---|---|
| about stored results | 49 | 49 | 8 | 41 / 0 | 9.1e-13 |
| open conjectures | 10 | 10 | 4 | 6 / 0 | 0.031 |
| ordinary mathematics | 20 | 20 | 20 | 0 / 0 | 1.0 |
| all | 79 | 79 | 32 | 47 / 0 | 1.4e-14 |

These are the marks after adjudication; as keyed they were 76 and 30. Without the brain the agent answered "unknown"
on 32 questions, with it on none. The questions about stored results measure access to the store's own results, so
the gap there is expected by construction. The other two rows carry the information: the brain did not cost anything
on ordinary mathematics, and on the conjectures it lifted full credit from 4 of 10 to 10 of 10.

Three marks changed at adjudication, and each time the key was at fault rather than the answer.

- On the Poisson minimal spanning forest, the key restated a store card which concluded, from no percolation at the
  critical point and uniqueness, that the forest is a single tree. Those facts give
  free = wired and one-ended trees, not connectedness, and the same argument would settle the lattice case in
  dimension 11 and above, which is open. Both arms gave the accepted picture (infinitely many trees in high
  dimension, after Newman and Stein) and were marked right.
- On a gossip-problem question, the key followed a result that had since been narrowed (unconditional for n = 4 and
  every k, and for k = 2 with n at most 5; the remaining values computed). The brain arm gave the narrowed statement.
- On one ordinary question, the key named the wrong first paper: Baik, Deift and Johansson (1999) proved the t^{1/3}
  fluctuations with the GUE Tracy-Widom limit for Poissonian last passage. Both arms named them.

On a fourth question the mark stood but the key's last clause was false: it called the 24-cell locally projectively
rigid, whereas arXiv:2609.02818 shows only that its expected local dimension, 48, exceeds dim PGL(5) = 24. The store
cards behind the first and fourth keys, and two related polytope cards (one held that all six regular 4-polytopes
are rigid, when only the 5-cell is; the other gave a wrong tangent dimension for the 24-cell), are now superseded in the store by corrected claims, which the hook serves first. On 7 of the
80 questions the hook served nothing, having judged them not to be mathematics.

## Files

`rows.json` holds each question's id, kind, whether its key could be guessed without the store, and its mark in each
arm before and after adjudication. `python recompute.py` derives both tables (as keyed and adjudicated) and checks
them. The questions, keys, answers and the grader's notes are not included, so that the bank stays usable.
