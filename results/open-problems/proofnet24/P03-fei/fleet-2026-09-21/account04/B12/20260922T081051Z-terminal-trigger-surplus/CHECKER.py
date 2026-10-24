#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

ETA = Fraction(1, 16)

def pc(x):
    return x.bit_count()

def subcube_mask(m, F, a):
    out = 0
    for x in range(1 << m):
        ok = True
        for j, k in enumerate(F):
            if ((x >> k) & 1) != ((a >> j) & 1):
                ok = False
                break
        if ok:
            out |= 1 << x
    return out

def crossing(m, E, F):
    N = 1 << m
    q = Fraction(pc(E), N)
    r = len(F)
    fibre = 1 << (m-r)
    total = Fraction(0)
    for z in range(1 << r):
        cnt = 0
        for x in range(N):
            if all(((x >> k) & 1) == ((z >> j) & 1)
                   for j, k in enumerate(F)):
                cnt += (E >> x) & 1
        p = Fraction(cnt, fibre)
        total += abs(p - Fraction(1,2))
    return total / (1 << r) - abs(q - Fraction(1,2))

def boundary(m, E, k):
    N = 1 << m
    cnt = 0
    for x in range(N):
        cnt += ((E >> x) & 1) != ((E >> (x ^ (1 << k))) & 1)
    return Fraction(cnt, N)

pairs = 0
boundary_checks = 0
min_cross_ratio = None
min_boundary_ratio = None

# Exact exhaustive regression for all support sets through 4 residual variables.
for m in range(1, 5):
    N = 1 << m
    for E in range(1, 1 << N):
        ecount = pc(E)
        if 2 * ecount > N:  # centered q <= 1/2
            continue
        q = Fraction(ecount, N)
        for r in range(m + 1):
            for F in combinations(range(m), r):
                for a in range(1 << r):
                    Q = subcube_mask(m, F, a)
                    diff = pc(E ^ Q)
                    if 16 * diff > ecount:
                        continue
                    pairs += 1
                    # A robust centered row cannot have an empty trigger set.
                    assert r > 0
                    c = crossing(m, E, F)
                    assert c >= Fraction(15,16) * q
                    cr = c / q
                    min_cross_ratio = cr if min_cross_ratio is None else min(min_cross_ratio, cr)
                    for k in F:
                        p = boundary(m, E, k)
                        assert p >= Fraction(7,4) * q
                        br = p / q
                        min_boundary_ratio = br if min_boundary_ratio is None else min(min_boundary_ratio, br)
                        boundary_checks += 1

aggregation_constant = Fraction(2,1) / (Fraction(15,16) * Fraction(7,8))
assert aggregation_constant == Fraction(256,105)

print("robust_support_pairs", pairs)
print("trigger_boundary_checks", boundary_checks)
print("min_crossing_over_q", min_cross_ratio)
print("min_boundary_over_q", min_boundary_ratio)
print("eta_1_16_aggregation_constant", aggregation_constant)
print("RESULT PASS")
