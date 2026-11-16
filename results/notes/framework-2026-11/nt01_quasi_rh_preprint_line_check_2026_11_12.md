---
name: nt01_quasi_rh_preprint_line_check_2026_11_12
description: "Quasi-Riemann hypothesis claimed (OpenAI preprint 5 Oct 2026, no zeros in Re s > 11/12 for Hecke L-functions over Q(sqrt -3)): read line by line, no error found, cited results match Dunn-Radziwill and Goldmakher-Louvel; one reader's pass, unconfirmed until a second audit; NT01 row keeps its place"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T06:39:49+02:00
  status: provisional
  evidence: "NT01_CHECK.md in 06_math_research/nt01_quasi_rh_agent_2026_11_12, brain repo commit edbc954e9b98dfe69b69095b240c4bede902605d; 49 pages read against the PDF, 3 computer tests, sources arXiv 2109.07463 and 1112.1642 compared"
---

The row NT01 (Riemann hypothesis) of the general-math list: on 5 Oct 2026 a 49-page preprint in the openai/math
repository (commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a) claims that no finite-order Hecke L-function over
Q(sqrt -3), hence no Dirichlet L-function and not zeta, has a zero in Re s > 11/12. A 199-page preprint of
30 Sep claims 7/8.

What was done (12 Nov, an agent): the 49-page paper was read line by line against the PDF pages and
reworked by hand, with three computer tests (Lemma 4.1 table, Lemma 4.2, the quadratic Gauss sum formula on 564
moduli). Section 3 (mean square implies the half-plane), Sections 4 to 7 (the mean-square estimate: Poisson in
the row, Gauss-Jacobi turning mu times a sextic Gauss sum into a cubic one, Kubota's theta function, the theta
transformation, the quadratic large sieve, the recursion that removes cube factors) and Appendices A and B: no
error found. The cited results were compared with their sources: Patterson's coefficient formula and cusp
expansions as recorded in Dunn-Radziwill arXiv 2109.07463 (5.4), (5.6), (5.7), (5.13), (5.14) and the table on
page 78; the Goldmakher-Louvel quadratic large sieve arXiv 1112.1642 Theorem 1.1. They are used as stated.

What it is not: a verification. One reader's pass. Not reworked: the Poisson limit behind (A.1) (tested), the
Phragmen-Lindelof step, the proofs of the cited results, Patterson's 1977 paper itself, the 199-page preprint.
Weakest under a single pass: uniformity of constants across the recursion in Section 5.

Rule for the list: the row keeps its place (the claim is 11/12, not 1/2). Nothing is to be called confirmed
until a second independent audit agrees.

Traps met on the way: pdftotext drops bars, hats, breves, tildes and square roots, so (2.10), (4.1), (4.3),
(7.3), (A.6) to (A.18) all look wrong in the text file and are right on the page
([[pdftotext_drops_overlines_look_at_the_page_2026_11_12]]). The preprint's additive character
e(z) = exp(4 pi i Im z/sqrt 3) is Dunn-Radziwill's e-breve(z/lambda); that is where the factor chi_n(lambda)^2
in (2.10) comes from.

Files: the private repository, 06_math_research/nt01_quasi_rh_agent_2026_11_12/NT01_CHECK.md (the
check, section by section), STATE.md, nt01_checkA1.py and the earlier test scripts there.

