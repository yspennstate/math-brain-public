# A research-grade fault bank, and notes from the store against no notes, 1-2 September 2026

Two tests of whether notes served from the math store help a solver find the faulty step in an argument.
Both come out null. The bank built for the second is the larger of the store's proof-audit banks.

## The powered run on the 22 August bank

A pre-registered comparison of the brain arm against no notes on the 22 August bank
(`bank10k-replication-2026-08-22`). Brain 301 of 358 right against 299 of 358 for no notes: +0.56 points,
discordant pairs 21 and 19, McNemar p 0.875. The Pocock rule stopped the run as null.

Matching all 1,200 verdicts to their served transcripts showed that the run was not sterile. 829 of the
serves had carried text from the harness's own hooks (407 in the no-notes arm, 422 in the brain arm),
because the sterile switch had been opt-in and some relaunches lacked it. Regraded by stratum, the null
holds everywhere: both arms hooked, n = 218, -1.4 points (p 0.69); both clean, n = 123, +3.3 points
(p 0.42). The runner is now sterile by default. It checks each served transcript and re-serves any that
carries an injection. The bank sits near an 84% ceiling for this solver, so the question it was built to
answer cannot be settled on it.

## The bank

6,527 items in 37 families from probability, random matrices, percolation and first-passage percolation,
concentration, spectral graph theory, learning theory and combinatorics. 5,121 items carry a fault and
1,406 are clean. Every fault ships with a certificate computed at build time (exact fractions, exhaustive
enumeration, LP feasibility, quadrature). A verifier recomputes every certificate. A candidate fault whose
certificate fails is refused. A quarantine check (400 probes over three corpora) found no item key text in
any retrieval corpus. Items in one family share an argument, so the information in the bank is smaller than
its count. Fault positions lean late in the argument, and a stratified sampler balances them when serving.
The items are not published.

The first full build had 2,788 items (2,183 faulted). Before it, the hand-written research-grade pairs
numbered about 369.

Without notes, the solver (Claude Haiku) is near its ceiling on local faults: algebra 9 of 10, constants
5 of 5, indices 4 of 4, mismatched citations 16 of 20, invalid inferences 13 of 15. It is weak on the
research-type faults: a dropped hidden hypothesis 18 of 33, a one-sided bound used as two-sided 1 of 4, an
overclaimed sharpness 5 of 8. That is where a note carrying a theorem's hypotheses could act.

## Results

240 items frozen. Full credit means the item is called flawed and the exact step is named. McNemar exact
tests on the discordant pairs; every verdict has a sterile transcript receipt.

| arm | notes | pairs | arm right | none right | diff | discordant | p |
|---|---|---|---|---|---|---|---|
| brain | token-overlap notes, 3,538-node store | 179 | 135 | 140 | -2.8 | 14 / 19 | 0.49 |
| brain_emb | embedding-ranked notes, 4,720-node store | 172 | 129 | 134 | -2.9 | 12 / 17 | 0.46 |
| B (hint framing) | as brain_emb, framed as hints | 178 | 131 | 141 | -5.6 | | 0.11 |
| C (one note) | brain_emb with k = 1 | 176 | | | +0.6 | | 1.0 |
| D (BM25) | BM25 notes, 4,732-node store | 179 | 136 | 140 | -2.2 | 13 / 17 | 0.59 |

Pre-registered primary comparisons between arms: B against brain_emb, 129 against 131 of 175, -1.1 points,
p 0.87; C against brain_emb, 140 against 134 of 176, +3.4, p 0.38; D against brain_emb, 134 against 132 of
176, +1.1, p 0.86. brain_emb against brain: 132 against 133 of 176, p 1.0. False positives on clean items
were 2 or 3 of 52 in every arm. Neither pre-registered mechanism cell moved: dropped hypotheses 30 against
28 of 42 (p 0.75); citation, scope and sharpness faults 33 against 34 of 52 (p 1.0).

How relevant the notes were matters. The token-overlap notes named the result an item needs on 111 of 188
items (59%). Embedding ranking on the grown store reached 73%, and BM25 reached 84%. Raising coverage did not
change the outcome.

What the bank can measure is the quality of the notes. Notes chosen for the item beat scrambled notes by 6.9
points (p 0.043), and the difference replicated.

Power: no notes was wrong on 38 of the 172 paired items, so the notes had 22% of the sample to act on. A true
gain of 10 points would have shown as roughly 23 discordant pairs against 6 (p about 0.003). A true gain of
5 points would sit near 19 against 10 (p about 0.14). The run rules out a large help and cannot rule out a
small one.

## The store's growth for the bank

The store grew from 3,538 to 4,720 nodes over the two days. The literature lane reached 1,474 arXiv papers:
1,053 from a first harvest over 88 queries in neuroscience, mathematics and network science, and the rest
from a later targeted harvest. Their theorem, lemma, proposition and definition blocks were turned into
attributed concept drafts, 1,129 statements from 702 papers on the first pass. Only papers whose arXiv page
carries CC-BY, CC-BY-SA or CC0 were filed into the store.
