#!/usr/bin/env python3
"""Numerical consistency checks for fleet03/B15 auto28.

The proof is analytic. This script only checks the explicit constants and samples
the phase-aligned-set measure m_s on [1,5]. Standard library only.
"""
import math


def normal_two_sided_tail(x: float) -> float:
    return math.erfc(x / math.sqrt(2.0))


def phase_measure_midpoint(s: float, n: int = 2_000_000) -> float:
    a, b = 1.0, 5.0
    dx = (b - a) / n
    total = 0.0
    for j in range(n):
        x = a + (j + 0.5) * dx
        if math.cos(s * x * x) >= 0.5:
            total += dx
    return total


def main() -> None:
    c0 = (1.0 - math.exp(-0.5)) / 8.0
    tail = normal_two_sided_tail(math.pi)
    heat = (c0 - tail) / 74.0
    print("c0 =", repr(c0))
    print("P(|G|>=pi) =", repr(tail))
    print("heat lower bound =", repr(heat))
    assert heat > 6e-4
    assert 1.0 / 292.0 > 0.0034

    for s in (math.pi, 2 * math.pi, 10.0, 50.0):
        m = phase_measure_midpoint(s, n=200_000)
        analytic_lower = 4.0 / 3.0 - math.pi / (3.0 * s)
        print(f"s={s:.8f}: sampled m_s={m:.8f}, analytic lower={analytic_lower:.8f}")
        assert analytic_lower >= 1.0 - 1e-12
        assert m > 0.99


if __name__ == "__main__":
    main()
