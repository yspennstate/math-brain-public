---
name: t286_degree2_ridge_bound_vs_universal_phase_2026_11_01
description: [PROVISIONAL] T286: universal phase = 2408.03733 with noise sum mu_k^2 (k>=3) is already in 2501.18530/2505.24849; degree-2 ridge gives activation-free bound E=(delta+E)/(delta+E+2 alpha)
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T22:15:26+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T286, 1 Nov. Target 2 is settled at the physics level by Barbier et al. (2501.18530, and the follow-up 2505.24849). Their universal branch is the 2408.03733 quadratic formula with noise g(1) = sum_{k>=3} mu_k^2. Specialization with Gaussian weights needs Hermite content above degree 2.

For target 1 I proved half, with ridge in place of GAMP-RIE. Optimal ridge on the d^2/2 orthonormal degree-2 Hermite features has excess error P_2 E, with E = (delta + E)/(delta + E + 2 alpha) and delta = noise / degree-2 power. It holds for any activation and is rigorous via 2204.10425 / 2205.06798, conditional on their target conditions, which I have not checked. Against 2408.03733 Result 1, computed with the subordination cubic: at alpha = 0.2 and delta = 0, ridge gives 0.600 and RIE gives 0.127, 0.392, 0.500 and 0.551 at kappa = 0.25, 0.5, 1 and 2.

Correction: the note's first title said "up to a factor 5". The table gives 1.9 to 3.8 at kappa = 0.25, delta = 0.1, and an unbounded ratio at delta = 0. I fixed it in place (965a057). A magnitude check in the audit caught it after the first push.

Pushed: research_pushes/2026-11-01-loop-T286-degree2-bound (15c6e4d, then 965a057); card claim_34c9c058abff4ccd8c27267ffb5778bf (3 links, one to the T285 card); frontier move on T286.

Related: [[t285_committee_amp_specializes_at_3p27_k_squared_2026_11_01]] is the fixed-K side of the same specialization question.
