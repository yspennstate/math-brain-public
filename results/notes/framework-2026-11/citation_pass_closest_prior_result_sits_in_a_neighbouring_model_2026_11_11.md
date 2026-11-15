---
name: citation_pass_closest_prior_result_sits_in_a_neighbouring_model_2026_11_11
description: "Citation pass found nothing under the problem name? Search by the METHOD and the QUANTITY too, and read the remarks of the closest paper: P0089 closest prior result (Choi-Sethuraman-Venkataramani 2016, same time change, other graph model) and P0072 same-law variant (Armfield-Mailler 2026) were both outside the problem-name search"
metadata:
  type: feedback
  created: 2026-11-11
  created_at: 2026-11-11T08:22:15+02:00
  status: provisional
  evidence: "P0089 repo 1a29cfcf and P0072 repo 3d1bf751 related-work commits, 11 Nov; arXiv:1402.4088 Theorem 2.3 and Remark 2.4 read in the PDF"
  lesson: true
---

Two of the four papers I ran the citation pass on (11 Nov, the author's order to cite every relevant source) had their closest earlier result outside the place a search by problem name looks.

P0089 (sublinear preferential attachment with fixed out-degree m, Open Problem 24 of Aletti et al.): the closest paper is Choi, Sethuraman and Venkataramani, Random Structures Algorithms 48 (2016), arXiv:1402.4088. It is about a different graph model (one edge per step, to a new vertex with probability p, otherwise between two old vertices), so a search for "fixed out-degree" or for the open problem does not find it. It proves the law of large numbers for degree counts under w(k)/k -> 0 with the same time change that makes the fluid equation linear, and its Remark 2.4 says the method should extend to finitely many edges per step. Our degree statement had to be presented as the counterpart of theirs, not as new.

P0072 (loop-erased ants): Armfield and Mailler, arXiv:2610.18453, define a forward-loop-erased variant that has the same law as the process in our paper, so our theorem applies to their model and they had to be cited.

**Why:** a paper that proves, under the author's name, something a neighbouring paper already has in another model reads as careless; a paper that does not notice its theorem covers a new variant undersells itself.

**How to apply:** in the citation pass, after the problem-name search, run three more searches and read the abstracts and remarks of the hits, not just titles: (1) by the METHOD (here "time change", "fluid limit", "sublinear preferential attachment"); (2) by the QUANTITY with the model words left out (degree distribution, product formula); (3) for variants of the process defined in the last year (forward / reversed / lazy versions). Read the remarks after the closest paper's main theorem: that is where authors say what their method should also give. Cite a paper only for what its abstract or text supports (I cut five candidate citations whose scope I had not checked). Start the edits from the repo HEAD, rebuild, pass paper_release_guard, then push repo, public table copy and brain mirror, and tell the Zenodo agent the commit.

Tools: ~/agent_run/crossref_check.py "<query>", crossref_doi.py <doi>, arxiv_check.py, arxiv_abs.py, cited_by.py (generic User-Agent, no owner details in the request).

Related: [[citation_pass_search_recent_arxiv_for_the_key_quantity_2026_11_11]], [[own_earlier_paper_overlap_is_the_missed_citation_2026_11_11]], [[citation_hooks_sixteen_before_a_paper_is_posted_2026_11_11]], [[p0089_sublinear_attachment_local_limit_paper_posted_2026_11_11]], [[p0072_loop_erased_ants_paper_posted_2026_11_11]].

