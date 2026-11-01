# Trap bank, four arms (25-26 September 2026)

The other banks of September ask for facts that exist once and stay put. This one asks three harder things of an agent
working from a record that changes over time:

- **Superseded (12 items).** The record holds an older answer that a later entry replaced. Correct is the current
  answer; the older one is the trap. In one item the agent's own standing instructions still carried the stale value.
- **Unanswerable (10 items).** The question asks for something the record does not hold, or rests on a false premise.
  Correct is to abstain or reject the premise; any asserted value is wrong. Several items have a near miss in the
  record that a careless agent could copy.
- **Join (12 items).** The answer needs two facts kept in different places.

The items are questions about the agents' own working records, not about mathematics, and are not published. Each key
names its correct, partial and wrong criteria and, for a superseded item, the stale answer.

## Arms

The arms and settings are those of the recall four-arm test of the same days (see `docs/cost.md`):

- **conn**: an ordinary session with the brain connected (instructions, wake step, hooks, the recall tool);
- **filesrec**: no connection, the records on disk, the recall tool run by hand;
- **files**: no connection, the records on disk, no recall tool;
- **sterile**: no tools and no records.

Opus 5.5 at high effort, a cap of 8 dollars a run, 60 minutes a run. Answers were shuffled with masked ids and graded
blind by two Opus 5.5 graders against the keys, with a third on disagreement. The graders agreed on all 129 graded rows.

## Results

Correct of n, with 95 percent Wilson intervals.

| arm | superseded | unanswerable | join | all |
|---|---|---|---|---|
| conn | 11/12 [0.65-0.99] | 8/10 [0.49-0.94] | 12/12 [0.76-1.00] | 31/34 [0.77-0.97] |
| filesrec | 11/12 [0.65-0.99] | 8/10 [0.49-0.94] | 12/12 [0.76-1.00] | 31/34 [0.77-0.97] |
| files | 11/12 [0.65-0.99] | 7/10 [0.40-0.89] | 12/12 [0.76-1.00] | 30/34 [0.73-0.95] |
| sterile | 0/12 [0.00-0.24] | 10/10 [0.72-1.00] | 0/12 [0.00-0.24] | 10/34 [0.17-0.46] |

The one item the three arms with records missed on the superseded family was graded partial in all three. The
unanswerable cells below ten are runs that produced no answer (two, two and three), not fabrications: no arm asserted a
value on an unanswerable item.

Paired exact McNemar tests: conn against files 2 to 1 (p = 1), conn against filesrec 1 to 1 (p = 1), files against
sterile 23 to 3 (p = 8.8e-5).

| arm | runs | median cost (dollars) | total cost | median wall time (s) |
|---|---|---|---|---|
| conn | 34 | 1.42 | 54.4 | 636 |
| filesrec | 34 | 0.81 | 30.4 | 726 |
| files | 34 | 0.76 | 27.6 | 818 |
| sterile | 34 | 0.03 | 1.0 | 25 |

## Reading

On this bank the records decide the score and the connection adds nothing measurable: every arm that could read them
gave the current answer on 11 of 12 superseded items, joined all 12 pairs, and invented nothing. The registered
falsifier (files within 5 points of conn on the superseded family) held, so the test does not support a claim that the
connection helps an agent prefer the current answer. Where the connection does differ is cost: about 1.9 times the
median run of the files arm (1.42 against 0.76 dollars).

The item whose stale value sat in the connected agent's own instructions was predicted to fail in that arm. It did
not: all three arms with records gave the current answer.

Two limits. Thirty-four items give wide intervals, so a difference of a few items is invisible. And in ten of the 34
runs of each arm with records the agent read a note that described this bank; those runs are scored with the rest. The
sterile arm read nothing and is clean.
