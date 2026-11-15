---
name: t405_switch_smoothing_off_at_escape_2026_11_01
description: [PROVISIONAL] T405: after the smoothed escape, plain SGD at step k/d finishes in 16-31 d/k steps; kept smoothing ~2000 d^1.5 (4.7x slower at d=64), slow not stuck
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T07:32:15+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



This follows [[t405_smoothing_gets_d2_slope_2p2_vs_3p2_2026_11_01]]. Pushed 55a3a7c, research_pushes/2026-11-01-loop-T405-anneal; frontier move 2e9883c6.

Set-up: one-unit online SGD on the spiked cumulant model. Smoothing is lam = d^(1/4) with eta = 0.025/sqrt d until |m| = 0.5, then one of three arms. The arms share seeds, 16 runs per cell, at d = 16, 32, 64.

Steps from escape to |m| = 0.95:

| d | kept smoothing | plain step 0.01/d | plain step 0.003/d | escape |
|---|---|---|---|---|
| 16 | 130,500 (1 row) | 37,900 | 82,900 | 42,100 |
| 32 | 385,600 (5 rows) | 87,000 | 177,050 | 192,400 |
| 64 | 919,400 (15 of 15) | 196,500 | 380,900 | 625,600 |

- Kept smoothing ends at final |m| 0.853, 0.910, 0.940. The plain arms end at 0.95-0.99.
- A plain step of 0.1/d loses the signal: final |m| 0.22 at d = 16, because E|G|^2 is about 4d.

**My error, corrected in the note before pushing:** from d = 16 and 32 I first wrote "keeping the smoothing stalls". Those medians were censored. At d = 64 every row got there, at about 2,000 d^1.5.

**Second error, also corrected before pushing:** I first put the crossover with the escape "well above d = 1000". sqrt(d) ln d = 54 puts it near d = 128.

**Why:** the d^2 claim for smoothing covers the whole run only with the smoothing switched off at escape.

**How to apply:** do not call a slow arm "stuck" from censored medians. Wait for a size where every row finishes, or report the censoring.
