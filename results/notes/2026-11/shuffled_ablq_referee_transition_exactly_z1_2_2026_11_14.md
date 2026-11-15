---
name: shuffled_ablq_referee_transition_exactly_z1_2_2026_11_14
description: "[VERIFIED] shuffled-ablq-dominating-pair (T353) refereed 14 Nov: every number reproduces; transition is exactly z1=2 (not 2.005), fixed public 685321f"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T07:22:35+02:00
  status: provisional
  evidence: ""
---

Independent referee pass (an agent, T-20261112-017) on yspennstate/shuffled-ablq-dominating-pair at f3f538a. Verdict ACCEPT WITH ONE MINOR CORRECTION.

Reproduced from the paper's statements only (plain scipy quadrature): z1=2.5 I_ANTI/I_SAME to 13 digits; T=2 pair 0.221269, reverse 0.205107, best-of-two 0.223234 (repo independent_check 0.2232343935; my first quadrature said 0.223235 - quadrature error, not the paper's); certificate interval [2.1,2.6] integral 1.51e-3 >= claimed 1.04e-4; T=3 point 1.535260930e-3 exact.

Fix (685321f, SHA256SUMS lines 94-95 rebuilt from staged blobs, clean clone passes all 106): the SAME/ANTI transition is exactly z1=2. There alpha = sqrt(e) gamma, the ANTI integrand is positive exactly on s>2, the SAME one on s>0, and both integrals equal beta(1/2 - sqrt(e)(1-Phi(1))). The 2.005 was the first point of a 0.005 grid.

Lesson: a 'transition near X' read off a grid often sits at a round value with a closed-form reason; bisect it and look for the identity before printing the grid value. Also: when your sixth digit disagrees with the paper's, check the repo's own independent check before 'correcting' the paper.

Not re-run: the Renyi/KL certificates (replayed 22 Oct). Report: 06_math_research/referee_reports/2026-11-14/T353_posted_referee/REPORT.md. Related: [[rr_constant_step_log_factor_referee_three_fixes_2026_11_14]].

Addendum 14 Nov 08:40: the best-of-two value at T=2 is 0.223234586369 by a closed-form inner integral (the integrand is phi times three exponentials, at most two roots; t353_exact.py in the report folder), so 0.223235 to six digits; the paper printed 0.223234 and is fixed in 9e54e0c, which also adds the missing Google Cloud funding line. Lesson: a value within 1e-7 of a rounding edge needs an exact inner integral, not a grid or an adaptive quad on a kinked integrand (the adaptive one ran 25 min without finishing one interval).
