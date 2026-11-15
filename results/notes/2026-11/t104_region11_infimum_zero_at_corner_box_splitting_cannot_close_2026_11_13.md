---
name: t104_region11_infimum_zero_at_corner_box_splitting_cannot_close_2026_11_13
description: "[PROVISIONAL] T104 5+1 region (11): open leaves keep growing under box splitting? The infimum is 0 at corner r=a=1 (explicit family); switch to a local expansion"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T07:20:20+02:00
  status: provisional
  evidence: ""
superseded_by: t104_region11_n6_proved_collars_strat13_2026_11_13
---

T104 (Alon Conj. 1.5) 5+1 class at N=6, STRAT9 region (11): Codex STRAT10 (13 Nov) found an explicit connected family
U=(-4,1+s,1+s,1-s,1-s), W=(0,1,-1,-1,1), r=1, a=(5+s^2)/(5+10s-s^2), 0<s<=1/100, inside every residual filter, with exact
T6 = s(1100-335s+...)/[4(s^2+5)(s^2-10s-5)^2] -> 0+ as s -> 0. So the residual's infimum is 0 at the corner (r,a)=(1,1).
Consequence (the lesson): exact box splitting cannot close a region whose infimum is attained at a boundary point - the
open-leaf count grew linearly (2,452 at 43k visits -> 5,244 at ~80k) and never turned. Stop splitting once the open count
grows past a few tens of thousands of visits and switch to a local expansion at the zero (linear term on the tangent cone
by exact LP, explicit remainder ball, boxes outside it) - that is STRAT11 (fillq_ctl/codex_strat11/PROMPT.md).
Also from STRAT10, PROVED and checked independently by an agent (400k random + 40 local searches, sharp at
u=(-1,0,0,0,1)/sqrt2): for zero-sum unit u in R^5, (sum u^3)^2 >= 3 sum u^4 - 3/2 (625K^2 + nonnegative monomials).
Uniform scale ceilings rose to a<=2849/5000 at N=6 and a<=129/250 for all N>=6. Final ledger: 24,708 positive, 10,226
excluded, 5,244 open leaves (open ~10% of root volume 1152). Status: provisional until the mini2 replay (push 137).

