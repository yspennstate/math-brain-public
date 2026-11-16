---
name: per_coordinate_fei_bound_is_sharp_2026_11_08
description: "FEI T021 8 Nov 03:1x: R_i <= I ln((1-I)/I) is sharp over all Boolean f; f = x_i on a k-subcube and bent off it gives R_i/(I ln(1/I)) -> 1 (0.99998 at k=14). Monotone constant still in [0.396,1]."
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T03:18:08-05:00
  status: verified
  evidence: "check_bent_cube.py/.out in the private brain repository: 06_math_research/frontier/T021/fei4_agent_2026_11_08"
---

The per-coordinate bound R_i <= max_x [x ln((1-I)/x) + (I-x)/e] (so R_i <= I ln((1-I)/I) for I <= 0.2029), proved in [[per_coordinate_fei_cost_is_at_most_i_ln_e_over_i_for_every_boolean_f_2026_11_08]], cannot be improved by a constant factor over all Boolean functions.

Construction: put f = x_i on the subcube C = {x_1..x_k = 1} and f = u(x_1..x_k) off C, where u is the inner-product bent function and k is even. Then I_i = 2^-k, every b_S^2 = 4^-k for S in [k], and a_S^2 = 2^-k (1 +- 2^-k/2)^2. So equality in Jensen holds up to 1 + O(2^-k/2).

Exact values of R/(I ln(1/I)): 0.396 at k=2 (the same as G(c,1)), 0.931 at 4, 0.989 at 6, 0.99958 at 10, 0.99998 at 14. I derived it analytically first, and the numbers agree.

Why it works: tightness needs a_S^2/b_S^2 = (1-I)/I on every pair. Writing f = g + x_i h with gh = 0 forces h onto the pivot set. A flat (bent) g on the complement does it.

Still open: the monotone version. A bent u is not monotone, so the monotone constant stays in [0.396, 1]. The question is how flat a monotone f can make its spectrum off the pivot set. Measured: 7 exact cases, n <= 15.
