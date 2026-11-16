---
name: conjecture_credited_to_the_preprint_that_quoted_it_and_already_proved_2026_11_11
description: "Paper takes a conjecture from a recent preprint? Read the line before it for the real source (copula W2<=1/10 was Catalano-Lavenant Remark 3, not Schrott) and search arXiv for the statement after that date: Ansari 2609.23940 had proved it 7 weeks before we posted (fixed Zenodo 24130551)"
metadata:
  type: feedback
  created: 2026-11-11
  created_at: 2026-11-11T10:44:04+02:00
  status: verified
  evidence: "Zenodo 24130551, commit 69890c2f, arXiv 2609.10467 p1, 2609.23940"
  lesson: true
---

The layered-permutation copula paper (github.com/yspennstate/wasserstein-layered-permutation-copulas, Zenodo 24069947, posted 9 Nov 2026) said "Schrott conjectured" that every copula is within W_2^2 = 1/10 of the uniform law, and its only reference was Schrott arXiv:2609.10467. Schrott's own text, one line above his Conjecture 1.1, credits it to Catalano and Lavenant (arXiv:2510.06034, Remark 3). And Ansari (arXiv:2609.23940, 20 Sep 2026, seven weeks before we posted) proves it with the equality cases. Found in the 11 Nov citation pass by one arXiv abstract search (copula AND Wasserstein AND independence AND maximal). Fixed as version 24130551 (commit 69890c2f): the conjecture is credited to Catalano-Lavenant, Ansari's proof is cited, and the paper's finite grid statement (A_n) is framed as what it is, a discrete statement that implies the bound and is not covered by the theorem for copulas. Mordant-Segers, De Keyser-Gijbels, Aurenhammer-Hoffmann-Aronov and the software were added. The README had also called (A_n) "equivalent" to the conjecture; it only implies it.

**Why:** a standing rule to cite every relevant source. A conjecture credited to the person who quoted it, and presented as open after it was proved, is two public mistakes on one page.

**How to apply:** when a paper takes a conjecture from a recent preprint, read the sentence before the conjecture in that preprint for its source and cite the first place it was posed with its number (hook C03). Then search arXiv for the statement itself in other words, dated after the source (C05/C11), before calling it open. A one-reference bibliography is the smell (C12). Related: [[citation_pass_search_recent_arxiv_for_the_key_quantity_2026_11_11]], [[citation_hooks_sixteen_before_a_paper_is_posted_2026_11_11]], [[arxiv_api_http_301_empty_search_reads_as_no_prior_work_2026_11_11]].

