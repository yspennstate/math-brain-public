#!/usr/bin/env python3
"""Exact finite checks accompanying agents/047.md; no third-party packages.

These checks supplement the analytic proof.  They are not a proof over all
learning algorithms or distributions.  All comparisons asserted below use
fractions, including the strict failure-probability comparison.
"""

from fractions import Fraction as Q
from itertools import product
from math import prod, sqrt
from random import Random
import json


def gaussian_moment(power, variance):
    if power % 2:
        return Q(0)
    return Q(prod(range(1, power, 2))) * variance ** (power // 2)


def polynomial_multiply(left, right):
    result = {}
    for (a, b), c in left.items():
        for (d, e), f in right.items():
            result[a + d, b + e] = result.get((a + d, b + e), Q(0)) + c * f
    return result


def gaussian_separation_checks():
    checked = []
    for m in range(2, 21):
        # X ~ N(0,1), Y ~ N(0,1/(m-1)), independent.
        # c_m = 1 + (X+(m-1)Y)/m, c_{m-1} = 1+Y.
        a, b = Q(1, m), Q(m - 1, m)
        difference_of_squares = {
            (1, 0): 2 * a,
            (0, 1): 2 * b - 2,
            (2, 0): a * a,
            (1, 1): 2 * a * b,
            (0, 2): b * b - 1,
        }
        square = polynomial_multiply(difference_of_squares, difference_of_squares)
        actual = sum(
            coefficient * gaussian_moment(xpower, Q(1))
            * gaussian_moment(ypower, Q(1, m - 1))
            for (xpower, ypower), coefficient in square.items()
        )
        d, s = Q(1, m * (m - 1)), Q(1, m - 1)
        proposed = 4 * d + 4 * s * d - d * d
        assert actual == proposed
        checked.append(m)

    def beta_a2(m):
        return Q(1, m * (m - 1))

    def beta_v2(m):
        d, s = Q(1, m * (m - 1)), Q(1, m - 1)
        return 4 * d + 4 * s * d - d * d

    def moment_a2(m):
        return 1 + Q(1, m)

    def moment_v2(m):
        return 1 + Q(6, m) + Q(3, m * m)

    n, delta = 1000, Q(1, 20)
    def width(beta, moment):
        term = (moment(n - 1) + (n - 1) * beta(n - 1)) / n
        return sqrt(2 / float(delta)) * (sqrt(float(beta(n))) + sqrt(float(term)))

    ea, ev = width(beta_a2, moment_a2), width(beta_v2, moment_v2)
    return {
        "exact_gaussian_fourth_moment_checks_m": checked,
        "n": n,
        "delta": float(delta),
        "epsilon_A": ea,
        "epsilon_V": ev,
        "lower_probability_of_strict_certified_gain":
            1 - float(delta) - 1 / (n * (1 - ea) ** 2),
    }


def enumerate_order_sensitive_rule(n):
    rng = Random(4700 + n)
    p = Q(2, 5)
    wlaw = ((0, Q(1, 3)), (1, Q(2, 3)))
    table = {}
    for m in (n - 2, n - 1, n):
        for t in product((0, 1), repeat=m):
            for w, _ in wlaw:
                for u in (0, 1):
                    table[t, w, u] = Q(rng.randint(-9, 11), 3)

    def weight(t):
        return p ** sum(t) * (1 - p) ** (len(t) - sum(t))

    def delete(t, i):
        return t[:i] + t[i + 1:]

    def f(t, w, u):
        return table[t, w, u]

    def pf(t, w):
        return (1 - p) * f(t, w, 0) + p * f(t, w, 1)

    def energy(t, td, w):
        return (1 - p) * (f(t, w, 0) - f(td, w, 0)) ** 2 + p * (
            f(t, w, 1) - f(td, w, 1)
        ) ** 2

    def beta2(m):
        return sum(
            weight(t) * pw * sum(energy(t, delete(t, i), w) for i in range(m)) / m
            for t in product((0, 1), repeat=m) for w, pw in wlaw
        )

    bm2 = sum(
        weight(t) * pw * ((1 - p) * f(t, w, 0) ** 2 + p * f(t, w, 1) ** 2)
        for t in product((0, 1), repeat=n - 1) for w, pw in wlaw
    )
    bn2, bn12 = beta2(n), beta2(n - 1)
    qbound = (bm2 + (n - 1) * bn12) / n
    f2 = d2 = h2 = Q(0)
    identities = {(i, j): Q(0) for i in range(n) for j in range(n) if i != j}
    for t in product((0, 1), repeat=n):
        for w, pw in wlaw:
            wt = weight(t) * pw
            fits = [delete(t, i) for i in range(n)]
            hs = [pf(fits[i], w) - f(fits[i], w, t[i]) for i in range(n)]
            dd = pf(t, w) - sum(pf(td, w) for td in fits) / n
            hh = sum(hs) / n
            ff = pf(t, w) - sum(f(fits[i], w, t[i]) for i in range(n)) / n
            assert ff == dd + hh
            f2, d2, h2 = f2 + wt * ff * ff, d2 + wt * dd * dd, h2 + wt * hh * hh
            for i, j in identities:
                common = tuple(value for k, value in enumerate(t) if k not in (i, j))
                hi0 = pf(common, w) - f(common, w, t[i])
                hj0 = pf(common, w) - f(common, w, t[j])
                identities[i, j] += wt * (
                    hs[i] * hs[j] - (hs[i] - hi0) * (hs[j] - hj0)
                )
    assert all(value == 0 for value in identities.values())
    assert d2 <= bn2
    assert h2 <= qbound
    remainder = f2 - bn2 - qbound
    assert remainder <= 0 or remainder * remainder <= 4 * bn2 * qbound
    return {
        "n": n,
        "full_data_seed_configurations": 2 ** n * len(wlaw),
        "ordered_pair_covariance_identities_verified": len(identities),
        "E_F2": str(f2), "E_D2": str(d2), "E_H2": str(h2),
        "beta_n_squared": str(bn2), "beta_n_minus_1_squared": str(bn12),
        "B_n_minus_1_squared": str(bm2), "Q_bound": str(qbound),
        "main_bound_squared_decimal": (sqrt(float(bn2)) + sqrt(float(qbound))) ** 2,
    }


def empirical_plugin_counterexample():
    n, p, delta, b = 100, Q(97, 100), Q(1, 25), 34
    q = 1 - p
    failure_probability = p ** n
    base_second, base_fourth = p + q * b ** 2, p + q * b ** 4
    ba2, bv2 = p ** (n - 1) * base_second, p ** (n - 1) * base_fourth
    ea2, ev2 = 2 * ba2 / (n * delta), 2 * bv2 / (n * delta)
    alignment, correction_energy = p - q * b, base_second
    # These are exact rational checks, not floating-point conclusions.
    assert failure_probability > delta
    assert p ** (n - 1) < Q(1, 20)
    assert ea2 < 1
    assert alignment == -Q(1, 20)
    ea, ev = sqrt(float(ea2)), sqrt(float(ev2))
    gate = min(1, (1 - ea) / (1 + ev))
    risk_increase = -2 * gate * float(alignment) + gate * gate * float(correction_energy)
    assert gate > 0 and risk_increase > 0  # Exact signs already follow above.
    return {
        "n": n, "p": str(p), "delta": str(delta), "negative_correction": -b,
        "failure_probability": float(failure_probability),
        "p_to_n_minus_1": float(p ** (n - 1)),
        "empirical_deletion_energies_on_failure_event": [0, 0],
        "exact_B_A_squared": str(ba2), "exact_B_V_squared": str(bv2),
        "plugin_epsilon_A": ea, "plugin_epsilon_V": ev,
        "actual_A_on_failure_event": str(alignment),
        "actual_V_on_failure_event": str(correction_energy),
        "plugin_gate_on_failure_event": gate,
        "risk_increase_on_failure_event": risk_increase,
    }


if __name__ == "__main__":
    results = {
        "gaussian_separation": gaussian_separation_checks(),
        "finite_order_sensitive_checks": [enumerate_order_sensitive_rule(n) for n in (3, 4)],
        "empirical_plugin_counterexample": empirical_plugin_counterexample(),
        "status": "All exact assertions passed. Numerical fields are supplementary.",
    }
    print(json.dumps(results, indent=2))
