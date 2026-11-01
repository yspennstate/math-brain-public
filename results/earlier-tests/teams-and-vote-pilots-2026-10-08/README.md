# Teams, single agents and a three-member vote: two small pilots, 8 and 9 October 2026

Twenty items (seven open questions and thirteen proof audits), each answered once by every arm. The question was
whether a team of agents, or the brain, adds anything a single agent does not already get on items of this size.

## Arms

| day | arm | what it is |
|---|---|---|
| 8 Oct | A | one Codex agent with the brain |
| 8 Oct | B | a Codex team with the brain |
| 8 Oct | C | one Codex agent, no brain |
| 8 Oct | D | a Codex team, no brain |
| 9 Oct | A | arm A again |
| 9 Oct | E | arm A with the hook layer delivered on every prompt |
| 9 Oct | F | team version 2: the checker verifies before the solver commits |

## Results (graded with grade.py v1.19)

| day | arm | right of 20 |
|---|---|---|
| 8 Oct | A brain, single | 19 |
| 8 Oct | B brain, team | 20 |
| 8 Oct | C no brain, single | 18 |
| 8 Oct | D no brain, team | 17 |
| 9 Oct | A brain, single | 20 |
| 9 Oct | E brain plus hook layer | 19 |
| 9 Oct | F team version 2 | 17 |

Paired on the same items (right only in the first arm, right only in the second):

| contrast | first only | second only | both | neither |
|---|---|---|---|---|
| A against C (brain, single) | 2 | 1 | 17 | 0 |
| B against D (brain, team) | 3 | 0 | 17 | 0 |
| B against A (team against single, brain) | 1 | 0 | 19 | 0 |
| D against C (team against single, no brain) | 1 | 2 | 16 | 1 |
| E against A (hook layer) | 0 | 1 | 19 | 0 |
| F against A (team version 2) | 0 | 3 | 17 | 0 |

Every contrast is a difference of one to three items on twenty. A team cost about three times the tokens of a single
agent (median 56,000 to 68,000 against 17,000 to 18,000 a run) and bought nothing measurable. The hook layer showed a
note on 17 of its 20 runs and added 64 seconds of wall time in all.

## A three-member Claude vote on the same items

Three Claude agents solved the twenty items blind and then audited their own answers. Members scored 18 of 19, 17 of
18 and 18 of 20 on the items each graded; after the audit 18, 19 and 19. The majority vote of the answer cores was 19
of 20 both before and after the audit, with no three-way split. A vote of three members from one model family was no
better than its best member, and Codex single agents score 18 to 20 on the same items.

## The grader

The first reading of these runs used grade.py v1.3, which scored every arm several items lower and left six
items that no run ever got. Those six were grading defects (equivalent expressions written differently, a one-field
JSON answer, a final period), not reasoning failures; under v1.19 every item is solved by at least one run, and two
numerical items whose 18 and 19 runs all gave the same answer form are right on every run. Two controls show the new
counts are not leniency: each of the 20 answer keys grades itself right, and none of 41 corrupted keys (a wrong line, a
swapped VALID, a wrong number, a wrong name) grades right.

| item type | items | runs per item | corrupted keys per item |
|---|---|---|---|
| proof audit | 13 | 8 to 19 | 1 or 2 |
| numerical | 6 | 9 to 19 | 3 |
| name | 1 | 11 | 2 |

`RESULTS.json` holds the per-arm counts, the paired tables and the control totals. The items, the keys and the
answers are not included.
