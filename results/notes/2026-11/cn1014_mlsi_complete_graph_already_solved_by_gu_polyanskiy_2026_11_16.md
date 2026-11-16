---
name: cn1014_mlsi_complete_graph_already_solved_by_gu_polyanskiy_2026_11_16
description: "[VERIFIED] Catalogue row CN1014 (exact modified log-Sobolev constant of K_n, 'not known' per Bristiel-Caputo 2021) is SOLVED: Gu-Polyanskiy arXiv:2005.05444, CMP 404 (2023), Theorem 1 at p=1. Our 5-page proof was withdrawn after the first-reader audit; the prior-art check stopped one reference short."
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T06:16:51+02:00
  status: provisional
  evidence: ""
---

status: verified

The exact constant rho(K_n) = n(1 + inf_{1/n<s<1} D(1/n||s)/D(s||1/n)), with minimisers taking one larger value at a single vertex, is Theorem 1 with display (10) at p = 1 of Y. Gu and Y. Polyanskiy, Non-linear log-Sobolev inequalities for the Potts semigroup and applications to reconstruction problems, arXiv:2005.05444 (May 2020), Comm. Math. Phys. 404 (2023) 769-831. Time change: rho(K_n) = (n-1) alpha_1. Their Proposition 2: n + n/log n <= rho(K_n) <= n + (1+o(1)) n/log n. Goel 2004 Lemma 2.6 already has the identity E(f, log f) = n Cov(f, log f) and the upper bound n(1 + 4/log(n+1)). The full-support dichotomy is Bobkov-Tetali 2006, not CCGP.

How it was missed (the scar): a 2021 paper (Bristiel-Caputo, Remark 1.2) said the value is not known, and I took that as the open check. I read CCGP 2409.07689 Examples 5 and 27, which cite GP23 three times on the complete graph, and did not follow those citations. The auditor found it in one search for 'Potts semigroup log-Sobolev'.

How to apply: an 'X is not known' sentence in a paper is dated by that paper and can be wrong already when written. Before calling a catalogue row open or writing it up: (1) follow every citation in the most recent paper that treats the same object (here the K_n examples of CCGP); (2) search the object under its other names (complete graph = Potts / mean-field / Curie-Weiss channel / k-ary symmetric channel); (3) run the first-reader audit before drafting the full paper, not after. Our own proof (third-order expansion for c_n < 1 and the 1_v - 1_w second-order step) is a shorter proof of the p = 1 case; it is not posted. Records: loops/72de1487_loop_1115/cn1014/paper/WITHDRAWN.md; audit audits/reports/2026/11/16/paper_audit_cn1014_paper_main_4d893e/REPORT.md. Related: [[open_problem_catalogue_1128_probability_networks_computation_2026_11_16]] [[owner_rule_check_literature_and_github_for_other_solutions]]
