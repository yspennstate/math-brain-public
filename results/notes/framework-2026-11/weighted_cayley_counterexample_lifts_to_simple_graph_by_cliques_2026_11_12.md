---
name: weighted_cayley_counterexample_lifts_to_simple_graph_by_cliques_2026_11_12
description: "Weighted Cayley counterexample to a heat-ratio property: does it transfer to an unweighted simple graph? Yes, blow each vertex up into a clique (Gamma x Z_N); ratios converge"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T18:20:10+02:00
  status: provisional
  evidence: "06_math_research/referee_reports/2026-11-12/ARC/REPORT.md section 8"
---

A weighted Cayley-graph counterexample to a heat-kernel ratio property transfers to a SIMPLE Cayley graph by blowing each vertex up into a clique. Found by the Codex referee of arc-transitive-edge-heat (24dd5c6), 12 Nov 2026, REPORT.md section 8.

Construction: Cayley graph on Gamma with inverse-closed S and weights m_s (make them rational by perturbation, then even integers by rescaling time). Take Gamma x Z_N, N > 1 + max m_s, generators {(e,j): j != 0} together with {(s,j): j in +-1..+-(m_s/2)}. Each fibre {g} x Z_N is a clique; the graph is simple, connected and vertex-transitive.

Why it works: the unnormalised Laplacian B_N restricted to fibre-constant functions is exactly the weighted Laplacian B, and on the orthogonal complement B_N >= N I (the clique part). So e^{-tau B_N}((g,i),(h,j)) = (1/N) e^{-tau B}(g,h) + O(e^{-N tau}), and any ratio of heat-kernel entries converges to the weighted one. A strict inequality at fixed times survives for large N, on a pair that is a real edge ((e,0) and (s_0,1)).

Use: whenever a paper says "the weighted example does not settle the unweighted question", check this lift first. It does not touch arc-transitive or 1-walk-regular graphs (the lift is not arc-transitive). Conditional in that paper on the weighted Regev-Shinkar example failing across an edge, which the referee could not check offline.

Related trap from the same report: "symmetric chain" read as a symmetric transition matrix does not give P^2(x,x) >= P^2(x,y): M = [[3/10,3/10,2/5],[3/10,1/5,1/2],[2/5,1/2,1/10]] has M^2(0,0) = 17/50 < 7/20 = M^2(0,1). The inequality needs equal diagonal entries (vertex-transitivity).

Report archived at the private repository, 06_math_research/referee_reports/2026-11-12/ARC/; corrections sent to an agent.

