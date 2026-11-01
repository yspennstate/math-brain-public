#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product

EPS = F(113009, 5000000)
R0 = F(1999313322941, 16492674416640000000)
ETA_CENTER = F(1) - EPS

def phi(m):
    return F(1) - m**4 - EPS * (F(1) - m*m)**3

def eta(p):
    return phi(F(1) - 2*p)

# Algebraic facts used by the proof.
assert R0 > 0
assert R0 < ETA_CENTER
assert eta(F(0)) == 0
assert eta(F(1)) == 0
assert eta(F(1,2)) == ETA_CENTER

# eta(p) = 2 V - V^2 - eps V^3 exactly.
for p in [F(0),F(1,8),F(1,4),F(1,2),F(3,4),F(7,8),F(1)]:
    V = 4*p*(1-p)
    assert eta(p) == 2*V - V*V - EPS*V**3

# The simplified one-step lower bound follows because, for fixed pivotal
# probability delta, the lower envelope in d is decreasing on 0<=d<=2 delta.
# Its derivative is <= 2 t(1-t)(R0-(1-EPS)) < 0.
assert R0 - ETA_CENTER < 0

def uniform_defect(table, n):
    N = 1 << n
    bits = [(table >> x) & 1 for x in range(N)]
    p_out = F(sum(bits), N)
    infl = []
    for i in range(n):
        mask = 1 << i
        cnt = sum(bits[x] != bits[x ^ mask] for x in range(N))
        infl.append(F(cnt, N))
    return sum(infl, F(0))*ETA_CENTER - eta(p_out)

def weight(x, n, ps):
    w = F(1)
    for i,p in enumerate(ps):
        w *= p if ((x >> i) & 1) else (1-p)
    return w

def biased_defect(table, n, ps):
    N = 1 << n
    bits = [(table >> x) & 1 for x in range(N)]
    p_out = sum((weight(x,n,ps) for x in range(N) if bits[x]), F(0))
    alphas = []
    for i in range(n):
        mask = 1 << i
        a = F(0)
        for x in range(N):
            if x & mask:
                continue
            if bits[x] != bits[x | mask]:
                w = F(1)
                for j,p in enumerate(ps):
                    if j == i:
                        continue
                    w *= p if ((x >> j)&1) else (1-p)
                a += w
        alphas.append(a)
    return sum(alphas[i]*eta(ps[i]) for i in range(n)) - eta(p_out)

uniform_rows = []
for n in range(1,5):
    zeros = 0
    minpos = None
    for table in range(1 << (1 << n)):
        D = uniform_defect(table,n)
        assert D >= 0
        if D == 0:
            zeros += 1
        elif minpos is None or D < minpos:
            minpos = D
    assert zeros == 2*n + 2  # constants plus +/- literals
    uniform_rows.append((n, zeros, minpos))

grid = [F(1,4),F(1,2),F(3,4)]
biased_rows = []
for n in [2,3]:
    zero_pairs = 0
    minpos = None
    total = 0
    for ps in product(grid, repeat=n):
        for table in range(1 << (1 << n)):
            total += 1
            D = biased_defect(table,n,ps)
            assert D >= 0
            if D == 0:
                zero_pairs += 1
            elif minpos is None or D < minpos:
                minpos = D
    assert zero_pairs == (2*n+2) * (3**n)
    biased_rows.append((n,total,zero_pairs,minpos))

print("PASS")
print("epsilon", EPS, float(EPS))
print("r0", R0, float(R0))
print("eta_center", ETA_CENTER, float(ETA_CENTER))
for n,zeros,minpos in uniform_rows:
    print("uniform_n", n, "zero_gates", zeros,
          "min_positive", minpos, None if minpos is None else float(minpos))
for n,total,zeros,minpos in biased_rows:
    print("biased_grid_n", n, "pairs", total, "zero_pairs", zeros,
          "min_positive", minpos, float(minpos))
