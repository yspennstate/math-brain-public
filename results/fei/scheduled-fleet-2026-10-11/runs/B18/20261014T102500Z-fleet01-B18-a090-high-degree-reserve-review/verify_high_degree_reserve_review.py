#!/usr/bin/env python3
"""Independent exact checks for B20-A097-HIGH-DEGREE-RESERVE-v1."""
from fractions import Fraction as F


def walsh(values, n):
    a = list(values)
    step = 1
    while step < len(a):
        for i in range(0, len(a), 2 * step):
            for j in range(i, i + step):
                x, y = a[j], a[j + step]
                a[j], a[j + step] = x + y, x - y
        step *= 2
    return [F(x, 1 << n) for x in a]


def check_spectrum(values, n):
    h = walsh(values, n)
    p = [x * x for x in h]
    W = [F(0) for _ in range(n + 1)]
    for s, x in enumerate(p):
        W[s.bit_count()] += x
    I = sum((F(d) * W[d] for d in range(1, n + 1)), F(0))
    M1 = sum((min(p[0], p[1 << i]) for i in range(n)), F(0))
    W2 = W[2] if n >= 2 else F(0)
    Q = I - M1 - W2
    exact = (W[1] - M1) + W2 + sum((F(d) * W[d] for d in range(3, n + 1)), F(0))
    Wge3 = sum(W[3:], F(0))
    assert Q == exact
    assert Q >= W2 + 3 * Wge3
    degree = max(d for d, x in enumerate(W) if x)
    if degree >= 3:
        assert Q > 0
    return degree, Q


def check_induction_recurrence():
    checks = 0
    for a in (F(0), F(1, 7), F(4), F(17, 3)):
        for b in (F(0), F(1, 4), F(3, 4), F(99, 100)):
            C = a / (1 - b)
            for n in range(1, 33):
                assert a + C * (n - 1) == C * (n - b)
                checks += 1
    return checks


def main():
    functions = assertions = degree3 = 0
    min_q = None
    for n in range(1, 5):
        size = 1 << n
        for mask in range(1 << (size - 1)):
            vals = [1] + [1 if (mask >> (j - 1)) & 1 else -1 for j in range(1, size)]
            degree, q = check_spectrum(vals, n)
            functions += 1
            assertions += 2
            if degree >= 3:
                degree3 += 1
                assertions += 1
                min_q = q if min_q is None or q < min_q else min_q
    recurrence = check_induction_recurrence()
    print("audited_claim=B20-A097-HIGH-DEGREE-RESERVE-v1")
    print("verdict=PASS_AT_REDUCTION_SCOPE")
    print(f"boolean_functions={functions}")
    print(f"degree_at_least_three={degree3}")
    print(f"spectral_assertions={assertions}")
    print(f"minimum_positive_Q_ge3={min_q}")
    print(f"induction_coefficient_checks={recurrence}")
    print("reserve_sign=verified")
    print("reserve_cancellation=exact")
    print("first_unsupported_line=degree_ge3_strengthened_leaf")
    print("material_repair=no")
    print("universal_GU=OPEN")
    print("full_FEI=OPEN")


if __name__ == "__main__":
    main()
