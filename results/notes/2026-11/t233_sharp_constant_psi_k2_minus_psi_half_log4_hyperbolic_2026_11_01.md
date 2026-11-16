---
name: t233_sharp_constant_psi_k2_minus_psi_half_log4_hyperbolic_2026_11_01
description: [PROVISIONAL] T233 sharp constant k>=2 at m=cL: n g(m,k) - E log s_min^2 -> psi(k/2)-psi(1/2) as c->0 (log 4, 2, 2.386 for k=2,3,4); k=2 law exact via H^2 Brownian motion (McKean), matches sim to 0.026 nats
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T15:21:43+04:00
  status: provisional
  evidence: ""
---



Measured 1 Nov (t233_sharp.py): McKean H^2 law vs Bartlett sim at L=512, c=0.5/1/2: mean within 0.026 nats (2.1 se), sd 0.3 percent, q01 0.06. Delta(2,T)=E v_T - T/2 = 0.672, 0.851, 1.037, 1.373 at T=0.5, 1, 2, 16. Mechanism: Bartlett product M upper triangular, s_min <= D_k/|xi|, xi = D_k M^-1 e_k, and xi direction -> bottom right singular vector, Haar by right O(k)-invariance; at m=128, T=16, E log|xi|^2 = 1.356/1.975/2.436 vs 1.386/2/2.386. Argued not proved: diffusion limit and the T,m limit swap. Prediction (5) window failed for k=4 (+0.07, 1.1 se) and k=2 non-monotone within se.

Related: [[t233_kxk_bartlett_reduction_tails_lyap_off_2026_11_01]] - identifies the offset that note measured and left open

Update 1 Nov 15:44 (t233_resid.py, 9aa6d47): the whole gap law holds at T=16, m=128: r = log D_k^2 - log s_min^2 -> -log Beta(1/2,(k-1)/2), KS p 0.87/0.30/0.09, independent of s_min (corr within 0.01), small-ball P(s_min < delta D_k) ~ (2/B(1/2,(k-1)/2)) delta. My pre-registered independence-from-D_k prediction was wrong: D_k^2 = s_min^2 e^r contains r; test independence against s_min.

Folders: research-repo research_pushes/2026-11-01-loop-T233-sharp, and research_pushes/2026-11-01-loop-T233-resid for the 15:44 update
