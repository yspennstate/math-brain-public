# Audit of agent B's next-order term under reshuffling with momentum and eps > 0 (T354, NOTE section of 20 Oct 04:2x)

Auditor agent A, 20 Oct 2026 04:3x. Verdict: CONFIRMED. The statement checked, with s = sqrt(B2), r = s/(s+eps),
p2 = s(eps+3s)/(4(eps+s)^2), H and K as in the momentum section, x0 = r d K B3/(2 B2):

    x*/x0 = 1 + d (r K - p2 T H/(r K B2 B3)) + O(d^2).

## By hand

psi(y) = (s+eps)/(s sqrt y + eps). With f = s sqrt y + eps, f'(1) = s/2, f''(1) = -s/4, psi' = -(s+eps) f'/f^2 and
psi'' = -(s+eps)(f''/f^2 - 2 f'^2/f^3), so psi'(1) = -r/2 and psi''(1) = s/(4(s+eps)) + s^2/(2(s+eps)^2) = s(3s+eps)/(4(s+eps)^2) = p2.
Finite differences agree to the printed digits at eps 1, 3, 10 (rr_eps_next_check_run1.txt).

E[m psi(y)] = x + psi'(1) E[m(y-1)] + (psi''(1)/2) E[m(y-1)^2] + O(d^3), and neither moment depends on eps: E[m(y-1)] = d K C/V and
E[m(y-1)^2] = Q = (d/B2)^2 T H + O(d^3) as in the eps = 0 momentum section (audited in AUDIT_NEXTORDER_RR_MOM). The cubic term is
O(d^3) under reshuffling for the same reason it is at eps = 0: E[(y-1)^2] is O(d^2) because each earlier epoch sums Z to zero. With
C/V = B3/B2 + 2x + O(d^2): x (1 - r d K) = r d K B3/(2 B2) - (p2/2)(d/B2)^2 T H, and dividing by x0 gives the stated bracket.
r and p2 move with V = x^2 + B2 only at O(d^2).

## Exact roots at points the peer did not run (rr_eps_next_check.py, rr_eps_next_check_run1.txt)

My exact solver (rr_exact_mom_eps.py, Laplace kernel, no Taylor step), test model b = (9, -1 x 9), n = 10, eps = 3:

    beta1 0.3   beta2 0.9995 / 0.999 / 0.998: exact -0.772454 / -0.771801 / -0.770502, gap/d -3.06 / -3.06 / -3.04
                limit r K0 - p2 T H/(r K0 B2 B3) = -0.773113; exact extrapolated linearly to d = 0: -0.773107
    beta1 0.7   exact -0.392040 / -0.390767 / -0.388222, gap/d 0.185 / 0.190 / 0.208
                limit -0.393316; extrapolated -0.393312

The gap over d is flat in d at both points, so what remains is O(d^2), and the d = 0 extrapolations meet the limit coefficient to
6e-6. Together with the peer's 18 rows (beta1 0, 0.5, 0.9; eps 1, 10), the formula is checked on five momenta and three eps.

## Not covered

a_i = 1, scalar, n d small; the test model only (B2, B3, T fixed); the expansion of psi is formal here and rests on the reshuffling
eps remainder lemma (two audits) for its rigour.
