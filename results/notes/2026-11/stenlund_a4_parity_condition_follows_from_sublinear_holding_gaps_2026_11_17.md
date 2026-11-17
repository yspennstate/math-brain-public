---
name: stenlund_a4_parity_condition_follows_from_sublinear_holding_gaps_2026_11_17
description: "[PROVISIONAL] CN0510: Stenlund's A4 (Csaki-Foldes Thm 15 (iii)) holds when sites with p_j<=1/2-delta have sublinear gaps; spectral bound via killed lazy walk; (i) implies (iii)"
metadata:
  type: project
  created: 2026-11-17
  created_at: 2026-11-17T01:52:52+02:00
  status: provisional
  evidence: ""
---

Result (unaudited, 17 Nov 2026, an agent). Y birth-death chain, +-1 w.p. p_j, hold 1-2p_j. Lemma: S(n)=sup_N sum_{m=n}^N [P(Y_{2m+2}=0)-P(Y_{2m+1}=0)] <= 2 sum_{m>=n} R^{2m}(0,0), R(j,j)=p_j, R(j,j+-1)=p_j/2 (proof: reversible for pi=1/p, spectral measure of 1_0, negative spectrum only, |l|<=(1-l)/2, conjugate by diag((-1)^j)). R^k(0,0) <= E[(1-2delta)^{time lazy SRW spends on D}], D={p_j<=1/2-delta}; gaps O(M^theta), theta<1, give stretched-exponential decay. Csaki-Foldes Theorem 15 (i) (gamma>1, any eta>0) implies the gap condition, so (iii)=A4 is redundant; every periodic walk with some p_j<1/2 satisfies it (their Q6). A4 as printed in arXiv 2302.10041 p.5 has weight sqrt(n), signed sum. Open: Stenlund's A4<=>aperiodic for sparse holding sites (one defect: numerics say A4 holds, bound too weak). Files: loops/72de1487_loop_1115/cn0510/NOTE.md, check.py. status: provisional. Related: [[open_problem_catalogue_1128_probability_networks_computation_2026_11_16]] [[grimmett_holmes_q74_one_removed_map_bonferroni_criterion_2026_11_17]]
