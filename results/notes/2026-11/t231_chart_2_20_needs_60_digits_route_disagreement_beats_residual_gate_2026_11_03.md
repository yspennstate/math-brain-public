---
name: t231_chart_2_20_needs_60_digits_route_disagreement_beats_residual_gate_2026_11_03
description: T231 reference chart 2^-20 read E3 (h^2 model failing) at dps 40; it was precision: newborn eigenvalue ~1.6e-30 vs 40 digits and a 1e-30 floor. At dps 60 the h^2 model holds to 5e-6. Judge sample accuracy by route-1 vs print disagreement, not the LSQ residual
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T02:32:37+02:00
  status: verified
  evidence: "06_math_research/frontier/rows/T231/campaign_s231a/STAGE53.md 53.23z-c; landed 6a10c7e7"
---

Stage 53.23z-c (3 Nov 2026, an agent). A new chart point 2^-20 for the T231 reference line 5301/0 read E3 by its prereg at the default dps 40 (u20 5.091263, step ratio 16/18/20 15.70, L 5.089272). The prereg gate on the route-1 LSQ residual (3e-9) passed at 7.6e-10, yet route 1 and the printed Q disagreed by 1.2e-4 (1.1e-6 on 2^-18). Cause: probe52k.py runs mpmath dps 40 with a newborn eigenvalue floor 1e-30, and at chart 2^-20 with eta 2^-24 the eigenvalue mu = m_0 lam is ~1.6e-30; each chart step loses ~256x relative accuracy. Rerun with DPS=60 TOLE=50 (m0fac53p.py): u20 5.091830, ratio 16.0026, L 5.089877 (E1); the 40-digit control is byte-identical to the first run. Lessons: (1) any chart 2^-20 or finer work in this probe needs dps >= 60; (2) a fit residual under-measures the error of the extracted quantity, so gate on the disagreement of two extraction routes; (3) a failed prediction with a visible accuracy warning gets an addendum-preregistered decider, not a landed failure. The 2^-18 rows carry ~2e-6 of the same term, under the 0.0003 bar. T231 not solved.
