#!/usr/bin/env python3
"""Regression checks for signed-opening activation history transfer."""
from fractions import Fraction
from math import log, log2
from random import Random


def xr(x, y):
    return 0.0 if x == 0 else float(x) * log2(float(y / x))


def T(a, b):
    return xr(a, a + b) + xr(b, a + b)


def q(t):
    return 0.0 if t == 0 else float(t) * log2(1 / float(t)) + 2 * float(t) / log(2)


def fwht(v):
    a = [Fraction(x) for x in v]
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2 * h):
            for k in range(j, j + h):
                x, y = a[k], a[k + h]
                a[k], a[k + h] = x + y, x - y
        h *= 2
    return [x / len(a) for x in a]


def caps(p):
    a = list(p)
    n = len(a).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for s in range(len(a)):
            if not s & bit:
                a[s] += a[s | bit]
    return a


def restrict(v, i, bit):
    n = len(v).bit_length() - 1
    out = []
    for z in range(1 << (n - 1)):
        lo = z & ((1 << i) - 1)
        hi = z >> i
        out.append(v[lo | (bit << i) | (hi << (i + 1))])
    return tuple(out)


def basic(v):
    h = fwht(v)
    p = [x * x for x in h]
    pi = caps(p)
    U = sum(xr(x, y) for x, y in zip(p, pi))
    I = sum(s.bit_count() * float(x) for s, x in enumerate(p))
    B = 0.0
    n = len(v).bit_length() - 1
    inf = []
    for i in range(n):
        bit = 1 << i
        inf.append(sum(float(p[s]) for s in range(len(p)) if s & bit))
        for s in range(len(p)):
            if not s & bit:
                B += T(p[s], p[s | bit])
    return U, I, B, h, p, inf


def stats(v):
    U, I, B, h, p, inf = basic(v)
    n = len(v).bit_length() - 1
    G = n * U
    for i in range(n):
        G -= 0.5 * basic(restrict(v, i, 0))[0]
        G -= 0.5 * basic(restrict(v, i, 1))[0]
    return U, I, B, G - B, h, p, inf


def phi(v):
    _, _, _, _, p, _ = basic(v)
    n = len(v).bit_length() - 1
    return sum(q(p[1 << i]) for i in range(n))


def theta_from(data, Xmask):
    _, _, _, _, p, inf = data
    n = len(p).bit_length() - 1
    ans = sum(q(inf[i]) for i in range(n) if Xmask & (1 << i))
    for i in range(n):
        if Xmask & (1 << i):
            continue
        e = Fraction(0)
        sub = Xmask
        while True:
            e += p[(1 << i) | sub]
            if sub == 0:
                break
            sub = (sub - 1) & Xmask
        ans += q(e)
    return ans


def activate(v):
    # Last/new coordinate is selector z: z=0 gives core, z=1 gives +1.
    return tuple(v) + tuple(1 for _ in v)


def L(v, c, eta):
    U, I, _, M, _, _, _ = stats(v)
    return M + (1 + eta) * U - c * I


c = 29 / 2 + 4 / log(2)
rng = Random(20261014112551)
vectors = []
for n in range(0, 4):
    size = 1 << n
    for mask in range(1 << size):
        vectors.append(tuple(1 if mask & (1 << j) else -1 for j in range(size)))
for n in range(4, 8):
    size = 1 << n
    for _ in range(20):
        vectors.append(tuple(1 if rng.getrandbits(1) else -1 for _ in range(size)))

checks = 0
max_identity_error = 0.0
max_node_drift = -1e100
min_theta_gap = 1e100
for v in vectors:
    n = len(v).bit_length() - 1
    F = activate(v)
    zbit = 1 << n
    bv = basic(v)
    bF = basic(F)
    phif = sum(q(bv[4][1 << i]) for i in range(n))
    phiF = sum(q(bF[4][1 << i]) for i in range(n + 1))
    Lv = {eta: L(v, c, eta) for eta in (0.25, 1.0)}
    LF = {eta: L(F, c, eta) for eta in (0.25, 1.0)}
    Xs = list(range(1 << n)) if n <= 3 else [0, (1 << n) - 1] + [rng.randrange(1 << n) for _ in range(14)]
    for X in Xs:
        thf = theta_from(bv, X)
        thF = theta_from(bF, X | zbit)
        m = float(bv[3][0])
        J = (1 - m) / 2
        DX = sum(bv[5][i] for i in range(n) if X & (1 << i))
        p = bv[4]
        for i in range(n):
            if X & (1 << i):
                continue
            sub = X
            while True:
                DX += float(p[(1 << i) | sub])
                if sub == 0:
                    break
                sub = (sub - 1) & X
        identity_rhs = q(J) + 0.5 * thf + 0.5 * DX
        max_identity_error = max(max_identity_error, abs(thF - identity_rhs))
        min_theta_gap = min(min_theta_gap, thf - phif)
        assert abs(thF - identity_rhs) < 2e-10, (n, X, thF, identity_rhs, J, DX, thf)
        assert thf + 2e-12 >= phif
        # At the selector node, inherited block is empty and active block is X+z.
        # R-O = Phi(F) - Theta_X(f)/2 exactly.
        signed = phiF - 0.5 * thf
        for eta in (0.25, 1.0):
            node = LF[eta] - 0.5 * Lv[eta] + 2 * signed
            max_node_drift = max(max_node_drift, node)
            assert node <= 2e-10
            checks += 1

print("status=PASS")
print("c=", c)
print("boolean_cores=", len(vectors))
print("signed_node_checks=", checks)
print("max_orbit_activation_identity_error=", max_identity_error)
print("min_Theta_minus_Phi=", min_theta_gap)
print("max_signed_node_drift=", max_node_drift)
print("seed=20261014112551")
