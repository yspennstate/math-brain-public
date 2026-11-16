---
name: t249_ntk_lambda_min_constant_is_koenigs_function_of_correlation_map_2026_11_01
description: T249: NTK lambda_min = kappa L chi_1^L in the ordered phase, kappa = (K/chi_1) lambda_min(-P A P) with A the Koenigs function of the correlation map; matches the exact recursion to 1e-5
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T19:03:04+04:00
  status: provisional
  evidence: "frontier T249 moves 281a8bd4, files ec0ea6f1 (kappa.py, kappa_s12.txt, kappa_s15.txt)"
---

T249 (trainability depth at the edge of chaos), 1 Nov 2026, an agent, move m249b.
In the ordered phase the infinite-width NTK Gram's smallest eigenvalue is kappa L chi_1^L (1 + O(1/L)) with
kappa = (K/chi_1) lambda_min(-P A P), K = chi_1 q* + sw2 q* E[phi''(sqrt(q*) z)^2] q*/(1 - chi_1), and A_ij = lim (1 - c_ij^l)/chi_1^l:
the Koenigs eigenfunction of the correlation map at c* = 1, applied to each pair. It matches the exact recursion to 1e-5 at sw2 1.2
and 1.5 (tanh, sb2 0.05, 8 inputs). The factor L is a double root: the forcing decays at the recursion's own rate chi_1.
Practical: the earlier measurement looked unconverged (0.192 at L 400) only because of a b/L term (b = -2.66). Extrapolating kappa + b/L
from three depths recovers the limit (0.19886).
Proof gaps: the O(om^2) remainders; strict conditional negative definiteness of A for distinct inputs.


ADDENDUM (1 Nov, m249c): kappa > 0 for distinct inputs (d >= 3, sb2 > 0). The correlation map is a power series with nonnegative
coefficients and F(1) = 1, so A = sum a_k (1 - c^k) with every a_k > 0 (a_1 is a convergent product; A(F(F(c))) = chi_1^2 A(c) pushes
positivity to every m). Chen-Menegatto-Sun then makes A strictly CND. Checked for tanh to degree 40. PREREG36 PASS. Owed: existence of
the coefficient limits, and the O(om^2) remainders.
Reusable: "nonnegative-coefficient series closed under composition" turns positivity questions about deep kernel recursions into
Schoenberg / Chen-Menegatto-Sun statements.

ADDENDUM 2 (1 Nov, m249d): the two owed steps are now written out in the row's dossier, unrefereed. The coefficient limits exist:
H_l = (F^l - F^l(0))/chi_1^l has nonnegative coefficients and H_l(1) is bounded, so the family is bounded on the closed disk, and
pointwise convergence on [0, 1/2] gives locally uniform convergence by Vitali, hence the coefficients by Cauchy. The O(om^2)
remainders are geometric, sum to the O(1) matrix B, and give the measured b/L. A Schur-complement step passes from -P D P to the full
Gram. With this, Target 1 is settled at fixed n in sharp form: lambda_min = kappa L exp(-L/xi_c)(1 + O(1/L)), kappa > 0 (sb2 > 0, d >= 3).
Not covered: n growing with L, sb2 = 0, finite width.
sb2 > 0 is no restriction: with sb2 = 0 and odd phi there is no ordered phase of this kind (sw2 < 1 sends q_l -> 0 and the map to the identity), and f(-x) = -f(x) makes the Gram singular at every depth for inputs with two antipodal pairs.
