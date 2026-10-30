#!/usr/bin/env python3
from fractions import Fraction
from math import comb

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

def pow2frac(m):
    return Fraction(1 << m, 1) if m >= 0 else Fraction(1, 1 << (-m))

def log2_bounds(x, terms=96):
    assert isinstance(x, Fraction) and x > 0
    m = x.numerator.bit_length() - x.denominator.bit_length()
    while pow2frac(m) > x:
        m -= 1
    while pow2frac(m+1) <= x:
        m += 1
    r = x / pow2frac(m)
    assert Fraction(1) <= r < Fraction(2)

    y = (r - 1)/(r + 1)
    s = Fraction(0)
    yp = y
    for j in range(terms):
        s += yp / (2*j+1)
        yp *= y*y
    ln_lo = 2*s
    ln_hi = ln_lo if y == 0 else ln_lo + 2*yp / ((2*terms+1)*(1-y*y))

    z = Fraction(1,3)
    s2 = Fraction(0)
    zp = z
    for j in range(terms):
        s2 += zp / (2*j+1)
        zp *= z*z
    l2_lo = 2*s2
    l2_hi = l2_lo + 2*zp / ((2*terms+1)*(1-z*z))

    return Fraction(m) + ln_lo/l2_hi, Fraction(m) + ln_hi/l2_lo

def seed(n):
    a = Fraction(1, 2**(n-1))
    vals = [1]*(1 << n)
    vals[0] = -1
    W = fwht(vals)
    assert W[0] == (1 << n) - 2
    assert all(w == -2 for w in W[1:])
    p = [Fraction(0)]*(n+1)
    p[0] = (1-a)**2
    for t in range(1,n+1):
        p[t] = comb(n,t)*a*a
    assert sum(p) == 1
    assert sum(Fraction(t)*p[t] for t in range(n+1)) == n*a
    return a,p

def conv(p,q):
    r = [Fraction(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        if x:
            for j,y in enumerate(q):
                if y:
                    r[i+j] += x*y
    return r

def collision_ratio_bounds(n,k):
    a,p = seed(n)
    dist = [Fraction(1)]
    for _ in range(k):
        dist = conv(dist,p)
    N = n*k
    beta = N*a
    lo = Fraction(0)
    hi = Fraction(0)
    for t,pr in enumerate(dist):
        if not pr:
            continue
        c = Fraction(comb(N,t))
        l1,u1 = log2_bounds(c)
        extra = Fraction(1) + a*Fraction(N-t,t+1)
        l2,u2 = log2_bounds(extra)
        lo += pr*(l1+l2)
        hi += pr*(u1+u2)
    return lo/beta, hi/beta

lo,hi = collision_ratio_bounds(4,32)
assert lo > 4
print("PASS")
print("seed n=4 exact Walsh pattern verified")
print("finite witness dimension", 1+4*32)
print("C_coll/(I-1) lower", format(float(lo), ".15f"))
print("C_coll/(I-1) upper", format(float(hi), ".15f"))
print("certified_gt_4", lo > 4)

import math
for n in [4,5,6,8,10,12]:
    a = 2.0**(1-n)
    h = -a*math.log2(a) -(1-a)*math.log2(1-a)
    print("limit", n, format(h/a, ".15f"))
