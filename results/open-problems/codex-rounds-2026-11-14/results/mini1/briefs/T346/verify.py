"""Small deterministic audits for PROOF.md. Standard library only."""

import itertools
import json
import math
import os
import random
import resource
import statistics
import time
from pathlib import Path

assert os.environ.get("OMP_NUM_THREADS") == "1"
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15, priority
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
started = time.monotonic()
rng = random.Random(346)
normal = statistics.NormalDist()


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def mv(a, v):
    return [dot(row, v) for row in a]


def quad(a, v):
    return dot(v, mv(a, v))


def inverse(a):
    n = len(a)
    b = [list(row) + [float(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for j in range(n):
        k = max(range(j, n), key=lambda i: abs(b[i][j]))
        b[j], b[k] = b[k], b[j]
        pivot = b[j][j]
        assert abs(pivot) > 1e-12
        b[j] = [x / pivot for x in b[j]]
        for i in range(n):
            if i != j:
                factor = b[i][j]
                b[i] = [x - factor * y for x, y in zip(b[i], b[j])]
    return [row[n:] for row in b]


def cdf(t):
    return 0.5 * math.erfc(-t / math.sqrt(2))


def phi(t):
    return math.exp(-t * t / 2) / math.sqrt(2 * math.pi)


def simpson(f, left, right, n=2000):
    step = (right - left) / n
    return step / 3 * (f(left) + f(right) + sum(
        (4 if k % 2 else 2) * f(left + k * step)
        for k in range(1, n)))


rows = []
max_cdf_error = 0.0
max_integral_error = 0.0
min_sign_ratio = math.inf
max_sign_identity_error = 0.0
matrix_cases = 0
halfspace_cases = 0
finite_radius_cases = 0
max_boundary_error = 0.0

for d in range(1, 8):
    for kind in ("isotropic", "diagonal", "correlated"):
        if kind == "isotropic":
            b = [[float(i == j) for j in range(d)] for i in range(d)]
        else:
            lower = [[(0.8 + rng.random() if i == j else
                       0.5 * rng.uniform(-1, 1) if j < i else 0.0)
                      for j in range(d)] for i in range(d)]
            if kind == "diagonal":
                lower = [[lower[i][j] if i == j else 0.0
                          for j in range(d)] for i in range(d)]
            b = [[dot(lower[i], lower[j]) for j in range(d)]
                 for i in range(d)]
            scale = d / sum(b[i][i] for i in range(d))
            b = [[scale * x for x in row] for row in b]
        inv = inverse(b)
        signs = list(itertools.product((-1.0, 1.0), repeat=d))
        sign_quads = [quad(inv, e) for e in signs]
        identity_error = abs(sum(sign_quads) / len(signs)
                             - sum(inv[i][i] for i in range(d)))
        max_sign_identity_error = max(max_sign_identity_error, identity_error)
        e_small = min(signs, key=lambda e: quad(b, e))
        assert quad(b, e_small) <= d + 1e-10
        assert quad(b, e_small) * quad(inv, e_small) >= d * d - 1e-9
        matrix_cases += 1

        raw = [[rng.uniform(-0.2, 0.2) for _ in range(d)] for _ in range(d)]
        deriv = [[(raw[i][j] + raw[j][i]) / 2 for j in range(d)]
                 for i in range(d)]
        for p in (2.01, 3.0, 4.0, math.inf):
            reciprocal = 0.0 if math.isinf(p) else 1.0 / p
            scale = d ** (-reciprocal)
            expected_floor = d ** (1 - 2 * reciprocal)
            sign_max = scale * scale * max(sign_quads)
            ratio = sign_max / expected_floor
            min_sign_ratio = min(min_sign_ratio, ratio)
            assert ratio >= 1 - 1e-10
            if kind == "isotropic":
                assert abs(ratio - 1) < 1e-10
            best = signs[max(range(len(signs)), key=lambda k: sign_quads[k])]
            v = [scale * t for t in best]
            s = math.sqrt(quad(inv, v))
            u = [t / s for t in mv(inv, v)]
            assert abs(quad(b, u) - 1) < 1e-10
            assert abs(dot(u, v) - s) < 1e-10
            lam = quad(deriv, u)
            for a in (0.1, 0.5, 0.75, 0.9, 0.99):
                z = normal.inv_cdf(a)
                eps = 1e-5
                analytic = [phi(z) * (-s - z * lam / 2),
                            phi(z) * (s - z * lam / 2)]
                numerical = []
                for sign in (1, -1):
                    def probability(t):
                        return cdf((z - sign * t * s) / math.sqrt(1 + t * lam))
                    numerical.append((probability(eps) - probability(-eps)) / (2 * eps))
                cdf_error = max(abs(q - r) for q, r in zip(analytic, numerical))
                max_cdf_error = max(max_cdf_error, cdf_error)
                # Independently integrate the conditional density score.
                integral = simpson(lambda t: (s * t + lam * (t*t-1)/2) * phi(t), -12, z)
                integral_error = abs(integral - analytic[0])
                max_integral_error = max(max_integral_error, integral_error)
                loss = max(abs(t) for t in analytic)
                assert abs(loss - phi(z) * (s + abs(z * lam) / 2)) < 1e-10
                assert loss >= phi(z) * math.sqrt(expected_floor) - 1e-10
                rows.append({"d": d, "covariance": kind,
                             "p": "infinity" if math.isinf(p) else p,
                             "a": a, "s": s, "lambda": lam,
                             "halfspace_derivatives": analytic,
                             "cdf_derivatives": numerical,
                             "score_integral": integral,
                             "sign_bound_ratio": ratio})
                if a > 0.5:
                    radius = z / s
                    finite_values = []
                    # Endpoint standard deviations chosen independently of B
                    # and of its derivative: no regularity is used here.
                    for endpoint_sd in (0.01, 0.3, 2.0, 100.0):
                        values = [cdf((z - factor * radius * s) / endpoint_sd)
                                  for factor in (0.99, 1.0, 1.01)]
                        assert values[0] > 0.5
                        assert abs(values[1] - 0.5) < 2e-14
                        assert values[2] < 0.5
                        max_boundary_error = max(max_boundary_error, abs(values[1] - 0.5))
                        finite_values.append({"endpoint_sd": endpoint_sd,
                                              "probabilities": values})
                        finite_radius_cases += 1
                    rows[-1]["halfspace_boundary_radius"] = radius
                    rows[-1]["finite_radius_checks"] = finite_values
                halfspace_cases += 1

assert max_cdf_error < 1e-7
assert max_integral_error < 1e-7
assert max_sign_identity_error < 1e-9
cancellation_z = normal.inv_cdf(0.9)
cancellation_lambda = -2 / cancellation_z
cancellation_derivatives = [phi(cancellation_z) * (-1 - cancellation_z * cancellation_lambda / 2),
                            phi(cancellation_z) * (1 - cancellation_z * cancellation_lambda / 2)]
assert abs(cancellation_derivatives[0]) < 1e-14
assert abs(cancellation_derivatives[1] - 2 * phi(cancellation_z)) < 1e-14
assert max(abs(t) for t in cancellation_derivatives) >= phi(cancellation_z)
summary = {"matrix_cases": matrix_cases, "halfspace_cases": halfspace_cases,
           "finite_radius_cases": finite_radius_cases,
           "max_boundary_probability_error": max_boundary_error,
           "max_cdf_derivative_error": max_cdf_error,
           "max_score_integral_error": max_integral_error,
           "max_sign_average_identity_error": max_sign_identity_error,
           "min_sign_bound_ratio": min_sign_ratio,
           "cancellation_halfspace_derivatives": cancellation_derivatives,
           "nice": priority, "OMP_NUM_THREADS": os.environ["OMP_NUM_THREADS"]}
Path("audit_data.json").write_text(json.dumps({"summary": summary, "rows": rows}, indent=2) + "\n")
print(json.dumps(summary, indent=2))
print("PASS: all assertions; audit_data.json written")
assert time.monotonic() - started < 30
