#!/usr/bin/env python3
"""Exact certificate for a 10-bit bent nullity-two shield with G/I > 2.974."""
from collections import Counter
from fractions import Fraction

M = (31, 52, 7, 34)
D_MASK = 13594860716390676976
M_DATA = 6
R = 4


def fwht(a):
    a = a[:]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def truth_table():
    vals = []
    for y in range(1 << M_DATA):
        d = 1 if (D_MASK >> y) & 1 else -1
        for x in range(1 << R):
            phase = 0
            for i, row in enumerate(M):
                phase ^= ((x >> i) & 1) & ((row & y).bit_count() & 1)
            vals.append(d if phase == 0 else -d)
    return vals


def restrict(vals, j, bit):
    b = 1 << j
    return [v for z, v in enumerate(vals) if ((z & b) != 0) == bool(bit)]


def rank(rows, width):
    rows = list(rows)
    r = 0
    for col in range(width):
        p = next((k for k in range(r, len(rows)) if (rows[k] >> col) & 1), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        for k in range(len(rows)):
            if k != r and ((rows[k] >> col) & 1):
                rows[k] ^= rows[r]
        r += 1
    return r


def log_interval_integer(q, terms=36):
    """Rigorous Fraction enclosure of log_2(q), q a positive integer."""
    if q == 1:
        return Fraction(0), Fraction(0)
    k = q.bit_length() - 1
    base = 1 << k
    x = Fraction(q - base, q + base)  # ln(q/base)=2 atanh(x)

    def ln_atanh_interval(t):
        lo = 2 * sum((t ** (2*j + 1)) / (2*j + 1) for j in range(terms))
        tail = 2 * (t ** (2*terms + 1)) / ((2*terms + 1) * (1 - t*t))
        return lo, lo + tail

    nlo, nhi = ln_atanh_interval(x)
    dlo, dhi = ln_atanh_interval(Fraction(1, 3))  # ln 2
    return Fraction(k) + nlo / dhi, Fraction(k) + nhi / dlo


def child_histogram(vals):
    hist = Counter()
    for j in range(10):
        for bit in (0, 1):
            child = restrict(vals, j, bit)
            w = fwht(child)
            support = [s for s, z in enumerate(w) if z]
            assert len(support) == 256
            assert {abs(w[s]) for s in support} == {32}
            A = set(support)
            for s in support:
                free = 511 ^ s
                q, count = free, 0
                while True:
                    count += (s | q) in A
                    if q == 0:
                        break
                    q = (q - 1) & free
                hist[count] += 1
    return hist


def main():
    assert rank(M, M_DATA) == 4
    assert all(any((row >> j) & 1 for row in M) for j in range(M_DATA))
    vals = truth_table()
    walsh = fwht(vals)
    assert {abs(z) for z in walsh} == {32}  # bent: p_S=1/1024

    disagree = 0
    for j in range(10):
        b = 1 << j
        disagree += sum(vals[z] != vals[z ^ b] for z in range(1024) if not z & b)
    I = Fraction(disagree, 512)
    assert I == 5

    hist = child_histogram(vals)
    assert sum(hist.values()) == 20 * 256
    slo = Fraction(0); shi = Fraction(0)
    for count, multiplicity in sorted(hist.items()):
        lo, hi = log_interval_integer(count)
        slo += multiplicity * lo
        shi += multiplicity * hi

    # Parent U=5. G=10*5-(1/2)*(1/256)*sum log2(count).
    Glo = Fraction(50) - shi / 512
    Ghi = Fraction(50) - slo / 512
    ratio_lo, ratio_hi = Glo / I, Ghi / I
    assert ratio_lo > Fraction(1487, 500)  # 2.974
    assert ratio_hi < Fraction(2975, 1000) # 2.975

    print('rank(M)=4; all six physical columns nonzero')
    print('Walsh magnitudes:', sorted({abs(z) for z in walsh}))
    print('H=10, U=5, I=5 (exact)')
    print('child upper-count histogram:', dict(sorted(hist.items())))
    print('G interval:', float(Glo), float(Ghi))
    print('G/I interval:', float(ratio_lo), float(ratio_hi))
    print('CERTIFIED: G/I > 2.974, hence every G <= a I + b U bound on this class requires a+b > 2.974')


if __name__ == '__main__':
    main()
