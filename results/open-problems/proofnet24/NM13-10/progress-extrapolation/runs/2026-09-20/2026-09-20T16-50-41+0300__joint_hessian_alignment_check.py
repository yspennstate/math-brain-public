import math
import random
import numpy as np


def c_p(p, x):
    return p*x*x/(p - 2 + 2*x*x)


def d_p(p, x):
    return (p - 1) - c_p(p, x)


def d_closed(p, x):
    return (p - 2)*((p - 1) + x*x)/(p - 2 + 2*x*x)


# 1. Shell coefficient identity and uniform lower bound.
rows = []
for p in [2.50, 2.70, 2.90, 2.99]:
    vals = []
    for x in [0.05, 0.2, 0.5, 1.2, 2.0, 10.0, 100.0]:
        d = d_p(p, x)
        dc = d_closed(p, x)
        assert abs(d - dc) < 1e-12
        assert d + 1e-12 >= (p - 2)/2
        vals.append(d)
    rows.append((p, min(vals), (p - 2)/2))

# 2. Endpoint quantile prefactor from the effective-gap root.
prefactor = 2*(1 + math.sqrt(2))*math.sqrt(math.e)
assert prefactor < 8

# 3. Near-sharp q bound:
# sigma <= 2 delta (q^{-2}-1);
# for q=1-eps, eps<=1/2, q^{-2}-1 <= 6 eps.
mx_eps_ratio = 0.0
mx_eps = None
for eps in np.linspace(1e-8, 0.5, 200000):
    ratio = ((1-eps)**(-2) - 1)/eps
    if ratio > mx_eps_ratio:
        mx_eps_ratio = ratio
        mx_eps = eps
assert mx_eps_ratio <= 6 + 1e-10

# 4. Exact shell formula for the total Hessian slack.
def shell_slack_direct(p, a, r, eta, y0_sq, others):
    # A z = a^2 z, e=z/r.
    # y = eta e + y0 + sum_b y_b, y0 in E_a cap e^perp.
    hz_z = (p - 1)*r**p
    hz_y = (p - 1)*r**(p - 1)*eta
    hz_yy = r**(p - 2)*(
        (p - 1)*eta**2
        + y0_sq
        + sum(c_p(p, b/a)*u2 for b, u2 in others)
    )
    u2 = eta**2 + y0_sq + sum(u2 for _, u2 in others)
    u = math.sqrt(u2)

    A0 = (p - 1)*r**p
    B0 = (p - 1)*r**(p - 1)*u
    C0 = (p - 1)*r**(p - 2)*u2
    sigma = A0 + 2*B0 + C0 - (hz_z + 2*hz_y + hz_yy)

    closed = (
        2*(p - 1)*r**(p - 1)*(u - eta)
        + r**(p - 2)*(
            (p - 2)*y0_sq
            + sum(d_p(p, b/a)*u2 for b, u2 in others)
        )
    )
    return sigma, closed


random.seed(20260920)
max_rel_err = 0.0
min_sigma = float("inf")
for _ in range(10000):
    p = random.uniform(2.5, 2.999)
    a = 10**random.uniform(-1, 1)
    r = 10**random.uniform(-1, 1)
    eta = random.uniform(-2, 2)
    y0_sq = 10**random.uniform(-4, 1)
    others = [
        (10**random.uniform(-1, 1), 10**random.uniform(-4, 1))
        for __ in range(3)
    ]
    sigma, closed = shell_slack_direct(p, a, r, eta, y0_sq, others)
    max_rel_err = max(max_rel_err, abs(sigma - closed)/(1 + abs(closed)))
    min_sigma = min(min_sigma, sigma)
    assert sigma >= -1e-10
assert max_rel_err < 1e-12

# 5. Exact sharp root relation and q-near-sharp slack bound.
def Rstar(p):
    return 1/(math.sqrt(2/(p - 1)) - 1)


max_q_ratio = 0.0
for p in np.linspace(2.5, 2.999, 300):
    delta = (3 - p)/2
    R = Rstar(p)
    aa = p - 1
    bb = (p - 1)/2
    assert abs(delta - (aa/R + bb/R**2)) < 1e-10
    for q in [0.5, 0.7, 0.9, 0.99]:
        f = aa/(q*R) + bb/(q*q*R*R)
        sigma_max = 2*(f - delta)
        rhs = 2*delta*(q**(-2) - 1)
        assert sigma_max <= rhs + 1e-12
        max_q_ratio = max(max_q_ratio, sigma_max/rhs)

# 6. Cross-Hessian saturation denominator bound for p>=5/2 and q>=1/2.
max_B_over_delta = 0.0
argmax_p = None
for p in np.linspace(2.5, 2.999999, 200000):
    delta = (3 - p)/2
    R = Rstar(p)
    Bstar = (p - 1)/(2*R*R)
    ratio = Bstar/delta
    if ratio > max_B_over_delta:
        max_B_over_delta = ratio
        argmax_p = p
denominator_factor = 1/(1 - max_B_over_delta/(0.5**2))
assert denominator_factor < 1.41

print("JOINT_HESSIAN_ALIGNMENT_CHECK")
print(f"critical_quantile_prefactor = {prefactor:.15f} < 8")
print(f"max_((1-eps)^(-2)-1)/eps = {mx_eps_ratio:.12f} at eps={mx_eps:.6f} <= 6")
print(f"shell_formula_random_max_relative_error = {max_rel_err:.3e}")
print(f"shell_formula_random_min_sigma = {min_sigma:.12e} >= 0")
print(f"q_near_sharp_bound_max_ratio = {max_q_ratio:.12f} <= 1")
print(f"max_Bstar_over_delta = {max_B_over_delta:.15f} at p={argmax_p:.6f}")
print(f"cross_saturation_denominator_factor(q>=1/2) = {denominator_factor:.15f} < 1.41")
for p, mn, lb in rows:
    print(f"p={p:.2f}: sampled min d_p(x)={mn:.12f}, lower bound={lb:.12f}")
print("CHECK_PASS")
