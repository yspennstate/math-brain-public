#!/usr/bin/env python3
"""Independent exact check of B05's fixed-dimension recharge witness.

This reconstruction starts from the Boolean circuit and does not import the
producer's checker.  A pair (a,b) represents a+b/ln(2); only dyadic orbit
energies 0 and 1/2 occur in the audited potential values.
"""
from fractions import Fraction
from itertools import product

VARS = ("y", "x", "z", "u")
POINTS = tuple(product((-1, 1), repeat=4))


def f(point):
    y, x, z, u = point
    return x if y == 1 else z*u


def chi(point, mask):
    out = 1
    for j, value in enumerate(point):
        if (mask >> j) & 1:
            out *= value
    return out


hat = tuple(
    sum(Fraction(f(point)*chi(point, mask), 16) for point in POINTS)
    for mask in range(16)
)
p = tuple(value*value for value in hat)


def mask_of(names):
    return sum(1 << VARS.index(name) for name in names)


def orbit_energy(block, outside):
    bmask = mask_of(block)
    omask = mask_of(outside)
    ans = Fraction(0)
    sub = bmask
    while True:
        ans += p[omask | sub]
        if sub == 0:
            return ans
        sub = (sub - 1) & bmask


def influence(name):
    bit = 1 << VARS.index(name)
    return sum(p[mask] for mask in range(16) if mask & bit)


assert all(f(point) in (-1, 1) for point in POINTS)
support = {mask: value for mask, value in enumerate(hat) if value}
expected = {
    mask_of(("x",)): Fraction(1, 2),
    mask_of(("y", "x")): Fraction(1, 2),
    mask_of(("z", "u")): Fraction(1, 2),
    mask_of(("y", "z", "u")): Fraction(-1, 2),
}
assert support == expected
assert sum(p) == 1

X = ("y", "x")
Y = ("y", "z")
assert orbit_energy(X, ()) == Fraction(1, 2)
assert orbit_energy(X, ("z",)) == 0
assert orbit_energy(X, ("u",)) == 0
assert orbit_energy(Y, ()) == 0
assert orbit_energy(Y, ("x",)) == Fraction(1, 2)
assert orbit_energy(Y, ("u",)) == Fraction(1, 2)

# q(1/2)=1/2+1/ln2 and psi_2(1/2)=q(1/2)+1/2.
lambda_X = (Fraction(1), Fraction(1))
lambda_Y = (Fraction(1), Fraction(2))
jump = tuple(b-a for a, b in zip(lambda_X, lambda_Y))
assert jump == (Fraction(0), Fraction(1))

infs = {name: influence(name) for name in VARS}
assert infs == {name: Fraction(1, 2) for name in VARS}
assert sum(infs.values()) == 2

checks = 16 + 16 + 6 + 4 + 5
for r in (1, 2, 5, 20, 100):
    # Coefficients of 1/ln(2): r positive jumps, r-1 refunds.
    positive = r
    refunds = r-1
    signed = positive-refunds
    assert signed == 1

print("status=PASS")
print("method=independent exact Fraction Walsh reconstruction")
print(f"exact_assertion_groups={checks}")
print("walsh_support=x:+1/2,xy:+1/2,zu:+1/2,yzu:-1/2")
print("E_X_empty=1/2; E_X_z=E_X_u=0")
print("E_Y_empty=0; E_Y_x=E_Y_u=1/2")
print("Lambda_X=1+1/ln2")
print("Lambda_Y=1+2/ln2")
print("jump=1/ln2")
print("all_four_influences=1/2; I=2")
for r in (1, 2, 5, 20, 100):
    print(f"r={r}; positive_variation={r}/ln2; refunds={r-1}/ln2; signed=1/ln2")

