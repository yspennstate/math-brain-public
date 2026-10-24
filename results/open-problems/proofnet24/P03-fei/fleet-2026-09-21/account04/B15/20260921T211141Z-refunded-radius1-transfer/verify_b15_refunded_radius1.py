#!/usr/bin/env python3
"""Exact-formula / finite sanity checks for B15 refunded radius-one transfer.
Standard library only. Finite checks are not a proof of the universal candidate.
"""
from __future__ import annotations
import math
from fractions import Fraction


def fwht(a):
    a = list(map(float, a))
    h = 1
    n = len(a)
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def spectrum(bits, n):
    N = 1 << n
    vals = [1.0 if (bits >> x) & 1 else -1.0 for x in range(N)]
    a = fwht(vals)
    return [x/N for x in a]


def entropy(prob):
    return sum(-x*math.log2(x) for x in prob if x > 0.0)


def metrics(bits, n):
    N = 1 << n
    a = spectrum(bits, n)
    p = [x*x for x in a]
    H = entropy(p)
    inf = [sum(p[s] for s in range(N) if (s >> i) & 1) for i in range(n)]
    q = [min(x, 1.0-x) for x in inf]
    J = sum(q)
    c = []
    A = []
    b = []
    g = []
    r = []
    for d in range(N):
        cd = sum(p[s]*p[s^d] for s in range(N))
        Ad = sum(math.sqrt(p[s]*p[s^d]) for s in range(N))
        c.append(cd); A.append(Ad)
        if cd <= 1e-30:
            b.append(0.0); g.append(0.0); r.append(0.0)
            continue
        qd = [p[s]*p[s^d]/cd for s in range(N) if p[s]*p[s^d] > 0.0]
        Hd = entropy(qd)
        bd = cd*math.log2(Ad/cd)
        rd = 0.5*cd*(Hd + math.log2(1.0/cd))
        gd = bd-rd
        b.append(bd); g.append(gd); r.append(rd)
    high = [d for d in range(N) if d.bit_count() >= 2]
    low = [0] + [1 << i for i in range(n)]
    T_fibre = sum(r[d] for d in high)
    T_local = 0.0
    for s, ps in enumerate(p):
        if ps <= 0.0:
            continue
        radius1 = ps + sum(p[s^(1 << i)] for i in range(n))
        T_local += ps*math.log2(1.0/ps)*(1.0-radius1)
    actual = sum(b[d] for d in high) - sum(g)
    actual2 = H - sum(b[d] for d in low)
    return H, J, T_fibre, T_local, actual, actual2


def one_point_exact(n):
    N = 1 << n
    P = Fraction((N-2)*(N-2), N*N)
    u = Fraction(4, N*N)
    J = Fraction(2*n, N)
    c0 = P*P + (N-1)*u*u
    c1 = Fraction(8*(N-2), N**3)
    return N, P, u, J, c0, c1


def main():
    count = 0
    max_strong_ratio = 0.0
    max_actual_ratio = 0.0
    max_identity_err = 0.0
    for n in range(1, 5):
        N = 1 << n
        for bits in range(1 << N):
            H,J,T1,T2,actual,actual2 = metrics(bits,n)
            count += 1
            max_identity_err = max(max_identity_err, abs(T1-T2), abs(actual-actual2))
            if T1 + 1e-10 < actual:
                raise AssertionError((n,bits,"actual exceeds high refunded entropy",actual,T1))
            if J > 1e-14:
                max_strong_ratio = max(max_strong_ratio, T1/J)
                max_actual_ratio = max(max_actual_ratio, actual/J)
                if T1 > 4.0*J + 2e-10:
                    raise AssertionError((n,bits,"finite T2<=4J failure",T1,J))
                if actual > 4.0*J + 2e-10:
                    raise AssertionError((n,bits,"finite refunded target failure",actual,J))
    print("exhaustive_boolean_functions_n_le_4", count)
    print("max_identity_error", format(max_identity_err,'.3e'))
    print("max_T2_over_J_n_le_4", format(max_strong_ratio,'.15f'))
    print("max_actual_refunded_over_J_n_le_4", format(max_actual_ratio,'.15f'))

    print("one_point_family")
    for n in [2,3,4,5,8,12,16,24,32,48]:
        N,P,u,J,c0,c1 = one_point_exact(n)
        Pf=float(P); uf=float(u); Jf=float(J); c0f=float(c0); c1f=float(c1)
        H = -Pf*math.log2(Pf) - (N-1)*uf*math.log2(uf)
        b0 = c0f*math.log2(1.0/c0f)
        b1sum = n*c1f*n
        actual = H-b0-b1sum
        LA = math.log2(1.0/Pf)
        Lu = math.log2(1.0/uf)
        farA = 1.0-Pf-n*uf
        farB = 1.0-(n+1)*uf
        T = Pf*LA*farA + n*uf*Lu*farA + (N-1-n)*uf*Lu*farB
        if not (H < 4.0*Jf + 1e-14):
            raise AssertionError((n,"analytic-family H<4J numerical witness failed",H,Jf))
        if actual > T + 1e-12:
            raise AssertionError((n,"actual>T",actual,T))
        print(n,
              "H/J",format(H/Jf,'.15f'),
              "T2/J",format(T/Jf,'.15f'),
              "actual/J",format(actual/Jf,'.15f'),
              "b0/J",format(b0/Jf,'.6e'),
              "sum_b1/J",format(b1sum/Jf,'.6e'))

    print("PASS")

if __name__ == '__main__':
    main()
