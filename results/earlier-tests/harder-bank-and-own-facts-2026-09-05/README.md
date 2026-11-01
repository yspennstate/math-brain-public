# A harder fault bank, and questions only the store can answer, 5-6 September 2026

Two tests run on the same evening, each under a protocol sealed before serving. One was a null at the
ceiling. The other gave the first controlled positive for the math hook.

## B13-hard: the fault bank at the ceiling

The nine families of the research-grade bank (`research-bank-b12-2026-09-01`) on which the smaller solver
had failed most, with items never served before, were given to a stronger solver (Claude Opus 5). There were
60 items per arm: 45 flawed and 15 clean.

| arm | flawed items right | clean items flagged |
|---|---|---|
| none | 44 / 45 (97.8%) | 1 / 15 |
| brain | 45 / 45 | 1 / 15 |
| placebo (notes served for a different item) | 45 / 45 | 1 / 15 |

Brain against none: +2.2 points on one discordant item, p 1.0. The pre-registered ceiling rule (no powered
stage when the none arm is above 85%) fired on the none arm alone. An independent re-derivation agreed on
every row, and every accepted verdict's transcript names the intended model.

The three fault-detection banks run so far read at or near the ceiling for their solvers: 84% for the 22
August bank and 78% for the research-grade bank with Claude Haiku 4.5, and 97.8% here. A note about
mathematics the solver already knows cannot help it, so these nulls say nothing about the store either way.
Before sizing a brain-against-control test, serve the none arm on the intended solver first. If it reads
above 85%, redesign.

## H1: sixty questions answered only by the store

Sixty questions ask for exact counts of constrained self-avoiding walks that the store's own enumerator
computed in August. No published table carries them, and the answer keys were sealed outside the store. The
solver was Claude Opus 5 with every tool denied, graded on the exact integer. Four arms ran through one
sterile runner: none (the question alone); brain (the question plus the block the production retrieval
served); placebo (a block served for a different question); and brain_v2 (the block after the fix described
below).

| arm | correct | answered unknown | wrong numbers |
|---|---|---|---|
| none | 0 / 60 | 60 | 0 |
| brain | 20 / 60 | 37 (3 timeouts) | 0 |
| placebo | 0 / 60 | 54 (6 timeouts) | 0 |
| brain_v2 | 48 / 60 (80%) | 12 | 0 |

Against none, brain_v2 scored +80.0 points (95% interval 69.9 to 90.1, discordant pairs 48 and 0, McNemar
p < 0.0001). Brain scored +33.3 points (21.4 to 45.3, 20 and 0). brain_v2 against brain is +46.7 points
(28 and 0). In both brain arms the number of correct answers equals the number of blocks that held the right number.
No arm produced a wrong number: an irrelevant block was not copied.

Two retrieval facts came out of building the test. First, the bank runner's own note builder kept only
word tokens. It dropped every digit and coordinate, and it returned the same three generic nodes for all 60
questions. A brain arm built on it measures that scorer, not the store, so every arm here used the
production path. Second, the production path saw the digits, but its clear-winner margin test stayed silent
on 34 of the 60. In an enumerated family the runner-up is the same sentence with other digits, scored a
hair apart. The fix is that a rival must differ from the leader in words, not only in digits: titles that
agree once every digit run is masked form one family. With the fix, blocks served went from 26 to 60, and
blocks holding the right number from 20 to 48. The 26 blocks served before were byte-identical, because the
rule changes abstention only. That is the brain_v2 arm.

The placebo arm ran across an API outage. Timeouts that never reached the model were set aside, and the arm
was re-served under an amendment written before the re-serve. A second script with its own data path
re-derived every number, with no disagreements.

The plain question form ("how many self-avoiding walks of length n in a strip of width w avoid a given
site") is refused by the hook's two-anchor prompt gate before retrieval runs. The test called the retrieval
directly, and an agent typing that form through the hook gets silence from the gate.
