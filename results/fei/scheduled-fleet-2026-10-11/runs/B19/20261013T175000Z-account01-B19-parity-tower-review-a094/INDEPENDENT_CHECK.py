#!/usr/bin/env python3
"""Independent reconstruction of the B05 parity-balanced tower formulas."""

from math import log2
import itertools
import random


def spectrum(values):
    """Walsh spectrum by recursive even/odd splitting (normalized)."""
    coeff = [float(x) for x in values]
    width = 1
    while width < len(coeff):
        nxt = coeff[:]
        for start in range(0, len(coeff), 2 * width):
            for j in range(width):
                a = coeff[start + j]
                b = coeff[start + width + j]
                nxt[start + j] = (a + b) / 2.0
                nxt[start + width + j] = (a - b) / 2.0
        coeff = nxt
        width *= 2
    return coeff


def upper_u(values):
    coeff = spectrum(values)
    p = [x * x for x in coeff]
    cap = p[:]
    n = len(values).bit_length() - 1
    for bit in range(n):
        for mask in range(1 << n):
            if not (mask >> bit) & 1:
                cap[mask] += cap[mask | (1 << bit)]
    return sum(x * log2(cap[s] / x) for s, x in enumerate(p) if x)


def influence(values):
    n = len(values).bit_length() - 1
    N = len(values)
    return sum(
        sum(values[x] != values[x ^ (1 << bit)] for x in range(N)) / N
        for bit in range(n)
    )


def balance(values):
    return list(values) + [-x for x in values]


def half_activate(values):
    return [1] * len(values) + list(values)


def tower(base, depth):
    q = balance(base)
    for level in range(depth):
        f = half_activate(q)
        if level + 1 < depth:
            q = balance(f)
    return f


def restrict(values, bit, value):
    return [
        values[x]
        for x in range(len(values))
        if ((x >> bit) & 1) == value
    ]


def tensor(f, h):
    return [a * b for b in h for a in f]


rng = random.Random(190942)
bases = []
for n in range(4):
    N = 1 << n
    for truth in itertools.product((-1, 1), repeat=N):
        bases.append(list(truth))

formula_checks = 0
coordinate_restriction_checks = 0
tensor_checks = 0
max_error = 0.0

for base in bases:
    U0 = upper_u(base)
    I0 = influence(base)
    for depth in range(1, 5):
        f = tower(base, depth)
        U = upper_u(f)
        I = influence(f)
        expected_u = 2.0 + (U0 - 2.0) / (1 << depth)
        expected_i = 2.0 + (I0 - 2.0) / (1 << depth)
        max_error = max(max_error, abs(U - expected_u), abs(I - expected_i))
        assert abs(U - expected_u) < 2e-12
        assert abs(I - expected_i) < 2e-12
        assert len(f).bit_length() - 1 == (len(base).bit_length() - 1) + 2 * depth
        if U0 <= 2.0 * I0 + 1e-12:
            assert U <= 2.0 * I + 2e-12
        formula_checks += 1

for base in bases[::19]:
    f = tower(base, 2)
    U = upper_u(f)
    I = influence(f)
    for bit in range(len(f).bit_length() - 1):
        for value in (0, 1):
            child_u = upper_u(restrict(f, bit, value))
            assert child_u >= -1e-14
            assert U - child_u <= U + 1e-14
            if upper_u(base) <= 2 * influence(base) + 1e-12:
                assert U - child_u <= 2 * I + 2e-12
            coordinate_restriction_checks += 1

for base in bases[::31]:
    f = tower(base, 3)
    h = [1, 1, 1, -1]
    assert abs(upper_u(tensor(f, h)) - upper_u(f) - upper_u(h)) < 2e-12
    tensor_checks += 1

# Exact scope falsifier: the family of positive-depth towers is not closed
# under arbitrary physical restrictions.  For P=1 and d=1, restricting the
# balancing character to -1 leaves a dictator, whose U is zero.  Every
# positive-depth tower has U=2+2^-d(U(P)-2)>=1.
t = tower([1], 1)
dictator = restrict(t, 0, 1)
assert dictator == [1, -1]
assert abs(upper_u(dictator)) < 1e-15
assert min(2.0 + (0.0 - 2.0) / (1 << d) for d in range(1, 20)) >= 1.0

print("B19 independent parity-tower audit")
print(f"boolean_bases={len(bases)}")
print(f"formula_checks={formula_checks}")
print(f"coordinate_restriction_checks={coordinate_restriction_checks}")
print(f"tensor_checks={tensor_checks}")
print(f"max_formula_error={max_error:.3e}")
print("restriction_closure_falsifier=P=1,d=1,w=-1 -> dictator,U=0")
print("PASS_ACCEPT_IDENTITIES_CORRECT_SCOPE_INTERPRETATION")
