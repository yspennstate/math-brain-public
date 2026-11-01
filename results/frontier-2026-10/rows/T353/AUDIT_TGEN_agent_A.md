# Audit of "Every T" (REFUTATION_T2.md, agent B) - agent A, 20:2x 19 Oct 2026

Verdict: CONFIRMED. The step-T switch at any T >= 3 reduces to the T = 3 two-variable function Delta(A, G), and the
audited T = 3 box (AUDIT_T3_agent_A.md) gives a strict gain on a prefix set of positive measure at every T >= 3.
The Monte Carlo gains quoted for T = 4..32 were not re-run here; the refutation does not rest on them.

## What was checked

1. Coordinates. t3_dp.py fixes step 1 at (a1, v1) = (-1, 1), so g1 has means -2 under x and -1 under x'; flipping g1
   gives the 2 | 1 means of the conjectured ANTI answers at the later steps. Hence x1 = exp(-g1 - 1/2), x_t =
   exp(g_t - 1/2) for t >= 2, and on the box x2/x1 = exp(g1 + g2). B = [-0.1, 0.3] x [2.2, 2.3] gives g1 + g2 in
   [2.1, 2.6] and eA/G^2 = (1 + r^2)/(1 + r)^2 in [0.80561, 0.87128], as stated.
2. Homogeneity. With the prefix fixed the step-T integrand is (p - e q)_+ with p = alpha phi(z) + beta phi(z - m),
   q = gamma phi(z) + beta phi(z - m'), linear in (alpha, gamma, beta), so I = beta I(A, G, 1) with A = alpha/beta =
   e^{-1} sum x_t^2 and G = gamma/beta = sum x_t (phi(g - 2)/phi(g) = e^{2g - 2} = e x^2, phi(g - 1)/phi(g) = x). Read by
   hand; correct.
3. Numerically, from the mechanism directly (check_tgen.py, written from scratch, not importing their code): the
   step-T inner difference I_SAME - I_ANTI at a T = 4 or 5 prefix against beta times the same difference at another
   prefix with equal (A, G) - a T = 3 prefix where one exists, otherwise a different prefix of the same length.
   Four of four agree to 1.5e-16 .. 4.6e-16 relative (check_tgen_run1.txt). Their own control tgen_identity_check.txt
   (reduced form against the Arb diff at six T = 3 points, ~1e-15) is consistent with this.
4. Reach. An m-prefix (m = T - 1 >= 2) gives every (A, G) with G > 0 and 1/m <= eA/G^2 < 1 (Cauchy-Schwarz; the scale
   and the ratio move independently). The box image has ratio in [0.806, 0.871], inside that range for every m >= 2
   since 1/m <= 1/2. The map g -> (A, G) has rank 2 wherever x is not a multiple of the all-ones vector (gradients
   2x and 1), which holds on the preimage since its ratio exceeds 1/m. So the preimage of the open image U of int B is a
   nonempty open set of R^m, of positive Gaussian measure, and beta > 0 on it.
5. Gain. Steps 1..T-1 keep the conjectured answers; only the g_T factor depends on the step-T answer, so answering SAME
   on that preimage raises the hockey-stick total by the integral of beta Delta over it, strictly positive because
   Delta > 0 on U by the T = 3 certificate.

## Small points, none affecting the verdict

- "For m >= 2 the region is G^2/m < eA < G^2": the lower end is attained (equal x), so <= there. Immaterial.
- The NaN rows in check_tgen_run1.txt are prefixes with eA/G^2 < 1/2, which no T = 3 prefix reaches; they are
  rechecked against same-length twins in the second block of the same file.
