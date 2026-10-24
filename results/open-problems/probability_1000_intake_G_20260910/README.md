# Claude intake G for the 1,000 open probability problems campaign (2026-09-10)

Sixth disjoint intake ledger, after the Codex tree (`Downloads/Probability_1000_20h_20260906/`), the 09-07 Claude
list, and intakes D, E and F. Problem ids carry the prefix `G`. Written by `claude-prob1000-0910` in one two-hour
session (15:42-17:42 local) whose other half went to F0090 (see below). Same schemas and tooling as intake F
(`intake_tools.py`, `add_batch.py`, `raw/arxiv_search.py`, copied and re-pointed).

## How the sources were chosen

`raw/all_prior_sources.tsv` is the union of every earlier ledger's `sources.jsonl` (426 rows, 09-10). The arXiv API
was queried for math.PR papers matching "open problems", "open questions", "open problem", "survey", "conjectures"
(238 candidates, `raw/arxiv_candidates.json`), filtered against that union by normalised title and arXiv number, and
twelve recent papers were downloaded and grepped for numbered conjectures, questions and "open problem" sentences.
Eight yielded admissible statements. Three of the other four RESOLVE problems that may sit in earlier ledgers and
are recorded here as leads, not rows:

- Zhu, arXiv:2609.06818, proves Aldous and Fill's Open Problem 6.14 (maximum relaxation time of simple random walk
  on regular graphs, bound (1+o(1)) 3n^2/(2 pi^2), cubic graphs extremal). The Codex row P0244 "Sharp extremal walk
  parameters among regular graphs" should be checked against it.
- Brown, Rosenthal and Zhou, arXiv:2609.07819, resolve all seven Haggstrom-Rosenthal (2007) open problems on Markov
  chain CLT variance formulae. No earlier ledger row names Haggstrom-Rosenthal, so probably nothing to exclude.
- Doumas and Spektor, arXiv:2606.21591, prove the siblings-coupon-collector conjecture (uniform distribution
  maximises the expected deficit). Not in the earlier ledgers.
- Caracciolo, Sicuro and Sportiello, arXiv:2608.22308 (two conjectures on spanning trees in the assignment problem)
  was downloaded but its conjectures are not numbered in the extracted text and were not mined in the time available.

## What is here

- `sources.jsonl` — 8 sources, all `validated_and_extracted`. Raw bytes and text under
  `Downloads/Probability_1000_intake_G_20260910/sources/<id>/`. Cerf's 708-page monograph exceeded the fetch tool's
  size limit (`source_failures.jsonl`) and was acquired with curl and recorded by hand with its hashes.
- `problems.jsonl` — 15 rows, `G0001`..`G0015`; 14 admitted. `G0003` (Cerf's deviations pivotal inequality) is
  recorded but not admitted because the source leaves its hypothesis class "intentionally vague".
- `attempts.jsonl` — 14 rows (`probability-attempt.v1`), one per admitted problem, all by this agent, all written
  in the same session: first attacks, reductions and sanity checks, not solutions. Two are flagged `partial_result`:
  G0008 (two-point monotonicity on Z^2 holds for large n at every p != p_c, by Ornstein-Zernike; the first attempt's
  small-p claim was withdrawn the same session, see G0008-A002 and the `corrected_by` field on G0008-A001) and
  G0014 (uniform integrability half of the Bramson conjecture follows from the x log^2 x criterion under bounded
  displacements). G0001 is shown EQUIVALENT to theta(p_c) = 0 modulo the supercritical tail theorem, so it is a
  reformulation of C0023 rather than a new target and should be merged with it.
- `batches/mk_b01.py` writes `batches/b01_g0001_g0015.json`, the exact batch appended.

## Counts (from `python intake_tools.py snapshot`)

    validated sources                 8
    problem rows                     15
    admitted rows                    14
    attempts (substantive)           14
    not admitted (ill-posed)          1   (G0003)
    rows flagged partial_result       2   (G0008, G0014)
    candidate full solutions          0

## Caveats a merger should know

- Every `status_search` field says "no other search run": the openness of each row rests on the source's own
  statement (all sources are August-September 2026 postings) plus a keyword dedup against the 1,107 earlier rows.
  The standing rule from intake D applies: compare the objects by name before excluding or admitting.
- G0002's attempt records a magnitude check that DISAGREES with the bound the source quotes (E|P_2^+| <= 6 sqrt n);
  the source's normalisation of second-order pivots (formulas (51.1)-(52.1)) was not extracted. Read them before
  attacking the row.
- The Kozma-Nitzan conjecture (G0005) is recorded from Flammant's restatement, not from Kozma and Nitzan's paper,
  which was not fetched.

## P0291 (later the same day, on the owner's "keep working on solving open problems")

Leskelä's Problem 3 (journal numbering) on a non-monotone CTMC with the supermodular time ordering is answered
yes by the symmetric three-state star chain, with a proof whose one combinatorial step has an exact 11-term
certificate. The memo is `../prob1000_lean_20260908/REPORT_P0291_...md` (copy in Downloads), the scripts
`p0291_*.py` beside it; the attempt is recorded here as the cross-ledger row `P0291-A002` in `attempts.jsonl`
(the problem itself belongs to the Codex tree, which was not edited).

## F0090 (same session)

The session's other deliverable is a full argument for Kalai's Conjecture 8 (= GPS 2010 open problem 1): the
spectral entropy of the percolation crossing event is O(I(f)), by a quadtree coding bound plus GPS's one-box
estimate and the polynomial lower bound on the four-arm probability. It lives in intake F as attempt `F0090-A002`
with the memo at `../prob1000_lean_20260908/REPORT_F0090_Kalai_conjecture_8_entropy_influence_percolation_2026-09-10.md`
(copy in Downloads). Author-checked, not refereed.
