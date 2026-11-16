---
name: t287_gaussian_prior_maximizes_product_mmse_via_rie_comparison_2026_11_01
description: [PROVISIONAL] T287 target 2: asymptotically the Gaussian iid prior maximizes product MMSE and MI (RIE is prior-blind and Bayes-optimal for Gaussian, so any prior can use it)
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T00:18:38+04:00
  status: provisional
  evidence: ""
---

Written 2026-11-01 00:18 +0400; T287 move (06_math_research/frontier/rows/T287/moves.jsonl). Three steps: noise bi-invariance + RIE equivariance make the RIE's MSE a function of the signal's singular-value law only; that law is universal for iid factors with matched variance; the RIE is Bayes-optimal for the Gaussian prior. So limsup MMSE_prior <= MMSE_Gauss at every Delta, and by I-MMSE the same for I. 2411.01974 (PRX 2025) states the prior-blindness of the RIE for symmetric denoising and finds strict gaps above a transition for Rademacher, and states the MMSE comparison informally in Section V.1 ("the associated MMSE cannot be larger than in the Gaussian case given the same data"; found on a second read of the HTML, chars 100k-200k). New here: the RIE proof route, the rectangular case and the MI half. Gaps: finite N, a rectangular continuity citation. Same scalar-channel extremality as the dossier's s^3 term (-k4^2/6). General pattern: when an estimator is optimal for the invariant prior and its risk is prior-blind, the invariant prior is least favourable.

Related: [[gaussian_prior_maximizes_mmse_and_mutual_information_small_snr_t287_2026_10_18]] - the small-snr series version; this extends it from order s^3 to every Delta in the limit.
