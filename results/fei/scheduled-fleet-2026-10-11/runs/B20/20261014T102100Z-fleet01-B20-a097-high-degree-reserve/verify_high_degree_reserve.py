#!/usr/bin/env python3
"""Exact rational verification of the retained high-degree reserve.

The proof is algebraic and all-dimensional.  This program exhausts Boolean
signs modulo global output sign through four variables and verifies the
Walsh-level identity and its strictness on every degree-at-least-three sign.
"""
from fractions import Fraction as F


def walsh(values, n):
    a = list(map(int, values))
    size = 1 << n
    step = 1
    while step < size:
        for i in range(0, size, 2 * step):
            for j in range(i, i + step):
                x, y = a[j], a[j + step]
                a[j], a[j + step] = x + y, x - y
        step *= 2
    return [F(x, size) for x in a]


def popcount(x):
    return x.bit_count()


def check(values, n):
    h = walsh(values, n)
    p = [x * x for x in h]
    W = [F(0) for _ in range(n + 1)]
    for s, mass in enumerate(p):
        W[popcount(s)] += mass
    I = sum((F(d) * W[d] for d in range(1, n + 1)), F(0))
    p0 = p[0]
    M1 = sum((min(p0, p[1 << i]) for i in range(n)), F(0))
    W2 = W[2] if n >= 2 else F(0)
    Wge3 = sum(W[3:], F(0))
    Q = I - M1 - W2
    W1 = W[1] if n >= 1 else F(0)
    rhs_exact = (W1 - M1) + W2 + sum((F(d) * W[d] for d in range(3, n + 1)), F(0))
    assert Q == rhs_exact
    assert Q >= W2 + 3 * Wge3
    degree = max((d for d, x in enumerate(W) if x), default=0)
    if degree >= 3:
        assert Q > 0
    return degree, Q, W2 + 3 * Wge3


def main():
    functions = assertions = degree3 = 0
    min_positive = None
    for n in range(1, 5):
        size = 1 << n
        # Fix the first truth-table value to +1, quotienting output sign.
        for mask in range(1 << max(0, size - 1)):
            values = [1] + [1 if (mask >> (j - 1)) & 1 else -1 for j in range(1, size)]
            degree, Q, lower = check(values, n)
            functions += 1
            assertions += 3
            if degree >= 3:
                degree3 += 1
                assertions += 1
                if min_positive is None or Q < min_positive:
                    min_positive = Q
    print("claim=B20-A097-HIGH-DEGREE-RESERVE-v1")
    print("candidate=G<=4I+(3/4)U")
    print(f"boolean_functions={functions}")
    print(f"degree_at_least_three={degree3}")
    print(f"exact_assertions={assertions}")
    print(f"minimum_positive_Q_ge3={min_positive}")
    print("identity=Q_ge3=I-M1-W2=(W1-M1)+W2+sum_{d>=3}dW_d")
    print("lower_bound=Q_ge3>=W2+3W_ge3")
    print("strengthened_cut=G<=D_ge2+V1/2+(2/ln2)(I-Q_ge3)")
    print("universal_GU=OPEN")
    print("status=PASS")


if __name__ == "__main__":
    main()
