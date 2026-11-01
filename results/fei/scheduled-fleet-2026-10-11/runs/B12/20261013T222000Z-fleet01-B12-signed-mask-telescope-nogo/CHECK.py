#!/usr/bin/env python3
"""Exact finite certificate and tensor controls for the A058 telescope no-go."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import log2


Q = (1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0)
G = (1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, -1, 1, 0, 0, 0)


def fwht(values):
    a = [Fraction(x) for x in values]
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2 * step):
            for j in range(start, start + step):
                x, y = a[j], a[j + step]
                a[j], a[j + step] = x + y, x - y
        step *= 2
    return tuple(x / len(a) for x in a)


def raw_entropy(values):
    answer = 0.0
    for coefficient in fwht(values):
        square = coefficient * coefficient
        if square:
            answer += float(square) * log2(1.0 / float(square))
    return answer


def tensor(left, right):
    return tuple(x * y for x in left for y in right)


def restrict_many(values, coordinates, bits):
    n = len(values).bit_length() - 1
    fixed = dict(zip(coordinates, bits))
    free = [i for i in range(n) if i not in fixed]
    out = []
    for y in range(1 << len(free)):
        x = sum(fixed[i] << i for i in fixed)
        x += sum(((y >> j) & 1) << i for j, i in enumerate(free))
        out.append(values[x])
    return tuple(out)


def corrected_potential(u, v, h):
    a = tuple(Fraction(x + y, 2) for x, y in zip(u, v))
    b = tuple(Fraction(y - x, 2) for x, y in zip(u, v))
    hb = tuple(x * y for x, y in zip(h, b))
    f = tuple(x + y for x, y in zip(a, hb))
    return raw_entropy(f) - raw_entropy(hb) + raw_entropy(b)


def main():
    # Exact four-bit Boolean realization.
    a = tuple(1 - q for q in Q)
    u = tuple(x - y for x, y in zip(a, G))
    v = tuple(x + y for x, y in zip(a, G))
    h = v
    b = G
    hb = tuple(x * y for x, y in zip(h, b))
    f = tuple(x + y for x, y in zip(a, hb))
    assert set(u) <= {-1, 1} and set(v) <= {-1, 1} and set(h) <= {-1, 1}
    assert b == G and hb == Q and f == (1,) * 16

    q_numerators = tuple(int(x * 16) for x in fwht(Q))
    g_numerators = tuple(int(x * 16) for x in fwht(G))
    assert Counter(abs(x) for x in q_numerators) == Counter({2: 15, 6: 1})
    assert Counter(abs(x) for x in g_numerators) == Counter({0: 10, 4: 6})
    expected_q = Fraction(9, 64) * log2(64 / 9) + Fraction(90, 64)
    expected_g = 1.5
    exact_formula_value = (6 - 9 * log2(64 / 9)) / 64
    assert abs(raw_entropy(Q) - expected_q) < 1e-14
    assert abs(raw_entropy(G) - expected_g) < 1e-14
    assert abs(corrected_potential(u, v, h) - exact_formula_value) < 1e-14
    assert exact_formula_value < -0.3

    # Every nonempty face has identical absolute spectra for Q and G.
    faces = 0
    block_drops = 0
    for size in range(1, 5):
        for coordinates in combinations(range(4), size):
            child_average = 0.0
            for bits in product((0, 1), repeat=size):
                qr = restrict_many(Q, coordinates, bits)
                gr = restrict_many(G, coordinates, bits)
                assert sorted(abs(x) for x in fwht(qr)) == sorted(
                    abs(x) for x in fwht(gr))
                ur = restrict_many(u, coordinates, bits)
                vr = restrict_many(v, coordinates, bits)
                hr = restrict_many(h, coordinates, bits)
                child = corrected_potential(ur, vr, hr)
                assert abs(child) < 1e-14
                child_average += child
                faces += 1
            child_average /= 1 << size
            assert abs(corrected_potential(u, v, h) - child_average
                       - exact_formula_value) < 1e-14
            block_drops += 1

    # Tensor family: J_m = m p^(m-1) J_1, p=3/8.
    q_power = (1,)
    g_power = (1,)
    tensor_rows = []
    p = Fraction(3, 8)
    for m in range(1, 5):
        q_power = tensor(q_power, Q)
        g_power = tensor(g_power, G)
        observed = raw_entropy(g_power) - raw_entropy(q_power)
        predicted = m * float(p ** (m - 1)) * exact_formula_value
        assert abs(observed - predicted) < 2e-12
        assert observed < 0
        tensor_rows.append((m, 4 * m, len(q_power), observed))

    print("q_walsh_numerator_counts=" + repr(Counter(abs(x) for x in q_numerators)))
    print("g_walsh_numerator_counts=" + repr(Counter(abs(x) for x in g_numerators)))
    print(f"E_q={raw_entropy(Q):.17g}")
    print(f"E_g={raw_entropy(G):.17g}")
    print("J_exact=(6-9*log2(64/9))/64")
    print(f"J_numeric={exact_formula_value:.17g}")
    print(f"certified_nonempty_faces={faces}")
    print(f"certified_query_blocks={block_drops}")
    for m, dimension, length, observed in tensor_rows:
        print(f"tensor_m={m} dimension={dimension} table_size={length} J={observed:.17g}")
    print("full_FEI=OPEN")
    print("PASS")


if __name__ == "__main__":
    main()
