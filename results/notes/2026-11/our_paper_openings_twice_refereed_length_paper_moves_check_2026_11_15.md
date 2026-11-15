---
name: our_paper_openings_twice_refereed_length_paper_moves_check_2026_11_15
description: "[PROVISIONAL] Our posted math papers' first intro paragraph 149-198 words vs refereed median 100 (4-7 cites vs 2, a display); abstracts say 'we' a third as often. paper_moves.py check now cleans raw .tex"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T09:44:37+02:00
  status: provisional
  evidence: ""
---

paper_moves.py check (writing_brain/papers) compares a paragraph's measures with the refereed arXiv shelf (4,365 papers, probability/combinatorics/stats/ML). Until 15 Nov it read 0 citations and 0 displayed formulas on a paragraph pasted from a .tex, because the shelf text is stored after cut_papers.clean ([cite], $$...$$); check now runs clean on raw LaTeX first.

Run on three papers posted 14 Nov (symmetric-gaussian-noise-stability-slabs, hyperbolic-voronoi-typical-cell-variance, stationary-cover-time-four-states): the first introduction paragraph ran 149, 193, 198 words against a shelf median of 100 (middle half 69-141), with 4, 7, 5 citations against 2, and two carried a displayed formula (the shelf's middle half has none). Ours define the object, give its history and cite the field in one paragraph; refereed openings state the object and why it matters and leave definitions and history to the next paragraphs. Abstracts: 0.7-0.9 'we' per 100 words against 2.2 (1.4-3.2); each says 'We show' once.

How to apply: before posting a paper, run python -I -X utf8 paper_moves.py check intro_opening <first paragraph file> and check abstract <abstract file>; split an opening paragraph over about 140 words. Size of doubt: three papers, all from our agents in one week; the shelf is cut by blank-line paragraphs, which if anything makes shelf paragraphs longer, not shorter. Related: [[paper_shelf_refereed_arxiv_moves_and_check_2026_11_14]], [[owner_order_papers_credit_the_mathematicians_intro_and_ai_declaration_2026_11_14]].
