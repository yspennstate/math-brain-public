---
name: t306_gaussian_and_product_laws_need_sqrt_d_over_eps_steps_2026_11_01
description: T306 diffusion steps: Gaussian and product laws tensorise, first-order EI samplers need sqrt(d)/eps (p 1.87-1.97); beating sqrt(d) needs correlated families or score error
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T17:11:54+04:00
  status: provisional
  evidence: "frontier/rows/T306 moves m306a a1533060, m306b bf77ee45"
---

T306 (optimal step count of diffusion samplers on well-conditioned laws; known bounds Omega~(sqrt d) queries (2604.10857) against O~(d) steps (2308.03686)).

Measured 1 Nov, moves m306a (a1533060) and m306b (bf77ee45):
- Gaussian targets with the exact score: the exponential-integrator DDPM and flow-ODE samplers keep Gaussians Gaussian. KL = d kl(N) is exact, with kl ~ N^-p, p = 1.945 for the ODE and about 1.87 for DDPM (local slope at 512 -> 1024 was 1.74, outside the pre-registered band). So N ~ sqrt(d)/eps.
- Product laws in general: OU marginals stay products and the exact score is separable, so KL tensorises to d kl1(N), and an order-r scheme needs d^(1/(2r))/eps^(1/r) steps. Checked with a variance-1 bimodal coordinate law: p 1.90-1.97.
- Consequence: a well-conditioned lower bound above sqrt(d) needs a correlated, non-product family (like Xun-Price's planted codebook) or score error.

Scars from the runs:
- Tuning one schedule to a single Gaussian mode lets the start error cancel the discretisation error (kl 1e-14), which is meaningless. Use a spread of modes that share one schedule.
- A "quadrature check" run at a large finite N measures discretisation, not the quadrature floor.


Related (linked 3 Nov by an agent, W22): the lower-bound hard families for the same row, [[diffusion_and_gmm_lower_bound_hard_families_conditioning_t306_t309_2026_10_18]].
