---
name: t268_relu_fixed_dim_fat_shattering_two_sided_exponent_2026_11_16
description: "[PROVISIONAL] T268 / Vardi-Shamir-Srebro fixed-input-dimension question: for u^T relu(Wx), |u|<=b, ||W||_F<=B (or spectral), |x|<=b_x, fat_eps ~ (bBb_x/eps)^{2(d-1)/(d+2)} both ways up to log, width-free; upper via Siegel 2307.15285 Thm1 (zonoids) on the sphere, lower via slice -> biased ReLU in d-1 + Mao-Siegel-Xu 2408.10996 Thm1 Sobolev embedding (s=(d+2)/2) on bumps; store cards misquote VSS Thm3 (it is min(nd,(bBb_x/eps)sqrt d)); notes fillq_ctl/t268_fixed_d/LEAD.md; not yet written up or audited"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T10:11:18+02:00
  status: provisional
  evidence: ""
---



Does a fixed input dimension shrink the fat-shattering dimension of norm-bounded one-hidden-layer ReLU nets
(Vardi-Shamir-Srebro, arXiv 2202.06233, Sec. 3.2 and Sec. 6)? Yes, provisionally (16 Nov, not yet audited):
for sigma = [z]_+ and R = bBb_x/eps, fat_eps = R^{2(d-1)/(d+2)} up to log factors and d-dependent constants,
for every width (upper) and once the width is large (lower); exponent < 2 for every d.
- Upper: the network is homogeneous, so it is |x| times a function on S^{d-1}; relu = (|z|+z)/2, the linear part
  is exact; Siegel, arXiv 2307.15285, Theorem 1 (n-point zonoid approximation, sup error n^{-1/2-3/(2(d-1))})
  plus a parameter grid gives sup-norm entropy R^{2(d-1)/(d+2)} log R; an external sup-norm cover bounds shattering.
- Lower: points on the slice x = b_x (y/sqrt2, 1/sqrt2) turn relu(w.x) into a biased ReLU in dimension d-1;
  signed bumps of width delta and height eps have Sobolev norm eps delta^{-s}, s = (d+2)/2; Mao-Siegel-Xu
  arXiv 2408.10996 Theorem 1 embeds W^s(L2) into the variation space; finite width by Siegel Theorem 3.
- Scar: the store cards for T268 and VSS quote VSS Theorem 3 as (bBb_x/eps)^2/d; it is min(nd, (bBb_x/eps) sqrt d).
- Not covered: the shared-bias activation [z - beta]_+ with beta > 0 (upper exponent 2d/(d+3) only).
Status: provisional. What would change it: a gap in the slice reduction or the half-integer interpolation step,
or a prior paper stating the two-sided rate. Notes: fillq_ctl/t268_fixed_d/LEAD.md.
Related: [[jgshg_lemma16_needs_square_g_depth4_full_rank_2026_11_16]] [[catalogue_row_already_solved_in_store_recall_first_2026_11_16]]

**Posted 16 Nov 17:41 (an agent):** public repo yspennstate/relu-fat-shattering-fixed-dimension, tag v1.0 at 1f643b32,
Zenodo record 24284960 (doi 10.5281/zenodo.24284960). First-reader audit MINOR EDIT, 0 must-fix; 18 should-fix items went
into v1.1 (fillq_ctl/t268_fixed_d/paper), whose re-audit is waiting for a reader slot. v1.1 goes up as a NEW tag and a
Zenodo new version of 24284960, never by moving v1.0.
