# A fresh bank of plain questions, and the older audit-brief bank, 3 September 2026

Measurements of the math hook on two banks, taken on a store that grew from 4,732 to 4,895 nodes over the
evening. The later reruns in `locate-and-proof-banks-2026-09-11` compare against these numbers.

## The banks

The older bank (built 22 August) has 1,051 probes written as audit briefs: a numbered argument in which one
step uses a named theorem without naming it. Tier 1 (470 probes) was used for tuning, tier 2 (263) was held
out, and 318 probes ask about results the store does not hold.

The fresh bank was built on 3 September. It covers 89 theorem families the store holds, none of them among the
older bank's 21. Each is asked twice, once as a working mathematician would ask in the middle of a proof
without naming the result, and once with the name. Forty more questions ask about results the store lacks.
Presence and absence were both checked by title stem at run time. A question counts as served when a title in
the served block carries the target's stem. The questions and their targets are not published.

## Results

Fresh bank, live hook, 4,862-node store:

| phrasing | theorem served | rank 1 | silent |
|---|---|---|---|
| without the name | 84.3% | 74.2% | 6.7% |
| with the name | 96.6% | 92.1% | 2.2% |

Of the 89 families, 73 were served under both phrasings and 88 under at least one. On the 40 absent results a
block was served 36 times. The abstention gates do not gate.

By area, without the name and with it: analysis 100/100 (14 families), topology and geometry 100/100 (9),
algebra 92/100 (13), random matrices 86/86 (7), probability 79/100 (19), combinatorics 75/100 (12),
statistical mechanics and learning theory 67/87 (15).

Six of the fourteen unnamed misses were silences, four of them with the right theorem ranked first or
second. The margin gate (MIN_MARGIN 0.1) refused to speak because a different, related result scored within
0.001 to 0.09 of the leader, on scores that run from 5 to 180. Six were ranking misses in which a neighbouring
result took the block, with the target ranked between 7 and 161. One served a sibling result, and one went to
a neighbouring theorem at rank 9. A hand reading of 20 random
unnamed blocks found the theorem's statement in 18. About half of those 18 spent one or two slots on noise,
and two spent all three slots on copies of one theorem.

Turning the margin test off, on the same retrieval hits over 1,180 items, raised the unnamed fresh score from
84.3% to 88.8% and tier 1 of the older bank from 61.9% to 64.3%. It also raised false fires on absent results
from 90.0% to 100.0%. The margin test buys 5 silences in 358 absence questions and costs 16 correct blocks in
822 presence questions, both by near-tie chance. It was left in place. No single score threshold separates
the two populations: the top score has a median of 163 when the answer ranks first and 142 on an
unanswerable probe.

After 35 new statements were written for results the store held only as harvested leads, the fresh bank on
the 4,895-node store read 87.6% unnamed (rank 1 75.3%, silent 5.6%) and 97.8% named. All 89 families were
served under at least one phrasing. False fires stayed at 90%. Learning theory and statistical mechanics rose
from 67% to 80%, and combinatorics from 75% to 83%.

Older bank, through the same hook path (0.875 s median a probe):

| run | tier 1 by id / theorem | tier 2 by id / theorem | fires on absent results |
|---|---|---|---|
| 15:52, 4,732 nodes | 54.9% / - | 29.3% / - | 98.4% |
| 17:41, 4,856 nodes | 50.6% / 62.1% | 28.5% / 39.9% | 99.7% |
| 20:5x, 4,891 nodes | 51.7% / 63.6% | 28.1% / 39.2% | 98.7% |

The bank labels one node per theorem. The store holds several copies of most theorems: a lede, a statement and
a sibling result. Counting any served title that carries the theorem's stem therefore raises the held-out
number from 29% to 40%. The evaluator reports both.

Self-retrieval, with every claim queried by its own text: hit@1 93.7% (98.1% counting duplicate copies),
hit@6 96.6%, MRR 0.951. Queried by title alone: 89.3%. On 22 August, at 1,130 claims, the same harness read
58.6%.

Two selector changes were measured and not landed. The first treats copies of one theorem as a single
candidate. It gained 10 and lost 0 on tier 1 and moved nothing on tier 2, with a few false merges. It did
show the size of the copy problem: 66 of 470 tier-1 blocks and 35 of 263 tier-2 blocks spent a slot on a
second copy of a theorem already in the block. The second is a family-aware margin rival. It cured none of
the six silences.

The two banks measure different tasks. Plain one-sentence questions name their objects. Audit briefs bury the
theorem in an argument. Neither number replaces the other.
