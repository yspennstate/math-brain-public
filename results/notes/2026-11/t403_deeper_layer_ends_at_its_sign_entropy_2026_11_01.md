---
name: t403_deeper_layer_ends_at_its_sign_entropy_2026_11_01
description: [PROVISIONAL] T403: in a 2-layer noisy tanh net the deeper layer's I(X;T) ends within 0.03 of its sign-pattern entropy and compresses further; data processing caught my estimator bug
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T07:52:59+04:00
  status: provisional
  evidence: ""
---



Follows [[t403_tanh_compresses_to_sign_pattern_entropy_2026_11_01]]. Pushed ab44780, research_pushes/2026-11-01-loop-T403-deep; move 11a20422.

**Set-up:** two noisy tanh layers, 64 inputs, sigma 0.3, width 8, no weight decay. I(X;T2) is estimated with a 64 x 24 mixture over the first layer's noise.

**Results:**
- At the end of training I(X;T2) is within 0.03 of H(P2) in 6 estimates (linear task: 1.34-1.39 vs 1.364, and 1.67-1.69 vs 1.669).
- H(P2) < H(P1) in every run.
- Layer 1 stays 0.2-0.5 above H(P1).
- On the linear task the late compression happens in layer 2 only.

**Two estimator traps:**
1. With noise in an earlier layer, H(T_l | X) is not the Gaussian constant. Subtracting it gave I(X;T2) > I(X;T1), and the data processing inequality flagged it.
2. At 12,000 samples I(Y;T2) reached 0.735 > ln 2. Tripling the samples brought it to <= 0.698. Use ln 2 and log n as live checks of the estimator.

**Why:** the "deeper nets" open item on T403 now has an answer at toy scale.

**How to apply:** put a ceiling check (I <= H(Y), I(X;T_l) <= I(X;T_{l-1})) into any mutual-information estimate before reading trends from it.
