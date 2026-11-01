# The thousand open problems in probability: a campaign report

12 September 2026

Six ledgers, 1,025 problem records, 908 admitted as genuine sourced open problems, 917 with a
recorded attempt, and a small number of results that the record itself is careful not to call
certified. This report says what was gathered, what was solved and by what argument, what stands one
named step away from a result, and what is left.

### What the campaign is

Between 6 and 10 September 2026 six separate intake efforts read the open-problem literature of
probability and recorded what they found in append-only ledgers: a Codex campaign run against a
twenty-hour clock on 6 and 7 September, and five Claude intakes labelled C, D, E, F and G. Each
ledger records a problem's source and locator, the statement, whether the source itself calls the
question open, what a literature search found later, and then every attempt made on it, including
the attempts that failed and the exact obligation each one stopped at.

The counts below are recomputed for this report from the six `problems.jsonl` files, taking the last
record for each problem identifier because those files are appended to when a status is revised.

| ledger | records | distinct ids | admitted | dedup keys | with an attempt |
| --- | --- | --- | --- | --- | --- |
| Codex campaign, 6-7 Sep | 590 | 495 | 451 | 468 | 455 |
| Claude intake C, 7 Sep | 160 | 160 | 129 | 159 | 131 |
| Claude intake D, 8 Sep | 102 | 102 | 94 | 100 | 94 |
| Claude intake E, 8 Sep | 115 | 113 | 109 | 113 | 110 |
| Claude intake F, 8 Sep | 140 | 140 | 111 | 138 | 113 |
| Claude intake G, 10 Sep | 15 | 15 | 14 | 15 | 14 |
| total | 1,122 | 1,025 | 908 | 993 | 917 |

There are 964 attempt records behind those 917 problems. Five dedup keys appear on more than one row
across the six ledgers, so the cross-ledger overlap is small but not zero.

This agrees with the snapshot taken on 9 September, which counted 894 admitted records across the
five ledgers that existed then; intake G added 14 admitted problems on 10 September, and 894 plus 14
is the 908 above. That snapshot also reported 870 components after merging rows by exact key and
provenance, a stricter merge than the ledgers' own dedup key, so 870 and 993 are two different
questions about the same corpus rather than a disagreement. Nobody should quote a single number as
"the campaign total" without saying which of the three it is.

### Status update, 13 September 2026

The counts and the tables in this report are the 12 September state and are left as they stand. One
thing has changed since. F0090, the entropy-influence question for the planar percolation crossing,
is closed: the author posted the write-up as a public preprint, *Entropy and singularity of spectral
and pivotal sets in planar percolation*, on ResearchGate on 13 September 2026, publication 414266816.
The ledger row carries a new appended record with `current_status: closed_published_by_author`. What
closes it is the author's decision to publish; the argument is still author-checked with one
independent agent read and no referee report, and its novelty is still uncertified. The posted paper
also answers a question that has no row in any of the six ledgers: the discrete triangular-site case
of the singularity question, open problem 5 of the same section of Garban, Pete and Schramm. That
question is recorded, not opened or closed, and is for the author to place.

Overnight on 13 to 14 September nine of Janson's problems were settled (Problem 18.9 answered in full,
Problems 18.41 and 18.42 answered in the negative, Problem 18.30 answered in the negative for both of its
parts, Problem 20.2 on the asymptotic normality of outdegree counts answered: yes in the finite-variance
critical case by the literature, no in general beyond it, against a published conjecture, Conjecture 20.1
on the moments of the level widths proved for every real exponent at least one, Problem 18.40 on the
largest box answered in the negative, and Problems 20.3 and 20.4 on the box and fringe-subtree counts, which
no ledger had ever recorded, answered as well), Aldous and Fill's
Open Problem 4.48 was settled (its part (a), whether the variation
threshold is at most Kemeny's constant, fails on a three-state birth-and-death chain; its part (b), whether
the relaxation time is at most the stopping-rule mixing time, holds with a short proof), and the results of
the ten-lane campaign of 13 September were gathered; both are in the
chapter on the results of 13 and 14 September. That chapter also settles Hasebe and Ueda's Problem 3.3 on
the unimodality of free Brownian motion, where the optimal constant turns out to be one rather than the
four their theorem gives, with the symmetric Bernoulli law the unique extremal measure. It also answers
Conjecture 13 of the Randomstrasse 2024 list, on the discrepancy of the Sylvester Hadamard matrices, which
turns out to be a question about the covering radius of the first-order Reed-Muller code and to have been
settled against the conjecture as long ago as 1983. It settles the sharp constant for the classical
companion, unimodality of ordinary Brownian motion started from a compactly supported law, which is a
quarter of the squared diameter against the thirty-six times larger bound the same paper proves; it
computes the largest discrepancy of a sign matrix exactly for every size to eleven by reading it as a
covering-code question; it reduces Aldous and Fill's Open Problem 7.31 on distance-regular graphs to an
identity in the intersection array and confirms Biggs's value as the maximum over all cubic such graphs;
and it removes the Cauchy laws, and the free stable laws of index down to about 0.7, from the candidates
for Hasebe and Ueda's Problem 3.11. It carries
corrections to the record, fifty-five new
open problems, and a seventh ledger of 118 records from thirty-four sources, 95 of them still open
problems after a literature sweep of every row whose source predates 2025, forty-four of them, found
fourteen no longer open, nine resolved outright and five in part: nineteen read out of September 2026 arXiv papers, and the rest found by sweeping the campaign's
own sources for numbered problems no ledger had ever recorded. Twenty-nine of the 191 sources with local
text had such gaps, 122 labels in all, among them thirteen from Aldous and Fill and nine from Schramm's
problem collection. The counts and tables above are still the 12 September state.

A derived registry that takes the last row of every ledger, carries the dedup key, status, result
label, stopping point and memo pointer for each of the 1,025 ids, and records the five cross-ledger
duplicates rather than merging them, is generated by `build_registry.py` in
`12_cognitive_architecture/brain_improvement/campaign_2026-09-13_10h_10sub/lanes/B2_registry/`. Its
counts reproduce every figure in the table above.

### What was solved

The ledgers carry 24 rows with a result label. Thirteen are labelled a candidate full solution:
P0032, P0033, P0174, P0189, P0193, P0208, P0209, P0266, P0267, P0276, P0288 and P0340 from the Codex
campaign, and F0090 from intake F. Four are labelled proved: E0061 and E0063 in the quadratic
stochastic operator family, F0055 and F0057 on Janson's simply generated trees. One is refuted,
E0078, by an exact rational counterexample. Two are settled in a restricted case, E0104 and E0105 in
the mobile Boolean model. One, E0060, is answered by a known example. Two, P0096 and P0140, are
rederivations of results already in the literature, one of them with a scope correction. One, P0205,
is an author-checked partial counterexample.

Separately from the labels, a session on 8 September wrote up thirteen problems in full, with the
mathematics on the page and, where the content is finite arithmetic, a machine-checked core in Lean 4
against Mathlib. Those write-ups overlap the labelled rows in part and extend them in part: a
handful of results have a written memo whose ledger row was never relabelled, and for those the memo
is the later record. Chapters 3 and 4 give every one of these results with its argument.

Two further results arrived after the intake window: the Kalai entropy-influence question for planar
percolation crossings (F0090, an author-checked argument with a first independent read) and Leskela's
problem 3 on nonmonotone chains with a supermodular time ordering (P0291). Both are in chapter 4.

**Nothing here is independently certified.** That is the record's own word. The 9 September audit put
it plainly: zero newly certified full solutions, where certification means full source correctness,
independent verification, and a verified check that the problem was still open. Seventeen rows carry
a full-answer claim; a claim is not a certificate. The Lean inventory is 22 files and 80 declarations
that the kernel accepts, with no complete verified correspondence between any Lean statement and a
source theorem. And for every result in this report the prior art is the weak link: a handful of
searches found nothing, which is a bounded search and not a clearance.

### What is close

Forty-two rows across the six ledgers carry a partial label: 29 partial results, 12 candidate partial
counterexamples, and one author-checked partial counterexample. The 9 September snapshot counted 38
of these across five ledgers. Chapter 5 takes them in order of how close they are, from the ones
where a single finite or computational obligation remains through to the ones where a special case is
proved and the general case is untouched. The clearest examples: Ross's second conjecture, where the
mechanism is verified and the quantitative half is not; the sparse parity counterexample, which needs
an exact tilt at a stated mean before the limit can be assembled; and the Catalano and Lavenant
conjecture, where an exhaustive search settles every case up to seven atoms and the general argument
is missing.

### How to read this report

Chapter 1 is the campaign's history and method, the status axes the ledgers use, and what each
verification word means. Chapter 2 is a synthesis by area of what was solved and by what kind of
argument, together with what the audits found about how the work goes wrong. Chapters 3 and 4 carry
the mathematics of the results. Chapter 5 carries the ones close to a result and the exact obligation
each is waiting on. Chapters 6 to 14 are the catalogue: all 1,025 problem records, one
per problem, in ledger order, with its source, its statement, its literature status, and what our
attempt found. Chapter 14 is what remains, in priority order. The appendix lists every source file
this report was built from.

A reader who wants only the mathematics should read chapters 3, 4 and 5. A reader who wants to
continue the campaign should read chapter 14 first and then the catalogue for the area they intend to
work in.
