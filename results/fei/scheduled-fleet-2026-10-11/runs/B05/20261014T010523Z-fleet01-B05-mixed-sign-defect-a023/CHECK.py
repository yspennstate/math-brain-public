#!/usr/bin/env python3
"""Deterministic checks for the mixed-sign point-defect tower theorem."""

from __future__ import annotations

import itertools
import math
import random

C = 8.0 / 3.0
TOL = 2e-10
SEED = 0xB05A023


def fwht(a):
    a = list(map(float, a))
    h = 1
    while h < len(a):
        for k in range(0, len(a), 2*h):
            for j in range(k, k+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    n = len(a)
    return [x/n for x in a]


def UI(vals):
    n = len(vals).bit_length()-1
    p = [x*x for x in fwht(vals)]
    upper = p[:]
    for j in range(n):
        for s in range(1 << n):
            if not ((s >> j) & 1):
                upper[s] += upper[s | (1 << j)]
    U = 0.0
    I = 0.0
    for s, x in enumerate(p):
        if x:
            U += x * math.log2(upper[s]/x)
        I += s.bit_count() * x
    return U, I, fwht(vals)[0]


def tensor(f, g):
    return [x*y for y in g for x in f]


def activate(q):
    out = []
    for x in q:
        out.extend([1, x])
    return out


def Q(r, sigma=1):
    v = [1]*(1 << r)
    v[0] = -1
    return [sigma*x for x in v]


def tower(P, steps):
    w = [-1, 1]
    F = activate(tensor(P, w))
    for sigma, r in steps:
        F = activate(tensor(F, Q(r, sigma)))
    return F


def R(t):
    def zlog(x):
        return 0.0 if x == 0 else x*math.log2(1/x)
    E = zlog((1+t)**2/4) + ((1-t)**2/4)*math.log2(2/(1-t)) if t < 1 else 0.0
    middle = 0.0 if t == 0 else 0.5*t*t*math.log2(1/(t*t))
    return E-middle+0.25*(1-t*t)


def scalar_suite():
    positive = negative = 0
    min_negative_slack = 1e9
    for j in range(200001):
        t = -1 + 2*j/200000
        if t >= 0:
            assert R(t) <= (4/3)*(1-t)+TOL
            positive += 1
        if t <= 0:
            assert R(t) <= 1+TOL
            slack = (4/3)*(1-t)-R(t)
            assert slack >= 1/3-TOL
            min_negative_slack = min(min_negative_slack, slack)
            negative += 1
    return positive, negative, min_negative_slack


def direct_suite():
    bases = endpoint = direct = mixed = 0
    worst = 0.0
    for bits in itertools.product((-1,1), repeat=8):
        u, i, _ = UI(bits)
        if u > C*i+TOL:
            continue
        bases += 1
        for steps in ([(1,2)], [(-1,2)], [(1,3)], [(-1,3)],
                      [(1,2),(-1,2)], [(-1,2),(1,2)],
                      [(1,3),(-1,2)], [(-1,3),(1,2)]):
            F = tower(list(bits), steps)
            uf, inf, _ = UI(F)
            assert uf <= C*inf+TOL
            endpoint += 1
            direct += 1
            mixed += int(len({s for s,_ in steps}) == 2)
            worst = max(worst, uf/inf)
    return bases, endpoint, direct, mixed, worst


def recurrence_suite():
    rng = random.Random(SEED)
    checks = negative_steps = 0
    min_reserve_gap = 1e9
    for _ in range(4000):
        IP = rng.random()*8
        UP = rng.random()*C*IP
        U = 1+UP/2
        I = 1+IP/2
        m = 0.5
        reserve = C*I-U
        lower = C-1 + 0.5*(C*IP-UP)
        assert reserve+TOL >= lower
        depth = rng.randint(1,80)
        discounted = lower
        for _k in range(2, depth+1):
            r = rng.randint(2,100)
            sigma = rng.choice((-1,1))
            beta = 1-2**(1-r)
            t = sigma*beta*m
            IQ = 2*r*(2**-r)
            UQ = beta*beta*math.log2(1/(beta*beta))+2*r*(2**-r)*beta
            U = 0.5*U+0.5*UQ+R(t)
            I = 0.5*I+0.5*IQ+0.5*(1-t)
            m = 0.5*(1+t)
            discounted = 0.5*discounted + (1/3 if sigma < 0 else 0)
            assert 0 <= m <= 1
            assert U <= C*I+TOL
            assert C*I-U+TOL >= discounted
            if sigma < 0:
                negative_steps += 1
                min_reserve_gap = min(min_reserve_gap, C*I-U-discounted)
            checks += 1
    return checks, negative_steps, min_reserve_gap


def restriction(vals, coord, bit):
    return [vals[x] for x in range(len(vals)) if ((x >> coord)&1)==bit]


def tree_suite():
    rng = random.Random(SEED+1)
    tests = tensor_tests = 0
    for signs in ([(1,2),(-1,2)], [(-1,3),(1,2)], [(1,2),(-1,3),(1,2)]):
        P = [1,1,1,-1]
        F = tower(P, signs)
        rootU, rootI, _ = UI(F)
        n = len(F).bit_length()-1
        for _ in range(40):
            leaves=[(F,1.0,list(range(n)))]
            for _step in range(min(7,n)):
                new=[]
                for v,w,coords in leaves:
                    if not coords or rng.random()<0.28:
                        new.append((v,w,coords)); continue
                    j=rng.randrange(len(coords))
                    rem=coords[:j]+coords[j+1:]
                    new.append((restriction(v,j,0),w/2,rem))
                    new.append((restriction(v,j,1),w/2,rem))
                leaves=new
            leafU=sum(w*UI(v)[0] for v,w,_ in leaves)
            assert rootU-leafU <= C*rootI+TOL
            h=[1,1,1,-1,-1,1,1,1]
            lhs=UI(tensor(F,h))[0]-sum(w*UI(tensor(v,h))[0] for v,w,_ in leaves)
            assert abs(lhs-(rootU-leafU))<2e-9
            tests += 1
            tensor_tests += 1
    return tests,tensor_tests


def main():
    s=scalar_suite(); d=direct_suite(); r=recurrence_suite(); t=tree_suite()
    print(f"scalar_positive_points={s[0]}")
    print(f"scalar_negative_points={s[1]}")
    print(f"minimum_negative_scalar_reserve={s[2]:.15g}")
    print(f"eligible_three_bit_bases={d[0]}")
    print(f"direct_towers={d[2]}")
    print(f"mixed_sign_direct_towers={d[3]}")
    print(f"largest_direct_U_over_I={d[4]:.15g}")
    print(f"recurrence_steps={r[0]}")
    print(f"negative_recurrence_steps={r[1]}")
    print(f"minimum_extra_reserve_gap={r[2]:.15g}")
    print(f"pruned_trees={t[0]}")
    print(f"terminal_tensor_checks={t[1]}")
    print("PASS")


if __name__ == "__main__":
    main()
