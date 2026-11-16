---
name: p0230_sirsn_span_length_poisson_line_case_audited_2026_11_16
description: "[PROVISIONAL] P0230 Aldous SIRSN Open Problem 35 (span of k points has mean length ~ ell k): candidate for the planar Poisson-line SIRSN, every gamma>2 (upper bound audited 6 times, lower bound checked once, more readings asked 16 Nov); general SIRSN still open"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T03:24:18+02:00
  status: provisional
  evidence: ""
---

Upper bound: split span by distance from the square; inside and near parts by Poissonization (E L_k <= E L_N / P(N>=k)); far parts by Hoelder over dyadic annuli with an exit tail q(R) <= C R^-a, a < gamma-1, from the proof of Kahn (AoP 44, 2016) Thm 5.1 recentred at 0 with T* = sup travel time over the unit square (Kahn Thm 3.1), and far-length moments from Kahn Thm 6.1. The tail needed is only R^(-1-eps), which is why every gamma>2 works; a single-scale fast-line count gives only gamma>3. Lower bound: Poissonize down at rate 1-eps, truncated local lengths in bulk cells, monotone convergence in the radius (an agent). Six independent audits of the upper bound. Prior art read 16 Nov: none. Note: brain-repo 12_cognitive_architecture/brain_improvement/agent_run/attempt_P0230_sirsn_length_reduction_2026_11_16.md. Next: paper.
