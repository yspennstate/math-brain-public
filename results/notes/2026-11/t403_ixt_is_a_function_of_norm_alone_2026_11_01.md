---
name: t403_ixt_is_a_function_of_norm_alone_2026_11_01
description: [PROVISIONAL] T403: I(X;T) of a noisy tanh layer under GD depends on |W| alone (spread <=0.017 over lr 0.01-0.2); |W| ~ ln t; predicted 1/|W| gap decay absent to |W| 9.3
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T08:13:23+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



Pushed 923e6fa, move 396bcccf. Follows [[t403_deeper_layer_ends_at_its_sign_entropy_2026_11_01]] and [[t403_tanh_compresses_to_sign_pattern_entropy_2026_11_01]].

One tanh layer, width 8, 64 inputs, sigma 0.3, linear labels, lr x steps = 2000.

- At matched |W| = 4-7, I(X;T) agrees across lr 0.01, 0.05 and 0.2 within 0.017 nats (seed 1) and 0.008 (seed 2).
- d|W|/d ln t = 0.9-1.45.
- My prediction that the gap to the saturated sign code falls like 1/|W| failed in the reached range: the gap rises to 0.5-0.7 and stays flat up to |W| 9.3. Only the near-zero pre-activation fraction falls like 1/|W|.
- The gap itself collapses poorly across lr (up to 0.14 apart), because the sign code is discontinuous in W.

**Why:** the T403 rate item is a norm question. Learning rate only sets the clock.

**How to apply:** compare runs at matched norm, not matched step. The limit sits beyond norms that training reaches in polynomial time.

Folder: research-repo research_pushes/2026-11-01-loop-T403-rate (T403_rate.md, t403_rate.py, t403_rate.txt)
