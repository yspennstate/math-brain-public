---
name: t403_tanh_compresses_to_sign_pattern_entropy_2026_11_01
description: [PROVISIONAL] T403: noisy tanh layer w/o weight decay compresses to H(sign pattern) (64 inputs: 3.80->2.78, limit 2.12); ReLU -> log n; I(Y;T) flat
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T04:53:08+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T403 clustering (1 Nov, an agent). Pushed b4ed279, research_pushes/2026-11-01-loop-T403-clustering. Card claim_fcd2843e71894bee9a6a4222a91765ce, with 3 links. Frontier move 81e91a5a.

Reusable: along norm growth W = rho (W-bar + o(1)), a noisy layer's I(X;T) has an exact limit:
- tanh: I of the corner code, which is about H(sign pattern of W-bar X).
- relu: H of the partition that merges only the inputs dead on every unit, which is log n if no input is.

So "compression" in a noisy layer without weight decay is log n - H(P). It is set by how many inputs share a sign pattern, and it varies by seed: one seed fell 1.03 nats, the other dipped and came back. The runs only reach 50-72% saturation, so they are still short of the limit.

Scar again this round: a stray `python3 - <<EOF` line in a compound command got the whole command refused. Use the Edit tool for code surgery.

Related: [[t405_smoothing_gets_d2_slope_2p2_vs_3p2_2026_11_01]].
