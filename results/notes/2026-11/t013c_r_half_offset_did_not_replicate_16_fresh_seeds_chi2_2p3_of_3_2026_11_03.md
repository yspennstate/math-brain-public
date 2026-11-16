---
name: t013c_r_half_offset_did_not_replicate_16_fresh_seeds_chi2_2p3_of_3_2026_11_03
description: [VERIFIED] T013c q=2 r=1/2 rectangle offset (p 0.001 on the grid) did not replicate: 16 fresh seeds at L=128/256/512 give chi2 2.3 on 3 dof vs 2^(-1/4); C1 holds, C2 partial (no exponent)
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T21:35:21+04:00
  status: provisional
  evidence: "brain-repo 06_math_research/frontier/rows/T013/m5f_T013c/REVIEW_v2_reseed.md commit 6c0ab4752f"
---

Correction to [[t013c_finished_grid_no_exponent_q2_r_half_rect_offset_0p009_p0p001_2026_11_03]], measured on 3 Nov between 21:2x and 21:33 +04.

The q = 2, r = 1/2 rect_medial rectangle offset of about -0.009 from 2^(-1/4) does not replicate. On the finished T013c grid it was chi2 18.2 on 4 dof, p 0.001. I reran it with 16 fresh seeds picked before looking (fk_alt, 20,000 sweeps after 2,000 burn-in, nice 15, batch-means SEs). Against the exact value:
- L = 128: -0.0009 +/- 0.0027 (4 seeds)
- L = 256: -0.0028 +/- 0.0020 (8 seeds)
- L = 512: +0.0013 +/- 0.0028 (4 seeds)

Together that is chi2 2.3 on 3 dof. The grid's offset was low draws at L = 32, 128 and 256, read with SEs that the grid's own validation shows can run 25 % small.

Still true: the self-dual square matches 1/(1 + sqrt q) (C1, classical). No decay exponent is identified (C2 partial). The r = 1/2 rectangle-minus-disk gap and the guess that the rectangle carries it are withdrawn.

Lesson: a p = 0.001 offset in one Monte Carlo grid, read with a single SE estimator, earned a fresh-seed rerun before it went into a memory as a finding. The rerun cost 5 CPU minutes, and I filed the claim 15 minutes before running it.

Online: brain-repo 06_math_research/frontier/rows/T013/m5f_T013c/REVIEW_v2_reseed.md and reseed_r_half/ (commit 6c0ab4752f), moves line da6c4227f5.

