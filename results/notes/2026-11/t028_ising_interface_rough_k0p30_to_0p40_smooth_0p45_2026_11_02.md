---
name: t028_ising_interface_rough_k0p30_to_0p40_smooth_0p45_2026_11_02
description: T028 3D Ising interface, Metropolis L 8-64: lowest-mode stiffness Q = 1/sigma_eff flat at L 32-64 for K 0.30/0.35/0.40 (2.37, 1.40, 0.763 > 2/pi), falls ~3x per doubling at K 0.45/0.50; roughening between 0.40 and 0.45; PREREG94 4/4
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T08:04:20+04:00
  status: provisional
  evidence: "rows/T028/moves.jsonl 13aeef31"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T028 (rough phase of the 3D Ising interface between K_c and K_R), first frontier move, 2 Nov 2026, an agent. m028a is in rows/T028/moves.jsonl (13aeef31); the code is t028_iface.c in 06_math_research/frontier/rows/T028.

- Setup: an L x L x 32 box with fixed +/- walls, periodic in x and y, Metropolis. Q = 4 pi^2 <|h_kmin|^2> = 1/sigma_eff(L).
- At L 32 -> 64, Q levels at 2.46/2.37 (K 0.30), 1.40/1.40 (0.35) and 0.763/0.763 (0.40): rough, and above the 2/pi KT value.
- Q falls about 3x per doubling at K 0.45 (0.123 -> 0.041) and K 0.50: smooth. So the roughening point lies between 0.40 and 0.45, consistent with the literature K_R about 0.4075.
- PREREG94 4/4. This confirms the expected picture numerically, not by proof.
- Method note: the lowest Fourier mode of the column heights is a clean rough/smooth test at modest L. Small-L bubble noise inflates Q like L^-2, so judge from the top two sizes.
- Related: [[t014_d7_percolation_tail_exponent_0p496_mean_field_2026_11_02]], [[t008_3d_ising_eta_0p037_binder_1p62_not_gaussian_2026_11_02]].

