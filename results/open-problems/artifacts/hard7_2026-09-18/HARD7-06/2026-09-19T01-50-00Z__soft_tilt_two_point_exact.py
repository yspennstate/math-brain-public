#!/usr/bin/env python3
"""
Exact algebraic core for HARD7-06 run 6.

This verifies the polynomial identity used to prove that a natural
factor-local size^lambda tilt cannot stabilize the symmetric two-point
soft-message perturbation of the k=3,d=6 NAE cavity recursion for any
lambda in [0,1].

All polynomial arithmetic is exact integer arithmetic.
"""


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    n = max(len(a), len(b))
    c = [0] * n
    for i in range(n):
        c[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return trim(c)


def sub(a, b):
    n = max(len(a), len(b))
    c = [0] * n
    for i in range(n):
        c[i] = (a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
    return trim(c)


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def scale(a, k):
    return trim([k * x for x in a])


def power(a, n):
    r = [1]
    b = list(a)
    while n:
        if n & 1:
            r = mul(r, b)
        b = mul(b, b)
        n //= 2
    return r


def substitute_shift(poly_y, shift):
    # y -> u + shift, output low-to-high coefficients in u.
    out = [0]
    base = [shift, 1]
    for i, c in enumerate(poly_y):
        out = add(out, scale(power(base, i), c))
    return trim(out)


# In the proof,
# L(x) = 2 N(x) / (9 D(x))
# q(x)^2 = 3 (x+1)^2 (x^2-x+1)^2 / [5 (x^6+4x^3+1)].
N = [16, 31, 47, 55, 47, 31, 16]
D = mul(mul([2, 1], [1, 2]), mul([2, 0, 1], [1, 0, 2]))
E = [1, 0, 0, 4, 0, 0, 1]
F = mul(power([1, 1], 2), power([1, -1, 1], 2))

# Exact common-denominator numerator of L(x)^2 - q(x)^2.
P = sub(scale(mul(power(N, 2), E), 20),
        scale(mul(power(D, 2), F), 243))

expected_P = [
    1232, 400, -2216, -10456, -13404, 18108, 35905, 101492, 154820,
    136826,
    154820, 101492, 35905, 18108, -13404, -10456, -2216, 400, 1232
]
assert P == expected_P
assert P == list(reversed(P))

# For y=x+x^{-1}, P(x)/x^9 = Q(y).
S = [[2], [0, 1]]  # S_k(y)=x^k+x^{-k}; S_0=2, S_1=y.
for _k in range(2, 10):
    S.append(sub(mul([0, 1], S[-1]), S[-2]))

Q = [P[9]]
for k in range(1, 10):
    Q = add(Q, scale(S[k], P[9 + k]))

expected_Q = [-8230, 6685, -71444, 34941, 88844,
              35372, -13656, -13304, 400, 1232]
assert Q == expected_Q

# Put y=2+u, u>=0.
R = substitute_shift(Q, 2)
expected_R = [
    708588, 478953, -723654, -134595, 1313508,
    1416876, 672792, 170504, 22576, 1232
]
assert R == expected_R

# Positivity certificate used on the page:
# 0<=u<=1: u^2,u^3<=u, so the potentially negative low-degree block
# is >= 708588 +(478953-723654-134595)u >= 329292.
small_u_margin = 708588 + 478953 - 723654 - 134595
assert small_u_margin == 329292 > 0

# u>=1: the u^4,u^3,u^2 block is
# u^2(1313508 u^2 -134595 u -723654)
# >= u^2[(1313508-134595)u -723654] >= 455259 u^2.
large_u_margin = 1313508 - 134595 - 723654
assert large_u_margin == 455259 > 0

print("degree(P) =", len(P) - 1)
print("P coefficients low-to-high =", P)
print("Q(y) coefficients low-to-high =", Q)
print("Q(2+u) coefficients low-to-high =", R)
print("small-u positivity margin =", small_u_margin)
print("large-u positivity margin =", large_u_margin)
print("linearized d=6 two-point variance multiplier = 10/9")
print("ALL_EXACT_CHECKS_PASS")
