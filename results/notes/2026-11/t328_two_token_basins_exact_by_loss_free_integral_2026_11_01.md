---
name: t328_two_token_basins_exact_by_loss_free_integral_2026_11_01
description: [VERIFIED] T328: two-token attention model f=v[a+b tanh kp]; gradient flow of any decreasing loss conserves H=v^2/2-F(p), so the worse-token basin is explicit; 18-47% of N(0,1) inits
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T03:31:49+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T328 (1 Nov, an agent). Pushed f036d6c, research_pushes/2026-11-01-loop-T328-two-token-basins. Card claim_0ea3ebf8e8974a418931babda1fbe108, with 3 links: stable manifold theorem, max-margin gradient flow, GD logistic implicit bias. Frontier move 0ccc55fe.

The trick to reuse: when a single-example model's gradient is -l'(f) times a loss-free vector field, the loss factor cancels in the orbit equation. Every decreasing loss then has the same orbits, and a first integral often comes from separating variables. Here H = v^2/2 - F(p) with F' = h(p) cosh^2(kp)/(bk). This fails for n >= 2 examples, where each example carries its own -l'(f_i).

Numbers: exact P_sub against RK4 flow (20,000 inits per cell) agrees within 2 s.e. in all 14 cells. The linear separatrix runs low by up to 0.03 at a/b = 0.9. GD at eta = 1/(bk) sits 0 to 0.006 below the flow share.

Related: [[t325_l6_step_minima_are_strict_not_stalls_2026_11_01]].
