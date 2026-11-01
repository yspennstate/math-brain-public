#!/usr/bin/env python3
"""Finite regression checks for the B05 sliding-history theorem."""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import log, log2


def fwht(v):
    a = [Fraction(x) for x in v]
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2*h):
            for k in range(j, j+h):
                x, y = a[k], a[k+h]
                a[k], a[k+h] = x+y, x-y
        h *= 2
    return tuple(x/len(a) for x in a)


def caps(p):
    a = list(p); n = len(a).bit_length()-1
    for i in range(n):
        for s in range(len(a)):
            if not s >> i & 1:
                a[s] += a[s | 1 << i]
    return tuple(a)


def restrict(v, i, b):
    n = len(v).bit_length()-1; out = []
    for z in range(1 << (n-1)):
        lo = z & ((1 << i)-1); hi = z >> i
        out.append(v[lo | (b << i) | (hi << (i+1))])
    return tuple(out)


def xr(x, y): return 0.0 if x == 0 else float(x)*log2(float(y/x))
def pair(a, b): return xr(a, a+b)+xr(b, a+b)
def q(t): return 0.0 if t == 0 else float(t)*log2(1/float(t))+2*float(t)/log(2)


@lru_cache(None)
def stats(v):
    h = fwht(v); p = tuple(x*x for x in h); pi = caps(p)
    n = len(v).bit_length()-1
    U = sum(xr(x, y) for x, y in zip(p, pi))
    I = sum(s.bit_count()*float(x) for s, x in enumerate(p))
    B = 0.0; inf = []
    for i in range(n):
        inf.append(sum((p[s] for s in range(len(p)) if s >> i & 1), Fraction(0)))
        B += sum(pair(p[s], p[s | 1 << i]) for s in range(len(p)) if not s >> i & 1)
    G = n*U
    for i in range(n):
        G -= .5*(stats(restrict(v, i, 0))[0]+stats(restrict(v, i, 1))[0])
    return U, I, B, G-B, p, tuple(inf)


def theta(v, X):
    p = stats(v)[4]; inf = stats(v)[5]; n = len(v).bit_length()-1
    ans = 0.0
    for i in range(n):
        if X >> i & 1:
            ans += q(inf[i])
        else:
            e = Fraction(0); sub = X
            while True:
                e += p[(1 << i) | sub]
                if sub == 0: break
                sub = (sub-1) & X
            ans += q(e)
    return ans


def L(v, c):
    U, I, B, M, _, _ = stats(v)
    return M+2*U-c*I


def remap(mask, d): return (mask & ((1 << d)-1)) | ((mask >> (d+1)) << d)


def drift(v, Y, x, Z, c):
    a, b = restrict(v, x, 0), restrict(v, x, 1); z = remap(Z, x)
    return L(v, c)-.5*(L(a, c)+L(b, c))+2*theta(v, Y)-theta(a, z)-theta(b, z)


def point_U(r):
    t = 2.0**(1-r)
    return (0.0 if t == 1 else -2*(1-t)**2*log2(1-t))+r*t*(1-t)


def point_B(r):
    t = 2.0**(1-r)
    return r*(pair((1-t)**2, t*t)+2*t*(1-t))


def point_D(r): return point_U(r)-(.5*point_U(r-1) if r > 1 else 0.0)
def point_M(r): return r*point_D(r)-point_B(r)
def point_theta(r, k):
    t = 2.0**(1-r)
    return k*q(t)+(r-k)*q((2**k)*t*t)


def threshold(r, kp, kc):
    t = 2.0**(1-r)
    child_m = point_M(r-1) if r > 1 else 0.0
    child_th = point_theta(r-1, kc) if r > 1 else 0.0
    return (point_M(r)-.5*child_m+2*point_D(r)+2*point_theta(r, kp)-child_th)/t


c0 = 14+4/log(2); cstar = 14.5+4/log(2)
sliding = [(threshold(r, 2, 2), r) for r in range(3, 41)]
full = [(threshold(r, r, r-1), r) for r in range(2, 31)]

overlap_max = (-1e100, None); overlap_positive = 0; tested = 0
for n in (3, 4):
    for tail in product((-1, 1), repeat=(1 << n)-1):
        v = (-1,)+tail
        d = drift(v, 0b011, 0, 0b110, cstar)
        tested += 1
        if d > overlap_max[0]: overlap_max = (d, (n, v))
        overlap_positive += d > 1e-10

print('status=DIAGNOSTIC_COMPLETE')
print(f'c0={c0:.15f}')
print(f'cstar={cstar:.15f}')
print(f'width_two_max_r3_to_r40={max(sliding)[0]:.15f}')
print(f'width_two_max_rank={max(sliding)[1]}')
print(f'width_two_r40={sliding[-1][0]:.15f}')
print(f'endpoint_r2={threshold(2,2,1):.15f}')
print(f'endpoint_r1={threshold(1,1,0):.15f}')
print(f'full_block_r30={full[-1][0]:.15f}')
print(f'full_block_asymptotic_target_r30={4*30-3+4/log(2):.15f}')
print(f'exhaustive_transition_functions={tested}')
print(f'exhaustive_transition_positive_cases={overlap_positive}')
print(f'exhaustive_transition_max_drift={overlap_max[0]:.15g}')
