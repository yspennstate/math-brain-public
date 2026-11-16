---
name: fei_restriction_step_on_symmetric_functions_stays_below_4_87_bits_2026_11_08
description: "[PROVISIONAL] FEI T021 8 Nov 05:1x: over symmetric Boolean f the GMP (arXiv:2606.00246 eq.21) step Delta_1/I_1 is at most 4.8677 bits, max at n=3 (OR3); exhaustive n<=16, climbs to n=64 give 4.0-4.2; far below the 7.05 general floor (claim_d15d0160)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T05:16:43-05:00
  status: provisional
  evidence: ""
---

Exact (Krawtchouk, integer sums) over all symmetric f with n <= 16: max Delta_1/I_1 in bits is 4.8677 at n = 3, by the table that is -1 only at weight 0, and between 4.0 and 4.75 for n = 4..16. Hill climbs at n = 24, 32, 48, 64 gave 4.21, 4.01, 4.16, 4.00; at n = 14 the climb found the exhaustive maximum. Brute-force Walsh sums agree on four tables. For symmetric f every coordinate is alike, so the some-m form of González-MacManus-Pereyra eq. (21) and the every-m form coincide; it appears to hold there with K = 4.8677, below Numaro's 6.5218 FEI floor and the 7.05 step floor from self-compositions ([[fei_opus_wave1_reduction_small_influences_gates_and_ltf_2026_09_23]], card claim_dc05672a). No proof. Repo the private brain repository: 06_math_research/frontier/T021/fei_sym_agent_2026_11_08 (a3a828ae).

**Why:** the large step ratios in the store all come from a distinguished coordinate or point; symmetry removes that, and the data say symmetric functions are not where extremal steps live.
**How to apply:** do not search symmetric or threshold-only families for FEI step counterexamples; look at compositions with one special coordinate. A proof of the symmetric bound would give FEI for symmetric f with an explicit 4.87 (O'Donnell-Wright-Zhou proved it with an unspecified constant). Related: [[fei_pair_cost_and_restriction_deficit_differ_by_at_most_3_i_2026_11_08]] [[fei_most_influential_coordinate_fails_by_composition_2026_09_24]]

Checked 05:3x against O'Donnell-Wright-Zhou (ICALP 2011): they prove FEI for symmetric f with C = 12.04, and for read-once decision trees with C = 4.88, where 4.88 is the sup of their root-step function ell(r) = (2-h(r))/(1/2-r/2) (sup 4.8723 at r = 0.541). Our symmetric maxima at n = 3,4,5,6,8,9,10,13 are OR_n, and those values are exactly ell(1-2^(2-n)) (4.8677 = ell(1/2)), so the maximum itself is OWZ's known root step, not a new number. New is only the measurement that no other symmetric table beats it up to n = 16. The open statement: Delta_1 <= 4.8723 I_1 for all symmetric f, which by induction would cut the symmetric FEI constant from 12.04 to 4.88 (lower bound 4). owz_ell.py, commit 0c9c40e0.
