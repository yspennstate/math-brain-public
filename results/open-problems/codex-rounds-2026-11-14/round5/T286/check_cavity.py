#!/usr/bin/env python3
"""Small independent algebra and quadrature checks for PROOF.md.

Standard library, one process, no external writes. The quadrature uses finite
deterministic cavity measures to check the exact Stein residual identity; these
measures are not asserted to satisfy the averaged Gaussian-prior hypothesis.
"""
import math
import os
import resource
import time
from fractions import Fraction as Q

resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
started = time.monotonic()
assert os.environ.get("OMP_NUM_THREADS") == "1"
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
print("priority:", os.getpriority(os.PRIO_PROCESS, 0))
print("OMP_NUM_THREADS:", os.environ.get("OMP_NUM_THREADS"))


def gm(n):
    return 0 if n % 2 else math.prod(range(1, n, 2))


# Direct scalar expansion in X, independent of the tensor-contraction formula.
# F=(w^3 X^3-3wX)/sqrt(6), -L^-1 F=(w^3 X^3/3+(2w^3-3w)X)/sqrt(6).
# Gamma is the product of their derivatives. Integrate X first, then w.
gamma = {(6, 4): Q(1, 2), (6, 2): Q(1), (4, 2): Q(-2),
         (4, 0): Q(-1), (2, 0): Q(3, 2)}
# exponents are (degree in w, degree in X)
kpoly = {}
for (dw, dx), coeff in gamma.items():
    kpoly[dw, 0] = kpoly.get((dw, 0), Q(0)) + coeff * gm(dx)
residual = dict(gamma)
for key, coeff in kpoly.items():
    residual[key] = residual.get(key, Q(0)) - coeff
exact = sum(c * d * gm(i + j) * gm(p + r)
            for (i, p), c in residual.items()
            for (j, r), d in residual.items())
second_way = 38 * gm(12) - 32 * gm(10) + 8 * gm(8)
assert exact == second_way == 365610
print("independent scalar Stein variance:", exact, "PASS")


def score_test(z, offsets, a, lam):
    """Return h_R and its analytic gradient for a sine output channel."""
    r = len(z) - 1
    s = [a * x + o for x, o in zip(z, offsets)]
    value = 0.0
    grad = [0.0] * len(z)
    for y in (-1, 1):
        p = [(1 + y * lam * math.sin(x)) / 2 for x in s]
        dp = [y * lam * math.cos(x) / 2 for x in s]
        ddp0 = -y * lam * math.sin(s[0]) / 2
        den = sum(p[1:]) / r
        value += dp[0] * math.log(den)
        grad[0] += a * ddp0 * math.log(den)
        for j in range(1, r + 1):
            grad[j] += a * dp[0] * dp[j] / (r * den)
    return value, grad


gradient_cases = 0
for r in (1, 2, 7, 31):
    for a in (0.03, 0.65, -1.2):
        for lam in (0.2, 0.9):
            z = [1.7 * math.sin(0.37 * j + 0.2) for j in range(r + 1)]
            offsets = [2.1 * math.cos(0.7 * j) for j in range(r + 1)]
            value, grad = score_test(z, offsets, a, lam)
            c = (1 - lam) / 2
            l1 = l2 = lam / 2
            teacher_bound = abs(a) * 2 * l2 * math.log(1 / c)
            replica_bound = abs(a) * 2 * l1 * l1 / (r * c)
            assert abs(grad[0]) <= teacher_bound + 1e-14
            assert all(abs(x) <= replica_bound + 1e-14 for x in grad[1:])
            assert sum(map(abs, grad)) <= teacher_bound + r * replica_bound + 1e-14
            for j in range(r + 1):
                h = 1e-5
                zp, zm = list(z), list(z)
                zp[j] += h
                zm[j] -= h
                numerical = (score_test(zp, offsets, a, lam)[0]
                             - score_test(zm, offsets, a, lam)[0]) / (2 * h)
                assert abs(numerical - grad[j]) < 2e-9
            gradient_cases += 1
print("finite-difference and summable-gradient checks:", gradient_cases, "PASS")


# Check the exact tanh-channel constants by a different one-variable maximization.
lam = 0.5
max_second = max(lam * abs(j / 10000) * (1 - (j / 10000) ** 2)
                 for j in range(-10000, 10001))
formula_second = 1 / (3 * math.sqrt(3))
assert max_second <= formula_second
assert formula_second - max_second < 1e-8
coefficient = math.log(4) / (3 * math.sqrt(3)) + 0.25
alternate = (2 * (formula_second * math.log(4) + (0.25 ** 2) / 0.25)) / 2
assert abs(coefficient - alternate) < 1e-15
print("tanh-channel L2:", f"{formula_second:.12f}")
print("coefficient multiplying epsilon+ell:", f"{coefficient:.12f}", "PASS")


def normal_simpson(n, bound=9.0):
    assert n % 2 == 0
    h = 2 * bound / n
    scale = h / (3 * math.sqrt(2 * math.pi))
    return [(-bound + j * h,
             (1 if j in (0, n) else (4 if j % 2 else 2))
             * scale * math.exp(-(-bound + j * h) ** 2 / 2))
            for j in range(n + 1)]


def integrate_identity(weights, masses, t, g, gp, n):
    """Direct I, covariance RHS, and exact Stein correction.

    d=k=1. The channel p_y(s)=(1+y*lambda*sin(s))/2 permits analytic
    integration over both teacher and cavity U. Only X,V need quadrature.
    No differentiation of the normalized test is used to compute I.
    """
    lam = 0.55
    a, b, e = math.sqrt(1 - t), math.sqrt(g), math.sqrt(t - g)
    ap, bp, ep_e = -1 / (2 * a), gp / (2 * b), (1 - gp) / 2
    damp = math.exp(-e * e / 2)
    k = [[(15 * w ** 3 * z ** 3 - 9 * (w ** 3 * z + w * z ** 3)
           + 9 * w * z) / 6 for z in weights] for w in weights]
    # This expression for K is obtained by integrating the raw cubic polynomials.
    for i, w in enumerate(weights):
        for j, z in enumerate(weights):
            chaos_k = w ** 3 * z ** 3 + 1.5 * (w ** 3 - w) * (z ** 3 - z)
            assert abs(k[i][j] - chaos_k) < 1e-14
    grid = normal_simpson(n)
    ii = jj = correction = 0.0
    size = len(weights)
    sqrt6 = math.sqrt(6)
    for x, wx in grid:
        f = [(w ** 3 * x ** 3 - 3 * w * x) / sqrt6 for w in weights]
        inverse_grad = [(w ** 3 * x * x + 2 * w ** 3 - 3 * w) / sqrt6
                        for w in weights]
        output_grad = [(3 * w ** 3 * x * x - 3 * w) / sqrt6 for w in weights]
        gamma_minus_k = [[inverse_grad[i] * output_grad[j] - k[i][j]
                          for j in range(size)] for i in range(size)]
        for v, wv in grid:
            theta = [a * ff + b * v for ff in f]
            pplus = [(1 + lam * damp * math.sin(z)) / 2 for z in theta]
            dpplus = [lam * damp * math.cos(z) / 2 for z in theta]
            ddpplus = [-lam * damp * math.sin(z) / 2 for z in theta]
            local_i = local_j = local_c = 0.0
            for y in (-1, 1):
                p = pplus if y == 1 else [1 - z for z in pplus]
                dp = dpplus if y == 1 else [-z for z in dpplus]
                ddp = ddpplus if y == 1 else [-z for z in ddpplus]
                den = sum(m * z for m, z in zip(masses, p))
                logden = math.log(den)
                dpavg = sum(m * z for m, z in zip(masses, dp))
                for i in range(size):
                    local_i += masses[i] * (dp[i] * (ap * f[i] + bp * v)
                                            + ep_e * ddp[i]) * logden
                    mixed_k = sum(masses[j] * k[i][j] * dp[j] for j in range(size))
                    local_j += 0.5 * masses[i] * ((1 - k[i][i]) * ddp[i] * logden
                                       + dp[i] * (gp * dpavg - mixed_k) / den)
                    mixed_residual = sum(masses[j] * gamma_minus_k[i][j] * dp[j]
                                         for j in range(size))
                    local_c += -0.5 * masses[i] * (
                        gamma_minus_k[i][i] * ddp[i] * logden
                        + dp[i] * mixed_residual / den)
            ii += wx * wv * local_i
            jj += wx * wv * local_j
            correction += wx * wv * local_c
    return ii, jj, correction


print("quadrature columns: case, intervals/axis, I, J_K, exact correction, identity error")
cases = [
    ("mixed", [0.55, 0.9, -0.7], [0.2, 0.5, 0.3], 0.4, 0.12, 0.3),
    ("opposite+duplicate", [0.8, -0.8, 0.8], [0.25, 0.25, 0.5], 0.8, 0.16, 0.2),
    ("zero", [0.0], [1.0], 0.4, 0.12, 0.3),
]
for name, weights, masses, t, g, gp in cases:
    previous = None
    for n in (120, 240, 480, 960):
        result = integrate_identity(weights, masses, t, g, gp, n)
        iv, jv, rv = result
        error = iv - jv - rv
        print(name, n, *(f"{z:.12g}" for z in result), f"{error:.3g}")
        if n == 960:
            assert max(abs(z - old) for z, old in zip(result, previous)) < 2e-9
            assert abs(error) < 2e-9
        previous = result
    if name != "zero":
        assert abs(iv - jv) > 1e-5, "example should detect omitted Stein residual"
print("direct normalized quadrature identities: PASS")
print("elapsed seconds:", round(time.monotonic() - started, 3))
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 1_000_000_000
print("peak RSS bytes:", rss)
print("ALL CHECKS PASSED")
