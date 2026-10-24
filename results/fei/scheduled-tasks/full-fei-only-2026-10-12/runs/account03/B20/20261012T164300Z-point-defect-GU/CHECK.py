#!/usr/bin/env python3
"""Independent direct Walsh/restriction check of point-defect GU formula.
No protected evaluation material; pure synthetic Boolean families.
"""
from math import log2, log
from itertools import product

def fwht(a):
    v = a.copy()
    N = len(v)
    step = 1
    while step < N:
        for i in range(0, N, 2 * step):
            for j in range(step):
                x, y = v[i + j], v[i + j + step]
                v[i + j], v[i + j + step] = x + y, x - y
        step *= 2
    return v

def upper_mass(p, n):
    pi = p.copy()
    for i in range(n):
        for mask in range(1 << n):
            if not (mask & (1 << i)):
                pi[mask] += pi[mask | (1 << i)]
    return pi

def statistics(v):
    N = len(v)
    assert N and N & (N - 1) == 0
    n = N.bit_length() - 1
    w = fwht(v)
    p = [(x / N) ** 2 for x in w]
    pi = upper_mass(p, n)
    U = sum(a * log2(b / a) for a, b in zip(p, pi) if a)
    I = sum(a * mask.bit_count() for mask, a in enumerate(p))
    return U, I, p, pi

def restriction(v, i, b):
    n = len(v).bit_length() - 1
    out = []
    for y in range(1 << (n - 1)):
        low = y & ((1 << i) - 1)
        high = y >> i
        x = low | (b << i) | (high << (i + 1))
        out.append(v[x])
    return out

def direct(v):
    n = len(v).bit_length() - 1
    U, I, *_ = statistics(v)
    G = sum(U - (statistics(restriction(v, i, 0))[0] +
                   statistics(restriction(v, i, 1))[0]) / 2 for i in range(n))
    return U, I, G

def A(t):
    return -2 * (1 - t) ** 2 * log2(1 - t) if t < 1 else 0.0

def exact_analytic(n):
    t = 2 ** (1 - n)
    U = A(t) + n * t * (1 - t)
    I = n * t
    G = n * (U - (A(2 * t) + (n - 1) * 2 * t * (1 - 2 * t)) / 2) if n >= 2 else 0.0
    return U, I, G

def defect(n):
    v = [1] * (1 << n)
    v[0] = -1
    return v

def tensor(f, g):
    return [f[x] * g[y] for y in range(len(g)) for x in range(len(f))]

def main():
    tol = 5e-11
    assertions = 0
    failures = 0
    print('RATIO  n  DIRECT_G/I    FORMULA_G/I    U/I    CURVATURE_UB')
    for n in range(1, 11):
        vals = defect(n)
        U, I, G = direct(vals)
        u2, i2, g2 = exact_analytic(n)
        for a, b in [(U, u2), (I, i2), (G, g2)]:
            assertions += 1
            failures += abs(a - b) > tol
        if n >= 4:
            ub = 1 + (n - 2 + 3 / log(2)) * 2 ** (1 - n)
            assertions += 1
            failures += (G / I > ub + tol)
        else:
            ub = None
        print(f'{n:2d}  {G/I:.12f}  {g2/i2:.12f}  {U/I:.12f}  {ub if ub is not None else "NA"}')

    for m, n in product(range(1, 5), repeat=2):
        U1, I1, G1 = direct(defect(m))
        U2, I2, G2 = direct(defect(n))
        U, I, G = direct(tensor(defect(m), defect(n)))
        for a, b in [(U, U1 + U2), (I, I1 + I2), (G, G1 + G2)]:
            assertions += 1
            failures += abs(a - b) > tol
    print(f'CHECKS: {assertions} assertions, {failures} failures; 10 complete point defects (n=1..10); 16 disjoint tensor controls')
    print('THEOREM_SHARP_CONSTANT:', .25 + 2.25 * log2(16/9))
    assert failures == 0

if __name__ == '__main__':
    main()
