---
name: a_fast_fourier_sum_dropped_the_level_zero_term_near_the_middle_2026_11_08
description: "[VERIFIED] FEI T021 8 Nov 11:4x: the log-space Fourier sum for Delta_1/I_1 started at level 1, so it left out the mean term. Far out that term is exponentially small, but near the middle its I-share is the pivot probability, about 1/sqrt n, and it moved the ratio by up to 0.31 bits (n = 256). Caught when the sum disagreed with the exact entropy ratio near n/2."
metadata:
  node_type: memory
  type: feedback
  status: verified
  modified: 2026-11-08T16:47:58.421Z
---

`ratio_scaled` (sym_far_threshold_limit.py) and the first `ratio_win` (sym_crossover.py) summed over s = 1..N. The identity Delta_1/I_1 = sum_s C(N,s) D(a_s,b_s) / sum_s C(N,s)((a_s - b_s)/2)^2 runs over s = 0..N. The level-0 pair is the two restrictions' means. Their difference is 2p, with p the pivot probability, so level 0 holds a fraction p of I_1 and adds about p ln(1/p^2) to the ratio.

- Far out (alpha <= 0.3), p is exponentially small and the earlier far-limit table is unaffected.
- At t = n/2 - c sqrt n, the sum without level 0 ran low by 0.058 (c = 0), 0.31 (c = 0.5) and 0.095 (c = 1) bits at n = 256, and by 0.03 to 0.19 bits at n = 1024 (sym_level0_check.out). One crossover table went to GitHub this way (bd20673bd18). It was corrected in the next push, and its conclusion that every column tends to 0 still held.
- Level 0 needs a stable form. The means agree to within delta, so D = ph(delta/2) + (2 ln m^2 + 6) delta^2/8 + O(delta^4). The plain formula cancels to noise. With that form the sum matches the exact entropy ratio to 1e-11.

**Why:** a sum checked in one regime (far out, where it matched the exact ratio to 4 digits) was reused in another regime where a term it skipped is no longer small.

**How to apply:** when a fast formula moves to a new regime, rerun it against the slow exact one at the new parameters before using it. A frequency sum that starts at 1 should say why level 0 can be dropped there. Linked: [[fei_bulk_bound_for_any_edge_count_by_alternating_charge_energy_2026_11_08]], [[a_ratio_already_in_bits_was_divided_by_ln2_again_2026_11_08]].
