---
name: i0096_balan_wang_conj20_open_gaussian_op21_solved_2026_11_13
description: "I0096 Balan-Wang omega(A) Conjecture 20 (worst case, N=2M-1) open; the Gaussian Open Problem 21 is solved: 4^{-M} (the author's 2607.06249, Haggblom 2609.28198)"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T16:49:20+02:00
  status: provisional
  evidence: "arXiv API abstracts of 2607.06249, 2609.28198, 2608.07410 and the 2603.29571v1 HTML Entry 10, read 13 Nov 2026"
---

I0096 is Randomstrasse101 2025 (arXiv:2603.29571v1) Entry 10: Conjecture 20 (Balan-Wang 2013) says every full-spark (2M-1) x M real A has omega(A) <= C max_k ||A_k|| beta^M, where omega(A) = min over S with rank(A_{S^c}) < M of sigma_M(A_S), i.e. at N = 2M-1 the least singular value minimised over all M-row submatrices. Open Problem 21 there (the Gaussian value) is ANSWERED in print: omega(A) = 4^{-M+o_P(M)} by the author's own preprint arXiv:2607.06249 (Y. Shmalo, 7 Jul 2026), sharpened to (w_M sqrt(M) K_M)^{-1} <= omega(A) <= w_M/(sqrt(M) K_M), K_M = binom(2M-1,M), by C. E. Haggblom arXiv:2609.28198 (23 Sep 2026), extended to bounded-density subgaussian entries by Yang-Wen-Shmalo arXiv:2608.07410. The worst-case Conjecture 20 is open as of 13 Nov 2026 (a web search found no proof or counterexample).

Our intake ledger listed I0096 as unattempted although the author's own paper answers its Open Problem 21: another case of the ledger being blind to posted papers ([[intake_ledger_blind_to_posted_papers_filter_by_repo_readmes_2026_11_13]]). The deterministic gap: Cauchy-Binet gives a minor with |det| <= c^M, c < 1, but a small determinant does not by itself give a small least singular value for one subset. A Codex claim run I0096A went into batch_0cf7 on worker machine 1 on 13 Nov.

