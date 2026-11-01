#!/usr/bin/env python3
"""Exact checker for the A075 row-wise bent-lift theorem.

Frozen pilot: five parameter vectors k_z, maximum full dimension 10, no
randomness, integer FWHT only.  It reconstructs the actual Boolean truth table,
checks Parseval, conditional product rows, and exact H/I formulas.
"""
from fractions import Fraction as F


G = [1, -1, -1, 0, -1, 0, 0, 1, -1, -1, -1, 0, -1, 0, 0, 1]
EDGES = ((3, 11), (5, 13), (6, 14))
ROWS = [G[:]] + [[1 if x in e else 0 for x in range(16)] for e in EDGES]
ALPHA = (F(5, 8), F(1, 8), F(1, 8), F(1, 8))


def parity(x):
    return x.bit_count() & 1


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def bent(u, k):
    exponent = 0
    for j in range(k):
        exponent ^= ((u >> (2 * j)) & 1) & ((u >> (2 * j + 1)) & 1)
    return -1 if exponent else 1


def product_squared(w, bits):
    q = [z * z for z in w]
    total = sum(q)
    marg = []
    for i in range(bits):
        one = sum(q[s] for s in range(1 << bits) if (s >> i) & 1)
        marg.append((total - one, one))
    scale = total ** (bits - 1)
    return all(q[s] * scale == product(marg[i][(s >> i) & 1] for i in range(bits))
               for s in range(1 << bits))


def product(xs):
    z = 1
    for x in xs:
        z *= x
    return z


def full_table(ks):
    K = max(ks)
    out = []
    # Bit order: y0,y1,x0..x3,u0..u(2K-1); y is fastest here.
    for u in range(1 << (2 * K)):
        for x in range(16):
            active = next(z for z, row in enumerate(ROWS) if row[x])
            assert sum(row[x] != 0 for row in ROWS) == 1
            for y in range(4):
                value = ROWS[active][x]
                value *= -1 if parity(active & y) else 1
                value *= bent(u, ks[active])
                assert value in (-1, 1)
                out.append(value)
    return out


def exact_metrics(table):
    w = fwht(table)
    N = len(table)
    assert sum(z * z for z in w) == N * N
    H = F(0)
    I = F(0)
    for s, z in enumerate(w):
        if not z:
            continue
        q = z * z
        assert q & (q - 1) == 0
        mass = F(q, N * N)
        H += mass * ((N * N).bit_length() - 1 - (q.bit_length() - 1))
        I += mass * s.bit_count()
    return H, I, w


def edge_influence(table):
    """Compute total influence directly from bichromatic cube edges."""
    N = len(table)
    n = N.bit_length() - 1
    assert 1 << n == N
    total = F(0)
    for i in range(n):
        disagreements = sum(table[x] != table[x ^ (1 << i)] for x in range(N))
        total += F(disagreements, N)
    return total


def row_table(z, k, K):
    out = []
    for u in range(1 << (2 * K)):
        for x in range(16):
            out.append(ROWS[z][x] * bent(u, k))
    return out


def run():
    tuples = [
        (0, 0, 0, 0),
        (1, 0, 0, 0),
        (0, 1, 1, 1),
        (1, 2, 0, 2),
        (2, 2, 2, 2),
    ]
    assertions = 0
    print("Arithmetic: integers and fractions.Fraction")
    print("Random seed: NONE")
    print("Frozen parameter tuples:", tuples)
    for ks in tuples:
        K = max(ks)
        table = full_table(ks)
        H, I, w = exact_metrics(table)
        I_edges = edge_influence(table)
        L = 5 * ks[0] + ks[1] + ks[2] + ks[3]
        expected_H = F(5) + F(L, 4)
        expected_I = F(17 + L, 8)
        assert H == expected_H
        assert I == expected_I
        assert I_edges == I
        assertions += 4  # Boolean construction, H, Fourier I, edge-count I.
        for z, k in enumerate(ks):
            rw = fwht(row_table(z, k, K))
            assert product_squared(rw, 4 + 2 * K)
            # Row Parseval mass alpha_z in the normalized full x,u cube.
            assert F(sum(v * v for v in rw), (16 * (1 << (2 * K))) ** 2) == ALPHA[z]
            assertions += 2
        print(f"ks={ks} n={6+2*K} H={H} I={I} H/I={H/I} nonzero_spectrum={sum(v!=0 for v in w)}")
    print("Truth tables reconstructed:", len(tuples))
    print("Largest truth table entries:", 1 << 10)
    print("Assertions passed:", assertions)
    print("Assertions failed: 0")
    print("ALL_EXACT_BENT_ROW_LIFT_CHECKS_PASS")


if __name__ == "__main__":
    run()
