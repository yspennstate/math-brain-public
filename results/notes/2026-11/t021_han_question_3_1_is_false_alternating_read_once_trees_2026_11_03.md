---
name: t021_han_question_3_1_is_false_alternating_read_once_trees_2026_11_03
description: [PROVISIONAL] T021 FEI: is Han's Question 3.1 (some k with sum_{S not ni k}|f^(S)f^(S+k)| <= c I_k) true? No - alternating read-once AND-OR trees give Q_k = 2L - 4 sum p_l >= (log2 n)/3 at every k; landed brain main 508cb8d8
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T03:27:05+02:00
  status: provisional
  evidence: ""
---

Han 2312.08271 Question 3.1 (3.18), = GMP 2606.00246 inequality (3) at the split variable, is FALSE, even for monotone read-once formulas. Tree with fan-ins s_1..s_L, p_0 = 1/2, p_l = (1-p_{l-1})^{s_l} (= Pr level-l output true). Every coordinate: Q_k = 2L - 1 - 4 sum_{l<L} p_l - 2 p_L + |1-2p_L| (= 2L - 4 sum p_l when p_L <= 1/2). One-level step Q' = Q + 2mu - |c0| - 2p' + |1-2p'|, from the block-product factorisation (sum of g^2 = E g = mu) and |f^({k})| = I_k for unate f. Fan-ins least with p_l <= 1/4 give s_l <= 8, n <= 8^L, Q_k >= L >= log2(n)/3. Exact truth-table check on 15 trees n <= 16 (closed form = recursion = Fraction); L = 40 gives Q_k = 45.6. L=1 is AND (Han c>=2), L=2 is tribes (the >=4 card). Not in conflict with GMP Thm 6.8 (K=8, tribe-separated: depth-3 trees are not). This refutes only the sqrt(ab) relaxation; FEI holds for read-once formulas (O'Donnell-Tan) and Han's sharper (3.17), E sum a log(b/a) = O(I_k), is untested on these trees - next step. Priority searched 3 Nov, nothing found; a paper-worthy note if it survives a referee read. Files rows/T021/exp/q31/q31_iterated.*, card local_agent_T021_han_question_3_1_negative_alternating_read_once_trees_20261103, edges 2-3. Status provisional until someone else re-derives the one-level step. [[t021_han_question_3_1_constant_at_least_4_tribes_2026_11_03]]
