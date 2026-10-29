# T354: the remainder uniform in n with eps > 0, audit 1 (agent C, 20 Oct 2026 08:0x)

Object: agent_B/NOTE.md, "The remainder, uniform in n", the sentence "With eps > 0 the same steps run with psi's derivatives
(p1, p2, p3 above) in place of -1/2, 3/8, -5/16" (push 59a1d8df, candidate). Claim, at beta1 = 0, a_i = 1, eps >= 0 fixed:

    (s + eps) D(x) = x + p1 d K_rr (2 x B2 + B3)/V + x e1(x) + e2(x),   |e1| <= C d, |e2| <= C d^2, all |x| <= rho, all n >= 4,

with s = sqrt(V), p1 = -r/2, r = s/(s + eps), and so x* = r x0 (1 + O(d)) uniformly in n.

Verdict:
- The conclusion x* = r x0 (1 + O(d)) uniformly in n: CONFIRMED, by hand and against an exact solver at n up to 2500.
- One slip in the sentence: p2 and p3 are psi''(1) and psi'''(1), derivatives, while -1/2, 3/8, -5/16 are Taylor coefficients.
  The substitution is p1, p2/2, p3/6. At eps = 0 these are -1/2, 3/8, -5/16, as they must be. Taken literally, "p2 in place of
  3/8" doubles the x d term; the exact solver below fits p2/2 and rules out p2. The conclusion does not depend on the constant.
  My own AUDIT_UNIFORM had the same slip in its last fix line and is corrected.
- The step that is genuinely new at eps > 0, the Taylor remainder of step 1, holds with a constant that does not grow with eps.

## By hand

Only the function changes; eta, the permutation moments and the bounds on E[b eta_c^k] do not involve eps.

1. psi(y) = (s + eps)/(s t + eps), t = sqrt(y). Every y-derivative of order k is a sum of terms
   c (s + eps) s^j t^(-a) (s t + eps)^(-1-j), j <= k. On y >= y_min = gamma/V > 0 we have (s + eps)/(s t + eps) <= max(1, 1/t_min)
   and s/(s t + eps) <= 1/t_min, both free of eps. So |psi''''| <= C(y_min, y_max) for every eps >= 0, and the cubic Taylor
   remainder is |R| <= C eta^4 with the eps = 0 constant or better. Numerically (eps_uniform_table.py part 1, |x| <= 0.5):
   sup |psi''''| on [0.027, 10.0] is 6.6e7 at eps 0, 2.8e6 at eps 1, 1.0e5 at eps 10, 79 at eps 1e4. Large, because y_min is
   small on this model, but n-free and decreasing in eps.
2. psi'(1), psi''(1), psi'''(1) by sympy: -s/(2(eps+s)), s(eps+3s)/(4(eps+s)^2), -3s(eps^2+4 eps s+5 s^2)/(8(eps+s)^3). These
   are the note's p1, p2, p3.
3. Then E[g psi] = x + p1 E[g eta] + (p2/2) E[g eta^2] + (p3/6) E[g eta^3] + E[g R]. The note's eps = 0 bounds on each E[g eta^k]
   carry over unchanged, because they are statements about eta and b alone. So e1 = (p2/2) E eta^2 + (p3/6) E eta^3 + ...
   and e2 = (p2/2) E[b eta_c^2] + (p3/6)(E[b eta_c^3] + 3 E[b eta_c] E eta_f^2) + E[g R].
4. s, r and the p_k depend on x through V = x^2 + B2. That needs no smoothness: on |x| <= rho they are bounded, and each
   multiplies a term already of size x d or d^2. At the zero, r(x*) = r(0)(1 + O(d^2)) since dV/dx = 0 at x = 0.
5. The zero: x (1 - r d K_rr B2/V + e1) = r d K_rr B3/(2V) - e2. The bracket is 1 - O(d), so |x*| <= C d, x* e1 = O(d^2), and
   x* = r x0 (1 + O(d)). This is the note's line 112, x*(eps) = r x*(0), now uniform in n.

## Exact solver (rrm_eps.py, rre_batch.sh, rre_out/)

rrm_eps.py is rrm_indep.py (the independent large-n solver of AUDIT_LARGE_N) with one change, the kernel
1/(sqrt(v) + eps) = (2/sqrt(pi)) int h(s) exp(-s^2 v) ds, h(s) = 1 - eps sqrt(pi) s erfcx(eps s) (u = s^2 in the note's k(u)).
- The quadrature reproduces 1/(sqrt(v) + eps) to 3e-13 relative on v in [q, A], eps 0, 1, 3.
- At eps = 0 it gives the same root as rrm_indep.py (n 10, beta2 .99: -1.247264).
- At eps = 1, n 10, beta2 .999 it gives -1.104672, the value of my earlier fixed-n route rr_exact_mom_eps.py (rr2e_runs.txt), to
  every printed digit.

(x*/(r x0) - 1)/d on the 9/-1 model, r = 3/(3 + eps):

| eps | n d | d = 0.01 | d = 0.005 | d = 0.002 | d -> 0 (last two) | slope per unit d |
|---|---|---|---|---|---|---|
| 1 | 1 | -0.707679 (n 100) | -0.686118 (n 200) | -0.673197 (n 500) | -0.6646 | -4.3 |
| 1 | 5 | -0.105173 (n 500) | -0.080387 (n 1000) | -0.066090 (n 2500) | -0.0566 | -4.8 |
| 1 | 10 | +0.060156 (n 1000) | +0.085397 (n 2000) | | +0.1106 | -5.0 |
| 3 | 1 | -0.708233 (n 100) | -0.694381 (n 200) | -0.686025 (n 500) | -0.6805 | -2.8 |
| 3 | 5 | -0.379022 (n 500) | -0.360359 (n 1000) | -0.349413 (n 2500) | -0.3421 | -3.7 |
| 3 | 10 | -0.298886 (n 1000) | -0.278636 (n 2000) | | -0.2584 | -4.1 |

- Every row moves linearly in d at fixed n d, with a slope of 3 to 5 that does not grow with n (n runs from 100 to 2500). So
  x*/(r x0) = 1 + d c_eps(n d) + O(d^2) with a bounded c_eps, the eps > 0 form of the large-n law.
- c_eps rises with n d, as c does at eps = 0 (-0.58, +0.38, +0.66 at n d 1, 5, 10), and sits lower the larger eps is. At n d 1 it
  is -0.58, -0.66, -0.68 at eps 0, 1, 3.

## The x d term (eps_uniform_table.py part 3)

E2 = (s + eps) D(x) - x - p1 d K_rr (2 x B2 + B3)/V from the exact solver at x = 0.1, n d = 1, d 0.01, 0.005, 0.0025:

| eps | fit | (p2/2) E eta^2/d | p2 E eta^2/d |
|---|---|---|---|
| 0 (AUDIT_UNIFORM) | 0.3650 x d + 2.464 d^2 | 0.376, 0.373, 0.371 | 0.75 |
| 1 | 0.2284 x d + 1.921 d^2 | 0.235, 0.233, 0.232 | 0.47 |
| 3 | 0.1220 x d + 1.212 d^2 | 0.126, 0.124, 0.124 | 0.25 |

Fit residuals are under 2e-7. The fitted coefficient is 0.97 to 0.98 of (p2/2) E eta^2/d at all three eps, the same ratio as at
eps = 0, and half of p2 E eta^2/d. That is the x e1 term with the Taylor coefficient p2/2.

## Not covered

- Momentum with eps > 0 (agent A is auditing the momentum paragraph).
- Uniformity in eps as eps -> 0 or infinity was not claimed; step 1's constant happens to be uniform, the rest was not checked.
- n d beyond 10, other distributions of b, a_i != 1. A second audit.

Files: rrm_eps.py, rre_batch.sh, rre_out/, eps_uniform_table.py, eps_uniform_table.txt, and rrm_indep.py and uniform_check2.py, which it imports.
