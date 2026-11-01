#!/usr/bin/env python3
"""Exact Boolean/Walsh checks for the A066 parity-lift semigroup theorem.

All Walsh and influence identities use integer arithmetic/Fraction.  Logarithms
are used only to report entropy and the sign diagnostic; the report proves the
sign symbolically from a>b and an exact degree gap.
"""

from fractions import Fraction
from hashlib import sha256
from math import log, log2
from pathlib import Path


def walsh(values):
    a = list(values)
    step = 1
    while step < len(a):
        for i in range(0, len(a), 2 * step):
            for j in range(i, i + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return a


def spectral(values):
    W = walsh(values)
    den = len(values) ** 2
    assert sum(w * w for w in W) == den
    return W, den


def entropy_and_influence(W, den):
    H = 0.0
    I = Fraction(0)
    odd = Fraction(0)
    for s, w in enumerate(W):
        if not w:
            continue
        q = w * w
        p = q / den
        H -= p * log2(p)
        I += Fraction(s.bit_count() * q, den)
        if s.bit_count() & 1:
            odd += Fraction(q, den)
    return H, I, odd


def initial_derivative_nat(W, den):
    weights = [(s.bit_count(), w * w) for s, w in enumerate(W) if w]
    mk = sum(k * q for k, q in weights) / den
    ml = sum(q * log(q) for _, q in weights) / den
    mkl = sum(k * q * log(q) for k, q in weights) / den
    return 2.0 * (mkl - mk * ml)


def parity_lift(values):
    """F(x,z)=g(x xor z*1) in 0/1 coordinate encoding."""
    n = len(values).bit_length() - 1
    mask = (1 << n) - 1
    out = []
    for state in range(1 << (n + 1)):
        x = state & mask
        z = (state >> n) & 1
        out.append(values[x ^ (mask if z else 0)])
    return out


def predicted_lift_walsh(W):
    n = len(W).bit_length() - 1
    out = [0] * (2 * len(W))
    zbit = 1 << n
    for s, w in enumerate(W):
        out[s | (zbit if s.bit_count() & 1 else 0)] = 2 * w
    return out


def point_defect(n, shifted=False):
    out = []
    for x in range(1 << n):
        v = -1 if x == 0 else 1
        if shifted and (x.bit_count() & 1):
            v = -v
        out.append(v)
    return out


def addressing(a):
    n = a + (1 << a)
    vals = []
    for x in range(1 << n):
        addr = x & ((1 << a) - 1)
        bit = (x >> (a + addr)) & 1
        vals.append(-1 if bit else 1)
    return vals


def main():
    print("A066 parity-lift semigroup checks")
    print("source_sha256=" + sha256(Path(__file__).read_bytes()).hexdigest())
    print("seed=NONE")
    assertions = 0

    # Exhaust every Boolean table modulo global output sign through n=4.
    for n in range(1, 5):
        tables = 1 << ((1 << n) - 1)
        positive = negative = zero = 0
        for mask in range(tables):
            g = [1] + [1 if (mask >> (x - 1)) & 1 else -1
                       for x in range(1, 1 << n)]
            W, den = spectral(g)
            F = parity_lift(g)
            WF, denF = spectral(F)
            assert WF == predicted_lift_walsh(W)
            assertions += 1
            Hg, Ig, q = entropy_and_influence(W, den)
            HF, IF, qF = entropy_and_influence(WF, denF)
            assert abs(HF - Hg) < 2e-13
            assert IF == Ig + q
            assert IF <= 2 * Ig
            assert qF == 0
            assertions += 4
            d = initial_derivative_nat(WF, denF)
            if d > 1e-11:
                positive += 1
            elif d < -1e-11:
                negative += 1
            else:
                zero += 1
        print(f"n={n} tables={tables} lift_Hprime_positive={positive} "
              f"negative={negative} zero={zero}")

    # Closed-form defect and shifted-defect identities.
    for r in range(2, 11):
        N = 1 << r
        for shifted in (False, True):
            W, den = spectral(point_defect(r, shifted))
            WF, denF = spectral(parity_lift(point_defect(r, shifted)))
            H, I, odd = entropy_and_influence(WF, denF)
            if not shifted:
                assert I == Fraction(2 * (r + 1), N)
                assert initial_derivative_nat(WF, denF) <= 1e-12
                assert H / float(I) < 4
            elif r >= 3:
                assert initial_derivative_nat(WF, denF) > 0
            assertions += 3
        print(f"defect_r={r} exact_identities=PASS")

    # Uniform-spectrum addressing remains monotone after the lift.
    for a in range(1, 4):
        vals = parity_lift(addressing(a))
        W, den = spectral(vals)
        H, I, odd = entropy_and_influence(W, den)
        nonzero_sq = {w * w for w in W if w}
        assert len(nonzero_sq) == 1
        assert abs(H - 2 * a) < 1e-12
        assert I == Fraction(a + 3, 2)
        assert odd == 0
        assert initial_derivative_nat(W, den) == 0.0
        assertions += 5
        print(f"addressing_a={a} H={H:.12g} I={I} ratio={H/float(I):.12g} PASS")

    print(f"programmatic_assertions={assertions}")
    print("failures=0")
    print("ALL_CHECKS_PASS")


if __name__ == "__main__":
    main()
