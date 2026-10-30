#!/usr/bin/env python3
"""Independent reconstruction of the B05 balanced-preconditioned transfer.

This checker deliberately does not import or execute the producer's checker.
Walsh coefficients are reconstructed from the character definition.  The
all-dimensional proof is analytic; these finite checks are corroborative.
"""

from fractions import Fraction
import itertools
import math
import random

ETA = 0.25
C = 1.75
SEED = 202610140544
TOL = 3e-11


def spectrum(values):
    npts = len(values)
    out = []
    for mask in range(npts):
        raw = 0
        for x, value in enumerate(values):
            raw += value * (-1 if (mask & x).bit_count() & 1 else 1)
        out.append(Fraction(raw * raw, npts * npts))
    return out


def caps(p):
    n = len(p).bit_length() - 1
    out = p[:]
    for bit_index in range(n):
        bit = 1 << bit_index
        for s in range(len(out)):
            if not s & bit:
                out[s] += out[s | bit]
    return out


def upper_entropy(values):
    p = spectrum(values)
    pi = caps(p)
    total = 0.0
    for mass, cap in zip(p, pi):
        if mass:
            total += float(mass) * math.log2(float(cap / mass))
    return total


def restriction(values, coordinate, bit):
    n = len(values).bit_length() - 1
    result = []
    for reduced in range(1 << (n - 1)):
        low = reduced & ((1 << coordinate) - 1)
        high = reduced >> coordinate
        x = low | (bit << coordinate) | (high << (coordinate + 1))
        result.append(values[x])
    return tuple(result)


def stats(values):
    p = spectrum(values)
    n = len(values).bit_length() - 1
    U = upper_entropy(values)
    I = sum(s.bit_count() * float(p[s]) for s in range(len(p)))
    G = 0.0
    for i in range(n):
        G += U - 0.5 * (
            upper_entropy(restriction(values, i, 0))
            + upper_entropy(restriction(values, i, 1))
        )
    B = 0.0
    for i in range(n):
        bit = 1 << i
        for s in range(len(p)):
            if s & bit:
                continue
            a = float(p[s])
            b = float(p[s | bit])
            pair = a + b
            if a:
                B += a * math.log2(pair / a)
            if b:
                B += b * math.log2(pair / b)
    return U, I, G, B, G - B


def residual(values):
    U, I, _G, _B, M = stats(values)
    return M + (1.0 + ETA) * U - C * I


def transform(q):
    # Bit 0 is the fair selector z; the new high bit is y.
    # At z=1 the value is 1. At z=0 it is y*q(x).
    out = []
    n = len(q).bit_length() - 1
    for ybit in (0, 1):
        y = -1 if ybit == 0 else 1
        for x in range(1 << n):
            out.extend((y * q[x], 1))
    return tuple(out)


def zlog(x):
    return 0.0 if x == 0.0 else x * math.log2(1.0 / x)


def R(t):
    left = (1.0 + t) ** 2 / 4.0
    right = (1.0 - t) ** 2 / 4.0
    endpoint = zlog(left)
    if right:
        endpoint += right * math.log2(2.0 / (1.0 - t))
    old = 0.0 if t == 0.0 else t * t * math.log2(1.0 / (t * t))
    return endpoint - old / 2.0 + (1.0 - t * t) / 4.0


def T(a, b):
    pair = a + b
    return (
        (0.0 if a == 0.0 else a * math.log2(pair / a))
        + (0.0 if b == 0.0 else b * math.log2(pair / b))
    )


def d(h):
    return R(0.0) - 0.5 * (R(h) + R(-h)) - 0.5 * T(1.0, h * h)


def product(f, g):
    return tuple(a * b for b in g for a in f)


def main():
    max_scalar = (-1e100, None)
    for j in range(500_001):
        h = j / 500_000.0
        gap = d(h) - h * h / 2.0
        if gap > max_scalar[0]:
            max_scalar = (gap, h)
        assert gap <= 2e-12

    cores = []
    for n in range(4):
        cores.extend(itertools.product((-1, 1), repeat=1 << n))
    rng = random.Random(SEED)
    for _ in range(1024):
        cores.append(tuple(1 if rng.getrandbits(1) else -1 for _ in range(16)))

    max_identity_error = 0.0
    max_transfer = -1e100
    restriction_checks = 0
    for q in cores:
        tq = transform(q)
        m = sum(q) / len(q)
        observed = residual(tq) - 0.5 * residual(q)
        predicted = d(m) + 1.0 + ETA - C
        max_identity_error = max(max_identity_error, abs(observed - predicted))
        max_transfer = max(max_transfer, observed)
        assert abs(observed - predicted) <= TOL
        assert observed <= TOL

        # Physical-input accounting: selector, balancing sign, then old inputs.
        n = len(q).bit_length() - 1
        assert restriction(tq, 0, 1) == tuple(1 for _ in range(len(q) * 2))
        balanced = tuple(-v for v in q) + tuple(q)
        assert restriction(tq, 0, 0) == balanced
        restriction_checks += 2
        for i in range(n):
            for bit in (0, 1):
                assert restriction(tq, i + 1, bit) == transform(restriction(q, i, bit))
                restriction_checks += 1

    # Independently test additivity of L on disjoint products.
    product_checks = 0
    small = cores[:278]
    for _ in range(256):
        f = small[rng.randrange(len(small))]
        g = small[rng.randrange(len(small))]
        lhs = residual(product(f, g))
        rhs = residual(f) + residual(g)
        assert abs(lhs - rhs) <= TOL
        product_checks += 1

    # The two balancing restrictions explicitly expose the uncovered A(q), A(-q).
    q = (-1, -1, -1, 1)
    tq = transform(q)
    y_coordinate = len(q).bit_length()
    y_minus = restriction(tq, y_coordinate, 0)
    y_plus = restriction(tq, y_coordinate, 1)
    assert y_minus != y_plus

    print("status=PASS")
    print("scalar_checks=500001")
    print(f"boolean_cores_checked={len(cores)}")
    print(f"transfer_identity_checks={len(cores)}")
    print(f"physical_restriction_checks={restriction_checks}")
    print(f"product_additivity_checks={product_checks}")
    print(f"max_identity_error={max_identity_error:.3e}")
    print(f"max_transfer_residual={max_transfer:.15f}")
    print(f"max_scalar_gap={max_scalar[0]:.3e}")
    print(f"max_scalar_gap_h={max_scalar[1]:.8f}")
    print(f"seed={SEED}")


if __name__ == "__main__":
    main()
