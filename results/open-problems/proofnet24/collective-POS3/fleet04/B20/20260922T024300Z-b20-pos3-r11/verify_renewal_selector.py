#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations
from math import sqrt

# Source-bound seven-element endpoint-fork witness from fleet03/B11.
V = tuple(range(7))
covers = {
    (0,2),(0,3),(0,4),(0,5),(0,6),
    (1,2),(1,5),(2,5),(4,5),(4,6),
}
rels = set(covers)
while True:
    add = {(a,d) for (a,b) in rels for (c,d) in rels if b == c and a != d and (a,d) not in rels}
    if not add:
        break
    rels |= add

def extensions(vertices):
    vertices = tuple(vertices)
    rr = {(a,b) for a,b in rels if a in vertices and b in vertices}
    ans = []
    for p in permutations(vertices):
        pos = {v:i for i,v in enumerate(p)}
        if all(pos[a] < pos[b] for a,b in rr):
            ans.append(p)
    return ans

def prob_before(ext, a, b):
    return Fraction(sum(p.index(a) < p.index(b) for p in ext), len(ext))

P = extensions(V)
Q = extensions(range(1,7))
assert len(P) == 79
assert len(Q) == 54

alpha = prob_before(P, 0, 1)
delta = 1 - alpha
q1 = prob_before(Q, 1, 3)
q2 = prob_before(Q, 1, 4)
rho_y = Fraction(sum(p.index(1) < p.index(3) and p.index(1) < p.index(4) for p in Q), len(Q))
R = Fraction(sum(p.index(1) < p.index(3) and p.index(1) < p.index(4) for p in P), len(P))

assert alpha == Fraction(54,79)
assert q1 == Fraction(20,27)
assert q2 == Fraction(5,9)
assert rho_y == Fraction(25,54)
assert R == Fraction(50,79)
assert R == delta + alpha * rho_y
assert R == 2 * delta
assert q1 * q2 <= rho_y <= delta / alpha

# Algebraic thresholds used by the symbolic proof.
single_cap = (5 + sqrt(17)) / 12
assert Fraction(2,3) < alpha < Fraction(9,13) < single_cap
# For alpha > 2/3, h >= 2 would force
# 1-alpha > 2 alpha (1 - 1/(3 alpha))^2, equivalent to
# 27 alpha^2 - 21 alpha + 2 < 0; its upper root is exactly 2/3,
# hence impossible.
def h2_poly(a):
    return 27*a*a - 21*a + 2
assert h2_poly(Fraction(2,3)) == 0
assert h2_poly(Fraction(7,10)) > 0

print("eP", len(P), "eQ", len(Q))
print("alpha", alpha, "delta", delta)
print("q_y_s1", q1, "q_y_s2", q2, "rho_y", rho_y)
print("joint_P", R, "2delta", 2*delta)
print("q_product", q1*q2, "delta_over_alpha", delta/alpha)
print("single_channel_cap_decimal", f"{single_cap:.12f}")
print("POS3_RENEWAL_SELECTOR_REGRESSION_PASS")
