#!/usr/bin/env python3
"""
Exact finite arithmetic self-check for SHPECTOROV-ZHAO-2026-SRG69.

This verifies only the finite consequences stated in the accompanying report:
(1) the universal triangle-window 36 <= T_L <= 103 obtained by combining
    exact block degree-square and common-neighbour/4-cycle convexity;
(2) the endpoint spectral-moment/localizing filter for
    a=m_L(5), b=m_L(-3), starting from the 20 pairs from the previous report;
(3) the resulting 17 surviving (a,b) pairs and exact contiguous T_L windows.

All arithmetic is integer/rational; no floating point and no graph search.
"""

from fractions import Fraction

F = [85,77,69,65,65,65,69,73,79,87,95]

def choose2(x):
    return x*(x-1)//2

def balanced_choose2(m, s):
    assert m >= 1 and 0 <= s
    q, r = divmod(s, m)
    return (m-r)*choose2(q) + r*choose2(q+1)

def block_min_degree_square(E):
    q, r = divmod(E, 48)
    assert 0 <= q <= 10
    if r == 0:
        return 48*F[q]
    assert q < 10
    return (48-r)*F[q] + r*F[q+1]

def universal_q_interval(T):
    E = 420 - 3*T
    if not (0 <= E <= 480):
        return None
    minD = block_min_degree_square(E)
    qmax = (4200 + 12*T - minD)//8
    low_twice = balanced_choose2(70, 3*T) + balanced_choose2(120, 420-3*T)
    qmin = (low_twice + 1)//2
    return qmin, qmax

def det3(a,b,c,d,e,f):
    return a*d*f + 2*b*c*e - a*e*e - d*c*c - f*b*b

def psd_hankel(m0,m1,m2,m3,m4):
    if min(m0,m2,m4) < 0:
        return False
    if m0*m2 - m1*m1 < 0:
        return False
    if m0*m4 - m2*m2 < 0:
        return False
    if m2*m4 - m3*m3 < 0:
        return False
    if det3(m0,m1,m2,m2,m3,m4) < 0:
        return False
    return True

def psd_localizing(m0,m1,m2,m3,m4):
    # q(theta)=(theta+3)(5-theta)=15+2theta-theta^2 >= 0 on [-3,5].
    g00 = 15*m0 + 2*m1 - m2
    g01 = 15*m1 + 2*m2 - m3
    g11 = 15*m2 + 2*m3 - m4
    return g00 >= 0 and g11 >= 0 and g00*g11 - g01*g01 >= 0

PAIRS = (
    [(0,b) for b in range(8)]
    + [(1,b) for b in range(7)]
    + [(2,b) for b in range(5)]
)
assert len(PAIRS) == 20

universal = []
for T in range(141):
    qi = universal_q_interval(T)
    if qi is not None and qi[0] <= qi[1]:
        universal.append(T)
assert universal == list(range(36,104))
print("UNIVERSAL_TRIANGLE_WINDOW", universal[0], universal[-1], len(universal))

survivors = {}
for a,b in PAIRS:
    feasible_T = {}
    r = 19-a-b
    m1 = -7-5*a+3*b
    m2 = 91-25*a-9*b
    for T in universal:
        qmin,qmax = universal_q_interval(T)
        for Q in range(qmin, qmax+1):
            m3 = 6*T - 343 - 125*a + 27*b
            m4 = 8*Q - 581 - 625*a - 81*b
            if psd_hankel(r,m1,m2,m3,m4) and psd_localizing(r,m1,m2,m3,m4):
                feasible_T.setdefault(T, []).append(Q)
    if feasible_T:
        survivors[(a,b)] = feasible_T

expected_windows = {
    (0,0):(36,103),(0,1):(36,100),(0,2):(36,95),(0,3):(36,88),
    (0,4):(36,79),(0,5):(36,68),(0,6):(36,55),
    (1,0):(54,103),(1,1):(54,100),(1,2):(54,95),(1,3):(54,88),
    (1,4):(54,78),(1,5):(54,68),
    (2,0):(83,103),(2,1):(83,100),(2,2):(83,95),(2,3):(84,86),
}
assert set(survivors) == set(expected_windows)
for pair,(lo,hi) in expected_windows.items():
    ts = sorted(survivors[pair])
    assert ts == list(range(lo,hi+1))
    print("SURVIVOR", pair, "T", lo, hi, "states", sum(len(v) for v in survivors[pair].values()))

eliminated = sorted(set(PAIRS)-set(survivors))
assert eliminated == [(0,7),(1,6),(2,4)]
print("ELIMINATED_ENDPOINT_PAIRS", eliminated)

assert sorted((T,min(Qs),max(Qs)) for T,Qs in survivors[(2,3)].items()) == [
    (84,261,261),(85,262,262),(86,263,264)
]
print("TIGHT_2_3", [(T,min(Qs),max(Qs)) for T,Qs in sorted(survivors[(2,3)].items())])

cubic_bounds = {0:107,1:102,2:97,3:90,4:82,5:72,6:60,7:42}
rhos = {
    0:Fraction(-21,17), 1:Fraction(-51,47), 2:Fraction(-39,43),
    3:Fraction(-9,13), 4:Fraction(-3,7), 5:Fraction(-3,31),
    6:Fraction(1,3), 7:Fraction(21,23),
}
for b in range(8):
    a = 0
    r = 19-a-b
    s1 = -7-5*a+3*b
    s2 = 91-25*a-9*b
    rho = rhos[b]
    U = (2*rho+5)*s2 + (-rho*rho-10*rho)*s1 + 5*rho*rho*r
    trace3_bound = Fraction(343 + 125*a - 27*b,1) + U
    Tbound = trace3_bound/Fraction(6,1)
    assert Tbound.numerator//Tbound.denominator == cubic_bounds[b]
    print("CUBIC_BOUND", b, rho, Tbound, cubic_bounds[b])

print("ALL_EXACT_CHECKS_PASS")
