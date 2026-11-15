---
name: t283_polytime_low_degree_conjecture_refuted_small_noise_only_2026_11_12
description: "T283 low-degree conjecture: which form is refuted? Polynomial-time form yes (Mao 2607.20318) but only for noise under 0.083; large-noise form, uniform sampler, repaired conjecture open"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T00:36:09+02:00
  status: provisional
  evidence: "arXiv 2607.20318v2 text: Theorem 1.2, Lemma 3.5, Section 4; arXiv phrase search 12 Nov"
---

T283 (the low-degree conjecture), read 12 Nov 2026 from the text of arXiv 2607.20318v2 (Mao, 28 Oct 2026), not from the abstract.

What it proves (Theorem 1.2): for every fixed r >= 3 a vertex-relabelling-invariant graph law P_n whose marginals on up to c_r (log2 n)^(r-1) edges are exactly uniform, and an O(n^2) rank test over F_2 that strongly distinguishes the resampled law from G(n, 1/2) for every fixed noise rate eps <= eps_r. That refutes the polynomial-time form (Conjecture 1.1 there, Hopkins 2.2.4), which quantifies over every eps.

What it leaves, read off the paper: (1) noise: Lemma 3.5 takes a > 2 and a(-log2(1 - eps_0)) < 1/4, so eps_r < 1 - 2^(-1/8) = 0.083 for every r; the large-noise form (no polynomial-time test for eps above some eps* < 1) is untouched, also by 2505.17360; (2) the sampler needs advice, a uniformly samplable example "remains open"; (3) a repaired conjecture with a natural extra hypothesis is called an open problem; (4) degree is only polylog.

Proofs of its Lemmas 2.4, 3.3, 3.4 not checked; one preprint. arXiv phrase search 12 Nov: no follow-up.

Use: a row or a paper that says "the low-degree conjecture" must say which form. Our 1 Nov card (the 2505.17360 family never reaches polynomial time for product nulls) is still right and no longer decides the polynomial-time question.

Note: 06_math_research/t283_lowdeg_agent_2026_11_12/T283_READ.md. Related: [[t283_reed_solomon_counterexample_never_polytime_2e_ln_log_q_floor_2026_11_01]], [[t284_ogp_chain_and_estimator_stability_meet_at_log_n_2026_11_01]].

