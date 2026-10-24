#!/usr/bin/env python3
"""Exact rational checks for agent 038's nonautonomous QSO report.

No numerical sample is used to prove the universal contraction statements.
These assertions check the scalar cap constants and the explicit coefficient
examples, and isolate the attracting period-two orbit in that example.
Uses only the Python standard library.
"""

from copy import deepcopy
from fractions import Fraction as F


N = 4
ONE = F(1)
ZERO = F(0)
Q = F(2, 5)


def uniform_array():
    return {
        (i, j): tuple(ZERO if k in (i, j) else F(1, N - len({i, j}))
                      for k in range(N))
        for i in range(N) for j in range(N)
    }


def deterministic_row(k):
    return tuple(ONE if r == k else ZERO for r in range(N))


def set_row(P, i, j, values):
    P[i, j] = P[j, i] = tuple(values)


def valid(P):
    for i in range(N):
        for j in range(N):
            assert P[i, j] == P[j, i]
            assert sum(P[i, j]) == ONE
            assert all(v >= 0 for v in P[i, j])
            assert P[i, j][i] == P[i, j][j] == ZERO


def V(P, x):
    return tuple(sum(P[i, j][k] * x[i] * x[j]
                     for i in range(N) for j in range(N))
                 for k in range(N))


def T(P, x):
    v = V(P, x)
    return tuple(F(3, 5) * a + F(2, 5) * b for a, b in zip(x, v))


def metric(P, R):
    return max(sum(abs(a - b) for a, b in zip(P[i, j], R[i, j]))
               for i in range(N) for j in range(N))


def scalar_envelope(s):
    return F(2, 5) - s / 5 + F(2, 5) * s * s


def lifted(s):
    return (s,) + ((ONE - s) / 3,) * 3


P_A = uniform_array()
P_B = deepcopy(P_A)
for i in range(1, N):
    for j in range(1, N):
        set_row(P_B, i, j, deterministic_row(0))
P_C = deepcopy(P_A)
set_row(P_C, 0, 0, (ZERO, ZERO, F(2, 3), F(1, 3)))
set_row(P_C, 1, 1, (F(2, 3), ZERO, ZERO, F(1, 3)))
set_row(P_C, 2, 2, (ZERO, F(2, 3), ZERO, F(1, 3)))

for P in (P_A, P_B, P_C):
    valid(P)
u = (F(1, 4),) * N
assert V(P_A, u) == u == V(P_C, u)
assert metric(P_A, P_B) == F(4, 3)
assert metric(P_A, P_C) == F(2, 3)

assert scalar_envelope(ONE) == F(3, 5)
assert scalar_envelope(F(3, 5)) == F(53, 125)
assert scalar_envelope(F(53, 125)) == F(30243, 78125) < Q
assert scalar_envelope(ZERO) == Q
assert scalar_envelope(Q) == F(48, 125) < Q

P_D = deepcopy(P_A)
set_row(P_D, 0, 0, deterministic_row(1))
set_row(P_D, 1, 1, deterministic_row(0))
set_row(P_D, 0, 1, deterministic_row(2))
valid(P_D)
x0 = (ONE, ZERO, ZERO, ZERO)
x1 = T(P_D, x0)
x2 = T(P_D, x1)
assert x1 == (F(3, 5), F(2, 5), ZERO, ZERO)
assert x2 == (F(53, 125), F(48, 125), F(24, 125), ZERO)
assert x2[0] > Q
P_E = uniform_array()
for i in range(3):
    for j in range(3):
        set_row(P_E, i, j, deterministic_row(3))
valid(P_E)
x3 = T(P_E, x2)
assert max(x3) == x3[3] == Q

# Equality of the scalar descriptions is checked as a polynomial identity.
# Three rational input values suffice for a polynomial of degree at most two.
for s in (ZERO, F(1, 3), ONE):
    assert V(P_A, lifted(s))[0] == F(4, 9) * (ONE - s) ** 2
    assert V(P_B, lifted(s))[0] == (ONE - s) ** 2


def t_a(s):
    return F(3, 5) * s + F(8, 45) * (ONE - s) ** 2


def t_b(s):
    return scalar_envelope(s)


def h(s):
    return t_b(t_a(s)) - s


# The report proves uniqueness by common-cap contraction. Here signs and
# monotonicity of t_a on [1/4, 2/5] give an exact interval for both phases.
lo, hi = F(1, 4), Q
assert h(lo) > 0 > h(hi)
for _ in range(32):
    mid = (lo + hi) / 2
    if h(mid) > 0:
        lo = mid
    else:
        hi = mid
assert h(lo) > 0 > h(hi)
b_lo, b_hi = t_a(lo), t_a(hi)
assert b_hi < lo
assert F("0.37580092219") < lo < hi < F("0.37580092224")
assert F("0.29474712909") < b_lo < b_hi < F("0.29474712911")

print("All exact rational assertions passed.")
print("Cap envelope: 1 -> 3/5 -> 53/125 -> 2/5.")
print("Last nonzero endpoint:", scalar_envelope(F(53, 125)))
print("Two-step counterexample state:", x2)
print("Three-step cap attained:", x3)
print("Coefficient metric eta(A,B) =", metric(P_A, P_B))
print("Coefficient metric eta(A,C) =", metric(P_A, P_C))
print("Period-two first-coordinate phase-0 interval:", lo, hi)
print("Period-two first-coordinate phase-1 interval:", b_lo, b_hi)
print("Decimal displays (not separate certificates):")
print("phase 0:", float(lo), float(hi))
print("phase 1:", float(b_lo), float(b_hi))
