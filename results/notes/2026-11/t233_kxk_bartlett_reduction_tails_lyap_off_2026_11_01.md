---
name: t233_kxk_bartlett_reduction_tails_lyap_off_2026_11_01
description: [VERIFIED] T233 tails: s_min of m x k Gaussian product = s_min of k x k Bartlett product (exact); uniform-in-L tail bound; Lyapunov mean 0.7-1.9 nats high for k>=2
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T11:38:44+04:00
  status: provisional
  evidence: ""
---



Pushed 2416259, card claim_52930b638f974edeb190079258580dbd export a803090, move 27bab606. Follows [[t233_end_layer_bound_caps_kernel_rate_2026_11_01]].

- The k x k reduction (W Q is Gaussian again, by rotation invariance) makes any s_min-of-a-Gaussian-product question a fixed-dimension problem. 20,000 draws per cell cost seconds.
- The bound det G/(tr G)^(k-1) is rigorous and flat in L, but it is loose by 19-40 nats at k=4.
- The Lyapunov mean n g(m,k) is exact only for k=1. At m=cL the bottom exponent has not separated, so I was wrong to predict it is within 1 nat for k=4.

**Why:** this closes the T233 finite-L tails item.

**How to apply:** for m proportional to depth, use the k x k Bartlett simulation for constants and do not trust Lyapunov means for k>=2. A sharp constant for k>=2 is still open.
