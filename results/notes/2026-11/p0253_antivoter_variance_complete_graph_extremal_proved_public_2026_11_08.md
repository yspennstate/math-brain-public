---
name: p0253_antivoter_variance_complete_graph_extremal_proved_public_2026_11_08
description: "[VERIFIED] P0253 Aldous-Fill antivoter: complete graph maximizes Var S among regular graphs, Var S <= n(n-2)/(2n-3) via Sylvester integral + resolvent diagonal; public repo antivoter-variance-complete-graph"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T00:06:50+02:00
  status: provisional
  evidence: ""
---

P0253 (Aldous-Fill, Reversible Markov Chains, Section 14.4.2: is the antivoter stationary variance maximized by the
complete graph among regular graphs?) is SOLVED and public: for every connected non-bipartite d-regular graph on n >= 3
vertices and every stationary distribution, Var S <= n(n-2)/(2n-3), equality only for K_n.

Proof in four lines: (1) the pair correlations solve QC+CQ=D, Q=I+P, D=diag(delta), delta_v = 2(1 + mean neighbour
correlation) >= 0, and Var S = (1/4) sum delta. (2) C = int e^{-tQ} D e^{-tQ} dt; c(v,v)=1 summed over v gives
sum_u delta_u (Q^{-1})_uu = 2n. (3) Split e_u = 1/n + b and apply Cauchy-Schwarz to b: (Q^{-1})_uu >= 1/(2n) +
(n-1)^2/(n(n-2)) = (2n-3)/(2(n-2)), with equality iff u is adjacent to every other vertex. (4) Combine. The trivial bound
(Q^{-1})_uu >= 1/Q_uu = 1 gives Aldous-Fill's Var S <= n/2; splitting off the constant vector is the sharpening they
guessed at. Bonus: on vertex-transitive graphs Var S = n^2/(2 sum_i 1/(1+lambda_i)) (Petersen 40/13, C7 1).

Reusable method: a stationary pair-correlation system of a linear spin dynamics is a Sylvester equation; integrate it
out and the diagonal constraint turns the question into the diagonal of a resolvent, where Cauchy-Schwarz off the top
eigenvector is sharp.

Public: yspennstate/antivoter-variance-complete-graph 74e8a8bad9b9eaf8beff84a517786ce17a4ac050 (5 pp, 0 Overfull,
paper_release_guard ok, scan clean by file); ledger open-problems-repo master 4dee342e1b516b5bcc08133632bc8b07a6ef5734
[skip ci]. Checks: all admissible regular graphs n <= 7, 297 random regular graphs n = 5..14, 8 vertex-transitive graphs.
Prior work: Aldous-Fill state it open; no solution found. An outside audit is owed. Working files papers_agent/P0253/.
Related: [[p0341_ansatz20_fails_beyond_root_term_log_decay_window_2026_11_07]].


8 Nov 00:3x second route (P0253/audit_sim.py, .out): direct simulation of the antivoter dynamics, 4000 chains, no correlation equations, matches the closed forms to within 1 se on K5, K7, Petersen (3.0771 vs 3.0769), C7 (1.0000) and circulant(9,{1,3}) (3.0246 vs 3.0237). An outside audit is still owed.
