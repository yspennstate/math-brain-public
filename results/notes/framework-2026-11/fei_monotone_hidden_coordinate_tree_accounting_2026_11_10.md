---
name: fei_monotone_hidden_coordinate_tree_accounting_2026_11_10
description: "FEI: which coordinate is good in a monotone function? No rule: f = MAJ_k(y) OR (x AND [y >= y0]) has E_x/Inf_x about k/2 (exact to k = 17), x in a shortest term and, after composing with MAJ_m, the largest influence. Use tree accounting: one tree with good AVERAGE node cost gives FEI; best good-coordinate constant = FEI constant"
metadata:
  node_type: memory
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T07:23:39+02:00
  status: provisional
  evidence: ""
  modified: 2026-11-10T18:52:31.379Z
---

Status: provisional (exact computations and short identities of mine, 10 Nov 2026; no referee).

Setting: E_i = H(1[i in U] | U - i) = sum_T Phi(g^(T)^2, h^(T)^2), g = E_i f, h = D_i f; a coordinate is good when
E_i <= C Inf_i; FEI <=> every Boolean function has a good coordinate
([[fei_equivalent_to_erasure_entropy_one_good_coordinate_2026_11_10]]).

1. A monotone function with a bad coordinate. f(x, y) = MAJ_k(y) OR (x AND [y >= y0]), k odd, |y0| = (k-1)/2.
   D_x f = 1[y = y0], Inf_x = 2^-k, and E_x/Inf_x = 3.5231, 4.2427, 4.9888, 5.7834, 6.6185, 7.4829, 8.3685, 9.2699
   at k = 3, 5, ..., 17: about k/2 = (1/2) log2(1/Inf_x). x lies in a shortest term. The y variables have
   E/Inf -> 0, so the function itself is harmless (H/I 1.9 to 2.4).
2. Composition. Replacing each y_j by a balanced function phi of fresh variables leaves E_x and Inf_x exactly
   unchanged (the ratio g^/h^ at S depends only on which blocks S meets; Phi is homogeneous). Checked exactly with
   phi = MAJ_3 at k = 3, 5, 7 and MAJ_5 at k = 3. With phi = MAJ_m, m of order 4^k / k, x becomes the unique
   largest-influence coordinate. So for monotone functions too: "the largest-influence coordinate is good" is
   false (ratio about (1/4) log2 n) and "every variable of a shortest term is good" is false. (FEIB21 had the
   first for non-monotone functions, [[fei_is_edge_entropy_of_the_spectrum_largest_influence_can_be_bad_2026_11_10]].)
   CORRECTION (10 Nov 09:3x): the failure of "the most influential coordinate is good" by composition was
   already in our record on 24 Sep, [[fei_most_influential_coordinate_fails_by_composition_2026_09_24]]
   (Prop 7.2); this entry adds only the monotone instance.
3. For majority, E_i = 0 at every coordinate (E_i f is odd, D_i f is even: disjoint Fourier supports). E_i is not
   bounded below by a multiple of Inf_i.
4. sup_f min_i E_i/Inf_i = sup_f H/I: the best constant in "some coordinate is good" is the FEI constant
   (min_i E_i/Inf_i <= sum E_i / sum Inf_i <= H/I by Han; the converse by the path formula). Lower bound 6.5218.
   CORRECTION (10 Nov, FLOW 12(w) item 1): equality is NOT proved. The path formula loses the J terms, so what
   holds is C* - 2/ln 2 <= G* <= A* <= C* with G* = sup_f min_i E_i/Inf_i, A* = sup_f sum_i E_i / I, C* = sup H/I.
   [UPDATE 10 Nov 09:40: the best explicit value is now 4.50505, the alternating-sign PM(K33) tower, computed exactly
   by code/sym_enum.py; see [[fei_round8_local_dictionary_refuted_towers_4505_relative_cost_2026_11_10]]. The figure on
   the next line is the earlier same-sign tower.]
   Best explicit value of G* and A*: 4.47499 (computed exactly by code/tower_audit.py, FLOW 12(y) item 4:
   depth-five tower of the 9-variable perfect-matching function,
   [[fei_step_ratio_towers_4475_referee_2026_11_10]]); 6.5218 is a lower bound for C* only (computed, earlier
   record [[fei_solve_plan_up_ratio_form_h_le_2b_plus_2i_2026_11_09]]).
5. Tree accounting. H(f) = (1/2) H(f_0) + (1/2) H(f_1) + J_i + E_i and I(f) = (1/2) I(f_0) + (1/2) I(f_1) + Inf_i with
   J_i <= (2/ln 2) Inf_i. So for any decision tree reading all variables H(f) = sum_v P(v)(E + J)(v) and
   I(f) = sum_v P(v) Inf(v): FEI for f needs ONE tree with sum_v P(v) E(v) <= C I(f). Bad nodes may be paid for by
   other nodes; in example 1 the y nodes pay for x many times over.
6. Divergence form: E_i/Inf_i = log2(1/Inf_i) - D(pi_h || nu) + O(1), pi_h the normalised spectrum of D_i f, nu
   the law of U - i. Good means g^(T)^2 <= K h^(T)^2 for typical T ~ pi_h.

7. Power weights (added 10 Nov 20:5x, an agent, FLOW 12(cc)): sum_i Inf_i^a E_i <= C sum_i Inf_i^(a+1) fails on
   monotone f for EVERY a != 0. FEIB31 had a < 0 and a > 1; substituting Ben-Or-Linial tribes (not majority) under
   the hidden coordinate of item 1 closes 0 < a <= 1: a biased substitution lemma keeps E_x, Inf_x (they become the
   p-biased values, p -> 1/2), and the leaves' sum of Inf^(1+a) is at most 2^(1+a) k w 2^(-a w) -> 0. Checked to 12
   digits against full truth tables (code/wa_tribes*.py). a = 0 is A*, i.e. FEI. Sharper (21:3x, FLOW 12(dd)): the
   same construction kills every g(Inf_i) with g(t) log(1/t) -> 0 and nothing at or above Talagrand's weight 1/log(1/t)
   (Talagrand keeps the right side >= c Var). Closed 22:1x (FLOW 12(gg)): Maj_m o psi (psi balanced) scales E_i
   and Inf_i by the same tau_m, so every slowly varying g (log(1/t)^-b for any b, constants) has C_g >= G(psi): a
   weight in Inf_i alone is false or no easier than the unweighted bound.

How to use: do not look for a rule that names a good coordinate from influences or term sizes; look for an
averaged (tree or sum over i) inequality. Codex workers FEIB23-25 (launched 10 Nov 07:18) are briefed on this form.

What would change this: nothing in 1-3 (exact); 4-5 are identities.

Where: the private repository, 06_math_research/fei_solve_2026_11_09/FLOW.md section 12(u);
code/mono_hidden.py, code/mono_hidden_comp.py.


Referee (an agent, 10 Nov 22:5x): items 1 and 3 reproduced with separate code (k = 3..15 ratios equal to four decimals, Inf = 2^-k; MAJ_3/5/7 E_i = 0); item 2 reproduced on MAJ_3 at k = 3 only (E, Inf equal to ten digits). Files: 06_math_research/fei_solve_2026_11_09/audit_agent/MONOTONE_BAD_COORDINATE_REFEREE_2026_11_10.md (594df103).

LIMIT (10 Nov 23:1x, FLOW 12(hh)): the 12(gg) closure lifts BALANCED psi only. n=6 monotone: sup G 3.031 overall, 1.784 balanced. For biased psi the composition identity holds with mu-biased outer coefficients and E' = E minus the (empty, {i}) pair Phi(mu^2, fhat(i)^2), 31 pct of the n=6 leader's E (checked to 6e-17, code/biased_comp_check.py). One Maj_3 lift raises the leader 3.031 -> 3.072; iterating drives mu to -1 and G to 2.914, so majority is not the biased lift; gates with an interior fixed point are (the 4.5064 towers). Multiplexer balancing drops it to 1.608. Do not re-try these two balancing routes.
