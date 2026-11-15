---
name: t380_threshold_margin_set_by_atom_size_not_noise_2026_11_01
description: [VERIFIED] T380: no-predictor SimSiam, one neuron: masking cancels linear signal exactly; threshold makes atoms maxima, margin ~exp(-r^2(1/sqrt k-b)^2/2); noise-tied bias loses it at d 60 (5/20 vs 19/20)
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T03:58:13+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T380 (1 Nov, an agent). Pushed 75891da, research_pushes/2026-11-01-loop-T380-threshold-margin. Card claim_4a765d7dbd2847908e7f91ffba3d7931, with 3 links. Frontier move 24eb14ce.

What carries over: under RandomMask with an orthonormal dictionary, the linear positive-pair objective is exactly p(|M^T w|^2 - sum w_k^2 (MM^T)_kk). That is flat, so any atom selection has to come from the unit's nonlinearity. With a hard threshold, the atom's edge over a k-mixture depends on b against 1/sqrt k, and is exponentially small when b sits well below 1/sqrt 2.

A bias tied to the noise level shrinks with d, and so does the margin. That fits the stalled d = 60 runs of 18 Oct. The one-neuron probe at both thresholds (5 of 20 against 19 of 20) supports it, but the full multi-neuron cosine-loss run at b = 0.6 has not been done. A large fixed b gives dead units (1 of 20 starts at b = 0.6).

Scar from this round: a python -c replace containing a newline escape wrote a real newline into the script (SyntaxError). For edits with escapes, use the Edit tool.

Related: [[t328_two_token_basins_exact_by_loss_free_integral_2026_11_01]], [[t298_escape_rate_width_free_digamma_offset_2026_11_01]].
