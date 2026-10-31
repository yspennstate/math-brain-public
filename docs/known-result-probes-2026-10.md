# Probing the store with known results (27-29 October 2026)

A recall test built from the store's own cards can only find ranking faults: every question has an answer card by
construction. It cannot find a theorem the store never held. For that, an agent asked recall about well-known results
in the areas the store covers, read what came back, and when nothing answered, checked the store directly before
blaming the ranking. Each round fixed one miss and measured the same searches before and after. All searches used the
math recall tool with two or three wordings in one call, top eight cards printed.

## The rounds

| question | before | what was missing | added | after |
|---|---|---|---|---|
| Kahn-Kalai conjecture, expectation threshold | 0 of 3 target cards in either top 8; the top hits shared only the authors' names (the Borsuk counterexample) | Park-Pham, Frankston-Kahn-Narayanan-Park, the expectation threshold itself | 3 cards, linked to the threshold-function and subgraph-appearance cards | Park-Pham and FKNP at ranks 1-2 in both searches, the definition third in one |
| Huang's sensitivity theorem | 0 of 16 printed cards relevant; "sensitivity" matched noise sensitivity in percolation | sensitivity, block sensitivity and degree; Huang's induced-subgraph theorem; s(f) >= sqrt(deg f) | 3 cards with proofs (the signed matrix with A^2 = nI and Cauchy interlacing), linked to KKL and influence | 5 of 16, every new card at rank 1-3; the first search fell from 231 s to 21 s |
| Friedgut's sharp threshold theorem | 0 of 16; rank 1 was a card withdrawing an earlier, garbled statement | correct statements of Friedgut (1999) and of Bourgain's appendix theorem | 2 cards with labelled proof outlines, linked to the Russo formula, KKL, colourability and the withdrawal card | the theorem and its main lemma in the top three of both searches |
| junta theorems, FKN, Majority is Stablest, cube edge-isoperimetry | 0 of 24 | all four | 4 cards with outlines, nine links to influence, hypercontractivity and KKL | 6 of 24, three of the four first in their own search |
| modern sunflower bounds | only the 1960 Erdos-Rado card | Alweiss-Lovett-Wu-Zhang, Rao, Bell-Chueluecha-Warnke, the open conjecture | 4 cards, six links (to FKNP and Park-Pham among them) | 3 of 3 targets in the top 4; three control searches unchanged |
| Kelley-Meka, PFR, cap sets | no Kelley-Meka, Freiman, PFR or cap-set card; Roth first | Kelley-Meka, Bloom-Sisask, Croot-Lev-Pach, Ellenberg-Gijswijt, Freiman, Gowers-Green-Manners-Tao | 6 cards, eight links to Roth, Green-Tao and the sunflower cards | 3 of 3 gap searches fixed; Roth and Green-Tao stayed in the top 8 |

The same sweep found hypercontractivity, the Lovasz Local Lemma and diagonal Ramsey well served, and those searches
were left alone. In five of the six rounds the store had no card at all; the sixth (Friedgut) had a wrong statement and
its withdrawal, so the answer card was a notice that there was no answer. None was a ranking fault.

## What the rounds taught

- Check the store before touching the ranking. A title and body search over the nodes settles in seconds whether a
  card exists. Twice a lead from the previous round was wrong (duplicate cards that turned out to be versions of one
  logical id, each with a supersedes link and only one current; edges thought to be written twice that a direct read
  showed once), and the read is what caught it.
- A withdrawn statement is not an answer. The withdrawal card ranked first for its own theorem, which is correct
  behaviour for the card and useless to the reader. The fix is the correct statement, linked to the withdrawal.
- Run the draft validator before submitting. One bundle was refused for a theorem without proof text, a licence the
  inbox does not accept and a relation kind drafts may not use ([adding-cards.md](adding-cards.md) lists the rules).
  A refused file counts as handled, so the corrected bundle needed a new name and a second lease on the store.
- Measure on a state that has the new cards. One after-run served a prepared search state whose store read had begun
  before the ingest, and it was identical to the before-run. Measure against the live store, or after a build that
  started after the ingest has finished.
- Keep control searches. Each round reran searches the new cards should not touch, and none moved.

## A related check on the test itself

In the three-arm test the Codex brain arm lost 69 of 437 rows. Reading each row: 47 were empty runs (the other arms
lost 51 and 85 the same way), 9 never called the recall tool, most likely because the client had not offered it that session, 6
answered without any tool call, and 7 called recall and were still wrong. So most of the "unknown after a miss"
answers were no search at all, and only 7 were recall failures. A row whose agent never reached the recall tool should be
treated like an empty run: rerun, not graded.
