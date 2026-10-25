# The proof-sense posture, reworded and remeasured, 12 September 2026

When an agent audits a proof, the math hook serves the notes that bear on the cited results and, on most proof
items, a short posture: a paragraph telling the auditor how to read a step. The earlier reruns had left six flawed
items that the auditor still passed with the notes in hand. Five of the six were one fault. A step names a general
principle as its licence, the principle is false as written, the step itself is true under the claim's real
hypotheses, and the auditor quietly supplies the correct reason and calls the argument clean. This test asked
whether rewording the posture to name that shape would catch them.

## Design

103 items: all 48 flawed items of the 100-item proof-audit bank, 20 of its 52 clean items drawn with a fixed seed,
and all 35 items of the harder bank, 67 flawed and 36 clean in all. The posture is served on 91 of them. The arms
differ only in the posture string inside the served material; the notes, the class checks, the item text, the
instructions, the batch size (15 items per solver) and the item order are identical. Sonnet solvers, graded against
the frozen keys.

| arm | posture | correct of 103 | flawed caught of 67 | clean passed of 36 | paired against control |
|---|---|---|---|---|---|
| control | the live wording | 94 | 58 | 36 | |
| v1 | re-derive the reason the step gives, not a better one you could supply | 94 | 59 | 35 | 2 helped, 2 harmed, p = 1.0 |
| v3 | v1, plus a rule for sentences that only restate what was proved | 94 | 61 | 33 | 5 helped, 5 harmed, p = 1.0 |

Neither wording passed the landing gate (helped at least harmed + 2 against the control, and no new false positive
on a clean item), so the live posture was not changed. The control missed 9 flawed items, so a better wording had
room to gain up to 9; the rewordings found 1 and 3 of them and lost as many elsewhere. The stronger wording caught three more flaws and cost three
clean items: the same rule, applied to a closing sentence that only summarises earlier steps, reads as an
unlicensed claim.

## Batch size

The control was run a second time with 5 items per solver instead of 15:

| batch | correct of 103 | flawed caught | clean passed |
|---|---|---|---|
| 15 items | 94 | 58 | 36 |
| 5 items | 97 | 61 | 36 |

3 helped, 0 harmed (p = 0.25). One 15-item batch had also come back with 10 answers, the same delivery failure the
earlier reruns met at 20 items a batch; the solver instruction now states the item count and asks the solver to count
its answers before it finishes.

## The gate

The posture is withheld on 13 of the 103 items. Both arms already answered 12 of those correctly, and the thirteenth
was harmed by the notes, not by the missing posture, so widening the gate could gain at most one item. It was left
as it is.

Counts only: the items, keys, served blocks and answers are not included. `proof_sense.py` in `framework/dreaming`
holds the posture that stayed live.
