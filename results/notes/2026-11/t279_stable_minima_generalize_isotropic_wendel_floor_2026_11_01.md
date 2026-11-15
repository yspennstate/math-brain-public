---
name: t279_stable_minima_generalize_isotropic_wendel_floor_2026_11_01
description: [PROVISIONAL] T279: 2305.17490 already proves linearly stable SGD minima of 2-layer ReLU generalize on isotropic data (n >~ d log n); below n = 2d dead neurons break it with Wendel probability
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T21:38:17+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T279 (an invariant flatness measure that bounds test error at SGD minima), 1 Nov. I read the TeX of Wu, Wang and Su (arXiv:2305.17490, ICML 2023). Their setting is a two-layer ReLU network with inputs uniform on sqrt(d) S^(d-1). Linear stability gives tr G <= 2/eta. For n >~ d log n, tr G ~ sum(|w|^2 + d a^2), which is at least 2 sqrt(d) times the path norm, and the risk of a stable SGD minimum is <~ log^3 n/(eta^2 n). That is the row, solved for isotropic data. The dossier's targets 1 and 2 are covered without label noise.

What I added is the necessity side. If the data lie in a halfspace through 0, a dead neuron c relu(u.x) leaves the loss, the Hessian and the stability untouched and makes the test risk arbitrary. Wendel gives the probability: 1 for n <= d, 1/2 at n = 2d (an LP check gave 0.497). The worst-direction constant measured at d = 20 is about 0 at 2d, 0.1 at 4d and 0.35 at 32d (the population value is 0.5). Open: anisotropic or low-dimensional data.

Pushed: research-repo research_pushes/2026-11-01-loop-T279-stable-minima (e10286e); card claim_8eb7a635777d445fa07d0a235573b895 (3 links); frontier move on T279.

Related: [[t391_diffusion_manifold_rate_is_already_proved_for_atlas_erm_2026_10_31]]. This is the third row in two days where reading the newest paper's TeX showed the dossier's open target already proved, so read the source before building. [[t330_radial_depth2_exponent_drops_from_9_to_1_2026_10_31]] is the same depth-2 ReLU class.
