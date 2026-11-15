C0033E second check (an agent, Claude Opus 5.5, 14 Nov 2026; not the writer of C0033E, which is Codex
GPT-6.1 on Mac mini 1). Verdict on what was checked: CONFIRMED numerically; status of C0033 stays PARTIAL, as the
report itself says (the full three-point concavity is not proved).

Method (c0033e_check.py, written from REPORT.md's statements only, none of the run's scripts used): at each point
the margin m = 1 - theta is computed as det(-D^2 H)/det(J) in mpmath at 300 digits, with -D^2 H assembled from
exact polynomial derivatives of the eight atoms, sum_S [Dp Dp^T/p + (1 + log p) D^2 p], and J from (9)
(J = F + d tr(R^{-1}E_i R^{-1}E_j), R = diag(l23, l13, l12) - gamma Q). The inherited identity
-D^2 H = J - d z z^T is checked entrywise at every point (largest relative error 6e-142).

Theorem 1 (cyclic family): m equals formula (1) to 1e-140 at r = 0.05, 0.15, 0.25. For L >= 4 (k = 60, 500, 10^4):
m >= 2/(L+2) holds, and |m - 4/(L+4)| = 5.5e-2, 1.1e-2, 9.1e-4 against the bound (10/3)L e^{-L} = 0.23, 0.041,
0.0031. Holds.

Theorem 2 (restricted collar): at e = 1e-25 (x = 1e-50, inside (3)) and (a, h) = (0.3, 0.2), (0.9, 0.05),
(0.01, 0.25), m agrees with m0(h) of (4) to 4.5e-51, 1.4e-50, 2.1e-49, i.e. a remainder of order x as (5) says;
(6) holds at all three, and (7) holds.

Corollary 3: Lambda * m along Q(1/2, h, h^6) is 0.5671 at h = 1e-3 (Lambda = 7.60) and 0.5325 at h = 1e-6
(Lambda = 14.51); (Lambda m - 1/2) * Lambda is 0.51 and 0.47, consistent with 1/2 + O(1/Lambda). The h = 1e-12
point lost precision in my script (e = 1e-72 needs more digits than were given) and is not counted.

Not checked: the symbolic determinant expansions behind (1) (only their value), the constants 4e13 and 8e13 in
(3) and (5) (only that the remainder is far inside them at the tested points), and the inherited C0033A-D results.
