#!/usr/bin/env python3
"""Exact/self-contained checks for B12 addressing obstruction and terminal shadow."""
from fractions import Fraction
from math import comb, log2

def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def addressing_values(k):
    m = 1 << k
    n = k + m
    vals = []
    for mask in range(1 << n):
        j = 0
        for r in range(k):
            if (mask >> r) & 1:
                j |= 1 << r
        vals.append(1 if ((mask >> (k+j)) & 1) else -1)
    return vals

def shadow_sum(k, a):
    return sum(
        Fraction(comb(k-a, b-a), comb(b+1, a+1))
        for b in range(a, k+1)
    )

def shadow_closed(k, a):
    return Fraction(
        sum(comb(k+1, c) for c in range(a+1, k+2)),
        comb(k+1, a+1),
    )

print("exact Walsh checks")
for k in range(1, 4):
    vals = addressing_values(k)
    W = fwht(vals)
    N = len(vals)
    m = 1 << k
    nz = [abs(w) for w in W if w]
    assert len(nz) == m*m
    assert set(nz) == {N//m}
    assert sum(Fraction(w*w, N*N) for w in W) == 1
    print(f"k={k}: nonzero={len(nz)} coefficient_abs=1/{m} mass=1")

print("exact terminal-shadow combinatorics")
for k in range(1, 8):
    for a in range(k+1):
        assert shadow_sum(k, a) == shadow_closed(k, a)
    print(f"k={k}: all a=0..{k} PASS")

print("calibration table")
for k in [1,2,3,4,8,16,32,64,128]:
    I = 1 + k/2
    H = 2*k
    B = 0.0
    for a in range(k+1):
        level_prob = comb(k,a)/(2**k)
        B += level_prob * log2(float(shadow_closed(k,a)))
    R = H-B
    assert abs((R+B)-H) < 1e-9
    print(
        f"k={k:3d} H/I={H/I:.9f} "
        f"R/I={R/I:.9f} Bsh/I={B/I:.9f} Bsh={B:.6f}"
    )
print("PASS")
