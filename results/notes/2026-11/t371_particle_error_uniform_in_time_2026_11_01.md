---
name: t371_particle_error_uniform_in_time_2026_11_01
description: [VERIFIED] T371 t2: mean-field policy gradient N-particle error <= L_z eps_N/beta uniformly in time, eps_N ~ sqrt(log|S||A|/N); 2-state MDP sqrt N x err 0.7-1.1 flat t 5-20
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T04:31:54+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T371 target 2 (1 Nov, an agent). Pushed 4914e80, research_pushes/2026-11-01-loop-T371-particles. Card claim_fb7377d074a64d19b8f63ae56c6e6787, with 3 links, one to the target 1 card claim_48b8b2e6. Frontier move 6721b324.

Reusable: when a mean-field drift depends on the measure only through finitely many integrals (here K = |S||A| policy logits), the fluctuation term in the synchronous coupling is a maximum of K sub-Gaussian averages. That makes the particle error dimension-free in theta, at rate sqrt(log K / N). A dissipative prior with beta > 0 then makes it uniform in time.

Numerics show the same behaviour well below the paper's threshold, at sigma = 0.5. The proof does not cover that case.

Related: [[t378_kappa_is_path_norm_plus_init_term_2026_11_01]].
