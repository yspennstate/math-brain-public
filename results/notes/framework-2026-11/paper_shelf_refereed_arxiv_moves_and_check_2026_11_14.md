---
name: paper_shelf_refereed_arxiv_moves_and_check_2026_11_14
description: "Writing an academic paper section and want to see how refereed papers made the same move? writing_brain/papers: paper_moves.py show/check on 334+ refereed CC-licence arXiv papers cut into ten moves"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T18:02:49+02:00
  status: verified
  evidence: "commits ffd318f9 (tools) and 684c97bd (shelf, 334 papers, 2,661 passages, 0 latex outside maths)"
---

Writing a section of a paper (abstract, the opening of the introduction, the paragraph that says what is proved, a theorem with its lead-in, the start of a proof, a definition, the idea of a proof in words, prior work, an open question)? The paper shelf shows how refereed papers did it and measures yours against them.

  python -I -X utf8 ~/the private repository, 12_cognitive_architecture/writing_brain/papers/paper_moves.py show contribution "<subject>" --k 3
  python -I -X utf8 .../paper_moves.py check contribution <your paragraph file>

Source: arXiv OAI-PMH (math.PR, math.CO, stat.ML, math.ST from 2016), kept only when the licence is CC BY, CC BY-SA or CC0 and there is a journal reference: 4,930 kept of 212,409 records listed (PR 1,224 of 50,084; CO 1,835 of 63,038; stat.ML 1,620 of 76,717; ST 251 of 22,570; every listing ran to its end). Sources fetched from arxiv.org/e-print at one request per 3.5 s (harvest_arxiv.py; data in ~/writing_brain_data/papers). cut_papers.py cuts each main .tex into the ten moves and leaves off any passage that would show LaTeX outside the maths (17 pct did before the cleaner learned \[ \], \( \), font switches, footnotes; now 0 of 2,661).

First reading of check (14 Nov, on a contribution paragraph I wrote): refereed papers say 'we' or 'our' about 2.3 times per 100 words (middle half 1.4 to 3.6), mine 5.4; two thirds of their sentences open on the object, a third of mine. A passage is shown to learn the move from, never to copy; name the source if a phrase is used. Lane H-papers, an agent; LANES/HOW_TO_USE entry asked of an agent. Related: [[word_walk_links_senses_not_words_drift_fixed_2026_11_14]]
