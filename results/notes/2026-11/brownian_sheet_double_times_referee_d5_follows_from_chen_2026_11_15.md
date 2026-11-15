---
name: brownian_sheet_double_times_referee_d5_follows_from_chen_2026_11_15
description: "[PROVISIONAL] Brownian sheet slice double times (Kho05 OP2) paper refereed 15 Nov: MINOR, proofs sound; d=5 already follows from K. Chen's EPFL thesis finiteness, so the new case is d=4; v1.1 bdb32915 says so"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T00:26:01+02:00
  status: provisional
  evidence: ""
---

Posted paper yspennstate/brownian-sheet-slice-double-times, Theorem: for d in {4,5}, a.s. for all s>0, dim_H of the off-diagonal double times of the slice is 0, and upper box dim is 0 on products of disjoint compact intervals. Independent Codex referee (gpt-6.1-sol, Mac 1, 15 Nov 01:3x-01:5x Tbilisi): lem:smallball, lem:moments, lem:holder and both parts of the proof SOUND; lem:var MINOR (Gaussian projection wording, independence is for centred bridge residuals); lem:lattice MINOR (anchor sets must be nonempty); novelty MINOR: Chen thesis Thm 1.3.3 (finiteness for d=5, every s) gives both parts for d=5. Chen (4.42) treats V(y)-U(x) as a Brownian sheet; its covariance s(min(x,x')+min(y,y')) is a sum, so that step fails, but the referee sketched an independent covering proof that d=5 slices have at most two unordered double pairs (exponents 10a-4, 15a-7). Also: Kho05 is arXiv math/0510518 (not 0511054); its (5.1) and (8.2) omit the distinct-time restriction too. Fixed in v1.1 (bdb32915), with the 23:34 credit sentence in the AI declaration. Report: 06_math_research/referee_reports/2026-11-15/BSSDR_posted_referee/REPORT.md. What would change it: a second audit of the d=4 moment bound by another referee.
