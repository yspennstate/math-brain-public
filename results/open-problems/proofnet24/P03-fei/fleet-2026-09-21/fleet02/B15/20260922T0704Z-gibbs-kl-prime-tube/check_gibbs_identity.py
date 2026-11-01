#!/usr/bin/env python3
"""Finite floating sanity check for the exact Gibbs-KL identities in REPORT.md.

This is not evidence for the universal gate inequality.  It reconstructs the
p-biased Fourier law directly from truth tables for 90 small-gate/bias cases and
checks only the algebraic identities (2.1) and (2.2).
"""
import math


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def fourier(tt, p):
    n = len(p)
    N = 1 << n
    out = {}
    for S in range(N):
        c = 0.0
        for x in range(N):
            prob = 1.0
            phi = 1.0
            for i, pi in enumerate(p):
                bit = (x >> i) & 1
                y = -1.0 if bit else 1.0
                prob *= pi if bit else (1.0 - pi)
                if (S >> i) & 1:
                    phi *= (y - (1.0 - 2.0 * pi)) / math.sqrt(4.0 * pi * (1.0 - pi))
            c += prob * tt[x] * phi
        out[S] = c
    return out


def output_mass(tt, p):
    n = len(p)
    q = 0.0
    for x, val in enumerate(tt):
        prob = 1.0
        for i, pi in enumerate(p):
            prob *= pi if ((x >> i) & 1) else (1.0 - pi)
        if val == -1:
            q += prob
    return q


lam = 0.7
gamma = lambda z: lam * z * (1.0 - z)
max_full = 0.0
max_cond = 0.0
checks = 0

for n in range(1, 4):
    N = 1 << n
    biases = [
        [0.23 + 0.07 * i for i in range(n)],
        [0.41 - 0.03 * i for i in range(n)],
    ]
    masks = list(range(1, (1 << N) - 1)) if n < 3 else list(range(1, 255, 7))
    for mask in masks:
        tt = [-1 if ((mask >> x) & 1) else 1 for x in range(N)]
        for p in biases:
            coeff = fourier(tt, p)
            w = {S: c * c for S, c in coeff.items()}
            q = output_mass(tt, p)
            v = 4.0 * q * (1.0 - q)
            if v < 1e-14:
                continue

            a = []
            xprice = []
            for pi in p:
                Vi = 4.0 * pi * (1.0 - pi)
                ai = (gamma(pi) + h2(Vi)) / Vi
                a.append(ai)
                xprice.append(2.0 ** (-ai))

            It = [sum(w[S] for S in w if (S >> i) & 1) for i in range(n)]
            H = -sum(z * math.log2(z) for z in w.values() if z > 0.0)
            D = sum(ai * ji for ai, ji in zip(a, It)) - gamma(q) - H

            Z = math.prod(1.0 + x for x in xprice)
            nu = {}
            for S in w:
                numer = math.prod(xprice[i] for i in range(n) if (S >> i) & 1)
                nu[S] = numer / Z
            KL = sum(w[S] * math.log2(w[S] / nu[S]) for S in w if w[S] > 0.0)
            rhs_full = KL - math.log2(Z) - gamma(q)
            max_full = max(max_full, abs(D - rhs_full))

            wp = {S: w[S] / v for S in w if S and w[S] > 0.0}
            nup = {}
            for S in w:
                if S:
                    numer = math.prod(xprice[i] for i in range(n) if (S >> i) & 1)
                    nup[S] = numer / (Z - 1.0)
            KLp = sum(wp[S] * math.log2(wp[S] / nup[S]) for S in wp)
            xq = 2.0 ** (-(gamma(q) + h2(v)) / v)
            rhs_cond = v * (KLp - math.log2((Z - 1.0) / xq))
            max_cond = max(max_cond, abs(D - rhs_cond))
            checks += 1

assert max_full < 1e-12
assert max_cond < 1e-12
print("PASS")
print("checks", checks)
print("max_full_identity_residual", repr(max_full))
print("max_conditional_identity_residual", repr(max_cond))
