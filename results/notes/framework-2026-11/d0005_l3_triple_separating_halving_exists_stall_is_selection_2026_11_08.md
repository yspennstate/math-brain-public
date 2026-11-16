---
name: d0005_l3_triple_separating_halving_exists_stall_is_selection_2026_11_08
description: "[VERIFIED] D0005 recursive halving: the L3 triple's frozen diameter 0.6489 is NOT forced - an admissible exact halving cuts it to 0.5646 (ratio 0.870); stall comes from which solution the recursion picks"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T19:44:53+02:00
  status: provisional
  evidence: ""
---

On the L3 halve5 triple (papers_agent/D0005) sep_split.py found 17 distinct admissible halvings that keep the frozen piece's diameter 0.6489, then hit 19 at theta (1.37327069, 1.42416917, 3.26117472) that separates its endpoints: residual 7.6e-16, every piece split exactly 1/2 by area, frozen 0.648877 -> 0.564628/0.506029, largest child/largest parent 0.870162, ray slacks 0.102/0.168. Re-checked by sep_check19.py (re-solved from rounded angles). Hit 20 is the same cut with angles +pi. Lesson: n of n solutions agreeing is a count, not a proof of necessity - keep the search to its final count before calling a rule dead. Next: recursion that picks the admissible halving minimising the largest child diameter.

Update 9 Nov 00:1x: the "weak" separating branch (sols 22/28/39/32, th2~1.96) is the same 1-parameter curve as hit 19: followed in th1 (th1_cont.py, step 0.02, residuals ~1e-15) it runs straight into hit 19's angles. Minimising the largest child along the curve (th1_min.py) gives th = (1.394951008, 1.394951008, 3.261679203), ratio 0.87004271, ray slack 0.073; verify_cut.py (shapely, independent) agrees at 0.870043. Small gain over 0.870162. At the minimum th1 = th2, matching the two equal-area pieces. halve6.py (min-largest-child rule) is running on quad_generic: level 1 max_diam 0.921 after 3.5 h; level 2 under way.
