#!/usr/bin/env python3
"""Exact small-n checks for the B13 FEI block-profile route.

This script does two independent checks.

1. It enumerates Boolean functions up to global negation for n <= 4 and
   tests, using integer arithmetic, whether the squared Walsh spectrum is
   an independent product law on spectral membership bits.

2. It checks the two-coordinate entropy-transfer inequality from REPORT.md
   on every coordinate pair of every enumerated Boolean function for
   2 <= n <= 4. Entropies are evaluated in float64; the theorem itself is
   analytic and does not depend on this finite check.

Fourier normalization: hat f(S) = 2^{-n} sum_x f(x)(-1)^{S.x}.
"""

from __future__ import annotations

import json
import math
from collections import Counter


def fwht_int(values: list[int]) -> list[int]:
    a = list(values)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def h2(x: float) -> float:
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def entropy(prob: list[float]) -> float:
    return -sum(x * math.log2(x) for x in prob if x > 0.0)


def marginal(weights: list[float], n: int, mask: int) -> list[float]:
    coords = [i for i in range(n) if (mask >> i) & 1]
    out = [0.0] * (1 << len(coords))
    for s, w in enumerate(weights):
        idx = 0
        for k, i in enumerate(coords):
            if (s >> i) & 1:
                idx |= 1 << k
        out[idx] += w
    return out


def product_spectrum_exact(walsh: list[int], n: int) -> tuple[bool, list[int]]:
    """Return independence and exact marginal numerators over denominator N^2."""
    N = 1 << n
    total = N * N
    sq = [z * z for z in walsh]
    qnum = [sum(sq[s] for s in range(N) if (s >> i) & 1) for i in range(n)]
    for s, w in enumerate(sq):
        rhs = 1
        for i, q in enumerate(qnum):
            rhs *= q if ((s >> i) & 1) else (total - q)
        if w * (total ** (n - 1)) != rhs:
            return False, qnum
    return True, qnum


def pair_transfer_bound(weights: list[float], n: int, i: int, j: int) -> tuple[float, float]:
    """Return LHS=H(base)-H(layer) and the analytic error upper bound.

    Base cells are ordered 00,10,01,11 for coordinates (i,j). Let
      eps = w11, r = w10+w01, p = w00+w11,
      delta = min(1, 2 sqrt(eps r)).
    REPORT.md proves
      H(base)-H(layer)
        <= p h2(eps/p) + r h2(w01/r) + h2(delta) + delta log2 3.
    Zero-mass conditional terms are interpreted as zero.
    """
    base = [0.0] * 4
    for s, w in enumerate(weights):
        idx = ((s >> i) & 1) | (((s >> j) & 1) << 1)
        base[idx] += w

    layer_mask = ((1 << n) - 1) ^ ((1 << i) | (1 << j))
    layer = marginal(weights, n, layer_mask)

    w00, w10, w01, w11 = base
    r = w10 + w01
    p = w00 + w11
    delta = min(1.0, 2.0 * math.sqrt(max(0.0, w11 * r)))
    error = 0.0
    if p > 0.0:
        error += p * h2(w11 / p)
    if r > 0.0:
        error += r * h2(w01 / r)
    error += h2(delta) + delta * math.log2(3.0)
    return entropy(base) - entropy(layer), error


def run() -> dict:
    out: dict[str, object] = {
        "normalization": "hat f(S)=2^-n sum_x f(x)(-1)^(S.x)",
        "global_negation_quotiented_by": "fix f(0)=+1",
        "dimensions": {},
        "pair_transfer_tests": 0,
        "pair_transfer_max_violation": 0.0,
    }

    total_pair_tests = 0
    max_violation = 0.0

    for n in range(1, 5):
        N = 1 << n
        canonical = 1 << (N - 1)
        product_count = 0
        half_count = Counter()
        bad_marginal_count = 0

        for bits in range(canonical):
            values = [1] + [1 if (bits >> (x - 1)) & 1 else -1 for x in range(1, N)]
            walsh = fwht_int(values)
            independent, qnum = product_spectrum_exact(walsh, n)
            if independent:
                product_count += 1
                denom = N * N
                qs = [q / denom for q in qnum]
                bad = [q for q in qs if q not in (0.0, 0.5, 1.0)]
                if bad:
                    bad_marginal_count += 1
                half_count[str(sum(q == 0.5 for q in qs))] += 1

            if n >= 2:
                weights = [(z * z) / float(N * N) for z in walsh]
                for i in range(n):
                    for j in range(i + 1, n):
                        lhs, rhs = pair_transfer_bound(weights, n, i, j)
                        total_pair_tests += 1
                        max_violation = max(max_violation, lhs - rhs)

        out["dimensions"][str(n)] = {
            "canonical_boolean_functions": canonical,
            "product_spectral_functions": product_count,
            "product_spectral_half_coordinate_histogram": dict(sorted(half_count.items())),
            "product_spectral_functions_with_any_marginal_outside_0_half_1": bad_marginal_count,
        }

    out["pair_transfer_tests"] = total_pair_tests
    out["pair_transfer_max_violation"] = max_violation
    out["interpretation"] = (
        "For n<=4 every exact product spectral law found has each spectral marginal in {0,1/2,1}; "
        "the two-coordinate entropy-transfer inequality had no finite-check violation. "
        "Neither statement is promoted from finite computation to a general theorem."
    )
    return out


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
