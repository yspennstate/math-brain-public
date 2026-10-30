#!/usr/bin/env python3
"""Diagnostic verification of the spectral-moment assembly.

The all-dimensional inequality is analytic.  This program exhausts Boolean
truth tables through four variables, verifies the half-envelope majorant, and
checks the exact point-defect formulas through dimension 40.
"""

from __future__ import annotations

import math
from decimal import Decimal, getcontext

TOL = 3e-11


def parity(x: int) -> int:
    return x.bit_count() & 1


def walsh_prob(vals: list[int], n: int) -> list[float]:
    N = 1 << n
    return [
        (sum(vals[x] * (-1 if parity(s & x) else 1) for x in range(N)) / N) ** 2
        for s in range(N)
    ]


def envelope_half(p: list[float]) -> float:
    n = (len(p) - 1).bit_length()
    N = 1 << n
    total = 0.0
    for j in range(N):
        m = [0.0] * N
        for s, q in enumerate(p):
            m[s & j] += q
        for a in range(N):
            if a & ~j or m[a] == 0.0:
                continue
            pi = sum(p[s] for s in range(N) if (s & a) == a)
            total += m[a] * math.log2(pi / m[a]) / N
    return total


def moment(p: list[float], base: float = 1.5) -> float:
    return sum(q * (base ** s.bit_count() - 1.0) for s, q in enumerate(p))


def influence(p: list[float]) -> float:
    return sum(s.bit_count() * q for s, q in enumerate(p))


def point_defect_envelope(n: int, t: float = 0.5):
    getcontext().prec = 80
    t = Decimal(str(t))
    two = Decimal(2)
    delta = two ** (-n)
    b = 4 * delta * delta
    total = Decimal(0)
    for j in range(n + 1):
        prob_j = math.comb(n, j) * t**j * (1 - t) ** (n - j)
        m0 = (1 - 2 * delta) ** 2 + (two ** (n - j) - 1) * b
        empty = -m0 * m0.ln() / two.ln() if m0 > 0 else Decimal(0)
        nonempty = b * j * (two ** (n - 1) - two ** (n - j))
        total += prob_j * (empty + nonempty)
    I = 2 * n * delta
    exact_nonempty_ratio = t * (1 - (1 - t / 2) ** (n - 1))
    empty_upper_ratio = 2 * (1 - (1 - t / 2) ** n) / (n * two.ln())
    return total / I, exact_nonempty_ratio, empty_upper_ratio


def main() -> None:
    checked = 0
    min_margin = math.inf
    max_ratio = 0.0
    for n in range(1, 5):
        local_max = 0.0
        for code in range(1 << (1 << n)):
            vals = [1 if (code >> x) & 1 else -1 for x in range(1 << n)]
            p = walsh_prob(vals, n)
            F = envelope_half(p)
            M = moment(p)
            margin = M / math.log(2.0) - F
            if margin < -TOL:
                raise AssertionError((n, code, F, M, margin))
            min_margin = min(min_margin, margin)
            I = influence(p)
            if I > TOL:
                local_max = max(local_max, F / I)
                max_ratio = max(max_ratio, F / I)
            checked += 1
        print(f"n={n}: functions={1 << (1 << n)}, max_Fhalf_over_I={local_max:.15g}")

    for n in range(1, 41):
        ratio, nonempty, empty_upper = point_defect_envelope(n)
        if ratio < nonempty or ratio > nonempty + empty_upper:
            raise AssertionError(("point-defect", n, ratio, nonempty, empty_upper))
        kappa = 2.0 * ((1.25) ** n - 1.0) / n
        if n in (4, 8, 16, 32, 40):
            print(
                f"point_defect_n={n}: Fhalf/I={float(ratio):.15g}, "
                f"moment/I={kappa:.15g}, empty_upper/I={float(empty_upper):.15g}"
            )

    print(f"boolean_functions_checked={checked}")
    print(f"minimum_majorant_margin={min_margin:.17g}")
    print(f"maximum_observed_Fhalf_over_I={max_ratio:.15g}")
    print("point_defect_formula_dimensions=40")
    print("STATUS: PASS")


if __name__ == "__main__":
    main()
