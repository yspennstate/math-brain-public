# Second audit of agent B's reshuffling lemmas with momentum and with eps > 0 (T354, push 9bf2f37b)

Auditor agent A, 20 Oct 2026 04:0x. Scope: remainder_rr_mom.py (NOTE "Rigorous remainder, reshuffling with momentum,
eps = 0") and remainder_rr_eps.py (NOTE "eps > 0"), test model g_i = x + b_i, b = (9, -1 x 9), n = 10. The first audit is
agent C's. Verdict: CONFIRMED. All twelve exact roots lie inside their enclosures.

## The independent route (rr_exact_mom_eps.py)

This extends rr_exact.py (the beta1 = 0, eps = 0 audit) to both features, with no Taylor step and no bound. Only the special sample's
slot in each epoch matters. With the current step at position p and the special at q_e in epoch e (independent, uniform),

    v = g_o^2 + A sum_e beta2^lag_e [past],     m = g_o + (g_s - g_o)(1 - beta1) sum_e beta1^lag_e [past],
    A = (1 - beta2)(g_s^2 - g_o^2),             lag_0 = p - q_0 (past iff q_0 <= p),  lag_e = p + e n - q_e.

1/(sqrt v + eps) is the integral of k(u) e^(-uv) du, with k(u) = (pi u)^(-1/2) [1 - eps sqrt(pi u) erfcx(eps sqrt u)] (the kernel
of eps_exact_logu.py). Given u, the epochs factorize. Pinning one epoch's slot gives the momentum term:

    E[m e^(-uv)] = e^(-u g_o^2) prod_e F_e(u) [ g_o + (g_s - g_o)(1 - beta1) sum_e G_e(u)/F_e(u) ],
    F_e = E_q e^(-u A beta2^lag_e [past]),   G_e = E_q beta1^lag_e [past] e^(-u A beta2^lag_e).

Epochs are computed exactly while the momentum weight is above 1e-17 or the u-spread of the exponent exceeds 1e-3. The remaining
log prod F is summed in closed form through the cumulants of beta2^(-q) to order 4. The integral uses the trapezoid rule in log u
on [e^-45, 60], and x* is the root of D(x) = E[m/(sqrt v + eps)].

Checks of the route:
- At beta1 = 0, eps = 0 it reproduces rr_exact.py (Gauss-Legendre in sqrt u) to six digits: 0.998725 at beta2 0.999 and
  0.993690 at beta2 0.995.
- Halving the step from h 0.04 to 0.02 changes no printed digit, and h 0.01 gives the same D.
- Direct RR simulation of D(x) at frozen x (rr_exact_mom_eps_mc.py: 400 chains, 4,000 epochs, several seeds):
    beta1 0.9, beta2 0.9, eps 1, x 0.2:   exact 3.834232e-2;  MC over 4 seeds 3.83418e-2 +/- 0.21e-5   (-0.2 se)
    beta1 0.5, beta2 0.95, eps 3, x 0.1:  exact 8.970742e-3;  MC over 5 seeds 8.97123e-3 +/- 0.05e-5   (0.95 se)
    beta1 0.9, beta2 0.9, eps 1, x 0.05:  exact 2.14586e-4;   MC 2.198e-4 +/- 0.045e-4                 (1.2 se)

## Against the enclosures (rr_exact_mom_eps_runs.txt; peer files remainder_rr_mom_runs.txt, remainder_rr_eps_runs.txt)

    beta1  beta2   eps   exact x*/x0   enclosure of x*/x0      (x*/x0 - 1)/d
    0.9    0.9999  0     0.999984      [0.99982, 1.00015]      -0.16
    0.9    0.999   0     0.999851      [0.98257, 1.01701]      -0.149
    0.9    0.99    0     0.999200      [0, 3] (vacuous)        -0.080
    0.5    0.999   0     0.999190      [0.99276, 1.00550]      -0.81
    0      0.999   0     0.998725      [0.99348, 1.00391]      -1.275
    0      0.999   1     0.998895      [0.99512, 1.00263]      -1.105
    0      0.999   3     0.999066      [0.99648, 1.00163]      -0.934
    0      0.999   10    0.999249      [0.99763, 1.00085]      -0.751
    0      0.99    0     0.987527      [0.13002, 1.87168]      -1.247
    0      0.99    1     0.989106      [0.40430, 1.58085]      -1.089
    0      0.99    3     0.990724      [0.60851, 1.37332]      -0.928
    0      0.99    10    0.992512      [0.76254, 1.22145]      -0.749

(x0 = (1 - beta2) K_rr 4 x 3/(3 + eps), K_rr from kfactor.py. It is a normalisation only: the comparison is of absolute x*.)

Every root is inside its enclosure. The tightest case, beta1 0.9 at beta2 0.9999 with width 3.3e-4, has its root 1.6e-4 from the
lower end. The coefficient (x*/x0 - 1)/d is nearly the same at beta2 0.99 and 0.999 for each eps (-1.247/-1.275, -0.749/-0.751),
which is what an O(d) correction to x*/x0 should show. With eps added, x*(eps) tracks x0 * 3/(3 + eps) to O(d), as the NOTE says.

Not asked, but computed (beta1 0.9, beta2 0.999): x*/x0 = 0.999862, 0.999874, 0.999887 at eps 1, 3, 10.

## Not covered

- The lemmas' proofs are not re-read line by line here. This audit checks their enclosures against an exact value computed by a
  different method; the first audit (C) read the proofs.
- At beta2 0.99 the enclosures are wide (beta1 0.9: [0, 3]). There n(1 - beta2) = 0.1 and the bound is not useful, as the NOTE
  itself says. The exact route works there, so it can stand in for the bound in that regime.
