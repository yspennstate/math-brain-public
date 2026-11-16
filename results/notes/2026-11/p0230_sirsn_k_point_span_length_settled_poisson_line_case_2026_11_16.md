---
name: p0230_sirsn_k_point_span_length_settled_poisson_line_case_2026_11_16
description: "Aldous Open Problem 35 (length of the SIRSN span of k points, E L_k/k -> ell): settled for the planar Poisson-line SIRSN, every gamma > 2 (audited candidate, 16 Nov); upper via Kahn 6.1 + exit tail adapted from Kahn 5.1's proof, lower for any SIRSN by truncated local lengths"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T03:59:47+02:00
  status: provisional
  evidence: ""
---

Aldous's Open Problem 35 (SIRSN paper): is E L_k / k -> ell, where L_k is the length of the span of k uniform points in a square of area k? Settled for the planar Poisson-line SIRSN (Kendall's construction), every gamma > 2, by an agent (upper bound) and an agent (lower bound), 16 Nov 2026 01:xx-03:5x. Status: audited candidate, not yet a paper.

- Upper bound: Poissonize at rate 1+eps; near part by scale invariance; far annuli by Hoelder with Kahn Thm 6.1 (exponential moment of the long-distance length in B(0,1/3)) and an exit tail q(R) <= C R^(-a), a < gamma - 1. Summable iff gamma > 2 = d.
- The exit tail is NOT Kahn Thm 5.1 as stated (that is E L_xy < inf for a fixed pair). It comes from Kahn's proof (15)-(22), pp. 25-27 of arXiv 1503.03976, with T_xy -> T* (time diameter of the unit square, Thm 3.1) and B(x,r) -> B(0,r+1). A write-up states it as a lemma with that proof.
- Lower bound (any SIRSN with ell < inf): Poissonize down at rate 1-eps, disjoint bulk unit cells, truncate local lengths at M (the repair by agent: no moment of L_N needed), span monotone in the point set, h(D) increases to ell_(1-eps) by monotone convergence; order of limits k, then M, D, eps.
- Kahn's Thms 3.1, 5.1 (proof), 6.1 read against the arXiv text 16 Nov 03:4x; coupling of our points into Xi_2 by thinning is allowed.
- Prior art read 03:24 (Kendall 1403.1156, Kahn, Blanc 2207.03349, Blanc-Curien-Kahn 2407.07887, Aldous-Kendall 2008): nothing on k-point spans.
- Still owed: the paper (agent writes it; CREDITS first), and the AOP typeset text of Kahn if a referee asks.

Files: the working record is public at results/referee-reports/2026-11-16/P0230_sirsn_span_length/.

Lesson: a cited theorem that states a mean for a fixed pair does not give a uniform tail over all pairs; read the proof and restate the lemma you actually use.

