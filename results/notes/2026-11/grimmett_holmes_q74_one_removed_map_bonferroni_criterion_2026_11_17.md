---
name: grimmett_holmes_q74_one_removed_map_bonferroni_criterion_2026_11_17
description: "[PROVISIONAL] Grimmett-Holmes Question 7.4 (CN0521): for G = F_S minus one map f, P is in P(G) iff sum_i p_{i,f(i)} <= n-1 (sharp Bonferroni/Frechet); Q -> 1 with log(1-Q_n) ~ -2 n^2 log n; positivity iff rank n(n-1)+1"
metadata:
  type: project
  created: 2026-11-17
  created_at: 2026-11-17T01:25:34+02:00
  status: provisional
  evidence: ""
---

status: provisional (LP-checked n=2,3; not audited). Grimmett and Holmes, Coalescence in Markov chains, arXiv 2510.13572, Question 7.4 asks what Q(P(G)) is for G a subset of F_S. Removing one map f: a coupling of the rows avoiding f exists iff sum_i (1 - p_{i,f(i)}) >= 1. Necessity is Bonferroni; sufficiency puts arcs of length 1 - p_{i,f(i)} end to end on a circle. So Q = Pr(X_1+...+X_n <= n-1), X_i iid q_1/(q_1+...+q_n), which equals 1/2 at n=2 (their Prop 7.5), about 0.99866 at n=3, and 1 - exp(-(2+o(1)) n^2 log n) in general. Removing a cylinder {g(i)=f(i), i in I} gives sum over I <= |I|-1, which contains their Prop 7.6(a). Q(P(G)) > 0 iff the incidence vectors of G span dimension n(n-1)+1. This covers their Prop 7.6(b) and Example 7.7. A partial answer only, not a solution, and too thin for a paper by itself. Files: 12_cognitive_architecture/loops/72de1487_loop_1115/cn0521/ (NOTE.md, check.py, cyl.py). What would change it: a facet description of conv{A_f} for general G, or the published JTP version answering more.
