#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
from itertools import combinations
getcontext().prec = 60

G0 = 0xC7C5
G1 = 0x3A38
TT = G0 | (G1 << 16)

def bit(tt, x):
    return (tt >> x) & 1

def walsh(tt, n=4):
    N = 1 << n
    f = [-1 if bit(tt,x) else 1 for x in range(N)]
    out = []
    for S in range(N):
        z = 0
        for x, fx in enumerate(f):
            chi = -1 if ((x & S).bit_count() & 1) else 1
            z += fx * chi
        out.append(Fraction(z, N))
    return out

def slice_pattern(tt, k, A, outside_assignment):
    A = tuple(A)
    outside = tuple(i for i in range(k) if i not in A)
    p = 0
    for ya in range(1 << len(A)):
        x = 0
        for j,var in enumerate(A):
            if (ya >> j) & 1:
                x |= 1 << var
        for j,var in enumerate(outside):
            if (outside_assignment >> j) & 1:
                x |= 1 << var
        if bit(tt,x):
            p |= 1 << ya
    return p

def is_relevant(tt, k, i):
    return any(bit(tt,x) != bit(tt,x ^ (1<<i)) for x in range(1<<k))

def decomposition_block(tt, k=5):
    # If f = F(g(x_A), x_{A^c}) with 2 <= |A| < k, then as the
    # outside assignment varies, all nonconstant A-slices are g or not-g.
    for r in range(2,k):
        for A in combinations(range(k), r):
            full = (1 << (1 << r)) - 1
            pats = [slice_pattern(tt,k,A,o) for o in range(1 << (k-r))]
            non = [p for p in pats if p not in (0,full)]
            if not non:
                return A
            p = non[0]
            if all(q in (0, full, p, full ^ p) for q in pats):
                return A
    return None

u = walsh(G0)
v = walsh(G1)
c = [(a+b)/2 for a,b in zip(u,v)]
a = [(b-a)/2 for a,b in zip(u,v)]
d = Fraction((G0 ^ G1).bit_count(),16)
beta = sum((a[j]*a[j] for j in range(16) if c[j] == 0), Fraction(0))
assert d == Fraction(7,8)
assert sum(x*x for x in a) == d
assert sum(x*x for x in c) == 1-d
assert sum(x*y for x,y in zip(c,a)) == 0
assert beta == d
assert all(is_relevant(TT,5,i) for i in range(5))
assert decomposition_block(TT,5) is None

expect_u = [Fraction(x,8) for x in (-1,-3,3,1,-1,-3,-5,1,1,-1,1,-1,1,-1,1,-1)]
expect_v = [Fraction(x,8) for x in (1,3,-3,-1,1,3,5,-1,1,-1,1,-1,1,-1,1,-1)]
assert u == expect_u and v == expect_v

# Universal five-input prime axial loss envelope.
# Prime + essential rules out d=0 and d=1; with four uniform residual bits
# d=j/16, 1<=j<=15. For j<=14,
# 170d + 16 sqrt(d(1-d)) <= 170*(14/16)+8 = 156.75.
# At j=15 it is 159.375+sqrt(15), which is larger.
assert Decimal("3.873")**2 > Decimal(15)
C = Decimal("6.521851214")
eps = Decimal("0.0000259")
A_bound = 4*C + Decimal("159.375") + Decimal("3.873")
loss = A_bound*eps + Decimal(30)*eps*eps
delta0 = Decimal("0.0049065")
gap = delta0-loss
assert A_bound == Decimal("189.335404856")
assert loss == Decimal("0.0049038071100704")
assert gap == Decimal("0.0000026928899296")
assert Decimal(1)/Decimal(32)-eps > Decimal(1)/Decimal(64)

print("PASS exact Boolean sharp-cancellation witness")
print("truth_table_hex=0x%08x" % TT)
print("d=beta=%s" % d)
print("composition_prime=True; all_5_variables_relevant=True")
print("PASS universal prime-axis envelope")
print("A_bound=%s" % A_bound)
print("epsilon=%s" % eps)
print("loss=%s" % loss)
print("certified_gap=%s" % gap)
