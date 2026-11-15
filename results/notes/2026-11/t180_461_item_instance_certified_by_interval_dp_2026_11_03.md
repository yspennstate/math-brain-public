---
name: t180_461_item_instance_certified_by_interval_dp_2026_11_03
description: T180 prophet secretary: is the 461-item instance below 0.7235 for real? Yes - own interval DP [0.7229334600126,..] + brute-force check of the symmetric DP; like-for-like with GMS 0.7235
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T03:50:24+02:00
  status: verified
  evidence: "~/loop_state_agent/t180_iv_400_30.out"
---

The 461-item two-cloud prophet secretary instance of T180 (400 prizes worth 1 w.p. 1e-9; 30 items worth 1.28233*400e-9 w.p. 0.2065/30; 30 items worth 1.38487*400e-9 w.p. 0.17698/30; one sure item worth 0.823*400e-9) has optimal-policy ratio V/E max in

    [0.722933460012600477658647124, 0.722933460012600477658647127]

computed in interval arithmetic (mpmath.iv, 100 bits, 141 s) by my own code, ~/loop_state_agent/t180_check.py (output t180_iv_400_30.out). Not cert.py: different loops and accumulation order, and intervals rather than 40-digit floats. It agrees with an agent's cert.py (0.7229334600126004776586471) to all 25 printed digits. Every operation is monotone in V (max, +, positive multiples), so the enclosure is honest; the decimal parameters are enclosed as intervals, so it bounds the instance with those exact decimal values.

The symmetric DP (state = prizes left, items of each cloud left, sure item left) was checked against a brute-force DP over all 2^n subsets of explicit items: n = 11 (k 6, m 2) equal to the last bit, n = 15 (k 8, m 3) to 1e-16. That checks the reduction from distinct items to counts.

Model: random arrival order, gambler knows every law and sees which item arrives, does not know the future order. That is the standard prophet secretary (the "order-unaware" setting of Giambartolomei-Mallmann-Trenn-Saona arXiv:2304.04024, whose bound is 0.7235); Bubna-Chiplunkar's 0.7254 (arXiv:2211.04145) holds even when the gambler knows the order in advance. So the comparison with 0.7235 is like for like. Best algorithm for this setting is 0.688 (Chen-Huang-Li-Tang arXiv:2411.01191), so 0.7229 contradicts nothing. Literature search 3 Nov 03:5x found no single-item random-order hardness below 0.7235 after v6 of 2304.04024 (Nov 2024).

What remains before a paper: the prose proof that the limit family is what the instance approximates is not needed (the finite instance is the bound); needed are a clean write-up, a check that the instance's tiny q is not an artefact (scale invariance: the ratio depends on q only through the first-order prize mass; recompute at q = 1e-12 to show stability), and a statement of the continuum value 0.72274 as numerics only. Candidate row in PAPER_CANDIDATES.md (T180).

Related: [[prophet_secretary_hardness_below_0_7235_two_value_cloud_2026_11_03]].

