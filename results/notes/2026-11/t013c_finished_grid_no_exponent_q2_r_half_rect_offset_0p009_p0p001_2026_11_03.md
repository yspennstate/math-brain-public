---
name: t013c_finished_grid_no_exponent_q2_r_half_rect_offset_0p009_p0p001_2026_11_03
description: [VERIFIED] T013c finished 136/136 FK runs: square matches 1/(1+sqrt q), no decay exponent identified (40 of 54 on bounds), q=2 r=1/2 rectangle 0.009 below 2^(-1/4) at every L, p 0.001
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T21:21:36+04:00
  evidence: "brain-repo 06_math_research/frontier/rows/T013/m5f_T013c/REVIEW_v2.md commit cde07a4356"
  originSessionId: 5009ea7f-1f15-49f8-b73c-df81dd7f43f3
  status: superseded
superseded_by: t013c_r_half_offset_did_not_replicate_16_fresh_seeds_chi2_2p3_of_3_2026_11_03
---

T013c finished on 3 Nov at 21:15 +04: all 136 FK Monte Carlo runs (96 grid, 40 endpoint; q = 2, 3; r = 1/2, 1, 2; L = 32 to 256) after the runners stopped killing work on distress (fleet rule 9). Total sampler CPU 1,148 s.

What it shows:
- The self-dual square agrees with the exact 1/(1 + sqrt q) at q = 2: chi2 5.1 on 4 dof against 0.41421. C1 is the classical duality identity, not new.
- No finite-size decay exponent is identified. 40 of 54 power-fit exponents sit on the imposed bounds 0.05 or 4, and the other 14 are saturated or rest on 1 to 2 dof.
- The q = 2, r = 1/2 rect_medial rectangle sits below 2^(-1/4) = 0.840896 at every size: -0.0090, +0.0003, -0.0102 and -0.0093 at L = 32, 64, 128, 256. That is chi2 18.2 on 4 dof (p 0.001), and it does not decay. r = 2 gives p 0.04.
- I recomputed the L = 256 point from the raw 0/1 series by batch means. P is 0.83160 in both, the SE is 0.00435 against the analysis's 0.00416, and z is -2.14 against -2.23.
- The raw r = 1/2 disks scatter around 2^(-1/4). So the -0.009 rectangle-minus-disk limit (corrected fit -0.0094 +/- 0.0044) looks like the rectangle's offset, not the disk's. That reading rests on four numbers.

Open: fresh seeds at r = 1/2, L = 128 and 256, and an exact enumeration of the smallest r = 1/2 rect_medial graphs against the formula.

Online: brain-repo 06_math_research/frontier/rows/T013/m5f_T013c/ (commit cde07a4356, 24 new files incl. REVIEW_v2.md and t013c_handcheck.py), moves line f87a2713a6.


Related: [[t013c_selfdual_square_exact_1_over_1_plus_sqrt_q_classical_mc_77_of_96_2026_11_03]] - the same row at 77 of 96 runs; this one finishes it and replaces its C2 reading.
