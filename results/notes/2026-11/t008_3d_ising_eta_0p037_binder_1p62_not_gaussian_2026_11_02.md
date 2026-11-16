---
name: t008_3d_ising_eta_0p037_binder_1p62_not_gaussian_2026_11_02
description: T008 3D Ising Wolff at K_c, L 8-64: eta 0.0373 +- 0.0053 with omega 0.83 correction (bootstrap 0.0363); Binder Q 1.55 -> 1.62 toward 1.604, far from Gaussian 3
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T07:42:56+04:00
  status: provisional
  evidence: "rows/T008/moves.jsonl 0f565f3f"
---

T008 (3D Ising at criticality: eta > 0 and a non-Gaussian scaling limit), first frontier move, 2 Nov 2026, an agent. Move m008a, rows/T008/moves.jsonl 0f565f3f; t008_ising3d.c and t008_fit.py are in 06_math_research/frontier/rows/T008.

- Setup: Wolff at K_c 0.22165463, L 8-64, about 6 minutes in all.
- eta: 0.0373 +- 0.0053 with a fixed omega 0.83 correction, against 0.0363 from the bootstrap. A pure power over L 16-64 gives 0.026 +- 0.009.
- Binder Q rises 1.548 -> 1.620, toward 1.604, far from the Gaussian 3.
- PREREG90: 3 of 4 passed. (d) monotone Q MISSED, inside the errors.
- Built on the measure-after-fixed-cluster-count lesson of [[t007_wolff_fixed_cluster_count_xi_matches_alles_2026_11_02]].
  - Checked the improved estimator (mean cluster = chi) and the high-temperature series before the critical runs.
- More precision would need about 4x the sweeps at L 48-64: chi se 1.5% gives eta +- 0.005.


Correction (3 Nov, an agent review): the +- 0.0053 is conditional on the grid-searched correction amplitude b held fixed. A joint fit of A, eta and b gives 0.0371 +- 0.0201, so eta > 0 holds at about 1.8 se, not 7. The Binder ratio result (3 - Q about 1.4) stands. See [[grid_searched_nuisance_held_fixed_error_4x_small_t008_eta_7se_was_1p8_2026_11_03]].
