#!/usr/bin/env python3
"""B15 mesh-band free-energy reduction sanity checks.

This verifies the new coarse-graining identity/inequality in REPORT.md.
It does not test or claim full FEI.
"""
import json
import math
import random

LN2 = math.log(2.0)


def coarse(p, b, delta):
    assert len(p) == len(b) and delta > 0
    assert abs(sum(p) - 1.0) < 1e-10
    X = [math.log2(1.0 / x) for x in b]
    D = sum(pi * xi for pi, xi in zip(p, X))
    bins = {}
    for pi, bi, xi in zip(p, b, X):
        j = math.floor(xi / delta)
        P, M = bins.get(j, (0.0, 0.0))
        bins[j] = (P + pi, M + pi / (bi * bi))
    F = 0.0
    for P, M in bins.values():
        F += 0.5 * P * math.log2(M / P)
    bound = LN2 * delta * delta / 4.0
    return {"D": D, "F": F, "loss": F - D, "bound": bound, "bins": len(bins)}


def punctured(n, c):
    m = 1.0 - 2.0 ** (1 - c) + 2.0 ** (1 - n)
    ah = 2.0 ** (1 - c) - 2.0 ** (1 - n)
    al = 2.0 ** (1 - n)
    p = [m * m, (2**c - 1) * ah * ah, (2**n - 2**c) * al * al]
    b = [m, ah, al * (2**c)]
    I = c * ah + (n - c) * al
    return p, b, I


def one_point(n):
    t = 2.0 ** (1 - n)
    p = [(1 - t) ** 2, (2**n - 1) * t * t]
    b = [1 - t, t]
    I = n * t
    return p, b, I


def random_case(rng, m, delta):
    raw = [rng.expovariate(1.0) for _ in range(m)]
    total = sum(raw)
    p = [x / total for x in raw]
    X = [12 * rng.random() for _ in range(m)]
    b = [2.0 ** (-x) for x in X]
    return coarse(p, b, delta)


def main():
    rng = random.Random(150921)
    max_ratio = 0.0
    for _ in range(5000):
        delta = 10 ** rng.uniform(-2, 0.5)
        out = random_case(rng, rng.randint(2, 20), delta)
        assert out["loss"] >= -1e-10
        assert out["loss"] <= out["bound"] + 1e-10
        ratio = out["loss"] / out["bound"] if out["bound"] else 0.0
        max_ratio = max(max_ratio, ratio)

    eps = 0.01
    structured = []
    for name, fn, args in [
        ("punctured-c3-n8", punctured, (8, 3)),
        ("punctured-c3-n12", punctured, (12, 3)),
        ("punctured-c3-n20", punctured, (20, 3)),
        ("punctured-c4-n20", punctured, (20, 4)),
        ("one-point-n8", one_point, (8,)),
        ("one-point-n16", one_point, (16,)),
        ("one-point-n24", one_point, (24,)),
    ]:
        p, b, I = fn(*args)
        delta = 2.0 * math.sqrt(eps * I / LN2)
        out = coarse(p, b, delta)
        assert out["loss"] <= eps * I + 1e-10
        structured.append(
            {
                "name": name,
                "I": I,
                "delta": delta,
                "D_over_I": out["D"] / I,
                "F_over_I": out["F"] / I,
                "loss_over_I": out["loss"] / I,
                "bins": out["bins"],
            }
        )

    result = {
        "theorem_checked": "0 <= F_pi-D <= (ln 2) delta^2/4",
        "random_cases": 5000,
        "max_observed_loss_over_hoeffding_bound": max_ratio,
        "epsilon_calibration": eps,
        "structured": structured,
        "full_FEI_claim": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
