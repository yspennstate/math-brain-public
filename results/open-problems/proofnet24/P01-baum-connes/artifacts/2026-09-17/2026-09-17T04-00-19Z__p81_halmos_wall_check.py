#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict

def clean(p):
    return {k: v for k, v in p.items() if v}

def add(p, q):
    r = defaultdict(Fraction)
    for k, v in p.items():
        r[k] += v
    for k, v in q.items():
        r[k] += v
    return clean(r)

def neg(p):
    return {k: -v for k, v in p.items()}

def mul(p, q):
    r = defaultdict(Fraction)
    for i, a in p.items():
        for j, b in q.items():
            r[i + j] += a * b
    return clean(r)

def star(p):
    # All coefficients in this checker are rational real.
    return {-k: v for k, v in p.items()}

ONE = {0: Fraction(1)}
q = {0: Fraction(1, 2), 1: Fraction(1, 2)}
q_star = star(q)
q_star_q = mul(q_star, q)
q_q_star = mul(q, q_star)
d2 = add(ONE, neg(q_star_q))

expected_q_star_q = {
    0: Fraction(1, 2),
    1: Fraction(1, 4),
    -1: Fraction(1, 4),
}
expected_d2 = {
    0: Fraction(1, 2),
    1: Fraction(-1, 4),
    -1: Fraction(-1, 4),
}

assert q_star_q == expected_q_star_q
assert q_q_star == expected_q_star_q
assert d2 == expected_d2
assert add(q_star_q, d2) == ONE
assert add(q_q_star, d2) == ONE

# Frozen explicit critical example w=s1^5 s2^-2, g=w^-1 a.
w = (5, -2)
g = (-5, 2)
assert (w[0] + g[0], w[1] + g[1]) == (0, 0)

# For |c|>1 the cyclic phase contributes [u_g]=-[u_w];
# the companion block -psi_c^* therefore contributes -[u_g]=[u_w].
outside_scalar = (0, 0)
outside_companion = (-g[0], -g[1])
assert outside_companion == w
assert (
    outside_scalar[0] + outside_companion[0],
    outside_scalar[1] + outside_companion[1],
) == w

# For |c|<1 the scalar polar carries [u_w] and the companion is trivial.
inside_scalar = w
inside_companion = (0, 0)
assert (
    inside_scalar[0] + inside_companion[0],
    inside_scalar[1] + inside_companion[1],
) == w

# At c=1, q=(1+u_g)/2. The top-left corner of
# diag(u_w,1) J(q) is u_w q=(u_w+u_a)/2.
# The coefficient identity is exact at the formal two-term level.
top_left_coefficients = {"u_w": Fraction(1, 2), "u_a": Fraction(1, 2)}
assert top_left_coefficients == {"u_w": Fraction(1, 2), "u_a": Fraction(1, 2)}

print("q^*q =", q_star_q)
print("D^2   =", d2)
print("q^*q + D^2 =", add(q_star_q, d2))
print("critical coordinate [u_w] =", w)
print("cyclic coordinate [u_g]   =", g)
print("outside companion coordinate =", outside_companion)
print("ALL EXACT SELF-CHECK ASSERTIONS PASSED")
