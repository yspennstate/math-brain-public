# The 1,000-item bank again, Codex agents with and without the brain, 28 October 2026

The bank of the 12-13 September test (`../hard1k-ab-2026-09-12`) was answered a second time by Codex agents
(gpt-6.1-sol at medium effort), once with no access to the store (brain off) and once with the store's recall tool
(brain on), here as an in-memory recall server answering a lookup in about 0.7 s. In the September test the brain arm
answered from the served note block alone; in this one the agent could query the store itself. The answers were
graded with the bank's own grader, whose scoring functions were run unchanged.

The first cycle of the run is not reported: the recall tool was broken in it, and its brain-on arm is invalid. The
cycle graded here is the second.

## Rows

2,030 answer rows: 1,000 with the brain off, 1,000 with it on, and 30 open-problem rows from the brain-on lane that are
not bank items and are not graded here. No item appears twice in one arm, and every bank item is present in both arms,
so there are 1,000 matched pairs: 923 lookups in the store and 77 proof audits.

## Result

| family | n | brain off | brain on | helped | harmed |
|---|---|---|---|---|---|
| op_pagesum | 260 | 0 | 260 | 260 | 0 |
| op_pagediff | 150 | 0 | 150 | 150 | 0 |
| op_oddsource | 140 | 0 | 140 | 140 | 0 |
| op_pagemax | 73 | 0 | 73 | 73 | 0 |
| self-avoiding walks (three families) | 300 | 300 | 300 | 0 | 0 |
| proof audits | 77 | 74 | 75 | 1 | 0 |
| all | 1,000 | 374 | 998 | 624 | 0 |

All 624 discordant pairs favour the brain (exact McNemar, two-sided, p = 2.9e-188).

Every one of the 623 store lookups the brain-off arm missed was answered UNKNOWN; it answered 377 items and got 374 of
them right. On the walk counts, which an agent can compute, both arms are perfect. Of the proof audits, the analysis
and functional analysis items were right in both arms (22 and 11), the dynamics items 21 of 22 in both, and the PDE
items 20 of 22 without the brain and 21 with it.

A plain exact string match on the same rows, leaving out the flawed proofs because their grade needs the faulty step
as well, gives 335 without the brain and 958 with it, which is the store and clean-proof counts above (300 + 35 and
923 + 35).

## What the number measures

The whole gap is the store lookups. Those items ask for values held only in store cards, so without the brain there is
no route to them, and the brain-on answers cite the cards they read. The 37.4 to 99.8 percent therefore measures
whether recall reaches the right card, not reasoning gained. On the items both arms can work out, the brain added one
proof audit and lost nothing.

The September arm A guessed the four-way page questions to chance (21 of 73) and read the odd-source answers off the
wording of the prompt (140 of 140). These agents did neither: they answered UNKNOWN to every store item they could
not look up, so the brain-off count here is lower than in September on the same items.

The answer keys were kept outside the trees the agents could read, and the brain-on evidence is card ids, but this
grade does not by itself prove that the agents' host could not reach the keys. The answers file has no cycle field,
so the first-cycle exclusion rests on the file chosen, which is the second cycle's.

## Files

Counts only. The items, the keys and the per-item rows stay private with the bank.
