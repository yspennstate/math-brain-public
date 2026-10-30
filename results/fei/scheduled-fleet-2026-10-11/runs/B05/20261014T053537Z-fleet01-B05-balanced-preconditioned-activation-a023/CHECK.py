#!/usr/bin/env python3
"""Corroborate the balanced-preconditioned activation transfer.

The all-dimensional result is analytic in PROOF.md.  This program checks the
scalar lemma on a dense deterministic grid, reconstructs U,G,B,M,I directly
from Boolean truth tables, and tests the exact transfer identity on exhaustive
small cores and seeded four-bit cores.
"""

from fractions import Fraction
import itertools
import math
import random

ETA = 0.25
C = 1.75
SEED = 202610140528
TOL = 2e-10


def fwht(values):
    a = [Fraction(v) for v in values]
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2 * h):
            for k in range(j, j + h):
                x, y = a[k], a[k + h]
                a[k], a[k + h] = x + y, x - y
        h *= 2
    return [x / len(a) for x in a]


def caps(p):
    out = list(p)
    n = len(p).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(len(p)):
            if not s & bit:
                out[s] += out[s | bit]
    return out


def U_only(values):
    p = [x * x for x in fwht(values)]
    c = caps(p)
    return sum(float(x) * math.log2(float(y / x)) for x, y in zip(p, c) if x)


def restrict(values, i, bit):
    n = len(values).bit_length() - 1
    out = []
    for z in range(1 << (n - 1)):
        lo = z & ((1 << i) - 1)
        hi = z >> i
        out.append(values[lo | (bit << i) | (hi << (i + 1))])
    return tuple(out)


def stats(values):
    p = [x * x for x in fwht(values)]
    n = len(values).bit_length() - 1
    U = U_only(values)
    I = sum(s.bit_count() * float(p[s]) for s in range(len(p)))
    G = sum(U - 0.5 * (U_only(restrict(values, i, 0)) +
                       U_only(restrict(values, i, 1))) for i in range(n))
    B = 0.0
    for i in range(n):
        bit = 1 << i
        for s in range(len(p)):
            if s & bit:
                continue
            a, b = float(p[s]), float(p[s | bit])
            mass = a + b
            if a:
                B += a * math.log2(mass / a)
            if b:
                B += b * math.log2(mass / b)
    return U, I, G, B, G - B


def L(values):
    U, I, _G, _B, M = stats(values)
    return M + (1.0 + ETA) * U - C * I


def balance(values):
    # New high bit y: restrictions are -q and q.
    return tuple(-v for v in values) + tuple(values)


def activate(values):
    # New low bit z: q on z=0 and +1 on z=1.
    out = []
    for v in values:
        out.extend((v, 1))
    return tuple(out)


def transform(values):
    return activate(balance(values))


def zlog(x):
    return 0.0 if x == 0.0 else x * math.log2(1.0 / x)


def R(t):
    x = (1.0 + t) ** 2 / 4.0
    y = (1.0 - t) ** 2 / 4.0
    e = zlog(x) + (0.0 if y == 0.0 else y * math.log2(2.0 / (1.0 - t)))
    u = 0.0 if t == 0.0 else t * t * math.log2(1.0 / (t * t))
    return e - u / 2.0 + (1.0 - t * t) / 4.0


def T(a, b):
    mass = a + b
    return ((0.0 if a == 0.0 else a * math.log2(mass / a)) +
            (0.0 if b == 0.0 else b * math.log2(mass / b)))


def d_scalar(h):
    return R(0.0) - 0.5 * (R(h) + R(-h)) - 0.5 * T(1.0, h * h)


def main():
    scalar_checks = 0
    max_scalar_slack = -1e100
    max_scalar_h = None
    for j in range(400001):
        h = j / 400000.0
        residual = d_scalar(h) - 0.5 * h * h
        assert residual <= 2e-12, (h, residual)
        if residual > max_scalar_slack:
            max_scalar_slack, max_scalar_h = residual, h
        scalar_checks += 1

    cores = []
    for n in range(4):
        for values in itertools.product((-1, 1), repeat=1 << n):
            cores.append(tuple(values))
    rng = random.Random(SEED)
    for _ in range(5000):
        cores.append(tuple(1 if rng.getrandbits(1) else -1 for _ in range(16)))

    identity_checks = 0
    inequality_checks = 0
    max_identity_error = 0.0
    max_transfer_residual = -1e100
    for q in cores:
        tq = transform(q)
        mean = sum(q) / len(q)
        observed = L(tq) - 0.5 * L(q)
        predicted = d_scalar(mean) + 1.0 + ETA - C
        error = abs(observed - predicted)
        max_identity_error = max(max_identity_error, error)
        assert error <= TOL, (len(q), mean, observed, predicted, error)
        assert observed <= TOL, (len(q), mean, observed)
        max_transfer_residual = max(max_transfer_residual, observed)
        identity_checks += 1
        inequality_checks += 1

    print("status=PASS")
    print(f"scalar_checks={scalar_checks}")
    print(f"boolean_cores_checked={len(cores)}")
    print(f"transfer_identity_checks={identity_checks}")
    print(f"transfer_inequality_checks={inequality_checks}")
    print(f"max_identity_error={max_identity_error:.3e}")
    print(f"max_transfer_residual={max_transfer_residual:.15f}")
    print(f"max_scalar_residual={max_scalar_slack:.3e}")
    print(f"max_scalar_residual_h={max_scalar_h:.8f}")
    print(f"seed={SEED}")


if __name__ == "__main__":
    main()
