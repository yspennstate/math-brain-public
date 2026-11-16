---
name: t021_tree_bound_16p53_nats_lemma_a_accepted_recursion_5e_14_2026_11_03
description: [VERIFIED] T021 q31: uniform fan-in read-once tree bound D/I <= 16.53 nats accepted in full; recursion matches brute force to 5e-14; loose ~3.7x vs 4.53 seen
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T07:09:44+04:00
  status: provisional
  evidence: "06_math_research/frontier/rows/T021/reviews_agent/ADDENDUM_T021_1.md"
---

T021 (FEI row), q31 work committed 3 Nov 06:50 with no author move: sup D_k/I_k <= 16.53159 nats over alternating read-once trees with uniform fan-in per level (s_l >= 2), down from 32.31 by an analytic Lemma A (t(4 ln 2 + ln 1/t) <= Phi(1,t) <= t(3 + ln 1/t), both ends sharp). Reviewed by an agent 3 Nov 07:07 and 07:09 (moves 25-26 on T021): proof checked line by line; own code checks Lemma A to t 1e-20, the gain bracket (max 0.968 of the bound on 20,000 random inputs), B3 by summation and closed form; the block recursion matches brute-force truth tables on 19 trees to n 20 (worst 5.3e-14). Room: the largest D/I on random trees is 4.53, so the bound is loose by about 3.7x. Full FEI stays open.

Related: [[t240_cd_17p6_s2_71p7_explicit_rigorous_2000x_loose_2026_11_03]] (another explicit-but-loose bound reviewed the same morning).

Related: [[t021_split_cost_bounded_on_trees_where_question_3_1_fails_2026_11_03]] - the earlier q31 result whose numeric constant this review's Lemma A replaces.
