# Audit of agent B's next-order term with eps > 0 (T354, NOTE.md "The next-order term with eps > 0", next_order_eps.py)

Auditor agent A, 20 Oct 2026 03:2x. Verdict: CONFIRMED (iid sampling, E b = 0, as stated). Second audit; the first is
agent C's.

    x*/x0 = 1 + d [ r K - (p2/4) S/B2^2 - (p2/r)(K2/K) E[b Z^2]/(B2 B3) - (p3/(2r)) S/B2^2 ] + O(d^2),   x0 = r d K B3/(2 B2).

## By hand

psi(y) = a/q(y), q = s sqrt(y) + eps, a = s + eps, r = s/a. With q'(1) = s/2, q''(1) = -s/4, q'''(1) = 3s/8:

    psi'(1)   = -a q'/a^2                              = -r/2
    psi''(1)  = -a [q''/a^2 - 2 q'^2/a^3]              = s/(4a) + s^2/(2a^2)             = s(eps + 3s)/(4a^2)
    psi'''(1) = -a [q'''/a^2 - 6 q' q''/a^3 + 6 q'^3/a^4] = -(3s/(8a^3)) (a^2 + 2sa + 2s^2) = -3s(eps^2 + 4 eps s + 5 s^2)/(8a^3)

so p1, p2, p3 are psi's first three derivatives at 1 (not the Taylor coefficients), as the solve uses them. The moments E1, E2, E3
do not involve eps and are the ones confirmed in AUDIT_NEXTORDER_agent_A.md. From x + p1 E1 + (p2/2) E2 + (p3/6) E3 = 0,
x = x0 (1 + d delta), divided by x0 d: r K from the 2 x B2 part of E1, -(p2/4) S/B2^2 from the x S part of E2, -(p2/r)(K2/K)
E[b Z^2]/(B2 B3) from its d^2 part, -(p3/(2r)) S/B2^2 from E3. Same bracket. s = sqrt(V) with V = B2 + x^2 moves r and the p's
by O(d^2), outside this order.

Limits: eps = 0 gives r = 1, p2 = 3/4, p3 = -15/8, the eps = 0 bracket. eps -> infinity gives p2 -> r/4, p3 -> -3r/8 (the
derivatives of -r sqrt y), the bracket tends to -(1/4)(K2/K)E[b Z^2]/(B2 B3) + (3/16) S/B2^2, -4/9 on the test model at b1 = 0,
and the printed -0.167 (eps 3), -0.427 (eps 10) move toward it. Test model eps 1, b1 0: r = 3/4, p2 = 15/32, p3 = -261/256; the
bracket is 3/4 + (64/9)(-15/128 - 5/8 + 87/128) = 3/4 - 4/9 = 0.30556, as printed.

The kernel k(u) = (pi u)^(-1/2)[1 - eps sqrt(pi u) erfcx(eps sqrt u)], re-derived: with t = 2 sqrt(u) tau the t integral is
(2/sqrt pi) u^(-1/2) int tau e^(-tau^2 - 2c tau) dtau, c = eps sqrt u, and that integral is 1/2 - c (sqrt pi/2) erfcx(c).

## Independent exact route (eps_exact_logu.py, eps_exact_logu_runs.txt)

Written from scratch, not from next_order_eps.py or laplace_exact.py: the kernel integral in t = log u by the trapezoid rule on
[-45, 6] (not Gauss-Legendre in sqrt u on [0, 7]), the lag product summed lag by lag to exponent 1e-5 and closed by cumulants to
order 4. Kernel check at eps 3: 1/(sqrt v + eps) to 2e-10 at v = 1, 9, 81. Step 0.04 and 0.02 give the same nine digits.

    case                         this route      peer (next_order_eps_runs.txt)
    test  eps 1   b2 .998 b1 0     1.000593101     1.000593100
    test  eps 1   b2 .999 b1 0     1.000301092     1.000301092
    test  eps 3   b2 .999 b1 0     0.999829193     0.999829192
    test  eps 3   b2 .998 b1 0     0.999650020     0.999650019
    test  eps 10  b2 .999 b1 0     0.999570669     0.999570667
    test  eps 10  b2 .998 b1 0     0.999136021     0.999136018
    test  eps 1   b2 .998 b1 .98   1.001195094     1.001195093
    test  eps 3   b2 .999 b1 .99   1.000078955     1.000078954
    test  eps 10  b2 .998 b1 .98   0.999522170     0.999522168
    3-val eps 3   b2 .999 b1 0     0.999593908     0.999593907
    3-val eps 3   b2 .998 b1 0     0.999182017     0.999182016
    3-val eps 3   b2 .998 b1 .98   0.999524924     0.999524923

Every row agrees to 3e-9. Richardson on the b1 = 0 pairs (2 f(d/2) - f(d) on (x*/x0 - 1)/d) against the bracket: eps 1 0.30563 /
0.30556, eps 3 -0.16663 / -0.16667, eps 10 -0.42667 / -0.42669, three-valued eps 3 -0.40319 / -0.40320. At r = 0.1 the gaps to the
d-dependent prediction are 0.0046/0.0022 (eps 1), 0.0059/0.0029 (eps 3), 0.0041/0.0021 (eps 10): halving with d.

## Not covered

Same as the eps = 0 audit: E b = 0, iid only, the coefficient of d and not a remainder bound. The exact route shares the Laplace
representation with the peer's (the kernel is unique); the hand derivation and agent C's kernel-free Taylor route are the
routes that do not.
