#!/usr/bin/env python3
"""Deterministic checks for the suspension/no-loss KL obstruction.

Uses only the standard library.  Exact integer FWHT checks are finite sanity checks;
the theorem in REPORT.md is analytic.
"""
import math
from fractions import Fraction

LN2 = math.log(2.0)
C_STAR = 6.538805311222222
THETA = 0.99

def h2_stable(x: float) -> float:
    if x == 0.0 or x == 1.0:
        return 0.0
    return (-x * math.log(x) - (1.0 - x) * math.log1p(-x)) / LN2

def fwht(a):
    a = list(a)
    h = 1
    n = len(a)
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def defect_values(m):
    n = 1 << m
    vals = [1] * n
    vals[0] = -1
    return vals

def exact_checks(m):
    n = 1 << m
    W = fwht(defect_values(m))
    assert W[0] == n - 2
    assert all(abs(W[s]) == 2 for s in range(1, n))
    # Each coordinate edge crosses the unique defect at exactly two oriented points.
    vals = defect_values(m)
    for i in range(m):
        flips = sum(vals[x] != vals[x ^ (1 << i)] for x in range(n))
        assert flips == 2
    alpha = Fraction(1, n)
    p0 = (1 - 2*alpha) ** 2
    ptail = 4 * alpha * alpha
    assert p0 + (n-1)*ptail == 1
    return p0, ptail

def stable_quantities(m, C=C_STAR, theta=THETA):
    alpha = math.ldexp(1.0, -m)
    I = 2.0 * m * alpha
    tail_mass = 4.0 * alpha * (1.0-alpha)
    # p0 = 1-tail_mass.  This form remains stable when p0 rounds to one.
    H0 = -(1.0-tail_mass) * math.log1p(-tail_mass) / LN2
    Htail = tail_mass * (2.0*m - 2.0)
    H = H0 + Htail
    Hmax = m * h2_stable(2.0*alpha)
    K = Hmax - H
    B = C*I - Hmax
    residual = C*I - H
    partial = B + theta*K
    return I, H, Hmax, K, B, residual, partial

def level_kl(m):
    alpha = math.ldexp(1.0, -m)
    q = 2.0*alpha
    p0 = (1.0-2.0*alpha)**2
    terms = [(p0, (1.0-q)**m)]
    for k in range(1, m+1):
        pk = math.comb(m,k)*4.0*alpha*alpha
        qk = math.comb(m,k)*(q**k)*((1.0-q)**(m-k))
        terms.append((pk,qk))
    return sum(pk*math.log2(pk/qk) for pk,qk in terms if pk > 0.0)

for m in range(2, 9):
    exact_checks(m)

print("exact_fwht_and_influence_checks=PASS m=2..8")
for m in (4, 8, 12, 20, 32):
    I,H,Hmax,K,B,R,P = stable_quantities(m)
    if m <= 20:
        KLlev = level_kl(m)
        assert abs(KLlev-K) < 5e-13
    print(
        f"m={m} H/I={H/I:.15f} Hmax/I={Hmax/I:.15f} "
        f"Kocc/I={K/I:.15f} residual/I={R/I:.15f} "
        f"theta99_proxy/I={P/I:.15f}"
    )

first = None
for m in range(2, 1000):
    *_, partial = stable_quantities(m)
    if partial < 0.0:
        first = m
        break
assert first == 258, first
I,H,Hmax,K,B,R,P = stable_quantities(first)
print(f"theta={THETA} Cstar={C_STAR} first_negative_m={first} proxy_over_I={P/I:.15f}")
print("level_KL_identity_checks=PASS m=4,8,12,20")
print("PASS")
