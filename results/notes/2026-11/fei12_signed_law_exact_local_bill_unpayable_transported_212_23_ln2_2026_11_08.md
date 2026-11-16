---
name: fei12_signed_law_exact_local_bill_unpayable_transported_212_23_ln2_2026_11_08
description: "Does signed conditioning all the way down give the FEI reference law, payable by influence? Law yes; local bill no (420.6 nats at m=12, diverging); transported (212/23)ln2 on G_d, wrappers (FEI12)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T15:07:59+04:00
  status: verified
  evidence: "workers/FEI12; fei12_check.py/.out; frontier T021 383299cd14"
---

Can the FEI reference law be built by signed conditioning all the way down, with no FEI9 fallback, and can its bill then be paid by influence? The law, yes; a local payment, no; a transported payment, yes on the families tried (8 Nov, FEI12, Codex, reviewed by an agent).

Signed Walsh conditioning at every surviving overlap, with exact multiplication at disjoint gates, gives the true Fourier spectrum. But the sum of local conditioning increments cannot be paid by influence measured in the whole function. For AND_m AND MAJ3 with two repeated selectors the local sum stays ln4 while I = (m + 3/2) 2^-m, so the ratio grows like 2^m/m (420.61 nats at m = 12). A rare disjoint ancestor suppresses the lower majority's influence. Moving each bill through its disjoint ancestors by their pivotal factors fixes this: a constant (212/23) ln2 = 6.389 nats holds for every FEI10 G_d, any nesting of FEI11 wrappers, and disjoint AND/OR compositions with read-once formulas. All read-twice formulas, the gate bias terms and FEI itself stay open.

A correction to FEI11's review: the AND_k interface ratio H(AND_k)/(4 ln2 I) is 1 - (1 - 1/(2 ln2))/k + O(2^-k), which is 0.993034 at k = 40. The bound 0.9930 on k = 2..40 is slightly false, and the right uniform constant is 1.

My check (fei12_check.py, own code): the ratio matches the worker's k = 40 value to 34 digits. Brute-force influence of AND_m AND MAJ3 equals (m + 3/2) 2^-m at m = 3, 4, 6, and the m = 12 number reproduces. I did not recheck the law's proof or the 212/23 constant. The worker's two codes agree on 1,577,224 coefficients.

Frontier T021, pushed 383299cd14. Math card claim_5248c9f318b6436b997760ac8fddd6f1.

Related: [[fei11_signed_lift_fails_in_cofactor_fallback_interface_paid_2026_11_08]] - the fallback this removes, and the 0.9930 figure corrected here.

Later (8 Nov, FEI13): the bias half is paid, K <= 36(I-Var) for every formula; see [[fei13_disjoint_bias_paid_k_le_36_i_minus_var_no_read_bound_2026_11_08]].
