---
name: potts_papers_now_cite_the_openai_preprints_github_only_2026_11_10
description: "Do the posted Potts Kesten-Stigum papers cite the OpenAI three- and four-state preprints? Yes on GitHub since 10 Nov 09:28 (q3 08bfc3ed, q4 7b0c27dd); ResearchGate/arXiv copies not yet updated"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T09:30:36+02:00
  status: verified
  evidence: "git fetch then rev-parse: local = origin/main on both repos; pdflatex logs clean; paper_release_guard rc 0"
---

Both posted Potts papers cite the OpenAI preprints since 10 Nov 2026 09:28.

Three-state paper (yspennstate/potts-kesten-stigum-small-degree, commit 08bfc3ed336dfab7dee41f6c964ef108aacd56e3): abstract, introduction, bibliography entry OAI3 and README say that the OpenAI preprint of 25 September 2026 establishes the threshold at every degree by an entropy argument and that Theorem 1.1 is the ferromagnetic regular-tree case of that result, proved by a different route. 17 pages, log clean, release guard passed.

Four-state paper (yspennstate/potts-four-state-binary-tree, commit 7b0c27ddd03919459fb28562af9819a38c06be68; local clone potts-four-state-binary-tree): abstract, introduction, bibliography entry OAI4 and README say the OpenAI preprint of 5 October 2026 establishes the threshold on every regular and Poisson tree (preserved polynomial constraint, cubic saving) and that the main theorem is the binary-tree case, proved by a different route. 9 pages, log clean, guard passed.

Not done: the ResearchGate and arXiv copies still carry the old text.

This completes the open item in [[t067_row_stated_in_openai_preprints_our_potts_papers_do_not_cite_them_2026_11_10]].

