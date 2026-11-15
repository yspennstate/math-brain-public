---
name: p0434_record_constant_optimum_split_looks_golden_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov: at low load the record-lemma constant is a ratio of finite sums; limit 0.180304 with optimal small split a* -> (3-sqrt5)/2 (0.381965970 at sizes 1e7)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:22:22-05:00
  status: superseded
  superseded_by: p0434_record_constant_is_5_sqrt5_minus_11_2026_11_08
  evidence: "codex_fleet/runs/own_p0434/lin_adigits.out"
---

P0434 (M-SERPT against Gittins), 8 Nov 2026. The record-lemma constant theta (small-class excess over large-class Gittins waiting, see [[p0434_record_lemma_constant_is_0_18_at_equal_large_work_2026_11_08]]) has a clean low-load form: in the SOAP formula 1 - rho_new[c] = 1 - rho E[min(S,c)]/E[S] exactly, so to first order in rho the gaps drop out and theta is a ratio of two finite sums over the law (lin_theta.py reproduces the exact 0.1802989 to seven digits).

In that form, on (1, 1+g, K1, K2) with equal large-class work, size corrections go as 1/K1 and 1/r (tenfold steps shrink them tenfold), the limit is about 0.180304, and the optimal small split is a* = 0.381966: two golden-section brackets ([0.36,0.40] and [0.30,0.47]) and a grid parabola (0.381948) agree. That is (3 - sqrt 5)/2, so the conjecture is that the near twin carries 1/phi of the small mass at the optimum.

Caution: numerical, not derived. A golden-ratio optimum is also what a golden-section search would print if it were stuck on its own bracket, which is why the second bracket and the grid fit were run; both agree. The derivation from the limit sums is the next check.

Evidence: ~/codex_fleet/runs/own_p0434/ lin_theta.out, lin_conv.out, lin_aopt.out, lin_aopt2.out, lin_agrid.out and NOTE.md 06:5x-07:1x; research-repo codex-fleet. lin_adigits.out: a* 0.381965970 at sizes 1e7 against 0.381966011.

