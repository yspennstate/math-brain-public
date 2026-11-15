"""Exact finite-law and independent constant checks; standard library only.

Path laws here test the concentration lemma, not existence of a neural flow.
No infinite-time conclusion is inferred from finite computations.
"""

import json
import math
import os
import random
import resource
import time
from fractions import Fraction as F
from itertools import product
from pathlib import Path

started = time.monotonic()
rng = random.Random(2240401)


def norm2(x):
    return sum(a * a for a in x)


# Three unit-duration blocks, each with a two-dimensional output.
# A single categorical initial variable determines the entire trajectory.
# The first law is constant in time: perfect temporal dependence.
laws = [
    (((1, 0, 1, 0, 1, 0), (-1, 0, -1, 0, -1, 0),
      (0, 1, 0, 1, 0, 1)), (F(1, 4), F(1, 4), F(1, 2))),
    (((1, 0, 0, 1, -1, 0), (-1, 0, 0, -1, 1, 0),
      (0, 1, 1, 0, 0, -1)), (F(1, 3),) * 3),
    (((2, -1, 0, 2, -2, 1), (-1, 2, 1, -2, 0, 0),
      (0, 0, 2, 1, 1, 2)), (F(1, 5), F(1, 2), F(3, 10))),
    (((0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0),
      (0, 0, 0, 0, 0, 0)), (F(1, 3),) * 3),
]

variance_checks = 0
tail_checks = 0
simplified_tail_checks = 0
max_tail_ratio = 0.0
bounded_difference_checks = 0
max_difference_ratio = 0.0
ordered_law_cross_checks = 0
for atoms, probs in laws:
    T = 3
    A2 = max(norm2(atom[j:j + 2]) for atom in atoms for j in (0, 2, 4))
    mu = tuple(sum(p * atom[j] for atom, p in zip(atoms, probs)) for j in range(6))
    path_variance = sum(p * norm2(atom) for atom, p in zip(atoms, probs)) - norm2(mu)
    for m in range(1, 13):
        distribution = []
        for n0 in range(m + 1):
            for n1 in range(m - n0 + 1):
                ns = (n0, n1, m - n0 - n1)
                mult = math.factorial(m)
                for n in ns:
                    mult //= math.factorial(n)
                probability = F(mult)
                for p, n in zip(probs, ns):
                    probability *= p ** n
                centered = tuple(sum(n * atom[j] for n, atom in zip(ns, atoms)) / F(m)
                                 - mu[j] for j in range(6))
                distribution.append((norm2(centered), probability))
        assert sum(p for _, p in distribution) == 1
        assert sum(j * p for j, p in distribution) == path_variance / m
        if m == 4:
            count_law, ordered_law = {}, {}
            for j, p in distribution:
                count_law[j] = count_law.get(j, F(0)) + p
            for labels in product(range(3), repeat=m):
                centered = tuple(sum(atoms[k][j] for k in labels) / F(m) - mu[j]
                                 for j in range(6))
                p = math.prod(probs[k] for k in labels)
                j = norm2(centered)
                ordered_law[j] = ordered_law.get(j, F(0)) + p
            assert ordered_law == count_law
            ordered_law_cross_checks += 1
        variance_checks += 1
        if not A2:
            assert all(j == 0 for j, _ in distribution)
            continue
        mean_norm = sum(math.sqrt(float(j)) * float(p) for j, p in distribution)
        mean_upper = math.sqrt(A2 * T / m)
        assert mean_norm <= mean_upper + 1e-13
        for threshold2 in sorted(set(j for j, _ in distribution)):
            threshold = math.sqrt(float(threshold2))
            if threshold < mean_upper:
                continue
            # >= gives a stronger check than the strict bad event in the proof.
            probability = float(sum(p for j, p in distribution if j >= threshold2))
            bound = math.exp(-m * (threshold - mean_upper) ** 2 / (2 * A2 * T))
            assert probability <= bound + 1e-13
            max_tail_ratio = max(max_tail_ratio, probability / bound)
            tail_checks += 1
            if m * threshold2 >= 4 * A2 * T:
                simple = math.exp(-float(m * threshold2) / (8 * A2 * T))
                assert probability <= simple + 1e-13
                simplified_tail_checks += 1

    # Enumerate actual coordinate replacements, independent of the count-law check.
    m = 4
    for labels in product(range(3), repeat=m):
        centered = tuple(sum(atoms[k][j] for k in labels) / F(m) - mu[j]
                         for j in range(6))
        old_norm = math.sqrt(float(norm2(centered)))
        for i in range(m):
            for k in range(3):
                changed = tuple(centered[j] + F(atoms[k][j] - atoms[labels[i]][j], m)
                                for j in range(6))
                diff = abs(math.sqrt(float(norm2(changed))) - old_norm)
                cap = 2 * math.sqrt(A2 * T) / m
                assert diff <= cap + 1e-13
                if cap:
                    max_difference_ratio = max(max_difference_ratio, diff / cap)
                bounded_difference_checks += 1


# A concrete perfectly time-correlated Rademacher path law.
# Count bad initializations exactly with binomial integers, not Monte Carlo.
m, T, A2, M2 = 512, F(4), F(1), F(1)
alpha, S = M2 / 4, T
threshold = 1 / (2 * alpha * S)
bad_count = sum(math.comb(m, k) for k in range(m + 1)
                if T * F(2 * k - m, m) ** 2 > threshold)
bad_probability = F(bad_count, 2 ** m)
# Independently build the binomial row by addition only.
pascal = [1]
for _ in range(m):
    pascal = [1] + [a + b for a, b in zip(pascal, pascal[1:])] + [1]
assert len(pascal) == m + 1
assert sum(pascal) == 2 ** m
assert sum(pascal[k] for k in range(m + 1)
           if T * F(2 * k - m, m) ** 2 > threshold) == bad_count
assert m >= 2 * M2 * A2 * T * S
markov = 2 * alpha * A2 * T * S / m
concentrated = math.exp(-float(m / (4 * M2 * A2 * T * S)))
assert float(bad_probability) <= concentrated < float(markov)


# Exact algebra for the concentration simplification, using x=sqrt(m/(2 alpha A^2 TS)).
for _ in range(300):
    x = F(rng.randrange(200, 10000), 100)
    assert (x - 1) ** 2 / 2 >= x ** 2 / 8
    M2_test, A2_test, T_test, S_test = [F(rng.randrange(1, 50), 7) for _ in range(4)]
    alpha_test = M2_test / 4
    assert 8 * alpha_test * A2_test * T_test * S_test == 2 * M2_test * A2_test * T_test * S_test
    assert 16 * alpha_test * A2_test * T_test * S_test == 4 * M2_test * A2_test * T_test * S_test


# Optimize the two power constraints independently on a rational grid of horizons.
power_checks = []
for c in (F(1, 10), F(1, 2), F(1), F(11, 10), F(3, 2), F(2), F(3)):
    for kappa in (F(0), F(1, 2), F(3)):
        b = 2 + 2 * kappa
        q = b + max(c - 1, 0)
        a = c / q
        # The concentration constraint is s<=1/b. The two output powers are
        # c*s and 1-(b-1)*s; their maximum lower envelope occurs at 1/q.
        for j in range(501):
            s = F(j, 500) / b
            assert min(c * s, 1 - (b - 1) * s) <= a
        s = 1 / q
        assert s <= 1 / b
        assert min(c * s, 1 - (b - 1) * s) == a
        assert a > c / (c + 2 + 2 * kappa)
        if c > 1:
            beta = (c - 1) / q
            r = c / (c - 1)
            assert beta * r == a
            assert (b - 1) / q - 1 == -a
        power_checks.append({"c": str(c), "kappa": str(kappa), "exponent": str(a)})


# Check explicit horizon substitution and prefactors numerically, including c=1.
max_log_constant_ratio = 0.0
max_logfree_constant_ratio = 0.0
logfree_constant_checks = 0
max_tail_to_power_log_ratio = -math.inf
for _ in range(500):
    A, B, M = [rng.uniform(.01, 3) for _ in range(3)]
    C, h0 = rng.uniform(0, 4), rng.uniform(0, 2)
    c = rng.choice((.1, .5, 1., 1.1, 1.5, 2., 3.))
    kappa = rng.choice((0., .5, 3.))
    b = 2 + 2 * kappa
    q = b + max(c - 1, 0)
    Q = 4 * M * M * A * A * math.exp(2 * h0)
    R = max(1, Q)
    m_num = math.exp(100)
    ell = 101.
    assert m_num >= 2 ** q * R * ell
    u = (m_num / (R * ell)) ** (1 / q)
    assert m_num >= (Q / 2) * u ** b
    assert m_num / (Q * u ** b) >= ell * (1 - 1e-12)
    # Upper-bound the full theorem using (26) and exp(-ell), then compare to (8).
    raw = ((8 * A * A + 16 * A * A * B * B * math.exp(2 * h0) * u ** (b - 1)) / m_num
           + 16 * A * A * math.exp(-ell) + 6 * C * u ** (-c))
    K = 24 * A * A + 16 * A * A * B * B * math.exp(2 * h0) + 6 * C
    final = K * u ** (-c)
    assert raw <= final * (1 + 1e-12)
    max_log_constant_ratio = max(max_log_constant_ratio, raw / final)
    if c > 1:
        r = c / (c - 1)
        # Compare x^r exp(-x) with its analytic maximum in log space.
        x = r * math.exp(rng.uniform(-6, 6))
        log_ratio = r * math.log(x) - x - r * (math.log(r) - 1)
        assert log_ratio <= 1e-11
        max_tail_to_power_log_ratio = max(max_tail_to_power_log_ratio, log_ratio)
        q_free = c + 1 + 2 * kappa
        beta, a = (c - 1) / q_free, c / q_free
        log_m = max(q_free * math.log(2), math.log(Q / 2) / beta) + rng.uniform(0, 10)
        assert beta * log_m >= math.log(Q / 2) - 1e-12
        # Divide all terms of (5) by m^-a before evaluating; this avoids overflow
        # even when the sufficient width itself exceeds floating-point range.
        normalized_raw = (8 * A * A * math.exp(-(1 - a) * log_m)
                          + 16 * A * A * B * B * math.exp(2 * h0)
                          + 6 * C
                          + 16 * A * A * math.exp(a * log_m - math.exp(beta * log_m) / Q))
        K_free = (8 * A * A + 16 * A * A * B * B * math.exp(2 * h0) + 6 * C
                  + 16 * A * A * (r * Q / math.e) ** r)
        assert normalized_raw <= K_free * (1 + 1e-12)
        max_logfree_constant_ratio = max(max_logfree_constant_ratio, normalized_raw / K_free)
        logfree_constant_checks += 1

assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 1024 ** 3
result = {
    "status": "PASS", "seed": 2240401,
    "exact_trajectory_variance_checks": variance_checks,
    "ordered_sample_law_cross_checks": ordered_law_cross_checks,
    "exact_finite_law_tail_checks": tail_checks,
    "simplified_tail_checks": simplified_tail_checks,
    "max_exact_tail_to_bound_ratio": max_tail_ratio,
    "coordinate_replacement_checks": bounded_difference_checks,
    "max_coordinate_difference_to_bound_ratio": max_difference_ratio,
    "exact_rademacher_example": {
        "m": m, "T": str(T), "actual_bad_probability": float(bad_probability),
        "markov_bound": float(markov), "concentration_bound": concentrated,
        "independent_pascal_count_matches": True,
    },
    "exact_concentration_constant_checks": 300,
    "exact_horizon_power_checks": power_checks,
    "explicit_prefactor_checks": 500,
    "max_log_rate_prefactor_ratio": max_log_constant_ratio,
    "logfree_prefactor_checks": logfree_constant_checks,
    "max_logfree_prefactor_ratio": max_logfree_constant_ratio,
    "max_tail_to_power_log_ratio": max_tail_to_power_log_ratio,
    "actual_nice": os.getpriority(os.PRIO_PROCESS, 0),
    "max_rss_bytes_macos": rss,
    "elapsed_seconds": time.monotonic() - started,
    "scope": "Finite-law concentration and algebra audits; not a neural-flow or infinite-time simulation.",
}
Path("concentration_results.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
