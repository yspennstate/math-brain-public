---
name: t226_depth_two_boundary_gaussian_edge_window_limit_is_0_t226c_2026_11_08
description: "Does depth-two GD at boundary Gaussian scale converge in a fixed edge window (T226)? No, limit 0 (8 Nov): OPEN-T226c, almost every exterior start escapes; checked 53,609 of 53,609"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T10:30:35+04:00
  status: verified
  evidence: "frontier T226 rows 8 Nov 10:29, push ea2c2beef0, card claim_4795f853, t226c_check.py"
  originSessionId: 81695323-627a-4240-9df2-cd66cd18fae9
---

Does depth-two GD at the boundary Gaussian scale ever converge inside a fixed edge-of-stability window (T226)? No, in the limit, as of 8 Nov 10:29. For F(u,v) = (uv-1)^2/2 with u0, v0 iid N(0, 1/eta), P(converges and |lambda - 2/eta| <= C) -> 0 for every fixed C. Starts inside the disk x^2 + y^2 < 4 (probability 1 - e^-2) converge to subcritical endpoints (OPEN-T226b), and Codex OPEN-T226c proved that almost every start outside the disk escapes.

Codex's proof: every exterior point has exactly three exterior preimages under T(x,y) = (x(1-y^2), y(1-x^2)), and the weighted area dx dy/(x^2+y^2-4) expands by more than 3 on the non-escape set, which has finite weighted area, so that set is null. Escape persists for small positive targets. There is also a rational certificate: the exterior mass not escaped by zero-target time 65,536 is below 1/3500.

My check (scratchpad t226c_check.py, now in the frontier folder as review_check_agent.py): 20,000 of 20,000 exterior targets have 3 exterior preimages; the minimum expansion is 3.0020 near the circle and 3.1433 for r^2-4 > 1; all 53,609 seeded exterior starts escape by step 15. I did not check the positive-target persistence or the rational certificate beyond reading them.

Rows in 06_math_research/frontier/rows/T226 and folder open_t226c_agent_11_08 (pushed ea2c2beef0). Card claim_4795f8530e4f4a04bce69de00c2dd9c4, depends on the T226b card claim_9cae2927. Higher depth and the general network problem stay open.

