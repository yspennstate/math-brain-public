#!/usr/bin/env python3
"""
R13 exact finite-core checker for the five-column Boolean Komlos bound B(5) <= 2.

Finite claims checked:
1. There are 7581 order ideals of the Boolean lattice B_5.
2. Every order ideal F satisfies the structural classifications used in the proof:
   - |F|>=3 => at least two singletons.
   - |F|>=5 => either at least four singletons, or at least three singletons
     and at least one pair.
   - |F|>=7 => one of:
       five singletons + at least one pair,
       exactly four singletons + at least two pairs,
       exactly three singletons + at least three pairs.
3. Exact algebra in the four-singleton energy inequality.
4. The double-counting margin 3*5 < 16.
5. The parameter-barrier obstruction below threshold 2:
   for every rational t<2, the two-coordinate family a=(c,c,0,0,0) with
   t/2<c<=1 has 8 bad antipodal sign classes; as c down to t/2,
   b/||a||^2 tends to 16/t^2 > 4 > 16/5.

No floating-point acceptance criterion is used.
"""
from fractions import Fraction
import itertools


def ideals_bool(n):
    # Ideals as frozensets of bitmasks. For n=0 the lattice has one element 0.
    if n == 0:
        return [frozenset(), frozenset({0})]
    prev = ideals_bool(n-1)
    high = 1 << (n-1)
    out = []
    for I0 in prev:
        for I1 in prev:
            if I1.issubset(I0):
                F = set(I0)
                F.update({s | high for s in I1})
                out.append(frozenset(F))
    return out


def singleton_count(F, n=5):
    return sum((1 << i) in F for i in range(n))


def pair_count(F, n=5):
    return sum(((1 << i) | (1 << j)) in F
               for i in range(n) for j in range(i+1, n))


ideals = ideals_bool(5)
assert len(ideals) == 7581
assert len(set(ideals)) == 7581

for F in ideals:
    b = len(F)
    r = singleton_count(F)
    p = pair_count(F)

    if b >= 3:
        assert r >= 2

    if b >= 5:
        assert (r >= 4) or (r >= 3 and p >= 1)

    if b >= 7:
        assert ((r == 5 and p >= 1)
                or (r == 4 and p >= 2)
                or (r == 3 and p >= 3))

# Exact algebra for the four-singleton case.
# Put a1=1-u and lower-bound a2 by (1+u)/2.
# Then:
# (1-u)^2 + a2^2 + (a2+1+u)^2/3
# at a2=(1+u)/2 equals 2+2u^2.
# Verify coefficientwise with rational polynomial arithmetic.
# Represent polynomial c0+c1*u+c2*u^2.
def add(p, q):
    return tuple(p[i] + q[i] for i in range(3))


def mul(p, q):
    out = [Fraction(0) for _ in range(5)]
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return tuple(out[:3])


one_minus_u = (Fraction(1), Fraction(-1), Fraction(0))
one_plus_u = (Fraction(1), Fraction(1), Fraction(0))
half_one_plus_u = tuple(c/Fraction(2) for c in one_plus_u)
threehalf_one_plus_u = tuple(c*Fraction(3, 2) for c in one_plus_u)

lhs = (Fraction(0), Fraction(0), Fraction(0))
lhs = add(lhs, mul(one_minus_u, one_minus_u))
lhs = add(lhs, mul(half_one_plus_u, half_one_plus_u))
term = mul(threehalf_one_plus_u, threehalf_one_plus_u)
lhs = add(lhs, tuple(c/Fraction(3) for c in term))
rhs = (Fraction(2), Fraction(0), Fraction(2))
assert lhs == rhs

# Exact incidence margin: total bad incidences I < 3*5 = 15 < 16 classes.
assert 3*5 < 16

# Parameter barrier below 2: for rational t<2 choose c=(t/2+1)/2,
# which lies strictly between t/2 and 1. Then a=(c,c,0,0,0) has exactly
# eight bad antipodal classes. Verify for several exact rational t values.
def bad_classes_two_coordinate(t):
    c = (t/Fraction(2) + Fraction(1))/Fraction(2)
    assert t/Fraction(2) < c <= 1
    # 16 antipodal classes represented by first coordinate +1.
    b = 0
    for tail in itertools.product((-1, 1), repeat=4):
        eps = (1,) + tail
        s = c*eps[0] + c*eps[1]
        if abs(s) > t:
            b += 1
    return b, c


for t in [Fraction(1), Fraction(3, 2), Fraction(19, 10), Fraction(199, 100)]:
    b, c = bad_classes_two_coordinate(t)
    assert b == 8
    # Limiting energy-only charge is 16/t^2, strictly >4>16/5.
    assert Fraction(16, 1)/(t*t) > 4
    assert Fraction(4, 1) > Fraction(16, 5)

print("R13 B(5)<=2 exact finite-core checker")
print("boolean_ideals_B5=", len(ideals))
print("ideal_classifications=PASS")
print("four_singleton_energy_identity=2+2u^2 PASS")
print("bad_incidence_margin: 3*5=15 < 16 PASS")
print("subthreshold_two_coordinate_barrier=PASS")
print("ALL_EXACT_CHECKS_PASS")
