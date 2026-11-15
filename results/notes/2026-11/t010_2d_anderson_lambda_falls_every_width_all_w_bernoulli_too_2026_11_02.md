---
name: t010_2d_anderson_lambda_falls_every_width_all_w_bernoulli_too_2026_11_02
description: T010 2D Anderson strip transfer matrix E 0, M 4-32: Lambda_M falls every width step for uniform W 4-12 and matched-variance Bernoulli; Bernoulli 1.5-2.6x more localized at band centre (between sub-bands)
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T07:37:06+04:00
  status: provisional
  evidence: "rows/T010/moves.jsonl 88db84a7"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T010 (2D Anderson localization in the bulk at every disorder strength, Bernoulli included), first frontier move, 2 Nov 2026, an agent. Move m010a, rows/T010/moves.jsonl 88db84a7; t010_tm.c and t010_table.py are in 06_math_research/frontier/rows/T010.

- Setup: strip transfer matrix at E 0, widths 4-32.
- Lambda_M = lambda_M / M falls at every width step for uniform W 4-12. W 4 goes 1.97 -> 1.47 (M 8 -> 32). No extended phase appears.
- Bernoulli of matched variance also falls, but is 1.5-2.6x more localized at the band centre. E 0 lies between its sub-bands at +-W_b/2.
  - This is why PREREG89 (c) MISSED: matching variance only matches Born-order perturbation theory, not W >= 6.
  - Next time, compare at matched Lyapunov exponent or use small W.
- Cost: under a minute for the whole scan (M 32, 2e6 slices, about 9 s).
- Larger M is cheap: M 64 is 8x the cost per slice. It would test W 4, where the localization length (more than 47) is still above M.
- Related: [[t007_wolff_fixed_cluster_count_xi_matches_alles_2026_11_02]] (a lesson from the same day: check absolute values against a published table).

