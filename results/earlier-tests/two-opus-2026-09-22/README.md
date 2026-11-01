# Two Opus 5 agents with and without the brain, 22 September 2026

Two Opus 5 agents at their highest thinking setting each took the same bank, one with the brain (the recall tool,
the math hook and the store's notes) and one without it, allowed only to read the questions and write its answers
once. The bank had two halves of 30 items. The half reported here asks about mathematical results that had entered
the math store that month: refutations and settlements of named open problems, constants found in the FEI
campaign, and similar. The other half was built from the brain's own working rules and is not published; the
control answered all of those from general knowledge, so that half did not discriminate. The control flagged as
contaminated any item whose answer sat in the instruction files every session loads, and those were dropped from
both arms, which leaves 27 math items. Answers were graded blind under masked row ids.

| items | brain correct | no brain correct | no brain partial / abstained | helped / harmed | exact sign test |
|---|---|---|---|---|---|
| 27 | 27 | 1 | 1 / 25 | 26 / 0 | p = 3.0e-08 |

Without the brain the agent abstained on 25 of 27, which is the expected outcome for results too recent to be in
its training; the test measures whether the store hands them back, and it did on every item. Both arms together
cost 27.17 dollars at Opus 5 list prices for the whole bank (22.80 with the brain, 4.37 without). Nearly all of
the difference is context the hooks inject and the agent re-reads on each tool call, not the answers.

The retrieval check run beside the arms found that the math hook served the source card for 25 of the 30
questions, 23 of them first. Four questions got no card: three were refused by the hook's anchor gate (they
named read-once formulas, a conjectured constant, and two numbered problems from Janson's list) and one by its
coverage gate. Widening the anchors with the words those three lacked (the plural numbered citation and the
eponyms the store carries) was measured against the gate's archive of refused prompts: one extra admission in
about 21,500, none of the must-stay-silent probes admitted, and all three questions then served their source card
first. That widening was kept. Adding "proved" as a weak anchor admitted 57 non-mathematical prompts and was
rejected.

## Files

`rows.json` holds each math item's id and its grade in each arm. `python recompute.py` derives the table and the
sign test. The questions, keys and answers are not included.
