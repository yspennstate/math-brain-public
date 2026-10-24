from fractions import Fraction as F
from itertools import product

# Exact certificate for R12 / D0011, run 3.
# No floating point arithmetic is used.

W5 = (5, 8, 4, 7, 6)
ST5 = list(product((0, 1), repeat=5))

def total(w, x):
    return sum(F(a) * b for a, b in zip(w, x))

def hinge(s, t):
    return max(s - F(t), F(0))

# Two affine LP-dual minorants for the five-Bernoulli family.
DUAL15 = (F(-7), F(1), F(4), F(3), F(3), F(3))
DUAL17 = (F(-3), F(0), F(2), F(1), F(1), F(1))

def affine(y, x):
    return y[0] + sum(y[i+1] * x[i] for i in range(len(x)))

EXPECTED_TIGHT15 = {
    (0,0,1,1,1), (0,1,0,0,1), (0,1,0,1,0),
    (0,1,1,0,0), (0,1,1,0,1), (1,0,1,0,1),
}
EXPECTED_TIGHT17 = {
    (0,0,1,1,1), (0,1,0,0,1), (0,1,0,1,0),
    (0,1,1,0,0), (0,1,1,0,1), (1,1,1,0,0),
}

for t, y, expected in [(15, DUAL15, EXPECTED_TIGHT15), (17, DUAL17, EXPECTED_TIGHT17)]:
    tight = set()
    for x in ST5:
        lhs = hinge(total(W5, x), t)
        rhs = affine(y, x)
        assert lhs >= rhs, (t, x, lhs, rhs)
        if lhs == rhs:
            tight.add(x)
    assert tight == expected, (t, tight ^ expected)

common = EXPECTED_TIGHT15 & EXPECTED_TIGHT17
assert len(common) == 5
assert all(x[0] == 0 for x in common)
print('DUAL_TIGHT_SETS_PASS')

# Affine-in-r masses represented as a + b*r. Verify the two optimal
# couplings symbolically coefficient-by-coefficient for all r.
def add(z1, z2):
    return (z1[0] + z2[0], z1[1] + z2[1])

def scale(c, z):
    return (c*z[0], c*z[1])

ZERO = (F(0), F(0))
ONE = (F(1), F(0))
R = (F(0), F(1))

Q15 = {
    (0,0,1,1,1): (F(1,5), F(-1)),
    (0,1,0,0,1): (F(1,5), F(-1)),
    (0,1,0,1,0): (F(1,10), F(1)),
    (0,1,1,0,0): (F(2,5), F(-1)),
    (0,1,1,0,1): (F(1,10), F(1)),
    (1,0,1,0,1): R,
}
Q17 = {
    (0,0,1,1,1): (F(1,5), F(0)),
    (0,1,0,0,1): (F(1,5), F(0)),
    (0,1,0,1,0): (F(1,10), F(0)),
    (0,1,1,0,0): (F(2,5), F(-1)),
    (0,1,1,0,1): (F(1,10), F(0)),
    (1,1,1,0,0): R,
}
TARGET = [R, (F(4,5),F(0)), (F(7,10),F(0)), (F(3,10),F(0)), (F(1,2),F(0))]

for Q, t, y in [(Q15, 15, DUAL15), (Q17, 17, DUAL17)]:
    mass = ZERO
    marg = [ZERO]*5
    obj = ZERO
    for x, q in Q.items():
        mass = add(mass, q)
        for i in range(5):
            if x[i]: marg[i] = add(marg[i], q)
        obj = add(obj, scale(hinge(total(W5,x), t), q))
    assert mass == ONE
    assert marg == TARGET, (t, marg)
    # dual expectation at p(r)
    dual_obj = (y[0], F(0))
    for i in range(5):
        dual_obj = add(dual_obj, scale(y[i+1], TARGET[i]))
    assert obj == dual_obj, (t, obj, dual_obj)

# Nonnegativity range: for 0 <= r <= 1/5, every affine mass above is >= 0.
for Q in (Q15, Q17):
    for a,b in Q.values():
        vals = [a, a + b*F(1,5)]
        assert min(vals) >= 0
print('PARAMETRIC_OPTIMAL_COUPLINGS_PASS')

# At r=0, first coordinate is deterministic and the following 4-variable
# coupling is a common minimizer of all stop-loss objectives.
W4 = (8, 4, 7, 6)
ST4 = list(product((0,1), repeat=4))
Q0 = {
    (0,1,1,1): F(1,5),
    (1,0,0,1): F(1,5),
    (1,0,1,0): F(1,10),
    (1,1,0,0): F(2,5),
    (1,1,0,1): F(1,10),
}
P4 = (F(4,5), F(7,10), F(3,10), F(1,2))
assert sum(Q0.values()) == 1
for i,p in enumerate(P4):
    assert sum(q*x[i] for x,q in Q0.items()) == p

# Only the nontrivial interior breakpoints need LP dual certificates.
DUALS4 = {
    13: (F(-11), F(7), F(4), F(6), F(5)),
    14: (F(-10), F(6), F(4), F(5), F(4)),
    15: (F(-7),  F(4), F(3), F(3), F(3)),
    17: (F(-3),  F(2), F(1), F(1), F(1)),
}
for t,y in DUALS4.items():
    for x in ST4:
        assert hinge(total(W4,x),t) >= affine(y,x), (t,x)
    primal = sum(q*hinge(total(W4,x),t) for x,q in Q0.items())
    dual = y[0] + sum(y[i+1]*P4[i] for i in range(4))
    assert primal == dual, (t,primal,dual)

spec = sorted({total(W4,x) for x in ST4})
assert spec == list(map(F, [0,4,6,7,8,10,11,12,13,14,15,17,18,19,21,25]))
assert min(total(W4,x) for x in Q0) == 12
assert max(total(W4,x) for x in Q0) == 18
print('R_ZERO_COMMON_STOPLOSS_CERTIFICATE_PASS')

# Weighted symmetric two-point theorem's finite structural core:
# complementing a binary vector reflects the weighted sum about W/2.
for w in [(1,2,4,7), (3,5,6), (2,2,9,10,11)]:
    W = sum(map(F,w))
    for x in product((0,1), repeat=len(w)):
        xb = tuple(1-z for z in x)
        assert total(w,x) + total(w,xb) == W
print('COMPLEMENT_SYMMETRY_IDENTITY_PASS')

print('ALL_EXACT_CHECKS_PASS')
