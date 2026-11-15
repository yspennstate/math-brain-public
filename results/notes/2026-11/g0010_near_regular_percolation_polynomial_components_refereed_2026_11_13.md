---
name: g0010_near_regular_percolation_polynomial_components_refereed_2026_11_13
description: "[PROVISIONAL] CMW Question 5.2 (largest subcritical component given Delta, lambda): near-regular is NOT enough for log n once (1-eps)(1+delta)>1; (log n)^3 at equality; two audits, PARTIAL"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T07:35:24+02:00
  status: provisional
  evidence: ""
---

Open-problem lane 13 Nov 2026 (an agent). Source: Christoph-Morawski-Wigderson, The critical probability for percolation on finite graphs, arXiv:2608.19145v1, Question 5.2 p.20 (Theorem 1.4 pp.4-5 gives L1=O(sqrt(n Delta) log n / lambda) at p<=(1-eps)/lambda). Results, Codex run G0010A + independent referee G0010AR (MINOR; status PARTIAL, not a counterexample): (A) if q(1+delta)>1, q=1-eps: a complete b-ary tree joined by one edge to K_{k+1} (b~rk, 1/q<r<1+delta; optional blow-up of vertices into independent sets of size b^{tau h}) has Delta<=(1+delta)lambda, lambda~k sets p, the tree is supercritical (b p ~ rq>1), so L1>=n^c whp, c<log(mu)/((1+tau)log b) <1/(2(1+tau)); refines CMW footnote 7 (d-ary trees). (B) q(1+delta)<1 gives O(log n) (Diskin-Erde-Kang-Krivelevich arXiv:2209.03722 Thm 2), sharp on the cycle. (C) p lambda<=q<1 and p Delta<=1 gives O_eps((log n)^3) via resolvent u=(I-pA)^{-1}1, max u=O(log n), exponential-moment induction for the multitype branching process. (D) degree-sensitive resolvent bound O(B^{log(qR)/log R+zeta} log n), R=Delta/lambda, B=sqrt(n Delta)/lambda, beats B log n for bounded R with small zeta. Not found in print (search, not a priority claim). Open: the tight bound, log vs (log n)^3 at equality, matching exponents above the margin. Archived 06_math_research (runs G0010A, G0010AR); ledger row G0010 in probability_1000_intake_G. Related [[c0159_grandparent_graph_finite_touching_refereed_2026_11_13]].

Published 13 Nov 2026 12:5x: github yspennstate/near-regular-percolation-components a1335703 (paper, verify/simulate/analyze code, data), Zenodo 10.5281/zenodo.24193275 (pdf md5 b4dd41ad). ResearchGate folder ready in researchgate_queue/q4. Follow-up not in the paper: the 11-12 Oct trio run (trio_2026_10_11/op/G0010, unaudited) claims O((log n)^3) under the wider p(Delta-1)<=1 wedge with a matching Theta(h^3) lower bound on the b-ary tree at eps=1-2/sqrt(b) - audit it before any second paper.
