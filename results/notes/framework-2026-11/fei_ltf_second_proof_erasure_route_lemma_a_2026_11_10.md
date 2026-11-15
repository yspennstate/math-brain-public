---
name: fei_ltf_second_proof_erasure_route_lemma_a_2026_11_10
description: "FEI for threshold functions by the erasure / good-coordinate route? Proved 10 Nov (second proof; class already ours since 23 Sep, 14.22): restrict the heaviest coordinate, level witness, Lemma A (window comparison, constant 2), Cross-Stay via refreshing a random set. Single-set local witness is not universal."
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T04:04:35+02:00
  status: provisional
  evidence: ""
---

Does the good-coordinate (erasure) method prove FEI on a whole class end to end? Yes, on linear threshold
functions (10 Nov 2026, session an agent). It is a SECOND proof: the class was already settled here on
22-23 Sep 2026 by the rank argument, H <= 14.22 I ([[fei_holds_for_linear_threshold_functions_rank_argument_2026_09_23]]),
and the October preprint is cited at 8.937. Nothing here is a new class. What is new is the route and two tools.

The route (FLOW.md section 11 in 06_math_research/fei_solve_2026_11_09, commit fc812efd1328 of
brain-repo):
1. f = sgn(w.x - theta), restrict the coordinate of largest weight w_1. With s = w'.y - theta and the slab
   S = {|s| < w_1}: D_1 f = 1_S, E_1 f = sgn(s) 1_{S^c}, Inf_1 = P[S] = delta.
2. Level witness: E_1 <= sum_k Phi(A_k, B_k), A_k, B_k the level weights of E_1 f and 1_S.
3. Two-sequence lemma: if A_{>=K} B_{<=K} <= M delta^2 for all K then sum_k Phi(A_k, B_k) <= (1/ln 2 + 4 +
   2 log2(1 + 2M)) delta.
4. Noise form: A_{>=K} B_{<=K} <= 6.33 (delta + 2 Cross_rho) Stay_rho at rho = 1 - 1/K (rho = 1/2 for K = 1),
   Stay = P[y, z both in S], Cross = P[s(y), s(z) on opposite sides of S].
5. Cross-Stay: Cross_rho Stay_rho <= M_cs delta^2 for every rho. Proof: refresh a random set T (independent of
   y); given T and the rest, s(y), s(z) are a constant plus two independent copies of a symmetric sum U over T
   with steps <= w_1. Cross <= 2 P[U > w_1 + |const|] <= (32/3)(1 + sigma_T/w_1) P[y in S | T, rest] by Lemma B;
   Stay <= delta E min(1, K_0 w_1/sigma_T) by Kolmogorov-Rogozin. The two factors cancel.

LEMMA A (reusable). R = sum w_j eps_j with 0 < w_j <= a. For 0 <= c <= alpha:
   P[alpha <= R <= alpha + a] <= 2 P[c - a <= R <= c + a]   (closed intervals; open ones fail for R = a eps).
Induction on the number of steps; the only case with work is centre c < w, handled by the symmetry of the
shorter sum and a split of the interval at e - a. Holds for any independent symmetric summands bounded by a.
LEMMA B. P[R > t + a] <= (16/3)(1 + sigma/a) P[|R - t| <= a] for t >= 0 (Levy + Chebyshev + Lemma A).

Checks: exact enumeration, 600 weight sets, n <= 13: Lemma A ratio max 1.0000 (bound 2), Lemma B 0.4551
(bound 16/3). Cross Stay/delta^2 <= 0.4609 by dynamic programming at n up to 401, 22 cases. Level witness at
the largest weight <= 2.73 Inf_1 at n = 14-20. The proof was re-derived once after writing; no second reader
yet (owed: a Codex referee), and not yet compared line by line with the September proof.

What it does NOT do. The criterion extends to any Boolean f and any i (Stay = both points i-pivotal, Cross =
E_i f changes sign), and to noise on a subset N (local form: (L0) E[P[i pivotal | x off N]^2] <= M Inf_i^2 and
(L1) Cross^N Stay^N <= M Inf_i^2 give a good coordinate). Full noise fails for tribes; N = the tribe works.
On the hill-search worst cases (n = 6-10, which turn out to be tribes of width 2 and OR-AND-OR) the best
single-set witness is within 0.25 of E_i/Inf_i. But a single set N cannot be universal: for an AND of w
majorities the best single-set witness loses about log w (hand estimate, not run). A statistic with one
count per scale is needed, and for general f nobody knows the scales. So this is a method test, not progress
on the general conjecture by itself.

Scar from this session: I called the class open after a web search and worked two hours toward "a new
theorem" before recalling the brain, which held the September proof. Recall the brain on a class before
investing in it; the outside literature is not our record.

