#!/usr/bin/env python3
"""Deterministic checks for agent 039's Boolean-thinning entropy identities.

No sampling or optimization. Probabilities, their derivatives, and normalized
generator identities are checked using fractions; logarithms use math.log.
Run from the research-session directory with ordinary Python.
"""

from fractions import Fraction as F
from itertools import permutations
from math import comb, log
from pathlib import Path
import json


def poly_thin(law, n, t):
    polys = [[F(0) for _ in range(n + 1)] for _ in range(1 << n)]
    for u, weight in law.items():
        s = u
        while True:
            k, ell = s.bit_count(), (u ^ s).bit_count()
            for j in range(ell + 1):
                polys[s][k + j] += weight * comb(ell, j) * (-1) ** j
            if s == 0:
                break
            s = (s - 1) & u
    p, dp, ddp = [], [], []
    for coeff in polys:
        p.append(sum(c * t**j for j, c in enumerate(coeff)))
        dp.append(sum(j * c * t ** (j - 1) for j, c in enumerate(coeff) if j >= 1))
        ddp.append(sum(j * (j - 1) * c * t ** (j - 2)
                       for j, c in enumerate(coeff) if j >= 2))
    return p, dp, ddp


def conditional_delete(law, n, i):
    bit = 1 << i
    mean = sum(weight for u, weight in law.items() if u & bit)
    if not mean:
        return mean, {}
    result = {}
    for u, weight in law.items():
        if u & bit:
            result[u ^ bit] = result.get(u ^ bit, F(0)) + weight / mean
    return mean, result


def determinant(a):
    size = len(a)
    result = F(0)
    for perm in permutations(range(size)):
        inversions = sum(perm[i] > perm[j] for i in range(size) for j in range(i + 1, size))
        value = F((-1) ** inversions)
        for i, j in enumerate(perm):
            value *= a[i][j]
        result += value
    return result


def dpp_law(k):
    n = len(k)
    minors = {}
    for u in range(1 << n):
        indices = [i for i in range(n) if u & (1 << i)]
        minors[u] = determinant([[k[i][j] for j in indices] for i in indices])
    law = {}
    for s in range(1 << n):
        law[s] = sum((-1) ** ((u ^ s).bit_count()) * minors[u]
                     for u in range(1 << n) if u & s == s)
    assert all(value >= 0 for value in law.values())
    assert sum(law.values()) == 1
    return law


def product_law(means):
    result = {}
    for s in range(1 << len(means)):
        weight = F(1)
        for i, mean in enumerate(means):
            weight *= mean if s & (1 << i) else 1 - mean
        result[s] = weight
    return result


def psi(a, b):
    if not a:
        return float(b)
    assert b > 0
    return float(a) * log(float(a / b)) - float(a) + float(b)


def check(name, law, n, t, expect_product=False):
    assert sum(law.values()) == 1
    assert all(value >= 0 for value in law.values())
    p, dp, ddp = poly_thin(law, n, t)
    assert sum(p) == 1 and sum(dp) == 0 and sum(ddp) == 0
    for s in range(1 << n):
        incoming = [s | (1 << i) for i in range(n) if not s & (1 << i)]
        assert t * dp[s] == s.bit_count() * p[s] - sum(p[u] for u in incoming)
        assert t * ddp[s] == (s.bit_count() - 1) * dp[s] - sum(dp[u] for u in incoming)

    entropy_prime = -sum(float(dp[s]) * log(float(p[s])) for s in range(1 << n) if p[s])
    fisher = sum(dp[s] ** 2 / p[s] for s in range(1 << n) if p[s])
    entropy_second = -float(fisher) - sum(float(ddp[s]) * log(float(p[s]))
                                        for s in range(1 << n) if p[s])
    first_rhs, second_rhs, marginal_second = 0.0, 0.0, F(0)
    chi_penalty, other_edge_penalty = 0.0, 0.0
    max_kl_error, kl_rows = 0.0, []
    for i in range(n):
        mean, qi = conditional_delete(law, n, i)
        if not mean:
            continue
        q, dq, _ = poly_thin(qi, n, t)
        bit = 1 << i
        for s in range(1 << n):
            if not s & bit:
                assert p[s | bit] == t * mean * q[s]
        ratio = [q[s] / p[s] if p[s] else F(0) for s in range(1 << n)]
        kl = sum(float(q[s]) * log(float(ratio[s])) for s in range(1 << n) if q[s])
        kl_direct = sum(float(dq[s]) * log(float(ratio[s])) - float(q[s] * dp[s] / p[s])
                        for s in range(1 << n) if q[s])
        edge_all, edge_other = 0.0, 0.0
        for u in range(1 << n):
            if not p[u]:
                continue
            for j in range(n):
                if u & (1 << j):
                    v = u ^ (1 << j)
                    contribution = float(p[u]) * psi(ratio[u], ratio[v]) / float(t)
                    assert contribution >= -1e-12
                    edge_all += contribution
                    if j != i:
                        edge_other += contribution
        chi_square = F(0)
        for s in range(1 << n):
            if not s & bit and p[s]:
                pzero = p[s] / (1 - t * mean)
                chi_square += (q[s] - pzero) ** 2 / pzero
        self_edge = mean * (1 + chi_square) / (1 - t * mean)
        max_kl_error = max(max_kl_error, abs(kl_direct - edge_all),
                           abs(edge_all - float(self_edge) - edge_other))
        assert abs(kl_direct - edge_all) < 1e-10
        assert abs(edge_all - float(self_edge) - edge_other) < 1e-10
        assert edge_all >= float(mean / (1 - t * mean)) - 1e-12
        first_rhs -= float(mean) * (log(float(t * mean)) + kl)
        second_rhs -= float(mean / t) + float(mean) * edge_all
        marginal_second -= mean / (t * (1 - t * mean))
        chi_penalty += float(mean**2 * chi_square / (1 - t * mean))
        other_edge_penalty += float(mean) * edge_other
        kl_rows.append({"coordinate": i, "mean": str(mean), "kl": kl,
                        "kl_derivative": edge_all, "chi_square": str(chi_square)})

    refined_rhs = float(marginal_second) - chi_penalty - other_edge_penalty
    assert abs(entropy_prime - first_rhs) < 1e-10
    assert abs(entropy_second - second_rhs) < 1e-10
    assert abs(entropy_second - refined_rhs) < 1e-10
    if expect_product:
        assert chi_penalty < 1e-12 and other_edge_penalty < 1e-12
        assert abs(entropy_second - float(marginal_second)) < 1e-10
    else:
        assert entropy_second < float(marginal_second) - 1e-9
    return {"name": name, "n": n, "t": str(t), "fisher_exact": str(fisher),
            "entropy_first": entropy_prime, "entropy_second": entropy_second,
            "marginal_entropy_second": float(marginal_second),
            "chi_square_penalty": chi_penalty, "other_edge_penalty": other_edge_penalty,
            "maximum_kl_identity_error": max_kl_error,
            "curvature_identity_error": abs(entropy_second - refined_rhs), "kl_rows": kl_rows}


def main():
    k = [[F(1, 2), F(1, 8), F(1, 10)],
         [F(1, 8), F(2, 5), F(1, 12)],
         [F(1, 10), F(1, 12), F(1, 3)]]
    # Strict diagonal dominance proves both K>0 and I-K>0 exactly.
    for i in range(3):
        radius = sum(abs(k[i][j]) for j in range(3) if i != j)
        assert k[i][i] > radius and 1 - k[i][i] > radius
    examples = [
        ("independent_with_deterministic_coordinates", product_law([F(0), F(1), F(2, 5), F(3, 4)]), 4, F(2, 3), True),
        ("perfect_positive_dependence", {0: F(1, 2), 3: F(1, 2)}, 2, F(1, 2), False),
        ("one_hot_negative_dependence", {1: F(1, 2), 2: F(1, 3), 4: F(1, 6)}, 3, F(3, 5), False),
        ("even_parity", {0: F(1, 4), 3: F(1, 4), 5: F(1, 4), 6: F(1, 4)}, 3, F(4, 5), False),
        ("asymmetric_four_site_law", {0: F(1, 10), 3: F(1, 5), 5: F(1, 10), 8: F(1, 5), 14: F(2, 5)}, 4, F(3, 7), False),
        ("non_diagonal_three_site_dpp", dpp_law(k), 3, F(5, 7), False),
    ]
    output = {"method": "six fixed cases; rational thinning and derivatives; floating logarithms; no sampling",
              "results": [check(*example) for example in examples]}
    destination = Path(__file__).with_name("039_scalar_thinning_output.json")
    destination.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
