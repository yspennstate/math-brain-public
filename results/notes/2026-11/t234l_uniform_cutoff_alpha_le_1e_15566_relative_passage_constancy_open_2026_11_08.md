---
name: t234l_uniform_cutoff_alpha_le_1e_15566_relative_passage_constancy_open_2026_11_08
description: "Is there a uniform small-alpha cutoff for T234 capture? Conditionally yes (T234l): every alpha <= 1e-15566, bound 9.988e-7 < 1e-6 rechecked; constancy open"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T18:34:44+04:00
  status: provisional
  evidence: "OPEN-T234l CUTOFF_CERTIFICATE.json, FINAL_AUDIT.json; t234l_check.py; push 9cce5e30c2"
---

Does gradient descent on the T234 instance (d=40, n=60, seed-234 G, step 1/20) have a cutoff below which every small initial scale alpha is captured by the outgoing family? Yes, conditionally (OPEN-T234l, 8 Nov): every 0 < alpha <= 10^-15566.

What changed from T234k: the absolute origin-error ball could never close (at p = 2150 its radius was 2e169 times the norm bound). T234l bounds the transverse error relative to alpha b r2^k, covers the whole incoming phase circle, carries the passage through 36050 updates with a triangular enclosure, and then a finite outgoing amplification A_out = 405307.18 over 23219 more updates. The cutoff is one scalar inequality, A_out [ D/(1000 delta) q^(N(p)-1) + (3/10) delta ] <= 1e-6, decreasing in p.

Numbers I rechecked myself (t234l_check.py, 60-digit mpmath from CUTOFF_CERTIFICATE.json): 9.988168726410012e-7 at p = 15566 (passes), 1.000080121e-6 at p = 15565 (fails the same majorant), 6.674e-7 at 16000, 5.032e-7 at 20000. audit.py and final_audit.py rerun pass; the planted wrong claim was flagged and the clean ones were not.

What is not settled: the constants gamma, log H, A_out, q and r_hi come from the author's enclosures under T234h's IEEE/dot-product model, with no outside referee. 15566 is where this majorant closes, not the real dynamical cutoff. Constancy of the outgoing excess and covariance along the family is still open (T234k's two enclosures only overlap).

Where: frontier row T234, folder 06_math_research/frontier/T234/open_t234l_agent_11_08, pushed 9cce5e30c2. Card claim_d49b2b471b3649d0b364057df3c3599e (depends on the T234k card claim_821cbbbb13f84762b54b551ac97fc171).

Related: [[t234k_two_enclosures_overlap_r_4p8e_21_k_constancy_cutoff_open_2026_11_08]] - the enclosures and the obstruction this replaces.

