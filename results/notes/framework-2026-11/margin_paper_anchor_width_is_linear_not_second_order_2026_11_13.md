---
name: margin_paper_anchor_width_is_linear_not_second_order_2026_11_13
description: "[VERIFIED] Margin paper said b0-anchored Phi differences have width 'second order' in |l-b0|: measured LINEAR (gain 57-251 at d=0.01); measure an order at several step sizes before stating it"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T01:05:30+02:00
  status: verified
  evidence: "r13/m1_order.out 13 Nov 00:35 (15 rows, radius halves with d); commit 5a90a04 on yspennstate/ising-perceptron-margin"
---

The margin paper (ising-perceptron-margin, v2.0) said for many versions that writing the differences of Phi against b0=(1,0) makes the parameter width enter "only at second order in |lambda-b0|", and quoted a gain of 50 to 160 at distance 0.01. The 14th referee read (13 Nov) noticed the two claims cannot both hold: a second-order width would give a gain that grows like 1/d^2, and its own one-node test showed a linear width.

Measured 13 Nov 00:35 at kappa=0.05 over the hull of the alpha_star interval [0.781073068, 0.781074776] (script scratchpad r13/m1_order.py, output r13/m1_order.out): the enclosure radius of the b0-anchored form is proportional to d = |lambda-b0| along all three directions tested (l1: 3.5e-5 d, l2: 7.9e-6 d, diagonal: 3.0e-5 d; halving d halves the radius from d=0.04 to 0.0025), while a difference of two plain Phi enclosures stays at radius 2.0e-5 regardless of d. Gain at d=0.01: 57 (l1), 66 (diagonal), 251 (l2).

The paper now says: width proportional to |lambda-b0|, 57 to 251 times narrower at distance 0.01, exactly {0} at b0 (abstract, introduction, Section 4.2; commit 5a90a04, tag v2.0). The docstring of verification/huang_cert_region1.py (~l.385) still says "second order"; it was left because the result JSONs pin that file's source_sha256, so editing a comment would break the certificate check.

**Why:** a scaling claim ("enters at second order") was written from the shape of the algebra, not measured, and survived thirteen reads because each reader checked the number, not whether the number fits the claim.
**How to apply:** when a paper states an order of convergence or a scaling, measure it at three or four step sizes and check the ratio before the sentence ships; a quoted single gain is not evidence of the order. Before changing any file in a certificate repository, check whether results pin its hash.

