---
name: p0143_longest_minimum_weight_path_paper_posted_2026_11_11
description: "Longest minimum-weight path M_n in K_n with exponential weights (P0143, Saint-Flour Open Problem 3.1): what is proved, posted and still open? Upper bound to second order posted 11 Nov; simulations put the mean 5.1-5.6 below b_n; whether M_n - b_n is tight is undecided (a barrier term and 1/log n corrections predict the same drift); Zenodo 10.5281/zenodo.24143542"
metadata:
  node_type: memory
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T20:04:22+02:00
  status: verified
  evidence: repo yspennstate/longest-geodesic-complete-graph b6b49a5c9f59; ledger open-problems-repo 4b9c15e61d59; math-brain-public 4cccdbc5193e; data/sim_summary.json in the repo; Codex referee REPORT.md sha256 e2fc677c
  modified: 2026-11-11T22:01:05.469Z
---

P0143 (van der Hofstad, Saint-Flour notes 2017, Open Problem 3.1: fluctuations of the longest minimum-weight path
M_n in K_n with Exp(1) weights) is posted as a PARTIAL result on 11 Nov 2026: paper "An upper bound to second order
for the longest minimum-weight path in a complete graph", public repo
https://github.com/yspennstate/longest-geodesic-complete-graph at b6b49a5c9f59d6fda266718dce4be1948679403f (12 pages,
programs, simulation data). Ledger row open-problems-repo master 4b9c15e61d59; public copy and table row
math-brain-public main 4cccdbc5193e; notes and the referee report in the brain repo under
06_math_research/p0143_longest_geodesic_2026_11_11/.

What is proved (alpha = 3.5911 solves alpha log alpha - alpha = 1, theta = log alpha,
b_n = alpha log n - (log log n)/(2 theta)): P(M_n >= b_n + x) <= C alpha^(-x); the expected number of pairs at
hopcount >= k_n is (C_* + o(1)) alpha^(-(k_n - b_n)), C_* = 0.0110396527896; at k = ceil(b_n) the second moment is at
least c n^(5 - alpha log 4) times a power of log n, so the plain second moment method fails; P(M_n = n-1) =
n/(2 (n-1)!). No lower bound beyond Addario-Berry, Broutin and Lugosi (2010).

What the simulations say (Dijkstra from every vertex, n = 250..4000, 8000 down to 120 graphs, on Mac mini 2 through
fillq): the mean of M_n sits 1.72, 1.86, 1.95, 2.11, 2.15 below k*_n (the level where the exact first moment is 1),
i.e. 5.13 to 5.60 below b_n, and the gap grows by 0.47 (s.e. 0.10) over that range. The frequency of {M_n >= k} just
above k*_n is 0.16 down to 0.08 of the first moment.

Is M_n - b_n tight? UNDECIDED, and simulation cannot decide it. A forced barrier (coefficient 3/(2 theta), as for
branching random walk) predicts a drift of 0.32 over n = 250..4000; tightness with 1/log n corrections of the size
seen exactly for one root (ratio 0.617 -> 0.510, fit 0.346 + 1.34/log n, squared for two ends) predicts 0.30;
observed 0.43 (s.e. 0.10). The two readings differ only in curvature and n = 10^5 would not separate them. A first
cluster heuristic (far end with a subtree of size (log n)^0.109) was wrong: under the size-biased measure the far
end has label n/T with T of density t^(-(alpha+2)), subtree of mean size 1.28; the log log offset is absorbed by
the local-limit factor. Counting pairs that share the middle of a long path also gives O(1). Working guess:
tight, proof by a truncated second moment. The paper says only that the range of n is too small to show it.

Tools worth reusing:
- single root, exactly: t_n(h) = P(height of a random recursive tree > h) satisfies
  t_n(h) = (1/(n-1)) sum_K [t_K(h-1)(1 - t_{n-K}(h)) + t_{n-K}(h)] (split at the subtree of vertex 2, uniform size);
  code/root_tail.py, n = 32000 in 90 s. P(R_n >= k) over the expected number of deep vertices at k = ceil(b_n) is
  0.62 (n=250) down to 0.49 (n=32000): for one root the first moment is sharp up to a constant.
- two-ball representation for a lower bound: grow the minimum-weight balls from i and j together; each is a random
  recursive tree; with sizes a, b the next event is growth at rates a(n-a-b), b(n-a-b) or a collision at rate 2ab;
  at the collision H(i,j) = D_U + D_V + 1 with U, V uniform in two independent recursive trees.
- a faster simulation if larger n is ever wanted: only edges lighter than the weighted diameter can lie on a
  minimum-weight path, so sample just the edges below 5 log n / n, run heap Dijkstra on that sparse graph, and
  accept the run when the largest distance found is below the cut (then it is exact). About n^2 log^2 n instead of n^3.
- an outlier is checked, not dropped: one of 8000 graphs at n = 250 had M_n = 24 where E N_{250,24} = 9.3e-7
  (probability at most 0.0075 for the sample). It was recomputed with a second algorithm (Bellman-Ford with a bounded
  number of edges, check_rep.c) and the generator read against its reference; it is a real sample and is reported in
  the paper.
- a slow drift in a simulated mean has two readings whenever log log n and 1/log n are the candidates: compute what
  each predicts over the simulated range before writing a conjecture down.

Referee: Codex gpt-6.1-sol at high on Mac mini 1 passed Theorems 1-2 and Propositions 3-4 with its own enumeration
and simulations and found two wrong remarks (order of the Gaussian error after Theorem 2; wording of the
Hamilton-path event), both corrected before posting. It had no network, so the literature rests on the citation pass
(22 outside entries, each checked against Crossref or arXiv; Chen-Ma arXiv:2604.20139 Proposition 3.1 credited for
the fixed-level one-root estimate).

Next on this problem: the lower bound needs a truncation on each of the two recursive trees and a four-ball bound
for two disjoint pairs; judged a project of several days. Zenodo: DOI 10.5281/zenodo.24143542 (record 24143542,
deposited by an agent, PDF identical to the repo's). A second, independent check by an agent found no
gap (brain repo 730fe21b, 06_math_research/lean_checks_agent/p0143_audit/). ResearchGate is with an agent.

Related: [[p0089_sublinear_attachment_local_limit_paper_posted_2026_11_11]],
[[zenodo_lagged_github_reference_commits_check_latest_md5_2026_11_11]],
[[citation_best_known_bound_check_the_live_record_table_fei_c71_2026_11_11]].

by 0.16. The frequency of {M_n >= k} just above k*_n is only 0.08 to 0.16 of the first moment and falls with n.
Working conjecture: M_n = alpha log n - c log log n + O(1) with c larger than 1/(2 theta), possibly 3/(2 theta) as
for branching random walk, so Theorem 1 is probably not sharp in the second-order term. Heuristic: the far end of a
path with b_n + O(1) edges has a subtree of size about (log n)^(1/(2 alpha theta)) = (log n)^0.109 in the other end's
tree, and every vertex of that subtree ends a path at least as long, so pairs come in clusters of that size. The
ResearchGate (told an agent; ResearchGate is with an agent).
