---
name: d0071_golden_mean_cubic_transitive_open_grimmett_grigorchuk_2608_codex_partial_2026_11_13
description: "D0071 (Grimmett-Li survey arXiv 1704.05884 Question 3.4: is mu(G) >= golden mean phi for every infinite connected simple vertex-transitive cubic graph?) is open on 13 Nov 2026. Covered since the survey: all two-ended graphs (Georgakopoulos-Wendland 2304.13317, Thm 1.3) and general Grigorchuk Cayley graphs under a condition on omega (Grimmett 2608.19349v2, Oct 2026). Codex report D0071A (13 Nov, PARTIAL, unrefereed): IMG(z^2+i) Cayley graph (girth 8, intermediate growth, no Z quotient) is an uncovered candidate, with exact SAW counts but no proof. Grimmett 2611.00816 (Oct 31 2026) is on trails versus SAWs at degree >= 4 and does not touch this"
metadata:
  node_type: memory
  status: provisional
  type: project
  originSessionId: agent-66b6-4575-b3c4-a8807fd17369
  modified: 2026-11-13T18:05:50.539Z
---

D0071, rank 52 on the 200 list. Source: Grimmett and Li, "Self-avoiding walks and connective constants", arXiv
1704.05884 (Springer PROMS 300, 2019), Section 3.2, Question 3.4, preprint p.13: is mu(G) >= phi = (1+sqrt5)/2 for
every G in G_3, the infinite, connected, simple, vertex-transitive cubic graphs? Quasi-transitive is false (mu = 1
examples; Grimmett-Li, Bounds, Fig 4.1).

Status 13 Nov 2026: open.
- Known (Grimmett-Li, "Cubic graphs and the golden mean", Discrete Math. 343 (2020) 111638, arXiv 1610.00107):
  mu >= phi given a transitive graph height function, for Q_harm graphs, for TLF-planar graphs, for the first
  Grigorchuk Cayley graph on {a,b,c}, and the small-girth lower bounds of the survey's Thms 3.5-3.7.
- Since the survey:
  - Georgakopoulos and Wendland, arXiv 2304.13317, Thm 1.3: every two-ended graph in G_3.
  - Grimmett, "Connective constants of Grigorchuk graphs", arXiv 2608.19349v2 (19 Aug, revised 7 Oct 2026):
    mu(G_omega) > phi for Cayley graphs of general Grigorchuk groups, subject to a simple condition on omega. The
    abstract restates the full conjecture as open.
  - Grant and Li, arXiv 2601.12571 (Jan 2026): substitution identities mu(G)^{-1} = g(mu(G_1)^{-1}) for gadget
    replacements; exact values for new quasi-transitive families. A tool, not a lower bound for all of G_3.
  - Grimmett, "SAWs, trails, kites, patterns", arXiv 2611.00816 (31 Oct 2026): trails versus SAWs at degree >= 4;
    for cubic graphs mu equals the trail constant, so nothing here bears on the question.
- Codex report referee_reports/2026-11-13/D0071A (13 Nov, PARTIAL, one run, unrefereed): a full literature table;
  rules out the Hanoi Towers group as uncovered (it has an infinite dihedral quotient); proposes the Cayley graph of
  IMG(z^2+i) as an uncovered candidate (girth 8, so not a standard three-generator Grigorchuk graph; intermediate
  growth by Bux-Perez); exact SAW counts with rigorous upper bounds mu <= min c_n^{1/n}, no lower bound mu >= phi.
- My arXiv check on 13 Nov (connective constant with cubic or transitive; golden mean with self-avoiding): the items
  above, nothing else on the question.
- Our 8 Sep pass D0071-A001: every solved case works through a height function (bridge counting gives the Fibonacci
  recursion with growth phi). The hard case is a group with no surjection onto Z and no known Lipschitz harmonic
  function, i.e. torsion groups such as IMG(z^2+i). That is the same wall the Codex run hit.

Related: [[d0069_grimmett_li_multigraph_saw_bound_open_atom_reduction_2026_11_13]] (same survey, Q2.2).
