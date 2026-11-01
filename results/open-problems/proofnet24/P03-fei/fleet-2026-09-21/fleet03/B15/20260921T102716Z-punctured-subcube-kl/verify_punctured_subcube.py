#!/usr/bin/env python3
"""Exact/elementary checks for the punctured-subcube B15 family.

No claim about unrestricted FEI is made.  The direct Walsh check is deliberately
small; the closed formulas are all-dimensional.
"""
from __future__ import annotations

from fractions import Fraction
from math import log2


def fwht(a: list[int]) -> list[int]:
    a = a[:]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def v2(x: int) -> int:
    x = abs(x)
    assert x
    return (x & -x).bit_length() - 1


def closed(n: int, c: int) -> dict[str, object]:
    assert 2 <= c < n
    d = n - c
    M = 2**d - 1
    m = Fraction(1, 1) - Fraction(2 * M, 2**n)
    a_h = Fraction(2 * M, 2**n)
    a_l = Fraction(2, 2**n)
    L_h = 2**c - 1
    L_l = 2**n - 2**c
    N_h = Fraction(L_h, 1)
    N_l = Fraction(L_l, 4**c)
    N_perp = N_h + N_l
    p_h = L_h * a_h * a_h
    p_l = L_l * a_l * a_l
    v = 1 - m * m
    I = c * a_h + d * a_l
    D = (
        float(m * m) * log2(1 / float(m))
        + float(p_h) * log2(1 / float(a_h))
        + float(p_l) * (n - c - 1)
    )
    residual_ratio = float(v) * log2(float(N_perp)) / float(I)
    alpha = float(p_h / v)
    beta = float(N_h / N_perp)
    kl = alpha * log2(alpha / beta) + (1 - alpha) * log2((1 - alpha) / (1 - beta))
    return {
        "M": M,
        "m": m,
        "a_h": a_h,
        "a_l": a_l,
        "L_h": L_h,
        "L_l": L_l,
        "r_h": 0,
        "r_l": c,
        "N_h": N_h,
        "N_l": N_l,
        "N_perp": N_perp,
        "p_h": p_h,
        "p_l": p_l,
        "v": v,
        "I": I,
        "D": D,
        "residual_ratio": residual_ratio,
        "residual_KL": kl,
    }


def direct(n: int, c: int) -> None:
    d = n - c
    N = 2**n
    # B is the coordinate subcube whose c high bits vanish; A=B\{0}.
    A = set(range(1, 2**d))
    indicator = [int(x in A) for x in range(N)]
    K = fwht(indicator)
    M = 2**d - 1
    # Characters trivial on B have zero low d frequency bits.
    H = {s for s in range(N) if (s & (2**d - 1)) == 0}
    assert len(H) == 2**c
    assert all(K[s] == M for s in H)
    assert all(K[s] == -1 for s in range(N) if s not in H)

    high_mask = [0] * N
    low_mask = [0] * N
    for s in range(1, N):
        if s in H:
            high_mask[s] = -1
        else:
            low_mask[s] = +1
    Vh, Vl = fwht(high_mask), fwht(low_mask)
    rh = min(v2(x) for x in Vh if x)
    rl = min(v2(x) for x in Vl if x)
    f = closed(n, c)
    assert rh == f["r_h"] == 0
    assert rl == f["r_l"] == c
    assert Fraction(sum(x * x for x in Vh), N * 4**rh) == f["N_h"]
    assert Fraction(sum(x * x for x in Vl), N * 4**rl) == f["N_l"]

    vals = [-1 if x in A else +1 for x in range(N)]
    W = fwht(vals)
    influence = Fraction(0, 1)
    for s, w in enumerate(W):
        influence += Fraction(s.bit_count() * w * w, N * N)
    assert influence == f["I"]


if __name__ == "__main__":
    for c in (2, 3, 4):
        for n in range(c + 1, min(11, c + 7)):
            direct(n, c)
    print("direct small Walsh checks: PASS")
    for c in (3, 4):
        for n in (8, 12, 16, 20):
            if n <= c:
                continue
            z = closed(n, c)
            print(
                f"c={c} n={n} m={float(z['m']):.7f} I={float(z['I']):.7f} "
                f"Nperp={float(z['N_perp']):.6f} "
                f"vlogN/I={z['residual_ratio']:.6f} D/I={z['D']/float(z['I']):.6f} "
                f"KL={z['residual_KL']:.6f}"
            )
