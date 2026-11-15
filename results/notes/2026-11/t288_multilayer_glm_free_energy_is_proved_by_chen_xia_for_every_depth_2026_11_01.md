---
name: t288_multilayer_glm_free_energy_is_proved_by_chen_xia_for_every_depth_2026_11_01
description: [PROVISIONAL] T288: depth-L multilayer GLM free energy (Gaussian weights, every fixed L) is already in Chen-Xia 2108.12615 under bounded C^(2^l) activations; left are ReLU, MMSE(X), ML-AMP optimality
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T22:32:02+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T288, 1 Nov. The row asked for a proof of the replica-symmetric mutual information of the depth-L multilayer GLM, for L >= 3, with Gaussian weights. Its dossier cites only 1701.06981 and 1805.09785, where L = 2 is proved. Chen and Xia (arXiv:2108.12615, TeX read) already prove it for every fixed L. They work by induction on depth: the (L-1)-layer free energy is the initial condition of a Hamilton-Jacobi equation whose weak solution is the L-layer one. They assume an iid signal in [-1,1] and bounded activations that are C^(2^l). They never compare with the replica formula. Eliminating their bilinear z-coupling, which is stationary at value -alpha y1 y2/2, gives the multilayer RS potential in structure. The signs against 1701.06981 are not fully checked.

What is left: (a) ReLU and other unbounded activations, via truncation plus L^2-continuity of the free energy in the activation; (b) the MMSE of the input, via a side channel that shifts Psi_0; (c) ML-AMP optimality, via graph-AMP state evolution 2109.11905 plus selection of the critical point.

Pushed: research_pushes/2026-11-01-loop-T288-chen-xia-close (0a1f2ea); card claim_155d9344d7da4bae9b456e06060ac545 with 3 links (Hopf-Lax semigroup, AMP state evolution, the T285 committee card); frontier move on T288.

Lesson: the row was a literature gap. One arXiv search on the row's own model name found the closing paper. Search for the row's model name before building anything.

Related: [[t285_committee_amp_specializes_at_3p27_k_squared_2026_11_01]] (the same AMP fixed-point selection question). [[t391_diffusion_manifold_rate_is_already_proved_for_atlas_erm_2026_10_31]] and [[t279_stable_minima_generalize_isotropic_wendel_floor_2026_11_01]] were also rows already proved in a paper the dossier missed.
