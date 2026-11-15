---
name: p0081_critical_warm_conserved_charges_paper_posted_2026_11_10
description: "[VERIFIED] P0081 critical WARM (alpha=1) / Lima Q1 law of the limit: paper posted 10 Nov 19:2x, public repo yspennstate/graph-urn-conserved-charges (2d3a7e6)"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T19:17:17+02:00
  status: provisional
  evidence: ""
---

Result (proved, 8 pp): for sigma in ker of the unsigned incidence matrix, sum sigma_e H(N_e-1) is an exact martingale; on even C_L, X -> (1+u,1-u,...) a.s. with L artanh(u) = M_inf; sqrt(L) artanh(u) => N(0,c), c = E int dt/(N_-1 N_0) on Z, ~1.64 numerically (mini2 warm2.c, L=100/400). Proof route: Benaim pseudotrajectory + equilibria lemma (boundary blocks transversally unstable, rate >= 1/(2L)) + charge pins the point; CLT via Harris locality + uniform tail (coupling with a local comparison process, Yule rate 1/2 from sqrt t). Z (Kleptsyn Conj 2 in Aletti et al.) only formal: envelope PDE v_tau = (tanh v)''/4, sd ~ (log t)^(-1/4), numerics consistent but fitted exponent -0.18. Small graphs: C4 limit not Beta (b~1.72), K4 random on 2-dim set. Literature checked 10 Nov (Chen-Lucas ECP 2014, Lima 2016, Dahiya-Sahasrabudhe, Kaur-Sahasrabudhe): no charge identity found. Push guard demanded the declaration sections (model: bilateral-preference-connectivity-window paper/main.tex). Working files: agent_run/p0081 (NOTES.md, paper/charges.tex + sec5.tex). Open: row in math-brain-public papers/README, ResearchGate. What would change it: a referee finding a gap in the type-(2) exclusion step of Thm conv (sketched via the growth comparison).
