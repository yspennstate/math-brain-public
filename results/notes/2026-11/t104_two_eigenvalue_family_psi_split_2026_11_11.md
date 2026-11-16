---
name: t104_two_eigenvalue_family_psi_split_2026_11_11
description: "T104 Alon 2/3 conjecture, two-eigenvalue family of the gap-weighted form: Gval = 2g^2 Psi and Psi = K((n-1)m - 1/n) + 2(n-3)D with K > 0, D >= 0 a Cauchy-Schwarz defect; Psi >= 0 open only for m < 1/(n(n-1)); numerically min 0 at the star, and an average over one prefix set suffices"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T03:57:24+02:00
  status: provisional
  evidence: "GAP_STATE_FORM.md, psi_split_check.out, psi_threshold_check.out in 06_math_research/t104_alon_agent_2026_11_11; second reader agent brain main 5c3b3e24"
---

T104 (G. Alon, arXiv 2610.22151, Conjecture 1.5), third round, 11 Nov 2026. Candidate work by one author; one independent reader (an agent) has checked the identity and searched for a negative value. Nothing here is proved beyond the algebra.

What it is. In the gap-weighted state form of Conjecture F (GAP_STATE_FORM.md), take the two-eigenvalue family: x a unit sum-zero vector, weights w_ij = (lam - g)/n - g x_i x_j, Laplacian lam x x^t + (lam - g)(Pi - x x^t), smallest admissible lam = g(1 + n m) with m = max_{i != j} x_i x_j. The star and the single edge lie in it and both equality cases are of this form. Then

    Gval = 2 g^2 Psi(x),  Psi = (n-4)(2q - 1) - 2(n-3) p3^2 + (n-1)(n^2 - 6n + 6 + 2nq) m,   q = sum x^4, p3 = sum x^3.

The split (exact). With K = n^2 - 6n + 6 + 2nq and D = q - 1/n - p3^2,

    Psi = K((n-1) m - 1/n) + 2(n-3) D,

K >= (n-2)(n-4) > 0 for n >= 5 and D >= 0 (Cauchy-Schwarz defect of p3 = <x, x^2 - 1/n>; D = 0 iff x takes two values). So Psi >= 0 as soon as m >= 1/(n(n-1)); the star sits exactly at m = 1/(n(n-1)), D = 0. Open region: m < 1/(n(n-1)), claim K(1/n - (n-1)m) <= 2(n-3)D.

What the numbers say. Minimum of Psi over x is 0 for n = 4..8 (two independent codes). Replacing m by the mean of x_i x_j over the pairs inside one set A and keeping q, p3 exact, the minimum over x of the best A is still 0 (all sets, n = 5..7; the k smallest or k largest coordinates only, n = 5..7 so far). Complements of one or two indices are not enough (negative at n = 6, 7).

Scar. The first proof attempt bounded m by the mean over all pairs of negatives and bounded q and p3 separately; it lost for 2/3 < u < (n-1)/n. The loss was the choice of pairs, not D: keep D exact and choose the set of pairs by x.

Where. the private repository, 06_math_research/t104_alon_agent_2026_11_11/ (GAP_STATE_FORM.md, two_eig_family.py, psi_split_check.py, psi_threshold_check.py and their .out files); independent check under 06_math_research/lean_checks_agent/t104_alon_n4/psi_referee/ (brain main 5c3b3e24).

What would change it. A vector with Psi < 0 (then the gap-weighted state does not prove Conjecture F even on this family), or a proof of the prefix-set inequality (then the family is done and the general case a lam + b >= 0 is the next step).

Added 11 Nov 04:5x (still candidate; the two reduction steps below were re-derived by an agent, who found no negative Psi for n = 5..12).
Bound for m in power sums. Take S = the coordinate of largest modulus, made positive by x -> -x, and c_i = S - x_i >= 0. Summing c_i c_j (m - x_i x_j) >= 0 over i != j gives m >= M = (1 - q + 2 S p3 - S^2)/(n(n-1)S^2 - 1), an equality at the star and at the edge. Then n(n(n-1)S^2 - 1) Psi >= Phi' = K N + 2n(n-3)(n(n-1)S^2 - 1) D with N = n(n-1)(1 - q + 2 S p3 - 2 S^2) + 1.
Concavity. For fixed S and n >= 5, Phi' is strictly concave in (q, p3), so it is enough to treat vectors with values S, possibly -S, and at most three others.
Scar. The relaxation of the other n-1 coordinates to a measure with fractional weights FAILS: Phi' is negative near S^2 = 0.41..0.44 (-2.79 at n = 5). On genuine three-valued vectors (S, s x k, t x (n-1-k)) Phi' >= 0 on a grid for n = 5..12, zeros only at edge and star. So a proof must use integer multiplicities; do not try the moment-space route again.
Shape of the problem. Both zeros of Psi are conical (Psi grows linearly away from the edge and from the star, because m moves at first order and q, p3^2 at second), so nothing delicate happens near them; what is missing is a global bound in the region n(n-1)m < 1, where x has at most one coordinate above 1/sqrt(n(n-1)) of each sign. The simplest averaged bound m >= (2 S^2 - 1)/((n-1)(n-2)) (all pairs outside the top coordinate) is tight at both zeros but is not enough on its own (with the pairs taken outside one or two fixed indices the minimum over x is negative at n = 6, 7); the set of pairs has to be chosen by x.
Files added: GAP_STATE_FORM.md sections 'A bound for m in power sums' and 'Where Phi' >= 0 can and cannot be proved', phi_boundary_scan.py/.out, phi_integer_scan.py/.out, psi_linear_weight_check.out (brain main a3cef1b42879).

Later, 11 Nov morning: superseded in part by [[t104_two_eigenvalue_family_n5_to_10_certified_aux_bound_fails_n14_2026_11_11]]. Psi >= 0 is now proved for n = 5..10 by a cone coefficient certificate and for any n with at most ten nonzero coordinates (zero padding); the auxiliary bound Phi' >= 0 used here is FALSE at n = 14 (y = (11, 1 x 11, -11, -11)), so the grid evidence for n = 5..12 above does not extend. A Codex referee found three wrong statements in the companion note HOOKS_AND_TWO_ROWS.md (corrected there).
