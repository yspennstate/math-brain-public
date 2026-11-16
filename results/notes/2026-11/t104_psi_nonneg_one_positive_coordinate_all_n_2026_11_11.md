---
name: t104_psi_nonneg_one_positive_coordinate_all_n_2026_11_11
description: "T104 Alon 2/3 conjecture two-eigenvalue family: Psi >= 0 proved for EVERY n when x has exactly one positive (or one negative) coordinate, by reducing a sextic in sorted increments to at most six levels with symbolic multiplicities; left: two or more of each sign, n >= 14"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T07:44:41+02:00
  status: provisional
  evidence: "one_positive_all.py: 12 forms (r=1..6, two shapes), no negative coefficient in shifted multiplicities; one_positive_all_check.py 311 exact evaluations and 20,000 exact random vectors n<=60, 0 negative; one reader"
---

T104 (G. Alon's 2/3 Specht-module conjecture, arXiv 2610.22151, Conj. 1.5), two-eigenvalue family: is Psi(x) >= 0 when x has exactly one positive coordinate? Yes, for every n >= 5 (11 Nov 2026, an agent). One reader so far. Continues [[t104_two_eigenvalue_family_n5_to_10_certified_aux_bound_fails_n14_2026_11_11]].

Statement. x in R^n, sum x = 0, exactly one positive (or exactly one negative) coordinate. Then Psi(x) = (n-4)(2q-1) - 2(n-3)p^2 + (n-1)(n^2-6n+6+2nq) m >= 0, with q = sum x^4 / T^2, p^2 = (sum x^3)^2 / T^3, m = max_{i<j} x_i x_j / T, T = sum x^2.

Proof in three lines. x = (a, -y_1, ..., -y_(n-1)), y sorted decreasing, a = sum y; then m T = y_1 y_2 and G = T^3 Psi is a sextic form in the increments w_i = y_i - y_(i+1) >= 0, which are free variables. A degree-6 monomial touches at most six increments, and its coefficient is the same after the others are set to zero, which leaves a vector with r <= 6 distinct nonzero levels of multiplicities c_1..c_r and j zeros. So the coefficients for ALL n sit among those of twelve forms G_r(z; c, j) (r = 1..6; c_1 = 1 or c_1 >= 2), polynomial in the multiplicities; in g_s = c_s - 1 and j none has a negative coefficient (sympy sparse ring; r = 6, c_1 >= 2 takes 223 s on the workstation). Checked: 311 random exact evaluations against the definition, 20,000 random exact one-positive vectors up to n = 60.

The method, reusable: an inequality for a homogeneous polynomial of degree d on a simplicial cone whose free coordinates are increments of a sorted vector, with n as a parameter, reduces to at most d levels with symbolic multiplicities; nonnegative coefficients in the shifted multiplicities prove it for every n at once. This is what replaced the per-n cone certificates (which stop at n = 13 because the auxiliary bound Phi' fails at n = 14).

What is left for the family: at least two coordinates of each sign, n >= 14, at least fourteen nonzero coordinates, four or more values, m < 1/(n(n-1)). There m T = max(x_1 x_2, x_n x_(n-1)); the sorted sum-zero cone is still simplicial (rays (n-k) x k, (-k) x (n-k)), so any lower bound for m T that is polynomial on a finite subdivision of it would settle all n by the same finite check.

Files: 06_math_research/t104_alon_agent_2026_11_11/ GAP_STATE_FORM.md (last section), one_positive_all.py, one_positive_all_check.py, one_positive_all_r4_6.out. What would change it: a second reader of the reduction (does setting the other increments to zero really give the listed level vector with y_1 y_2 as stated) and a rerun in another system.

