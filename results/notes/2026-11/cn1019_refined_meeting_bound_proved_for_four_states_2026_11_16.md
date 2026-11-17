---
name: cn1019_refined_meeting_bound_proved_for_four_states_2026_11_16
description: "[PROVISIONAL] ABOPS meeting-before-trap conjecture, sharpened F >= 1/3 + (2/3) sum pi^3: proved n=3 by hand algebra and n=4 by Cramer-rule polynomial positivity on all six graphs (sym4c.py); referee pending"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T09:59:14+02:00
  status: provisional
  evidence: ""
---

Problem CN1019 (Addario-Berry, Oliveira, Peres, Sousi, EJP 2016, Conj 1.5/1.6). Refined form D = F - 1/3 - (2/3) sum pi^3 >= 0, equality for 2-state chains, approached by multi-scale chains. n=4: multiply each pair equation by p_x p_y, Cramer's rule, N*Q polynomial in p and c; every coefficient positive for star, path, cycle, paw, diamond, K4 (K4 764,076 terms, 397 s sympy on a worker machine). Checked by float vs meet.F (<=9.3e-14) and exact Fraction identity at integer points. Lesson: sympy solve+together took 30+ min per cyclic graph; Cramer's rule in Poly arithmetic takes seconds. Files: 12_cognitive_architecture/loops/72de1487_loop_1115/cn1019/ (NOTE.md, sym4c.py, exact_check.py). Status provisional until the Codex referee returns. What would change it: a convention mismatch with the paper (ties, time scale) or a covering gap.
