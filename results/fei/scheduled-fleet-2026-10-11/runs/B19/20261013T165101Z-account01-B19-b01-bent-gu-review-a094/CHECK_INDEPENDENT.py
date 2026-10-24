#!/usr/bin/env python3
"""Independent reconstruction of the B01 ten-variable GU witness."""
from collections import Counter
from fractions import Fraction

ROWS = (31, 52, 7, 34)
CORE = 13594860716390676976
N = 10


def bit_rank(rows, width):
    basis = [0] * width
    for v in rows:
        while v:
            j = v.bit_length() - 1
            if basis[j]:
                v ^= basis[j]
            else:
                basis[j] = v
                break
    return sum(v != 0 for v in basis)


def value(z):
    x, y = z & 15, z >> 4
    phase = sum(((x >> i) & 1) * ((ROWS[i] & y).bit_count() & 1)
                for i in range(4)) & 1
    d = 0 if (CORE >> y) & 1 else 1
    return -1 if phase ^ d else 1


def direct_walsh(vals):
    size = len(vals)
    return [sum(v * (-1 if ((s & z).bit_count() & 1) else 1)
                for z, v in enumerate(vals)) for s in range(size)]


def fix_coordinate(vals, j, bit):
    low = (1 << j) - 1
    out = []
    for u in range(len(vals) // 2):
        z = (u & low) | (bit << j) | ((u >> j) << (j + 1))
        out.append(vals[z])
    return out


def upper_count_histogram(vals):
    histogram = Counter()
    per_child_u_counts = []
    for j in range(N):
        for bit in (0, 1):
            w = direct_walsh(fix_coordinate(vals, j, bit))
            support = {s for s, a in enumerate(w) if a}
            assert len(support) == 256
            assert {abs(w[s]) for s in support} == {32}
            child = Counter()
            for s in support:
                count = sum(1 for t in support if (t & s) == s)
                child[count] += 1
                histogram[count] += 1
            per_child_u_counts.append(child)
    return histogram, per_child_u_counts


def ln_interval_from_atanh(r, terms=28):
    """Exact enclosure for ln(r), r>=1 rational, by positive series."""
    z = (r - 1) / (r + 1)
    term = z
    partial = Fraction(0)
    for k in range(terms):
        partial += term / (2 * k + 1)
        term *= z * z
    lo = 2 * partial
    hi = lo + 2 * term / ((2 * terms + 1) * (1 - z * z))
    return lo, hi


def log2_interval(q):
    power = 1 << (q.bit_length() - 1)
    k = power.bit_length() - 1
    alo, ahi = ln_interval_from_atanh(Fraction(q, power))
    blo, bhi = ln_interval_from_atanh(Fraction(2))
    return Fraction(k) + alo / bhi, Fraction(k) + ahi / blo


def anf_degree(bits):
    a = bits[:]
    for j in range(N):
        for s in range(1 << N):
            if s & (1 << j):
                a[s] ^= a[s ^ (1 << j)]
    return max(s.bit_count() for s, c in enumerate(a) if c)


def main():
    assert bit_rank(ROWS, 6) == 4
    assert all(r != 0 for r in ROWS)
    assert all(any((r >> j) & 1 for r in ROWS) for j in range(6))

    vals = [value(z) for z in range(1 << N)]
    parent = direct_walsh(vals)
    assert set(map(abs, parent)) == {32}

    influences = []
    for j in range(N):
        changes = sum(vals[z] != vals[z ^ (1 << j)]
                      for z in range(1 << N) if not z & (1 << j))
        influences.append(Fraction(changes, 1 << (N - 1)))
    assert influences == [Fraction(1, 2)] * N

    hist, children = upper_count_histogram(vals)
    assert sum(hist.values()) == 5120

    log_lo = log_hi = Fraction(0)
    for c, mult in hist.items():
        lo, hi = log2_interval(c)
        log_lo += mult * lo
        log_hi += mult * hi
    g_lo = 50 - log_hi / 512
    g_hi = 50 - log_lo / 512
    ratio_lo, ratio_hi = g_lo / 5, g_hi / 5
    assert ratio_lo > Fraction(1487, 500)
    assert ratio_hi < Fraction(119, 40)

    truth_bits = [0 if v == 1 else 1 for v in vals]
    degree = anf_degree(truth_bits)
    assert degree > 2

    print('rank=4, all rows/columns nonzero')
    print('parent Walsh magnitudes={32}; H=10, U=5')
    print('coordinate influences=', [str(q) for q in influences], 'I=5')
    print('histogram=', dict(sorted(hist.items())))
    print('G interval=', float(g_lo), float(g_hi))
    print('G/I interval=', float(ratio_lo), float(ratio_hi))
    print('algebraic degree=', degree, '(therefore nonquadratic)')
    print('PASS')


if __name__ == '__main__':
    main()
