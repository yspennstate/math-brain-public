import math
import numpy as np
from scipy.integrate import quad


def D2phi_matrix(x, p):
    x = np.asarray(x, dtype=float)
    r = np.linalg.norm(x)
    n = x.size
    if r == 0:
        return np.zeros((n, n))
    alpha = p - 2.0
    e = x / r
    return p * (r ** alpha) * (np.eye(n) + alpha * np.outer(e, e))


def hessian_form(A, z, u, v, p):
    A = np.asarray(A, dtype=float)
    z = np.asarray(z, dtype=float)
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)
    sq = np.sqrt(A)

    def integrand(s):
        es = np.exp(-A * s)
        x = es * z
        hu = sq * es * u
        hv = sq * es * v
        M = D2phi_matrix(x, p)
        return float(hu @ M @ hv)

    val, _ = quad(integrand, 0, np.inf, epsabs=2e-10, epsrel=2e-9, limit=300)
    return val


def sigma_value(A, z, y, p):
    r = np.linalg.norm(z)
    u = np.linalg.norm(y)
    if r == 0:
        return 0.0
    a = hessian_form(A, z, z, z, p)
    b = hessian_form(A, z, z, y, p)
    c = hessian_form(A, z, y, y, p)
    A0 = (p - 1) * r ** p
    B0 = (p - 1) * r ** (p - 1) * u
    C0 = (p - 1) * r ** (p - 2) * u * u
    return A0 + 2 * B0 + C0 - a - 2 * b - c


rng = np.random.default_rng(20260920)

cstar = 5 * (3 - 2 * math.sqrt(2)) / 24
Cpack = 2 / cstar
print(f"cstar={cstar:.15f}")
print(f"Cpack=2/cstar={Cpack:.15f}")
print(f"8*Cpack={8*Cpack:.15f}")
print(f"(8*Cpack)^1/4={(8*Cpack)**0.25:.15f}")
print(f"critical_migration_second_constant={22*(8*Cpack)**0.25:.15f}")

# q=2/(4-p) must lie below p for the weighted Holder step.
grid = np.linspace(2.5, 2.999, 1000)
max_q_minus_p = max(2 / (4 - p) - p for p in grid)
print(f"max(q-p) on [2.5,2.999]={max_q_minus_p:.15e}")
assert max_q_minus_p <= 1e-12

# Pointwise Holder continuity of the Hilbert-space p-power Hessian.
max_ratio = 0.0
for _ in range(5000):
    n = 5
    p = float(rng.uniform(2.5, 2.999))
    x = rng.normal(size=n)
    w = rng.normal(size=n)
    d = np.linalg.norm(x - w)
    if d < 1e-12:
        continue
    M = D2phi_matrix(x, p) - D2phi_matrix(w, p)
    op = np.linalg.norm(M, 2)
    ratio = op / (p * d ** (p - 2))
    max_ratio = max(max_ratio, ratio)
assert max_ratio < 6 + 1e-10
print(f"max_holder_ratio_over_p={max_ratio:.12f} < 6")

# Random finite-dimensional checks of the new pointwise packet-migration inequality.
min_margin = float("inf")
positive_rhs_tests = 0
for _ in range(240):
    n = 6
    A = 2.0 ** np.arange(n)
    P = np.zeros(n, dtype=bool)
    P[2:5] = True
    p = float(rng.uniform(2.5, 2.99))

    z = np.zeros(n)
    z[P] = rng.normal(size=P.sum())
    rz = np.linalg.norm(z)
    leak = float(10 ** rng.uniform(-4, -0.7))
    h = rng.normal(size=(~P).sum())
    h /= np.linalg.norm(h)
    z[~P] = leak * rz * h

    y = rng.normal(size=n)
    r = np.linalg.norm(z)
    u = np.linalg.norm(y)
    d = np.linalg.norm(z[~P]) / r
    qy = np.linalg.norm(y[~P])

    rhs = ((p - 1) * r ** (p - 1) * qy * qy / u
           - 22 * d ** (p - 2) * r ** (p - 1) * u)
    S = sigma_value(A, z, y, p)
    margin = S - rhs
    min_margin = min(min_margin, margin)
    if rhs > 0:
        positive_rhs_tests += 1
    assert margin > -3e-7

print(f"migration_random_tests=240 positive_rhs_tests={positive_rhs_tests}")
print(f"min_numeric_margin={min_margin:.12e}")

Q0 = 8 * Cpack
first = 16 / 3
second = 22 * (8 * Cpack) ** 0.25
print(f"Q0={Q0:.12f}")
print(f"M/I <= {first:.12f}/Q + {second:.12f}/Q^(5/4) for Q>=Q0")
print("CHECK_PASS")
