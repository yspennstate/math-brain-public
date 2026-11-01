#!/usr/bin/env python3
"""Finite-support consistency checks for PROB20-14 correlation-budget formulas.

This is only an algebra/indexing certificate. It does not verify the
infinite-variance theorem.
"""
from fractions import Fraction
from math import exp, log, sqrt

PI = {0: Fraction(1, 2), 1: Fraction(1, 4), 3: Fraction(1, 4)}


def conv(a, b):
    out = {}
    for x, px in a.items():
        for y, py in b.items():
            out[x+y] = out.get(x+y, Fraction(0)) + px*py
    return out


def conv_power(base, n):
    out = {0: Fraction(1)}
    for _ in range(n):
        out = conv(out, base)
    return out


def conditioned_marginal(n):
    sn = conv_power(PI, n)
    a_n = sn[n-1]
    sn1 = conv_power(PI, n-1)
    mu = {
        d: p * sn1.get(n-1-d, Fraction(0)) / a_n
        for d, p in PI.items()
    }
    return a_n, mu


def kl(dist_p, dist_q):
    ans = 0.0
    for x, px0 in dist_p.items():
        px = float(px0)
        if px:
            ans += px * log(px / float(dist_q[x]))
    return ans


def bern_kl(a, b):
    if a == 0.0:
        return -log(1.0-b)
    if a == 1.0:
        return -log(b)
    return a*log(a/b) + (1.0-a)*log((1.0-a)/(1.0-b))


def lam(theta):
    return log(sum(float(p)*exp(-theta*(d-1)) for d, p in PI.items()))


rows = []
for n in (8, 10, 12, 14, 20):
    a_n, mu = conditioned_marginal(n)
    lambda_n = -log(float(a_n))
    d_mu_pi = kl(mu, PI)

    # Exact chain-rule numerical identity:
    # D(Q||mu^n) = lambda_n - n D(mu||pi).
    correlation_budget = lambda_n - n*d_mu_pi
    assert correlation_budget >= -1e-13

    # Data-processing lower bound via the exact-sum event under mu^n.
    mu_sum = conv_power(mu, n)
    product_center = float(mu_sum.get(n-1, Fraction(0)))
    event_cost = -log(product_center)
    assert correlation_budget + 1e-12 >= event_cost

    # Direct concentration diagnostic: sqrt(n)*max atom stays bounded.
    max_atom = max(float(v) for v in mu_sum.values())
    scaled_max_atom = sqrt(n)*max_atom
    assert scaled_max_atom < 1.0

    # Tilted Bernoulli data-processing check for hard mark g=1_{xi=3}.
    alpha = float(mu[3])
    p = float(PI[3])
    assert alpha > 0 and p > 0
    tilt_checks = []
    for theta in (0.1, 0.3, 0.7):
        L = lam(theta)
        rho = p*exp(-theta*(3-1)-L)
        lhs = n*bern_kl(alpha, rho)
        rhs = n*d_mu_pi - theta + n*L
        assert lhs <= rhs + 1e-12
        tilt_checks.append((theta, lhs, rhs))

    rows.append((
        n,
        float(a_n),
        lambda_n,
        n*d_mu_pi,
        correlation_budget,
        event_cost,
        scaled_max_atom,
        tilt_checks,
    ))

print("critical test law: pi(0)=1/2, pi(1)=1/4, pi(3)=1/4")
for row in rows:
    n, a_n, lambda_n, marg, corr, event, scaled, checks = row
    print(
        f"n={n:2d} a_n={a_n:.12g} lambda={lambda_n:.9f} "
        f"nDmu={marg:.9f} corr={corr:.9f} "
        f"-log(mu^n center)={event:.9f} sqrt(n)*maxatom={scaled:.9f}"
    )
    for theta, lhs, rhs in checks:
        print(
            f"  theta={theta:.1f}: n KL(Ber(alpha)||Ber(rho_theta))="
            f"{lhs:.9f} <= nD(mu||pi)-theta+nLambda={rhs:.9f}"
        )
print("ALL ASSERTIONS PASSED")
