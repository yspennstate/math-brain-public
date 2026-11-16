# The paper shelf

Refereed papers in probability, combinatorics, statistics and machine learning, released under an open licence (CC BY,
CC BY-SA or CC0), cut into the moves a paper has to make. An agent about to write an introduction, a contribution
paragraph or the entry to a proof first reads how published authors made the same move on the nearest subject, then
compares its own paragraph with theirs. Older literary shelves (Darwin, Abbott) give good prose, but nobody writes a
2026 introduction that way.

- `harvest_arxiv.py` lists arXiv records through the OAI-PMH feed and keeps a paper only when its licence is open and
  it carries a journal reference, then fetches the LaTeX source. It waits 3.5 seconds between requests, as arXiv asks
  of harvesters, and resumes where it stopped. Raw data goes to `$PAPER_SHELF_DATA` (`meta.jsonl`, `src/`).
- `cut_papers.py` cuts each source into passages by move (abstract, intro_opening, contribution, result_stated with
  its lead-in sentence, proof_entered, definition, idea_given, prior_work, open_question, section_opening) and writes
  `shelf/papers_NNN.jsonl`, each passage with its arXiv id, authors, journal reference, DOI and licence.
- `paper_moves.py` is the writer's tool:

      python -I -X utf8 paper_moves.py show intro_opening "random walk on a percolation cluster, mixing time"
      python -I -X utf8 paper_moves.py check contribution my_paragraph.txt
      python -I -X utf8 paper_moves.py moves

  `show` prints three published passages making that move on the nearest subject, with their sources. `check` sets
  a paragraph's measures beside the shelf's (median and middle half): length, sentence length, words before the first
  full stop, citations, displayed formulas, "we" per hundred words, and the share of sentences that open on the
  object rather than on "We", "In this" or "It is". A paragraph pasted from a .tex file is cleaned the way the shelf
  was (`\cite` to [cite], display math to a marker), so citations and displays are counted.

The shelf itself is not in this repository: it is excerpts of other authors' papers, and anyone can rebuild it from
arXiv with the two scripts above. A passage is there to learn the move from, never to copy; a phrase taken from one is
quoted and cited. About one math paper in two hundred on arXiv is both openly licensed and refereed, so a shelf grows
slowly; ours held 8,429 papers cut into 50,668 passages on 16 November 2026.

## Three of our posted papers against the shelf (15 November 2026)

- The first paragraph of the introduction ran 149, 193 and 198 words against a shelf median of 100 (middle half 69 to
  141), with 4, 7 and 5 citations against 2, and two of the three carried a displayed formula, which a refereed
  opening paragraph almost never does. Ours defined the object, gave its history and cited the field in one
  paragraph; refereed openings state the object and why it matters, and leave definitions and history to the next.
- The abstracts used "we" 0.7 to 0.9 times per hundred words against 2.2 (middle half 1.4 to 3.2). Refereed authors
  say "we" about three times in an abstract ("We prove", "we also show"); each of ours said "We show" once and gave
  every other sentence to the object.

Three papers is a small sample; the opening-paragraph length fell outside the shelf's middle half on all three.

## Credit: what existed before and what is new (16 November 2026)

A paper should say what existed before, what is new and how the two are related, and should name the mathematicians
whose work mattered most. `paper_moves.py credit` pulls, from the abstract, introduction, contribution and prior-work
passages, the sentences where a refereed paper ties a result or method to a cited earlier one: extends, generalizes or
improves; follows, builds on or adapts; differs from; answers or recovers; or names the origin ("proved by Chernoff
[cite] in dimension one ... due to Nelson [cite]").

    python -I -X utf8 paper_moves.py credit show "hypercontractivity, Gaussian Poincare inequality"
    python -I -X utf8 paper_moves.py credit check intro.tex

The shelf holds 2,005 such sentences from 1,306 papers; 424 of them (21 per cent) name the author as well as citing.
A sentence that cites only by number tells a reader that something came before, not whose it was. `check` lists the
credit sentences of an introduction and says when there are none. On the introduction of one of our posted papers
(1,117 words, 22 citations) it found one, the sentence crediting Chernoff and Nelson. `check` finds only a credit
sentence with a citation and one of those verbs; credit given in other words has to be read by a person.

## Acknowledgements

The shelf exists because arXiv (Cornell University) offers its metadata through an open harvesting interface, and
because the authors of these papers chose open licences. Every passage keeps its authors and identifiers.
