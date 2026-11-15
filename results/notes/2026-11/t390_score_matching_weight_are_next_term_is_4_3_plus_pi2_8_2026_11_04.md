---
name: t390_score_matching_weight_are_next_term_is_4_3_plus_pi2_8_2026_11_04
description: "[VERIFIED] T390 score matching vs ML for the mixing weight of 1/2 N(-m,1)+1/2 N(m,1): ARE = sqrt(2 pi) e^(-m^2/2)/m (1 - c/m^2), exact c = 4/3 + pi^2/8 = 2.56703 (source said 'about 2.5')"
metadata:
  type: project
  created: 2026-11-04
  created_at: 2026-11-04T12:32:38+02:00
  status: verified
  evidence: "rank10_t390_check.py/.json in brain-repo 12_cognitive_architecture/top10_7_10_agent (mpmath 40 digits, two independent quadratures); board brain-tasks-board df6beda"
---

Review 4 Nov 2026 (an agent, rank 10 TOP400 review). Source research-repo 465b73ba T390_weight_are_asymptotic.md.

How: p(x) = phi(x) e^(-m^2/2) cosh(m x) exactly, so y = m x turns H and V into int sech^3 e^(-eps y^2/2) and int sech^3 (tanh y + eps y)^2 e^(-eps y^2/2), eps = 1/m^2, with no approximation. First order: c = 8/3 - (2/pi) J3 + (4/pi) J5, J3 = int y^2 sech^3 = pi^3/8 - pi, J5 = int y^2 sech^5 = 3 pi^3/32 - 5 pi/6, so c = 4/3 + pi^2/8.

Check: two independent quadratures (y-form and the source's own x-form) agree and reproduce the source table; m^2(1-ratio) = 2.486 (m=8), 2.554 (20), 2.5665 (100) -> 2.56703. The source read 'about 2.5' from m <= 8 where the m^-4 term still pulls it down. Lesson: a coefficient read off small-m numerics is biased by the next term; go to m = 100 or derive it.

Not checked: sandwich rigour, denoising part, k-component conjecture, prior art. Files: rank10_T390_review.md beside the check.

**Part 2 (12:4x 4 Nov):** the denoising table (noise integrated out) reproduces 7/7 rows in both columns by an independent nested quadrature (rank10_t390_noise_check.py). The lower bound H^2/(V_s I) is valid because the noise-integrated DSM and explicit gradients coincide (Stein on z), so V <= V_s. "Loose by about 3" holds only at sigma = m; the m/tau sentence fits H^2/(V_s I_s), not the bound column. Board fe6534d.

**Part 3 (13:0x 4 Nov):** next term exact, d = 58/9 - pi^2/2 + 5 pi^4/128 = 5.31468 (ARE ~ lead x (1 - c/m^2 + d/m^4 + O(m^-6)); PSLQ, 40 digits; m^6 x remainder -> -9.955). Sandwich regularity holds (derivatives dominated by C(1+x^2), unique minimiser). Board ac5dfa1.
