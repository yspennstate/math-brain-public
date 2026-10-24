#!/usr/bin/env python3
"""Exact-rational self-checks for the random fixed-size restriction currency formulas.

This is a falsification checker for the analytic proof in REPORT.md.  It does not
prove FEI and it does not replace the theorem-sized derivation.
"""
from fractions import Fraction


def falling(a, k):
    z = 1
    for j in range(k):
        z *= a - j
    return z


def theta(n, r, k):
    if r < k:
        return Fraction(0)
    return Fraction(falling(r, k), falling(n, k))


def run(limit=50):
    tested = 0
    failures = []
    for n in range(2, limit + 1):
        for r in range(n + 1):
            t = Fraction(r, n)
            for k in range(2, n + 1):
                th = theta(n, r, k)
                child = k * (1 - t) - 1 + th
                # Remaining-currency contraction, coefficientwise.
                if child < 0 or child > (1 - t) * (k - 1):
                    failures.append(("contraction", n, r, k, child))

                qcoef = t * k - th
                if 0 < r < n:
                    bonus = Fraction(r * (n - r), n * (n - 1))
                    # qcoef - t(k-1) = t-theta_k >= t-theta_2.
                    if qcoef - t * (k - 1) < bonus:
                        failures.append(("bonus", n, r, k, qcoef, bonus))

                if r < n:
                    child_next = k * (1 - Fraction(r + 1, n)) - 1 + theta(n, r + 1, k)
                    lhs = child - child_next
                    ratio = (Fraction(falling(r, k - 1), falling(n - 1, k - 1))
                             if r >= k - 1 else Fraction(0))
                    rhs = Fraction(k, n) * (1 - ratio)
                    if lhs != rhs:
                        failures.append(("increment", n, r, k, lhs, rhs))
                tested += 1

    # Exact one-coordinate aggregate identity on an arbitrary rational level profile.
    n = 9
    W = {2: Fraction(3, 100), 3: Fraction(1, 50), 5: Fraction(7, 200), 9: Fraction(1, 80)}
    P = Fraction(1, 4) * sum((k - 1) * w for k, w in W.items())
    q1 = Fraction(1, 4) * sum((Fraction(k, n) - theta(n, 1, k)) * w for k, w in W.items())
    Wge2 = sum(W.values())
    if n * q1 != P + Wge2 / 4:
        failures.append(("one-step-aggregate", n * q1, P + Wge2 / 4))

    print(f"tested_coefficients={tested}")
    print(f"aggregate_identity={n*q1 == P + Wge2/4}")
    print(f"failures={len(failures)}")
    print(f"PASS={int(not failures)}")
    if failures:
        for row in failures[:20]:
            print(row)
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(run())
