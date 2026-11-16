---
name: t002_square_site_cardy_aligned_and_45deg_within_0p003_2026_11_02
description: T002 square-lattice site percolation: Cardy crossing within 0.003 for aligned and 45-deg rotated rectangles, rotational invariance holds at 0.003
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T09:53:12+04:00
  status: provisional
  evidence: "brain-repo 06_math_research/frontier/rows/T002/moves.jsonl 60c020c9"
---

T002 (square-lattice site percolation scaling limit / SLE6; the claimed proofs are Tsai-Yam-Zhou 1112.2017 and Zhou 2409.03235), first move m002a (moves.jsonl 60c020c9, 2 Nov). Crossing probabilities at p_c 0.59274621 in rectangles of aspect 0.5, 1 and 2, lattice-aligned and rotated 45 degrees, L 32-256, 2e5 samples each, a + b/L fit over L 64-256. All six limits lie within 0.003 of Cardy (0.82435 / 0.5 / 0.17565). Rotated minus aligned is -0.0018, +0.0027 and +0.0001 (each about 0.0015-0.0019 se). So rotational invariance holds at the 0.003 level. That is consistent with the claims, not an audit of their proofs. PREREG104 3/3. Caveats: the rotated runs at L 32-64 are not monotone (jagged boundary), and the r 1 rotated limit sits 2.0 se high. Code: scratchpad t002/cross.c, cardy.py, fit.py (pushed as t002_*; the first pushed fit.py imported 'cardy', which is t002_cardy.py in the row folder, fixed locally for the next push). A finer test needs more samples (se 0.0005 needs about 1e6 per case) or a non-rectangular domain.
Related: the percolation runs of [[t014_d7_percolation_tail_exponent_0p496_mean_field_2026_11_02]] (high-d tails) and [[t001_theta_pc_bounds_d3_0p10_d7_0p004_conditional_2026_11_02]].

Related: [[codex_wave_c0017_conformal_invariance_critical_bond_percolation_2026_10_10]] - the same conformal-invariance question for bond percolation on Z^2.
