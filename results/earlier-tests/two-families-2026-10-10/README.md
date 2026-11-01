# Two agents through the brain: one model family or two, 10 October 2026

Forty-eight proof-audit items (20 clean proofs, 20 with a local logical fault, 8 with a misused cited result), each
answered once by every arm and graded once under the pre-registered proof-audit rule. The question was whether two
agents working together through the brain do better than one agent, and what kind of second agent helps. The bank
began with 60 items; three blind readers found that 12 of the 20 cited-result items held no real fault, and those 12
were dropped before grading, as the protocol required.

## Arms

- A: one GPT agent with the brain block
- C: one GPT agent without it
- P: a pair of GPT agents (an analytic and a sceptical member solve blind and commit, then audit each other where they
  split, and a reader settles what is left)
- Q: the same pair, with the brain's crux block on a split
- P and Q, run 2: the same pairs with the second member on a different GPT model
- X: one Claude agent, blind; then Claude on the exact prompts the GPT agents saw in arms C and A

## Results

| arm | right of 48 | tokens |
|---|---|---|
| A, GPT single, brain block | 37 | 2.68M |
| C, GPT single, no brain | 35 | 1.62M |
| P, GPT pair, one model | 35 | 7.56M |
| Q, GPT pair with the crux block | 35 | 7.63M |
| P, GPT pair, two models (run 2) | 36 | 9.13M |
| Q, GPT pair, two models (run 2) | 35 | 9.53M |
| X, Claude single, blind | 42 | 0.30M |
| Claude on the C prompt | 41 | 0.35M |
| Claude on the A prompt (brain block) | 41 | 0.36M |

Two copies of one GPT model agree on almost everything: both right on 34 items, both wrong on 12, exactly one right on
2. On ten of the twelve shared misses both members gave the same wrong answer, so agreement between them cannot flag
the error, and neither the pair's audit nor the crux block recovered any of them. A second GPT model splits more often
(exactly one right on 5 items) but is the weaker model alone (32 against 35), and the pair's audit picked the right
side once.

Claude solved 8 of the 12 items both GPT members missed: 16 of 20 clean proofs, 20 of 20 local faults and 6 of 8
cited-result faults, against 15, 15 and 5 for the GPT single agent. A blind Claude reader confirmed 9 of the 11 keys a
GPT reader had doubted and all 11 control keys, so the misses were a blind spot of one family rather than bad keys.
A GPT-Claude pair could reach at most 43 (both right on 34 items, Claude alone on 8, GPT alone on 1, neither on
5), one more than Claude alone.

The brain block gained the GPT single agent two items, both local faults; for Claude it gained two and lost two.

## Cost

The GPT pairs spent four to six times the single agent's tokens and gained nothing. Each member's blind solve cost 3.1
times a single solve, because committing took two tool calls and each re-read the context. Claude ran at the command
line's default effort and GPT at its maximum, and token counts are not comparable across vendors; a Claude read cost
between $0.06 and $0.22.

## The same arrangement on open problems

The same day the design was used as a pipeline: GPT solvers on open probability problems, a sealed Claude referee on
each claimed result, and the store as the shared memory.

- Four GPT solvers answered 10 problems in about 90 minutes: 2 proofs, 1 counterexample, 6 partial answers and 1
  problem found to be already solved. The referee kept 7 and dropped 2; the 7 became 23 cards in the store.
- A GPT drafter wrote 33 cards from proofs written in September. Checked against each proof, 15 were faithful and 18
  stated more or less than the proof shows; all 33 entered the store corrected.
- One Claude read per target sorted the 1,021 claims a larger GPT wave had marked proved or checked: 723 held up as
  proved steps, 37 partial, 241 counterexamples (mostly to proposed routes) and 20 drafts, with 31 sent back for
  correction. Each read covered about 40 lemma-sized claims at once, so this is a triage by a second family, not a
  line-by-line check.

## Reading

A pair or an ensemble helps when its members fail on different items. Two members of one model family fail on the
same items, so a same-family pair or vote repeats one answer at a higher price; the 8-9 October pilots in
`../teams-and-vote-pilots-2026-10-08` show the same for teams and a three-member vote. Where one member is much
stronger than the other, pairing buys little. The arrangement that worked was a solver from one family, a referee from
another, and the store between them, so that the next solver starts from checked results.

Counts only: the items, the keys and the agents' answers are not included.
