---
name: t325_l6_step_minima_are_strict_not_stalls_2026_11_01
description: [VERIFIED] T325: L=6 noisy real-step GD landscape has 3 strict local minima per q (Hessian PD); global gets 38-45% of starts
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T03:02:58+04:00
  status: provisional
  evidence: ""
---



T325 (1 Nov, an agent). Pushed 06b0a74, with a range fix in 9b0063f; card claim_8e61d23d87244730acca88ee4775f4a2.

Result: the 16 Oct L = 6 end values are genuine minima. The gradient is 1e-18 and the analytic Hessian is positive definite. The minima are coincident-step patterns (4+2, 6, 2+4). The fourth value, 0.0795123, was an L-BFGS stall.

Method worth reusing: before calling optimizer end values "minima", polish them with Newton steps on an analytic Hessian. One of four 16 Oct values was a stall.

Related: [[t298_escape_rate_width_free_digamma_offset_2026_11_01]].

Folder: research-repo research_pushes/2026-11-01-loop-T325-l6-minima
