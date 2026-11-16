---
name: method_pair_copies_to_get_a_uniform_piece_2026_10_29
description: [PROVISIONAL] Method: pair copies so F*F has a uniform piece (g*g continuous), solve there, lift back by conditional law; plus linear tilts that average to uniform
metadata:
  type: reference
  created: 2026-10-29
  created_at: 2026-10-29T23:08:38-04:00
  status: provisional
  evidence: "used in D0007 proof of Wang OP7, exact check 1000/0, zero audits"
---

Technique from D0007 (29 Oct): to prove a statement about n copies of an arbitrary absolutely continuous law F, group the copies in pairs. The sum of two independent copies has law F*F, which dominates a multiple of a uniform law on an interval, because g*g is continuous for g = min(f, M) and has positive integral. Solve the problem for laws with a uniform piece, which are much easier, then lift back: draw each pair (X, X') from the conditional law of (X, X') given X + X' = P_i. Odd n: carry one copy as an extra bounded variable.

The second half of the same proof is reusable too. A bounded error with mean zero can be absorbed by tilting a uniform piece linearly, (1 + beta z/H)/(2H) with beta proportional to the error. The mixture over beta averages back to the uniform law exactly, because the density is affine in beta. Copies from the rest of the law go on a quantile grid Q((sigma(i) + W)/k), whose sum stays within the support length of k times the mean. Keep a random count near its mean by rounding K to the two integers next to it instead of sampling independently.

Why it matters: the pairing step is what turned "densities bounded below on a subinterval" into "every density", and that is what answered Wang's Open Problem 7. Reach for it whenever a hypothesis only fails because a density can be thin everywhere.

Status: the technique was used in a proof with zero audits, [[d0007_step_densities_completely_mixable_2026_10_29]].

