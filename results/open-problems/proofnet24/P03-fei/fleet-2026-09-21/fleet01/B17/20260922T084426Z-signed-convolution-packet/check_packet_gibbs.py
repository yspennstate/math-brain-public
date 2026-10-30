#!/usr/bin/env python3
"""Sanity checker for B17 signed convolution packet theorem.
Standard library only. The theorem is analytic; finite enumeration is diagnostic.
"""
from itertools import combinations
from math import comb, exp, log, log2, sqrt

C = 0.01
QEXP = 20.0
TOL = 1e-10

def fwht(a):
    a = list(map(float, a))
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def packet_constants(k, c=C, q=QEXP):
    y = c/k
    A = (1+y)**k - 1
    bracket = max(0.0, 3 - 2*(1+y)**(k-2))
    P = 2*sqrt(comb(k,2))*y/A*bracket
    Q = 1 + sqrt(((1+(q-1)*y)**k - 1)/A)
    alpha = (q-4)/(q-2)
    B = Q**(2-alpha)
    lo, hi = 0.0, max(1.0, P)
    while 2*hi + B*hi**alpha < P:
        hi *= 2
    for _ in range(120):
        mid = (lo+hi)/2
        if 2*mid + B*mid**alpha < P:
            lo = mid
        else:
            hi = mid
    return y, A, P, Q, alpha, hi

def check_one(f, k):
    n = 1 << k
    a = [z/n for z in fwht(f)]
    y, A, P, Q, alpha, dstar = packet_constants(k)
    rho = [0.0]*n
    for s in range(1,n):
        rho[s] = y**(s.bit_count())/A
    b = [0.0]*n
    for s in range(1,n):
        sign = 1.0 if a[s] >= 0 else -1.0
        b[s] = sign*sqrt(rho[s])
    d = sqrt(sum((a[s]-b[s])**2 for s in range(n)))
    g = fwht(b)
    packet_norm = sqrt(sum((z*z-1.0)**2 for z in g)/n)
    w = [z*z for z in a]
    kl = sum(w[s]*log2(w[s]/rho[s])
             for s in range(1,n) if w[s] > 0.0)
    assert packet_norm + TOL >= P
    assert d + TOL >= dstar
    assert kl + TOL >= dstar*dstar/log(2.0)
    return d, packet_norm, kl, dstar, P

def balanced_functions(k):
    n = 1 << k
    half = n//2
    for plus in combinations(range(n), half):
        f = [-1.0]*n
        for j in plus:
            f[j] = 1.0
        yield f

def uniform_corollary(c=C, q=QEXP):
    P = c*(3-2*exp(c))/(exp(c)-1)
    Q = 1 + sqrt((exp((q-1)*c)-1)/c)
    alpha = (q-4)/(q-2)
    B = Q**(2-alpha)
    d0 = min(P/4, (P/(2*B))**(1/alpha))
    return P, Q, alpha, d0, d0*d0/log(2.0)

def main():
    print("c =", C, "q =", QEXP)
    P0,Q0,a0,d0,kl0 = uniform_corollary()
    print("uniform P(c) =", repr(P0))
    print("uniform Q(c,q) =", repr(Q0))
    print("alpha =", repr(a0))
    print("explicit dimension-free d0 =", repr(d0))
    print("explicit dimension-free KL lower bound =", repr(kl0))
    total = 0
    for k in (2,3,4):
        mind = minpacket = minkl = float("inf")
        count = 0
        ds = pp = None
        for f in balanced_functions(k):
            count += 1
            d, packet, kl, ds, pp = check_one(f,k)
            mind = min(mind,d)
            minpacket = min(minpacket,packet)
            minkl = min(minkl,kl)
        total += count
        print("k =", k, "count =", count,
              "min_d =", repr(mind),
              "dstar =", repr(ds),
              "min_packet =", repr(minpacket),
              "P_k =", repr(pp),
              "min_KL =", repr(minkl),
              "proved_KL_floor =", repr(ds*ds/log(2.0)))
    print("balanced truth tables checked =", total)
    print("PASS")

if __name__ == "__main__":
    main()
