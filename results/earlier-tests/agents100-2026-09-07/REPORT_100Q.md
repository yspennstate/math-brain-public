# 100 random bank questions, ten subagents, brain against no brain

2026-09-07. The question: *"take 100 random questions from the math test bank and test with 10 subagents on these
questions, with and without the brain to see how they do."* Design registered in `PROTOCOL_100Q.md` before any
answer was served.

## The result

Same model, same 100 items, ten shards of ten, ten subagents per arm. One difference: whether the agent could
consult the brain.

| arm | full credit on the 67 flawed items | detected at all | false positives on 33 clean |
|---|---|---|---|
| no brain | **37 / 67 (55.2%)** | 40 / 67 | 6 / 33 |
| with brain | **36 / 67 (53.7%)** | 38 / 67 | 5 / 33 |

Brain against no brain, paired by item: **-1.5 points, CI [-11.2, +8.2], exact McNemar p = 1.0.** Detection alone,
-3.0 points, CI [-12.2, +6.2], p = 0.75. The two arms returned the same outcome on 56 of the 67 flawed items; of the
11 they disagreed on, the brain won 5 and lost 6.

The treatment was delivered. The brain agents ran roughly 95 queries and marked 65 of the 100 items as
brain-informed; several recovered the exact source lemma of the paper an item came from. Having the brain, using
the brain, and answering better are three different things, and only the first two happened.

## What it is not

**Not equivalence.** n = 67 flawed pairs detects a swing of roughly fifteen points, no better. At the discordance
rate we observed, a powered test needs 129. This is a null with a ten-point interval either way, and it supports no
claim that the brain is harmless any more than that it helps.

**But it had room to fail.** The no-brain arm sat at 55.2%, well below the 85% ceiling rule, so 30 of the 67 flawed
items were there for the brain arm to win and it won none of them net — 44.8 points of headroom, unused. A null
from a test whose treatment arm is already near-perfect says nothing; this one is not that. It is underpowered, not
unfalsifiable.

**Not leakage.** The store keeps 53,355 arXiv statements, including the papers these items were cut from, so a brain
agent reading its own item's unaltered proof step would have made any gain fake. Checked over all 67 flawed items:
zero carry the clean step text. The detector fires on 23 of the 100 items' claim statements — the statement-level
text the builder deliberately retains, which is answer-free — and on 0 of 40 shuffled controls, so the zero is a
real negative and not a broken check.

## What the arms were blind to, together

| operator | no brain | with brain |
|---|---|---|
| flipped inequality | 14/17 | 12/17 |
| swapped hypothesis | 0/7 | 1/7 |
| dropped hypothesis | 0/2 | 0/2 |
| inequality to equality | 1/6 | 1/6 |
| swapped cited theorem | 2/2 | 1/2 |

The failure in both arms is under-calling: 67 of the items are flawed and the no-brain arm flagged 46, so 27 real
faults read as valid proofs. When it did call a fault it usually named the right step (40 detected, 37 exact). The
blind spots are the hypothesis families — precisely what a store of named results and their hypotheses was built to
fix — and the brain arm moved one item of nine there. It also lost the one item where the fault was a swapped
citation, the case the store should own outright: a retrieved note about a result is not a check that the step uses
that result correctly, and here it read as reassurance.

## Where this sits

Third independent read of the same question, and they agree. The B12 bank found served notes helping only on
dropped-hypothesis faults; plit stage 1 this morning found -2.4 points for Haiku on tier A and -1.6 for Opus on
tier B with notes served into the prompt; this run replaces served notes with an agent that queries the store
itself, on a different model, and lands in the same place. Stage 1's own verdict named "a solver with tools" as the
open question. Tools were not the missing piece.

What has NOT been tested and would move this: notes filtered for whether they apply to the item in front of the
solver; a solver that is made to look at each step rather than handed material about the argument; and the
per-step token inventory the proof-audit layer reports as its actual mechanism, which is a different intervention
from retrieval and was not what this run varied.

Everything above is measured by `grade_plit.py` unchanged, over `run_agents100_0907/verdicts`, against the
quarantined keys. One repair is logged: an agent mistyped an item id by dropping two characters; the malformed id
was a subsequence of exactly one unanswered item in that shard, so the mapping was forced
(`CONTROLS_AND_REPAIR.json`).
