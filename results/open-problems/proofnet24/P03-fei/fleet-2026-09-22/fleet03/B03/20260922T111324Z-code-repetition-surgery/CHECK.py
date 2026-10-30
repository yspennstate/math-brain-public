#!/usr/bin/env python3
from fractions import Fraction
import math

CANDIDATE_CENTER = 6.558445288811087

def parity(x):
    return x.bit_count() & 1

def chi(mask, x):
    return -1 if parity(mask & x) else 1

def gate(n, x):
    # F_n = chi_{e1} times a sign flip on repetition code C_n={0,1^n}.
    base = chi(1, x)
    if x == 0 or x == (1 << n) - 1:
        return -base
    return base

def walsh(n):
    N = 1 << n
    out = []
    for s in range(N):
        num = sum(gate(n, x) * chi(s, x) for x in range(N))
        out.append(Fraction(num, N))
    return out

def expected_coeff(n, s):
    q = Fraction(1, 1 << (n - 2))
    if parity(s) == 0:
        return Fraction(0)
    if s == 1:
        return 1 - q
    return -q

def xor_convolution(a, w):
    return sum(a[s] * a[s ^ w] for s in range(len(a)))

def formulas(n):
    q = 2.0 ** (2-n)
    J = (n-2)*q
    H = -(1-q)**2 * math.log2((1-q)**2) + q*(2-q)*(2*n-4)
    return q, J, H

def positive_root_c(n):
    q = 2.0 ** (2-n)
    def f(c):
        return 1-c - (1-c*(1-q))*(1-c*q)**(n-1)
    lo, hi = 0.5, 1.0 - 1e-15
    flo, fhi = f(lo), f(hi)
    if flo == 0:
        return lo
    if flo*fhi > 0:
        lastx, lastf = 1e-8, f(1e-8)
        found = False
        for j in range(1,10000):
            x = j/10000
            fx = f(x)
            if lastf*fx < 0 and x > 1e-4:
                lo, hi = lastx, x
                found = True
            lastx, lastf = x, fx
        if not found:
            raise AssertionError("positive root not bracketed")
    for _ in range(120):
        mid=(lo+hi)/2
        fm=f(mid)
        if f(lo)*fm <= 0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2

def h2(x):
    if x <= 0 or x >= 1:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

print("Exact Walsh/convolution regression")
for n in range(3,9):
    a = walsh(n)
    assert all(v == expected_coeff(n,s) for s,v in enumerate(a))
    assert sum(v*v for v in a) == 1
    assert a[0] == 0
    for w in range(1<<n):
        target = Fraction(1 if w == 0 else 0)
        assert xor_convolution(a,w) == target
    q = Fraction(1, 1 << (n-2))
    r=[]
    for i in range(n):
        ri=sum(a[s]*a[s] for s in range(1<<n) if (s>>i)&1)
        r.append(ri)
    assert r[0] == 1-q
    assert all(x == q for x in r[1:])
    I=sum(r)
    assert I == 1+(n-2)*q
    print(f"n={n}: q={q}, I-1={(n-2)*q}, exact_signed_convolution=PASS")

print("\nEntropy / I-projection / candidate-defect comparison")
for n in [3,4,5,6,8,10,20,30]:
    q,J,H = formulas(n)
    c=positive_root_c(n)
    Hmax=(h2(c*(1-q))+(n-1)*h2(c*q)-h2(c))/c
    K=Hmax-H
    D=CANDIDATE_CENTER*J-H
    print(
        f"n={n:2d} q={q:.12g} H/J={H/J:.12f} "
        f"Kocc/J={K/J:.12f} Dcandidate/J={D/J:.12f} c={c:.12f}"
    )
    assert H/J < 5.0 + 1e-12
    assert D > 0
    assert K >= -1e-12

print("\nPASS")
