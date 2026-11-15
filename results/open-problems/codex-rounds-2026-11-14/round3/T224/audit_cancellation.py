"""Independent algebra/constant checks for PROOF.md, standard library only.

The exact quadratic-feature checks test local identities, not the global
bounded-feature assumptions. The trigonometric feature map is bounded.
No infinite-time theorem is inferred from numerical trajectories.
"""

import json
import math
import os
import random
import resource
from fractions import Fraction as F
from pathlib import Path


rng = random.Random(2240315)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def norm(a):
    return math.sqrt(dot(a, a))


def phi(w):
    a, b = w
    return (math.sin(a), math.cos(a), math.sin(b), math.cos(b),
            math.sin(a + b))


def jac(w):
    a, b = w
    return ((math.cos(a), 0.), (-math.sin(a), 0.),
            (0., math.cos(b)), (0., -math.sin(b)),
            (math.cos(a + b), math.cos(a + b)))


def mean_feature(ws):
    fs = [phi(w) for w in ws]
    return tuple(sum(f[j] for f in fs) / len(ws) for j in range(5))


def jt(w, r):
    j = jac(w)
    return tuple(sum(row[k] * ri for row, ri in zip(j, r)) for k in range(2))


def jv(w, e):
    return tuple(dot(row, e) for row in jac(w))


def mean_vectors(xs):
    return tuple(sum(x[k] for x in xs) / len(xs) for k in range(len(xs[0])))


# 2-parameter, 5-output bounded smooth feature map:
# A=sqrt(3), B=sqrt(3), M=sqrt(5) are valid global bounds.
M = math.sqrt(5.)
identity_errors = []
remainder_ratios = []
riccati_slacks = []
old_slacks = []
square_errors = []
for case in range(600):
    n = rng.randrange(1, 9)
    vs = [tuple(rng.uniform(-3, 3) for _ in range(2)) for _ in range(n)]
    amp = (0., .0001, .01, .3, 2., 8.)[case % 6]
    ws = [tuple(vk + rng.uniform(-amp, amp) for vk in v) for v in vs]
    es = [sub(w, v) for w, v in zip(ws, vs)]
    y = sum(dot(e, e) for e in es) / n
    fv, fw = mean_feature(vs), mean_feature(ws)
    fm = tuple(rng.uniform(-1, 1) for _ in range(5))
    r = tuple(rng.uniform(-1, 1) for _ in range(5))
    delta, zeta, Delta = sub(fw, fm), sub(fv, fm), sub(fw, fv)
    rw = tuple(ri + di for ri, di in zip(r, delta))
    wdots = [tuple(-x for x in jt(w, rw)) for w in ws]
    vdots = [tuple(-x for x in jt(v, r)) for v in vs]
    half_yprime = sum(dot(e, sub(wd, vd))
                     for e, wd, vd in zip(es, wdots, vdots)) / n
    JWE = mean_vectors([jv(w, e) for w, e in zip(ws, es)])
    curvature = -sum(dot(r, sub(jv(w, e), jv(v, e)))
                     for w, v, e in zip(ws, vs, es)) / n
    identity_rhs = curvature - dot(JWE, delta)
    identity_errors.append(abs(half_yprime - identity_rhs))
    R = sub(JWE, Delta)
    if y > 0:
        remainder_ratios.append(norm(R) / (M * y / 2))
    assert norm(R) <= M * y / 2 + 2e-14
    u = sub(zeta, R)
    square_rhs = -dot(sub(delta, tuple(ui / 2 for ui in u)),
                      sub(delta, tuple(ui / 2 for ui in u))) + dot(u, u) / 4
    square_errors.append(abs(-dot(JWE, delta) - square_rhs))
    h = M * norm(r)  # valid global bound; not claimed exact for this map
    eta = norm(zeta)
    riccati_rhs = 2 * h * y + eta * eta + M * M * y * y / 4
    riccati_slacks.append(riccati_rhs - 2 * half_yprime)
    B = math.sqrt(3.)
    old_rhs = (h + M * eta + M * B * math.sqrt(y)) * y + B * eta * math.sqrt(y)
    old_slacks.append(old_rhs - half_yprime)


# Entirely independent exact scalar calculation, phi(w)=w^2/2.
exact_cases = 0
for case in range(300):
    n = rng.randrange(1, 7)
    vs = [F(rng.randrange(-9, 10), rng.randrange(1, 6)) for _ in range(n)]
    ws = [F(rng.randrange(-9, 10), rng.randrange(1, 6)) for _ in range(n)]
    es = [w - v for w, v in zip(ws, vs)]
    y = sum(e * e for e in es) / n
    fv = sum(v * v / 2 for v in vs) / n
    fw = sum(w * w / 2 for w in ws) / n
    fm, r = F(rng.randrange(-9, 10), 7), F(rng.randrange(-9, 10), 5)
    delta, zeta = fw - fm, fv - fm
    direct = 2 * sum(e * (-w * (r + delta) + v * r)
                     for w, v, e in zip(ws, vs, es)) / n
    JWE = sum(w * e for w, e in zip(ws, es)) / n
    R = JWE - (fw - fv)
    assert R == y / 2
    assert direct == -2 * r * y - 2 * JWE * delta
    assert -JWE * delta == -(delta - (zeta - R) / 2) ** 2 + (zeta - R) ** 2 / 4
    assert direct <= 2 * max(F(0), -r) * y + zeta * zeta + y * y / 4
    exact_cases += 1


# Equality example for the local Young inequality, with nonzero displacement.
# This unbounded quadratic map is used only for an exact algebra check.
v, w = F(-2, 3), F(2, 3)
y = (w - v) ** 2
R = y / 2
fw = w * w / 2
fm = fw + R
delta, zeta = fw - fm, v * v / 2 - fm
direct = 2 * (w - v) * (-w * delta)  # r=0
assert direct == zeta * zeta + y * y / 4


# Constant-forcing Riccati ODE with h=0 has exact tangent solution.
# Compare with the reciprocal-integral majorant, not an Euler simulation.
min_riccati_ratio = 1.
max_riccati_ratio = 0.
for _ in range(300):
    alpha = rng.uniform(.01, 4.)
    T = rng.uniform(.1, 5.)
    rho = rng.uniform(.0001, .5)  # alpha * J_T * S_T
    forcing = rho / (alpha * T * T)
    exact = math.sqrt(forcing / alpha) * math.tan(math.sqrt(alpha * forcing) * T)
    J = forcing * T
    reciprocal_bound = J / (1 - rho)
    assert exact <= reciprocal_bound * (1 + 1e-13)
    assert reciprocal_bound <= 2 * J * (1 + 1e-13)
    ratio = exact / reciprocal_bound
    min_riccati_ratio = min(min_riccati_ratio, ratio)
    max_riccati_ratio = max(max_riccati_ratio, ratio)


# Check constants with exact rational arithmetic, including M=0 and B=0.
max_constant_ratio = F(0)
for _ in range(300):
    A, B, M = [F(rng.randrange(0, 31), 10) for _ in range(3)]
    T, E = F(rng.randrange(1, 50)), F(rng.randrange(1, 50))
    K = 2 * A ** 2 + 4 * A ** 2 * B ** 2 + 2 * M ** 2 * A ** 4
    fine = 2 * A ** 2 + 4 * A ** 2 * B ** 2 * T * E + 2 * M ** 2 * A ** 4 * T ** 2 * E
    coarse = K * (1 + T) ** 2 * E
    assert fine <= coarse
    if coarse:
        max_constant_ratio = max(max_constant_ratio, fine / coarse)
    # Re-derive the bad-event coefficient from cap * Markov * iid variance.
    alpha = M * M / 4
    assert 4 * A ** 2 * 2 * alpha * A ** 2 == 2 * M ** 2 * A ** 4


powers = []
for c in (F(1, 4), F(1, 2), F(1), F(3, 2), F(7, 4), F(2)):
    for kappa in (F(0), F(1, 2), F(3)):
        b = 1 / (c + 2 + 2 * kappa)
        a = c * b
        assert (2 + 2 * kappa) * b - 1 == -a
        old_a = c / (c + 4 + 2 * kappa)
        assert a > old_a
        powers.append({"c": str(c), "kappa": str(kappa),
                       "new": str(a), "old": str(old_a)})


assert max(identity_errors) < 3e-12
assert max(square_errors) < 3e-12
assert min(riccati_slacks) >= -1e-12
assert min(old_slacks) >= -1e-12
nice_value = os.getpriority(os.PRIO_PROCESS, 0)
assert nice_value >= 15
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
# On this Mac ru_maxrss is in bytes.
assert rss < 1024 ** 3
result = {
    "status": "PASS", "seed": 2240315,
    "bounded_feature_direct_cases": len(identity_errors),
    "max_direct_identity_error": max(identity_errors),
    "max_completed_square_error": max(square_errors),
    "max_taylor_remainder_bound_ratio": max(remainder_ratios),
    "min_riccati_inequality_slack": min(riccati_slacks),
    "min_inherited_inequality_slack": min(old_slacks),
    "exact_rational_cancellation_cases": exact_cases,
    "exact_local_equality_example": True,
    "exact_riccati_solution_cases": 300,
    "min_exact_solution_to_majorant_ratio": min_riccati_ratio,
    "max_exact_solution_to_majorant_ratio": max_riccati_ratio,
    "exact_constant_cases": 300,
    "max_constant_ratio": float(max_constant_ratio),
    "exact_exponent_balances": powers,
    "actual_nice": nice_value,
    "max_rss_bytes_macos": rss,
    "scope": "Algebra and scalar-comparison checks supplement the written proof; no infinite-time simulation."
}
Path("cancellation_results.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
