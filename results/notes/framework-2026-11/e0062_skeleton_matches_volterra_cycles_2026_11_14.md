---
name: e0062_skeleton_matches_volterra_cycles_2026_11_14
description: "[PROVISIONAL] E0062 Volterra QSO ergodic theorem, A with zeros: the piecewise-linear skeleton on log-sizes gives the full map's dwell growth to 3 decimals on C4/C5 networks; symmetric chordless cycles grow by rho(a)=log(1/(1-a))/log(1+a)>1, so non-ergodic for every weight"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T10:59:24+02:00
  status: provisional
  evidence: ""
---

Note, code and output: 12_cognitive_architecture/math/trio_1011/op/E0062 (NOTE.md, skel.py, skel_out.txt). Builds on the 9 Sep memo 06_math_research/prob1000_lean_20260908/ultracode_20260909/E0062/memo.md (nondegenerate A settled: ergodic iff transitive tournament). Measured 14 Nov, 300k steps: C4 all 0.5 1.71 per 2 visits (skeleton 1.711); C5 all 0.5 1.709 per 3 visits (1.710); C5 all 0.2 1.224 (1.224); C5 + chord 1 beats 3 both pick the short cycle, 1.712 vs 1.708. Conjecture: with zeros and no strict 3-cycle, failure iff the skeleton has a cycle with period growth > 1. Not proved: that the full map follows the skeleton (o(1) and transition-phase control). Status provisional; what would change it: a full-map orbit whose growth departs from the skeleton.
