---
name: p0107_critical_fpp_z3_log_n_open_needs_theta_pc_zero_2026_11_13
description: "[PROVISIONAL] P0107 critical Bernoulli FPP in Z^3 (ADH Q19): E T(0,dB(n)) ~ log n open; any growth at all implies theta(p_c)=0 in d=3, itself open"
metadata:
  type: project
status: provisional
---
P0107 (200 list rank 13; Auffinger-Damron-Hanson "50 years of FPP", Question 19, arXiv 1511.03262 p.71): edge times 0 with
probability p_c(Z^3), 1 otherwise; is E T(0, boundary B(n)) comparable to log n?

Status 13 Nov 2026: OPEN. Two extended web searches found no paper on critical FPP in d >= 3. What exists is planar:
Chayes-Chayes-Durrett (log n growth for 2D critical Bernoulli), Damron-Lam-Wang arXiv 1505.07544 (2D asymptotics),
Jiang-Yao arXiv 1612.01803 and Yao arXiv 1310.1247 (triangular lattice, explicit constants). High-dimensional FPP papers
(Auffinger-Tang 1601.07898, revisited 2501.11589; Alexander 2304.08669) are about the time constant or fluctuations, not p_c.

Why it is hard: T(0, boundary B(n)) is the fewest closed edges a path to distance n must cross. If there were an infinite
open cluster at p_c, T would stay bounded with positive probability, so any proof that E T -> infinity in Z^3 also gives
theta(p_c) = 0 in three dimensions, a well-known open problem. The upper bound side (E T <= C log n) needs 3D replacements for
RSW crossing estimates, which are not available either. In high dimensions (lace expansion, d >= 11) theta(p_c) = 0 and the
Kozma-Nachmias one-arm bound P(0 <-> boundary B(r)) ~ r^-2 are known, so the high-d version may be tractable. That would be
the route to try, not d = 3.

How to apply: skip P0107 as a solve target. If revisited, aim at the high-dimensional analogue and say plainly that d = 3
contains theta(p_c(Z^3)) = 0. What would change this: a d >= 3 critical FPP paper, which these searches missed.
Related: [[p0098_strict_fpp_comparison_large_atom_d_ge_3_open_marchand_d2_2026_11_13]].
