---
name: sen_virag_constant_digits_wrong_in_paper8_2026_11_12
description: "[VERIFIED] Sen-Virag Toeplitz norm constant: 0.828843 (square 0.686981, Sen-Virag quoting Garsia-Rodemich-Rumsey), not 0.8288582/0.6870697; paper 8 fixed 12 Nov, renamed theta"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T10:00:24+02:00
  status: provisional
  evidence: ""
---

Paper 8 (toeplitz-hankel-section-profiles) printed the Sen-Virag constant as rho = 0.8288582... and rho^2 = 0.6870697...
The two numbers do not even agree with each other (0.8288582^2 = 0.6870059), and both are wrong past the fourth decimal.

The source: Sen and Virag, "The top eigenvalue of the random Toeplitz matrix and the sine kernel" (Ann. Probab. 41 (2013);
arXiv 1109.5494). The abstract gives only 0.8288...; the end of the paper quotes, from Garsia, Rodemich and Rumsey (1969),
K_1^2 = 0.686981293033114600949413..., where K_1 = ||Sin||^2_{2->4} is the limit of lambda_1(T_n)/sqrt(2n log n).
So the constant is theta = K_1 = 0.8288433465..., theta^2 = 0.6869812930..., 2 theta^2 = 1.3739626, e^{1/theta^2} = 4.28724.

What changed on 12 Nov (an agent): in paper 8 the constant is renamed theta (paper 7 uses rho for crossing cores, and
paper 8's notation table) with 0.828843..., 0.686981..., 2 theta^2 = 1.37396 and e^{1/theta^2} = 4.2872, and verify/verdict.py
prints the corrected targets. Paper 7 does not use the constant (its s_new.tex in the scratch folder is not \input by main.tex).
No conclusion moved: the Richardson value 1.3734 stays within 10^-3 of 2 theta^2 (gap 0.0006), and 4.20-4.24 against 4.2872 is
still the same consistency check.

How to apply: a constant quoted to seven digits needs its digits checked against the source, not copied from an earlier draft;
when a paper prints both c and c^2, square one and compare with the other. The old digits came from the p7run verify notes
(identification_attacks.md, 0.68707), which never cited where they came from.

