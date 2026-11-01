#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
import math

N = 16
NEG = {0,1,2,3,4,5,6,8}
f = [-1 if x in NEG else 1 for x in range(N)]

def chi(s,x):
    return -1 if ((s & x).bit_count() & 1) else 1

W = [sum(f[x]*chi(s,x) for x in range(N)) for s in range(N)]
expected = [0,-4,-4,0,-4,0,0,-4,-12,0,0,4,0,4,4,0]
assert W == expected
assert sum(f) == 0

# uniform spectral influences j_i = sum_{S contains i} \hat f(S)^2
j = [
    Fraction(sum(W[s]*W[s] for s in range(N) if (s >> i) & 1), N*N)
    for i in range(4)
]
assert j == [Fraction(1,4), Fraction(1,4), Fraction(1,4), Fraction(3,4)]
I = sum(j, Fraction())
assert I == Fraction(3,2)
q = [x/I for x in j]
assert q == [Fraction(1,6), Fraction(1,6), Fraction(1,6), Fraction(1,2)]

# Signed magnitude-packet valuations r_a.
def v2(z):
    z = abs(z)
    assert z
    r = 0
    while z % 2 == 0:
        r += 1
        z //= 2
    return r

packet_vals = {}
for mag in sorted({abs(z) for z in W if z}):
    support = [s for s,z in enumerate(W) if abs(z) == mag]
    phys = []
    for x in range(N):
        V = sum((1 if W[s] > 0 else -1)*chi(s,x) for s in support)
        if V:
            phys.append(V)
    assert phys
    packet_vals[mag] = min(v2(z) for z in phys)
assert packet_vals == {4:0, 12:0}

# Price/magnitude cells (k, |raw Walsh|).
cells = {}
for s,z in enumerate(W):
    if not z:
        continue
    cells.setdefault((s.bit_count(), abs(z)), []).append(s)
assert cells == {(1,4):[1,2,4], (3,4):[7,11,13,14], (1,12):[8]}

def price(s):
    out = Fraction(1,1)
    for i in range(4):
        if (s >> i) & 1:
            out *= q[i]
    return out

# Only the (k=3, mag=4) cell has price dispersion.
assert len({price(s) for s in cells[(1,4)]}) == 1
assert len({price(s) for s in cells[(1,12)]}) == 1
C = cells[(3,4)]
prices = [price(s) for s in C]
assert prices == [Fraction(1,216), Fraction(1,72), Fraction(1,72), Fraction(1,72)]
Z = sum(prices, Fraction())
Q = [p/Z for p in prices]
P = [Fraction(1,4)]*4
assert Q == [Fraction(1,10), Fraction(3,10), Fraction(3,10), Fraction(3,10)]

# D_cell = log2(5) - 1 - (3/4)log2(3).
# Strict positivity is exact: 4*D_cell > 0 iff 5^4 > 2^4*3^3.
assert 5**4 > 2**4 * 3**3
cell_mass = sum(Fraction(W[s]*W[s], N*N) for s in C)
assert cell_mass == Fraction(1,4)

Dcell = math.log2(5) - 1 - 0.75*math.log2(3)
Dprice = 0.25*Dcell
assert Dcell > 0

# Verify the AM/GM formula numerically as an independent implementation.
AM = sum(float(p) for p in prices)/4.0
GM = math.prod(float(p) for p in prices)**0.25
assert abs(math.log2(AM/GM)-Dcell) < 1e-14

# Composition-prime certificate:
# If a nontrivial block A (2 <= |A| <= 3) were compressed to one Boolean
# inner gate, rows indexed by x_A could have at most two distinct truth vectors.
def row_count(A):
    A = tuple(A)
    B = tuple(i for i in range(4) if i not in A)
    rows = set()
    for aa in range(1 << len(A)):
        row = []
        for bb in range(1 << len(B)):
            x = 0
            for t,i in enumerate(A):
                if (aa >> t) & 1:
                    x |= 1 << i
            for t,i in enumerate(B):
                if (bb >> t) & 1:
                    x |= 1 << i
            row.append(f[x])
        rows.add(tuple(row))
    return len(rows)

row_counts = {}
for r in (2,3):
    for A in combinations(range(4), r):
        row_counts[A] = row_count(A)
        assert row_counts[A] >= 3

H = 4 - (9/8)*math.log2(3)
beta = 0.5
Cstar = 6.5218512
Dstar = Cstar*beta - H
C0 = 6.4548
Wcurrency = beta/4
margin = -(C0*beta-H)/Wcurrency

print("PASS")
print("walsh =", W)
print("j =", [str(x) for x in j], "I =", I, "q =", [str(x) for x in q])
print("packet valuations =", packet_vals)
print("price cell P =", [str(x) for x in P], "Q =", [str(x) for x in Q])
print("D_cell =", format(Dcell, ".15f"))
print("D_price|mag =", format(Dprice, ".15f"))
print("row_counts =", {str(k):v for k,v in row_counts.items()})
print("H =", format(H, ".15f"), "balanced_defect_at_Cstar =", format(Dstar, ".15f"))
print("uniform base margin c_G =", format(margin, ".15f"))
