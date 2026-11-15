---
name: p0034_berw_gpu_numerics_return_prob_do_not_decide_recurrence_2026_11_13
description: "P0034 2D balanced excited walk (Lyons-Peres Q2.27): Mac 2 GPU numerics L=128..2048, p(return before exit) .671->.718; a positive-limit fit (a=0.10) beats a pure power of log, but ln L spans 4.9..7.6 so the numerics do NOT decide recurrence; returns grow ~(ln L)^2; spend no more GPU here"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T16:14:36+02:00
  status: provisional
  evidence: ""
---

The C0132 GPU loop on Mac mini 2 (~/gpu_work/c0132_mc, ew_loop.py + ew_gpu.py, MLX Metal kernel, one walker per thread, bitmap of visited sites, walk censored on leaving a box of side L started at its centre; stopped by its STOP file since 12 Nov) left 84,470 batch rows in summary.jsonl. Nobody had read them. Aggregated 13 Nov by an agent (scratchpad ew_agg.py on the Mac, ew_fit.py here).

Mode 0 is P0034's walk exactly (first visit: horizontal step; revisit: vertical step; Lyons-Peres Q2.27 = 2D balanced excited walk, recurrence conjectured by Angel-Holmes-Ramirez 2023, see [[p0034_is_2d_balanced_excited_walk_open_angel_holmes_ramirez_2026_11_13]]). p = P(return to start before leaving the box), walkers 5.9e9 at L=128 down to 2.3e7 at L=2048, 0 censored:

    L      p_return  (se)       mean returns before exit   E[tau]/L^2
    128    0.67093  (0.00001)   4.314                       0.279
    256    0.68587  (0.00001)   5.499                       0.277
    512    0.69824  (0.00002)   6.853                       0.273
    1024   0.70862  (0.00005)   8.375                       0.269
    2048   0.71779  (0.00009)  10.095                       0.264

P(ever return) is the limit of p as L grows (the box only censors), so recurrence needs p -> 1. Fits of the escape q = 1 - p (chi2 against the binomial se): q = C (ln L)^-beta, limit 0, gives beta 0.345 but chi2 234 on 3 dof; q = a + C (ln L)^-beta gives a = 0.100, beta 0.51, chi2 3.5 on 2 dof; q = a + b/ln L, chi2 2059. So on L = 128..2048 the data PREFER a positive limit (about 10 pct escape, i.e. transience) over a pure power of log, but ln L spans only 4.9..7.6 and a slowly varying correction would reverse that: the numerics do not decide P0034, in either direction. Do not quote them as evidence for or against recurrence.

What the data do say: mean returns before exit grow by 1.19, 1.35, 1.52, 1.72 per doubling of L (2D simple walk: (2/pi) ln 2 = 0.44, constant), i.e. roughly (ln L)^k with k drifting 1.8 -> 2.0 - returns come in clusters (a revisit steps vertically, a fresh site horizontally, so the walk re-crosses its own column). Exit time stays diffusive (E[tau]/L^2 0.26-0.28). Controls: the 3D modes M(1,2) and M(2,1) level off at p = 0.559 and 0.353 by L = 256, as transience (Peres-Popov-Sousi) requires.

**How to apply:** do not spend GPU extending this loop to settle P0034: separating a = 0 from a = 0.1 needs L of order 1e4 and above with se near 5e-4, about 1e13 walker-steps with L^2/8 bytes of bitmap per walker - not a Mac mini job. A proof route, not more numerics, is what P0034 needs; the (ln L)^2 return count is the one numeric fact worth carrying into one. Raw data stay on Mac mini 2 (summary.jsonl, 84,470 rows).

