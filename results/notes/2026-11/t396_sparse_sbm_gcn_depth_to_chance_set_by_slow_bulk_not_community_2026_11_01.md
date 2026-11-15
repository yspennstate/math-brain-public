---
name: t396_sparse_sbm_gcn_depth_to_chance_set_by_slow_bulk_not_community_2026_11_01
description: [PROVISIONAL] T396 target 2 at bounded degree: weight-1 linear GCN stays above chance 20-50 layers even below KS; community-eigenvalue prediction 3-6x short; P's slow bulk (0.86-0.97, rising with N) buries the community mode; own-feature memory ruled out
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T01:10:45+04:00
  status: provisional
  evidence: ""
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

Written 2026-11-01 01:10 +0400; T396 move e0c70609, files 9203ee21 (sbm_*.py/txt). k* about 27-47 (a 8 b 2) and 22-48 (a 5 b 3, below KS) over N 1e3-1e6; the label component decays at 0.84 in both models. Median P^k_ii is 5e-4 at k 20 while accuracy is 0.858, and low-degree nodes are less accurate, so the signal is not own-feature memory. Lesson: under random-walk normalisation at bounded degree, depth-to-chance does not measure detectability, and the equitable-partition eigenvalue is not the decay rate. Next: sym-normalised operator and degree ~ log N. Related: [[t420_ising_rbm_ml_has_no_minimiser_hidden_copies_odd_spin_2026_11_01]] - same session's frontier rounds.

Related: [[t396_gcn_oversmoothing_master_stability_2026_10_30]] - target 1 of the same row (consensus-manifold rate); this is target 2.

Update 2026-11-01 01:13: follow-up moves 189b7d6c (files 1675f30e) and a literature note. Sym normalisation has the same spectrum, so k* is unchanged. At degree ~ log N the community mode separates and k* ~ (1/2) log N / log(1/lambda_2) (14.3/15.5/17.5 predicted vs 16.3/19.0/18.7). The log N / log log N of 2212.10701 is the onset of oversmoothing, not the depth to chance.
