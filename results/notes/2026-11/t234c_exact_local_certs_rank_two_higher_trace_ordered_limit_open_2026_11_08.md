---
name: t234c_exact_local_certs_rank_two_higher_trace_ordered_limit_open_2026_11_08
description: "Exact certificates that small-init GD in matrix sensing can end above planted trace (n>d)? Locally yes (8 Nov): 2 instances, rank-two interpolants with trace excess 0.349/0.523 and attracting balls; reaching them from small alpha is open"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T11:36:51+04:00
  status: verified
  evidence: "06_math_research/frontier/T234/open_t234c_agent_11_08 (0cc538d318); scratchpad t234c_check.py"
  originSessionId: 81695323-627a-4240-9df2-cd66cd18fae9
---

Are there exact certificates that small-init GD in matrix sensing can end above the planted trace when n > d? Locally yes (8 Nov 11:36): Codex OPEN-T234c certified, in exact rational arithmetic, two saved instances (d40 n60 trial 1 and d80 n100 trial 4). Each has a positive-loss strict rank-one minimum (loss above 0.00696 and 0.00320) and a nearby regular rank-two interpolant whose trace beats ||x||^2 by 0.349 and 0.523. An attracting full-width ball sits around each, for flow and for GD at 0.05. Open: whether small-alpha starts actually reach that ball (the validated connecting segments and the transported seed). For GD there is also a discrete escape-phase family.

My check (scratchpad t234c_check.py) reproduced every tabled number in floating point: Hessian minima 0.005801 and 0.016542, Jacobian smallest singular values 1.230 and 2.153 (above one, as needed), and Gauss-Newton moves of 7e-15 and 3e-13, inside the certified radii. The .npz inputs were left out of the push because the secret scanner cannot read binaries; provenance.py rebuilds them.

Pushed 0cc538d318 to 06_math_research/frontier/T234/open_t234c_agent_11_08.

Related: [[t234b_misses_finite_alpha_28_of_30_rank_one_trap_2026_11_08]] is the floating-point evidence this certifies.

