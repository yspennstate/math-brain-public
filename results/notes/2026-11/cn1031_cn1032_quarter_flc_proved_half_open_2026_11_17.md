---
name: cn1031_cn1032_quarter_flc_proved_half_open_2026_11_17
description: "[PROVISIONAL] CN1031/1032 half-FLC of k-matching and nonsymmetric k-DPP laws: 1/4 is proved (ASV 2102.02708 Cor 63-64 Gamma_1/2-stable + Lemma 69), 1/2 open; small-case search n<=8 found no counterexample"
metadata:
  type: project
  created: 2026-11-17
  created_at: 2026-11-17T01:48:01+02:00
  status: provisional
  evidence: ""
---

Alimohammadi, Anari, Shiragur, Vuong (arXiv 2102.02708) show the k-DPP polynomial (L+L^T psd, Cor 63) and the 2k-vertex perfect-matching polynomial (Cor 64), and their duals, are Gamma_{1/2}-sector-stable. Lemma 69 there: Gamma_{2a}-sector-stable implies a-fractionally log-concave, so they get a = 1/4. Yang (2023) asks for a = 1/2 (catalogue CN1031, CN1032). Secondary sources disagree (2109.06442 says 1/4, 2106.04105 reads as 1/2): the primary statement settles it at 1/4. Our numerical check on a worker machine (17 Nov; random graphs n=4..8 for matchings, random L with L+L^T psd n=3..7 for DPPs; Hessian of log g(z^{1/2}) checked for negative semidefiniteness) found no violation of 1/2. Status: open, evidence only. Next move if picked up: compute the largest alpha for which each small instance is alpha-FLC, to see whether 1/2 is ever tight; scripts at 12_cognitive_architecture/brain_improvement/agent_run NEXT.md lines of 17 Nov.
