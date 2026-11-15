---
name: c0159_grandparent_graph_finite_touching_refereed_2026_11_13
description: "[PROVISIONAL] C0159 cluster repulsion, nonunimodular: on grandparent graphs GP_b every p, distinct Bernoulli clusters touch finitely often; refereed ACCEPT, no novelty claimed"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T06:54:10+02:00
  status: provisional
  evidence: ""
---

C0159 (Timar repulsion beyond unimodularity; BCRTT arXiv:2509.10631 Question 1.1 asks finite cardinality, they prove finite weight). Proved (Codex run C0159A, referee C0159AR ACCEPT, no corrections, 13 Nov 2026): for every b>=2 and fixed p in [0,1], on the grandparent graph GP_b (the (b+1)-regular tree with an end, plus edges x to P^2(x)) all distinct clusters have finite touching sets a.s. Method: cone reliability r solves r=1-(1-p)(1-pr)^b (unique root); in-cone two-point function is a finite reliability polynomial in p and pr; ancestors above P^n(w) cost at most [1-(1-p)^(b+2)]^(floor(n/3)+1) via disjoint closed boundaries, so P_p(u<->v) is continuous on (0,1); HPS sprinkling (BCRTT v2 Lemma 3.5) then excludes infinite touching. Credit Menard-Senizergues (the equation) and Spakulova (decomposition). Referee: novelty not established; general nonunimodular case open. Archives: 06_math_research/referee_reports/2026-11-13/C0159A (3d4ac79f) and C0159AR. Status: provisional until a paper agent checks priority.

Published 13 Nov 2026 12:3x: github.com/yspennstate/grandparent-graph-cluster-repulsion commit 8c7fb8b3a4f9f61f7278b2dd73c96c6ad68bf632 (7 pp, lint 0 MUST, 12 references checked), Zenodo 10.5281/zenodo.24192744; ResearchGate folder q4/grandparent-graph-cluster-repulsion queued.
