# Two agents through the brain: a solver and a referee from another family (10 Oct 2026)

The question was how two agents working through the brain can do better than one agent alone, or than a group of
agents with no brain. On this test the answer was the second agent's model family, not the pairing itself. Two copies
of one model fail on the same items, so a pair of them, a crux exchange or a vote adds nothing. A solver from a
different family does not share those blind spots. The arrangement that worked was one family solving, the other
refereeing, and the brain holding what both had checked.

## The test: 48 proof audits

Each item is a proof from the literature, either clean or with one planted fault: a local-logic fault, or a misuse of a
cited result. The solver says CLEAN, or names the faulty step. Every arm got the same 48 items, blind, one sealed call
per item, and the same grader scored them all.

| arm | right of 48 | tokens |
|---|---|---|
| GPT single, with the brain block (A) | 37 | 2.68M |
| GPT single, no brain (C) | 35 | 1.62M |
| GPT pair, same model (P) | 35 | 7.56M |
| GPT pair with the crux exchange (Q) | 35 | 7.63M |
| GPT pair, two GPT models (P, run 2) | 36 | 9.13M |
| Claude single, blind (X) | 42 | 0.30M |
| Claude on the GPT C prompt | 41 | 0.35M |
| Claude on the GPT A prompt (brain block) | 41 | 0.36M |

GPT is gpt-6.1-sol at max effort. Claude is Opus 5.5 at the CLI's default effort.

- Two copies of one GPT model: both right 34, both wrong 12, one right 2. On ten of the twelve shared misses both gave
  the same wrong answer, so agreement between them cannot flag those items.
- Claude solved 8 of the 12 items both GPT members missed. By kind: clean proofs 16 of 20, local-logic faults 20 of 20,
  cited-result faults 6 of 8. The single GPT agent got 15, 15 and 5.
- The GPT reader had doubted 11 answer keys. A blind Claude reader confirmed 9 of them and all 11 controls, so most of
  those misses were a GPT blind spot, not bad keys.
- A GPT-Claude pair could reach at most 43, one more than Claude alone. Where one member is much stronger, pairing buys
  little. A pair earns its cost when the two members are close in strength and wrong on different items.
- The brain block moved a single GPT agent by two items and left Claude where it was (41 with and without it, two
  items gained and two lost) at 16 percent more tokens.
- Cost: the GPT pairs spent four to six times the single agent's tokens for no gain. Each pair member's blind solve cost
  3.1 times a single solve, because committing took two tool calls and each one re-read the context. A Claude read cost
  USD 0.06 to 0.22. Token counts are not comparable between vendors.

Caveats: one run of 48 items, graded once on 10 Oct and not regraded since. The two families ran at different effort
settings, and both have read arXiv, where the proofs come from. The first grading of the Claude arm read 0 of 48,
because Claude answered in the item's own words rather than the harness's FLAWED/CLEAN form. The answers were mapped to
that form and graded by the same grader as the GPT arms.

## The 8-9 Oct pilots, regraded

The smaller pilots of 8-9 Oct (teams against single agents, brain against none, 20 items) were first graded by an early
grader, grade.py v1.3. On 25 Oct they were regraded with v1.19, using the same runs:

- 8 Oct: brain single 19, brain team 20, plain single 18, plain team 17 of 20 (v1.3 had read 14, 14, 13, 11).
- 9 Oct: brain single 20, brain with its prompt hooks 19, a team whose checker verifies 17.
- The "six truly hard items" that no Codex run had solved were grading defects (expression equivalence, a one-field
  JSON answer, a final period). Every one of them is solved by some or all runs under the current grader.
- Controls: each of the 20 keys grades itself right, and none of 41 corrupted keys does.

What still stands: teams bought nothing over a single agent at about three times the tokens (56-68k median against
17-18k), and a vote of three members from one family was no better than its best member.

## The same design on open problems

On 10 Oct the campaign ledgers held 673 distinct probability problems: 546 open, 105 solved in the literature, and 22
answered in September.

- Four GPT solvers answered 10 open problems in about 90 minutes: 2 proofs, 1 counterexample, 6 partial answers, and 1
  found to be solved already in the literature. A sealed Claude referee read each claim, kept 7 and dropped 2. The 7
  became 23 nodes in the math brain.
- September's results: a GPT drafter wrote 33 nodes from the written proofs. A Claude check of each node against its
  proof found 15 faithful and 18 that stated more or less than the proof shows. All 33 entered the brain corrected.
  Without the second family, more than half of those nodes would have entered wrong.
- One Claude read per target sorted the 1,021 claims that groups of three GPT agents in a 300-agent campaign had called proved or checked.
  723 held up as proved steps, 37 were partial, 241 were counterexamples (mostly to proposed routes) and 20 were drafts.
  31 went back for correction. Each read covered about 40 lemma-sized claims at once, so this was a triage by a second
  family, not a line-by-line check. None of it claims a large problem solved.

## What it means for ensembles

An ensemble works when its members fail differently. Within one family they mostly do not, so a same-family ensemble
repeats one answer at a higher price. The ensemble that worked here had three parts: a solver, a referee from another
family, and the brain as shared memory between them, so the next solver starts from checked results rather than drafts.
The referee's verdicts cost a few cents each, and they are where the errors were caught, on the test and on the open
problems alike.

Item texts and answer keys are not published here, so they stay unseen by future test takers.
