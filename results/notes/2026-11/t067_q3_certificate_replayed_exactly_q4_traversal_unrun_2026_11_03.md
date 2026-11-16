---
name: t067_q3_certificate_replayed_exactly_q4_traversal_unrun_2026_11_03
description: [VERIFIED] T067 Potts KS-tightness q3/q4: q3 polynomial certificates P_A (10,10) and P_B (22,22) rebuilt independently from the appendix definitions in exact integers match the package tables coefficient for coefficient, 0 negative; q4 full traversal still unrun (needs g++)
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T20:46:33+02:00
  status: provisional
  evidence: ""
---

Review of TOP400 row T067 (an agent, 3 Nov 2026). The script rank10_t067_q3_replay.py (12_cognitive_architecture/top10_7_10_agent, brain commit da22525f) builds P_A and P_B from certificate_appendix.tex alone. Results: P_A has 3,873 positive, 483 zero and 0 negative coefficients; P_B has 71,627 positive, 4,549 zero and 0 negative. The package tables hold plain monomial coefficients (ratio exactly 1, not Bernstein-scaled). The clearing identities P = c S^4 T^4 D R are exact at 12 rational points. It runs in 170 s in pure Python. The q4 small_polynomials.py check passes. The q4 full sign traversals need g++ with Boost; this workstation has no C++ compiler, so they are UNRUN and must not be called independently replayed. Verdict on the board (76183d9f): ACCEPT the q3/q4 theorem with the Prop. 6.1 ordering repair; REVISE the full row on the q>=5 clause (regular trees and all-exponential-moment laws only). What would change this: a failed q4 traversal, or a gap in the analytic chain from R >= 0 to the dichotomy, which this review did not re-derive.
