#!/usr/bin/env python3
import itertools
import json
import math
import random

TOL = 1e-10


def entropy(probs):
    return -sum(p * math.log2(p) for p in probs if p > 0.0)


def marginal_dist(weights, n, block):
    block = tuple(block)
    out = [0.0] * (1 << len(block))
    for x, p in enumerate(weights):
        y = 0
        for j, i in enumerate(block):
            if (x >> i) & 1:
                y |= 1 << j
        out[y] += p
    return out


def total_correlation(weights, n, block):
    block = tuple(block)
    if not block:
        return 0.0
    h_joint = entropy(marginal_dist(weights, n, block))
    h_marg = 0.0
    for i in block:
        p = sum(w for x, w in enumerate(weights) if (x >> i) & 1)
        h_marg += entropy((p, 1.0 - p))
    return h_marg - h_joint


def all_q_checks(weights, n):
    T = total_correlation(weights, n, range(n))
    rows = []
    for q in range(1, n):
        vals = [
            total_correlation(weights, n, B)
            for B in itertools.combinations(range(n), q)
        ]
        bar_T = sum(vals) / len(vals)
        K = T - (n / q) * bar_T
        factor = (n - q) / (q * (n - 1))
        floor = factor * T
        rows.append(
            {
                "q": q,
                "T": T,
                "bar_T_q": bar_T,
                "K_q": K,
                "factor": factor,
                "floor": floor,
                "slack": K - floor,
            }
        )
    return rows


def main():
    rng = random.Random(20260921)
    min_random_slack = float("inf")
    random_cases = 0

    for n in range(2, 7):
        for _ in range(100):
            raw = [rng.expovariate(1.0) for _ in range(1 << n)]
            z = sum(raw)
            weights = [x / z for x in raw]
            for row in all_q_checks(weights, n):
                random_cases += 1
                min_random_slack = min(min_random_slack, row["slack"])
                if row["slack"] < -TOL:
                    raise AssertionError((n, row))

    max_common_bit_abs_slack = 0.0
    common_bit_cases = 0
    for n in range(2, 9):
        weights = [0.0] * (1 << n)
        weights[0] = 0.5
        weights[-1] = 0.5
        for row in all_q_checks(weights, n):
            common_bit_cases += 1
            max_common_bit_abs_slack = max(
                max_common_bit_abs_slack, abs(row["slack"])
            )
            if abs(row["slack"]) > TOL:
                raise AssertionError(("common-bit", n, row))

    n = 20
    T_phase_floor = 0.0579604858411688
    stress = {}
    for q in (1, 2, 3, 5, 10, 19):
        factor = (n - q) / (q * (n - 1))
        stress[str(q)] = {
            "factor": factor,
            "K_floor_bits": factor * T_phase_floor,
        }

    out = {
        "status": "PASS",
        "tolerance": TOL,
        "random_probability_law_cases": random_cases,
        "min_random_slack": min_random_slack,
        "common_bit_equality_cases": common_bit_cases,
        "max_common_bit_abs_slack": max_common_bit_abs_slack,
        "stress_n20_T_floor_bits": T_phase_floor,
        "stress_fixed_q": stress,
        "note": (
            "Random tests are implementation evidence only. The theorem is the "
            "analytic monotone-slope proof in REPORT.md; the common-bit law "
            "attains the coefficient exactly."
        ),
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
