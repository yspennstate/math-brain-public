#!/usr/bin/env python3
"""Deterministic checks for B01/A004 convention and bridge-constant ledger."""
from fractions import Fraction
from math import log, log2, sqrt


def walsh(values):
    n = (len(values)).bit_length() - 1
    N = 1 << n
    return [
        Fraction(sum(values[x] * (-1 if ((x & s).bit_count() & 1) else 1)
                     for x in range(N)), N)
        for s in range(N)
    ]


def entropy(masses):
    return sum(float(p) * log2(1.0 / float(p)) for p in masses if p)


def influence(masses):
    return sum(s.bit_count() * float(p) for s, p in enumerate(masses))


def phi(t):
    ans = 0.0
    for z in (1.0 + t, 1.0 - t):
        if z:
            ans += 0.5 * z * log2(z)
    return ans


def u(r):
    return r * log2(1.0 + 1.0 / r)


def v(r):
    return (r + 1.0) * phi(2.0 * sqrt(r) / (r + 1.0))


def bent_value(x, m):
    exponent = sum(((x >> (2*j)) & 1) * ((x >> (2*j+1)) & 1)
                   for j in range(m // 2)) & 1
    return -1 if exponent else 1


checks = 0

# Exhaustive n=3 convention audit: sign/indicator scaling, character translation,
# entropy preservation, and the exact transformed-influence formula.
n = 3
N = 1 << n
for mask in range(1 << N):
    f = [1 if ((mask >> x) & 1) else -1 for x in range(N)]
    fh = walsh(f)
    p = [z*z for z in fh]
    g = [Fraction(1-fx, 2) for fx in f]
    gh = walsh(g)
    for s in range(1, N):
        assert gh[s] == -fh[s] / 2
        checks += 1
    H = entropy(p)
    I = influence(p)
    alpha = [sum(p[s] for s in range(N) if (s >> i) & 1) for i in range(n)]
    for U in range(N):
        translated = [p[s ^ U] for s in range(N)]
        assert abs(entropy(translated)-H) < 2e-14
        expected = I + U.bit_count() - 2*sum(float(alpha[i]) for i in range(n) if (U >> i) & 1)
        assert abs(influence(translated)-expected) < 2e-14
        checks += 2

# Exact bent-one-point-surgery spectrum and sign-count audit, m <= 8.
for m in (2, 4, 6, 8):
    M = 1 << m
    uvals = [bent_value(x, m) for x in range(M)]
    vvals = uvals[:]
    vvals[0] *= -1
    uh = walsh(uvals)
    vh = walsh(vvals)
    a = [(uh[s] + vh[s]) / 2 for s in range(M)]
    b = [(uh[s] - vh[s]) / 2 for s in range(M)]
    Q = 1 << (m // 2)
    assert all(abs(z) == Fraction(1, Q) for z in uh)
    assert all(abs(z) == Fraction(1, M) for z in b)
    ratios = [(a[s]*a[s]) / (b[s]*b[s]) for s in range(M)]
    assert ratios.count(Fraction((Q-1)**2, 1)) == (M+Q)//2
    assert ratios.count(Fraction((Q+1)**2, 1)) == (M-Q)//2
    assert sum(a[s]*b[s] for s in range(M)) == 0
    checks += 5

print("PASS")
print(f"exact_and_numeric_checks={checks}")
print("random_seed=None")
print(f"one_over_ln2={1/log(2):.15f}")
print(f"two_over_ln2={2/log(2):.15f}")
print(f"three_over_ln2={3/log(2):.15f}")
print(f"K_ref_bits={3+2*log2(3)+log2(6*2.718281828459045):.15f}")
print("m  E_minus_L/alpha  JS/alpha  combined/alpha")
for m in (2, 4, 6, 8, 10, 20, 40):
    Q = 2.0**(m/2)
    rp, rm = (Q-1)**2, (Q+1)**2
    wp, wm = (1+1/Q)/2, (1-1/Q)/2
    ur = wp*u(rp) + wm*u(rm)
    vr = wp*v(rp) + wm*v(rm)
    print(f"{m:2d} {ur:.12f} {vr:.12f} {ur+vr:.12f}")

