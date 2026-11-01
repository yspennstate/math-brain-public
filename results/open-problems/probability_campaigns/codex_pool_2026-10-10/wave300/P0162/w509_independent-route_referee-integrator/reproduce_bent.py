"""Bounded independent truth-table check of the P0162 selector formulas."""
from __future__ import annotations

import json
import math
import time

START = time.perf_counter()


def spectrum(values: list[int]) -> list[float]:
    a = [float(x) for x in values]
    size = len(a)
    step = 1
    while step < size:
        for k in range(0, size, step * 2):
            for j in range(step):
                u, v = a[k + j], a[k + j + step]
                a[k + j], a[k + j + step] = u + v, u - v
        step *= 2
    return [x / size for x in a]


def entropy(coefficients: list[float]) -> float:
    return -sum(p * math.log2(p) for a in coefficients if (p := a * a) > 0)


def influence(values: list[int], bit: int) -> float:
    return sum(values[x] != values[x ^ (1 << bit)] for x in range(len(values))) / len(values)


def check(m: int, flips: tuple[int, ...]) -> dict:
    n = 1 << m
    assert n <= 256 and 0 < len(flips) and 2 * len(flips) < math.sqrt(n)
    g = [(-1) ** sum(((x >> (2 * j)) & 1) * ((x >> (2 * j + 1)) & 1) for j in range(m // 2)) for x in range(n)]
    h = g.copy()
    for x in flips:
        h[x] = -h[x]
    f = g + h  # selector bit is the high bit; the sign does not affect squared spectra
    ug, uh, uf = spectrum(g), spectrum(h), spectrum(f)
    defect = entropy(uf) - (entropy(ug) + entropy(uh)) / 2
    selector_influence = influence(f, m)
    other_influences = [influence(f, j) for j in range(m)]
    assert abs(selector_influence - len(flips) / n) < 1e-12
    assert all(abs(abs(u) - 1 / math.sqrt(n)) < 1e-12 for u in ug)
    k = len(flips)
    b = [(u - v) / 2 for u, v in zip(ug, uh)]
    r = [z * z / selector_influence for z in b if z != 0]
    hr = -sum(q * math.log2(q) for q in r)
    theta = 2 * k / math.sqrt(n)
    lower = hr - math.log2(k) + 2 * math.log2(1 - theta) + 3 / math.log(2)
    upper = hr - math.log2(k) + 2 * math.log2(1 + theta) + 3 / math.log(2)
    ratio = defect / selector_influence
    assert lower - 1e-10 <= ratio <= upper + 1e-10
    out = {"m": m, "K": k, "selector_influence": selector_influence,
           "min_other_influence": min(other_influences), "entropy_defect_ratio": ratio,
           "sparse_lower": lower, "sparse_upper": upper, "spectral_H_r": hr,
           "global_entropy": entropy(uf), "total_influence": sum(other_influences) + selector_influence}
    if k == 1:
        one_point_lower = math.log2(n - 2 * math.sqrt(n) + 2)
        assert ratio + 1e-10 >= one_point_lower
        out["one_point_lower"] = one_point_lower
        assert min(other_influences) > selector_influence
    return out


if __name__ == "__main__":
    cases = [(4, (0,)), (6, (0, 1)), (8, (0, 1, 7))]
    rows = [check(m, E) for m, E in cases]
    assert time.perf_counter() - START < 60
    print(json.dumps({"command": "python -X utf8 reproduce_bent.py", "rows": rows,
                      "elapsed_seconds": time.perf_counter() - START}, indent=2))
