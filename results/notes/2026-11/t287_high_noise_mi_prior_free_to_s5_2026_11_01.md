---
name: t287_high_noise_mi_prior_free_to_s5_2026_11_01
description: [PROVISIONAL] T287: extensive-rank UV^T factorization per-entry MI = (1/2)log(1+s beta) - alpha beta^2 s^4/8 + alpha beta^3 s^5/2, prior enters only at O(1/N) through s^5
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T00:08:06+04:00
  status: provisional
  evidence: ""
---



T287 (1 Nov, an agent), pushed ed51a75 to research-repo (research_pushes/2026-11-01-loop-T287-high-noise-mi), card claim_cad2764f61ce48939845ef86917eac2a, frontier move 735a4d0a.

For symmetric X with C = beta I: I = (1/2) log det(I + sC) - (s^4/48)(1+s beta)^-4 sum kappa4^2 + O(s^6). Terms linear in kappa4 never appear. For X = UV^T/sqrt N the nonzero fourth cumulants are (i,j)^4, two row-sharing shapes, two column-sharing shapes, and rectangles (beta/N, which use only second moments). Per entry, sum kappa4^2 -> 6 alpha beta^2, and the prior parts are O(1/N). Checked two ways: brute-force cumulants of four three-point instances matched exactly, and the exact I(s) for N=1, P=2, M=1 Gaussian matched the predicted -2 s^4 + 8 s^5.

Trap: a pre-compaction note guessed that the prior would enter "through EU^4 EV^4 at order s^3". That was wrong (never pushed). Around a Gaussian-covariance base there are no linear-kappa4 terms, so the first prior effect is quadratic in the cumulants.

Open: uniformity in N of the series, and whether prior terms stay O(1/N) at every order. Related: [[t390_score_matching_weight_are_closed_form_2026_11_01]], [[t388_partial_trace_finds_cumulant_spike_at_d2_2026_11_01]].
