#!/usr/bin/env python3
"""Exact finite checker for the Palm trigger-cluster lemmas.

This checker is diagnostic evidence only; the theorem is proved analytically in REPORT.md.
It enumerates Boolean functions up to n=4 (fixing global sign), computes exact rational
Walsh-square spectra, each derivative Palm law, and the closest uniform power-set law.
"""

from fractions import Fraction
from itertools import product

EPS = Fraction(1, 16)
G = (Fraction(1, 2) - EPS) / EPS
R = (Fraction(1, 2) + EPS) / (Fraction(1, 2) - EPS)

def popcount(x):
    return x.bit_count()

def walsh_squares(values, n):
    N = 1 << n
    out = {}
    for mask in range(N):
        s = 0
        for x, fx in enumerate(values):
            parity = popcount(mask & x) & 1
            s += fx * (-1 if parity else 1)
        out[mask] = Fraction(s*s, N*N)
    assert sum(out.values(), Fraction()) == 1
    return out

def tv_to_uniform(palm, Fmask, n, i):
    support = [m for m in range(1 << n) if (m & (1 << i)) == 0 and (m & ~Fmask) == 0]
    u = Fraction(1, len(support))
    keys = set(palm) | set(support)
    return sum(abs(palm.get(k, Fraction()) - (u if k in support else Fraction()))
               for k in keys) / 2

def best_trigger(palm, n, i):
    others = [k for k in range(n) if k != i]
    best = None
    for bits in range(1 << len(others)):
        F = 0
        for a, k in enumerate(others):
            if bits & (1 << a):
                F |= 1 << k
        tv = tv_to_uniform(palm, F, n, i)
        key = (tv, popcount(F), F)
        if best is None or key < best[0]:
            best = (key, F)
    return best[1], best[0][0]

def check_function(values, n):
    p = walsh_squares(values, n)
    j = [sum(mass for S, mass in p.items() if S & (1 << i)) for i in range(n)]
    palm = [None]*n
    F = [0]*n
    tv = [None]*n
    robust = [False]*n

    for i in range(n):
        if j[i] == 0:
            palm[i] = {}
            continue
        pi = {}
        for S, mass in p.items():
            if S & (1 << i):
                A = S & ~(1 << i)
                pi[A] = pi.get(A, Fraction()) + mass / j[i]
        assert sum(pi.values(), Fraction()) == 1
        palm[i] = pi
        F[i], tv[i] = best_trigger(pi, n, i)
        robust[i] = tv[i] <= EPS

    q = [[Fraction() for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for k in range(n):
            if i != k:
                q[i][k] = sum(mass for S, mass in p.items()
                              if (S & (1 << i)) and (S & (1 << k)))

    for i in range(n):
        if not robust[i]:
            continue
        for k in range(n):
            if k == i:
                continue
            if F[i] & (1 << k):
                assert q[i][k] >= j[i]*(Fraction(1,2)-EPS)
                assert q[i][k] <= j[i]*(Fraction(1,2)+EPS)
            else:
                assert q[i][k] <= j[i]*EPS

    for i in range(n):
        if not robust[i]:
            continue
        for k in range(n):
            if k == i or not robust[k] or not (F[i] & (1 << k)):
                continue
            if not (F[k] & (1 << i)):
                assert j[k] >= G*j[i]
            else:
                assert j[k] <= R*j[i] and j[i] <= R*j[k]
                assert (F[i] & ~(1 << k)) == (F[k] & ~(1 << i))

    seen=set()
    for root in range(n):
        if not robust[root] or root in seen:
            continue
        comp=[]
        stack=[root]
        seen.add(root)
        while stack:
            a=stack.pop()
            comp.append(a)
            for b in range(n):
                if b==a or not robust[b]:
                    continue
                if (F[a] & (1<<b)) and (F[b] & (1<<a)) and b not in seen:
                    seen.add(b)
                    stack.append(b)
        Ts={(F[a] | (1<<a)) for a in comp}
        assert len(Ts)==1

    return sum(robust), sum(
        1 for i in range(n) for k in range(n)
        if i != k and robust[i] and robust[k]
        and (F[i] & (1<<k)) and (F[k] & (1<<i))
    )

def main():
    totals=[]
    for n in range(1,5):
        N=1<<n
        functions=0
        functions_with_robust=0
        robust_rows=0
        reciprocal_directed=0
        for tail in product((-1,1), repeat=N-1):
            values=(1,)+tail
            functions += 1
            r, rd = check_function(values,n)
            robust_rows += r
            reciprocal_directed += rd
            if r:
                functions_with_robust += 1
        totals.append({
            "n":n,
            "functions":functions,
            "functions_with_robust_rows":functions_with_robust,
            "robust_rows":robust_rows,
            "reciprocal_directed_edges":reciprocal_directed,
        })
        print(totals[-1])
    print("PASS exact enumeration; zero violations")

if __name__ == "__main__":
    main()
