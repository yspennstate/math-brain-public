---
name: p0434_suffix_netted_charge_fails_small_classes_gain_2026_11_08
description: "P0434 8 Nov 18:5x: per-class d_k on the worker machine law is [-0.69,-0.29,0.98,0.97,0]; the suffix netted form sum_{j>=k} d_j <= 1 fails at 1.95, the prefix form holds but equals R-1 there; a proof must pay large losers from the small classes' gains"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T18:53:37-05:00
  status: verified
  evidence: "codex_fleet/runs/own_p0434/netted_check.out"
---

P0434 (M-SERPT vs Gittins, Conj. 8.1 T_MS <= 2 T_G), 8 Nov 18:5x, an agent. Write d_k = p_k (T_MS,k - T_G,k) / T_G
with sizes ascending; the conjecture is sum_k d_k <= 1.

On the worker machine law (s [1, 1.1426, 2.1909, 2.1943, 17259], 1-rho 1e-6) the per-class split is d = [-0.6912, -0.2922,
0.9803, 0.9699, 0.0]: the two small classes GAIN under M-SERPT and the two near-2.19 classes LOSE. So the suffix form
sum_{j>=k} d_j <= 1 (charge the large losers alone against T_G) fails at 1.9502 (1.768 at 1e-5, 1.913 at 1e-7, 1.969
on the polished R 1.985 law). The prefix form sum_{j<=k} d_j <= 1 holds on every law checked, but its maximum sits
at the last class, where it equals R - 1, so on these laws it is the conjecture again and not a stronger lemma. A
10-start Nelder-Mead hunt (m 3-5, 250 evaluations each) found no interior prefix above the total. That search is weak
and is not a bound.

How to apply: a proof has to pay each losing large class out of the gains it causes in the small classes it jumps;
a charge that looks only at the losers, or only at the classes above a cut, is already refuted at 1.95. Scripts and
output: codex_fleet/runs/own_p0434/netted_check.py/.out, netted_prefix_hunt.py/.out, NOTE.md section 18:5x.
Related: [[p0434_gross_loss_lemma_is_false_mac_mini_law_1_95_2026_11_08]], [[p0434_prefix_lemmas_fail_because_mserpt_jumps_at_near_equal_sizes_2026_11_08]], [[p0434_no_cut_or_class_local_charge_one_class_can_be_111x_slower_2026_11_08]].

