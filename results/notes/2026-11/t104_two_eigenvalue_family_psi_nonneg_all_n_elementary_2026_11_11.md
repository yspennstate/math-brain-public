---
name: t104_two_eigenvalue_family_psi_nonneg_all_n_elementary_2026_11_11
description: "T104 Alon 2/3 two-eigenvalue family: is Psi >= 0 for every n? Proof written 11 Nov: n=5..13 cone certificate, n>=14 elementary (identity + Gram, m from the top or bottom pair, edge perturbation below eps ~ 2/n^2); read 11 Nov by an agent (no gap, Lean for steps 1-3) and a Codex referee (SOUND); gives Conjecture F on graphs with two Laplacian eigenvalues"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T08:11:44+02:00
  status: verified
  evidence: "all_n_check.py: scalar facts n=14..2000 exact, 22,260 vectors every step asserted exactly; all_n_check2.py 5,325 arbitrary vectors, four cases; split_dense.c n<=14 zero negative coefficients; readers 11 Nov: an agent no gap + Lean lean_checks_agent/t104_all_n 628d7761 (steps 1-3, N>=14); Codex referee gpt-6.1-sol high on worker machine 1 SOUND (AUDIT_CODEX_ALLN_REPORT.md); family_F_check.py direct Specht check n=5..7, 6,120 graphs"
---

T104 (G. Alon's 2/3 Specht-module conjecture, arXiv 2610.22151, Conj. 1.5), two-eigenvalue family: is Psi(x) >= 0 for every n? A proof is written (11 Nov 2026, an agent): n = 5..13 by the cone certificate, n >= 14 by a short elementary argument. Checked step by step in exact arithmetic; read on 11 Nov by two independent readers: an agent (hostile read, no gap, exact constants n = 14..3000, then Lean for steps 1 to 3, lean_checks_agent/t104_all_n, commit 628d7761) and a Codex referee on worker machine 1 (gpt-6.1-sol, high; verdict SOUND, AUDIT_CODEX_ALLN_REPORT.md). Continues [[t104_two_eigenvalue_family_n5_to_10_certified_aux_bound_fails_n14_2026_11_11]] and [[t104_psi_nonneg_one_positive_coordinate_all_n_2026_11_11]].

Psi = (n-4)(2q-1) - 2(n-3)p^2 + C m, C = (n-1)(n^2-6n+6+2nq), q = Q/T^2, p^2 = P^2/T^3, m = max_{i<j} x_i x_j / T.

The argument for n >= 14.
1. Identity: Psi = 2(n-3)(q - p^2 - 1/n) + C(m - 1/(n(n-1))), and q - p^2 >= 1/n is the Gram determinant of (1, x, x^2). So m >= 1/(n(n-1)) is enough.
2. Normalise x sorted, x_1 = 1 >= b = -x_n. If x_2 + x_(n-1) >= 0 put eps = x_2, M = x_1 x_2; otherwise eps = -x_(n-1), M = x_n x_(n-1). Either way all middle coordinates lie in [-eps, eps], so T <= 2 + (n-2) eps^2 and M/T >= 1/(n(n-1)) unless eps < about 2/n^2 (thresholds 2.1/(n(n-1)) and 2/((n-2)(n+1)); the star is the equality case of the second).
3. For eps that small x is a perturbation of the edge vector (1, 0, ..., 0, -1): the positive term C M T^2 is of order n^3 eps, the two negative terms are of order n eps (crude bounds 4Y2 + Y2^2 and (3(n-2)eps)^2 with Y2 <= (n-2) eps^2). With these constants (Y2 <= 0.002, first term under one hundredth of the main one) the argument closes from n = 13, not from 10 as first written here; with 0.005 and one fiftieth it closes from n = 10 (all_n_remark2_check.py, exact). The referee found this.

What made it work, after a day of cone certificates: the bound for m does not have to be one polynomial. The pair (x_1, x_2) or (x_n, x_(n-1)) gives m directly, and the only region where that is below 1/(n(n-1)) is a neighbourhood of the edge of radius 2/n^2, where first-order perturbation is enough. The polynomial lower bound Phi' for m (which fails at n = 14) and the power-mean bounds (fail from n = 14 and n = 30) were the wrong tool; the identity in step 1 was already in hand and the question to ask was "where exactly is m small".

Independent evidence: the split certificate (T^3 Psi_A on {x_2 + x_(n-1) >= 0}, T^3 Psi_B on the complement, in extreme-ray coordinates) has no negative coefficient for n = 5..14 at least (split_dense.c on worker machine 2; sympy to n = 11; an agent separately to n = 10).

Files: 06_math_research/t104_alon_agent_2026_11_11/ GAP_STATE_FORM.md (section "Psi >= 0 for every n"), all_n_check.py, all_n_check2.py, split_dense.c, split_rays.py, split_dense_status.txt. What would change it: a reader who breaks step 2 (the bound for b in case II) or the constants of step 3; what the family means for the conjecture itself is in the first memory of the chain.

Referee repairs (08:42, all applied in the note, marked [referee]): the normalisation must sort again after x -> -x; the comparisons of step 3 needed a monotonicity argument in n (supplied, four lines) and eps = 0 apart; the two equality vectors (edge, star) are the only ones. So every n >= 5 has two independent checks: n = 5..10 the cone certificate by two programs, n >= 10 the argument with the repaired constants, n >= 14 the printed constants (two readers and Lean).

What it gives (same note, section "What Psi >= 0 gives"): Conjecture F, lambda_min(G,[2,1^(n-2)]) >= ((n-2)/(n-1)) lambda_min(G,[2,2,1^(n-4)]), for every weighted graph on n >= 5 vertices whose Laplacian has spectrum {0, mu (n-2 times), lam}, that is w_ij = c - g x_i x_j. The family has dimension n and contains both equality cases. Checked directly with Specht modules for n = 5, 6, 7 (smallest ratio exactly (n-2)/(n-1), at the star). Conjecture F in general and Alon's Conjecture 1.5 stay open: row T104 is not solved.

Lesson: a side remark gets the same exact check as the theorem. The line about n = 10 was written from the size of the margin at n = 14 without rerunning the constants, and it was the one wrong statement the referee found.

Later the same day (09:16): an agent formalised the whole theorem for n >= 14 in Lean, normalisation included (T104Full.psi_nonneg, 06_math_research/lean_checks_agent/t104_all_n_full, commit 952215e, standard axioms).
