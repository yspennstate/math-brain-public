#!/usr/bin/env python3
"""Exact verifier for the adjacent-mesh boundary identity used by B15.

Standard library only. All theorem checks use integer arithmetic and Fraction.
The deterministic n=5 sample is a stress test, not part of the proof.
"""
from fractions import Fraction
import random


def fwht(a):
    a = list(map(int, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def v2(z):
    z = abs(int(z))
    if not z:
        return 10**9
    c = 0
    while z % 2 == 0:
        z //= 2
        c += 1
    return c


def values(mask, n):
    return [1 if (mask >> i) & 1 else -1 for i in range(1 << n)]


def packets(vals):
    N = len(vals)
    n = N.bit_length() - 1
    W = fwht(vals)
    groups = {}
    for s, w in enumerate(W):
        if w:
            groups.setdefault(abs(w), []).append((s, 1 if w > 0 else -1))

    out = []
    influence = Fraction(0)
    for mag, arr in groups.items():
        eps = [0] * N
        for s, sign in arr:
            eps[s] = sign
        V = fwht(eps)
        r = min(v2(z) for z in V if z)
        t = v2(mag)
        q = mag >> t
        e = n - t
        d = e - r
        p = Fraction(len(arr) * mag * mag, N * N)
        for s, _ in arr:
            influence += Fraction(s.bit_count() * mag * mag, N * N)
        out.append((q, e, d, r, p, mag, len(arr)))
    return out, influence


def depth_sum(ps):
    return sum((p*d for q,e,d,r,p,mag,cnt in ps), Fraction(0))


def boundary(ps):
    """Half-weighted upward mesh variation for the 1/2,1/4 catalyst."""
    by_q = {}
    for q,e,d,r,p,mag,cnt in ps:
        by_q.setdefault(q, {})[e] = (d, r, p)
    ans = Fraction(0)
    for q, chain in by_q.items():
        for e, (d0, r0, p0) in chain.items():
            if e+1 not in chain:
                continue
            d1, r1, p1 = chain[e+1]
            if d1 > d0:
                ans += Fraction(1,2) * p0 * (d1-d0)
            elif d0 > d1:
                ans += Fraction(1,2) * p1 * (d0-d1)
    return ans


def tensor_values(a, b):
    return [x*y for y in b for x in a]


A_MASK = 0x17
A, IA = packets(values(A_MASK, 4))
A_profile = sorted((e, p, d) for q,e,d,r,p,mag,cnt in A)
assert A_profile == [(1, Fraction(1,2), 0), (2, Fraction(1,2), 0)]
assert IA == Fraction(5,4)

selected = [
    (5, 0x24495ba0),
    (5, 0x029a7245),
    (6, 0x7f405283f9c0d604),
]
selected_rows = []
for n, mask in selected:
    B, IB = packets(values(mask, n))
    bd = boundary(B)
    F, IF = packets(tensor_values(values(A_MASK, 4), values(mask, n)))
    direct_delta = depth_sum(F) - depth_sum(B)
    assert direct_delta == bd
    assert bd <= Fraction(21,10) * IB
    selected_rows.append((n, hex(mask), bd, IB, bd/IB if IB else 0))

count = 0
max_small = (Fraction(0), None)
for n in range(1, 5):
    for mask in range(1 << (1 << n)):
        B, IB = packets(values(mask, n))
        bd = boundary(B)
        assert bd <= Fraction(21,10) * IB
        if IB and bd/IB > max_small[0]:
            max_small = (bd/IB, (n, mask, bd, IB))
        count += 1

rng = random.Random(20260921)
max_sample = (Fraction(0), None)
for _ in range(10000):
    mask = rng.getrandbits(32)
    B, IB = packets(values(mask, 5))
    bd = boundary(B)
    assert bd <= Fraction(21,10) * IB
    if IB and bd/IB > max_sample[0]:
        max_sample = (bd/IB, (mask, bd, IB))

print("PASS")
print("A profile:", A_profile, "I(A)=", IA)
print("exhaustive functions n<=4:", count, "max boundary/I:", max_small[0])
for row in selected_rows:
    print("selected:", row)
print("deterministic n=5 sample: 10000")
print("sample max boundary/I:", max_sample[0],
      "mask=", hex(max_sample[1][0]),
      "boundary=", max_sample[1][1],
      "I=", max_sample[1][2])
